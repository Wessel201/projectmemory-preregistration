# Plan: repair, develop, then one confirmatory study

Written 22 October 2026, after the disproof review (`22-disproof-review.md`) and the bug reproductions of stage 23. Revised the same day, after the supervisor accepted the clarified objective (decision 5). The revision adds:
- the objective, the central question and the quality targets below;
- per-mechanism verdicts in place of a single score against RAG;
- a Phase D entry gate, with a fallback;
- a clean evaluation package as the freeze;
- the thesis framing (Phase F).

This plan replaces the batch structure of `21-design-cycle-2-plan.md` (batches R, W and H). From that plan it carries over:
- the contracts;
- most integrity rules (adapted below);
- the validation studies V1–V6;
- the held-out series choice.

## What the evaluation is for

- **Objective.** The thesis investigates what works and what doesn't when AI mechanisms turn conversational evidence (meeting transcripts) into maintained project knowledge. ProjectMemory is the means of that investigation, not its aim. Its accuracy and its comparison with RAG are measures, not the goal.
- **Central question.** Once implementation defects are removed, which of the investigated mechanisms work for turning conversational evidence into maintained project knowledge, which don't, and at which transformation boundary (extraction, filing, state maintenance, reading) does each succeed or fail?
- **Results limited by a defect show nothing** about the mechanism, in either direction. The audit enters the thesis as the reason cycle 1 is measured again, and as reflection on method. It is never a finding about the design.
- **Two-sided.** This is not a failure-mode study: each mechanism can come out as working or not.
- **Artifact metrics stay** (overall accuracy, family scores, the RAG comparison) as context for the verdicts, not as the headline.
- **RQ1–RQ4 stay.** The objective explains why they were asked.
- **Focus.** Everything in this plan serves the central question. Work that doesn't is cut or moved to an appendix.

**Quality targets.** The plan aims at these qualities, not at a grade:

| Quality | Delivered by |
|---|---|
| Problem investigation | Phase F: Ch. 2, with difficulties from conversation kept apart from those the architecture introduces |
| Design science | Phase F: each Ch. 4 decision traced from a Ch. 2 difficulty; P0-D fixed |
| Experimental rigour | Phases B, D, E: repairs, validated instruments, held-out series, package freeze, stop rule |
| Explanatory depth | Phases B2, D, E: the loss trace and the attribution coding |
| Contribution | Phases D–F: per-mechanism verdicts, bounded to the series tested |
| Critical reflection | Phase F: the audit as reflection on method |

## Why the plan changes

- **The bugs are real and they fired.**
  - The review found six system bugs and five harness bugs (`22-bug-list.md`).
  - Each is reproduced by a minimal offline test (`tests/test_bug_reproductions.py`).
  - Every one fired in the cycle-1 runs (`23-bug-incidence.json`).
