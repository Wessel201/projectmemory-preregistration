export const meta = {
  name: 'am1-step0-build',
  description: 'Build the Step 0 package of plan 23 amendment 1: registers, claims register, mapping, probe note, pre-coder template',
  phases: [
    { title: 'Build', detail: 'design part, implementation part, claims sweeps, mapping, probe note, pre-coder template' },
    { title: 'Merge', detail: 'assemble the design-and-controls register and the claims register' },
  ],
}

const R = '/Users/wesselvansommeren/Documents/Project-Context-Protocol'
const A = R + '/thesis/notes/thesis_completion/artifacts'
const S = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad/step0'

const RULES = `
You are building one part of the Step 0 package for "plan 23, amendment 1" in the repository ${R}. The repository holds a master's thesis on ProjectMemory, an LLM system that turns meeting transcripts into maintained project state, and the system's code (app/). The amendment is ${A}/23-plan-amendment-1-ceilings-and-root-cause.md. Read its "Step 0" section, and whatever else your task names. The author has approved its text; never change it.

Hard rules:
- No LLM or embedding API calls of any kind, and no network access. Do not open, print or source the .env file. Do not run run-ami-eval, replay-ami-answers, or any CLI command or script that could call a model. Reading files, git show/log/diff/blame, grep, and pure-Python scripts over local files (with ${R}/.venv/bin/python) are fine.
- Do not modify any existing file. Do not run git commands that change state (no checkout, switch, stash, commit, reset, add). Read old versions with \`git show <commit>:<path>\`. Write only the output files your task names (create ${S} with mkdir -p if needed).
- Quote verbatim when you quote, and cite each source as path:line, or commit:path:line for old versions. Never paraphrase inside quotation marks. Mark your own glosses as glosses.
- Where something needs the author's judgement, do not decide it silently: put it in decisions_for_author, with the options and your recommendation.
- Style: plain formal English, short sentences, lists rather than long paragraphs, like the amendment. No marketing language.

Facts you can rely on (checked):
- Evaluated runs (EL2020 series, four meetings EL2020a-d, checkpoints k=0..3): A0 and A1 ran at commit 332037578beb88a91d1b0e41a4f67d632ffcd1c8 (short 3320375). A2 and RAG ran at b4d6b6c, whose only non-thesis change from 3320375 is one .gitignore line, so the code is the same.
- Run folders (gitignored, local): data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/{a0_r1,a0_r2,a0_r3,a1_r2,a1_r3}; data/ami_eval/a1_smoke/el2020_a1_20261022T211107Z (the A1 smoke run, i.e. a1_r1); data/ami_eval/a1_smoke/el2020_a2_rag_20261023T061545Z/{a2_r1,a2_r2b,a2_r3,rag_r1,rag_r2,rag_r3}. Each has artifacts/*.trace.json (keys run_id, mode, model, by_mode, by_seam, served_models, steps; each step has seam, workflow, mode ('llm' or '—'), model, served_model, input (the messages, as a Python-repr string), output, metrics), *.state.json, *.answers.json and *.coldstart.json. coldstart.json has a "config" block with the effective settings (model, resolver_embeddings, expansion_reuse_policy=semantic, expansion_reuse_threshold=0.8, judge_model=gpt-5.4-2026-03-05, cycle2_flags, ...).
- Seams recorded in the A1 and A2 traces: memory_gatekeeper, extraction, state_key_resolution, registry_expansion_generation, registry_expansion_review, resolution, conflict_detection, question_answering_grounding, question_answering, ami_eval_question; A2 adds claim_support_check and filing_type_check. The generator is gpt-5.4-mini (served gpt-5.4-mini-2026-03-17), temperature 0.0 (app/core/config.py:22; the run environment sets the same value). Embeddings: text-embedding-3-small.
- Arms: A0 is the evaluated system. A1 is A0 plus ten default-off repair switches (Phase B, commits 401f2c8 and 3320375). A2 is A1 plus four write contracts (filing_type_check, resolution_same_meeting_conflict, supersession_requires_new_evidence, filing_support_check). WD is the whole-decision extraction contract extraction_whole_decisions. Flags: app/core/cycle2_flags.py, and wherever the A1 repair switches are defined (find them).
- Parameters at app/core/config.py: embedding_top_k=8 (l.82), embedding_min_similarity=0.30 (l.83), resolver_prune_threshold=12 (l.86), expansion_reuse_threshold=0.80 (l.71), answer_relevance_min_similarity=0.42 (l.89), answer_canonical_min_similarity=0.80 (l.95). _prompt_registry: app/services/state_key_resolution_service.py:676. _reviewer_would_accept (the harness reviewer): app/evaluation/ami/informed_reviewer.py:78. Check all of these at 3320375, not only in the working tree.
- Ch. 4 of the thesis is thesis/implementation_chapter.tex. Its design decisions D1-D9 as worded at commit 94c049d (9 September 2026, before the cycle-1 runs) are extracted verbatim, with paragraph ids such as D4.p3, in ${A}/23-am1-design-text-94c049d.md. D10 and D11 entered at 5de9911 (19 October). Later commits touching the chapter: b422b27 (14 Sep), 50cf0f3 (15 Sep), c6fbdc0, 5de9911, 9b96138, 38a0f4a (19 Oct), b1b3454 (20 Oct).
- The loss trace: script ${A}/23-loss-trace.py, codebook ${A}/23-loss-trace.md, results ${A}/23-loss-trace-results.md, output ${A}/23-loss-trace.json. Chain of steps: admitted, carried, polarity, modality (boundary extraction); filed, proposed, applied (filing); current (state maintenance); status; key_reached, in_payload, answered (reading).
- Plan 23 is ${A}/23-plan-development-and-confirmation.md. Its Phase D3 mechanisms are: epistemic status, change and supersession, rejection, restraint on incidental talk (being removed by the amendment's Step 0 fixes), complete decisions, evidence and provenance, plus each contract.
`

