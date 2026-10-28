"""Plan 23 amendment 1, Step 0: re-derive the package's checks (decision sheet B3).

One script for the checks that were scratch work before the tag. It reads only git objects
(`git show`) and files under the repository root. It makes no model, embedding, network or API
call, never opens `.env`, and changes no git state. Nothing in the repository is written: every
output that a re-run produces goes to a temporary directory that is removed afterwards.

Checks, in order (each prints PASS, FAIL or SKIP with its reason; one item prints CLOSED):

 1. template   Prompt and schema text of `23-am1-precoder-template.md` (Section 1): their SHA-256
               and character count as recorded there; the three placeholders once each; the
               extract's SHA-256, characters and lines; the filled prompt ({REGISTER_SHEET}
               literally replaced by the whole extract file) and its SHA-256; the schema parses;
               `23-am1-precoder-extract.py --check` rebuilds the extract byte-identical; the
               register and design-text SHA-256 that Section 1 records as the extract's inputs
               equal those files.
 2. schema     The template's schema test: built-in valid and invalid records, checked with the
               schema checker of `23-am1-v4.py` (the validator the package uses).
 3. register   `23-am1-check-register.py` on the design-and-controls register (subprocess).
 4. code       What the register cites and its checker does not cover (register decision 10):
               the code-derived prompt hashes at 3320375 (expansion generator, WD extraction
               template, judge, RAG generator); each evaluated static text in
               `23-am1-prompts-evaluated.md` against its hash and the register's prompt table, and
               the four system texts and the extraction text against the code constants at
               3320375; the schema-strictness checks; the alias-merge check (41 of 42 rule-based
               merges in a0_r1, 38 of 38 in a1_r2). The merge's completeness check is reported as
               CLOSED: a one-time historical check, its result in the register's Checks section;
               its inputs (the two pre-merge parts) were never in the repository.
 5. claims     The claims register's quote check (ported from the scratch `qcheck_claims.py`,
               logic unchanged). Exactly one error is expected and named by its text: the dated
               history line that quotes the decision sheet's former C1 wording. None, or more than
               one, is a failure.
 6. sheet      The decision sheet's quote check (ported from the scratch `qcheck.py`): every
               straight-quoted string of six or more characters occurs in one of its sources.
               Two sources were scratch copies of git objects; they are read from git here.
 7. ids        Id resolution across all `23-am1-*.md` (ported from the scratch `ids.py`).
 8. probe      The probe note's substitution (Part 1, section 1.4): the evaluated static part
               rebuilt from the 3320375 constants and compared with every recorded extraction
               call of the nine runs; both static hashes, lengths and the hashes with the
               registry placeholder; the (b2) text printed in the note; the response_format hash;
               and the overlap check of section 1.3 (ported from `compute.py`, `overlap.py`,
               `overlap_reg.py`).
 9. audit      `23-am1-audit-list.py` re-run with its output redirected to a temporary file; the
               bytes must equal the committed `23-am1-audit-list.json`.
10. hashes     Every SHA-256 in the index's file table and the decision sheet's file table
               against the file on disk, the index's template prompt and schema hashes, and the
               run archive's hash where the archive exists. A mismatch is a failure; the output
               names the files modified today, whose rows are refreshed last before the tag.
               Completeness: every `23-am1-*.md`, `.py` and `.json` file next to this script, and
               the amendment, must have a row in the index's file table ("What you sign"); a file
               without one is a failure. Exempt: the index itself and the `23-am1-records` folder.
11. manifest   `23-am1-run-manifest.py` (subprocess, no `--zip`).

Run files under `data/ami_eval/a1_smoke/` are gitignored but lie inside the repository; checks
that need them are skipped, with the reason, when they are absent.

Usage: .venv/bin/python -I -B thesis/notes/thesis_completion/artifacts/23-am1-check-package.py [--verbose]
Exit status 0 when no check fails, 1 otherwise (SKIP and CLOSED are not failures).
"""

import ast
import contextlib
import datetime
import glob
import hashlib
import importlib.util
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile

import yaml

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RUNS = ROOT / "data/ami_eval/a1_smoke"
CODE = "3320375"  # A0 and A1 ran at 3320375 (amendment, run manifest)
THESIS = "b4d6b6c"  # the thesis and notes commit the claims register quotes
VERBOSE = "--verbose" in sys.argv
PY = [sys.executable, "-I", "-B"]

TEMPLATE = HERE / "23-am1-precoder-template.md"
EXTRACT = HERE / "23-am1-precoder-extract.md"
EXTRACT_BUILDER = "23-am1-precoder-extract.py"
DESIGN_TEXT = HERE / "23-am1-design-text-94c049d.md"
REGISTER = HERE / "23-am1-register-design-and-controls.md"
CLAIMS = HERE / "23-am1-register-claims.md"
SHEET = HERE / "23-am1-decisions.md"
PROBE = HERE / "23-am1-probe-note.md"
INDEX = HERE / "23-am1-step0-index.md"
PROMPTS = HERE / "23-am1-prompts-evaluated.md"
AMENDMENT = HERE / "23-plan-amendment-1-ceilings-and-root-cause.md"

NINE_RUNS = {  # the evaluated EL2020 PM runs, in the probe note's order (section 1.1)
    "a0_r1": "el2020_batch_20261022T214813Z/a0_r1",
    "a0_r2": "el2020_batch_20261022T214813Z/a0_r2",
    "a0_r3": "el2020_batch_20261022T214813Z/a0_r3",
    "a1_r1": "el2020_a1_20261022T211107Z",
    "a1_r2": "el2020_batch_20261022T214813Z/a1_r2",
    "a1_r3": "el2020_batch_20261022T214813Z/a1_r3",
    "a2_r1": "el2020_a2_rag_20261023T061545Z/a2_r1",
    "a2_r2b": "el2020_a2_rag_20261023T061545Z/a2_r2b",
    "a2_r3": "el2020_a2_rag_20261023T061545Z/a2_r3",
}
SEP = "\n\nRegistry of state keys (the domain definition):\n"
REGISTRY_PLACEHOLDER = "⟦registry⟧"  # convention of 23-am1-prompts-evaluated.md

RESULTS = []


def report(check, status, text, details=()):
    RESULTS.append((check, status, text))
    print(f"[{status}] {check}: {text}")
    for d in details:
        print(f"         {d}")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


_git = {}