- **They confound the thesis question.** Cycle 1 cannot separate "the architecture is worse" from "this implementation is defective".
- **They mask each other.**
  - Bug 2 (facts cite the oldest claim's span) props up the evidence family.
  - Correcting bug 2 alone breaks 10 of 20 ES2009 evidence answers and 6 of 20 EL2020 ones, and fixes none (`23-bug2-answer-estimate.json`), because bug 3 had already replaced the value.
  - So the bugs must be fixed together and their effect measured, not assumed.
- **Neither current series can carry a confirmatory claim any more.** ES2009 and EL2020 have both been used to find defects.
- **No external deadline.** The timeline was self-imposed. Quality of evidence comes first.

## Decisions taken (22 October)

1. **Batch R stopped by the author.**
   - It stopped at stage `c2r_es_r2`, with status PAUSED and exit code 1, after one job was aborted mid-run.
   - Completed stages: `c2r_el_r2` (first and rest), `c2r_el_r3`, `c2r_el_re`, `c2r_es_r0`, `c2r_es_r1`, and 2 of the 5 jobs of `c2r_es_r2`.
   - Recorded spend: about $14.2.
   - These are kept and reported as development results.
   - Pre-declaration R and its amendment 1 are superseded, not deleted.
   - Batches W and H were never launched.
2. **Cycle 1 becomes the development evaluation.**
   - The thesis discloses that it was pre-declared as an evaluation and downgraded after the audit, and why.
   - It is reported in full. The audit and the bug reproductions are the reason it is measured again, not findings about the design.
3. **The headline moves to the per-mechanism verdicts of one pre-registered confirmatory study on held-out series** (Phases D–E).
4. **Stop rule.** Once the confirmatory study is analysed under its pre-registered plan, the evaluation is finished, whatever it shows. Defects found afterwards are documented, not fixed for the thesis. A mechanism they affect gets the verdict *can't tell*.
5. **Supervisor accepted** the clarified objective (above) and this second cycle entering the graded version.
6. **The freeze is a clean evaluation package in its own repository**, not this repository (Phase D2).

## Phase A: Bug reproduction (done 22 October; offline, $0)

| Level | Artifact | Result |
|---|---|---|
| A1 Minimal reproductions | `tests/test_bug_reproductions.py` | 17 strict xfails assert the designed behaviour. With the four cycle-2 write switches on, two pass: bug 2's evidence (`filing_support_check`) and bug 3 (`resolution_same_meeting_conflict` / `supersession_requires_new_evidence`). The full suite stays green (1634 passed). |
| A2 Incidence in the cycle-1 runs | `23-bug-incidence.py`, `.json` | See the table below. |
| A3 Answer cost | `23-bug2-answer-estimate.py`, `.json` | Bug 2 (offline, deterministic). Bug 7 is measured by rescoring after its fix (Phase B). Bugs 3 and 5 change what is stored, so their cost needs the re-runs of Phase C. |
| A4 Re-reading cycle 1 (22 October) | `23-answerable-only.py`, `.json`; `23-informed-gate-replay.py`, `.json` | Two families decide the ES2009 ranking, and the reference-informed gate confirms on wording (bug 14). See below. |

**Incidence.** ES2009 is autonomous r1–r5. EL2020 is autonomous r1–r3.

| Bug | ES2009 | EL2020 |
|---|---|---|
| 1. Asserted negation of the current value, from a later meeting, with no effect | 4 (none left current at the end) | 0 |
| 2. Current facts citing a span without their value | 304 / 539 | 190 / 501 |
| 3. Facts replaced by a rival from their own meeting | 97 (43 by lower confidence) | 147 (52 by lower confidence) |
| 4. Supersessions by the same value (of all supersessions) | 109 / 823 | 103 / 681 |
| 5. Facts under undefined keys (of them, under `'null'`) | 42 (27) | 22 (10) |
| 6. Facts dated by ingestion time | 1603 / 1603 | 1287 / 1287 |
| 7. Rejection questions judged without their status | 15 | 36 |
| 9. "Wrong key" diagnoses whose resolved key holds a gold value | 30 / 97 | 10 / 166 |
| 10. Traces read from another checkpoint | 150 / 215 | 78 / 315 |
| 11. Spans over the coder's 12-claim cut; gold values losing a number | 9; — | 27; 10 of 59 |
| 13. Facts whose validity ends before it starts (stale proposals applied) | 0 (reference-informed: 4) | 0 |

The bug-1 count was 5. It became 4 when a ruled-out alternative recorded next to the current value stopped being counted as a current value (third review). Bug 13 was found in Phase B; its count is a lower bound.

**Bug 2's cost on answers** (offline; the template re-implementation matches the run's answers 40 of 40 times):

| Measure | ES2009 | EL2020 |
|---|---|---|
| Change answers, with perfect resolution: gold values covered, actual → corrected lineage | 7 → 18 of 90 | 5 → 20 of 72 |
| Evidence answers right, actual → corrected lineage | 20 → 10 of 20 | 15 → 9 of 20 |

In the evaluated runs the change answers fail earlier, at question-to-key resolution (`resolver_miss`), so lineage is not their first failure.

**Re-reading cycle 1 (22 October; offline, $0).**

*Answerable questions only* (`23-answerable-only.py`; all arms with the bug-7 repaired rejection items). The noise items forbid nothing, so every arm scores 100% on them. The unknown items reward abstaining. Set both apart and the cycle-1 comparison reads differently:

| Series | Arm | Overall | Answerable only | With corrected lineage (bug 2, estimate) |
|---|---|---|---|---|
| ES2009 (29 of 43 questions, 5 repeats) | Autonomous | 59.5% | 40.0% | about 33% |
| | RAG | 49.3% | 41.4% | — |
| | Reference-informed | 49.3% | 24.8% | — |
| EL2020 (87 of 105 questions, 3 repeats) | Autonomous | 39.7% | 30.3% | about 28% |
| | RAG | 72.7% | 68.6% | — |

On ES2009 the 6 unknown items are worth 11.2 points to the autonomous arm over RAG (100% against 20%). That is more than its whole 10.2-point lead. On the answerable questions there is no lead, and part of the autonomous arm's 40.0% is bug 2. This is the same restraint behaviour that is now off the verdict list.

*The reference-informed gate* (`23-informed-gate-replay.py`; bug 14 in `22-bug-list.md`). Of the 494 values it confirmed in its five runs:
- 120 (24%) match a gold value that holds;
- 9 (2%) match only gold values marked rejected, six of them the rejected touch screen;
- 365 (74%) match only the wording of the AMI decision annotations: long transcript passages, where every content word of a one-word value can occur.

It confirms on vocabulary and holds back the rest: 215 current facts in five runs, against 539 for the autonomous arm. It is also the arm bug 13 damages (4 of 5 runs). Its cycle-1 results therefore show nothing about review, nor about a ceiling.

## Phase B: Repair

All repairs go behind switches whose default is the evaluated behaviour (integrity rule 1). One code base can then run three arms:
- **A0:** cycle 1 as evaluated;
- **A1:** bugs fixed;
- **A2:** bugs fixed plus contracts.

