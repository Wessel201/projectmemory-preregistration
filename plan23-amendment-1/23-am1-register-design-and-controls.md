# Design-and-controls register

Plan 23, amendment 1, Step 0, first bullet. **Draft for signing** with the amendment; not signed. Assembled on 27 October 2026 from two parts built that day: the design part, and the implementation and held-constant part. Both were built offline from git history and local run files, with no model or embedding calls and no network access. No existing file was changed.

## What this register is

**What the amendment asks for** (Step 0, first bullet):
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:101`: "For each component (admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading), it lists three kinds of entry."
- Design entries, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:102`: "the Ch. 4 decisions **as worded at 94c049d (9 September, before the cycle-1 runs), quoted verbatim.**"
- Retrospective entries, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:103`: "D10 and D11, which entered at 5de9911 on 19 October;" Line 104 is quoted below.
- Step type, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:106`: "Each component also records whether it is an **LLM step** or a **deterministic step**."
- Implementation entries, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:107`: "the evaluated prompt texts, including the example roles and the registry they carry." The rest of that line is quoted under K2-R6.
- Held-constant controls, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:108`: "the generator gpt-5.4-mini at temperature 0 (shared with RAG), text-embedding-3-small, and the judge."
- Use on the case pages, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:397`: "the register checklist for the boundary." Line 334 is quoted at the head of the register sheets.

**How this file is organised.**
- One section per component: A admission, E extraction, K1 key assignment at extraction, K2 key resolution and expansion, S state rules, R reading. Each section gives, in this order:
  1. the step type: LLM or deterministic, the trace seams and calls, and the code entry points;
  2. the design entries as worded at 94c049d, the inputs the design gives the step, and what the design requires the step to do or not do;
  3. the retrospective entries;
  4. the implementation entries: evaluated prompts, parameters, deterministic logic, and what each arm changes.
- X: cross-cutting entries. D1 and D9 bind every component; the A1, A2 and WD switches act on several.
- H: the held-constant controls.
- Register sheets: one checklist per caused-at boundary, for the case pages.
- Then the coverage of the design-text file, the decisions for the author, an annex of other 94c049d Chapter 4 text, the limits of this register, the checks, and the review record.
- The mapping from boundaries and sub-causes to mechanisms is not in this register. It belongs to the claims register (`23-am1-register-claims.md`).

**The amendment's rule.** Only 94c049d text can ground architectural weakness or a design trade-off. Retrospective entries never can.
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:326`: "the loss follows from a design decision **as worded at 94c049d**, quoted on the case page"
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:347`: "A retrospective entry can never ground architectural weakness or a trade-off, nor rule out an alternative."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:348`: "A case whose only design ground is a retrospective entry is coded implementation choice if an alternative consistent with the 94c049d text meets (i)–(iv). Otherwise it is unclear."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:31`: "No loss becomes a design limit by default, by a threshold, by a cap on repairs, or on the strength of design text written after the results."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:104`: "any design text written or signed after 9 September, including decisions signed under this amendment."
- **Age of the code:** following the amendment, prompt text and code count as implementation whatever their age; implementation entries carry no dates.
- The 38a0f4a sentence on open conflicts is not a design entry (amendment line 106); see S-R4.

## Sources and conventions

**Companion files** (in `thesis/notes/thesis_completion/artifacts/`):

| File | What it holds | SHA-256 |
|---|---|---|
| `23-am1-design-text-94c049d.md` | the Ch. 4 text at 94c049d, with paragraph ids such as D4.p3; the source of every design quote | b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759 |
| `23-am1-prompts-evaluated.md` | the evaluated prompt texts as sent, per seam and arm, with calls per run and the registry carried per meeting; the source of every trace-derived prompt hash and prompt quote | b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf |
| `23-am1-prompts.py` | the pure-local script that writes `23-am1-prompts-evaluated.md` from the nine trace.json files | c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6 |
| `23-am1-check-register.py` | the quote and code-reference checker of this register (section Checks); in the package, untracked until the amendment is tagged | 794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9 |

**Sources.**
- Design text: `thesis/notes/thesis_completion/artifacts/23-am1-design-text-94c049d.md`. It is generated from `git show 94c049d:thesis/implementation_chapter.tex`, commit 94c049dd4ca0f9ca44a1541e70b87b32c5adc518, 9 September 2026.
- Code: commit 3320375 (A0 and A1 runs). A2 and RAG ran at b4d6b6c, whose only non-thesis change is one .gitignore line. The working tree's `app/` is identical to 3320375 (`git diff 3320375 -- app` is empty).
- Run facts: the nine ProjectMemory runs of the EL2020 series in the amendment's run manifest (a0_r1–r3, a1_r1–r3, a2_r1, a2_r2b, a2_r3), read from their `trace.json`, `state.json` and `coldstart.json`.
- Retrospective entries cite these later commits: b422b27 (14 September); 50cf0f3 (15 September); c6fbdc0 (committed 19 October with the message baseline; its wording can be dated only to the commit); 5de9911, 9b96138 and 38a0f4a (19 October); b1b3454 and 3c5ab49 (20 October); 0b2a8dc and 72540ab (the cycle-2 switches and prompts); 401f2c8 and 3320375 (Phase B, 22 October); ce75b1f (the disproof review, 22 October).
- The three RAG runs enter only the held-constant controls (H).

**How text is cited.**
- A design id (D4.p3, T.rationale) is a paragraph id of the design-text file. A design quote is copied from that file. The LaTeX source breaks lines inside sentences; a quote joins those breaks with one space. Nothing else is changed, markup included.
- A retrospective quote cites `commit:path:lines`, with line numbers at that commit, or `path:lines` for an uncommitted file in the working tree on 27 October 2026 (for example the amendment).
- Code references are all at commit 3320375:
  - in step-type, design and retrospective entries, `name` (`3320375:path:line`);
  - in implementation entries, `path:line`, with the path shortened once the file has been named. A bare `l.N` or `:N` is a line of the file the entry is about. Where the merge moved an entry away from its file name, the file is named.
  - A2 and RAG ran at b4d6b6c; `git diff --stat 3320375 b4d6b6c -- . ':!thesis'` shows one `.gitignore` line, so the lines hold for every arm. On 27 October `git diff 3320375 -- app scripts` was empty, so the working tree has the same lines.
- **Quotes** are verbatim. A quote of prompt text is the text as the runs sent it (from `23-am1-prompts-evaluated.md`), with the source lines that build it.
- The label Gloss marks the builders' own words and readings. A gloss is never design text, and it is not a finding until a case page uses it.
- Straight double quotation marks are used only for verbatim quotes.
- Every quote and every code reference in this file was checked by script against its source (section Checks).

**Tags on design entries** (my classification, a gloss):
- (T) title of the decision;
- (C) commitment: what the component does or must do;
- (B) a stated benefit, a stated cost, or a rejected alternative;
- (L) a disclosed limitation: what the text says the component does not do, or can get wrong;
- (E) evaluation scope only.

**Labels on implementation entries, hashes and runs.**
- **Step type:** each entry says *LLM step* or *deterministic step*, and *system* or *harness* (evaluation-side code that stands in for a reviewer or the scorer).
- **Prompt hashes** are SHA-256 of the static text in UTF-8, with each dynamic field replaced by `⟦name⟧` (the split rule of `23-am1-prompts.py`). Trace-derived hashes come from `23-am1-prompts-evaluated.md` (SHA-256 `b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf`, generated by `23-am1-prompts.py`, SHA-256 `c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6`). Code-derived hashes are for prompts the traces do not record. They were computed in this session from the string constants of `git show 3320375:<file>`, parsed with Python's `ast` module and assembled as the builder does; no app code was run for them. The schema checks marked "checked in this session" imported the schema classes and the client's two pure schema helpers, with no settings loaded and no call made. These scratch checks are not kept here; a committed script is to re-derive them before the tag (decision sheet B3).
- **Run settings common to every PM run** (A0, A1, A2), from `run_lane.sh` / `run_lane_fixed.sh` in the batch folders and the `config` block of each `coldstart.json`: mode `project-memory-cold-start-live`, `--provider openai`, `--temperature 0.0`, `--strict-live`, `--model gpt-5.4-mini`, `--judge-model gpt-5.4-2026-03-05`, `--resolver-embeddings`, `--expansion-reuse-policy semantic`, `--cold-start-acceptance quality`, `--value-policy structural`. The config block records `"acceptance": "quality"`, `"value_policy": "structural"`, `"resolver_embeddings": true`, `"expansion_reuse_policy": "semantic"`, `"expansion_reuse_threshold": 0.8`, `"judge_model": "gpt-5.4-2026-03-05"` and `cycle2_flags`. The A1 smoke run has no lane script; its config block shows the same values.
- **`EXPANSION_AUTO_ACCEPT`:** set to false by the batch and A2 lane scripts. For a1_r1 it is not recorded: the config block does not hold it, `.env` does not set it (main-session check, 27 October), and the code default is True (`config.py:117`). So a1_r1 ran with True unless the shell set it. The setting is read only off the evaluated path (K2.6c, Not on this path), so behaviour is unaffected.
- **Arms as run** (from each `coldstart.json` `config.cycle2_flags`): A0 has `repair_judge_rejection_status` and `repair_dump_diagnostics` on (both instrument repairs) and the other eight repairs off; A1 has all ten repairs on; A2 has all ten repairs and the four write contracts on. `extraction_whole_decisions` (WD) is off in every arm.
- The register words the arms as run (decision sheet B5).

## Overview

**Step types and seams** (seam names as recorded in the traces; calls per run, ranges over the three runs of each arm):

| Section | Step type | Seams | Model calls per run | What the arms add |
|---|---|---|---|---|
| A Admission | LLM per span; segmentation and evidence creation deterministic | memory_gatekeeper | 135 in every run | nothing |
| E Extraction | LLM per admitted span; claim status mapping deterministic | extraction | 124–130 | WD rewrites the instructions; no new call (WD is off in A0–A2) |
| K1 Key assignment at extraction | LLM, inside the extraction call (the hint field); filing under the hint deterministic | none of its own (extraction) | (in extraction) | A1 stops filing under undefined keys; A2's type check can strip a hint (deterministic) |
| K2 Key resolution and expansion | mixed | state_key_resolution (claim routing), registry_expansion_generation, registry_expansion_review | routing A0 219–254, A1 247–295, A2 293–345; generation A0 141–164, A1 155–191, A2 169–186 | A2's type-check re-routes add routing calls |
| S State rules | deterministic | resolution, conflict_detection; filing_type_check (A2) | none (A0, A1); A2: claim_support_check 286–313 | A2 adds the support check (LLM) and embedding equivalence |
| R Reading | mixed | state_key_resolution (question routing), question_answering, question_answering_grounding | routing 105; grounding 98 | nothing (the read contracts are off in A0–A2) |

Gloss on the table:
- The A0 runs carry the two instrument switches (`repair_judge_rejection_status`, `repair_dump_diagnostics`); they touch no component.
- registry_expansion_generation steps are recorded with mode `—`, but every one carries the served model gpt-5.4-mini-2026-03-17 and `generation_method: llm_assisted`. They are model calls.
- filing_type_check steps (45–53 per A2 run) carry no model; the check is deterministic.
- The split of state_key_resolution calls into claim routing and question routing matches each call's text against the run's question texts.
- Counts above are per run, as ranges over the three runs of each arm. Some implementation entries also give totals per arm over its three runs, from `23-am1-prompts-evaluated.md`.

**Prompt hashes** (implementation entries; the full static texts are in `23-am1-prompts-evaluated.md`):

| Seam | Role | SHA-256 | Source | Arms |
|---|---|---|---|---|
| `memory_gatekeeper` | system | `6b8c0ba94772469ba6768977845f6b3a6709a3849aa8b039d969f677e08c4fcf` | trace | A0, A1, A2 |
| `memory_gatekeeper` | user template | `188dbe98e53d5d4c112bd73d75bad619351162a0492e29888e7427ab045ce99f` | trace | A0, A1, A2 |
| `extraction` | system template | `725f1c00a2d188376cc361f2a939d1e564b1d6ba810a277d276962e95843663f` | trace | A0, A1, A2 |
| `extraction` | user template | `c3635f7bb986417284eb97b2e9b5b677fe8c28b940b5735e4b5be18b8c122e4a` | trace | A0, A1, A2 |
| `state_key_resolution` | system | `fb29d2fadfef7b41827628186bc249dd1522633b5ef73c2021a685d06654fb3f` | trace | A0, A1, A2 |
| `state_key_resolution` | user template | `6e907422766a464599728226ba972bc53d8841c4c9980a97d2718c11c00e50aa` | trace | A0, A1, A2 |
| `question_answering_grounding` | system | `76eb844f30d6ec4604436b58b91f8b878ff6c6e7b0aae83dbc24a50867ecf0dd` | trace | A0, A1, A2 |
| `question_answering_grounding` | user template | `163a9efe1ef66a32fef87cd34b586d64a18404da678cc9a29ffb932eb0ea2594` | trace | A0, A1, A2 |
| `claim_support_check` | system | `15fb33bbdef2091e66ffc00b118d47dde4c352e949de71994899887534f879eb` | trace | A2 only |
| `claim_support_check` | user template | `5a787f081939e82ff99800e100b1dc62f278d0c7fb563e11abff3016edb3db27` | trace | A2 only |
| `registry_expansion_generation` | system | `f570f53ad9920c0fe97856337e41dd0d314e8146704911ccfdbc90e6a37c08bc` | code-derived | A0, A1, A2 (not recorded) |
| `extraction` under WD | system template | `daf30b70d954f478ec9e50ee9a00e2a9de186d1b5c5169fc80ba357a73ea75af` | code-derived | not run |
| judge | system | `8469921dd02deb6544dbcd67fca1451a816439bb5eb8979dd31c54dbb63d9a35` | code-derived | all PM arms and RAG (not recorded) |
| RAG generator | system | `a2d74d5e4d89b19a04ae3b068f519b56c99f71b6359bd771a72678cac90a2cce` | code-derived | RAG (not recorded) |

- **One static variant per seam and role.** Every recorded seam has exactly one system variant and one user-template variant in every arm and in every run, with no unparsed message (`23-am1-prompts-evaluated.md`, "Static variants per seam and arm"). So no A1 switch and no A2 contract changes a recorded prompt text; A2 adds one seam.
- **Code check.** Each trace-derived system text equals the code constant at 3320375: `GATEKEEPER_SYSTEM_PROMPT` (`app/services/memory_gatekeeper_service.py:272-308`), `RESOLUTION_SYSTEM_PROMPT` (`app/services/state_key_resolution_service.py:108-133`), `GROUNDING_SYSTEM_PROMPT` (`app/services/answer_service.py:53-87`), `CLAIM_SUPPORT_SYSTEM_PROMPT` (`app/services/cycle2_filing.py:149-160`). The extraction text equals `EXTRACTION_BASE_INSTRUCTIONS` (`app/services/extraction_service.py:177-211`) with `_COLLECTION_PREFERENCE` replaced by `_SCALAR_PREFERENCE` (l.224-233), plus the registry header (l.288-292). It does not equal the text with that replacement left out. So `expansion_force_scalar` was on in the runs.

**Where a loss surfaces, by loss-trace step** (codebook `thesis/notes/thesis_completion/artifacts/23-loss-trace.md`, section The chain). Gloss: this maps surfaced-at only. Caused-at comes from the oracles and the case page (amendment, Step 3).

| Loss-trace step | Section |
|---|---|
| admitted | A |
| carried, polarity, modality | E |
| filed | K1 or K2, by the claim's path; A2 parks: S (the contract that parked it) |
| proposed, applied | S (K1 or K2 when a rival was misrouted) |
| current, status | S |
| key_reached, in_payload, answered | R |

Gloss: the loss trace groups its steps into four boundaries of its own: extraction (admitted to modality), filing (filed to applied), state maintenance (current, status) and reading (codebook, The chain). The caused-at boundaries of Step 3 differ; the register sheets use those.

---

## A. Admission

### A.1 Step type

- **LLM step:** the gatekeeper classifies each span (seam memory_gatekeeper; one call per span; 135 model calls per run, in every run, plus one summary record per meeting with mode `—`). Segmentation, redaction and evidence creation are deterministic.
- **Chain:** segmentation (deterministic, system) → gatekeeper (LLM, system) → evidence creation (deterministic, system).
- **Entry points at 3320375:**
  - `_api_process` (`3320375:app/evaluation/ami/runner.py:799`) posts the four processing routes for each meeting.
  - `ingest_text_artifact` (`3320375:app/services/artifact_ingestion_service.py:19`), `_store_spans` (`3320375:app/services/artifact_ingestion_service.py:62`), `_derive_authority` (`3320375:app/services/artifact_ingestion_service.py:85`).
  - `segment` (`3320375:app/services/segmentation_service.py:25`), `_segment_transcript` (`3320375:app/services/segmentation_service.py:49`).
  - `run_gatekeeper` (`3320375:app/api/routes_artifacts.py:248`), `evaluate_artifact_spans` (`3320375:app/services/memory_gatekeeper_service.py:415`), `evaluate_span` (`3320375:app/services/memory_gatekeeper_service.py:332`), `_build_gate_prompt` (`3320375:app/services/memory_gatekeeper_service.py:311`), `_build_gate_decision` (`3320375:app/services/memory_gatekeeper_service.py:226`).
  - `create_evidence` (`3320375:app/api/routes_artifacts.py:336`), `create_evidence_for_artifact` (`3320375:app/services/evidence_service.py:63`), `create_evidence_from_gate_decision` (`3320375:app/services/evidence_service.py:20`), `_apply_redactions` (`3320375:app/services/evidence_service.py:78`).

Cross-cutting entries that bind A: D1.p3, D1.p4, D9.p3 (X).

### A.2 Design entries (94c049d)

- **D2.p1** (T) "\subsection{D2: Admit Evidence before Durable Interpretation}"
- **D2.p2** (B) "Processing everything preserves opportunities for capture but exposes all content to interpretation and review. Filtering only at answer time retains a broad searchable record and can tailor exclusions to a question, but allows incidental material into durable interpretations first. Selective admission before extraction places the decision earlier, at the cost of losses before a claim is ever formed."
  - Gloss: two rejected alternatives, and the stated cost of the chosen one. A ground for a trade-off code at admission.
