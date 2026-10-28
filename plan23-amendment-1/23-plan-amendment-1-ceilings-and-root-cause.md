# Plan 23, amendment 1: ceiling tests, achievability probes, the root-cause study, a second series

Drafted 23 October 2026, revised 27 October. **Draft 5,** after four rounds of adversarial review: round 1 had three lenses and 34 substantive findings; round 2 checked coverage and read the draft cold, with 25; round 3, a coverage and consistency check, found 13; round 4 found 3 major and 7 minor ones. A skeptic checked every finding, and none was refuted. Status: **draft, not signed.** **Draft 6 (27 October, evening; reviewed 28 October):** V4 is a machine coder, a Google Gemini model run as an agent in Google Antigravity. Changed on 27 October: lines 116, 405–407, 430, 432, 583 and 612. Changed on 28 October, after a package check and a fifth review round (five lenses, a skeptic per lens and a completeness critic): lines 116, 405–407, 411, 414, 419, 430, 432, 572 and 583. The known-answer set is dropped, V4 starts after pass 1, and V4 does not re-code at item 8. Every line keeps its number.

**Names:**
- "D1"–"D11" mean only the design decisions of Ch. 4. Plan 23's phases are written "Phase D1" and "Phase D3".
- **WD** is the whole-decision extraction contract (`extraction_whole_decisions`).
- **R**, **E+R** and **E+R\*** are the Step 2 oracles.
- **C** and **A1′** are Step 4's control and repaired configurations.
- **A1-ref** is the reference arm that carries the admitted repairs.

**How this file is bound:**
- It amends `23-plan-development-and-confirmation.md` (plan 23), which stays in force. Everything not changed here is unchanged.
- Development stays "logged, not pre-declared" (plan 23, integrity rule 3). But this file fixes decision rules that their own outcomes must not steer. It is signed together with the Step 0 registers and the audit list, then committed and tagged `plan23-amendment-1` with its frozen inputs, **before any Step 2, 2b or 2c output exists.** Every later output cites the tag.
- It is **not blind.** Its rules were set after the items under "Already read" had been read.
- Edit only before signing. Afterwards, changes go in a dated note that says what had been read by then.

## Why

The EL2020 development runs and the loss trace (`23-el2020-arms.md`, `23-loss-trace-results.md`) show:
- the repaired system (A1) stores no more than the evaluated one (A0);
- A2 scores below A0, and below A1 when questions are resampled;
- about a third of the gold rows are lost at extraction;
- about a quarter to a third surface as other values winning against, or overwriting, the gold value.

The trace gives the **location** of each loss, not its **cause**, and it cannot tell bad implementation from a limit of the design. Plan 23's principle is that a result limited by a defect shows nothing. Applied here: **every coded loss ends in exactly one of three states.** Uncoded losses enter the bound rule through their arm's sample shares.
1. **Repaired:** the repair passed its check and was admitted (Step 4), or, for A0 only, the loss rests on a Phase B bug.
2. **Shown, with evidence, to come from the design as documented before cycle 1, the conversation, the evaluation, or the held-constant model.**
3. **An unrepaired implementation defect, or unclear.** It enters the bound rule (Step 3), which can make a verdict *can't tell*.

No loss becomes a design limit by default, by a threshold, by a cap on repairs, or on the strength of design text written after the results. "Design or model, not separated" (Step 3) is reported under its own label and is never cited as a design limit.

## Already read when these rules were fixed (23 October)

- **The loss trace,** per run and sub-code (`23-loss-trace.json`, `23-loss-trace-results.md`):
  - routing-type sub-codes, 34–41 rows per run in A0/A1;
  - extraction, about 45;
  - reading, 9–11 (of which `key_reached` about 7);
  - only 12 of 65 values have the same first-loss boundary in all six A0/A1 runs;
  - the largest within-arm range at `carried` is 9 rows and 5 distinct values. It is up to 11 rows at any single step, and 13 at the grouped extraction and filing boundaries.
- **The A2 analyses:** the 16-key conflict sample, and the hand traces of rounds 2 and 3 (A2 r1, r2b, r3).
- **A0 r1 case by case:** its reading-loss keys, and the round-1 hand traces (48 rows over six runs).
- **The "66-key shortlist" case** (`23-el2020-a0-a1.md`).
- **Reviewer probes and counts:**
  - 134 of 203 routing-lost rows had every carrier keyed by the extractor's hint;
  - the first-checkpoint extraction loss rate rises from 27% at meeting a to 46–47% at c and d;
  - the extraction prompt grows from 2.5k to about 39k characters;
  - 119 of 271 A0/A1 extraction-lost rows (44%) have a single-value question; 75 of them (28% of 271, 63% of the 119) had a credited RAG answer citing a gold line in at least 2 of 3 runs;
  - `_prompt_registry`, applied to span text, keeps a median of 95 of the 146 keys of a1_r2's final registry (65%), and 68–76% of the keys listed in each recorded extraction prompt;
  - at least 27 of 66 `key_reached` rows had the holding key outside the pruned question-time prompt;
  - per run: 1–3 claims carry values of two gold keys, 3–12 carriers carry the value only through their subject, and 0–1 gold keys would get a confidence tie;
  - 4 of the 16 sampled A2 conflict keys hold variants of one matter;
  - 12.2 of the 45.2 extraction-lost current rows per A0/A1 run are lost at polarity or modality;
  - only 313 of 534 a2_r1 claims carry a recorded support verdict;
  - A0 pass rows carry defect flags (17/11/20 per run, nearly all bug 2);
  - each A1/A2 run has 59–64 lost cases.
- **The ES2009 adapter prototype** on 17 cycle-1 runs (raw bounds, unadjudicated).
- **The four fact reports and the four review rounds,** and the loss trace's verification rounds. Their full records (scripts, arguments, every agent's findings and skeptic verdicts) are the Claude workflow records under `~/.claude/projects/…/workflows/`:
  - wf_ebdcd91e (fact reports);
  - wf_12870ac1, wf_536a6a0a, wf_ad8f2921 and wf_d3a83b84 (review rounds 1–4);
  - wf_4e0604f8, wf_bbe042f0, wf_c00c1888, wf_0db6eaa4 and wf_317beeac (loss-trace verification and adjudication).

  Whether they are archived in the repository is a decision for signing. The reviewers' scratch files and the ES2009 adapter prototype were in a temporary session folder and are not kept; their results are in those records.

