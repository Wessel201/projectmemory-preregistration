export const meta = {
  name: 'step0-pretag',
  description: 'Apply the pre-tag edits of plan 23 amendment 1 (register, template, extract, B8, check scripts) offline, then verify them adversarially',
  phases: [
    { title: 'Register', detail: 'B22, C8 tags, C17, C62 on the register; B8 on the claims register' },
    { title: 'Template', detail: 'C8 check 6, C62, B18, extract build and fill (B21)' },
    { title: 'Checks', detail: 'committed check script (B3), run end to end' },
    { title: 'Verify', detail: 'reviewers with skeptics on every change' },
  ],
}

const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const R = '/Users/wesselvansommeren/Documents/Project-Context-Protocol'
const SCR = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad'
const PY = `${R}/.venv/bin/python`

const COMMON = `
Context: the Step 0 package of "plan 23, amendment 1" in ${A}, about to be signed (the author has asked that every decision take its recommendation; nothing is committed). The decision sheet ${A}/23-am1-decisions.md lists every decision; its entry C1 lists the pre-tag items. The amendment is ${A}/23-plan-amendment-1-ceilings-and-root-cause.md ("line N" means its line N); never edit it. Other package files: the design-and-controls register 23-am1-register-design-and-controls.md ("the register"), the claims register 23-am1-register-claims.md, the probe note 23-am1-probe-note.md, the pre-coder template 23-am1-precoder-template.md, the 94c049d design text 23-am1-design-text-94c049d.md, the audit list 23-am1-audit-list.json/.py (already re-run by the main session under C18 (b) and C20 a_shared: 479 decisions), the V4 script 23-am1-v4.py, the index 23-am1-step0-index.md. Existing checkers (scratch, read-only for you): ${SCR}/step0/complete/qcheck_claims.py <claims.md>; ${SCR}/step0/verify/decisions/qcheck.py <artifacts dir> ${SCR}/step0/verify/decisions; ${SCR}/step0/complete/sheet/ids.py <artifacts dir>; ${SCR}/step0/verify/pt/hashes.py <template>; ${A}/23-am1-check-register.py.

Binding rules:
- Edit ONLY the files your task names. Scratch work only under ${SCR}/pretag/<your label>/.
- Offline: no network, no model/LLM/embedding/API call, never open or print any .env. Run Python as ${PY} -I -B (no bytecode in the repository). No git command that changes state (git show/diff/log are fine).
- Take the recommended option of every decision you apply, exactly as its entry states it, including its Corrections. Where an entry leaves something to judgement, research the files first and choose the reading most faithful to the amendment's wording; record the reason.
- Every file you change gets a short dated record (28 October 2026) at its end or in its existing record section, naming the decision ids applied.
- Style: plain, short declarative sentences, as the surrounding text.
- Never move or renumber anything that other files cite by line without updating those cites; prefer in-place edits.`

const REPORT = { type: 'object', properties: {
  done: { type: 'array', items: { type: 'string' } },
  not_done: { type: 'array', items: { type: 'string' } },
  hashes: { type: 'string', description: 'new SHA-256 of each file you changed or created, and any prompt/schema/extract/filled-prompt hashes' },
  tests: { type: 'string' },
  open: { type: 'array', items: { type: 'string' } } },
  required: ['done', 'not_done', 'hashes', 'tests', 'open'] }

const VERDICT = { type: 'object', properties: {
  problems: { type: 'array', items: { type: 'object', properties: {
    severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] },
    where: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } },
    required: ['severity', 'where', 'problem', 'evidence', 'fix'] } },
  summary: { type: 'string' } }, required: ['problems', 'summary'] }

