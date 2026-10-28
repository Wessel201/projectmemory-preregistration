"""Plan 23 amendment 1, Step 0: the evaluated prompt texts, as the runs sent them.

Reads the trace.json of every evaluated EL2020 cycle-2 run (A0, A1, A2; the RAG
runs keep no trace) and extracts, per seam and arm, the distinct static prompt
texts the system actually sent: every system message, and every user message
reduced to its template. Each variant is hashed (SHA-256 of its UTF-8 text) and
counted. It also records how much of the registry each prompt carried. Reads
nothing but the trace files; makes no network or model call.

Split rule (static versus dynamic). Each seam has one pattern per message role,
with a named group for every dynamic field. The static text of a message is the
message with each matched group replaced by the placeholder ⟦name⟧. A message
with no dynamic field is static as a whole. A message its pattern does not match
is kept whole and counted as an unparsed variant, so a template change shows up
as an extra variant instead of being hidden. Dynamic fields are the span or
question text, the registry lines, the claim fields, the drafted answer, the
citations, the facts and the flags. The registry-line format itself is fixed by
the prompt builder and is described in the register, not hashed here.

Usage: .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-prompts.py
Writes 23-am1-prompts-evaluated.md next to this script.
"""

import collections
import hashlib
import json
import pathlib
import re
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).with_name("23-am1-prompts-evaluated.md")
BATCH = "data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z"
SMOKE = "data/ami_eval/a1_smoke/el2020_a1_20261022T211107Z"
A2RAG = "data/ami_eval/a1_smoke/el2020_a2_rag_20261023T061545Z"
RUNS = [
    ("A0", "a0_r1", f"{BATCH}/a0_r1"),
    ("A0", "a0_r2", f"{BATCH}/a0_r2"),
    ("A0", "a0_r3", f"{BATCH}/a0_r3"),
    ("A1", "a1_r1", SMOKE),
    ("A1", "a1_r2", f"{BATCH}/a1_r2"),
    ("A1", "a1_r3", f"{BATCH}/a1_r3"),
    ("A2", "a2_r1", f"{A2RAG}/a2_r1"),
    ("A2", "a2_r2b", f"{A2RAG}/a2_r2b"),
    ("A2", "a2_r3", f"{A2RAG}/a2_r3"),
]
ARMS = ("A0", "A1", "A2")

EXTRACTION_MARK = "\n\nRegistry of state keys (the domain definition):\n"
EMPTY_REGISTRY = "(no registry keys provided — use state_key_hint: null)"
S = re.S
#: seam -> role -> pattern with one named group per dynamic field (None: all static).
PATTERNS = {
    "memory_gatekeeper": {
        "system": None,
        "user": re.compile(r"\AClassify this span:\n\n(?P<span>.*)\Z", S),
    },
    "extraction": {
        "system": re.compile(r"\A.*?" + re.escape(EXTRACTION_MARK) + r"(?P<registry>.*)\Z", S),
        "user": re.compile(r"\AExtract project-state claims from:\n\n(?P<span>.*)\Z", S),
    },
    "state_key_resolution": {
        "system": None,
        "user": re.compile(
            r"\AResolve this text to registry keys\.\n\nText: (?P<text>.*?)\n"
            r"Detected intent hint: (?P<intent>[a-z_]+)\n\nRegistry:\n(?P<registry>.*)\Z", S),
    },
    "question_answering_grounding": {
        "system": None,
        "user": re.compile(
            r"\AQuestion: (?P<question>.*?)\n\nDraft answer:\n(?P<draft>.*?)\n\n"
            r"Available citations:\n(?P<citations>.*?)\n\nCurrent facts:\n(?P<facts>.*?)\n\n"
            r"review_state_present: (?P<review_state_present>True|False)\Z", S),
    },
    "claim_support_check": {
        "system": None,
        "user": re.compile(
            r"\ASpan:\n(?P<span>.*)\n\nKey: (?P<label>.*?)\nClaim value: (?P<value>.*?)\n"
            r"Commitment status: (?P<status>[^\n]*)\Z", S),
    },
}
#: Dynamic fields drawn from a fixed vocabulary; their values are tallied.
VOCAB_FIELDS = {
    ("state_key_resolution", "intent"),
    ("question_answering_grounding", "review_state_present"),
    ("claim_support_check", "status"),
}
#: Registry lines as each builder writes them (key name only).
EXTRACTION_KEY = re.compile(r"(?m)^  - ([a-z0-9_.]+) \[")
RESOLVER_KEY = re.compile(r"(?m)^  - ([a-z0-9_.]+): ")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split(seam: str, role: str, text: str):
    """(static template, dynamic fields, parsed) for one message."""
    pattern = PATTERNS[seam][role]
    if pattern is None:
        return text, {}, True
    m = pattern.match(text)
    if m is None:
        return text, {}, False
    out, last = [], 0
    for name in sorted(m.groupdict(), key=lambda n: m.start(n)):
        out += [text[last : m.start(name)], f"⟦{name}⟧"]
        last = m.end(name)
    out.append(text[last:])
    return "".join(out), m.groupdict(), True