## Frozen inputs (Steps 2–4)

| Input | SHA-256 |
|---|---|
| `23-loss-trace.py` (v3.1) | 4c12ccef9f7f788806b36eb8f71da25902cf755f8567c7be38f1fb052a52ffb1 |
| `23-loss-trace-adjudications.yaml` (670 model decisions, v1) | e084d95cd72431fd494b8e5aa7c9e1c69ad80da3481e1271c9d88cd6c272f089 |
| `23-loss-trace.json` | da4576242eda6fc181352eb8a4f74172c2961b187ca5e1b5391142c554c9e8a9 |
| `data/ami_eval/suites/transfer_el2020.yaml` | 2361f17cdb14a64dbe77c99115bfddb3c3e615188799d632feb76fb59d8121d4 |
| `data/ami_eval/gold/reviewed/EL2020.reviewed.yaml` | 6b963af028fb6f318218a4bd0bca2d532e4db446b5a4f31d18f136b5bfdc0ac8 |

**Run manifest.** It is committed with the amendment. Each run's hash covers its state, trace, answers and report, concatenated; the RAG runs' covers the `.rag.json` file.

| Run | Hash |
|---|---|
| a0_r1 | dedea0ba34fa052685efc6c2823a1f75eef31fa69b5066c8bb72cf519284e739 |
| a0_r2 | 899119b8a52b580e5d01199c81abe449219874d98d0d3c707e3438097baf40fa |
| a0_r3 | 45c820908b6a14e3b0c163ff5758a896523ded26fefc813ae61712e72908a7fd |
| A1 smoke run | 1a897ba97a07199bf8aa97347a409cd440cfb53eae307da1d59bf0800f12eb2a |
| a1_r2 | a17261f2d72d04c452b6817d6e27c48e38fe18528fab65df6f880b51afe4feaa |
| a1_r3 | 60d2a29e79e014cb2b239aee2f1afbd16abe5277a1dda6ed64fd38eed354be07 |
| a2_r1 | d5292f23fbca162ca742934c29beaa3ed8f7625a38d8c8b01a2606cd24df53d8 |
| a2_r2b | 56be9f3bc597f963b5447a9a510da4d89ad254aa75449e67fe71654ec7c169e7 |
| a2_r3 | c608781ae86e81c363898b94ab9ffdfbb34f4c2c1b0cd63c3cd444eaf0405b50 |
| rag_r1 | 8d25e1950f9933345ee0b18d166b853d421959ab9b3d215ab9a2552882dfb737 |
| rag_r2 | f0c37a3adb30ae3fea2a7938d3a68004b4dc59de41400816866d7fbf908af95b |
| rag_r3 | 488235daae0df1f01c79e746e18c609ae810a77cb346e66c1718ead3fe8ba0bf |

**Rules for the frozen inputs:**
- The run folders are gitignored, so they are also archived off the repository as a zip with its SHA-256.
- New adjudications (probes, WD, Step 4) go to separate dated files per batch, never into v1.
- **v2** is v1 with the V4 audit's labels on the audited decisions (Step 3, item 6). The oracles are always computed under both v1 and v2. A cause's eligibility, and any caused-at boundary set by an oracle, must hold under both. Cases whose row result differs between v1 and v2 are re-coded at the reveal, under item 8. If the audit is late, v2 = v1, and this is reported.
- Steps 2–4 use the frozen EL2020 suite and gold. Post-B3 scores are reported beside them.

## Step 0: registers and housekeeping

**Before signing:**
- **Design-and-controls register.** For each component (admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading), it lists three kinds of entry.
  - **Design:** the Ch. 4 decisions **as worded at 94c049d (9 September, before the cycle-1 runs), quoted verbatim.** Listed separately and marked **retrospective**:
    - D10 and D11, which entered at 5de9911 on 19 October;
    - any design text written or signed after 9 September, including decisions signed under this amendment.

    The 38a0f4a sentence that the autonomous arm leaves conflicts open reports a Chapter 5 observation and is **not** a design entry. The design text is D5's "leaving unresolved cases reviewable" (94c049d). Each component also records whether it is an **LLM step** or a **deterministic step**.
  - **Implementation:** the evaluated prompt texts, including the example roles and the registry they carry. Also the parameter values (`embedding_top_k`=8, `embedding_min_similarity`=0.30, `resolver_prune_threshold`=12, `expansion_reuse_threshold`=0.80), the resolver shortlist and pruning, and the harness reviewer `_reviewer_would_accept`. Prompt text is implementation even where it is older than cycle 1.
  - **Held-constant controls:** the generator gpt-5.4-mini at temperature 0 (shared with RAG), text-embedding-3-small, and the judge.
- **Claims register.** One row per causal claim the thesis text now makes about where or why the system loses information. Each row gives:
  - the claim and its location;
  - the result here that would confirm it, and the one that would overturn it;
  - the text action in either case.

  It also carries the mapping from boundaries and sub-causes to the mechanisms (complete decisions, change and supersession, rejection, evidence and provenance, and each contract). **The mapping signed here governs every Phase C verdict.** The Phase D3 registration may revise it for Phase D only, in a dated note.
- **The audit list:** every v1 decision that decides an oracle row result. That is the carrier decisions on A0/A1 rows lost at filing or state maintenance, which decide R, and the "does not carry" decisions on values lost at extraction in an A0/A1 run, which decide E+R against R. It comes to about 420 of the 670. A script computes the list from the frozen inputs, and the list is committed with its hash.
- **The V4 second coder:** a machine coder from a third model family, Google Gemini. It is neither Claude, the family of the pre-coder and the v1 adjudicators, nor GPT, the family of the system and its judge. It runs as an agent in Google Antigravity, one new conversation per packet, on a clean workspace outside the repository that holds only that packet, with the pre-coder's prompt unchanged for the cases and the loss trace's carry standard (`23-loss-trace.md`) for the audit (`23-am1-v4.py`; template Section 9). The model is chosen explicitly in Antigravity's picker; its label is fixed in a dated note before the first packet and recorded with every answer. The due date is set at signing (fallback in Step 3). It is disclosed as agreement with an independent machine coder, not as human inter-rater reliability. It stands in for plan 23's human second coder (plan 23:234) in this amendment; whether plan 23's V4 item and the Phase D1 gate are met by it is decided before Phase D, in a dated note.
- **The probe note:** the neutral example text for (b2), and gpt-5.4's settings for (d), fixed and dated.
- **The model pre-coder's prompt template,** fixed and dated.

