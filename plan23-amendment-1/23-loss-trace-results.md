# Loss trace: EL2020 results, A0 / A1 / A2 (23 October 2026)

**Inputs:**
- The nine same-period EL2020 runs of `23-el2020-arms.md`: A0 ×3, A1 ×3, A2 ×3.
- Script `23-loss-trace.py` (v3.1); codebook `23-loss-trace.md`.
- Adjudications `23-loss-trace-adjudications.yaml`: 670 decisions, model, not human.
- Output `23-loss-trace.json`.

The output has `primary_series_complete: true`: no adjudication item is open. Development result (plan 23, Phase C): one series, three runs per arm.

**How to read it:**
- **Units:**
  - The unit is a **row**: one current gold value at one checkpoint. There are 133 per run.
  - They cover 56 distinct values: 11 / 28 / 42 / 52 rows at checkpoints 0–3. A value that persists is counted at every checkpoint, so row counts weigh late, persistent values more.
  - Distinct-value counts are given where the unit matters.
- **Counting:** each row is lost at the first step it fails, or passes.
- **Figures:** means over the three runs of an arm, with the runs in brackets where useful.
- **Series:**
  - **Primary** = strict bound with every deciding text adjudicated.
  - **Raw** = no adjudications.

## Where the current rows are lost

| First loss (current rows, of 133) | A0 | A1 | A2 |
|---|---:|---:|---:|
| Extraction | 46.0 (39/52/47) | 44.3 (45/40/48) | 39.7 (38/44/37) |
| Filing | 21.7 (24/22/19) | 25.7 (21/34/22) | 61.7 (68/58/59) |
| State maintenance | 24.0 (18/29/25) | 22.0 (26/21/19) | 3.3 (3/1/6) |
| Reading (asked rows) | 9.3 | 11.0 | 5.3 |
| Passes (stored, right status) | 32.0 | 30.0 | 23.0 |
| of which also read and answered | 14.3 | 12.3 | 8.0 |
| Distinct values stored with the right status at some checkpoint | 27 / 22 / 28 | 26 / 22 / 24 | 9 / 12 / 11 |

**Outcomes behind the boundaries** (mean rows per run; sub-codes of at most 1 in every arm omitted):

| Outcome | A0 | A1 | A2 |
|---|---:|---:|---:|
| `carried:claims_without_the_value` | 28.3 | 26.3 | 26.0 |
| `modality:carried_only_proposed` | 10.3 | 8.7 | 6.0 |
| `admitted:ignored` | 4.0 | 4.0 | 5.0 |
| `polarity:negated_value_read_as_rejection` | 2.0 | 2.3 | 0.7 |
| `carried:no_claims_from_cited_span` | 0.7 | 2.0 | 1.3 |
| `proposed:another_value_won` | 21.3 | 15.0 | 2.3 |
| `proposed:same_meeting_conflict` | 0 | 0 | 36.7 |
| `filed:cycle2_parked_unsupported_by_span` | 0 | 0 | 14.0 |
| `applied:proposal_expired` | 0 | 4.0 | 5.3 |
| `proposed:current_value_ranks_higher` | 0 | 3.3 | 0 |
| `current:overwritten_by_non_gold_value` | 19.7 | 19.0 | 3.0 |
| `current:displaced_by_other_gold_value` | 4.3 | 3.0 | 0.3 |
| `key_reached:other_keys_resolved` | 6.7 | 7.3 | 3.7 |
| `answered:answer_or_judge` | 1.7 | 2.7 | 1.0 |
| `ok:stored_not_asked` | 17.7 | 17.7 | 15.0 |
| `ok:None` (read and credited) | 14.3 | 12.3 | 8.0 |

**Funnel** (rows reaching → passing each step, current rows):

