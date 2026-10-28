"""Plan 23 amendment 1, Step 0: build the pre-coder extract, `23-am1-precoder-extract.md`
(template Section 1; decision sheet B21, B22, A19, C8 Correction 2).

Reads only two repository files, the register `23-am1-register-design-and-controls.md` and the
design-text file `23-am1-design-text-94c049d.md`, both next to this script, and writes the
extract next to them. No model, network, git or app import. Every edit of register text is an
exact replacement that must apply exactly once, or the build stops. The edits remove run counts,
incidence figures and other run observations (A19; amendment line 402), the probe-mapping quotes
and the mentions of a claims-register list the pre-coder does not have.

Usage: .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-precoder-extract.py [--check]
  without --check  writes the extract and prints its paragraph and pointer lists, characters,
                   lines and SHA-256, with the SHA-256 of the two input files.
  --check          rebuilds into a temporary file and compares its bytes with the committed
                   extract; exit status 0 when they are identical, 1 otherwise. Writes nothing
                   next to this script.

Record: 28 October 2026, ported from the pre-tag pass's working file (`build_extract.py` in the
session scratchpad) with four more cuts from the extract only, the register keeping them as
record: the two statements that the expansion generator's fallback did not occur in these runs
(sheet K2; K2.6b), the frequency clause on write-path intents (K2.6a) and the a2_r2b run
example (S.6).
"""
import hashlib
import re
import sys
import tempfile
from pathlib import Path

ART = Path(__file__).resolve().parent
REGISTER = ART / "23-am1-register-design-and-controls.md"
DESIGN_FILE = ART / "23-am1-design-text-94c049d.md"
OUT = ART / "23-am1-precoder-extract.md"
REG = REGISTER.read_text(encoding="utf-8").split("\n")
DESIGN = DESIGN_FILE.read_text(encoding="utf-8").split("\n")
AMEND = "thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def paragraphs():
    paras, i = {}, 0
    while i < len(DESIGN):
        m = re.match(r"\*\*(D\d+\.p\d+|T\.rationale)\*\* \(lines (\d+)-(\d+)\)", DESIGN[i])
        if m:
            a = DESIGN.index("```latex", i) + 1
            b = DESIGN.index("```", a)
            paras[m.group(1)] = norm(" ".join(DESIGN[a:b]))
            i = b
        i += 1
    return paras


PARAS = paragraphs()


def block(start_pred, stop_pred):
    """Lines from the first line matching start_pred up to (not including) the next matching stop_pred."""
    s = next(i for i, l in enumerate(REG) if start_pred(l))
    e = next(i for i in range(s + 1, len(REG)) if stop_pred(REG[i]))
    return REG[s:e]


def heading_block(head, level):
    """A section from its heading to the next heading of the same or a higher level."""
    marks = "#" * level
    def stop(l):
        m = re.match(r"(#+) ", l)
        return bool(m) and len(m.group(1)) <= level or l == "---"
    return block(lambda l: l == f"{marks} {head}" or l.startswith(f"{marks} {head} ") or l.startswith(f"{marks} {head}\t"), stop)


def replace_once(text, old, new, where):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{where}: {n} occurrences of {old[:90]!r}")
    return text.replace(old, new)


def shorten(text):
    text = re.sub(r"`" + re.escape(AMEND) + r":(\d+)`", r"amendment line \1", text)
    return re.sub(r"(?m)(^- |^   - |\. )amendment line", r"\1Amendment line", text)


# ---------------- sheets ----------------

SHEETS = {
    "E": "Sheet E: extraction (admission and extraction)",
    "K1": "Sheet K1: key assignment at extraction",
    "K2": "Sheet K2: key resolution and expansion",
    "S": "Sheet S: state rules (with A2's contracts and support check)",
    "R": "Sheet R: reading",
}

