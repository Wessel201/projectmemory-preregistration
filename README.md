# ProjectMemory: pre-registered analysis rules

This repository holds the analysis rules for a master's thesis. Each set of rules was published before the results it governs existed, so the rules can't have been adjusted to fit those results.

The thesis asks what works, and what doesn't, when AI turns meeting transcripts into project knowledge that stays up to date. The system built for the study is called ProjectMemory. It reads meeting transcripts, extracts the decisions and facts in them, keeps a record of the project's current state, and answers questions about that state with citations.

Each set of rules is one folder, fixed by a git tag. A tag is never moved. Any later change to a set of rules is made in a new, dated note that says what had been seen by then.

| Tag | Folder | Fixed on |
|---|---|---|
| `plan23-amendment-1` | [`plan23-amendment-1/`](plan23-amendment-1/) | 28 October 2026 |

## What the first set of rules covers

In development runs on four meetings from the ELITR Minuting Corpus, ProjectMemory lost many of the facts it should have kept. A trace of every lost fact showed where each was lost:
- about a third were never extracted from the transcript;
- a quarter to a third were lost because another value won out over the right one, or overwrote it.

The trace shows where a fact was lost, but not why. The rules fix, in advance, how the next steps will find out why and how their results will be judged:

- **Step 2, ceilings:** the recorded runs are replayed from their records, with the losses at one stage removed at a time. This shows how far the score could rise if that stage worked.
- **Step 2b, probes:** small live tests of single model calls on recorded inputs, to see whether a stage can get a lost fact right at all.
- **Step 2c, whole-decision extraction:** the most common extraction loss is a claim that states only part of a multi-part value. A variant that asks the model to extract whole decisions is tested against the current version.
- **Step 3, root-cause study:** the author codes, blind, the cause of each lost fact in a sample of 180. An independent second coder, a Google Gemini model, codes the same cases as a check.
- **Step 4, one repair round:** a repair is accepted only on criteria fixed in advance, such as a test that fails before the repair and passes after it.
- **Step 5, a second meeting series:** development runs on four meetings from the AMI Meeting Corpus. Their lost facts are then coded with the causes found in Step 3, as a check that those causes carry over.

The central rule is that every coded loss ends in exactly one of three states:
1. It was repaired.
2. It was shown, with evidence, to come from the design as documented before the first runs, from the conversation itself, from the evaluation, or from the language model, which was held constant.
3. It is an unrepaired defect, or unclear. A result can then be "can't tell".

No loss counts as a limit of the design by default.

## Where to start reading

- [`23-plan-amendment-1-ceilings-and-root-cause.md`](plan23-amendment-1/23-plan-amendment-1-ceilings-and-root-cause.md): the rules themselves. Other files cite it by line number.
- [`23-am1-step0-index.md`](plan23-amendment-1/23-am1-step0-index.md): a table of every file in the package and what it is.
- [`23-am1-decisions.md`](plan23-amendment-1/23-am1-decisions.md): every open question the rules raised, and how each was answered.
- [`23-plan-amendment-1-signing-record.md`](plan23-amendment-1/23-plan-amendment-1-signing-record.md): the exact text of the commit and the tag, with the hash of every file.

The files are working documents, so they use many internal terms. The glossary below covers the common ones.

## Glossary

| Term | Meaning |
|---|---|
| Plan 23 | the plan for the thesis's second design cycle (`23-plan-development-and-confirmation.md`). Amendment 1 changes parts of it and leaves the rest in force. |
| Step 0 to Step 5 | the stages of work in the amendment. Step 0 prepared this package, Step 1 prepares the second meeting series, and Steps 2 to 5 are described above. |
| A0, A1, A2 | the system versions compared: A0 is the version evaluated in the first cycle, A1 has its known bugs fixed, and A2 adds new design rules ("contracts") to A1. |
| Arm | one system version run under the same conditions, usually three times. |
| EL2020 | the development set: four meetings from the ELITR Minuting Corpus (EL2020a–d), with 105 questions. |
| ES2009 | the second series: four meetings from the AMI Meeting Corpus (ES2009a–d). |
| Gold value | the reference answer a fact should have. |
| Loss trace | the record of where each gold value was lost, in each run. |
| Oracle; R, E+R | the ceiling computations of Step 2. |
| Case | one gold value in one run, at one place where it was lost: the unit the root-cause study codes. |
| Adjudications; v1, v2 | judgments on whether a stored text carries a gold value. v1 are the original judgments, made by Claude models. v2 is v1 with the second coder's labels in place of the audited ones. |
| Audit list | the 479 v1 judgments that change a Step 2 result. The second coder re-judges all of them blind. |
| V4 | the second, independent coder of the root-cause study: a Google Gemini model, run in Google Antigravity. |
| Pre-coder | a Claude model that codes every case from its case page before the author's blind pass, using the template fixed here. |
| Registers | two reference tables. The design-and-controls register sets the documented design (the thesis's Chapter 4 as committed on 9 September 2026, before the first runs) beside the code. The claims register lists the thesis's claims and the rule that decides each verdict. |
| C1, B3, … | numbered entries in the decision sheet, `23-am1-decisions.md`. |
| Line 14, line 405, … | line numbers in the amendment. |

## Checking the files

`SHA256SUMS` lists every file in the folder with its SHA-256 hash. To check them:

```bash
shasum -a 256 -c SHA256SUMS
```

The tag's own message also lists the hashes of the 35 core files.

The scripts in the folder were written for the private repository where the work is done. They read that repository's history and its run data, which aren't published here, so they won't run from this repository. They are kept unchanged because their hashes are part of the record.

## Data and licence

Some files quote short excerpts of meeting transcripts and minutes from two public corpora:

- **ELITR Minuting Corpus** (English): Nedoluzhko, A., Singh, M., Hledíková, M., Ghosal, T. and Bojar, O. (2022). *ELITR Minuting Corpus: A Novel Dataset for Automatic Minuting from Multi-Party Meetings in English and Czech.* LREC 2022. http://hdl.handle.net/11234/1-4692. Licensed CC BY-NC-SA 4.0.
- **AMI Meeting Corpus**: Carletta, J. et al. (2005). *The AMI Meeting Corpus: A Pre-announcement.* MLMI 2005. https://groups.inf.ed.ac.uk/ami/corpus/. Licensed CC BY 4.0.

The ELITR excerpts may only be shared under CC BY-NC-SA 4.0, so this repository uses the same licence. See [LICENSE.md](LICENSE.md).
