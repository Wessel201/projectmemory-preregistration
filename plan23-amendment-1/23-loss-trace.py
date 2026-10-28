"""Loss trace (plan 23, B2 and D3): for each gold value at each checkpoint of a
run, the step where it is lost (extraction, filing, state maintenance or
reading), or that it gets through. It replaces the cycle-1 lexical failure coder
(bug 11: 20-failure-analysis.py, 20-failure-funnel.py). The codebook, with the
sub-codes and the verification record, is 23-loss-trace.md.

Unit: one gold row (a gold value at checkpoint k, from the suite's ``gold:``
block) in one run. Every row is traced, not only failures, so each step is
counted two-sided (reached / passed). Questions are a derived view.

The chain, in order; the first step that fails is the row's loss:
  extraction   admitted     the value's cited span went to the extractor
                            (extract_to_state, extract_as_candidate or
                            evidence_only), or a claim from another span
                            carries the value
               carried      a claim extracted by checkpoint k carries the value
               polarity     ... with the polarity the value needs (negative for
                            an explicitly ruled-out value)
               modality     ... asserted (any modality for a candidate value)
  filing       filed        such a claim's last logged evaluation by k filed it
                            under a key (not parked, not refused)
               proposed     a proposal carrying the value was raised by k
               applied      a fact carrying the value was created by k
  state        current      that fact is current at k (rejected at k for a
                            ruled-out value)
               status       ... with the expected status at k
  reading      key_reached  a key the reader resolved holds such a fact
               in_payload   the reader was given that fact as an answer fact
               answered     the question is scored correct
Reading is traced through single-value questions only (one gold row asked),
each question on its own; the row takes the question that got furthest. A
value the gold marks superseded at a later checkpoint ("demoted") passes when
it is not current at k.

Checkpoint state is rebuilt from the trace (transaction time). A step's phase
is the number of checkpoints already questioned. Accepted proposals are
replayed in creation order against the dumped facts, as the projection applies
them, which gives each fact the phase it was created in and each demotion the
phase it happened in. Status at k is the status a fact was created with (a
status change creates a new fact).

Matcher (when a text carries the gold value): see _match, phrases and Judge.
The matcher proposes; adjudication decides. Every text that decides a pass, and
every text the lenient bound counts that changes a row's outcome, goes to the
adjudication queue until it has a decision (--adjudications). The primary
series is the strict bound once the queue is empty.

Run from the repository root (it imports the system's transcript rendering):
    .venv/bin/python thesis/notes/thesis_completion/artifacts/23-loss-trace.py \\
        --suite data/ami_eval/suites/transfer_el2020.yaml RUN_DIR [RUN_DIR ...]
Each RUN_DIR holds artifacts/*.coldstart.json, *.state.json, *.answers.json and
*.trace.json. Writes 23-loss-trace.json next to this script (or --out).
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from functools import cache
from pathlib import Path
from statistics import mean

import yaml

sys.path.insert(0, str(Path.cwd()))
from app.evaluation.ami.synthetic_suite import parse_transcript_lines
from app.evaluation.ami.transcript_builder import (
    TRANSCRIPT_FILE_HEADER_LINES,
    build_transcript_text,
    segment_line_numbers,
)
from app.services.segmentation_service import SegmentationService

HERE = Path(__file__)
EXTRACTED_POLICIES = {"extract_to_state", "extract_as_candidate", "evidence_only"}
SYSTEM_REPAIRS = {"repair_negation_affirmation", "repair_proposal_lineage", "repair_same_meeting_supersession",
                  "repair_hedged_same_value", "repair_undefined_key_filing", "repair_meeting_dates",
                  "repair_open_proposal_dedup", "repair_settle_before_confirm"}
WRITE_CONTRACTS = {"filing_type_check", "resolution_same_meeting_conflict", "supersession_requires_new_evidence",
                   "filing_support_check"}
INSTRUMENT_REPAIRS = {"repair_judge_rejection_status", "repair_dump_diagnostics"}
SINGLE_VALUE_FAMILIES = {"current_state", "candidate_decided", "rejection"}
BOUNDARY = {
    "admitted": "extraction", "carried": "extraction", "polarity": "extraction", "modality": "extraction",
    "filed": "filing", "proposed": "filing", "applied": "filing",
    "current": "state_maintenance", "status": "state_maintenance",
    "key_reached": "reading", "in_payload": "reading", "answered": "reading",
}
CHAIN = list(BOUNDARY)
# Why a filed carrier raised no proposal for the value, when its last logged
# evaluation raised none: the evaluation's reason.
NO_PROPOSAL_REASONS = (
    ("Tied authority and time", "tie_left_as_conflict"),
    ("Design cycle 2: rival", "same_meeting_conflict"),
    ("New evidence agrees with current value", "judged_same_as_current"),
    ("Value already in collection", "judged_same_as_current"),
    ("Low-authority dissent", "outranked_dissent"),
    ("Negation below the member's authority", "outranked_dissent"),
    ("Hedged negation of a collection member", "hedged_negation"),
    ("No positive claims", "no_positive_claim_left"),
    ("Stage-23 repair (bug 3)", "current_value_ranks_higher"),
    ("Stage-23 repair (bug 4)", "hedged_same_value"),
)

# ------------------------------------------------------------------ matcher

STOP = {"a", "an", "the", "of", "to", "in", "on", "for", "and", "or", "is", "are", "be", "by", "with", "at", "as",
        "it", "that", "this", "from", "into", "per", "its", "their", "which", "will", "was", "were", "has", "have",
        "can", "also", "so", "we", "they", "them", "our", "there", "then", "than", "about", "up", "i", "me", "my",
        "you", "your", "us", "he", "she", "him", "her", "his"}
NEGATORS = {"not", "no", "never", "avoid", "without", "none", "nothing", "nobody", "neither", "nor"}
UNITS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
         "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
ORDINALS = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8,
            "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
            "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19,
            "twentieth": 20, "thirtieth": 30}
MONTHS = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"}
IRREGULAR = {"used": "use", "using": "use", "uses": "use", "based": "base", "basis": "base", "bases": "base"}
COMPOUND = re.compile(rf"\b({'|'.join(TENS)})[\s-]+({'|'.join(w for w, n in UNITS.items() if 0 < n < 10)})\b")
# anonymisation placeholders ("PERSON3", "[ORGANIZATION6]") are one digit-free word
PLACEHOLDER = re.compile(r"\[?\b(person|organization|organisation|project|location|annotator)\d+\]?")


def _stem(w: str) -> str:
    """A light suffix strip, applied alike to every word of both texts
    ("files" = "file", "segmenting" = "segment", "dropped" = "drop")."""
    if w in IRREGULAR:
        return IRREGULAR[w]
    if w.isdigit() or len(w) <= 3:
        return w
    if w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    stripped = False
    if len(w) > 5 and w.endswith("ing"):
        w, stripped = w[:-3], True
    elif len(w) > 4 and w.endswith("ed"):
        w, stripped = w[:-2], True
    if stripped and len(w) > 3 and w[-1] == w[-2] and w[-1] not in "lsz":
        w = w[:-1]  # "dropp" -> "drop"
    return w[:-1] if len(w) > 4 and w.endswith("e") else w


@cache
def _tokens(text: str) -> tuple[tuple[str, str], ...]:
    """(word, normalised token) pairs: lower case, accents and punctuation
    removed, numbers kept. Number words and compound numbers ("forty-two")
    become digits; an ordinal becomes a digit only next to a month name
    ("twentieth of April"). A placeholder is one word, a possessive "'s" is
    dropped, a hyphen joins a one-letter part ("e-mail" = "email")."""
    text = unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode().lower()
    text = PLACEHOLDER.sub(lambda m: f" {m.group(1)}x ", text)
    text = re.sub(r"['’]s\b", "", text)
    text = COMPOUND.sub(lambda m: str(TENS[m.group(1)] + UNITS[m.group(2)]), text)
    text = re.sub(r"\b([a-z])-(?=[a-z])", r"\1", text)
    text = re.sub(r"(?<=[a-z])-([a-z])\b", r"\1", text)
    text = re.sub(r"\b(re|pre)-(?=[a-z])", "", text)  # "re-listening" = "listening"
    raw = re.findall(r"[a-z]+|\d+(?:[.,]\d+)?", text.replace("-", " "))
    out: list[tuple[str, str]] = []
    for i, w in enumerate(raw):
        if w in TENS:
            out.append((w, str(TENS[w])))
        elif w in UNITS:
            out.append((w, str(UNITS[w])))
        elif w in ORDINALS and MONTHS & set(raw[max(0, i - 2): i + 3]):
            out.append((w, str(ORDINALS[w])))
        elif w in ("st", "nd", "rd", "th") and out and out[-1][1].isdigit():
            continue  # "20th" was split into "20", "th"
        else:
            out.append((w, _stem(w)))
    return tuple(out)


def tokens(text: str) -> list[str]:
    return [t for _, t in _tokens(str(text or ""))]


@cache
def _content(text: str) -> tuple[str, ...]:
    return tuple(t for w, t in _tokens(text) if w not in STOP)


def content(text: str) -> list[str]:
    return list(_content(str(text or "")))


def _required_numbers(value: str) -> set[str]:
    """Numbers the text must contain: every number in the value except the
    determiner "one" ("one shared paper")."""
    return {t for w, t in _tokens(value) if t[0].isdigit() and w != "one"}


def _contains(hay, needle) -> bool:
    """Every needle token occurs in hay (order free, as a multiset)."""
    counts = Counter(hay)
    return all(counts[t] >= n for t, n in Counter(needle).items())


def _near(hay, needle) -> bool:
    """The needle's tokens occur together: within a window of its length plus
    two tokens (an alias must be a phrase of the text, not scattered words)."""
    width = len(needle) + 2
    return any(_contains(hay[i: i + width], needle) for i in range(max(1, len(hay) - width + 1)))


def _coverage(hay, needle) -> float:
    return len(set(needle) & set(hay)) / len(set(needle))


def _distinctive(alias: str) -> bool:
    """A one-word alias that names something (a proper noun, number or date:
    "Antrecorp", "23rd"), not a common word ("working", "paper")."""
    words = [w for w in re.findall(r"[A-Za-z0-9]+", alias) if w.lower() not in STOP]
    return len(words) == 1 and (words[0][0].isupper() or any(ch.isdigit() for ch in words[0]))


@cache
def _match(candidate: str, value: str, aliases: tuple[str, ...]) -> tuple[str | None, str | None]:
    """(level, why). STRONG: a gold alias of two or more content words occurs
    as a phrase of the text; or the text contains every content word of the
    value (a one-word value only if the text has at most two content words),
    or three quarters of a value of four or more content words. WEAK: a
    one-word alias, the one-word value inside a longer text, or half the
    value's content words. A number in the value must occur in the text,
    unless an alias matches."""
    cand = _content(candidate)
    if not cand:
        return None, None
    one_word = [a for a in aliases if len(_content(a)) == 1 and _content(a)[0] in cand]
    for alias in aliases:
        a = _content(alias)
        if len(a) >= 2 and _near(cand, a):
            return "strong", "alias"
    whole = _content(value)
    if not whole or not _required_numbers(value) <= set(cand):
        return ("weak", "one_word_alias") if one_word else (None, None)
    if _contains(cand, whole) and (len(set(whole)) >= 2 or len(cand) <= 2):
        return "strong", "value"
    if len(set(whole)) >= 4 and _coverage(cand, whole) >= 0.75:
        return "strong", "coverage"
    if _contains(cand, whole):
        return "weak", "one_word_value"
    if one_word:
        return "weak", "one_word_alias"
    if _coverage(cand, whole) >= 0.5:
        return "weak", "half"
    return None, None


def match_level(candidate: str, value: str, aliases) -> str | None:
    """'strong', 'weak' or None: does the text carry the gold value?"""
    return _match(str(candidate or ""), str(value or ""), tuple(aliases or ()))[0]


def phrases(text: str, row: dict) -> list[frozenset]:
    """The parts of the row's value the text contains: each value or alias it
    contains, and the covered words of the value when it covers half of them."""
    cand = _content(str(text or ""))
    out = []
    for phrase in [row["value"], *row["aliases"]]:
        p = _content(phrase)
        if p and (_near(cand, p) if len(p) >= 2 and phrase != row["value"] else _contains(cand, p)):
            out.append(frozenset(p))
    whole = _content(row["value"])
    if whole and _coverage(cand, whole) >= 0.5:
        out.append(frozenset(set(whole) & set(cand)))
    return out


def _norm(value) -> str:
    return " ".join(str(value or "").lower().split()).strip(" .")


# ----------------------------------------------------------------- gold side

def render_spans(suite: dict) -> dict:
    """The system's own transcript rendering and segmentation, so a gold line
    maps to the span the gatekeeper and the extractor saw."""
    out = {}
    for meeting in suite["meetings"]:
        segs = parse_transcript_lines(meeting, suite["transcripts"][meeting])
        text = build_transcript_text(segs)
        spans = SegmentationService().segment(text)
        rendered = {int(k.rsplit(".", 1)[1]): v - 1 - TRANSCRIPT_FILE_HEADER_LINES
                    for k, v in segment_line_numbers(segs).items()}
        r2span = {r: i for i, sp in enumerate(spans) for r in range(sp.start_index, sp.end_index + 1)}
        out[meeting] = {"spans": [sp.text for sp in spans],
                        "line2span": {line: r2span[r] for line, r in rendered.items() if r in r2span}}
    return out


def gold_rows(suite: dict) -> list[dict]:
    rows = []
    for k, meeting in enumerate(suite["meetings"]):
        for g in suite["gold"][meeting]:
            if g["status"] == "rejected":
                kind = "ruled_out" if str(g["fact_id"]).startswith("R") else "demoted"
            else:
                kind = "candidate" if g["status"] == "candidate" else "current"
            rows.append({"k": k, "meeting": meeting, "fact_id": g["fact_id"], "value": g["value"],
                         "aliases": list(g.get("aliases") or []), "status": g["status"], "kind": kind,
                         "state_key": g.get("state_key"), "evidence": list(g.get("evidence") or [])})
    return rows


def question_map(suite: dict, rows: list[dict]) -> dict:
    """question id -> checkpoint, family and the gold rows it asks for: by
    exact value, or by the id suffix for evidence questions (whose expected
    answer is a meeting)."""
    meetings = suite["meetings"]
    by_value = defaultdict(dict)
    for r in rows:
        by_value[r["k"]][r["value"]] = r["fact_id"]
    out = {}
    for q in suite["questions"]:
        k = meetings.index(q["after_meeting"])
        expected = q.get("expected") or {}
        fids = [by_value[k][v] for v in expected.get("must_include", []) if v in by_value[k]]
        suffix = re.search(r"_([FR]\d+)$", q["id"])
        if not fids and suffix and q["family"] == "evidence":
            fids = [suffix.group(1)]
        out[q["id"]] = {"k": k, "family": q["family"], "fact_ids": fids,
                        "expected_meetings": expected.get("must_include", []) if q["family"] == "evidence" else []}
    return out


def alias_collisions(rows: list[dict]) -> list[dict]:
    """Gold lint: pairs of values at one checkpoint where a value or alias of
    either strongly matches the other. The matcher's sibling rule separates
    them; the list says where it has to."""
    out = set()
    by_k = defaultdict(list)
    for r in rows:
        by_k[r["k"]].append(r)
    for rs in by_k.values():
        for a in rs:
            for b in rs:
                if a["fact_id"] != b["fact_id"] and any(
                        match_level(p, b["value"], b["aliases"]) == "strong" for p in [a["value"], *a["aliases"]]):
                    out.add(tuple(sorted((a["fact_id"], b["fact_id"]))))
    return [{"a": a, "b": b} for a, b in sorted(out)]


# ------------------------------------------------------------------ run side

def _one(pattern: str) -> Path:
    found = glob.glob(pattern)
    if len(found) != 1:
        raise SystemExit(f"expected one file for {pattern}, found {len(found)}")
    return Path(found[0])


def _norm_ws(text: str) -> str:
    return " ".join(str(text).split())


def _value(claim: dict) -> str:
    obj = claim.get("object") or {}
    return str(obj.get("value") or obj.get("role") or "")


def _spo(claim: dict) -> str:
    return f"{claim.get('subject') or ''} {claim.get('predicate') or ''} {_value(claim)}".strip()


class Run:
    """One run's trace and dump, joined: spans, claims, evaluations, proposals
    and facts, each with the phase (checkpoints already questioned) it
    happened in."""

    def __init__(self, run_dir: Path, suite: dict, spans: dict, questions: dict):
        art = run_dir / "artifacts"
        self.dir = str(run_dir)
        self.report = json.loads(_one(str(art / "*.coldstart.json")).read_text())
        self.state = json.loads(_one(str(art / "*.state.json")).read_text())
        self.answers = {a["question_id"]: a["answer"]
                        for a in json.loads(_one(str(art / "*.answers.json")).read_text())["answers"]}
        steps = json.loads(_one(str(art / "*.trace.json")).read_text())["steps"]
        flags = {k for k, v in (self.report["config"].get("cycle2_flags") or {}).items() if v}
        repaired = SYSTEM_REPAIRS <= flags
        if flags - SYSTEM_REPAIRS - WRITE_CONTRACTS - INSTRUMENT_REPAIRS:
            self.arm = "mixed"  # a read or extraction contract is on
        elif WRITE_CONTRACTS & flags:
            self.arm = "A2" if repaired and WRITE_CONTRACTS <= flags else "mixed"
        else:
            self.arm = "A1" if repaired else "A0" if not SYSTEM_REPAIRS & flags else "mixed"
        self.scores = {s["question_id"]: s for s in self.report["scorecard"]["scores"]}
        self.defined = {d["state_key"] for d in self.state["state_key_definitions"]}
        self.join_counts = Counter()

        asked: set[int] = set()
        for st in steps:
            if st["seam"] == "ami_eval_question":
                st["_phase"] = questions[st["input"]["question_id"]]["k"]
                asked.add(st["_phase"])
            else:
                st["_phase"] = len(asked)
        if asked != set(range(len(suite["meetings"]))):
            raise SystemExit(f"{run_dir}: a checkpoint without questions breaks the phase count")

        text2span: dict[str, tuple] = {}
        for m in spans:
            for i, txt in enumerate(spans[m]["spans"]):
                if txt in text2span:
                    raise SystemExit(f"two spans with the same text: {text2span[txt]} and {(m, i)}")
                text2span[txt] = (m, i)
        self.gate: dict[tuple, str] = {}
        for st in steps:
            if st["seam"] == "memory_gatekeeper" and st["mode"] == "llm":
                txt = st["input"]["messages"][-1]["content"].split("Classify this span:\n\n", 1)[1]
                self.gate[text2span[txt]] = st["output"].get("extraction_policy")

        # evidence -> span: normalised prefix match within the meeting, unique
        self.ev_span: dict[str, tuple] = {}
        for e in self.state["evidence"]:
            head = _norm_ws(e["text"].rstrip("…"))
            hits = [(e["meeting_id"], i) for i, txt in enumerate(spans[e["meeting_id"]]["spans"])
                    if _norm_ws(txt).startswith(head)]
            if len(hits) == 1:
                self.ev_span[e["evidence_id"]] = hits[0]
            else:
                self.join_counts["evidence_without_unique_span"] += 1
        self.ev_meeting = {e["evidence_id"]: e["meeting_id"] for e in self.state["evidence"]}

        # claim -> phase of the extraction call that produced it (a span whose
        # extraction returned nothing is extracted again at the next meeting)
        produced = defaultdict(list)
        for st in steps:
            if st["seam"] == "extraction" and st["mode"] == "llm":
                txt = st["input"]["messages"][-1]["content"].split("Extract project-state claims from:\n\n", 1)[1]
                span = text2span.get(txt)
                for c in st["output"].get("claims") or []:
                    produced[(span, c.get("subject"), c.get("predicate"), c.get("object_value"),
                              c.get("polarity"), c.get("modality"))].append(st["_phase"])
        self.claims = self.state["claims"]
        self.trail = defaultdict(list)
        for st in steps:
            if st["seam"] == "conflict_detection":
                inp, outp = st["input"], st["output"]
                self.trail[inp.get("claim_id")].append({
                    "phase": st["_phase"], "state_key": inp.get("state_key"), "result": outp.get("result_type"),
                    "proposal_id": outp.get("proposal_id"), "reason": outp.get("reason") or ""})
        self.claim_phase: dict[str, int] = {}
        for c in self.claims:
            key = (self.ev_span.get(c["evidence_id"]), c["subject"], c["predicate"], (c.get("object") or {}).get("value"),
                   c["polarity"], c["modality"])
            if produced.get(key):
                self.claim_phase[c["claim_id"]] = min(produced[key])
            else:
                # not joined to its extraction call: no earlier than its first evaluation
                self.join_counts["claims_without_extraction_call"] += 1
                rows = self.trail.get(c["claim_id"])
                self.claim_phase[c["claim_id"]] = rows[0]["phase"] if rows else 0

        # design-cycle-2 parking (A2): dated by the support-check step whose
        # reason the claim records (and whose message holds the claim's value),
        # or by the type-check step that parked it
        support_rows = defaultdict(list)
        type_phase = {}
        for st in steps:
            out = st.get("output") or {}
            if st["seam"] == "claim_support_check" and out.get("supported") is False:
                support_rows[out.get("reason")].append((st["_phase"], st["input"]["messages"][-1]["content"]))
            if st["seam"] == "filing_type_check" and out.get("parked"):
                type_phase.setdefault(st["input"].get("claim_id"), st["_phase"])
        self.parked: dict[str, tuple[str, int]] = {}
        for c in self.claims:
            rec = (c.get("object") or {}).get("cycle2") or {}
            if not rec.get("parked"):
                continue
            if rec["parked"] == "no_fitting_key":
                phase = type_phase.get(c["claim_id"])
            else:
                rows = support_rows.get((rec.get("support") or {}).get("reason"), [])
                if len(rows) > 1:
                    rows = [r for r in rows if _value(c) in r[1]] or rows
                phase = rows[0][0] if rows else None
            if phase is None:
                self.join_counts["parked_claims_not_dated"] += 1
                phase = self.claim_phase[c["claim_id"]]
            self.parked[c["claim_id"]] = (rec["parked"], phase)

        # proposals with the phase they were raised in and their value
        self.proposals: dict[str, dict] = {}
        claim_value = {c["claim_id"]: (c.get("object") or {}).get("value") for c in self.claims}
        prev = None
        for st in steps:
            if st["seam"] == "resolution":
                prev = st
                continue
            if st["seam"] != "conflict_detection":
                continue
            inp, outp = st["input"], st["output"]
            if inp.get("cardinality") == "collection":
                # collection keys log a rejected membership as 'new' and propose
                # the canonical value: the joins below do not cover them
                self.join_counts["collection_key_evaluations"] += 1
            pid = outp.get("proposal_id")
            if pid and pid not in self.proposals:
                key = inp.get("state_key")
                if inp.get("cardinality") == "collection":
                    value = claim_value.get(inp.get("claim_id"))
                else:
                    value = (prev["output"].get("winning_value")
                             if prev and prev["input"].get("state_key") == key else None)
                if value is None:
                    self.join_counts["proposals_without_value"] += 1
                self.proposals[pid] = {"phase": st["_phase"], "state_key": key, "value": value,
                                       "type": outp.get("result_type"), "reason": outp.get("reason") or ""}
        dumped = self.state["proposals"]
        if len(dumped) == len(self.proposals) and all(
                (d["state_key"], d["value"]) == (p["state_key"], p["value"]) for d, p in zip(dumped, self.proposals.values())):
            for pid, d in zip(self.proposals, dumped):
                # the dumped reason is the final one (the lineage repair refreshes
                # an open proposal's reason before acceptance)
                self.proposals[pid].update(status=d["status"], reason=d.get("reason") or self.proposals[pid]["reason"])
        else:
            self.join_counts["proposal_status_not_joined"] += 1

        self.facts = {f["fact_id"]: f for f in self.state["state_facts"]}
        self.created: dict[str, int | None] = {}
        self.created_by: dict[str, str] = {}
        self.order: dict[str, int] = {}  # creation order (the dump lists facts in it)
        self.demoted_at: dict[str, int] = {}
        self.placement = "replay" if self._replay() else "heuristic"
        if self.placement == "heuristic":
            self._place_by_order()
        self.join_counts["facts_not_placed_in_time"] = sum(1 for v in self.created.values() if v is None)
        self.order = {f["fact_id"]: i for i, f in enumerate(self.state["state_facts"])}

    def _replay(self) -> bool:
        """Accepted proposals in creation order against the dumped facts (in
        creation order), as the projection applies them: a rejection of a
        current value demotes it; every other accepted proposal creates the
        next fact, and a positive one supersedes the key's current fact."""
        if any("status" not in p for p in self.proposals.values()):
            return False
        facts = self.state["state_facts"]
        current: dict[str, str] = {}
        fi = 0
        for pid, p in self.proposals.items():
            if p["status"] != "accepted":
                continue
            if p["type"] == "reject":
                cur = current.get(p["state_key"])
                if cur and str(self.facts[cur]["value"]).strip().lower() == str(p["value"]).strip().lower():
                    self.demoted_at[cur] = p["phase"]
                    del current[p["state_key"]]
                    continue
            if fi >= len(facts) or (facts[fi]["state_key"], facts[fi]["value"]) != (p["state_key"], p["value"]):
                self.created.clear(), self.created_by.clear(), self.demoted_at.clear()
                return False
            f = facts[fi]
            fi += 1
            self.created[f["fact_id"]], self.created_by[f["fact_id"]] = p["phase"], pid
            if p["type"] != "reject":
                current[p["state_key"]] = f["fact_id"]
        if fi != len(facts):
            self.created.clear(), self.created_by.clear(), self.demoted_at.clear()
            return False
        return True

    def _place_by_order(self) -> None:
        """Fallback when the replay does not align: facts matched to proposals
        by key, value and type, in valid_from order."""
        by_kvt = defaultdict(list)
        for pid, p in self.proposals.items():
            by_kvt[(p["state_key"], p["value"], p["type"])].append((p["phase"], pid))
        for lst in by_kvt.values():
            lst.sort()
        predecessor = {f["superseded_by"]: f["fact_id"] for f in self.facts.values() if f.get("superseded_by")}
        used = Counter()
        for f in sorted(self.facts.values(), key=lambda f: str(f.get("valid_from") or "")):
            types = (["reject"] if self.ruled_out_record(f["fact_id"]) else ["supersede", "new"]
                     if f["fact_id"] in predecessor else ["new", "supersede"])
            self.created[f["fact_id"]] = None
            for t in types:
                lst = by_kvt.get((f["state_key"], f["value"], t))
                if lst and used[(f["state_key"], f["value"], t)] < len(lst):
                    self.created[f["fact_id"]], self.created_by[f["fact_id"]] = lst[used[(f["state_key"], f["value"], t)]]
                    used[(f["state_key"], f["value"], t)] += 1
                    break
        for f in self.facts.values():
            if f["status"] == "rejected" and f.get("valid_to") is not None:
                phases = [p["phase"] for p in self.proposals.values() if p["type"] == "reject"
                          and p["state_key"] == f["state_key"] and _norm(p["value"]) == _norm(f["value"])]
                if phases:
                    self.demoted_at[f["fact_id"]] = min(phases)

    def ruled_out_record(self, fid: str) -> bool:
        """A REJECTED fact recorded next to the current value (never current)."""
        f = self.facts[fid]
        return f["status"] == "rejected" and f.get("valid_to") is None

    def created_by_k(self, fid: str | None, k: int) -> bool:
        return fid is not None and self.created.get(fid) is not None and self.created[fid] <= k

    def current(self, fid: str, k: int) -> bool:
        if not self.created_by_k(fid, k) or self.ruled_out_record(fid):
            return False
        if self.created_by_k(self.facts[fid].get("superseded_by"), k):
            return False
        return not (fid in self.demoted_at and self.demoted_at[fid] <= k)

    def rejected_at(self, fid: str, k: int) -> bool:
        if not self.created_by_k(fid, k):
            return False
        if self.ruled_out_record(fid):
            return True
        return fid in self.demoted_at and self.demoted_at[fid] <= k

    def status_at(self, fid: str, k: int) -> str:
        """The fact's status at checkpoint k. A fact keeps the status it was
        created with while it is current (a status change creates a new fact);
        the dump only shows the status at the end of the run."""
        if self.rejected_at(fid, k):
            return "rejected"
        if not self.current(fid, k):
            return "superseded" if self.created_by_k(fid, k) else "absent"
        end = self.facts[fid]["status"]
        if end in ("current_confirmed", "current_unconfirmed"):
            return end
        reason = self.proposals.get(self.created_by.get(fid), {}).get("reason", "")
        return "current_unconfirmed" if "Only hedged" in reason else "current_confirmed"