# Edits of the sheets as signed: run counts, incidence figures, probe-mapping quotes (A19, template
# point 18) and the two mentions of a claims-register list the pre-coder does not have.
SHEET_EDITS = {
    "E": [
        ('   - Mapping, amendment line 272: "implementation choice at extraction. The sub-cause is registry-conditioned extraction, or out-of-domain examples."\n', ""),
        ('   - Mapping, amendment line 278: "caused at extraction, sub-cause registry-conditioned extraction, class **unclear** (possible implementation)."\n', ""),
        ("the empty-registry sentinel at meeting a, 116–166 keys at meetings b–d (E.6, How the registry enters)", "the empty-registry sentinel at meeting a (E.6, How the registry enters)"),
        ("the neutral examples of the probe note in place of the AMI role examples. Mapping as for cause 1 (line 272).", "the neutral examples of the probe note in place of the AMI role examples."),
        ('- Model-limited needs probe (i)(d), amendment line 279: "(d) recovered, and (b), (b2) and (c) not recovered."', "- Model-limited needs probe (i)(d)."),
    ],
    "K1": [
        ('   - Mapping, amendment line 276: "implementation choice at key assignment at extraction, sub-cause registry-conditioned hinting."\n', ""),
        ("takes the joint condition (line 258; mapping lines 274–275).", "takes the joint condition (line 258)."),
        ("The model also writes the literal key `null`; in a1_r2, 31 conflict rows record that no concept definition exists for it (K1.6).", "The model also writes the literal key `null`; conflict rows record that no concept definition exists for it (K1.6)."),
        ("and none exists in the nine runs, because", "and none exists in these runs, because"),
    ],
    "K2": [
        ('   - Mapping, amendment line 273: "only where the offline check shows the fitting key was missing from the recorded prompt; otherwise the sub-cause is set on the page, within key resolution."\n', ""),
        (", behind 41 of the 42 rule-based merges in a0_r1 and 38 of 38 in a1_r2 (K2.6b, step 1;", " (K2.6b, step 1;"),
        ("(K2.6c; 0–8 accept-error review records per run, from 0–2 distinct proposals per run, each holding one parked claim; no listed cause, left to the pilot)", "(K2.6c; no listed cause, left to the pilot)"),
        ("and none exists in the nine runs, because", "and none exists in these runs, because"),
        (" Its silent fallback to rules did not occur in these runs (K2.6b).", ""),
    ],
    "S": [
        ("every key in the nine runs is scalar.", "every key in these runs is scalar."),
        ("  - Only 313 of 534 a2_r1 claims carry a recorded verdict (S.6).\n", ""),
        ("(the affirmation check: the sentence on negating the current value, which is on the claims register's R-4 list, and the legacy-policy sentence)", "(the affirmation check: the sentence on negating the current value, and the legacy-policy sentence)"),
        ("The sentence of D3.p3 on negating the current value is a commitment but is on R-4's list, so it is not listed.", "The sentence of D3.p3 on negating the current value is a commitment, but it is a disclosed limitation here (above), so it is not listed."),
    ],
    "R": [
        ('Mapping, amendment line 277: "implementation choice at reading, sub-cause the question-time shortlist excluded the holding key."', ""),
        ("question resolution through `_prompt_registry`, 8–177 keys listed per call (R.6)", "question resolution through `_prompt_registry` (R.6)"),
    ],
}


def sheet_text(key):
    lines = block(lambda l: l == f"### {SHEETS[key]}", lambda l: l == "---")
    text = shorten("\n".join(lines).rstrip("\n") + "\n")
    for old, new in SHEET_EDITS[key]:
        text = replace_once(text, old, new, f"sheet {key}")
    text = text.replace("Decided by: probe (iii), re-resolution with the unpruned registry. \n", "Decided by: probe (iii), re-resolution with the unpruned registry.\n")
    return add_ids(key, text)


def add_ids(key, text):
    out, mode, n_cause, n_entry = [], None, 0, 0
    for line in text.split("\n"):
        if line.startswith("### Sheet"):
            line = "## " + line[4:]
        if line.startswith("**Candidate causes listed by the amendment**"):
            mode = "cause"
        elif line.startswith("**Further implementation entries"):
            mode = "entry"
        elif line.startswith("**A2's contracts**"):
            mode = "contract"
        elif line.startswith("**") or line.startswith("## "):
            mode = None
        m = re.match(r"(\d)\. (.*)", line)
        if mode == "cause" and m:
            n_cause += 1
            assert int(m.group(1)) == n_cause, line
            line = f"- [{key}-cause-{n_cause}] {m.group(2)}"
        elif mode == "entry" and line.startswith("- "):
            n_entry += 1
            line = f"- [{key}-entry-{n_entry}] {line[2:]}"
        elif mode == "contract" and re.match(r"- (Support check|Type check|Same-meeting conflict)", line):
            n_entry += 1
            line = f"- [{key}-entry-{n_entry}] {line[2:]}"
        out.append(line)
    return "\n".join(out)


