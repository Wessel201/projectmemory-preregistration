"""Plan 23 amendment 1, Step 0: the adjudication audit list.

What the list covers:
- The amendment's criterion is "every v1 decision that decides an oracle row
  result" (amendment line 115). The same line then names two kinds of
  decision: the carrier decisions on A0/A1 rows lost at filing or state
  maintenance, and the "does not carry" decisions on values lost at extraction
  in an A0/A1 run.
- This script computes those two kinds, plus the rival decisions that decide R.
- It does not cover the whole criterion. Open decisions AL-1 and AL-3 below
  name the v1 decisions it leaves out. The author decides whether they join
  the list; DECISIONS records the choice.

Roles, computed from the frozen loss trace and the v1 adjudications:
- r_carrier: decisions on the carrier texts of A0/A1 rows lost at filing or
  state maintenance (the texts in a row's support). They decide R.
- r_rival: decisions on the rival texts of those rows that are not already
  carrier decisions. A rival text is either of these:
  - a wording pair of the row (the loss trace records these only for rows lost
    at the proposed step);
  - for a row lost at state maintenance, a successor value: a value that
    overwrote or displaced the gold value by k. Only decisions on the row's own
    fact id count.
  R files carriers under the gold key and removes non-carriers, so whether a
  rival carries the value decides R too.
- e_no_carry: the "does not carry" decisions on every value with an A0/A1 row
  lost at extraction. They decide whether a row is extraction-lost, and so E+R
  against R. This takes every false decision on such a value, whichever run its
  text came from: a superset of the decisions any one A0/A1 row depends on.

Roles that enter only if the author adopts an option of AL-1 or AL-3:
- e_wrong_form_carrier (AL-1): decisions on the carried texts (support
  "carried") of A0/A1 rows lost at polarity or modality. They decide E+R and
  E+R* on those rows, and the exceptions of amendment line 373.
- r_shared_key_carrier (AL-3): decisions on the carrier texts of F25 or F36 in
  an A0/A1 run where the value that shares its gold key (F58 or F59, amendment
  line 203) is lost at filing or state maintenance at or after the first
  checkpoint where the text is a carrier. They decide R on those rows.
- r_pass_carrier (AL-3): decisions on texts that are support texts only of
  A0/A1 rows that passed or were lost at reading. They decide R's pass-to-lost
  column (amendment line 209).

A decision can have more than one role (a rival text of a value that is lost at
filing in one run and at extraction in another); it is listed once.

Fields of each item:
- id: the first 12 hex digits of the SHA-256 of "fact_id|text".
- fact_id, text: the v1 decision, as in the adjudications file.
- roles: as above.
- decides_rows: the rows that each role's rule names, for every role except
  e_no_carry.
  - For r_carrier and r_rival: the A0/A1 rows lost at filing or state
    maintenance whose support, wording pairs or successor values hold the text.
  - For the optional roles: the rows named in their rules above.
  - An item whose only role is e_no_carry has an empty list. That does not
    mean that the decision decides no row.
  - The field leaves out rows decided through the sibling rule
    (23-loss-trace.py:711), and, except for r_shared_key_carrier, through the
    two-gold-key routing rule (amendment line 203).
  - Line 410's agreement over rows the oracles flip takes its rows from the
    oracle outputs, not from this field.
- recorded_result_rows: only on items with a successor-value rival. These are
  the rows where the text is the row's last successor value by k.
  - There the decision also sets the recorded loss. If it were true, the
    successor fact would hold the value and the row would pass the current
    step.
  - On the other rows in decides_rows, a later value overwrote the text by k.
    There the decision bears on R only. For F06 the trace records those rows
    as displaced by F38 or F39, so the two-gold-key routing rule also applies.

Rows are named "<run suffix>:<fact_id>@<k>". The JSON header's run_map gives
each suffix's arm and run folder, copied from 23-loss-trace.json
(runs[].run_id, runs[].arm, runs[].dir).

The list and the v1 labels:
- The list has no label field. But its roles and decides_rows determine every
  v1 label. r_carrier and each optional role are always true. e_no_carry and
  r_rival are always false. The script checks this and stops if it fails.
- Anyone who holds the list, or the v1 adjudications file, can recover the
  labels. So V4 gets only the packet fields below, never the list itself.

V4's packet, proposed rule for the signing note (open decision AL-5):
- Fields: id, fact_id, the gold value and its aliases, text, and the text's
  context.
- Excluded: roles, decides_rows, recorded_result_rows, and any field derived
  from them.
- Order: ascending SHA-256 of "<salt>|<id>", with the salt stated in the
  signing note.
- Access: V4 has no access to the repository or to the tagged commit (which
  holds the v1 adjudications file) until their audit labels are hashed.

The inputs are checked against the hashes frozen in the amendment.

Open decisions for the author:
- DECISIONS below holds the choices. None means open; nothing is then added.
- Setting an option and re-running the script adds its decisions. The JSON's
  open_decisions lists every candidate decision and the count each option
  adds. The counts are against the list with no option adopted.

AL-1. The carrier decisions on A0/A1 rows lost at polarity or modality.
- What is left out: 44 true decisions on 17 values. They are carried texts of
  the 120 A0/A1 rows lost at polarity or modality, and they are not on the
  list. Every one of the 120 rows rests on a v1-decided carrier. 105 of them
  have at least one carrier that is not on the list.
- Why it matters: R files every carrier, whatever its polarity, under the gold
  key (amendment line 203). E+R* still loses "any remaining wrong-modality
  carriers and positive carriers of ruled-out values" (amendment line 206).
  Line 373's exception turns on such a carrier. With these decisions
  unaudited, v2 equals v1 on them, so the rule of amendment line 95 cannot
  test them. The false decisions on the same values are listed (every such
  value is extraction-lost), so v2 can still change these rows through them.
  What goes untested is an error in the carrier decisions themselves.
- Where the risk is: 54 of the 105 rows are current values lost at modality.
  There the injected asserted claim should confirm the value either way, so
  the decision changes the sub-code more than the E+R result. The results at
  real risk are on 51 rows (ruled-out at polarity 35, ruled-out at modality
  12, negated current value 4). They rest on 15 of the 44 decisions.
- Two of the three F25 decisions also sit on the gold key that F25 shares with
  F58. They are carriers by k in 44a72348 (F58@3), f03636da (F58@2-3) and
  15995a72 (F58@2-3), where F58 is lost at filing or state maintenance. The
  third is a carrier only in 48405ba5, where F58 is lost at extraction.
- Options:
  - a: keep line 115's enumeration. The signing note states that E+R and E+R*
    results, and the line-373 exceptions, on these rows rest on unaudited v1
    decisions.
  - b: add all 44 with role e_wrong_form_carrier, citing line 115's first
    sentence as the criterion. Three listed decisions (one on F30, two on F38)
    also gain the role and their rows.
  - b_prime: add only the 15 decisions with a row that is ruled-out or lost
    as a negated current value.
- Recommendation: b. Line 206 names both kinds of carrier as sources of loss
  under E+R*. The list grows from 430 to 474 decisions (479 with AL-3's
  a_shared). Amendment line 583 plans "about 420 audit decisions (2–3 h)" for
  V4; the signing note records the change.

AL-3. The carrier decisions on A0/A1 rows that passed or were lost at reading.
- What is left out: 56 true decisions on 26 values. They are support texts
  only of such rows: 110 distinct rows, 128 decision-row incidences. 27 of them
  are the only carried text of 82 rows (39 current pass, 22 ruled-out pass,
  14 current reading, 7 ruled-out reading).
- Why it matters: they decide R's pass-to-lost column (amendment line 209).
  Under v2 they also decide whether a recorded pass is a pass at all. The
  audited decisions can move recorded losses later or turn them into passes.
  They can turn a pass into a loss only indirectly (through the sibling rule,
  or a demoted row). So the v2 loss-trace figures (amendment line 410) are
  biased toward recovery.
- Line 115's enumeration does exclude them, and caused-at uses oracle results
  only for rows lost at or before the status step (amendment line 368).
- Five of them are F36 carriers by k in runs where F59, which shares F36's
  gold key, is lost at filing or state maintenance (44a72348 F59@2; f03636da
  F59@3). They decide F59's R result on lost rows.
- Options:
  - a: keep the exclusion. The signing note discloses the bias toward
    recovery.
  - a_shared: as a, plus role r_shared_key_carrier. This adds the five F36
    decisions, and the two F25 decisions of AL-1 that meet the rule if AL-1
    does not add them. Four listed F36 decisions also gain the role and their
    F59 rows.
  - b_sole: a_shared, plus the 27 sole-carrier decisions with role
    r_pass_carrier.
  - b_all: a_shared, plus all 56 with role r_pass_carrier.
- Recommendation: a_shared, with the disclosure. The shared-key decisions
  decide R on lost rows of another value. The other pass carriers set no
  caused-at boundary.

AL-5. When V4's packet rule is fixed.
- The rule matters at Step 3, item 6 (amendment line 410), not at Step 0.
- Options:
  - a: fix it now, in the signing note, as proposed above.
  - b: fix it at Step 3, item 6, before the packet is built.
- Recommendation: a. It is cheap pre-commitment. The salt is a fixed string
  that the signing note states.

AL-7. Where the list's hash is recorded.
- Amendment line 115 requires that "the list is committed with its hash". This
  script prints the SHA-256 of the JSON it writes. The JSON records the hashes
  of its inputs and of this script, but no file records the JSON's own hash.
- Options:
  - a: the signing commit message and the annotation of the tag
    plan23-amendment-1.
  - b: a signing note next to the frozen-input table.
- Not in the run manifest or the register files. The page-provenance check
  of 23-am1-precoder-template.md (section "How blindness is checked", item 1)
  admits a hash found in "the run manifest, or the signed register files".
  That would admit a file whose roles encode the v1 labels.
- Recommendation: a, with the script's hash beside it. Every later output
  cites the tag (amendment line 14). Also name the audit list in that
  check's exclusion of "any audit or v2 file".

Review record (27 October 2026):
- Workflow: am1-step0-verify. A reviewer raised the findings, and a skeptic
  tried to refute each. AL-1, AL-2, AL-3, AL-5, AL-6 and AL-7 survived.
- AL-1: not applied. It needs the author's judgement (open decision AL-1). The
  claim that the list meets line 115's criterion is corrected, here and in the
  JSON's "what" field. The finding's evidence names three F25 carriers on the
  shared key; only two are carriers in runs where F58 is lost at filing or
  state maintenance.
- AL-2: applied. r_rival also takes the successor values of A0/A1 rows lost at
  state maintenance, decided on the row's own fact id. This adds 4 decisions
  (two on F01, two on F06; 17 rows) and gives one listed decision (F62,
  "bigger files") the role. recorded_result_rows marks the rows whose recorded
  loss the decision sets: the five k=1 rows of F01 and F06, and
  48405ba5:F62@3. The list now holds 430 decisions.
  The author confirms the addition at signing, since it extends line 115's
  enumeration in the way r_rival already does.
- AL-3: not applied. It needs the author's judgement (open decision AL-3). The
  count wording is corrected: 110 distinct rows, 128 decision-row incidences.
- AL-4: not among the surviving findings; no change.
- AL-5: applied in part. The text above now says that the roles and
  decides_rows determine the v1 label, and the script checks it. The packet
  rule is proposed above; when to fix it is open decision AL-5.
- AL-6: applied. decides_rows is documented above, and the JSON header has a
  fields note and a run_map copied from 23-loss-trace.json. The rows for E
  decisions are not computed by hand; line 410's rows come from the oracle
  outputs.
- AL-7: not applied in this file. The hash belongs in the signing record,
  outside this file (open decision AL-7). The edits above change both hashes;
  the script prints the new list hash when it runs.

Usage: .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-audit-list.py
Writes 23-am1-audit-list.json next to this script.
"""

