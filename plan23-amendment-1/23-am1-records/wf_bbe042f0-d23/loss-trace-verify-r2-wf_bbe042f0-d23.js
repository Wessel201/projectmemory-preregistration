export const meta = {
  name: 'loss-trace-verify-r2',
  description: 'Round-2 adversarial verification of loss trace v2: held-out blind hand-traces, code review, matcher audit, queue adjudication',
  phases: [
    { title: 'Trace', detail: 'blind hand-traces of held-out rows (A2 r1 and fresh A0/A1 rows)' },
    { title: 'Compare', detail: 'adjudicate disagreements with v2' },
    { title: 'Audit', detail: 'v2 code review, matcher audit on held-out A2, queue adjudication' },
    { title: 'Verify', detail: 'one skeptic per substantive finding' },
  ],
}

const SP = args.sp
const OUT = `${SP}/ltv2`
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol (run commands from there; python is .venv/bin/python).
The loss trace v2: thesis/notes/thesis_completion/artifacts/23-loss-trace.py; its codebook thesis/notes/thesis_completion/artifacts/23-loss-trace.md (read it: chain, sub-codes, matcher, bounds, transaction-time replay).
Suite (gold block from line ~1376, transcripts, questions): data/ami_eval/suites/transfer_el2020.yaml. Meetings EL2020a..d = checkpoints k=0..3.
Each run dir holds artifacts/*.coldstart.json (scorecard, config.cycle2_flags), *.state.json (claims, evidence, state_facts, proposals, state_key_definitions), *.answers.json, *.trace.json (steps: seam, mode, input, output; seams include memory_gatekeeper, extraction, resolution, conflict_detection, claim_support_check, filing_type_check, ami_eval_question).
Arms: A0 = evaluated system; A1 = all ten Stage-23 repairs; A2 = repairs plus the four design-cycle-2 write contracts (filing_type_check, resolution_same_meeting_conflict, supersession_requires_new_evidence, filing_support_check). App code under app/ is the authority on behaviour.
Runs: ${JSON.stringify(args.runs)}.
Offline only: never call any LLM/OpenAI API, never run the system live, never print .env. Do not edit any repository file; write scratch files only under ${OUT}/work/<your-own-subdir>/.`

const TRACE_SCHEMA = {
  type: 'object',
  properties: {
    rows: { type: 'array', items: { type: 'object', properties: {
      run: { type: 'string' }, fact_id: { type: 'string' }, k: { type: 'integer' },
      first_failing_step: { type: 'string' }, sub_code: { type: 'string' },
      evidence: { type: 'string' }, depends_on_wording_judgement: { type: 'boolean' },
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
      agree_step_with_adjudicated: { type: 'boolean' },
      agree_step_with_raw_strict: { type: 'boolean' },
      who_is_right: { type: 'string', enum: ['both', 'script', 'hand_trace', 'neither', 'codebook_ambiguous'] },
      cause: { type: 'string' }, explanation: { type: 'string' },
    }, required: ['run', 'fact_id', 'k', 'agree_step_with_adjudicated', 'agree_step_with_raw_strict', 'who_is_right', 'cause', 'explanation'] } },
    script_defects: { type: 'array', items: { type: 'string' } },
  },
  required: ['rows', 'script_defects'],
}
const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      title: { type: 'string' },
      severity: { type: 'string', enum: ['changes_counts', 'changes_subcodes', 'documentation', 'minor'] },
      location: { type: 'string' }, claim: { type: 'string' },
      estimated_rows_affected: { type: 'string' }, suggested_fix: { type: 'string' },
    }, required: ['title', 'severity', 'location', 'claim', 'estimated_rows_affected', 'suggested_fix'] } },
    measurements: { type: 'string' },
  },
  required: ['findings', 'measurements'],
}
const VERDICT_SCHEMA = {
  type: 'object',
  properties: { refuted: { type: 'boolean' }, reproduced: { type: 'boolean' }, rows_affected_measured: { type: 'string' }, reasoning: { type: 'string' } },
  required: ['refuted', 'reproduced', 'rows_affected_measured', 'reasoning'],
}
const ADJ_SCHEMA = {
  type: 'object',
  properties: {
    decisions: { type: 'array', items: { type: 'object', properties: {
      fact_id: { type: 'string' }, text: { type: 'string' }, carries: { type: 'boolean' }, reason: { type: 'string' },
    }, required: ['fact_id', 'text', 'carries', 'reason'] } },
    notes: { type: 'string' },
  },
  required: ['decisions', 'notes'],
}

const tracePrompt = (runs) => `${CTX}

TASK: blind, independent hand-trace of held-out loss-trace rows. You must NOT read, import or run 23-loss-trace.py, and must NOT open any file under ${OUT} except ${OUT}/sample.json, nor any file under ${SP}/ltv. Read the codebook (23-loss-trace.md) for the step definitions and sub-codes, then work from the raw run files with your own small scripts.

Rows to trace: the entries of ${OUT}/sample.json for run dirs ${JSON.stringify(runs)}.

For each row (run dir, fact_id, k): the gold value is the suite gold row with that fact_id under meeting index k (gold evidence "EL2020a:29" = transcript line 29 of that meeting). Locate the span the system saw via memory_gatekeeper rows (text after "Classify this span:\\n\\n", policy in output.extraction_policy) and extraction rows (text after "Extract project-state claims from:\\n\\n", claims produced). state.json claims link to evidence (evidence_id -> text, meeting); conflict_detection rows (input.claim_id/state_key, output.result_type/proposal_id/reason) are the logged evaluations; the preceding resolution row has winning_value; A2 parking is in claim.object.cycle2 and the claim_support_check / filing_type_check rows. Checkpoints: ami_eval_question steps; a write step's phase = number of checkpoints already questioned. Rebuild facts at checkpoint k in transaction time (not end-of-run statuses), the status at k, and for rows asked by a single-value question (one gold value asked) the reader's resolved keys, answer facts vs near matches, answer, and score (coldstart.json scorecard.scores[].correct).

Judge "carries the value" semantically, as a careful human coder would; set depends_on_wording_judgement when the verdict hinges on it. Report the first failing step per the codebook (or "passes"), the sub-code, and the evidence. List codebook ambiguities.`

const comparePrompt = (runs, trace) => `${CTX}

TASK: compare a blind hand-trace with the loss trace v2's verdicts and adjudicate every disagreement from the raw data.

Hand-trace result (independent coder, semantic judgement): ${JSON.stringify(trace)}

Script verdicts for the same rows: ${OUT}/script_verdicts.json, entries for ${JSON.stringify(runs)}: adjudicated_strict (strict bound with the round-1 model adjudications ${OUT}/adj_round1.yaml applied; the primary series), raw_strict, raw_lenient, steps. Full outputs: ${OUT}/lt_r2.json (adjudicated) and ${OUT}/lt_r2_raw.json; you may import the script (runpy.run_path) to inspect joins.

For each row: does the hand-trace's first failing step agree with adjudicated_strict, and with raw_strict? If not, examine the raw files and decide who is right per the codebook, and the cause (matcher_lexical_vs_semantic, join_or_phase_bug, status_or_state_bug, reading_logic, codebook_ambiguity, hand_trace_error, other). Be skeptical of both sides. List concrete defects in 23-loss-trace.py (file:line, reproducing row).`

const AUDITS = [
  { key: 'code', prompt: `${CTX}

TASK: adversarial code review of loss trace v2 (23-loss-trace.py) against its codebook and the application code. v2 rewrote v1 after a first review; the first review's confirmed defects were: strong matches counted from any span; sibling-alias collisions; placeholder digits; ordinals = cardinals; claims matched on object only; one-word values always weak; possessive/duplicate tokens/'mask-k'; negated-value polarity; list values split across claims; paraphrase misses in the other-gold test; evidence_only treated as not admitted; ruled-out records passing 'applied' for current rows; multi-value questions in reading and OR across questions; defect flags differing from 23-bug-incidence.py; unlogged evaluate_claim returns; applied_after_checkpoint vs expired; current sub-code from one arbitrary successor; fact placement by valid_from (now an exact replay); stale verification figures; status/reading inconsistency; credit_without_state missing reading losses; extracted_after_checkpoint missing.
(1) Check each is actually fixed, and that each fix is correct (no new defect). (2) Look for NEW defects introduced by v2: the Judge class (sibling rule via phrases(), the one-word upgrade, locality via the ±1 window and text-keyed local set), identity propagation (carried_kv: a proposal/fact holding a carrier claim's value under a key that claim was evaluated under), the replay (_replay) incl. reject proposals that demote vs create records, A2 parking dating (self.parked), reading per question (best question), filing() codes, applied/current sub-codes, demoted rows, the adjudication override, the queue construction, arm_summary, case pages. (3) Check codebook text against code (every sub-code emitted is documented and vice versa; the verification figures).
Run the script yourself (see its docstring) on the runs above with --out under your work dir. Each finding needs a reproducing row or command.` },
  { key: 'matcher', prompt: `${CTX}

TASK: audit the v2 matcher (match_level, phrases, Judge.level/counts, locality, identity propagation via carried_kv) on HELD-OUT data: the A2 run (${args.runs[args.runs.length - 1]}) was not used to design v2. Use ${OUT}/lt_r2_raw.json (raw bounds) and import the script with runpy to recompute.
Measure on the A2 run:
(a) PRECISION of the strict bound: census of every (fact_id, text) that decided a strict pass at carried, proposed or applied (including passes via identity propagation — then judge the claim text that carried); judge semantically (T carries / P fragment / X another gold value / F does not). Report rates and examples.
(b) RECALL: every strict row lost at carried (claims_without_the_value, no_claims_from_cited_span, split_across_claims): read the cited span's claims (subject|predicate|object) and claims by k anywhere; is any a semantic carrier? Report misses and causes.
(c) The sibling rule: list texts that v2 refuses (level None) or downgrades because of another row; judge whether the assignment is right.
(d) Lenient-only texts: precision of strong non-local matches and local weak ones.
Then also measure (a) on one A0 and one A1 run of your choice for comparison. Report systematic defects with fixes.` },
]

const adjudicatePrompt = `${CTX}

TASK: adjudicate the loss trace's open adjudication queue. ${OUT}/lt_r2.json holds, per run, 'adjudication_queue' (fact_id, text) — the texts still undecided after the round-1 model adjudications (${OUT}/adj_round1.yaml). Collect the union over all runs, dedupe, and for each (fact_id, text) decide whether the text carries the gold value of that fact_id (the suite gold row; read its value and aliases, and where useful the claim or fact the text comes from, with subject and predicate, and its span). "Carries" = a careful human coder would say this text states that gold value (not a fragment of a compound value unless the fragment is the value's core, not a different value, not merely the topic). Give a one-line reason each. These decisions will be stored as MODEL adjudications, labelled non-human.`

const verifyPrompt = (f, key) => `${CTX}

TASK: try to REFUTE this finding about loss trace v2 (from the ${key} audit). Reproduce it from the raw files and the script. refuted=true if it does not reproduce, or if it changes no count or sub-code and is not a documentation error. Measure the rows affected yourself.

Finding: ${JSON.stringify(f)}`

phase('Trace')
const groups = [[args.runs[args.runs.length - 1]], args.runs.filter(r => /a0_r2|a0_r3|el2020_a1_|a1_r3/.test(r))]
const [traceResults, auditResults, adjudication] = await parallel([
  () => pipeline(groups,
    g => agent(tracePrompt(g), { label: `trace:${g.map(x => x.split('/').pop()).join('+')}`, phase: 'Trace', schema: TRACE_SCHEMA }),
    (t, g) => agent(comparePrompt(g, t), { label: `compare:${g.length}runs`, phase: 'Compare', schema: COMPARE_SCHEMA }).then(c => ({ group: g, trace: t, compare: c }))),
  () => pipeline(AUDITS,
    a => agent(a.prompt, { label: `audit:${a.key}`, phase: 'Audit', schema: FINDINGS_SCHEMA }),
    (res, a) => parallel((res.findings || []).filter(f => f.severity !== 'minor').map(f => () =>
      agent(verifyPrompt(f, a.key), { label: `verify:${a.key}:${f.title.slice(0, 30)}`, phase: 'Verify', schema: VERDICT_SCHEMA })
        .then(v => ({ ...f, verdict: v })))).then(vs => ({ key: a.key, measurements: res.measurements, findings: vs.filter(Boolean), minor: (res.findings || []).filter(f => f.severity === 'minor') }))),
  () => agent(adjudicatePrompt, { label: 'adjudicate:queue', phase: 'Audit', schema: ADJ_SCHEMA }),
])
return { traces: traceResults, audits: auditResults, adjudication }