Each fix turns its reproduction green with its switch on. The test file then gains a "fixed" mode, and the evaluated mode keeps documenting the old behaviour.

### B1. System bugs

| Bug | Repair |
|---|---|
| 1 | Built: one definition of "ruled out" (no positive claim of the value survives the asserted negations). A ruled-out current value is superseded by what the key resolves to without it, or rejected with a floor. A negation is never appended as support. Details are in `22-bug-list.md` (Repair status). |
| 2 | Take evidence, confidence and authority from the claim that supplied the winning value. Cycle 2's `filing_support_check` fixes only the evidence, and only when it is on. |
| 3 | The current value's own claims compete. Same-meeting rivals are decided by confidence (as Ch. 4 says), or become a conflict (cycle-2 contract). Pick one for A1 and record which. |
| 4 | The hedged-only branch compares with the current fact and returns "supports" for the same value. (Implemented as a no-op: no support is appended.) |
| 5 | Park claims whose key has no concept definition, including the literal `'null'`. Apply the type check after this, not instead of it. |
| 6 | The runner passes each meeting's date as `created_at_source`. (Done differently: the AMI metadata does carry recording dates and start times, so no synthetic gaps are needed. See the Phase B status.) |
| 12 | Found in Phase B. An applied proposal no longer deduplicates, so a value can be reinstated. It goes with the bug-3 and bug-4 repairs, because bug 12 hid bug 3's oscillation. |
| 13 | Found in Phase B (third review). Before confirmation, every key is evaluated again and pending proposals it no longer produces expire, so the gate never applies a proposal from a partial view or an earlier checkpoint. It goes with the bug-12 repair. |

### B2. Harness and instrument

| Bug | Repair |
|---|---|
| 7 | The gold string states the rejected status. Rescore the preserved cycle-1 rejection answers of both systems, PM and RAG; the reviewer's EL2020 correction moves RAG too (18 → 17 of 24). Report both versions. **Prepared** (`app/evaluation/ami/rejection_rescore.py`), offline:<br>- 33 runs (ES2009 from the two sealed GPT-5.4 rescores without the selection grid, EL2020 from the transfer study), 153 rejection items;<br>- every item rebuilt and checked against its recorded score;<br>- only the prose layer is judged again, 132 calls, each differing from the original only in the gold string;<br>- the state layer's judge sees values without statuses, so its scores are carried over;<br>- the recorded ES2009 prose calls of these items cost $0.0043 on average, so about $0.57 is expected; the estimate at p95 output is $0.77, under a $1.00 budget with a stop at $0.95.<br>The scorer credits an answer that contains the option without a judge call, so rescoring cannot fix a deterministic credit; there are none among these items. There is no control run of the original gold strings (about $0.6 more), so the judge's call-to-call variance is not separated; every flipped item is listed.<br>**Run 22 October** (`23-bug7-rescore.md`, $0.52 nominal). Only EL2020 changes:<br>- PM rejection items 4 → 6 of 36, RAG 18 → 14 of 36;<br>- prose overall: PM 39.0% → 39.7%, RAG 74.0% → 72.7%;<br>- the gap goes from −35.0 to −33.0 points;<br>- ES2009 is unchanged.<br>Of the 8 flips, 7 read as the repair intends; one (EL2020a R01, RAG r1) is ambiguous. |
| 9 | No "wrong key" diagnosis in cold-start runs unless the resolved keys hold no gold value. |
| 10 | Key traces by question id and checkpoint. |
| 11 | Fix the lexical failure coder (decided in this revision): keep numbers, drop the 12-claim cap, count facts not pairs. It becomes the **loss trace**. For each gold value, the trace gives the boundary where it was lost: extraction, filing, state maintenance or reading. It keeps "stored but not reached by the reader" apart from "never stored", and it is a registered analysis (Phase D3). From cycle 1, only the extraction-stage numbers in Ch. 5 and Ch. 6 are recounted, because no bug touches that stage. The later-stage numbers are defect-limited and dropped; they come from A1 runs instead. |
| 8 | Add separate embedding switches per component, only if a restraint-mechanism claim is kept. Otherwise drop the claim. |

### B3. Benchmark repairs (a new suite version, frozen before Phase D)

- Noise items about incidental talk that does occur, with that content forbidden. For example, the ES2009a ice-breaker items must not appear as project state.
- Status items that can fail: some items expect "candidate" or "proposed".
- Rejection items carry an expected status.
- More than three distinct values in the candidate/decided family.
- The development gold. Settle P1-8 first, then P1-7 (`22-fix-priorities.md`); the universal-remote reversal may make about 12 questions wrong. Do this before the A0/A1/A2 comparisons.
- Unknown items about topics the meetings discussed without settling, so abstaining pays only where it is selective (from the re-reading above). Together with the noise items, this comes before any comparison whose overall score is read.

### B4. Validation (from the 21 plan's Phase 1)

