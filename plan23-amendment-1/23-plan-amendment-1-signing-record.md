# Plan 23, amendment 1: signing record (draft for the author)

Dated 28 October 2026. This is the commit message and the tag annotation for signing (decision sheet B24, B25). The hashes are of the files as they stand now. If any file changes before the commit, re-run `23-am1-check-package.py` and regenerate this record. This file is not in the index's table, because it records the index's hash. It is committed with the package.

**Where it is signed.** The commit and the tag go in a separate public repository, `projectmemory-preregistration` (its README is the cover note). It holds only this package, byte-identical, in the folder `plan23-amendment-1/`, plus a README, a licence note and `SHA256SUMS`. The files were made and checked in the source repository (`Project-Context-Protocol`, branch `thesis/design-cycle-2`, HEAD b4d6b6c, the package in `thesis/notes/thesis_completion/artifacts/`), which stays private. The commit carries no co-author trailer.

## Commit message

```
Plan 23, amendment 1: sign the amendment and its Step 0 package

Signs the amendment (draft 6, reviewed and fixed 28 October 2026) with its
Step 0 package: the design-and-controls register, the claims register with
Rule M, the probe note, the pre-coder template and extract, the audit list
(479 decisions), the V4 setup (Gemini in Antigravity), the decision sheet
(every entry answered or at its recommendation) and the check scripts. Also
commits plan 23 and 22-bug-list.md at their cited states (C63 (a)), the
frozen inputs and plan-23 records (the loss trace v3.1, its adjudications and
results, the EL2020 arms, answerable-only and informed-gate records), and the
archived workflow records (C4 (b)). No Step 2, 2b or 2c output exists.

Package hashes (SHA-256, folder plan23-amendment-1/; made in the source repository's thesis/notes/thesis_completion/artifacts/ at b4d6b6c):
b9c8c50b1f9b202d01a886670ba17c2788306ea26598b656ba34224a5e2dbef4  23-plan-amendment-1-ceilings-and-root-cause.md
493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf  23-am1-audit-list.json
e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f  23-am1-audit-list.py
78b32be0633f42e8ebc326795b951cda98edadb1a090d2def4edc15b09222ee1  23-am1-author-tasks.md
dd08cb8b07b04e026abe75ab18b536c6eec418761a260ec0086cd1f8d02650bc  23-am1-check-package.py
794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9  23-am1-check-register.py
89b712301f5b1d1fb97c0872c37f2659fedc17ba59c830dc6189c4ee77daecb3  23-am1-decisions.md
b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759  23-am1-design-text-94c049d.md
84cdd77e726d7813b810505965023797c777d94f0897fb13edf6baebc6e3707b  23-am1-design-text.py
09036929cd59dc0eb37ba14c3f3f068c9825177a0ee0b0210a95ce51399b4d78  23-am1-precoder-extract.md
2b1a0d29cb9c8015814698515bcae2b193126e5f1e8755ef8ab614a0dfcf4f2a  23-am1-precoder-extract.py
71ba1072dcc014617d67c53eb123e0bfd34ceb998f70b4e3a007dc62e22931da  23-am1-precoder-template.md
056dda5a96e30b6108d3eb64169a35bb1a116717688cdf3b8728c417ed8d0e07  23-am1-probe-note.md
b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf  23-am1-prompts-evaluated.md
c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6  23-am1-prompts.py
a3d77cd94466b6c366a57001d669c525c71974d486168950571bb3339098ea1c  23-am1-register-claims.md
9c7af4e0f7a96103ecc0fb423236a64e21559bad7a6f1b2c2f44cb28a3a8e0da  23-am1-register-design-and-controls.md
c1d8d2f525c702bfa6aa960161c62e22b967e73dd9c6e4133b46e6d20f1fc743  23-am1-run-manifest.py
111695e51b9ec9073b30a6e30d56224098574eb2ea08a7632530aed16079581e  23-am1-step0-index.md
1d550b32813435025996eb1ddaabee21668cb8c6b7179ab2b89ca784aed513f9  23-am1-v4.py
14ecd086a5a5614ac1b46537e67d2c1f788532d427dc23e8d02b7d33ff5aface  23-am1-records/README.md
590684b406986ceb21b968485cbaafde2edf400870afe8ca38fa81506c1bbf58  23-plan-development-and-confirmation.md
2096a1f405c127dab59b821ce008bd840761973bc5a7511ed3ab3aa305bc8fd6  22-bug-list.md
4c12ccef9f7f788806b36eb8f71da25902cf755f8567c7be38f1fb052a52ffb1  23-loss-trace.py
e084d95cd72431fd494b8e5aa7c9e1c69ad80da3481e1271c9d88cd6c272f089  23-loss-trace-adjudications.yaml
da4576242eda6fc181352eb8a4f74172c2961b187ca5e1b5391142c554c9e8a9  23-loss-trace.json
d9a922f1822ea4ef0f97dd3eb28ee230a5492adb8a5ddbe3446118b8da0d1014  23-loss-trace.md
faaa826676dd3699b203652b591b6362f0d3ee6041db2f3a311f9e08cdae377d  23-loss-trace-results.md
4007cbce62173814090380080a388af43824b788e65172ae41baf93e571a961f  23-el2020-arms.md
075c9660233cc16ec20786527cc8f8088373c8028a105a8d9e7f42314a86d33f  23-el2020-arms.json
c41db081c383bfc36011793c4fa6a77a5fe8001b98d9da0da1e685a429776fef  23-el2020-arms.py
047f35ff7903716b03b1478a86d75f72a310b69e66e64c6e3d1724ba444d0449  23-answerable-only.json
90ed1f091ae22d695ede29c85209ffea49669d563b96740f1cbf35b2e70b04cc  23-answerable-only.py
d2ef54895bac467c7e1ce628164affb866a5058b9d9dfad101f1db748541e837  23-informed-gate-replay.json
b508e93cebc2b872826d522bf809d33bbeab8987bc709247e6ca664a4171b453  23-informed-gate-replay.py

Pre-coder template: prompt 8b4422c9b6ee1979a2f3dc369cbea7986440029fa75b5c5c573c7b4facdfd3a9, schema 0c05d09cf63101f59bbf2ba8ec681bff40876472273aee0ef7fa9e46cfec3ddf, extract filled in bae517630fe414f893ed4caeeb00f09645e7c6b7ce49d8de3ccb856a59c23154 (template Section 1).
Audit list (B25): 23-am1-audit-list.json 493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf, 479 decisions; script 23-am1-audit-list.py e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f.
V4 packet salt (B24): 2a8b797065b8d259795962bc44ccc323
Run archive (line 93, outside the repository): data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip a7f86acf08e31ae470c70e206df4e10fa18901458ede89016ab284f9d5f5faed
Workflow transcripts (C4 (b), outside the repository): data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip b067ab052453dbddf16f7a83408fe47f2839c4a2ea4778b8a6c2e2636eaa9a70
Check, in the source repository at b4d6b6c with these files in its working tree: python -I -B thesis/notes/thesis_completion/artifacts/23-am1-check-package.py (11 passed, 1 closed, 28 October 2026).
```

