export const meta = {
  name: 'loss-trace-r3',
  description: 'Loss trace v3: double-blind adjudication of the queue with tie-breaks, blind hand-traces on held-out A2 runs, v3 code review',
  phases: [
    { title: 'Adjudicate', detail: 'two independent adjudicators per item group' },
    { title: 'Tie-break', detail: 'third adjudicator on disagreements' },
    { title: 'Trace', detail: 'blind hand-traces on held-out A2 r2b and r3' },
    { title: 'Review', detail: 'adversarial code review of v3' },
    { title: 'Verify', detail: 'one skeptic per substantive finding' },
  ],
}

const SP = args.sp
const D = `${SP}/ltv3`
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol (run commands from there; python is .venv/bin/python).
Loss trace v3: thesis/notes/thesis_completion/artifacts/23-loss-trace.py; codebook thesis/notes/thesis_completion/artifacts/23-loss-trace.md.
Suite (gold block from line ~1376, transcripts, questions): data/ami_eval/suites/transfer_el2020.yaml; meetings EL2020a..d = checkpoints k=0..3.
Runs (EL2020; A0 = evaluated system, A1 = ten Stage-23 repairs, A2 = repairs + four design-cycle-2 write contracts): ${JSON.stringify(args.runs)}.
Offline only: never call any LLM/OpenAI API, never run the system live, never print .env. Do not edit repository files; scratch only under ${D}/work/<your-own-subdir>/.`

const STANDARD = `ADJUDICATION STANDARD. For each item, decide whether the TEXT carries the GOLD VALUE of its fact_id. "Carries" means: a careful coder would say the text states that gold value, so that an answer built from this text would be judged correct for a question asking for that value. Specifically:
- A paraphrase, a more specific or a more complete statement of the same value carries it.
- For a value made of two or more independent parts (e.g. "small MP3 files; a readme with cluster links for files too long", "the team does the automated processing; all manual refinement goes to the annotators"), a text stating only one part does NOT carry it, even if that part is listed as a gold alias. A text that states the main decision and leaves out a minor qualifier (e.g. "30 minutes, close at quarter to 5" for "30 minutes, closing sharply at quarter to five") DOES carry it.
- A text about the same topic that states a different value, a rival option, another gold value (a sibling fact), or only the topic words, does NOT carry it.
- For ruled-out values (kind ruled_out): the text carries it if it names the ruled-out option (its polarity is judged elsewhere; judge only whether the option named is the gold option).
- For demoted values: as for current values (the text names that same earlier value).
- Use the contexts (claim subject | predicate | object, the key it was filed under, the span) to understand what the text means; a fact's text is read with its key. If the same text means different things in different contexts, decide by its most common context and say so.
Return carries true/false and a one-line reason for every item, including items with a previous decision (re-check those under this standard; say "changed" in the reason if you differ).`

const ADJ_SCHEMA = {
  type: 'object',
  properties: {
    decisions: { type: 'array', items: { type: 'object', properties: {
      fact_id: { type: 'string' }, text: { type: 'string' }, carries: { type: 'boolean' }, reason: { type: 'string' },
    }, required: ['fact_id', 'text', 'carries', 'reason'] } },
  },
  required: ['decisions'],
}
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

const adjPrompt = (facts, who) => `${CTX}

TASK (adjudicator ${who}, working independently): ${STANDARD}

Your items: every entry of ${D}/adj_items.json whose fact_id is one of ${JSON.stringify(facts)}. Each entry has the gold value, aliases, kind, gold evidence lines, the questions asking for the value, and up to four contexts where the text occurs. You may read the suite (gold rows, transcript lines) and the run files for more context. Do not read any other adjudicator's output or ${D}/work. Return a decision for every one of your items, with the exact fact_id and text strings.`

const tiePrompt = (items) => `${CTX}

TASK (tie-break adjudicator): two independent adjudicators disagreed on the items below. ${STANDARD}

Items, with both adjudicators' decisions and reasons (look up more context in ${D}/adj_items.json, the suite and the run files as needed): ${JSON.stringify(items)}

Return your decision for every item (exact fact_id and text).`

const tracePrompt = (runs) => `${CTX}

TASK: blind, independent hand-trace of held-out loss-trace rows. You must NOT read, import or run 23-loss-trace.py, and must NOT open any file under ${SP}/ltv, ${SP}/ltv2 or ${D} except ${D}/sample.json. Read the codebook (23-loss-trace.md) for step definitions and sub-codes, then work from the raw run files with your own small scripts.

Rows to trace: the entries of ${D}/sample.json for run dirs ${JSON.stringify(runs)}.

For each row (run dir, fact_id, k): the gold value is the suite gold row with that fact_id under meeting index k (gold evidence "EL2020a:29" = transcript line 29 of that meeting). Locate the span the system saw via memory_gatekeeper rows (text after "Classify this span:\\n\\n", policy in output.extraction_policy) and extraction rows (text after "Extract project-state claims from:\\n\\n", claims produced). state.json claims link to evidence; conflict_detection rows are the logged evaluations (the preceding resolution row has winning_value); A2 parking is in claim.object.cycle2 with claim_support_check / filing_type_check rows. Checkpoints: ami_eval_question steps; a write step's phase = number of checkpoints already questioned. Rebuild facts at checkpoint k in transaction time (accepted proposals in creation order create facts; the dump shows end-of-run statuses), the status at k, and for rows asked by a single-value question the reader's resolved keys, answer facts vs near matches, answer and score.

Judge "carries the value" by this standard: ${STANDARD.replace('ADJUDICATION STANDARD. For each item, decide whether the TEXT carries the GOLD VALUE of its fact_id. ', '')}
Report the first failing step (or "passes"), the sub-code and the evidence. List codebook ambiguities.`

