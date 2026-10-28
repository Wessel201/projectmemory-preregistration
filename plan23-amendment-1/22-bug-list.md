# Clear bugs found by the disproof review (verified at c2109bf)

A finding counts as a clear bug only if two things hold:

1. The code at the run revision contradicts its own docstring or comments, or the design the thesis states.
2. The run outputs show it happening.

The consolidating session checked everything in sections A and B on 22 October 2026, except where a line says "reviewer". Section D lists design choices that turned out badly; they are not bugs.

## A. Bugs in the evaluated system

### 1. Negating the current value can never take effect

- **Code:** `resolution_service.py:276-315`. The relevant line is `affirmed = any(C(p.value) == cur_canon for p in positives)`. The claims it checks come from `conflict_service.py:136`: every claim on the key, with no status or time filter (`repositories.py:196-204`).
- **Why the branch is dead:** the claim the current fact was projected from is always among `positives`. So `affirmed` is always true, and both the reject branch and the exclusion branch are unreachable.
- **Contradicts:** the engine docstring ("Gated negation — an ASSERTED negation … unaffirmed, yields exclusion") and Chapter 4's D3 and D5.
- **Runs:** across the 13 evaluated state dumps, "Current value explicitly negated" occurs 0 times and "Ruled-out value recorded as rejected" occurs 559 times.
- **Effect:**
  - Current state can change only by supersession, never by retraction.
  - The same value can end up both rejected and current (reviewer: r1 `technology.voice_recognition`).

### 2. Facts take their evidence, confidence and authority from the oldest claim on their key

The source of those three fields should be the claim that supplied the fact's value; instead it is the oldest claim on the key.

- **Code:**
  - `conflict_service.py:228-230` evaluates every claim oldest-first (`repositories.py:181` orders by `source_time`, then `created_at`).
  - `_create_proposal` (`conflict_service.py:499-551`) copies `claim.evidence_id`, `claim.extraction_confidence` and `claim.source_authority` from the claim that triggered the proposal. The fact's value is `resolution.winning_value` and its time is `winning_source_time`, both from a possibly different claim.
  - `repositories.py:354-363` returns the existing open proposal for the same key, value and type, so the first (oldest) trigger wins.
- **Contradicts:** D9, under which provenance links a fact to the evidence that supports it.
- **Runs:**
  - In r1, all three facts in the universal-remote chain carry confidence 0.92, whichever claim won.
  - Reviewer: 53–59% of current scalar facts in the ES2009 autonomous runs, and 34–39% on ELITR, cite a span that does not contain their value.
- **Effect:**
  - Provenance is wrong.
  - The change template, which counts facts whose earliest evidence is the latest meeting, sees only a fraction of new values (reviewer: 13/51, 11/44, 9/41).
  - Evidence answers name the first meeting.
  - The flagship trace in Chapter 6 is affected.

### 3. A rival from the same meeting can supersede the current value, even with lower confidence

- **Code:** `resolution_service.py:373-405`.
  - `disagree` excludes the current value, so the current value's own claims never compete.
  - Eligibility is `source_time >= valid_from`, and all claims from one meeting share one timestamp (bug 6).
  - `_best` then picks among the challengers only.
- **Order dependence:** when there is no current fact (rule 3), an equal-time clash between values becomes a conflict. Once a current fact exists (rule 4), there is no such check, so the outcome depends on evaluation order.
- **Contradicts:** Chapter 4's D5: "same-meeting rivals … are decided by extraction confidence and the losers never become facts".
- **Runs:**
  - In r1, `product.remote_control.is_universal` goes 'universal remote control' → 'universal' → 'electronic device'. The last two changes both happen within ES2009b, and the 'universal' fact has zero-length validity. 'electronic device' is the current value at the end.
  - Reviewer: 5–11 such replacements per ES2009 run, 15–19 per ELITR run.
- **Origin:** commit 6aac7b8 (29 Jul) set `valid_from` from the claim's source time. Table 4.3 lists that commit as a fix.

### 4. Unchanged values get "superseded" by themselves