| Study | Priority | Why |
|---|---|---|
| V6: judge decisions, two annotators plus adjudication, gates registered first | Required before Phase D | It is the instrument of the confirmatory study. |
| V5: ES2009 gold, second person | Recommended | Reports the development gold's quality. |
| V1: EL2020 gold | Recommended | Same, for EL2020. Already sent. |
| V4: the loss trace and the attribution coding, with a second coder on a sample | Required before Phase D | They carry the explanatory claims: where and why a mechanism fails. |
| V3: stance, V2: citations | Optional | |

The 21 plan's rule 6 ("no new human labelling of cycle-2 answers") is lifted for the confirmatory study. There is now time for blind human checks, and the confirmatory claim needs them.

### Phase B status (22 October; offline, $0)

**Done.** Every repair in B1, and bugs 7, 9, 10 and 12, sit behind switches. `22-bug-list.md` ("Repair status") says what each one does.

- **Tests:**
  - `tests/test_bug_reproductions.py`: 267 tests. 240 pass, under the repairs, under arm A1 and under arm A2; 1 is skipped (an A2 conflict case). 26 are strict xfails:
    - 17 document the evaluated behaviour;
    - 6 document the cycle-2 write switches alone;
    - 2 show bug 13 under the bug-1 repair without settling;
    - 1 is bug 8, unrepaired.
  - Judge-wrapper tests sit at each scoring site: the PM run loops, the answer replay, and the RAG runner and its CLI.
  - The full suite: 1892 passed, 2 skipped, 39 xfailed.
- **Switches off = evaluated:**
  - The faithful trace replay is identical: 686/686 recorded calls served, dump identical, 0 answers differing.
  - A reach test covers all 25 repair entry points. With every switch off, none of them runs. Under A2, all run except one: the bug-13 lookup that the evaluated deduplication path uses, which runs only with the bug-13 repair on and the bug-12 repair off and has its own test. Under A1, the A2-only support check does not run either.
  - A switches-off test pins the evaluated deduplication for a proposal expired by artifact deletion.
- **Reviewed in five rounds by LLM reviewer agents.**
  - **Round 1:** eight agents tried to break the first version. 22 findings were upheld, and all were addressed. The main ones:
    - bug 1 counted hedges and earlier same-meeting mentions as re-affirmation;
    - "not X, Y instead" left the key empty;
    - bug 12 re-raised rejections on every pass;
    - midnight dates;
    - the tripwire did not reach the repairs.
  - **Round 2:** five reviewers, each finding checked by a skeptic. 25 findings were upheld; all are addressed or recorded in `22-bug-list.md` section F. The main ones: with bug 12 no longer braking it, the repaired engine did not settle. A hedge after a negation flipped the key on every pass, and rejecting the current value brought back a value superseded long before. Bug 1 now has one definition of "ruled out". A ruled-out current value is superseded by what the key resolves to without it, or rejected with a floor.
  - **Round 3:** four reviewers, each with a skeptic. 21 findings were upheld and none refuted; all are addressed or recorded. The main ones:
    - with review gates that leave proposals pending, a negated value stayed current while its replacement waited;
    - cold-start mapping evaluates claims one at a time, and their proposals were confirmed from that partial view;
    - the gates applied stale proposals from earlier checkpoints, which is bug 13 and also in the cycle-1 runs;
    - under A2, the claims bug 1 relied on were not support-checked;
    - claims of one meeting were ordered by extraction time, not transcript position.
  - **Round 4:** three reviewers, each with a skeptic. 19 findings were upheld and none refuted; all are addressed or recorded. The main ones:
    - under A2 a restated negation of the current value half-applied;
    - a rejection that settling had expired blocked every later ruling-out of that value;
    - a replacement applied a checkpoint after its predecessor's rejection overlapped it;
    - the bug-7 repair asked the status-blind state layer about a status.
  - **Round 5:** three reviewers, each with a skeptic, on the committed tree. 14 findings were upheld and none refuted; all are addressed. The main ones:
    - the round-4 expired-proposal skip ran with every switch off: the artifact-deletion route expires proposals too. It now runs only under the bug-13 repair, and a switches-off test pins the evaluated behaviour;
    - the ruled-out branch dated and cited a rejection at a negation a re-affirmation had answered;
    - a late-extracted negation could end a value before its dated start;
    - a late re-affirmation left the value current and still recorded as ruled out. This is not repaired: it is a read-path question that also applies to in-order re-adoptions and to A0. It is recorded in `22-bug-list.md` section F as a Phase C item for the rejection family.
  - **Checks after round 4:** fuzzers over random claim scripts found no change of state on a pass with nothing new said, in A1 or A2. They also found no stale application, no ruled-out value left current, and no supersession by the same value. The scripts varied authority, modality and ties, used review gates that leave proposals pending, ran cold-start mapping in random span order, used restated values and two keys, and had 30% unsupported spans under A2. A0 shows all of these defects.