const OUT = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    files_written: { type: 'array', items: { type: 'string' } },
    decisions_for_author: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, options: { type: 'string' }, recommendation: { type: 'string' } }, required: ['item', 'options', 'recommendation'] } },
    gaps: { type: 'array', items: { type: 'string' } },
  },
  required: ['summary', 'files_written', 'decisions_for_author', 'gaps'],
}

const CLAIMS = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    claims: { type: 'array', items: { type: 'object', properties: {
      quote: { type: 'string', description: 'verbatim LaTeX source of the claim sentence(s)' },
      file: { type: 'string' }, line: { type: 'integer' }, label: { type: 'string', description: 'nearest \\label or section' },
      claim: { type: 'string', description: 'the causal claim in one plain sentence (gloss)' },
      kind: { type: 'string', enum: ['where', 'why', 'where and why'] },
      boundaries: { type: 'array', items: { type: 'string' } },
      mechanisms: { type: 'array', items: { type: 'string' } },
      confirm: { type: 'string' }, overturn: { type: 'string' },
      action_if_confirmed: { type: 'string' }, action_if_overturned: { type: 'string' },
      testable_here: { type: 'string', enum: ['yes', 'partly', 'no'] },
      note: { type: 'string' },
    }, required: ['quote', 'file', 'line', 'label', 'claim', 'kind', 'boundaries', 'mechanisms', 'confirm', 'overturn', 'action_if_confirmed', 'action_if_overturned', 'testable_here', 'note'] } },
    dormant: { type: 'array', items: { type: 'object', properties: { quote: { type: 'string' }, file: { type: 'string' }, line: { type: 'integer' }, note: { type: 'string' } }, required: ['quote', 'file', 'line', 'note'] } },
    decisions_for_author: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, options: { type: 'string' }, recommendation: { type: 'string' } }, required: ['item', 'options', 'recommendation'] } },
  },
  required: ['summary', 'claims', 'dormant', 'decisions_for_author'],
}

