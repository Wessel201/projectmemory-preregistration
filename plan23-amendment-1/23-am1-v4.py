"""Plan 23, amendment 1: V4, the machine second coder, a Gemini model run as
an agent in Google Antigravity.

V4 is a model from a third family: not Claude (the pre-coder and the v1
adjudicators), not GPT (the system under test and its judge). Antigravity is an
agent with file, terminal and browser tools, so it never opens the repository:
each packet is staged alone into a clean workspace folder outside it, coded in
a new Antigravity conversation with the fixed instruction below, and its
answer file is collected back here. This script makes the packets, stages
them and records the answers; it makes no API call.

V4 starts after author pass 1 (amendment, order of work, item 4) is
committed: no packet, case or audit, is staged before then (line 405).

Two jobs (amendment, Step 3, items 5 and 6). Each set of packets is built into
its own --out folder:
  cases   case pages, coded with the pre-coder's prompt, unchanged
          (23-am1-precoder-template.md, Section 1): the template with the
          extract filled in at signing, the frozen sub-cause list and one page,
          by literal replacement, once each. One case per conversation, so the
          instrument is the pre-coder's and only the model differs. The same
          command builds each set of cases V4 codes:
            - the channel trial: the 20 pilot cases (amendment line 310),
              coded before the first of the 180 and counting toward nothing;
            - the 180 cases of 3a;
            - after a codebook revision (line 409), every case packet again,
              with the revised sub-cause list, coded before item 7; both sets
              are kept hashed;
            - the fresh sample after a revision (line 311);
            - 3b (lines 305 and 312).
          V4 does not re-code at item 8 (line 414): its mechanically resolved
          blind code is its final code.
  audit   the adjudication audit list, under the loss trace's carry standard
          as worded in 23-loss-trace.md. Packet fields: id, fact_id, gold
          value, the gold value's status in the suite, aliases, text,
          contexts; never roles, decides_rows or recorded_result_rows.
          Order: ascending sha256("<salt>|<id>"), salt from the signing note.

Commands (run from the repository root with the project's .venv):
  .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-v4.py \\
      audit-packets --salt S --out DIR [--batch 60]
  ... case-packets --template T --subcauses F --pages DIR --salt S --out DIR
  ... stage --out DIR --packet NAME --workspace WS
  ... collect --out DIR --packet NAME --workspace WS --model LABEL \\
      --antigravity-version V [--void REASON] [--model-change]
  ... reject --out DIR --packet NAME --reason TEXT

stage writes a marker beside the workspace WS, outside it, at
WS.parent/.<WS.name>.v4-staging.json (the resolved DIR, the packet, the
staging number and the packet's SHA-256). It then empties WS, copies the
packet into it as packet.txt and appends a line to DIR/staging.log (staging
number, packet, its SHA-256, workspace, time). A new Antigravity
conversation, opened on WS only, then gets INSTRUCTION below, word for word,
and nothing else. stage refuses:
  - a workspace inside the repository, compared by file identity;
  - a workspace with a marker, whatever DIR it names: a staging is open there;
  - a workspace holding anything other than packet.txt and answer.json;
  - a workspace with a staging of DIR that has no collected attempt yet, or a
    packet.txt or answer.json that no open staging accounts for, for example
    an answer the agent wrote after collect: it is kept with the AG7 record
    and removed by hand;
  - a packet with a staging not yet collected, with a counted valid attempt,
    or with two attempts.
Emptying the workspace only ever removes packet.txt and answer.json, and
only as the leftovers of a collected staging of DIR.

collect records exactly one attempt per staging, as
DIR/responses/<packet>.attempt-N.json, then removes answer.json and
packet.txt from the workspace, and then the marker. It refuses unless the
marker names DIR, the packet and the staging being collected, so it never
removes another job's files, and it checks that the workspace still holds the
packet. A missing, unreadable or non-UTF-8 answer.json is a failed attempt,
and so is an answer given only in the chat: there is no other source.
--void REASON records a void attempt and runs no checks; it stores --model as
given and neither checks nor updates model.json, so an answer given under a
wrong label can be voided (AG3), and --model-change is refused with it. An
answer too deeply nested to store is kept as raw only, as a failed attempt.
Checks:
  audit   one JSON object {"answers": [{"id", "carries"}]} naming exactly the
          packet's ids, each a string and each once, carries true or false;
  cases   template Section 4, checks 1, 2 (case_id), 3, 7 and 8. Check 3
          tests each quote only against the Part H block of its stated
          source, the case page or the extract. Check 7 needs an exact name
          from the frozen list, or "none fits"; case-packets reads the names
          from the list's Markdown table (column "Name" or "Sub-cause") and
          records them in the manifest. A case record that passes is valid
          only provisionally: the shared validator (Section 4, checks 1-9)
          runs on every stored case record before any agreement.
A single code fence around the JSON is removed and the removal recorded; any
other text around it fails the check.

reject records that the shared validator rejected a packet's stored valid
attempt, in DIR/responses/<packet>.attempt-N.rejected.json; the attempt file
is never changed. The attempt then counts as failed. Case records only.

A packet gets at most two attempts (template R7), voids, missing answers and
rejected attempts included. A packet with two failed attempts has no V4 code.
The first collect in DIR without --void fixes the model label in
DIR/model.json; a different --model is refused unless --model-change, which
records the change.

No packet contains a coder's codes, a pre-code, a v1 label, a result or a
Step 2, 2b or 2c output: the case packets are the pre-coder's assembled
prompts, whose inputs pass the template's blindness checks, and the audit
packets carry only the fields listed above.

Record: 28 October 2026, check_case's check 7 also accepts sub_cause "not
applicable" when the class is neither "implementation defect" nor "unclear"
(decision sheet B18; template Section 4, check 7).
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import yaml

ART = Path(__file__).resolve().parent
ROOT = ART.parents[3]
AUDIT_LIST = ART / "23-am1-audit-list.json"
TRACE = ART / "23-loss-trace.json"
TRACE_DOC = ART / "23-loss-trace.md"
TEMPLATE_DOC = ART / "23-am1-precoder-template.md"
SUITE = ROOT / "data/ami_eval/suites/transfer_el2020.yaml"
MAX_CONTEXTS = 3

# The loss trace's carry standard as 23-loss-trace.md words it (its line 148).
# That wording is a condensed form of the adjudicator prompts of round 3 and
# the fixpoint, not their exact text. Checked against that file on every run.
STANDARD = """a text carries the gold value when a careful coder would say it states that value, so that an answer built from it would be judged correct for a question asking for that value.
  - A paraphrase, or a more specific or more complete statement, carries it.
  - For a value of two or more independent parts, one part alone does not, even if it is a gold alias. Leaving out a minor qualifier does not prevent carrying.
  - A different value, a rival option, a sibling's value or the topic words alone do not carry it.
  - A ruled-out option carries when the text names it; polarity is judged elsewhere.
  - Texts are read with their contexts (subject, predicate, key). When a text means different things in different contexts, its most common context decides."""

AUDIT_HEADER = """You are checking, one by one, whether a short text extracted from a meeting carries a gold value.