- **Code:** `resolution_service.py:318-331`. When a key has only hedged claims, the engine returns "new" with the most recent hedged value and never compares it with the current fact. Dispatch then turns it into a supersede proposal.
- **Runs:** in r1, 25 of the 172 supersessions replace a value with the identical value (reviewer: 25/20/21 for r1–r3).
- **Effect:** inflates the supersession counts that Chapters 5 and 6 report (172/167/167, and "146/139/140 sharing evidence").

### 5. Claims are filed under unvalidated key hints from the model, including the literal string "null"

- **Code:** `extraction_service.py:621` (`state_key = claim.state_key_hint`). The hint is never checked against the registry.
- **Contradicts:** D4 ("matched to an existing concept or parked") and Chapter 1 ("new concepts admitted only through review").
- **Runs:** in r1, 14 of 334 facts sit under keys with no concept definition. Several are under the key 'null' ('battery', 'lithium', 'teletext support'), and one is under 'remote.remote?'.

### 6. Valid time is ingestion time; meeting dates never reach the system

- **Code:** `extraction_service.py:356` uses `artifact.created_at_source or artifact.ingested_at`. No evaluation runner or script sets `created_at_source` (git grep at c2109bf finds no hits).
- **Contradicts:** D7's two clocks, and Chapter 3's "validity fields set from meeting time".
- **Runs:**
  - Every fact's `valid_from` equals its meeting's ingestion time.
  - All four ES2009 meetings fall within 17 minutes on 19 September.
  - ELITR facts are dated 23 September 2026 instead of March–April 2020.
- **Effect:** makes bug 3 possible, and "valid time" carries no information about the domain.

### 12. An accepted proposal blocks the same proposal for good (found in Phase B, 22 October)

- **Code:** `create_proposal` (`repositories.py`) returns any existing proposal with the same `proposal_key` (key, value, type), whatever its status. Once "supersede to X" was accepted, a later "supersede to X" returns that accepted proposal, so nothing is re-applied.
- **Contradicts:** the idempotency comment it sits under ("a matching OPEN proposal"), and D6's lifecycle, under which a value can be reinstated.
- **Runs** (`23-bug12-incidence.py`, `.json`, written by a reviewer agent): it fired in all 13 runs checked. It blocked 72 supersessions: ES2009 autonomous 24, EL2020 36, reference-informed 12. Only 3 of the 72 were fresh re-affirmations in a later meeting. The other 69 were old claims evaluated again, which is bug 3's same-meeting oscillation.
- **Effect:** bug 12 hid most of bug 3. With bug 12 repaired alone, same-meeting rivals oscillate on every pass. Its repair must therefore go with the bug-3 and bug-4 repairs.

### 13. Proposals are confirmed against a state they were not computed for (found in Phase B, third review)

- **Code:** the runner's confirmation step (`runner._internal_confirm`, both value policies) accepts pending proposals in creation order, without checking them against the current state. `ProjectionService.apply_proposal` then supersedes whatever is current. Two kinds of proposal reach it:
  - proposals left pending at an earlier checkpoint, because the gate did not yet accept them (the gold-backed gate waits for the gold to cover a value);
  - proposals from a partial view: cold-start mapping and release evaluate each claim as it gets its key (`re_evaluate_claim`), before the rest of the meeting's claims are on it, and nothing evaluates the key again before confirmation.
- **Contradicts:** D6, under which a proposal is the reviewable form of a resolution of the key, and the engine's own outcome for the full claim set.
- **Runs:** an older, weaker value can replace a later decision at a checkpoint with nothing new said, leaving a validity that ends before it starts. In the cycle-1 dumps such facts occur in 4 of the 5 reference-informed runs (one each) and in none of the autonomous runs (`23-bug-incidence.py`, count 13). That is a lower bound: a stale application whose dates happen to be in order is not counted.
- **Effect:** wrong checkpoint states in the reference-informed arm. Under the bug-1 repair, partial views also let a value be rejected at a checkpoint and come back one pass later.

## B. Bugs in the evaluation harness and analysis scripts

### 7. The judge is never told that a rejection item's option was rejected

