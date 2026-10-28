# Plan 23, amendment 1: Step 0 package index

Dated 27 October 2026, updated 28 October after the pre-tag pass. Status: **ready to sign, not signed.** Nothing is committed or tagged. No model, embedding or other API call was made to build any file listed here.

The amendment (line 14) is signed together with this package, then committed and tagged `plan23-amendment-1` **before any Step 2, 2b or 2c output exists**. This index lists what is signed, the hash of each file as it stands now, how each file is checked, and the steps from here to the tag. The hashes change when your answers are applied (decision sheet C1). The tag annotation records the final hashes (B25).

## What you sign

| File | What it is | SHA-256 (28 October, after the pre-tag pass) |
|---|---|---|
| `23-plan-amendment-1-ceilings-and-root-cause.md` | the amendment; draft 6 (27 October, evening): V4 is a machine coder, Gemini in Google Antigravity, with lines changed in place; reviewed and fixed in place on 28 October (line 3 lists the lines) | `b9c8c50b1f9b202d01a886670ba17c2788306ea26598b656ba34224a5e2dbef4` |
| `23-am1-decisions.md` | **start here.** Every open decision once: C (yours, 67), B (operational defaults, 26), A (settled by the amendment, 21); "How to sign" at the top | `89b712301f5b1d1fb97c0872c37f2659fedc17ba59c830dc6189c4ee77daecb3` |
| `23-am1-register-design-and-controls.md` | design-and-controls register: the six components, 94c049d design text versus implementation entries, five per-boundary sheets with the signed readings written in (B22) and per-sentence tags (C8), decisions 1–17 | `9c7af4e0f7a96103ecc0fb423236a64e21559bad7a6f1b2c2f44cb28a3a8e0da` |
| `23-am1-design-text-94c049d.md` | D1–D9 and the rationale table, verbatim from `git show 94c049d`, with the paragraph ids the register cites | `b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759` |
| `23-am1-prompts-evaluated.md` | the prompts as the evaluated runs sent them, from the traces | `b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf` |
| `23-am1-register-claims.md` | claims register (151 rows, R-1 to R-22). Section 9 is the mechanism mapping (M-1 to M-21), including **Rule M** (section 7a), the verdict rule for the architectural mechanisms | `a3d77cd94466b6c366a57001d669c525c71974d486168950571bb3339098ea1c` |
| `23-am1-audit-list.json` | the V4 adjudication audit list: 479 decisions under C18 (b) and C20 a_shared (134 r_carrier, 47 e_wrong_form_carrier, 11 r_shared_key_carrier, 16 r_rival, 286 e_no_carry; some carry two roles). No v1 labels | `493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf` |
| `23-am1-audit-list.py` | computes the list from the frozen trace and adjudications; checks their hashes first | `e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f` |
| `23-am1-probe-note.md` | the Step 2b probe note (decisions PN-1 to PN-14), with the drafted **owner-or-role-claim definition** for the WD rule (C41) | `056dda5a96e30b6108d3eb64169a35bb1a116717688cdf3b8728c417ed8d0e07` |
| `23-am1-precoder-template.md` | the pre-coder template. Prompt `8b4422c9b6ee1979a2f3dc369cbea7986440029fa75b5c5c573c7b4facdfd3a9` (61,451 characters), schema `0c05d09cf63101f59bbf2ba8ec681bff40876472273aee0ef7fa9e46cfec3ddf`; the extract filled in gives `bae517630fe414f893ed4caeeb00f09645e7c6b7ce49d8de3ccb856a59c23154` (291,972 characters; Section 1) | `71ba1072dcc014617d67c53eb123e0bfd34ceb998f70b4e3a007dc62e22931da` |
| `23-am1-design-text.py` | regenerates the design-text file | `84cdd77e726d7813b810505965023797c777d94f0897fb13edf6baebc6e3707b` |
| `23-am1-prompts.py` | regenerates the evaluated-prompts file from the traces | `c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6` |
| `23-am1-check-register.py` | checks every quote and cite in the design-and-controls register against git objects and files | `794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9` |
| `23-am1-run-manifest.py` | recomputes the amendment's run manifest (lines 75–90); `--zip` writes the run archive | `c1d8d2f525c702bfa6aa960161c62e22b967e73dd9c6e4133b46e6d20f1fc743` |
| `23-am1-v4.py` | V4 (Gemini in Antigravity): builds the case and audit packets, stages each into a clean workspace, collects, voids and rejects attempts, at most two per packet (template Section 9, AG1 to AG7) | `1d550b32813435025996eb1ddaabee21668cb8c6b7179ab2b89ca784aed513f9` |
| `23-am1-precoder-extract.md` | the pre-coder extract (B21): the five signed sheets with tagged 94c049d sentences, conformance requirements and implementation entries, item ids on every checklist item | `09036929cd59dc0eb37ba14c3f3f068c9825177a0ee0b0210a95ce51399b4d78` |
| `23-am1-precoder-extract.py` | rebuilds the extract from the register and the design text; `--check` compares bytes | `2b1a0d29cb9c8015814698515bcae2b193126e5f1e8755ef8ab614a0dfcf4f2a` |
| `23-am1-check-package.py` | the package check (B3): every hash, quote, id, schema, probe-overlap, audit-list and manifest check, from repository files only | `dd08cb8b07b04e026abe75ab18b536c6eec418761a260ec0086cd1f8d02650bc` |
| `23-am1-author-tasks.md` | the jobs only the author can do, in order: signing, spend go-aheads, coding passes, running V4 | `78b32be0633f42e8ebc326795b951cda98edadb1a090d2def4edc15b09222ee1` |
| `23-am1-records/README.md` | the archived workflow records (C4 (b)): each run's script and journal, with hashes; not checked by the package check's row rule | `14ecd086a5a5614ac1b46537e67d2c1f788532d427dc23e8d02b7d33ff5aface` |
| `23-am1-step0-index.md` | this file | (recorded in the tag annotation) |