## Tag annotation (`plan23-amendment-1`)

```
Plan 23, amendment 1, signed 28 October 2026 (line 14): decision rules fixed
before any Step 2, 2b or 2c output exists. Every later output cites this tag.

Package hashes (SHA-256, folder plan23-amendment-1/; made in the source repository's thesis/notes/thesis_completion/artifacts/ at b4d6b6c):
b9c8c50b1f9b202d01a886670ba17c2788306ea26598b656ba34224a5e2dbef4  23-plan-amendment-1-ceilings-and-root-cause.md
493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf  23-am1-audit-list.json
e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f  23-am1-audit-list.py
78b32be0633f42e8ebc326795b951cda98edadb1a090d2def4edc15b09222ee1  23-am1-author-tasks.md
dd08cb8b07b04e026abe75ab18b536c6eec418761a260ec0086cd1f8d02650bc  23-am1-check-package.py
794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9  23-am1-check-register.py
89b712301f5b1d1fb97c0872c37f2659fedc17ba59c830dc6189c4ee77daecb3  23-am1-decisions.md
b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759  23-am1-design-text-94c049d.md
84cdd77e726d7813b810505965023797c777d94f0897fb13edf6baebc6e3707b  23-am1-design-text.py
09036929cd59dc0eb37ba14c3f3f068c9825177a0ee0b0210a95ce51399b4d78  23-am1-precoder-extract.md
2b1a0d29cb9c8015814698515bcae2b193126e5f1e8755ef8ab614a0dfcf4f2a  23-am1-precoder-extract.py
71ba1072dcc014617d67c53eb123e0bfd34ceb998f70b4e3a007dc62e22931da  23-am1-precoder-template.md
056dda5a96e30b6108d3eb64169a35bb1a116717688cdf3b8728c417ed8d0e07  23-am1-probe-note.md
b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf  23-am1-prompts-evaluated.md
c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6  23-am1-prompts.py
a3d77cd94466b6c366a57001d669c525c71974d486168950571bb3339098ea1c  23-am1-register-claims.md
9c7af4e0f7a96103ecc0fb423236a64e21559bad7a6f1b2c2f44cb28a3a8e0da  23-am1-register-design-and-controls.md
c1d8d2f525c702bfa6aa960161c62e22b967e73dd9c6e4133b46e6d20f1fc743  23-am1-run-manifest.py
111695e51b9ec9073b30a6e30d56224098574eb2ea08a7632530aed16079581e  23-am1-step0-index.md
1d550b32813435025996eb1ddaabee21668cb8c6b7179ab2b89ca784aed513f9  23-am1-v4.py
14ecd086a5a5614ac1b46537e67d2c1f788532d427dc23e8d02b7d33ff5aface  23-am1-records/README.md
590684b406986ceb21b968485cbaafde2edf400870afe8ca38fa81506c1bbf58  23-plan-development-and-confirmation.md
2096a1f405c127dab59b821ce008bd840761973bc5a7511ed3ab3aa305bc8fd6  22-bug-list.md
4c12ccef9f7f788806b36eb8f71da25902cf755f8567c7be38f1fb052a52ffb1  23-loss-trace.py
e084d95cd72431fd494b8e5aa7c9e1c69ad80da3481e1271c9d88cd6c272f089  23-loss-trace-adjudications.yaml
da4576242eda6fc181352eb8a4f74172c2961b187ca5e1b5391142c554c9e8a9  23-loss-trace.json
d9a922f1822ea4ef0f97dd3eb28ee230a5492adb8a5ddbe3446118b8da0d1014  23-loss-trace.md
faaa826676dd3699b203652b591b6362f0d3ee6041db2f3a311f9e08cdae377d  23-loss-trace-results.md
4007cbce62173814090380080a388af43824b788e65172ae41baf93e571a961f  23-el2020-arms.md
075c9660233cc16ec20786527cc8f8088373c8028a105a8d9e7f42314a86d33f  23-el2020-arms.json
c41db081c383bfc36011793c4fa6a77a5fe8001b98d9da0da1e685a429776fef  23-el2020-arms.py
047f35ff7903716b03b1478a86d75f72a310b69e66e64c6e3d1724ba444d0449  23-answerable-only.json
90ed1f091ae22d695ede29c85209ffea49669d563b96740f1cbf35b2e70b04cc  23-answerable-only.py
d2ef54895bac467c7e1ce628164affb866a5058b9d9dfad101f1db748541e837  23-informed-gate-replay.json
b508e93cebc2b872826d522bf809d33bbeab8987bc709247e6ca664a4171b453  23-informed-gate-replay.py

Pre-coder template: prompt 8b4422c9b6ee1979a2f3dc369cbea7986440029fa75b5c5c573c7b4facdfd3a9, schema 0c05d09cf63101f59bbf2ba8ec681bff40876472273aee0ef7fa9e46cfec3ddf, extract filled in bae517630fe414f893ed4caeeb00f09645e7c6b7ce49d8de3ccb856a59c23154 (template Section 1).
Audit list (B25): 23-am1-audit-list.json 493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf, 479 decisions; script 23-am1-audit-list.py e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f.
V4 packet salt (B24): 2a8b797065b8d259795962bc44ccc323
Run archive (line 93, outside the repository): data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip a7f86acf08e31ae470c70e206df4e10fa18901458ede89016ab284f9d5f5faed
Workflow transcripts (C4 (b), outside the repository): data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip b067ab052453dbddf16f7a83408fe47f2839c4a2ea4778b8a6c2e2636eaa9a70
Check, in the source repository at b4d6b6c with these files in its working tree: python -I -B thesis/notes/thesis_completion/artifacts/23-am1-check-package.py (11 passed, 1 closed, 28 October 2026).
```

## Commands (run by the author, or by the main session on request)

In the public repository's root (`~/Documents/projectmemory-preregistration`). First check every file against `SHA256SUMS`:

```bash
shasum -a 256 -c SHA256SUMS
```

```bash
git add README.md LICENSE.md SHA256SUMS plan23-amendment-1
```

```bash
git commit -F <file holding the commit message above>
```

```bash
git tag -a plan23-amendment-1 -F <file holding the tag annotation above>
```

Then create the public GitHub repository and push the branch and the tag (`git push origin main plan23-amendment-1`).