- **Code:** `scorer.py:1007-1016` (`_build_gold_answer`) sends only "Must include: <option>", because rejection items have no `expected_status`.
- **Effect (reviewer):**
  - On R06 (Antrecorp), all six answers correctly said the option was excluded, and all were scored wrong.
  - On R07 and R03, answers saying the option was "not ruled out" were credited.
  - Corrected, the EL2020 focused rejections are 6/24 vs 17/24, not 4/24 vs 18/24.

### 8. The "resolver embeddings" ablation switch reaches beyond the resolver

- **Code:** `build_embedding_client()` returns `None` for every caller (`embeddings.py:129-137`). The callers are `answer_service.py:132`, `retrieval_service.py:94` and `state_key_resolution_service.py:268`, so the switch also turns off answer-time retrieval and the relevance gate.
- **Effect:** the ablation does not isolate the resolver. In the traces, the resolver gave keys for 1 of 24 questions, but 22 of 24 answers carried keys.

### 9. The wrong-key diagnosis is true by construction in cold-start runs

- **Code:** `_diagnose` in `state_dump.py` labels a failure `retrieval_wrong_key` whenever the resolved keys miss the gold key labels.
- **Why:** keys generated from an empty registry never match those labels.

### 10. Per-question trace logs are keyed by question text

- **Code:** `state_dump.py:132` (`qa_logs[question] = lg`).
- **Effect:** a question asked at four checkpoints keeps only its first log, the earliest checkpoint's. The runner reads the logs newest first, so the loop ends on the oldest one. (This list first said "its last log". A reviewer of the repairs corrected the direction; the count is unchanged.) Per-checkpoint diagnostics are therefore wrong for every repeated question, including all noise items. Examples are the "attached 8 of 24" and "Resolved 24/24" figures.

### 11. The failure coder drops numbers, truncates spans and counts pairs

- **Code:** `20-failure-analysis.py` and `20-failure-funnel.py`.
  - Tokens of two characters or fewer are dropped (`len(w) > 2`).
  - Claims and facts per span are cut to 12 (`[:12]`).
  - Gold × fact pairs are counted as separate cases.

### 14. The reference-informed gate confirms on wording, not on gold values (found 22 October, after Phase B)

- **Code:** `AmiEvalRunner._internal_confirm`, value policy `gold_backed` (`runner.py:812`, line numbers at 3320375; Phase B did not change the gate). Its docstring says it accepts a pending proposal "whose state key is a gold state key at this checkpoint AND whose value lexically overlaps a gold value or decision annotation". The code does three things differently:
  - it checks no state key;
  - it ignores the gold's status, matching every gold fact's value (`gold_texts = [f.value for f in ctx.gold_facts]`, line 848);
  - it matches the AMI decision annotations, which are long transcript passages (16 at the last ES2009 checkpoint, about 1,400 characters each). A value passes if every one of its content words occurs somewhere in a passage, or if it shares two content words with one.
- **Contradicts:** its own docstring (the state-key condition), and the arm's role as reference-informed: a value the gold marks rejected can be confirmed as current.
- **Runs** (`23-informed-gate-replay.py`, `.json`). The five ES2009 reference-informed runs all used the default two-word threshold with the semantic route off, so a lexical replay accounts for every acceptance. Of 494 accepted values (rejection proposals excluded):
  - 120 (24%) match a gold value that holds at some checkpoint from the value's meeting on;
  - 9 (2%) match only gold values marked rejected. Six of them adopt the rejected touch screen itself, e.g. "touch screen remote" and "simple touch screen";
  - 365 (74%) match no gold value at all, only decision-annotation text. Of these, 154 passed because each content word occurs somewhere in a passage, 50 of them one-word values such as "complicated"; 211 passed because they share two words with a passage.
- **Effect:** the arm is neither an oracle nor an approximation of a reviewer. It confirms on vocabulary and holds back the rest: 215 current facts over its five runs, against 539 for the autonomous arm (`23-bug-incidence.json`). That is why it scores lowest on answerable questions (24.8%; section C). Bug 13 also hits this arm: 4 of its 5 runs hold a fact whose validity ends before it starts, against none of the autonomous runs. Its cycle-1 results therefore show nothing about review. The thesis already calls it "not human review and not a performance ceiling" and explains its lower score by delayed availability (eval.tex, §H7). The replay adds what its gate actually confirms.

