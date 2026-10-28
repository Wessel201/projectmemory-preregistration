export const meta = {
  name: 'amendment-review-3',
  description: 'Final check of plan-23 amendment 1 draft 3: round-2 coverage and internal consistency',
  phases: [{ title: 'Check' }, { title: 'Verify' }],
}
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol. Draft 3: thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md. Round-2 findings: ${args.sp}/amend/review2_result.json (digest review2_digest.md). Read-only; no LLM/API calls; no repository edits; scratch under ${args.sp}/amend/review3_<you>/.`
const SCHEMA = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: {
  title: { type: 'string' }, severity: { type: 'string', enum: ['blocking', 'major', 'minor'] }, section: { type: 'string' }, problem: { type: 'string' }, proposed_change: { type: 'string' } },
  required: ['title', 'severity', 'section', 'problem', 'proposed_change'] } }, overall: { type: 'string' } }, required: ['findings', 'overall'] }
const VSCHEMA = { type: 'object', properties: { refuted: { type: 'boolean' }, reasoning: { type: 'string' }, better_change: { type: 'string' } }, required: ['refuted', 'reasoning', 'better_change'] }
const TASKS = [
  { key: 'coverage', p: `For every round-2 finding (coverage C0-C8 and minors; fresh F0-F15 and minors), check whether draft 3 addresses it (the skeptic's better_change is the reference). Report as findings only the ones not addressed or addressed wrongly; in 'overall' give a one-line status per round-2 finding.` },
  { key: 'consistency', p: `Read draft 3 cold. Report only real problems: internal contradictions (between steps, the rules list, the cost table, the decisions list), sequencing errors (an input needed before it exists; a rule that must be fixed before a result but is scheduled after), steps that cannot be executed as written given the app code, and arithmetic errors in the numbers (check the cost total and the budget sentence). Do not re-litigate design choices that are internally consistent.` },
]
phase('Check')
return await pipeline(TASKS,
  t => agent(`${CTX}\n\nTASK: ${t.p}`, { label: `check:${t.key}`, phase: 'Check', schema: SCHEMA }),
  (r, t) => parallel(((r && r.findings) || []).filter(f => f.severity !== 'minor').map(f => () =>
    agent(`${CTX}\n\nTASK: try to REFUTE this finding about draft 3. refuted=true if wrong, already handled, or not worth changing; else give the best concrete change.\n\nFinding: ${JSON.stringify(f)}`, { label: `verify:${t.key}:${f.title.slice(0, 28)}`, phase: 'Verify', schema: VSCHEMA }).then(v => ({ ...f, verdict: v }))))
    .then(vs => ({ key: t.key, overall: r && r.overall, findings: vs.filter(Boolean), minor: ((r && r.findings) || []).filter(f => f.severity === 'minor') })))
