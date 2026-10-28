export const meta = {
  name: 'loss-trace-notes-verify',
  description: 'Independently recompute and try to refute the loss-trace results, the arms note and plan-23 entries; check codebook vs v3.1 code',
  phases: [{ title: 'Check', detail: 'recompute numbers, refute claims, codebook vs code' }],
}
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol (python: .venv/bin/python). Artifacts in thesis/notes/thesis_completion/artifacts/: 23-loss-trace-results.md, 23-el2020-arms.md, 23-loss-trace.md (codebook), 23-loss-trace.py (v3.1), 23-loss-trace.json (output, primary series), 23-loss-trace-adjudications.yaml, 23-el2020-arms.json, 23-el2020-arms.py, and in 23-plan-development-and-confirmation.md the entries starting '**Bug 11: done 23 October' and '**A2 and same-period RAG on EL2020'. Run dirs: ${JSON.stringify(args.runs)} (RAG runs: ${JSON.stringify(args.rag)}). Offline only; never call an LLM/OpenAI API; do not edit repository files; scratch only under ${args.sp}/ltv3/work/notes_<you>/.`
const SCHEMA = { type: 'object', properties: {
  problems: { type: 'array', items: { type: 'object', properties: {
    location: { type: 'string' }, statement: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, correction: { type: 'string' },
    severity: { type: 'string', enum: ['wrong_number', 'unsupported_claim', 'overstated', 'doc_mismatch', 'minor'] } },
    required: ['location', 'statement', 'problem', 'evidence', 'correction', 'severity'] } },
  checked: { type: 'string' } }, required: ['problems', 'checked'] }
const tasks = [
  { key: 'recompute', p: `${CTX}

TASK: independently recompute EVERY number in 23-loss-trace-results.md, in the loss-trace paragraph and the state-statistics table of 23-el2020-arms.md, and in the two plan-23 entries named above. Use your own code on 23-loss-trace.json (records per run, both bounds; arms summaries), 23-el2020-arms.json, the run reports and state dumps. The raw-strict column of the 'Effect of adjudication' table comes from running the script without --adjudications (do so, --out under your scratch dir). Report every number that does not reproduce (with the correct value), and say what you checked.` },
  { key: 'refute', p: `${CTX}

TASK: try to REFUTE each interpretive claim in 23-loss-trace-results.md ('What the trace says', 'Effect of adjudication'), in the 'What the data supports' section of 23-el2020-arms.md, and in the two plan-23 entries. Examples: 'A0 and A1 differ in sub-codes, not totals'; 'the repairs do not touch this stage [extraction]'; 'A2 stores 28.3 values ... which accounts for its lower score'; 'the conflicts mostly come from routing'; 'credit without state is rare ... correct current_state answers mostly rest on the stored value'; 'Reading loses 40–47%'; the description of what adjudication rejects. For each, test it against the data (the json, the run files, the scorecards). Report claims that are unsupported, overstated or wrong, with evidence and a corrected wording. Do not report matters of taste.` },
  { key: 'codebook', p: `${CTX}

TASK: check 23-loss-trace.md (codebook) against the code of 23-loss-trace.py (v3.1) and its output: every sub-code the code can emit is documented (and vice versa), the matcher, sibling, locality, identity, queue and adjudication rules are described as the code implements them, and the verification figures quoted are supported (recompute what you can: e.g. the replay checks against the reader packs over the nine runs). Report mismatches.` },
]
phase('Check')
const res = await parallel(tasks.map(t => () => agent(t.p, { label: `check:${t.key}`, phase: 'Check', schema: SCHEMA }).then(r => ({ key: t.key, ...(r || {}) }))))
return res
