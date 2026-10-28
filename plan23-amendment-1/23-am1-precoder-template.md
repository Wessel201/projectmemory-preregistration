# Plan 23, amendment 1: the model pre-coder's prompt template

Dated 27 October 2026. Part of the Step 0 package of `23-plan-amendment-1-ceilings-and-root-cause.md` (the amendment). **Status: draft for signing** with the amendment. It is fixed at signing. Afterwards, changes go in a dated note (amendment line 16).

**What this file fixes:**
- Step 0: `- **The model pre-coder's prompt template,** fixed and dated.` (amendment line 118).
- Step 3, order of work, item 3: `3. The model pre-codes every case from the page only, in a fresh context with no repository memory or result reports. It uses the template fixed at signing, and the frozen sub-cause list is its only added input.` (amendment line 402).

**Contents:**
1. Inputs and assembly
2. The prompt (fixed text)
3. Where each part of the prompt comes from
4. The output and the agreement measures
5. Run conditions
6. Leak check of the blind case page
7. Open points (decisions for the author)
8. Review record (27 October 2026)

**Conventions.** Citations are `path:line`; amendment lines refer to the file as of 28 October 2026 (draft 6; every line keeps its number). Lines of `22-bug-list.md`, which has uncommitted edits, are working-tree lines of the same day. Text in code spans or marked "verbatim" is copied exactly. Text marked "gloss" is this file's own wording.

## 1. Inputs and assembly