**Decisions recorded.**
- **Bug 3:** A1 uses the Ch. 4 rule. The current value's own claims compete, and an exact tie keeps the current value. The conflict contract is A2's alternative.
- **Bug 6:** dates come from AMI `meetings.xml` (ES2009: 14 Feb 2005, 11:07 / 12:12 / 12:16 / 14:22) and from the ELITR suite. The run fails closed if a date or start time is missing or the dates do not increase. Only 14 of the 35 AMI scenario series have four dated meetings: ES2003, ES2005–ES2009, IS1000, IS1001, IS1003, IS1004 and IS1006–IS1009. IS1002 and IS1005 have three. Seventeen have no start times; ES2004 and ES2010 lack meeting d's. **This constrains the held-out AMI series in Phase D.** Pick it among these, or define and disclose a fallback ordering before the registration.
- **Bug 12** is repaired for scalar keys only. Collection keys keep the evaluated deduplication; the cycle-1 runs have none.
- **Bug 1's floor:** once a value is ruled out, only claims said after it took effect may replace it, so a value that lost to it in its own meeting stays lost (Ch. 4, D5).
- **Arms and the instrument.** "All repairs on" includes the instrument repairs (bugs 7, 9 and 10). A comparison of A0 with A1 that should differ only in the system must switch the instrument repairs on for A0 as well, and for RAG.

**Open, for you:**
- **Bug 7 rescoring.** Done 22 October (see B2 and `23-bug7-rescore.md`): only EL2020 changes, and the PM − RAG gap goes from −35.0 to −33.0 points. A control run of the original gold strings would add about $0.6 and needs its own go-ahead.
- **Bug 8:** decided 22 October: the restraint claim is dropped from the verdict list, so no per-component switches are built.
- **Bug 11: done 23 October (EL2020).** The loss trace replaces the failure coder: `23-loss-trace.py` with its codebook `23-loss-trace.md`, adjudications `23-loss-trace-adjudications.yaml` and results `23-loss-trace-results.md`.
  - **Unit:** every gold value at every checkpoint (a row), counted two-sided.
  - **State:** rebuilt in transaction time; it matches the reader's packs in all nine runs (`pack_check` in the output: 9551/9551 question keys, 8430/8430 statuses).
  - **Verification:** three adversarial rounds, and an independent check of the result notes. Blind coders agreed with the script on 21 of 24 held-out rows in the last round.
  - **Adjudication:** the matcher proposes and adjudication decides. The 670 decisions are model judgements (two independent adjudicators, kappa 0.94), so V4's human second coder is still required.
  - **Open:** ES2009 needs its own provenance join, because its gold cites decision passages, not transcript lines.
- **B3 and B4:** benchmark repairs and validation studies; your work.
- **A1 smoke run, done 22 October** (`23-a1-smoke-el2020.md`): one EL2020 run, valid, $3.33. Every system-bug incidence count is zero. Overall 38.1% against 39.7% for A0 (rescored), with evidence 42.9% against 71.4%, as the bug-2 estimate predicted. This is one run with no same-period A0, so it carries no weight yet.
- **A1 against a same-period A0 on EL2020, done 23 October** (`23-el2020-a0-a1.md`, $15.01 for 5 more runs): three runs per arm, both with the instrument repairs.
  - Overall: A0 41.0%, A1 37.1%, difference −3.8, interval [−9.2, +1.3] (questions resampled) or [−11.1, +2.9] (runs resampled too); state layer level at 36.2%.
  - A1 does not beat A0. "Worse" is not established.
  - The drop sits mostly on bug-2 credit (evidence) and one conflict that the autonomous arm never resolves. Without those three items the difference is −1.3.
  - The score is limited by routing and the registry in both arms.
  - Every system-bug incidence count is zero under A1.
  - Phase C items: no reviewer resolves conflicts in the autonomous arm; record judge inputs in the trace; the resolver shortlist; a paired replay design to measure repair effects without generation noise.
- **A2 and same-period RAG on EL2020, done 23 October** (`23-el2020-arms.md`, $13.67 against a $20 stop). Three runs each; one A2 run crashed on an API timeout and was replaced.
  - Overall: A0 41.0%, A1 37.1%, A2 31.1%, RAG 67.0%.
  - A2 − A0 −9.8 [−17.5, −2.5] with runs resampled; A2 − A1 −6.0 [−10.8, −1.3] with questions resampled ([−13.0, +0.6] with runs too); state layer −12.7 against both.
  - Every system-bug incidence count is zero under A2.
  - Loss trace (rows = value × checkpoint, 133 current rows per run): in A2 filing losses rise (61.7 vs 22–26 rows per run) and state-maintenance losses fall (3.3 vs 22–24).
    - Of A2's filing losses, 36.7 rows (11–21 distinct values) end in same-meeting conflicts the autonomous arm never resolves, and the cycle-2 checks park 15 more.
    - A2 stores 28 rows (9–12 distinct values) with the right status, against about 41 rows (22–28 values). Rows the other arms store correctly are lost at filing in A2 about half the time.
  - The rival values are mostly different matters routed to one key.
  - A0 and A1 store about the same and lose rows at the same boundaries in nearly the same numbers (adjudicated series). The largest loss in both is extraction (about 45 of 133 rows).
  - **This is evidence for the write contracts' development verdict, not the verdict itself:** the verdict rule is still to be written (Phase C). The evidence is that on EL2020, in the autonomous arm, the four contracts together lower the score and the stored state. Whether the conflict contract works with a reviewer is the open design decision above. The contracts were tested together, not one at a time.