# --------------------------------------------------------------- the trace

def defect_flags(run: Run, fids: list[str], k: int) -> list[str]:
    """The incidence events (23-bug-incidence.py definitions) on the facts
    that carry the row's value, as far as they happened by k. Bug 2 skips
    ruled-out records, which cite their negation span by design."""
    flags = set()
    carriers = defaultdict(set)
    for c in run.claims:
        if c["polarity"] == "positive":
            carriers[(c["state_key"], _norm(_value(c)))].add(c["evidence_id"])
    for fid in fids:
        f = run.facts[fid]
        nxt = run.facts.get(f.get("superseded_by") or "")
        ended = (nxt is not None and run.created_by_k(nxt["fact_id"], k)) or (
            fid in run.demoted_at and run.demoted_at[fid] <= k)
        if f["state_key"] not in run.defined:
            flags.add("bug5_undefined_key")
        if nxt and run.created_by_k(nxt["fact_id"], k):
            if _norm(nxt["value"]) == _norm(f["value"]):
                flags.add("bug4_superseded_by_same_value")
            elif nxt.get("valid_from") == f.get("valid_from"):
                flags.add("bug3_replaced_in_own_meeting")
        if ended and f.get("valid_to") and f.get("valid_from") and f["valid_to"] < f["valid_from"]:
            flags.add("bug13_validity_inverted")
        if not run.ruled_out_record(fid) and not (
                set(f.get("supporting_evidence") or []) & carriers.get((f["state_key"], _norm(f["value"])), set())):
            flags.add("bug2_cites_span_without_value")
    return sorted(flags)