phase('Register')
const [reg, b8] = await parallel([
  () => agent(`${COMMON}
YOUR TASK (edit only ${A}/23-am1-register-design-and-controls.md):
1. B22: resolve every "decision N" pointer on the five register sheets (E, K1, K2, S, R; and wherever else the register sheets point to its decisions 1-17) by writing the signed reading into the sheet text itself, so no sheet depends on a decision pointer. The signed reading of each register decision is its recommendation, as the decision sheet maps it (find each register decision's C/B/A entry in 23-am1-decisions.md via the sheet's source lines; e.g. register decision 2 is C8). Keep the decision list itself as the record.
2. C8 (a) with both Corrections: sentences that state a shortfall (L tags), R-4's list, and D4.p4's matching sentence (now K2.4) cannot ground architectural weakness or a trade-off; B-tagged sentences may ground a trade-off, C-tagged sentences architectural weakness. Make sure every 94c049d sentence the sheets list as quotable carries its tag per sentence (so the extract can carry tags and template check 6 can test a quote against C or B sentences only), and that the sheets' C and B lists agree with the per-sentence tags (D2.p4's window sentence is L; D6.p4 and D7.p5 carry L sentences). Apply Correction 1's coding rule where the register states decision 2 (a).
3. C17 (a): "D4's scalar-concept passage" (line 355) is D4.p5; align D4.p5's scalar sentence tag between E.2 (B) and K2.2 (C) at signing. Research which tag is right from the 94c049d text and line 355 (WD cases keep D4.p5 whole) and record why.
4. C62 (b) and its second item (i): sheet K2 names "candidate generation (LLM)" as a step where line 340's condition and "design or model, not separated" apply; the gatekeeper stays limited to admitted:ignored cases.
Then run ${A}/23-am1-check-register.py (it must report 0 errors) and list every place the template or the extract will have to follow (the template agent runs after you).`, { label: 'register', phase: 'Register', schema: REPORT }),
  () => agent(`${COMMON}
YOUR TASK (edit only ${A}/23-am1-register-claims.md, and only if needed):
B8: (1) in the claims register's mapping section 6.1, cite amendment line 143, not 144, for "status items that can fail" (verify against the amendment first). (2) Check \`fallback_count\` and \`strict_live\` in the coldstart.json (or equivalent cold-start record) of the ten runs not yet checked for claims row C144 — find which runs C144 and claims section 10 say were checked and which remain, locate their files under ${R}/data (read-only; gitignored run folders and data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip may be read by extracting into your scratch folder), and record the result in C144 and section 10 with a dated line. If any run has fallback_count > 0 or strict_live false, say so plainly in the row and report it as an open item; do not change any verdict. Then run the claims quote checker; it must still show only its one known history error.`, { label: 'b8-claims', phase: 'Register', schema: REPORT }),
])

phase('Template')
const tmpl = await agent(`${COMMON}
The register agent has just edited the register; its report is below. YOUR TASK (edit ${A}/23-am1-precoder-template.md, and create ${A}/23-am1-precoder-extract.md):
1. C8 Correction 2: the extract carries the sentence tags; template check 6 (Section 4) and the prompt text it governs (Parts D/E and wherever the prompt tells the coder what may ground architectural weakness or a trade-off) accept a design-ground quote only from a C sentence (architectural weakness) or a B sentence (trade-off); WD cases keep D4.p5 whole (line 355; C17).
2. C62 (b): template A5 and the schema add "candidate generation" among the LLM steps where line 340's condition and "design or model, not separated" apply; the gatekeeper stays as written (C62 second item (i)). Section 7 point 24 marked done.
3. B18: add "not applicable" to the schema's sub-cause values for non-implementation classes.
4. B21/B22: build the pre-coder extract exactly as template Section 1 specifies (five sheets E, K1, K2, S, R from the register as now signed; after each sheet the verbatim 94c049d paragraphs it names from 23-am1-design-text-94c049d.md with sentence tags; the conformance requirements and implementation entries it names; item ids on every checklist item; no decision pointers, no run counts or incidence figures, no "Already read" item, no probe-mapping quotes; B21's note: K1's "(quoted above)" must not point above). Write it to 23-am1-precoder-extract.md. Run blindness check 7 (Section 5) on it and record the result.
5. Record in Section 1: the new prompt hash and schema hash (as Section 1 defines them, before substitution), the extract's SHA-256, and the SHA-256 of the prompt text with {REGISTER_SHEET} filled by literal replacement. Mark Section 7 points 16-18 and any other point these decisions settle as done. Update anything else in the template that the changes make stale (Section 9 must stay consistent: V4's case-packets --template T is "the template with the extract filled in"; say where that filled text comes from).
6. Test the schema with a small local checker in scratch (valid and invalid records, including "not applicable" and "candidate generation"), and confirm ${A}/23-am1-v4.py case-packets still builds packets from a filled template with a mock sub-cause table and mock page (in scratch).

REGISTER AGENT'S REPORT:
${JSON.stringify(reg, null, 1)}`, { label: 'template-extract', phase: 'Template', schema: REPORT })