## Phase C: Development (ES2009 and EL2020; not pre-registered, all runs logged)

- **Arms:** A0, A1, A2, plus RAG in the same period, because the canary found drift. Three repeats while iterating.
- **Two jobs only.** Development checks conformance: the repaired system does what the design says. It also diagnoses where and why information is still lost. Beyond that it settles only the choices listed below. No tuning for overall score: that is the proxy drift this plan was written to escape.
- **Log every run** with its code hash and switches. Development results claim nothing beyond development.
- **Conformance on runs, not only in unit tests.** Re-run `23-bug-incidence.py` and `23-bug12-incidence.py` on the A1 and A2 dumps. Every count must be zero or explained.
- **Report answerable-only accuracy next to the overall score** for every arm (`23-answerable-only.py`), and read the noise and unknown families on their own.
- **Choose what goes into the final configuration:**
  - which cycle-2 contracts survive. Before judging D1 (whole-decision extraction, failed twice in the build), repair the whole-item metric: the build diagnosis put most D1 misses on filler words in the gold descriptions, and only the lost role claims were real.
    - Bug 3's rule is decided: A1 uses the Ch. 4 rule.
    - The conflict contract competes as an A2 contract like the others.
  - whether the read contract (evidence fallback, answerability) is on.

  A contract enters the final configuration only if its development verdict is *works*, under the rule the registration will use (Phase D3). It is not picked by best overall score. Write the rule down before the last development comparison.
- **Dry-run the registered analyses** on development runs: the verdicts, the loss trace and the attribution coding.
- **Dress rehearsal.** The last development comparison runs from an exported package (Phase D2).
- **The partial batch R** (read-contract replays on cycle-1 dumps) counts as a development result for the read contract. It still carries write-path bugs 2, 3, 5 and 6, so it cannot decide the read contract on its own.

## Phase D: Entry gate, freeze and pre-registration

### D1. Entry gate

All of these must hold before the freeze:
- every bug reproduction passes in fixed mode;
- the incidence scripts, run on the final configuration's development dumps, show zero or explained incidence;
- V6 meets its registered gates, and V4 is done;
- a second annotator is confirmed for the held-out gold, V6 and the attribution coding;
- the registered analyses have been dry-run on development data;
- the supervisor agrees (met on 22 October).

**Fallback.** If the gate is not met, there is no confirmatory study. The thesis reports the development study and the audit as a formative evaluation, without confirmatory claims.

### D2. The freeze: a clean evaluation package

This repository stays the development repository. Its clutter never enters the signature: the thesis, notes, documents, `teams/`, `infra/`, `demo-ui/`, the old studies and runs.

- **Contents by trace, not by folder.** A recorder logs every import and every file opened while each configuration runs: the faithful replay, a switches-on run per arm, the RAG runner, the judge, the launcher and the analysis. The union is the manifest.
  - A static import scan is not enough, because most imports are lazy. It finds 33 modules; the faithful replay alone loads 108 of the 171 tracked `app/` modules (22 October).
- **Export script.** It copies exactly the manifest's files into the package repository, at the same relative paths. It writes `MANIFEST.json`: each path with its sha256, the source commit, and one package hash. Re-exporting is one command.
- **In the package:**
  - the traced `app/` modules and the launcher;
  - `pyproject.toml` and `uv.lock`, unchanged;
  - configuration, registries, protocol and suites;
  - the analysis script, moved out of `thesis/notes/…/artifacts/`;
  - the tests that cover package code;
  - a frozen settings file without secrets;
  - a README.
- **Not in it:**
  - `.env`. The API key comes from the environment only.
  - The corpora. They are listed by file hash, at the paths the code expects, with instructions for fetching them.
- **Settings.** Today `.env` can set behaviour outside the freeze: `LLM_MODEL`, `LLM_TEMPERATURE`, the `LLM_ENABLE_*` switches, `RESOLVER_EMBEDDINGS_ENABLED`, `EXPANSION_REUSE_POLICY` and its threshold, `EMBEDDING_MODEL`. In the package these values live in the frozen settings file, and the launcher refuses to start if the effective settings differ.
- **Checks before signing:**
  - the package's own tests, in its own venv built from the same `uv.lock`;
  - the faithful replay with `--code-root` pointing at the package, identical to this repository;
  - the analysis dry run on development data, with the same output hash;
  - the recorder asserts that the system side never opens annotation or gold files. The AMI loader reads the human summaries and decision annotations; nothing downstream uses them, but the held-out gold comes from exactly those files.