**Outside the repository** (gitignored): the full workflow transcripts, `data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip`, SHA-256 `b067ab052453dbddf16f7a83408fe47f2839c4a2ea4778b8a6c2e2636eaa9a70`; and, reproducible with `23-am1-run-manifest.py --zip`, `data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip`, the three batch folders, 108 files including the crashed a2_r2. SHA-256 `a7f86acf08e31ae470c70e206df4e10fa18901458ede89016ab284f9d5f5faed`. Keep a copy of both off this machine (line 93).

**Cited but not part of the package:** `22-bug-list.md` and `23-plan-development-and-confirmation.md` are modified and uncommitted. They also hold another session's uncommitted work. The claims register and the template cite their working-tree lines; under C63 (a) both go into the signing commit.

## Checks (offline, 28 October)

One committed script re-derives everything: `python -I -B thesis/notes/thesis_completion/artifacts/23-am1-check-package.py` from the repository root. It reads only repository files and git objects, writes nothing in the repository, and exits non-zero on any failure.

| Check | What it re-derives |
|---|---|
| 1 template | prompt and schema hashes, the three placeholders, the extract's byte-identical rebuild and the hashes of its inputs, the filled-prompt hash |
| 2 schema | built-in valid and invalid records through the script's own validator |
| 3 register | `23-am1-check-register.py`: every quote and cite against git objects and files |
| 4 code | code-derived prompt hashes and prompt-to-constant equality; the merge-completeness check is closed (one-time, register decision 10) |
| 5 claims | every quote in the claims register; exactly one deliberate history error |
| 6 sheet | every quote in the decision sheet |
| 7 ids | every C/B/A, R-, M-, AL-, PN-, template-point and register-decision id resolves |
| 8 probe | the probe note's substitution hashes and overlap checks |
| 9 audit | the audit list re-run, byte-identical |
| 10 hashes | every row of this table and of the sheet's file table; every package file has a row |
| 11 manifest | the twelve runs against the amendment's manifest |

Also run: `23-am1-v4.py`'s end-to-end suite on mock inputs (254 of 254) and blindness check 7 on the extract (template Section 5). The last results are in the signing record.

## How the package was reviewed

