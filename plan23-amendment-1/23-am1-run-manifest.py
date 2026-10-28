"""Plan 23 amendment 1: check the run manifest, and archive the run folders.

The amendment's run manifest gives one SHA-256 per run: over the run's state,
trace, answers and report (coldstart.json), concatenated in that order; for a
RAG run, over its .rag.json file. This script recomputes each hash and compares
it with the manifest table in the amendment.

With --zip PATH it also writes the three batch folders (gitignored) to one zip
archive with sorted entries and fixed timestamps, so the archive's SHA-256 is
reproducible from the same files, and prints that hash.

Usage:
  .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-run-manifest.py
  .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-run-manifest.py --zip data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip
"""

import argparse
import hashlib
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[4]
AMENDMENT = pathlib.Path(__file__).with_name("23-plan-amendment-1-ceilings-and-root-cause.md")
BASE = ROOT / "data/ami_eval/a1_smoke"
BATCHES = ["el2020_batch_20261022T214813Z", "el2020_a1_20261022T211107Z", "el2020_a2_rag_20261023T061545Z"]
RUNS = {
    "a0_r1": "el2020_batch_20261022T214813Z/a0_r1",
    "a0_r2": "el2020_batch_20261022T214813Z/a0_r2",
    "a0_r3": "el2020_batch_20261022T214813Z/a0_r3",
    "A1 smoke run": "el2020_a1_20261022T211107Z",
    "a1_r2": "el2020_batch_20261022T214813Z/a1_r2",
    "a1_r3": "el2020_batch_20261022T214813Z/a1_r3",
    "a2_r1": "el2020_a2_rag_20261023T061545Z/a2_r1",
    "a2_r2b": "el2020_a2_rag_20261023T061545Z/a2_r2b",
    "a2_r3": "el2020_a2_rag_20261023T061545Z/a2_r3",
    "rag_r1": "el2020_a2_rag_20261023T061545Z/rag_r1",
    "rag_r2": "el2020_a2_rag_20261023T061545Z/rag_r2",
    "rag_r3": "el2020_a2_rag_20261023T061545Z/rag_r3",
}


def one(folder, suffix):
    found = sorted((folder / "artifacts").glob(f"*.{suffix}"))
    if len(found) != 1:
        raise SystemExit(f"{folder}: expected one *.{suffix}, found {len(found)}")
    return found[0].read_bytes()


def run_hash(name, rel):
    folder = BASE / rel
    if name.startswith("rag_"):
        return hashlib.sha256(one(folder, "rag.json")).hexdigest()
    parts = [one(folder, s) for s in ("state.json", "trace.json", "answers.json", "coldstart.json")]
    return hashlib.sha256(b"".join(parts)).hexdigest()


def write_zip(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(p for b in BATCHES for p in (BASE / b).rglob("*") if p.is_file())
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            info = zipfile.ZipInfo(str(p.relative_to(BASE)), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes(), compresslevel=9)
    return len(files), hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", type=pathlib.Path)
    args = ap.parse_args()
    table = dict(re.findall(r"^\| (.+?) \| ([0-9a-f]{64}) \|$", AMENDMENT.read_text(), re.M))
    bad = 0
    for name, rel in RUNS.items():
        got = run_hash(name, rel)
        ok = table.get(name) == got
        bad += not ok
        print(f"{name:13} {'ok' if ok else 'MISMATCH'} {got}")
    if bad:
        sys.exit(f"{bad} run(s) do not match the manifest")
    if args.zip:
        n, digest = write_zip(args.zip if args.zip.is_absolute() else ROOT / args.zip)
        print(f"zip {args.zip}: {n} files, sha256 {digest}")


if __name__ == "__main__":
    main()
