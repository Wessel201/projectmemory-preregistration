export const meta = {
  name: 'fix-v4-script-2',
  description: 'Second, small fix pass on 23-am1-v4.py from the verifiers of the first pass, then an independent verification',
  phases: [{ title: 'Fix' }, { title: 'Verify' }],
}
const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const SCR = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad'
const PY = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/.venv/bin/python'
const RULES = `
Binding: edit ONLY ${A}/23-am1-v4.py. Scratch work only under ${SCR}/fix-v4-2/<label>/. No network, no model/API call, never read .env, run Python as ${PY} -I -B (no bytecode in the repository). Never point --out or --workspace inside the repository; for guard tests use a fake repository in scratch. No git state changes. Keep the file's style. Do not change the interface: audit-packets --salt S --out DIR [--batch 60]; case-packets --template T --subcauses F --pages DIR --salt S --out DIR; stage --out DIR --packet NAME --workspace WS; collect --out DIR --packet NAME --workspace WS --model LABEL --antigravity-version V [--void REASON] [--model-change]; reject --out DIR --packet NAME --reason TEXT. Do not change INSTRUCTION or STANDARD text.`
const TASK = `${RULES}
The script was rewritten in a first fix pass (results and verifier reports in ${SCR}/fix-v4-result.json). Apply exactly these follow-ups:
1. Open stagings across --out folders: stage writes a marker beside the workspace, outside it, at WS.parent/.<WS.name>.v4-staging.json, holding the resolved --out path, packet, staging number and packet sha256. stage refuses while a marker for that workspace exists, whatever --out it names. collect (with or without --void) refuses unless the marker names this --out, this packet and the staging being collected, so it never removes another job's packet.txt or answer.json; it removes the marker after recording the attempt. Keep the existing per-folder checks.
2. Wrong-label voids: with --void, store --model exactly as given, and neither check nor update model.json. Refuse --model-change together with --void.
3. A RecursionError (or any error) when storing a parsed answer must not crash: set answer to null, valid false, add the problem "answer nested too deeply to store; raw kept", and store the record.
4. The final status print must not crash on a lone surrogate (use backslashreplace or repr).
5. Comments: the SETTINGS comment cites AG5 and Section 9's "What this does not give" (not AG7); the comment on never removing leftovers cites AG1 (not AG5).
6. The audit header's status sentence becomes exactly: 'The status line gives the gold value's status after each meeting that lists it. A value rejected at every meeting that lists it is an option ruled out there, and the standard's rule for a ruled-out option applies to it. A value first listed as current or candidate and later rejected was replaced later; it carries when the text states that same value.'
7. When stage finds a packet.txt or answer.json that no open staging accounts for (for example an answer the agent wrote after collect), its message says so plainly: keep the file with the AG7 record and remove it by hand. It must not tell the author to collect a packet that was already collected.
Then re-run your own end-to-end tests in scratch for every rule (old and new), and report the new SHA-256.`
const REPORT = { type: 'object', properties: { done: { type: 'array', items: { type: 'string' } }, tests: { type: 'string' }, sha256: { type: 'string' }, open: { type: 'array', items: { type: 'string' } } }, required: ['done', 'tests', 'sha256', 'open'] }
const VERDICT = { type: 'object', properties: { problems: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] }, where: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'where', 'problem', 'fix'] } }, summary: { type: 'string' } }, required: ['problems', 'summary'] }
phase('Fix')
const rep = await agent(TASK, { label: 'fix-script-2', phase: 'Fix', schema: REPORT })
phase('Verify')
const ver = await agent(`${RULES}
YOU ARE THE VERIFIER (do not edit any file). Read all of ${A}/23-am1-v4.py. Independently test, with fresh mocks in ${SCR}/fix-v4-2/verify/, every rule of the interface: audit-packets (fields id, fact_id, gold value, status, aliases, text, contexts; no role or v1 label), case-packets (exact sub-cause names from a Markdown table with a Name or Sub-cause column; Part H block checks), stage refusals (repository guard by samestat incl. case variants, firmlink spelling and symlinks; extra files; open stagings in the same and in another --out; valid attempt; two attempts; changed packet file), collect (one attempt per staging; --void; missing, unreadable, non-UTF-8 and symlinked answers; non-string ids; deep nesting; lone surrogates; model.json and --model-change; wrong-label void; marker handling across --out folders), reject (then re-ask; refusals), and the two-attempt limit. Also check the seven follow-ups below were done as specified, and look for regressions and any path that deletes something other than packet.txt, answer.json or the marker. Report only real problems with a reproduction.

THE FOLLOW-UPS:
${TASK}

FIXER'S REPORT:
${JSON.stringify(rep, null, 1)}`, { label: 'verify-script-2', phase: 'Verify', schema: VERDICT })
return { fixer: rep, verifier: ver }