def git_show(commit, path):
    """Text of path at commit, or None."""
    key = (commit, path)
    if key not in _git:
        r = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, capture_output=True, text=True)
        _git[key] = r.stdout if r.returncode == 0 else None
    return _git[key]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def str_constants(source):
    """Module-level string constants of a Python source, evaluated from the AST (no import)."""
    env = {}

    def ev(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return ev(node.left) + ev(node.right)
        if isinstance(node, ast.Name) and node.id in env:
            return env[node.id]
        raise ValueError("not a string constant")

    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name, value = node.targets[0].id, node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value is not None:
            name, value = node.target.id, node.value
        else:
            continue
        try:
            env[name] = ev(value)
        except ValueError:
            pass
    return env


def run_dir(rel):
    return RUNS / rel / "artifacts"


def runs_present():
    return all(run_dir(rel).is_dir() for rel in NINE_RUNS.values())


def one_file(rel, suffix):
    found = sorted(run_dir(rel).glob(f"*.{suffix}"))
    if len(found) != 1:
        raise SystemExit(f"{rel}: expected one *.{suffix}, found {len(found)}")
    return found[0]


_traces = {}


def trace(run):
    if run not in _traces:
        _traces[run] = json.loads(one_file(NINE_RUNS[run], "trace.json").read_text())
    return _traces[run]


def state(run):
    return json.loads(one_file(NINE_RUNS[run], "state.json").read_text())


# ---------------------------------------------------------------------------------------------
# 1. Template hashes (template Section 1)
# ---------------------------------------------------------------------------------------------

def template_texts():
    lines = TEMPLATE.read_text().split("\n")
    s = lines.index("~~~~ prompt")
    e = lines.index("~~~~", s + 1)
    pl = lines[s + 1 : e]
    prompt = "".join(line + "\n" for line in pl)
    a = pl.index("BEGIN OUTPUT SCHEMA")
    b = pl.index("END OUTPUT SCHEMA")
    schema = "".join(line + "\n" for line in pl[a + 1 : b])
    return prompt, schema


def num(s):
    return int(s.replace(",", ""))


def check_template():
    text = TEMPLATE.read_text()
    sec1 = text.split("\n## 1. Inputs and assembly\n")[1].split("\n## 2. The prompt\n")[0]
    prompt, schema = template_texts()
    fails, notes = [], []

    m = re.search(r"SHA-256 of that text, before substitution: `([0-9a-f]{64})` \(([\d,]+) characters", sec1)
    if not m:
        fails.append("Section 1 records no prompt hash")
    else:
        notes.append(f"prompt {sha(prompt)} ({len(prompt):,} characters)")
        if m.group(1) != sha(prompt):
            fails.append(f"prompt hash {sha(prompt)} differs from Section 1 {m.group(1)}")
        if num(m.group(2)) != len(prompt):
            fails.append(f"prompt has {len(prompt):,} characters, Section 1 says {m.group(2)}")
    m = re.search(r"SHA-256 of the schema text \([^)]*\): `([0-9a-f]{64})`", sec1)
    if not m:
        fails.append("Section 1 records no schema hash")
    else:
        notes.append(f"schema {sha(schema)}")
        if m.group(1) != sha(schema):
            fails.append(f"schema hash {sha(schema)} differs from Section 1 {m.group(1)}")
    for ph in ("{REGISTER_SHEET}", "{SUBCAUSES}", "{CASE_PAGE}"):
        if prompt.count(ph) != 1:
            fails.append(f"placeholder {ph} occurs {prompt.count(ph)} times")
    try:
        json.loads(schema)
    except json.JSONDecodeError as exc:
        fails.append(f"schema text is not JSON: {exc}")

    m = re.search(r"the extract, `23-am1-precoder-extract\.md`: SHA-256 `([0-9a-f]{64})` "
                  r"\(([\d,]+) characters, ([\d,]+) lines\)", sec1)
    if not EXTRACT.exists():
        fails.append("23-am1-precoder-extract.md is missing")
    elif not m:
        fails.append("Section 1 records no extract hash")
    else:
        ext = EXTRACT.read_text()
        n_lines = len(ext.splitlines())
        notes.append(f"extract {sha_file(EXTRACT)} ({len(ext):,} characters, {n_lines:,} lines)")
        if m.group(1) != sha_file(EXTRACT):
            fails.append(f"extract hash {sha_file(EXTRACT)} differs from Section 1 {m.group(1)}")
        if num(m.group(2)) != len(ext) or num(m.group(3)) != n_lines:
            fails.append(f"extract size {len(ext):,} characters, {n_lines:,} lines; "
                         f"Section 1 says {m.group(2)}, {m.group(3)}")
        filled = prompt.replace("{REGISTER_SHEET}", ext)
        notes.append(f"filled prompt {sha(filled)} ({len(filled):,} characters)")
        m2 = re.search(r"the filled prompt: .*?SHA-256 `([0-9a-f]{64})` \(([\d,]+) characters\)", sec1)
        if not m2:
            fails.append("Section 1 records no filled-prompt hash")
        else:
            if m2.group(1) != sha(filled):
                fails.append(f"filled-prompt hash {sha(filled)} differs from Section 1 {m2.group(1)}")
            if num(m2.group(2)) != len(filled):
                fails.append(f"filled prompt has {len(filled):,} characters, Section 1 says {m2.group(2)}")
    # the extract's inputs as Section 1 records them, and a byte-identical rebuild
    m3 = re.search(r"built from the register, `23-am1-register-design-and-controls\.md`, SHA-256 `([0-9a-f]{64})`, "
                   r"and the design-text file, `23-am1-design-text-94c049d\.md`, SHA-256 `([0-9a-f]{64})`", sec1)
    if not m3:
        fails.append("Section 1 records no register and design-text hashes for the extract")
    else:
        for path, want in ((REGISTER, m3.group(1)), (DESIGN_TEXT, m3.group(2))):
            if sha_file(path) != want:
                fails.append(f"{path.name} is {sha_file(path)[:12]}…, Section 1 records the extract built from {want[:12]}…")
        notes.append(f"extract inputs: register {m3.group(1)[:12]}…, design text {m3.group(2)[:12]}… as recorded")
    if not (HERE / EXTRACT_BUILDER).exists():
        fails.append(f"{EXTRACT_BUILDER} is missing")
    else:
        rc, out = run_script(EXTRACT_BUILDER, ["--check"])
        notes.append(f"{EXTRACT_BUILDER} --check: " + (out.strip().splitlines() or ["no output"])[-1])
        if rc != 0:
            fails.append(f"{EXTRACT_BUILDER} --check: the rebuilt extract differs from the committed one (exit {rc})")
    if fails:
        report("1 template", "FAIL", "; ".join(fails), notes)
    else:
        report("1 template", "PASS", "prompt, schema, extract and filled-prompt hashes equal Section 1; "
               "three placeholders once each; schema parses; the extract rebuilds byte-identical from the "
               "register and design text Section 1 records", notes)


# ---------------------------------------------------------------------------------------------
# 2. Schema test
# ---------------------------------------------------------------------------------------------

def base_record():
    return {
        "case_id": "case-1",
        "inputs_received": ["instructions", "register sheet", "sub-cause list", "case page"],
        "other_input": None,
        "series": "EL2020",
        "arm": "A1",
        "surfaced_at": {"step": "filed", "sub_code": "unmapped"},
        "caused_at": "key resolution and expansion",
        "caused_at_step": "resolver",
        "caused_at_is_llm_step": True,
        "caused_at_basis": "page",
        "misrouted_claims": [],
        "class": "implementation defect",
        "held": None,
        "implementation_basis": "conformance",
        "criteria_met": [],
        "phase_b_bug": None,
        "sub_cause": "a listed name",
        "proposed_sub_cause": None,
        "pending": [],
        "checklist": [{"boundary": "key resolution and expansion", "item_id": "K2-cause-1", "item": "an item",
                       "status": "counts", "basis": "a basis",
                       "evidence": {"source": "case page", "quote": "a quote"}}],
        "design_ground": [],
        "tradeoff_benefit_quote": None,
        "llm_step_argument": None,
        "retrospective_design_only": False,
        "recoverability": {"rag_outcome": "lost", "rag_bar": False, "rag_reason": None, "other_runs": "lost",
                           "other_run_bar": False, "what_differed": None, "evaluation_defect_candidate": False},
        "evidence": [{"source": "case page", "section": "trace", "quote": "a quote"}],
        "unclear_reason": None,
        "note": "",
    }


def variant(**changes):
    r = base_record()
    for k, v in changes.items():
        if v is KeyError:
            del r[k]
        else:
            r[k] = v
    return r


def schema_cases():
    design = {"implementation_basis": None, "design_ground": [{"entry": "D4.p5", "retrospective": False, "quote": "q"}]}
    valid = {
        "implementation defect, conformance": variant(),
        "architectural weakness at candidate generation, with the line-340 argument, sub_cause not applicable":
            variant(**design, **{"class": "architectural weakness", "caused_at_step": "candidate generation",
                                 "llm_step_argument": "argued from line 340", "sub_cause": "not applicable"}),
        "design or model, not separated, at candidate generation":
            variant(**{"class": "design or model, not separated", "caused_at_step": "candidate generation",
                       "implementation_basis": None}),
        "design trade-off at the alias merge, with a benefit quote":
            variant(**design, **{"class": "design trade-off", "caused_at_step": "alias merge",
                                 "caused_at_is_llm_step": False, "tradeoff_benefit_quote": "q"}),
        "conversational difficulty at the transcript":
            variant(**{"class": "conversational difficulty", "caused_at": "transcript", "caused_at_step": "",
                       "caused_at_is_llm_step": None, "implementation_basis": None}),
        "unclear, caused-at unclear, with a reason":
            variant(**{"class": "unclear", "caused_at": "unclear", "caused_at_step": "", "caused_at_is_llm_step": None,
                       "implementation_basis": None, "unclear_reason": "page does not show the path"}),
        "Phase B bug on A0":
            variant(**{"arm": "A0", "implementation_basis": "Phase B bug", "phase_b_bug": "5"}),
        "sub_cause none fits, with a proposal":
            variant(**{"sub_cause": "none fits", "proposed_sub_cause": "a new name"}),
    }
    invalid = {
        "class model-limited (held constant)": variant(**{"class": "model-limited (held constant)", "implementation_basis": None}),
        "architectural weakness at candidate generation without the argument":
            variant(**design, **{"class": "architectural weakness", "caused_at_step": "candidate generation"}),
        "sub_cause not applicable with implementation defect": variant(sub_cause="not applicable"),
        "sub_cause not applicable with unclear":
            variant(**{"class": "unclear", "caused_at": "unclear", "caused_at_step": "", "caused_at_is_llm_step": None,
                       "implementation_basis": None, "unclear_reason": "r", "sub_cause": "not applicable"}),
        "an extra property": variant(extra_field="x"),
        "a required property missing": variant(note=KeyError),
        "caused-at extraction with the step resolver": variant(caused_at="extraction"),
        "implementation defect with no basis": variant(implementation_basis=None),
        "design trade-off with no benefit quote":
            variant(**design, **{"class": "design trade-off", "caused_at_step": "alias merge", "caused_at_is_llm_step": False}),
        "counts with evidence from the register sheet":
            variant(checklist=[{"boundary": "key resolution and expansion", "item_id": "K2-cause-1", "item": "i",
                                "status": "counts", "basis": "b",
                                "evidence": {"source": "register sheet", "quote": "q"}}]),
        "Phase B bug number on A1": variant(implementation_basis="Phase B bug", phase_b_bug="5"),
        "design or model at the gatekeeper outside admitted:ignored":
            variant(**{"class": "design or model, not separated", "caused_at": "extraction", "caused_at_step": "gatekeeper",
                       "implementation_basis": None}),
        "the LLM-step flag false at the resolver": variant(caused_at_is_llm_step=False),
        "none fits with no proposal": variant(sub_cause="none fits"),
        "note longer than 600 characters": variant(note="x" * 601),
    }
    return valid, invalid


def check_schema():
    v4path = HERE / "23-am1-v4.py"
    if not v4path.exists():
        report("2 schema", "FAIL", "23-am1-v4.py is missing")
        return
    v4 = load_module("am1_v4_for_check", v4path)
    prompt, _ = template_texts()
    try:
        schema = v4.prompt_schema(prompt)
    except Exception as exc:  # noqa: BLE001 - report any parse failure
        report("2 schema", "FAIL", f"schema not parsed from the prompt: {exc}")
        return
    valid, invalid = schema_cases()
    wrong = []
    for name, rec in valid.items():
        try:
            errs = v4.errors(rec, schema)
        except SystemExit as exc:
            wrong.append(f"valid record '{name}': checker stopped: {exc}")
            continue
        if errs:
            wrong.append(f"valid record '{name}' rejected: {errs[:3]}")
    for name, rec in invalid.items():
        if not v4.errors(rec, schema):
            wrong.append(f"invalid record '{name}' accepted")
    if wrong:
        report("2 schema", "FAIL", f"{len(wrong)} of {len(valid) + len(invalid)} records not as intended", wrong)
    else:
        report("2 schema", "PASS", f"{len(valid)} valid records accepted and {len(invalid)} invalid records "
               "rejected by the template's schema (checker of 23-am1-v4.py)")


# ---------------------------------------------------------------------------------------------
# 3. Register checker
# ---------------------------------------------------------------------------------------------

def run_script(name, args=()):
    r = subprocess.run(PY + [str(HERE / name), *args], cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def check_register():
    rc, out = run_script("23-am1-check-register.py")
    lines = [line for line in out.splitlines() if line.strip()]
    tail = lines[-8:] if not VERBOSE else lines
    report("3 register", "PASS" if rc == 0 else "FAIL", f"23-am1-check-register.py exit status {rc}", tail)


# ---------------------------------------------------------------------------------------------
# 4. Code-derived prompts, prompt-to-constant equality, strictness, alias merge (register dec. 10)
# ---------------------------------------------------------------------------------------------

def register_prompt_table():
    """{(seam, role): sha} from the register's 'Prompt hashes' table."""
    out = {}
    for m in re.finditer(r"^\| (?:`([^`]+)`( under WD)?|([\w ]+?)) \| ([\w ]+?) \| `([0-9a-f]{64})` \| ([\w-]+) \|",
                         REGISTER.read_text(), re.M):
        seam = (m.group(1) + (m.group(2) or "")) if m.group(1) else m.group(3)
        out[(seam, m.group(4))] = (m.group(5), m.group(6))
    return out


def prompts_evaluated_blocks():
    """{(seam, role): (stated sha, text)} from the full texts in 23-am1-prompts-evaluated.md."""
    lines = PROMPTS.read_text().split("\n")
    out = {}
    i = 0
    while i < len(lines):
        m = re.match(r"### `(\w+)` (system|user) `[0-9a-f]{12}`$", lines[i])
        if m:
            j = i + 1
            stated = None
            while not lines[j].startswith("```text"):
                mm = re.match(r"- SHA-256: `([0-9a-f]{64})`", lines[j])
                if mm:
                    stated = mm.group(1)
                j += 1
            k = lines.index("```", j + 1)
            out[(m.group(1), m.group(2))] = (stated, "\n".join(lines[j + 1 : k]))
            i = k
        i += 1
    return out


def extraction_constants():
    c = str_constants(git_show(CODE, "app/services/extraction_service.py"))
    static = c["EXTRACTION_BASE_INSTRUCTIONS"].replace(c["_COLLECTION_PREFERENCE"], c["_SCALAR_PREFERENCE"])
    return c, static


def schema_modules(tmp):
    """Write the 3320375 modules the schema checks need into tmp and return them imported."""
    files = ["app/__init__.py", "app/core/__init__.py", "app/core/enums.py", "app/llm/__init__.py",
             "app/llm/base.py", "app/llm/openai_llm.py", "app/llm/expansion_generator.py",
             "app/schemas/__init__.py", "app/schemas/llm_extraction.py", "app/schemas/llm_gatekeeper.py",
             "app/schemas/llm_resolution.py", "app/schemas/llm_grounding.py", "app/schemas/llm_claim_support.py"]
    for f in files:
        text = git_show(CODE, f)
        if text is None:
            raise SystemExit(f"cannot read {CODE}:{f}")
        p = pathlib.Path(tmp) / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    sys.path.insert(0, tmp)
    try:
        import importlib
        mods = {name: importlib.import_module(name) for name in (
            "app.llm.openai_llm", "app.llm.expansion_generator", "app.schemas.llm_extraction",
            "app.schemas.llm_gatekeeper", "app.schemas.llm_resolution", "app.schemas.llm_grounding",
            "app.schemas.llm_claim_support")}
    finally:
        sys.path.remove(tmp)
    return mods


def class_from_source(source, name):
    """Define one pydantic class from a module source without importing the module."""
    from typing import Literal

    from pydantic import BaseModel, ConfigDict, Field
    tree = ast.parse(source)
    node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
    ns = {"BaseModel": BaseModel, "ConfigDict": ConfigDict, "Field": Field, "Literal": Literal}
    exec(compile(ast.Module(body=[node], type_ignores=[]), f"{CODE}:{name}", "exec"), ns)  # noqa: S102
    return ns[name]


def check_code(tmp):
    table = register_prompt_table()
    fails, notes = [], []

    # 4a. code-derived hashes (register, prompt table; character counts from the implementation entries)
    mods = schema_modules(tmp)
    c, static = extraction_constants()
    wd = static
    if c["_PER_VALUE_SENTENCE"] not in wd:
        fails.append("the per-value sentence is not in the evaluated extraction instructions")
    wd = wd.replace(c["_PER_VALUE_SENTENCE"], c["_PER_DECISION_SENTENCE"]) + c["_WHOLE_DECISION_RULE"]
    src_es = git_show(CODE, "app/services/extraction_service.py")
    if repr(SEP)[1:-1] not in src_es.replace('"', "'"):
        fails.append("the registry header is not literal in extraction_service.py")
    judge = str_constants(git_show(CODE, "app/evaluation/ami/judge.py"))["JUDGE_SYSTEM_PROMPT"]
    rag = str_constants(git_show(CODE, "app/evaluation/ami/rag_components.py"))["RAG_SYSTEM_PROMPT"]
    gen = mods["app.llm.expansion_generator"].expansion_system_prompt(force_scalar=True, families=True)
    derived = {
        ("registry_expansion_generation", "system"): (gen, 1412),
        ("extraction under WD", "system template"): (wd + SEP + REGISTRY_PLACEHOLDER, 3516),
        ("judge", "system"): (judge, 1934),
        ("RAG generator", "system"): (rag, 1390),
    }
    for key, (text, n) in derived.items():
        want = table.get(key)
        got = sha(text)
        notes.append(f"{key[0]} {key[1]}: {got} ({len(text):,} characters)")
        if want is None:
            fails.append(f"register prompt table has no row for {key}")
        elif want[0] != got:
            fails.append(f"{key}: code-derived {got} differs from the register's {want[0]}")
        if len(text) != n:
            fails.append(f"{key}: {len(text):,} characters, register says {n:,}")
    # The judge row of the prompt table names the seam 'judge', the RAG row 'RAG generator'.

    # 4b. evaluated static texts: own hash, register table, code constant
    blocks = prompts_evaluated_blocks()
    consts = {
        "memory_gatekeeper": ("app/services/memory_gatekeeper_service.py", "GATEKEEPER_SYSTEM_PROMPT"),
        "state_key_resolution": ("app/services/state_key_resolution_service.py", "RESOLUTION_SYSTEM_PROMPT"),
        "question_answering_grounding": ("app/services/answer_service.py", "GROUNDING_SYSTEM_PROMPT"),
        "claim_support_check": ("app/services/cycle2_filing.py", "CLAIM_SUPPORT_SYSTEM_PROMPT"),
    }
    for (seam, role), (stated, text) in sorted(blocks.items()):
        got = sha(text)
        if stated != got:
            fails.append(f"prompts-evaluated {seam} {role}: text hashes to {got}, file states {stated}")
        reg_role = "system" if role == "system" and seam not in ("extraction",) else (
            "system template" if seam == "extraction" and role == "system" else "user template")
        want = table.get((seam, reg_role))
        if want is None or want[0] != got:
            fails.append(f"register prompt table row ({seam}, {reg_role}) is {want} for text hash {got}")
    for seam, (path, name) in consts.items():
        const = str_constants(git_show(CODE, path)).get(name)
        text = blocks.get((seam, "system"), (None, None))[1]
        if const is None or text != const:
            fails.append(f"{seam} system text differs from {name} ({CODE}:{path})")
    ext = blocks.get(("extraction", "system"), (None, ""))[1]
    if ext != static + SEP + REGISTRY_PLACEHOLDER:
        fails.append("the evaluated extraction system text differs from the base instructions under expansion_force_scalar")
    if ext == c["EXTRACTION_BASE_INSTRUCTIONS"] + SEP + REGISTRY_PLACEHOLDER:
        fails.append("the evaluated extraction system text equals the text without the scalar replacement")
    notes.append(f"{len(blocks)} evaluated static texts; 4 system texts equal their 3320375 constants; "
                 "the extraction text equals the base instructions with the scalar replacement, and not without it")

    # 4c. schema strictness (register A.6, E.6, K2.6b, judge and RAG entries)
    ol = mods["app.llm.openai_llm"]
    schemas = {
        "GateClassificationResponse": (mods["app.schemas.llm_gatekeeper"].GateClassificationResponse, False),
        "LLMExtractionResponse": (mods["app.schemas.llm_extraction"].LLMExtractionResponse, True),
        "KeyResolutionResponse": (mods["app.schemas.llm_resolution"].KeyResolutionResponse, True),
        "GroundingResponse": (mods["app.schemas.llm_grounding"].GroundingResponse, True),
        "ClaimSupportResponse": (mods["app.schemas.llm_claim_support"].ClaimSupportResponse, True),
        "ExpansionCandidateWithFamilyResponse": (mods["app.llm.expansion_generator"].ExpansionCandidateWithFamilyResponse, True),
        "JudgeResponse": (class_from_source(git_show(CODE, "app/evaluation/ami/judge.py"), "JudgeResponse"), True),
        "RagAnswerSchema": (class_from_source(git_show(CODE, "app/evaluation/ami/rag_components.py"), "RagAnswerSchema"), True),
    }
    strict_notes = []
    for name, (cls, want) in schemas.items():
        got = ol._is_strict_safe(ol._strictify_schema(cls.model_json_schema()))
        strict_notes.append(f"{name}={got}")
        if got != want:
            fails.append(f"{name}: strict {got}, register says {want}")
    notes.append("strict: " + ", ".join(strict_notes))

    # 4d. alias merge (register K2.6b step 1)
    if not runs_present():
        notes.append("alias-merge check skipped: run folders under data/ami_eval/a1_smoke are absent")
        report("4 code", "FAIL" if fails else "PASS", "code-derived hashes, prompt-to-constant equality, strictness"
               + ("; alias merge SKIPPED (runs absent)" if not fails else ""), fails + notes)
        return

    def norm_alias(t):  # StateKeyRegistryService._normalize at 3320375
        return " ".join(t.lower().replace("-", " ").replace("_", " ").split())

    expected = {"a0_r1": (42, 41), "a1_r2": (38, 38)}  # register K2.6b, step 1
    for run, (n_want, hit_want) in expected.items():
        spans = set()
        for st in trace(run)["steps"]:
            if st["seam"] == "extraction" and (st.get("input") or {}).get("messages"):
                u = st["input"]["messages"][1]["content"]
                spans.add(u.split("Extract project-state claims from:\n\n", 1)[1])
        flat = {s: " ".join(s.split()) for s in spans}
        s = state(run)
        defs = {d["state_key"]: d for d in s["state_key_definitions"]}
        merges = [p for p in s["expansion_proposals"] if p.get("generation_method") == "rule_based" and p["status"] == "merged"]
        hits, unmatched = 0, 0
        for p in merges:
            full = []
            for t in p["triggered_by_texts"]:
                pre = " ".join((t[:-1] if t.endswith("…") else t).split())
                cand = [x for x, f in flat.items() if f.startswith(pre)]
                unmatched += len(cand) != 1
                full += cand
            d = defs[p["merged_into_key"]]
            aliases = d["aliases"] + [d["label"], d["state_key"].replace(".", " ")]
            hits += any(norm_alias(a) in norm_alias(f) for f in full for a in aliases)
        notes.append(f"alias merge {run}: {hits} of {len(merges)} rule-based merges have an alias, label or "
                     f"dotted name of the target key in the full span ({unmatched} trigger texts not matched to one span)")
        if (len(merges), hits) != (n_want, hit_want) or unmatched:
            fails.append(f"alias merge {run}: {hits} of {len(merges)}, register says {hit_want} of {n_want}")
    report("4 code", "FAIL" if fails else "PASS",
           "code-derived hashes, prompt-to-constant equality, strictness and alias merge as the register states"
           if not fails else f"{len(fails)} mismatch(es)", fails + notes)
    report("4 code: merge completeness", "CLOSED", "closed: one-time historical check, result in the register's "
           "Checks section (register decision 10; its inputs, the two pre-merge parts, were never in the repository)")


# ---------------------------------------------------------------------------------------------
# 5. Claims register quote check (port of qcheck_claims.py; logic unchanged)
# ---------------------------------------------------------------------------------------------

CLAIMS_EXPECTED = {  # known, deliberate: a dated history line quoting the sheet's former C1 wording
    "the M-19 rule if C43 takes option (a)",
}

_wt = {}


def cq_norm(s):
    return re.sub(r"\s+", " ", s).strip()


def cq_show(commit, path):
    k = (commit, path)
    if k not in _wt:
        if commit is None:
            f = ROOT / path
            _wt[k] = f.read_text().split("\n") if f.exists() else None
        else:
            t = git_show(commit, path)
            _wt[k] = t.split("\n") if t is not None else None
    return _wt[k]


def cq_design_paras():
    t = (HERE / "23-am1-design-text-94c049d.md").read_text().split("\n")
    out, i = {}, 0
    while i < len(t):
        m = re.match(r"\*\*(D\d+\.p\d+|T\.rationale)\*\* \(lines (\d+)-(\d+)\)", t[i])
        if m:
            s = t.index("```latex", i) + 1
            e = t.index("```", s)
            out[m.group(1)] = cq_norm(" ".join(t[s:e]))
            i = e
        i += 1
    return out


THESIS_FILES = {"eval.tex", "conclusion.tex", "main.tex", "implementation_chapter.tex", "problem_domain.tex",
                "background.tex", "appendix_walkthrough.tex", "appendix_reproducibility.tex",
                "appendix_design_evidence.tex", "discussion.tex"}


def cq_resolve(cite, design):
    c = cite.strip().strip("`").replace("–", "-")
    m = re.fullmatch(r"(D\d+\.p\d+)", c)
    if m:
        return ("design", design.get(m.group(1)))
    m = re.fullmatch(r"([0-9a-f]{7,40}):([\w./-]+):(\d+)(?:-(\d+))?", c)
    if m:
        return (cq_show(m.group(1), m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3)))
    m = re.fullmatch(r"(amendment|plan 23|codebook|script):(\d+)(?:-(\d+))?", c)
    if m:
        f = {"amendment": "23-plan-amendment-1-ceilings-and-root-cause.md", "plan 23": "23-plan-development-and-confirmation.md",
             "codebook": "23-loss-trace.md", "script": "23-loss-trace.py"}[m.group(1)]
        return (cq_show(None, str((HERE / f).relative_to(ROOT))), int(m.group(2)), int(m.group(3) or m.group(2)))
    m = re.fullmatch(r"(?:thesis/)?((?:generated/)?[\w]+\.tex):(\d+)(?:-(\d+))?", c)
    if m and (m.group(1) in THESIS_FILES or m.group(1).startswith("generated/")):
        return (cq_show(THESIS, "thesis/" + m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2)))
    m = re.fullmatch(r"(?:thesis/notes/thesis_completion/artifacts/|…/)?((?:2\d|1\d)-[\w.-]+\.(?:md|py|yaml|json)):(\d+)(?:-(\d+))?", c)
    if m:
        return (cq_show(None, str((HERE / m.group(1)).relative_to(ROOT))), int(m.group(2)), int(m.group(3) or m.group(2)))
    return None