def local_texts(run: Run, row: dict, spans: dict) -> tuple[set, set, list]:
    """The row's cited spans, its window (the cited spans and the spans next
    to them), and the claims extracted from the window."""
    prov = set()
    for ref in row["evidence"]:
        m, line = ref.split(":")
        sp = spans[m]["line2span"].get(int(line))
        if sp is not None:
            prov.add((m, sp))
    window = {(m, i + d) for m, i in prov for d in (-1, 0, 1)}
    claims = [c for c in run.claims if run.ev_span.get(c["evidence_id"]) in window]
    return prov, window, claims


class Judge:
    """Does a text carry one gold row's value, under one bound? Adjudications
    decide first; the matcher only proposes. Records the texts the lenient
    bound counts and the strict one does not (pending)."""

    def __init__(self, row: dict, ctx: dict, adj: dict, local: set[str], lenient: bool, local_of=None):
        self.row, self.ctx, self.local, self.lenient = row, ctx, local, lenient
        self.adj, self.adj_all = adj.get(row["fact_id"], {}), adj
        evidence = set(row["evidence"])
        # a value and the alternative it ruled out, cited from the same line,
        # are two sides of one decision, not rivals for a text
        self.others = [r for r in ctx["rows_by_k"][row["k"]] if r["fact_id"] != row["fact_id"] and not (
            evidence & set(r["evidence"]) and "ruled_out" in (row["kind"], r["kind"]))]
        self.local_of = local_of or (lambda r: set())
        self.pending: set[str] = set()

    def level(self, text: str) -> str | None:
        """strong / weak / None after the sibling rule. A text does not carry
        this row when every part of the value it contains is part of a longer
        value or alias of another gold row of the checkpoint that it also
        contains. A part shared equally with another row stays with this row
        when the text is local to this row and not to the other; otherwise
        the match is weak. A one-word value, or a distinctive one-word alias
        (a name, number or date), in a local text that no other row shares
        counts as strong."""
        lv, why = _match(str(text or ""), str(self.row["value"]), tuple(self.row["aliases"]))
        if lv is None:
            return None
        mine = phrases(text, self.row)
        theirs = []
        for r in self.others:
            if self.adj_all.get(r["fact_id"], {}).get(text) is False:
                continue  # adjudicated: the text does not carry that row
            for q in phrases(text, r):
                theirs.append((q, text in self.local and text not in self.local_of(r)))
        free = [p for p in mine if not any(p < q or (p == q and not ours) for q, ours in theirs)]
        shared = [p for p in mine if any(p == q for q, _ in theirs) and not any(p < q for q, _ in theirs)]
        if mine and not free:
            return "weak" if shared else None
        if lv == "weak" and text in self.local and free:
            one = {frozenset(_content(a)) for a in self.row["aliases"] if _distinctive(a)}
            if (why == "one_word_value" and frozenset(_content(self.row["value"])) in free) or (
                    why == "one_word_alias" and one & set(free)):
                return "strong"
        return lv

    def verdict(self, text: str, local: bool | None = None) -> tuple[bool, bool]:
        """(counts in the strict bound, counts in the lenient bound)."""
        if text in self.adj:
            return bool(self.adj[text]), bool(self.adj[text])
        lv = self.level(text)
        local = (text in self.local) if local is None else local
        if lv == "strong" and local:
            return True, True
        if lv == "strong" or (lv == "weak" and local):
            return False, True
        return False, False

    def counts(self, text: str, local: bool | None = None) -> bool:
        strict, lenient = self.verdict(text, local)
        if lenient and not strict:
            self.pending.add(text)
        return lenient if self.lenient else strict