The standard: {standard}

Each item gives an id, the gold value's fact id, the gold value, its status, any accepted aliases, the text, and the contexts the text was extracted in: subject, predicate and the state key it was filed under, with how often each context occurs. The status line gives the gold value's status after each meeting that lists it. A value rejected at every meeting that lists it is an option ruled out there, and the standard's rule for a ruled-out option applies to it. A value first listed as current or candidate and later rejected was replaced later; it carries when the text states that same value. Decide each item on its own, from what is written in this message only. Do not use tools, any other file, or anything you remember about this project.

Return one JSON object and nothing else, no prose and no code fence:
{{"answers": [{{"id": "<item id>", "carries": true}}, ...]}}
with one entry per item below, each id once, in any order. "carries" is true or false.

ITEMS
"""


# The whole message of each Antigravity conversation (template Section 9, AG2).
# It maps the packet's "this message" and "Do not use tools" onto the
# workspace (AG4); the packet itself is unchanged.
INSTRUCTION = ('packet.txt in this folder is the message it refers to: where it says "this message", '
               'it means packet.txt. Read packet.txt and do what it asks. Its "Do not use tools" allows '
               'exactly three actions here: listing this folder, reading packet.txt, and writing your '
               'answer to answer.json in this folder. Do not read any other file, run a command, open a '
               'browser or search the web. Write to answer.json the JSON object the packet asks for and '
               'nothing else, and do not answer in the chat.')
CHANNEL = "Google Antigravity, new conversation on a clean workspace"
SETTINGS = "none exposed"  # Antigravity exposes no sampling settings (AG5; Section 9, "What this does not give")
WORKSPACE_FILES = {"packet.txt", "answer.json"}
MAX_ATTEMPTS = 2  # template R7
ATTEMPT_FILE = re.compile(r"(?P<packet>.+)\.attempt-(?P<n>\d+)\.json")


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_text(t: str) -> str:
    return sha_bytes(t.encode("utf-8"))


def order_key(salt: str, ident: str) -> str:
    return sha_text(f"{salt}|{ident}")


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise SystemExit(f"{path} exists; packets and answers are never overwritten")
    data = text.encode("utf-8")  # encode first, so a failed encode leaves no empty file
    path.write_bytes(data)


def say(text: str) -> None:
    """Print, with a lone surrogate (from an answer or an argument) escaped
    instead of crashing after the record is written."""
    enc = sys.stdout.encoding or "utf-8"
    print(text.encode(enc, "backslashreplace").decode(enc))


# ---------- audit packets ----------

def _value(claim: dict) -> str:
    obj = claim.get("object") or {}
    return str(obj.get("value") or obj.get("role") or "")


def _spo(claim: dict) -> str:
    return f"{claim.get('subject') or ''} {claim.get('predicate') or ''} {_value(claim)}".strip()


def gold_by_fact() -> dict:
    """fact_id -> its values, aliases and its status after each meeting that
    lists it (the suite's `status` field, in meeting order)."""
    suite = yaml.safe_load(SUITE.read_text())
    gold: dict = {}
    for meeting in suite["meetings"]:
        for g in suite["gold"][meeting]:
            entry = gold.setdefault(g["fact_id"], {"values": [], "aliases": [], "statuses": []})
            if g["value"] not in entry["values"]:
                entry["values"].append(g["value"])
            for a in g.get("aliases") or []:
                if a not in entry["aliases"]:
                    entry["aliases"].append(a)
            entry["statuses"].append((meeting, g["status"]))
    return gold


def status_line(statuses: list[tuple[str, str]]) -> str:
    """'current_confirmed after EL2020b; rejected after EL2020c, EL2020d'."""
    runs: list[tuple[str, list[str]]] = []
    for meeting, status in statuses:
        if runs and runs[-1][0] == status:
            runs[-1][1].append(meeting)
        else:
            runs.append((status, [meeting]))
    return "; ".join(f"{status} after {', '.join(meetings)}" for status, meetings in runs)


def contexts(run_dirs: list[Path]) -> dict:
    """text -> Counter of (subject, predicate, state_key) over every traced
    run; a text is a claim's object, or its subject + predicate + object, as
    the loss trace reads claims; a stored value no claim states verbatim gets
    its key only."""
    found: dict = collections.defaultdict(collections.Counter)
    for run in run_dirs:
        (state,) = run.rglob("*.state.json")
        dump = json.loads(state.read_text())
        for c in dump["claims"]:
            ctx = (c.get("subject") or "", c.get("predicate") or "", c.get("state_key") or "(none)")
            for text in {_value(c), _spo(c)}:
                if text:
                    found[text][ctx] += 1
        # rival texts can be stored values that no claim states verbatim
        for row in [*dump["proposals"], *dump["state_facts"]]:
            text = str(row.get("value") or "")
            if text and text not in found:
                found[text][("(stored value)", "", row.get("state_key") or "(none)")] += 1
    return found


def audit_packets(args) -> None:
    if args.batch < 1:
        raise SystemExit("--batch must be at least 1")
    doc = TRACE_DOC.read_text()
    if STANDARD not in doc:
        raise SystemExit("the carry standard no longer matches 23-loss-trace.md")
    audit = json.loads(AUDIT_LIST.read_text())
    gold = gold_by_fact()
    # contexts from every traced run: the v1 decisions were made on texts from all arms
    trace = json.loads(TRACE.read_text())
    ctx = contexts([ROOT / r["dir"] for r in trace["runs"]])
    items = sorted(audit["items"], key=lambda i: order_key(args.salt, i["id"]))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    header = AUDIT_HEADER.format(standard=STANDARD)
    manifest = {"job": "audit", "salt": args.salt, "batch_size": args.batch,
                "audit_list_sha256": sha_bytes(AUDIT_LIST.read_bytes()),
                "suite_sha256": sha_bytes(SUITE.read_bytes()),
                "trace_sha256": sha_bytes(TRACE.read_bytes()),
                "script_sha256": sha_bytes(Path(__file__).read_bytes()),
                "standard_sha256": sha_text(STANDARD), "packets": {}}
    no_context = 0
    for n in range(0, len(items), args.batch):
        batch = items[n:n + args.batch]
        lines = []
        for i in batch:
            g = gold[i["fact_id"]]
            seen = ctx.get(i["text"]) or collections.Counter()
            no_context += not seen
            lines.append(f"- id: {i['id']}")
            lines.append(f"  fact_id: {i['fact_id']}")
            lines.append(f"  gold value: {' | '.join(g['values'])}")
            lines.append(f"  status: {status_line(g['statuses'])}")
            lines.append(f"  aliases: {' | '.join(g['aliases']) if g['aliases'] else '(none)'}")
            lines.append(f"  text: {i['text']}")
            if seen:
                lines.append("  contexts:")
                for (s, p, k), c in seen.most_common(MAX_CONTEXTS):
                    lines.append(f"    - subject: {s}; predicate: {p}; key: {k} ({c}x)")
            else:
                lines.append("  contexts: (none recorded)")
        name = f"audit-{n // args.batch + 1:02d}"
        text = header + "\n".join(lines) + "\n"
        write_new(out / f"{name}.txt", text)
        manifest["packets"][name] = {"ids": [i["id"] for i in batch], "sha256": sha_text(text)}
    manifest["items"] = len(items)
    manifest["items_without_context"] = no_context
    write_new(out / "manifest.json", json.dumps(manifest, indent=2))
    print(f"{len(items)} items in {len(manifest['packets'])} packets; "
          f"{no_context} without a recorded context")


# ---------- case packets ----------

def blocks(prompt: str) -> dict:
    """The three filled slots of the prompt's Part H, cut at the delimiters
    of template Section 2. The extract and the sub-cause list are cut at their
    first closing line, the page at the last one, which only the fixed closing
    text follows."""
    sheet, rest = prompt.split("\n<register_sheet>\n", 1)[1].split("\n</register_sheet>\n\n<subcauses>\n", 1)
    subcauses, rest = rest.split("\n</subcauses>\n\n<case_page>\n", 1)
    page = rest.rsplit("\n</case_page>\n", 1)[0]
    return {"register sheet": sheet, "sub-cause list": subcauses, "case page": page}


def _cells(line: str) -> list[str]:
    """A Markdown table row's cells, with a wrapping ** or ` pair removed."""
    cells = []
    for cell in re.split(r"(?<!\\)\|", line.strip().strip("|")):
        cell = cell.replace("\\|", "|").strip()
        for mark in ("**", "`"):
            if len(cell) > 2 * len(mark) and cell.startswith(mark) and cell.endswith(mark):
                cell = cell[len(mark):-len(mark)].strip()
        cells.append(cell)
    return cells


def subcause_names(text: str) -> list[str]:
    """The names in a frozen sub-cause list, for check 7 (template E7: "a name
    from the sub-cause list, exactly as written"). The list is a Markdown table,
    or several; a name is a cell of the column headed "Name" or "Sub-cause"."""
    names: list[str] = []
    column = None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            column = None
            continue
        cells = _cells(line)
        if column is None:  # a table's header row
            heads = [c.lower() for c in cells]
            column = next((n for n, h in enumerate(heads) if h in ("name", "sub-cause")), -1)
        elif 0 <= column < len(cells) and not all(re.fullmatch(r":?-+:?", c) for c in cells):
            if cells[column] and cells[column] not in names:
                names.append(cells[column])
    return names


def case_packets(args) -> None:
    template = Path(args.template).read_text(encoding="utf-8")
    if "{REGISTER_SHEET}" in template:
        raise SystemExit("the template's extract is not filled in (template Section 1)")
    for slot in ("{SUBCAUSES}", "{CASE_PAGE}"):
        if template.count(slot) != 1:
            raise SystemExit(f"{slot} must occur exactly once")
    subcauses = Path(args.subcauses).read_text(encoding="utf-8")
    names = subcause_names(subcauses)
    if not names:
        raise SystemExit("no sub-cause names found: the list needs a Markdown table with a "
                         "column headed Name or Sub-cause (check 7)")
    pages = sorted(Path(args.pages).glob("*.md"), key=lambda p: order_key(args.salt, p.stem))
    if not pages:
        raise SystemExit(f"no case pages (*.md) in {args.pages}")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    manifest = {"job": "cases", "salt": args.salt, "template_sha256": sha_text(template),
                "subcauses_sha256": sha_text(subcauses), "subcause_names": names,
                "script_sha256": sha_bytes(Path(__file__).read_bytes()), "packets": {}}
    for n, page_path in enumerate(pages, 1):
        page = page_path.read_text(encoding="utf-8")
        prompt = template.replace("{SUBCAUSES}", subcauses, 1).replace("{CASE_PAGE}", page, 1)
        try:
            parts = blocks(prompt)
        except (IndexError, ValueError):
            raise SystemExit("the template's Part H delimiters are missing (template Section 2)")
        if parts["sub-cause list"] != subcauses or parts["case page"] != page:
            raise SystemExit(f"{page_path.name} or the sub-cause list contains a Part H delimiter")
        manifest.setdefault("extract_sha256", sha_text(parts["register sheet"]))
        name = f"case-{n:04d}"
        write_new(out / f"{name}.txt", prompt)
        manifest["packets"][name] = {"case_id": page_path.stem, "page_sha256": sha_text(page),
                                     "prompt_sha256": sha_text(prompt)}
    write_new(out / "manifest.json", json.dumps(manifest, indent=2))
    print(f"{len(pages)} case packets; {len(names)} sub-cause names: {'; '.join(names)}")


# ---------- schema (the subset of draft-07 the pre-coder schema uses) ----------

TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def _is(value, t: str) -> bool:
    if t in ("integer", "number"):
        return isinstance(value, (int, float)) and not isinstance(value, bool) and (
            t == "number" or float(value).is_integer())
    return isinstance(value, TYPES[t])


def errors(value, schema: dict, path: str = "$") -> list[str]:
    out: list[str] = []
    for kw, arg in schema.items():
        if kw in ("$schema", "title", "description"):
            continue
        if kw == "type":
            if not any(_is(value, t) for t in (arg if isinstance(arg, list) else [arg])):
                out.append(f"{path}: not {arg}")
                return out
        elif kw == "enum" and value not in arg:
            out.append(f"{path}: {value!r} not in enum")
        elif kw == "const" and value != arg:
            out.append(f"{path}: not {arg!r}")
        elif kw == "required" and isinstance(value, dict):
            out += [f"{path}: missing {k}" for k in arg if k not in value]
        elif kw == "properties" and isinstance(value, dict):
            for k, sub in arg.items():
                if k in value:
                    out += errors(value[k], sub, f"{path}.{k}")
        elif kw == "additionalProperties" and isinstance(value, dict) and arg is False:
            out += [f"{path}: unexpected {k}" for k in value if k not in schema.get("properties", {})]
        elif kw == "items" and isinstance(value, list):
            for n, v in enumerate(value):
                out += errors(v, arg, f"{path}[{n}]")
        elif kw == "contains" and isinstance(value, list):
            if not any(not errors(v, arg) for v in value):
                out.append(f"{path}: no item matches 'contains'")
        elif kw == "minItems" and isinstance(value, list) and len(value) < arg:
            out.append(f"{path}: fewer than {arg} items")
        elif kw == "maxItems" and isinstance(value, list) and len(value) > arg:
            out.append(f"{path}: more than {arg} items")
        elif kw == "uniqueItems" and arg and isinstance(value, list):
            if len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
                out.append(f"{path}: items not unique")
        elif kw == "minLength" and isinstance(value, str) and len(value) < arg:
            out.append(f"{path}: shorter than {arg}")
        elif kw == "maxLength" and isinstance(value, str) and len(value) > arg:
            out.append(f"{path}: longer than {arg}")
        elif kw == "allOf":
            for sub in arg:
                out += errors(value, sub, path)
        elif kw == "not":
            if not errors(value, arg, path):
                out.append(f"{path}: matches 'not'")
        elif kw == "if":
            branch = schema.get("then") if not errors(value, arg, path) else schema.get("else")
            if branch:
                out += errors(value, branch, path)
        elif kw in ("then", "else"):
            continue
        elif kw not in ("type", "enum", "const", "required", "properties", "additionalProperties",
                        "items", "contains", "minItems", "maxItems", "uniqueItems", "minLength",
                        "maxLength"):
            raise SystemExit(f"schema keyword {kw!r} is not supported by this checker")
    return out


def prompt_schema(prompt: str) -> dict:
    return json.loads(prompt.split("\nBEGIN OUTPUT SCHEMA\n")[1].split("\nEND OUTPUT SCHEMA\n")[0])


# ---------- answer checks ----------

def parse_answer(raw: str) -> tuple[object, bool]:
    text = raw.strip()
    fence = re.fullmatch(r"```(?:json)?\s*\n(.*)\n```", text, re.S)
    if fence:
        text = fence.group(1).strip()
    return json.loads(text), bool(fence)


def check_audit(answer, ids: list[str]) -> list[str]:
    if not isinstance(answer, dict) or set(answer) != {"answers"} or not isinstance(answer["answers"], list):
        return ['not {"answers": [...]}']
    out = []
    got = []
    for a in answer["answers"]:
        if not isinstance(a, dict) or set(a) != {"id", "carries"} or not isinstance(a["carries"], bool):
            out.append(f"malformed entry {a!r}"[:200])
        elif not isinstance(a["id"], str):
            out.append(f"id {a['id']!r} is not a string"[:200])
        else:
            got.append(a["id"])
    wanted = set(ids)
    missing = sorted(wanted - set(got))
    extra = sorted(k for k, c in collections.Counter(got).items() if c > 1 or k not in wanted)
    if missing or extra:
        out.append(f"ids differ from the packet: missing {missing}, extra or repeated {extra}")
    return out


def _quotes(record: dict) -> list[tuple[str, str]]:
    """(stated source, quote) for every quote of template check 3. design_ground
    and tradeoff_benefit_quote state no source: both quote 94c049d text, which
    only the extract carries (field notes; check 6)."""
    quotes = [(e["source"], e["quote"]) for e in record["evidence"]]
    quotes += [(c["evidence"]["source"], c["evidence"]["quote"]) for c in record["checklist"]]
    quotes += [("register sheet", d["quote"]) for d in record["design_ground"]]
    if record["tradeoff_benefit_quote"] is not None:
        quotes.append(("register sheet", record["tradeoff_benefit_quote"]))
    return quotes


def check_case(record, prompt: str, case_id: str, names: list[str]) -> list[str]:
    out = errors(record, prompt_schema(prompt))  # check 1
    if out or not isinstance(record, dict):
        return out
    if record["case_id"] != case_id:  # check 2, case_id only
        out.append(f"case_id {record['case_id']!r} is not {case_id!r}")
    parts = blocks(prompt)
    for source, quote in _quotes(record):  # check 3: only the block of the stated source
        if source == "none":
            if quote:
                out.append(f"a quote with source none: {quote[:80]!r}")
        elif quote not in parts[source]:
            out.append(f"quote not found in the {source}: {quote[:80]!r}")
    sub = record["sub_cause"]
    if sub == "not applicable":  # check 7: allowed for a class other than these two (decision sheet B18)
        if record["class"] in ("implementation defect", "unclear"):
            out.append(f"sub_cause 'not applicable' with class {record['class']!r}")
    elif sub != "none fits" and sub not in names:  # check 7: an exact name
        out.append(f"sub_cause {sub[:80]!r} is not a name in the frozen list")
    expected = {"instructions", "register sheet", "sub-cause list", "case page"}
    if set(record["inputs_received"]) != expected or record["other_input"] is not None:  # check 8
        out.append("inputs_received is not exactly the four inputs, or other_input is set")
    return out


# ---------- records in DIR ----------

def _manifest(out: Path) -> dict:
    path = out / "manifest.json"
    if not path.exists():
        raise SystemExit(f"no manifest.json in {out}; build the packets first")
    return json.loads(path.read_text(encoding="utf-8"))


def _packet(out: Path, manifest: dict, name: str) -> bytes:
    """The packet's bytes, refused if the packet is unknown or its file no
    longer has the hash its manifest recorded."""
    entry = manifest["packets"].get(name)
    if entry is None:
        raise SystemExit(f"no packet {name}")
    data = (out / f"{name}.txt").read_bytes()
    if sha_bytes(data) != entry.get("sha256", entry.get("prompt_sha256")):
        raise SystemExit(f"{name}.txt has changed since its manifest was written")
    return data


def _stagings(out: Path) -> list[dict]:
    path = out / "staging.log"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _records(out: Path) -> list[dict]:
    """Every stored attempt in DIR/responses. "rejected" is read from the
    attempt's separate rejection file; the attempt file is never changed."""
    found = []
    for path in sorted((out / "responses").glob("*.attempt-*.json")):
        if ATTEMPT_FILE.fullmatch(path.name):
            record = json.loads(path.read_text(encoding="utf-8"))
            record["rejected"] = path.with_name(path.name[:-len(".json")] + ".rejected.json").exists()
            found.append(record)
    return found


def _attempts(out: Path, packet: str) -> list[dict]:
    return sorted((r for r in _records(out) if r["packet"] == packet), key=lambda r: r["attempt"])


def _counted(record: dict) -> bool:
    return record["valid"] and not record["rejected"]


# ---------- workspace ----------

def _workspace(path: str) -> Path:
    """The workspace, refused if it is the repository or inside it (AG1). It is
    compared by file identity, not by spelling, so a case variant, a firmlink
    path (/System/Volumes/Data/...) or a symbolic link does not get past."""
    ws = Path(path).expanduser().resolve()
    root = os.stat(ROOT)
    for p in (ws, *ws.parents):
        if p.exists() and os.path.samestat(os.stat(p), root):
            raise SystemExit("the workspace must be outside the repository")
    return ws


def _same_place(recorded: str, ws: Path) -> bool:
    other = Path(recorded)
    return other == ws or (other.exists() and ws.exists() and os.path.samestat(os.stat(other), os.stat(ws)))


def _marker_path(ws: Path) -> Path:
    """The marker of an open staging: beside the workspace, outside it, so the
    agent does not see it and stage finds it whatever --out it is run with
    (AG1)."""
    if not ws.name:
        raise SystemExit("the workspace cannot be a filesystem root")
    return ws.parent / f".{ws.name}.v4-staging.json"


def _read_marker(path: Path) -> dict | None:
    """The marker's content, or None if it is missing or cannot be read as one."""
    try:
        note = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if (not isinstance(note, dict) or not isinstance(note.get("out"), str)
            or not isinstance(note.get("packet"), str) or type(note.get("staging")) is not int):
        return None
    return note


def _open_staging(marker: Path) -> str:
    """What the marker names, and what to do about it. A marker whose staging
    is already collected was left by an interrupted collect; collecting it
    again is refused, so the message does not ask for that."""
    note = _read_marker(marker)
    if note is None:
        return (f"{marker} marks an open staging in this workspace but cannot be read; check it against "
                "the AG7 record and remove it by hand")
    where = f"staging {note['staging']} ({note['packet']}) of {note['out']}"
    try:
        collected = any(r.get("staging") == note["staging"] for r in _records(Path(note["out"])))
    except (OSError, ValueError, AttributeError, TypeError):
        collected = False
    if collected:
        return (f"{where} is already collected, but its marker {marker} is still there (collect was "
                "interrupted); keep the marker and the workspace's files with the AG7 record and remove "
                "them by hand")
    return (f"{where} is open in this workspace (marker {marker}); collect it first, under that --out "
            "(with --void if the conversation is void)")


def _check_leftovers(out: Path, ws: Path, log: list[dict], records: list[dict]) -> None:
    """A packet.txt or answer.json in the workspace may be removed only as the
    leftover of a staging of this folder that has a collected attempt. stage
    checks this only when no marker is open, so anything else is a file that
    no open staging accounts for, for example an answer the agent wrote after
    collect. It is kept with the AG7 record and removed by hand, never by this
    script (AG1)."""
    held, answer = ws / "packet.txt", ws / "answer.json"
    if not os.path.lexists(held) and not os.path.lexists(answer):
        return
    by_hand = ("no open staging accounts for (for example an answer the agent wrote after collect); "
               "keep it with the AG7 record and remove it by hand")
    done = {r["staging"]: r for r in records}
    staging = None
    if held.is_file() and not held.is_symlink():
        sha = sha_bytes(held.read_bytes())
        staging = next((e for e in reversed(log) if e["packet_sha256"] == sha and e["staging"] in done
                        and _same_place(e["workspace"], ws)), None)
    if staging is None:
        raise SystemExit(f"the workspace holds a packet.txt or answer.json that {by_hand}")
    if os.path.lexists(answer):
        raw_sha = done[staging["staging"]]["raw_sha256"]
        if answer.is_symlink() or not answer.is_file() or sha_bytes(answer.read_bytes()) != raw_sha:
            raise SystemExit(f"the workspace holds an answer.json that no stored attempt records and {by_hand}")


def stage(args) -> None:
    out, ws = Path(args.out), _workspace(args.workspace)
    manifest = _manifest(out)
    packet = _packet(out, manifest, args.packet)
    records, log = _records(out), _stagings(out)
    attempts = sorted((r for r in records if r["packet"] == args.packet), key=lambda r: r["attempt"])
    if any(_counted(a) for a in attempts):
        raise SystemExit(f"{args.packet} already has a valid answer")
    if len(attempts) >= MAX_ATTEMPTS:
        raise SystemExit(f"{args.packet} has {len(attempts)} failed attempts; it gets no V4 code (template R7)")
    marker = _marker_path(ws)
    if os.path.lexists(marker):  # an open staging, whatever --out staged it
        raise SystemExit(_open_staging(marker))
    done = {r["staging"] for r in records}
    for e in log:
        if e["staging"] in done:
            continue
        if e["packet"] == args.packet:
            raise SystemExit(f"{args.packet} has staging {e['staging']} with no collected attempt; collect it first")
        if _same_place(e["workspace"], ws):
            raise SystemExit(f"staging {e['staging']} ({e['packet']}) in this workspace has no collected "
                             "attempt; collect it first (with --void if the conversation is void)")
    if ws.exists() and not ws.is_dir():
        raise SystemExit(f"{ws} is not a folder")
    try:
        ws.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"the workspace {ws} could not be created: {exc.strerror or exc}")
    present = {p.name for p in ws.iterdir()}
    if present - WORKSPACE_FILES:
        raise SystemExit(f"the workspace holds other files: {sorted(present - WORKSPACE_FILES)}")
    _check_leftovers(out, ws, log, records)
    entry = {"staging": len(log) + 1, "packet": args.packet, "packet_sha256": sha_bytes(packet),
             "workspace": str(ws), "staged_at": now()}
    note = {"out": str(out.resolve()), "packet": args.packet, "staging": entry["staging"],
            "packet_sha256": entry["packet_sha256"]}
    try:
        with marker.open("x", encoding="utf-8") as f:  # exclusive: a second stage on this workspace fails here
            f.write(json.dumps(note, indent=2) + "\n")
    except FileExistsError:
        raise SystemExit(_open_staging(marker))
    except OSError as exc:
        raise SystemExit(f"the staging marker {marker} could not be written: {exc.strerror or exc}")
    logged = False
    try:
        for name in WORKSPACE_FILES:  # the only files stage ever removes
            if os.path.lexists(ws / name):
                (ws / name).unlink()
        (ws / "packet.txt").write_bytes(packet)
        with (out / "staging.log").open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        logged = True
    except OSError as exc:
        raise SystemExit(f"the staging failed, so no staging is open: {exc}")
    finally:
        if not logged:  # no staging.log line, so no staging is open
            marker.unlink(missing_ok=True)
    say(f"staging {entry['staging']}: {args.packet} in {ws}, attempt {len(attempts) + 1} of {MAX_ATTEMPTS}. "
        f"In a new Antigravity conversation on that folder, send:\n\n{INSTRUCTION}\n\n"
        f"(instruction sha256 {sha_text(INSTRUCTION)})")