# ---------------- quotable lists and tags ----------------

QUOTE = re.compile(r'"(.*?)"(?= "| \(|$)')
TAG = re.compile(r"\(([TCBLE](?:, [TCBLE])*)\) ")


def quotable(sheet):
    """{pid: [(sentence, list)]} from the sheet's '94c049d text a page may quote' block."""
    out, lst = {}, None
    on = False
    for line in sheet.split("\n"):
        if line.startswith("**94c049d text a page may quote**"):
            on = True
            continue
        if not on:
            continue
        if line.startswith("**Retrospective"):
            break
        if line.startswith("- For architectural weakness (C)"):
            lst = "C"
        elif line.startswith("- For a trade-off (B)"):
            lst = "B"
        elif line.startswith("- For WD cases"):
            lst = "WD"
        elif line.startswith("- "):
            lst = None
        m = re.match(r"  - \*\*(D\d\.p\d|T\.rationale)\*\* \(([BC](?:, [BC])?)\) (.*)", line)
        if m and lst:
            for q in QUOTE.findall(m.group(3)):
                out.setdefault(m.group(1), []).append((q, lst if lst != "WD" else "WD, " + m.group(2)))
    return out


def register_tags():
    """{pid: [(tag, quote)]} from the register's design-entry sections (A.2 ... R.2, X.1)."""
    out = {}
    for head in ("A.2", "E.2", "K1.2", "K2.2", "S.2", "R.2", "X.1"):
        for line in heading_block(head, 3):
            m = re.match(r"- \*\*(D\d\.p\d|T\.rationale)\*\* (.*)", line)
            if not m:
                continue
            rest, tag = m.group(2), None
            pos = 0
            while pos < len(rest):
                t = TAG.match(rest, pos)
                if t:
                    tag = t.group(1)
                    pos = t.end()
                    continue
                q = re.compile(r'"(.*?)"(?= "| \(|$)').match(rest, pos)
                if q:
                    out.setdefault(m.group(1), []).append((tag, q.group(1)))
                    pos = q.end()
                    while pos < len(rest) and rest[pos] == " ":
                        pos += 1
                    continue
                break
    return out


REGTAGS = register_tags()


def split_sentences(pid, text):
    text = text.strip()
    if not text:
        return []
    if pid == "T.rationale":
        parts = re.split(r"(?<=\\\\) ", text)
    else:
        parts = re.split(r"(?<=[.!?])\s+(?=[A-Z`\\$(])", text)
    return [p.strip() for p in parts if p.strip()]


def tagged(pid, listed):
    """The paragraph as (tag, sentence) pairs: the sheet's listed sentences keep their list's tag."""
    para = PARAS[pid]
    spans = []
    for q, lst in listed:
        i = para.find(q)
        if i < 0:
            raise SystemExit(f"{pid}: listed sentence not in the paragraph: {q[:70]!r}")
        if para.find(q, i + 1) >= 0:
            raise SystemExit(f"{pid}: listed sentence occurs twice: {q[:70]!r}")
        spans.append((i, i + len(q), lst))
    spans.sort()
    # WD: D4.p5's sentences are listed under B and C as well; keep the B/C tag of each.
    merged = []
    for s in spans:
        if merged and s[0] < merged[-1][1]:
            if (s[0], s[1]) == merged[-1][:2]:
                continue
            raise SystemExit(f"{pid}: overlapping listed sentences")
        merged.append(s)
    out, pos = [], 0
    l_quotes = [q for t, q in REGTAGS.get(pid, []) if t and "L" in t.split(", ") and "C" not in t.split(", ")]
    def gap(t):
        for s in split_sentences(pid, t):
            out.append(("L" if any(s in q or q in s for q in l_quotes) else "—", s))
    for a, b, tag in merged:
        gap(para[pos:a])
        out.append((tag, para[a:b]))
        pos = b
    gap(para[pos:])
    return out


WD_TAGS = None