**Before Step 2:**
- **Plan 23 fixes:**
  - remove "restraint on incidental talk" from the Phase D3 mechanisms;
  - add the Open decision on conflicts in the autonomous arm;
  - update `22-bug-list.md` row 11;
  - replace P23:264's whole-item metric, for judging WD, by the Step 2c endpoint;
  - Phase C ends after the dress rehearsal, which follows Step 5 and the admission rule.
- **Answerable-only accuracy** for the twelve EL2020 cycle-2 runs.
- **Instrument changes:** they change no A0/A1 behaviour, and a switches-off unit test and a seeded replay of the cassette path show that.
  - Record the judge's inputs in `trace.json`.
  - Log the rival values of every conflict.
  - Record an embedding cassette in `run-ami-eval`. Wire `CassetteEmbeddingClient` into the trace replay, lift its embedding refusal for cassette-backed runs, and write attempt and study metadata for CLI runs.
  - Commit the faithful replay's output hashes, as a data-dependent test that skips when the attempt is absent.
  - Optional: set the seam on every LLM usage record.

## Step 1: ES2009 prerequisites (your decisions first; then offline)

**B3 gold decisions** (plan 23 B3; all open). Each is recorded with its transcript evidence and committed **before any score under it is computed**. Each applies to every arm, RAG included, and scores are reported under both the old and the new gold. The decisions:
- **P1-8,** the universal-remote reversal.
- **P1-7,** gold provenance.
- **The three author-confirmed corrections.**
- **The B3 item fixes** for ES2009 and EL2020:
  - noise items with forbidden content;
  - status items that can fail;
  - rejection items with an expected status;
  - more than three candidate/decided values;
  - unknown items on discussed-but-unsettled topics.
- **The V5 packet** is sent.

**Older runs keep their recorded answers.**
- An item whose question is unchanged but whose gold *string* changes is re-judged by the judge only (bug-7 procedure).
- Where gold *values* change, the deterministic scoring and the state layer are re-run too, with their own estimate.
- New or reworded items are left out for old runs. Comparisons across suite versions use the common items.
- **The re-judged runs:** the twelve EL2020 cycle-2 runs; any cycle-1 run is re-judged only if Ch. 5 reports it under the new gold.

**The EL2020 comparisons** of 22–23 October were read before B3 and are disclosed as such.

**What ES2009 can carry,** stated here and in Ch. 5. It is a weaker second series:
- It is the series on which every prompt was developed.
- Its gold is weaker. 19 entries are machine-only, including every rejection value, and 27 of its 87 rows are summary-only.
- It has 87 rows over 35 values, against 159 over 65 in EL2020.
- Its gold keys are coarse, so it gets no oracle ceiling.
- Its trace reaches reading for only 10 rows.

It tests the write path. Agreement with EL2020 is a consistency check, not a replication. If A2 is ever run on ES2009, ES2009 is stated to be the contracts' home series, and a favourable result there does not outweigh EL2020.

**The ES2009 loss-trace adapter.** Its decisions are recorded in the codebook before any ES2009 adjudication:
- **Provenance:** AMI summlinks primary, then decision annotations, then transcript lines. Each row records its source.
- **The three retiring rejections:** coded ruled-out, with derived demoted rows.
- **Scorecard:** each run's own.
- **Excluded:** the reference-informed runs.
- **Adjudications:** a separate ES2009 adjudication file.

The build is 3–5 days of agent work after the new gold is frozen.

## Step 2: offline ceilings on EL2020

**Harness.** It rebuilds a run's state by running only the deterministic services for real (in-process, fresh database): the conflict service, the resolution engine, proposals, the A1 settle, the structural confirm and the projection. A call to an LLM seam is an error. The only exceptions are listed per variant with their call counts and written to a cassette: live embeddings for A2's equivalence check, and live support checks in the A2 variants. Everything else is replayed from the run's trace, coldstart report and dump:
- **Claims:** each claim is inserted at its recorded extraction phase and order, with explicit `created_at`. It carries its recorded `state_key_hint`, its meeting's authority and source time, and its span position.
- **Key timeline:** every recorded key change and filing evaluation is applied in sequence, except those caused by a contract the variant switches off.
- **Registry and parking:**
  - each key definition enters the registry at its recorded acceptance;
  - parked claims are released as recorded;
  - claims that were never released stay parked.
- **Provenance:** the SHA-256 of every input read is written to the output.

The build is 2–4 days of agent work.

**Identity gate, per run.** With the recorded keys, the harness must reproduce:
- the `conflict_detection` trail in order;
- the proposals (key, value, type, final status, phase);
- the settle expiry counts per meeting;
- the facts with creation phases, statuses and supersession links.

**When a gate fails:**
- A failed gate is a harness defect. It gets at most three fix rounds, or 4 days of agent work. A run that still fails counts as failed, the report names the passing runs, and oracle definitions never change.
- **There is no live fallback.**
- **Without passing A1 runs,** state-logic repairs cannot be checked and stay unrepaired.

**The oracles, defined here:**

