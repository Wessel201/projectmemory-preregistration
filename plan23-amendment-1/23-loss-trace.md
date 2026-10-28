# Loss trace: codebook (plan 23, B2/D3)

**Files:**
- `23-loss-trace.py`: the script, offline, no API calls.
- `23-loss-trace-adjudications.yaml`: the adjudications.
- `23-loss-trace.json`: the output.
- `23-loss-trace-results.md`: the results.

It replaces the cycle-1 lexical failure coder (bug 11). That coder's counts were unusable because of:
- its value-only word test;
- its 12-claim cap;
- its use of end-of-run state;
- its fact join through `supporting_evidence` (bug 2).

## Unit and population

- **Unit:** one gold row (one gold value at one checkpoint) in one run. EL2020 has 159 rows over 65 values and four checkpoints.
- **Every row is traced**, so each step has two counts: rows that reached it and rows that passed it.
- **Questions are a derived view** (`questions` in the output), not the unit.

| Kind | Gold rows | Passes when |
|---|---:|---|
| current | 133 | it gets through the whole chain below |
| candidate | 1 | as current, any modality, expected status `current_unconfirmed` |
| ruled_out (R items) | 16 | carried by a negative asserted claim and stored as a REJECTED fact at k (a ruled-out record, or a demoted current fact) |
| demoted | 9 | a value the gold marks rejected after it was current or a candidate (a rejected row whose id does not start with R): passes when no fact holding it is current at k. Only the state is traced, in two steps, `was_stored` and `no_longer_current` (outcomes `ok:demoted`, `ok:never_stored`, `current:still_current`) |

## The chain

The first step that fails is the row's **loss**. Its boundary is the coarse label.