def meeting_of(steps):
    """Each step's meeting: the meeting of the next checkpoint question."""
    out, cur = [None] * len(steps), None
    for i in range(len(steps) - 1, -1, -1):
        s = steps[i]
        if s["seam"] == "ami_eval_question":
            m = re.match(r"([A-Za-z]+\d+[a-z])_", s["input"]["question_id"])
            cur = m.group(1) if m else "?"
        out[i] = cur
    return out


def stats(values):
    if not values:
        return "–"
    return f"{min(values)} / {statistics.median(values):g} / {max(values)}"


def fence(text: str) -> str:
    longest = max((len(r) for r in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def main():
    variants = {}  # hash -> {"seam", "role", "text", "calls": Counter[arm], "parsed"}
    calls = collections.defaultdict(collections.Counter)  # (seam, arm) -> Counter[run]
    per_run_variant = collections.defaultdict(set)  # (seam, role, run) -> {hash}
    path_calls = collections.Counter()  # (arm, path, hash) for the resolver user template
    schemas = collections.defaultdict(collections.Counter)  # (seam, arm) -> response_schema
    served = collections.defaultdict(collections.Counter)  # (seam, arm) -> (model, served_model)
    vocab = collections.defaultdict(collections.Counter)  # (seam, field, arm) -> value
    other = collections.defaultdict(collections.Counter)  # (seam, arm) -> mode
    expansion = collections.defaultdict(collections.Counter)  # arm -> (method, served_model)
    registry_rows, sources = [], []

    for arm, run, folder in RUNS:
        found = sorted((ROOT / folder / "artifacts").glob("*.trace.json"))
        if len(found) != 1:
            raise SystemExit(f"{run}: expected one trace.json in {folder}/artifacts, found {len(found)}")
        raw = found[0].read_bytes()
        sources.append((arm, run, found[0].relative_to(ROOT), hashlib.sha256(raw).hexdigest()))
        trace = json.loads(raw)
        steps = trace["steps"]
        meeting = meeting_of(steps)
        questions = {s["input"]["question"] for s in steps if s["seam"] == "ami_eval_question"}
        per_meeting = collections.defaultdict(lambda: collections.defaultdict(list))
        seen_spans = set()

        for i, step in enumerate(steps):
            seam, inp = step["seam"], step["input"]
            if isinstance(inp, str) and "messages" in inp:
                raise SystemExit(f"{run}: step {step['i']} records its messages as a string; no split rule for that")
            messages = inp.get("messages") if isinstance(inp, dict) else None
            if not messages:
                other[(seam, arm)][step["mode"] or "none"] += 1
                if seam == "registry_expansion_generation":
                    metrics = step.get("metrics") or {}
                    expansion[arm][(metrics.get("generation_method"), step.get("served_model"))] += 1
                continue
            if seam not in PATTERNS:
                raise SystemExit(f"{run}: no split rule for seam {seam!r}")
            roles = [m["role"] for m in messages]
            if roles != ["system", "user"]:
                raise SystemExit(f"{run}: {seam} step {step['i']} has roles {roles}")
            calls[(seam, arm)][run] += 1
            schemas[(seam, arm)][inp.get("response_schema")] += 1
            served[(seam, arm)][(step.get("model"), step.get("served_model"))] += 1
            fields = {}
            for message in messages:
                role = message["role"]
                static, dyn, parsed = split(seam, role, message["content"])
                fields.update(dyn)
                h = sha(static)
                v = variants.setdefault(h, {"seam": seam, "role": role, "text": static,
                                            "calls": collections.Counter(), "parsed": parsed})
                v["calls"][arm] += 1
                per_run_variant[(seam, role, run)].add(h)
                if seam == "state_key_resolution" and role == "user":
                    path = "read" if dyn.get("text") in questions else "write"
                    path_calls[(arm, path, h)] += 1
            for s_, f_ in VOCAB_FIELDS:
                if s_ == seam and f_ in fields:
                    vocab[(seam, f_, arm)][fields[f_]] += 1

            m = meeting[i]
            if seam == "extraction":
                reg = fields.get("registry", "")
                keys = frozenset(EXTRACTION_KEY.findall(reg))
                row = per_meeting[m]
                row["ex_keysets"].append(keys)
                row["ex_chars"].append(len(messages[0]["content"]))
                row["ex_empty"].append(reg.strip() == EMPTY_REGISTRY)
                row["ex_repeat"].append(fields.get("span") in seen_spans)
                seen_spans.add(fields.get("span"))
            elif seam == "state_key_resolution":
                keys = frozenset(RESOLVER_KEY.findall(fields.get("registry", "")))
                path = "read" if fields.get("text") in questions else "write"
                per_meeting[m][f"res_{path}"].append(keys)

        order = sorted(per_meeting, key=lambda x: (x is None, x))
        ex_registry = {m: (per_meeting[m]["ex_keysets"] or [None])[0] for m in order}
        for n, m in enumerate(order):
            row = per_meeting[m]
            ks = row["ex_keysets"]
            full_write = ex_registry.get(m)
            nxt = order[n + 1] if n + 1 < len(order) else None
            full_read = ex_registry.get(nxt) if nxt else None
            w, r = row["res_write"], row["res_read"]
            registry_rows.append({
                "arm": arm, "run": run, "meeting": m,
                "ex_calls": len(ks),
                "ex_keysets": len(set(ks)),
                "ex_keys": sorted({len(k) for k in ks}),
                "ex_chars": sorted(set(row["ex_chars"])),
                "ex_empty": sum(row["ex_empty"]),
                "ex_repeat": sum(row["ex_repeat"]),
                "w_calls": len(w),
                "w_keys": stats([len(k) for k in w]),
                "w_zero": sum(1 for k in w if not k),
                "w_full": (sum(1 for k in w if k == full_write) if full_write is not None else "n/a"),
                "r_calls": len(r),
                "r_keys": stats([len(k) for k in r]),
                "r_full": (sum(1 for k in r if k == full_read) if full_read is not None else "n/a"),
            })

    # ------------------------------------------------------------------ report
    out = [
        "# Evaluated prompt texts, as sent (plan 23 amendment 1, Step 0)",
        "",
        "Generated by `23-am1-prompts.py` from the trace.json of each evaluated EL2020 cycle-2 run. "
        "Nothing here is edited by hand. A0 and A1 ran at 3320375, A2 at b4d6b6c (same code). "
        "The RAG runs keep no trace.json, so their prompt is not covered here.",
        "",
        "**Split rule.** Each seam has one pattern per message role, with a named group for each dynamic field. "
        "The static text of a message is the message with each dynamic field replaced by `⟦name⟧`. "
        "A message with no dynamic field is static as a whole. A message its pattern does not match is kept "
        "whole and reported as an unparsed variant. The hash is the SHA-256 of the static text in UTF-8.",
        "",
        "**Dynamic fields per seam:**",
    ]
    for seam, roles in PATTERNS.items():
        parts = []
        for role, pattern in roles.items():
            names = list(pattern.groupindex) if pattern is not None else []
            parts.append(f"{role}: {', '.join(names) if names else 'none (static as a whole)'}")
        out.append(f"- `{seam}`: " + "; ".join(parts) + ".")
    out += ["", "## Sources", "", "| Arm | Run | Trace file | SHA-256 |", "|---|---|---|---|"]
    out += [f"| {a} | {r} | `{p}` | `{h}` |" for a, r, p, h in sources]

    out += [
        "",
        "## Static variants per seam and arm",
        "",
        "Calls are LLM calls whose messages the trace records. *Variants* is the number of distinct static "
        "texts of that role in the arm; *per run* is the largest number seen in any one run of the arm.",
        "",
        "| Seam | Role | Arm | Calls | Variants | Per run | Hash (first 12) | Unparsed |",
        "|---|---|---|---:|---:|---:|---|---:|",
    ]
    for seam in PATTERNS:
        for role in ("system", "user"):
            for arm in ARMS:
                hs = [h for h, v in variants.items() if v["seam"] == seam and v["role"] == role and v["calls"][arm]]
                if not hs:
                    continue
                n = sum(variants[h]["calls"][arm] for h in hs)
                per_run = max(len(per_run_variant[(seam, role, r)]) for a, r, _ in RUNS if a == arm)
                unparsed = sum(variants[h]["calls"][arm] for h in hs if not variants[h]["parsed"])
                out.append(f"| `{seam}` | {role} | {arm} | {n} | {len(hs)} | {per_run} | "
                           + ", ".join(f"`{h[:12]}`" for h in sorted(hs)) + f" | {unparsed} |")
    out += ["", "**Calls per run:**", "", "| Seam | " + " | ".join(r for _, r, _ in RUNS) + " |",
            "|---|" + "---:|" * len(RUNS)]
    for seam in PATTERNS:
        if not any(calls[(seam, a)] for a in ARMS):
            continue
        out.append(f"| `{seam}` | " + " | ".join(str(calls[(seam, a)][r]) for a, r, _ in RUNS) + " |")

    out += ["", "**Response schema named in each call, and model requested / served:**", "",
            "| Seam | Arm | Response schema | Requested model → served snapshot (calls) |", "|---|---|---|---|"]
    for seam in PATTERNS:
        for arm in ARMS:
            if not schemas[(seam, arm)]:
                continue
            sch = ", ".join(f"`{k}` ({v})" for k, v in sorted(schemas[(seam, arm)].items()))
            mod = ", ".join(f"{a} → {b} ({v})" for (a, b), v in sorted(served[(seam, arm)].items(), key=str))
            out.append(f"| `{seam}` | {arm} | {sch} | {mod} |")

    out += ["", "**State-key resolution, user template by path.** A call is on the read path when its text "
            "is one of the run's checkpoint questions, and on the write path otherwise.", "",
            "| Arm | Path | Hash (first 12) | Calls |", "|---|---|---|---:|"]
    for (arm, path, h), n in sorted(path_calls.items()):
        out.append(f"| {arm} | {path} | `{h[:12]}` | {n} |")

    out += ["", "**Dynamic fields with a fixed vocabulary (values as sent):**", "",
            "| Seam | Field | Arm | Values (calls) |", "|---|---|---|---|"]
    for (seam, field, arm), counter in sorted(vocab.items()):
        out.append(f"| `{seam}` | {field} | {arm} | "
                   + ", ".join(f"`{k}` ({v})" for k, v in sorted(counter.items())) + " |")

    out += [
        "",
        "## LLM calls whose messages the trace does not record",
        "",
        "- `registry_expansion_generation`: the trace records only the claim value, subject, evidence texts "
        "and existing domains, with the served model in the step. The prompt text is in the register, from "
        "the code at 3320375.",
        "",
        "| Arm | Generation method | Served snapshot | Calls |",
        "|---|---|---|---:|",
    ]
    for arm in ARMS:
        for (method, model), n in sorted(expansion[arm].items(), key=str):
            out.append(f"| {arm} | {method} | {model} | {n} |")
    out += [
        "",
        "- The judge (gpt-5.4-2026-03-05) is not a trace step; its inputs are not recorded in trace.json.",
        "",
        "## Trace steps without messages",
        "",
        "These steps are workflow logs of deterministic services (or of LLM calls listed above).",
        "",
        "| Seam | Mode | " + " | ".join(ARMS) + " |",
        "|---|---|" + "---:|" * len(ARMS),
    ]
    keys = sorted({(seam, mode) for (seam, arm), c in other.items() for mode in c})
    for seam, mode in keys:
        out.append(f"| `{seam}` | {mode} | " + " | ".join(str(other[(seam, a)][mode]) for a in ARMS) + " |")

    out += [
        "",
        "## Registry carried per meeting",
        "",
        "A step belongs to the meeting of the next checkpoint question in the trace. Key sets are read from "
        "the registry lines (`  - <key> [` in extraction, `  - <key>: ` in resolution).",
        "- **Extraction:** calls; distinct key sets listed (one means one registry per meeting); keys listed; "
        "system-message length in characters; calls with the empty-registry sentinel; calls whose span text "
        "an earlier extraction call of the run already sent.",
        "- **Resolution, write path:** calls; keys listed (min / median / max); calls listing no key; calls "
        "listing exactly the key set of that meeting's extraction prompt.",
        "- **Resolution, read path:** calls; keys listed; calls listing exactly the key set of the next "
        "meeting's extraction prompt (n/a after the last meeting).",
        "",
        "| Arm | Run | Mtg | Ex calls | Ex key sets | Ex keys | Ex chars | Ex empty | Ex repeat "
        "| W calls | W keys | W none | W whole | R calls | R keys | R whole |",
        "|---|---|---|---:|---:|---|---|---:|---:|---:|---|---:|---:|---:|---|---:|",
    ]
    for row in registry_rows:
        out.append(
            f"| {row['arm']} | {row['run']} | {row['meeting']} | {row['ex_calls']} | {row['ex_keysets']} | "
            f"{', '.join(map(str, row['ex_keys']))} | {', '.join(map(str, row['ex_chars']))} | {row['ex_empty']} | "
            f"{row['ex_repeat']} | {row['w_calls']} | {row['w_keys']} | {row['w_zero']} | {row['w_full']} | "
            f"{row['r_calls']} | {row['r_keys']} | {row['r_full']} |")

    out += ["", "## Full texts of the static variants", ""]
    for h, v in sorted(variants.items(), key=lambda kv: (list(PATTERNS).index(kv[1]["seam"]), kv[1]["role"], kv[0])):
        arms = ", ".join(f"{a} {v['calls'][a]}" for a in ARMS if v["calls"][a])
        f = fence(v["text"])
        out += [
            f"### `{v['seam']}` {v['role']} `{h[:12]}`",
            "",
            f"- SHA-256: `{h}`",
            f"- Calls: {arms}. Length: {len(v['text'])} characters." + ("" if v["parsed"] else " **Unparsed.**"),
            "",
            f + "text",
            v["text"],
            f,
            "",
        ]
    OUT.write_text("\n".join(out))
    print(OUT, hashlib.sha256(OUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