- **The prompt** is the text of the fenced block in Section 2: the lines between the line `~~~~ prompt` and the next line `~~~~`, both excluded, each line ending in a newline.
  - SHA-256 of that text, before substitution: `8b4422c9b6ee1979a2f3dc369cbea7986440029fa75b5c5c573c7b4facdfd3a9` (61,451 characters, recomputed 28 October 2026 in the pre-tag pass, after decision sheet C8 (a) Correction 2, C62 (b), B18 and B21 (Part G's sentence on the extract's item ids); previous `fd7e2f6b…` (60,369 characters), recomputed 27 October 2026, late evening, after Part B's gloss of "V4" was made true for a machine V4, which reads this prompt; `5345f42e…` (60,362 characters), after the second review; `52faa1a7…` (60,033 characters), after the review of the completion pass; `f54c1292…`, after the completion pass; `65d423b0…`, after the review fixes; the first draft's hash was `ee185603…`). Recompute and record it again at signing if any edit is made before then. The hash of the text with the extract filled in is recorded below; recompute it at signing if anything changes.
  - The output schema is inside the prompt, between the lines `BEGIN OUTPUT SCHEMA` and `END OUTPUT SCHEMA`. The validator uses that text, so there is one schema. SHA-256 of the schema text (the lines between those two lines, each ending in a newline): `0c05d09cf63101f59bbf2ba8ec681bff40876472273aee0ef7fa9e46cfec3ddf` (recomputed 28 October 2026 in the pre-tag pass, after C62 (b) and B18; previous `e790d1a6…`, recomputed 27 October 2026 after the review of the completion pass and unchanged after the second review; `0f6d1bb5…`, after the completion pass; `c32025b5…`, after the review fixes; the first draft's was `931fb563…`).
  - The schema was tested on 79 sample records (valid and invalid) with a small local checker, after the review of the completion pass, and again after the second review; every record validated or failed as intended. In the pre-tag pass (28 October 2026) the test grew to 95 records and 11 check-9 records, with "candidate generation" and "not applicable"; all were as intended, and `23-am1-v4.py`'s own schema checker gave the same result on all 106. The checker is a working file, not part of this package.
  - **The extract and the filled prompt** (recorded 28 October 2026, pre-tag pass; decision sheet B21; rebuilt the same day in the pre-tag follow-ups):
    - the extract, `23-am1-precoder-extract.md`: SHA-256 `09036929cd59dc0eb37ba14c3f3f068c9825177a0ee0b0210a95ce51399b4d78` (230,537 characters, 1,940 lines); previous, before the follow-ups, `744b7398…` (231,036 characters);
    - built from the register, `23-am1-register-design-and-controls.md`, SHA-256 `9c7af4e0f7a96103ecc0fb423236a64e21559bad7a6f1b2c2f44cb28a3a8e0da`, and the design-text file, `23-am1-design-text-94c049d.md`, SHA-256 `b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759`. `23-am1-precoder-extract.py` rebuilds it from those two files; with `--check` it rebuilds into a temporary file and compares the bytes with the committed extract;
    - the filled prompt: the prompt text above with `{REGISTER_SHEET}` replaced, by literal replacement, with the whole content of the extract file (its final newline included). SHA-256 `bae517630fe414f893ed4caeeb00f09645e7c6b7ce49d8de3ccb856a59c23154` (291,972 characters); previous, before the follow-ups, `b570fe0c…` (292,471 characters). This is the template fixed at signing that amendment line 402 names, and the T of `23-am1-v4.py case-packets --template T` (Section 9). It is not kept as a separate file: it is made from this file and the extract, and checked against this hash.
    - Recompute all four hashes if this file's prompt or the extract changes before signing.
- **Three placeholders,** each occurring exactly once in the prompt: `{REGISTER_SHEET}`, `{SUBCAUSES}`, `{CASE_PAGE}`.
  - They are replaced by literal string replacement, once each. Not by a formatting function: the schema contains braces.
  - `{REGISTER_SHEET}` is filled **once, at signing,** with the pre-coder extract (below). The filled text is part of the template fixed at signing, and the template's hash covers it. It is not a run-time input. Amendment line 402: "It uses the template fixed at signing, and the frozen sub-cause list is its only added input." The SHA-256 of the extract and of the filled prompt text are recorded above. Decision sheet B21 adopts this form (Section 7, point 16).
  - `{SUBCAUSES}`: the frozen sub-cause list (order of work, item 2, amendment line 401), unchanged, as committed with its hash. It is a Markdown table whose names are in a column headed "Name" (or "Sub-cause"). `23-am1-v4.py case-packets` reads the names from that column, records them in its manifest and refuses a list where it finds none; the shared validator's check 7 uses the same names (Section 9, AG5).
  - `{CASE_PAGE}`: one Step 3 case page, unchanged. That is the blind page (`--case-pages`) plus the items the amendment lists (amendment lines 390-397), plus the arm and series (Section 7, point 3).
  - The page keeps its own register checklist for one boundary (amendment line 397), for the author. The prompt tells the model that the five sheets of the extract govern (prompt Part A4).
- **The pre-coder extract** (`23-am1-precoder-extract.md`). It is built from the signed design-and-controls register after the register's decisions are signed, and then hashed. Points 16 to 18 of Section 7 are the decisions behind it (decision sheet B21, B22, A19).
  - It contains:
    - the five register sheets: extraction (E), key assignment at extraction (K1), key resolution and expansion (K2), state rules (S), reading (R), each with its list of the 94c049d sentences a page may quote, every sentence under its tag;
    - after each sheet, the verbatim text of every 94c049d paragraph the sheet names, under its paragraph id, copied from `23-am1-design-text-94c049d.md`, sentence by sentence, each sentence with its tag on that sheet (decision sheet C8 (a), Correction 2): (C) or (B) where the sheet lists it under that tag, (L) where the register tags it a disclosed limitation, (—) otherwise; on sheet E, D4.p5's sentences are (WD, B) or (WD, C), since sheet E lists D4.p5 only for WD cases. Line breaks inside a sentence are joined with one space, as the register quotes them;
    - after each sheet, the text of every conformance requirement the sheet names by id (for example E-C1 to E-C5), and of every implementation entry it points to (for example E.6), copied from the register;
    - an item id on every checklist item, one item per line: each listed candidate cause (`E-cause-1`, `E-cause-2`, ...), each further implementation entry (`E-entry-1`, ...; on sheet S, the entries under A2's contracts are further entries), and each conformance requirement under its register id (for example `E-C1`).
  - It does not contain:
    - a pointer to the register's decisions. Each "decision N" reference is replaced by the signed reading. On the sheets as built on 27 October, the pointers were to decisions 1, 2, 3, 4, 5, 6, 13, 15, 16 and 17. Done: the register's pre-tag edit (28 October 2026, B22) wrote the signed readings into the sheets and the entries they point to, so the extract carries the sheets' text unchanged in this respect;
    - run counts, incidence figures, or any item of the amendment's "Already read" list (amendment lines 33-63). Parameter values stay: they are implementation entries (amendment line 107);
    - quotes of the probe mapping (amendment lines 271-281).
  - It is checked once, at signing: Section 5, blindness check 7. Result of 28 October 2026 in Section 5.
  - **How it was built** (28 October 2026). `23-am1-precoder-extract.py` (committed in the pre-tag follow-ups, ported from the pre-tag pass's working file `build_extract.py` in the session scratchpad) reads the register and the design-text file and writes the extract. Every edit it makes to register text is an exact replacement that must apply once. Where Section 1 left something to judgement, the build read it as follows:
    - Item ids are written `- [ID] text`, so that the item's text is the rest of its line. On sheet S the three bullets under A2's contracts that name a step (support check, type check, same-meeting rules) are further entries S-entry-9 to S-entry-11; the first two bullets there are rules, not entries. A-C5 is named on sheet E but is not a checklist item there, and the extract says so.
    - "Every implementation entry it points to": the register's implementation section (A.6, E.6, K1.6, K2.6, S.6, R.6 or X.4) for every pointer on the sheet, repeated after each sheet that points to it, as "after each sheet" reads. Where a sheet names only a part of K2.6 (sheet K1: K2.6c; sheet R: K2.6a and its Parameters), only that part is carried. Pointers to design or step-type sections (for example E.3, K2.1) are not implementation entries and are not carried; the extract's opening says so.
    - Paragraphs: every paragraph id on the sheet, including those named only in its disclosed-limitation line. The conformance requirements are those of the sheet's conformance line; for sheet S also S.4's list of disclosed limitations, which the sheet says holds them.
    - Removed: every run count and incidence figure (for example the registry sizes per meeting, calls per run, the review records per run, "313 of 534"), the quotes of amendment lines 272, 273, 276, 277, 278 and 279, and the statement that the harness reviewer rejected no proposal in any run, which prompt Part A1 also leaves out (completion pass, X12). In the follow-ups (28 October 2026) also: the two statements that the expansion generator's fallback did not occur in these runs (sheet K2's further entries; K2.6b), the frequency clause on write-path intents (K2.6a) and the a2_r2b run example (S.6); the register keeps them as record, and the code-level statements around them stay. "The nine runs" reads "these runs". Parameter values stay.
    - Sheet S's two mentions of the claims register's R-4 list, which is not an input, now say that the sentence is a disclosed limitation here; the listed sentences were already without it.
    - The amendment's path in citations reads "amendment line N"; the extract's opening says that this is the study plan of Parts B and D.
    - The extract carries no date or build record, so that no such numeral enters the prompt. Its provenance is this section.
- **Nothing else is added at run time:** no system prompt text, no examples, no earlier outputs, no comments, no repository content. The run-time inputs are the sub-cause list and the case page.
- What the inputs must not contain: Section 6.4.

## 2. The prompt

~~~~ prompt
You are a coder in a root-cause study of information loss in a software system. You code one case. Work only from the material in this message: these instructions, the register sheets (Part H), a sub-cause list and one case page. You have no other information about the system, the study or its results. Do not use or guess any. Do not use tools. Return one JSON object and nothing else.

==================================================================
PART A. THE SYSTEM, THE CASE AND THE PAGE
==================================================================

A1. The system turns meeting transcripts into maintained project state. Its components, in order. The step names of A5 are in quotes. This is a summary; where it and the register sheets differ, the register sheets govern.
- Admission. "segmentation" cuts each transcript into spans. The "gatekeeper" (an LLM step) gives each span a policy. Spans with the policy extract_to_state, extract_as_candidate or evidence_only are admitted: "evidence creation" makes evidence of them, and they go to extraction. Other spans do not.
- Extraction. "extraction" (an LLM step) turns an admitted span into claims: subject, predicate, object value, polarity and modality. "claim persistence" stores them. In the same call, "the `state_key_hint` field of the extraction call" can name a state key from the registry shown in the extraction prompt.
- Key assignment at extraction. Where that hint names a registered key, "the hint becomes the claim's key": the claim is filed under that key.
- Key resolution and expansion. Other claims go to the "resolver" (an LLM step), which chooses a key from a shortlist of the registry. If it returns no key, registry expansion proposes a key definition: "alias merge", "candidate generation" (an LLM step), "semantic reuse" and "attach or new proposal". A reuse rule can map that proposal onto an existing key. The "harness reviewer" (in these runs, the evaluation harness's reviewer) accepts a proposed key, as a new key or as a merge into an existing one. It submits no reject: a proposal it would reject is only recorded. "review validation and release" validates an accepted key and releases the claims parked on it.
- State rules. Deterministic rules turn the claims filed under a key into proposals and stored facts with a status. In arm A2, four contracts act here as well; one of them, the "support check", is an LLM step.
- Reading. At question time, "question resolution" (an LLM step) chooses keys. Deterministic steps widen the keys ("widening"), pack the facts on them into a context ("context pack") and build the answer ("answer templates and gates"). "grounding" (an LLM step) can revise the answer. A judge scores the answer. The judge, the gold and the question suite belong to the evaluation, not to the system.

A2. Arms and series. The page states both.
- A0 is the evaluated system.
- A1 is A0 with the repairs of verified implementation bugs switched on. Part F lists them.
- A2 is A1 with four write contracts switched on. Their one-line specifications, as the code states them:
  - filing_type_check: "Before filing, check a claim's value against the key's declared value type and cardinality; park the claim on a mismatch."
  - resolution_same_meeting_conflict: "Rival asserted claims under a scalar key with equal authority from the same source artifact become a conflict instead of a confidence contest."
  - supersession_requires_new_evidence: "A challenger supersedes only with evidence that does not already support the current fact and comes from another meeting."
  - filing_support_check: "Before filing, check that the linked span establishes the claim's value, commitment status and time; park the claim otherwise."
- WD is the whole-decision extraction contract (extraction_whole_decisions): "One claim per asserted decision, with the full decision text as its value, filed once." It is not switched on in A0, A1 or A2.
- A1-ref and "final configuration" are later arms on the ES2009 series. They carry repairs and contracts admitted later; the page states which.
- The series is EL2020 or ES2009.

A3. The case. A case is one gold value in one run, at a step where the value is lost, taken at that step's earliest failing checkpoint. The page gives this step and its sub-code: the surfacing step. Checkpoints and phases are counted from 0; phase k holds the writes up to checkpoint k.

The steps, in order. The first step that fails is the loss.
- admitted: the value's cited span went to the extractor (extract_to_state, extract_as_candidate or evidence_only), or a claim from another span carries the value
- carried: a claim extracted by checkpoint k carries the value
- polarity: ... with the polarity the value needs (negative for an explicitly ruled-out value)
- modality: ... asserted (any modality for a candidate value)
- filed: such a claim's last logged evaluation by k filed it under a key (not parked, not refused)
- proposed: a proposal carrying the value was raised by k
- applied: a fact carrying the value was created by k
- current: that fact is current at k (rejected at k for a ruled-out value)
- status: ... with the expected status at k
- key_reached: a key the reader resolved holds such a fact
- in_payload: the reader was given that fact as an answer fact
- answered: the question is scored correct
A value the gold marks superseded at a later checkpoint (a demoted value) passes when no fact holding it is current at k. Its loss is current, sub-code still_current.

The sub-codes, by step:
- admitted: `ignored` (the gatekeeper gave a cited span another policy); `span_not_seen` (no gatekeeper decision for any cited span, or the gold line maps to no span)
- carried: from the cited spans or the spans next to them: `extracted_after_checkpoint` (a carrier exists, extracted later), `sibling_value_only` (a claim matches strongly, but the text belongs to another gold row), `split_across_claims` (claims with one subject carry it only together); from the cited spans proper: `no_claims_from_cited_span`; otherwise `claims_without_the_value`
- polarity: `negated_value_read_as_rejection` (the gold value or an alias contains a negator, e.g. "not much better than before", and the value was extracted only as a negative claim); `carried_only_positive` / `carried_only_negative`
- modality: `carried_only_<modalities>`
- filed: most common of: `cycle2_parked_<reason>` (A2 checks, dated by the parking step); `undefined_key` (bug-5 repair; in A0 an undefined key, including the literal key `null`, is filed and flagged `bug5`); `no_key`; `not_evaluated`
- proposed: from the filed claims' last logged evaluation: `another_value_won` (it raised a proposal for another value); `own_value_not_matched` (it raised one for its own value, whose stored words alone do not match: the pair goes to adjudication); or by its reason: `tie_left_as_conflict`, `same_meeting_conflict` (A2: rival values or challengers in one meeting), `judged_same_as_current`, `outranked_dissent`, `current_value_ranks_higher` (bug-3 repair), `hedged_same_value` (bug-4 repair), `hedged_negation`, `no_positive_claim_left`; else the raw result type
- applied: `proposal_expired`, `proposal_pending_review` (the final status of the proposals that passed), `fact_not_found`
- current: `displaced_by_other_gold_value` (the fact that replaced it holds another current or candidate gold value of the checkpoint, adjudicated so or strong for it under the matcher and sibling rule; `displaced_by` names it); `overwritten_by_non_gold_value` (a later gold value further down the chain is recorded as `later_gold_in_chain`); `rejected`; `rejection_after_checkpoint`; demoted: `still_current`. `not_current` cannot occur under the replay
- status: `stored_as_<status>`
- key_reached: `other_keys_resolved`, `no_key_resolved`
- in_payload: `near_match_only` (only disclosed as a near match, when the answer was "unknown"); `key_resolved_fact_not_given`
- answered: `answer_or_judge`

A4. The page. It shows: the gold value, its kind, its expected status and its aliases; the cited span(s) with the gatekeeper's policy; the claims from the cited span(s) and the spans next to them, and claims from other spans that share words with the value, each with its evaluation trail (phase, key, result, reason) and any parking; the facts under those keys at the checkpoint, with their status; the single-value questions with the keys resolved, the facts given, the answer and its score; the surfacing step and sub-code; the key history; the path of every carrier and rival; the registry size; the value's outcome in every other run of the system, labelled by arm group: per run, the step, sub-code and checkpoint of its first loss, and whether it passed this case's step at this case's checkpoint; RAG's outcome on the value, per RAG run, with whether a credited answer cited a chunk containing a gold line; and the register checklist for one boundary. The five register sheets in Part H govern: take every checklist from them (E5), not from the page. RAG is a retrieval baseline that answers from transcript chunks. If the page has a form headed "Coder's verdict", ignore it.

Terms. A carrier is a claim that carries the gold value. A rival is a claim of another value under the same key. A claim's path is how it reached its key: the hint ("the `state_key_hint` field of the extraction call"), the "resolver", or expansion.

A5. The steps within each boundary. Use these names for caused_at_step, exactly. They are the register's step names. Each is marked LLM or deterministic, as the register gives the step types.
- extraction: "segmentation" (deterministic); "gatekeeper" (LLM); "evidence creation" (deterministic); "extraction" (LLM: the extraction call, apart from its hint field); "claim persistence" (deterministic).
- key assignment at extraction: "the `state_key_hint` field of the extraction call" (LLM); "the hint becomes the claim's key" (deterministic).
- key resolution and expansion: "resolver" (LLM); "alias merge" (deterministic); "candidate generation" (LLM); "semantic reuse" (deterministic); "attach or new proposal" (deterministic); "harness reviewer" (deterministic); "review validation and release" (deterministic).
- state rules: "conflict evaluation and the resolution engine", "proposals" (deterministic); "settle" (deterministic, not in A0: it is the bug-13 repair of Part F); "confirmation", "projection" (deterministic); "type check" (deterministic, A2, and the final configuration where the page states that filing_type_check was admitted); "same-meeting conflict and new-evidence rules" (deterministic, A2, and the final configuration where the page states that resolution_same_meeting_conflict or supersession_requires_new_evidence was admitted); "support check" (LLM, A2, and the final configuration where the page states that filing_support_check was admitted).
- reading: "question resolution" (LLM); "widening", "context pack", "answer templates and gates" (deterministic); "grounding" (LLM).
The rule for an LLM step with no model condition applies step by step, not to a whole boundary. Part B defines "Design or model, not separated" by "the caused-at boundary is an LLM step with no model condition (routing, reading, A2's support check, the gatekeeper for `admitted:ignored` cases)". Part D, Burden, last bullet, gives the rule: "At an LLM step with no model condition", "architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value." The register sheets name the steps where it applies, and the rule and the class "design or model, not separated" apply only at these seven: the "gatekeeper" (for `admitted:ignored` cases), "the `state_key_hint` field of the extraction call", the "resolver", "candidate generation", the "support check", "question resolution" and "grounding". They never apply at a deterministic step, or at "extraction", which has a model condition (probe (i)(d)).

==================================================================
PART B. THE EIGHT LABELS
==================================================================

Use exactly one of these strings for "class":
  "implementation defect"
  "architectural weakness"
  "design trade-off"
  "conversational difficulty"
  "evaluation defect"
  "model-limited (held constant)"
  "design or model, not separated"
  "unclear"

Their definitions, verbatim from the study plan:

| Class | Definition |
|---|---|
| Implementation defect | **(1) Conformance:** the code contradicts the register. **(2) Implementation choice:** the loss rests on an *implementation* entry, and an alternative counts. An alternative counts when any of these holds: (i) a Step 2b probe recovers the case under the mapping; (ii) the prompt omits information the register gives that step, or contradicts the register; (iii) the trace shows a parameter excluded the right item, or admitted a wrong one (e.g. an expansion-reuse or similarity threshold filing a different matter under the key); (iv) for `carried:claims_without_the_value`, the WD rule below. Wording quality without (i)–(iv) does not count. |
| Architectural weakness | the loss follows from a design decision **as worded at 94c049d**, quoted on the case page |
| Design trade-off | the loss is the cost of a deliberate choice whose benefit the 94c049d text states. Where the loss trace can measure the benefit, it is measured |
| Conversational difficulty | the transcript makes the value hard to recover |
| Evaluation defect | the gold, the suite, an adjudication or the judge is wrong |
| Model-limited (held constant) | only under the probe mapping. Bounded to gpt-5.4-mini |
| Design or model, not separated | the caused-at boundary is an LLM step with no model condition (routing, reading, A2's support check, the gatekeeper for `admitted:ignored` cases). Implementation was considered and rejected; the step lacked no input the register gives it; no parameter excluded the right item or admitted a wrong one; every available in-design probe was not recovered; and the transcript is not difficult. Reported with its count, bounded to gpt-5.4-mini. Never cited as a design limit or as model-limited |

Terms in these definitions and in Part D:
- "The register" is the design-and-controls register. The register sheets in Part H are its five per-boundary sheets. Each sheet names its design entries by paragraph id (for example D4.p3): the design text of the system's design chapter as worded at commit 94c049d (9 September 2026). Each sheet lists the 94c049d sentences a page may quote, each under its tag: (C), a commitment, for architectural weakness; (B), a stated benefit or cost, for a design trade-off. The text of every paragraph a sheet names follows the sheet, verbatim, sentence by sentence, each sentence with its tag on that sheet. Entries written later are marked retrospective. Its implementation entries are the prompts, parameters and deterministic logic. Its held-constant controls are the generator model, the embedding model and the judge.
- "Step 2b" is a set of probes: single model calls that re-run one step of one case under a changed condition. "The mapping" turns a probe result into a code. Part C lists them.
- "Step 2c" is the WD runs. "The WD rule" is in Part D.
- "The reveal" is the moment the sealed outputs (Part C) are opened, after all blind codes are committed.
- "V4" is the second coder; "pass 1" is the author's blind code. You see the codes of neither.
- "Step 4(b)" is a later repair round; it does not affect your code.

==================================================================
PART C. SEALED OUTPUTS, PENDING ALTERNATIVES AND THE CONDITIONAL CODE
==================================================================

C1. Some alternatives are decided by outputs that are sealed from every coder until the blind codes are committed. You will never see them. Use these output ids exactly:

- "probe (i)(b)": the cited span re-extracted with the recorded prompt, its registry cut to the resolver's embedding candidates for the span text. Can set criterion (i) at extraction: registry-conditioned extraction.
- "probe (i)(b2)": as (b), with neutral examples in place of the prompt's AMI role examples. Can set criterion (i) at extraction: out-of-domain prompt examples.
- "probe (i)(c)": the recorded prompt with an empty registry. If (c) recovers and (b) and (b2) do not: caused at extraction, registry-conditioned extraction, class unclear.
- "probe (i)(d)": a larger model (gpt-5.4) with the recorded prompt, only on cases (b) and (b2) do not recover. Model-limited only if (d) recovers and (b), (b2) and (c) do not.
- "probe (ii) offline check": whether the gold-holding key, or a fitting one, was in the recorded resolver prompt (for a hint-routed claim, in the registry of that meeting's extraction prompt). Can set the sub-cause "the shortlist or prune excluded a fitting key".
- "probe (ii-r)": resolver-routed misfiled carriers and rivals re-resolved with the unpruned registry of that moment. Can set criterion (i) at key resolution and expansion.
- "probe (ii-h)": the spans of hint-routed misfiled carriers and rivals re-extracted with the registry cut as in (b). Can set criterion (i) at key assignment at extraction: registry-conditioned hinting.
- "probe (ii) joint condition": (ii-r) and (ii-h) together, for a case with misfiled claims on both paths. If it recovers: routing, path unclear (possible implementation at both).
- "offline reading check": whether the holding key was in the recorded question-routing prompt, and its rank. It decides whether the question-time shortlist alternative applies: where the key was in the prompt, it is ruled out.
- "probe (iii)": the question re-resolved with the unpruned registry. Can set criterion (i) at reading: the question-time shortlist excluded the holding key.
- "oracle row result": the run's state rebuilt, offline, with routing made perfect (R); with R plus one injected correct claim for a value lost at extraction (E+R); and with E+R plus the removal of negative carriers of current values (E+R*). Sets caused-at only (Part D, Caused-at).
- "A2 leave-one-out: filing_type_check", "A2 leave-one-out: resolution_same_meeting_conflict", "A2 leave-one-out: supersession_requires_new_evidence", "A2 leave-one-out: filing_support_check": the A2 run's state rebuilt with that one contract switched off. Sets caused-at only: if it recovers the row, caused-at is the state rules (that contract).
- "WD result": three runs with WD against three fresh A1 runs. Can set criterion (iv) (Part D, WD cases).

C2. Which outputs exist for which case. Read the arm, the series and the surfacing step from the page.
- probe (i)(b), (i)(b2), (i)(c), (i)(d): EL2020, arms A1 and A2, cases surfaced at admitted (except admitted:ignored and admitted:span_not_seen), carried, polarity or modality. ES2009: the same cases in the run that is author-coded (not A0).
- probe (ii) offline check, (ii-r), (ii-h), joint condition: EL2020, arms A1 and A2, cases in which the page shows a misfiled carrier or rival (a carrier or rival whose matter does not fit its recorded key's definition). (ii-r) applies when the misfiled claims are all resolver-routed, (ii-h) when they are all hint-routed, the joint condition when they lie on both paths. The other path's probe does not apply. Expansion-routed misfilings are not probed; they are coded from the page under criterion (iii) or the harness-reviewer entry.
- offline reading check: EL2020 cases surfaced at key_reached.
- probe (iii): EL2020, arms A1 and A2, cases surfaced at key_reached, only where the offline reading check shows the holding key was pruned out. So it is pending together with the offline reading check.
- oracle row result: EL2020, arms A0 and A1, cases surfaced at or before the status step, unless an oracle exception applies (Part D, Caused-at).
- A2 leave-one-out (all four): EL2020, arm A2, cases surfaced at or before the status step.
- WD result: cases surfaced at carried:claims_without_the_value, in EL2020. In ES2009 only if the page states that WD is in the arm.
- No probe exists for any A0 case.

C3. Pending, and no output.
- Mark an alternative "pending" when it is decided only by a sealed output that C2 says exists for this case. List that output under "pending".
- When an alternative applies to the case (it is on the checklist for the caused-at boundary and its precondition holds on the page) but C2 says no output exists for this case, its status is "not ruled out: no output". It is not ruled out.
- An alternative applies only on the sheet of the caused-at boundary (both routing sheets for "routing, path unclear"). On any other sheet you take (E5), a probe-type item with no output is "not applicable", with the basis "not on the checklist for the caused-at boundary". So no item on another sheet is ever "not ruled out: no output".
- A sealed output can fail to appear later. You do not know which. Mark pending by C2.

C4. The conditional code. Give the class, sub-cause and caused-at the case gets if every pending output comes back not recovered, or does not move the boundary. For each output, that means:
- a probe: not recovered;
- probe (ii) offline check: the fitting key was in the recorded prompt;
- offline reading check: the holding key was in the recorded question-routing prompt;
- oracle row result, A2 leave-one-out: caused-at stays where the page puts it;
- WD result: WD carries the value in 0 of 3 WD runs, and the fresh A1 runs carry it in at most 1 of 3.
At the reveal, the sealed outputs resolve the conditional code by fixed rules; you do not apply them. Two consequences you do apply:
- "model-limited (held constant)" is never a conditional code, because it needs probe (i)(d) to recover;
- criteria (i) and (iv) are never met in your code, because they need a probe or the WD result to recover. Record them only under "pending".

==================================================================
PART D. THE RULES (verbatim from the study plan)
==================================================================

On A0:
- **A0:** model pre-coding and defect flags only. A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound. A0 enters no admission verdict.

**Class rules:**
- **Burden.** Architectural weakness, design trade-off, conversational difficulty, model-limited, and design-or-model-not-separated are assigned only after implementation defect has been considered and rejected on the case page. The per-boundary register sheet is a checklist: the page addresses every listed candidate cause for its caused-at boundary.
  - An alternative that meets none of (i)–(iv) counts as ruled out.
  - A probe-type alternative (registry cut, neutral examples, unpruned resolution, re-hinting) is ruled out only by its probe returning *not recovered*, where that probe applies to the case under Step 2b (ii).
  - The question-time shortlist alternative applies only where the offline reading check shows the holding key was pruned out. Where the key was in the recorded question-routing prompt, that check rules it out.
  - Where a probe-type alternative applies to the case (it is on the checklist for the caused-at boundary, and its precondition holds) but has no probe output (Step 2b not run, or no output), it is not ruled out, and the code is implementation defect or unclear.
  - Where no probe-type alternative applies, alternatives are ruled out under (ii)–(iv) and the page as above. Examples: the state rules, A2's support check, `admitted:ignored` cases, and a reading case whose holding key was in the question-routing prompt.
  - **At an LLM step with no model condition,** architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value. An example is the step's 94c049d contract giving it no way to carry the value. Otherwise the case is design or model, not separated.
- **Pending results (blind coding).** At pass 1, in the model pre-codes and in V4's blind codes, an alternative decided only by a sealed output is marked *pending*. The sealed outputs are a Step 2b probe, the offline reading check, an oracle row result, an A2 leave-one-out result, and the WD result. The coder records a *conditional* code: the class, sub-cause and caused-at the case gets if every pending output comes back *not recovered*, or does not move the boundary. At the reveal:
  - recovered: the probe mapping, the oracle rule, the leave-one-out rule or the WD rule sets the code;
  - not recovered: the conditional code stands;
  - inconclusive, not reproduced or no output, for a probe or WD alternative: the code is implementation defect or unclear;
  - an oracle row result or a leave-one-out sets only caused-at. When it has no output (a failed gate), the conditional code stands, with caused-at from the page, or unclear.
- **Retrospective design:**
  - A retrospective entry can never ground architectural weakness or a trade-off, nor rule out an alternative.
  - A case whose only design ground is a retrospective entry is coded implementation choice if an alternative consistent with the 94c049d text meets (i)–(iv). Otherwise it is unclear.
  - Such cases are tallied in a *retrospective design* column.
- **WD cases** (`carried:claims_without_the_value`; sub-cause *no whole-decision contract*):
  - WD is judged and admitted only by the Step 2c rule. This sub-cause is never eligible under Step 4(b) and takes no repair slot.
  - **(iv) holds** when WD carries the value at the case's checkpoint in at least 2 of 3 WD runs, while the fresh A1 runs carry it in at most 1 of 3. The case is then implementation choice: repaired if WD is admitted, unrepaired otherwise.
  - Fresh A1 carries it in 2 or 3 of 3: sampling instability, unclear.
  - WD carries it in exactly 1 of 3: inconclusive.
  - WD and fresh A1 both carry it in at most 1 of 3 and WD in 0: architectural may be argued only from the quoted 94c049d text (D4's scalar-concept passage).
  - No WD run covers the value: unclear. That covers every case if Step 2c is not run, and 3b cases unless WD is in the final configuration.
- **Autonomous-arm conflicts:**
  - An A2 case caused at the state rules by an open same-meeting conflict rests on D5 ("leaving unresolved cases reviewable"), and the harness reviewer is an implementation entry.
  - Such cases are coded **held: conflict decision.** They are scored as unclear in the agreement measures, and count as unclear in every bound.
  - Signing the open decision later does not reclassify losses observed before it.
- **Unclear,** an unclear caused-at, and coder disagreement on implementation versus not, all count as possible implementation. They count toward the 10% unclear limit, and are never architectural, trade-off, model-limited or design-or-model.
- **Recoverability:**
  - A value that RAG answered correctly from a cited chunk containing a gold line, in at least 2 of 3 runs, may not be coded conversational difficulty without a written reason.
  - A value that passed the same step at the same checkpoint in at least one other run of its arm group (A1 with A0; A2 alone) may not be coded conversational difficulty. The page states what differed.
  - A value every run of both systems misses is checked against the transcript as an evaluation-defect candidate.

**Caused-at.** Every case records *surfaced at* (the loss-trace step and sub-code) and *caused at*. Caused-at is the earliest boundary where a correction inside that boundary alone would have prevented the loss:
- **Oracle row results** (A0/A1 runs that pass the gate) apply only to rows lost at or before the status step in the recorded run. They decide between routing and the other boundaries:
  - recovered by R: routing;
  - recovered by E+R but not R, or by E+R\* but not E+R: extraction (the second is polarity);
  - not recovered by E+R\*: state rules, transcript or evaluation.
- **Exceptions to the oracle:**
  - where the page shows the deciding claim is a recorded wrong-modality carrier, or a positive carrier of a ruled-out value, that misreads its span, caused-at is extraction (listed);
  - where the displaced rival was about the same matter, R is not routing evidence, and caused-at is set from the page (listed).
- **Within routing,** the misrouted claim (carrier or rival) is the one whose matter does not fit the key's definition. Its path gives the boundary: a hint means key assignment at extraction; the resolver or expansion means key resolution and expansion. If the page cannot decide, the code is *routing, path unclear* (possible implementation at both).
- **A2 cases:** a contract whose leave-one-out recovers the row sets caused-at to the state rules (that contract). Otherwise caused-at comes from the page.
- **Reading cases** (stored with the right status in the recorded run): from the offline reading analysis, probe (iii) and the page.
- **Default:** with neither oracle nor page evidence, caused-at is unclear. It never defaults to the surfacing step. When two boundaries would each have prevented the loss, the earlier is primary.

**Candidate implementation causes, listed now** (the pilot may add new ones, but may not split or merge these):

| Boundary | Candidate causes |
|---|---|
| Extraction | registry-conditioned extraction; out-of-domain prompt examples; a modality or negation instruction missing from the prompt; the gatekeeper ignoring a span its own criteria admit; no whole-decision contract (WD rule only) |
| Key assignment at extraction | a hint to a registered key about another matter; registry-conditioned hinting |
| Key resolution and expansion | the shortlist or prune excluded a fitting key; the harness reviewer accepted a near-duplicate or over-broad key; a reuse or similarity threshold merged a new matter into an existing key |
| State rules | the settle expired a correct proposal; any state behaviour contradicting the register |
| Reading | the question-time shortlist excluded the holding key; the scalar focus gate demoted a correct fact to a near match |

==================================================================
PART E. HOW TO CODE THIS CASE
==================================================================

This procedure applies the rules of Parts B to D. Where it and Part D seem to differ, Part D governs.

E1. Copy case_id, series, arm and surfaced_at (step and sub-code) from the page.

E2. Read the page in full: the cited spans, every claim with its path and trail, the key history, the facts, the questions, the recoverability lines.

E3. Caused-at.
- Boundaries, in order: extraction (admission included), key assignment at extraction, key resolution and expansion, state rules, reading. Outside the system: transcript, evaluation.
- For each boundary in order, ask: would a correction inside this boundary alone have prevented the loss? The earliest such boundary is caused-at. It may be earlier than the surfacing step. It never defaults to the surfacing step.
- Routing: find the misrouted claim(s), the carrier or rival whose matter does not fit its key's definition, and its path. Hint: key assignment at extraction. Resolver or expansion: key resolution and expansion. If the page cannot decide: "routing, path unclear".
- Transcript: the transcript itself makes the value hard to recover. Evaluation: the gold, the suite, an adjudication or the judge is wrong.
- Oracle: for an EL2020 A0 or A1 case surfaced at or before the status step, list "oracle row result" as pending, and give caused-at from the page. If an oracle exception holds on the page, set caused_at_basis to it and do not list the oracle.
- A2: for an EL2020 A2 case surfaced at or before the status step, list the four A2 leave-one-out outputs as pending, and give caused-at from the page.
- Reading: for an EL2020 case surfaced at key_reached, list the offline reading check (and, for A1 and A2, probe (iii)) as pending.
- With no evidence for any boundary: caused-at "unclear".
- If you set caused-at to one system boundary, name the step within it in caused_at_step, using a name from A5, and set caused_at_is_llm_step as A5 marks it. For "routing, path unclear", caused_at_step is "".

E4. Held. If the arm is A2, caused-at is the state rules, and the loss rests on an open same-meeting conflict: set held to "conflict decision" and class to "unclear". Still fill in the checklist (E5); E6 does not change the class of a held case.

E5. The checklist. Take the register sheet of the caused-at boundary. For "routing, path unclear", take both routing sheets. For transcript, evaluation or unclear, take the sheet of every system boundary you considered, and at least the home sheet of the surfacing step:
- admitted, carried, polarity, modality: extraction;
- filed: key assignment at extraction, and key resolution and expansion; for cycle2_parked_*, state rules;
- proposed, applied, current, status: state rules, plus both routing sheets where the page shows a misfiled carrier or rival;
- key_reached, in_payload, answered: reading.
Each sheet lists its items under item ids: the candidate causes, the further implementation entries, and the conformance requirements. Give every item on those sheets exactly one status:
- "counts": the page shows that this case's loss rests on the entry, and either an alternative to it meets (ii) or (iii) on this page, or the entry contradicts the register (conformance);
- "ruled out": the alternative is not probe-type, and meets none of (i) to (iv) on this page;
- "pending": it is decided only by a sealed output that C2 says exists for this case;
- "not ruled out: no output": it applies (C3), but no sealed output exists for this case. This status occurs only on the sheet of the caused-at boundary;
- "not applicable": its precondition fails on the page (for example the case is not on that path), it concerns another kind of case, or it is a probe-type item on another sheet (C3).
A probe-type alternative is never "ruled out" in your code. For each item give its item id and its text as the sheet lists them, the basis (which criterion, precondition or output) and one line from the page, or the sheet, copied exactly, that shows the status. For "counts", the line comes from the page and shows this case's own link to the entry, not only the entry.

E6. The class, in this order. "The caused-at sheet" is the sheet of the caused-at boundary (both routing sheets for "routing, path unclear").
1. If an item on another sheet "counts", a correction at that boundary would also have prevented the loss. Go back to E3. Caused-at is the earliest boundary where a correction alone would have prevented the loss; a counting item at a later boundary does not move it.
2. If caused-at is "unclear": "unclear". If caused-at is "evaluation": "evaluation defect" (the gold, the suite, an adjudication or the judge is wrong). Apart from step 1, items on other sheets do not change these two classes.
3. If the arm is A0 and the page shows that the loss rests on a Phase B bug (Part F): "implementation defect", with implementation_basis "Phase B bug", phase_b_bug set to the bug's number, and criteria_met empty. This step comes before the retrospective rule below.
4. If any item on the caused-at sheet "counts": "implementation defect", with implementation_basis "conformance" or "implementation choice", and criteria_met ((ii) and/or (iii)) for a choice.
5. Else, if any item on the caused-at sheet is "not ruled out: no output": "unclear", and say which item in unclear_reason.
6. Else (every item on the caused-at sheet is ruled out, pending or not applicable, or caused-at is "transcript"), give the conditional code, assuming every pending output comes back not recovered:
   - "architectural weakness": the loss follows from a 94c049d design entry that the caused-at sheet lists for architectural weakness (its commitments, tagged (C)). Quote its operative sentence exactly, from one sentence that the caused-at sheet lists under (C). No other sentence of the paragraph grounds it: not one tagged (L), (—) or (B).
   - "design trade-off": the loss is the cost of a deliberate choice whose benefit the 94c049d text states, in an entry that the caused-at sheet lists for a trade-off (its stated benefits and costs, tagged (B)). Quote the choice and the benefit exactly, each from one sentence that the caused-at sheet lists under (B).
   - For either of these two where the rule for an LLM step with no model condition applies (A5): also show, from the page, that a correct output of that step, given its recorded inputs, would still have lost the value. If you cannot, the class is "design or model, not separated".
   - "conversational difficulty" (caused-at "transcript"): the transcript makes the value hard to recover. Not allowed when other_run_bar is true. When rag_bar is true, give a written reason.
   - "design or model, not separated": only where the rule for an LLM step with no model condition applies (A5), and only when every condition in its definition holds.
   - Otherwise "unclear".
Further rules:
- A retrospective entry never grounds architectural weakness or a design trade-off, and never rules out an alternative. If the only design ground you find is retrospective, set retrospective_design_only to true, and code "implementation defect" (implementation choice) if an alternative consistent with the 94c049d text meets (ii) or (iii); otherwise "unclear".
- If caused-at is "routing, path unclear", the class is "unclear" or "implementation defect".
- Never "model-limited (held constant)" (C4).
- WD cases (surfaced at carried:claims_without_the_value): the item "no whole-decision contract" is pending on the WD result where C2 says it exists, otherwise "not ruled out: no output". In the conditional code, architectural weakness may be argued only from the quoted 94c049d text (D4's scalar-concept passage): D4.p5, which sheet E lists whole for WD cases. Any of its sentences may be quoted, whatever its tag. No other paragraph grounds it.

E7. Sub-cause. Use a name from the sub-cause list, exactly as written. For "implementation defect", the primary implementation cause; for "unclear", the most likely possible implementation cause. If none fits, write "none fits" and give a short name and one-line definition in proposed_sub_cause. For any other class, use a name from the list that fits the class; if the list has none, write "not applicable". "Not applicable" is never used for "implementation defect" or "unclear".

E8. Recoverability. Copy the page's RAG line and its other-runs line. Set rag_bar, other_run_bar and evaluation_defect_candidate by the Recoverability rules in Part D:
- rag_bar is true when the RAG line shows a credited answer that cited a chunk containing a gold line in at least 2 of 3 RAG runs.
- other_run_bar is true when the other-runs line shows that the value passed this case's surfacing step at this case's checkpoint in at least one other run of its arm group (A1 with A0; A2 alone). Runs of other arm groups do not count here.
- evaluation_defect_candidate is true when the page shows that every run of both systems misses the value: every other run of the system, in every arm group, loses it at some step, and no RAG run gives a credited answer. If the page does not show every run, it is false.

E9. Evidence. Copy the page lines your code rests on, exactly, each with its section heading. Do not paraphrase inside a quote.

E10. If class or caused-at is unclear, say why in unclear_reason.

==================================================================
PART F. PHASE B BUGS (for A0 cases only)
==================================================================

A1, A2 and the later arms run with these repairs on; A0 runs without them. Each line states what the repair changes, as the code states it; the A0 behaviour is the unrepaired one. An A0 loss that rests on one of these bugs is coded "implementation defect", with implementation_basis "Phase B bug" and phase_b_bug set to the bug's number (E6, step 3). In A1 and A2 cases, phase_b_bug is null.
- Bug 1: a value is ruled out when none of its positive claims survives the asserted negations (a claim said before a negation of at least its authority, or a hedge with no assertion after the negation, does not; order is source time, span position, extraction order). A ruled-out current value is superseded by what the key resolves to without it (only claims said after it took effect compete), with its rejection raised in the same pass, or rejected when that is nothing; a non-current value is recorded as ruled out only by the same rule; a negation is never appended as support; under the cycle-2 support check the claims the rule relies on are checked first.
- Bug 2: a proposal takes its evidence, confidence and authority from the claim that supplied the winning value, not from the claim whose evaluation triggered it; a proposal still waiting for review takes the lineage computed when the engine returns it again.
- Bug 3: the current value's own claims compete with its challengers, so a rival that ranks lower (for example one from the same meeting with lower confidence) cannot supersede it.
- Bug 4: when only hedged claims remain, a value equal to the current one changes nothing instead of superseding the current value with itself.
- Bug 5: a claim whose key has no concept definition is not filed; registry expansion maps or parks it.
- Bug 6: the evaluation runner passes each meeting's date (from the suite or the AMI metadata) as the artifact's source time, so valid time is meeting time; it fails closed when a date or AMI start time is missing or the dates do not increase strictly in suite order.
- Bug 12 (found in Phase B): for new and supersede proposals and the rejection of the current value, a proposal applied as proposed, or expired, no longer deduplicates (an open, declined or reviewer-edited one still does), so a value can be reinstated or rejected again. Alone it lets same-meeting rivals oscillate (bug 12 braked bug 3); use it with the bug-1, bug-3, bug-4 and bug-13 repairs.
- Bug 13 (found in Phase B): before a checkpoint's proposals are confirmed, every key is evaluated again with all its claims, and a pending proposal that evaluation no longer produces expires; so a proposal from a partial view (claims mapped one by one) or an earlier pass is never applied to a state it was not computed for; an expired proposal never stands in for a later one. Use it with the bug-12 repair.

==================================================================
PART G. OUTPUT
==================================================================

Return one JSON object that validates against the schema below, and nothing else: no prose, no code fence.

Field notes:
- inputs_received: list what this message gave you, from "instructions", "register sheet", "sub-cause list", "case page". If you received, or recall, anything else about this system, this study or its results, add "other" and describe it in other_input; otherwise other_input is null.
- caused_at_step: a name from A5, of a step of the caused-at boundary; "" when caused_at is "routing, path unclear", unclear, transcript or evaluation. caused_at_is_llm_step: true for a step A5 marks LLM, false for a deterministic one, null when caused_at_step is "".
- caused_at_basis: "page"; an oracle exception; or "no evidence" when caused_at is unclear.
- misrouted_claims: each carrier or rival whose matter does not fit its key's definition, with the claim id as the page shows it. Empty when there is none.
- implementation_basis: "Phase B bug" only for an A0 case under E6 step 3, and then criteria_met is empty.
- pending: one entry per sealed output your code depends on; "sets" says what it can set; "alternative" names the checklist item or cause it decides.
- checklist: "item_id" and "item" are the item's id and text exactly as the register sheets give them. The id is the text in square brackets; the text is the rest of that line. "evidence.source" is "none", with an empty quote, only for "not applicable" when no line shows it. For "counts", it is "case page".
- design_ground: the entry id as the caused-at sheet lists it, for architectural weakness among its commitments (C), for a design trade-off among its stated benefits and costs (B); its operative sentence copied exactly from one sentence that the sheet lists under that tag (a part of the sentence is allowed); and whether the sheet marks it retrospective. Required for architectural weakness and design trade-off, and then only 94c049d entries. For a WD case, only D4.p5, from any of its sentences.
- tradeoff_benefit_quote: for a design trade-off, the 94c049d sentence stating the benefit, copied exactly from one sentence that the caused-at sheet lists under (B); otherwise null.
- llm_step_argument: for architectural weakness or design trade-off at one of the seven steps where A5's rule applies, the argument of E6; otherwise null.
- note: at most 600 characters; "" if none.
- Every quote must be an exact substring of the case page or of the register sheets in Part H.

BEGIN OUTPUT SCHEMA
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Pre-code of one case (plan 23, amendment 1, Step 3)",
  "type": "object",
  "additionalProperties": false,
  "required": ["case_id", "inputs_received", "other_input", "series", "arm", "surfaced_at", "caused_at", "caused_at_step", "caused_at_is_llm_step", "caused_at_basis", "misrouted_claims", "class", "held", "implementation_basis", "criteria_met", "phase_b_bug", "sub_cause", "proposed_sub_cause", "pending", "checklist", "design_ground", "tradeoff_benefit_quote", "llm_step_argument", "retrospective_design_only", "recoverability", "evidence", "unclear_reason", "note"],
  "properties": {
    "case_id": {"type": "string", "minLength": 1},
    "inputs_received": {"type": "array", "uniqueItems": true, "minItems": 1, "items": {"enum": ["instructions", "register sheet", "sub-cause list", "case page", "other"]}},
    "other_input": {"type": ["string", "null"]},
    "series": {"enum": ["EL2020", "ES2009"]},
    "arm": {"enum": ["A0", "A1", "A2", "A1-ref", "final configuration"]},
    "surfaced_at": {
      "type": "object", "additionalProperties": false, "required": ["step", "sub_code"],
      "properties": {
        "step": {"enum": ["admitted", "carried", "polarity", "modality", "filed", "proposed", "applied", "current", "status", "key_reached", "in_payload", "answered"]},
        "sub_code": {"type": "string", "minLength": 1}
      }
    },
    "caused_at": {"enum": ["extraction", "key assignment at extraction", "key resolution and expansion", "routing, path unclear", "state rules", "reading", "transcript", "evaluation", "unclear"]},
    "caused_at_step": {"enum": ["", "segmentation", "gatekeeper", "evidence creation", "extraction", "claim persistence", "the `state_key_hint` field of the extraction call", "the hint becomes the claim's key", "resolver", "alias merge", "candidate generation", "semantic reuse", "attach or new proposal", "harness reviewer", "review validation and release", "conflict evaluation and the resolution engine", "proposals", "settle", "confirmation", "projection", "type check", "same-meeting conflict and new-evidence rules", "support check", "question resolution", "widening", "context pack", "answer templates and gates", "grounding"]},
    "caused_at_is_llm_step": {"type": ["boolean", "null"]},
    "caused_at_basis": {"enum": ["page", "oracle exception: carrier misreads its span", "oracle exception: same-matter rival", "no evidence"]},
    "misrouted_claims": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["claim", "role", "path"],
        "properties": {
          "claim": {"type": "string", "minLength": 1},
          "role": {"enum": ["carrier", "rival"]},
          "path": {"enum": ["hint", "resolver", "expansion", "not shown"]}
        }
      }
    },
    "class": {"enum": ["implementation defect", "architectural weakness", "design trade-off", "conversational difficulty", "evaluation defect", "model-limited (held constant)", "design or model, not separated", "unclear"]},
    "held": {"enum": ["conflict decision", null]},
    "implementation_basis": {"enum": ["conformance", "implementation choice", "Phase B bug", null]},
    "criteria_met": {"type": "array", "uniqueItems": true, "items": {"enum": ["(ii)", "(iii)"]}},
    "phase_b_bug": {"enum": ["1", "2", "3", "4", "5", "6", "12", "13", null]},
    "sub_cause": {"type": "string", "minLength": 1},
    "proposed_sub_cause": {"type": ["string", "null"]},
    "pending": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["output", "sets", "alternative"],
        "properties": {
          "output": {"enum": ["probe (i)(b)", "probe (i)(b2)", "probe (i)(c)", "probe (i)(d)", "probe (ii) offline check", "probe (ii-r)", "probe (ii-h)", "probe (ii) joint condition", "probe (iii)", "offline reading check", "oracle row result", "A2 leave-one-out: filing_type_check", "A2 leave-one-out: resolution_same_meeting_conflict", "A2 leave-one-out: supersession_requires_new_evidence", "A2 leave-one-out: filing_support_check", "WD result"]},
          "sets": {"enum": ["criterion (i)", "criterion (iv)", "caused-at", "precondition", "sub-cause", "model-limited", "unclear (possible implementation)"]},
          "alternative": {"type": "string", "minLength": 1}
        }
      }
    },
    "checklist": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "additionalProperties": false, "required": ["boundary", "item_id", "item", "status", "basis", "evidence"],
        "properties": {
          "boundary": {"enum": ["extraction", "key assignment at extraction", "key resolution and expansion", "state rules", "reading"]},
          "item_id": {"type": "string", "minLength": 1},
          "item": {"type": "string", "minLength": 1},
          "status": {"enum": ["ruled out", "counts", "pending", "not ruled out: no output", "not applicable"]},
          "basis": {"type": "string", "minLength": 1},
          "evidence": {
            "type": "object", "additionalProperties": false, "required": ["source", "quote"],
            "properties": {
              "source": {"enum": ["case page", "register sheet", "none"]},
              "quote": {"type": "string"}
            }
          }
        },
        "allOf": [
          {"if": {"properties": {"status": {"const": "counts"}}, "required": ["status"]},
           "then": {"properties": {"evidence": {"properties": {"source": {"const": "case page"}, "quote": {"minLength": 1}}}}}}
        ]
      }
    },
    "design_ground": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["entry", "retrospective", "quote"],
        "properties": {
          "entry": {"type": "string", "minLength": 1},
          "retrospective": {"type": "boolean"},
          "quote": {"type": "string", "minLength": 1}
        }
      }
    },
    "tradeoff_benefit_quote": {"type": ["string", "null"]},
    "llm_step_argument": {"type": ["string", "null"]},
    "retrospective_design_only": {"type": "boolean"},
    "recoverability": {
      "type": "object", "additionalProperties": false,
      "required": ["rag_outcome", "rag_bar", "rag_reason", "other_runs", "other_run_bar", "what_differed", "evaluation_defect_candidate"],
      "properties": {
        "rag_outcome": {"type": "string"},
        "rag_bar": {"type": "boolean"},
        "rag_reason": {"type": ["string", "null"]},
        "other_runs": {"type": "string"},
        "other_run_bar": {"type": "boolean"},
        "what_differed": {"type": ["string", "null"]},
        "evaluation_defect_candidate": {"type": "boolean"}
      }
    },
    "evidence": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "additionalProperties": false, "required": ["source", "section", "quote"],
        "properties": {
          "source": {"enum": ["case page", "register sheet"]},
          "section": {"type": "string"},
          "quote": {"type": "string", "minLength": 1}
        }
      }
    },
    "unclear_reason": {"type": ["string", "null"]},
    "note": {"type": "string", "maxLength": 600}
  },
  "allOf": [
    {"not": {"properties": {"class": {"const": "model-limited (held constant)"}}, "required": ["class"]}},
    {"if": {"properties": {"held": {"const": "conflict decision"}}, "required": ["held"]},
     "then": {"properties": {"class": {"const": "unclear"}, "caused_at": {"const": "state rules"}, "arm": {"const": "A2"}}}},
    {"if": {"properties": {"class": {"const": "implementation defect"}}, "required": ["class"]},
     "then": {"properties": {"implementation_basis": {"enum": ["conformance", "implementation choice", "Phase B bug"]}, "caused_at": {"enum": ["extraction", "key assignment at extraction", "key resolution and expansion", "routing, path unclear", "state rules", "reading"]}}},
     "else": {"properties": {"implementation_basis": {"const": null}, "criteria_met": {"maxItems": 0}, "phase_b_bug": {"const": null}}}},
    {"if": {"properties": {"implementation_basis": {"const": "implementation choice"}}, "required": ["implementation_basis"]},
     "then": {"properties": {"criteria_met": {"minItems": 1}}}},
    {"if": {"properties": {"implementation_basis": {"const": "Phase B bug"}}, "required": ["implementation_basis"]},
     "then": {"properties": {"arm": {"const": "A0"}, "phase_b_bug": {"type": "string"}, "criteria_met": {"maxItems": 0}}}},
    {"if": {"properties": {"phase_b_bug": {"type": "string"}}, "required": ["phase_b_bug"]},
     "then": {"properties": {"arm": {"const": "A0"}, "implementation_basis": {"const": "Phase B bug"}}}},
    {"if": {"properties": {"caused_at": {"enum": ["routing, path unclear", "transcript", "evaluation", "unclear"]}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"const": ""}, "caused_at_is_llm_step": {"const": null}}}},
    {"if": {"properties": {"caused_at": {"const": "extraction"}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"enum": ["segmentation", "gatekeeper", "evidence creation", "extraction", "claim persistence"]}}}},
    {"if": {"properties": {"caused_at": {"const": "key assignment at extraction"}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"enum": ["the `state_key_hint` field of the extraction call", "the hint becomes the claim's key"]}}}},
    {"if": {"properties": {"caused_at": {"const": "key resolution and expansion"}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"enum": ["resolver", "alias merge", "candidate generation", "semantic reuse", "attach or new proposal", "harness reviewer", "review validation and release"]}}}},
    {"if": {"properties": {"caused_at": {"const": "state rules"}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"enum": ["conflict evaluation and the resolution engine", "proposals", "settle", "confirmation", "projection", "type check", "same-meeting conflict and new-evidence rules", "support check"]}}}},
    {"if": {"properties": {"caused_at": {"const": "reading"}}, "required": ["caused_at"]},
     "then": {"properties": {"caused_at_step": {"enum": ["question resolution", "widening", "context pack", "answer templates and gates", "grounding"]}}}},
    {"if": {"properties": {"caused_at_step": {"enum": ["gatekeeper", "extraction", "the `state_key_hint` field of the extraction call", "resolver", "candidate generation", "support check", "question resolution", "grounding"]}}, "required": ["caused_at_step"]},
     "then": {"properties": {"caused_at_is_llm_step": {"const": true}}}},
    {"if": {"properties": {"caused_at_step": {"enum": ["segmentation", "evidence creation", "claim persistence", "the hint becomes the claim's key", "alias merge", "semantic reuse", "attach or new proposal", "harness reviewer", "review validation and release", "conflict evaluation and the resolution engine", "proposals", "settle", "confirmation", "projection", "type check", "same-meeting conflict and new-evidence rules", "widening", "context pack", "answer templates and gates"]}}, "required": ["caused_at_step"]},
     "then": {"properties": {"caused_at_is_llm_step": {"const": false}}}},
    {"if": {"properties": {"class": {"enum": ["architectural weakness", "design trade-off"]}}, "required": ["class"]},
     "then": {"properties": {
       "design_ground": {"minItems": 1, "items": {"properties": {"retrospective": {"const": false}}}},
       "retrospective_design_only": {"const": false},
       "caused_at": {"enum": ["extraction", "key assignment at extraction", "key resolution and expansion", "state rules", "reading"]}}}},
    {"if": {"properties": {"class": {"const": "design trade-off"}}, "required": ["class"]},
     "then": {"properties": {"tradeoff_benefit_quote": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"class": {"enum": ["architectural weakness", "design trade-off"]}, "caused_at_step": {"enum": ["the `state_key_hint` field of the extraction call", "resolver", "candidate generation", "support check", "question resolution", "grounding"]}}, "required": ["class", "caused_at_step"]},
     "then": {"properties": {"llm_step_argument": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"class": {"enum": ["architectural weakness", "design trade-off"]}, "caused_at_step": {"const": "gatekeeper"}, "surfaced_at": {"properties": {"step": {"const": "admitted"}, "sub_code": {"const": "ignored"}}, "required": ["step", "sub_code"]}}, "required": ["class", "caused_at_step", "surfaced_at"]},
     "then": {"properties": {"llm_step_argument": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"class": {"const": "design or model, not separated"}}, "required": ["class"]},
     "then": {"required": ["caused_at_step"], "properties": {"caused_at_step": {"enum": ["gatekeeper", "the `state_key_hint` field of the extraction call", "resolver", "candidate generation", "support check", "question resolution", "grounding"]}}}},
    {"if": {"properties": {"class": {"const": "design or model, not separated"}, "caused_at_step": {"const": "gatekeeper"}}, "required": ["class", "caused_at_step"]},
     "then": {"properties": {"surfaced_at": {"properties": {"step": {"const": "admitted"}, "sub_code": {"const": "ignored"}}}}}},
    {"if": {"properties": {"class": {"const": "conversational difficulty"}}, "required": ["class"]},
     "then": {"properties": {"caused_at": {"const": "transcript"}, "recoverability": {"properties": {"other_run_bar": {"const": false}}}}}},
    {"if": {"properties": {"class": {"const": "conversational difficulty"}, "recoverability": {"properties": {"rag_bar": {"const": true}}, "required": ["rag_bar"]}}, "required": ["class", "recoverability"]},
     "then": {"properties": {"recoverability": {"properties": {"rag_reason": {"type": "string", "minLength": 1}}}}}},
    {"if": {"properties": {"recoverability": {"properties": {"other_run_bar": {"const": true}}, "required": ["other_run_bar"]}}, "required": ["recoverability"]},
     "then": {"properties": {"recoverability": {"properties": {"what_differed": {"type": "string", "minLength": 1}}}}}},
    {"if": {"properties": {"class": {"const": "evaluation defect"}}, "required": ["class"]},
     "then": {"properties": {"caused_at": {"const": "evaluation"}}}},
    {"if": {"properties": {"class": {"const": "unclear"}}, "required": ["class"]},
     "then": {"properties": {"unclear_reason": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"caused_at": {"const": "unclear"}}, "required": ["caused_at"]},
     "then": {"properties": {"class": {"const": "unclear"}, "unclear_reason": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"caused_at": {"const": "routing, path unclear"}}, "required": ["caused_at"]},
     "then": {"properties": {"class": {"enum": ["unclear", "implementation defect"]}}}},
    {"if": {"properties": {"retrospective_design_only": {"const": true}}, "required": ["retrospective_design_only"]},
     "then": {"properties": {"class": {"enum": ["implementation defect", "unclear"]}}}},
    {"if": {"properties": {"sub_cause": {"const": "none fits"}}, "required": ["sub_cause"]},
     "then": {"properties": {"proposed_sub_cause": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"sub_cause": {"const": "not applicable"}}, "required": ["sub_cause"]},
     "then": {"properties": {"class": {"not": {"enum": ["implementation defect", "unclear"]}}}}},
    {"if": {"properties": {"inputs_received": {"contains": {"const": "other"}}}, "required": ["inputs_received"]},
     "then": {"properties": {"other_input": {"type": "string", "minLength": 1}}}}
  ]
}
END OUTPUT SCHEMA