## C. Defects in the benchmark (not code)

- The 8 ES2009 noise items forbid nothing (`must_not_include: []`) and ask about topics absent from the meetings, so noise leakage is 0 by construction. The 8 EL2020 noise items forbid nothing either.
- No item expects a candidate or proposed status, and forbidden values occur only in the rejection lists.
- Rejection items carry no expected status, which is what lets bug 7 bite.
- **Measured effect: two families decide the ES2009 ranking** (`23-answerable-only.py`, `.json`; all arms read with the bug-7 repaired rejection items).
  - The noise items score 100% for every arm.
  - The 6 unknown items reward abstaining: autonomous 100%, reference-informed 100%, RAG 20%. That difference is worth 11.2 points, more than the autonomous arm's whole 10.2-point lead (59.5% against 49.3%).
  - On the 29 answerable questions: autonomous 40.0%, RAG 41.4%, reference-informed 24.8%.
  - With corrected lineage (bug 2: `23-bug2-answer-estimate.json`), the autonomous arm's 40.0% falls to about 33%. That is an estimate, with bugs 1 and 3-6 still present.
  - EL2020, answerable only: autonomous 30.3% (about 28% with corrected lineage), RAG 68.6%.

  The overall score is therefore not a fair headline. The thesis already says the ES2009 lead depends on how unknown-answer stance is read; on the answerable questions there is no lead. Report answerable-only accuracy next to the overall score, and read the noise and unknown families on their own.

## D. Not bugs: design choices that turned out badly

- **Span-level admission:** a turn that mixes project talk and small talk is admitted whole (the ES2009a L31 ice-breaker), and the autonomous structural gate accepted the concepts built from it.
- **Forced scalar concepts** (`expansion_force_scalar`): there are no collection keys, so list answers have to aggregate across keys.
- **The read path is template-only**, with no fallback to the evidence text.
- **Restraint is a by-product of retrieval thresholds**, not a declared outcome. This is latent: with embeddings off, value retrieval re-adds keys the resolver had declined.
- **Cold-start key proliferation:** 99–196 generated keys, which questions then have to be resolved against.

## E. Suspected, not verified

- ~~In the reference-informed arm, gold-backed confirmation may accept values that match rejected gold entries (ch5a open attack).~~ Verified 22 October: bug 14 (9 of 494 accepted values).
- The hedged-only branch could replace a confirmed fact if the asserted claim behind that fact were missing from the claim set (ch4-03). This has not been shown to occur in the runs.
- Conflict records are not deduplicated: r1 has 11 records for one key (ch4-06).
- The extension (81e7e2f) and ablation (6056c08) runs ran on uncommitted trees, so their exact code cannot be reconstructed.

## F. Latent: real, but did not occur in the cycle-1 runs

