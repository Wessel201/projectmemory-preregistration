export const meta = {
  name: 'loss-trace-verify',
  description: 'Adversarially verify the EL2020 loss trace: blind hand-traces, matcher audit, code review, transaction-time audit',
  phases: [
    { title: 'Trace', detail: 'blind hand-traces of sampled rows from raw run files' },
    { title: 'Compare', detail: 'adjudicate disagreements between hand-trace and script' },
    { title: 'Audit', detail: 'matcher audit, code review, transaction-time audit' },
    { title: 'Verify', detail: 'one skeptic per audit finding' },
  ],
}

const SP = args.sp
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol (run commands from there; python is .venv/bin/python).
The loss trace: thesis/notes/thesis_completion/artifacts/23-loss-trace.py, codebook thesis/notes/thesis_completion/artifacts/23-loss-trace.md.
Suite (gold block from line ~1376, transcripts, questions): data/ami_eval/suites/transfer_el2020.yaml. Meetings in order EL2020a..d = checkpoints k=0..3.
Each run dir holds artifacts/*.coldstart.json (scorecard, config.cycle2_flags), *.state.json (claims, evidence, state_facts, proposals, state_key_definitions), *.answers.json (reader answers with state_keys, facts, near_matches), *.trace.json (steps with seam, mode, input, output; seams include memory_gatekeeper, extraction, resolution, conflict_detection, ami_eval_question).
A0 = evaluated system; A1 = all ten Stage-23 repair switches on. App code under app/ is the authority on behaviour (e.g. app/services/conflict_service.py, app/services/resolution_service.py).
This is offline analysis: never call any LLM/OpenAI API, never run the system live, never print .env. Do not edit any repository file; write scratch files only under ${SP}/ltv/work/.`

const TRACE_SCHEMA = {
  type: 'object',
  properties: {
    rows: { type: 'array', items: { type: 'object', properties: {
      run: { type: 'string' }, fact_id: { type: 'string' }, k: { type: 'integer' },
      first_failing_step: { type: 'string', description: 'one of admitted, carried, polarity, modality, filed, proposed, applied, current, status, key_reached, in_payload, answered, or passes' },
      sub_code: { type: 'string' },
      evidence: { type: 'string', description: 'claim ids / values / trail rows / fact ids that decided it' },
      depends_on_wording_judgement: { type: 'boolean' },
      confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    }, required: ['run', 'fact_id', 'k', 'first_failing_step', 'sub_code', 'evidence', 'depends_on_wording_judgement', 'confidence'] } },
    codebook_ambiguities: { type: 'array', items: { type: 'string' } },
  },
  required: ['rows', 'codebook_ambiguities'],
}

const COMPARE_SCHEMA = {
  type: 'object',
  properties: {
    rows: { type: 'array', items: { type: 'object', properties: {
      run: { type: 'string' }, fact_id: { type: 'string' }, k: { type: 'integer' },
      agree_step: { type: 'boolean' },
      who_is_right: { type: 'string', enum: ['both', 'script', 'hand_trace', 'neither', 'codebook_ambiguous'] },
      cause: { type: 'string', description: 'if they disagree: matcher_lexical_vs_semantic, join_or_phase_bug, status_or_state_bug, codebook_ambiguity, hand_trace_error, other' },
      explanation: { type: 'string' },
    }, required: ['run', 'fact_id', 'k', 'agree_step', 'who_is_right', 'cause', 'explanation'] } },
    script_defects: { type: 'array', items: { type: 'string' }, description: 'concrete defects in 23-loss-trace.py found while adjudicating, with file:line and a reproducing row' },
  },
  required: ['rows', 'script_defects'],
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      title: { type: 'string' },
      severity: { type: 'string', enum: ['changes_counts', 'changes_subcodes', 'documentation', 'minor'] },
      location: { type: 'string' },
      claim: { type: 'string', description: 'the defect, with a concrete reproducing row (run, fact_id, k) or command' },
      estimated_rows_affected: { type: 'string' },
      suggested_fix: { type: 'string' },
    }, required: ['title', 'severity', 'location', 'claim', 'estimated_rows_affected', 'suggested_fix'] } },
    measurements: { type: 'string', description: 'rates, counts and summaries measured (e.g. matcher precision/recall estimates)' },
  },
  required: ['findings', 'measurements'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },
    reproduced: { type: 'boolean' },
    rows_affected_measured: { type: 'string' },
    reasoning: { type: 'string' },
  },
  required: ['refuted', 'reproduced', 'rows_affected_measured', 'reasoning'],
}

const tracePrompt = (runs) => `${CTX}

TASK: blind, independent hand-trace of sampled loss-trace rows. You must NOT read, import or run 23-loss-trace.py, and must NOT open ${SP}/ltv/script_verdicts.json or ${SP}/ltv/lt_verify.json or any file under ${SP}/ltv/work written by others. Read the codebook (23-loss-trace.md) for the step definitions and sub-codes, then work from the raw run files with your own small scripts.

Rows to trace (from ${SP}/ltv/sample.json): the entries for these run dirs: ${JSON.stringify(runs)}.

For each row (run dir, fact_id, k): the gold value is the suite gold row with that fact_id under meeting index k (gold evidence "EL2020a:29" = transcript line 29 of that meeting in the suite's transcripts). Find the span the system saw: the memory_gatekeeper trace rows (mode llm) contain the span text after "Classify this span:\\n\\n" and the policy in output.extraction_policy; extraction rows contain the span after "Extract project-state claims from:\\n\\n" and the claims they produced. Claims in state.json link to evidence (evidence_id -> evidence text, meeting). conflict_detection rows (input.claim_id, input.state_key, output.result_type/proposal_id/reason) are each claim's evaluation trail; the preceding resolution row carries winning_value. Checkpoints: ami_eval_question steps; a write step's phase = number of checkpoints already questioned. Decide which facts held the value at checkpoint k (transaction time, not the end-of-run statuses), the status at k, and for asked rows the reader's resolved keys, facts given, answer and score (coldstart.json scorecard.scores[].correct).

Judge "carries the value" semantically, as a careful human coder would (you are not bound by any lexical matcher); set depends_on_wording_judgement when the verdict hinges on whether two wordings are the same value. Report the first failing step per the codebook (or "passes"), the sub-code, and the evidence. List any codebook ambiguity you hit.`

const comparePrompt = (runs, trace) => `${CTX}

TASK: compare a blind hand-trace with the script's verdicts and adjudicate every disagreement from the raw data.

Hand-trace result (independent coder, semantic judgement): ${JSON.stringify(trace)}

Script verdicts for the same rows: read ${SP}/ltv/script_verdicts.json, entries for ${JSON.stringify(runs)} (lower_bound = strong matches only; upper_bound = weak matches counted too; steps = each step's pass/fail). The full script output is ${SP}/ltv/lt_verify.json; you may import the script's functions (runpy.run_path on 23-loss-trace.py) to inspect its intermediate joins.

For each row: do they agree on the first failing step? If not, examine the raw run files and decide who is right per the codebook, and the cause: matcher_lexical_vs_semantic (the script's lexical matcher and a semantic reading differ — say which way), join_or_phase_bug, status_or_state_bug, codebook_ambiguity, hand_trace_error, other. Be skeptical of both sides. Separately list concrete defects in 23-loss-trace.py you found (file:line, reproducing row).`

const AUDITS = [
  { key: 'matcher', prompt: `${CTX}

TASK: audit the loss trace's lexical matcher (match_level, tokens, the locality rule for weak matches) for precision and recall against careful semantic judgement. Script output for six runs: ${SP}/ltv/lt_verify.json (records per run under lower/upper; adjudication_queue per run). You may import the script with runpy.run_path to recompute carriers (Run class, trace_row, match_level).
Measure, on the six runs:
(a) PRECISION of strong matches that decided a pass: sample at least 40 (row, carrier text) pairs where the lower bound passed 'carried' or 'applied' via a strong match, across runs and values (include short values such as F02 '20 April', F06 '42 languages', F21 'Czech and English', F26, F68, F69, F81 'three'); judge each semantically; report false-positive rate with examples.
(b) RECALL: for every row lost at carried:claims_without_the_value in one A0 run (a0_r1) and one A1 run (a1_r2), read the claims extracted from the cited span(s) and any claim by checkpoint k anywhere, and judge whether one semantically carries the gold value; report how many are matcher misses (and which texts).
(c) For rows with sub-code another_value_won or overwritten_by_non_gold_value in a1_r2 and a0_r1: is the winning/successor value actually the gold value in other words?
(d) Decide every adjudication_queue item across the six runs (fact_id, text): true if the text carries the gold value, false otherwise, with a one-line reason. Put these decisions in measurements as a YAML block (fact_id: {text: true|false}); they will be labelled as model adjudications, not human.
Report findings for systematic matcher defects (with the rows they change and a concrete fix).` },
  { key: 'code', prompt: `${CTX}

TASK: adversarial code review of thesis/notes/thesis_completion/artifacts/23-loss-trace.py against its codebook (23-loss-trace.md) and the application code that produced the traces. Look for defects that change counts or sub-codes. Check at least:
- phase assignment (ami_eval_question rows; steps interleaved with questions);
- the proposal-value join: for non-collection keys the script takes winning_value from the most recent resolution row with the same state_key before the conflict_detection row that first carries a proposal_id — verify against app/services/conflict_service.py (evaluate_claim and the E1 ruled-out branch, engine path, collection path) that this is always the right value, including reject proposals and repeated proposal ids (open-proposal dedup/refresh, bug-13 settle);
- fact placement (facts matched to proposals by key, value, type, ordered by valid_from) and current()/rejected_at()/status_at() for superseded, rejected-with-valid_to (demoted), and ruled-out records (rejected, valid_to None);
- the filing() reason prefixes against the exact strings in app code (Stage-23 repair (bug 5), Design cycle 2 parked/re-routed, 'Claim has no state key');
- NO_PROPOSAL_REASONS prefixes against the app's reason strings;
- reading-step logic (state_keys, facts + near_matches, scorecard correct), SINGLE_VALUE_FAMILIES, credit_without_state;
- demoted and ruled_out kinds; the question_map (exact value join and evidence id suffix);
- defect flags vs the definitions in 23-bug-incidence.py;
- consistency of codebook text with code (every sub-code the code can emit is documented and vice versa).
Run the script yourself (command in its docstring; run dirs: ${JSON.stringify(args.runs)}) with --out under ${SP}/ltv/work/. Each finding needs a concrete reproducing row or command.` },
  { key: 'txtime', prompt: `${CTX}

TASK: audit the loss trace's transaction-time reconstruction (Run.__init__: phases, claim_phase, proposals, created, created_by; current(), rejected_at(), status_at()) on the six runs ${JSON.stringify(args.runs)}. Use runpy.run_path to load the script's Run class.
Checks:
(1) claim_phase: for every claim, is the phase of the extraction call that produced it consistent with the claim's evidence meeting (meeting index j -> phase j, re-extractions later)? Count claims joined only by the fallback (join_counts) and claims whose extraction phase is earlier than their evidence meeting.
(2) proposals: for each proposal id, compare the script's (state_key, value, type, phase) with the dumped state.json proposals (state_key, value, status) — every dumped proposal should be matched by value; report mismatches.
(3) fact placement: count facts where several proposals share (key, value, type) so the ordering decides the phase; for A1 runs (repair_meeting_dates on, valid_from = meeting start) check created phase >= the meeting index of valid_from; for all runs check created phase <= phase of the fact's successor.
(4) Independently re-derive, for every question in answers.json, the set of non-rejected facts current at its checkpoint for each resolved key, and compare with the facts+near_matches the reader was given (the script's docstring claims 1023/1023 on two runs; extend to six runs) and the status in the pack vs status_at (claimed 6209/6210).
(5) Any case where a fact is current at k per the script but its value never reached the reader although its key was resolved — explain.
Report findings with reproducing rows.` },
]

const verifyPrompt = (f, key) => `${CTX}

TASK: try to REFUTE this finding about the loss trace (from the ${key} audit). Reproduce it from the raw files and the script. refuted=true if it does not reproduce, or if it does not change any count or sub-code and is not a documentation error. Measure the rows affected yourself.

Finding: ${JSON.stringify(f)}`

phase('Trace')
const groups = [args.runs.slice(0, 2), args.runs.slice(2, 4), args.runs.slice(4, 6)]
const [traceResults, auditResults] = await parallel([
  () => pipeline(groups,
    g => agent(tracePrompt(g), { label: `trace:${g.map(x => x.split('/').pop()).join('+')}`, phase: 'Trace', schema: TRACE_SCHEMA }),
    (t, g) => agent(comparePrompt(g, t), { label: `compare:${g.map(x => x.split('/').pop()).join('+')}`, phase: 'Compare', schema: COMPARE_SCHEMA }).then(c => ({ group: g, trace: t, compare: c }))),
  () => pipeline(AUDITS,
    a => agent(a.prompt, { label: `audit:${a.key}`, phase: 'Audit', schema: FINDINGS_SCHEMA }),
    (res, a) => parallel((res.findings || []).filter(f => f.severity !== 'minor').map(f => () =>
      agent(verifyPrompt(f, a.key), { label: `verify:${a.key}:${f.title.slice(0, 30)}`, phase: 'Verify', schema: VERDICT_SCHEMA })
        .then(v => ({ ...f, verdict: v })))).then(vs => ({ key: a.key, measurements: res.measurements, findings: vs.filter(Boolean), minor: (res.findings || []).filter(f => f.severity === 'minor') }))),
])
return { traces: traceResults, audits: auditResults }