==================================================================
PART H. MATERIALS
==================================================================

<register_sheet>
{REGISTER_SHEET}
</register_sheet>

<subcauses>
{SUBCAUSES}
</subcauses>

<case_page>
{CASE_PAGE}
</case_page>

Code this case now, following Part E. Return only the JSON object.
~~~~

## 3. Where each part of the prompt comes from

All amendment lines are in `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md`.

| Prompt part | Source | Verbatim or gloss |
|---|---|---|
| Opening paragraph | amendment line 402 (page only, fresh context, no memory or result reports) | gloss |
| A1, the system | the amendment's component list (line 101) and probe text (lines 249-251); `app/services/state_key_resolution_service.py` at 3320375, lines 935-1010 (a claim carrying a registered key is skipped; others go to the resolver, then to expansion); for reading, the register's section R.1 (Step type, Chain); the step names in quotes are A5's; evidence creation follows the register's A.6: "Evidence is created for every admitted decision of the artifact"; the harness reviewer follows the register's K2.6c: "A rejected proposal is only recorded; under `quality` no reject is submitted" | gloss; the register sheets govern where they differ |
| A2, contract and WD lines | `app/core/cycle2_flags.py` at 3320375: WD lines 61-64, filing_type_check 65-69, resolution_same_meeting_conflict 70-74, supersession_requires_new_evidence 75-79, filing_support_check 80-85 | the quoted sentences are verbatim (the `summary` strings, joined) |
| A3, the steps | `23-loss-trace.py` lines 12-29 (the chain in the docstring) | verbatim, line breaks joined; the demoted-value sentence is a gloss of lines 31-33 |
| A3, the sub-codes | `23-loss-trace.md` lines 34-45, last column | verbatim. The codebook's Limits section (lines 189-196) is left out on purpose: lines 192 and 195 make frequency statements ("often", "usually") that would steer the coder |
| A3, phase numbering | `23-loss-trace.py` lines 1085-1086 and 1092 | gloss |
| A4, the page | `23-loss-trace.py` lines 1081-1155 (`case_page`); amendment lines 390-397; the per-run detail of the other-runs and RAG lines from amendment lines 363-365 (Section 6.2; Section 7, point 14) | gloss |
| A5, the steps | the step names and their LLM or deterministic marks: the Chain lines of the register's sections A.1, E.1, K1.1, K2.1, S.1 and R.1; for the "type check" and the "same-meeting conflict and new-evidence rules", which the S.1 Chain line does not name, sheet S's list of A2's contracts ("Type check: deterministic"; "Same-meeting conflict and new-evidence rules: deterministic"). The scope of the rule, per step, from the sheets: sheet E, cause 4: "the gatekeeper is an LLM step with no model condition"; sheet K1: "The hint field of the extraction call is an LLM step with no model condition, so the page must also meet the condition of line 340"; sheet K2: "The resolver and candidate generation are LLM steps with no model condition. At either step the page must also meet the condition of line 340 (quoted on sheet K1); otherwise the case is design or model, not separated."; sheet S: "A2's support check is an LLM step with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1)."; sheet R: "Question resolution and grounding are LLM steps with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1)." Amendment line 331: "the caused-at boundary is an LLM step with no model condition (routing, reading, A2's support check, the gatekeeper for `admitted:ignored` cases)". Amendment line 340: "**At an LLM step with no model condition,** architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value." | the step names are verbatim from those lines; the K1 names keep their leading article and backticks, and the S.1 Chain line's "A2 adds the support check" gives "support check". The arm marks are a gloss: the marks of the three contract steps from sheet S's list of A2's contracts and the register's X.4 table of A2's four write contracts (which give each step's contract), and from amendment line 534, where the final configuration is "A1-ref plus each admitted contract and its admitted A2-only repairs", with no contract in A1-ref (line 533: "A1-ref replaces A1 as the no-contract reference"); "not in A0" for "settle" from the S.1 Chain line, "settle (A1, A2; deterministic, harness)", and from Part F, whose bug 13 is the settle repair and which the later arms also run. The rest is a gloss. Sheet R's "question routing" (in its criterion (ii) block) is the R.1 Chain line's "question resolution", the name sheet R's line-340 sentence uses. The register's K2.1 counts the embedding shortlist and prompt pruning among the deterministic parts, but its Chain line has no such step, so A5 has none. A loss resting on it is the candidate cause "the shortlist or prune excluded a fitting key", which the sealed routing outputs decide (C1, C2), so it never reaches the class rule in a pre-code. Sheet K2 names "candidate generation" beside the resolver, as decision sheet C62 (b) adopts (Section 7, point 24). If the signed register names its steps differently, the names are aligned before signing, and both hashes change |
| B, the eight labels | amendment line 321 (the count) and lines 323-331 (the table) | the table is verbatim; the lower-case label strings are this file's choice |
| B, terms | amendment lines 102-108 (register entries), 233-281 (Step 2b), 283-297 (Step 2c), 399-420 (reveal, pass 1, V4) | gloss |
| C1, sealed outputs | amendment lines 241-260 (probes), 216-219 (offline reading check), 199-206 (oracles), 223 (leave-one-out), 289-297 and 350-356 (WD); the "can set" column follows the mapping at lines 271-281 | gloss |
| C2, which outputs exist | amendment lines 238, 241, 246, 249-252, 257-258, 260, 216, 368, 376, 223, 305, 356; "No probe exists for any A0 case" follows from line 238; the exception of `admitted:span_not_seen` from probe (i) follows the probe note's PN-8 and P2 (`23-am1-probe-note.md:311`, "Probe (i) does not apply to them."), as decision sheet A11 settles it | gloss. See Section 7, points 6 and 22 |
| C3, pending and no output | amendment lines 336-339 (probe-type alternatives, no output) and 341 (pending) | gloss; the status name "not ruled out: no output" is this file's (Section 7, point 5) |
| C4, the conditional code | amendment lines 341-345; the WD outcome from line 355; the two consequences follow from lines 278-279 (model-limited needs (d)) and 325 (criteria (i) and (iv)) | gloss |
| D, A0 | amendment line 309 | verbatim |
| D, class rules | amendment lines 333-365 | verbatim |
| D, caused-at | amendment lines 367-378 | verbatim |
| D, candidate causes | amendment lines 380-388 | verbatim |
| E, procedure | Parts B-D | gloss, as follows. E5's "counts" reads line 325: "the loss rests on an *implementation* entry, and an alternative counts". C3's last bullet and the limit of E6 steps 4-5 to the caused-at sheet read line 338: "it is on the checklist for the caused-at boundary". E6 step 1 reads line 378: "When two boundaries would each have prevented the loss, the earlier is primary." E6 step 2 reads line 361 (an unclear caused-at) and line 334, whose burden does not name evaluation defect (Section 7, point 19). E6 step 3 reads line 309 (Section 7, point 20). E6 step 5 ("unclear" when an item is not ruled out for lack of output and none counts) reads line 338's "implementation defect or unclear" with the class definition at line 325: implementation choice needs an alternative that meets (i)-(iv). The (C) and (B) limits in E6 step 6 follow the sheets' lists of 94c049d text a page may quote, sentence by sentence (decision sheet C8 (a), Correction 2). E5's home sheets per surfacing step are this file's mapping |
| E6, D4's scalar-concept passage | amendment line 355; in `23-am1-design-text-94c049d.md` the paragraph on scalar concept generation is D4.p5 (lines 258-270 of that file); the register's sheet E: "For WD cases (surfaced at `carried:claims_without_the_value`), only D4.p5, quoted whole, whatever the tag of its sentences (amendment line 355):" | the identification as D4.p5 is a gloss (Section 7, point 9; decision sheet C17 (a)). The extract carries its text under sheet E, each sentence marked (WD, B) or (WD, C) (Section 1) |
| F, Phase B bugs | `app/core/cycle2_flags.py` at 3320375, lines 87-140 (the `summary` strings of the eight system repairs); the eight system repairs are the `SYSTEM_REPAIRS` set at `23-loss-trace.py:81-83` | the bug lines are verbatim (strings joined); the framing sentences are a gloss. The basis "Phase B bug" is this file's (Section 7, point 20) |
| G, output | Section 4 | this file's design |

Parts of the amendment deliberately left out of the prompt:
- The oracle table in full (lines 199-206), the probe mapping (lines 271-281), the recovery rule (lines 262-269) and the WD admission thresholds (lines 289-294). The reveal applies them mechanically; the pre-coder only marks the outputs pending. The register sheets as built quote six lines of the probe mapping; the extract leaves them out (Section 1).
- Every result: the "Already read" list (lines 33-63), the Why section (lines 18-31), the cost table, and every count. The prompt contains no run result. This holds for the filled prompt only if the extract is built as Section 1 requires: the register sheets as built carry run counts, one of them on the "Already read" list (Section 7, point 18). Blindness check 7 (Section 5) tests it; the extract passed it on 28 October 2026.

## 4. The output and the agreement measures

**How the fields serve the agreement measures** (amendment lines 422-430):

| Measure | Fields |
|---|---|
| Cohen's kappa on the eight labels | `class`. A held case has `class` "unclear" by the schema, as line 359 scores it |
| Kappa and positive agreement on implementation versus not, unclear counted with implementation | `class` in {"implementation defect", "unclear"} = 1, else 0 |
| Kappa on caused-at | `caused_at` (nine values) |
| Sub-cause agreement where both coders code implementation | `sub_cause` (and `phase_b_bug` for A0) |
| Each coder's blind caused-at match rate with the oracle | `caused_at`, with `caused_at_basis` to list the oracle exceptions |
| Share of pending cases; blind binary kappa on cases with no pending alternative | Primary, as recommended (Section 7, point 21): a case has a pending alternative when `pending` has an entry whose `sets` is not "caused-at". Reported beside it: `pending` non-empty, or empty |
| The copy check (line 430) | `class` mapped to implementation versus not, blind codes, compared with V4's and the author's |

**Other uses:**
- Candidate causes, reported only (line 406): `sub_cause` where `class` is implementation (a candidate cause is one given as primary implementation cause for at least 3 distinct values; the value id comes from the page index, not from the pre-code). A candidate cause selects no case and adds no condition to Step 4(b), whose eligibility is line 480. V4 codes every case (line 405).
- The retrospective design column (line 349): `retrospective_design_only`.
- Held cases: `held`.
- 3b's share of cases that fit no frozen sub-cause (line 305): `sub_cause` = "none fits". "Not applicable" is not counted there: it marks a code of a non-implementation class (decision sheet B18).
- The unclear limit (line 442): `class`.
- A0 shares in the bound rule (lines 309 and 459): `class`, `implementation_basis` and `phase_b_bug`. A record with `implementation_basis` "Phase B bug" counts as repaired (Phase B) and enters no bound (line 309).

**Validation after each call** (by a script, not by the model). A record that fails any check is not used (Section 5, R7):
1. The output parses as one JSON object and validates against the schema in the prompt.
2. `case_id`, `series`, `arm` and `surfaced_at` equal the page's values.
3. Every quote (`evidence`, `checklist[].evidence`, `design_ground[].quote`, `tradeoff_benefit_quote`) is an exact substring of the stated source: the case page, or the extract filled into `{REGISTER_SHEET}` (Section 1).
4. `checklist` lists every item of the sheets E5 requires for the case's caused-at and surfacing step, each once, under its item id and with the extract's text for that id, and no other item. In the extract an item is a line that starts with `- [ID] ` under a sheet (its candidate causes and further implementation entries) or under the sheet's list of conformance requirements; its text is the rest of that line. Items on a sheet other than the caused-at sheet have no status "not ruled out: no output" (C3).
5. `pending` uses only outputs that C2 allows for this arm, series and surfacing step.
6. `design_ground` entries and `tradeoff_benefit_quote`, sentence by sentence (decision sheet C8 (a), Correction 2). The sentences are those of the caused-at sheet's block "94c049d text a page may quote" in the extract; after the sheet, the same sentences carry the tag (C) or (B) in the paragraph text.
   - Architectural weakness: each `entry` is an id that the caused-at sheet lists under "For architectural weakness (C)", and its quote is a substring of one sentence listed there under that id.
   - Design trade-off: each `entry` is an id that the caused-at sheet lists under "For a trade-off (B)", and its quote is a substring of one sentence listed there under that id. `tradeoff_benefit_quote` is a substring of one sentence that the caused-at sheet lists under (B).
   - A sentence the register tags (B, C) counts under the list in which it appears on that sheet.
   - A WD case (surfaced at `carried:claims_without_the_value`): the only entry is D4.p5, and each quote is a substring of one of its sentences, as sheet E lists them for WD cases, whatever the tag (amendment line 355; decision sheet C17).
   - No other sentence passes: not one tagged (L) or (—), and not a sentence of a listed paragraph that the sheet does not list.
7. `sub_cause` is a name in the frozen list, "none fits", or "not applicable" (decision sheet B18). "Not applicable" is allowed only when `class` is neither "implementation defect" nor "unclear"; the schema tests this too.
8. `inputs_received` is exactly the four expected inputs, and `other_input` is null.
9. `caused_at_step` is a step of the case's arm (A5): not "settle" if `arm` is A0; not "type check", "same-meeting conflict and new-evidence rules" or "support check" if `arm` is A0, A1 or A1-ref. A1-ref runs no contract (amendment line 533: "A1-ref replaces A1 as the no-contract reference"). For the final configuration the check tests none of the three steps, since the page states which contracts were admitted.

## 5. Run conditions (requirements)

- **R1. One case per call.** Each call starts a new context: no conversation history, no earlier page, pre-code or output.
- **R2. Page only.** The model's whole input is the assembled prompt (Section 1). If the channel adds its own system prompt, that text is recorded, and it contains no repository content.
- **R3. No tools.** The model cannot read files, run commands, browse, or call other agents. A call with any recorded tool call is void.
- **R4. No repository memory or result reports.** The input contains none of:
  - the auto-memory index (`MEMORY.md`) or any memory file;
  - `AGENTS.md` or `CLAUDE.md` files, git status, or the working directory listing;
  - the amendment, plan 23, the bug list, the loss-trace results, or any other report;
  - any Step 2, 2b or 2c output;
  - any coder's codes.

  **This needs action.** The channel used for the loss-trace adjudications does not meet R3 or R4 as configured. The transcript of the adjudicator subagent of workflow wf_0db6eaa4 (`~/.claude/projects/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/subagents/workflows/wf_0db6eaa4-f2a/agent-aa447f1839f5ee03c.jsonl`) records:
  - line 6: the auto-memory index, as an attachment of type "instructions", file type "AutoMem";
  - line 7: a `session_context` attachment. Its git status lists commit messages that report results, for example "3320375 Phase B, fifth review: ruled-out records hold; bug-7 rescoring results";
  - line 3: an `environment` attachment (working directory, platform); line 5: a `skill_listing` attachment; line 8: a `date` attachment;
  - 12 tool calls: 11 Bash calls and one StructuredOutput call. (The string "Bash" occurs in 20 tool-use blocks; 9 of them are copies inside `api-request-blob` records.)

  Also:
  - the workflow subagent that drafted this file also received the auto-memory index in its context;
  - the memory index includes result summaries and a profile of the generator model. Both would steer the coder.
- **R5. Model.** Proposed: `claude-opus-5-5` (Claude Opus 5.5), the model of the loss-trace adjudications. The adjudicator transcripts record `"model":"claude-opus-5-5"` (for example `agent-aa447f1839f5ee03c.jsonl:12` above, and the agent transcripts of workflow wf_c00c1888). The same model also did the stance correction (`thesis/notes/thesis_completion/artifacts/17-human-studies.md:23`). One model id for every case; the served model id is recorded per call. **Decision for the author** (Section 7, point 1).
- **R6. Settings.** The channel's defaults. No tuning, no prompt changes after signing. Whatever settings the channel exposes are recorded per call. If it exposes none, "none exposed" is recorded.
- **R7. One output per case.** No sampling of several outputs. If an output fails validation (Section 4), the call is repeated once, in a fresh context, with the identical input. Both attempts are logged. A case that fails twice gets no pre-code, and the count is reported. For V4, AG5 (Section 9) applies this rule, with voids, missing answers and rejected attempts counted as attempts.
- **R8. Timing.** The pre-codes are made after the sub-cause list is frozen and committed (order of work item 2), and hashed and committed before author pass 1 (item 4). They are not shown to V4 (copy check, line 430). R8 covers the pre-codes only: V4's packets are staged only after item 4 is committed (amendment line 405; Section 9).
- **R9. Records per call:** case id; SHA-256 of the template (with the extract filled in at signing), the extract, the page, the sub-cause list and the assembled prompt; model id (requested and served); channel; settings; time; raw output; validation result; the channel's transcript, where it writes one.

**How blindness is checked:**
1. **Page provenance.** The page builder records the SHA-256 of every data file it reads. Each must match the amendment's frozen-input table, the run manifest, or the signed register files.
   - A run's four files (state, trace, answers, report) are checked together: the verifier recomputes the hash of their concatenation, in that order, as `23-am1-run-manifest.py` does, and compares it with the run manifest (amendment line 75). A RAG run's `.rag.json` file is compared directly.
   - Any Step 2, 2b or 2c output, any adjudication batch after v1, or any audit or v2 file fails the check. The audit list `23-am1-audit-list.json` is such a file and fails it (decision sheet B25).
   - Code is pinned by hash, not by this check: `23-loss-trace.py` by its frozen hash (amendment line 69), and the Step 3 page builder by the hash recorded when it is committed (order of work item 1). The modules the builder imports are not data files.
2. **Page content.** Each page's section headings must be in the allowed set: the `case_page` sections, the Step 3 items (amendment lines 390-397), and the arm and series. A term scan (oracle, E+R, leave-one-out, probe, recovered, inconclusive, gate, WD, pre-code, pass 1, V4, v2) flags hits for a hand check. Transcript spans can contain such words, so a hit is not a failure by itself.
3. **Assembly.** A verifier rebuilds each assembled prompt from the template (with the extract filled in) and the two run-time inputs, and compares hashes.
4. **Channel audit.** Each call's recorded input contains the assembled prompt, plus only the channel attachments on a list fixed with the channel (Section 7, point 2). It contains no memory or instruction-file attachment, no session context or git status, no working-directory listing, and no tool call.
5. **Context declaration.** `inputs_received` must be exactly the four expected inputs. A record declaring "other" is void, and the case is re-run on a clean channel.
6. **No access to sealed files.** Follows from R3; for V4, from AG1, AG2 and AG4 (Section 9). The sealed outputs exist only as hashed files until items 4 and 5 are committed (amendment line 411).
7. **Extract content** (once, at signing, before the template hash is recorded). The text filled into `{REGISTER_SHEET}`:
   - contains no string "decision" or "decisions" followed by a number (Section 7, point 17; sheet S as built on 27 October had "decisions 5 and 13 (iii)");
   - contains no text of amendment lines 271-281 (the probe mapping);
   - contains no numeral other than an id, a parameter value, or a line or section reference. A script lists every numeral with its context, and the list is checked by hand (Section 7, point 18).
   - **Result, 28 October 2026** (pre-tag pass; extract SHA-256 `744b7398…`; script `blind7.py` and its output in the session scratchpad, folder `pretag/template/`, working files):
     - no "decision" or "decisions" followed by a number. Nor any "decision sheet", "Decisions for the author", "claims register" or "R-4".
     - no quote of amendment lines 271-281. A search for every run of six words of those lines finds two, both candidate-cause names that the extract quotes from line 386 ("the shortlist or prune excluded a fitting key") and line 388 ("the question-time shortlist excluded the holding key"); the mapping lines repeat these names. Neither is mapping text.
     - numerals: after masking ids, line and section references, code spans and fenced code, 392 numerals in 183 distinct contexts were listed and read by hand. All are parameter values (for example 0.30, 8, 12, 0.80, 0.42, 5.0, the rule-scorer weights, `MEETING_DISCUSSION` 30), ids (bug, rule, step, cause and DR numbers, the DR column of the rationale table, the years inside LaTeX citation keys of 94c049d text, "Line 309"), code values (the HTTP status 400, `answer_canonical_max_items` 0) or numbers in quoted prompt or 94c049d text ("'40 dollars'"). No run count, incidence figure or "Already read" item is left. Pass.
   - **Result after the pre-tag follow-ups, 28 October 2026** (extract SHA-256 `09036929…`, rebuilt by `23-am1-precoder-extract.py`; the same `blind7.py`, its output in the session scratchpad, folder `pretag2/`, working files): the same findings. No "decision" or "decisions" followed by a number, and none of the other pointer strings; the same two six-word windows, from lines 273 and 277, both candidate-cause names; the same 392 numerals, line for line apart from line numbers. The follow-ups removed only text without an unmasked numeral and added S.4's line for D5.p6's first sentence, which has none. Pass.

## 6. Leak check of the blind case page

Code read: `thesis/notes/thesis_completion/artifacts/23-loss-trace.py`, the working-tree file. Its SHA-256 equals the frozen v3.1 hash (amendment line 69), checked on 27 October 2026. The check is by reading the code. No pages were generated, because running the script imports `app` packages, and this task may not risk reading `.env`.

The page builder is `case_page` (lines 1081-1155). The option is `--case-pages DIR` with `--sample N` (lines 1197-1199). It writes `{case_id}.md` per sampled row (lines 1262-1271).

### 6.1 What `case_page` prints

| Lines | Printed | Source | Sealed output? | Verdict |
|---|---|---|---|---|
| 1090; 1264-1265 | `# Case {case_id}`: the first 10 hex digits of sha256(run_id\|fact_id\|k) | hash | no | keep |
| 1091-1093 | gold value, kind, expected status, checkpoint k, the meeting after which k falls, aliases | frozen suite | no | keep |
| 1094-1095 | each cited span's text, with the gatekeeper's policy | trace (`memory_gatekeeper` output, lines 415-419) | no | keep |
| 1097-1113, 1115-1119 | claims from the cited spans and the spans next to them, by k: claim id suffix, span, extraction phase, subject, predicate, value, polarity, modality; parking by k; the evaluation trail by k (phase, key, result, proposal value, reason) | state dump and trace | no | keep |
| 1112, 1073-1078 | the reason, after `_neutral`, cut at 110 characters | trace | no | keep. It still shows the arm: checked on a0_r1, a1_r2 and a2_r1, the neutralised reasons include "current value ranks higher", "hedged same value" and "no concept definition for ..." only in A1 and A2, and "same meeting conflict" only in A2. The arm is not a sealed output, and the Step 3 page needs it anyway (Section 7, point 3) |
| 1120-1124 | claims from those spans extracted only after k (first line only) | state dump and trace | no | keep |
| 1125-1129 | claims by k from other spans that share words with the value | matcher (`match_level`), not adjudications | no | keep |
| 1130-1140 | facts under those keys, or sharing words with the value, at k: key, value, creation phase, status at k, replacement | rebuilt state | no | keep |
| 1141-1153 | single-value questions at k: question, keys resolved, answer facts (up to 12), near matches (up to 8), answer (up to 400 characters), scored correct | answers file; scores from the run's own report (`report["scorecard"]["scores"]`, line 395) | no. It is the recorded judge result of the frozen run | keep; Step 3 pages must use the frozen run's scores, not post-B3 re-judgings |
| 1154 | a "Coder's verdict" form: first failing step, sub-code, note | fixed text | no | **withhold** from Step 3 pages. It asks for the loss-trace coding, which Step 3 gives on the page, and it conflicts with the JSON output. The prompt also says to ignore it |

**Not printed** (good): the trace's verdict (loss and sub-code), the defect flags, the support texts, the adjudication decisions, the matcher's pending items, `credit_without_state`, the arm label, the run id, the fact id. The docstring says so (lines 1082-1084), and so does the codebook (`23-loss-trace.md:187`).

**Conclusion for the existing page:** it prints no sealed output. No Step 2, 2b or 2c output exists yet, and the function reads none of their inputs. One field must go: the "Coder's verdict" form.

### 6.2 The Step 3 additions (amendment lines 390-397)

The Step 3 page builder is not written yet (order of work item 1, amendment line 400). Requirements per added item:

| Item | Sealed output at risk | Requirement |
|---|---|---|
| step and sub-code | none (the frozen loss trace under v1) | keep; take it from the frozen `23-loss-trace.json` |
| the key history | none | keep, from the trace. For routing, the coder needs each involved key's registered definition at the time; include it (Section 7, point 8) |
| the path of every carrier and rival | **the Step 2b (ii) offline check** (amendment lines 249-250) | give the path only (hint, resolver, expansion with reuse or a new key). **Withhold** the resolver prompt's candidate list, the registry shown in the extraction prompt, and any statement of whether the gold-holding or a fitting key was in either |
| registry size | none | keep: the size only, not the list |
| reading cases | **the offline reading check** (amendment lines 216-219) | **withhold** the question-routing prompt's key list and the holding key's rank. "keys resolved" (already printed) stays |
| first loss in every other run of the arm group | none (frozen loss trace) | keep; take it from the frozen trace only, never from any coder's codes of those runs' cases. Per run: the step, sub-code and checkpoint of the first loss, and whether the value passed this case's step at this case's checkpoint (amendment line 364). As recommended (Section 7, point 14), every run of the system is shown, labelled by arm group |
| RAG's outcome | none (frozen RAG runs) | keep. Per RAG run: whether a credited answer cited a chunk containing a gold line (amendment line 363) |
| the register checklist | none | keep, for the author. Take it from the extract (Section 1): the boundary's sheet with its item ids, as the extract carries it. Decision sheet B22 asks that the page checklist be built from the same text, so that the author, V4 and the pre-coder see one text; and the signed sheets still carry run counts and mapping quotes (Section 6.4), which the page must not carry (amendment line 402). The pre-coder takes every checklist from the extract, which the prompt says governs (Part A4). Changed in the pre-tag pass, 28 October 2026: before, "the signed sheet, unchanged" |

### 6.3 Must never be on a page

- Any Step 2 output: gate pass or fail, the first differing event, oracle transitions (R, E+R, E+R\*), R-hint or R-resolver, the reviewer ceiling, the offline reading analysis, the A2 gate, leave-one-out results.
- Any Step 2b output: probe outputs, k and k0, cut sizes, whether a gold-holding key is in the cut, probe adjudication batches.
- Any Step 2c output: WD or fresh A1 runs, their carried counts.
- The V4 audit's labels and v2.
- Any coder's codes: pilot codes, author pass 1 or 2, V4, other model pre-codes.
- The "already read" flag of the coverage disclosure (amendment line 313).
- The loss trace's defect flags (recommended; Section 7, point 4).

### 6.4 What the other two inputs must not contain

- `{SUBCAUSES}`: names, boundaries, definitions and the candidate cause each falls under (amendment line 380). No counts, case ids, examples taken from coded cases or the pilot, or results. A pilot case can be the same value as a sampled case in another run, so a pilot example would carry another coder's code of a related case.
- `{REGISTER_SHEET}` (filled at signing): the pre-coder extract of Section 1 only. That is the signed sheets, with the 94c049d paragraph texts, conformance requirements and implementation entries they name. No results, run counts, incidence counts or reports; no item of the amendment's "Already read" list (lines 33-63); no quote of the probe mapping (lines 271-281); no pointer to the register's decisions. Parameter values stay (amendment line 107). Blindness check 7 (Section 5) tests this. The bug list's rows mix specification with results (for example `22-bug-list.md:195` reports re-scoring figures), so bug text enters only through Part F of the prompt, verbatim from the code.
- The register sheets as reviewed on 27 October 2026 (the register's section "Register sheets per caused-at boundary") do not meet this rule unchanged. The extract leaves these figures and the mapping quote out (Section 1; blindness check 7, 28 October 2026). The signed sheets still carry them, so the page's checklist is taken from the extract (Section 6.2). Examples: on sheet S, "Only 313 of 534 a2_r1 claims carry a recorded verdict (S.6)." (the same figure as amendment line 54, on the "Already read" list); on sheet K2, "behind 41 of the 42 rule-based merges in a0_r1 and 38 of 38 in a1_r2"; on sheet E, the quote of amendment line 272 (the probe mapping). Section 7, points 17 and 18.

## 7. Open points (decisions for the author)

Each needs the author's judgement before signing. The template is written for the recommended option. Where another option is chosen, the parts named in the point change, and so do both hashes (Section 1). Points 1 to 15 are the builder's decision list of 27 October 2026, copied here with their options and recommendations. The review of 27 October added points 16 to 21 and widened point 14. The completion pass of 27 October added points 22 to 24. Points 22 and 23 followed decisions of other package files (decision sheet A11 and B25) and are done (second review, 27 October 2026).

1. **The pre-coder model.**
   - (a) `claude-opus-5-5`. It is the model recorded in the loss-trace adjudicator transcripts (wf_0db6eaa4, wf_c00c1888), and the one used for the stance correction (`17-human-studies.md:23`).
   - (b) A different Claude model, so that the pre-codes do not share a model with the v1 adjudications that fix each case's surfacing step.
   - Recommendation: (a), as R5 proposes. Disclose that the surfacing steps (v1 adjudications) and the pre-codes come from the same model. Record the served model id for every call.
2. **The channel that meets R2-R4** (page only, no tools, no memory or result reports).
   - (a) A Claude Code workflow subagent, as used for the adjudications. It fails as recorded (R4): the memory attachment, the session context with git status, and tool calls.
   - (b) A workflow subagent started from a session in a clean directory outside the repository. Each recorded transcript is audited for memory or instruction attachments and tool calls.
   - (c) The Anthropic Messages API: one user message, no system prompt, no tools. It is clean but paid, against the amendment's "$0 API" for Step 3 (line 583), and needs its own estimate.
   - (d) Fresh claude.ai chats with memory off. This is manual and impractical for 200+ cases.
   - Recommendation: (b), with the per-call transcript audit as the gate (blindness check 4). Fall back to (c) on its own estimate and go-ahead if any audited call shows memory, instruction files or a tool call. Do not assume that a clean directory removes the memory attachment; show it in the transcripts. The list of channel attachments that check 4 allows is fixed with this choice.
3. **Arm and series stated on the Step 3 page.**
   - (a) State them explicitly: A0, A1, A2, A1-ref or final configuration, and EL2020 or ES2009.
   - (b) Leave them implicit: the meeting names and the arm-group line reveal them partly.
   - Recommendation: (a). The held rule, the oracle and leave-one-out applicability, and the recoverability arm group all need the arm. The arm is not a sealed output.
4. **Loss-trace defect flags on A0 pages.**
   - (a) Withhold them from the page, and compare them with the pre-codes' `phase_b_bug` afterwards.
   - (b) Show them.
   - Recommendation: (a). The model's Phase B attribution then stays independent of the flags, and the two can be compared.
5. **The fifth checklist status, "not ruled out: no output".**
   - (a) Adopt it, for an alternative that applies but for which no sealed output will ever exist: probes on A0; probes (ii) and (iii) and the oracles on ES2009; WD on ES2009 without WD.
   - (b) Use only the four statuses, and mark these "pending".
   - Recommendation: (a). "Pending" would promise an output that never comes. The burden rule (line 338) already makes such alternatives not ruled out.
6. **The applicability table C2: which sealed outputs exist for which case.** Confirm or amend three readings:
   - (1) the offline reading check covers EL2020 `key_reached` cases in all arms, A0 and A2 included (line 216 names no arm);
   - (2) the routing-probe population is the cases where the page shows a misfiled carrier or rival;
   - (3) all four A2 leave-one-outs are pending for every EL2020 A2 case surfaced at or before status.
   - Recommendation: confirm as written. A mismatch with the probe build only turns an item into "no output" at the reveal, which the reveal rules already handle.
7. **How "held: conflict decision" is recorded.**
   - (a) A separate field, `held` = "conflict decision", with `class` forced to "unclear" by the schema.
   - (b) A ninth class string, mapped to unclear for kappa.
   - Recommendation: (a). The eight-label kappa then needs no mapping, and the held tally stays visible.
8. **Key definitions on the Step 3 page.**
   - (a) The key history shows each involved key's registered definition at the time (carrier and rival keys).
   - (b) Key names only.
   - Recommendation: (a). The routing rule (line 375) turns on whether a claim's matter fits the key's definition. Without definitions, most routing cases become "path unclear".
9. **D4's scalar-concept passage (line 355).** **Done** (pre-tag pass, 28 October 2026): decision sheet C17 adopts (a), D4.p5. The register now tags D4.p5's scalar sentence (C) in E.2, as in K2.2 and R.2, and sheet E lists D4.p5 whole for WD cases. The prompt and check 6 follow it. The text below is kept as the point was put. Confirm that it is D4.p5 in `23-am1-design-text-94c049d.md` (the paragraph with "The September defaults favour scalar concept generation"), or name another paragraph.
   - Recommendation: confirm D4.p5. The extract carries its text under sheet E (Section 1).
10. **Does the author see the model pre-codes before pass 1?**
    - (a) Sealed (hashed) until pass 1 is committed.
    - (b) Visible as an aid during pass 1.
    - Recommendation: (a). The amendment calls pass 1 blind. The pre-codes stay a third, independent coding, usable in the agreement measures, the copy check and the 0.40 design-limit rule (amendment line 430), only if the author has not seen them.
11. **Which A0 cases are pre-coded.**
    - (a) All lost cases of the three A0 runs.
    - (b) The first 30 lost cases per A0 run in sha256(run_id|fact_id|k) order, as for A1 and A2.
    - Recommendation: (a). The cost is low through a subagent channel, and A0's bound-rule shares come only from these pre-codes (line 459).
12. **Does the frozen sub-cause list cover non-implementation classes?** **Done** (pre-tag pass, 28 October 2026): decision sheet B18 adds "not applicable" before the hash is recorded, since the pilot list is not known at signing. E7, the schema and check 7 allow it only for a class other than implementation defect and unclear. Both hashes changed. The text below is kept as the point was put.
    - (a) The pilot list gives sub-causes for every class.
    - (b) It lists implementation causes only, and the schema adds "not applicable" for the other classes.
    - Recommendation: (a). Otherwise add "not applicable" before signing, because "none fits" feeds 3b's share of cases that fit no sub-cause (line 305). Adding it changes the prompt hash.
13. **Where the Phase B bug descriptions live.**
    - (a) Part F of the prompt: the verbatim code summaries at 3320375, free of results.
    - (b) The register sheets.
    - (c) Both.
    - Recommendation: (a). Text taken from `22-bug-list.md` would bring result figures (for example its line 195). Decide before signing; moving it changes the prompt hash.
14. **Runs shown for recoverability** (widened by review finding PT-9).
    - (a) The page shows the first loss only for the arm group, as amendment line 395 lists.
    - (b) It shows every run of the system, labelled by arm group, so that the check of line 365 ("A value every run of both systems misses") can be applied. Per run it gives the step, sub-code and checkpoint of the first loss, and whether the value passed the case's step at the case's checkpoint.
    - In both options: the RAG line gives, per RAG run, whether a credited answer cited a chunk containing a gold line (line 363); and `other_run_bar` uses only the arm group, A1 with A0 and A2 alone (line 364).
    - Recommendation: (b). The template is written for it (A4, E8, Section 6.2). The extra runs serve line 365 only. Under (a), the validator sets `evaluation_defect_candidate` from the frozen trace instead, and A4 and E8 change.
15. **Pre-codes after a codebook revision.**
    - (a) Re-run all pre-codes with the revised sub-cause list, and keep both sets hashed.
    - (b) Keep the original pre-codes.
    - Recommendation: (a). The template is unchanged; only `{SUBCAUSES}` differs. The copy check, the candidate causes (line 406) and the 0.40 design-limit rule (line 430) then use pre-codes under the same codebook as the codes they are compared with.
16. **How the register sheets reach the pre-coder** (PT-1). **Done** (pre-tag pass, 28 October 2026): decision sheet B21 adopts (a). The extract is `23-am1-precoder-extract.md`, built as Section 1 says; its hash and the filled prompt's are in Section 1. The text below is kept as the point was put. The sheets as reviewed name 94c049d paragraphs, conformance requirements and implementation entries by id and section pointer only. They quote one 94c049d fragment. The pre-coder needs the texts to quote a design ground and to apply the checklist.
    - (a) A fixed pre-coder extract (Section 1): the five sheets, each followed by the verbatim text of every 94c049d paragraph it names and of every conformance requirement and implementation entry it points to, with an item id on every checklist item. It is filled into the template at signing, and the template's hash covers it. Amendment line 402 then holds as worded: the sub-cause list stays the only added input.
    - (b) The same extract, appended by the page builder to every case page. Amendment line 326 ("quoted on the case page") reads most directly this way, and the author would see the same text. The `{REGISTER_SHEET}` slot and its block in Part H are then removed, and A4, Part B's terms and E5 point to the page.
    - Not offered: passing the whole register. It carries run counts and an "Already read" figure (its section S.6 gloss on `filing_support_check`), against Section 6.4 and amendment line 402.
    - In both options: every checklist item carries an id, so validation check 4 is mechanical; an architectural ground comes only from the caused-at sheet's (C) list, a trade-off ground only from its (B) list, and a WD case's ground only from D4.p5 (E6, Part G, validation check 6). These parts are already in the template.
    - Recommendation: (a). The pre-coder's quote is then checked against a fixed, hashed text. If line 326 is read as requiring the text on the page itself, choose (b).
17. **Decision pointers in the sheets** (PT-3). **Done** (pre-tag pass, 28 October 2026): decision sheet B22 adopts (a). The register's pre-tag edit wrote every signed reading into the sheets and the entries they point to, and blindness check 7 finds no pointer in the extract (Section 5). The text below is kept as the point was put. The sheets point to the register's "Decisions for the author", which is not an input to the prompt. On the sheets as reviewed, the pointers are to decisions 1 (criterion (ii) on the hint path), 2 (disclosed limitations as design grounds), 3 (bug 5's ground), 4 (bug 3's rule), 5 (harness-side code), 6 (the grounding pass), 13 (unlisted implementation entries), 15 (criterion (ii) and retrospective entries), 16 (the expansion generator) and 17 (what D4.p3's values means). Each changes whether an item counts or a design ground exists.
    - (a) Resolve every pointer by the signed reading before hashing. Preferably do it in the signed register sheets themselves: the page's checklist (amendment line 397) then matches the pre-coder's, and "the signed sheet, unchanged" (Section 6.2) stays true. Blindness check 7 scans for "decision" or "decisions" followed by a number.
    - (b) Append a fixed block with the signed outcomes of the register's decisions 1 to 17 to the extract, and let the pre-coder apply them.
    - Recommendation: (a). The pre-coder should not apply conditionals.
18. **Counts and mapping quotes in the sheets** (PT-5). **Done** (pre-tag pass, 28 October 2026): decision sheet A19 settles (a). The extract leaves out every run count, incidence figure and mapping quote, and keeps the parameter values; blindness check 7 records the hand check (Section 5). The text below is kept as the point was put. The sheets as reviewed carry run counts and incidence figures (Section 6.4 gives examples), one of them on the amendment's "Already read" list (line 54). They also quote six lines of the probe mapping (lines 272, 273, 276, 277, 278 and 279).
    - (a) Build the extract without run counts, "Already read" items or mapping quotes, and keep the parameter values (amendment line 107). Blindness check 7 lists every numeral for a hand check, and scans for lines 271-281.
    - (b) Keep the sheets as they are, and correct Sections 3 and 6.4 to disclose what enters.
    - Recommendation: (a). Section 6.4 already forbids incidence counts, and one figure is on the "Already read" list.
19. **The burden for evaluation-defect and transcript cases** (PT-4). Amendment line 334's burden names five classes and leaves out evaluation defect. Line 338 makes a probe-type alternative "not ruled out" only where "it is on the checklist for the caused-at boundary". The earlier draft let the items of the surfacing step's home sheet gate every class. An A0 case caused at evaluation could then become unclear, and a counting home-sheet item gave a class that the schema rejects with caused-at evaluation.
    - (a) Align with lines 334 and 338, as the template now does. Evaluation defect is decided before the checklist (E6 step 2). Only items on the caused-at sheet can make a case unclear for lack of output (C3; E6 steps 4-5). A counting item on another sheet sends the coder back to caused-at (E6 step 1).
    - (b) Keep the stricter rule of the earlier draft. The amendment is final, so this needs a dated note to it (amendment line 16); a template gloss cannot carry it.
    - Recommendation: (a).
20. **A0 cases resting on a Phase B bug whose design ground is retrospective** (PT-6). Line 309: "A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound." Line 348 codes a case whose only design ground is retrospective as implementation choice only where an alternative meets (i)-(iv), and as unclear otherwise. For bug 3 under the register's decision 4 (b), and bug 5 under its decision 3 (b), the two rules give different codes.
    - (a) Line 309 takes precedence for A0. The case is implementation defect with basis "Phase B bug" (E6 step 3, Part F, the schema).
    - (b) Line 348 applies first. Such a case is unclear unless an alternative consistent with the 94c049d text meets (ii) or (iii).
    - Recommendation: (a). Line 309 is the A0-specific rule. The register takes the same position for bug 5 (its decision 3): "For A0 the Phase B rule applies either way."
21. **"Cases with no pending alternative" in the agreement measures** (PT-10; amendment line 428). Under E3 and C2, nearly every EL2020 case has a pending entry: the oracle row result (A0, A1) or the four leave-one-outs (A2) are pending for every case surfaced at or before status.
    - (a) A pending alternative is a `pending` entry whose `sets` is not "caused-at". The oracle row result and the leave-one-outs, which set only caused-at, do not count.
    - (b) Any `pending` entry counts. Line 341 lists the oracle and leave-one-out results among the sealed outputs. The population is then the cases surfaced at `in_payload` or `answered`, plus oracle exceptions. In the frozen `23-loss-trace.json` (strict bound; the first 30 lost cases per A1 and A2 run in hash order, as amendment line 308 samples them), 8 of the 180 cases surface at those two steps (computed 27 October 2026).
    - Recommendation: report (a) as the primary measure, for statistical power, and (b) beside it, for purity. Section 4 is written so.
22. **Probe (i) on `admitted:span_not_seen` cases** (cross-package check X7). Depends on the probe note's decision PN-8 (decision sheet A11). **Done** (second review, 27 October 2026): decision sheet A11 settles PN-8 as (a), "listed apart, with no probe output", so C2 now excepts `admitted:ignored` and `admitted:span_not_seen` from probe (i). The prompt hash changed; the schema did not. The text below is kept as the point was put.
    - C2 gave probes (i)(b) to (i)(d) to every case surfaced at `admitted` in the probed runs (EL2020 A1 and A2; the author-coded ES2009 run), except `admitted:ignored`. So a `span_not_seen` case listed them as pending.
    - Amendment line 241 excepts only `admitted:ignored` cases, and re-extracts "the cited span"; its control is "the recorded prompt" (line 242). The probe note: "They have no recorded extraction call on a cited span" (`23-am1-probe-note.md:311`).
    - PN-8 (a), "list them apart, no probe": C2 also excepts `admitted:span_not_seen`. The probe-type items of such a case are then "not ruled out: no output" (C3), so its pre-code is unclear unless an item counts. The prompt hash changes; the schema does not.
    - PN-8 (b), "probe a neighbouring span": C2 stands, and C1's probe (i) lines say which span is re-extracted for these cases. The prompt hash changes.
23. **The audit list in blindness check 1** (cross-package check X10). Depends on the audit-list script's decision AL-7 (decision sheet B25). **Done** (second review, 27 October 2026): decision sheet B25 adopts option (a) and the naming, so check 1 now names `23-am1-audit-list.json` among the files that fail. Section 5 changed; the prompt and both hashes did not. The text below is kept as the point was put.
    - Check 1 (Section 5) admits a data file whose hash matches "the amendment's frozen-input table, the run manifest, or the signed register files", and fails "any audit or v2 file".
    - AL-7 asks where the audit list's hash is recorded: (a) "the signing commit message and the annotation of the tag" `plan23-amendment-1` (`23-am1-audit-list.py:179-180`), or (b) "a signing note next to the frozen-input table." (`23-am1-audit-list.py:181`). On check 1 it says: "That would admit a file whose roles encode the v1 labels." (`23-am1-audit-list.py:185`).
    - Under either option, check 1 names the audit list (`23-am1-audit-list.json`) among the files that fail, as decision sheet B25 adopts. Under (b) this is needed, since a note next to the frozen-input table could be read as part of it. Section 5 changes; the prompt and both hashes do not.
24. **"candidate generation" and the rule for an LLM step with no model condition** (raised by this pass, from cross-package check X6). **Done** (pre-tag pass, 28 October 2026): decision sheet C62 adopts (b), with its second item (i). Sheet K2 now names candidate generation beside the resolver; A5, Part G and the schema add the step to the steps where line 340's argument is required and "design or model, not separated" is allowed. The gatekeeper rule stays as written. Both hashes changed. The text below is kept as the point was put.
    - The register's K2.1 Chain line marks "candidate generation (LLM)". No probe gives it a model condition. Amendment line 251: "Expansion-routed misfilings (the resolver returned no key, and expansion reused or created one) are not probed."
    - Amendment line 340 sets the rule "At an LLM step with no model condition", and line 331 names "routing" among the boundaries with such steps. Sheet K2 names only the resolver: "for the resolver, the condition of line 340 applies."
    - (a) As the sheets: the rule and the class "design or model, not separated" do not apply at "candidate generation". The template is written so (A5; the schema).
    - (b) As the amendment's wording: they apply there too. Sheet K2 then names the step (a register edit), and A5 and the schema add it. Both hashes change.
    - Recommendation: (b), unless the register records why the step is left out. Few codes move, since line 251 codes expansion-routed misfilings "under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry". Unlike the other points, the template follows the sheets here until they change.

**A consequence to note (not a decision).** No probe runs on A0 (amendment line 238). Under the burden rule (amendment line 338), an A0 case whose caused-at boundary has an applicable probe-type alternative is therefore "not ruled out: no output", and its pre-code is unclear unless a Phase B bug, criterion (ii) or (iii), or conformance applies. Few Phase B bugs act at extraction or routing, so A0 pre-codes there will mostly be unclear by construction. A0's shares in the bound rule come from these pre-codes (amendment line 459).

## Review record (27 October 2026)

**Workflow:** am1-step0-verify. A reviewer read this file against the amendment, the register and the run records ("pre-coder template" lens). A skeptic tried to refute each finding and failed for all twelve (PT-1 to PT-12); where it gave a better fix, that fix was applied. A fixer then edited this file only. The amendment, the register and the other package files were not changed.

**Findings and what was done:**
- **PT-1** (major; the sheets carry ids, not the texts the pre-coder must quote). Applied in part. The form of the extract is a decision for the author (Section 7, point 16; recommended: filled into the template at signing). Applied in every option: the extract's content and item ids (Section 1); Part B's terms; E6 step 6, Part G and validation check 6 (architectural grounds only from the caused-at sheet's (C) list, trade-off grounds only from its (B) list, a WD case only from D4.p5); validation checks 3 and 4; `item_id` in the schema's checklist entries.
- **PT-2** (major; the empty-sheet branch is always taken). Applied. The conditional and the prompt line on an empty block are removed. `{REGISTER_SHEET}` is filled once, at signing, so it is not a run-time input (amendment line 402). The page keeps its own checklist, and the prompt says the five sheets govern (A4; Section 6.2). Both hashes were recomputed.
- **PT-3** (major; the sheets point to unsigned register decisions). Not decided here: Section 7, point 17 (recommended: resolve every pointer before hashing, preferably in the signed sheets). Written for the recommended option: Section 1, Section 6.4, and blindness check 7 (scan for "decision" followed by a number). Decision 2 and the other pointers found on the sheets are listed.
- **PT-4** (major; home-sheet items gated evaluation defect). Applied for the alignment with amendment lines 334 and 338 (C3, last bullet; E5 statuses; E6 steps 1, 2, 4 and 5). The stricter alternative is Section 7, point 19, as a dated-note route, since the amendment is final.
- **PT-5** (minor; the sheets carry counts and mapping quotes). Not decided here: Section 7, point 18 (recommended: an extract without counts, "Already read" items or mapping quotes, parameter values kept). Section 3 and Section 6.4 now state that the claims hold only for an extract built so; blindness check 7 tests it.
- **PT-6** (minor; an A0 Phase B case could be coded two ways). Applied: E6 step 3; Part F; the basis "Phase B bug" in the schema, allowed only with arm A0 and a bug number, with no criteria, and the only basis allowed with `phase_b_bug` set; Part G; Section 4. The precedence of line 309 over line 348 for A0 is Section 7, point 20.
- **PT-7** (minor; "counts" lacked the "rests on" link). Applied: E5's "counts" now requires that the page shows the case's loss rests on the entry, for conformance too; the evidence must come from the page and show the case's own link. The schema requires the page as source for a counting item.
- **PT-8** (minor; the line-340 condition was keyed on the boundary only). Applied, with the skeptic's correction. Prompt Part A5 lists the step names per boundary with their type, from the register's Chain lines; `caused_at_step` is an enum, tied to its boundary and to `caused_at_is_llm_step`. The argument of line 340 is required at key assignment, key resolution and reading (amendment line 331 names routing and reading as a whole), and at the gatekeeper and the A2 support check. "Design or model, not separated" is allowed only there, so it is forbidden at the extractor. Its earlier requirement `caused_at_is_llm_step` = true was dropped: under the whole-boundary reading, a deterministic routing or reading step needs the argument, and a case that fails it must be able to take that class. Consequential edit: A1's reading line now follows the register's section R.1 (the answer is built by deterministic templates; the grounding pass is the LLM step).
- **PT-9** (minor; the recoverability fields did not follow amendment lines 363-365). Applied: E8 defines the three fields; A4 and Section 6.2 require the per-run detail. The choice of runs shown is Section 7, point 14, now with both options.
- **PT-10** (minor; "no pending alternative" had an almost empty population). Not decided here: Section 7, point 21 (recommended: (a) as primary, (b) beside it). Section 4 is written so. The figure for (b), 8 of 180 sampled cases at `in_payload` or `answered`, was recomputed from the frozen `23-loss-trace.json`.
- **PT-11** (minor; Section 5 statements and checks). Applied: the tool-call count corrected to 11 Bash calls and one StructuredOutput call; the `session_context` (git status), `environment`, `skill_listing` and `date` attachments added to R4's list; blindness check 4 restated with an allowed-attachment list fixed with the channel (Section 7, point 2); check 1 restated to compare each run's concatenated hash with the run manifest, and to pin code by hash; R6 records "none exposed" where the channel exposes no settings.
- **PT-12** (minor; the open points had titles only). Applied: Section 7 now gives all fifteen of the builder's decisions with options and recommendations, and points 16 to 21 for the decisions raised by PT-1, PT-3, PT-4, PT-5, PT-6 and PT-10.

**Checks after the fixes** (27 October 2026; working files in the session scratchpad, folder `step0/verify/pt/`, not part of the package):
- Prompt and schema hashes recomputed (Section 1).
- The schema was tested on 51 sample records with a subset validator; all validated or failed as intended. No third-party validator was available.
- The verbatim parts of the prompt were compared with their sources again: Part B's table and Part D with the amendment (0 lines differ); the contract and bug summaries with `app/core/cycle2_flags.py` at 3320375; the sub-codes with `23-loss-trace.md` lines 34-45; the step chain with `23-loss-trace.py`. All match. Each placeholder occurs once.
- Every quote and line reference added by the fixes was checked against its source: the amendment (working tree, draft 5), the register (working tree at 14:22 on 27 October), `23-am1-design-text-94c049d.md`, and the adjudicator transcript. The names in Part A5 equal the schema's step enum, and its LLM steps equal the schema's LLM list.
- This file cites the register by section, not by line, because the register was being edited by another fixer during this pass. The quotes taken from it were still present at the end of the pass.

**Cross-package consistency pass (27 October 2026).** Edits outside the prompt block only; the prompt and schema hashes of Section 1 are unchanged (recomputed).
- Section 1 and Section 7, point 17: the decision pointers on the register sheets now include decisions 5 (sheet S) and 17 (sheets K1 and K2), which the register gained during the same review; point 17 (b) reads "decisions 1 to 17".
- Section 5, blindness check 7, and point 17 (a): the scan also covers the plural "decisions", which sheet S uses.
- Conventions: lines of `22-bug-list.md` are stated to be working-tree lines (its line 195 does not exist at the committed version).

**Completion pass (27 October 2026).** Fixes from the cross-package check of 27 October (X5, X6, X12), the probe-note renaming and the "Already read" range. This file only; the amendment, the register, the probe note, the decision sheet and the other package files were not changed. The prompt and the schema changed, and both hashes were recomputed (Section 1).
- **X5, step names.** Every step name now follows the register verbatim: the Chain lines of its sections A.1, E.1, K1.1, K2.1, S.1 and R.1, and, for the two A2 contracts that the S.1 Chain line does not name, sheet S's list of A2's contracts.
  - Renamed: "extractor" to "extraction"; "key hint" to "the `state_key_hint` field of the extraction call"; "hint filing" to "the hint becomes the claim's key"; "conflict evaluation and resolution engine" to "conflict evaluation and the resolution engine"; "A2 type check" to "type check"; "A2 same-meeting conflict and new-evidence rules" to "same-meeting conflict and new-evidence rules"; "A2 support check" to "support check" (S.1: "A2 adds the support check (LLM, system)"). A5 marks the three A2 steps "A2 only".
  - Removed: "shortlist and pruning". The K2.1 Chain line has no such step; K2.1 lists "the embedding shortlist and prompt pruning" among the deterministic parts. A loss resting on it is decided by sealed outputs (Section 3, row A5).
  - Where: A1, rewritten to name the steps in quotes; the Terms line on a claim's path; A5; Part G; the schema (the `caused_at_step` enum, the per-boundary enums, the LLM and deterministic lists, and the two rules under X6); Section 3, rows A1 and A5. A3 keeps "went to the extractor", which is verbatim from `23-loss-trace.py`. The review record above keeps the old names as history.
- **X6, the scope of the line-340 condition.** The condition and the class "design or model, not separated" now apply per step, only at the six LLM steps the sheets name: the "gatekeeper" (sheet E, cause 4), "the `state_key_hint` field of the extraction call" (sheet K1), the "resolver" (sheet K2), the "support check" (sheet S), "question resolution" and "grounding" (sheet R). Before, A5, E6 (through A5) and the schema applied them to every step of key assignment at extraction, key resolution and expansion, and reading, deterministic steps included. This reverses the whole-boundary reading recorded under PT-8.
  - A5 quotes amendment line 331 (as Part B gives it) and line 340 (as Part D gives it). Section 3, row A5, quotes both with their line numbers, and the five sheet sentences.
  - Schema: one rule requires `llm_step_argument` for architectural weakness or a trade-off at the six steps; "design or model, not separated" requires `caused_at_step` to be one of them. Part G's note on `llm_step_argument` says the same.
  - Reported, not resolved: the K2.1 Chain line marks "candidate generation (LLM)", and no probe gives that step a model condition (amendment line 251: expansion-routed misfilings "are not probed"). Line 340 covers it by its wording; sheet K2 names only the resolver. The template follows the sheets, and the sheets were not changed. Section 7, point 24.
  - Also noted: sheet R says "question routing" where the R.1 Chain line says "question resolution". A5 uses the Chain name (Section 3, row A5).
- **X12, the harness reviewer.** A1 said the reviewer "accepts or rejects new keys". It now follows the register's K2.6c: "A rejected proposal is only recorded; under `quality` no reject is submitted". A1 states no run result, so the register's log finding that no proposal was rejected is not in the prompt.
- **Probe-note decisions renamed PN-1 to PN-14.** This file had no reference to the probe note's decisions D1 to D14 (checked by search). The new point 22 cites PN-8. References to Ch. 4 decisions (D4, D4.p5, D5) are unchanged.
- **"Already read" range.** The amendment's block runs from its heading at line 33 to line 63, the last line of its item on the fact reports and review rounds. This file's "lines 33-63" (Sections 1, 3 and 6.4) is correct and unchanged.
- **X7 and X10.** Not resolved. Neither was listed before. Section 7 now lists them as point 22 (probe (i) on `admitted:span_not_seen`, dependent on PN-8) and point 23 (the audit list in blindness check 1, dependent on AL-7). The decision sheet's sources name the template's points 1 to 21 only, so points 22 to 24 are not yet on it.
- **Checks** (working files in the session scratchpad, folder `step0/complete/`, not part of the package):
  - Hashes recomputed with the same script as before: prompt `f54c1292…` (59,260 characters), schema `0f6d1bb5…` (Section 1).
  - The verbatim check of the prompt passes as before: Part B and Part D, 0 lines differ from the amendment; the contract and bug summaries match `app/core/cycle2_flags.py` at 3320375; the sub-codes and the step chain match their sources; each placeholder occurs once.
  - The schema test was rerun with the new step names and 20 more records, 71 in all: the rule at each kind of step, and the old names rejected. Two expectations changed with X6: architectural weakness at the "harness reviewer" with no argument is now valid, and "design or model, not separated" there is now invalid. All 71 validated or failed as intended.
  - A names check: A5's names equal the schema's step enum, per boundary and in order; A5's LLM and deterministic marks equal the schema's two lists; A5's six steps equal the lists of the schema's two rules; every name occurs verbatim in a Chain line or, for the two A2 contracts, on sheet S. Every quote added in this pass occurs in its source: amendment lines 251, 331 and 340; the register's A.6, K2.6c and sheets E, K1, K2, S and R; `23-am1-audit-list.py:179-185`; `23-am1-probe-note.md:309`.
- **Review of the completion pass** (27 October 2026; workflow review of the Step 0 package, findings MX-F1 to MX-F11; this file has MX-F3, MX-F7 and MX-F8). Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. This file only; the probe note's findings are recorded there.
  - **MX-F3** (point 22 cited the probe note at :309). Applied. Point 22 now cites `23-am1-probe-note.md:311`. The check record above is left as written. The probe note's completion pass moved the quoted sentence from line 309 to 311; point 22 now cites :311 (checked 27 October 2026). The probe note's later edits of this review are all below line 311.
  - **MX-F7** (A5 dropped the arm mark of "settle"). Applied, with other words than the finding's. A5 now reads "settle" (deterministic, not in A0: it is the bug-13 repair of Part F). "A1 and A2 only" would exclude A1-ref and the final configuration, which run the settle: Part F says "A1, A2 and the later arms run with these repairs on". The S.1 Chain line, "settle (A1, A2; deterministic, harness)", names the two EL2020 arms that have it. Section 4 gains validation check 9 (outside the prompt): no "settle" on A0, and no "type check", "same-meeting conflict and new-evidence rules" or "support check" on A0 or A1. The A2 steps are included because A5 marks them in the same way. Section 3, row A5, gives the source of the arm marks. The prompt hash changed; the schema did not change for this finding.
  - **MX-F8** (the schema allowed "design or model, not separated" at the "gatekeeper" for any surfacing step). Applied in the schema, as the better fix's first option. (1) "Design or model, not separated" with `caused_at_step` "gatekeeper" requires `surfaced_at` step "admitted" and sub-code "ignored". (2) The `llm_step_argument` rule is split. The five other steps keep it as before. The "gatekeeper" requires the argument only for `admitted:ignored` cases. This matches A5 ("the "gatekeeper" (for `admitted:ignored` cases)"), amendment line 331, and sheet E, cause 4 ("Only for `admitted:ignored` cases"). Both hashes changed.
  - **Checks** (working files in the session scratchpad, folder `step0/complete/`: `check_schema4.py` and `names_check2.py`, not part of the package):
    - Hashes recomputed with `step0/verify/pt/hashes.py`: prompt `52faa1a7…` (60,033 characters), schema `e790d1a6…` (Section 1).
    - `step0/verify/pt/vq.py` passes as before: Part B and Part D, 0 lines differ from the amendment; the contract and bug summaries match `app/core/cycle2_flags.py` at 3320375 (the scratch copy equals `git show 3320375:app/core/cycle2_flags.py`); the sub-codes and the step chain match their sources; each placeholder occurs once.
    - The schema test has 79 records, all as intended. Two expectations changed with MX-F8: architectural weakness at the "gatekeeper" with no argument is now valid for a case surfaced at `carried`, and "design or model, not separated" at the "gatekeeper" is now invalid there. Eight records were added: the gatekeeper rules at `admitted:ignored`, at `admitted:span_not_seen` and at `filed`, a trade-off at the gatekeeper, and the class at the "resolver" with no surfacing condition. Six more records, all valid under the schema, test check 9: each passed or failed it as intended.
    - The names check passes: A5's names equal the schema's step enum, per boundary and in order; A5's LLM and deterministic marks equal the schema's two lists; A5's six steps equal the union of the two argument rules and the list of the class rule. The S.1 Chain line has "settle (A1, A2; deterministic, harness)".
- **Second review** (27 October 2026; second review round of the Step 0 package; this file has finding R2-5 and the two pre-tag edits X7 and X10 that decision sheet C1 lists). Only defects were applied. Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. This file only; the probe note's findings (R2-OWN-1 to R2-OWN-3) are recorded there.
  - **R2-5** (A5 marked the three contract steps "A2 only", although the final configuration, which item 3 also pre-codes, carries each admitted contract). Applied, as the better fix, with each step's contract named so that "the contract" is not left to a guess for the step that covers two contracts. A5 now marks "type check", "same-meeting conflict and new-evidence rules" and "support check" as in A2, and in the final configuration where the page states that the step's contract (`filing_type_check`; `resolution_same_meeting_conflict` or `supersession_requires_new_evidence`; `filing_support_check`) was admitted. Section 3, row A5, gives the sources: sheet S's list of A2's contracts, the register's X.4 table, and amendment lines 533-534. Validation check 9 now also excludes the three steps on A1-ref, which runs no contract (amendment line 533; the finding cited line 532, but the A1-ref item is on line 533). For the final configuration, check 9 tests none of the three steps, as the page states which contracts were admitted. The prompt hash changed; the schema did not. Not applied here: the decision sheet's B26 (`23-am1-decisions.md:668-670`) still says that A5 marks the three steps "A2 only" and that check 9 "covers both marks". This file may not edit the sheet, so it is left for the author.
  - **X7** (decision sheet C1; Section 7, point 22). Applied: C2 now excepts `admitted:ignored` and `admitted:span_not_seen` from probe (i), as decision sheet A11 settles the probe note's PN-8 ("listed apart, with no probe output"). Section 3, row C2, gives the source (`23-am1-probe-note.md:311`). Point 22 is marked done. The prompt hash changed; the schema did not.
  - **X10** (decision sheet C1; Section 7, point 23). Applied: blindness check 1 now names `23-am1-audit-list.json` among the files that fail, as decision sheet B25 adopts. Point 23 is marked done. Section 5 changed; the prompt and schema did not.
  - Left as written, as history: the completion pass's X7-and-X10 entry ("Not resolved."), its X5 entry, which records the earlier mark "A2 only", and the MX-F7 entry, which records check 9 "on A0 or A1".
  - **Checks** (working files in the session scratchpad, folder `step0/reverify/`, not part of the package):
    - Hashes recomputed with `step0/verify/pt/hashes.py`: prompt `5345f42e…` (60,362 characters); schema `e790d1a6…`, unchanged (Section 1).
    - `step0/verify/pt/vq.py` passes, with output identical to the run before this round: Part B and Part D, 0 lines differ from the amendment; the contract and bug summaries match `app/core/cycle2_flags.py` at 3320375 (the scratch copy equals `git show 3320375:app/core/cycle2_flags.py`); the sub-codes and the step chain match their sources; each placeholder occurs once.
    - The schema test (`check_schema5.py`, the previous test with check 9 extended): the 79 schema records give the same results as before, all as intended. The check-9 records rise from 6 to 11, all schema-valid: the three contract steps on A1-ref fail check 9, and two contract steps on the final configuration pass it. All as intended.
    - The names check (`step0/complete/names_check2.py`) gives the same output as before this round, apart from the A5 state line it prints.
    - Every quote added in this round occurs in its source (`quotes_r2.py`): amendment lines 533 and 534; `23-am1-probe-note.md:311`; decision sheet A11; the register's sheet S ("Support check (`filing_support_check`)") and its X.4 rows of the four contracts. The four contract names in A5 equal those of prompt Part A2.

## 9. V4: the same prompt, run by a Gemini agent in Google Antigravity (27 October 2026, evening; rewritten 28 October 2026)

Added after the second review, for the author's decision C2: V4 is a machine coder (amendment line 116). The channel is Google Antigravity, an agent environment with file, terminal and browser tools, like Claude Code, and not a chat app. V4's agreement is disclosed as agreement with an independent machine coder, not as human inter-rater reliability (line 116). This section adds no text to the prompt and changes neither hash in Section 1. It was rewritten on 28 October 2026 after the review round on draft 6 (record at the end of this file). It follows the amendment as of that date (lines 116, 305, 310-312, 405-414, 430, 480 and 583) and decision sheet entries C64 to C67.

**What V4 receives.**
- **Cases.** The assembled prompt of Section 1, byte for byte the pre-coder's: the template with the extract filled in at signing, the frozen sub-cause list and one case page, each placed by literal replacement. `23-am1-v4.py case-packets --template T --subcauses F --pages DIR --salt S --out DIR` assembles it from the same three inputs (T the template with the extract filled in at signing, F the sub-cause list in force, S the V4 packet salt fixed at signing, B24), in salted hash order. T is not this Markdown file: `case-packets` takes the whole of T as the prompt. T is the filled prompt text of Section 1: the text of Section 2's block (the lines between `~~~~ prompt` and `~~~~`, each ending in a newline), with `{REGISTER_SHEET}` replaced, by literal replacement, with the whole content of `23-am1-precoder-extract.md`. It is generated from these two files at signing and can be regenerated at any time. Its SHA-256 must equal the filled-prompt hash recorded in Section 1; `case-packets` records it as `template_sha256` in its manifest, and the extract's own hash as `extract_sha256`. Its manifest records each packet's case id, page hash and prompt hash, and the sub-cause names. Blindness check 3 applies to every V4 case packet (AG6).
- **The channel trial** (amendment line 407). Before the first of the 180 cases, V4 codes the 20 pilot cases (line 310). They are built with `case-packets` into their own folder and run under AG1 to AG7. They count toward nothing: they enter no agreement measure. The trial shows whether the agent reads the packet, writes `answer.json` and uses no other tool. If V4's instruction has to change, the change is made to the script's `INSTRUCTION`. A dated note, written before any of the 180 is staged, gives the new text, its SHA-256, the script's new SHA-256 and the trial attempts that showed the need. The change concerns only the channel (which files and tools may be used, and where the answer goes) and adds nothing on how to code. The prompt does not change.
- **Audit.** `23-am1-v4.py audit-packets --salt S --out DIR [--batch 60]`: every decision on the audit list (amendment line 410), in packets of 60 decisions, the last one smaller, in salted hash order (S as above). Each packet opens with a header: the task, the loss trace's carry standard (checked against `23-loss-trace.md` on every run), the sentences that explain the status line, and the answer format. The status sentences say that a value rejected at every meeting that lists it is a ruled-out option, under the standard's ruled-out bullet, and that a value first listed as current or candidate and later rejected was replaced, and carries when the text states that same value, as the v1 adjudicators' bullet for demoted values said. Each item gives:
  - id;
  - fact_id;
  - the gold value;
  - its statuses in meeting order, from the `status` field of the value's gold rows in `data/ami_eval/suites/transfer_el2020.yaml` (for example `candidate after EL2020b; rejected after EL2020c, EL2020d`);
  - aliases;
  - the text;
  - its contexts: up to three, each a subject, predicate and key with a count, from every traced run, since the standard reads texts with their contexts.

  No item carries a role, a v1 label, `decides_rows` or `recorded_result_rows` (decision sheet B24).
- **The instruction.** The whole message of each conversation is the script's `INSTRUCTION`, word for word:

  > packet.txt in this folder is the message it refers to: where it says "this message", it means packet.txt. Read packet.txt and do what it asks. Its "Do not use tools" allows exactly three actions here: listing this folder, reading packet.txt, and writing your answer to answer.json in this folder. Do not read any other file, run a command, open a browser or search the web. Write to answer.json the JSON object the packet asks for and nothing else, and do not answer in the chat.

  It tells the agent that `packet.txt` is the "message" the prompt speaks of, and how the prompt's "Do not use tools" applies in this channel. Its SHA-256 is stored with every answer (`instruction_sha256`).

**The audit standard, and what V4's audit is compared with** (review finding L3-3). The standard in the packets is the text of the "Standard" bullet of `23-loss-trace.md`. It is a condensed form of what the v1 adjudicators received. Their prompts, in round 3 (workflow wf_c00c1888) and in the fixpoint round (wf_0db6eaa4), have the same bullets in substance, plus worked examples (round 3), a bullet for demoted values, a ruled-out bullet keyed on the value's kind, and a contexts bullet that says to decide by the most common context and say so. Per item, the v1 adjudicators also had the kind, the gold evidence lines, the questions asking for the value and up to four contexts, and they could read the suite, the transcripts and the run files. V4 gets the condensed standard; no evidence lines and no questions; at most three contexts; the gold statuses in meeting order, but not the kind; and no file access. The status sentences of the header stand in for the kind-keyed ruled-out bullet and the demoted-values bullet. A disagreement can therefore come from the instrument as well as from an error in v1. This is disclosed with the audit agreement (line 410), together with the partial exposure that decision sheet B24 notes: the case pages V4 codes at item 5 show steps and sub-codes that rest on v1.

**Timing** (amendment line 405; decision sheet C67).
- No V4 packet, case or audit, is staged before item 4 (author pass 1) is committed. The author, who runs V4, opens no V4 conversation or answer before then.
- The channel trial comes first, then the 180 cases. The audit packets are run after item 4 is committed and before item 7.
- V4's due date is seven days after item 4's commit (decision sheet C2 and C67, answered by the author on 28 October). It covers the channel trial, the first coding of the 180 cases and their R7 re-asks; so that re-asks fall inside it, the shared validator is run on each V4 case record right after it is collected. The calendar date is stated in a dated note when item 4 is committed. If V4's case codes are not in by then, the V4 fallback applies (amendment line 432).
- The audit, a re-run after a codebook revision and the fresh sample are due before item 7 and have no fallback of their own. An audit not done by then leaves v2 equal to v1 (line 95), and this is reported.
- V4's codes and audit labels are hashed and committed before item 7 (AG7).

**Run conditions for V4:** AG1 to AG7 (AG for Antigravity). They replace R1 to R6 and R9 for V4. R7 holds for V4, with voids, missing answers and rejected attempts counted as attempts (AG5). R8 applies to the pre-codes only; V4's timing is above.
- **AG1. Workspace.** One folder outside the repository, used for nothing else. `stage --out DIR --packet NAME --workspace WS` refuses:
  - a folder inside the repository. It compares the folder and each of its parents with the repository root by file identity (`os.path.samestat`), not by path text, so another letter case or a `/System/Volumes/Data` path is caught;
  - a folder that holds anything other than `packet.txt` and `answer.json`;
  - a folder with an open staging, whatever job folder staged it. `stage` writes a marker beside the folder, outside it (`.<folder name>.v4-staging.json` in its parent, so it needs write access there), naming the job folder, the packet and the staging; it refuses while a marker exists, and `collect` removes it only for its own staging;
  - a `packet.txt` or `answer.json` that no collected staging accounts for, for example an answer the agent wrote after `collect`. It is kept with the AG7 record and removed by hand;
  - a packet that has a staging with no collected attempt, in any folder; a packet that already has a valid attempt that was not rejected; a packet with two attempts; a packet file whose hash differs from its manifest.

  Otherwise it copies the packet in as `packet.txt` (removing only a `packet.txt` or `answer.json` left by a collected staging of the same job folder) and appends one JSON line to `DIR/staging.log`: the staging number, the packet, the packet's SHA-256, the workspace and the time.

  Staging limits what the folder holds. It does not confine the agent. Antigravity's agent runs as the author's macOS user, and a terminal or file tool could reach any file that user can read, the repository included. Blindness therefore rests on AG2 (terminal and browser execution need approval or are off), AG4 (any other tool call voids the answer) and AG7 (every conversation's tool calls are kept). The stronger option is to run Antigravity under a separate macOS user account that cannot read `~/Documents`, where the repository is; if it is used, a dated note records it. Such an account must not be able to read `~/.claude` either, which holds the session memory and transcripts. On 28 October 2026, `~/Documents` was closed to other users, but the home folder and `~/.claude` were readable by group `staff`, to which macOS users belong by default. The repository is never opened in Antigravity.
- **AG2. Conversation and settings.** One new Antigravity conversation per packet, opened on that folder. Its only message is the instruction. Terminal and browser execution are set to require approval, or off. Global and workspace rules, saved knowledge or memories, and MCP servers are empty or off, and so is any setting that carries context from earlier conversations. A dated screenshot records these settings at the start of each working session and after any Antigravity update. The Antigravity version is recorded with every answer (`collect --antigravity-version`).
- **AG3. Model.** A Gemini model, chosen explicitly in Antigravity's model picker; Antigravity also offers other families. Its picker label, with any variant or reasoning level the picker shows, and the conversation mode, if Antigravity offers one, are fixed in a dated note before the first packet, which is the first of the channel trial. Every answer is collected with the label in force (`collect --model LABEL`): the one in that note, or the last change recorded since. An answer given under any other label, or in another mode, is void: it is collected with `--void` and the label it was given under, and with `--void` the script neither checks nor updates `model.json`.
  - Each job folder has its own `DIR/model.json`, written by its first `collect`. A later `collect` there with another label is refused, unless `--model-change` is given; it appends the new label, with the time and the packets coded so far.
  - The first `collect` of a new job takes the label in force, which the author checks by hand against the AG7 record. A label change at the start of a job is recorded in a dated note, not with `--model-change`; a change during a job is recorded with `--model-change`. The packets coded after a change are reported apart.
  - For 3b, the same label is used if it is offered. Otherwise the new label is recorded, and 3b's kappa is reported as coded by a different V4 model.
- **AG4. Tools.** The agent may do three things: list the workspace folder, read `packet.txt`, and write `answer.json`. Repeated calls of these three kinds are allowed; a long packet may be read in parts. The attempt is void, mechanically:
  - on any other tool call, whether it ran, failed or was refused: reading or listing another path, writing another file, a terminal command, browsing or web search, an MCP call;
  - on any approval prompt. The author declines it.

  The decision is taken from the conversation's tool-call list (AG7), by this rule alone; the content of the answer plays no part. A void is recorded with `collect --void REASON`.
- **AG5. Answers.** Per packet, in this order: `stage`; a new conversation with the instruction; the conversation's export, or screenshots of its tool-call list, saved (AG7); the tool-call list read against AG4, and the label against AG3; then one `collect`:

  `collect --out DIR --packet NAME --workspace WS --model LABEL --antigravity-version V [--void REASON] [--model-change]`

  - It records exactly one attempt per staging; a second `collect` for the same staging is refused. It checks that the workspace still holds that packet.
  - With `--void REASON` it records a void attempt (valid false, void true, the reason, and the raw answer if there is one), runs no checks, and neither checks nor updates `model.json` (AG3). An attempt whose export or tool-call screenshots were not saved before `collect` is collected with `--void` (AG7).
  - A missing, unreadable or non-UTF-8 `answer.json` is recorded as a failed attempt, with the problem. An answer given only in the chat is a failed attempt: the script takes answers only from the workspace.
  - Otherwise it removes one surrounding code fence, if there is one, and records that it did. Then it runs its checks. Audit: one JSON object `{"answers": [{"id", "carries"}]}` that names exactly the packet's ids, each once and as a string, with `carries` true or false. Cases: Section 4's check 1; check 2 for `case_id`; check 3, with each quote tested only against the block of its stated source in the assembled prompt (`<case_page>` to `</case_page>` for "case page", `<register_sheet>` to `</register_sheet>` for "register sheet"), and `design_ground` quotes and `tradeoff_benefit_quote`, which state no source, tested against the `<register_sheet>` block, since they quote 94c049d text that only the extract carries; check 7, with `sub_cause` equal to a name in the manifest's list of sub-cause names (Section 1), or "none fits"; and check 8. Check 7 also allows "not applicable" for a class other than implementation defect and unclear (decision sheet B18; Section 4).
  - After recording, it removes `answer.json`, `packet.txt` and the staging marker. Attempts are stored as `DIR/responses/<packet>.attempt-N.json`.
  - Every record holds: packet, attempt number, staging reference, model label, `antigravity_version`, settings "none exposed", channel, `instruction_sha256`, `collected_at`, the packet's `prompt_sha256`, source "workspace", `raw_sha256`, the raw answer, `fence_removed`, the parsed answer, `valid`, `void`, `void_reason`, `rejected` (false) and `problems`.

  A packet gets at most two attempts (R7), voids, missing answers and rejected attempts included. A packet with two failed attempts has no V4 code, and `stage` refuses it.

  A case record that passes `collect`'s checks is valid only provisionally. Before any agreement is computed, the shared validator (Section 4, checks 1–9) runs on every stored case record, V4's and the pre-coder's alike. If it rejects V4's stored valid attempt, `reject --out DIR --packet NAME --reason TEXT` records this in a separate file, `DIR/responses/<packet>.attempt-N.rejected.json`; the attempt file is never changed. The attempt then counts as failed, so the packet is asked again if it has fewer than two attempts. A V4 record that declares "other" fails check 8 and is a failed attempt; blindness check 5's re-run is its second attempt.

  Packets left without a code are excluded from the kappa. Their number is reported per job (channel trial, cases, audit, re-run after a revision, fresh sample, 3b), with the numbers of voids, missing answers and rejections.
- **AG6. Blindness.** V4 never sees pass 1, the pre-codes, the v1 labels, the audit list's roles, results, or a Step 2, 2b or 2c output; the reveal opens those outputs to the author only (amendment line 411). The packets contain none of them (Section 6; decision sheet B24), and the workspace holds nothing else. Blindness check 3, as Section 5 defines it, is required for every V4 case packet before any agreement is computed: each prompt is rebuilt from the template with the extract, the sub-cause list in force and the page, and the hashes are compared. Where the pre-coder has a record of the same case under the same list, the two prompt hashes must also be equal. For V4, AG2's settings record and AG4's reading of every tool-call list take the place of blindness check 4, and check 6 rests on AG1, AG2 and AG4 instead of R3. The author does not discuss the cases with Antigravity outside the packets.
- **AG7. The record.** Committed and hashed before the reveal (amendment item 7), and for 3b before its probe results are opened (line 305):
  - the packet manifests of every job;
  - each folder's `staging.log` and `model.json`, and the dated notes of AG3, of a label change between jobs and of the channel trial;
  - every attempt file, voids and rejections included, and every rejection file;
  - the settings screenshots (AG2);
  - for every conversation, its export or screenshots of its tool-call list. An attempt with neither is void.

**No re-code at item 8** (amendment line 414; decision sheet C65). V4's mechanically resolved blind code is its final code: the pending results resolve it by the same rules as the author's (line 413). Where an oracle or a leave-one-out moves a case's boundary, or its row result differs between v1 and v2, only the author re-codes. These cases are reported apart. On a moved case, V4's final code keeps its blind class and sub-cause, with the caused-at that the oracle or leave-one-out sets mechanically (line 413); it agrees with the author's final code under line 480 only where class, caused-at and sub-cause all match. Every change the author makes after V4's first packet, at a codebook revision (line 409) or at item 8, is disclosed as made after V4's blind codes could be seen (line 414). There is no re-code packet and no re-code command.

**Codebook revision, fresh sample and 3b** (amendment lines 305, 311, 312 and 409). Each uses the case procedure above, in its own `--out` folder: `case-packets`, then AG1 to AG7, with at most two attempts per packet and the shared validator before any agreement. As for the 180, V4's packets of a job are staged only after the author's codes of the same cases are committed.
- **After a codebook revision** (line 409), every V4 case packet is rebuilt with the revised sub-cause list and run again before item 7. Both sets are kept and hashed, as Section 7, point 15 (a) does for the pre-codes.
- **The fresh sample** (line 311): the next 10 cases per A1/A2 run in hash order after the pilot, coded under the revised list.
- **3b** (lines 305 and 312): coded under the codebook frozen in 3a, with no revision. The model follows AG3. V4's 3b codes are due seven days after 3b's item-4 commit, as in 3a (C67). If they are not in by then, 3b's probe results are opened on the author's codes alone, and 3b's V4 kappa is reported as missing.

**What this does not give.**
- Reproducibility call for call. Antigravity does not pin a model version or expose sampling settings, so every record says "none exposed". The answers are reproducible only as recorded files.
- R2's record. Antigravity adds its own agent instructions and tool definitions to the model's input, and they cannot be recorded. What is recorded is the instruction's hash, the settings screenshots, the Antigravity version and each conversation's tool-call list.
- Confinement of the agent (AG1).
- An audit under v1's instrument (see the audit standard above).
- An author blind to V4 after item 4. The author runs V4 and reads its conversations, so every change the author makes after V4's first packet is disclosed (line 414).

The thesis says so where it reports V4's agreement.

**Main session sync (27 October 2026, late evening).** Draft 6 left four passages describing a human V4 or the pre-codes selecting V4's cases. Part B's gloss now reads "the second coder" and "You see the codes of neither", which is true for the pre-coder and for V4, since V4 reads this prompt; the prompt hash changed to `fd7e2f6b…` (Section 1), the schema hash did not. Section 4's "V4's double-coded set" is now the candidate causes of line 406; point 15's recommendation names the candidate causes instead of V4's selection; "the human coders" (Section 1, Section 6.2, point 16) is now "the author".

**Review round on draft 6 (28 October 2026).** The review round on draft 6 (findings L1 to L6, each checked by a skeptic) found defects in Section 9 and in the parts of this file that still assumed draft 5. The main session decided the findings as decision sheet entries C64 to C67, which the author may still override; this file follows those decisions and the amendment as edited on 28 October. Section 9 above, down to the main session sync, was rewritten; the two dated records are unchanged. Made offline: no LLM, embedding or other API call; `.env` not opened; git state not changed. This file only. The prompt was not edited: its hash is unchanged (recomputed: `fd7e2f6b…`, 60,369 characters), and so is the schema's.
- **Section 9, what changed:**
  - The known-answer set is gone (C64; L1-1, L1-4, L2-2, L4-1, L4-2, L5-1, L5-4, L5-5, L6-5). In its place is the channel trial on the 20 pilot cases, which count toward nothing (amendment line 407; L4-4).
  - A timing paragraph: no V4 packet, case or audit, before item 4 is committed; the due date seven days after item 4's commit, pending the author's answer (C67; L1-2, L2-1, L5-2, L4-6).
  - The run conditions are renamed AG1 to AG7, since V1 to V7 clashed with the coder name V4 (L4-13). "R7 and R8 hold as written" is replaced: R7 holds with voids, missing answers and rejected attempts counted as attempts, and R8 applies to the pre-codes only (L2-1, L5-2, L5-7).
  - AG1: the repository guard compares by file identity (L3-4); the staging log, the refusals of an uncollected staging, of a packet with a counted valid attempt and of a packet with two attempts, and emptying limited to the two files (L1-6, L2-3, L3-1, L3-5, L5-7); a plain statement that staging does not confine the agent, with the separate-user option and a check of the home-folder permissions (L2-4).
  - AG2: execution policy, settings screenshots at each session start and after any update, and the Antigravity version with every answer (L2-4, L6-6).
  - AG3: the picker label fixed in a dated note before the first packet, void under any other label, `--model-change`, and the rule for 3b (L1-10, L5-8).
  - AG4: a mechanical void rule read from the tool-call list; listing the workspace is allowed; an approval prompt voids the attempt (L1-6, L2-3, L3-1, L4-4, L5-7).
  - AG5: the order of work per packet; one `collect` per staging; `--void`; a missing or unreadable answer and a chat-only answer as failed attempts, with no `--response` (L3-8, L4-4); at most two attempts, voids, missing answers and rejections included (L1-6, L2-3, L3-1, L5-7); check 7 as an exact name match and check 3 against the stated source's block (L1-11, L3-2); validity provisional until the shared validator, and `reject` (L1-11, L3-2); `answer.json` removed after collecting (L3-5); the record's fields (L3-8, L6-6); packets without a code excluded from the kappa and counted per job (L5-7).
  - AG6: blindness check 3 required for every V4 case packet (L2-6); what replaces checks 4 and 6 for V4 (L2-4); the Step 2 outputs opened to the author only (amendment line 411; L5-3).
  - AG7: every conversation's export or tool-call screenshots, an attempt with neither void; the staging logs, model files, dated notes, settings screenshots and rejection files (L1-6, L2-4, L6-6).
  - Audit packets: fact_id and the gold value's status are printed, and the header explains the status line (L3-9, L4-12, L3-3). The standard's provenance and how V4's audit instrument differs from the v1 adjudicators', disclosed with the audit agreement (L3-3).
  - The instruction, quoted in its new form (L4-4, L5-7).
  - V4 does not re-code at item 8; codebook-revision re-runs, the fresh sample and 3b use the case procedure (C65; L1-3, L2-5, L4-5, L5-3, L6-5).
  - "What this does not give": R2's record is not available for V4 (L6-6); the agent is not confined (L2-4); the audit's instrument (L3-3); the author is not blind to V4 after item 4 (L5-3).
- **Elsewhere in this file:**
  - Conventions: amendment lines are now as of 28 October 2026 (draft 6; every line keeps its number) (L4-8).
  - Section 4: the copy-check row now reads "`class` mapped to implementation versus not, blind codes, compared with V4's and the author's" (C66; L1-7, L4-7, L5-6). "Candidate causes for Step 4 (line 406)" is now "Candidate causes, reported only (line 406)", with amendment line 406's wording (L6-1).
  - Section 5: R7 points to AG5 for V4, and R8 says it covers the pre-codes only (L2-1, L5-2). Blindness check 6 now gives amendment line 411 as changed ("until items 4 and 5 are committed") and names AG1, AG2 and AG4 for V4.
  - Section 7, point 10: "usable in the agreement and selection rules" is now "usable in the agreement measures, the copy check and the 0.40 design-limit rule (amendment line 430)". Under draft 6 the pre-codes select no case, and they enter the 0.40 rule (C66).
  - Not changed: the Contents list, which has never listed Section 9.
- **Checks** (working files in the session scratchpad, folder `fix-v4/template/`, not part of the package):
  - The prompt between `~~~~ prompt` and `~~~~` is byte-identical to the version before this round: SHA-256 `fd7e2f6b…`, 60,369 characters.
  - Outside the prompt and the dated records, the file has no "known-answer", no run condition V1 to V7, no "fresh chat", "re-code" only where Section 9 says V4 does not re-code, and "human" only in the line-116 disclosure and in the file name `17-human-studies.md`.
  - Every amendment line Section 9 cites was read as it stood on 28 October 2026: lines 3, 116, 301, 305, 308-312, 403-437, 480, 572 and 583.

**Main session follow-ups (28 October 2026).** After the fix pass, its two verifiers and a cross-check found one major and several minor gaps; the main session applied them here, outside the prompt (hash unchanged): the due date's scope and the audit's deadline (Timing); the status sentences, which separate ruled-out from replaced values (Audit); the sub-cause list's table format (Section 1, AG5); quotes without a stated source tested against the extract (AG5); check 3 as Section 5's rebuild, with the pre-coder comparison where a record exists (Cases, AG6); the instruction-change rule of the channel trial; AG1's full refusal list, the staging marker and the emptying rule; AG3's per-job `model.json`, the conversation mode and wrong-label voids; attempt and rejection file locations; the final-code rule on moved cases and the wider disclosure (No re-code; line 414); 3b's due date; point 15's reasons now include the 0.40 rule. The script's second fix pass and the main session's last two fixes (an encode before any file is written; a clean refusal when the workspace cannot be created) leave its hash at `d9571abd…`.

**C67 answered (28 October 2026).** The author confirmed (a): V4's seven days start at item 4's commit (Timing). Outside the prompt; no hash in Section 1 changed.

**Pre-tag pass (28 October 2026).** Decision sheet entries applied, each with its recommended option: C8 (a) with Correction 2; C62 (b) with its second item (i); B18; B21; B22; and, as they bear on this file, C17 (a) and A19. Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. This file was edited, and `23-am1-precoder-extract.md` was created; the register had been edited just before by another agent (its "Pre-tag record (28 October 2026)").
- **C8, Correction 2.** The extract carries the sentence tags (Section 1). Part B's terms, E6 step 6, E6's WD rule, Part G (`design_ground`, `tradeoff_benefit_quote`) and validation check 6 now accept a design ground only from one sentence that the caused-at sheet lists under (C) for architectural weakness, or under (B) for a trade-off; a (B, C) sentence counts under the list it appears in; a WD case keeps D4.p5 whole. Section 3, rows E and E6, follow. Reading chosen: the benefit quote of a trade-off must also come from a (B) sentence, since the correction limits every trade-off quote to B sentences.
- **C62 (b), item (i).** A5, Part G and the schema add "candidate generation" to the steps where line 340's argument is required and "design or model, not separated" is allowed. The gatekeeper rules are unchanged. Section 3, row A5, re-quotes the five sheet sentences as the register now words them. Point 24 is done.
- **B18.** E7, the schema and check 7 add "not applicable", only for a class other than implementation defect and unclear. Reading chosen: "none fits" stays as it was, and the schema does not forbid it for other classes, since B18 adds a value and changes no class; E7 tells the coder to use "not applicable" there. Section 4's 3b row says that "not applicable" is not counted. Section 9's AG5 notes that `23-am1-v4.py` does not yet accept it (below). Point 12 is done.
- **B21, B22, A19.** The extract was built as Section 1 says, and Section 1 now records how, with the judgements taken. Under B21, Part G's checklist note also gained the sentence on the extract's item ids ("The id is the text in square brackets; the text is the rest of that line."), a prompt change, so B21 is among the edits behind the new prompt hash (credited in Section 1 in the follow-ups below). Blindness check 7 passed (Section 5). Section 1 records the new prompt and schema hashes, the extract's hash and the filled prompt's hash. Section 9 says what T is and where it comes from. Points 16, 17 and 18 are done; point 9 is done under C17 (a).
- **Made stale and updated:** Section 6.2's row for the register checklist (the page takes the boundary's sheet from the extract, as B22 asks for one text, and since the signed sheets still carry counts); Section 6.4's last bullet; Section 3's note on the parts left out.
- **Open, for other owners:**
  - The decision sheet's hash table and the index (`23-am1-step0-index.md`) still carry the template's old hashes, and neither lists the extract yet.
  - The build script and `blind7.py` are working files in the session scratchpad. Decision sheet B3 may want them committed with the other check scripts.
  - The Step 3 page builder (order of work item 1) must take the page's checklist from the extract (Section 6.2).
  - The extract is long: 231,036 characters, so the filled prompt has 292,471. Repeating the implementation sections after each sheet that points to them accounts for most of it.
- **Checks** (working files in the session scratchpad, folder `pretag/template/`, not part of the package):
  - Hashes recomputed with `step0/verify/pt/hashes.py`: prompt `8b4422c9…` (61,451 characters), schema `0c05d09c…`. Extract and filled prompt with `fill.py` (Section 1).
  - Schema test `check_schema6.py`: 95 records and 11 check-9 records, all as intended. Changed expectations: architectural weakness at "candidate generation" without the argument is now invalid, and "design or model, not separated" there is now valid. New records: the trade-off and the argument at that step; "not applicable" with architectural weakness, trade-off, conversational difficulty, evaluation defect and design-or-model (valid), and with implementation defect, unclear and a held case (invalid); "none fits" without a proposal (invalid). `23-am1-v4.py`'s schema checker agrees on all 106.
  - Check 6 test `check6_test.py` on the extract: on every sheet the sentences listed under (C) and (B) equal the sentences so tagged in the paragraph text; item ids are unique per sheet (E 24, K1 10, K2 18, S 33, R 17 items). 19 sample grounds passed or failed as intended, among them D2.p4's window sentence (fails), D3.p3's sentence on negating the current value (fails), D4.p5 outside a WD case on sheet E (fails), D4.p5's (B) sentence in a WD case (passes), and D7.p5's first sentence: a trade-off on sheet S and architectural weakness on sheet R pass, architectural weakness on sheet S fails.
  - `23-am1-v4.py case-packets` with the filled prompt as T, a mock sub-cause table (two names, column "Name") and one mock page: one packet; the manifest's `template_sha256` equals the filled-prompt hash and its `extract_sha256` the extract file's hash; `blocks()` returns the extract and the page unchanged; the schema parses from the packet. `check_case` passes a record with a list name, and rejects the same record with "not applicable" at check 7, as noted above.

**Pre-tag follow-ups (28 October 2026).** After the pre-tag pass's reviews, the main session's follow-ups were applied here and in the files named; the prompt text is unchanged (prompt `8b4422c9…`, schema `0c05d09c…`), so only the extract's and the filled prompt's hashes changed. Made offline: no model, embedding, network or API call; `.env` not opened; git state not changed.
- **V4 check 7 (B18).** `23-am1-v4.py`'s `check_case` now accepts `sub_cause` "not applicable" when the class is neither implementation defect nor unclear, as Section 4's check 7 does. AG5's sentence that the script did not yet accept it, and the pre-tag record's open item on it, were removed. The script's hash is now `1d550b32813435025996eb1ddaabee21668cb8c6b7179ab2b89ca784aed513f9` (was `d9571abd…`). Its end-to-end suite (a working file in the session scratchpad, folder `pretag2/e2e/`) passed 254 of 254: the 248 earlier tests, of which five audit-packet expectations were updated from 430 to 479 decisions and from 57 to 78 rejected statuses, since the audit list was re-run under C18 and C20 after that suite was written, and six new tests of check 7 with "not applicable" (accepted for design trade-off, architectural weakness, conversational difficulty and evaluation defect; refused for implementation defect and unclear).
- **Extract builder committed (B21; B3).** `23-am1-precoder-extract.py` replaces the scratch `build_extract.py`; it reads only the register and the design-text file and writes the extract, and `--check` rebuilds it into a temporary file and compares the bytes. It also cuts four run observations the register keeps as record (Section 1, Removed). The register's own follow-ups (S.4's line for D5.p6's first sentence; one cite of amendment line 251 in sheet K2's expansion-generator line) entered the extract with the rebuild.
- **Section 1.** New extract and filled-prompt hashes; the register and design-text hashes the extract was built from; the rebuild script. Two wording fixes: the filled-prompt hash is said to be recorded below, to be recomputed at signing if anything changes; the prompt hash note credits B21 (Part G's item-id sentence), as does the pre-tag record's B21 bullet.
- **Section 5, blindness check 7.** Re-run on the rebuilt extract: pass, with the same findings.
- **Checks** (working files in the session scratchpad, folder `pretag2/`): `fill.py` gave the hashes above; `check6_test.py` on the rebuilt extract: all as expected; `23-am1-check-register.py`: 0 errors.
- **Open, for other owners:** the decision sheet's and the index's hash rows for this file, the extract, the register, `23-am1-v4.py`, `23-am1-check-package.py` and the new `23-am1-precoder-extract.py`.