- **D2.p3** (C) "ProjectMemory chooses early admission. Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created. Approved redactions are applied before extraction. Ignored spans and sensitive spans routed for review produce no evidence record through this path." "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."
- **D2.p4** (C) "The implemented threshold is permissive within the admitted set. Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction. Evidence-only is therefore \emph{not} an enforced prohibition on state extraction." (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - Gloss: every admitted policy is extracted. Keeping admitted content out of state is the job of S, not of the gate.
- **D2.p5** (C) "The selected balance favours retaining potentially useful project context while excluding clearly incidental material. It does not settle how selective admission should be." (L) "Raw artifacts remain stored, redaction and classification are fallible, and evidence access checks do not constitute production authentication or retention policy. Thus DR8 is only partly addressed, and the gate supplies no privacy guarantee." (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state." (E) "Noise questions and state recall partially test that balance."
  - Gloss: the admission criterion, and the stated benefit (fewer answers about incidental content).
- **D1.p3** (C) "``Approved evidence'' means admitted by the implemented gate, which may itself be model-assisted."
- **D1.p4** (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts."
- **D5.p5** (L) "Authority is assigned at source artifact level, not inferred reliably per statement." "Source time is the artifact timestamp, falling back to ingestion time; it need not identify when a reported decision took effect."
  - Gloss: both attributes are fixed per artifact at ingest and used by S.
- **D5.p6** (E) "The AMI workflow normally assigns the same discussion authority to every transcript, so it does not substantively test organisational authority hierarchies."
- **T.rationale** (B) "D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"

### A.3 Inputs the design gives this step

- The stored, segmented source text; the gate decides per span (D2.p3).
- The criterion to apply: keep potentially useful project context, exclude clearly incidental material (D2.p5).
- Not specified by the design: what the gate sees beyond the span (neighbouring turns, earlier meetings, the registry, project state); its relevance classes; any threshold.

### A.4 What the design requires the step to do or not do

- A-C1. One persisted gate decision per span decides whether an evidence span is created (D2.p3).
- A-C2. Ignored spans, and sensitive spans routed for review, create no evidence record (D2.p3).
- A-C3. Approved redactions are applied before extraction (D2.p3).
- A-C4. Spans under state extraction, candidate extraction and evidence-only all become evidence that reaches extraction; evidence-only does not block extraction (D2.p4).
- A-C5. The admission balance, in D2.p5's own words. D2.p5: "The selected balance favours retaining potentially useful project context while excluding clearly incidental material. It does not settle how selective admission should be."
  - Gloss: a stated balance, not a rule the gate can contradict. D2.p5 also calls the classification fallible (A.2). For the LLM gate it is compared under criterion (ii), where the prompt omits or contradicts it, and under sheet E's cause 4. It is not a conformance item (class (1)).
- A-C6. Gate decisions and redactions stay inspectable and linked (D2.p3, D9.p3).
- A-C7. Raw artifacts remain stored (D2.p5).
- Not required: that admission establish truth (D1.p3).
- Disclosed limitations and stated costs: loss before a claim is formed (D2.p2); fallible classification, no privacy guarantee (D2.p5); a model-assisted gate (D1.p3); authority and source time per artifact (D5.p5).

### A.5 Retrospective entries

- **A-R1** D2.p5; b422b27 (14 September) added one passage, 5de9911 (19 October) rewrote the paragraph.
  - before `94c049d:thesis/implementation_chapter.tex:215-224`: "Noise questions and state recall partially test that balance. Organisational privacy, sensitive-data retention, and an optimal admission threshold are not evaluated in Chapter~\ref{chap:evaluation}."
  - after `b4d6b6c:thesis/implementation_chapter.tex:215-227`: "There is no read-side classifier for incidental content, so noise resistance is observable only as absent or non-matching maintained state."
  - Gloss: the added sentence binds R as well (R-R4). 5de9911 dropped the access-checks clause; the 94c049d wording stays in the register.
  - Not a design entry (gloss: it reports a development observation, like the 38a0f4a sentence of amendment line 106) `b4d6b6c:thesis/implementation_chapter.tex:215-227`: "As a development observation from one run, the gate ignored 76 of 251 spans; 60 of those were social or logistical by its own classification"
- **A-R2** D2.p4; c6fbdc0. Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:205-213`: "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - after `b4d6b6c:thesis/implementation_chapter.tex:205-213`: "Retained context remains usable, addressing a problem documented during development. Resolution and confirmation remain responsible for preventing inappropriate promotion."
- **A-R3** Disproof review, design choices that turned out badly (`22-bug-list.md`, ce75b1f, 22 October; lines at 3320375).
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:131`: "a turn that mixes project talk and small talk is admitted whole (the ES2009a L31 ice-breaker), and the autonomous structural gate accepted the concepts built from it."
- **A-R4** The read contract's default names D2 (21 October): listed under R (R-R5).
- Gloss, not a design entry: the amendment's Step 0 removes restraint on incidental talk from the Phase D3 mechanisms (amendment line 122), after plan 23 dropped the restraint claim (R-R7). These are evaluation-scope decisions.

### A.6 Implementation entries

#### Evaluated prompt

- **Builder:** `_build_gate_prompt`, `app/services/memory_gatekeeper_service.py:311-315`; system text `GATEKEEPER_SYSTEM_PROMPT`, l.272-308; user template `"Classify this span:\n\n{text}"` (l.314).
- **Hashes:** system `6b8c0ba94772`, user template `188dbe98e53d`; the same in A0, A1, A2.
- **Response schema:** `GateClassificationResponse`. It is sent with `strict: false`, because the redaction items are open dictionaries (`app/llm/openai_llm.py:134-139`; checked in this session with that module's `_strictify_schema` and `_is_strict_safe`).
- **Examples the prompt carries** (text as sent; l.272-308):
  - "POSSIBLE_PROJECT_SIGNAL: hedged proposals ('considering', 'leaning toward', 'option')"
  - "MEETING_LOGISTICS: audio/video issues, greetings, 'can everyone hear me', joining/leaving"
  - "SOCIAL_SMALLTALK: lunch, weather, personal chat, parties, celebrations unrelated to the project"
  - "A project keyword ('decided', 'launch', 'approved', 'confirmed') inside clearly social or personal content is NOISE, not signal."
  - "'The weather decided to ruin our launch party' is SOCIAL_SMALLTALK + IGNORE"
  - "HUMAN_REVIEW: ONLY for sensitive content (credentials, personal, medical, financial)."
- **Registry:** none. The prompt carries no registry and no project description.
- **Not shown that later steps need** (gloss): the span alone is sent (five transcript lines, see Parameters), with no neighbouring spans. The prompt offers three admitting policies, but the system treats them the same (all three are extracted). The prompt does not say that a redaction removes the fragment from the text the extractor later reads.

#### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `_GROUP_TARGET` | 5 lines | `app/services/segmentation_service.py:20` | a transcript span is five consecutive lines |
| `_GROUP_MIN` | 3 lines | `segmentation_service.py:21`, used l.55-57 | a remainder under three lines joins the last span |
| `_TRANSCRIPT_THRESHOLD` | 0.30 | `segmentation_service.py:19`, l.39-43 | share of speaker lines (pattern `_TRANSCRIPT_LINE`, l.15) at which a text is segmented as a transcript |
| admitting policies | `EXTRACT_TO_STATE`, `EXTRACT_AS_CANDIDATE`, `EVIDENCE_ONLY` | `memory_gatekeeper_service.py:240-244` | these create an evidence span; `IGNORE` and `HUMAN_REVIEW` do not |
| redactions | as returned by the model | `app/services/evidence_service.py:46`, l.78-85 | each fragment is replaced (first occurrence) before the evidence text is stored |
| guard | every redaction has `fragment` and `replacement` | `memory_gatekeeper_service.py:344-347` | otherwise the call fails (`LLMSeamError`, `app/llm/guarded.py:120-132`) |

- `_SCORE_MAP` (l.35-45) sets a stored relevance score. Gloss: nothing on the evaluated path filters on it.

#### Deterministic logic

- One decision per span, idempotent (`memory_gatekeeper_service.py:334-336`).
- Evidence is created for every admitted decision of the artifact (`evidence_service.py:63-75`).
- Gloss: what decides extraction is admitted (three policies) versus not admitted (two policies). The extractor runs on every evidence span (E).

#### Arm-specific

- No A1, A2 or WD switch acts here, and the prompt is the same in every arm. The A1 meeting-dates repair sets each artifact's source time at ingest (`_ingest_meeting` (`3320375:app/evaluation/ami/runner.py:744`), `_repair_source_times` (`3320375:app/evaluation/ami/runner.py:750`)); S uses that value.

---

## E. Extraction

### E.1 Step type

- **LLM step:** one extraction call per admitted evidence span (seam extraction; 124–130 calls per run; `23-am1-prompts-evaluated.md`, table Calls per run). Deterministic parts: the mapping from polarity and modality to claim status, and the copying of the artifact's authority and source time onto each claim.
- **Chain:** extraction (LLM, system) → claim persistence (deterministic, system).
- **Entry points at 3320375:**
  - `run_extraction` (`3320375:app/api/routes_projects.py:99`), `extract_for_project` (`3320375:app/services/extraction_service.py:635`), `extract_from_evidence` (`3320375:app/services/extraction_service.py:377`), `_extract_with_llm` (`3320375:app/services/extraction_service.py:529`).
  - `_build_extraction_prompt` (`3320375:app/services/extraction_service.py:285`), `extraction_instructions` (`3320375:app/services/extraction_service.py:271`), `EXTRACTION_BASE_INSTRUCTIONS` (`3320375:app/services/extraction_service.py:177`), `_format_registry` (`3320375:app/services/extraction_service.py:214`), `_registry` (`3320375:app/services/extraction_service.py:565`).
  - `_persist_claims` (`3320375:app/services/extraction_service.py:643`); the claim's authority and source time are read at `authority_level` (`3320375:app/services/extraction_service.py:395`) and `created_at_source` (`3320375:app/services/extraction_service.py:396`).

Cross-cutting entries that bind E: D1.p3, D1.p4, D9.p3 (X).

### E.2 Design entries (94c049d)

- **D2.p3** (C) "Approved redactions are applied before extraction." "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts."
- **D2.p4** (C) "Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction." (L) "Local transcript windows further bound interpretation: a commitment completed outside the window can be missed. The normal ingestion path does not invoke the separate discourse-linking mechanism to repair such omissions."
  - Gloss: the unit of extraction is a local window. A commitment completed outside it is a disclosed limitation, with no repair in the normal path.
- **D1.p3** (C) "a claim records an interpretation"
- **D1.p4** (B) "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
- **D3.p1** (T) "\subsection{D3: Represent Epistemic Status Explicitly}"
- **D3.p2** (B) "For DR1 and DR4, a simple alternative is to treat every extracted claim as an asserted fact, perhaps weighted by confidence. This retains mentions but collapses considering a battery into selecting it." (C) "ProjectMemory instead represents polarity and modality separately from review status and fact lifecycle. Positive asserted claims are classified as accepted interpretations, positive non-asserted claims as proposed interpretations, and negative claims as rejected interpretations. These extraction labels are not acceptance of state. Extraction confidence likewise describes interpretation, not the probability that a project commitment is true."
- **D3.p3** (C) "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value."
  - Gloss: names the non-asserted modalities that S consumes. That extraction must be able to emit them is my inference.
- **D3.p5** (L) "Extraction can misclassify modality or negation in either model."
- **D4.p3** (C) "Open extraction can leave the concept unassigned."
  - Gloss: extraction need not assign a concept. Whether it may, and with what inputs, is K1.
- **D4.p5** (B) "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions." (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions."
  - Gloss: the amendment names this passage as the only 94c049d text from which an architectural code may be argued for WD cases (amendment line 355). It is the whole of D4.p5. The scalar sentence is tagged (C), as in K2.2 and R.2 (record of 28 October 2026). It speaks of concept generation; it does not say how many claims extraction emits per statement. Whether it reaches claim granularity is for the case page.
- **D9.p3** (C) "evidence-linked claims"
- **T.rationale** (B) "D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"

### E.3 Inputs the design gives this step

- Admitted evidence, with approved redactions applied, from all three admitted policies (D2.p3, D2.p4).
- One local transcript window at a time, without discourse linking (D2.p4).
- Not specified by the design: whether the extractor sees the concept registry, examples, earlier meetings or project state. D4.p3's matching covers the extractor's key hint (K1.3), so the matching inputs of K1 apply to that output field, not to claim formation.
- Gloss: the artifact's authority and source time are copied onto each claim (D5.p5). They are attributes, not prompt inputs.

### E.4 What the design requires the step to do or not do

- E-C1. Form claims only from admitted evidence, each linked to its evidence (D1.p3, D2.p3, D9.p3).
- E-C2. Represent polarity and modality separately from review status and fact lifecycle (D3.p2).
- E-C3. Classify: positive asserted as accepted interpretation; positive non-asserted as proposed; negative as rejected (D3.p2).
- E-C4. Extraction labels are not acceptance of state; confidence describes interpretation (D3.p2).
- E-C5. Extraction may leave the concept unassigned (D4.p3).
- Not specified by the design: claim granularity (one claim per decision, per value or per clause), and what a claim's value must contain. Gloss: D10 (retrospective, E-R1) is the first text that fixes granularity.
- Disclosed limitations and stated costs: window-bounded interpretation (D2.p4); misclassified modality or negation (D3.p5); no downstream recovery (D1.p4); classification and transition errors (T.rationale, D3 row).

### E.5 Retrospective entries

- **E-R1** D10, entered at 5de9911 (19 October); unchanged at b4d6b6c. Quoted in full, except the `\label` line (591).
  - title `b4d6b6c:thesis/implementation_chapter.tex:590`: "\subsection{D10: Extract Scalar Claims under Generated Keys}"
  - first paragraph `b4d6b6c:thesis/implementation_chapter.tex:593-604`: "\DR{1} and \DR{7} meet at the extraction step: an interpretation has to be formed before the concept it belongs to exists. Three contracts are possible. Extraction can emit one claim per asserted decision and keep the decision whole, deferring the choice of key until a concept is reviewed; it can emit short scalar claims, each under a generated or reused key, and let resolution and review sort them out; or it can require typed filing, checking a claim's value against the key's declared type and cardinality before it is stored. ProjectMemory selects the second contract. The extractor emits several short scalar claims per admitted span, each with polarity, modality and confidence (\Dn{3}) and each matched to an existing concept or parked for expansion (\Dn{4}); key definitions declare a value type and a cardinality, but nothing checks a claim's value against them when it is filed."
  - second paragraph `b4d6b6c:thesis/implementation_chapter.tex:606-618`: "The benefit intended is coverage from an empty registry: short scalar claims match generated concepts more often than compound statements, and a missed decision can still be reconstructed from its parts at read time. The costs are fragmentation and mis-filing. A two-clause rule can be split across two keys, the neighbouring statement of a turn can be filed instead of the decision, and a date can land under a key defined as a percentage; once filed, the per-key rule of \Dn{5} decides between such rivals by extraction confidence. The contract places no obligation on keeping a stated decision whole and no check at filing, and both omissions surface in the evaluation. Expected consequence: broad claim coverage at the cost of fragmented representations of compound decisions; tested indirectly as \Hy{1} and \Hy{2}, and directly by the span-level trace of Section~\ref{subsec:eval-transfer} (mechanism~\ref{mech:extraction})."
  - rationale-table row `b4d6b6c:thesis/implementation_chapter.tex:692`: "\Dn{10} Extraction contract & Whole-decision claims; typed filing & Short scalar claims under generated keys; no type check at filing & 1, 7 & Coverage from an empty registry & Fragmented and mis-filed decisions \\"
  - Gloss: the cost sentence beginning with the two-clause rule names mis-filing mechanisms of K1 and K2 and the per-key rule of S. It is quoted again at K1-R1, K2-R4 and S-R3, so the sheets show that these mechanisms are named only in retrospective text.
  - Gloss: D10 names whole-decision extraction as an alternative and states a benefit for the chosen contract. Both are retrospective, so neither grounds a trade-off code for a `carried` loss.
- **E-R2** D3.p5; 5de9911. Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:260-270`: "DR1 and DR4 are therefore only partially realised across the full lifecycle."
  - after `b4d6b6c:thesis/implementation_chapter.tex:259-267`: "Extraction can misclassify modality or negation in either model, so \DR{1} and \DR{4} are only partially realised across the full lifecycle."
- **E-R3** D4.p5 wording (c6fbdc0, b1b3454): listed under K2 (K2-R2).
- **E-R4** WD, the whole-decision contract (specified 20–21 October; switch and summary 0b2a8dc; prompt 72540ab).
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-design-cycle-2-plan.md:35`: "One claim per asserted decision, full decision text, filed once"
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-design-cycle-2-plan.md:323`: "one claim per asserted decision, with the full decision text as the value (compound values allowed), filed once;"
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-design-cycle-2-plan.md:325`: "key matching unchanged."
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:152`: "One decision with several parts stays one claim" "Several independent decisions stay separate claims. The prompt must tell the two apart, and this is the riskiest prompt."
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:146`: "These are Chapter 4 design decisions, so they are yours."
  - `3320375:app/core/cycle2_flags.py:63`: "One claim per asserted decision, with the full decision text as its value, filed once."
  - Gloss: the prompt text that realises WD (`_WHOLE_DECISION_RULE` (`3320375:app/services/extraction_service.py:248`)) is implementation, not design (amendment line 107). WD is admitted only by the amendment's Step 2c rule.
- **E-R5** Chapter 6 principle and contract (contract bullet 5de9911; principles table 3c5ab49, 20 October).
  - `b4d6b6c:thesis/conclusion.tex:185`: "1. Keep a stated decision whole when extracting it"
  - `b4d6b6c:thesis/conclusion.tex:211-213`: "the extraction contract of \Dn{10} can, because it asks for scalar claims under generated concepts and places no obligation on keeping a stated decision whole."
  - `b4d6b6c:thesis/conclusion.tex:357-361`: "An \emph{extraction and filing contract} (revising \Dn{10} and \Dn{4}) that keeps a stated decision whole and files it once"
- **E-R6** Plan 23, Phase C, on WD (401f2c8, 22 October).
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:225`: "Before judging D1 (whole-decision extraction, failed twice in the build), repair the whole-item metric"
  - Gloss: D1 here is the cycle-2 build's label for WD, not Chapter 4's D1; the Step 0 plan-23 fix writes WD there (decision sheet B1). The amendment replaces this metric by the Step 2c endpoint.

### E.6 Implementation entries

#### Evaluated prompt

- **Builder:** `_build_extraction_prompt`, `app/services/extraction_service.py:285-296`. Instructions: `extraction_instructions()`, l.271-282, from `EXTRACTION_BASE_INSTRUCTIONS`, l.177-211; the scalar key-selection sentence replaces the collection one (l.278-279). The registry is appended to the system message (l.288-292). User template `"Extract project-state claims from:\n\n{text}"` (l.295).
- **Hashes:** system template `725f1c00a2d1`, user template `c3635f7bb986`; the same in A0, A1, A2.
- **Response schema:** `LLMExtractionResponse`, strict (checked as above). Fields of a claim: `app/schemas/llm_extraction.py:14-21`.
- **Examples and example roles the prompt carries** (text as sent; l.177-211 with l.230-233):
  - "predicate: 'decided' | 'selected' | 'rejected' | 'proposed' | 'considered' | 'owns' | similar."
  - "polarity: NEGATIVE when the value is explicitly or implicitly rejected or ruled out — paraphrase negation counts ('off the table', 'ruled out', 'not going with', \"won't use\"). POSITIVE otherwise."
  - "modality: ASSERTED for firm decisions ('decided', 'locked in', 'going with'); HEDGED for tentative ('leaning', 'not locked in'); PROPOSED for candidates ('option', 'considering'); HYPOTHETICAL for future speculation."
  - "For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value."
  - "Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively."
  - The AMI role examples (l.201-207): "Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager'), predicate 'owns'."
  - "Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner."
  - Gloss: the four titles are the roles of the AMI scenario. Session check: none of them occurs in any EL2020 span (the 135 gatekeeper inputs of a1_r2 cover every span), and the claims a1_r2 extracted with predicate `owns` carry values such as `PERSON14`.
- **How the registry enters:**
  - The whole active registry, not pruned. `self._registry()` (`extraction_service.py:565-569`) calls `StateKeyRegistryService.list_keys()` (`app/services/state_key_registry_service.py:42-49`: active keys, ordered by `state_key`).
  - Loaded once per `ExtractionService` instance (`_registry_cache`, l.375, l.566-568). The extraction endpoint makes one instance per call (`app/api/routes_projects.py:99-102`), and the harness calls it once per meeting (`app/evaluation/ami/runner.py:804`). So one registry per meeting: the traces show one key set per meeting in every run ("Registry carried per meeting", column "Ex key sets").
  - Line format, verbatim `app/services/extraction_service.py:217-220`:
    ```python
        return "\n".join(
            f"  - {k.state_key} [{k.value_type}, {k.key_cardinality}]: {k.label}. "
            f"{k.description} aliases: {k.aliases_json}"
            for k in registry
    ```
    Fields shown: key name, value type, cardinality, label, description, aliases. Not shown: negative aliases, example questions, family (`parent_key`), related keys, the values a key holds.
  - Empty registry (meeting a): the sentinel "(no registry keys provided — use state_key_hint: null)" (l.216).
  - Size, from the traces: meeting a sends the sentinel (system message 2,489 characters). Meetings b–d list 116–166 keys (36,792–49,928 characters).
- **Re-extraction of spans that gave no claims.** Idempotency skips only evidence that already has claims (l.389-392), and `extract_for_project` runs over all evidence of the project (l.635-637). So a span with no claims is sent again at every later meeting, with the larger registry. Traces: 0 such calls at meeting b, 1–2 at c, 4–9 at d per run ("Ex repeat"). Their claims keep the source time of their own meeting (l.394-396). The docstring of `_said_at` notes this case (`app/services/resolution_service.py:288-293`).
- **Not shown that later steps need** (gloss):
  - The prompt asks for "extraction_confidence: 0.0–1.0." and says nothing more. The state rules use it as the last ranking key within a meeting and for tie conflicts (S).
  - No meeting identity, date, neighbouring span or current state is shown.
  - All keys are scalar (K2), but the prompt keeps the collection sentence quoted above.

#### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `expansion_force_scalar` | True (default; confirmed by the sent text, see *Code check* in the Overview) | `app/core/config.py:137`; used `extraction_service.py:278-279` | which key-selection sentence the prompt carries |
| claim status | NEGATIVE → `REJECTED`; ASSERTED → `ACCEPTED`; otherwise `PROPOSED` | `extraction_service.py:654-659` | the stored claim status |
| claim identity | `make_claim_key(evidence_id, state_key or "", object_value, polarity)` | `extraction_service.py:667-672`; `app/db/repositories.py:164-173` | gloss: two claims of one span with the same hint, value and polarity are stored once |
| `extraction_confidence` default | 0.8 schema default. Unreachable under the strict schema, which makes every property required (`openai_llm.py:44-45`), except after a strict-to-non-strict downgrade on a 400 (`openai_llm.py:211-213`). Such a downgrade is not recorded: a 400 records no usage (`openai_llm.py:265-272`), `run.log` logs per call, not per attempt, and `trace.json` keeps no attempt envelope (a known limit, H) | `app/schemas/llm_extraction.py:21` | ranking input (S) |
| guard | every claim has a non-empty `object_value` | `extraction_service.py:545` | otherwise the call fails |
| source time | `artifact.created_at_source or artifact.ingested_at` | `extraction_service.py:396` | A0: ingestion clock (bug 6); A1, A2: meeting date (`repair_meeting_dates`) |
| source authority | `MEETING_DISCUSSION` = 30 for meeting transcripts | `app/core/enums.py:128`, `:137`; `app/services/artifact_ingestion_service.py:85-91` | the authority every claim carries (S) |

#### Deterministic logic

- Claims are persisted per span (`extraction_service.py:643-686`). Decisions, action items, risks and open questions are stored too (l.571-633). Gloss: these four are not on the state path.

#### Arm-specific

- **By arm:**
  - WD (`extraction_whole_decisions`) rewrites the instructions (`_whole_decision_instructions` (`3320375:app/services/extraction_service.py:264`)). No new call. Off in A0, A1 and A2.
  - `expansion_force_scalar` (`3320375:app/core/config.py:137`), on in every arm, also swaps a key-selection sentence of the extraction prompt (`expansion_force_scalar` (`3320375:app/services/extraction_service.py:278`)). Gloss: so the generator preference of D4.p5 reaches this prompt too.
  - A1 and A2 do not change this step. A2's support check later tests claims against their spans (S).
- **The WD instructions** (`extraction_whole_decisions`, `extraction_service.py:236-268`, applied l.280-281): `_PER_VALUE_SENTENCE` is replaced by `_PER_DECISION_SENTENCE` and `_WHOLE_DECISION_RULE` is appended. Code-derived system template hash `daf30b70d954…` (3,516 characters with the placeholder). Its examples (l.248-260, verbatim): "(e.g. 'English and French at launch' rather than separate claims 'English' and 'French'; 'design freeze on Friday, bug fixes only afterwards' rather than 'Friday')" and "('40 dollars', not 'charge forty dollars for it')". The source comment (l.238-239, one comment joined across its line break): "The examples are generic on purpose: no development or test series supplies them."

---

## K1. Key assignment at extraction

### K1.1 Step type

- **LLM step, inside the extraction call.** The extraction prompt asks for a key hint per claim and lists the registry. There is no separate seam; the hint is part of the extraction step's output.
- **Chain:** the `state_key_hint` field of the extraction call (LLM, system) → the hint becomes the claim's key (deterministic, system).
- **Entry points at 3320375** for the deterministic filing (what they do: K1.6): `state_key_hint` (`3320375:app/services/extraction_service.py:661`); `evaluate_conflicts` (`3320375:app/api/routes_proposals.py:28`) and `evaluate_claim` (`3320375:app/services/conflict_service.py:124`), which evaluate the claim under that key; `get_key` (`3320375:app/evaluation/ami/registry_expansion_eval.py:248`) and `get_key` (`3320375:app/services/state_key_resolution_service.py:472`), which keep a registered key from being resolved again.

Cross-cutting entries that bind K1: D9.p3 (X).

### K1.2 Design entries (94c049d)

- **D4.p1** (T) "\subsection{D4: Park Unmatched Claims and Review Concept Expansion}"
- **D4.p2** (B) "DR7 makes an unmatched claim a normal case. Discarding it keeps the schema coherent but loses novel state. Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning." "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
  - Gloss: rejected alternatives: discard, force-match, immediate concept generation.
- **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion. Open extraction can leave the concept unassigned. Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution."
  - Gloss: the text names one matching step and its inputs, without naming a path. The register reads it as covering the extractor's key hint as well as the resolver, since both code paths perform that step (K1.3).
- **D4.p4** (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"

### K1.3 Inputs the design gives this step

- The claim's content, and the existing concepts' descriptions, aliases, values and question examples (D4.p3). D4.p3 names one matching step without naming a path, and both code paths perform it, so these inputs apply to the hint path too.
- Values here means the concept definition's canonical values. The 94c049d matcher scored definition fields, canonical values included (`94c049d:app/services/state_key_resolution_service.py:651-661`); where Chapter 4 means the values a key holds, it says observed values (D8.p3).
- Not specified by the design: labels, value types, cardinalities, negative aliases, the span beyond the claim, a limit on the number of concepts shown.

### K1.4 What the design requires the step to do or not do

- K1-C1. A claim that fits no existing concept is neither forced into the nearest one nor discarded: it is retained, parked and proposed for expansion (D4.p2, D4.p3).
- K1-C2. A claim enters ordinary state resolution under an existing concept, or after its concept is accepted or merged (D4.p3). Gloss: the register's reading of the release sentence. Filing a claim under a key with no concept definition contradicts it, so bug 5 is a conformance defect and its repair a conformance repair. The bug list quoted D10's wording for it (K1-R2).
- K1-C3. Extraction may leave the concept unassigned (D4.p3).
- Disclosed limitation: matching does not establish equivalence (D4.p4).

### K1.5 Retrospective entries

- **K1-R1** D10 (5de9911; quoted in full at E-R1).
  - `b4d6b6c:thesis/implementation_chapter.tex:590-604`: "each matched to an existing concept or parked for expansion (\Dn{4})"
  - cost sentence `b4d6b6c:thesis/implementation_chapter.tex:606-618`: "A two-clause rule can be split across two keys, the neighbouring statement of a turn can be filed instead of the decision, and a date can land under a key defined as a percentage; once filed, the per-key rule of \Dn{5} decides between such rivals by extraction confidence."
- **K1-R2** Bug 5 in the disproof review (ce75b1f, 22 October; lines at 3320375).
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:62`: "matched to an existing concept or parked"
  - Gloss: the bug list attributes this phrase to D4. It is D10's wording of 19 October (K1-R1), not 94c049d D4. Bug 5's design ground is 94c049d D4.p3 (K1-C2).
- **K1-R3** The bug-5 repair (401f2c8, 22 October).
  - `3320375:app/core/cycle2_flags.py:116`: "Bug 5: a claim whose key has no concept definition is not filed; registry expansion maps or"
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:120`: "Apply the type check after this, not instead of it."
- **K1-R4** A2's type check also acts on hinted claims; its specification is under S (S-R9).

### K1.6 Implementation entries

#### Evaluated prompt

- **Seam and builder:** the extraction call of E; the same hashes.
- **Instructions** (text as sent; l.183, l.231-232):
  - "state_key_hint: the registry state_key the claim is about, or null if none fits."
  - "Key selection: map each claim to the MOST SPECIFIC matching registry key — the key about exactly this item/attribute, never a broad catch-all key. One claim per independent item."
  - The ownership sentence quoted in E.6 asks for a claim "keyed to the owner/assignment registry key". Gloss: a cold-start registry has no such key unless one was minted.
- **Registry:** as in E.6 (the whole registry, with the fields listed there).
- **Not shown** (gloss): the values each key already holds. So the hint cannot take into account whether the claim would rival a key's current value about another matter.

#### Deterministic logic

- The hint becomes the claim's key unchanged; nothing checks that it is registered (`extraction_service.py:661`, `:673`).
- A claim whose key is registered is never resolved again: the cold-start mapping skips it (`app/evaluation/ami/registry_expansion_eval.py:248-249`, `active_only=False`), and so does `resolve_state_key_for_claim` (`app/services/state_key_resolution_service.py:472-473`). Gloss: a hint to a registered key about another matter is kept whatever its matter.
- A hint to an unregistered key:
  - A0: the claim is filed under that key by the conflict pass (`app/services/conflict_service.py:134-158`; no definition, scalar path) and later mapped or parked by the expansion step (bug 5).
  - A1, A2: `repair_undefined_key_filing` returns noop instead (`conflict_service.py:152-153`, l.823-838).
  - Traces: the model also writes the literal key `null`. In a1_r2, 31 conflict rows give "Stage-23 repair (bug 5): no concept definition for 'null'; not filed".

#### Arm-specific

- **Under A1, A2, WD:** no prompt change. WD changes the extraction instructions, not the hint sentence.
- **Filing, by arm:**
  - A1: the bug-5 repair stops filing under a key with no definition (`_repair_undefined_key` (`3320375:app/services/conflict_service.py:823`)). No new call.
  - A2: the type check (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`), deterministic) can strip a hint whose key's type the value does not fit and send the claim back to the resolver (`_c2_reroute` (`3320375:app/services/conflict_service.py:899`)). No call at this step.
  - WD: none.

---

## K2. Key resolution and expansion

### K2.1 Step type

- **Mixed.**
  - LLM: claim routing by the resolver (seam state_key_resolution; claim-routing calls per run A0 219–254, A1 247–295, A2 293–345). Expansion generation (seam registry_expansion_generation; 141–191 per run; recorded with mode `—`, but each carries a served model and `generation_method: llm_assisted`).
  - Deterministic: the embedding shortlist and prompt pruning, removal of out-of-registry keys, semantic and alias reuse, the harness concept reviewer (seam registry_expansion_review, reviewer coldstart_harness, mode `—`), and the release of parked claims.
  - Embeddings (text-embedding-3-small) serve the shortlist and the reuse check. They are not trace steps.
- **Chain:** resolver (LLM, system) → expansion: alias merge (deterministic), candidate generation (LLM), semantic reuse (deterministic, embeddings), attach or new proposal (deterministic) → harness reviewer (deterministic, harness) → review validation and release (deterministic, system).
- **Harness order per meeting** (`registry_expansion_eval.py:191-318`): every claim without a registered key, and not parked at an earlier meeting, is resolved or parked, one at a time, in project order (l.245-257; order `repositories.py:176-183`, by source time then creation). Then every pending proposal is reviewed (l.267-309).
  - Claims parked at an earlier meeting are skipped before the registered-key check and before the resolver (l.231, l.246-247). `_parked_claim_ids` (l.493-498) collects the parked claims of all proposals, whatever their status.
  - So a parked claim is never routed again, even when the registry later gains a fitting key. It reaches state only when its own proposal is accepted or merged (K2.6c, Release).
- **Entry points at 3320375:**
  - `_internal_expand` (`3320375:app/evaluation/ami/registry_expansion_eval.py:191`) maps or parks every claim without a registered key (`resolve_state_key_for_claim` (`3320375:app/evaluation/ami/registry_expansion_eval.py:250`)), then reviews the pending expansions.
  - `resolve_state_key_for_claim` (`3320375:app/services/state_key_resolution_service.py:441`); the routed text is the claim's subject and value (`claim_text` (`3320375:app/services/state_key_resolution_service.py:489`)).
  - `resolve` (`3320375:app/services/state_key_resolution_service.py:272`), `_embedding_candidates` (`3320375:app/services/state_key_resolution_service.py:625`), `_prompt_registry` (`3320375:app/services/state_key_resolution_service.py:676`), `_build_resolution_prompt` (`3320375:app/services/state_key_resolution_service.py:224`), `RESOLUTION_SYSTEM_PROMPT` (`3320375:app/services/state_key_resolution_service.py:108`), `_strip_out_of_registry` (`3320375:app/services/state_key_resolution_service.py:898`).
  - `handle_unmapped_claim` (`3320375:app/services/registry_expansion_service.py:117`), `find_or_create_proposal` (`3320375:app/services/registry_expansion_service.py:196`), `_dedup_match` (`3320375:app/services/registry_expansion_service.py:269`), `generate_candidate` (`3320375:app/services/registry_expansion_service.py:355`), `LLMExpansionGenerator` (`3320375:app/llm/expansion_generator.py:368`), `build_expansion_generator` (`3320375:app/llm/factory.py:90`).
  - `_quality_gated` (`3320375:app/evaluation/ami/registry_expansion_eval.py:421`), `_reviewer_would_accept` (`3320375:app/evaluation/ami/informed_reviewer.py:78`), `_accept_self_organized` (`3320375:app/evaluation/ami/registry_expansion_eval.py:431`), `submit_expansion_review` (`3320375:app/services/registry_expansion_review_service.py:63`), `_accept` (`3320375:app/services/registry_expansion_review_service.py:119`).
  - `release_parked_claims` (`3320375:app/services/claim_reevaluation_service.py:26`), `re_evaluate_claim` (`3320375:app/services/claim_reevaluation_service.py:77`).
  - Parameters (values and roles in K2.6, Parameters): `embedding_top_k` (`3320375:app/core/config.py:82`), `embedding_min_similarity` (`3320375:app/core/config.py:83`), `resolver_prune_threshold` (`3320375:app/core/config.py:86`), `expansion_reuse_threshold` (`3320375:app/core/config.py:71`).

Cross-cutting entries that bind K2: D1.p4 (X).

### K2.2 Design entries (94c049d)

- **D4.p1** (T) "\subsection{D4: Park Unmatched Claims and Review Concept Expansion}"
- **D4.p2** (B) "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition. Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
- **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples. An expansion contains a candidate definition and its triggering evidence. Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution. A rejected expansion discards waiting claims from this release workflow without erasing their source evidence. Concept review and value confirmation are separate decisions."
- **D4.p4** (B) "This supports an empty initial registry without treating generated labels as research outcomes. Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted." (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence. Review may itself merge distinct meanings or fail to recognise synonyms."
  - Gloss: the 94c049d text treats similarity-based reuse as fallible. It is the text against which criterion (iii) (a reuse or similarity threshold filing a different matter) is read. The paragraph was deleted from the chapter at c6fbdc0 (K2-R1); it stays in the register.
- **D4.p5** (B) "The representation choice within an open schema remains substantial. A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics. Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions." (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions. This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
- **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation. It does not establish that fine-grained concepts are universally better." (E) "The intended consequence is useful state coverage from an empty registry, assessed by the cold-start protocol in Section~\ref{subsec:eval-cold-start}. Fragmentation and family quality remain diagnostic properties; reference key-name agreement is not a correctness endpoint." (L) "Moreover, the gold-informed reviewer can influence which concepts survive. Cold start must therefore be interpreted together with confirmation sensitivity, rather than as fully unaided schema discovery."
  - Gloss: the EL2020 runs use the quality acceptance policy (`coldstart.json`: acceptance quality), a structural reviewer, not the gold-informed one.
- **D1.p4** (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- **D6.p4** (B) "Deferral and parking can make a correctly extracted fact unavailable when needed."
- **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"

### K2.3 Inputs the design gives this step

- Claim routing: the claim's content; the existing concepts' descriptions, aliases, values and question examples (D4.p3).
- Expansion generation: the claim and its triggering evidence (D4.p3); a preference for scalar concepts with family metadata (D4.p5).
- Concept review: the expansion, that is, the candidate definition and its triggering evidence (D4.p3).
- Not specified by the design: a shortlist or pruning of concepts; any similarity or reuse threshold; the number of concepts shown; negative aliases, labels or value types; project state; the reviewer's acceptance criteria.

### K2.4 What the design requires the step to do or not do

- K2-C1. An unmatched claim is retained and parked against a proposed expansion; it is neither discarded nor force-matched (D4.p2, D4.p3).
- K2-C2. An expansion carries a candidate definition and its triggering evidence (D4.p3).
- K2-C3. Concept review can accept, edit, reject or merge; acceptance or merging releases the waiting claims into ordinary state resolution (D4.p3).
- K2-C4. A rejected expansion discards its waiting claims from release but keeps their source evidence (D4.p3).
- K2-C5. Concept review is separate from value confirmation (D4.p3).
- K2-C6. The generator prefers scalar concepts and attaches family metadata; collections stay possible (D4.p5).
- Disclosed limitations and stated costs: matching, alias-based or semantic, does not establish equivalence (D4.p4; listed as requirement K2-C7 before the review of 27 October, and moved here as K1.4 lists it); parking delays availability and can leave state unavailable for good (D4.p4); review may merge distinct meanings or miss synonyms (D4.p4); fragmentation and near-duplicates (D4.p5); waiting for concept review (D1.p4, D6.p4); the reviewer shapes which concepts survive (D4.p6).

### K2.5 Retrospective entries

- **K2-R1** D4.p4 deleted from the chapter; c6fbdc0 (committed 19 October).
  - before `94c049d:thesis/implementation_chapter.tex:294-299`: "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence. Review may itself merge distinct meanings or fail to recognise synonyms."
  - after: no counterpart at b4d6b6c. Gloss: the 94c049d wording stays in the register.
- **K2-R2** D4.p5 wording; c6fbdc0 and b1b3454 (20 October). Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:301-309`: "The representation choice within an open schema remains substantial." "The September defaults favour scalar concept generation"
  - after `b4d6b6c:thesis/implementation_chapter.tex:291-299`: "An open schema still requires a choice of representation." "The evaluated configuration favours scalar concept generation"
- **K2-R3** D4.p6 rewritten; c6fbdc0 and 5de9911. Gloss: c6fbdc0 first reworded the reviewer sentence (dropping "Moreover"); 5de9911 rewrote it as below.
  - before `94c049d:thesis/implementation_chapter.tex:311-321`: "Moreover, the gold-informed reviewer can influence which concepts survive."
  - after `b4d6b6c:thesis/implementation_chapter.tex:301-311`: "Semantic reuse treats a label match as concept identity, and the reference-informed reviewer can influence which concepts survive, so cold start is interpreted together with confirmation sensitivity rather than as unaided schema discovery."
  - after `b4d6b6c:thesis/implementation_chapter.tex:301-311`: "with the cost of reuse on a larger schema examined in Section~\ref{subsec:eval-transfer} (mechanism~\ref{mech:hubs})"
  - Gloss: the new clause states how reuse behaves; 94c049d D4.p4 said only that matching does not establish equivalence. Being retrospective, it cannot ground an architectural code for a reuse misfiling.
- **K2-R4** D10 (5de9911; quoted in full at E-R1).
  - `b4d6b6c:thesis/implementation_chapter.tex:590-604`: "it can emit short scalar claims, each under a generated or reused key, and let resolution and review sort them out"
  - cost sentence `b4d6b6c:thesis/implementation_chapter.tex:606-618`: "A two-clause rule can be split across two keys, the neighbouring statement of a turn can be filed instead of the decision, and a date can land under a key defined as a percentage; once filed, the per-key rule of \Dn{5} decides between such rivals by extraction confidence."
- **K2-R5** Disproof review, design choices that turned out badly (lines at 3320375).
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:132`: "there are no collection keys, so list answers have to aggregate across keys."
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:135`: "99–196 generated keys, which questions then have to be resolved against."
- **K2-R6** The amendment classifies the shortlist, pruning and harness reviewer as implementation, not design (listed so the boundary is visible).
  - `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:107`: "the resolver shortlist and pruning, and the harness reviewer `_reviewer_would_accept`. Prompt text is implementation even where it is older than cycle 1."
- **K2-R7** A2's type check re-routes claims here; its specification is under S (S-R9).

### K2.6 Implementation entries

#### K2.6a Resolver, write path

- **Seam:** `state_key_resolution`. Write-path calls, totals per arm over its three runs: A0 711, A1 806, A2 945 (read path in R).
- **Builder:** `_build_resolution_prompt`, `state_key_resolution_service.py:224-249`; system `RESOLUTION_SYSTEM_PROMPT`, l.108-133. Called from `resolve()` (l.272-357) via `resolve_state_key_for_claim` (l.441-531).
- **Hashes:** system `fb29d2fadfef`, user template `6e907422766a`; the same in A0, A1, A2 and on both paths. The user message starts with "Resolve this text to registry keys." in every call, so no context digest was sent (`context_digest`, pinned off by `runner.py:607-609`).
- **Example the prompt carries** (text as sent; l.126-128): "Example: 'Redis is the datastore for session state' uses 'datastore' (an alias for architecture.database.primary) but Redis-as-session-store is NOT the primary operational database." Gloss: an example from the database worked example of the rule baseline (`extraction_service.py:8-12`), not from the meeting domain.
- **Text sent:** the claim's subject and value joined by " — " (l.487-492); the evidence span only when both are empty. The intent hint comes from keyword rules (`detect_intent`, l.533-549); write-path calls carry mostly `current_state_question` ("Dynamic fields with a fixed vocabulary").
- **How the registry enters:** `_prompt_registry` (l.676-705) over `list_keys()`. Verbatim, l.689-705:
  ```python
        if not embedding_candidates:
            return registry_keys
        if len(registry_keys) <= get_settings().resolver_prune_threshold:
            return registry_keys
        keep = {key for key, _ in embedding_candidates}
        normalized_text = self._normalize(text)
        tokens = self._tokens(normalized_text)
        for definition in registry_keys:
            if definition.state_key in keep:
                continue
            lexical = (
                self._alias_score(definition.aliases_json, normalized_text, tokens)[0] > 0
                or bool(self._key_tokens(definition) & set(tokens) - STOPWORDS)
            )
            if lexical or definition.supported_intents_json.get(intent.value) == "primary":
                keep.add(definition.state_key)
        return [d for d in registry_keys if d.state_key in keep]
  ```
  - **Embedding part** (`_embedding_candidates`, l.625-643): the cosine between the text and each key's profile; keys at or above `embedding_min_similarity` (0.30), best first, at most `embedding_top_k` (8). Key profile (l.663-674): key name with dots as spaces, label, description, domain, aliases, example questions, canonical values. Key vectors are cached per registry signature (l.645-661).
  - **Lexical part:** a positive alias score (the normalised alias is a substring of the text, or all its tokens are text tokens; l.829-845), or any shared token between the text and the key's name, label, description and domain (`_key_tokens`, l.876-878) outside `STOPWORDS` (l.42-65), or the key declares the intent primary.
  - **Whole registry** when no key reaches 0.30, or when the registry has at most `resolver_prune_threshold` (12) keys.
  - Gloss: `STOPWORDS` (l.42-65) does not contain common words such as "and", "in", "on", "with" or "this", so the lexical part admits any key whose description shares such a word with the claim text.
  - Line format, verbatim l.230-235:
    ```python
    registry_lines = "\n".join(
        f"  - {k.state_key}: {k.label}. {k.description} "
        f"[aliases: {k.aliases_json}; negative_aliases: {k.negative_aliases_json}; "
        f"value_type: {k.value_type}]"
        for k in registry
    )
    ```
    Fields shown: key name, label, description, aliases, negative aliases, value type. Not shown: cardinality, family, example questions, the values a key holds.
    - Example questions are present on every minted key (129 of 129 to 177 of 177 keys per run, `state.json`). They never reach the prompt; no trace holds the field. They enter only deterministically, in two ways: through the embedding profile behind the shortlist (`_key_profile`, l.663-674), and, for a text that `is_broad_list_question` accepts (l.88-94), through the rule candidates (`_example_overlap`, l.777-780, l.869-874; reached through l.347-355; R.6).
    - Canonical values: no key in the nine runs has any, because the harness clears them on accept (K2.6c). They are the values D4.p3 names as a matching input (K1.3), so the clearing empties that input.
  - Size, from the traces ("Registry carried per meeting"): at meeting a every write-path call lists no key (122–143 calls per run; the registry is empty, so the model cannot return a key and every claim goes to expansion). At meetings b–d, calls list 1–166 keys, with medians of 13–38. In 1–11 calls per meeting the whole registry was listed.
- **Use of the output:** keys outside the registry are dropped (l.313, l.898-915). The first remaining primary key is taken (l.508-510). Gloss: on the write path, supporting keys, `needs_clarification` and `confidence` are not used. On the read path, supporting keys are used: broad questions append them to the context pack (R.6, Retrieval).
- **Not shown that later steps need** (gloss): the span, the claim's polarity and modality, and the values each key holds. Filing then puts the claim among that key's claims (S).

#### K2.6b Expansion: what happens to a claim the resolver did not map

Order in `handle_unmapped_claim` (`app/services/registry_expansion_service.py:117-166`):

1. **Alias merge** (deterministic). `find_by_alias` runs on the claim's whole evidence span (l.127-135, span from `_evidence_text`, l.474-478). Verbatim, `state_key_registry_service.py:57-64`:
   ```python
       def find_by_alias(self, text: str) -> list[models.StateKeyDefinition]:
           normalized_text = self._normalize(text)
           matches: list[models.StateKeyDefinition] = []
           for definition in self.list_keys():
               aliases = definition.aliases_json + [definition.label, definition.state_key.replace(".", " ")]
               if any(self._normalize(alias) in normalized_text for alias in aliases):
                   matches.append(definition)
           return matches
   ```
   The first match, in key-name order, gets a merge recommendation (`registry_expansion_service.py:132-135`, l.439-472). It runs under every reuse policy except `disabled` (l.127-131).
   - Gloss: plain substring containment on the whole span, not on the claim. A short alias also matches inside other words; for example, `organization.document.audience` in a0_r1 has the alias "for".
   - Session check (not kept): 41 of the 42 rule-based merges in a0_r1, and 38 of 38 in a1_r2, had an alias, label or dotted name of the target key inside the full span (spans from `trace.json`, proposals from `state.json`). The remaining one in a0_r1 is the semantic merge counted in step 3.
   - Rule-based merges per run (`state.json`, `generation_method: rule_based`, merged): 12–56. They include the semantic merges into a key of step 3, which use the same recommendation record.
   - A generated candidate that names an existing key is merged by the harness (K2.6c); `state.json` shows 0–10 such merges per run (`generation_method: llm_assisted`, merged).
2. **Candidate generation** (LLM). Seam `registry_expansion_generation`. Its messages are not recorded in the trace.
   - Calls, totals per arm over its three runs: A0 463, A1 512, A2 535, all `llm_assisted`, all served by gpt-5.4-mini-2026-03-17.
   - Builder: `LLMExpansionGenerator.generate_expansion_candidate`, `app/llm/expansion_generator.py:387-411`. System text `expansion_system_prompt(force_scalar=True, families=True)`, l.354-365, from l.321-335, l.339-344, l.345-351 (both flags at their defaults, `config.py:137`, `:144`; every key in every `state.json` is scalar and has a family). Code-derived hash `f570f53ad992…` (1,412 characters).
   - Examples it carries (verbatim, l.339-344): "Never propose a collection — a list of independent items (features, owners, options) is one key PER ITEM (e.g. 'product.feature.voice_control', not 'product.features')." And l.345-348: "(e.g. 'product.feature', 'project.action', 'product.spec', 'project.risk')". Gloss: AMI product-design examples.
   - Instruction (l.326-328): "Prefer an existing key from existing_state_keys over inventing a new one; if one fits, set proposed_state_key to it and list it in proposed_related_keys so the reviewer can MERGE."
   - User template (claim-scoped branch), verbatim l.438-450:
     ```python
                return (
                    "Propose a state key for THIS single claim (one concept only):\n"
                    f"  value:     {request.claim_value}\n"
                    f"  subject:   {request.claim_subject or '(none)'}\n"
                    f"  predicate: {request.claim_predicate or '(none)'}\n\n"
                    f"{digest}"
                    f"{granularity}\n\n"
                    "Supporting evidence — CONTEXT ONLY:\n"
                    f"{evidence}\n\n"
                    f"Existing state keys: {keys}\n"
                    f"Existing domains: {domains}\n"
                    f"{families_line}"
                )
     ```
     The granularity sentence (`expansion_concept_level` pinned off, `runner.py:610-612`), l.430-433: "Do NOT widen the key to cover other topics mentioned in the evidence; the key must be about the claim above."
   - How the registry enters: the names of all active keys, all domains and all families (`registry_expansion_service.py:363`, l.374-386). Not shown: the labels, descriptions and aliases of existing keys, and the values they hold. Gloss: the generator is asked to prefer an existing key, but it sees only key names.
   - On failure the generator silently falls back to rules (`expansion_generator.py:406-411`), and the method is still logged as `llm_assisted` (`registry_expansion_service.py:388-389`). No `state.json` holds a rule-based description ("Auto-proposed (rule-based)"), so no fallback happened (session check).
   - Schema: `ExpansionCandidateWithFamilyResponse`, strict. Cardinality is forced to scalar after the call (`expansion_generator.py:304-318`).
3. **Semantic reuse** (deterministic, embeddings). `_dedup_match` (`registry_expansion_service.py:269-296`): the cosine between the candidate's profile and each pending proposal's and registry key's profile (key, label, description, aliases; l.262-267). The best match at or above `expansion_reuse_threshold` (0.80) is reused: the claim joins that proposal (l.217-220), or a merge recommendation into that key is made (l.221-223). `run.log` counts (progress lines starting `⊕ dedup`): 5–11 proposal reuses and 0–2 key merges per run.
4. **Exact attach**: a pending proposal with the same proposed key takes the claim (l.226-231).
5. **New proposal** (l.233-246). The claim is parked against the proposal in every case (l.141-151).

#### K2.6c Review: the harness reviewer, validation and release

- **Harness reviewer** (deterministic, harness). Acceptance `quality` (`registry_expansion_eval.py:290-295`, l.420-429). Verbatim, `app/evaluation/ami/informed_reviewer.py:74-90`:
  ```python
  #: What a reviewer expects a state key to look like: dotted snake_case, >= 2 segments.
  _KEY_SHAPE = re.compile(r"[a-z0-9_]+(\.[a-z0-9_]+)+")


  def _reviewer_would_accept(proposal) -> tuple[bool, str]:
      """Structural gate shared by the 'quality' arm and informed Tier 1: would a
      reasonable human reviewer approve this proposal on sight? Checks only what a
      reviewer can see on the review card — key shape, a label, and supporting
      evidence — never the gold ontology. Returns (accept, reject_reason)."""
      key = (proposal.proposed_state_key or "").strip()
      if not _KEY_SHAPE.fullmatch(key):
          return False, f"malformed state key {key!r} (want dotted snake_case, >= 2 segments)"
      if not (proposal.proposed_label or "").strip():
          return False, "no label"
      if not [t for t in (proposal.triggered_by_texts or []) if (t or "").strip()]:
          return False, "no supporting evidence text"
      return True, ""
  ```
  - A rejected proposal is only recorded; under `quality` no reject is submitted (`registry_expansion_eval.py:293-295`).
  - Accepted proposals go to `_accept_self_organized` (l.431-462): canonical values are cleared and unlisted values allowed (l.446-447). If the key already exists it is a merge, otherwise an accept.
  - Every pending proposal is reviewed again at every meeting (l.267).
- **Validation** (deterministic, system): `RegistryExpansionReviewService._validate_definition`, `app/services/registry_expansion_review_service.py:268-303`. Rules: a key of 2–4 segments (l.31-32); at most 10 canonical values; at least one alias, defaulted to the label (l.136-141); a valid cardinality; a known domain, or one named in the review note. A new key that duplicates an active key is refused (l.147-151). A failure leaves the proposal pending and is recorded as `accept_error` (`registry_expansion_eval.py:307-308`).
- **From the `coldstart.json` expansion logs:** the harness reviewer rejected no proposal in any run. Accept errors were 0–8 review records per run, all `STATE_KEY_INVALID_FORMAT` on keys of five or more segments. Gloss: `_KEY_SHAPE` admits such keys and the validator refuses them, so the proposal stays pending and its parked claims are never released.
  - The records count reviews, not proposals: a stuck proposal is reviewed again at every meeting. They come from 0–2 distinct proposals per run: a0_r1, a0_r3 and a1_r3 none; a0_r2, a1_r1, a1_r2 and a2_r1 4 records from 1 proposal; a2_r2b 7 records from 2; a2_r3 8 records from 2.
  - In `state.json`, each such pending proposal holds one parked claim and has released none.
- **Merge** adds the proposal's aliases to the target key (`registry_expansion_review_service.py:217-262`, l.326-341). Merge recommendations carry no aliases (`registry_expansion_service.py:462`).
- **Release:** `ClaimReEvaluationService.release_parked_claims` (`app/services/claim_reevaluation_service.py:26-75`) sets each waiting claim's key and runs `ConflictService.evaluate_claim` (l.77-90).
- **Not on this path:** the informed reviewer's LLM tier (acceptance `informed` only, `registry_expansion_eval.py:320-327`); `expansion_auto_accept` (used only by `resolve_unmapped_claims`, `state_key_resolution_service.py:1006`, which the step endpoints the harness calls do not run; `app/api/routes_artifacts.py:135` is the `/process` endpoint); `expire_stale_proposals` (`registry_expansion_service.py:320`, no caller).

#### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `resolver_embeddings_enabled` | true (`--resolver-embeddings`; config block `"resolver_embeddings": true`) | `config.py:65`; set by `runner.py:604-606` | the embedding part of the shortlist is on |
| `embedding_top_k` | 8 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:82`; `state_key_resolution_service.py:643` | at most eight embedding candidates |
| `embedding_min_similarity` | 0.30 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:83`; `state_key_resolution_service.py:641` | a key below this cosine is not an embedding candidate; with none above it, the whole registry is sent |
| `resolver_prune_threshold` | 12 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:86`; `state_key_resolution_service.py:691` | at or below 12 keys the whole registry is sent |
| `STOPWORDS` | 22 words | `state_key_resolution_service.py:42-65` | words that do not count as shared tokens in the lexical part |
| first primary key | `fitting[0]` | `state_key_resolution_service.py:508-510` | the key the claim is filed under |
| `expansion_reuse_policy` | `semantic` (config block) | `config.py:70`; `registry_expansion_eval.py:218-230` | alias merge, semantic reuse and exact attach are all on |
| `expansion_reuse_threshold` | 0.80 (config block `0.8`) | `config.py:71`; `runner.py:298`; `registry_expansion_service.py:44`, l.296 | cosine at which a candidate reuses a proposal or merges into a key |
| alias merge target | first matching key in name order | `state_key_registry_service.py:42-49`, l.57-64; `registry_expansion_service.py:133-135` | which key an alias-matched claim goes to |
| `_KEY_SHAPE` | two or more dotted segments | `informed_reviewer.py:75` | harness accept test |
| `_STATE_KEY_RE` | 2–4 segments | `registry_expansion_review_service.py:31-32` | validator accept test |
| canonical values on accept | cleared | `registry_expansion_eval.py:446-447` | keys are open-vocabulary, so `canonical_match` is never called (no such trace step) |
| `expansion_force_scalar`, `concept_families_enabled` | true, true | `config.py:137`, `:144` | scalar keys only; every key gets a family |
| `_MERGE_CONFIDENCE` | 0.4 | `registry_expansion_service.py:36` | stored on merge recommendations; gloss: not used to decide |

#### Deterministic logic (checklist)

- Shortlist and pruning: `_embedding_candidates` (l.625-643), `_key_profile` (l.663-674), `_prompt_registry` (l.676-705).
- Output filtering: `_strip_out_of_registry` (l.898-915); first fitting key (l.508-510).
- Parked claims skipped at later meetings: `registry_expansion_eval.py:231`, l.246-247, l.493-498 (K2.1).
- Parking and expansion: `handle_unmapped_claim` (`registry_expansion_service.py:117-166`), `find_by_alias` (`state_key_registry_service.py:57-64`), `_dedup_match` (l.269-296), `find_or_create_proposal` (l.196-246).
- Harness reviewer: `_reviewer_would_accept` (`informed_reviewer.py:78-90`), `_accept_self_organized` (`registry_expansion_eval.py:431-462`).
- Validation, merge and release: `registry_expansion_review_service.py:119-182`, l.217-262, l.268-303; `claim_reevaluation_service.py:26-90`.

#### Arm-specific

- **A1:** no new call, and no change to the resolver prompt or logic. In every arm the cold-start step already sends claims whose key is not registered to the resolver; the bug-5 repair only stops their filing under the undefined key (K1).
- **A2** (`filing_type_check`): type-check re-routes come back here with the rejected keys excluded (`type_rejected` (`3320375:app/services/state_key_resolution_service.py:485`), `fitting` (`3320375:app/services/state_key_resolution_service.py:508`)). Keys the claim's value did not fit are removed from the result, and a claim parked for good is not resolved (`state_key_resolution_service.py:475-485`, l.508). This adds resolver calls.
- **WD:** none.

---

## S. State rules

### S.1 Step type

- **Deterministic:** resolution and conflict detection (seams resolution and conflict_detection, mode `—`), proposal creation, value confirmation by the harness, and projection.
- **Chain:** conflict evaluation and the resolution engine (deterministic, system) → proposals (deterministic, system) → settle (A1, A2; deterministic, harness) → confirmation (deterministic, harness) → projection (deterministic, system). A2 adds the support check (LLM, system).
- **Value confirmation in the runs** is the runner's structural policy (`coldstart.json`: value_policy structural). Its rules are under S.6 (Confirmation). Entry points: `_internal_confirm` (`3320375:app/evaluation/ami/runner.py:812`), `_internal_confirm_structural` (`3320375:app/evaluation/ami/runner.py:900`), `_confirmable_value` (`3320375:app/evaluation/ami/runner.py:170`), `_confirm_accept` (`3320375:app/evaluation/ami/runner.py:940`).
- **Entry points at 3320375:**
  - `evaluate_project_claims` (`3320375:app/services/conflict_service.py:324`), `evaluate_claim` (`3320375:app/services/conflict_service.py:124`), `_dispatch` (`3320375:app/services/conflict_service.py:332`), `_create_proposal` (`3320375:app/services/conflict_service.py:614`), `_create_reject_proposal` (`3320375:app/services/conflict_service.py:556`), `_create_conflict` (`3320375:app/services/conflict_service.py:951`), `_evaluate_collection_claim` (`3320375:app/services/conflict_service.py:427`) (collections; not reached in these runs).
  - `resolve_state_key` (`3320375:app/services/resolution_service.py:406`), `_eligible_challengers` (`3320375:app/services/resolution_service.py:263`), `make_to_canonical` (`3320375:app/services/resolution_service.py:173`).
  - `submit_review` (`3320375:app/services/confirmation_service.py:45`), `apply_proposal` (`3320375:app/services/projection_service.py:41`).

Cross-cutting entries that bind S: D1.p4, D1.p5, D9.p3, D9.p4, D9.p5 (X).

### S.2 Design entries (94c049d)

**Promotion and epistemic status (D3, D2).**
- **D3.p3** (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values. Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value. Confirmation can accept that proposal while preserving its unconfirmed epistemic status. Explicit negation does not justify inventing a replacement. Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact." (C) "Negating the current value additionally passes the resolver's authority and affirmation checks." (L) "With the legacy negation policy, exclusion instead makes the current fact ambiguous and opens a question for review."
  - Gloss: the evaluated configuration uses the rejecting negation policy (`scalar_negation_rejects` (`3320375:app/core/config.py:129`)), not the legacy one.
  - Gloss: the sentence on negating the current value is on the claims register's R-4 list: it describes the affirmation gate behind bug 1 (R-4 cites the chapter's lines 248–250 at b4d6b6c. Those lines hold this sentence and the sentence before it on negating an alternative, which works in the runs; bug 1 concerns only the current-value branch, so the register reads R-4's item as this sentence). So it cannot ground architectural weakness or a trade-off, and sheet S does not list it as quotable. It stays the requirement behind S-C4.
- **D3.p4** (C) "Current collection proposals distinguish asserted positive members, unconfirmed positive members, and asserted negative members targeting rejected status. Hedged negation is dissent; rejection of an existing member also requires sufficient authority." (B) "The earlier mechanism gave proposed and negative material a confirmed membership target and relied on concept meaning and confirmation to prevent incorrect promotion."
  - Gloss: collection keys only. Every key in the nine EL2020 runs is scalar (129–177 keys per run in the state dumps), so this paragraph binds no evaluated key.
- **D3.p5** (C) "An agreeing positive claim adds support to an existing member without automatically upgrading an unconfirmed member." (L) "Membership still depends on correctly interpreted concept meaning, and heterogeneous content can enter the same broad collection."
  - Gloss: collection keys only, as D3.p4.
- **D2.p4** (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."

**Authority and time (D5).**
- **D5.p1** (T) "\subsection{D5: Separate Authority from Temporal Eligibility}"
- **D5.p2** (B) "Newest-statement-wins is transparent but treats later mentions as replacements. Highest-extraction-confidence-wins confuses interpretation confidence with authority. Highest-authority-wins preserves priority but can privilege stale evidence. Human-only resolution permits contextual judgement at the cost of reviewing every contradiction." (C) "ProjectMemory selects an authority-gated temporal policy, leaving unresolved cases reviewable."
  - Gloss: the amendment takes leaving unresolved cases reviewable as the design text for conflicts (amendment line 106).
- **D5.p3** (C) "The governing principle is that authority determines eligibility to supersede and recency orders temporally eligible evidence. In the scalar policy, a challenger must have at least the current fact's authority and a source time no earlier than the fact's validity start. Eligible challengers are ranked by authority, source time, and extraction confidence. Authority thus retains precedence within the eligible set; recency does not override a higher eligible authority. The same ranking selects an initial asserted positive candidate. Different initial values tied on all three dimensions produce a conflict."
  - Gloss: the text ranks eligible challengers. It does not say whether the current fact's own claims take part in that ranking. The A1 rule that they do (bug 3's repair) rests on the 5de9911 per-key sentence, so the register treats it as retrospective design (S-R3, X-R6).
  - Gloss: one 94c049d sentence states which claims scalar resolution considers. It sits in a disclosed provenance limitation, D9.p4: "Scalar resolution considers all claims for a concept, while proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation." It does not by itself say that the current value's agreeing claims rank against challengers. As a sentence of a disclosed limitation it grounds no design code.
- **D5.p4** (C) "Checking eligibility before ranking matters. Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered. Lower-authority dissent does not overwrite current state. Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict. A conflict need not retract the standing value: the ordinary answer can retain it with a caveat."
  - Gloss: the action threshold's value is not given at 94c049d; 9b96138 states it (S-R4).
- **D5.p5** (L) "Authority is assigned at source artifact level, not inferred reliably per statement. Two participants in one meeting therefore normally inherit the same authority. Source time is the artifact timestamp, falling back to ingestion time; it need not identify when a reported decision took effect. In addition, the explicit tie-to-conflict check applies when no current fact exists. The supersession branch selects a maximum without an equivalent check for tied incompatible challengers, so conflict handling is not uniformly complete. Negation uses different checks: its current-value branch lacks the positive-supersession temporal gate, and an earlier positive claim can block a relevant negation through the affirmation check."
  - Gloss: discloses behaviour that the disproof review later listed as bugs 1, 3 and 6. As disclosed limitations, these sentences cannot ground architectural weakness or a trade-off.
- **D5.p6** (L) "These limitations qualify both requirements." (B) "The intended consequence is stable state under casual dissent, replacement by eligible later commitments, and exposed unresolved conflicts." (E) "The AMI workflow normally assigns the same discussion authority to every transcript, so it does not substantively test organisational authority hierarchies."
  - Gloss: the first sentence refers back to D5.p5's limitations and states that they qualify the requirements, so it is tagged (L), not (B) (record of 28 October 2026).

**Proposal and confirmation (D6).**
- **D6.p1** (T) "\subsection{D6: Propose Changes before Separate Confirmation}"
- **D6.p2** (B) "Direct model mutation minimises delay. Confidence-threshold approval retains automation but uses an admission rule whose reliability must be established. Manual entry keeps responsibility explicit while moving capture and maintenance back to the user." (C) "ProjectMemory instead routes new values, replacements, and current-default rejection outcomes through a reviewable proposal and a separate confirmation operation:" "machine interpretation $\rightarrow$ proposal $\rightarrow$ confirmation $\rightarrow$ projection."
- **D6.p3** (C) "The project-specific application is to expose the proposed value, concept, prior value, target status, evidence, and reason before projection. Confirmation can accept, reject, edit, defer, or request more evidence. Its review record is stored separately from the proposal and before the requested projection. An existing fact can also be placed under review without immediately deleting it. Review identifies a responsibility and contestability boundary; its occurrence does not establish truth."
- **D6.p4** (B) "The costs are intrinsic. Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error. Deferral and parking can make a correctly extracted fact unavailable when needed." (L) "An edited proposal is projected without rerunning authority and temporal resolution, so the reviewer's correction can bypass parts of that policy."
- **D6.p5** (L) "Normal confirmation records review before application, but the separately exposed apply operation accepts pending, drafted, deferred, and already accepted proposals without checking for an accepting review. The legacy exclusion branch also changes a fact to ambiguous during resolution. The repository therefore supports a controlled workflow but does not enforce a universal invariant that every state mutation has passed review."
- **D6.p6** (B) "The intended consequence is that changing confirmation policy changes which interpretations become answerable, making quality and availability trade-offs observable." (E) "Section~\ref{subsec:eval-oracle-confirmation} and the paired-system protocol define autonomous and privileged-review comparisons and acceptance-policy sensitivity."
  - Gloss: the autonomous arm is part of the 94c049d evaluation design. In the runs, its value confirmation is the harness's structural policy (S.1 and S.6). That policy is an implementation entry, marked harness, like the concept reviewer of K2.6c.

**Projection and history (D7).**
- **D7.p1** (T) "\subsection{D7: Preserve Supersession and Distinguish the Two Clocks}"
- **D7.p2** (B) "For DR2 and DR3, overwriting a value makes current retrieval simple but loses its prior validity. Appending every value without status preserves the record while making each question reconstruct currency." (C) "ProjectMemory instead preserves current and superseded facts, validity bounds, and replacement links." (L) "The artifact adopts this distinction without implementing a complete bitemporal query system."
- **D7.p3** (C) "An accepted scalar replacement closes the prior fact's validity interval, marks it superseded, creates a successor with a backward supersession link, and completes the predecessor's forward link. The winning claim's source time is carried as the proposal's effective time and becomes the new validity start; the predecessor's validity end uses the same boundary." (L) "Missing or unusable effective times fall back to projection time. Source time is thus a proxy for domain validity, whereas audit timestamps record when the system processed the change."
- **D7.p4** (C) "Collections retain independent members instead of superseding siblings. Rejection also differs from positive replacement. Applying rejection can demote a matching current row to rejected and close its validity, or record a ruled-out alternative without displacing another current value. This branch does not construct the predecessor--successor pair of a scalar replacement. A rejected proposal, by contrast, records a review decision without creating a rejected fact about the project."
  - Gloss: the first sentence binds collection keys only.
- **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values." (B) "It costs additional transitions and consistency obligations." (L) "Projection is not enclosed in one transaction: review, supersession, creation, link completion, proposal status, and event recording can commit independently. Failure can therefore leave an incomplete transition."
- **D7.p6** (E) "The expected consequence is an answerable current replacement with the earlier fact still identifiable as superseded."

**Provenance at the state boundary (D9, D1).**
- **D9.p3** (C) "Normal projection copies proposal evidence identifiers to the fact. Application events connect proposals with facts and record the actor."
- **D9.p4** (L) "First, a new fact does not store the winning claim identifier, and proposals lack a complete claim-to-fact foreign-key chain. Scalar resolution considers all claims for a concept, while proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation. If it differs from the selected winner, the projected value and recorded support can diverge. Later agreement appends a supporting claim identifier without adding its evidence identifier to the fact's citation list."
  - Gloss: discloses the behaviour later listed as bug 2. As a disclosed limitation it cannot ground architectural weakness or a trade-off.
- **D9.p5** (L) "Second, demoting an existing fact to rejected retains its earlier evidence rather than copying the rejection proposal's evidence onto it. A citation can therefore support the former positive value without explaining its rejection. Recovering who reviewed a change likewise requires review or event records: the standard apply path does not populate the fact's confirming-actor fields."
- **D1.p4** (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- **D1.p5** (L) "The normal write workflow realises these distinctions, but enforcement is incomplete across all callable operations, as D6 explains."
- **T.rationale** (B) "D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\" "D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\" "D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"

### S.3 Inputs the design gives this step

- Per concept, all claims filed under it (D9.p4).
- The current fact, with its authority and validity start (D5.p3).
- Per claim: authority (artifact level), source time (artifact timestamp, else ingestion time) and extraction confidence (D5.p3, D5.p5); polarity and modality (D3.p2, D3.p3).
- The action threshold (D5.p4). Its value is not specified by the design.
- Value confirmation: the proposed value, concept, prior value, target status, evidence and reason (D6.p3).
- Not specified by the design: a check of a claim's value against its concept's type; a check that a claim's span supports it; the order of claims within one artifact; whether the current fact's own claims rank with the challengers. Gloss: the A2 contracts add the first two (S-R9).
- Gloss on the last item and the first input above: D9.p4 says that scalar resolution considers all claims for a concept. It does not say whether the current value's claims rank against the challengers. The A1 rule that they do is retrospective design (S-R3).

### S.4 What the design requires the step to do or not do

Promotion and status:
- S-C1. Scalar: an asserted positive claim may propose a confirmed current value. Without an asserted positive candidate, a proposed, hedged or hypothetical positive claim may propose an unconfirmed value (D3.p3).
- S-C2. Confirmation can accept an unconfirmed proposal and keep it unconfirmed (D3.p3).
- S-C3. A negation does not invent a replacement (D3.p3).
- S-C4. Under the default policy, an asserted negation of an alternative can propose a rejected fact; negating the current value must pass the authority and affirmation checks (D3.p3).
- S-C5. Collections: member statuses as in D3.p4–p5 (no collection key in the evaluated runs).

Resolution:
- S-C6. A challenger needs at least the current fact's authority and a source time no earlier than its validity start (D5.p3).
- S-C7. Eligibility is checked before ranking (D5.p4).
- S-C8. Eligible challengers are ranked by authority, source time and extraction confidence; the same ranking picks an initial asserted positive candidate (D5.p3).
- S-C9. Different initial values tied on all three produce a conflict (D5.p3).
- S-C10. Lower-authority dissent does not overwrite; ineligible dissent below the action threshold changes nothing; other unresolved dissent produces a conflict (D5.p4).
- S-C11. Unresolved cases stay reviewable (D5.p2); a conflict need not retract the standing value (D5.p4).

Proposal and confirmation:
- S-C12. New values, replacements and current-default rejections pass through a proposal and a separate confirmation before projection (D6.p2).
- S-C13. A proposal exposes value, concept, prior value, target status, evidence and reason; confirmation can accept, reject, edit, defer or request evidence; the review record is stored before projection (D6.p3).
- S-C14. Value confirmation is separate from concept review (D4.p3).
- S-C15. Resolution and confirmation are where admitted but inappropriate content is kept out of state (D2.p4).

Projection:
- S-C16. A scalar replacement closes the predecessor's validity, marks it superseded, links both ways, and starts at the winning claim's source time (D7.p3).
- S-C17. A rejection can demote a matching current fact or record a ruled-out alternative without displacing the current value; a rejected proposal creates no rejected fact (D7.p4).
- S-C18. Projection copies the proposal's evidence identifiers to the fact; application events record the actor (D9.p3).

Disclosed limitations (listed so a coder can tell a disclosed limitation from a contradiction; none can ground architectural weakness or a trade-off):
- D3.p3: negation of the current value is gated by the affirmation check.
- D5.p5: authority per artifact; source time from the artifact or ingestion; no tie check in the supersession branch; negation lacks the temporal gate and can be blocked by an earlier positive claim.
- D5.p6's first sentence: D5.p5's limitations qualify both requirements.
- D6.p4: an edited proposal bypasses resolution. D6.p5: the apply operation does not check for a review; the legacy exclusion branch.
- D7.p3: fallback to projection time. D7.p5: non-atomic projection.
- D9.p4: support taken from the triggering claim, not the winner. D9.p5: a demoted fact keeps its earlier evidence; no confirming actor on the fact.

Stated benefits and costs: D1.p4, D2.p4, D5.p6, D6.p4, D6.p6, D7.p5; T.rationale rows D5–D7.

### S.5 Retrospective entries

- **S-R1** D3.p3; b1b3454 (20 October). Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:240-249`: "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
  - after `b4d6b6c:thesis/implementation_chapter.tex:243-252`: "In the evaluated configuration, an asserted negation of an alternative can create a proposal for a rejected fact."
- **S-R2** D3.p4; c6fbdc0. Gloss: the version history and the hedged-negation clause were dropped; collection keys only.
  - before `94c049d:thesis/implementation_chapter.tex:251-258`: "Hedged negation is dissent; rejection of an existing member also requires sufficient authority."
  - after `b4d6b6c:thesis/implementation_chapter.tex:254-257`: "Rejecting an existing member additionally requires sufficient authority."
- **S-R3** D5.p6; b422b27 (14 September), then replaced at 5de9911 (19 October).
  - before `94c049d:thesis/implementation_chapter.tex:364-371`: "Resolver tests provide diagnostic evidence for selected authority and time cases; they do not establish that this model matches real project governance."
  - b422b27 `b422b27:thesis/implementation_chapter.tex:373-378`: "Resolver tests and the nine-case conformance table in Appendix~\ref{app:authority-conformance}, which drives the implemented resolver through mixed-authority configurations including the affirmation limitation above, provide diagnostic evidence that the mechanism follows the stated policy"
  - after (5de9911) `b4d6b6c:thesis/implementation_chapter.tex:363-378`: "Resolution is winner-take-all per key: evaluating a claim passes all claims under its key to the resolver, which projects only the top-ranked one, so same-meeting rivals under a scalar key are decided by extraction confidence and the losers never become facts, and on a corpus whose records all carry one authority level the policy reduces to the latest, or most confident, claim filed under a key."
  - Gloss: the bug list (bug 3) and plan 23 (A1 uses the Ch. 4 rule) rely on this per-key sentence. It was added after the results (X-R6), so the register treats the A1 rule as retrospective design.
  - The same per-key rule in D10's cost sentence (5de9911; E-R1) `b4d6b6c:thesis/implementation_chapter.tex:606-618`: "once filed, the per-key rule of \Dn{5} decides between such rivals by extraction confidence."
- **S-R4** D5.p4; 9b96138, then 38a0f4a (both 19 October).
  - after (9b96138) `b4d6b6c:thesis/implementation_chapter.tex:334-349`: "The action threshold is the authority of a meeting decision, above the meeting-discussion authority every transcript receives, so on a transcript-only corpus dissent against a standing scalar fact is either an eligible replacement or a logged no-op."
  - after (38a0f4a) `b4d6b6c:thesis/implementation_chapter.tex:334-349`: "On such a corpus a conflict arises only when initial candidates tie on authority, time and extraction confidence."
  - Gloss: the first sentence fixes the action threshold's value; retrospective design.
  - Replaced at 38a0f4a `9b96138:thesis/implementation_chapter.tex:337-344`: "The conflict outcome is reached only when initial candidates tie on authority, time and extraction confidence, which means the representation of conflict that \DR{3} requires is not exercised in Chapter~\ref{chap:evaluation}."
  - **Not a design entry** (amendment line 106; it reports a Chapter 5 observation) `b4d6b6c:thesis/implementation_chapter.tex:334-349`: "Chapter~\ref{chap:evaluation} records between none and thirteen such conflicts per autonomous repeat, all left open, so the representation of conflict is exercised there for tied first claims and not for the dissent against standing state that \DR{3} is concerned with."
  - Gloss: the design text for conflicts is D5.p2's leaving unresolved cases reviewable (94c049d).
- **S-R5** D6.p5; b422b27, 50cf0f3 (15 September), c6fbdc0.
  - before `94c049d:thesis/implementation_chapter.tex:408-415`: "There is also an enforcement gap." "The legacy exclusion branch also changes a fact to ambiguous during resolution."
  - b422b27 `b422b27:thesis/implementation_chapter.tex:415-425`: "Since 9 September the projection boundary enforces the invariant itself: a proposal that requires confirmation is projected only when an accepting or editing review is recorded"
  - 50cf0f3 `50cf0f3:thesis/implementation_chapter.tex:415-427`: "The legacy exclusion branch still changes a fact to ambiguous during resolution when scalar rejection is disabled."
  - after `b4d6b6c:thesis/implementation_chapter.tex:415-426`: "In the described revision the projection boundary enforces the invariant itself: a proposal that requires confirmation is projected only when an accepting or editing review is recorded. The public apply operation therefore fails on an unreviewed proposal." "Proposals flagged as not requiring confirmation would remain applicable without review, but the production pipeline sets the flag on every proposal it creates."
  - Gloss: these sentences report a code change made on or after 9 September; they describe the implementation. The legacy-exclusion sentence was dropped at c6fbdc0. The 94c049d D6.p5 stays the register entry.
- **S-R6** D6.p4 and D6.p6; c6fbdc0 and 5de9911. Gloss: wording and evaluation scope.
  - before `94c049d:thesis/implementation_chapter.tex:400-406`: "The costs are intrinsic."
  - after: removed (`b4d6b6c:thesis/implementation_chapter.tex:407-413` begins "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error.")
  - before `94c049d:thesis/implementation_chapter.tex:417-424`: "These partially evaluate the mediation hypothesis."
  - after `b4d6b6c:thesis/implementation_chapter.tex:428-433`: "tested as \Hy{7} by the contrast between the autonomous and the reference-informed policy"
- **S-R7** T.rationale, D6 row; b422b27. Gloss: the stated cost changes.
  - before `94c049d:thesis/implementation_chapter.tex:618`: "Effort, delay, incomplete enforcement"
  - after `b4d6b6c:thesis/implementation_chapter.tex:684`: "Effort, delay, reviewer fallibility"
- **S-R8** D7; b422b27 (a citation added), c6fbdc0, 5de9911 (D7.p6 scope). Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:458-465`: "Auditability is not atomicity or event sourcing."
  - after `b4d6b6c:thesis/implementation_chapter.tex:468-475`: "These audit records provide neither atomicity nor event sourcing."
- **S-R9** The four A2 write contracts: retrospective design alternatives (specified 20–21 October; summaries 0b2a8dc; built 72540ab).
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:146`: "These are Chapter 4 design decisions, so they are yours."
  - filing_type_check `3320375:app/core/cycle2_flags.py:67-68`: "Before filing, check a claim's value against the key's declared value type and cardinality;" "park the claim on a mismatch."
  - filing_type_check `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:153`: "Never drop it."
  - resolution_same_meeting_conflict `3320375:app/core/cycle2_flags.py:72-73`: "Rival asserted claims under a scalar key with equal authority from the same source artifact" "become a conflict instead of a confidence contest."
  - resolution_same_meeting_conflict `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:154`: "The conflict is shown in answers as both values with a caveat."
  - supersession_requires_new_evidence `3320375:app/core/cycle2_flags.py:77-78`: "A challenger supersedes only with evidence that does not already support the current fact" "and comes from another meeting."
  - filing_support_check `3320375:app/core/cycle2_flags.py:82-83`: "Before filing, check that the linked span establishes the claim's value, commitment status" "and time; park the claim otherwise."
  - Chapter 6 `b4d6b6c:thesis/conclusion.tex:186`: "2. Check a value against its key, its rivals and its evidence before it becomes a fact"
  - Chapter 6 `b4d6b6c:thesis/conclusion.tex:357-361`: "checks a claim's value against the key's declared type and cardinality before filing, and treats same-meeting rivals under a scalar key as a conflict rather than a confidence contest (revising the per-key rule of \Dn{5})."
  - Chapter 6 `b4d6b6c:thesis/conclusion.tex:362-365`: "A \emph{supersession contract} (revising \Dn{5} and \Dn{7}) that distinguishes genuinely new source information from another interpretation of an existing span"
  - Gloss: each contract is judged for admission only by the amendment's leave-one-out rule; one not admitted is a design alternative not taken (amendment Step 4).
- **S-R10** The A1 repairs (Phase B, 401f2c8 and 3320375, 22 October). Gloss: plan 23 counts A0 losses resting on a Phase B bug as repaired (amendment line 27). For A1, these rules are implementation; where a rule is said to follow Chapter 4, S-R11 shows which wording it cites.
  - Bug 1 `3320375:app/core/cycle2_flags.py:89`: "Bug 1: a value is ruled out when none of its positive claims survives the asserted negations"
  - Bug 1 `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:201`: "once a value is ruled out, only claims said after it took effect may replace it, so a value that lost to it in its own meeting stays lost (Ch. 4, D5)."
  - Bug 2 `3320375:app/core/cycle2_flags.py:100`: "Bug 2: a proposal takes its evidence, confidence and authority from the claim that supplied the"
  - Bug 3 `3320375:app/core/cycle2_flags.py:106`: "Bug 3: the current value's own claims compete with its challengers, so a rival that ranks lower"
  - Bug 3 `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:198`: "A1 uses the Ch. 4 rule. The current value's own claims compete, and an exact tie keeps the current value. The conflict contract is A2's alternative."
  - Bug 3 `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:226`: "Bug 3's rule is decided: A1 uses the Ch. 4 rule."
  - Bug 3 `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:118`: "Same-meeting rivals are decided by confidence (as Ch. 4 says), or become a conflict (cycle-2 contract)."
  - Bug 4 `3320375:app/core/cycle2_flags.py:111`: "Bug 4: when only hedged claims remain, a value equal to the current one changes nothing instead"
  - Bug 6 `3320375:app/core/cycle2_flags.py:121`: "Bug 6: the evaluation runner passes each meeting's date (from the suite or the AMI metadata) as"
  - Bug 12 `3320375:app/core/cycle2_flags.py:127`: "Bug 12 (found in Phase B): for new and supersede proposals and the rejection of the current value,"
  - Bug 12 `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:200`: "is repaired for scalar keys only."
  - Bug 13 `3320375:app/core/cycle2_flags.py:135`: "Bug 13 (found in Phase B): before a checkpoint's proposals are confirmed, every key is evaluated"
- **S-R11** The design readings behind the bug list's Contradicts lines (ce75b1f, 22 October; lines at 3320375).
  - Bug 1 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:16`: "and Chapter 4's D3 and D5."
  - Bug 2 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:30`: "D9, under which provenance links a fact to the evidence that supports it."
  - Bug 3 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:47`: "same-meeting rivals … are decided by extraction confidence and the losers never become facts"
  - Bug 3, repair table `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:170`: "This is the Ch. 4 rule; the cycle-2 conflict contract is the alternative (A2)."
  - Bug 6 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:68`: "D7's two clocks, and Chapter 3's"
  - Bug 12 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:78`: "and D6's lifecycle, under which a value can be reinstated."
  - Bug 13 `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:87`: "D6, under which a proposal is the reviewable form of a resolution of the key, and the engine's own outcome for the full claim set."
  - Gloss: the bug-3 phrase is D5 wording of 5de9911 (S-R3), not 94c049d. For bugs 1, 2, 3 and 6 the 94c049d text itself discloses the behaviour (D5.p5, D9.p4, and the fallback in D5.p5 and D7.p3). For bug 12, the 94c049d chapter's Operational Limits section does (Annex).
  - Gloss: bug 1's line also cites the engine's own docstring, and bug 12's the comment above the code. Code comments are not design text in this register.
- **S-R12** Conflicts in the autonomous arm (this amendment; once signed, retrospective design under amendment line 104).
  - `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:358`: "An A2 case caused at the state rules by an open same-meeting conflict rests on D5"
  - `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:359`: "held: conflict decision."
  - `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:123`: "add the Open decision on conflicts in the autonomous arm;"

### S.6 Implementation entries

#### Evaluated prompts

- A0, A1: none. The canonical-match seam (`app/services/resolution_service.py:144-170`) is never called, because every key is open-vocabulary (K2.6c).
  - The conflict service builds a canonical-match model client (`canonical_match` (`3320375:app/services/conflict_service.py:68`)), but no canonical_match step is recorded in the nine traces. Gloss: the harness pins no canonical vocabulary on accepted keys (`proposed_canonical_values` (`3320375:app/evaluation/ami/registry_expansion_eval.py:446`)).
- **A2, support check** (seam `claim_support_check`, contract `filing_support_check`; X.4): builder `support_messages`, `cycle2_filing.py:175-180`; system l.149-160; hashes `15fb33bbdef2` (system) and `5a787f081939` (user template).
  - It shows the span, the key's label only (l.198), the value and a status phrase (l.163-172; values sent: "firmly decided" 621, "proposed or considered" 181, "rejected / ruled out" 85, "tentative" 23).
  - Not shown (gloss): the key's description, the rival values, the meeting.
  - It carries no examples.
  - Gloss: under `filing_support_check`, only 313 of 534 a2_r1 claims carry a recorded verdict (amendment, "Already read").

#### Order of evaluation

- `conflicts/evaluate` runs the engine over every claim of the project after extraction (`app/api/routes_proposals.py:28-33`; `conflict_service.py:324-326`; order by source time, then creation).
- Mapped and released claims are evaluated again one at a time during expansion (K2).
- Gloss: the repaired settle (A1, A2) is the only pass that evaluates every key with all its claims just before confirmation.

#### Rules (checklist, with `path:line`)

- **Entry** (`conflict_service.py:124-322`): a claim with no key is skipped (l.134-140). The collection path (l.164-180, l.427-506) is unused, since every key is scalar.
- **E1, a ruled-out alternative** (`scalar_negation_rejects` = True, `config.py:129`): an asserted negation of a value that is not current becomes a `reject` proposal (`conflict_service.py:200-254`). Traces show "Ruled-out value recorded as rejected-fact proposal." in every arm.
- **Engine** (`resolve_state_key`, `resolution_service.py:406-727`):
  - Ranking key, verbatim l.251-252:
    ```python
    def _sort_key(c: ClaimView):
        return (c.authority, c.source_time or _EPOCH, c.extraction_confidence)
    ```
  - Rule 1, negation of the current value (l.480-544).
  - Rule 2, only asserted positive claims can be confirmed; otherwise the most recent hedged claim becomes unconfirmed (l.546-588; `_most_recent`, l.259-260, ranks by source time, then confidence).
  - Rule 3, no current fact: the best claim wins. If another claim ties on all three ranking keys with a different value, the result is a conflict and no proposal (l.590-607). Gloss: within one meeting, authority (30) and source time are equal, so the model's `extraction_confidence` decides, and equal confidences make a conflict. Traces: "Tied authority and time with different values; human review required." 3 times in a0_r1, 19 in a1_r2, 71 in a2_r1.
  - Rule 4, supersession: a challenger is eligible with authority at least the fact's and source time at or after the fact's `valid_from` (l.263-280); the best eligible challenger supersedes (l.659-697).
  - Rule 5: with no eligible challenger, dissent below `DISSENT_THRESHOLD` = `MEETING_DECISION` (50) is a noop (l.403, l.699-711). Gloss: transcript claims carry 30, so rule 6 (l.713-727) cannot occur for them.
  - Value identity in the engine: the exact raw string, for keys with no canonical values. That is every key in these runs (cleared at `registry_expansion_eval.py:446`; 0 keys with canonical values in all nine `state.json` files).
    - `make_to_canonical` uses only the baseline when a key has no canonical values (`resolution_service.py:198-201`). The baseline then returns the raw `surface` (l.121-134). `C(v)` is `to_canonical(v) or v` (l.459-460), so it is the raw string whether or not unlisted values are allowed.
    - Gloss: the baseline's docstring (l.116) says the normalised surface is returned, but l.133-134 return `surface`.
    - Rule 3's tie test compares `C()` directly (l.594-597). Under A2, `differs` adds `normalise_value` and embedding cosine ≥ 0.80 (`cycle2_filing.py:54-76`) when `same_meeting_conflict` or `require_new_evidence` is on (`resolution_service.py:462-467`), but the tie test does not use `differs`.
    - Lower-case comparison occurs only in E1 (`conflict_service.py:207`), in reject projection (`projection_service.py:107-109`), and on the collection path (`conflict_service.py:447-457`; not reached, since no key is a collection).
    - Run example: in a2_r2b, `project.repository.destination` holds both `GitHub repository` and `Github repository` as positive asserted claim values (`state.json`).
- **Proposals** (`conflict_service.py:614-674`, l.556-608): deduplicated by `make_proposal_key(state_key, value, type)` (l.651-653; `repositories.py:423-445`). A0: any earlier proposal with the same key, in any status, blocks a new one (bug 12). A1, A2: see `repair_open_proposal_dedup` and `repair_settle_before_confirm` in X.4.
- **Settle** (A1, A2 only): `repair_settle_pending` (`runner.py:111-136`, called l.833-836).
- **Confirmation** (harness; `value_policy` `structural`, config block): `_internal_confirm_structural` (`runner.py:900-938`) accepts every pending proposal whose value passes `_confirmable_value` (l.170-190). A proposal that fails stays pending; it is never rejected (l.925-928).
  - `scrub_gold_value` (`app/evaluation/ami/question_set.py:113-138`) runs with an empty denylist: it fails a value that ends in an ellipsis or is a discourse fragment, and a value with a narration lead-in counts as wrapped.
  - The value then needs a word of at least four characters (`_content_words`, `runner.py:151-155`) that is not in `_STOPWORDS` (l.143-148) and not in `_VALUE_FILLER` (l.161-167).
  - Verbatim `runner.py:143-148`:
    ```python
    _STOPWORDS = {
        "the", "and", "that", "this", "with", "have", "they", "them", "from",
        "will", "group", "decided", "decide", "would", "could", "should", "about",
        "into", "than", "then", "were", "which", "while", "feature", "features",
        "device", "remote", "control",
    }
    ```
  - Gloss: a value whose words all have fewer than four characters (an acronym such as ASR, or a bare number) can never be confirmed. The list contains AMI words ("feature", "device", "remote", "control").
- **Projection** (`app/services/projection_service.py:41-184`):
  - A proposal needs an accepting review (l.61-66).
  - `valid_from` is the proposal's `effective_time` (l.86-97).
  - A `reject` proposal demotes a current fact with the same value, compared by lower case (l.105-128); otherwise it creates a REJECTED fact next to the current one.
  - Scalar supersession (l.130-140).
  - The current fact is the most recently updated current fact of the key (`repositories.py:219-229`).
- **Review responses:** `app/services/confirmation_service.py:45-104`.

#### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| authority of transcript claims | 30 | `enums.py:128`, `:137` | eligibility and dissent gates |
| `DISSENT_THRESHOLD` | 50 | `resolution_service.py:403` | below it, ineligible dissent is a noop |
| ranking key | (authority, source time, extraction confidence) | `resolution_service.py:251-252` | which claim wins; ties make conflicts |
| source time | A0: ingestion clock; A1, A2: meeting date | `extraction_service.py:396`; `runner.py:744-778` | ordering across meetings; eligibility |
| `scalar_negation_rejects` | True (default; traces show the E1 branch) | `config.py:129` | ruled-out values become REJECTED facts |
| proposal identity | (key, value, type) | `conflict_service.py:651-653`; `repositories.py:423-445` | deduplication |
| `_STOPWORDS`, `_VALUE_FILLER`, word length ≥ 4 | as quoted | `runner.py:143-167` | which proposals the harness confirms |
| `claim_multi_key_facets` | False (default; no `claim_key_mapping` step in any trace) | `config.py:149` | one key per claim |
| settle (A1, A2) | one pass before each confirmation; no time window | `runner.py:111-136`, l.833-836 | a pending proposal the pass does not return again expires |
| `auto_approve_threshold` | 0.85 | `runner.py:268` | gloss: written to reports only; it decides nothing on this path |

#### Arm-specific

- **By arm:**
  - A1: the repairs change deterministic rules: the settle pass (`repair_settle_pending` (`3320375:app/evaluation/ami/runner.py:111`)), the engine repairs inside `resolve_state_key`, the lineage repair (`_repair_lineage` (`3320375:app/services/conflict_service.py:680`)), and the meeting dates set at ingest (A). No model call.
  - A2: adds the LLM seam claim_support_check (`ClaimSupportChecker` (`3320375:app/services/cycle2_filing.py:183`); calls at `supported` (`3320375:app/services/conflict_service.py:213`), `supported` (`3320375:app/services/conflict_service.py:279`) and `supported` (`3320375:app/services/conflict_service.py:752`); 286–313 calls per A2 run).
  - A2: the same-meeting conflict and new-evidence rules are deterministic, with embedding equivalence at 0.80 (`make_equivalence` (`3320375:app/services/cycle2_filing.py:54`), `_c2_equivalence` (`3320375:app/services/conflict_service.py:858`), `_create_cycle2_conflict` (`3320375:app/services/conflict_service.py:926`)).
  - A2: the type check is deterministic (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`); 45–53 filing_type_check records per A2 run, none with a model).
  - WD: none.
- The full A1 switch table and A2 contract table are in X.4.

---

## R. Reading

### R.1 Step type

- **Mixed.**
  - LLM: question routing by the resolver (seam state_key_resolution; 105 calls per run, one per question; the same `resolve` and pruning as K2). The grounding pass (seam question_answering_grounding; 98 calls per run).
  - Deterministic: the context pack (broad-list widening, value matching by embedding at cosine 0.55, family siblings), the answer templates, the scalar focus gate and the structured payload (seam question_answering, mode `—`).
  - Embeddings serve the shortlist, value matching, member relevance (0.42) and collection canonicalisation (0.80).
- **Chain:** question resolution (LLM, system) → widening (deterministic) → context pack (deterministic) → answer templates and gates (deterministic) → grounding (LLM, system).
- **Entry points at 3320375:**
  - `_api_ask` (`3320375:app/evaluation/ami/runner.py:1027`), `ask_question` (`3320375:app/api/routes_questions.py:39`), `answer_question` (`3320375:app/services/answer_service.py:135`).
  - `build_context_pack` (`3320375:app/services/retrieval_service.py:97`), `_value_matched_keys` (`3320375:app/services/retrieval_service.py:210`), `_widen_family_siblings` (`3320375:app/services/retrieval_service.py:267`), `_widen_broad_primary_keys` (`3320375:app/services/retrieval_service.py:290`), `_VALUE_MATCH_COSINE` (`3320375:app/services/retrieval_service.py:47`).
  - `_generate_answer` (`3320375:app/services/answer_service.py:644`); the scalar focus gate starts at line 930 and uses `_question_focus_terms` (`3320375:app/services/answer_service.py:405`) and `_relevant_collection_values` (`3320375:app/services/answer_service.py:416`); `_canonicalize_collection` (`3320375:app/services/answer_service.py:463`).
  - `_attach_structured_payload` (`3320375:app/services/answer_service.py:283`), `_apply_grounding` (`3320375:app/services/answer_service.py:198`).
  - Parameters (values and roles in R.6, Parameters): `answer_relevance_min_similarity` (`3320375:app/core/config.py:89`), `answer_canonical_min_similarity` (`3320375:app/core/config.py:95`).

Cross-cutting entries that bind R: D1.p5, D9.p3, D9.p5, D9.p6 (X).

### R.2 Design entries (94c049d)

- **D8.p1** (T) "\subsection{D8: Resolve Maintained State before Loading Evidence}"
- **D8.p2** (B) "The read-side alternative is to retrieve transcript passages first and ask a model to infer state for the question." "This keeps broad source access and avoids a write-time schema, but repeatedly places temporal and epistemic interpretation at the question boundary." (C) "ProjectMemory selects a different context-construction order for DR2, DR4, and DR5: resolve concepts and facts first, then follow evidence links."
- **D8.p3** (C) "Concept descriptions, aliases, examples, and observed values associate a question with generated concepts. Broad list questions may aggregate candidate concepts and family siblings; specific questions remain narrower. Normal context contains current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions, and decision records. Templates distinguish confirmed from proposed values. If no concept, current fact, or relevant value answers a specific question, the service can return an explicit unknown outcome and retain nearby facts only as near matches." (L) "This makes a retrieval gap visible, although unknown alone cannot distinguish genuine absence from information lost during admission, extraction, review, or retrieval." (C) "Although the public schema defines a disputed outcome, ambiguous facts are excluded by ordinary current-fact retrieval and normally reach the unknown branch; a standing confirmed fact can instead carry a conflict caveat."
- **D8.p4** (B) "The narrower context is intended to reduce exposure to superseded alternatives and attach evidence to the selected state. Its cost is restricted answerability." (C) "Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims, or events. Current code adds a bounded exception: rejection-phrased questions can retrieve rejected facts for resolved concepts, including scalar alternatives never previously current." "Negative interpretations must first reach a representable, projected lifecycle state; rejected expansions and rejected state proposals do not become answerable merely because they persist."
- **D8.p5** (C) "For collection-like or multi-concept questions, it selects current facts whose earliest linked source artifact is the most recently ingested artifact." (L) "It does not traverse supersession links, compare arbitrary snapshots, or reconstruct all removals and replacements. A single scalar change question normally follows the current-value template. This latest-addition heuristic fits some checkpoint questions but is not a general temporal-difference engine."
- **D8.p6** (B) "The expected behavior is current-value accuracy with meaningful abstention and evidence support, alongside weaker historical coverage." (E) "A complete-system difference also cannot isolate retrieval order from review and write-time work."
- **D1.p5** (C) "If it behaves as intended, tentative or rejected interpretations should not appear as settled answers, and returned facts should carry inspectable evidence."
- **D2.p3** (C) "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts."
- **D2.p5** (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
- **D3.p5** (C) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
- **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions."
- **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation."
- **D5.p4** (C) "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat. Keeping uncertainty visible does not imply abstaining whenever disagreement exists."
- **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
  - Gloss: one sentence with two tags: a stated benefit of supersession (S.2) and a commitment on reading (R-C7) (record of 28 October 2026).
- **D9.p3** (C) "Citations expose stored evidence text and source identifiers."
- **D9.p5** (L) "Third, public citations expose evidence spans but not stored locators or an exact mapping from answer sentences to supporting spans. A provenance question selects an earliest linked artifact using ingestion order, which need not be the original source of the decisive statement."
- **D9.p6** (B) "The intended consequence is an answer whose evidence permits verification and correction."
- **T.rationale** (B) "D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"

### R.3 Inputs the design gives this step

- Question routing: the question, and the concepts' descriptions, aliases, examples and observed values (D8.p3).
- Broad list questions: candidate concepts and family siblings (D8.p3, D4.p5).
- Answer context: current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions and decision records (D8.p3).
- Rejection-phrased questions: rejected facts of resolved concepts (D8.p4).
- Change questions over collections or several concepts: current facts whose earliest linked source artifact is the most recently ingested (D8.p5).
- Excluded by the design for ordinary current-state questions: superseded facts, rejected proposals, all negative claims, events (D8.p4); raw artifacts (D2.p3). Gloss: the reader reaches admitted evidence only through facts (D8.p2).
- The scalar focus gate's outcome is specified by the design. D8.p3: "If no concept, current fact, or relevant value answers a specific question, the service can return an explicit unknown outcome and retain nearby facts only as near matches." The stated cost of the narrower context, D8.p4: "Its cost is restricted answerability."
  - The gate's relevance test is implementation: the focus terms, `_FOCUS_STOPWORDS`, `answer_relevance_min_similarity` 0.42 and the embedding relevance (R.6).
  - Gloss: the gate was in the code when the 94c049d text was written (`94c049d:app/services/answer_service.py:891`).
- Not specified by the design: a question-time shortlist or pruning, similarity thresholds, the relevance test of the scalar focus gate, and the model grounding pass. Gloss: the grounding pass is described at 94c049d outside D1–D9 (Annex) and in D11 (retrospective).

### R.4 What the design requires the step to do or not do

- R-C1. Resolve concepts and facts first, then follow evidence links (D8.p2).
- R-C2. Associate a question with concepts by descriptions, aliases, examples and observed values (D8.p3).
- R-C3. Broad list questions may aggregate candidate concepts and family siblings; specific questions stay narrower (D8.p3, D4.p5, D4.p6).
- R-C4. Templates distinguish confirmed from proposed values; answers keep current, proposed and ruled-out apart; tentative or rejected interpretations do not appear as settled (D8.p3, D3.p5, D1.p5).
- R-C5. If no concept, current fact or relevant value answers a specific question, the service can return an explicit unknown and retain nearby facts only as near matches (D8.p3); answers should abstain when no current value is established (D3.p5).
- R-C6. Ambiguous facts are excluded by ordinary retrieval; a standing confirmed fact can carry a conflict caveat (D8.p3, D5.p4).
- R-C7. Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims or events; rejection-phrased questions may retrieve rejected facts of resolved concepts (D8.p4, D7.p5).
- R-C8. Change answering as in D8.p5.
- R-C9. Citations use evidence records and expose the stored evidence text and source identifiers; returned facts carry inspectable evidence (D2.p3, D9.p3, D1.p5).
- Disclosed limitations and stated costs: restricted answerability (D8.p4); unknown cannot tell absence from loss (D8.p3); the change heuristic (D8.p5); citation granularity and provenance by ingestion order (D9.p5); weaker historical coverage (D8.p6).

### R.5 Retrospective entries

- **R-R1** D11, entered at 5de9911 (19 October); unchanged at b4d6b6c. Quoted in full, except the `\label` line (621).
  - title `b4d6b6c:thesis/implementation_chapter.tex:620`: "\subsection{D11: Render Answers from Resolved State through Templates}"
  - first paragraph `b4d6b6c:thesis/implementation_chapter.tex:623-633`: "\DR{4} and \DR{5} shape the final step. Once \Dn{8} has resolved keys and loaded facts, three renderings are possible. The answer can be generated freely from the selected facts and their evidence, which reads well but can add unsupported content. It can be rendered through templates over the resolved keys' current values, which keeps every stated value traceable and makes abstention a fixed sentence. Or it can be rendered from templates with a fallback to the admitted evidence text when the resolved keys carry no value of the required kind. ProjectMemory selects templated rendering with an optional model grounding pass that may revise prose and confidence while retaining the structured fields (Section~\ref{subsec:structured-answer-payload})."
  - second paragraph `b4d6b6c:thesis/implementation_chapter.tex:635-646`: "The benefit intended is restraint and provenance: a templated answer asserts only stored values and cites their evidence, and a question that resolves to nothing yields an explicit decline. The cost is that the template has no relevance filter over the values it lists and no route back to the evidence text. A list template concatenates every value under the resolved keys, so a correct value can be buried among unrelated ones or absent while a neighbouring key holds it, and a hub key's current value is rendered whatever it is. Expected consequence: answers that are traceable and abstain cleanly, at the cost of answers assembled from whatever the resolved keys hold; tested as \Hy{4} and \Hy{5} for the restraint half and, for the cost, by the transfer trace (mechanism~\ref{mech:reading}) and the read-context replay of Section~\ref{subsec:eval-replay}."
  - Gloss: the list-template cost sentence names a mechanism of losses at `in_payload` and `answered`. It appears only in this retrospective text.
  - rationale-table row `b4d6b6c:thesis/implementation_chapter.tex:694`: "\Dn{11} Rendering contract & Free generation; templates with evidence fallback & Templates over resolved keys with an optional grounding pass & 4, 5 & Traceable answers; clean abstention & No relevance filter; no route back to evidence \\"
- **R-R2** D8.p6; 5de9911.
  - before `94c049d:thesis/implementation_chapter.tex:521-530`: "The paired comparator is specifically cumulative transcript RAG"
  - after `b4d6b6c:thesis/implementation_chapter.tex:528-533`: "The reader's preference for resolved keys over the admitted evidence text is examined in Section~\ref{subsec:eval-transfer} (mechanism~\ref{mech:reading})"
  - Gloss: the added sentence describes reading behaviour found in the results.
- **R-R3** D8.p3; c6fbdc0. Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:487-500`: "This makes a retrieval gap visible, although unknown alone cannot distinguish"
  - after `b4d6b6c:thesis/implementation_chapter.tex:495-507`: "A retrieval gap is visible, but unknown alone cannot distinguish"
- **R-R4** D2.p5 addition; b422b27.
  - `b4d6b6c:thesis/implementation_chapter.tex:215-227`: "There is no read-side classifier for incidental content, so noise resistance is observable only as absent or non-matching maintained state."
- **R-R5** The read contracts of cycle 2 (off in every evaluated arm; specified 20–21 October).
  - `3320375:app/core/cycle2_flags.py:52`: "When no key resolves, no current fact remains, or no resolved key answers, answer from the"
  - `3320375:app/core/cycle2_flags.py:57`: "After resolution, check each resolved key's label and current values against the question;"
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:150`: "Reading all turns would undo the admission decision (D2) and make the arm RAG under another name."
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/21-phase-0-prep.md:151`: "Never candidates or scores. Same generator model."
  - `b4d6b6c:thesis/conclusion.tex:371-375`: "A \emph{read contract} (revising \Dn{8} and \Dn{11}) that falls back to the admitted evidence text when the resolved keys carry no value of the required kind"
  - `b4d6b6c:thesis/conclusion.tex:366-370`: "An \emph{aggregation and change contract} (revising \Dn{8}) tested on complete current lists"
  - `b4d6b6c:thesis/conclusion.tex:187`: "3. Assemble broad answers across concepts deliberately"
  - `b4d6b6c:thesis/conclusion.tex:188`: "4. Keep source evidence reachable when the state cannot answer"
  - `b4d6b6c:thesis/conclusion.tex:189`: "5. Make restraint a declared outcome, not a by-product"
- **R-R6** Disproof review, design choices that turned out badly (lines at 3320375).
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:133`: "with no fallback to the evidence text."
  - `3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:134`: "not a declared outcome. This is latent: with embeddings off, value retrieval re-adds keys the resolver had declined."
- **R-R7** Plan decision on restraint (not a design entry; evaluation scope).
  - `b4d6b6c:thesis/notes/thesis_completion/artifacts/23-plan-development-and-confirmation.md:206`: "the restraint claim is dropped from the verdict list, so no per-component switches are built."

### R.6 Implementation entries

#### Evaluated prompts

- **Question resolution:** the resolver of K2.6a with the question as text. 105 calls per run (315 per arm). Same hashes (`fb29d2fadfef`, `6e907422766a`). Registry via `_prompt_registry` with the intent from `detect_intent`. Keys listed: 8–177 per call; the whole registry in 0–3 calls per meeting ("Registry carried per meeting", R columns).
- **Grounding:** seam `question_answering_grounding`, 98 calls per run. Builder `_build_grounding_prompt`, `app/services/answer_service.py:90-118`; system `GROUNDING_SYSTEM_PROMPT`, l.53-87. Hashes: system `76eb844f30d6`, user template `163a9efe1ef6`; the same in A0, A1, A2.
  - It is skipped for provenance questions (l.202-203).
  - It sees the question, the drafted answer, the citations (evidence texts) and the current facts (key, value, status, review state).
  - Its `revised_answer` replaces the answer prose (l.249-253). Gloss: an LLM step after the state that can remove asserted values from the prose; the structured payload is kept.
  - Example (text as sent; l.79-81): "An abstaining answer ('I do not see a confirmed…', 'I was unable to find relevant project state…') asserts nothing and is trivially grounded (grounded=true, unsupported_sentences=[])."
  - `review_state_present` was False in every call.
- **Not shown** (gloss): the resolver sees key definitions but not their values, so a question about a value held under an oddly named key depends on the widening steps below. Nor does it see the keys' example questions; they enter only deterministically (K2.6a; Deterministic widening below).

#### Deterministic widening and answer logic (checklist)

- **After the LLM**, in `resolve()`:
  - Change questions add the keys that declare `change_explanation` primary (`state_key_resolution_service.py:322-336`). Gloss: minted keys declare no intents (every key in every `state.json` has empty `supported_intents`), so this adds nothing here.
  - Broad list questions (`is_broad_list_question`, l.88-94) add the rule-based candidates after the LLM's own picks, up to `BROAD_LIST_MAX_KEYS` = 10 (l.76, l.347-355).
    - The candidates are every key with a positive rule score (`_compute_rule_based_response`, l.551-621; `_score_key`, l.745-807), plus the embedding candidates with a bonus of cosine × `embedding_score_weight` 5.0 (`config.py:84`; l.707-743). They are sorted by score, with no other minimum. A negative alias with no positive alias disqualifies a key (l.758-760, l.725-731).
    - Score parts live in these runs: alias match, 4.5–5.5 for a substring match and 3.4–4.2 for a token-subset match (l.829-845); key-token overlap, 0.75 per token, at most 3 (l.771-775); example-question overlap, 0.5 per token, at most 2 (l.777-780, l.869-874); the decision-domain bonus 3.5 for DECISION_LOOKUP (l.803-805).
    - Inert in these runs: the intent bonuses 2.5 and 1.0 (l.794-801; minted keys declare no intents) and the canonical score 2.5 (l.766-769, l.847-856; no key has canonical values).
    - Gloss: so example questions reach question routing here, deterministically, and never through the prompt (K2.6a).
- **Retrieval** (`app/services/retrieval_service.py:97-203`):
  - Broad questions pass the resolver's candidate list to `_widen_broad_primary_keys` (l.114-117, l.290-308): candidates scoring at least `_BROAD_CANDIDATE_RATIO` 0.25 of the top, up to `_BROAD_MAX_KEYS` 10 (l.41-42).
    - On the LLM path the response's `candidate_keys` is empty: the field is internal and is not in the schema sent to the model (`app/schemas/llm_resolution.py:8-11`, l.33-40). `_to_resolve_result` then substitutes the primary keys and the supporting keys, all at one score, the LLM confidence (`state_key_resolution_service.py:918-923`). For a broad question the primary keys already include the rule candidates, capped at 10 (l.347-355 of that file).
    - So the 0.25 ratio is inert. The net effect is that the resolver LLM's supporting keys are appended until there are 10 keys.
    - Review check (27 October; scratch, not kept): in a1_r2, 0 of 400 resolver outputs carry candidate keys, and in 25 of 105 question traces of `state.json` the resolved primary keys include a key the resolver returned only as supporting.
  - Keys whose current values match the question focus at cosine ≥ `_VALUE_MATCH_COSINE` 0.55 are added, up to 6 (l.47-48, l.210-260). Focus terms are words of three or more characters outside `_FOCUS_STOP` (l.60-75).
  - Broad questions add family siblings, up to `_FAMILY_MAX_SIBLINGS` 10 per family (l.264-287).
  - Facts: the current fact of each scalar key (l.142-154).
- **Answer** (`_generate_answer`, `answer_service.py:644-984`):
  - The focus key (l.580-586).
  - Broad versus specific (l.676-678). Focus terms: words of four or more characters outside `_FOCUS_STOPWORDS` (l.355-369, l.389-413), which include AMI words ("product", "feature", "device", "remote", "control").
    - The focus key's own label and alias words are removed from the focus terms (`_question_focus_terms`, l.405-413).
    - A question with no focus terms left counts as broad (l.676-678). The scalar focus gate runs only for a specific question that keeps focus terms (l.937-939). So this removal decides both broad versus specific and whether the gate runs.
  - The relevance filter for list-like answers: cosine ≥ `answer_relevance_min_similarity` 0.42 (`config.py:89`; l.416-455).
  - Canonicalisation of near-duplicates at `answer_canonical_min_similarity` 0.80 (`config.py:95`; l.463-524), with no cap (`answer_canonical_max_items` 0, `config.py:101`).
  - Rejection questions read REJECTED facts (l.734-788). Change questions read the facts first established in the latest meeting (l.589-634, l.794-822).
    - When `_REJECTION_Q_RE` matches (l.376-380, l.739), the current facts of any resolved key whose name contains `reject` are read as ruled-out values too (l.750-754). `get_current_collection` filters by status only (`app/db/repositories.py:294-305`), so scalar keys qualify.
    - Minted keys of that form (`state.json`): one in a0_r3, two in a1_r3, one in a2_r1.
  - **Scalar focus gate** (l.930-952): a specific question whose focus matches no candidate value is answered "unknown", and the held facts move to `near_matches` (l.319-321).
  - Answer status (l.260-280); mapped to the scorer's status by `runner.py:1067-1071`.

#### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `embedding_top_k`, `embedding_min_similarity`, `resolver_prune_threshold` | 8, 0.30, 12 | as in K2.6 | the question-time shortlist |
| `BROAD_LIST_MAX_KEYS` | 10 | `state_key_resolution_service.py:76` | cap on the keys a broad question resolves to |
| `embedding_score_weight` | 5.0 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:84` | weight of embedding similarity in the rule candidates used for widening |
| rule-scorer weights | alias 4.5–5.5 (substring) or 3.4–4.2 (token subset); key-token overlap 0.75 per token, at most 3; example overlap 0.5 per token, at most 2; decision-domain bonus 3.5 (DECISION_LOOKUP); intent bonuses 2.5 and 1.0 and canonical score 2.5, inert here | `state_key_resolution_service.py:745-807`, l.829-874 | which keys fill the broad-question slots |
| `_BROAD_CANDIDATE_RATIO`, `_BROAD_MAX_KEYS` | 0.25, 10 | `retrieval_service.py:41-42` | broad-question widening; the 0.25 ratio is inert on the LLM path, where all candidates share one score |
| `_VALUE_MATCH_COSINE`, `_VALUE_MATCH_MAX_KEYS` | 0.55, 6 | `retrieval_service.py:47-48` | keys pulled in by value match |
| `_FAMILY_MAX_SIBLINGS` | 10 | `retrieval_service.py:264` | family widening cap |
| `answer_relevance_min_similarity` | 0.42 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:89`; `answer_service.py:454` | which held values count as relevant; drives the scalar focus gate |
| `answer_canonical_min_similarity` | 0.80 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:95`; `answer_service.py:490` | near-duplicate values merged in answers; also A2's value equivalence (X.4) |
| `answer_canonical_max_items` | 0 (no cap; default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:101` | cap on listed values |
| `_FOCUS_STOPWORDS` | as listed | `answer_service.py:355-369` | which question words count as focus |

#### Arm-specific

- No arm adds a model call here. The read contracts (`answer_evidence_fallback`; `answer_answerability_check`, with its key_answerability seam) are off in A0, A1 and A2.
- **Under A1, A2, WD:** no prompt change. A2 adds a disputed answer for open same-meeting conflicts (`answer_service.py:899-915`).

---

## X. Cross-cutting

D1 and D9 bind every component. Each component section lists the X entries it relies on. The A1, A2 and WD switches act on several components; their tables are in X.4.

### X.1 Design entries (94c049d): D1 and D9

- **D1.p1** (T) "\subsection{D1: Separate Source, Evidence, Interpretation, and State}"
  - Gloss: every stage writes its own kind of record.
- **D1.p2** (B) "Three architectures are possible: answer from raw records; extract structured assertions and immediately use them as facts; or preserve boundaries between source, admitted evidence, interpretation, proposed mutation, and reviewed state." "Both leave less opportunity to inspect the point at which an interpretation acquires persistent state consequences."
  - Gloss: the rejected alternatives. The first is the architecture of the RAG comparator.
- **D1.p3** (C) "ProjectMemory selects the third architecture:" "raw source $\rightarrow$ approved evidence $\rightarrow$ extracted interpretation \\[3pt] $\rightarrow$ proposed change $\rightarrow$ reviewed state." "A source artifact records what was received; approved evidence records what was admitted for further use; a claim records an interpretation; a proposal records a candidate change; a state fact records the outcome projected by the confirmation workflow." "``Approved evidence'' means admitted by the implemented gate, which may itself be model-assisted. It does not mean that a person verified the statement or that its content is true."
  - Gloss: one record type per boundary: evidence (A), claim (E), proposal and fact (S). No record is named for key assignment or for reading.
- **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist. Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - Gloss: the stated benefit, and costs that name three boundaries: admission (A), concept review (K2) and value review (S). The last sentence says an extraction loss cannot be recovered downstream (E). These are 94c049d grounds for a trade-off code at those boundaries.
- **D1.p5** (L) "The normal write workflow realises these distinctions, but enforcement is incomplete across all callable operations, as D6 explains." (C) "If it behaves as intended, tentative or rejected interpretations should not appear as settled answers, and returned facts should carry inspectable evidence." (E) "the aggregate comparison cannot attribute an effect to record separation alone."
  - Gloss: the (C) sentence is a requirement on reading (R).
- **D9.p1** (T) "\subsection{D9: Retain Provenance across Consequential Boundaries}"
- **D9.p2** (B) "Attaching only a source title is cheap but cannot locate the supporting passage. Keeping only the final citation loses admission and interpretation history. A fully linked derivation graph offers richer reconstruction but adds modelling and consistency work." (C, L) "ProjectMemory adopts evidence identifiers and review/event records across principal boundaries, with incomplete relational linkage between some of them."
- **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts. Normal projection copies proposal evidence identifiers to the fact. Application events connect proposals with facts and record the actor. Citations expose stored evidence text and source identifiers." "This adapts provenance principles; it is not a claim of PROV conformance."
  - Gloss: binds A (gate decisions, locators), E (claims linked to evidence), S (proposals carry evidence; projection copies it; application events) and R (citations).
- **D9.p4** (L) "Three limitations distinguish lineage from evidential correctness."
  - Gloss: the first limitation is quoted in full under S.
- **D9.p5** (L) "Second, demoting an existing fact to rejected retains its earlier evidence rather than copying the rejection proposal's evidence onto it."
  - Gloss: the second limitation is quoted under S, the third under R.
- **D9.p6** (L) "The normal path thus stores and returns linked evidence identifiers when available, but does not guarantee that every link supports the selected value and lifecycle status. Claim-level support, state derivation, and auditability are related but distinct." (B) "The intended consequence is an answer whose evidence permits verification and correction." (E) "Full semantic support and complete lineage therefore remain unevaluated conditions of a stronger provenance claim."
- **T.rationale** (B) "D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\" "D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"

### X.2 What D1 and D9 require of every component

- X-C1. Each boundary writes its own record: evidence, claim, proposal, fact (D1.p3).
- X-C2. Records stay linked by evidence identifiers across boundaries; review and event records are kept (D9.p2, D9.p3).
- X-C3. Admission is not verification (D1.p3).
- Inputs: none. D1 and D9 constrain records, not the inputs of a step (gloss).
- Disclosed limitations: incomplete enforcement (D1.p5); incomplete linkage (D9.p2); links need not support the value and status (D9.p6).

### X.3 Retrospective entries

- **X-R1** D1.p4, first sentence; c6fbdc0 (committed 19 October with the message baseline). Gloss: wording only.
  - before `94c049d:thesis/implementation_chapter.tex:170-171`: "The rationale is to make commitments inspectable before their consequences persist."
  - after `b4d6b6c:thesis/implementation_chapter.tex:172-173`: "These boundaries are intended to make commitments inspectable before their consequences persist."
- **X-R2** D1.p5; 5de9911, 19 October. Gloss: the requirement on answers stays; the attribution sentence moves to the section introduction (X-R5).
  - before `94c049d:thesis/implementation_chapter.tex:178-185`: "the aggregate comparison cannot attribute an effect to record separation alone."
  - after `b4d6b6c:thesis/implementation_chapter.tex:180-185`: "Expected consequence: tentative or rejected interpretations do not appear as settled answers and returned facts carry inspectable evidence; tested as \Hy{1} and \Hy{8}."
- **X-R3** D9.p5 and a new paragraph; b422b27, 14 September. Gloss: restates the D9.p4–p5 limitations; binds S.
  - after `b4d6b6c:thesis/implementation_chapter.tex:564-573`: "Cited spans are also not independent sources: several spans can derive from one artifact."
  - after `b4d6b6c:thesis/implementation_chapter.tex:575-580`: "ProjectMemory does not implement justification-based retraction: later support appends a claim identifier without extending the fact's evidence, and a demoted fact retains its earlier evidence. Retraction occurs only through a reviewed rejection or replacement proposal."
- **X-R4** D9.p3 and D9.p6; c6fbdc0 and 5de9911. Gloss: wording, and evaluation scope.
  - before `94c049d:thesis/implementation_chapter.tex:550`: "This adapts provenance principles; it is not a claim of PROV conformance."
  - after `b4d6b6c:thesis/implementation_chapter.tex:553`: "The design adapts provenance principles without claiming PROV conformance."
  - before `94c049d:thesis/implementation_chapter.tex:571-580`: "Its specified claim-level citation precision and coverage are not yet implemented as the complete claim-to-span assessment described there"
  - after `b4d6b6c:thesis/implementation_chapter.tex:582-588`: "tested as \Hy{8} by the source checks and the claim-level citation audit (Table~\ref{tab:eval-citation-support})."
- **X-R5** Section introduction (outside D1–D9); 5de9911.
  - after `b4d6b6c:thesis/implementation_chapter.tex:136-143`: "the evaluation compares complete configurations, so no decision is attributed an isolated effect"
- **X-R6** Why D10, D11 and the D5 per-key sentence are retrospective: the argument map records that they were added on 19 October to name the loss mechanisms found in the results (file last committed 3c5ab49, 20 October).
  - `b4d6b6c:thesis/notes/argument_map/argument_graph.yaml:2456`: "Two of the three loss mechanisms trace to design choices Chapter 4 never states as decisions"
  - `b4d6b6c:thesis/notes/argument_map/argument_graph.yaml:2457`: "neither is one of D1-D9, and the winner-take-all per-key rule is only implicit in D5's ranking sentence."
  - `b4d6b6c:thesis/notes/argument_map/argument_graph.yaml:2460`: "D10 (extraction and filing contract) and D11 (rendering contract) added to Chapter 4 with alternatives, costs and tests; the per-key winner-take-all rule stated in D5"
- **X-R7** D9 contracts and repairs: `filing_support_check` and the bug-2 repair are listed under S (S-R9, S-R10).

### X.4 Arm-specific implementation across components

#### A1: the ten repair switches

Table: `app/core/cycle2_flags.py:86-151`; Settings fields `config.py:162-171`; RunConfig `runner.py:341-350`; the runner writes every switch to the environment (`runner.py:615-618`). In the runs, A0 already had the last two switches on.

| Switch | Bug | What it changes (summary from `cycle2_flags.py`) | Main code |
|---|---|---|---|
| `repair_negation_affirmation` | 1 | a value is ruled out when none of its positive claims survives the asserted negations; a ruled-out current value is superseded or rejected; a negation is never appended as support (l.87-97) | `resolution_service.py:288-375`, l.495-517, l.519-523, l.547-550; `conflict_service.py:208-225`, l.261-262, l.372, l.691-804, l.811-821, l.880-883 |
| `repair_proposal_lineage` | 2 | a proposal takes evidence, confidence and authority from the claim that supplied the winning value (l.98-103) | `conflict_service.py:359`, l.576-578, l.648-650, l.680-689, l.877-879; `repositories.py:409-420` |
| `repair_same_meeting_supersession` | 3 | the current value's own claims compete with its challengers (l.104-108) | `resolution_service.py:378-389`, l.662-673 |
| `repair_hedged_same_value` | 4 | with only hedged claims, a value equal to the current one changes nothing (l.109-113) | `resolution_service.py:392-396`, l.555-565 |
| `repair_undefined_key_filing` | 5 | a claim whose key has no definition is not filed (l.114-118) | `conflict_service.py:152-153`, l.823-838 |
| `repair_meeting_dates` | 6 | the meeting's date becomes the artifact's source time (l.119-124) | `runner.py:87-109`, l.744-778 |
| `repair_open_proposal_dedup` | 12 | an applied or expired proposal no longer blocks a new one with the same key (l.125-132) | `repositories.py:354-393`, l.436-438; `conflict_service.py:358`, l.605, l.671 |
| `repair_settle_before_confirm` | 13 | every key is evaluated again before confirmation; a pending proposal not produced again expires (l.133-140) | `runner.py:111-136`, l.833-836; `conflict_service.py:806-809`; `repositories.py:396-406`, l.439-440 |
| `repair_judge_rejection_status` | 7 (instrument) | the judge's gold string for rejection items states the expected status (l.141-144) | `app/evaluation/ami/judge_repairs.py:19-58`; on in A0, A1, A2 and RAG |
| `repair_dump_diagnostics` | 9, 10 (instrument) | state-dump traces matched per checkpoint; wrong-key diagnosis corrected (l.145-151) | `app/evaluation/ami/state_dump.py:99`, `:109`, `:124`, `:222`; on in A0, A1, A2 |

- Gloss: no repair changes a prompt text, which the one-variant result confirms. The repairs change which claims are filed, what the engine returns, which proposals are raised and kept, and the source times.

#### A2: the four write contracts

| Contract | What it changes | Seam or LLM call added | Code |
|---|---|---|---|
| `filing_type_check` | before filing, a value that does not fit the key's declared type (numbers, dates, booleans, or a ';' enumeration under a scalar key) leaves the key; it is resolved again without that key, and parked for good after a second misfit | no LLM call; deterministic, logged as `filing_type_check` (149 steps over three runs) | `conflict_service.py:154-157`, l.899-924; `app/services/cycle2_filing.py:101-123`; `state_key_resolution_service.py:475-485`, l.508 |
| `resolution_same_meeting_conflict` | rival asserted values of equal authority from the same meeting become an open conflict, not a confidence contest | no LLM call; uses embeddings for value equivalence (cosine ≥ `answer_canonical_min_similarity` 0.80) | `resolution_service.py:472-475`, l.608-620, l.674-686; `conflict_service.py:403-406`, l.858-862, l.926-949; `cycle2_filing.py:54-76`; read side `answer_service.py:899-915` |
| `supersession_requires_new_evidence` | a challenger supersedes only with evidence and a meeting the current fact does not rest on | none; embeddings for equivalence as above | `resolution_service.py:274-279`, l.345-348; `conflict_service.py:850-856` |
| `filing_support_check` | a claim becomes a fact only if its own span establishes its value, status and time; an unsupported winner is parked and the key resolved again (up to 8 times) | the `claim_support_check` LLM seam, one call per claim, cached on the claim: 313, 311 and 286 calls in a2_r1, a2_r2b, a2_r3 | `conflict_service.py:185-191`, l.213-218, l.270-284, l.643-646; `cycle2_filing.py:149-210` |

- The support-check prompt is under S.6.

#### WD: `extraction_whole_decisions`

- It changes only the extraction instructions (E.6): the per-value sentence is replaced, and the whole-decision rule is appended (`extraction_service.py:236-268`, l.280-281).
- No new seam. Code-derived system template hash `daf30b70d954…`. Not run in any evaluated arm (config blocks: `"extraction_whole_decisions": false`).
- Plan role: `cycle2_flags.py:61-64`, decisions D10 and D4.

---

## H. Held-constant controls

### Generator (all PM seams, and the RAG generator)

- **Model requested:** `gpt-5.4-mini`.
  - Default `config.py:21`. The runner writes `LLM_MODEL` from `--model gpt-5.4-mini` (`runner.py:580-581`). The factory builds every seam's client with it (`app/llm/factory.py:77-87`); no per-seam override (`LLM_SEAM_MODELS` "{}", `runner.py:584-586`).
  - Recorded: trace `model` field on every LLM step; `coldstart.json` `config.model`.
- **Served snapshot:** `gpt-5.4-mini-2026-03-17` on every LLM step of all nine traces.
  - Trace top-level `served_models`: 827, 864, 879 (A0); 921, 926, 870 (A1); 1255, 1309, 1225 (A2).
  - Taken from the response's `model` field (`app/llm/guarded.py:54-65`; `openai_llm.py:300`), and recorded for the expansion generator too (`registry_expansion_service.py:430`).
  - The batch and smoke usage ledgers (`usage.json`) count one gpt-5.4-mini call per run more than the traces: the live preflight (`runner.py:623-656`).
- **Temperature:** 0.0.
  - Default `config.py:22`. The runner writes `LLM_TEMPERATURE` from `--temperature 0.0` (`runner.py:602`), and the client adds it to each request (`openai_llm.py:175-176`).
  - The client drops it only after a provider 400 that names temperature (l.208-210).
  - Recorded: the attempt envelope keeps `temperature_sent` (l.328-331), but `trace.json` does not keep the envelope. So whether temperature was sent is not recorded (a known limit, decision sheet B6).
- **Response format:** `response_format` of type `json_schema`, with the response schema's class name, the strictified schema and a `strict` flag (l.163-174).
  - `strict` is true for every recorded seam's schema except `GateClassificationResponse` (A.6). After a 400, `strict` falls back to false (l.211-213).
- **Other call settings:**
  - No `max_tokens` or `max_completion_tokens`, `top_p`, `seed` or reasoning setting is sent (l.163-177).
  - `llm_max_attempts` 3 (`config.py:26`; retries on bad bodies, l.232-245).
  - `llm_request_timeout` 120 s (`config.py:31`).
  - `llm_sdk_max_retries` 4 (`config.py:37`; the SDK's own back-off for 429 and 5xx).
- **Failure policy:** strict-live for the LLM seams. A failed or malformed call raises `LLMSeamError` and never falls back to rules (`guarded.py:120-132`). The expansion generator is the exception (K2.6b). Embeddings follow another policy (Embeddings, Failure policy). Recorded: `coldstart.json` `fallback_count` is 0 and `status` `valid` in all nine runs; no step of the nine traces has `fallback` or `error` set.

### Embeddings

- **Model:** `text-embedding-3-small`.
  - Default `config.py:77`; RAG default `app/evaluation/ami/rag_runner.py:182`, written to `EMBEDDING_MODEL` (l.374).
  - Recorded: every `usage.json` ledger (the price table admits only listed models, `app/llm/study_budget.py:53-54`) and the RAG `config.embedding_model`. Not in `coldstart.json` or the traces.
- **Call:** `OpenAIEmbeddingClient.embed` sends `client.embeddings.create(model=self.model, input=texts)` with no `dimensions` parameter (`app/llm/embeddings.py:67-80`). Cosine is computed locally (l.242-246). Built by `build_embedding_client` (l.205-239).
- **No cassette for the PM runs:** `embedding_cassette_path` is empty by default (`config.py:80`), and `.env` sets no cassette path (main-session check), so the PM runs keep no vectors. Step 0's instrument changes add a cassette.
- **RAG vectors:** the A2 and RAG lane script passes `--embedding-cache` with the lane's `shared/rag_embeddings.json`.
  - That file is byte-identical (SHA-256 94b4df26ff3b4f8e12e5ad42ae16d5da35881c565458daa7bc8ac929f2a9c8ea) to the cache of the September transfer study (`data/ami_eval/transfer_studies/transfer_20260923T230223026681Z/shared/rag_embeddings.json`, last modified 24 September). It holds 237 vectors, with model_id text-embedding-3-small.
  - All three RAG reports record 0 cache misses (`config.embedding_cache`: hits 21910, misses 0, size 237), and the RAG run logs have no embedding lines. So the RAG runs made no embedding call, and their vectors date from September.
  - The cache's model_id is the requested model. The served embedding snapshot is therefore unrecorded for RAG as well.
- **Failure policy:** five call sites catch an embedding error and fall back silently to a deterministic path:
  - resolver shortlist: no candidates, so the whole registry is sent (`state_key_resolution_service.py:631-635`, l.689-690);
  - value-matched retrieval: stem containment (`retrieval_service.py:239-260`);
  - relevance filter: compact matching (`answer_service.py:449-452`, l.434-439);
  - canonicalisation: values unchanged (`answer_service.py:485-488`);
  - A2 value equivalence: not equivalent (`cycle2_filing.py:58-64`).
  - Gloss: expansion semantic reuse (`_dedup_match`, `registry_expansion_service.py:269-296`) does not catch an error, so a failure there would stop the run.
  - No trace or `coldstart.json` field records such a fallback.
  - **Check that none occurred** (review, 27 October; scratch, not kept). The client writes a start line to `run.log` before each call and an ok line only after success (`embeddings.py:76`, l.130); on error it re-raises (l.81-103). Start and ok counts are equal in all nine PM run logs: a0_r1 567, a0_r2 604, a0_r3 604, a1_r1 652, a1_r2 642, a1_r3 607, a2_r1 1009, a2_r2b 1038, a2_r3 1041. They sum to the `usage.json` text-embedding-3-small call counts: 3024 for the batch, 652 for the smoke run, and 3494 for the A2 and RAG lane, with the failed a2_r2 (406, equal counts) included. So no embedding call failed after it started.
  - A budget refusal in `before_request` (`embeddings.py:75`) comes before the start line and would not be logged. Spend stayed under budget in every ledger: batch $15.01 of $20.25; smoke $3.33 of $4.75; A2 and RAG lane $13.67 of $20.25.
- **Uses on the evaluated path:**
  - resolver candidates (K2.6a);
  - expansion semantic reuse (K2.6b);
  - value-matched retrieval, relevance filter and canonicalisation (R.6);
  - A2 value equivalence (X.4);
  - RAG dense retrieval (`rag_runner.py:248-252`).
  - Gloss: the informed reviewer's Tier 2 and `confirm_semantic_cosine` are not on this path.
- **Served model:** kept only in the client's `last_call_metadata` (`embeddings.py:107-129`), which no artifact stores.

### Judge

- **Model:** `gpt-5.4-2026-03-05`, a dated snapshot id.
  - Passed by `--judge-model`; strict-live requires a judge distinct from the answering model (`runner.py:578-579`, l.1085-1097).
  - Recorded: `coldstart.json` `config.judge_model`; RAG `config.judge_model` and `judge_prompt_version` `ami_judge_v1`; `usage.json` ledgers (calls: 593 for the five batch runs, 126 for the A1 smoke run, 543 for the A2 and RAG lane).
- **Prompt:** `JUDGE_SYSTEM_PROMPT`, `app/evaluation/ami/judge.py:23-49` (version `ami_judge_v1`, l.21); user template l.85-95 ("QUESTION", "GOLD", "SYSTEM ANSWER"). Code-derived hash `8469921dd02d…` (1,934 characters).
  - Example it carries (verbatim, l.29-31): "For example, treat 'universal remote control' as covering 'universal compatibility', and 'plastic casing' as covering 'plastic as their casing material'." Gloss: AMI examples.
- **When it is called:** only when the deterministic match leaves gold values missing and the answer did not abstain. Prose layer: `app/evaluation/ami/scorer.py:816-826`. State layer: l.712-718, with "State values: " answers. Bug-7 wrapper: `judge_repairs.py:19-58`.
- **Call settings:** its own `OpenAILLMClient` with temperature 0.0 fixed in code (`judge.py:73-80`), the client's default of 3 attempts (`openai_llm.py:82`), and the timeout and SDK retries from settings. JSON schema `JudgeResponse` (l.52-63), sent strict (checked as in A.6). The same request code as the generator, so no `max_tokens`, `top_p` or `seed`. A judge error gives status `failed`, not a crash (l.96-103).
- **Recorded:** verdicts in `coldstart.json` `scorecard.scores[].diagnostics.judge` (49–61 judged questions per run). Inputs and the served snapshot are not recorded; Step 0's instrument changes add the inputs to `trace.json`.

### RAG generator (shared settings)

- **Model:** `gpt-5.4-mini`; **temperature:** 0.0.
  - Defaults `rag_runner.py:170`, `:173`. The RAG runner reuses the PM harness's `_configure_mode` (l.376-384), so the same environment variables and the same `OpenAILLMClient` apply (`build_llm_client("rag_generator")`, l.265).
  - Recorded: every `rag.json` `config.model` = `gpt-5.4-mini`, `config.temperature` = 0.0, `generator_prompt_version` `rag_answer_prompt_v1`, `fallback_count` 0, `status` valid.
- **Prompt:** `RAG_SYSTEM_PROMPT`, `app/evaluation/ami/rag_components.py:177-187`; user template l.201-210; schema `RagAnswerSchema` (l.168-174), sent strict (checked as in A.6). Code-derived hash `a2d74d5e4d89…` (1,390 characters).
  - Gloss: the RAG prompt is its own, not shared with the PM seams. It frames the task as "a product-design project" (l.177) and gives the passage-id example "[ES2009a.chunk.3]" (l.178).
- **Served snapshot:** not recorded. `SharedReferenceGenerator` reads `last_call_metadata` (l.227), which `OpenAILLMClient` does not set (it keeps `last_call_attempts`), so `operation_metadata` holds only `prompt_version` and `intended_model`.

---

## Register sheets per caused-at boundary

**What a sheet is.**
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:334`: "The per-boundary register sheet is a checklist: the page addresses every listed candidate cause for its caused-at boundary."
- One sheet per caused-at boundary of Step 3: extraction, key assignment at extraction, key resolution and expansion, state rules (with A2's contracts and support check), reading.
- Gloss: Step 3 names no admission boundary. The amendment lists the gatekeeper among the extraction causes, and the loss trace's extraction boundary begins at `admitted`. So the admission entries (A) are on sheet E.
- A case coded *routing, path unclear* takes sheets K1 and K2 both.
- Each sheet gives, in order:
  1. scope: which cases the sheet serves and what sets caused-at there;
  2. the candidate implementation causes the amendment lists for the boundary, verbatim, each with what decides it and the register entries behind it;
  3. further implementation entries of this register at the boundary, which the amendment's list does not name. Two are mapped to a listed cause; the pilot may add a cause that rests on any of the others, but may not split or merge the listed causes (amendment line 380);
  4. for criterion (ii), the inputs the design gives the step set beside what the evaluated prompt shows (a gloss; the page applies it);
  5. the conformance checklist: the design requirements of the boundary;
  6. the 94c049d disclosed limitations, which cannot ground architectural weakness or a trade-off, and the 94c049d sentences a page may quote after implementation is rejected, each with its tag: commitments (C) for architectural weakness, stated benefits and costs (B) for a trade-off;
  7. the retrospective entries at the boundary, which can never ground a design code.
- Pointers such as (E.6) name the register section that holds the entry. A pointer is not a finding.

**Rules that apply on every sheet** (amendment, Step 3):
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:325`: "**(1) Conformance:** the code contradicts the register." and "(ii) the prompt omits information the register gives that step, or contradicts the register; (iii) the trace shows a parameter excluded the right item, or admitted a wrong one (e.g. an expansion-reuse or similarity threshold filing a different matter under the key)"
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:335`: "An alternative that meets none of (i)–(iv) counts as ruled out."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:336`: "A probe-type alternative (registry cut, neutral examples, unpruned resolution, re-hinting) is ruled out only by its probe returning *not recovered*, where that probe applies to the case under Step 2b (ii)."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:338`: "it is not ruled out, and the code is implementation defect or unclear."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:340`: "architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:331`: "Implementation was considered and rejected; the step lacked no input the register gives it; no parameter excluded the right item or admitted a wrong one; every available in-design probe was not recovered; and the transcript is not difficult."
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:378`: "with neither oracle nor page evidence, caused-at is unclear. It never defaults to the surfacing step."
- The retrospective rule (lines 347–348) is quoted under *What this register is*.

---

### Sheet E: extraction (admission and extraction)

**Scope.**
- Losses surface at `admitted`, `carried`, `polarity` or `modality`.
- Oracle evidence, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:370`: "recovered by E+R but not R, or by E+R\* but not E+R: extraction (the second is polarity);"
- Exception, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:373`: "where the page shows the deciding claim is a recorded wrong-modality carrier, or a positive carrier of a ruled-out value, that misreads its span, caused-at is extraction (listed);"
- Step type: the gatekeeper and the extractor are LLM steps (A.1, E.1). The extractor has a model condition, probe (i)(d). The gatekeeper has none.

**Candidate causes listed by the amendment** (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`). The page addresses each.
1. "registry-conditioned extraction" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`)
   - Decided by: probe (i), conditions (b) (the registry cut to the resolver's embedding candidates, at `embedding_top_k`=8 and `embedding_min_similarity`=0.30) and (c) (an empty registry). Probe (i) covers every extraction-lost case except `admitted:ignored`.
   - Mapping, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:272`: "implementation choice at extraction. The sub-cause is registry-conditioned extraction, or out-of-domain examples."
   - Mapping, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:278`: "caused at extraction, sub-cause registry-conditioned extraction, class **unclear** (possible implementation)."
   - Entries to check: the whole active registry in the extraction prompt, one key set per meeting, the empty-registry sentinel at meeting a, 116–166 keys at meetings b–d (E.6, How the registry enters); re-extraction of spans that gave no claims, with the larger registry (E.6; mapped to this cause at signing).
2. "out-of-domain prompt examples" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`)
   - Decided by: probe (i), condition (b2): the neutral examples of the probe note in place of the AMI role examples. Mapping as for cause 1 (line 272).
   - Entries to check: the AMI role examples of the extraction prompt, and the session check that none of the four titles occurs in any EL2020 span (E.6, Examples); the ownership sentence (K1.6).
3. "a modality or negation instruction missing from the prompt" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`)
   - Decided by: criterion (ii) and the page. Gloss: no Step 2b condition tests this cause.
   - Entries to check: the polarity and modality instructions (E.6, Examples); `extraction_confidence` requested without a definition (E.6, Not shown); the claim-status mapping (E.6, Parameters).
   - Design to compare: E-C2 and E-C3 (D3.p2); the non-asserted modalities named in D3.p3 (E.2).
4. "the gatekeeper ignoring a span its own criteria admit" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`)
   - Only for `admitted:ignored` cases. No probe applies, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:241`: "Those are gatekeeper losses with no extraction call, and are listed apart."
   - Decided by: criteria (ii)–(iv) and the page (line 339 names `admitted:ignored` cases among those with no probe-type alternative).
   - Entries to check: the gatekeeper prompt's classes and examples; the span sent alone (five lines, no neighbouring spans); the three admitting policies treated alike (A.6).
   - Design to compare: A-C5, the admission criterion of D2.p5 (A.4).
   - If implementation is rejected: the gatekeeper is an LLM step with no model condition, so the class *design or model, not separated* is available, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:331`: "the gatekeeper for `admitted:ignored` cases"
   - At the gatekeeper, architectural weakness or a trade-off also needs the argument of line 340 (quoted on sheet K1). Both this condition and the class apply at the gatekeeper only for `admitted:ignored` cases, as line 331 scopes them.
5. "no whole-decision contract (WD rule only)" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`)
   - Only for `carried:claims_without_the_value`. `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:351`: "WD is judged and admitted only by the Step 2c rule. This sub-cause is never eligible under Step 4(b) and takes no repair slot."
   - Decided by: the WD rule (amendment lines 352–356; criterion (iv)).
   - Entries to check: the WD instructions, run in no evaluated arm (E.6, Arm-specific; X.4, WD).
   - Design: an architectural code may be argued only from D4.p5's scalar-concept passage (amendment line 355; E.2), quoted whole below. D10 and the WD specification are retrospective (E-R1, E-R4 to E-R6).

**Further implementation entries at this boundary** (not in the amendment's list; the pilot may add a cause that rests on one, amendment line 380):
- Segmentation into spans of five transcript lines, with a remainder under three lines joined to the last span (A.6, Parameters). Gloss: this fixes the local window of D2.p4.
- Redactions replace the first occurrence of each fragment before the evidence text is stored; the gatekeeper prompt does not say that a redaction removes the fragment from the extractor's text (A.6).
- Re-extraction of zero-claim spans at later meetings, with the claims keeping their own meeting's source time (E.6; mapped to cause 1).
- Claim identity: two claims of one span with the same hint, value and polarity are stored once (E.6, Parameters).
- `extraction_confidence` has a schema default of 0.8, reachable only after an unrecorded strict-to-non-strict downgrade (E.6, Parameters).
- The guard that fails the call when a claim has an empty `object_value` (E.6, Parameters).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Gatekeeper.
  - Design gives: the stored, segmented span, and D2.p5's criterion: keep potentially useful project context, exclude clearly incidental material (A.3). Not specified: anything beyond the span.
  - Prompt shows: the span alone, with the classes and examples of A.6. No registry, no project description, no neighbouring span.
- Extractor.
  - Design gives: admitted evidence with redactions applied, one local window at a time, no discourse linking (E.3). Whether the extractor sees the registry is not specified (E.3).
  - Prompt shows: the span; the whole active registry (key name, value type, cardinality, label, description, aliases); the instructions and examples of E.6. Not shown: meeting identity, date, neighbouring span, current state (E.6).

**Conformance checklist** (class (1)): A-C1 to A-C4, A-C6 and A-C7 (A.4); E-C1 to E-C5 (E.4); X-C1 and X-C3 (X.2). A-C5, D2.p5's admission balance, is not on this list: it is compared under criterion (ii) and cause 4 (A.4 gloss).

**Disclosed limitations at 94c049d:** window-bounded interpretation without discourse linking (D2.p4, its last two sentences); fallible classification and no privacy guarantee (D2.p5, its third and fourth sentences); misclassified modality or negation (D3.p5). Listed here before as limitations, but tagged (B) or (C) and quotable below: loss before a claim is formed (D2.p2, B); a model-assisted gate (D1.p3, C); no downstream recovery (D1.p4, B). The disclosed limitations cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D1.p3** (C) "ProjectMemory selects the third architecture:" "raw source $\rightarrow$ approved evidence $\rightarrow$ extracted interpretation \\[3pt] $\rightarrow$ proposed change $\rightarrow$ reviewed state." "A source artifact records what was received; approved evidence records what was admitted for further use; a claim records an interpretation; a proposal records a candidate change; a state fact records the outcome projected by the confirmation workflow." "``Approved evidence'' means admitted by the implemented gate, which may itself be model-assisted." "It does not mean that a person verified the statement or that its content is true."
  - **D2.p3** (C) "ProjectMemory chooses early admission." "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created." "Approved redactions are applied before extraction." "Ignored spans and sensitive spans routed for review produce no evidence record through this path." "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts." "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."
  - **D2.p4** (C) "The implemented threshold is permissive within the admitted set." "Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction." "Evidence-only is therefore \emph{not} an enforced prohibition on state extraction."
  - **D2.p5** (C) "The selected balance favours retaining potentially useful project context while excluding clearly incidental material." "It does not settle how selective admission should be."
  - **D3.p2** (C) "ProjectMemory instead represents polarity and modality separately from review status and fact lifecycle." "Positive asserted claims are classified as accepted interpretations, positive non-asserted claims as proposed interpretations, and negative claims as rejected interpretations." "These extraction labels are not acceptance of state." "Extraction confidence likewise describes interpretation, not the probability that a project commitment is true."
  - **D3.p3** (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values." "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value." "Confirmation can accept that proposal while preserving its unconfirmed epistemic status." "Explicit negation does not justify inventing a replacement." "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D2.p2** (B) "Processing everything preserves opportunities for capture but exposes all content to interpretation and review." "Filtering only at answer time retains a broad searchable record and can tailor exclusions to a question, but allows incidental material into durable interpretations first." "Selective admission before extraction places the decision earlier, at the cost of losses before a claim is ever formed."
  - **D2.p4** (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - **D2.p5** (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
  - **D3.p2** (B) "For DR1 and DR4, a simple alternative is to treat every extracted claim as an asserted fact, perhaps weighted by confidence." "This retains mentions but collapses considering a battery into selecting it."
  - **T.rationale** (B) "D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\" "D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- For WD cases (surfaced at `carried:claims_without_the_value`), only D4.p5, quoted whole, whatever the tag of its sentences (amendment line 355):
  - **D4.p5** (B) "The representation choice within an open schema remains substantial." "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics." "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
- Model-limited needs probe (i)(d), `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:279`: "(d) recovered, and (b), (b2) and (c) not recovered."
- Conversational difficulty is limited by the recoverability rules (amendment lines 363–364).

**Retrospective entries here** (cannot ground a design code): A-R1 to A-R4, E-R1 to E-R6, X-R1, X-R6.

---

### Sheet K1: key assignment at extraction

**Scope.**
- Routing losses whose misrouted claim, carrier or rival, was keyed by the extractor's hint. `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:375`: "Its path gives the boundary: a hint means key assignment at extraction; the resolver or expansion means key resolution and expansion."
- Oracle evidence, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:369`: "recovered by R: routing;" R-hint and R-resolver are evidence only, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:204`: "they do not set caused-at."
- Exception, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:374`: "where the displaced rival was about the same matter, R is not routing evidence, and caused-at is set from the page (listed)."
- Path undecided, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:375`: "If the page cannot decide, the code is *routing, path unclear* (possible implementation at both)." Use sheet K2 as well.
- Step type: an LLM output (the hint field of the extraction call) filed deterministically (K1.1). Routing has no model condition (amendment line 331).

**Candidate causes listed by the amendment** (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:385`):
1. "a hint to a registered key about another matter" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:385`)
   - Decided by: criteria (ii) and (iii) and the page. Gloss: Step 2b gives this cause no condition by name; a recovery under (ii-h) maps to cause 2.
   - Entries to check: the hint becomes the claim's key unchecked, and a claim whose key is registered is never resolved again (K1.6, Deterministic logic); the instruction to map each claim to the most specific matching key, and the values each key holds not being shown (K1.6, Evaluated prompt).
2. "registry-conditioned hinting" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:385`)
   - Decided by: probe (ii-h), the spans of hint-routed carriers and rivals re-extracted under (a) (control) and (b) (registry cut). The offline check, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:250`: "Hint-routed carriers have no resolver prompt; their check uses the registry in that meeting's extraction prompt."
   - Mapping, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:276`: "implementation choice at key assignment at extraction, sub-cause registry-conditioned hinting."
   - Applicability: a case whose misfiled claims all lie on one path takes only that path's probe (line 257). A case with misfiled claims on both paths takes the joint condition (line 258; mapping lines 274–275).
   - Entries to check: the registry in the extraction prompt (E.6, How the registry enters).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- The ownership sentence asks for a claim keyed to an owner or assignment key, which a cold-start registry lacks unless one was minted (K1.6).
- The model also writes the literal key `null`; in a1_r2, 31 conflict rows record that no concept definition exists for it (K1.6).
- A0 files a claim under an unregistered hint (bug 5); A1 and A2 do not (K1.6). A0 cases resting on a Phase B bug count as repaired, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:309`: "A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound." Bug 5's design ground is 94c049d D4.p3 (K1-C2): filing a claim under a key with no concept definition contradicts the register, so bug 5 is a conformance defect, and its repair a conformance repair.
- A2's type check can strip a hint and send the claim to the resolver (K1.6; X.4).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Design gives: the claim's content, and the existing concepts' descriptions, aliases, values and question examples (D4.p3; K1.3). D4.p3's matching covers the hint path, so criterion (ii) applies here. Values means the concept definition's canonical values (K1.3).
- Prompt shows: the span, and the whole registry with key name, value type, cardinality, label, description and aliases (E.6). Not shown: negative aliases, example questions, family, related keys, the values a key holds (E.6; K1.6).
- Gloss: question examples are a D4.p3 input that the hint prompt does not show. Canonical values are another: the hint prompt does not show them, and none exists in the nine runs, because the harness clears them on accept (K2.6c). That clearing is the implementation entry that empties the input. The values a key holds are not a D4.p3 input; the hint prompt does not show them either (K1.6, an implementation note).

**Conformance checklist:** K1-C1 to K1-C3 (K1.4); X-C2 (X.2).

**Disclosed limitation at 94c049d:** D4.p4: "neither establishes equivalence". This sentence cannot ground architectural weakness or a trade-off. A loss resting on it is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
- For a trade-off (B):
  - **D4.p2** (B) "DR7 makes an unmatched claim a normal case." "Discarding it keeps the schema coherent but loses novel state." "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning." "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition." "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
  - **D4.p4** (B) "This supports an empty initial registry without treating generated labels as research outcomes." "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
  - **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- The hint field of the extraction call is an LLM step with no model condition, so the page must also meet the condition of line 340, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:340`: "At an LLM step with no model condition," "architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value." "Otherwise the case is design or model, not separated."

**Retrospective entries here:** K1-R1 to K1-R4; D10 (E-R1); X-R6.

---

### Sheet K2: key resolution and expansion

**Scope.**
- Routing losses whose misrouted claim was routed by the resolver or by expansion (line 375, quoted on sheet K1). Oracle evidence and the same-matter exception as on sheet K1.
- `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:251`: "Expansion-routed misfilings (the resolver returned no key, and expansion reused or created one) are not probed. They are coded from the trace, under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry."
- Gloss: losses where a claim stays parked because its concept is never accepted (D4.p4's delayed availability) also belong here when the page shows it.
- Step type: mixed (K2.1). The resolver and candidate generation are LLM steps with no model condition (amendment line 331; for candidate generation, line 251: expansion-routed misfilings are not probed).

**Candidate causes listed by the amendment** (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:386`):
1. "the shortlist or prune excluded a fitting key" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:386`)
   - Decided by: the offline check whether the gold-holding key, or a fitting one, was in the resolver prompt; and probe (ii-r), the resolver-routed carriers and rivals re-resolved with the unpruned registry against the recorded prompt as control.
   - Mapping, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:273`: "only where the offline check shows the fitting key was missing from the recorded prompt; otherwise the sub-cause is set on the page, within key resolution."
   - Entries to check: `_prompt_registry` (the embedding part at 8 and 0.30, the lexical part with `STOPWORDS`, the whole registry at or below 12 keys) (K2.6a); the parameter table (K2.6, Parameters).
2. "the harness reviewer accepted a near-duplicate or over-broad key" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:386`)
   - Decided by: the trace and the page (line 251).
   - Entries to check: `_reviewer_would_accept` checks only key shape, a label and evidence text; no reject is submitted under `quality`; accepted keys have canonical values cleared; a merge adds the proposal's aliases to the target key; every pending proposal is reviewed again at every meeting (K2.6c).
3. "a reuse or similarity threshold merged a new matter into an existing key" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:386`)
   - Decided by: criterion (iii), from the trace (line 251).
   - Entries to check: semantic reuse at `expansion_reuse_threshold` 0.80 (K2.6b, step 3); the alias merge, plain substring containment on the whole span with the first match in key-name order, behind 41 of the 42 rule-based merges in a0_r1 and 38 of 38 in a1_r2 (K2.6b, step 1; mapped to this cause at signing).
   - Design to read it against: D4.p4 (K2.2 gloss). K2-R3's sentence on semantic reuse is retrospective.

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- `_KEY_SHAPE` admits keys of five or more segments that the validator refuses; such proposals stay pending and their parked claims are never released (K2.6c; 0–8 accept-error review records per run, from 0–2 distinct proposals per run, each holding one parked claim; no listed cause, left to the pilot).
- A claim parked at an earlier meeting is never routed again, even when the registry later gains a fitting key; it reaches state only through its own proposal's acceptance or merge (K2.1).
- At meeting a every write-path resolver call lists no key, so every claim goes to expansion (K2.6a; no listed cause, left to the pilot).
- The first remaining primary key is taken; supporting keys, `needs_clarification` and `confidence` are not used on the write path (K2.6a). On the read path broad questions append the supporting keys (R.6).
- The routed text is the claim's subject and value; the span is sent only when both are empty; polarity, modality and the values each key holds are not shown (K2.6a).
- The expansion generator sees only key names, domains and families (K2.6b). Criterion (ii) does not apply to it (see below); a page can still note this entry. Its silent fallback to rules did not occur in these runs (K2.6b).
- A2's type-check re-routes (K2.6, Arm-specific; X.4).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Resolver.
  - Design gives: the claim's content; the existing concepts' descriptions, aliases, values and question examples (D4.p3; K2.3). Values means the concept definition's canonical values (K1.3).
  - Prompt shows: the claim's subject and value; for the pruned registry, key name, label, description, aliases, negative aliases and value type (K2.6a). Not shown: cardinality, family, example questions, the values a key holds.
  - Example questions never reach the prompt. They enter only deterministically: through the embedding profile behind the shortlist, and, for a text that `is_broad_list_question` accepts, through the rule candidates (K2.6a).
  - Values: the prompt does not show canonical values, and none exists in the nine runs, because the harness clears them on accept (K2.6c). That clearing is the implementation entry that empties the input. The input would also reach the embedding profile, empty in these runs (K2.6a).
  - The values a key holds are not a D4.p3 input. Claim routing never sees them (the context digest is off, K2.6a); an implementation note.
- Expansion generator. Criterion (ii) does not apply to expansion-routed misfilings, which `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:251` codes "under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry", and a generator merge reaches the registry only through the harness reviewer's acceptance. The lines below are an implementation entry a page can note.
  - Design gives: the claim and its triggering evidence; the preference for scalar concepts with family metadata (D4.p5; K2.3).
  - Prompt shows: the claim's value, subject and predicate, the evidence as context only, and the names of all keys, domains and families. Not shown: the labels, descriptions, aliases and values of existing keys (K2.6b). Neither canonical nor held values are shown.
- Concept review.
  - Design gives: the expansion, a candidate definition with its triggering evidence; acceptance criteria are not specified (K2.3).
  - The harness reviewer checks: key shape, a label, supporting evidence text (K2.6c).

**Conformance checklist:** K2-C1 to K2-C6 (K2.4); X-C1 and X-C2 (X.2). D4.p4's sentence that matching does not establish equivalence is a disclosed limitation (K2.4), not a checklist item; criterion (iii) is read against it (cause 3).

**Disclosed limitations at 94c049d:** matching does not establish equivalence, and review may merge distinct meanings or miss synonyms (D4.p4, its last two sentences); the reviewer shapes which concepts survive (D4.p6, its last two sentences). They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies. Stated costs, which are (B) and quotable below: parking delays availability (D4.p4); fragmentation and near-duplicates (D4.p5); waiting for concept review (D1.p4, D6.p4).

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D4.p2** (B) "DR7 makes an unmatched claim a normal case." "Discarding it keeps the schema coherent but loses novel state." "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning." "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition." "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
  - **D4.p4** (B) "This supports an empty initial registry without treating generated labels as research outcomes." "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
  - **D4.p5** (B) "The representation choice within an open schema remains substantial." "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics." "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
  - **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation." "It does not establish that fine-grained concepts are universally better."
  - **D6.p4** (B) "The costs are intrinsic." "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error." "Deferral and parking can make a correctly extracted fact unavailable when needed."
  - **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- The resolver and candidate generation are LLM steps with no model condition. At either step the page must also meet the condition of line 340 (quoted on sheet K1); otherwise the case is design or model, not separated.

**Retrospective entries here:** K2-R1 to K2-R7; D10 (K2-R4); X-R1; X-R6.

---

### Sheet S: state rules (with A2's contracts and support check)

**Scope.**
- Losses that surface at `filed` (A2 parks), `proposed`, `applied`, `current` or `status`, where the page or an oracle puts the cause in the state rules.
- Oracle evidence, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:371`: "not recovered by E+R\*: state rules, transcript or evaluation."
- A2, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:376`: "a contract whose leave-one-out recovers the row sets caused-at to the state rules (that contract)."
- No probe-type alternative applies, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:339`: "Where no probe-type alternative applies, alternatives are ruled out under (ii)–(iv) and the page as above."
- Step type: deterministic (S.1). A2's support check is an LLM step with no model condition (amendment line 331).

**Candidate causes listed by the amendment** (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:387`):
1. "the settle expired a correct proposal" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:387`)
   - A1 and A2 only. Decided by: the trace and the page.
   - Entries to check: `repair_settle_pending`, one pass before each confirmation with no time window; a pending proposal the pass does not return again expires (S.6, Rules and Parameters; X.4, `repair_settle_before_confirm`).
2. "any state behaviour contradicting the register" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:387`)
   - Decided by: the conformance checklist below, against the rules of S.6.

**Conformance checklist** (S.4; the rule of S.6 to compare is a gloss):
- Promotion and negation: S-C1 to S-C4. Compare E1, Rule 1 and Rule 2 (S.6).
- Collections: S-C5. Not reached; every key in the nine runs is scalar.
- Resolution: S-C6 to S-C11. Compare the ranking key, Rules 3 to 5, `DISSENT_THRESHOLD` (S.6).
- Proposal and confirmation: S-C12 to S-C15. Compare Proposals and Confirmation (S.6).
- Projection: S-C16 to S-C18. Compare Projection (S.6).
- Records and links: X-C1 and X-C2 (X.2).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- Within one meeting, authority and source time are equal, so `extraction_confidence` decides, and equal confidences make a tie conflict; the extraction prompt does not define it (S.6, Rule 3; E.6).
- Value identity in the engine is the exact raw string for every key in these runs, since no key has canonical values; case and version tokens are not normalised. Lower case is compared only in E1, in reject projection and on the unused collection path. A2's equivalence (normalised equality or cosine ≥ 0.80) does not reach rule 3's tie test (S.6, Rules).
- Proposals are deduplicated by key, value and type; in A0 any earlier proposal with the same key blocks a new one (bug 12) (S.6).
- The structural value confirmation: `scrub_gold_value`, the rule of a word of at least four characters, and `_STOPWORDS` with AMI words (S.6). It is an implementation entry, marked harness, like the concept reviewer; no listed cause, left to the pilot.
- A reject proposal demotes a current fact with the same value compared by lower case; the current fact is the most recently updated current fact of the key (S.6, Projection).
- Source time: the ingestion clock in A0 (bug 6), the meeting date in A1 and A2 (E.6; X.4).
- The order of evaluation: the repaired settle is the only pass that evaluates every key with all its claims just before confirmation (S.6).
- The A1 repair rules (X.4). Bug 3's rule (the current value's own claims compete; an exact tie keeps the current value) is retrospective design: its wording rests on the 5de9911 per-key sentence (S-R3). An A1 state-rule loss whose only design ground is this rule is implementation choice if an alternative consistent with the 94c049d text meets (i)–(iv), and unclear otherwise; it is tallied in the retrospective column (amendment lines 348–349).

**A0.** Line 309 (quoted on sheet K1) applies. The Phase B bugs whose repairs act at this boundary are 1, 2, 3, 4, 6, 12 and 13 (gloss; X.4; S-R10, S-R11).

**A2's contracts** (retrospective design, S-R9; implementation, X.4):
- Each contract's leave-one-out can set caused-at (line 376 above).
- An open same-meeting conflict is coded held: conflict decision (S-R12).
- Support check (`filing_support_check`), an LLM step with no model condition:
  - Specified (retrospective, S-R9): that the linked span establishes the claim's value, commitment status and time.
  - Prompt shows: the span, the key's label only, the value and a status phrase. Not shown: the key's description, the rival values, the meeting (S.6).
  - Criterion (ii) compares this prompt with the contract's retrospective wording too, so the meeting missing from the prompt is a checklist item. The alternative must still be consistent with the 94c049d text (amendment line 348).
  - Only 313 of 534 a2_r1 claims carry a recorded verdict (S.6).
- Type check: deterministic (K1.6; X.4).
- Same-meeting conflict and new-evidence rules: deterministic, with embedding equivalence at 0.80 (S.6, Arm-specific; X.4).

**Disclosed limitations at 94c049d:** D3.p3 (the affirmation check: the sentence on negating the current value, which is on the claims register's R-4 list, and the legacy-policy sentence), D5.p5, D5.p6's first sentence, D6.p4's edited-proposal sentence, D6.p5, D7.p3's fallback sentences, D7.p5's non-atomic projection, D9.p4, D9.p5. They are listed in S.4. They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence. The sentence of D3.p3 on negating the current value is a commitment but is on R-4's list, so it is not listed.
- For architectural weakness (C) (D3.p4 and D3.p5's collection rules bind no evaluated key; D7.p4's first sentence binds collections only):
  - **D3.p3** (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values." "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value." "Confirmation can accept that proposal while preserving its unconfirmed epistemic status." "Explicit negation does not justify inventing a replacement." "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
  - **D5.p2** (C) "ProjectMemory selects an authority-gated temporal policy, leaving unresolved cases reviewable."
  - **D5.p3** (C) "The governing principle is that authority determines eligibility to supersede and recency orders temporally eligible evidence." "In the scalar policy, a challenger must have at least the current fact's authority and a source time no earlier than the fact's validity start." "Eligible challengers are ranked by authority, source time, and extraction confidence." "Authority thus retains precedence within the eligible set; recency does not override a higher eligible authority." "The same ranking selects an initial asserted positive candidate." "Different initial values tied on all three dimensions produce a conflict."
  - **D5.p4** (C) "Checking eligibility before ranking matters." "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered." "Lower-authority dissent does not overwrite current state." "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict." "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat." "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."
  - **D6.p2** (C) "ProjectMemory instead routes new values, replacements, and current-default rejection outcomes through a reviewable proposal and a separate confirmation operation:" "machine interpretation $\rightarrow$ proposal $\rightarrow$ confirmation $\rightarrow$ projection."
  - **D6.p3** (C) "The project-specific application is to expose the proposed value, concept, prior value, target status, evidence, and reason before projection." "Confirmation can accept, reject, edit, defer, or request more evidence." "Its review record is stored separately from the proposal and before the requested projection." "An existing fact can also be placed under review without immediately deleting it." "Review identifies a responsibility and contestability boundary; its occurrence does not establish truth."
  - **D7.p2** (C) "ProjectMemory instead preserves current and superseded facts, validity bounds, and replacement links."
  - **D7.p3** (C) "An accepted scalar replacement closes the prior fact's validity interval, marks it superseded, creates a successor with a backward supersession link, and completes the predecessor's forward link." "The winning claim's source time is carried as the proposal's effective time and becomes the new validity start; the predecessor's validity end uses the same boundary."
  - **D7.p4** (C) "Collections retain independent members instead of superseding siblings." "Rejection also differs from positive replacement." "Applying rejection can demote a matching current row to rejected and close its validity, or record a ruled-out alternative without displacing another current value." "This branch does not construct the predecessor--successor pair of a scalar replacement." "A rejected proposal, by contrast, records a review decision without creating a rejected fact about the project."
  - **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts." "Normal projection copies proposal evidence identifiers to the fact." "Application events connect proposals with facts and record the actor." "Citations expose stored evidence text and source identifiers." "This adapts provenance principles; it is not a claim of PROV conformance."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D2.p4** (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - **D5.p2** (B) "Newest-statement-wins is transparent but treats later mentions as replacements." "Highest-extraction-confidence-wins confuses interpretation confidence with authority." "Highest-authority-wins preserves priority but can privilege stale evidence." "Human-only resolution permits contextual judgement at the cost of reviewing every contradiction."
  - **D5.p6** (B) "The intended consequence is stable state under casual dissent, replacement by eligible later commitments, and exposed unresolved conflicts."
  - **D6.p2** (B) "Direct model mutation minimises delay." "Confidence-threshold approval retains automation but uses an admission rule whose reliability must be established." "Manual entry keeps responsibility explicit while moving capture and maintenance back to the user."
  - **D6.p4** (B) "The costs are intrinsic." "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error." "Deferral and parking can make a correctly extracted fact unavailable when needed."
  - **D6.p6** (B) "The intended consequence is that changing confirmation policy changes which interpretations become answerable, making quality and availability trade-offs observable."
  - **D7.p2** (B) "For DR2 and DR3, overwriting a value makes current retrieval simple but loses its prior validity." "Appending every value without status preserves the record while making each question reconstruct currency."
  - **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
  - **D7.p5** (B) "It costs additional transitions and consistency obligations."
  - **T.rationale** (B) "D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\" "D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\" "D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- For conflicts, D5.p2's sentence on leaving unresolved cases reviewable (above; S-R4 gloss).
- A2's support check is an LLM step with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1).

**Retrospective entries here:** S-R1 to S-R12; X-R1; X-R2; X-R3; X-R4; X-R6.

---

### Sheet R: reading

**Scope.**
- Rows stored with the right status in the recorded run; losses surface at `key_reached`, `in_payload` or `answered`.
- Caused-at, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:377`: "from the offline reading analysis, probe (iii) and the page."
- Step type: mixed (R.1). Question routing and the grounding pass are LLM steps with no model condition (amendment line 331).

**Candidate causes listed by the amendment** (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:388`):
1. "the question-time shortlist excluded the holding key" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:388`)
   - Applies only where the offline reading check shows the holding key was pruned out. `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:337`: "Where the key was in the recorded question-routing prompt, that check rules it out."
   - Decided by: probe (iii), re-resolution with the unpruned registry. Mapping, `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:277`: "implementation choice at reading, sub-cause the question-time shortlist excluded the holding key."
   - Entries to check: question resolution through `_prompt_registry`, 8–177 keys listed per call (R.6); the shortlist parameters (K2.6, Parameters).
2. "the scalar focus gate demoted a correct fact to a near match" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:388`)
   - Decided by: the page. Gloss: no probe tests this cause.
   - Entries to check: the scalar focus gate; the relevance filter at `answer_relevance_min_similarity` 0.42; focus terms of four or more characters outside `_FOCUS_STOPWORDS`, which include AMI words (R.6; an implementation entry with no listed cause, left to the pilot); the removal of the focus key's own label and alias words from the focus terms, which decides broad versus specific and whether the gate runs at all (R.6).
   - Design to read it against: D8.p3 (the gate's outcome: an explicit unknown, with nearby facts kept as near matches) and D8.p4 (its stated cost, restricted answerability) (R.3). The relevance test itself is implementation (R.3).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- Widening after the resolver (R.6):
  - broad questions take the rule candidates after the LLM's picks, up to 10 keys, ranked by the rule-scorer weights and the embedding bonus at `embedding_score_weight` 5.0;
  - they then append the resolver LLM's supporting keys up to 10; the 0.25 candidate ratio is inert on the LLM path;
  - value-matched keys at cosine 0.55, up to 6; family siblings up to 10.
- Rejection questions also read the current facts of resolved keys whose names contain `reject` (R.6).
- Change questions add keys that declare `change_explanation` primary; minted keys declare no intents (R.6).
- Near-duplicate values are canonicalised at 0.80, with no cap (R.6).
- The grounding pass's revised answer replaces the prose; it is skipped for provenance questions (R.6).
- A2 adds a disputed answer for open same-meeting conflicts (R.6, Arm-specific).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Question routing.
  - Design gives: the question, and the concepts' descriptions, aliases, examples and observed values (D8.p3; R.3).
  - Prompt shows: the question with its intent, and the pruned registry with key name, label, description, aliases, negative aliases and value type (K2.6a). Not shown: example questions, the values each key holds (R.6). Observed values enter only through the deterministic value-match widening (R.6). Example questions enter only deterministically: through the embedding profile behind the shortlist, and, for broad questions, through the rule candidates (K2.6a; R.6).
- Answer context and grounding.
  - Design gives: current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions and decision records (D8.p3; R.3).
  - The grounding pass sees: the question, the drafted answer, the citations and the current facts (key, value, status, review state). `review_state_present` was False in every call (R.6).
  - The grounding pass has no 94c049d design entry: Chapter 4 text outside D1–D9 is context only (amendment line 102; R.3; Annex).

**Conformance checklist:** R-C1 to R-C9 (R.4), which include D1.p5's requirement on answers (X.1).

**Disclosed limitations at 94c049d:** unknown cannot tell absence from loss (D8.p3, its sixth sentence); the latest-addition change heuristic (D8.p5, its last three sentences); citation granularity and provenance by ingestion order (D9.p5); links need not support the value (D9.p6, its first two sentences). They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies. Stated costs, which are (B) and quotable below: restricted answerability (D8.p4); weaker historical coverage (D8.p6).

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D1.p5** (C) "If it behaves as intended, tentative or rejected interpretations should not appear as settled answers, and returned facts should carry inspectable evidence."
  - **D2.p3** (C) "ProjectMemory chooses early admission." "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created." "Approved redactions are applied before extraction." "Ignored spans and sensitive spans routed for review produce no evidence record through this path." "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts." "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."
  - **D3.p5** (C) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
  - **D5.p4** (C) "Checking eligibility before ranking matters." "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered." "Lower-authority dissent does not overwrite current state." "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict." "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat." "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."
  - **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
  - **D8.p2** (C) "ProjectMemory selects a different context-construction order for DR2, DR4, and DR5: resolve concepts and facts first, then follow evidence links."
  - **D8.p3** (C) "Concept descriptions, aliases, examples, and observed values associate a question with generated concepts." "Broad list questions may aggregate candidate concepts and family siblings; specific questions remain narrower." "Normal context contains current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions, and decision records." "Templates distinguish confirmed from proposed values." "If no concept, current fact, or relevant value answers a specific question, the service can return an explicit unknown outcome and retain nearby facts only as near matches." "Although the public schema defines a disputed outcome, ambiguous facts are excluded by ordinary current-fact retrieval and normally reach the unknown branch; a standing confirmed fact can instead carry a conflict caveat."
  - **D8.p4** (C) "Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims, or events." "Current code adds a bounded exception: rejection-phrased questions can retrieve rejected facts for resolved concepts, including scalar alternatives never previously current." "Negative interpretations must first reach a representable, projected lifecycle state; rejected expansions and rejected state proposals do not become answerable merely because they persist."
  - **D8.p5** (C) "For collection-like or multi-concept questions, it selects current facts whose earliest linked source artifact is the most recently ingested artifact."
  - **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts." "Normal projection copies proposal evidence identifiers to the fact." "Application events connect proposals with facts and record the actor." "Citations expose stored evidence text and source identifiers." "This adapts provenance principles; it is not a claim of PROV conformance."
- For a trade-off (B):
  - **D2.p5** (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
  - **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation." "It does not establish that fine-grained concepts are universally better."
  - **D8.p2** (B) "The read-side alternative is to retrieve transcript passages first and ask a model to infer state for the question." "This keeps broad source access and avoids a write-time schema, but repeatedly places temporal and epistemic interpretation at the question boundary."
  - **D8.p4** (B) "The narrower context is intended to reduce exposure to superseded alternatives and attach evidence to the selected state." "Its cost is restricted answerability."
  - **D8.p6** (B) "The expected behavior is current-value accuracy with meaningful abstention and evidence support, alongside weaker historical coverage."
  - **D9.p6** (B) "The intended consequence is an answer whose evidence permits verification and correction."
  - **T.rationale** (B) "D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- Question resolution and grounding are LLM steps with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1).

**Retrospective entries here:** R-R1 to R-R7; D11 (R-R1); A-R1's read-side sentence (R-R4); X-R2; X-R4; X-R6.

---

## Coverage of the design-text file

The file holds 51 D-paragraph ids and the rationale table (T.rationale): 52 ids in all. Every id is assigned. Tags as above; X = cross-cutting.

| Id | Sections | Tags | Note (gloss) |
|---|---|---|---|
| D1.p1 | X | T | |
| D1.p2 | X | B | alternatives only |
| D1.p3 | X, A, E | C | |
| D1.p4 | X, A, E, K2, S | B | costs by boundary |
| D1.p5 | X, S, R | L, C, E | |
| D2.p1 | A | T | |
| D2.p2 | A | B | |
| D2.p3 | A, E, R | C | |
| D2.p4 | A, E, S | C, B, L | |
| D2.p5 | A, R | C, L, B, E | |
| D3.p1 | E | T | |
| D3.p2 | E | B, C | |
| D3.p3 | E, S | C, L | the C sentence on negating the current value is on R-4's list; not quotable |
| D3.p4 | S | C, B | collections only; binds no evaluated key |
| D3.p5 | E, S, R | C, L, E | collection sentences bind no evaluated key |
| D4.p1 | K1, K2 | T | |
| D4.p2 | K1, K2 | B | alternatives only |
| D4.p3 | E, K1, K2 | C | |
| D4.p4 | K1, K2 | B, L | deleted from the chapter at c6fbdc0; kept here |
| D4.p5 | E, K2, R | B, C | WD's 94c049d ground per the amendment, whole; scalar sentences C |
| D4.p6 | K2, R | B, E, L | |
| D5.p1 | S | T | |
| D5.p2 | S | B, C | conflicts: leaving unresolved cases reviewable |
| D5.p3 | S | C | |
| D5.p4 | S, R | C | |
| D5.p5 | A, S | L | |
| D5.p6 | A, S | L, B, E | first sentence L (28 October 2026) |
| D6.p1 | S | T | |
| D6.p2 | S | B, C | |
| D6.p3 | S | C | |
| D6.p4 | K2, S | B, L | |
| D6.p5 | S | L | |
| D6.p6 | S | B, E | |
| D7.p1 | S | T | |
| D7.p2 | S | B, C, L | |
| D7.p3 | S | C, L | |
| D7.p4 | S | C | first sentence: collections only |
| D7.p5 | S, R | B, L, C | first sentence B and C |
| D7.p6 | S | E | no requirement |
| D8.p1 | R | T | |
| D8.p2 | R | B, C | |
| D8.p3 | R | C, L | |
| D8.p4 | R | B, C | |
| D8.p5 | R | C, L | |
| D8.p6 | R | B, E | |
| D9.p1 | X | T | |
| D9.p2 | X | B, C, L | |
| D9.p3 | X, A, E, S, R | C | |
| D9.p4 | X, S | L | |
| D9.p5 | X, S, R | L | |
| D9.p6 | X, R | L, B, E | |
| T.rationale | X (D1, D9), A (D2), E (D3), K1 and K2 (D4), S (D5–D7), R (D8) | B | one row per decision |

**Assigned to no component:** none.

**Assigned, but binding no key in the evaluated runs:** the collection rules in D3.p4, D3.p5 (first three sentences) and D7.p4 (first sentence). Every key in the nine EL2020 state dumps is scalar.

**Assigned for rationale or evaluation scope only (no requirement):** D1.p2, D2.p2, D4.p2, D7.p6, and the (E) sentences of other paragraphs.

---

## Decisions for the author

Each needs your judgement before signing. My recommendation is given. **Record of 28 October 2026:** the author asked that every decision take its recommendation. Each decision below carries the reading written into the sections and sheets above (decision sheet B22), so no sheet points to this list any more. The list stays as the record of the questions.

1. **Does D4.p3's matching cover the extractor's key hint?** D4.p3 names one matching step and its inputs; the code assigns keys on two paths (the extraction hint and the resolver).
   - (a) Yes: the matching inputs (claim content; concept descriptions, aliases, values, question examples) apply to the hint path too, so criterion (ii) can apply to hint-routed cases.
   - (b) No: the hint path has no design inputs, so criterion (ii) cannot apply to it.
   - Recommendation: (a). The 94c049d text describes one matching step without naming a path, and both code paths perform it.
   - **Reading written into the sheets** (28 October 2026; decision sheet C12): (a). K1.3, E.3 and sheet K1 state it.
2. **Can a 94c049d sentence that discloses a shortfall ground architectural weakness or a trade-off?** Examples: D3.p3 (affirmation check), D5.p5, D6.p4–p5, D7.p3 (fallback), D7.p5, D9.p4–p5. Several describe behaviour that Phase B later called bugs 1, 2, 3 and 6.
   - (a) No: they are disclosed implementation limitations. A loss resting on one is an implementation defect (or, for A0, repaired under the Phase B rule).
   - (b) Yes: they are 94c049d text and can be quoted on a case page like any other.
   - (c) Case by case on the page.
   - Recommendation: (a) for sentences that state a shortfall against a principle of the same decision (for example D5.p5: "conflict handling is not uniformly complete"), and (b) only for sentences that state a deliberate choice with a stated benefit (for example D2.p4's permissive threshold, D4.p4's parking).
   - Added at review (27 October): D4.p4's sentence that alias-based or semantic matching does not establish equivalence was listed as requirement K2-C7. It is now a disclosed limitation (K2.4), as K1.4 lists it, so it falls under this decision. It stays the text that criterion (iii) is read against (K2.2 gloss).
   - **Reading written into the sheets** (28 October 2026; decision sheet C8, with both Corrections): (a). Sentences that state a shortfall (L tags), the claims register's R-4 list, and D4.p4's sentence that matching does not establish equivalence cannot ground architectural weakness or a trade-off. A (B) sentence may ground a trade-off and a (C) sentence architectural weakness. Correction 1 replaces the second sentence of option (a): a loss resting on such a sentence is coded conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies; for A0, line 309 applies. Correction 2: each sheet now lists its quotable sentences one by one, each with its tag. Tags changed on 28 October: D4.p5's scalar sentence (C) in E.2 (decision sheet C17); D5.p6's first sentence (L); D7.p5's first sentence (B, C) in S.2 and R.2. The sentence of D3.p3 on negating the current value keeps (C) but is on R-4's list, so no sheet lists it as quotable.
3. **Bug 5's design ground.** The bug list cites D4 with D10's wording of 19 October.
   - (a) Ground it in 94c049d D4.p3 (claims enter ordinary state resolution after concept acceptance or merging), so filing under an undefined key contradicts the register.
   - (b) Treat its ground as retrospective (D10).
   - Recommendation: (a), and note that the bug list quoted D10. For A0 the Phase B rule applies either way.
   - **Reading written into the sheets** (28 October 2026; decision sheet C11): (a). K1-C2, K1-R2 and sheet K1 state it.
4. **The A1 rule for bug 3 (the current value's own claims compete).** Plan 23 calls it the Ch. 4 rule; the wording it rests on is the 5de9911 per-key sentence. 94c049d D5.p3 ranks eligible challengers and is silent on the current value's claims; D5.p5 discloses the missing tie check.
   - Added at review (27 October), for you to weigh before choosing. One 94c049d sentence states which claims scalar resolution considers, D9.p4: "Scalar resolution considers all claims for a concept, while proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation." It sits in a disclosed provenance limitation. It does not by itself say that the current value's agreeing claims rank against challengers (S.2, S.3 glosses).
   - Further post-9-September readings that call the A1 rule the Ch. 4 rule: plan 23 at b4d6b6c, line 118 (S-R10), and the bug list's repair table at 3320375, line 170 (S-R11), beside plan 23 lines 198 and 226 (S-R10).
   - (a) Treat the A1 rule as an implementation entry consistent with D5.p3's principle.
   - (b) Treat it as retrospective design: A1 state-rule losses whose only design ground is this rule are coded under the amendment's retrospective rule.
   - Recommendation: (b). It does not let 5de9911 text stand in for 94c049d text.
   - **Reading written into the sheets** (28 October 2026; decision sheet C10): (b). S.2, S.3, S-R3 and sheet S state it.
5. **Harness-side code that decides which proposals become keys and facts.** The amendment names the concept reviewer `_reviewer_would_accept` as an implementation entry (amendment line 107). It does not name the harness's value-confirmation policy (`_internal_confirm_structural`, `_confirmable_value`), the A1 settle (`repair_settle_pending`) or the judge wrapper of bug 7. (This item merges decision 5 of the design part with the implementation part's item on harness-side code.)
   - (a) List the concept reviewer, the value confirmation and the settle under implementation, marked harness, as this register does (K2.6c, S.6). Keep the judge under the held-constant controls (H) and the bug-7 wrapper as an instrument repair (X.4).
   - (b) Move the value confirmation and the judge wrapper to the evaluation side (the evaluation-defect class).
   - Recommendation: (a). The value confirmation is the value-confirmation counterpart of `_reviewer_would_accept`, and the confirmation and the settle decide which proposals become facts.
   - **Reading written into the sheets** (28 October 2026; decision sheet C15): (a). S.2 and sheet S state it.
6. **Other 94c049d Chapter 4 text** (Annex): Final Artifact, Operational Limits, the domain-records and requirements tables.
   - (a) Keep the register to D1–D9 and the rationale table, as the amendment words it.
   - (b) Add named Annex passages as design entries.
   - Recommendation: (a), with the Annex attached to the register as context that cannot ground a design code. Note that under (a) the grounding pass has no 94c049d design entry.
   - **Reading written into the sheets** (28 October 2026; decision sheet A1): (a). The Annex and sheet R state it.
7. **Code docstrings and comments that state intended behaviour** (cited by bugs 1 and 12).
   - Recommendation: implementation entries, as the amendment rules for prompt text (amendment line 107); a code path that contradicts its own docstring is then coded against the implementation part, not the design part.
   - **Reading written into the sheets** (28 October 2026; decision sheet A2): as recommended.
8. **The label D1 for WD in plan 23** (Phase C, line 225 at b4d6b6c; line 264 in the working tree) collides with Chapter 4's D1.
   - Recommendation: write WD there as part of the Step 0 plan-23 fix that already replaces that line's metric.
   - **Reading written into the sheets** (28 October 2026; decision sheet B1): as recommended (E-R6).
9. **Post-9-September sentences that report observations.** The amendment names the 38a0f4a sentence as not a design entry. The b422b27 sentence on the gate ignoring 76 of 251 spans is of the same kind.
   - Recommendation: mark it, and any like it, as not a design entry. As a retrospective entry it could not ground a design code anyway, so only the label changes.
   - **Reading written into the sheets** (28 October 2026; decision sheet B2): as recommended (A-R1).
10. **Reproducibility of the register's checks.** These checks are scratch work in the session scratchpad and are not committed:
    - the design-quote and code-reference check (`check_register.py`, with `paras.json` built from the design-text file), which the merge also ran on this file (Checks). **Resolved at review (27 October):** the package now holds `23-am1-check-register.py`, which checks every quote and code reference of this file from git objects and files alone (Checks; companion-files table). The items below stay open;
    - the code-derived prompt hashes (expansion generator `f570f53a…`, judge `8469921d…`, RAG `a2d74d5e…`, WD extraction template `daf30b70…`), the equality of the recorded system prompts with the 3320375 constants, and the schema-strictness checks;
    - the alias-merge check (41 of 42 rule-based merges in a0_r1, 38 of 38 in a1_r2);
    - the merge's own completeness check (Checks).
    - (a) Commit a separate script (for example `23-am1-code-prompts.py`) that parses `git show 3320375:` string constants with `ast`, re-derives the code-derived hashes and re-runs the alias check from `trace.json` and `state.json`. (The quote-checker part of this option is done: `23-am1-check-register.py`.) `23-am1-prompts.py` stays trace-only, as specified.
    - (b) Extend `23-am1-prompts.py` to read git objects and `state.json` as well.
    - (c) Leave them as session notes in the register.
    - Recommendation: (a). The register cites these numbers, so they should be reproducible before the amendment is tagged.
    - **Reading written into the register** (28 October 2026; decision sheet B3): (a), a committed script before the tag. It is a pre-tag item, not done in this file.
    - **Merge completeness** (28 October 2026, pre-tag follow-ups): closed: one-time historical check, result in the register's Checks section (`verify_merge.py`). Its inputs, the two pre-merge parts, were scratch files and never in the repository, so `23-am1-check-package.py` reports it as closed, not as a check it re-derives. The other items of this decision are re-derived by that script (its check 4).
11. **Thresholds the runner does not pin and the run artifacts do not record:** `embedding_top_k`=8, `embedding_min_similarity`=0.30, `resolver_prune_threshold`=12, `embedding_score_weight`=5.0, `answer_relevance_min_similarity`=0.42, `answer_canonical_min_similarity`=0.80, `answer_canonical_max_items`=0, `llm_max_attempts`=3. Settings reads `.env` for declared fields (`app/core/config.py:188-192` at 3320375). `.env` was not read under the build rules. Probe (b) of Step 2b relies on 8 and 0.30 as the evaluated parameters. Already confirmed from run artifacts: `expansion_force_scalar` and families (prompt text, `state.json`), `scalar_negation_rejects` (E1 rows in the trace), multi-key facets off, and the embedding model (`usage.json`).
    - **Record added at review (27 October 2026).** The check of option (a) has been made, by the main session, by variable name only; `.env` was not printed.
      - `.env` was last modified on 6 August 2026, before the runs. It sets none of the eight thresholds above, including `llm_max_attempts`.
      - It sets `EMBEDDING_MODEL=text-embedding-3-small`, which agrees with H. It does not set `EXPANSION_AUTO_ACCEPT` or an embedding cassette path.
      - The lane scripts set only `OPENAI_API_KEY`, `PM_STUDY_BUDGET_FILE` and `EXPANSION_AUTO_ACCEPT=false`. The runner at 3320375 pins none of the eight.
      - Residual limit: the process environment at run time is not recorded, and process environment variables take precedence over `.env`. This weighs more for a1_r1, which has no lane script.
    - What remains for you: whether this record satisfies option (a), or whether (b) or (c) is still wanted for the residual limit.
    - (a) You check `.env` for these variable names only (EMBEDDING_TOP_K, EMBEDDING_MIN_SIMILARITY, RESOLVER_PRUNE_THRESHOLD, EMBEDDING_SCORE_WEIGHT, ANSWER_RELEVANCE_MIN_SIMILARITY, ANSWER_CANONICAL_MIN_SIMILARITY, ANSWER_CANONICAL_MAX_ITEMS, LLM_MAX_ATTEMPTS, EMBEDDING_MODEL) and record 'not set', or the values, in this register.
    - (b) Register the defaults, marked 'not confirmed from run artifacts'.
    - (c) Confirm them later from a cassette-backed replay.
    - Recommendation: (a) before signing. If that is not possible, (b)'s wording. After the record above: accept it as (a), and keep the residual limit in Limits.
    - **Reading written into the register** (28 October 2026; decision sheet B4): the record above is accepted as (a); the residual limit stays in Limits.
12. **Wording of A0.** As run (`coldstart.json` `config.cycle2_flags`), A0 had `repair_judge_rejection_status` and `repair_dump_diagnostics` on. So A1 differs from A0 by the eight system repairs, not by ten switches.
    - (a) State the as-run switch sets: A0 is the evaluated system plus the two instrument repairs; A1 adds the eight system repairs (ten on); A2 adds the four contracts. This register does so (Sources and conventions; X.4).
    - (b) Keep the 'A0 + ten switches' shorthand.
    - Recommendation: (a). The amendment text is unchanged, and the register records what ran.
    - **Reading written into the register** (28 October 2026; decision sheet B5): (a).
13. **Implementation entries that the amendment's candidate-cause list does not name.** Step 3 lets the pilot add causes but not split or merge the listed ones. The entries:
    - (i) the alias-substring merge on the whole span, first key in name order (K2.6b; `registry_expansion_service.py:127-135`, `state_key_registry_service.py:57-64`);
    - (ii) `_KEY_SHAPE` (two or more segments) against the validator's 2–4 segments, which leaves proposals of five or more segments pending and their parked claims never released (K2.6c; 0–2 such proposals per run, each holding one parked claim);
    - (iii) AMI-specific deterministic constants in the value confirmation (`_STOPWORDS`, `runner.py:143-148`; the rule of a word of at least four characters; S.6) and in reading (`_FOCUS_STOPWORDS`, `answer_service.py:355-369`; R.6);
    - (iv) re-extraction of zero-claim spans at later meetings, with a larger registry (E.6);
    - (v) write-path resolver calls at meeting a against an empty registry (K2.6a).
    - (a) Record all five as entries now and map two of them: (i) to "a reuse or similarity threshold merged a new matter into an existing key" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:386`), and (iv) to "registry-conditioned extraction" (`thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:384`). Leave (ii), (iii) and (v) for the pilot to add as causes if cases rest on them.
    - (b) Record them as entries only, and let the pilot decide every mapping.
    - (c) Decide every mapping now.
    - Recommendation: (a). Recording them keeps them on the sheets' checklists, where they now stand under *Further implementation entries*, with the proposed mappings marked as proposed. Mapping (i) to the listed reuse cause avoids a new cause; (ii), (iii) and (v) have no clean listed cause. The implementation part's recommendation did not mention (v); leaving it to the pilot is the merge's addition.
    - **Reading written into the sheets** (28 October 2026; decision sheet C16): (a). Sheets E and K2 state the two mappings as made at signing; sheets K2, S and R mark (ii), (iii) and (v) as left to the pilot.
14. **Known limits of the held-constant controls.** `trace.json` does not keep the attempt envelope, so whether temperature 0.0 was actually sent is not recorded; the client drops temperature only after a 400 that names it (`openai_llm.py:208-210`). Also not recorded: the served snapshots of the judge, the embeddings and the RAG generator. RAG's served model is lost because `SharedReferenceGenerator` reads `last_call_metadata`, which `OpenAILLMClient` does not set.
    - (a) Record these as known limits (H does), and note that the attempt envelope (`openai_llm.py:296-332`) already holds `temperature_sent` and `actual_model`, so a later dated note could persist them without any behaviour change.
    - (b) Treat them as blocking for signing.
    - Recommendation: (a). The amendment's instrument list is fixed, and nothing in the nine runs shows a fallback or error (`fallback_count` 0, no error steps).
    - **Reading written into the register** (28 October 2026; decision sheet B6): (a).
15. **Criterion (ii) and retrospective entries** (raised at the merge). Criterion (ii) lets an alternative count where `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md:325`: "(ii) the prompt omits information the register gives that step, or contradicts the register". For some steps the only text that says what the step should receive is retrospective: A2's support check (the contract's wording, S-R9) and the rendering contract (D11, R-R1).
    - (a) Criterion (ii) compares the prompt with every entry the register gives the step, retrospective entries included. The alternative must still be consistent with the 94c049d text (amendment line 348).
    - (b) Criterion (ii) compares the prompt only with 94c049d entries.
    - Recommendation: (a). Line 347 bars a retrospective entry from grounding architectural weakness or a trade-off and from ruling out an alternative. It does not bar it from showing that a contract's prompt omits what the contract was built to check. The A2 contracts are judged on their implementation, so such an omission should count as possible implementation. Under (a), the meeting that the support-check prompt does not show (sheet S) is a checklist item; under (b), it is not.
    - **Reading written into the sheets** (28 October 2026; decision sheet C14): (a). Sheet S states it.
16. **The expansion generator and D4.p3's matching** (raised at the merge). The generator is told to prefer an existing key (K2.6b, `expansion_generator.py:326-328`), but it sees only key names, domains and families, not the descriptions, aliases or values that D4.p3 names as matching inputs. Decision 1 asks the same question for the extractor's hint.
    - (a) D4.p3's matching inputs apply to the generator's choice of an existing key too, so criterion (ii) can apply to expansion-routed misfilings where the generator named an existing key.
    - (b) They do not. The generator proposes a definition, D4.p3: "An expansion contains a candidate definition and its triggering evidence." Expansion-routed misfilings are then coded only under criterion (iii) or the harness-reviewer entry, as amendment line 251 says.
    - Recommendation: (b). Line 251 names criterion (iii) and the harness-reviewer entry as the routes for expansion-routed misfilings, and a generator merge reaches the registry only through the harness reviewer's acceptance. The generator's inputs stay on sheet K2 as an implementation entry, so a page can still note them.
    - Note added at review: the word values above is D4.p3's; which values it means is decision 17. The generator sees neither canonical nor held values.
    - **Reading written into the sheets** (28 October 2026; decision sheet A3): (b). Sheet K2 states it.
17. **What D4.p3's values means** (raised at review, 27 October). D4.p3: "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." Sheets K1 and K2 had read values as the values a key holds, without raising it as a reading.
    - (a) The concept definition's values (canonical values).
    - (b) The values a key holds (the current facts filed under it).
    - (c) Both.
    - Evidence for the readings:
      - The 94c049d matcher that D4.p3 describes scored definition fields. Its embedding profile joins key name, label, description, domain, aliases, example questions and canonical values (`94c049d:app/services/state_key_resolution_service.py:651-661`). Its rule scorer adds a canonical-value score (same file at 94c049d, line 753).
      - Where Chapter 4 means held values, it says observed values. D8.p3: "Concept descriptions, aliases, examples, and observed values associate a question with generated concepts."
    - Consequences. The resolver prompt and the hint prompt show neither canonical nor held values, so the prompt-side omission holds under every reading. The reading changes two things:
      - whether the omitted input is empty in these runs. Under (a) it is: no key in the nine runs has canonical values, because the harness clears them on accept (K2.6c; `registry_expansion_eval.py:446`). Under (b) or (c) it is not;
      - which implementation entry a page names. Under (a), the harness clearing (K2.6c); the input would also reach the embedding profile, empty here (K2.6a). Under (b) or (c), the prompts' line formats (K2.6a; E.6); claim routing never sees held values (the context digest is off), and question routing sees them only through the value-match widening (R.6).
    - Until you decide, sheets K1 and K2 state both readings. The K1.6 and K2.6a Not shown glosses stay as implementation notes.
    - Recommendation: (a). The 94c049d matcher scored the definition's canonical values, and D8.p3 uses a distinct term, observed values, for held values.
    - **Reading written into the sheets** (28 October 2026; decision sheet C13): (a). K1.3, K2.6a and sheets K1 and K2 state it; the readings (b) and (c) were removed from the sheets.

---

## Annex: other 94c049d Chapter 4 text that bears on components

The amendment's design entries are the Chapter 4 decisions as worded at 94c049d (amendment line 102). The passages below are 94c049d text outside D1–D9. They are not in the register above. None enters: they are context only and cannot ground a design code (amendment line 102).

- Section introduction (all components) `94c049d:thesis/implementation_chapter.tex:137-141`: "An alternative belongs to the design space unless Section~\ref{sec:design-evolution} supplies evidence that it was implemented or tested."
- Architecture (K2) `94c049d:thesis/implementation_chapter.tex:755-758`: "However, cold-start expansion is not an automatic branch of the generic ingestion graph. The evaluated orchestrator explicitly locates unassigned claims, invokes expansion and review, and releases claims for resolution."
- Domain records (E) `94c049d:thesis/implementation_chapter.tex:765-767`: "Decisions, action items, risks, and open questions can also be extracted as specialised interpretations, but their existence does not create a current fact."
- Domain records table (E) `94c049d:thesis/implementation_chapter.tex:787`: "Claim / interpretation & Value, relation, polarity, modality, confidence, source context & Accepted extraction label is not accepted state \\"
- Public question interface (R) `94c049d:thesis/implementation_chapter.tex:806-808`: "Payload construction precedes optional model-assisted grounding, which may revise prose and confidence while retaining structured state fields."
- Operational limits (K1) `94c049d:thesis/implementation_chapter.tex:834-835`: "Typed responses, structural validation, and constrained choices limit malformed model outputs and invented registry identifiers."
- Operational limits (S) `94c049d:thesis/implementation_chapter.tex:851-853`: "They do not establish global idempotency: proposal reuse spans terminal statuses, and lower-level application accepts an already accepted proposal."
- Requirements table, DR4 row (R) `94c049d:thesis/implementation_chapter.tex:955`: "D3, D8: unconfirmed state, unknown, focus filtering"

Further post-9-September locations with design readings, not quoted here: `thesis/notes/thesis_completion/artifacts/19-one-week-plan.md` (lines 195–197, a precursor of the principles table) and the disproof review's Chapter 4 reports (`thesis/notes/thesis_completion/artifacts/22-disproof/ch4/`).

---

## Limits of this register

**From the design part:**
- The design-text file has 51 D-paragraph ids plus T.rationale: 52 ids in all. Every one is assigned (Coverage).
- c6fbdc0 was committed on 19 October under the message baseline. Its wording may have been written at any time between 15 September (50cf0f3) and 19 October; it is dated only to the commit.
- The search for post-9-September design text covered the chapter's history, plans 21 and 23, `21-phase-0-prep.md`, `cycle2_flags.py`, `conclusion.tex`, the bug list and the argument map. `19-one-week-plan.md` and the disproof review's Chapter 4 reports are listed by location only (Annex). `21-build-report.md` and the pre-declaration-R files were not examined for design text.
- The table of where a loss surfaces maps surfaced-at only. It does not decide caused-at.
- The working-tree versions of plan 23 and `22-bug-list.md` have uncommitted edits. Quotes cite the committed versions (b4d6b6c and 3320375; the bug list is identical at both). The amendment, which is untracked, is cited at its working-tree line numbers of 27 October; they shift if the file is edited before signing.
- The RAG runs were not examined for design entries. RAG enters only the held-constant controls (H).

**From the implementation part:**
- The `registry_expansion_generation` messages are not recorded in `trace.json`. That prompt's text and hash come from the code at 3320375 only.
- The judge's inputs and served snapshot are not recorded; only its verdicts are, in `coldstart.json`. The judge prompt and its hash come from code.
- The RAG runs keep no `trace.json`. The RAG prompt hash is code-derived, and the RAG served snapshot is recorded nowhere.
- No artifact records whether temperature was sent on each call (a known limit, decision sheet B6).
- The PM runs keep no embedding vectors (no cassette). The RAG runs read vectors cached in September and made no embedding call (H, Embeddings). The served embedding snapshot is recorded for neither. The embedding model id is confirmed through the `usage.json` price ledgers, the RAG config block and the RAG cache's model_id.
- The numeric thresholds are given at their 3320375 defaults and are not recorded in run artifacts. `.env` (checked by variable name by the main session on 27 October), the runner and the lane scripts set none of them. The process environment at run time is not recorded, and it would take precedence over `.env`; this weighs more for a1_r1, which has no lane script (decision sheet B4).
- The A1 smoke run (a1_r1) has no lane script. Its command line is inferred from its coldstart config block and the A1 smoke note.
- The registry-line formats are quoted from code. `23-am1-prompts.py` hashes only the templates (⟦registry⟧), not the per-key line format.
- `23-am1-prompts.py` assigns read versus write path by exact match of the text with a checkpoint question, and a meeting by the next checkpoint question in the trace. Both rules are stated in its output.
- The items marked *Not shown* are glosses. No probe has tested them.
- a2_r2, which failed with a 503 at question time, is not covered; a2_r2b is used, as in the run manifest.
- The implementation part does not map its entries to the design text. The merge links them only through the register sheets.

**From the merge:**
- The criterion (ii) comparisons on the register sheets set the design inputs beside the prompt fields that the two parts recorded. They are glosses made at the merge. Neither part compared them, and no probe has tested them.
- Some implementation entries cite lines as `l.N`, relative to the file under discussion (Sources and conventions). Where the merge moved an entry, its file is named. Elsewhere the reader takes the file from the entry, as in the implementation part.

---

## Checks

**Package checker** (current; re-run on 28 October 2026, after the pre-tag edits; record at the end):
- Script: `23-am1-check-register.py`, SHA-256 794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9. It is in the package, untracked until the amendment is tagged. It reads only git objects (`git show`) and files; it makes no model, network or app call. Its docstring states the rules.
- Run with `python3 -I -B` on this file after the pre-tag edits of 28 October 2026. Result:
  - 52 design paragraphs, each compared with `git show 94c049d`;
  - design 360, commit 142, worktree 70, code-file 51, code-block 8, coderef 115, skipped 20 (on 27 October: design 157, worktree 66; the rise is the sentence lists of the sheets and the quotes of line 340 and line 251);
  - 0 errors; exit status 0;
  - 2 direction notes, at lines 852 and 857 (851 and 856 before the follow-ups of 28 October 2026, which added one line to S.4). Both are disclosed: S-R6's after-passage begins with a sentence that 94c049d also has, and S-R7's phrase also occurs in the 94c049d requirements table (DR6 row).
- The counts depend on this file's text. The SHA-256 of this file cannot be stated inside it; it is reported with the review result.
- The checks below are the build-time checks. Their scratch quote checker is superseded by this script.

**Design part** (as built, 27 October 2026):

- Every quoted string in the design part was compared, after joining whitespace, with its cited source: design quotes with the paragraph of the design-text file named on the bullet; other quotes with the cited lines (`git show` for commits, the working tree otherwise).
- Every code reference `name` (`3320375:path:line`) was checked: the name occurs on that line at 3320375.
- Script: `check_register.py` in the scratchpad `step0/work/` folder, with the normalised paragraph file `paras.json` built from the design-text file. Result on 27 October 2026: 148 design quotes, 146 other quotes and 115 code references checked, 0 errors. Not kept; superseded by `23-am1-check-register.py` (Package checker above).
- Every before/after pair was also checked in both directions: each before passage occurs at 94c049d and not at b4d6b6c, and each after passage occurs at b4d6b6c and not at 94c049d. Exceptions, as stated in the entries: the 9b96138 sentence (S-R4) exists only at 9b96138, and the phrase of S-R7 also occurs in the 94c049d requirements table (DR6 row), though not in the rationale table's D6 row.
- Run facts checked in all nine runs: 135 gatekeeper calls plus 4 summary records; every expansion-generation step carries a served model and `llm_assisted`; every concept review is by coldstart_harness; no canonical_match step; acceptance quality and value_policy structural in every `coldstart.json`; generator gpt-5.4-mini on every model step. Key cardinalities come from the nine state dumps.

**Implementation part** (as built, 27 October 2026):
- Every quote and code block was checked against the code at 3320375, the evaluated prompt texts or the traces. These were scratch checks and are not kept; a committed script is to re-derive them before the tag (decision sheet B3).
- `23-am1-prompts.py` was run twice, with the same output.

**Merge** (this file, 27 October 2026). Scripts in the session scratchpad, folder `step0/work/merge/` (not kept; decision sheet B3):
- `assemble.py` builds this file from the two parts. It copies their lines by range. The only edits inside copied lines are listed in the script: cross-references renumbered to this file's sections, the word sheet changed to section where it meant a component, and lines merged where both parts said the same thing. Each edit must match exactly once.
- `check_register.py` (the design part's checker) was run on this file: 150 design quotes, 213 other quotes and 115 code references. (Superseded: `23-am1-check-register.py` also resolves the implementation format; Package checker above.)
  - Every quote in design-part format, and every quote the merge added (amendment lines, two design quotes), passed.
  - 136 quotes failed only because their lines cite in the implementation part's format, which the checker cannot resolve. Each occurs verbatim in the implementation part.
- `verify_inherited.py` checked those quotes against the code at 3320375, `23-am1-prompts-evaluated.md`, the amendment and the loss-trace files. 126 were found verbatim, and 6 after joining Python string literals. The other 4 were checked by hand: the extraction prompt's polarity line (`23-am1-prompts-evaluated.md`), the WD source comment (`extraction_service.py`, 3320375), the bug-5 reason string (31 rows in the a1_r2 trace), and the implementation part's own label for its schema checks.
- `verify_merge.py` checked completeness. Every quote and every backtick span of the design part occurs in this file. Of the implementation part, all occur except two: a reference to the table Calls per run, now written without quotation marks, and the amendment's file name in that part's header. The lines of either part that do not occur verbatim (73 design, 91 implementation) were reviewed one by one. They are headings renamed for this file, cross-references renumbered, and lines merged with the other part.
- No fact in one part contradicts the other. Two differences of form were kept: the two styles of code reference (Sources and conventions), and counts given per run (design part) beside totals per arm (implementation part).

---

## Review record (27 October 2026)

**Workflow:** am1-step0-verify.
- Two reviewers read this file: register, design side; and register, implementation side.
- A skeptic tried to refute each finding. The findings below survived. Where the skeptic gave a better fix, the better fix was applied.
- Both reviewers numbered from F1, so the ids are prefixed here: D for the design side, I for the implementation side.
- Files changed: this file only. `23-am1-prompts.py` and `23-am1-prompts-evaluated.md` needed no change. The amendment was not changed.
- The fixer re-checked every finding against git objects (`git show` at 94c049d, 3320375 and b4d6b6c) and the run files before applying it. No model, embedding or network call was made, and `.env` was not opened; its modification date was read with `stat`.

**Design side:**
- D-F1 (major; example questions missing from the resolver and question-routing Not shown lists). Applied, with the better fix.
  - Example questions added to the Not shown lists of K2.6a, sheet K2 and sheet R.
  - Their two deterministic routes are stated: the embedding profile behind the shortlist, and the broad-list rule candidates (K2.6a; R.6).
  - Canonical values were not added to the Not shown lists. They are recorded as absent from the nine runs, and their status as a D4.p3 input is decision 17.
- D-F2 (major; D4.p3's values read as held values). Applied, with the better fix.
  - New decision 17, with options (a)–(c) and recommendation (a).
  - Sheets K1 and K2 now state both readings. The held-values comparison was not deleted. The K1.6 and K2.6a glosses stay as implementation notes. A note was added at decision 16.
- D-F3 (minor; three requirements stated more strongly than the 94c049d text). Applied.
  - K2-C7 moved to K2.4's disclosed limitations and off sheet K2's checklist; a note under decision 2 records the move.
  - R-C5 now uses D8.p3's permission (can return) and D3.p5's should.
  - A-C5 now quotes D2.p5, is marked for criterion (ii) and cause 4, and is off sheet E's class (1) checklist.
- D-F4 (minor; R.3 and R-C5 disagreed on the focus gate). Applied. R.3 states that D8.p3 specifies the gate's outcome (cost in D8.p4) and that its relevance test is implementation. Sheet R's cause 2 points to D8.p3 and D8.p4.
- D-F6 (minor; D9.p4 not cited on whether the current value's claims compete). Applied. D9.p4 is quoted in the D5.p3 gloss and reconciled in S.3. It is added to decision 4 without changing the recommendation. Plan 23 at b4d6b6c, line 118, is added to S-R10, and the bug list at 3320375, line 170, to S-R11.
- D-F7 (minor; D10 and D11 quoted only in part). Applied. D10 and D11 are quoted in full in E-R1 and R-R1, except their label lines. D10's cost sentence is added to K1-R1, K2-R4 and S-R3.
- D-F8 (minor; Checks cited a scratch checker). Applied, with the better fix. The companion-files table and Checks cite `23-am1-check-register.py` with its SHA-256 and this run's counts, as untracked until the amendment is tagged. Only the quote-checker part of decision 10 is marked resolved.
- D-F9 (minor; decision 11 asked for a check already made). Applied, with the better fix, together with I-F3. The check is recorded under decision 11, and the choice among (a)–(c) is left to you. The parameter cells keep not recorded and add not set in `.env`, the runner or the lane scripts. Limits is updated.
- D-F10 (nit; retrospective lists and dates). Applied, with the better fix. Sheets E, K1, K2, S and R list the binding X-R entries. K2-R3 is dated c6fbdc0 and 5de9911. A-R1 says one passage.

**Implementation side:**
- I-F1 (major; example questions, and the reading of values). Applied together with D-F1 and D-F2, with the better fix: decision 17 states that the prompt-side omission holds under every reading, and what the reading changes.
  - Not applied: the proposed sheet line saying that an omitted input meets criterion (ii) and rules out design or model, not separated. Reason: it would turn a gloss into a class rule that the case page must decide. The sheets' rules section already quotes amendment lines 325 and 331 verbatim.
- I-F2 (minor; value identity in the engine). Applied, with the better fix. S.6 Rules and sheet S state that the engine compares the exact raw string for keys with no canonical values, list the three lower-case sites, note the docstring mismatch, and state that A2's equivalence does not reach rule 3's tie test.
- I-F3 (minor; `.env` and the eight thresholds). Applied with D-F9, with the better fix: attributed to the main session, `llm_max_attempts` and the embedding model included, and the residual limit on the process environment kept.
- I-F4 (minor; four reading rules). Applied, with the better fix's corrected weights.
  - (a) The 0.25 ratio is inert on the LLM path, and broad questions append the supporting keys (R.6; sheet R; K2.6a).
  - (b) The focus key's label and alias words are removed from the focus terms (R.6; sheet R, cause 2).
  - (c) Keys whose names contain reject are read for rejection questions, only when `_REJECTION_Q_RE` matches (R.6; sheet R).
  - (d) The rule-scorer weights are in R.6 and in a parameter row.
- I-F5 (minor; embedding failure policy and RAG vectors). Applied, with the better fix. H gives the five silent fallback sites and the no-failure check. The fixer added the A2 and RAG lane ledger to that check (3494 calls, with the failed a2_r2 included). H and Limits state that RAG read the September cache with no misses and made no embedding call.
- I-F6 (minor; parked claims and accept-error counts). Applied as proposed. K2.1, the K2 checklist and sheet K2 state that a parked claim is never routed again. K2.6c, sheet K2 and decision 13 (ii) give the accept errors as review records from 0–2 proposals per run.
- I-F7 (nit; `EXPANSION_AUTO_ACCEPT` for a1_r1). Applied, with the optional addition that `.env` does not set it.
- I-F8 (nit; the `extraction_confidence` default). Applied, with the optional reason why a downgrade is not recorded.

**Checks after the fixes:** `23-am1-check-register.py`, 0 errors (Checks, Package checker).

**Cross-package consistency pass (27 October 2026).** One edit: the `answer_canonical_max_items` cell (R.6, Parameters) now carries the same default, not-recorded and not-set note as the other thresholds of decision 11. `23-am1-check-register.py` was re-run afterwards: the same counts as in Checks, 0 errors.

## Pre-tag record (28 October 2026)

The author asked that every decision take its recommendation. This file was changed for the pre-tag items of decision sheet C1 that fall on the register. Decision ids are those of `23-am1-decisions.md`. The amendment was not changed. No model, embedding or network call was made.

- **B22 (decision pointers).** Every pointer to this register's decisions 1–17 on the five sheets, and in the sections, requirements and implementation entries the sheets point to, now states the signed reading in place. The readings: C12 (a), C8 (a) with both Corrections, C11 (a), C10 (b), C15 (a), A1, A2, B1, B2, B3, B4, B5, C16 (a), B6, C14 (a), A3, C13 (a). Sheets K1 and K2 no longer state the (b) and (c) readings of what D4.p3's values means. The decision list stays as the record; each decision now carries the reading written into the sheets. Pointers remain only in the decision list, the Limits and Checks sections' history and the review record of 27 October.
- **C8 (a), with both Corrections.** Each sheet now lists the 94c049d sentences it allows as a design ground one by one, each under its tag: (C) for architectural weakness, (B) for a trade-off. The list holds every (C) or (B) sentence of the paragraphs the sheet listed before, and no other sentence. L sentences are out: D2.p4's window sentences on sheet E, D6.p4's edited-proposal sentence and D7.p5's non-atomic sentences on sheet S. Each sheet states that an L sentence, a sentence on R-4's list and D4.p4's equivalence sentence cannot ground either code, and gives Correction 1's coding rule. The disclosed-limitation lines were split: sentences tagged (B) or (C) (D2.p2, D1.p3 and D1.p4 on sheet E; D4.p4's parking sentence, D4.p5, D1.p4 and D6.p4 on sheet K2; D8.p4 and D8.p6 on sheet R) are quotable and no longer listed as limitations. Research for the tags:
  - D3.p3's sentence on negating the current value keeps (C) and stays the requirement behind S-C4. It is on R-4's list: R-4 cites the chapter's lines 248–250 at b4d6b6c for bug 1, and of the two sentences on those lines only this one describes the current-value branch that bug 1 concerns. So no sheet lists it as quotable, and sheet E's D3.p3 list stops before it.
  - D5.p6's first sentence was tagged (B). It states that D5.p5's limitations qualify the requirements, which is a shortfall, so it is now (L).
  - D7.p5's first sentence was (B) in S.2 and (C) in R.2. It states a benefit of supersession and a commitment on reading (R-C7), so it carries both tags in both sections. Sheet S lists it under (B), sheet R under (C), as before.
- **C17 (a).** D4's scalar-concept passage (amendment line 355) is D4.p5. Its scalar sentence is now (C) in E.2, as in K2.2 and R.2. Reason: line 355 says an architectural code may be argued from this passage, and architectural weakness needs a commitment; the sentence states what the generator does by default, which is a commitment by this register's tags. Sheet E quotes D4.p5 whole for WD cases, with its sentence tags (B for the first three sentences, C for the last two), since WD cases keep D4.p5 whole.
- **C62 (b), with its second item (i).** Sheet K2 names candidate generation (LLM) beside the resolver: the condition of line 340 and the class design or model, not separated apply at both. Sheet E states that the condition and the class apply at the gatekeeper only for `admitted:ignored` cases (line 331). Sheet K1 quotes line 340 itself, so the extract no longer points to the rules block above the sheets; sheets E, K2, S and R point to that quote on sheet K1.
- **Other.** Sheet K2's expansion-generator block now cites amendment line 251 as a governed quote. The Coverage table notes the tag changes. `23-am1-check-register.py` was re-run: 0 errors, counts as in Checks.
- **Follow-ups (28 October 2026).** S.4's list of disclosed limitations now includes D5.p6's first sentence, retagged (L) above; sheet S already said it is listed there. Sheet K2's expansion-generator line cites amendment line 251 once, as the governing source of its quote, instead of naming the line and then citing it. Four run observations stay here as record and are cut from the pre-coder extract by its builder, `23-am1-precoder-extract.py` (decision sheet A19; amendment line 402): the two statements that the expansion generator's fallback did not occur in these runs (sheet K2's further entries; K2.6b), the frequency clause on write-path intents (K2.6a) and the a2_r2b run example (S.6). Decision 10 now records the merge's completeness check as closed: a one-time historical check, its result in Checks. `23-am1-check-register.py` was re-run: 0 errors, the same counts; the two direction notes moved down one line (Checks).