| Oracle | What is made perfect | Endpoint |
|---|---|---|
| **R** (routing) | Every carrier of a gold value is filed under that value's gold key from its first evaluation on. A carrier is a primary-series carrier at any checkpoint from its extraction on. The gold keys are registered before meeting a, as scalar, open-vocabulary definitions. Values sharing a gold key share it; on EL2020 these are only F25→F58 and F36→F59. A claim carrying values of two gold keys goes to the value whose polarity it has; if both qualify, to the value whose cited span holds its evidence; otherwise to the lower fact id. These cases are listed. The 5 no-successor demoted rows (F27@c,d; F35@c,d; F56@d) are excluded from R's tallies and listed as oracle artifacts. | stored with the right status at k |
| **R-hint / R-resolver** | R restricted to carriers routed by the extractor's hint, or by the resolver or expansion. **Evidence only;** they do not set caused-at. Path shares are reported beside each arm's base rate of hint-keyed claims. | as R |
| **E+R** | R, plus one injected claim per gold value for every current, candidate or ruled-out row first lost at admitted, carried, polarity or modality. It is injected once, at the earliest such checkpoint, at the span of the row's last cited line; if that span was never admitted, an evidence span is created. It enters in that meeting's phase, after that span's recorded claims. Object: the gold value. Polarity: positive, or negative for ruled-out values. Modality: asserted, or proposed for a candidate. Authority and source time: as the run's own claims from that meeting. Confidence: the median of the run's asserted claims. Filed under the gold key. F27, F35 and F56 get an injected asserted negation at their verified change span (CH6, CH2, CH5). | as R |
| **E+R\*** | E+R, plus removal of the negative carriers of current values. It still loses the state rules' share, plus any remaining wrong-modality carriers and positive carriers of ruled-out values; these are listed. | as R |

**Two-sided output:**
- **Per oracle and run:** a transition matrix (lost→pass, pass→lost, unchanged) in rows and distinct values, per boundary and kind. "Recovered" means net.
- **Endpoint:** for R and E+R the trace stops after the status step; reading is not re-run on oracle states.
- **Adjudication:** injected claims are carriers by construction. Other new deciding texts go through the two-adjudicator protocol, capped at three rounds. Items still open are reported unresolved and excluded from that oracle's result.
- **The decomposition is nested and order-dependent:**
  - extraction's share is given under perfect routing;
  - R removes every non-carrier from the gold key, including any legitimate same-matter rival.

**Reading, offline.** For every single-value question lost at `key_reached`, the analysis records:
- whether the holding key was in the resolver's prompt, and its rank;
- the chosen key and its label overlap;
- the effect of the deterministic widening.

**A2, offline (on runs that pass an A2 gate):**
- **A2 gate:** the three A2 runs are replayed with recorded keys. A recorded support verdict is reused, as the code's per-claim cache does. Embeddings are live, for the equivalence check only. Parks and open conflicts per key must reproduce.
- **Leave-one-out:** each of the four contracts is switched off in turn.
  - A winner with no recorded verdict gets one live support call, counted, at about $0.2 per variant and run.
  - Type check off: the recorded type-check re-routes and `no_fitting_key` parks are not applied.
- **Reviewer ceiling:** at each checkpoint, every open same-meeting conflict is resolved to the gold value where it is among the rivals (rival values matched with the loss-trace matcher and adjudication), and otherwise by the A1 rule.
  - Values the ceiling chooses are not support-checked.
  - It is **the most a perfect reviewer could recover, not an estimate of a reviewer.**
  - Keys holding more than one gold value are counted separately.

The contracts were tested in the A2 context only, with no one-contract-on variants over A1. Their admitted subset is first run together in Step 5. A2 is not run on ES2009 until the conflict decision is taken.

## Step 2b: achievability probes (live, small; own estimate and go-ahead)

**What a probe is:**
- Each probe output is one LLM call, for one span or claim and one repeat, on inputs taken from `trace.json` or rebuilt from it as stated.
- It is scored only at its own boundary, with the loss-trace matcher and an adjudication batch file, never on the overall score.
- The probes run on the author-sampled A1 and A2 runs (Step 3). On the Step 5 run that 3b codes, only probe (i) runs.
- All conditions are fixed here or in the dated probe note. There are no sweeps.

- **(i) Extraction:** every extraction-lost case, except `admitted:ignored` cases. Those are gatekeeper losses with no extraction call, and are listed apart. The cited span is re-extracted, three repeats per condition:
  - **(a)** the recorded prompt (control);
  - **(b)** the recorded prompt with the registry cut to the resolver's embedding candidates for the span text, at the evaluated parameters (`embedding_top_k`=8, `embedding_min_similarity`=0.30), without the lexical part of `_prompt_registry`. Each case's cut size is recorded, with whether a key holding the gold value is in the cut;
  - **(b2)** as (b), with the neutral examples of the probe note in place of the AMI role examples;
  - **(c)** an empty registry;
  - **(d)** gpt-5.4 with the recorded prompt, only on cases that (b) and (b2) do not recover. Settings as in the probe note.

  (b) and (b2) make live embedding calls, under $0.01.
- **(ii) Routing.**
  - **Offline:** whether the gold-holding key, or a fitting one, was in the resolver prompt. Hint-routed carriers have no resolver prompt; their check uses the registry in that meeting's extraction prompt.
  - **(ii-r) Resolver path, live:** the resolver-routed carriers and rivals of routing-lost rows are re-resolved three times with the unpruned registry at that moment (from the registry timeline). The control is three repeats of each such claim's recorded resolver prompt. Expansion-routed misfilings (the resolver returned no key, and expansion reused or created one) are not probed. They are coded from the trace, under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry.
  - **(ii-h) Hint path, live:** the spans of hint-routed carriers and rivals of routing-lost rows are re-extracted three times under (a) (control) and (b).
  - **Scoring:**
    - A re-resolved or re-hinted claim passes in a repeat when its output key's registered definition fits the claim's own matter. If no registered key fits that matter, returning no key also passes. Fit is adjudicated under the two-adjudicator protocol, against the registry at that moment.
    - Repeat j of every probed claim of the case forms output j of the case. The output passes when every probed claim passes, and no claim of another matter shares a key with a carrier, with unprobed claims kept on their recorded keys.
    - k and k0 count these case outputs.
    - **Applicability.** A misfiled claim is a carrier or rival whose matter does not fit its recorded key's definition. A case whose misfiled claims all lie on one path takes only that path's probe. The other path's probe does not apply to it: its result is reported but never counts as *not recovered*.
    - **Joint condition.** A case with misfiled claims on both paths takes a joint condition. Output j combines (ii-r) repeat j with (ii-h) (b) repeat j, and the control combines the recorded-resolver repeat j with (ii-h) (a) repeat j. Each probed claim's own pass or fail is recorded per repeat.
    - **Counterparts in (ii-h).** A carrier's re-extracted counterparts are the output claims the loss-trace matcher matches to the gold value, adjudicated where the matcher is unsure. A rival's counterparts are the output claims the adjudicators judge to state the recorded rival's matter. Every counterpart must pass. A carrier with no counterpart fails the repeat. A rival with no counterpart passes the repeat, and the case is listed as recovered by omission (sub-cause extraction, not hinting).