Every round ran offline. The run records sit under this session's workflow folder, outside the repository; whether they are archived is C4. Each round's reviewers wrote findings, a skeptic tried to refute each one, and a fixer applied the survivors and appended a dated record to the file it changed.

1. **Build** (workflow run `wf_c0d332aa-9c7`): the registers, probe note and template drafted from the sources.
2. **Verification** (`wf_6aa3c2d7-a38`, 23 agents): eight reviewers, one skeptic per reviewer, one fixer per file group, the decision sheet, and a cross-package consistency check. Applied: register 17, claims 25, audit list 5, probe note 11, template 13, plus 8 mechanical consistency fixes.
3. **Completion** (`wf_13bbca79-d64`, 11 agents): Rule M and the owner-claim definition drafted, the naming clashes fixed (probe-note D1–D14 → PN-1 to PN-14, because line 6 reserves D1–D11; Rule V items vs the coder V4), the template aligned with the register's step names and the line-340 scope. 43 findings, 1 refuted, the other 42 applied (the decision-sheet parts in the sheet step).
4. **Second review** (`wf_ae4a7251-a3c`, 11 agents): defects only. Rule M was implemented as code on synthetic inputs, and so was the owner-claim definition. 35 findings survived (1 blocks-signing: "single-value question" was undefined for the evidence family), 1 refuted, 17 nits left. All surviving findings are applied. The main session made the last sync edits (M-11, M-20, C35, C44, the M-17 pointer).
5. **Draft 6 and the author's answers** (another session, 27 October, evening): C1, C2, C4, C25 and C63 answered; the wording entries moved to Phase F; V4 made a machine coder (amendment draft 6, template Section 9, `23-am1-v4.py`). The main session then checked the package against draft 6 and aligned the template, sheet and claims register (their dated records).
6. **Review of draft 6** (`wf_17dc1094-fbf`, 12 agents, 28 October): five lenses, a skeptic each, a completeness critic. 54 findings, 46 survived, 10 of them blocking: the known-answer set (11 cases, not 17; no established answer), V4 able to run before pass 1, and no instrument for V4's item-8 re-codes. Decided as C64 to C67 and fixed in the amendment in place.
7. **Fixes** (`wf_d914f894-e2d`, 5 agents; `wf_7901e997-9ae`, 2 agents; 28 October): the script and template Section 9 rewritten to one interface, each verified, then cross-checked; the follow-ups applied by a second script pass and by the main session. The sheet's record of 28 October lists them.
8. **Pre-tag pass** (`wf_12f53368-49a`, 10 agents; `wf_55666b1e-eee`, 2 agents; 28 October): every remaining decision took its recommendation (the author's instruction). Register B22, C8, C17, C62; claims B8; template C8, C62, B18, B21 with the extract; the package check B3. Three reviewers, each with a skeptic, found nothing that blocks signing; their two major points (V4's check 7, the extract's provenance) were fixed and verified.

**Known limit.** The fixes of rounds 6 and 7 were verified by the agents that made or checked them, not by a fresh review round. Rule M and the bound arithmetic in mapping section 7 took 59 fixes over two rounds, and the second round still found real gaps. The real test that Rule M can be decided is the verdict script, which has to exist before the Step 3 reveal. Any gap it shows goes into a dated note before the reveal (line 16), while the Step 2–2c outputs are still sealed.

## From here to the tag

1. **You read** the signing record, `23-plan-amendment-1-signing-record.md`: the commit message and the tag annotation, with every hash, the audit list's hash, the V4 packet salt and both zip hashes (B24, B25). Your own later jobs are in `23-am1-author-tasks.md`.
2. **You commit and tag** `plan23-amendment-1`, or ask the main session to. The commit holds the package files above, the `23-am1-records` folder, the signing record, plan 23 and `22-bug-list.md` (C63 (a)). The run and transcript zips stay outside the repository.
3. **After the tag,** any change needs a dated note (line 16). No Step 2, 2b or 2c output may exist before the tag (line 14). The next phase is Step 2 with the 3a case pages; Step 2b and 2c each need their own go-ahead on spend.