def cq_found(q, res):
    nq = cq_norm(q)
    if res is None:
        return None
    if res[0] == "design":
        return res[1] is not None and nq in res[1]
    lines, a, b = res
    if lines is None:
        return False
    return nq in cq_norm(" ".join(lines[a - 1 : b + 6]))


def cq_block(lines_src, n, block):
    text = cq_norm(" ".join(block))
    frags = [cq_norm(f) for f in text.split("[...]")]
    frags = [f for f in frags if f]
    if not frags:
        return "empty"
    start_line = cq_norm(lines_src[n - 1])
    joined = cq_norm(" ".join(lines_src[n - 1 :]))
    i = joined.find(frags[0])
    if i < 0:
        return f"first fragment not found from line {n}: {frags[0][:70]!r}"
    if i >= len(start_line):
        return f"first fragment does not start on line {n} (starts later): {frags[0][:70]!r}"
    pos = i + len(frags[0])
    for f in frags[1:]:
        j = joined.find(f, pos)
        if j < 0:
            return f"later fragment not found in order: {f[:70]!r}"
        pos = j + len(f)
    return None


TOK_RE = re.compile(r"`?([0-9a-f]{7,40}:[\w./-]+:\d+(?:[–-]\d+)?|(?:amendment|plan 23|codebook|script):\d+(?:[–-]\d+)?"
                    r"|(?:thesis/)?(?:generated/)?\w+\.tex:\d+(?:[–-]\d+)?|(?:…/)?[12]\d-[\w.-]+\.(?:md|py|yaml|json):\d+(?:[–-]\d+)?"
                    r"|D\d+\.p\d+)`?")