- **(iii) Question time:** `key_reached` losses are re-resolved with the unpruned registry, only where the offline check shows the holding key was pruned out. The control is three repeats of the recorded question-routing prompt. A repeat passes when the resolved keys include the holding key.

**Recovery rule, fixed here.** For a case and a condition, k is the number of passing repeats (of 3), and k0 is the same count for its control. The rows are applied in order:

| Result | When |
|---|---|
| **Not reproduced** (sub-cause *sampling instability*) | k0 ≥ 2 |
| **Recovered** | k ≥ 2 |
| **Not recovered** | k = 0 |
| **Inconclusive** | k = 1 |

**Mapping, fixed here, applied at the reveal:**
- **(b) or (b2) recovered:** implementation choice at extraction. The sub-cause is registry-conditioned extraction, or out-of-domain examples.
- **(ii-r) recovered:** implementation choice at key resolution. The sub-cause is *the shortlist or prune excluded a fitting key* only where the offline check shows the fitting key was missing from the recorded prompt; otherwise the sub-cause is set on the page, within key resolution.
- **Joint condition recovered:** routing, path unclear (possible implementation at both).
- **Joint condition not recovered:** it rules out a path's alternative only if that path's own probed claims failed in every repeat. Any other path stays possible implementation at that path.
- **(ii-h) recovered under (b):** implementation choice at key assignment at extraction, sub-cause registry-conditioned hinting.
- **(iii) recovered:** implementation choice at reading, sub-cause the question-time shortlist excluded the holding key.
- **(c) recovered, and (b) and (b2) not recovered, whatever (d) shows:** caused at extraction, sub-cause registry-conditioned extraction, class **unclear** (possible implementation).
- **Model-limited:** (d) recovered, and (b), (b2) and (c) not recovered.
- **Every applicable condition not recovered:** evidence against an implementation cause at that boundary. It is not proof.
- **Not reproduced, inconclusive, or any other combination:** no probe evidence. It can never support an architectural or trade-off code. The code is unclear, unless the page shows an implementation entry behind the case.

## Step 2c: the whole-decision contract (WD) on EL2020 (own estimate and go-ahead)

- **Why:** the largest extraction sub-cause is `carried:claims_without_the_value`, and most texts rejected there state one part of a multi-part value. WD is the built alternative.
- **Arm:** three A1 + `extraction_whole_decisions` runs, interleaved with three fresh A1 runs at the same commit, after the Step 0 instrument changes. The fresh A1 runs are also a drift check against the frozen 22 October A1 runs.
- **Adjudication:** WD and fresh-A1 texts enter one pooled queue, without arm labels.
- **Endpoint:** current rows lost at `carried`, per run, in rows and distinct values.
- **WD rule, fixed here.** It is WD's only route to admission (Step 4). WD *works* only if all of these hold:
  - every WD run has fewer such losses than every fresh A1 run (exact one-sided p = 1/20);
  - the WD mean is lower by more than 9 rows and 5 distinct values;
  - mean filing losses rise by no more than 13 rows (the largest within-arm range at the grouped filing boundary);
  - no owner or role claim is lost;
  - there is no new incidence.

  Otherwise the result is *not shown*.
- **If Step 2c is not run:** WD is dropped from Phase C with its reason, and the Step 0 plan-23 fixes record that P23:264 is withdrawn. Cases whose only named remedy is WD are coded unclear.

## Step 3: the root-cause study (plan 23's attribution coding, built and dry-run)

**Unit.** A *case* is one gold value in one run at each distinct loss step it reaches, taken at that step's earliest failing checkpoint, with its step and sub-code. Current, candidate, ruled-out and demoted values all count.

**Two parts:**
- **3a, before Step 4:** the EL2020 runs. Only 3a feeds the repair round.
- **3b, after Step 5:** coded under the codebook frozen in 3a, with no revision, following items 3, 4, 5 (all cases), 7 and 8 of the order of work below. Its probe results stay sealed until its author and V4 codes are hashed. It feeds no repair. It is reported as the codebook-transfer check, with its own kappa, its unclear share, and the share of cases that fit no frozen sub-cause.

**Sample, fixed now:**
- **Author-coded:** the first 30 lost cases, in the order of sha256(run_id|fact_id|k), of each A1 and A2 run. That is 180 cases.
- **A0:** model pre-coding and defect flags only. A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound. A0 enters no admission verdict.
- **Pilot:** the next 20 cases in one pooled hash order over the six A1/A2 runs. It counts toward nothing.
- **Fresh sample after a codebook revision:** the next 10 cases per A1/A2 run in hash order after the pilot, coded blind by both coders.
- **3b:** all cases of the final configuration's r1 on ES2009 get author and V4 coding. ES2009 A0 r1 gets model pre-coding only, plus author coding of the ES2009b walkthrough cases.
- **Coverage disclosure:** each run's first-loss profile and the sample's profile are reported. Cases from rows already read are flagged.

**Passes are examined too, for defects in both directions,** on every question flagged `credit_without_state` and on a 20% sample of pass rows per author-coded run (seed 23). For each examined pass the coder records:
- any evaluation defect;
- whether the pass rests on an implementation defect (yes, no or unclear, with the boundary and evidence). Examples: a rival kept off the value's key by a mis-filing; a demoted value retired by a rival from another matter; a demoted row passing only because the value was never stored.

The loss trace's defect flags are reported for pass rows. Evaluation defects change no gold, suite or score within this study. Corrections go through B3 and apply to every arm and to RAG.