const CLAIM_TASK = (files) => `${RULES}
Your task: one third of the CLAIMS REGISTER sweep. Read the live (uncommented) LaTeX of: ${files} (in ${R}/thesis, at the working tree, which equals HEAD for the thesis). Lines starting with % are commented out.

The amendment's definition: "One row per causal claim the thesis text now makes about where or why the system loses information. Each row gives: the claim and its location; the result here that would confirm it, and the one that would overturn it; the text action in either case."

Include every sentence that says or implies WHERE in the pipeline information is lost or kept (admission/gatekeeper, extraction, key assignment or routing or filing, state maintenance and supersession/conflicts, reading/answering), or WHY it is lost or why a mechanism succeeds or fails (a design decision, a trade-off, the conversation's difficulty, the model, an implementation defect, the evaluation). That includes claims that a mechanism works or does not work, claims about what limits the score, explanations of the RAG gap, claims about vagueness or write-time normalisation, about restraint, about change/supersession/rejection handling, and design-cost claims ("the cost of D4 is ..."). Exclude pure descriptions of how the system is built that make no claim about loss, and claims only about RAG's own internals.

For each claim:
- quote it verbatim (the LaTeX source; long sentences may be cut with [...] but never reworded);
- confirm / overturn: name the concrete result of THIS amendment's study that would confirm or overturn it. The available results are: the loss trace's first-loss tables per arm (surfaced-at); the Step 2 oracles R, E+R, E+R* (row results and the caused-at they set); the A2 leave-one-out and the reviewer ceiling; the Step 2b probes (i) extraction (b, b2, c, d), (ii-r)/(ii-h) routing, (iii) question time; the Step 2c WD result; the Step 3 codes (caused-at x class tables, eight classes: implementation defect, architectural weakness, design trade-off, conversational difficulty, evaluation defect, model-limited, design-or-model-not-separated, unclear) under the bound rule and the 0.40 kappa rule; the Step 5 ES2009 runs and 3b codes. Be specific (which table, which direction, roughly what size). If the study cannot test it, say so and set testable_here to 'no' or 'partly';
- action_if_confirmed / action_if_overturned: the text change (keep and cite; qualify; rewrite as ...; remove), in a few words.
Also list dormant claims: commented-out passages that make such claims (they may be restored later). Return everything in the schema; write no files.`