def trace_row(run: Run, row: dict, spans: dict, ctx: dict, lenient: bool, adj: dict) -> dict:
    k, kind, fid = row["k"], row["kind"], row["fact_id"]
    prov, window, local_claims = ctx["local"][(run.dir, fid, k)]
    local = {_value(c) for c in local_claims} | {_spo(c) for c in local_claims}
    judge = Judge(row, ctx, adj, local, lenient,
                  local_of=lambda r: ctx["local_text"][(run.dir, r["fact_id"], r["k"])])

    out = {"run": run.dir, "arm": run.arm, "k": k, "meeting": row["meeting"], "fact_id": fid, "kind": kind,
           "value": row["value"], "steps": {}, "loss": None, "sub": None, "flags": [], "pending": judge.pending,
           "support": {}, "wording_pairs": [], "questions": [], "ok_facts": [],
           "cited_spans": sorted(f"{m}#{i}" for m, i in prov)}
    steps, support = out["steps"], out["support"]

    def fail(step: str, sub: str) -> dict:
        out["loss"], out["sub"] = step, sub
        return out

    def claim_text(c: dict) -> str | None:
        """The text by which the claim carries the value, or None. A decision
        on either of the claim's texts decides the claim."""
        texts = [_value(c)] + ([_spo(c)] if run.ev_span.get(c["evidence_id"]) in window else [])
        decided = [judge.adj[t] for t in texts if t in judge.adj]
        if decided:
            return next((t for t in texts if judge.adj.get(t)), None)
        if judge.counts(texts[0]):
            return texts[0]
        if len(texts) > 1 and judge.counts(texts[1], local=True):
            return texts[1]
        return None

    by_k = [c for c in run.claims if run.claim_phase[c["claim_id"]] <= k]
    text_of = {c["claim_id"]: claim_text(c) for c in by_k}
    carriers = [c for c in by_k if text_of[c["claim_id"]]]
    want = "negative" if kind == "ruled_out" else "positive"
    right = [c for c in carriers if c["polarity"] == want and (kind == "candidate" or c["modality"] == "asserted")]
    # a proposal or fact holding a carrier claim's value under a key the claim
    # was evaluated under (by k) carries the value too. A claim that carries it
    # only through its subject passes it on only when the key's words and the
    # value together still match the gold value.
    carried_kv: dict[tuple, str] = {}
    for c in right:
        t = text_of[c["claim_id"]]
        for r in run.trail.get(c["claim_id"], []):
            if r["phase"] > k or not r["state_key"]:
                continue
            keyed = f"{r['state_key']} {_value(c)}".replace(".", " ").replace("_", " ")
            if t == _value(c) or judge.level(keyed) is not None:
                carried_kv.setdefault((r["state_key"], _norm(_value(c))), t)

    def holds(key, value) -> str | None:
        """The text by which a proposal or fact carries the value, or None."""
        if value in judge.adj:
            return value if judge.adj[value] else None
        t = carried_kv.get((key, _norm(value)))
        if t:
            return t
        return value if judge.counts(value) else None

    held_text = {f: holds(x["state_key"], x["value"]) for f, x in run.facts.items() if run.created_by_k(f, k)}
    holding = [f for f, t in held_text.items() if t]
    out["flags"] = defect_flags(run, holding, k)

    if kind == "demoted":
        held = [f for f in holding if not run.ruled_out_record(f)]
        still = [f for f in held if run.current(f, k)]
        steps["was_stored"] = bool(held)
        steps["no_longer_current"] = not still
        if still:
            support["still_current"] = sorted({held_text[f] for f in still})
            return fail("current", "still_current")
        out["sub"] = "demoted" if held else "never_stored"
        return out

    # extraction
    policies = {run.gate.get(p) for p in prov}
    out["cited_span_policies"] = sorted(str(p) for p in policies)
    out["carrier_source"] = ("cited_span" if any(run.ev_span.get(c["evidence_id"]) in window for c in carriers)
                             else "other_span" if carriers else None)
    steps["admitted"] = bool(policies & EXTRACTED_POLICIES) or bool(carriers)
    if not steps["admitted"]:
        return fail("admitted", "ignored" if policies - {None} else "span_not_seen")
    steps["carried"] = bool(carriers)
    if not carriers:
        if any(claim_text(c) for c in local_claims if run.claim_phase[c["claim_id"]] > k):
            return fail("carried", "extracted_after_checkpoint")
        # claims with an adjudicated text are decided: they neither stand for
        # a sibling's claim nor join a split
        local_by_k = [c for c in local_claims if run.claim_phase[c["claim_id"]] <= k
                      and not {_value(c), _spo(c)} & set(judge.adj)]
        if any(match_level(t, row["value"], row["aliases"]) == "strong"
               for c in local_by_k for t in (_value(c), _spo(c))):
            return fail("carried", "sibling_value_only")
        by_subject = defaultdict(list)
        for c in local_by_k:
            by_subject[_norm(c.get("subject"))].append(c)
        for cs in by_subject.values():
            joined = f"{cs[0].get('subject') or ''} " + " ".join(_value(c) for c in cs)
            if len(cs) > 1 and judge.level(joined) == "strong":
                return fail("carried", "split_across_claims")
        from_cited = [c for c in by_k if run.ev_span.get(c["evidence_id"]) in prov]
        return fail("carried", "no_claims_from_cited_span" if not from_cited else "claims_without_the_value")
    support["carried"] = sorted({text_of[c["claim_id"]] for c in carriers})
    right_pol = [c for c in carriers if c["polarity"] == want]
    steps["polarity"] = bool(right_pol)
    if not right_pol:
        words = {w for p in [row["value"], *row["aliases"]] for w, _ in _tokens(p)}
        if kind != "ruled_out" and NEGATORS & words:
            return fail("polarity", "negated_value_read_as_rejection")
        return fail("polarity", f"carried_only_{'positive' if want == 'negative' else 'negative'}")
    steps["modality"] = bool(right)
    if not right:
        return fail("modality", "carried_only_" + "_".join(sorted({c["modality"] for c in right_pol})))

    # filing
    def filing(c: dict) -> str:
        parked = run.parked.get(c["claim_id"])
        if parked and parked[1] <= k:
            return "cycle2_parked_" + parked[0]
        rows = [r for r in run.trail.get(c["claim_id"], []) if r["phase"] <= k]
        if not rows:
            return "not_evaluated" if c.get("state_key") else "no_key"
        last = rows[-1]
        if not last["state_key"]:
            return "no_key"
        if last["reason"].startswith("Stage-23 repair (bug 5)"):
            return "undefined_key"
        return "filed"

    codes = {c["claim_id"]: filing(c) for c in right}
    filed = [c for c in right if codes[c["claim_id"]] == "filed"]
    steps["filed"] = bool(filed)
    if not filed:
        return fail("filed", Counter(codes.values()).most_common(1)[0][0])
    wanted_type = {"reject"} if kind == "ruled_out" else {"new", "supersede"}
    props = {}
    for pid, p in run.proposals.items():
        if p["phase"] <= k and p["type"] in wanted_type and p["value"]:
            t = holds(p["state_key"], p["value"])
            if t:
                props[pid] = t
    steps["proposed"] = bool(props)
    if not props:
        found = Counter()
        for c in filed:
            r = [r for r in run.trail[c["claim_id"]] if r["phase"] <= k][-1]
            if r["proposal_id"] and r["result"] in ("new", "supersede", "reject"):
                winner = run.proposals.get(r["proposal_id"], {}).get("value")
                if winner and _norm(winner) == _norm(_value(c)):
                    # the claim's own value won, but its stored words alone do
                    # not match: the adjudicator decides whether they carry it
                    code = "own_value_not_matched"
                    out["wording_pairs"].append(winner)
                else:
                    code = "another_value_won"
                    if winner and match_level(winner, row["value"], row["aliases"]):
                        out["wording_pairs"].append(winner)
            else:
                code = next((c for prefix, c in NO_PROPOSAL_REASONS if r["reason"].startswith(prefix)), r["result"])
                if code == "judged_same_as_current":
                    out["wording_pairs"] += sorted({f["value"] for f in run.facts.values() if f["state_key"] == r["state_key"]
                                                    and run.created_by_k(f["fact_id"], k)})
            found[code] += 1
        return fail("proposed", found.most_common(1)[0][0])
    support["proposed"] = sorted(set(props.values()))
    made = [f for f in holding if (run.facts[f]["status"] == "rejected" if kind == "ruled_out"
                                   else not run.ruled_out_record(f))]
    steps["applied"] = bool(made)
    if not made:
        statuses = Counter(run.proposals[pid].get("status", "unknown") for pid in props)
        if statuses.get("expired") or statuses.get("pending_review"):
            return fail("applied", "proposal_" + ("expired" if statuses.get("expired") else "pending_review"))
        return fail("applied", "fact_not_found")
    support["applied"] = sorted({held_text[f] for f in made})

    # state maintenance
    live = [f for f in made if (run.rejected_at(f, k) if kind == "ruled_out" else run.current(f, k))]
    steps["current"] = bool(live)
    if not live:
        if kind == "ruled_out":
            return fail("current", "rejection_after_checkpoint")
        f = max(made, key=lambda x: (run.created[x], run.order[x]))
        if f in run.demoted_at and run.demoted_at[f] <= k:
            return fail("current", "rejected")
        chain, nxt = [], run.facts.get(run.facts[f].get("superseded_by") or "")
        while nxt is not None and run.created_by_k(nxt["fact_id"], k):
            chain.append(nxt["value"])
            nxt = run.facts.get(nxt.get("superseded_by") or "")
        out["successor_values"] = chain
        if not chain:
            return fail("current", "not_current")  # cannot occur under the replay

        def gold_of(value: str) -> str | None:
            for g in ctx["rows_by_k"][k]:
                if g["fact_id"] != fid and g["kind"] in ("current", "candidate"):
                    other = adj.get(g["fact_id"], {})
                    if other.get(value) or (value not in other and Judge(
                            g, ctx, adj, ctx["local_text"][(run.dir, g["fact_id"], k)], False,
                            local_of=lambda r: ctx["local_text"][(run.dir, r["fact_id"], r["k"])]).level(value) == "strong"):
                        return g["fact_id"]
            return None
        later = [g for g in (gold_of(v) for v in chain[1:]) if g]
        if later:
            out["later_gold_in_chain"] = later[0]
        displaced = gold_of(chain[0])
        if displaced:
            out["displaced_by"] = displaced
            return fail("current", "displaced_by_other_gold_value")
        return fail("current", "overwritten_by_non_gold_value")
    expected = {"current": "current_confirmed", "candidate": "current_unconfirmed", "ruled_out": "rejected"}[kind]
    ok = [f for f in live if run.status_at(f, k) == expected]
    steps["status"] = bool(ok)
    out["stored_facts"] = live
    if not ok:
        return fail("status", "stored_as_" + run.status_at(live[0], k))
    support["status"] = sorted({held_text[f] for f in ok})
    out["ok_facts"] = ok

    # reading: single-value questions, each on its own
    asked = ctx["single"].get((fid, k), [])
    out["questions"] = asked
    if not asked:
        out["sub"] = "stored_not_asked"
        return out
    best = None
    for q in asked:
        ans = run.answers.get(q) or {}
        resolved = set(ans.get("state_keys") or [])
        given = {f["fact_id"] for f in ans.get("facts") or []}
        near = {f["fact_id"] for f in ans.get("near_matches") or []}
        reached = any(run.facts[f]["state_key"] in resolved for f in ok)
        stage = (3 if reached and given & set(ok) and run.scores.get(q, {}).get("correct")
                 else 2 if reached and given & set(ok) else 1 if reached else 0)
        cand = (stage, q, bool(resolved), bool(near & set(ok)))
        best = cand if best is None or cand[0] > best[0] else best
    stage, q, any_key, near = best
    out["reading_question"] = q
    steps["key_reached"] = stage >= 1
    if stage == 0:
        return fail("key_reached", "other_keys_resolved" if any_key else "no_key_resolved")
    steps["in_payload"] = stage >= 2
    if stage == 1:
        return fail("in_payload", "near_match_only" if near else "key_resolved_fact_not_given")
    steps["answered"] = stage == 3
    if stage == 2:
        return fail("answered", "answer_or_judge")
    return out


