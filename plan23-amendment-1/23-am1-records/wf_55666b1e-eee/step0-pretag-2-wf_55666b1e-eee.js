export const meta = {
  name: 'step0-pretag-2',
  description: 'Follow-ups of the pre-tag pass: V4 check 7, register S.4, committed extract builder, extract rebuild, check-script hardening; then verify',
  phases: [{ title: 'Fix' }, { title: 'Verify' }],
}
const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const R = '/Users/wesselvansommeren/Documents/Project-Context-Protocol'
const SCR = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad'
const RULES = `Context: the Step 0 package of plan 23, amendment 1 in ${A} (see the decision sheet 23-am1-decisions.md and the index 23-am1-step0-index.md). The previous pass's full results, including every reviewer's surviving problems, are in ${SCR}/pretag-result.json. Rules: offline; no network/model/API call; never open .env; Python as ${R}/.venv/bin/python -I -B; no git state changes; scratch only under ${SCR}/pretag2/; never edit the amendment, the decision sheet or the index (the main session does those); keep each file's style; add a dated (28 October 2026) record line to each file you change.`
const TASK = `${RULES}
Apply exactly these follow-ups, in this order:
1. 23-am1-v4.py: check_case's check 7 also accepts sub_cause "not applicable" when the record's class is neither "implementation defect" nor "unclear" (B18). Remove the matching 'did not yet accept' sentence and open item in template Section 9 AG5. Re-run the V4 end-to-end suite ${SCR}/fix-v4-2/e2e/run_tests.py (it must still pass 248/248; add tests for the new case if easy).
2. Register (23-am1-register-design-and-controls.md): add D5.p6's first sentence to S.4's disclosed-limitation list (it was retagged L); reword the doubled line-251 cite (register ~line 1522) so the path cite appears once and 23-am1-check-register.py still checks the quote. Cut, in the register text the extract is built from, the two 'did not occur in these runs' sentences (expansion fallback), the 'mostly' frequency clause on write-path intents, and the a2_r2b run example — or, if the register should keep them as record, cut them in the extract build instead. Keep code-level statements. 23-am1-check-register.py must report 0 errors.
3. Commit the extract builder: port ${SCR}/pretag/template/build_extract.py into ${A}/23-am1-precoder-extract.py (reads only repository files, writes 23-am1-precoder-extract.md; with --check it rebuilds into a temporary path and compares bytes with the committed extract). Rebuild the extract. Run blindness check 7 on it (port or reuse ${SCR}/pretag/template/blind7.py logic). Record in template Section 1: the extract's SHA-256, characters and lines; the filled-prompt SHA-256 ({REGISTER_SHEET} literally replaced by the whole extract file); the SHA-256 of the register and of 23-am1-design-text-94c049d.md it was built from; and that 23-am1-precoder-extract.py rebuilds it. Fix the two template Section 1 nits: line ~24 says the filled hash is recorded below (recompute at signing if anything changes), and the hash note and pre-tag record also credit B21 (Part G's item-id sentence).
4. 23-am1-check-package.py: check 1 also runs 23-am1-precoder-extract.py --check (byte-identical rebuild) and compares the recorded register/design-text hashes with the files; check 10 fails on any 23-am1-*.md/.py/.json file, or the amendment, that has no row in the index's file table (exempt the index itself and the 23-am1-records folder); the merge-completeness check is reported as "closed: one-time historical check, result in the register's Checks section" (not SKIP) and register decision 10 says the same; check 5 requires exactly one expected history error; the docstring says "the four system texts and the extraction text". Run it: everything should pass except check 6 (the decision sheet's B21 note quote) and check 10 (stale hash rows / missing rows), which the main session fixes next — list exactly which rows and quotes fail.
Report every change, every new hash, and test results.`
const REPORT = { type: 'object', properties: { done: { type: 'array', items: { type: 'string' } }, hashes: { type: 'string' }, tests: { type: 'string' }, open: { type: 'array', items: { type: 'string' } } }, required: ['done', 'hashes', 'tests', 'open'] }
const VERDICT = { type: 'object', properties: { problems: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] }, where: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'where', 'problem', 'fix'] } }, summary: { type: 'string' } }, required: ['problems', 'summary'] }
phase('Fix')
const rep = await agent(TASK, { label: 'pretag-fix-2', phase: 'Fix', schema: REPORT })
phase('Verify')
const ver = await agent(`${RULES}
YOU ARE THE VERIFIER (edit no file). Check that each of the four follow-ups below was done as specified and correctly: re-run 23-am1-precoder-extract.py --check, 23-am1-check-package.py, 23-am1-check-register.py, the V4 e2e suite; recompute the template Section 1 hashes; diff the extract against the previous one (${SCR}/pretag/template/ may hold the earlier build; otherwise reason from the register diff) to confirm only the intended content changed and blindness check 7 still passes. Report only real problems with evidence.
FOLLOW-UPS:
${TASK}
FIXER'S REPORT:
${JSON.stringify(rep, null, 1)}`, { label: 'pretag-verify-2', phase: 'Verify', schema: VERDICT })
return { rep, ver }
