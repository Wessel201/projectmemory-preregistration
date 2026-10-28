# ProjectMemory: pre-registration record

This repository is the public, timestamped record of the decision rules for a master's thesis evaluation of ProjectMemory, a system that keeps a project's decisions across meetings. Each signed amendment is one folder and one annotated tag. The tag is made before any output that the amendment's rules govern exists.

| Tag | Folder | Signed |
|---|---|---|
| `plan23-amendment-1` | [`plan23-amendment-1/`](plan23-amendment-1/) | 28 October 2026 |

## plan23-amendment-1

Plan 23, amendment 1 fixes the ceilings and the root-cause coding rules of the second design cycle before its Step 2, 2b and 2c outputs exist. Start with these files:

- [`23-plan-amendment-1-ceilings-and-root-cause.md`](plan23-amendment-1/23-plan-amendment-1-ceilings-and-root-cause.md): the amendment itself. Other files cite it by line number.
- [`23-am1-step0-index.md`](plan23-amendment-1/23-am1-step0-index.md): the index of the Step 0 package.
- [`23-plan-amendment-1-signing-record.md`](plan23-amendment-1/23-plan-amendment-1-signing-record.md): the commit message, the tag annotation and every file hash.
- [`23-am1-decisions.md`](plan23-amendment-1/23-am1-decisions.md): every open decision and how it was answered.

The folder also holds plan 23 and the bug list at their cited states, the frozen inputs (the loss trace, its adjudications and results, and the EL2020 arm, answerable-only and informed-gate records) and the workflow records (`23-am1-records/`).

## Verifying

Every file is byte-identical to the file that was checked before signing. To compare them with the recorded hashes:

```bash
shasum -a 256 -c SHA256SUMS
```

The scripts here were written for the source repository, which stays private. They read its git history and its run data, which this repository doesn't include. They are kept unchanged so that their signed hashes still match. They are part of the record, not tools to run from here. Paths of the form `thesis/notes/thesis_completion/artifacts/` in the files refer to the source repository. Inside this repository, the same files are in `plan23-amendment-1/`.

## Data and licence

Some files quote short excerpts of meeting transcripts and minutes from two corpora:

- **ELITR Minuting Corpus** (English): Nedoluzhko, A., Singh, M., Hledíková, M., Ghosal, T. and Bojar, O. (2022). *ELITR Minuting Corpus: A Novel Dataset for Automatic Minuting from Multi-Party Meetings in English and Czech.* LREC 2022. http://hdl.handle.net/11234/1-4692. Licensed CC BY-NC-SA 4.0.
- **AMI Meeting Corpus**: Carletta, J. et al. (2005). *The AMI Meeting Corpus: A Pre-announcement.* MLMI 2005. https://groups.inf.ed.ac.uk/ami/corpus/. Licensed CC BY 4.0.

The ELITR excerpts are shared under CC BY-NC-SA 4.0, so this repository uses the same licence. See [LICENSE.md](LICENSE.md).