def check_claims():
    design = cq_design_paras()
    reg = CLAIMS.read_text().split("\n")
    errors, ok_blocks, ok_inline, unsourced, unresolved = [], 0, 0, [], []
    cur = None
    in_fence, fence_start, fence_lines, fence_cite = False, 0, [], None
    for ln, line in enumerate(reg, 1):
        if line.startswith("```"):
            if not in_fence:
                in_fence, fence_start, fence_lines = True, ln, []
                fence_cite = cur
            else:
                in_fence = False
                if fence_cite and reg[fence_start - 1].startswith("```tex"):
                    path, n = fence_cite
                    src = cq_show(THESIS, path)
                    if src is None:
                        errors.append((ln, f"line {fence_start}: cannot read {path}", None))
                    else:
                        r = cq_block(src, n, fence_lines)
                        if r:
                            errors.append((ln, f"line {fence_start} ({path}:{n}): {r}", None))
                        else:
                            ok_blocks += 1
                elif reg[fence_start - 1].startswith("```tex"):
                    errors.append((ln, f"line {fence_start}: tex block with no cited location", None))
                cur = None if not line.startswith("```tex") else cur
            continue
        if in_fence:
            fence_lines.append(line)
            continue
        m = re.match(r"#### (C\d+[a-z]?) · `(thesis/[^`:]+):(\d+)`", line)
        if m:
            cur = (m.group(2), int(m.group(3)))
        m = re.match(r"\*\*Dormant \d+\*\* · `(thesis/[^`:]+):(\d+)`", line)
        if m:
            cur = (m.group(1), int(m.group(2)))
        m = re.match(r"Quote at `(thesis/[^`:]+):(\d+)`", line)
        if m:
            cur = (m.group(1), int(m.group(2)))
        stripped = re.sub(r"`[^`]*`", lambda mm: "\x00" * len(mm.group(0)), line)
        quotes = [(mm.start(), mm.end(), line[mm.start() + 1 : mm.end() - 1]) for mm in re.finditer(r'"[^"\x00]*"', stripped)]
        for k, (s, e, q) in enumerate(quotes):
            if line[max(0, s - 10):s].lower().rstrip().endswith("proposed:"):
                continue
            rest = line[e:]
            cm = re.match(r"\s*[,.;]?\s*\(([^()]*)\)", rest)
            cite = None
            if cm:
                cite = cm.group(1)
            else:
                j = k + 1
                while j < len(quotes):
                    gap = line[quotes[j - 1][1] : quotes[j][0]]
                    if not re.fullmatch(r"\s*(?:,|;|and|or|/|,\s*and)?\s*", gap):
                        break
                    cm2 = re.match(r"\s*[,.;]?\s*\(([^()]*)\)", line[quotes[j][1]:])
                    if cm2:
                        cite = cm2.group(1)
                        break
                    j += 1
            if cite is None:
                cm3 = re.match(r"\s*,\s*([^()\"]*?)\)", rest)
                if cm3 and line[:s].rstrip().endswith("("):
                    cite = cm3.group(1)
            if cite is None:
                bm = re.search(r"([\w./`-]+:\d+(?:[–-]\d+)?)`?\s*\(\s*$", line[:s])
                if bm:
                    cite = bm.group(1)
            if cite is None:
                if len(cq_norm(q)) >= 12:
                    unsourced.append(f"line {ln}: {q[:80]!r}")
                continue
            toks = TOK_RE.findall(cite)
            if not toks:
                unresolved.append(f"line {ln}: cite {cite[:60]!r} for {q[:60]!r}")
                continue
            if any(cq_found(q, res) for res in (cq_resolve(t, design) for t in toks) if res is not None):
                ok_inline += 1
            else:
                errors.append((ln, f"line {ln}: inline quote not in {toks}: {q[:90]!r}", q))
    expected = [e for e in errors if e[2] in CLAIMS_EXPECTED]
    real = [e for e in errors if e[2] not in CLAIMS_EXPECTED]
    rows = len(re.findall(r"^#### C\d+[a-z]? ", CLAIMS.read_text(), re.M))
    notes = [f"{ok_blocks} row and dormant quote blocks verified; {ok_inline} inline quotes verified; {rows} row headings",
             f"expected history error(s) present: {len(expected)} ({'; '.join(e[1] for e in expected) or 'none'})",
             f"inline quotes with a citation the check does not parse: {len(unresolved)}; "
             f"quotes of 12+ characters with no citation on their line: {len(unsourced)} (not errors)"]
    if VERBOSE:
        notes += ["UNRESOLVED " + x for x in unresolved]
    problems = [e[1] for e in real]
    if len(expected) != 1:
        problems.append(f"expected exactly one history error, found {len(expected)}")
    report("5 claims", "FAIL" if problems else "PASS",
           "; ".join(([f"{len(real)} unexpected error(s)"] if real else [])
                     + ([f"{len(expected)} expected history error(s), not exactly one"] if len(expected) != 1 else []))
           if problems else "every quote verified except the one expected history error",
           problems + notes)


