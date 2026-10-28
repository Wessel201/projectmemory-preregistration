export const meta = {
  name: 'amendment-review-2',
  description: 'Second review of plan-23 amendment 1 draft 2: coverage of round-1 findings, and new contradictions or loopholes',
  phases: [{ title: 'Review', detail: 'coverage check and fresh adversarial read' }, { title: 'Verify', detail: 'one skeptic per finding' }],
}
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol. Draft 2 under review: thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md. It amends thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md. The round-1 review findings (34 substantive plus minor) are in ${args.sp}/amend/review_result.json (and digests review_digest.md, review_fv.md). Fact reports: ${args.sp}/amend/facts_*.md. Read-only: do not edit repository files, never call an LLM/OpenAI API, never run the system. Scratch under ${args.sp}/amend/review2_<you>/.`
const SCHEMA = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: {
  title: { type: 'string' }, severity: { type: 'string', enum: ['blocking', 'major', 'minor'] }, section: { type: 'string' },
  problem: { type: 'string' }, proposed_change: { type: 'string' } }, required: ['title', 'severity', 'section', 'problem', 'proposed_change'] } },
  overall: { type: 'string' } }, required: ['findings', 'overall'] }
const VSCHEMA = { type: 'object', properties: { refuted: { type: 'boolean' }, reasoning: { type: 'string' }, better_change: { type: 'string' } }, required: ['refuted', 'reasoning', 'better_change'] }
const LENSES = [
  { key: 'coverage', p: `TASK: for EVERY round-1 finding (substantive and minor, all three lenses) in review_result.json, check whether draft 2 addresses it adequately (its skeptic's better_change is the reference). Report as findings only those NOT addressed, addressed wrongly, or addressed in a way that creates a new problem; in 'overall' give a one-line status per round-1 finding id (lens + index).` },
  { key: 'fresh', p: `TASK: read draft 2 cold as an adversarial examiner and as the engineer who must execute it. Find: internal contradictions (between steps, between the rules list and the steps, between numbers); sequencing errors (a step needing an output that exists only later; rules that must be frozen before a result but are scheduled after it); loopholes that would let an outcome steer a decision or let an implementation defect end up labelled design; unexecutable instructions (check against the app code where a step depends on it: the harness replay inputs, probe conditions such as '_prompt_registry', the A2 offline gate and per-contract switches, D1's switch extraction_whole_decisions, the reviewer oracle); numbers that do not follow from the loss trace outputs (thesis/notes/thesis_completion/artifacts/23-loss-trace.json) or cost reports; and anything an examiner would still call an excuse. Also judge proportionality: is anything here so heavy that it should be cut or made optional, given the thesis goal (what works and what doesn't, with implementation ruled out as an excuse)?` },
]
phase('Review')
return await pipeline(LENSES,
  l => agent(`${CTX}\n\n${l.p}`, { label: `review2:${l.key}`, phase: 'Review', schema: SCHEMA }),
  (r, l) => parallel(((r && r.findings) || []).filter(f => f.severity !== 'minor').map(f => () =>
    agent(`${CTX}\n\nTASK: try to REFUTE this review finding about draft 2 (lens ${l.key}). Check it against the draft and the repository. refuted=true if it is wrong, already handled, or not worth changing; else give the best concrete change.\n\nFinding: ${JSON.stringify(f)}`, { label: `verify2:${l.key}:${f.title.slice(0, 28)}`, phase: 'Verify', schema: VSCHEMA }).then(v => ({ ...f, verdict: v }))))
    .then(vs => ({ key: l.key, overall: r && r.overall, findings: vs.filter(Boolean), minor: ((r && r.findings) || []).filter(f => f.severity === 'minor') })))