**Classes** (plan 23's five, plus two labels; "unclear" makes eight):

| Class | Definition |
|---|---|
| Implementation defect | **(1) Conformance:** the code contradicts the register. **(2) Implementation choice:** the loss rests on an *implementation* entry, and an alternative counts. An alternative counts when any of these holds: (i) a Step 2b probe recovers the case under the mapping; (ii) the prompt omits information the register gives that step, or contradicts the register; (iii) the trace shows a parameter excluded the right item, or admitted a wrong one (e.g. an expansion-reuse or similarity threshold filing a different matter under the key); (iv) for `carried:claims_without_the_value`, the WD rule below. Wording quality without (i)–(iv) does not count. |
| Architectural weakness | the loss follows from a design decision **as worded at 94c049d**, quoted on the case page |
| Design trade-off | the loss is the cost of a deliberate choice whose benefit the 94c049d text states. Where the loss trace can measure the benefit, it is measured |
| Conversational difficulty | the transcript makes the value hard to recover |
| Evaluation defect | the gold, the suite, an adjudication or the judge is wrong |
| Model-limited (held constant) | only under the probe mapping. Bounded to gpt-5.4-mini |
| Design or model, not separated | the caused-at boundary is an LLM step with no model condition (routing, reading, A2's support check, the gatekeeper for `admitted:ignored` cases). Implementation was considered and rejected; the step lacked no input the register gives it; no parameter excluded the right item or admitted a wrong one; every available in-design probe was not recovered; and the transcript is not difficult. Reported with its count, bounded to gpt-5.4-mini. Never cited as a design limit or as model-limited |

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

**Case pages** carry the blind page (`--case-pages`) plus:
- step and sub-code;
- the key history;
- the path of every carrier and rival;
- registry size;
- the value's first loss in every other run of its arm group;
- RAG's outcome on the value, or "no independent recoverability evidence";
- the register checklist for the boundary.

**Order of work and blindness, fixed now:**
1. **Right after signing,** in parallel with the Step 2 harness build, the 3a case pages are built from the frozen trace and the register.
2. The pilot is coded and the sub-causes frozen, committed with their hash.
3. The model pre-codes every case from the page only, in a fresh context with no repository memory or result reports. It uses the template fixed at signing, and the frozen sub-cause list is its only added input.
4. **Author pass 1, blind:** a conditional code for each of the 180 cases. Hashed and committed.
5. **V4 codes blind** the same fields from the same pages:
   - every one of the 180 cases, each in a new Antigravity conversation, only after item 4 is committed; the author, who runs V4, opens no V4 conversation or answer before then. Its codes are hashed and committed before item 7, and V4 never sees pass 1 or the pre-codes;
   - a *candidate* cause, a sub-cause that the model or pass 1 gives as primary implementation cause for at least 3 distinct values, is reported only. It selects no case and adds no condition to Step 4(b), whose eligibility is line 480;
   - before the first of the 180, V4's channel is tried on the 20 pilot cases (line 310), which count toward nothing. A change to V4's instruction found necessary there is fixed, with its hash, in a dated note before any of the 180 is staged.

   Hashed and committed. Only the blind kappa (items 4–5) can trigger a codebook revision. Any revision, and the recoding it needs, happens before item 7.
6. **Adjudication audit (V4):** every decision on the audit list, shuffled and unmarked, blind to the v1 label. Agreement is reported over the whole list and over rows the oracles flip. If it is below 0.80, the adjudicated-series figures of the loss trace are also reported under v2.
7. **Reveal.** Only now are the Step 2, 2b and 2c outputs opened to the author; V4 never sees them. Until items 4 and 5 are committed, they are computed only into hashed files. The author's gate review sees only pass/fail and the first differing event, and the go-aheads for 2b and 2c rest on estimates. Any early read is logged with its date and contents.
8. **Final codes.**
   - The pending results resolve each conditional code mechanically, for both coders.
   - Where an oracle or a leave-one-out moves a case's boundary, or where its row result differs between v1 and v2, the author re-codes class and sub-cause. V4 does not re-code: its mechanically resolved blind code is its final code. These cases are reported apart. The author runs V4, so every change the author makes after V4's first packet, at a codebook revision (line 409) or here, is disclosed as made after V4's blind codes could be seen.
   - Pass 2 (author) may revise further. Every change from the conditional code is logged with its reason, as one of three kinds:
     - *mechanical*: set by a rule from a pending result;
     - *forced re-code*: a re-code under the previous bullet;
     - *discretionary*: anything else.
   - Cases that pass 2 newly codes as implementation already carry V4's blind code (item 5). They are reported apart in the agreement.
   - **The anchoring measure** is the discretionary change rate only.

**Agreement:**
- Cohen's kappa on the eight labels;
- kappa and positive agreement on implementation versus not, with unclear counted with implementation, with its lower 95% bound;
- kappa on caused-at;
- sub-cause agreement where both coders code implementation;
- each coder's blind caused-at match rate with the oracle;
- the share of pending cases, and the blind binary kappa on cases with no pending alternative.

Each comes with bootstrap intervals (values resampled), blind and final. The **copy check,** for a machine V4: V4's blind binary agreement and kappa with the model pre-codes are reported beside the author's with each, as a check for a bias the two models share; it switches nothing. **Target:** 0.60 for the author's blind binary kappa with V4, on implementation versus not. If it falls short, there is one codebook revision, recoding, and the fresh sample. A second shortfall is reported as a limit. **The 0.40 design-limit rule takes the lower of two lower 95% bounds: the author's blind binary kappa with V4, and with the pre-codes. If it is below 0.40, no loss is reported as a design limit on these codes.**

**V4 fallback.** If V4's blind codes are not in by the date set at signing:
- Step 4(b) is skipped;
- the stopping rule's agreement condition is reported as not met;
- the oracles stay on v1;
- only (a) conformance repairs proceed among the repairs;
- WD and the A2 contracts are still judged for admission, on the author's codes. This is disclosed.

**Stopping rule.** The study ends when:
- every sampled case has caused-at, class and evidence;
- agreement is computed;
- unclear is at most 10% of cases, or the excess is reported.

**Outputs:**
- surfaced × caused tables per arm, with the decomposition, the probe results and the WD result beside them;
- the joint table of the first-loss step against RAG's outcome;
- defects found among losses and among passes, in both directions;
- 8–10 worked examples, among them the implementation-side walkthrough of ES2009b (3b) against Appendix B, whose line ranges and episodes stay stable;
- the claims register filled in.

**Bound rule for verdicts** (development verdicts and admission). A verdict is first computed on the recorded outcomes. For each mechanism, the cases that weaken it are:
- its unrepaired implementation cases;
- its unclear cases, including disagreements and *held* cases;
- its passes that rest on a defect, or whose defect status is unclear.

These are scaled to the mechanism's whole case population per run, using the sample share at the upper end of its 95% bootstrap interval. For runs with no coded sample, the shares are borrowed, and this is disclosed:
- the 2c, C and A1′ runs take A1's 3a shares;
- the A2 leave-one-out variants take A2's;
- A0 runs take their model pre-code shares;
- Step 5's runs take the shares of 3b's coded run (the final configuration's r1), for both A1-ref and the final configuration. **Cases coded implementation because the mechanism under test is their alternative are that mechanism's measured effect.** They are left out of the shares, and never counted as recovered on the comparator side. These are:
- for WD, its (iv) cases;
- for a (b) repair, the cases of the cause it repairs;
- for an A2 contract, the cases its leave-one-out recovers.

The bounds:
- **Doesn't work** stands only if it still holds when the weakening losses are counted as recovered.
- **Works** stands only if it still holds when the weakening passes are counted as lost. In an on/off contrast, it must also hold when the comparator's weakening losses are counted as recovered.
- Known-bug incidence enters both bounds the same way.
- Otherwise the verdict is **can't tell (defect-limited).**

Both verdicts are reported. **The bounded one counts, including for admission.** It is the dry run of the rule the registration carries into Phase D3.

## Step 4: one bounded repair round

**(a) Conformance repairs** (the code contradicts the register):
- They are made whatever their size.
- Each is accepted on a failing-then-passing reproduction test, the conformance tests and zero incidence. **Acceptance is admission.** The loss trace is reported, not used to accept.

**(b) Implementation-choice repairs:**
- **Eligibility:** at least 3 distinct gold values on which the author's final code and V4's final code agree: class implementation, the same caused-at, and the same sub-cause. A cause whose remedy has its own admission rule (WD) is not eligible.
- **Ordering:** within one repair per boundary, plus one A2-only slot, in one round. Eligible causes are repaired in order of distinct values. Without oracle results, causes are ordered by distinct values from the agreed codes alone.
- **"Not approved"** is allowed only for infeasibility within the bound, or for cost above the estimate. Each such decision is recorded with its reason.
- **Value fixed in advance:** the alternative and any parameter value are fixed in a dated note, from a design argument, before any repaired run or recovery computation. No value is picked by recovered rows.

**Checking a repair:**
- **Configurations:**
  - **C** is A1 plus every accepted (a) repair and every admitted state-logic repair. **A1′** is C plus the repair under test.
  - **C2** is C plus the four contracts. **A2′** is C2 plus an A2-only repair under test.
  - In the harness, C and C2 contain only repairs that need no LLM call; any others are listed.
  - Every (a) and state-logic repair is settled before the shared live C set runs. A later change to C re-runs it.
- **State-logic repairs** are checked in the harness on the A1 runs that pass the gate (not A0), paired, at $0. Prediction:
  - net recovered rows at the boundary, summed over the runs where the cause occurs, are above zero and come from at least 3 distinct values;
  - no run has more rows lost at the status step under A1′ than under C;
  - there is no new incidence.

  A repair that reaches an LLM seam inside the harness is checked as an LLM-seam repair.
- **Read-path repairs** are first screened by paired answer replay (`replay-ami-answers`, state_first) over the three A1 dumps, about $2.4 per dump. Prediction: fewer losses at `key_reached` or `in_payload` in at least 2 of 3 dumps, and no question newly lost. A failed screen ends the repair. A repair that passes is checked as an LLM-seam repair, with its endpoint at the `key_reached` and `in_payload` rows of the coded values.
- **LLM-seam repairs** use three A1′ runs interleaved with three fresh same-period C runs. One C set is shared by every LLM-seam repair in that period.
  - **Endpoint:** the rows of the distinct values coded with the cause, at its boundary, paired by value and checkpoint.
  - **Prediction, fixed here:**
    - net recovered rows on those values, summed over the three pairs, of at least 5, from at least 3 distinct values;
    - every A1′ run strictly better than every C run on those values (exact one-sided p = 1/20);
    - the whole boundary's mean loss not higher by more than 13 rows;
    - no new incidence.
- **A2-only repairs** are checked on the A2 runs that pass the A2 gate:
  - in the A2 harness, or with re-run support verdicts (about $0.2 per run), with the state-logic prediction and C2/A2′ in place of C/A1′;
  - a repair that changes routing or extraction uses three A2′ runs against three same-period C2 runs (about $21, on its own go-ahead), with the LLM-seam prediction. Its contract's leave-one-out for admission then runs on the A2′ runs that pass the A2 gate; otherwise the repair is not checkable.

  Without a passing A2 run, the repair is *not checkable*.
- **If a prediction fails, or the check is not possible,** the result is *not shown*. The switch stays off, the cause stays an unrepaired implementation defect, and there is no second attempt.

**Admission to the final configuration, fixed here.** This is plan 23's verdict rule for Phase C. It amends plan 23 line 269, and it is signed before any input it governs exists. Every admission except an (a) repair's uses the **bounded** verdict (Step 3).
- **(a) repairs:** acceptance is admission.
- **WD:** the Step 2c rule.
- **Each A2 contract,** from the leave-one-out in the A2 harness, paired, on gate-passing runs. With n such runs, n must be at least 2. *Works* when:
  - switching the contract on gains at least 3 distinct values net in every gate-passing run;
  - no run is net negative;
  - parked or open-conflict rows do not increase among the values that at least 2 of 3 A1 runs store with the right status.

  With fewer than 2 gate-passing runs, the contract is *not checkable* and not admitted. An A2-only repair enters only together with its contract, and only if that contract is admitted. The contract's leave-one-out for admission is then computed with the repair on.
- **(b) repairs:** a passed Step 4 check.
- **Only *works* is admitted.**
  - An A2 contract that is not admitted is a design alternative not taken, and its losses are not recoded.
  - If WD is not admitted, its cases keep their codes under the WD-cases rule; (iv) cases stay unrepaired implementation choices.
  - A (b) repair that fails its check, is not checkable or is not approved leaves its losses unrepaired.

**Out of scope:** design changes, for example a new key model, need their own dated amendment or are future work. Defects found after Step 5 are documented, not fixed.

## Step 5: ES2009 development runs (after Steps 1 and 4)

- **Arms:** three runs each, on the new suite version, with the Step 0 instruments on:
  - A0;
  - **A1-ref:** A1 plus every accepted (a) repair and every admitted (b) repair that is not A2-only. A1-ref replaces A1 as the no-contract reference for every contract verdict, here and in Phase D3;
  - where it differs, **the final configuration:** A1-ref plus each admitted contract and its admitted A2-only repairs. If the conflict contract is admitted, it waits for the conflict decision; the other admitted contracts run.

  RAG runs in the same period, three runs.
- **Disclosure:** the admitted repairs enter A1-ref together. State-logic repairs were checked cumulatively in C. Each LLM-seam and read-path repair was checked against C alone. Their combination is first run here, on ES2009, and Step 5's incidence check covers it.
- **Framing:** a repair chosen on EL2020 is **not** replicated or confirmed by ES2009, a second development series already used for defect finding. Implementation defects first found in 3b are not repaired; they enter the bound rule.
- **Analysis:**
  - incidence;
  - answerable-only;
  - the loss trace with the adapter;
  - probes (i) on 3b's run;
  - Step 3b.

## Rules fixed by this amendment, before any outcome

Each rule below is fixed as written in its step:
- the three end states;
- every class definition and class rule (burden, pending results, retrospective design, WD cases, autonomous-arm conflicts, unclear, recoverability);
- the candidate causes;
- the caused-at rule;
- the oracle definitions, which a failed gate never changes, and the gate caps;
- the probe conditions, the dated probe note, the recovery rule and the mapping;
- the WD rule;
- the sample, the pilot, the fresh sample, and the order of work and blindness;
- the double-coded set;
- the agreement measures and the 0.40 rule;
- the copy check and the V4 fallback;
- the audit list and v2;
- the stopping rule;
- the bound rule;
- repair eligibility, ordering, configurations, checks and the limits on "not approved";
- the admission rule;
- the mechanism mapping;
- the frozen inputs and their version rules;
- the scope limits.

**Every result is reported whatever it shows:**
- every ceiling, probe, code table, repair decision and verdict, recorded and bounded;
- the counts of unrepaired implementation, unclear, and design-or-model-not-separated cases;
- any statement that a loss comes from the design, made only where the codes say architectural or trade-off on 94c049d text, with the binary kappa's lower bound at or above 0.40 (line 430: the lower of the author's two blind bounds).

## Cost and time (nominal list price; each paid step gets its own estimate and go-ahead)

| Step | Paid | Agent work | Your time |
|---|---|---|---|
| 0 | $0 | 1–2 days | approve the registers and notes |
| 1 | re-judging the twelve EL2020 cycle-2 runs, about $5 (9 PM at about $0.5, 3 RAG at about $0.2); cycle-1 runs only if reported under the new gold; value changes have their own estimate | adapter 3–5 days | the B3 decisions |
| 2 | about $3 (A2 live support calls and embeddings) | harness 2–4 days; analyses about 2 days; adjudication rounds | gate pass/fail only |
| 2b | about $24–37: (i) (a)–(c) about $8, (d) about $5–11; (ii-r) about $4–7; (ii-h) about $5–8; (iii) under $0.5; the 3b run about $2 | 1–2 days, plus adjudication of about 2,500–3,000 probe outputs | — |
| 2c | about $20 (3 WD + 3 fresh A1) | adjudication rounds | — |
| 3 | $0 API | pages, pre-coding | pilot 1–2 h; pass 1 about 10–18 h (210 cases at 3–5 min); pass 2 about 3–6 h; pass examinations 2–3 h; fresh sample if needed 3–5 h: **about 17–34 h**. V4 (Gemini in Antigravity): the 20 pilot cases of the channel trial and the 180 cases, one conversation each (about 1–2 min each to stage, run and collect), plus 8 audit packets of about 60 decisions, plus 60 cases if the fresh sample is triggered, and the 180 again with the revised list if a codebook revision is: **about 4–8 h** of your time, about 3–6 h more on the revision branch, $0 API |
| 4 | state logic $0; read-path screen about $7 per repair; LLM seam: shared C set about $10 once, plus about $10 per repair; A2 routing or extraction repair about $21 | per repair | approve each repair |
| 5 | A0 + A1-ref about $14–17; RAG about $1; a final-configuration arm about $8 if any contract is admitted | adjudication rounds | — |

**Total:**
- **Scheduled steps** (1, 2, 2b, Step 5's A0, A1-ref and RAG): about $47–63.
- **Add-ons, each on its own go-ahead:**
  - Step 2c, about $20;
  - the final-configuration arm, about $8;
  - a read-path screen, about $7 per repair;
  - LLM-seam checks, about $10 once plus about $10 per repair;
  - an A2 routing or extraction repair, about $21.

**Against plan 23's budget.** Phase C has spent about $32 of plan 23's $60–100.
- The scheduled steps take it to about $79–95.
- With Step 2c, about $99–115.
- Any further add-on then goes past $100.

Each such item needs its own go-ahead against plan 23's ceiling.

## Decisions needed from you

1. **Sign this amendment** with its Step 0 registers, notes and audit list. What decides outcomes:
   - the class rules (retrospective design, the model as a held-constant control, pending results);
   - the probe rule;
   - the WD rule;
   - the admission rule;
   - the bound rule;
   - the sample.
2. **The V4 second coder:** Gemini, a machine coder (line 116), with the date for its blind codes.
3. **The B3 gold decisions:** P1-8 first.
4. **The ES2009 adapter choices** (Step 1).
5. **Step 2c (WD):** yes or no. If no, its cases are coded unclear and P23:264 is withdrawn.
6. **The open conflict decision** for the autonomous arm. It may be taken at any time, but it never reclassifies losses observed before it.
7. **Archive the review and verification records in the repository:** the ten workflow records named under "Already read", with their hashes. Yes or no.

## Unchanged

- The Phase D1 entry gate, the freeze, the Phase D3 registration, the held-out series rules and the confirmatory study.
- No tuning for overall score.
- ES2009 and EL2020 remain development data.