| Step | A0 | A1 | A2 |
|---|---|---|---|
| carried | 129 → 99.3 | 129 → 100.7 | 128 → 100.0 |
| modality | 97.3 → 87.0 | 98.3 → 88.7 | 99.3 → 93.3 |
| filed | 87.0 → 87.0 | 88.7 → 88.7 | 93.3 → 77.3 |
| proposed | 87.0 → 65.3 | 88.7 → 67.0 | 77.3 → 37.0 |
| applied | 65.3 → 65.3 | 67.0 → 63.0 | 37.0 → 31.7 |
| current | 65.3 → 41.3 | 63.0 → 41.0 | 31.7 → 28.3 |
| status | 41.3 → 41.3 | 41.0 → 41.0 | 28.3 → 28.3 |
| key_reached (asked) | 23.7 → 16.7 | 23.3 → 15.7 | 13.3 → 9.3 |
| in_payload | 16.7 → 16.0 | 15.7 → 15.0 | 9.3 → 9.0 |
| answered | 16.0 → 14.3 | 15.0 → 12.3 | 9.0 → 8.0 |

**Other kinds** (per run: 16 ruled-out rows, 9 demoted rows, 1 candidate):
- **Ruled-out values** are mostly lost at extraction in every arm: 9.3 / 8.7 / 8.7 of 16.
  - The largest part, 6.0 / 5.7 / 6.0, is `polarity:carried_only_positive`: the option was extracted, but only as a positive claim, not as its rejection.
  - A2 adds 5.3 filing losses, 3.3 of them parked negations, leaving 1.7 that pass, against 4.7 / 4.0 for A0 / A1.
- **Demoted values** are mostly never stored: about 6 of 9.
  - Of those that were stored, 1.0 of 3.3 are still current at the checkpoint in A0, 0 of 3 in A1, and 2.3 of 3 in A2.

**Flags:**
- `credit_without_state` (a single-value question scored correct without the stored value among its answer facts):
  - current rows per run: A0 2/4/4, A1 2/2/3, A2 4/4/0;
  - against correct single-value current_state questions: about one in six in A0 (9 of 52) and A1 (7 of 44), and 8 of 29 in A2. In A2 r1 it is 4 of 7, mostly values the support check parked.
- **Defect flags:** 33–36 current rows per A0 run carry one, 0 in A1 and A2.

## What the trace says

- **In the adjudicated series, extraction is the largest loss in A0 and A1:** about 45 of 133 rows are never carried by an asserted claim with the right polarity.
  - Most (26–28 per run on average, 24–31 in single runs) have claims from the cited span that do not state the value.
  - About 9–10 are stated only as proposed.
  - No repair changes the extraction code. Extraction does see the run's state-key registry, which downstream processing shapes. Even so, the extraction losses do not move between A0 and A1 (46.0 vs 44.3).
- **A0 and A1 store about the same, through different sub-codes.** Each stores about 41 rows with the right status by the checkpoint (22–28 distinct values per run).
  - A1 replaces about 6 `another_value_won` losses with `proposal_expired` (4.0) and `current_value_ranks_higher` (3.3), the bug-13 and bug-3 repairs at work.
  - State-maintenance losses are level (24.0 vs 22.0): in both arms the gold value is overwritten on its key by a non-gold value (19.7 and 19.0).
  - This is the trace-level counterpart of the score result in `23-el2020-a0-a1.md`: A1 does not beat A0.
- **In A2, filing losses rise and state-maintenance losses fall:**
  - Filing goes up by about 36–40 rows per run, and state maintenance down by about 20.
  - Of the rows that reach state maintenance, A2 loses 10% there, against 35–37% in A0 and A1. So values that are applied are rarely overwritten; 3.0 rows per run still are.
  - The extra filing losses are not only the old overwrites. Rows that an A0 or A1 run stores with the right status are lost at filing in an A2 run about 50% of the time, against 14–17% between A0 and A1 runs.
  - A2's filing losses:
    - 36.7 rows (11–21 distinct values) end in same-meeting conflicts that the autonomous arm never resolves;
    - 15 are parked claims (14.0 unsupported by span, 1.0 no fitting key);
    - 5.3 are expired proposals.
  - A2 stores 28.3 rows with the right status (9–12 distinct values), against about 41 rows (22–28 values) for A0 and A1.
  - That accounts for most of A2's current_state drop: about 7.7 of the 10.3 questions per run it loses against A0. The rest of the score gap is in rejection (parked negations), noise resistance and evidence.
  - The conflicts mostly mix different matters on one key (`23-el2020-arms.md`, sample of 16 keys).