import collections
import hashlib
import json
import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
TRACE = HERE / "23-loss-trace.json"
ADJ = HERE / "23-loss-trace-adjudications.yaml"
OUT = HERE / "23-am1-audit-list.json"
FROZEN = {
    TRACE.name: "da4576242eda6fc181352eb8a4f74172c2961b187ca5e1b5391142c554c9e8a9",
    ADJ.name: "e084d95cd72431fd494b8e5aa7c9e1c69ad80da3481e1271c9d88cd6c272f089",
}
ORACLE_ARMS = ("A0", "A1")
LOST_R = ("filing", "state_maintenance")
SHARED_KEYS = {"F25": "F58", "F36": "F59"}  # amendment line 203

# The author's choices on the open decisions; None means open (nothing added).
DECISIONS = {"AL-1": "b", "AL-3": "a_shared"}  # adopted at signing (decision sheet C18, C20)
OPTIONS = {
    "AL-1": {"a": (), "b": ("e_wrong_form_carrier",), "b_prime": ("e_wrong_form_carrier:ro",)},
    "AL-3": {
        "a": (),
        "a_shared": ("r_shared_key_carrier",),
        "b_sole": ("r_shared_key_carrier", "r_pass_carrier:sole"),
        "b_all": ("r_shared_key_carrier", "r_pass_carrier"),
    },
}
RECOMMENDED = {"AL-1": "b", "AL-3": "a_shared"}
TRUE_ROLES = ("r_carrier", "e_wrong_form_carrier", "r_shared_key_carrier", "r_pass_carrier")
FALSE_ROLES = ("e_no_carry", "r_rival")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decision_id(fact_id, text):
    return hashlib.sha256(f"{fact_id}|{text}".encode()).hexdigest()[:12]