phase('Build')
const designAndImpl = () => parallel([
  () => agent(`${RULES}
Your task: the DESIGN PART of the "design-and-controls register" (amendment Step 0, first bullet). Write it to ${S}/design_part.md.

The register is organised by component: admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading. Put D1 and D9 (and anything else that constrains all components) in a short "cross-cutting" block, and cross-reference it from the components it binds.

For each component give:
1. **Design entries (94c049d).** Every paragraph of ${A}/23-am1-design-text-94c049d.md that governs this component, by id (e.g. D4.p3), each with the operative sentence(s) copied exactly from that file, and a one-line gloss of what it commits the component to. Two lists matter most for later coding, so make them explicit:
   - **Inputs the design gives this step** (the amendment's criterion (ii): "the prompt omits information the register gives that step"). Only what the 94c049d text gives; say "not specified by the design" where it is silent.
   - **What the design requires the step to do or not do** (the basis for conformance: "the code contradicts the register").
   Check every one of the 52 D-paragraphs and the rationale table; list at the end any paragraph you assign to no component, with the reason.
2. **Retrospective entries.** Everything written after 9 September that could be read as design for this component, each marked retrospective, with commit, date and verbatim text:
   - D10 and D11 (current text in thesis/implementation_chapter.tex; entered at 5de9911);
   - every change after 94c049d to the wording of D1-D9 (use git log -p 94c049d..HEAD -- thesis/implementation_chapter.tex; give before/after quotes for each changed passage that bears on a component);
   - other post-9-September design text, e.g. the specifications of the cycle-2 contracts and WD (find where they were specified: plan documents under thesis/notes/thesis_completion/, docstrings in app/core/cycle2_flags.py) and decisions in plan 23 such as "Bug 3: A1 uses the Ch. 4 rule". List them as retrospective design alternatives with location.
   - The 38a0f4a sentence that the autonomous arm leaves conflicts open: list it, marked "not a design entry (reports a Chapter 5 observation)", as the amendment says; the design text is D5's "leaving unresolved cases reviewable".
3. **Step type.** Whether the component is an LLM step or a deterministic step, or mixed (say which sub-steps are which), with the seams from the traces and the code entry points at 3320375 (path:line). Note where an arm (A1, A2, WD) adds an LLM call to a component (e.g. A2's claim_support_check, filing_type_check).

Start the file with a short header: what it is, source commit, how ids are cited, and that the amendment's rule applies: only 94c049d text can ground architectural weakness or a trade-off; retrospective entries never can.`, { label: 'design part', phase: 'Build', schema: OUT }),
  () => agent(`${RULES}
Your task: the IMPLEMENTATION and HELD-CONSTANT parts of the "design-and-controls register" (amendment Step 0, first bullet: "Implementation: the evaluated prompt texts, including the example roles and the registry they carry. Also the parameter values ..., the resolver shortlist and pruning, and the harness reviewer _reviewer_would_accept. Prompt text is implementation even where it is older than cycle 1. Held-constant controls: the generator gpt-5.4-mini at temperature 0 (shared with RAG), text-embedding-3-small, and the judge.").

Write three files:
(a) ${A}/23-am1-prompts.py — a pure-local script (no network, no model calls; reads only the trace.json files listed above) that extracts, for each seam and arm, the distinct STATIC prompt texts actually sent (system messages, and the fixed parts of user-message templates where you can separate them), with call counts and SHA-256 hashes, and writes ${A}/23-am1-prompts-evaluated.md with the full text of each distinct static prompt. Where a prompt embeds dynamic content (the registry, the span text), split the static part from the dynamic part with a documented rule, and report how many distinct static variants each seam has per arm (ideally one). Use the same docstring/usage style as ${A}/23-am1-design-text.py. Run it.
(b) ${S}/impl_part.md — organised by the same components (admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading). For each:
   - **Evaluated prompts:** seam; prompt builder at 3320375 (path:line); the static-prompt hash(es) from (a) per arm; the example roles and examples the prompt carries (quote them); how the registry enters the prompt (which function, which selection rule — e.g. _prompt_registry's lexical and embedding parts —, what fields of each key are shown); anything the prompt does not show that the step later needs. Mark which of these differ under A1 switches, A2 contracts or WD.
   - **Parameters:** every parameter on that component that selects, excludes, admits, ranks or thresholds an item (key, claim, fact, evidence), with its value in the runs (config default at 3320375, confirmed against the coldstart.json config block where recorded), path:line, and one line on what it decides. Include at least the ones listed in the facts, plus whatever else you find (shortlists, prune sizes, settle/expiry windows, confidence ties, scalar focus gate, deterministic widening, answer similarity thresholds, embedding candidate counts).
   - **Deterministic logic that decides filing or state:** the resolver shortlist and pruning; registry expansion (generation, the semantic reuse policy, review); the harness reviewer _reviewer_would_accept (quote its rules, path:line); the resolution engine, conflict service, proposal/settle and projection rules, with path:line — briefly, as a checklist of implementation entries.
   - **Arm-specific implementation:** the ten A1 repair switches (name, what each changes, path:line) and the A2 contracts and WD (name, what each changes, which seam/LLM call it adds).
(c) Inside impl_part.md, a final section **Held-constant controls**: generator (model id, served snapshot from the traces, temperature, response format, max tokens or other call settings, from the client code at 3320375); embedding model and how it is called; the judge (model id gpt-5.4-2026-03-05 per coldstart config, its prompt location, its call settings); RAG's generator settings (shared). Say where each value is recorded in the run artifacts.`, { label: 'implementation part', phase: 'Build', schema: OUT }),
]).then(parts => agent(`${RULES}
Your task: MERGE the two parts of the design-and-controls register into one file, ${A}/23-am1-register-design-and-controls.md.
Inputs: ${S}/design_part.md (design entries, retrospective entries, step type) and ${S}/impl_part.md (implementation entries, held-constant controls). The builders' summaries: ${JSON.stringify(parts)}.
Structure: a header (what the register is, the amendment's rules on design vs retrospective vs implementation entries, the source commits, the companion files 23-am1-design-text-94c049d.md and 23-am1-prompts-evaluated.md); then one section per component (admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading), each with: step type; design entries (inputs given, requirements); retrospective entries; implementation entries (prompts, parameters, deterministic logic, arm-specific); then a cross-cutting section; then the held-constant controls; then a "register sheet per boundary" — for each caused-at boundary, the checklist the case pages carry (amendment Step 3: "The per-boundary register sheet is a checklist: the page addresses every listed candidate cause for its caused-at boundary"), built from the amendment's candidate-cause table plus the implementation entries and the design requirements for that boundary. Boundaries for the sheets: extraction, key assignment at extraction, key resolution and expansion, state rules, reading (and A2's support check under state rules).
Keep every verbatim quote and citation exactly as in the parts; do not re-quote from memory. Remove duplication. Do not drop content; if the parts conflict, keep both and flag it in decisions_for_author.`, { label: 'merge register', phase: 'Merge', schema: OUT }))