def paragraph_section(key, sheet, listed):
    pids = []
    for m in re.finditer(r"\b(D[1-9]\.p\d|T\.rationale)\b", sheet):
        if m.group(1) not in pids:
            pids.append(m.group(1))
    pids.sort(key=lambda p: (p == "T.rationale", p))
    lines = [f"### Sheet {key}: the 94c049d paragraphs this sheet names", ""]
    for pid in pids:
        lst = listed.get(pid, [])
        # A WD-list sentence counts under its own tag on sheet E (B or C); keep one entry per sentence.
        seen, uniq = set(), []
        cb = {q for q, l in lst if l in ("B", "C")}
        for q, l in lst:
            if l.startswith("WD") and q in cb:
                continue
            if q not in seen:
                seen.add(q)
                uniq.append((q, l))
        lines.append(f"**{pid}**")
        for tag, s in tagged(pid, uniq):
            lines.append(f'- ({tag}) "{s}"')
        lines.append("")
    return "\n".join(lines), pids


# ---------------- requirements ----------------

REQ_SECTIONS = ["A.4", "E.4", "K1.4", "K2.4", "S.4", "R.4", "X.2"]


def requirements():
    req = {}
    for head in REQ_SECTIONS:
        for line in heading_block(head, 3):
            m = re.match(r"- ([A-Z][A-Z0-9]*-C\d+)\. (.*)", line)
            if m:
                req[m.group(1)] = m.group(2)
    return req


REQ = requirements()