| Boundary | Step | Passes when | Sub-codes when it fails |
|---|---|---|---|
| extraction | admitted | the cited span went to the extractor (`extract_to_state`, `extract_as_candidate` or `evidence_only`, all of which the system extracts), or a claim from another span carries the value | `ignored` (the gatekeeper gave a cited span another policy); `span_not_seen` (no gatekeeper decision for any cited span, or the gold line maps to no span) |
| | carried | a claim extracted by checkpoint k carries the value | from the cited spans or the spans next to them: `extracted_after_checkpoint` (a carrier exists, extracted later), `sibling_value_only` (a claim matches strongly, but the text belongs to another gold row), `split_across_claims` (claims with one subject carry it only together); from the cited spans proper: `no_claims_from_cited_span`; otherwise `claims_without_the_value` |
| | polarity | ... with the needed polarity (negative for ruled_out) | `negated_value_read_as_rejection` (the gold value or an alias contains a negator, e.g. "not much better than before", and the value was extracted only as a negative claim); `carried_only_positive` / `carried_only_negative` |
| | modality | ... asserted, read from the claim's modality field (candidate: any modality) | `carried_only_<modalities>` |
| filing | filed | such a claim's last logged evaluation by k filed it under a key | most common of: `cycle2_parked_<reason>` (A2 checks, dated by the parking step); `undefined_key` (bug-5 repair; in A0 an undefined key, including the literal key `null`, is filed and flagged `bug5`); `no_key`; `not_evaluated` |
| | proposed | a proposal raised by k carries the value (`new`/`supersede`; `reject` for ruled_out) | from the filed claims' last logged evaluation: `another_value_won` (it raised a proposal for another value); `own_value_not_matched` (it raised one for its own value, whose stored words alone do not match: the pair goes to adjudication); or by its reason: `tie_left_as_conflict`, `same_meeting_conflict` (A2: rival values or challengers in one meeting), `judged_same_as_current`, `outranked_dissent`, `current_value_ranks_higher` (bug-3 repair), `hedged_same_value` (bug-4 repair), `hedged_negation`, `no_positive_claim_left`; else the raw result type |
| | applied | a fact carrying the value was created by k (current/candidate: not a ruled-out record; ruled_out: a REJECTED fact) | `proposal_expired`, `proposal_pending_review` (the final status of the proposals that passed), `fact_not_found` |
| state maintenance | current | that fact is current at k (ruled_out: rejected at k) | `displaced_by_other_gold_value` (the fact that replaced it holds another current or candidate gold value of the checkpoint, adjudicated so or strong for it under the matcher and sibling rule; `displaced_by` names it); `overwritten_by_non_gold_value` (a later gold value further down the chain is recorded as `later_gold_in_chain`); `rejected`; `rejection_after_checkpoint`; demoted: `still_current`. `not_current` cannot occur under the replay |
| | status | ... with the expected status at k | `stored_as_<status>` |
| reading | key_reached | a key the reader resolved holds a stored fact with the right status | `other_keys_resolved`, `no_key_resolved` |
| | in_payload | the reader got that fact as an answer fact | `near_match_only` (only disclosed as a near match, when the answer was "unknown"); `key_resolved_fact_not_given` |
| | answered | the question is scored correct (the report's prose `correct`) | `answer_or_judge` |

**Outcomes for rows that pass:**
- `ok:None`: passed reading too;
- `ok:stored_not_asked`: stored with the right status, but no single-value question asks for it at k;
- demoted rows: `ok:demoted` or `ok:never_stored`.

**Reading** is traced only through **single-value questions**: a current_state, candidate_decided or rejection question whose expected answer is exactly one gold value.
- This includes `EL2020a_rejected_so_far`, which asks for R01 only.
- Excluded: the other `rejected_so_far` questions (2–8 values), `dates_current` (3 values) and change-over-time (8 values).
- **Per question:** each asking question is traced on its own, and the row takes the question that got furthest. A row passes reading only if one question resolved the key, got the fact and was scored correct.

**The "last logged evaluation".** Some early returns of `evaluate_claim` write no `conflict_detection` row: no key, cycle-2 parking, the D9 support parks, the type-check re-route (logged only to `filing_type_check`), and the bug-1 "already recorded" return. Parking is therefore dated separately: by the `claim_support_check` row whose reason the claim records (checked against the claim's value when reasons repeat), or by the `filing_type_check` row that parked it. A parked claim may still carry a later logged noop row; parking by k takes precedence.

**Flags on each record:**
- `credit_without_state`: some single-value question asking for the row was scored correct, although no stored fact with the value and the right status was among that question's answer facts. It is computed per question, whatever step the row was lost at.
- `carrier_source`: `cited_span` (the cited span or a span next to it) or `other_span`.
- `support`: the texts the pass rests on, for the steps carried, proposed, applied and status (for a demoted row, the texts that keep it `still_current`). They feed the adjudication queue.
- Defect flags, with the `23-bug-incidence.py` definitions, counted only for events by k:
  - `bug2_cites_span_without_value`: no positive claim on the fact's key with its value in a cited span; ruled-out records are exempt, since they cite their negation span;
  - `bug3_replaced_in_own_meeting`: replaced by a different value with the same `valid_from`, the successor created by k;
  - `bug4_superseded_by_same_value`: the successor created by k;
  - `bug5_undefined_key`;
  - `bug13_validity_inverted`: the ending happened by k.

  Flags are taken from the facts that carry the value and were created by k. Plan 23 calls them "can't tell" markers.

**Evidence questions** (in `questions`) record:
- whether the value was stored;
- which meetings the stored fact cites;
- whether one of them is the meeting the gold names.

**Unknown and noise questions** carry no gold value. They record how many keys were resolved and facts given, and whether the answer was credited.

## Checkpoint state (transaction time)

- **Phase:** a step's phase is the number of checkpoints already questioned. The script refuses a run where a checkpoint has no questions.
- **Re-extraction:** a span whose extraction returned nothing is extracted again at the next meeting, so a claim is dated by its extraction call.
- **Replay:** accepted proposals are replayed in creation order against the dumped facts (also in creation order), as the projection applies them:
  - a rejection of the key's current value demotes it;
  - any other accepted proposal creates the next fact;
  - a positive proposal also supersedes the current fact.

  This gives every fact its creation phase, its creation order and every demotion its phase. A fact is dated by its proposal's phase, which is right under the structural value policy: a proposal is accepted in the phase it was raised in, or never. The script checks that the replay aligns, and falls back to a key/value/type ordering otherwise (`placement` in the output).
- **Status at k:** a fact keeps the status it was created with while it is current; a status change creates a new fact. The dump only shows the status at the end of the run. A fact no longer current at the end takes its status from its proposal's final reason.

| Check (recorded in the output as `pack_check`; nine runs; it agrees with an independent replay by the round-1 auditor) | Result |
|---|---|
| Per question and resolved key, the rebuilt current facts against the non-rejected facts the reader got | 9551 / 9551 |
| Status at k of every fact the reader got, answer facts and near matches, against its pack status | 8430 / 8430 (answer facts alone: 7993 / 7993) |
| Replay alignment | every run, no fallback |

## Matcher

The matcher **proposes**; adjudication decides (next section).

**Normalisation:**
- lower case; accents and punctuation removed;
- numbers kept; number words and compound numbers become digits;
- an ordinal becomes a digit only next to a month ("twentieth of April");
- an anonymisation placeholder ("PERSON3", "[ORGANIZATION6]") is one digit-free word;
- a possessive "'s" is dropped;
- a hyphen joins a one-letter part ("e-mail" = "email"), and a "re-"/"pre-" prefix is dropped;
- a light suffix strip is applied alike to both texts, undoubling "dropp" to "drop", with a few irregulars (used = use, based = basis);
- stop words and pronouns are dropped.

**A number in the value must occur in the text,** unless an alias matches. The determiner "one" ("one shared paper") is exempt.

| Level | The text contains |
|---|---|
| strong | a gold alias of two or more content words, as a phrase (within the alias's length plus two words); or every content word of the value (a one-word value only if the text has at most two content words); or three quarters of a value of four or more content words |
| weak | a one-word alias, the one-word value inside a longer text, or half the value's content words |

**Sibling rule.** Gold values of one checkpoint share words and aliases (`gold_alias_collisions` lists each pair once: a pair where a value or alias of either strongly matches the other).
- A text does not carry a row when every part of the value it contains (each value or alias it contains, and its covered value words) is part of a longer value or alias of another row that it also contains. For example, "based on pause durations" is F59's, not demoted F36's.
- A part shared equally with another row stays with this row when the text is local to this row and not to the other; otherwise the match is weak.
- Ignored as rivals:
  - a row whose adjudication says the text does not carry it;
  - a value and the ruled-out alternative cited from the same gold line.
- **Upgrade:** a one-word value ("Romanian"), or a distinctive one-word alias (a name, number or date: "Antrecorp", "23rd"), in a local text that no other row shares counts as strong. This acts in the strict bound too.

**Locality and identity:**
- A text is local when it equals the object, or the subject + predicate + object, of a claim extracted from the cited span or a span next to it in the same meeting.
- Claims are matched on their object; local claims also on subject + predicate + object.
- A proposal or fact holding the value of a carrier claim with the needed polarity and modality, under a key that claim was evaluated under by k, carries the value too. This applies when the claim's object itself carries it, or when the key's words plus that value still match. A value stated only through the subject ("ASR | considered | worst component") is not passed on to an unrelated stored object.

**Bounds:**
- **Strict:** strong local matches.
- **Lenient:** also strong matches elsewhere, and weak local ones.
- The lenient bound is not a true upper bound. A paraphrase sharing too few words with the value and its aliases never matches; round 3 found one (F36, "longer duration indicates end of sentence").

## Adjudication

- **Queue:** the run repeats until no item is open. The output records `queue_open` and `primary_series_complete`. Items not yet decided are:
  - the `support` texts of every strict row, per step, unless one of that step's texts is decided true;
  - for a row whose lenient outcome differs from its strict one, all texts the lenient bound counted for it;
  - the wording pairs of either bound:
    - every value stored under the key by k when a carrier was judged the same as the current value;
    - the winning value when it shares words with the gold value;
    - the claim's own value under `own_value_not_matched`.
- **Precedence:** a decision on a text overrides the matcher in both bounds, before identity propagation.
- **Claim level:** a decision on either of a claim's two texts (object, or subject + predicate + object) decides the claim.
- **Format:** `{adjudicator, note, decisions: {fact_id: {text: true|false}}}`. Its sha256, adjudicator and number of decisions are in the output.
- **Standard** (given verbatim to every adjudicator): a text carries the gold value when a careful coder would say it states that value, so that an answer built from it would be judged correct for a question asking for that value.
  - A paraphrase, or a more specific or more complete statement, carries it.
  - For a value of two or more independent parts, one part alone does not, even if it is a gold alias. Leaving out a minor qualifier does not prevent carrying.
  - A different value, a rival option, a sibling's value or the topic words alone do not carry it.
  - A ruled-out option carries when the text names it; polarity is judged elsewhere.
  - Texts are read with their contexts (subject, predicate, key). When a text means different things in different contexts, its most common context decides.
- **Protocol:** two independent model adjudicators (Claude subagents) decide each item, and a third decides where they disagree. The decisions are **model adjudications, not human**. A human second coder samples them in V4.
- **Primary series:** the strict bound with the queue empty. The raw strict and lenient bounds (no decisions) are reported next to it.

## Verification record

**Round 1, v1 (23 October; 29 agents):**
- **Hand-traces:** 48 rows, traced blind by three coders. They agreed with the script on the first failing step for 38 (37 on step and sub-code). Of the 10 step disagreements, the script was wrong on 9 (all matcher causes) and right on 1. The eleventh difference was a sub-code ambiguity (F06).
- **Matcher audit:** strong matches were 53% right and 32% wrong or a sibling's value; wrong matches were 7.5% of local pairs but 72.6% of non-local ones.
- **Findings:** 20 substantive findings, all reproduced by skeptics, plus 9 minor ones. v2 fixed or documented them all.

**Round 2, v2 (24 agents; held-out A2 r1):**
- **Hand-traces:** agreement on 15 of 24 rows. The disagreements were mostly fragment aliases, which counted in the strict bound and could not be adjudicated.
- **Strict precision:** 3–6% of texts wrong (A2: 74% right, 22% fragments).
- **Findings:** 13 reproduced findings. v3 fixes them; the main change makes adjudication complete.

**Round 3, v3 (35 agents):**
- **Adjudication:** 637 items (411 open, plus 226 earlier decisions re-checked). The two adjudicators both decided 635 and agreed on 615 (96.9%, kappa 0.94). 22 went to the tie-break (20 disagreements, 2 missing one decision), and 5 earlier decisions changed.
- **Code review:** 3 more reproduced defects (the sibling rule ignoring a sibling's adjudication; `another_value_won` for the claim's own value; sub-codes ignoring claim-level adjudication). v3.1 fixes them, plus four latent points.
- **Hand-traces on held-out A2 r2b and r3:** agreement on the first failing step for 21 of 24 rows. The three disagreements:
  - two main-decision-versus-part calls on compound values, F32 and F82, where the double adjudication and the hand coder differ;
  - one paraphrase the matcher cannot propose (F36).
- **Fixpoint:** one more round of 33 newly decisive texts (full agreement), after which the queue is empty: 670 decisions in all.
- **Result notes:** recomputed and challenged by three further agents; their corrections are applied (`23-loss-trace-results.md`).

## Second coder (V4)

`--case-pages DIR --sample N` writes N blind case pages per run. The sample is deterministic (ordered by a hash of run, value and checkpoint). Each page contains:
- the gold value and its aliases;
- the cited span with the gatekeeper's policy;
- the claims from the cited and neighbouring spans, the claims from those spans extracted only after k, and claims from other spans sharing words with the value. Each claim shows subject, predicate, object, its parking by k and its evaluation trail up to k;
- the facts at k under the keys those claims were evaluated under, or sharing words with the value, with status at k;
- the reader's single-value questions, with resolved keys, answer facts, near matches, the answer and its score.

The page hides the trace's verdict and states evaluation reasons without the repair or contract prefixes. The arm is not fully hidden: repair-only and contract-only outcomes (hedged same value, parking, same-meeting conflicts) show that a run is A1 or A2. The coder enters the first failing step and sub-code; agreement is computed on the step.

## Limits

- **Value-based:** the trace follows the value, not the gold's state key. Generated key labels are not evaluation targets, so "applied" means any fact holding the value, whichever claim or key produced it.
- **Steps are necessary conditions in order.** The trace locates the first missing condition, not a causal path. For example, `proposal_expired` gives the proposal's final status, not what expired it (in A2, often a later same-meeting conflict).
- **Compound values:** a value split by the extractor across claims with different subjects is coded `claims_without_the_value`, and only a one-subject split is `split_across_claims`. Whether a part is the main decision or a qualifier is an adjudication call, and the round-3 hand coder disagreed on two of them.
- **Adjudications are keyed by text per value** and apply in every run. A text that means different things in different runs is decided by its most common context.
- **`overwritten_by_non_gold_value`** usually means unrelated content was filed under the same key (wrong routing). It is counted at state maintenance, because that is where the value was lost.
- **Scope:** EL2020 only. There are no collection keys (the script counts collection-key evaluations as a join warning), and the structural value policy is assumed (facts are dated by their proposal's phase). ES2009 gold cites decision-annotation passages, not transcript lines, and needs its own provenance join.