def main():
    for path in (TRACE, ADJ):
        if sha(path) != FROZEN[path.name]:
            raise SystemExit(f"{path.name} does not match its frozen hash")
    for d, choice in DECISIONS.items():
        if choice is not None and choice not in OPTIONS[d]:
            raise SystemExit(f"{d}: unknown option {choice!r}")
    trace = json.loads(TRACE.read_text())
    v1 = yaml.safe_load(ADJ.read_text())["decisions"]
    label = {(f, t): v for f, d in v1.items() for t, v in d.items()}

    rows = collections.defaultdict(set)
    recorded = collections.defaultdict(set)
    roles = collections.defaultdict(set)
    extraction_values = set()
    # rule rows for the optional roles, keyed by (fact_id, text)
    opt_rows = {r: collections.defaultdict(set) for r in (
        "e_wrong_form_carrier", "e_wrong_form_carrier:ro", "r_shared_key_carrier", "r_pass_carrier",
        "r_pass_carrier:sole")}
    support_boundaries = collections.defaultdict(set)
    first_carrier_k = collections.defaultdict(dict)  # (fact_id, text) -> {run suffix: k}
    lost_r_rows = collections.defaultdict(list)  # (run suffix, fact_id) -> [k]
    run_map = {}
    for run in trace["runs"]:
        if run["arm"] not in ORACLE_ARMS:
            continue
        rid = run["run_id"].rsplit("_", 1)[-1]
        run_map[rid] = {"arm": run["arm"], "dir": run["dir"]}
        for rec in run["strict"]["records"]:
            fid, k = rec["fact_id"], rec["k"]
            row = f"{rid}:{fid}@{k}"
            if rec["boundary"] == "extraction":
                extraction_values.add(fid)
            carriers = {t for texts in rec["support"].values() for t in texts}
            for t in carriers:
                if (fid, t) in label:
                    support_boundaries[(fid, t)].add(rec["boundary"])
                    ks = first_carrier_k[(fid, t)]
                    ks[rid] = min(k, ks.get(rid, k))
            if rec["loss"] in ("polarity", "modality"):
                ro = rec["kind"] == "ruled_out" or rec["sub"] == "negated_value_read_as_rejection"
                for t in rec["support"].get("carried", []):
                    if (fid, t) in label:
                        opt_rows["e_wrong_form_carrier"][(fid, t)].add(row)
                        if ro:
                            opt_rows["e_wrong_form_carrier:ro"][(fid, t)].add(row)
            if rec["boundary"] in (None, "reading"):
                carried = rec["support"].get("carried", [])
                for t in carriers:
                    if (fid, t) in label:
                        opt_rows["r_pass_carrier"][(fid, t)].add(row)
                        if carried == [t]:
                            opt_rows["r_pass_carrier:sole"][(fid, t)].add(row)
            if rec["boundary"] not in LOST_R:
                continue
            lost_r_rows[(rid, fid)].append(k)
            for t in carriers:
                if (fid, t) in label:
                    roles[(fid, t)].add("r_carrier")
                    rows[(fid, t)].add(row)
            successors = rec.get("successor_values", []) if rec["boundary"] == "state_maintenance" else []
            for t in (set(rec["wording_pairs"]) | set(successors)) - carriers:
                if (fid, t) in label:
                    roles[(fid, t)].add("r_rival")
                    rows[(fid, t)].add(row)
                    if successors and t == successors[-1]:
                        recorded[(fid, t)].add(row)
            for t in set(successors) - carriers:
                if (fid, t) in label:
                    recorded.setdefault((fid, t), set())
    for (f, t), v in label.items():
        if f in extraction_values and v is False:
            roles[(f, t)].add("e_no_carry")

    # pass carriers: support texts only of rows that passed or were lost at reading
    for key in list(opt_rows["r_pass_carrier"]):
        if not support_boundaries[key] <= {None, "reading"}:
            del opt_rows["r_pass_carrier"][key]
            opt_rows["r_pass_carrier:sole"].pop(key, None)
    # shared-key carriers: carriers of F25/F36 by k on rows where F58/F59 is lost at filing or state
    for (f, t), ks in first_carrier_k.items():
        if f not in SHARED_KEYS:
            continue
        for rid, k0 in ks.items():
            for k in lost_r_rows.get((rid, SHARED_KEYS[f]), []):
                if k >= k0:
                    opt_rows["r_shared_key_carrier"][(f, t)].add(f"{rid}:{SHARED_KEYS[f]}@{k}")

    base = set(roles)
    open_decisions = {}
    for d, opts in OPTIONS.items():
        rules = sorted({r for rs in opts.values() for r in rs})
        cands = sorted({key for r in rules for key in opt_rows[r]} - base)
        by_option = {}
        for o, rs in opts.items():
            keys = {key for r in rs for key in opt_rows[r]}
            by_option[o] = {"adds_items": len(keys - base), "listed_items_gaining_a_role": len(keys & base)}
        open_decisions[d] = {
            "status": "open" if DECISIONS[d] is None else f"adopted: {DECISIONS[d]}",
            "recommended": RECOMMENDED[d],
            "options": by_option,
            "candidates": [
                {
                    "id": decision_id(f, t),
                    "fact_id": f,
                    "text": t,
                    "added_by": sorted(o for o, rs in opts.items() if any((f, t) in opt_rows[r] for r in rs)),
                    "rows_by_role": {r: sorted(opt_rows[r][(f, t)]) for r in rules
                                     if ":" not in r and (f, t) in opt_rows[r]},
                }
                for f, t in cands
            ],
        }
        if DECISIONS[d] is not None:
            # a rule "role:subset" selects decisions by the subset; their rows are the role's full rows
            for r in opts[DECISIONS[d]]:
                role = r.split(":")[0]
                for key in opt_rows[r]:
                    roles[key].add(role)
                    rows[key] |= opt_rows[role][key]

    # the roles determine the v1 label (finding AL-5); stop if that ever fails
    for key, rs in roles.items():
        want = {label[key]}
        got = {True for r in rs if r in TRUE_ROLES} | {False for r in rs if r in FALSE_ROLES}
        if got != want:
            raise SystemExit(f"roles {sorted(rs)} do not match the v1 label of {key}")

    items = []
    for (f, t), r in roles.items():
        item = {
            "id": decision_id(f, t),
            "fact_id": f,
            "text": t,
            "roles": sorted(r),
            "decides_rows": sorted(rows.get((f, t), ())),
        }
        if (f, t) in recorded:
            item["recorded_result_rows"] = sorted(recorded[(f, t)])
        items.append(item)
    items.sort(key=lambda x: (x["fact_id"], x["text"]))
    counts = collections.Counter(role for x in items for role in x["roles"])
    values = {g: len({x["fact_id"] for x in items if g in x["roles"]}) for g in counts}
    out = {
        "what": "plan 23 amendment 1: adjudication audit list (the enumeration of amendment line 115, plus rival "
                "texts; open_decisions holds the v1 decisions it leaves out, for the author to decide)",
        "inputs": {TRACE.name: FROZEN[TRACE.name], ADJ.name: FROZEN[ADJ.name]},
        "script_sha256": sha(pathlib.Path(__file__)),
        "oracle_arms": list(ORACLE_ARMS),
        "fields": {
            "decides_rows": "rows named by each role's rule, for every role except e_no_carry; empty for an "
                            "e_no_carry-only item, which does not mean the decision decides no row; see the "
                            "script's docstring",
            "recorded_result_rows": "only on items with a successor-value rival: rows where the text is the last "
                                    "successor value by k, so the decision also sets the recorded loss",
            "rows": "named <run suffix>:<fact_id>@<k>; run_map gives each suffix's arm and folder",
            "labels": "roles, decides_rows and recorded_result_rows determine the v1 label; V4 gets only the "
                      "packet fields named in the script's docstring, never this file",
            "open_decisions": "per open decision: status, recommended option, the count each option adds "
                              "against the list with no option adopted, and each candidate decision with the "
                              "options that add it and the rows of each role it would take",
        },
        "run_map": {"source": f"{TRACE.name} runs[].run_id, runs[].arm, runs[].dir", "runs": run_map},
        "v1_decisions": len(label),
        "audited": len(items),
        "by_role": dict(sorted(counts.items())),
        "values_by_role": dict(sorted(values.items())),
        "with_two_roles": sum(len(x["roles"]) > 1 for x in items),
        "open_decisions": open_decisions,
        "items": items,
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(OUT.name, sha(OUT), out["audited"], out["by_role"], out["values_by_role"], out["with_two_roles"])
    for d, od in open_decisions.items():
        print(d, od["status"], {o: v["adds_items"] for o, v in od["options"].items()})


if __name__ == "__main__":
    main()