# ---------- collect ----------

def _model_label(out: Path, label: str, change: bool, records: list[dict]) -> dict | None:
    """The model label is fixed by the first collect in DIR without --void
    (AG3); a void neither checks nor updates it. Returns model.json's new
    content, or None when it is unchanged."""
    path = out / "model.json"
    if not path.exists():
        if change:
            raise SystemExit("--model-change, but no label is recorded in this folder yet")
        return {"labels": [{"model": label, "at": now(), "packets_coded_so_far": []}]}
    data = json.loads(path.read_text(encoding="utf-8"))
    current = data["labels"][-1]["model"]
    if label == current:
        if change:
            raise SystemExit(f"--model-change, but the label is already {current!r}")
        return None
    if not change:
        raise SystemExit(f"the model label in this folder is {current!r}; a different label needs "
                         "--model-change, which records the change")
    coded = sorted({r["packet"] for r in records if _counted(r)})
    data["labels"].append({"model": label, "at": now(), "packets_coded_so_far": coded})
    return data


def read_answer(path: Path) -> tuple[str | None, str | None, list[str]]:
    """(raw text, SHA-256 of the file's bytes, problems). A missing, linked,
    unreadable or non-UTF-8 answer.json is a problem, not a crash."""
    if not os.path.lexists(path):
        return None, None, ["no answer.json in the workspace"]
    if path.is_symlink():
        return None, None, ["answer.json is a symbolic link; it was not read"]
    try:
        data = path.read_bytes()
    except OSError as exc:
        return None, None, [f"answer.json could not be read: {exc.strerror or exc}"]
    try:
        return data.decode("utf-8"), sha_bytes(data), []
    except UnicodeDecodeError as exc:
        return (data.decode("utf-8", "backslashreplace"), sha_bytes(data),
                [f"answer.json is not UTF-8 ({exc.reason} at byte {exc.start}); raw keeps it with backslash escapes"])


