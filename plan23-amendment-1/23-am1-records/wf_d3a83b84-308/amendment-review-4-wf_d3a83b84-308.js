export const meta = {
  name: 'amendment-review-4',
  description: 'Last focused check of plan-23 amendment 1 draft 4: round-3 fixes landed, no new contradictions',
  phases: [{ title: 'Check' }, { title: 'Verify' }],
}
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol. Draft 4: thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md. Round-3 findings: ${args.sp}/amend/review3_result.json (digest review3_digest.md). Read-only; no LLM/API calls; no repository edits.`
const SCHEMA = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: {
  title: { type: 'string' }, severity: { type: 'string', enum: ['blocking', 'major', 'minor'] }, section: { type: 'string' }, problem: { type: 'string' }, proposed_change: { type: 'string' } },
  required: ['title', 'severity', 'section', 'problem', 'proposed_change'] } }, overall: { type: 'string' } }, required: ['findings', 'overall'] }
const VSCHEMA = { type: 'object', properties: { refuted: { type: 'boolean' }, reasoning: { type: 'string' }, better_change: { type: 'string' } }, required: ['refuted', 'reasoning', 'better_change'] }
phase('Check')
const r = await agent(`${CTX}\n\nTASK: (1) For each round-3 finding (coverage cov0-cov6 and minors; consistency con0-con5 and minors), check that draft 4 adopts its skeptic's better_change correctly; give a one-line status each in 'overall'. (2) Read draft 4 for NEW internal contradictions, sequencing errors, rules that cannot be applied, or arithmetic errors introduced by the draft-4 edits (pending/conditional codes, the eighth label, WD (iv), probe (ii-r)/(ii-h) scoring, C/C2/A1-ref, the bounded admission, the audit list, the cost totals). Report only real problems, as findings; do not re-litigate consistent design choices.`, { label: 'check:draft4', phase: 'Check', schema: SCHEMA })
const vs = await parallel(((r && r.findings) || []).filter(f => f.severity !== 'minor').map(f => () =>
  agent(`${CTX}\n\nTASK: try to REFUTE this finding about draft 4. refuted=true if wrong, already handled, or not worth changing; else give the best concrete change.\n\nFinding: ${JSON.stringify(f)}`, { label: `verify:${f.title.slice(0, 28)}`, phase: 'Verify', schema: VSCHEMA }).then(v => ({ ...f, verdict: v }))))
return { overall: r && r.overall, findings: vs.filter(Boolean), minor: ((r && r.findings) || []).filter(f => f.severity === 'minor') }