def expand(spec):
    """'A-C1 to A-C4' -> [A-C1..A-C4]."""
    m = re.match(r"([A-Z][A-Z0-9]*)-C(\d+) to \1-C(\d+)$", spec)
    if m:
        return [f"{m.group(1)}-C{n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)]
    return [spec]


REQ_IDS = {
    "E": ["A-C1", "A-C2", "A-C3", "A-C4", "A-C6", "A-C7", *expand("E-C1 to E-C5"), "X-C1", "X-C3"],
    "K1": [*expand("K1-C1 to K1-C3"), "X-C2"],
    "K2": [*expand("K2-C1 to K2-C6"), "X-C1", "X-C2"],
    "S": [*expand("S-C1 to S-C18"), "X-C1", "X-C2"],
    "R": [*expand("R-C1 to R-C9")],
}
REQ_NAMED_NOT_ITEMS = {"E": ["A-C5"]}


def requirement_section(key):
    lines = [f"### Sheet {key}: the conformance requirements this sheet names", "",
             "Each is a checklist item of this sheet, under its id."]
    for rid in REQ_IDS[key]:
        lines.append(f"- [{rid}] {REQ[rid]}")
    for rid in REQ_NAMED_NOT_ITEMS.get(key, []):
        lines += ["", f"Named on the sheet, but not a checklist item (the sheet's conformance line says why):",
                  f"- {rid}. {REQ[rid]}"]
    if key == "S":
        lim = heading_block("S.4", 3)
        s = lim.index(next(l for l in lim if l.startswith("Disclosed limitations (listed so a coder")))
        e = lim.index(next(l for l in lim if l.startswith("Stated benefits and costs:")))
        lines += ["", "The disclosed limitations that the sheet says are listed in S.4 (they are not checklist items):"]
        lines += [l for l in lim[s + 1:e] if l.startswith("- ")]
    return "\n".join(lines) + "\n"


# ---------------- implementation entries ----------------

IMPL_EDITS = {
    "E.6": [
        ("Session check: none of them occurs in any EL2020 span (the 135 gatekeeper inputs of a1_r2 cover every span), and the claims a1_r2 extracted with predicate `owns` carry values such as `PERSON14`.",
         "Session check: none of them occurs in any EL2020 span, and the claims extracted with predicate `owns` carry values such as `PERSON14`."),
        ("  - Size, from the traces: meeting a sends the sentinel (system message 2,489 characters). Meetings b–d list 116–166 keys (36,792–49,928 characters).\n", ""),
        (' Traces: 0 such calls at meeting b, 1–2 at c, 4–9 at d per run ("Ex repeat").', ""),
        (" Code-derived system template hash `daf30b70d954…` (3,516 characters with the placeholder).", " Code-derived system template hash `daf30b70d954…`."),
    ],
    "K1.6": [
        ('In a1_r2, 31 conflict rows give "Stage-23 repair (bug 5)', 'Conflict rows then give "Stage-23 repair (bug 5)'),
    ],
    "K2.6": [
        (" Write-path calls, totals per arm over its three runs: A0 711, A1 806, A2 945 (read path in R).", " Read path in R."),
        ("Example questions are present on every minted key (129 of 129 to 177 of 177 keys per run, `state.json`).", "Example questions are present on every minted key (`state.json`)."),
        ("no key in the nine runs has any", "no key in these runs has any"),
        ('  - Size, from the traces ("Registry carried per meeting"): at meeting a every write-path call lists no key (122–143 calls per run; the registry is empty, so the model cannot return a key and every claim goes to expansion). At meetings b–d, calls list 1–166 keys, with medians of 13–38. In 1–11 calls per meeting the whole registry was listed.',
         "  - At meeting a every write-path call lists no key (the registry is empty, so the model cannot return a key and every claim goes to expansion)."),
        ("   - Session check (not kept): 41 of the 42 rule-based merges in a0_r1, and 38 of 38 in a1_r2, had an alias, label or dotted name of the target key inside the full span (spans from `trace.json`, proposals from `state.json`). The remaining one in a0_r1 is the semantic merge counted in step 3.\n", ""),
        ("   - Rule-based merges per run (`state.json`, `generation_method: rule_based`, merged): 12–56. They include the semantic merges into a key of step 3, which use the same recommendation record.\n", ""),
        ("merged by the harness (K2.6c); `state.json` shows 0–10 such merges per run (`generation_method: llm_assisted`, merged).", "merged by the harness (K2.6c)."),
        ("   - Calls, totals per arm over its three runs: A0 463, A1 512, A2 535, all `llm_assisted`, all served by gpt-5.4-mini-2026-03-17.", "   - Calls: all `llm_assisted`, all served by gpt-5.4-mini-2026-03-17."),
        ("Code-derived hash `f570f53ad992…` (1,412 characters).", "Code-derived hash `f570f53ad992…`."),
        (" `run.log` counts (progress lines starting `⊕ dedup`): 5–11 proposal reuses and 0–2 key merges per run.", ""),
        ("- **From the `coldstart.json` expansion logs:** the harness reviewer rejected no proposal in any run. Accept errors were 0–8 review records per run, all `STATE_KEY_INVALID_FORMAT` on keys of five or more segments.",
         "- **From the `coldstart.json` expansion logs:** accept errors were all `STATE_KEY_INVALID_FORMAT` on keys of five or more segments."),
        ("  - The records count reviews, not proposals: a stuck proposal is reviewed again at every meeting. They come from 0–2 distinct proposals per run: a0_r1, a0_r3 and a1_r3 none; a0_r2, a1_r1, a1_r2 and a2_r1 4 records from 1 proposal; a2_r2b 7 records from 2; a2_r3 8 records from 2.",
         "  - The records count reviews, not proposals: a stuck proposal is reviewed again at every meeting."),
        ("  - In `state.json`, each such pending proposal holds one parked claim and has released none.\n", ""),
        (' No `state.json` holds a rule-based description ("Auto-proposed (rule-based)"), so no fallback happened (session check).', ""),
        ('; write-path calls carry mostly `current_state_question` ("Dynamic fields with a fixed vocabulary").', "."),
    ],
    "S.6": [
        ('a status phrase (l.163-172; values sent: "firmly decided" 621, "proposed or considered" 181, "rejected / ruled out" 85, "tentative" 23).', "a status phrase (l.163-172)."),
        ('  - Gloss: under `filing_support_check`, only 313 of 534 a2_r1 claims carry a recorded verdict (amendment, "Already read").\n', ""),
        ("no canonical_match step is recorded in the nine traces.", "no canonical_match step is recorded in the traces."),
        ('human review required." 3 times in a0_r1, 19 in a1_r2, 71 in a2_r1.', 'human review required."'),
        ("(cleared at `registry_expansion_eval.py:446`; 0 keys with canonical values in all nine `state.json` files).", "(cleared at `registry_expansion_eval.py:446`)."),
        ("    - Run example: in a2_r2b, `project.repository.destination` holds both `GitHub repository` and `Github repository` as positive asserted claim values (`state.json`).\n", ""),
        (" and `supported` (`3320375:app/services/conflict_service.py:752`); 286–313 calls per A2 run).", " and `supported` (`3320375:app/services/conflict_service.py:752`))."),
        ("(`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`); 45–53 filing_type_check records per A2 run, none with a model).", "(`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`); no model call)."),
    ],
    "R.6": [
        (" 105 calls per run (315 per arm).", ""),
        (' Keys listed: 8–177 per call; the whole registry in 0–3 calls per meeting ("Registry carried per meeting", R columns).', ""),
        ("seam `question_answering_grounding`, 98 calls per run.", "seam `question_answering_grounding`."),
        ("    - Review check (27 October; scratch, not kept): in a1_r2, 0 of 400 resolver outputs carry candidate keys, and in 25 of 105 question traces of `state.json` the resolved primary keys include a key the resolver returned only as supporting.\n", ""),
        ("    - Minted keys of that form (`state.json`): one in a0_r3, two in a1_r3, one in a2_r1.\n", ""),
    ],
    "X.4": [
        ("- Gloss: no repair changes a prompt text, which the one-variant result confirms.", "- Gloss: no repair changes a prompt text."),
        (" (149 steps over three runs)", ""),
        ("one call per claim, cached on the claim: 313, 311 and 286 calls in a2_r1, a2_r2b, a2_r3", "one call per claim, cached on the claim"),
    ],
}

IMPL_HEADS = {"A.6": "A.6 Implementation entries", "E.6": "E.6 Implementation entries", "K1.6": "K1.6 Implementation entries",
              "K2.6": "K2.6 Implementation entries", "S.6": "S.6 Implementation entries", "R.6": "R.6 Implementation entries",
              "X.4": "X.4 Arm-specific implementation across components"}


def impl_text(sec):
    lines = heading_block(IMPL_HEADS[sec], 3)
    text = "\n".join(lines).rstrip("\n") + "\n"
    text = shorten(text)
    for old, new in IMPL_EDITS.get(sec, []):
        text = replace_once(text, old, new, sec)
    return text


def impl_sub(sec, sub):
    """A #### subsection of an implementation section, after the edits."""
    text = impl_text(sec).split("\n")
    s = next(i for i, l in enumerate(text) if l.startswith("#### ") and l[5:].startswith(sub))
    e = next((i for i in range(s + 1, len(text)) if text[i].startswith("#### ") or text[i].startswith("### ")), len(text))
    return "\n".join(text[s:e]).rstrip("\n") + "\n"


def demote(text, sec, sub=None):
    """Headings one level down, so that each sits under its sheet."""
    out = []
    for l in text.split("\n"):
        if l.startswith("### "):
            l = "#### " + l[4:]
        elif l.startswith("#### "):
            l = "##### " + l[5:]
        out.append(l)
    if sub:
        out.insert(0, f"#### {IMPL_HEADS[sec]} (part)")
        out.insert(1, "")
    return "\n".join(out)


# What each sheet points to, at the granularity of a #### subsection where the sheet names one
# and the section is long (K2.6 on sheets K1 and R); otherwise the whole section.
POINTS = {
    "E": [("A.6", None), ("E.6", None), ("K1.6", None), ("X.4", None)],
    "K1": [("E.6", None), ("K1.6", None), ("K2.6", "K2.6c"), ("X.4", None)],
    "K2": [("K2.6", None), ("R.6", None), ("X.4", None)],
    "S": [("E.6", None), ("K1.6", None), ("S.6", None), ("X.4", None)],
    "R": [("K2.6", "K2.6a"), ("K2.6", "Parameters"), ("R.6", None)],
}


def pointer_check(key, sheet):
    """Every implementation pointer on the sheet is covered by POINTS."""
    found = set(re.findall(r"\b(A\.6|E\.6|K1\.6|K2\.6[abc]?|S\.6|R\.6|X\.4)\b", sheet))
    have = {s for s, _ in POINTS[key]} | {sub for _, sub in POINTS[key] if sub and sub.startswith("K2.6")}
    missing = set()
    for f in found:
        base = f[:4] if f.startswith("K2.6") else f
        if f.startswith("K2.6") and len(f) == 5:
            if not (f in have or ("K2.6", None) in POINTS[key]):
                missing.add(f)
        elif base not in {s for s, _ in POINTS[key]}:
            missing.add(f)
    return found, missing


def impl_section(key):
    parts = [f"### Sheet {key}: the implementation entries this sheet points to", ""]
    for sec, sub in POINTS[key]:
        if sub:
            parts.append(demote(impl_sub(sec, sub), sec, sub))
        else:
            parts.append(demote(impl_text(sec), sec))
    return "\n".join(parts)


INTRO = """# The register sheets: pre-coder extract

This text holds the five register sheets of the design-and-controls register, one per caused-at boundary: extraction (E), key assignment at extraction (K1), key resolution and expansion (K2), state rules (S) and reading (R). After each sheet come three parts: the text of every 94c049d paragraph the sheet names, sentence by sentence; the conformance requirements the sheet names; and the register's implementation entries the sheet points to.

How to read it:
- "Amendment line N" cites line N of the study plan quoted in Parts B and D of the instructions.
- A pointer such as (E.6) or (K2.6c) names the register section that holds an entry. The sections that a sheet points to for implementation entries follow the sheet. Pointers to other sections, such as (E.3), only give the source of a gloss; those sections are not part of this text. A pointer is not a finding.
- Checklist items carry an id in square brackets, one item per line: candidate causes ([E-cause-1], ...), further implementation entries ([E-entry-1], ...), and conformance requirements under their register ids ([E-C1], ...). The conformance requirements are listed after each sheet. An item's text is the rest of its line after the id. Indented lines under an item are notes on it, not items.
- Each sheet lists, under "94c049d text a page may quote", the only sentences that may ground a design code on that sheet: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. A sentence the register tags (B, C) counts under the list it appears in on that sheet. The paragraphs after the sheet repeat each listed sentence with that tag. Their other sentences are marked (L), a disclosed limitation, or (—), not listed on this sheet. Neither may ground a design code.
- For WD cases (surfaced at `carried:claims_without_the_value`), sheet E lists D4.p5 whole: any sentence of D4.p5 may be quoted, whatever its tag (amendment line 355). After sheet E these sentences are marked (WD, B) or (WD, C). On sheet E they ground nothing in any other case.
- Text marked Gloss is the register's own reading, not design text.
"""


def build():
    out = [INTRO]
    report = []
    for key in SHEETS:
        sheet = sheet_text(key)
        listed = quotable(sheet)
        found, missing = pointer_check(key, sheet)
        if missing:
            raise SystemExit(f"sheet {key}: implementation pointers not covered: {sorted(missing)}")
        para_sec, pids = paragraph_section(key, sheet, listed)
        out += ["---", "", sheet.rstrip("\n"), "", para_sec.rstrip("\n"), "", requirement_section(key).rstrip("\n"), "",
                impl_section(key).rstrip("\n"), ""]
        report.append((key, pids, sorted(found)))
    text = "\n".join(out).rstrip("\n") + "\n"
    return text, report


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(argv):
    if argv not in ([], ["--check"]):
        raise SystemExit("usage: 23-am1-precoder-extract.py [--check]")
    text, report = build()
    if argv == ["--check"]:
        with tempfile.TemporaryDirectory() as tmp:
            rebuilt = Path(tmp) / OUT.name
            rebuilt.write_text(text, encoding="utf-8")
            same = OUT.exists() and rebuilt.read_bytes() == OUT.read_bytes()
        print(("identical: " if same else "DIFFERS: ") + f"rebuilt extract sha256 {hashlib.sha256(text.encode()).hexdigest()}, "
              f"committed {sha(OUT) if OUT.exists() else 'missing'}")
        return 0 if same else 1
    OUT.write_text(text, encoding="utf-8")
    for key, pids, found in report:
        print(key, "paragraphs:", " ".join(pids))
        print(key, "impl pointers:", " ".join(found))
    print(f"{OUT.name}: {len(text)} characters, {text.count(chr(10))} lines, sha256 {sha(OUT)}")
    print(f"{REGISTER.name}: sha256 {sha(REGISTER)}")
    print(f"{DESIGN_FILE.name}: sha256 {sha(DESIGN_FILE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