def credit_without_state(rec: dict, run: Run, ctx: dict) -> bool:
    """A single-value question asking for the row is scored correct, although
    no stored fact with the value and the right status was among its answer
    facts."""
    ok = set(rec.get("ok_facts") or [])
    for q in ctx["single"].get((rec["fact_id"], rec["k"]), []):
        given = {f["fact_id"] for f in (run.answers.get(q) or {}).get("facts") or []}
        if run.scores.get(q, {}).get("correct") and not given & ok:
            return True
    return False


def question_view(run: Run, ctx: dict, traces: dict) -> list[dict]:
    """Per question: the outcome of each gold row it asks for. Evidence
    questions also say whether a stored fact cites the meeting the gold names.
    Unknown and noise questions carry no gold value: the record says whether
    the reader was given facts and whether the answer was credited."""
    out = []
    for q, v in ctx["qmap"].items():
        ans = run.answers.get(q) or {}
        rec = {"question_id": q, "family": v["family"], "k": v["k"],
               "correct": bool(run.scores.get(q, {}).get("correct")),
               "rows": [{"fact_id": f, "loss": traces[(f, v["k"])]["loss"], "sub": traces[(f, v["k"])]["sub"]}
                        for f in v["fact_ids"] if (f, v["k"]) in traces]}
        if v["family"] == "evidence" and rec["rows"]:
            stored = traces[(v["fact_ids"][0], v["k"])].get("stored_facts", [])
            cited = sorted({run.ev_meeting[e] for f in stored for e in run.facts[f].get("supporting_evidence") or []
                            if e in run.ev_meeting})
            rec.update(stored=bool(stored), cited_meetings=cited,
                       cites_expected_meeting=bool(set(cited) & set(v["expected_meetings"])))
        if not v["fact_ids"]:
            rec.update(keys_resolved=len(ans.get("state_keys") or []), facts_given=len(ans.get("facts") or []))
        out.append(rec)
    return out