phase('Checks')
const checks = await agent(`${COMMON}
The register, claims and template agents have finished (reports below). YOUR TASK (create ${A}/23-am1-check-package.py; edit nothing else): B3. One committed script that reads only git objects and files in the repository (no scratch paths, no network) and re-derives, printing a clear pass/fail per check and exiting non-zero on any failure:
- the template: prompt and schema hashes per Section 1; the extract hash and filled-prompt hash recorded in Section 1; the schema test (a few built-in valid and invalid records); the code-derived prompt hashes and prompt-to-constant equality that 23-am1-check-register.py does not already cover (read the register's decision 10 and claims section 10 for what B3 lists);
- the register: delegate to 23-am1-check-register.py (subprocess) or import it;
- the claims register's quote check, the decision sheet's quote check and the id resolution across all 23-am1-*.md, ported from the scratch checkers named above into this script (read them; keep their logic, including the known, deliberate history error in the claims register as an expected exception named by its text, not its line);
- the probe note's substitution hashes and overlap checks, ported from ${SCR}/step0/probe/compute.py, overlap.py and overlap_reg.py (read the probe note §1.4 for what they verify);
- the audit list: re-run 23-am1-audit-list.py into a temporary copy and compare bytes with the committed JSON; or call it in a mode that does not overwrite;
- every hash table in 23-am1-step0-index.md and in the decision sheet's file table against the files on disk (report mismatches; the main session will refresh them last, so mismatches now are expected only for files changed today — list them);
- 23-am1-run-manifest.py's manifest check.
Run it, and report what passes and fails. A check may be marked "skipped" only with a stated reason (for example an input outside the repository). Keep it plain Python 3 with only the stdlib plus yaml if needed.

REPORTS:
${JSON.stringify({ reg, b8, tmpl }, null, 1)}`, { label: 'check-script', phase: 'Checks', schema: REPORT })

phase('Verify')
const LENSES = [
  ['register-extract', `Verify the register edits (B22, C8 tags, C17, C62) and the extract ${A}/23-am1-precoder-extract.md against template Section 1's specification, the decision sheet entries' recommendations and Corrections, and 23-am1-design-text-94c049d.md (verbatim paragraphs, per-sentence tags). Look for a pointer left unresolved, a tag that contradicts the register, a paragraph not verbatim, a forbidden item in the extract (run counts, incidence, Already-read items, probe-mapping quotes), a missing item id.`],
  ['template', `Verify the template edits: check 6 and the prompt text under C8, C62 in A5 and the schema, B18 in the schema, Section 1's recorded hashes (recompute each), Section 7's points marked done, Section 9's consistency, and that nothing else in the prompt changed beyond these decisions (diff against ${SCR}/template-before-main-fixes.md and the current file; the prompt between "~~~~ prompt" and "~~~~").`],
  ['checks-claims', `Verify ${A}/23-am1-check-package.py: run it; read it; confirm each check really re-derives what it claims from repository files only, that failures are detected (make a scratch copy of the artifacts folder, corrupt one quote / one hash / one extract byte, and run the script against the copy if it supports a root argument, or reason from the code), and that the B8 claims edits are correct.`],
]
const verified = await pipeline(
  LENSES,
  ([key, focus]) => agent(`${COMMON}
YOU ARE A REVIEWER (do not edit any repository file). ${focus}
Report only real defects with evidence (file:line, verbatim quotes). Severity: blocks-signing / major / minor / nit.
REPORTS OF THE AGENTS WHOSE WORK YOU CHECK:
${JSON.stringify({ reg, b8, tmpl, checks }, null, 1)}`, { label: `review-${key}`, phase: 'Verify', schema: VERDICT }),
  (v, [key]) => (!v || !v.problems.length) ? { key, review: v, skeptic: null } :
    agent(`${COMMON}
YOU ARE THE SKEPTIC for reviewer ${key}. For each problem below, re-check the evidence yourself and try to refute it. Default to refuted if not convinced. Return the problems that survive, with your severity and the minimal fix. Do not edit any file.
PROBLEMS:
${JSON.stringify(v.problems, null, 1)}`, { label: `skeptic-${key}`, phase: 'Verify', schema: VERDICT }).then(s => ({ key, review: v, skeptic: s })),
)
return { reg, b8, tmpl, checks, verified: verified.filter(Boolean) }
