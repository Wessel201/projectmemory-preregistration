"""Stage 23, re-reading cycle 1: accuracy on the questions where an answer has
to be right, kept apart from the two families that cannot separate the systems.

Reads saved reports only (no repository code, no API calls) and writes
23-answerable-only.json next to this script.

Run from the repository root:
    python3 -I thesis/notes/thesis_completion/artifacts/23-answerable-only.py

Families (app/evaluation/ami/scorer.py):
  noise_resistance  the ES2009 items forbid nothing, so every answer is right
                    (22-bug-list.md, section C);
  unknown           the gold expects an abstention, so abstaining is right;
  answerable        every other family: the answer must carry the gold values.

Sources, all read with the bug-7 repaired rejection items (23-bug7-rescore.md):
  ES2009  the sealed GPT-5.4 rescores of the reduced study and its extension:
          autonomous r1-r5, RAG pilot r1-r5, reference-informed r1-r5;
  EL2020  the transfer study's reports, judged live by the same pinned judge:
          autonomous r1-r3, RAG r1-r3.

Bug-2 estimate: the autonomous runs' evidence items scored as they would be with
corrected lineage (23-bug2-answer-estimate.json, ``corrected_ok``), every other
item as recorded. An estimate only: bugs 1 and 3-6 are still present in these
runs, and bug 3 had already replaced some values.
"""
from __future__ import annotations

import glob
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path.cwd()
OUT = Path(__file__).with_suffix(".json")
ES_RESCORES = ("data/ami_eval/reduced_rescores/rescore_20260921T093315613712Z",
               "data/ami_eval/reduced_rescores/rescore_20260923T102607073385Z")
EL_TRANSFER = "data/ami_eval/transfer_studies/transfer_20260923T230223026681Z"
BUG7 = "data/ami_eval/rejection_rescores/bug7_20261022T194724Z"
BUG2 = Path(__file__).with_name("23-bug2-answer-estimate.json")
ES_GROUPS = {"pm_autonomous": "autonomous", "rag_pilot": "RAG", "pm_informed_privileged": "reference-informed"}
EL_GROUPS = {"el_pm_autonomous": "autonomous", "el_rag": "RAG"}
SET_APART = ("noise_resistance", "unknown")


def bug7(job_id: str) -> dict[str, bool]:
    path = ROOT / BUG7 / "reports" / f"{job_id}.json"
    return {r["question_id"]: r["repaired"]["correct"] for r in json.loads(path.read_text())["items"]}


def stem(path: str) -> str:
    return Path(path).name.split(".")[0]


def es_runs():
    for rescore in ES_RESCORES:
        for path in sorted(glob.glob(str(ROOT / rescore / "reports" / "*.json"))):
            job = Path(path).stem
            group = job.rsplit("_r", 1)[0]
            if group in ES_GROUPS:
                report = json.loads(Path(path).read_text())
                yield ES_GROUPS[group], job, report["scorecard"]["scores"], stem(report["source_report"])


def el_runs():
    for path in sorted(glob.glob(str(ROOT / EL_TRANSFER / "stages/*/jobs/*/attempts/attempt-01/artifacts/*.json"))):
        if not path.endswith((".coldstart.json", ".rag.json")):
            continue
        job = path.split("/jobs/")[1].split("/")[0]
        yield EL_GROUPS[job.rsplit("_r", 1)[0]], job, json.loads(Path(path).read_text())["scorecard"]["scores"], stem(path)


def bug2_corrections() -> dict[str, dict[str, bool]]:
    """Run stem -> {evidence question id: correct with corrected lineage}."""
    estimate = json.loads(BUG2.read_text())
    return {stem(run["run"]): {e["question_id"]: e["corrected_ok"] for e in run["evidence"]}
            for group in estimate.values() for run in group["runs"]}


def read(scores: list[dict], replace: dict[str, bool]) -> dict:
    by_family = defaultdict(list)
    for s in scores:
        by_family[s["family"]].append((replace.get(s["question_id"], s["correct"]), s["abstained"]))
    answerable = [c for f, rows in by_family.items() if f not in SET_APART for c, _ in rows]
    return {
        "n_questions": len(scores),
        "overall": mean(1.0 if replace.get(s["question_id"], s["correct"]) else 0.0 for s in scores),
        "answerable": mean(1.0 if c else 0.0 for c in answerable),
        "n_answerable": len(answerable),
        "families": {f: {"n": len(rows), "right": mean(1.0 if c else 0.0 for c, _ in rows),
                         "abstained": mean(1.0 if a else 0.0 for _, a in rows)}
                     for f, rows in sorted(by_family.items())},
    }


def summarise(runs) -> dict:
    lineage = bug2_corrections()
    arms: dict[str, list] = defaultdict(list)
    for arm, job, scores, run_stem in runs:
        repaired = bug7(job)
        entry = {"job_id": job, **read(scores, repaired)}
        if arm == "autonomous" and run_stem in lineage:
            entry["answerable_bug2_corrected"] = read(scores, {**repaired, **lineage[run_stem]})["answerable"]
        arms[arm].append(entry)
    out = {}
    for arm, runs_ in arms.items():
        families = sorted({f for r in runs_ for f in r["families"]})
        out[arm] = {
            "repeats": len(runs_),
            "overall": mean(r["overall"] for r in runs_),
            "answerable": mean(r["answerable"] for r in runs_),
            "n_answerable": runs_[0]["n_answerable"],
            "n_questions": runs_[0]["n_questions"],
            "families": {f: {"n": runs_[0]["families"][f]["n"],
                             "right": mean(r["families"][f]["right"] for r in runs_),
                             "abstained": mean(r["families"][f]["abstained"] for r in runs_)}
                         for f in families},
            "runs": runs_,
        }
        corrected = [r["answerable_bug2_corrected"] for r in runs_ if "answerable_bug2_corrected" in r]
        if corrected:
            out[arm]["answerable_bug2_corrected"] = mean(corrected)
    return out


def main() -> None:
    result = {"ES2009": summarise(es_runs()), "EL2020": summarise(el_runs())}
    es = result["ES2009"]
    unknown = es["autonomous"]["families"]["unknown"]
    rag_unknown = es["RAG"]["families"]["unknown"]
    result["ES2009_unknown_items_worth_points"] = 100 * (unknown["right"] - rag_unknown["right"]) * unknown["n"] / \
        es["autonomous"]["n_questions"]
    result["ES2009_overall_lead_points"] = 100 * (es["autonomous"]["overall"] - es["RAG"]["overall"])
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")

    for series in ("ES2009", "EL2020"):
        print(f"== {series}")
        for arm, a in result[series].items():
            extra = (f"; bug-2 corrected {100 * a['answerable_bug2_corrected']:.1f}%"
                     if "answerable_bug2_corrected" in a else "")
            print(f"  {arm:20s} overall {100 * a['overall']:5.1f}% | answerable {100 * a['answerable']:5.1f}% "
                  f"(n={a['n_answerable']}, {a['repeats']} repeats{extra})")
            print("      " + ", ".join(f"{f} {100 * v['right']:.0f}% right / {100 * v['abstained']:.0f}% abstained"
                                       for f, v in a["families"].items()))
    print(f"ES2009: unknown items worth {result['ES2009_unknown_items_worth_points']:.1f} points of autonomous over "
          f"RAG; the whole overall lead is {result['ES2009_overall_lead_points']:.1f} points")


if __name__ == "__main__":
    main()