def summarise(records: list[dict]) -> dict:
    """Two-sided: for each step, the rows that reached it and the rows that
    passed it, per kind of gold row."""
    by_kind = defaultdict(list)
    for r in records:
        by_kind[r["kind"]].append(r)
    out = {}
    for kind, rows in sorted(by_kind.items()):
        reached, passed = Counter(), Counter()
        for r in rows:
            for step, ok in r["steps"].items():
                reached[step] += 1
                passed[step] += bool(ok)
        out[kind] = {
            "rows": len(rows),
            "first_loss_by_boundary": dict(Counter(r["boundary"] or "none" for r in rows)),
            "outcomes": dict(Counter(f"{r['loss'] or 'ok'}:{r['sub']}" for r in rows)),
            "funnel": {s: {"reached": reached[s], "passed": passed[s]}
                       for s in CHAIN + ["was_stored", "no_longer_current"] if reached[s]},
            "carried_only_from_another_span": sum(1 for r in rows if r.get("carrier_source") == "other_span"),
            "defect_flagged": sum(1 for r in rows if r["flags"]),
            "credit_without_state": sum(1 for r in rows if r["credit_without_state"]),
        }
    return out


def arm_summary(runs: list[dict], bound: str) -> dict:
    """Per arm, the mean per run of each boundary count and outcome, per kind."""
    by_arm = defaultdict(list)
    for e in runs:
        by_arm[e["arm"]].append(e[bound]["summary"])
    out = {}
    for arm, sums in sorted(by_arm.items()):
        out[arm] = {"runs": len(sums)}
        for kind in sums[0]:
            fields = {}
            for field in ("first_loss_by_boundary", "outcomes"):
                keys = sorted({x for s in sums for x in s[kind][field]})
                fields[field] = {x: round(mean(s[kind][field].get(x, 0) for s in sums), 2) for x in keys}
            fields["credit_without_state"] = round(mean(s[kind]["credit_without_state"] for s in sums), 2)
            out[arm][kind] = fields
    return out