const reviewPrompt = `${CTX}

TASK: adversarial code review of loss trace v3 (23-loss-trace.py) against its codebook (which still describes v2 in places; note mismatches) and the application code. v3 changed, relative to v2: the sibling rule (rows sharing a gold evidence line are not siblings; an equally shared part stays with the row the text is local to; phrases() always adds the covered part; aliases must occur as a phrase within a window, _near); one-word upgrade extended to distinctive aliases (_distinctive); required numbers exclude the determiner 'one'; stemmer (undoubling, irregulars); claim-level adjudication (claim_text: a decision on the object or the subject+predicate+object text decides the claim); identity propagation only from claims whose object carries, or when the key's words plus the value still match (carried_kv, trail rows by k); holds() checks adjudications first; the queue now holds every text that decides a strict pass (support per step), plus lenient-only texts that change the outcome, plus wording pairs from both bounds; primary_series_complete flag; split_across_claims via the judge and a new sibling_value_only sub-code; displaced decided on the immediate successor with later_gold_in_chain; applied_after_checkpoint removed; not_current marked unreachable; defect flags limited to events by k; credit_without_state per question; arm label requires all four contracts; A2 parking dated with a value check on reason collisions; status_at reads the dumped (final) proposal reason; case pages neutralise arm-revealing reasons and show parking by k and claims extracted after k; 'null' keys are filed (A0 bug 5).
Check each change is correct and look for new defects. Run the script (see its docstring) with --adjudications ${D}/adj_r12.yaml and without, --out under your work dir. Every finding needs a reproducing row or command.`

const verifyPrompt = (f) => `${CTX}

TASK: try to REFUTE this finding about loss trace v3. Reproduce it from the raw files and the script. refuted=true if it does not reproduce, or if it changes no count or sub-code and is not a documentation error. Measure the rows affected yourself.

Finding: ${JSON.stringify(f)}`

const groups = args.groups
const heldout = args.runs.filter(r => /a2_r2b|a2_r3/.test(r))

const [adjResults, traceResults, review] = await parallel([
  () => pipeline(groups,
    async (facts, _o, i) => {
      const [a, b] = await parallel([
        () => agent(adjPrompt(facts, 'A'), { label: `adj:A:g${i}`, phase: 'Adjudicate', schema: ADJ_SCHEMA }),
        () => agent(adjPrompt(facts, 'B'), { label: `adj:B:g${i}`, phase: 'Adjudicate', schema: ADJ_SCHEMA }),
      ])
      return { facts, a: (a && a.decisions) || [], b: (b && b.decisions) || [] }
    },
    async (r, _o, i) => {
      const key = d => `${d.fact_id}\u0000${d.text}`
      const bmap = new Map(r.b.map(d => [key(d), d]))
      const amap = new Map(r.a.map(d => [key(d), d]))
      const disagree = []
      for (const [k, da] of amap) {
        const db = bmap.get(k)
        if (!db || db.carries !== da.carries) disagree.push({ fact_id: da.fact_id, text: da.text, A: db ? da : da, B: db || null })
      }
      for (const [k, db] of bmap) if (!amap.has(k)) disagree.push({ fact_id: db.fact_id, text: db.text, A: null, B: db })
      let tie = []
      if (disagree.length) {
        const t = await agent(tiePrompt(disagree), { label: `tie:g${i}`, phase: 'Tie-break', schema: ADJ_SCHEMA })
        tie = (t && t.decisions) || []
      }
      return { ...r, disagree, tie }
    }),
  () => parallel(heldout.map(rd => () => agent(tracePrompt([rd]), { label: `trace:${rd.split('/').pop()}`, phase: 'Trace', schema: TRACE_SCHEMA }).then(t => ({ run: rd, trace: t })))),
  () => agent(reviewPrompt, { label: 'review:v3', phase: 'Review', schema: FINDINGS_SCHEMA }).then(res => !res ? null :
    parallel((res.findings || []).filter(f => f.severity !== 'minor').map(f => () =>
      agent(verifyPrompt(f), { label: `verify:${f.title.slice(0, 30)}`, phase: 'Verify', schema: VERDICT_SCHEMA }).then(v => ({ ...f, verdict: v }))))
      .then(vs => ({ measurements: res.measurements, findings: vs.filter(Boolean), minor: (res.findings || []).filter(f => f.severity === 'minor') }))),
])
return { adjudication: adjResults, traces: traceResults, review }