def collect(args) -> None:
    out = Path(args.out)
    manifest = _manifest(out)
    packet = _packet(out, manifest, args.packet)
    ws = _workspace(args.workspace)
    void = args.void is not None
    if void and not args.void.strip():
        raise SystemExit("--void needs a reason")
    if void and args.model_change:
        raise SystemExit("--model-change cannot go with --void: a void attempt stores --model as given and "
                         "neither checks nor updates model.json (AG3)")
    if not args.model.strip() or not args.antigravity_version.strip():
        raise SystemExit("--model and --antigravity-version must not be empty")
    records = _records(out)
    stagings = [e for e in _stagings(out) if e["packet"] == args.packet]
    if not stagings:
        raise SystemExit(f"{args.packet} was never staged from {out}")
    staging = stagings[-1]
    if staging["staging"] in {r["staging"] for r in records}:
        raise SystemExit(f"staging {staging['staging']} of {args.packet} is already collected; "
                         "a new attempt needs a new staging")
    if not _same_place(staging["workspace"], ws):
        raise SystemExit(f"{args.packet} was staged in {staging['workspace']}, not in {ws}")
    attempts = [r for r in records if r["packet"] == args.packet]
    if len(attempts) >= MAX_ATTEMPTS:
        raise SystemExit(f"{args.packet} already has {len(attempts)} attempts (template R7)")
    marker = _marker_path(ws)
    note = _read_marker(marker)
    if note is None or not _same_place(note["out"], out.resolve()) or note["packet"] != args.packet \
            or note["staging"] != staging["staging"]:
        # the workspace's files may belong to another job's staging; they are not touched
        held_by = _open_staging(marker) if os.path.lexists(marker) else f"there is no marker {marker}"
        raise SystemExit(f"the workspace's staging marker does not name staging {staging['staging']} of "
                         f"{args.packet} in {out}: {held_by}")
    held = ws / "packet.txt"
    if not void and (held.is_symlink() or not held.is_file() or held.read_bytes() != packet):
        raise SystemExit(f"the workspace no longer holds {args.packet}; if the conversation changed or "
                         "removed packet.txt, record the attempt with --void")
    model = None if void else _model_label(out, args.model, args.model_change, records)  # AG3

    raw, raw_sha, problems = read_answer(ws / "answer.json")
    answer, fence = None, None
    if not void and not problems:
        try:
            answer, fence = parse_answer(raw)
        except (ValueError, RecursionError) as exc:
            fence, problems = False, [f"not JSON: {exc}"]
        else:
            if manifest["job"] == "audit":
                problems = check_audit(answer, manifest["packets"][args.packet]["ids"])
            else:
                problems = check_case(answer, packet.decode("utf-8"), manifest["packets"][args.packet]["case_id"],
                                      manifest["subcause_names"])
    record = {"packet": args.packet, "attempt": len(attempts) + 1, "staging": staging["staging"],
              "model": args.model, "antigravity_version": args.antigravity_version, "settings": SETTINGS,
              "channel": CHANNEL, "instruction_sha256": sha_text(INSTRUCTION), "collected_at": now(),
              "prompt_sha256": sha_bytes(packet), "source": "workspace", "raw_sha256": raw_sha, "raw": raw,
              "fence_removed": fence, "answer": answer, "valid": not void and not problems, "void": void,
              "void_reason": args.void if void else None, "rejected": False, "problems": problems}
    try:
        text = json.dumps(record, indent=2, ensure_ascii=False)
    except Exception:  # a RecursionError from a deeply nested answer, or any other error
        record.update(answer=None, valid=False,
                      problems=[*record["problems"], "answer nested too deeply to store; raw kept"])
        text = json.dumps(record, indent=2, ensure_ascii=False)
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:  # a lone surrogate from a \ud800-style escape in the answer
        text = json.dumps(record, indent=2)
    responses = out / "responses"
    responses.mkdir(exist_ok=True)
    path = responses / f"{args.packet}.attempt-{record['attempt']}.json"
    if model is not None:
        (out / "model.json").write_text(json.dumps(model, indent=2), encoding="utf-8")
    write_new(path, text)
    for name in ("answer.json", "packet.txt"):  # files only; never a folder
        target = ws / name
        if target.is_symlink() or target.is_file():
            target.unlink()
    marker.unlink(missing_ok=True)  # the staging is closed
    if record["valid"]:
        status = "valid" + (" (provisional: the shared validator runs before any agreement)"
                            if manifest["job"] == "cases" else "")
    else:
        status = (f"VOID: {args.void}" if void else "INVALID: " + "; ".join(record["problems"][:5]))
        status += ("; one more attempt in a new conversation" if record["attempt"] < MAX_ATTEMPTS
                   else "; no V4 code (template R7)")
    say(f"{path.name}: {status}")


