"""Phase C development comparison on EL2020, all same-period arms, three runs
each: A0 (the evaluated system), A1 (all repairs), A2 (repairs plus the four
write contracts) and the frozen RAG baseline. Every arm is scored with the
repaired judge wrapper (bug 7); the ProjectMemory arms also carry the bug 9-10
dump diagnostics.

Reads the run reports only (no API calls) and writes 23-el2020-arms.json next
to this script. Development result (plan 23, Phase C): it claims nothing
beyond EL2020 and this period.

Each pairwise difference gets two 95% intervals, as in 23-el2020-a0-a1.py
(whose functions this script reuses): questions resampled (paired by
question), and questions and runs resampled. Families with few items get wide
intervals; they are reported, not tested. The state layer exists only for the
ProjectMemory arms.

Run from the repository root:
    python3 -I thesis/notes/thesis_completion/artifacts/23-el2020-arms.py \\
        --a0 DIR... --a1 DIR... --a2 DIR... --rag DIR...
Each ProjectMemory DIR holds artifacts/*.coldstart.json and *.state.json; each
RAG DIR holds artifacts/*.rag.json.
"""
from __future__ import annotations

import argparse
import glob
import json
import runpy
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
OUT = Path(__file__).with_suffix(".json")
BASE = runpy.run_path(str(HERE / "23-el2020-a0-a1.py"), run_name="arms")
arm_rate, interval, interval_runs_and_questions = (BASE["arm_rate"], BASE["interval"],
                                                   BASE["interval_runs_and_questions"])
INCIDENCE_KEYS = BASE["INCIDENCE_KEYS"]

INSTRUMENT = {"repair_judge_rejection_status", "repair_dump_diagnostics"}
SYSTEM = {"repair_negation_affirmation", "repair_proposal_lineage", "repair_same_meeting_supersession",
          "repair_hedged_same_value", "repair_undefined_key_filing", "repair_meeting_dates",
          "repair_open_proposal_dedup", "repair_settle_before_confirm"}
WRITE = {"filing_type_check", "resolution_same_meeting_conflict", "supersession_requires_new_evidence",
         "filing_support_check"}
EXPECTED_FLAGS = {"A0": INSTRUMENT, "A1": INSTRUMENT | SYSTEM, "A2": INSTRUMENT | SYSTEM | WRITE}
PAIRS = (("A1", "A0"), ("A2", "A0"), ("A2", "A1"), ("RAG", "A0"), ("RAG", "A1"), ("RAG", "A2"))


def load_run(run_dir: Path, arm: str) -> dict:
    pattern = "*.rag.json" if arm == "RAG" else "*.coldstart.json"
    (path,) = glob.glob(str(run_dir / "artifacts" / pattern))
    report = json.loads(Path(path).read_text(encoding="utf-8"))
    if arm == "RAG":
        flags_ok = bool(report["config"].get("repair_judge_rejection_status"))
    else:
        flags = {k for k, v in (report["config"].get("cycle2_flags") or {}).items() if v}
        flags_ok = flags == EXPECTED_FLAGS[arm]
    if report["status"] != "valid" or report["validity"]["status"] != "valid":
        raise SystemExit(f"invalid run, not compared: {run_dir}")
    if not flags_ok:
        raise SystemExit(f"not an {arm} run: {run_dir}")
    return {"dir": str(run_dir), "run_id": report["run_id"], "fallbacks": report.get("fallback_count"),
            "scores": {s["question_id"]: s for s in report["scorecard"]["scores"]}}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    for arm in ("a0", "a1", "a2", "rag"):
        ap.add_argument(f"--{arm}", nargs="+", type=Path, required=True)
    args = ap.parse_args()
    arms = {name.upper(): [load_run(p, name.upper()) for p in getattr(args, name)] for name in ("a0", "a1", "a2", "rag")}
    questions = sorted(arms["A0"][0]["scores"])
    for runs in arms.values():
        for run in runs:
            if sorted(run["scores"]) != questions:
                raise SystemExit(f"question set differs: {run['dir']}")
    family_of = {q: arms["A0"][0]["scores"][q]["family"] for q in questions}
    families = defaultdict(list)
    for q in questions:
        families[family_of[q]].append(q)

    result = {"runs": {a: [{k: r[k] for k in ("dir", "run_id", "fallbacks")} for r in runs] for a, runs in arms.items()},
              "draws": BASE["DRAWS"], "seed": BASE["SEED"], "arms": {}, "pairs": {}}
    for a, runs in arms.items():
        result["arms"][a] = {"overall": arm_rate(runs, questions), "per_run": [arm_rate([r], questions) for r in runs],
                             "families": {f: arm_rate(runs, qs) for f, qs in sorted(families.items())}}
        if a != "RAG":
            result["arms"][a]["state_overall"] = arm_rate(runs, questions, "state")
    for x, y in PAIRS:
        pair = {"overall": {**interval(arms[x], arms[y], questions, "prose"),
                            "ci95_runs_and_questions": interval_runs_and_questions(arms[x], arms[y], questions)},
                "families": {f: interval(arms[x], arms[y], qs, "prose") for f, qs in sorted(families.items())}}
        if "RAG" not in (x, y):
            pair["state_overall"] = interval(arms[x], arms[y], questions, "state")
        result["pairs"][f"{x}-{y}"] = pair

    analyse = runpy.run_path(str(HERE / "23-bug-incidence.py"), run_name="incidence")["analyse"]
    result["incidence"] = {}
    for a in ("A0", "A1", "A2"):
        result["incidence"][a] = []
        for run in arms[a]:
            (state,) = glob.glob(str(Path(run["dir"]) / "artifacts" / "*.state.json"))
            counts = analyse(Path(state))
            result["incidence"][a].append({k: counts[k] for k in INCIDENCE_KEYS})
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")

    pct = lambda x: f"{100 * x:5.1f}%"  # noqa: E731
    print(f"{'':22s} " + " ".join(f"{a:>7s}" for a in arms))
    print(f"{'overall (prose)':22s} " + " ".join(pct(result["arms"][a]["overall"]) for a in arms))
    print(f"{'state overall':22s} " + " ".join(pct(result["arms"][a]["state_overall"]) if a != "RAG" else "     - "
                                               for a in arms))
    for f, qs in sorted(families.items()):
        print(f"{f + f' ({len(qs)})':22s} " + " ".join(pct(result["arms"][a]["families"][f]) for a in arms))
    for a in arms:
        print(f"per run {a}:", [pct(x) for x in result["arms"][a]["per_run"]])
    for name, pair in result["pairs"].items():
        o = pair["overall"]
        lo, hi = o["ci95"]
        rlo, rhi = o["ci95_runs_and_questions"]
        line = (f"{name:8s} {100 * o['difference']:+6.1f}  [{100 * lo:+.1f}, {100 * hi:+.1f}]; "
                f"runs too: [{100 * rlo:+.1f}, {100 * rhi:+.1f}]")
        if "state_overall" in pair:
            s = pair["state_overall"]
            line += f"; state {100 * s['difference']:+.1f} [{100 * s['ci95'][0]:+.1f}, {100 * s['ci95'][1]:+.1f}]"
        print(line)
    for a in ("A0", "A1", "A2"):
        print(f"incidence {a}:", result["incidence"][a])


if __name__ == "__main__":
    main()