# ---------------------------------------------------------------------------------------------
# 6. Decision sheet quote check (port of qcheck.py)
# ---------------------------------------------------------------------------------------------

def check_sheet_quotes():
    def norm(t):
        t = t.replace("**", "").replace("*", "").replace("`", "")
        t = re.sub(r"^\s*[-+>]?\s*", "", t, flags=re.M)
        return re.sub(r"\s+", " ", t)

    files = ["23-plan-amendment-1-ceilings-and-root-cause.md", "23-am1-design-text-94c049d.md",
             "23-am1-register-design-and-controls.md", "23-am1-register-claims.md", "23-am1-probe-note.md",
             "23-am1-precoder-template.md", "23-am1-audit-list.py", "23-plan-development-and-confirmation.md"]
    texts = {f: norm((HERE / f).read_text()) for f in files}
    # The scratch checker read two copies of git objects: the bug list as committed and the
    # expansion service at the code commit.
    for label, commit, path in (("22-bug-list.md@" + THESIS, THESIS, "thesis/notes/thesis_completion/artifacts/22-bug-list.md"),
                                ("registry_expansion_service.py@" + CODE, CODE, "app/services/registry_expansion_service.py")):
        t = git_show(commit, path)
        if t is None:
            report("6 sheet", "FAIL", f"cannot read {commit}:{path}")
            return
        texts[label] = norm(t)
    qs = re.findall(r'"([^"\n]{6,})"', SHEET.read_text())
    missing = [q for q in qs if not any(norm(q) in t for t in texts.values())]
    report("6 sheet", "FAIL" if missing else "PASS", f"{len(qs)} quotes, {len(missing)} missing",
           [f"MISSING: {q}" for q in missing])