- **Reading:** of the asked rows stored with the right status, 39–47% fail at reading.
  - The largest part are lost at key resolution (6.7 in A0, `other_keys_resolved`). In A0 r1, about half of those hold the value under a key unrelated to the question's topic, so routing contributes to them too.
  - Once the key is resolved and the fact given, the answer is credited in most cases (14.3 of 16.0 in A0).

## Effect of adjudication

| First loss, current rows (mean per run) | A0 raw strict | A0 primary | A1 raw strict | A1 primary | A2 raw strict | A2 primary |
|---|---:|---:|---:|---:|---:|---:|
| Extraction | 34.7 | 46.0 | 30.0 | 44.3 | 25.7 | 39.7 |
| Filing | 19.3 | 21.7 | 29.3 | 25.7 | 67.3 | 61.7 |
| State maintenance | 30.0 | 24.0 | 25.0 | 22.0 | 4.7 | 3.3 |
| Reading | 12.7 | 9.3 | 15.0 | 11.0 | 7.3 | 5.3 |
| Passes | 36.3 | 32.0 | 33.7 | 30.0 | 28.0 | 23.0 |

- **Adjudication moves a net 11–14 rows per run to extraction:** about 15 in and 2 out; 7–18 in single runs.
- **What it rejects.** Of the 130 open round-3 texts that both adjudicators rejected:
  - 71 state only one part of a multi-part value, for example "small MP3 files" for the two-part storage rule; the matcher had often counted these through a gold alias;
  - 41 state a different value;
  - 8 state a sibling's value;
  - 10 fall elsewhere.
- **What holds under either series:**
  - A2's profile (filing up, state maintenance near zero) holds in both.
  - A0 ≈ A1 holds for the pass counts in both, but for the boundary profile only in the primary series: unadjudicated, A1 loses about 10 more rows per run at filing and fewer at extraction.
  - "Extraction is the largest loss" needs the adjudicated series:
    - in A1 it is level with filing in the raw strict bound (30.0 vs 29.3) and behind it in the raw lenient bound (24.7 vs 29.0);
    - in A0 it stays ahead in raw strict (34.7) but is level with state maintenance in raw lenient (30.3 vs 29.7).

## Verification (details in the codebook)

**Three rounds, about 90 agents.**
- Each round had blind hand-traces from the raw run files, a matcher audit, a code review and a skeptic per finding.
- Agreement of the blind coders with the script on the first failing step:
  - 38/48 rows for v1;
  - 15/24 for v2 (held-out A2 r1);
  - 21/24 for v3 (held-out A2 r2b and r3).
- The three round-3 disagreements: two main-decision-versus-part calls on compound values (F32, F82) and one paraphrase the matcher cannot propose (F36).

**Adjudication:**
- In round 3 the two independent adjudicators both decided 635 of the 637 items, and agreed on 615 (96.9%, kappa 0.94). 22 went to the tie-break: the 20 disagreements and 2 items missing one decision.
- The fixpoint round of 33 items had full agreement.
- **The decisions are model judgements:** a human second coder on a sample (V4) is still required before Phase D.

**Transaction-time state:** the output records the check (`pack_check`):
- per question and resolved key, the rebuilt current facts equal what the reader got: 9551 / 9551;
- the status at k of every fact the reader got equals its pack status: 8430 / 8430 (answer facts and near matches; 7993 / 7993 answer facts alone).

**These notes** were recomputed and challenged by three further independent agents. The corrections they found are in this version.

## Limits

- One series (EL2020), three runs per arm, development only.
- The decisions are model adjudications. The standard (one part of a compound value does not carry it) is stricter than the gold aliases, which list some parts.
- The trace follows values, not keys, and locates the first missing condition, not a cause; see the codebook's Limits.