def reject(args) -> None:
    """Records that the shared validator rejected the packet's stored valid
    attempt. The attempt then counts as failed, so a second attempt is allowed
    if the packet has only one (template R7)."""
    out = Path(args.out)
    manifest = _manifest(out)
    _packet(out, manifest, args.packet)
    if manifest["job"] != "cases":
        raise SystemExit("only case records go through the shared validator; an audit answer is not rejected")
    if not args.reason.strip():
        raise SystemExit("--reason must not be empty")
    valid = [a for a in _attempts(out, args.packet) if _counted(a)]
    if not valid:
        raise SystemExit(f"{args.packet} has no stored valid attempt to reject")
    attempt = valid[-1]["attempt"]
    stored = out / "responses" / f"{args.packet}.attempt-{attempt}.json"
    note = {"packet": args.packet, "attempt": attempt, "attempt_sha256": sha_bytes(stored.read_bytes()),
            "rejected_by": "the shared validator (template Section 4, checks 1-9)",
            "reason": args.reason, "rejected_at": now()}
    path = stored.with_name(f"{args.packet}.attempt-{attempt}.rejected.json")
    text = json.dumps(note, indent=2, ensure_ascii=False)
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        text = json.dumps(note, indent=2, ensure_ascii=True)
    write_new(path, text)
    left = "one more attempt in a new conversation" if attempt < MAX_ATTEMPTS else "no V4 code (template R7)"
    print(f"{path.name}: attempt {attempt} now counts as failed; {left}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("audit-packets")
    a.add_argument("--salt", required=True)
    a.add_argument("--out", required=True)
    a.add_argument("--batch", type=int, default=60)
    c = sub.add_parser("case-packets")
    for name in ("--template", "--subcauses", "--pages", "--salt", "--out"):
        c.add_argument(name, required=True)
    s = sub.add_parser("stage")
    for name in ("--out", "--packet", "--workspace"):
        s.add_argument(name, required=True)
    k = sub.add_parser("collect")
    for name in ("--out", "--packet", "--workspace", "--model", "--antigravity-version"):
        k.add_argument(name, required=True)
    k.add_argument("--void", metavar="REASON")
    k.add_argument("--model-change", action="store_true")
    r = sub.add_parser("reject")
    for name in ("--out", "--packet", "--reason"):
        r.add_argument(name, required=True)
    args = ap.parse_args()
    {"audit-packets": audit_packets, "case-packets": case_packets, "stage": stage,
     "collect": collect, "reject": reject}[args.cmd](args)


if __name__ == "__main__":
    main()
