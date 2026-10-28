"""Stage 23, re-reading cycle 1: what the reference-informed arm's gold-backed
gate confirmed, replayed offline over its five ES2009 runs.

The gate (``AmiEvalRunner._internal_confirm``, value policy gold_backed) accepts
a pending proposal that passes the value hygiene check when the value's content
words are contained in, or share at least two words with, any gold text
available at the checkpoint: the value of every gold fact (of any status) and
the text of every AMI decision annotation. All five runs used the default
threshold (two words) with the semantic route off (their job commands), so a
lexical replay accounts for every acceptance.

Each accepted value (rejection proposals excluded) is placed at the meeting
where its fact starts (``valid_from`` against the meetings' ingestion times),
and matched with the gate's own rule (``runner._content_words``) against the
gold of every checkpoint from that meeting on. Classes:
  live gold        it matches a gold fact that is current or candidate at some
                   such checkpoint (the benefit of the doubt);
  rejected gold    it matches gold facts, but only ones the gold marks rejected;
  decision text    it matches no gold fact, only decision-annotation text;
  none             no lexical match (would mean the semantic route; none here).

Reads the sealed extension rescore (the runs' checkpoint gold) and the runs'
state dumps; no API calls. Also copies, from 23-bug-incidence.json, the current
fact counts and bug-13 counts of the two ES2009 arms. Writes
23-informed-gate-replay.json next to this script.

Run from the repository root:
    .venv/bin/python thesis/notes/thesis_completion/artifacts/23-informed-gate-replay.py
"""
from __future__ import annotations

import glob
import json
import sys
from collections import Counter
from pathlib import Path
from statistics import mean

ART = Path(__file__).resolve().parent
ROOT = ART.parents[3]
sys.path.insert(0, str(ROOT))

from app.evaluation.ami.rescore import read_sealed  # noqa: E402
from app.evaluation.ami.runner import _GROUND_MIN_SHARED, _content_words  # noqa: E402

RESCORE = ROOT / "data/ami_eval/reduced_rescores/rescore_20260923T102607073385Z"
EXTENSION = ROOT / "data/ami_eval/reduced_extensions/extension_20260922T205257256516Z"
INCIDENCE = ART / "23-bug-incidence.json"
OUT = ART / "23-informed-gate-replay.json"
CLASSES = ("live gold", "rejected gold", "decision text", "none")


def gate_match(words: set[str], gold: set[str]) -> str | None:
    """The gate's rule; which branch matched."""
    if not words:
        return None
    if words <= gold:
        return "contained"
    if len(words & gold) >= _GROUND_MIN_SHARED:
        return "shares two words"
    return None


def replay_run(job_id: str, run: dict) -> dict:
    (state_path,) = glob.glob(str(EXTENSION / f"stages/*/jobs/{job_id}/attempts/attempt-01/artifacts/*.state.json"))
    state = json.loads(Path(state_path).read_text())
    ingested = sorted((a["ingested_at"], a["title"]) for a in state["artifacts"])
    order = [title for _, title in ingested]

    def meeting_of(timestamp: str) -> str | None:
        found = None
        for when, title in ingested:
            if timestamp >= when:
                found = title
        return found

    starts: dict[tuple[str, str], str] = {}
    for fact in state["state_facts"]:
        meeting = meeting_of(fact["valid_from"]) if fact.get("valid_from") else None
        key = (fact["state_key"], str(fact["value"]).lower())
        if meeting and (key not in starts or order.index(meeting) < order.index(starts[key])):
            starts[key] = meeting

    contexts = run["contexts"]
    counts: Counter = Counter()
    paths: Counter = Counter()
    one_word = 0
    examples: dict[str, list] = {c: [] for c in CLASSES}
    for proposal in state["proposals"]:
        reason = str(proposal.get("reason", "")).lower()
        if proposal["status"] != "accepted" or "reject" in reason or "negat" in reason:
            continue
        value = str(proposal["value"])
        words = _content_words(value)
        start = starts.get((proposal["state_key"], value.lower()))
        checkpoints = order[order.index(start):] if start in order else order
        live = rejected = False
        decision_path = None
        for checkpoint in checkpoints:
            context = contexts.get(checkpoint)
            if context is None:
                continue
            for gold in context["gold_facts"]:
                if gate_match(words, _content_words(gold["value"])):
                    if gold["status"] == "rejected":
                        rejected = True
                    else:
                        live = True
            for annotation in context["decision_annotations"]:
                decision_path = decision_path or gate_match(words, _content_words(annotation["text"]))
        cls = ("live gold" if live else "rejected gold" if rejected
               else "decision text" if decision_path else "none")
        counts[cls] += 1
        if cls == "decision text":
            paths[decision_path] += 1
            one_word += len(words) == 1
        if len(examples[cls]) < (20 if cls == "rejected gold" else 6):
            examples[cls].append({"state_key": proposal["state_key"], "value": value})
    last = contexts[order[-1]]["decision_annotations"]
    return {"job_id": job_id, "accepted": sum(counts.values()), "classes": {c: counts[c] for c in CLASSES},
            "decision_text_by_rule": dict(paths), "decision_text_one_content_word": one_word,
            "decision_annotations_at_last_checkpoint": len(last),
            "decision_annotation_mean_chars": round(mean(len(a["text"]) for a in last)) if last else 0,
            "examples": examples}


def main() -> None:
    payload = read_sealed(RESCORE / "inputs.json")
    runs = {r["job_id"]: r for r in payload["runs"] if r["job_id"].startswith("pm_informed_privileged")}
    results = [replay_run(job, runs[job]) for job in sorted(runs)]
    totals = {c: sum(r["classes"][c] for r in results) for c in CLASSES}
    incidence = json.loads(INCIDENCE.read_text())["groups"]
    arms = {"autonomous": incidence["ES2009 autonomous (r1-r5)"],
            "reference-informed": incidence["ES2009 reference-informed (r1-r5)"]}
    context = {arm: {"current_facts": group["totals"]["current_facts"],
                     "bug13_runs_with_inverted_validity": sum(1 for r in group["runs"]
                                                              if r["bug13_validity_ends_before_it_starts"]),
                     "runs": len(group["runs"])}
               for arm, group in arms.items()}
    result = {"min_shared": _GROUND_MIN_SHARED, "runs": results, "totals": totals,
              "accepted": sum(totals.values()), "arms_from_incidence": context}
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")

    n = result["accepted"]
    print(f"accepted values (rejection proposals excluded), five runs: {n}")
    for c in CLASSES:
        print(f"  {totals[c]:4d} ({100 * totals[c] / n:4.1f}%)  {c}")
    by_rule = Counter()
    for r in results:
        by_rule.update(r["decision_text_by_rule"])
    print("  decision-text matches by rule:", dict(by_rule), "| one content word:",
          sum(r["decision_text_one_content_word"] for r in results))
    print("  decision annotations at the last checkpoint:", results[0]["decision_annotations_at_last_checkpoint"],
          "| mean length:", results[0]["decision_annotation_mean_chars"], "chars")
    print("  rejected-gold examples:", sorted({e["value"] for r in results for e in r["examples"]["rejected gold"]}))
    for arm, c in context.items():
        print(f"  {arm}: {c['current_facts']} current facts over {c['runs']} runs; "
              f"bug 13 (validity ends before it starts) in {c['bug13_runs_with_inverted_validity']} runs")


if __name__ == "__main__":
    main()