- **Identified three ways.**
  - Commit and tag the package repository.
  - Build the zip from the tag with `git archive`.
  - Register the tag, the commit's tree hash and the zip's sha256, and upload the zip to OSF. The tree hash is the content fingerprint; the zip is the immutable copy.
- **The study runs from a fresh clone of the tag**, never from this repository.
- Creating the package's public repository and uploading to OSF need your go.

### D3. Registration, in two steps

1. **Freeze the package and register on OSF** before the author or the system reads any held-out transcript (21 plan's rule 3).
2. **Build and verify the held-out gold** under the registered procedure. Then add its hash in a dated addendum before any run.

**What the registration fixes:**
- **Held-out series and the rule that selected them.** Two series are recommended:
  - KUFR (ELITR series B, 3 meetings, 17–31 May 2019);
  - a different kind of series, an unseen AMI scenario series selected by rule (21 plan, 4.5).

  One series of three meetings is too thin for a confirmatory claim.
- **Gold procedure.**
  - Candidates come from the minutes and AMI annotations before any system output exists.
  - You verify them, and a second annotator does too.
  - Disagreements are adjudicated and recorded.
- **Arms:**
  - the final configuration;
  - RAG (the frozen selected configuration), in the same period;
  - A1 (bugs fixed, no contracts), required whenever the final configuration includes a contract, because the contracts' verdicts need it.

  A0 does not run on held-out data, since its results are defect-limited.
- **Repeats:** 5.
- **Mechanisms under test.** Drafted in Phase C and fixed here:
  - each contract in the final configuration;
  - the architecture's mechanisms for the conversational difficulties: epistemic status, change and supersession, rejection, restraint on incidental talk, complete decisions, evidence and provenance.
- **Verdicts.** Each mechanism gets an endpoint and a pre-registered rule for *works*, *doesn't work* or *can't tell*.
  - Switchable mechanisms are judged by an on/off contrast:
    - for the contracts, A1 against the final configuration. That gives a joint verdict; a per-contract verdict needs one extra arm per contract, which is decided here.
    - for restraint, if kept, the per-component switches.
  - Architectural mechanisms are judged by their family endpoint against RAG. The loss trace shows at which boundary their failures arise.
  - Every registered verdict is reported, so none can be picked afterwards.
- ***Can't tell*** applies:
  - when the effect lies within the instrument range;
  - when a known defect affects the mechanism. This cuts both ways: bug 2 propped up the evidence answers, so a defect can produce a false *works* as well as a false *doesn't work*.

  "Affected" is decided by a rule fixed here, from the incidence checks and the attribution coding.
- **The RAG comparison** is reported as an estimate: the paired overall difference with its interval, with no success threshold. Per-family differences are context for the verdicts.
- **Registered analyses:**
  - the loss trace (B2, bug 11);
  - the attribution coding. Each failure (all of them, or a registered random sample) is coded as an implementation defect, an architectural weakness, a design trade-off, a conversational difficulty or an evaluation defect. A second coder codes a subset. A failure coded as an implementation defect makes its mechanism *can't tell*.
- **Statistics:**
  - Intervals come from resampling questions or meetings, not from three repeat clusters.
  - The instrument range for the new series is defined here, for example from V6 on the held-out answers. The cycle-1 ranges were per series (ES2009 14.4 points, EL2020 0) and do not transfer.
  - Absolute scores are never compared across series.
- **Failures other than infrastructure.** Batch R showed that a guardrail can stop a batch. The default: such a run is reported, not re-run, and counted as a failure. Any other handling needs a dated amendment filed before any outcome is read.
- **The stop rule.**

## Phase E: Confirmatory study

- Run once, from a fresh clone of the package tag.
- Report every run, and every result whatever its direction.
- Re-runs only for logged infrastructure failures. Other failures are handled as registered (Phase D3).
- A defect found during or after the run is documented, not fixed. The mechanisms it affects get *can't tell*.

## Phase F: The thesis

1. **First, once Phase E is done** (moved here on 27 October; it previously ran "now, independent of Phases B–E", so the thesis is rewritten once, at the end):
   - the P0 text fixes in `22-fix-priorities.md`, as that file stands at ce75b1f, so the current text is honest at every point. Their content was fixed before any outcome. Any change to their wording made after the outcomes were read is disclosed as such;
   - P1-3, so Ch. 4 says which arm enforces which design decision;
   - the text actions that Step 0 of amendment 1 decided before signing (decision sheet C46, C47, C48 (b)), and the wording entries it leaves to this phase (C43.3, C48, C50, C53, C55, C56).
2. **Framing:**
   - **Ch. 1** states the objective and the central question as a clarification of why RQ1–RQ4 were asked, not as a retelling. In outline: the aim was always to learn about the transformation from conversation to maintained state; the research questions measured the artifact as the means; the audit showed that measurement was confounded, and this is what was done about it.
   - **Contributions** are the investigation: what works, what doesn't, and where. The confirmatory study sets how strong its empirical part is.
   - **Ch. 2** keeps the difficulties that come from conversation apart from those the architecture introduces. The domain is conversational language from transcripts, not speech. This means:
     - rewording "Spoken project language" (`problem_domain.tex:133`);
     - adding a transcript-only boundary to the scope list, whose "two four-meeting series" also changes.
   - **Ch. 4** traces each decision from a Ch. 2 difficulty; P0-D labels the retrospective parts.
   - **Ch. 6** follows, for each mechanism, the chain from conversational challenge to design response, observed behaviour and design lesson.
     - Claims stay bounded to the series tested: design propositions, not general principles.
     - Three questions stay apart: did the artifact work, what did the investigation learn, and how strong is the evidence.
   - **Critical reflection:** the audit appears as reflection on method (why the defects went undetected, what changed), not as findings about the design.
3. **Focus pass.**
   - State the argument in one paragraph.
   - Check the apparatus against the central question: RQ1–4, H1–9, DR1–8, D1–11, the batches, the stance screenings and the instrument ranges.
   - Cut or move to an appendix whatever does not serve it.
4. **Structure:**
   - Ch. 5 becomes the development evaluation. It contains:
     - cycle 1;
     - the disclosed reframing;
     - the audit, as the reason for measuring again;
     - the bug reproductions and incidence;
     - the development comparisons A0/A1/A2.
   - A new chapter holds the confirmatory evaluation.
   - The abstract, the Ch. 1 contributions and the Ch. 6 conclusions report the per-mechanism verdicts; the confirmatory study sets their strength.
   - Under the fallback (Phase D1), Ch. 5's development study is the empirical contribution, framed as formative.
5. **Disclose:**
   - the review was performed by LLM agents and checked in part by hand;
   - what was independently checked, and by whom (the 21 plan's standing rule).

## Integrity rules carried over from the 21 plan, and what changes

| 21 plan rule | Under this plan |
|---|---|
| 1. Baseline preserved behind switches | Kept. The bug fixes are switches too. |
| 2. No tuning on test material | ES2009 and EL2020 are both development data now. Only the held-out series are test material. |
| 3. Predictions before runs | Required for the confirmatory study: an OSF registration with the package's tag, tree hash and zip, and the verdict rules. Development runs are logged, not pre-declared. |
| 4. Same measurement | The instrument is repaired (B2, B3). Cycle-1 numbers are reported under both the original and the repaired instrument, where rescoring allows. |
| 5. Every run reported | Kept. |
| 6. No new human labelling | Lifted for the confirmatory study. |
| 7. No formal v7 batch | Revisit: the confirmatory study may be the formal protocol run once its gates (V6 among them) are met. |
| 8. One code freeze per cycle | One freeze, for the confirmatory study only: the clean evaluation package (Phase D2). Development is not frozen. |

## Freeze note

- The cycle-2 launcher refuses to start while app/, scripts/ or tests/ have uncommitted or untracked changes. The new test file therefore blocks any relaunch on `cycle2-freeze-2`.
- That is intended, since those batches are superseded. Any later batch needs its own freeze.
- The confirmatory study does not use this repository's freeze. It runs from the package (Phase D2).

## Rough cost and time

There is no deadline, so these figures are for planning only. Each batch states its own estimate and ceiling.

| Phase | Your time | Paid runs |
|---|---|---|
| B: repair and tests | review and approve | about $1 (rescoring) |
| C: development | gates | about 24–36 runs, ≈ $60–100 |
| D: gate, package and held-out gold | the package build (about a day, $0); gold verification, 1–2 h per series, plus a second annotator | — |
| E: confirmatory | attribution coding of the failures, plus a second coder on a subset | about 30 runs (2 series × 3 arms × 5 repeats), ≈ $70–110; a per-contract verdict adds 10 runs per contract |
| F: writing | reading and approving | $0 |

## Open decisions

- **Second reader:** tell them about the reframing before Phase D. The supervisor accepted it (decision 5).
- **Second held-out series:** an unseen AMI scenario series (a different kind; recommended), or ELITR series A's held-back meetings (the same project, so it tests time rather than project).
- ~~**Restraint**~~ decided 22 October: left off the verdict list (bug 8 not repaired).
- **The reference-informed arm** (bug 14). Recommended: drop it from the thesis's comparisons, and report its cycle-1 results as development data together with bug 14. The alternative is a rebuilt gate, matching against gold values only and by status, re-run under A1; even then it reads checkpoint gold, so it could serve only as a diagnostic, not as a confirmatory arm. The thesis text on the arm follows the decision: eval.tex §H7, the abstract ("The reference-informed policy scores below the autonomous one") and Ch. 1 ("a measured negative result for a reference-informed acceptance policy").
- **Per-contract verdicts:** one extra arm per contract, or a joint verdict for the contracts.
- **Reviewers:** who annotates the held-out gold, V6, V4 and the attribution coding.
- **The package repository:** its local path, its name, and public or private.