const claimsAndMapping = () => parallel([
  () => agent(CLAIM_TASK('main.tex (the abstract and Ch. 1, including any \\begin{abstract} and the introduction), conclusion.tex (Ch. 6), problem_domain.tex (Ch. 2), background.tex (Ch. 3)'), { label: 'claims: abstract, Ch1-3, Ch6', phase: 'Build', schema: CLAIMS }),
  () => agent(CLAIM_TASK('implementation_chapter.tex (Ch. 4), appendix_reproducibility.tex, appendix_walkthrough.tex, appendix_design_evidence.tex'), { label: 'claims: Ch4, appendices', phase: 'Build', schema: CLAIMS }),
  () => agent(CLAIM_TASK('eval.tex (Ch. 5). It is long (about 1,285 lines); read all of it'), { label: 'claims: Ch5', phase: 'Build', schema: CLAIMS }),
  () => agent(`${RULES}
Your task: the MECHANISM MAPPING that the claims register carries (amendment Step 0: "It also carries the mapping from boundaries and sub-causes to the mechanisms (complete decisions, change and supersession, rejection, evidence and provenance, and each contract). The mapping signed here governs every Phase C verdict."). Write it to ${S}/mapping_part.md.

Read: plan 23's Phase D3 mechanism list and verdict text; the amendment (Steps 2-5, especially the classes, candidate causes, the bound rule, which scales "for each mechanism, the cases that weaken it", and the admission rule); the loss-trace codebook ${A}/23-loss-trace.md and the sub-codes the script ${A}/23-loss-trace.py actually emits (list every (step, sub) pair present in ${A}/23-loss-trace.json, over all runs and row kinds: current, candidate, ruled_out, demoted); the gold families in data/ami_eval/suites/transfer_el2020.yaml (question families and row kinds).

Mechanisms: epistemic status (polarity, modality, lifecycle status), change and supersession, rejection, complete decisions, evidence and provenance, and each contract: the four A2 contracts, WD, and the read contract (evidence fallback, answerability). Restraint on incidental talk is removed by the amendment's Step 0 fixes: say so and map nothing to it.

Produce:
1. A table: each (boundary, step, sub-code) and each candidate implementation cause (from the amendment's candidate-cause table) -> the mechanism(s) whose verdict it weakens or supports, with the rule used (e.g. by row kind: a ruled_out row lost at polarity weakens rejection; a demoted row weakens change and supersession; a current row lost at carried with claims_without_the_value weakens complete decisions).
2. The rule for a case touching more than one mechanism (counted for each, or primary only) — propose one and flag it.
3. For each mechanism: its endpoint population (which gold rows and questions belong to it), consistent with plan 23's "architectural mechanisms are judged by their family endpoint against RAG; the loss trace shows at which boundary their failures arise" and the amendment's bound rule; and for each contract, its on/off contrast and the cases that are its measured effect (amendment: WD's (iv) cases; an A2 contract's leave-one-out cases).
4. Every gap or ambiguity, as decisions_for_author.`, { label: 'mechanism mapping', phase: 'Build', schema: OUT }),
]).then(([c1, c2, c3, map]) => agent(`${RULES}
Your task: ASSEMBLE the claims register, ${A}/23-am1-register-claims.md.
Inputs: three sweeps of the thesis text (JSON below) and the mechanism mapping at ${S}/mapping_part.md (its builder's summary is in the JSON too).
Structure:
- Header: what the register is (amendment Step 0, second bullet), the commit the line numbers refer to (run \`git rev-parse HEAD\`), the rule that the mapping signed here governs every Phase C verdict and that the Phase D3 registration may revise it for Phase D only, in a dated note.
- The claims table, one row per claim, ids C01, C02, ... in thesis order (abstract, Ch. 1, ..., appendices). Columns: id; location (file:line, label); claim (gloss) with the verbatim quote below or in a details line; where/why; boundaries; mechanisms; confirms if; overturns if; text action if confirmed; text action if overturned; testable here. Merge exact duplicates (the same claim in two places becomes one row listing both locations; the thesis aims at one home per claim, so flag claims stated in more than one place).
- A short list of claims the study cannot test, with the text action proposed for each.
- Dormant (commented-out) claims, listed apart.
- The mechanism mapping (copy ${S}/mapping_part.md in, unchanged in substance).
- Do not drop any claim from the sweeps. Keep every verbatim quote exactly as given; spot-check 10 quotes against the .tex files with grep and fix any that do not match the source.
Sweeps and mapping summary: ${JSON.stringify({ sweep_front_and_ch6: c1, sweep_ch4_appendices: c2, sweep_ch5: c3, mapping: map })}`, { label: 'assemble claims register', phase: 'Merge', schema: OUT }))