- **Open-vocabulary values are compared case-sensitively.** `make_baseline_canonical_fn` returns the raw surface for an open-vocabulary key, although its docstring says "normalised surface". So "Lithium Battery" and "lithium battery" are different values: a negation differing only in case misses the current value, and a case variant could supersede it. In the cycle-1 dumps this never happens. All 109 + 103 same-value supersessions have identical raw values, and no negation matches a fact by case alone. Not repaired.
- **Bug 12 on collection keys.** Collection proposals keep the evaluated deduplication under the repair, so a member added, rejected and added again stays rejected. The cycle-1 runs have no collection keys (`expansion_force_scalar`). Not repaired; a collection repair would also need negations gated by time (an older negation now undoes a newer re-adoption).
- **A ruled-out value that is adopted again stays listed as rejected (A0 and the repaired arms).** A rejection record is never withdrawn. The read path lists every REJECTED fact, so a value ruled out and later re-adopted is current and also "ruled out so far" in rejection answers. This happens after any re-adoption: in transcript order, and after a re-affirmation extracted at a later meeting. Telling an overturned ruling-out from a standing one is a read-path rule (a value's latest record decides). On a REJECTED fact, `valid_to` marks when a demoted value stopped being current, so it cannot also mark the end of a ruling-out. Not repaired in Phase B; a Phase C item for the rejection family.
- **Adopting and ruling out a value in one pass (evaluated behaviour).** In A0, "not V … OK, V then" in one meeting creates both "supersede to V" and "reject V" in the same pass. The rejection, applied second, demotes the V just adopted. Under the bug-1 repair the full evaluation does not raise the rejection, because V survives the negation. A partial view in cold-start mapping can still raise it; the bug-13 repair expires it before confirmation.

## What the cycle-2 plan targets

This section goes by `21-design-cycle-2-plan.md`, not the frozen code.

- **Bug 3** is targeted by the supersession contract and by the rule that same-meeting rivals under a scalar key become a conflict.
- **Bug 5** may be touched by the type checks before filing.
- **Bug 2** is not fixed by the evidence check alone. That check validates a claim's own span at filing, but the copying happens later, when the proposal is created.
- **Bugs 1, 4 and 6, and harness bug 7,** are not obviously addressed by anything in the plan.

Check cycle2-freeze-2 before batch W runs. (Batches R, W and H are superseded by `23-plan-development-and-confirmation.md`.)

## Repair status (stage 23, Phase B)

Each repair is a switch in `app/core/cycle2_flags.py` (contract "repair"), off by default. With every switch off the code behaves as evaluated: the faithful trace replay is identical, and `tests/test_bug_reproductions.py::test_repair_code_runs_only_with_its_switches` shows no repair code runs. Tests are in `tests/test_bug_reproductions.py`.

| Bug | Switch | What the repair does |
|---|---|---|
| 1 | `repair_negation_affirmation` | One definition of "ruled out" for the whole engine: a value is ruled out when none of its positive claims survives the asserted negations. A claim said before a negation of at least its authority does not survive. Nor does a hedged or proposed mention with no assertion after the negation, since a hedge does not take a ruling-out back. "Before" is source time, then the span's position in the transcript, then extraction order within a span. Under A2 a restatement (the cycle-2 equivalence) is the same value. Consequences:<br>(1) A negation of the current value X takes effect.<br>(2) The engine resolves the key as if X were gone, with X as a floor: only claims said after X took effect compete (under A2, also on evidence X did not rest on). A value the key had moved past does not come back, nor does one that lost to X in its own meeting (D5). Among those that qualify, the ranking is the usual one.<br>(3) If that adopts a value, an asserted one in "not X, Y instead" or a hedged one (unconfirmed) when no assertion qualifies, X is superseded by it at once. The same pass also raises X's rejection, so X's ruling-out does not wait for Y to be confirmed. The change is dated at the later of the negation and Y's own claim. A replacement adopted at a later checkpoint, because a gate applied the rejection first, starts where X ended.<br>(4) Otherwise X is rejected. The rejection cites the latest negation in transcript order and never ends X before X started. The floor stays, and same-meeting rivals or a tie become a conflict on the next pass.<br>(5) The ruled-out branch for non-current values (E1) records a rejection only under the same rule and the same identity (a restated negation of the current value goes through rule 1), so "not Y … OK, Y then" adopts Y. The rejection is dated and cited at the latest negation, not at one a re-affirmation answered. A ruling-out already recorded is not raised again, while a value ruled out again after a re-adoption is.<br>(6) A negation is never appended as support.<br>(7) Under A2, every negation and every re-affirmation the rule relies on is support-checked (D9) before it is used, and parked if its span does not establish it.<br>Fuzzers over random claim scripts found no state change on a pass with nothing new said, in A1 or A2. They also found no stale application, no ruled-out value left current, and no supersession by the same value. The scripts varied authority and modality and included ties, review gates that leave proposals pending, cold-start mapping in random span order, restated values, two keys, and 30% unsupported spans under A2. |
| 2 | `repair_proposal_lineage` | Evidence, confidence and authority come from the claim that supplied the winning value. A proposal still waiting for review when the engine returns it again takes the lineage computed now: a later, stronger claim for the same value replaces the earlier one. On the reject path the proposal carries the negation's span, confidence and authority, while the demoted REJECTED fact keeps the provenance of its adoption. |
| 3 | `repair_same_meeting_supersession` | The current value's own claims compete with its best challenger. The challenger supersedes only if it ranks strictly higher on (authority, source time, confidence), so an exact tie keeps the current value. This is the Ch. 4 rule; the cycle-2 conflict contract is the alternative (A2). |
| 4 | `repair_hedged_same_value` | With only hedged claims, a most recent value equal to the current one is a no-op. |
| 5 | `repair_undefined_key_filing` | A claim under a key with no concept definition is not filed. |
| 6 | `repair_meeting_dates` | The runner sends each meeting's date: the suite's recorded date for ELITR, and for AMI the recording date and start time in `meetings.xml`. ES2009 is 14 Feb 2005, 11:07 / 12:12 / 12:16 / 14:22. No time of day is invented. The run fails closed, before the first ingest, if a date or start time is missing or the dates do not increase strictly in suite order; synthetic suites need recorded dates too. Of the 35 AMI scenario series, 14 have four meetings with start times (ES2003, ES2005–ES2009, IS1000, IS1001, IS1003, IS1004 and IS1006–IS1009). IS1002 and IS1005 have three meetings, all dated. Seventeen have no start times, and their four meetings share one date. ES2004 and ES2010 lack only meeting d's. The run refuses those 19. |
| 7 | `repair_judge_rejection_status` | The judge's gold string for a rejection item says the values were ruled out. This lives in a judge wrapper (`judge_repairs.py`), because `scorer.py` must stay byte-identical for the sealed cycle-1 studies. It reaches the PM runner, the answer replays and the RAG runner (`--repair-judge-rejection-status`), and the RAG report records it. Only the prose call is repaired. The state layer's judge sees fact values without their statuses, so the state layer stays status-blind. The rescoring of the preserved cycle-1 answers is a separate module (`rejection_rescore.py`; `rescore.py` refuses the switch). It ran on 22 October: 132 prose calls on 153 items in 33 runs, with results in `23-bug7-rescore.md`. Only EL2020 changes: PM rejection items go from 4 to 6 of 36 and RAG from 18 to 14 of 36, so the PM − RAG gap moves from −35.0 to −33.0 points. |
| 9, 10 | `repair_dump_diagnostics` | Traces are matched per checkpoint in asking order. A resolved key that has held a gold value (a fact of any status) is not called a wrong key. After that test, two cases are `answer_layer`: a rejection item whose key holds the gold value as a rejected fact, and any item whose key holds it as a current unconfirmed fact. A key that held the gold value only as a fact no longer current at the end of the run is `gold_value_not_current_at_end`, since the end-of-run dump cannot tell whether the value was current at the checkpoint. Evidence items are not reached: their gold is a meeting, not a value. |
| 12 | `repair_open_proposal_dedup` | For scalar new and supersede proposals and the rejection of the current value, a proposal applied as proposed no longer deduplicates, and neither does one that expired (bug 13). An open or declined proposal still does, and so does one a reviewer edited before applying (an edit review, of the value or the status). A value edit blocks only that proposal: a proposal of another type for the original value can still be raised. |
| 13 | `repair_settle_before_confirm` | Before a checkpoint's proposals are confirmed, every claim is evaluated again with its key's full claim set. A pending proposal that evaluation no longer produces expires, so only proposals computed for the current state reach the gate. A proposal the settling pass expired was never decided, so under this repair it never stands in for a later one on any path, including the ruled-out branch's deduplication. With the switch off, a proposal expired otherwise (the artifact-deletion route) still blocks, as evaluated. It is meant to run with the bug-12 repair. With a gate that leaves a proposal pending, the proposal may take a new form once after the state changes (for example "supersede to Y" becomes "new Y" once Y's target is rejected); the state does not change. |
| 8 | none | Not repaired: the restraint claim is dropped from the verdict list (decided 22 October). |
| 11 | none | Not repaired in Phase B: the failure coder is an analysis script (`20-failure-*.py`); it is to be fixed as the loss trace (23 plan, B2). |
| 14 | none | Not repaired. Recommended: drop the reference-informed arm from the thesis's comparisons (23 plan, open decision). A rebuilt gate would match against gold values only, by status, and never against decision text. |