def _neutral(reason: str) -> str:
    """An evaluation reason without the arm-revealing prefixes."""
    code = next((c for prefix, c in NO_PROPOSAL_REASONS if reason.startswith(prefix)), None)
    if code:
        return code.replace("_", " ")
    return re.sub(r"^(Stage-23 repair \(bug \d+\)|Design cycle 2): ", "", reason)


def case_page(run: Run, row: dict, spans: dict, ctx: dict, case_id: str) -> str:
    """A blind case page for the second coder (V4): the raw material for one
    gold row, without the arm or the trace's verdict (cycle-2 parking and
    same-meeting conflicts can still reveal the A2 arm). The coder assigns the
    first failing step from the codebook (23-loss-trace.md). Phases and
    checkpoints are both counted from 0."""
    k, fid, value, aliases = row["k"], row["fact_id"], row["value"], row["aliases"]
    meetings = sorted(spans)
    prov, window, local_claims = ctx["local"][(run.dir, fid, k)]
    lines = [f"# Case {case_id}", "",
             (f"Gold value ({row['kind']}, expected status {row['status']}), checkpoint {k} "
              f"(after {meetings[k]}; phase k = writes up to that checkpoint): **{value}**"),
             f"Aliases: {aliases}", "", "## Cited span(s)"]
    for m, i in sorted(prov):
        lines += [f"- {m}#{i}, gatekeeper policy `{run.gate.get((m, i))}`:", "", "```", spans[m]["spans"][i], "```"]

    def claim_line(c: dict) -> list[str]:
        sp = run.ev_span.get(c["evidence_id"])
        out = [(f"- `{c['claim_id'][-8:]}` from {sp[0]}#{sp[1]} " if sp else f"- `{c['claim_id'][-8:]}` ")
               + (f"(extracted in phase {run.claim_phase[c['claim_id']]}): {c.get('subject')} | {c.get('predicate')}"
                  f" | \"{_value(c)}\", polarity {c['polarity']}, modality {c['modality']}")]
        parked = run.parked.get(c["claim_id"])
        if parked and parked[1] <= k:
            out.append(f"    - parked in phase {parked[1]}: "
                       + ("the span does not support it" if parked[0] == "unsupported_by_span" else "no fitting key"))
        shown = set()
        for r in run.trail.get(c["claim_id"], []):
            if r["phase"] <= k and (r["phase"], r["state_key"], r["result"], r["proposal_id"], r["reason"]) not in shown:
                shown.add((r["phase"], r["state_key"], r["result"], r["proposal_id"], r["reason"]))
                pv = run.proposals.get(r["proposal_id"], {}).get("value") if r["proposal_id"] else None
                out.append(f"    - phase {r['phase']}: key `{r['state_key']}` -> {r['result']}"
                           + (f" (proposal value \"{pv}\")" if pv else "") + f"; {_neutral(r['reason'])[:110]}")
        return out

    by_k = [c for c in run.claims if run.claim_phase[c["claim_id"]] <= k]
    lines += ["", "## Claims by this checkpoint from the cited span(s) and the spans next to them"]
    for c in by_k:
        if run.ev_span.get(c["evidence_id"]) in window:
            lines += claim_line(c)
    later = [c for c in local_claims if run.claim_phase[c["claim_id"]] > k]
    if later:
        lines += ["", "## Claims from those spans extracted only after this checkpoint"]
        for c in later:
            lines += claim_line(c)[:1]
    lines += ["", "## Claims by this checkpoint from other spans that share words with the value"]
    for c in by_k:
        if run.ev_span.get(c["evidence_id"]) not in window and (match_level(_value(c), value, aliases)
                                                                 or match_level(_spo(c), value, aliases)):
            lines += claim_line(c)
    keys = {r["state_key"] for c in by_k if run.ev_span.get(c["evidence_id"]) in window
            or match_level(_value(c), value, aliases) for r in run.trail.get(c["claim_id"], [])
            if r["phase"] <= k and r["state_key"]}
    lines += ["", "## Facts under those keys, or sharing words with the value, at this checkpoint"]
    for f in run.facts.values():
        if (f["state_key"] in keys or match_level(f["value"], value, aliases)) and run.created_by_k(f["fact_id"], k):
            nxt = run.facts.get(f.get("superseded_by") or "")
            lines.append(f"- `{f['fact_id'][-8:]}` key `{f['state_key']}`: \"{f['value']}\", created phase "
                         f"{run.created[f['fact_id']]}, status at this checkpoint {run.status_at(f['fact_id'], k)}"
                         + (f"; replaced by \"{nxt['value']}\" in phase {run.created.get(nxt['fact_id'])}"
                            if nxt and run.created_by_k(nxt["fact_id"], k) else ""))
    asked = ctx["single"].get((fid, k), [])
    lines += ["", "## Single-value questions asking for this value at this checkpoint"]
    for q in asked:
        ans = run.answers.get(q) or {}
        given = [f"`{f['state_key']}`: \"{f['value']}\" ({f['status']})" for f in ans.get("facts") or []]
        near = [f"`{f['state_key']}`: \"{f['value']}\"" for f in ans.get("near_matches") or []]
        lines += [f"- {q}: \"{ans.get('question', '')}\"", f"    - keys resolved: {ans.get('state_keys')}",
                  f"    - answer facts: {given[:12]}" + (f" (+{len(given) - 12} more)" if len(given) > 12 else ""),
                  f"    - near matches (disclosed, not asserted): {near[:8]}",
                  f"    - answer: \"{str(ans.get('answer', ''))[:400]}\"",
                  f"    - scored correct: {bool(run.scores.get(q, {}).get('correct'))}"]
    if not asked:
        lines.append("- none (no reading step)")
    lines += ["", "## Coder's verdict", "", "First failing step (or `passes`): ", "Sub-code: ", "Note: ", ""]
    return "\n".join(lines)