const others = () => parallel([
  () => agent(`${RULES}
Your task: the PROBE NOTE (amendment Step 0: "The probe note: the neutral example text for (b2), and gpt-5.4's settings for (d), fixed and dated."). Write ${A}/23-am1-probe-note.md, dated 27 October 2026.
Read the amendment's Step 2b (probe (i) conditions a, b, b2, c, d) first.
Part 1, neutral examples for (b2): find, at 3320375, the extraction prompt's examples (the "AMI role examples" — examples drawn from the AMI remote-control design meetings, with roles such as project manager or industrial designer; confirm what they actually are, with path:line and verbatim quotes, and cross-check against the recorded extraction system prompt in a trace.json). Then write replacement examples that:
- teach exactly the same things (same count, same output fields and JSON shape, same polarity/modality/rejection/supersession cases, same roles of each example), so that only the domain changes;
- come from a neutral domain that is neither AMI product design nor ELITR/EL2020 (speech, annotation, language data, research projects) nor anything in the gold of ES2009 or EL2020 (check data/ami_eval/gold/reviewed/EL2020.reviewed.yaml and the ES2009 gold under data/ami_eval/gold/ so no value or topic overlaps);
- have about the same length.
Give an exact substitution spec: which strings in the prompt are replaced by which (old text quoted verbatim, new text verbatim), so the probe can apply it mechanically, and a SHA-256 of the resulting static prompt if you can compute it locally.
Part 2, settings for (d) (gpt-5.4 with the recorded prompt): the model id (the judge already uses gpt-5.4-2026-03-05 per the runs' coldstart config; find how the judge calls it — temperature, response format, reasoning or other parameters — in the code at 3320375), and the settings the probe uses: the same request as the recorded gpt-5.4-mini call with only the model changed, plus whatever parameter differences the API requires for gpt-5.4 as evidenced by the judge's working calls in the code. Fix a rule now for any parameter the model rejects at run time (e.g. drop it and record that), since no test call is allowed. Do not invent API parameters; cite the code.
Part 3: list the probe conditions' other fixed inputs the amendment leaves to the note, if any, and anything still open as decisions_for_author.`, { label: 'probe note', phase: 'Build', schema: OUT }),
  () => agent(`${RULES}
Your task: the MODEL PRE-CODER'S PROMPT TEMPLATE (amendment Step 0: "The model pre-coder's prompt template, fixed and dated", and Step 3, item 3: "The model pre-codes every case from the page only, in a fresh context with no repository memory or result reports. It uses the template fixed at signing, and the frozen sub-cause list is its only added input."). Write ${A}/23-am1-precoder-template.md, dated 27 October 2026.
Read the amendment's Step 3 in full (unit, classes table, class rules incl. burden, pending results, retrospective design, WD cases, held: conflict decision, unclear, recoverability; caused-at; candidate causes; case pages; order of work and blindness; agreement measures). Read what a blind case page contains: the case_page function and the --case-pages option in ${A}/23-loss-trace.py, and the amendment's list of what case pages carry.
The template must contain:
1. The full prompt text, with placeholders: {CASE_PAGE} (the case page, inlined), {SUBCAUSES} (the frozen sub-cause list from the pilot), {REGISTER_SHEET} (the per-boundary register checklist, if the page does not already carry it). Nothing else may be added at run time.
2. The coding instructions, faithful to the amendment: the eight labels and their definitions; the burden rule and the LLM-step rule; pending alternatives and the CONDITIONAL code (what the case gets if every pending output comes back not recovered or does not move the boundary); held: conflict decision; retrospective entries never ground architectural or trade-off; recoverability limits on conversational difficulty; caused-at (earliest boundary where a correction inside it alone would have prevented the loss; never defaults to the surfacing step; unclear allowed); within routing, the misrouted claim's path; WD-case handling.
3. A strict JSON output schema with: case_id; surfaced_at (copied from the page); caused_at (boundary or "unclear"); class (one of the eight labels, exact strings); sub_cause (from {SUBCAUSES} or "none fits"); for implementation, which criterion (i)-(iv) or conformance; pending (list of sealed outputs the code depends on: probe id, offline reading check, oracle row result, A2 leave-one-out, WD result); checklist (each register-sheet item: ruled out / counts / pending / not applicable, with the evidence line from the page); evidence (quotes from the page); unclear_reason. The fields must cover what the agreement measures need (Cohen's kappa on the eight labels, the binary implementation-vs-not with unclear counted as implementation, kappa on caused-at, sub-cause agreement, share of pending cases).
4. Run conditions, as requirements: one case per call; page only; no tools, no file or repository access, no memory or result reports; which model (propose the Claude model the author uses for the other model adjudications, and flag it as a decision); how blindness is checked. Do not invent CLI flags or tool features; describe the requirement and list concrete options as decisions_for_author.
5. A check that nothing in a blind case page leaks a sealed output (Step 2/2b/2c results, oracle results, other coders' codes). Inspect the case_page code and say what it prints; flag any field that should be withheld.`, { label: 'pre-coder template', phase: 'Build', schema: OUT }),
])

const [reg, claims, oth] = await parallel([designAndImpl, claimsAndMapping, others])
return { register: reg, claims, probe_note: oth && oth[0], precoder: oth && oth[1] }
