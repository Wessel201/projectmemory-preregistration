# Plan 23, amendment 1: archived workflow records (decision C4 (b))

Dated 28 October 2026. For every workflow run that the amendment's "Already read" list (lines 58–63) and the Step 0 package cite, this folder holds the run's script and its `journal.jsonl`. The journal gives every agent's return value: the findings, the skeptic verdicts and the fixers' reports. Before archiving, the records were scanned for secrets (API keys, tokens, private keys); none were found.

The full agent transcripts are not kept here. They carry session attachments and come to about 330 MB. They are zipped outside the repository, in `data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip` (SHA-256 b067ab052453dbddf16f7a83408fe47f2839c4a2ea4778b8a6c2e2636eaa9a70, 92,738,247 bytes). Keep a copy of that zip off this machine (amendment line 93).

| Run | What it was | File | SHA-256 |
|---|---|---|---|
| `wf_0db6eaa4-f2a` | loss-trace adjudication, fixpoint | `journal.jsonl` | `8f3f95e6dcd832bd991a2ce1053bafaa478f0b8f635f08c5c15e427be0145c51` |
| `wf_0db6eaa4-f2a` | loss-trace adjudication, fixpoint | `loss-trace-adjudicate-wf_0db6eaa4-f2a.js` | `0b18a710e1c1b9225bb9c4bed6e6f1ae84e0de18e882f9e9cb5b381b61d22899` |
| `wf_12870ac1-8bc` | amendment review round 1 | `amendment-review-wf_12870ac1-8bc.js` | `98bfabf08c9ff1387392b27b55d45a3a775fd79af15e562b181fc57567566526` |
| `wf_12870ac1-8bc` | amendment review round 1 | `journal.jsonl` | `661940308c1d875e9bd3d81b0078462c0ec679907ae7883786daf3feb81ef7ba` |
| `wf_12f53368-49a` | pre-tag pass (register, template, extract, B8, check script) | `journal.jsonl` | `fda32f9a9f4ca8625527c04d462ddf1cb275470d49d9c253ef2a8d1787133f9b` |
| `wf_12f53368-49a` | pre-tag pass (register, template, extract, B8, check script) | `step0-pretag-wf_12f53368-49a.js` | `0281f4739b7993f7579bf6a14e6b8511f837dc7ceb37fa937af4563180403556` |
| `wf_13bbca79-d64` | Step 0 completion pass | `am1-step0-complete-wf_13bbca79-d64.js` | `bd9223f6f7f1078762c701dddfe2248800dbdf3afa4f0947ad0246f9492aa0d8` |
| `wf_13bbca79-d64` | Step 0 completion pass | `journal.jsonl` | `01a899a6d62572d1fdbcec6828ebade9deec8414aeed61501ce70cc6d7bdb19e` |
| `wf_17dc1094-fbf` | review of draft 6 (V4) | `journal.jsonl` | `ed1e98b5243f886d7b7d00fc76c81fc36fe010d4653df8acb831676f5844fc61` |
| `wf_17dc1094-fbf` | review of draft 6 (V4) | `review-draft6-v4-wf_17dc1094-fbf.js` | `584a08a08115f1d4bd07b3d807ace33849d3ff6e20a07a6d052e43a46f31b7f8` |
| `wf_317beeac-5f6` | loss-trace notes verification | `journal.jsonl` | `f742bfd2717d544e1253c20c960252c147d92ed7d951a5521863c8e07507bf56` |
| `wf_317beeac-5f6` | loss-trace notes verification | `loss-trace-notes-verify-wf_317beeac-5f6.js` | `d9ae3ef331bfa175e29f880cf092140b832e6da7420bbab089a6274614e1472e` |
| `wf_4e0604f8-389` | loss-trace verification | `journal.jsonl` | `bd768f3917a99a6d8e80ce977c829927624420d6e9c8400edf6f7a0a91a3f69f` |
| `wf_4e0604f8-389` | loss-trace verification | `loss-trace-verify-wf_4e0604f8-389.js` | `7aa2a3d8d6a9b21f9bc03da5ae385767ee89ead84584c2138457307677615c11` |
| `wf_536a6a0a-1ae` | amendment review round 2 | `amendment-review-2-wf_536a6a0a-1ae.js` | `a69c71b661ee8b4730992d3debda43ac47e46aacae5e1bb2828887f11f28ab4e` |
| `wf_536a6a0a-1ae` | amendment review round 2 | `journal.jsonl` | `7ae3158942c935e15b254d91b937a35e42add4c0c5f75c4bedb10be8c5e67bdd` |
| `wf_55666b1e-eee` | pre-tag follow-ups | `journal.jsonl` | `2035a9d6756dd12fd43a90d4ed66792964a48fc3630a80c071cf4104e2e942f1` |
| `wf_55666b1e-eee` | pre-tag follow-ups | `step0-pretag-2-wf_55666b1e-eee.js` | `32fcc13daa013ad3159b0f702c754016b74af8acea4a09050dbd5775bc0646fc` |
| `wf_6aa3c2d7-a38` | Step 0 verification | `am1-step0-verify-wf_6aa3c2d7-a38.js` | `5b9177ccbe805e66459fad217a8aa80ec78dc5febe21a6728fa40cad56e8b55b` |
| `wf_6aa3c2d7-a38` | Step 0 verification | `journal.jsonl` | `6390f1ca484873ae3b16559a1838bb6fb837b05a3f4899625a10729f2b637d8d` |
| `wf_7901e997-9ae` | second V4 script pass | `fix-v4-script-2-wf_7901e997-9ae.js` | `e37d8bbe3d29d678d6de720233b5a5fa842d8e12bc45b78026a8320e42bb7f33` |
| `wf_7901e997-9ae` | second V4 script pass | `journal.jsonl` | `2a5bd27944b01575ca20a6c24c30bb0825538c4caf4cfd991d224c310ce30172` |
| `wf_ad8f2921-1d7` | amendment review round 3 | `amendment-review-3-wf_ad8f2921-1d7.js` | `1fc29dd5282582b6e50822aad74c42acace6a10cd955087d2949469ac3e8cbaa` |
| `wf_ad8f2921-1d7` | amendment review round 3 | `journal.jsonl` | `a9f97fb47e6027b453537102ceb085ea2d895a305133c795bf18c0de54330484` |
| `wf_ae4a7251-a3c` | Step 0 second review | `am1-step0-reverify-wf_ae4a7251-a3c.js` | `3e5b47bc67802c485830420ac1a9f3a007843ca78d28ec63e878a6e65392da7f` |
| `wf_ae4a7251-a3c` | Step 0 second review | `journal.jsonl` | `64fb682c6a110b033915439fccd851446e6e6c07678b0e7320a79661040f6bb9` |
| `wf_bbe042f0-d23` | loss-trace verification, round 2 | `journal.jsonl` | `67afd99496d53710493b11614914eeac9d53e9af28859af38ab40e879aca8ce9` |
| `wf_bbe042f0-d23` | loss-trace verification, round 2 | `loss-trace-verify-r2-wf_bbe042f0-d23.js` | `65ba9baad2e5e14dfe481da35a4fda6b5a39fe760c7eb2b397a3a508864c5c63` |
| `wf_c00c1888-413` | loss-trace adjudication, round 3 | `journal.jsonl` | `0ac81462fae99ce173c6be2314ea24efa7feddbf6be7a432db3f2fbf95592858` |
| `wf_c00c1888-413` | loss-trace adjudication, round 3 | `loss-trace-r3-wf_c00c1888-413.js` | `d3f7868bf16eb68565d0f1633cbee04d4857423e9b94e1919a8e0a488991e872` |
| `wf_c0d332aa-9c7` | Step 0 build | `am1-step0-build-wf_c0d332aa-9c7.js` | `56d9217b2947cccfc6593a5d068777d8831cbb2d7934940b0de9155fb88ae58e` |
| `wf_c0d332aa-9c7` | Step 0 build | `journal.jsonl` | `22b40399bf9958f64f2858ad035096f9b51cb8afe5966be3332cf0e0fddb9bdb` |
| `wf_d3a83b84-308` | amendment review round 4 | `amendment-review-4-wf_d3a83b84-308.js` | `b51966068d884ae7151b48897ffe390fa0d6777b0737bc0221934126719bf990` |
| `wf_d3a83b84-308` | amendment review round 4 | `journal.jsonl` | `d076bce9bb7d6197962aaa456bcbfb9d912478990e02ea935eadeef57c5f3b7c` |
| `wf_d914f894-e2d` | fix pass on the V4 script and template Section 9 | `fix-v4-setup-wf_d914f894-e2d.js` | `1778035061a206d4fd60ccb9815f8a169ab14bebb4ac3976fdcf2662f128c7b9` |
| `wf_d914f894-e2d` | fix pass on the V4 script and template Section 9 | `journal.jsonl` | `41323a3adb3464ae61f6aee9bd0c11f687aac0fc75cb9621c70ca6417f517fa0` |
| `wf_ebdcd91e-4ab` | the amendment's fact reports (line 58) | `amendment-facts-wf_ebdcd91e-4ab.js` | `f3e1512a765af13fb1344c9e12babb37021e49eaaf0b4aed27f03aa3a15956c7` |
| `wf_ebdcd91e-4ab` | the amendment's fact reports (line 58) | `journal.jsonl` | `c9474bd7dba8a1c7161b6d4f57877ae3b1e4b31cca393300b9a97ca8204f079d` |