# ---------------------------------------------------------------------------------------------
# 7. Id resolution across 23-am1-*.md (port of ids.py)
# ---------------------------------------------------------------------------------------------

def check_ids():
    files = sorted(HERE.glob("23-am1-*.md"))
    T = {p.name: p.read_text() for p in files}
    sheet = T["23-am1-decisions.md"]
    claims = T["23-am1-register-claims.md"]
    reg = T["23-am1-register-design-and-controls.md"]
    probe = T["23-am1-probe-note.md"]
    tmpl = T["23-am1-precoder-template.md"]
    audit = (HERE / "23-am1-audit-list.py").read_text()
    S = {k: set(re.findall(rf"^\*\*({k}\d+)\. ", sheet, re.M)) for k in "CBA"}
    S["C"] |= {"C43.1", "C43.2", "C43.3"}
    rows = set(re.findall(r"^#### (C\d+[a-z]?) ", claims, re.M))
    Rs = set(re.findall(r"^- \*\*(R-\d+)\.", claims, re.M)) | set(re.findall(r"^\*\*(R-\d+)\.", claims, re.M))
    Ms = set(re.findall(r"^- \*\*(M-\d+)\.", claims, re.M))
    PNs = set(re.findall(r"^- \*\*(PN-\d+)\.", probe, re.M))
    Ps = set(re.findall(r"\*\*(P\d+)\.", probe))
    ALs = set(re.findall(r"^(AL-\d+)\.", audit, re.M)) | {"AL-2", "AL-4", "AL-6"}  # review findings in the docstring
    pts = set(re.findall(r"^(\d+)\. \*\*", tmpl.split("## 7. Open points")[1].split("## Review record")[0], re.M))
    regdec = set()
    m = re.search(r"\n## [^\n]*Decisions for the author[^\n]*\n(.*?)(\n## |\Z)", reg, re.S)
    if m:
        regdec = set(re.findall(r"^(?:\*\*)?(\d+)\. ", m.group(1), re.M)) | set(re.findall(r"^- \*\*(?:Decision )?(\d+)[.:]", m.group(1), re.M))
    bad = []

    def chk(fname, tok, ok, line):
        if not ok:
            bad.append(f"{fname}:{line} {tok}")

    for fname, t in T.items():
        for i, line in enumerate(t.split("\n"), 1):
            for x in re.findall(r"\bR-\d+\b", line):
                chk(fname, x, x in Rs, i)
            for x in re.findall(r"\bM-\d+\b", line):
                chk(fname, x, x in Ms, i)
            for x in re.findall(r"\bPN-\d+\b", line):
                chk(fname, x, x in PNs, i)
            for x in re.findall(r"\bAL-\d+\b", line):
                chk(fname, x, x in ALs, i)
            for x in re.findall(r"(?:decision sheet(?:'s)?|decision|decisions|sheet's) ([CBA]\d+(?:\.\d)?)\b", line):
                chk(fname, x, x in S[x[0]], i)
            for x in re.findall(r"\b([CBA]\d+) on the decision sheet", line):
                chk(fname, x, x in S[x[0]], i)
            for x in re.findall(r"decision sheet (?:entry |entries )?([CBA]\d+)", line):
                chk(fname, x, x in S[x[0]], i)
            if fname == "23-am1-decisions.md":
                for x in re.findall(r"\b(C\d+[a-z]?(?:\.\d)?)\b", line):
                    chk(fname, x, (x in S["C"] and not re.match(r"C0", x)) or x in rows, i)
                for x in re.findall(r"\bB(\d+)\b", line):
                    chk(fname, "B" + x, ("B" + x) in S["B"], i)
                for x in re.findall(r"\bA(\d+)\b(?!′)", line):
                    chk(fname, "A" + x, ("A" + x) in S["A"] or x in ("0", "1", "2"), i)
                for x in re.findall(r"register decision (\d+)", line):
                    chk(fname, "regdec " + x, x in regdec, i)
                for x in re.findall(r"amendment decision (\d+)", line):
                    chk(fname, "amdec " + x, 1 <= int(x) <= 7, i)
                for x in re.findall(r"template point (\d+)", line):
                    chk(fname, "pt " + x, x in pts, i)
                for x in re.findall(r"points? (\d+)(?:–|-| to )(\d+)", line):
                    chk(fname, "pts %s-%s" % x, x[0] in pts and x[1] in pts, i)
                for x in re.findall(r"\bP(\d+)\b", line):
                    if x in ("0", "23"):
                        continue  # P0 text fixes (claims R-2) and P23:264 (plan 23 item), not probe proposals
                    chk(fname, "P" + x, ("P" + x) in Ps, i)
            if fname == "23-am1-register-claims.md":
                for x in re.findall(r"\brows? (C\d+[a-z]?)\b", line):
                    chk(fname, x, x in rows, i)
            if fname in ("23-am1-precoder-template.md", "23-am1-register-design-and-controls.md"):
                for x in re.findall(r"(?<!amendment )\bdecisions? (\d+)\b", line):
                    chk(fname, "regdec " + x, x in regdec, i)
    defs = (f"definitions: sheet C {len(S['C'])}, B {len(S['B'])}, A {len(S['A'])}; claim rows {len(rows)}; "
            f"R {len(Rs)}; M {len(Ms)}; PN {len(PNs)}; P {len(Ps)}; AL {len(ALs)}; template points {len(pts)}; "
            f"register decisions {len(regdec)}; files {len(files)}")
    report("7 ids", "FAIL" if bad else "PASS", f"{len(bad)} unresolved id(s)", bad[:60] + [defs])


# ---------------------------------------------------------------------------------------------
# 8. Probe note: substitution hashes and overlap check (port of compute.py, overlap.py, overlap_reg.py)
# ---------------------------------------------------------------------------------------------

def probe_constants():
    text = PROBE.read_text()
    block = text.split("The same, as Python:\n\n```python\n")[1].split("\n```")[0]
    env = {}
    for node in ast.parse(block).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                env[node.targets[0].id] = ast.literal_eval(node.value)
            except ValueError:
                pass
    table = {}
    for m in re.finditer(r"^\| (Recorded \(A0, A1, A2\)|\(b2\)) \| ([\d,]+) \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|$", text, re.M):
        table[m.group(1)] = (num(m.group(2)), m.group(3), m.group(4))
    full = text.split("**The (b2) static part, in full:**\n\n```text\n")[1].split("\n```")[0]
    counts = re.search(r"\| Extraction calls in the nine runs \| ([\d,]+) \(a0: (\d+), (\d+), (\d+); a1: (\d+), (\d+), (\d+); "
                       r"a2: (\d+), (\d+), (\d+)\) \|", text)
    rf = re.search(r"has SHA-256 `([0-9a-f]{64})`", text)
    return env, table, full, counts, rf.group(1) if rf else None, text