def pack_check(run: Run, qmap: dict) -> dict:
    """The rebuilt state against what the reader was given: per question and
    resolved key, the facts current at k against the non-rejected facts the
    reader got on that key; and the status at k of every fact the reader got
    (answer facts and near matches) against the status it was given with."""
    by_key = defaultdict(list)
    for f in run.facts.values():
        by_key[f["state_key"]].append(f["fact_id"])
    out = Counter()
    for q, ans in run.answers.items():
        k = qmap[q]["k"]
        given = (ans.get("facts") or []) + (ans.get("near_matches") or [])
        for f in given:
            out["statuses"] += 1
            out["statuses_matching"] += run.status_at(f["fact_id"], k) == f["status"]
        ids = {f["fact_id"] for f in given if f["status"] != "rejected"}
        for key in set(ans.get("state_keys") or []):
            out["question_keys"] += 1
            out["question_keys_matching"] += ({f for f in by_key[key] if run.current(f, k)}
                                              == {f for f in ids if run.facts[f]["state_key"] == key})
    return dict(out)


def load_adjudications(path: Path | None) -> tuple[dict, str | None]:
    """YAML {adjudicator: human|model, decisions: {fact_id: {text: bool}}}; a
    bare {fact_id: {text: bool}} mapping is read with adjudicator unknown."""
    if not path:
        return {}, None
    doc = yaml.safe_load(path.read_text()) or {}
    if "decisions" in doc:
        return doc["decisions"] or {}, str(doc.get("adjudicator") or "unknown")
    return doc, "unknown"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--suite", required=True, type=Path)
    ap.add_argument("--adjudications", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=HERE.with_suffix(".json"))
    ap.add_argument("--case-pages", type=Path, default=None,
                    help="write blind case pages for the second coder to this directory")
    ap.add_argument("--sample", type=int, default=0, help="case pages per run (deterministic sample)")
    ap.add_argument("runs", nargs="+", type=Path)
    args = ap.parse_args()
    suite = yaml.safe_load(args.suite.read_text())
    adj, adjudicator = load_adjudications(args.adjudications)
    spans = render_spans(suite)
    rows = gold_rows(suite)
    qmap = question_map(suite, rows)
    ctx = {"qmap": qmap, "rows_by_k": defaultdict(list), "single": defaultdict(list), "local": {}, "local_text": {}}
    for r in rows:
        ctx["rows_by_k"][r["k"]].append(r)
    for q, v in qmap.items():
        if v["family"] in SINGLE_VALUE_FAMILIES and len(v["fact_ids"]) == 1:
            ctx["single"][(v["fact_ids"][0], v["k"])].append(q)

    result = {"suite": str(args.suite), "suite_sha256": hashlib.sha256(args.suite.read_bytes()).hexdigest(),
              "adjudications": str(args.adjudications) if args.adjudications else None,
              "adjudicator": adjudicator,
              "adjudications_sha256": (hashlib.sha256(args.adjudications.read_bytes()).hexdigest()
                                       if args.adjudications else None),
              "decisions": sum(len(v) for v in adj.values()),
              "script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(),
              "gold_rows": len(rows), "questions": len(qmap), "gold_alias_collisions": alias_collisions(rows),
              "runs": []}
    for run_dir in args.runs:
        run = Run(run_dir, suite, spans, qmap)
        for r in rows:
            prov, window, claims = local_texts(run, r, spans)
            ctx["local"][(run.dir, r["fact_id"], r["k"])] = (prov, window, claims)
            ctx["local_text"][(run.dir, r["fact_id"], r["k"])] = ({_value(c) for c in claims}
                                                                   | {_spo(c) for c in claims})
        entry = {"dir": str(run_dir), "arm": run.arm, "run_id": run.report["run_id"], "placement": run.placement,
                 "joins": dict(run.join_counts), "pack_check": pack_check(run, qmap)}
        for bound, lenient in (("strict", False), ("lenient", True)):
            traces = {}
            for r in rows:
                rec = trace_row(run, r, spans, ctx, lenient, adj)
                rec["boundary"] = BOUNDARY[rec["loss"]] if rec["loss"] else None
                rec["credit_without_state"] = credit_without_state(rec, run, ctx)
                traces[(r["fact_id"], r["k"])] = rec
            records = list(traces.values())
            entry[bound] = {"summary": summarise(records), "records": records,
                            "questions": question_view(run, ctx, traces)}
        # the queue: every text that decides a pass of the strict bound, and
        # every text the lenient bound counts that changes a row's outcome,
        # until it has a decision; the wording pairs of either bound
        strict = {(r["fact_id"], r["k"]): r for r in entry["strict"]["records"]}
        queue = set()
        for r in entry["strict"]["records"]:
            for texts in r["support"].values():
                if not any(adj.get(r["fact_id"], {}).get(t) for t in texts):
                    queue |= {(r["fact_id"], t, "decides") for t in texts}
        for r in entry["lenient"]["records"]:
            lo = strict[(r["fact_id"], r["k"])]
            if (lo["loss"], lo["sub"]) != (r["loss"], r["sub"]):
                queue |= {(r["fact_id"], w, "lenient") for w in r["pending"]}
        for r in entry["strict"]["records"] + entry["lenient"]["records"]:
            queue |= {(r["fact_id"], w, "wording") for w in r["wording_pairs"]}
        open_items = {}
        for f, t, why in sorted(queue):
            if t not in adj.get(f, {}):
                open_items.setdefault((f, t), why)
        entry["adjudication_queue"] = [{"fact_id": f, "text": t, "why": w} for (f, t), w in sorted(open_items.items())]
        if args.case_pages and args.sample:
            # deterministic sample: rows ordered by a hash of run, value and checkpoint
            def case_id(r: dict, run_id: str = run.report["run_id"]) -> str:
                return hashlib.sha256(f"{run_id}|{r['fact_id']}|{r['k']}".encode()).hexdigest()[:10]
            args.case_pages.mkdir(parents=True, exist_ok=True)
            entry["case_pages"] = {}
            for r in sorted(rows, key=case_id)[: args.sample]:
                cid = case_id(r)
                (args.case_pages / f"{cid}.md").write_text(case_page(run, r, spans, ctx, cid), encoding="utf-8")
                entry["case_pages"][cid] = {"fact_id": r["fact_id"], "k": r["k"]}
        result["runs"].append(entry)
    result["arms"] = {bound: arm_summary(result["runs"], bound) for bound in ("strict", "lenient")}
    result["queue_open"] = sum(len(e["adjudication_queue"]) for e in result["runs"])
    result["pack_check"] = dict(sum((Counter(e["pack_check"]) for e in result["runs"]), Counter()))
    result["primary_series_complete"] = result["queue_open"] == 0
    args.out.write_text(json.dumps(result, indent=1, default=sorted), encoding="utf-8")

    for entry in result["runs"]:
        print(f"== {entry['arm']} {Path(entry['dir']).name}  placement {entry['placement']}; joins {entry['joins']}; "
              f"open queue: {len(entry['adjudication_queue'])}")
        for bound in ("strict", "lenient"):
            s = entry[bound]["summary"]
            line = "; ".join(f"{kind} {v['rows']}: " + ", ".join(f"{b} {n}" for b, n in sorted(
                v["first_loss_by_boundary"].items())) for kind, v in s.items())
            print(f"   {bound}: {line}")
    print(f"open queue items: {result['queue_open']}; primary series complete: {result['primary_series_complete']}; "
          f"pack check: {result['pack_check']}")


if __name__ == "__main__":
    main()
