# Plan 23, amendment 1: the author's tasks

Dated 28 October 2026. These are the jobs in plan 23, amendment 1 that only the author can do. Each one cites the rule it comes from: the amendment by line, the decision sheet (`23-am1-decisions.md`) by entry, and template Section 9 (`23-am1-precoder-template.md`) by run condition. They are in the order they come up. Every other decision took its recommendation (decision sheet, "How to sign").

## 1. At signing

- [ ] Read the signing record that the main session drafts: the commit message, the tag annotation and every hash (B24, B25).
- [ ] Commit everything that `23-plan-amendment-1-signing-record.md` lists: the package, the frozen inputs and other plan-23 records (the loss trace and its adjudications among them), the 23-am1-records folder, plan 23 and `22-bug-list.md` (C63 (a)). Then tag `plan23-amendment-1`. This must happen before any Step 2, 2b or 2c output exists (line 14). You can also ask the main session to do it.
- [ ] Keep copies off this machine (line 93) of `data/ami_eval/a1_smoke/archive/plan23-am1-runs.zip` and of the full workflow transcripts, `data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip`. Both hashes are in the signing record.

## 2. Before Step 2 and the probes (spend)

- [ ] Give the go-ahead for Step 2c (WD, about $20; C3 (a), line 582) when its estimate is ready. Spend above $15 is put to you first.
- [ ] Give the go-ahead for Step 2b (the probes, up to about $16 under C25 (a)) when its estimate is ready.
- [ ] Answer C6 before any score under it (line 137). That means the B3 gold decisions, the three corrections you confirm (line 140), and sending the V5 packet (line 147).
- [ ] Before Phase D, write a dated note that decides whether the machine V4 meets plan 23's V4 item and the Phase D1 gate (line 116).

## 3. Step 3a: your coding

- [ ] Code the pilot, 20 cases (line 310). Then freeze the sub-cause list and commit it with its hash (item 2, line 401). It must be a Markdown table with the names in a column headed "Name" (template Section 1). `23-am1-v4.py case-packets` refuses any other form.
- [ ] Pass 1: code the 180 cases blind (item 4), then hash and commit the codes. Open no V4 conversation or answer before this commit (line 405).
- [ ] Right after the item-4 commit, write a dated note that fixes V4's calendar due date: seven days later (C2, C67).
- [ ] Pass 2 and the pass examinations, after the reveal (items 7 and 8; lines 315 onward). Every change you make after V4's first packet is disclosed as such (line 414).
- [ ] If a codebook revision is triggered (line 409): recode, then rerun V4's case packets with the revised list.

## 4. Step 3a: running V4 in Antigravity (template Section 9)

Do this once, before the first packet:
- [ ] Pick a workspace folder outside the repository, used for nothing else. Its parent folder must be writable (AG1). If you want the stronger option, run Antigravity under a separate macOS user that can read neither `~/Documents` nor `~/.claude`, and record that in a dated note (AG1).
- [ ] In Antigravity, set terminal and browser execution to require approval, or turn them off. Turn off, or empty, rules, saved knowledge or memories, MCP servers and anything that carries context between conversations. Take a dated screenshot of these settings at the start of every working session and after every Antigravity update (AG2).
- [ ] Write a dated note with the Gemini model label exactly as the picker shows it, any variant or reasoning level, and the conversation mode (AG3).

For every packet:
1. `23-am1-v4.py stage --out DIR --packet NAME --workspace WS`.
2. Open a new Antigravity conversation on WS. Pick the model, and send only the instruction that `stage` prints.
3. Save the conversation export, or screenshots of its tool-call list (AG7).
4. Read the tool-call list. Anything other than listing the folder, reading `packet.txt` and writing `answer.json`, or any approval prompt, makes the attempt void (AG4).
5. `23-am1-v4.py collect --out DIR --packet NAME --workspace WS --model LABEL --antigravity-version V`. Add `--void REASON` if step 4 voided it, or if the label or mode was wrong (AG3, AG5).
6. If the shared validator later rejects a stored case answer, run `23-am1-v4.py reject --out DIR --packet NAME --reason TEXT`. The packet then gets its second attempt (AG5).

The order of the jobs:
- [ ] The channel trial: the 20 pilot cases, in their own `--out` folder (line 407). If the instruction has to change, the main session makes the change and a dated note records it before any of the 180 is staged.
- [ ] The 180 cases (item 5), due seven days after the item-4 commit.
- [ ] The audit: 479 decisions in 8 packets (item 6), before the reveal. If it is not done by then, v2 equals v1 (line 95).
- [ ] The fresh sample and any revision re-run, before the reveal (lines 311, 409).
- [ ] Commit the whole V4 record before the reveal (AG7): the manifests, `staging.log`, `model.json`, every attempt, the rejections, the screenshots, the exports and the dated notes.

## 5. Step 3b and later

- [ ] 3b on ES2009: your pass 1, then V4. V4's codes are due seven days after your 3b pass 1 is committed. Use the same model label if it is still offered; otherwise record the new label (template Section 9, 3b; AG3).
- [ ] Phase F, rewriting the thesis once at the end, including the wording entries C43.3, C48, C50, C53, C55 and C56 and the timing entries C46 and C47.

## 6. Optional

- [ ] Override C64, C65 or C66 from the review round on draft 6. Each is applied as recommended, so overriding one means editing the amendment and the template back.