def check_probe(tmp):
    env, table, full_b2, counts, rf_hash, text = probe_constants()
    fails, notes = [], []
    need = ("SEP", "S1_OLD", "S1_NEW", "S2_OLD", "S2_NEW", "RECORDED", "NEUTRAL")
    if any(k not in env for k in need) or len(table) != 2 or counts is None:
        report("8 probe", "FAIL", "the probe note's constants, hash table or call counts were not found")
        return
    if env["SEP"] != SEP:
        fails.append("the note's SEP differs from the registry header of the extraction prompt")
    c, static_code = extraction_constants()
    new_code = static_code
    for old, new in ((env["S1_OLD"], env["S1_NEW"]), (env["S2_OLD"], env["S2_NEW"])):
        if new_code.count(old) != 1:
            fails.append(f"old text occurs {new_code.count(old)} times in the static part: {old[:50]!r}")
        new_code = new_code.replace(old, new)
    rec_len, rec_sha, rec_reg = table["Recorded (A0, A1, A2)"]
    b2_len, b2_sha, b2_reg = table["(b2)"]
    checks = [
        ("code-built static SHA-256 equals RECORDED", sha(static_code) == env["RECORDED"] == rec_sha),
        ("code-built static length", len(static_code) == rec_len),
        ("static + SEP + registry placeholder", sha(static_code + SEP + REGISTRY_PLACEHOLDER) == rec_reg),
        ("(b2) static SHA-256 equals NEUTRAL", sha(new_code) == env["NEUTRAL"] == b2_sha),
        ("(b2) static length", len(new_code) == b2_len),
        ("(b2) + SEP + registry placeholder", sha(new_code + SEP + REGISTRY_PLACEHOLDER) == b2_reg),
        ("(b2) text printed in the note equals the substituted text", full_b2 == new_code),
        ("each new text once in the (b2) text", new_code.count(env["S1_NEW"]) == 1 and new_code.count(env["S2_NEW"]) == 1),
        ("the note's step 2 and step 4 hashes", f"`{rec_sha}`" in text.split("### 1.4")[1].split("**Steps:**")[1][:600]
         and f"`{b2_sha}`" in text.split("### 1.4")[1].split("**Steps:**")[1][:900]),
    ]
    for name, ok in checks:
        if not ok:
            fails.append(name)
    notes.append(f"recorded static {sha(static_code)} ({len(static_code):,} chars); (b2) {sha(new_code)} ({len(new_code):,} chars)")
    for w in ("Industrial", "Marketing", "Designer", "Interface", "Expert", "Project Manager"):
        if new_code.count(w):
            notes.append(f"after substitution {w!r} still occurs {new_code.count(w)} time(s)")

    # response_format of LLMExtractionResponse, as the client builds it (sorted-key compact JSON)
    import pydantic
    mods = schema_modules(tmp)
    ol = mods["app.llm.openai_llm"]
    cls = mods["app.schemas.llm_extraction"].LLMExtractionResponse
    schema = ol._strictify_schema(cls.model_json_schema())
    rf = {"type": "json_schema", "json_schema": {"name": cls.__name__, "schema": schema, "strict": ol._is_strict_safe(schema)}}
    got_rf = sha(json.dumps(rf, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    notes.append(f"response_format {got_rf} (pydantic {pydantic.VERSION}; the note computed it with 2.13.4)")
    if got_rf != rf_hash:
        fails.append(f"response_format hash {got_rf} differs from the note's {rf_hash}")

    if not runs_present():
        report("8 probe", "FAIL" if fails else "PASS", "substitution hashes as the note states; recorded calls and "
               "overlap SKIPPED: run folders under data/ami_eval/a1_smoke are absent", fails + notes)
        return

    # every recorded extraction call of the nine runs
    want_counts = dict(zip(NINE_RUNS, (int(x) for x in counts.groups()[1:])))
    total, statics, elsewhere, bad_calls = 0, set(), 0, 0
    user_spans, reg_parts = [], []
    for run in NINE_RUNS:
        n = 0
        for st in trace(run)["steps"]:
            if st["seam"] != "extraction":
                continue
            n += 1
            if st.get("fallback") or st.get("error") or st.get("mode") != "llm" or st.get("model") != "gpt-5.4-mini" \
                    or st.get("served_model") != "gpt-5.4-mini-2026-03-17" or st["input"]["response_schema"] != "LLMExtractionResponse":
                bad_calls += 1
            sysmsg, user = st["input"]["messages"][0]["content"], st["input"]["messages"][1]["content"]
            parts = sysmsg.split(SEP)
            if len(parts) != 2:
                bad_calls += 1
                continue
            statics.add(parts[0])
            reg_parts.append(parts[1])
            user_spans.append(user)
            for o in (env["S1_OLD"], env["S2_OLD"]):
                elsewhere += parts[1].count(o) + user.count(o)
        total += n
        if n != want_counts[run]:
            fails.append(f"{run}: {n} extraction calls, the note says {want_counts[run]}")
    if total != num(counts.group(1)):
        fails.append(f"{total} extraction calls, the note says {counts.group(1)}")
    if statics != {static_code}:
        fails.append(f"{len(statics)} distinct recorded static parts; equal to the code-built one: {static_code in statics}")
    if bad_calls:
        fails.append(f"{bad_calls} calls with a fallback, error, other model, other schema or no single SEP")
    if elsewhere:
        fails.append(f"the old texts occur {elsewhere} times outside the static part")
    notes.append(f"{total} recorded extraction calls, one static part equal to the code-built one; "
                 f"old texts outside the static part: {elsewhere}")

    # overlap check (section 1.3)
    words = ["payroll", "legal", "counsel", "vehicle", "fleet", "specialist", "facilities", "coordinator",
             "Payroll Specialist", "Legal Counsel", "Vehicle Fleet Specialist", "Facilities Coordinator"]
    gold_texts, tr_texts, reg_texts = probe_sources(user_spans, reg_parts)

    def count(term, texts):
        rx = re.compile(r"\b" + re.escape(term) + r"(s|es)?\b", re.I)
        return sum(len(rx.findall(x)) for x in texts)

    hits = []
    for w in words:
        g, t, r = count(w, gold_texts), count(w, tr_texts), count(w, reg_texts)
        if g or t or r:
            hits.append(f"{w!r}: gold and suites {g}, transcripts {t}, registries and ontology {r}")
    control = count("procurement", reg_texts)  # a rejected word the note found in a run registry
    if hits:
        fails += ["overlap: " + h for h in hits]
    if not control:
        fails.append("positive control failed: 'procurement' not found in the run registries")
    notes.append(f"overlap: {len(words)} words and titles, 0 hits in every column expected; "
                 f"{len(gold_texts)} gold and suite strings, {len(tr_texts)} transcript texts, {len(reg_texts)} registry texts; "
                 f"control 'procurement' found {control} times in the registries")
    report("8 probe", "FAIL" if fails else "PASS",
           "substitution hashes, recorded calls and overlap check as the probe note states" if not fails
           else f"{len(fails)} mismatch(es)", fails + notes)


def probe_sources(user_spans, reg_parts):
    """The three columns of the probe note's overlap table (section 1.3)."""
    def strings(node, out, skip=("transcript_support", "text", "word_ranges", "verification", "evidence",
                                 "precision_reference_ids")):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in skip:
                    continue
                strings(v, out, skip)
        elif isinstance(node, list):
            for x in node:
                strings(x, out, skip)
        elif isinstance(node, str):
            out.append(node)

    d = ROOT / "data/ami_eval"
    gold = []
    for p in ("gold/reviewed/EL2020.reviewed.yaml", "gold/reviewed/ES2009.reviewed.yaml"):
        strings(yaml.safe_load((d / p).read_text()), gold)
    strings(json.loads((d / "gold/generated/ES2009.timeline.json").read_text()), gold)
    for p in ("ES2009.grounding_audit.json", "ES2009.reviewed_audit.json"):
        strings(json.loads((d / "gold/audits" / p).read_text()), gold)
    strings(yaml.safe_load((d / "gold/audits/ES2009.review_queue.yaml").read_text()), gold)
    gold.append((d / "gold/audits/ES2009.completeness_candidates.md").read_text())
    transcripts = []
    suite = yaml.safe_load((d / "suites/transfer_el2020.yaml").read_text())
    t = suite["transcripts"]
    if isinstance(t, dict):
        transcripts += [v if isinstance(v, str) else json.dumps(v) for v in t.values()]
    else:
        transcripts.append(json.dumps(t))
    strings({k: v for k, v in suite.items() if k != "transcripts"}, gold)
    # The note lists the ES2009 suites and lifecycle_probes.yaml; every other suite file is read whole.
    for p in sorted((d / "suites").glob("*.yaml")):
        if p.name != "transfer_el2020.yaml":
            strings(yaml.safe_load(p.read_text()), gold)
    for p in sorted((d / "transcripts").glob("ES2009*.txt")):
        transcripts.append(p.read_text())
    transcripts += user_spans
    regs = list(reg_parts)
    for f in sorted(RUNS.rglob("*.state.json")):
        regs.append(json.dumps(json.loads(f.read_text())["state_key_definitions"]))
    regs.append((d / "registry.yaml").read_text())
    return gold, transcripts, regs


# ---------------------------------------------------------------------------------------------
# 9. Audit list re-run
# ---------------------------------------------------------------------------------------------

def check_audit(tmp):
    committed = HERE / "23-am1-audit-list.json"
    mod = load_module("am1_audit_for_check", HERE / "23-am1-audit-list.py")
    out = pathlib.Path(tmp) / "23-am1-audit-list.json"
    mod.OUT = out
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mod.main()
    except SystemExit as exc:
        report("9 audit", "FAIL", f"23-am1-audit-list.py stopped: {exc}")
        return
    same = out.read_bytes() == committed.read_bytes()
    data = json.loads(out.read_text())
    report("9 audit", "PASS" if same else "FAIL",
           ("re-run output is byte-identical to the committed JSON" if same else "re-run output differs from the committed JSON"),
           [f"re-run {sha_file(out)}, committed {sha_file(committed)}; {data['audited']} decisions, by role {data['by_role']}"])


# ---------------------------------------------------------------------------------------------
# 10. Hash tables of the index and the decision sheet
# ---------------------------------------------------------------------------------------------

def check_hash_tables():
    today = datetime.date.today()
    rows = []
    for m in re.finditer(r"^\| `([^`]+)` \|.*\| `([0-9a-f]{64})` \|$", INDEX.read_text(), re.M):
        rows.append(("index", m.group(1), m.group(2)))
    for m in re.finditer(r"^\| (`[^`]+`|amendment) \| ([0-9a-f]{64}) \|$", SHEET.read_text(), re.M):
        name = m.group(1).strip("`")
        rows.append(("sheet", AMENDMENT.name if name == "amendment" else name, m.group(2)))
    bad, ok, changed_today = [], 0, set()
    for where, name, want in rows:
        p = HERE / name
        if not p.exists():
            bad.append(f"{where}: {name} does not exist")
            continue
        got = sha_file(p)
        if got == want:
            ok += 1
            continue
        mdate = datetime.date.fromtimestamp(p.stat().st_mtime)
        if mdate == today:
            changed_today.add(name)
        bad.append(f"{where}: {name} recorded {want[:12]}…, on disk {got[:12]}… (modified {mdate.isoformat()})")
    # the index's template row also records the prompt and schema hashes
    prompt, schema = template_texts()
    m = re.search(r"Prompt `([0-9a-f]{64})` \(([\d,]+) characters\), schema `([0-9a-f]{64})`", INDEX.read_text())
    if m:
        if m.group(1) != sha(prompt):
            bad.append(f"index: template prompt recorded {m.group(1)[:12]}…, computed {sha(prompt)[:12]}…")
        else:
            ok += 1
        if m.group(3) != sha(schema):
            bad.append(f"index: template schema recorded {m.group(3)[:12]}…, computed {sha(schema)[:12]}…")
        else:
            ok += 1
    z = re.search(r"`(data/ami_eval/a1_smoke/archive/[\w.-]+\.zip)`.*?SHA-256 `([0-9a-f]{64})`", INDEX.read_text())
    zip_note = "run archive: not recorded in the index"
    if z:
        zp = ROOT / z.group(1)
        if zp.exists():
            if sha_file(zp) == z.group(2):
                ok += 1
                zip_note = f"run archive {z.group(1)} equals the index"
            else:
                bad.append(f"index: run archive recorded {z.group(2)[:12]}…, on disk {sha_file(zp)[:12]}…")
                zip_note = ""
        else:
            zip_note = f"run archive SKIPPED: {z.group(1)} is absent (gitignored; written by 23-am1-run-manifest.py --zip)"
    # completeness: every package file has a row in the index's file table
    index_text = INDEX.read_text()
    table = index_text.split("\n## What you sign\n", 1)[1].split("\n## ", 1)[0]
    listed = set(re.findall(r"^\| `([^`]+)` \|", table, re.M))
    package = sorted({p.name for ext in ("md", "py", "json") for p in HERE.glob(f"23-am1-*.{ext}") if p.is_file()}
                     | {AMENDMENT.name})
    unlisted = [name for name in package if name != INDEX.name and name not in listed]
    for name in unlisted:
        bad.append(f"index: {name} has no row in the file table")
    notes = [f"{ok} recorded hashes equal the files", zip_note,
             f"{len(package) - 1 - len(unlisted)} of {len(package) - 1} package files have an index row (the index itself exempt)",
             "files modified today with a stale row: " + (", ".join(sorted(changed_today)) or "none")]
    report("10 hashes", "FAIL" if bad else "PASS", f"{len(bad)} mismatch(es)" if bad else "every recorded hash equals its file",
           bad + [n for n in notes if n])


# ---------------------------------------------------------------------------------------------
# 11. Run manifest
# ---------------------------------------------------------------------------------------------

def check_manifest():
    if not RUNS.is_dir():
        report("11 manifest", "SKIP", "data/ami_eval/a1_smoke is absent (gitignored)")
        return
    rc, out = run_script("23-am1-run-manifest.py")
    report("11 manifest", "PASS" if rc == 0 else "FAIL", f"23-am1-run-manifest.py exit status {rc}",
           [line for line in out.splitlines() if line.strip()])


def main():
    print(f"Plan 23 amendment 1, Step 0 package check (repository {ROOT}, code commit {CODE}, thesis commit {THESIS})")
    with tempfile.TemporaryDirectory(prefix="am1-check-") as tmp:
        steps = [
            ("1 template", check_template), ("2 schema", check_schema), ("3 register", check_register),
            ("4 code", lambda: check_code(tmp)), ("5 claims", check_claims), ("6 sheet", check_sheet_quotes),
            ("7 ids", check_ids), ("8 probe", lambda: check_probe(tmp)), ("9 audit", lambda: check_audit(tmp)),
            ("10 hashes", check_hash_tables), ("11 manifest", check_manifest),
        ]
        for name, fn in steps:
            try:
                fn()
            except Exception as exc:  # noqa: BLE001 - a crashed check is a failed check
                report(name, "FAIL", f"the check crashed: {type(exc).__name__}: {exc}")
    n = {s: sum(1 for r in RESULTS if r[1] == s) for s in ("PASS", "FAIL", "SKIP", "CLOSED")}
    print(f"\nSummary: {n['PASS']} passed, {n['FAIL']} failed, {n['SKIP']} skipped, {n['CLOSED']} closed")
    for check, status, text in RESULTS:
        if status != "PASS":
            print(f"  {status} {check}: {text}")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()

# Record (28 October 2026). Written for decision sheet B3 in the pre-tag pass. It ports the scratch
# checkers qcheck_claims.py, qcheck.py, ids.py, hashes.py, compute.py, overlap.py and overlap_reg.py,
# and adds the code checks of register decision 10 (B3). No other file was changed.
# Record (28 October 2026, pre-tag follow-ups). Check 1 also runs 23-am1-precoder-extract.py --check and
# compares the register and design-text hashes template Section 1 records; check 10 also fails on a
# 23-am1-*.md/.py/.json file, or the amendment, with no row in the index's file table; the merge's
# completeness check is reported as CLOSED; check 5 requires exactly one expected history error;
# the docstring names the four system texts and the extraction text.
