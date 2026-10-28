export const meta = {
  name: 'fix-v4-setup',
  description: 'Apply the review fixes to 23-am1-v4.py and template Section 9, then verify each fix and cross-check script, template and amendment',
  phases: [
    { title: 'Fix', detail: 'one fixer for the script, one for the template' },
    { title: 'Verify', detail: 'one verifier per file' },
    { title: 'Cross-check', detail: 'script vs template Section 9 vs amendment' },
  ],
}

const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const SCR = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad'
const PY = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/.venv/bin/python'
const FINDINGS = `${SCR}/review-d6-survivors.md`

const COMMON = `
Context: a thesis evaluation package (plan 23, amendment 1, Step 0) in ${A}. A review round found defects in "draft 6", which made the second coder V4 a machine coder (a Gemini model run by the author as an agent in Google Antigravity, one packet per conversation, staged by ${A}/23-am1-v4.py into a clean workspace outside the repository). The surviving findings, with each skeptic's verdict and fix, are in ${FINDINGS} (ids L1-*, L2-*, L3-*, L4-*, L5-*, L6-*). The main session has ALREADY edited the amendment (${A}/23-plan-amendment-1-ceilings-and-root-cause.md) in place; read its lines 3, 116, 305, 310-312, 399-440, 480, 572 and 583 as they now stand. The decisions the main session took (recorded as decision-sheet entries C64-C67, recommendations the author may still override):
- C64: the known-answer set is DROPPED entirely (no gate, no diagnostic). Line 407 now holds a channel trial instead: before the first of the 180 cases, V4's channel is tried on the 20 pilot cases (line 310), which count toward nothing; a change to V4's instruction found necessary there is fixed, with its hash, in a dated note before any of the 180 is staged.
- C65: V4 does NOT re-code at item 8 (line 414): its mechanically resolved blind code is its final code. After a codebook revision (line 409) every V4 case packet is rebuilt with the revised sub-cause list and re-run before item 7, both sets kept hashed (as template point 15 (a) for the pre-codes). The fresh sample (line 311) and 3b (lines 305, 312) use the same case procedure.
- C66: the copy check switches nothing; the 0.40 design-limit rule takes the lower of the two lower 95% bounds of the author's blind binary kappa with V4 and with the pre-codes (line 430).
- C67: no V4 packet, case or audit, is staged before item 4 (author pass 1) is committed (line 405); V4's due date is seven days after item 4's commit (pending the author's confirmation in C2).

The agreed command-line interface of 23-am1-v4.py after the fix (both the script and template Section 9 must match it exactly):
- audit-packets --salt S --out DIR [--batch 60]
- case-packets --template T --subcauses F --pages DIR --salt S --out DIR   (also used for the 20 pilot cases of the channel trial, the fresh sample, a codebook-revision re-run and 3b, each into its own --out)
- stage --out DIR --packet NAME --workspace WS
- collect --out DIR --packet NAME --workspace WS --model LABEL --antigravity-version V [--void REASON] [--model-change]
- reject --out DIR --packet NAME --reason TEXT   (records that the shared validator rejected the packet's stored valid attempt; it then counts as a failed attempt)
- There is NO --response option any more: an answer given only in the chat is a failed attempt.
Rules the script enforces and Section 9 states:
- stage appends a JSON line to DIR/staging.log (packet, packet sha256, workspace, time) for every staging. It refuses: a workspace inside the repository (compare with os.path.samestat against the repository root for the workspace and every parent, so case variants and /System/Volumes/Data firmlink paths are caught); a workspace holding anything other than packet.txt and answer.json; a workspace whose packet.txt has a staging with no collected attempt yet; a packet that already has a counted valid attempt; a packet that already has two attempts. Emptying the workspace only ever removes packet.txt and answer.json.
- collect records exactly one attempt per staging (a second collect for the same staging is refused). It checks the workspace still holds that packet. With --void it records a void attempt (valid false, void true, the reason, the raw answer if any) and runs no checks. A missing, unreadable or non-UTF-8 answer.json is recorded as a failed attempt with the problem, not a crash; non-string ids in an audit answer are a problem, not a crash. After recording it removes answer.json and packet.txt from the workspace. Every record carries: packet, attempt number, staging reference, model label, antigravity_version, settings "none exposed", channel, instruction_sha256, collected_at, prompt_sha256 (the packet's), source "workspace", raw_sha256, raw, fence_removed, answer, valid, void, void_reason, rejected (false), problems.
- At most two attempts per packet, voids, missing answers and rejected attempts included (R7). A packet with two failed attempts has no V4 code; stage refuses it.
- Model label: the first collect in DIR writes DIR/model.json; a later collect with a different --model is refused unless --model-change, which appends the new label with the time and the packets coded so far.
- reject writes a separate DIR/<packet>.attempt-N.rejected.json (the original attempt file is never changed); that attempt then counts as failed, so a re-ask is allowed if fewer than two attempts exist.
- Collect's case checks: check 7 is an exact match of sub_cause against a name in the frozen sub-cause list (or "none fits"), not a substring of the whole text; check 3 tests each quote only against the block of its stated source (the case page block or the register-extract block of the assembled prompt; find the actual delimiters in the template's Section 1/2). A record passing collect's checks is "valid" only provisionally: the shared validator (template Section 4, checks 1-9) runs on every stored case record before any agreement, and a rejection is recorded with reject.
- Audit packets: each item prints id, fact_id, gold value, the gold value's status from the suite (find the field in data/ami_eval/suites/transfer_el2020.yaml via the script's SUITE path), aliases, text and contexts. The header explains the status line in one sentence, so the standard's ruled-out bullet can be applied.
- INSTRUCTION (the whole message of each conversation) becomes: "packet.txt in this folder is the message it refers to: where it says \\"this message\\", it means packet.txt. Read packet.txt and do what it asks. Its \\"Do not use tools\\" allows exactly three actions here: listing this folder, reading packet.txt, and writing your answer to answer.json in this folder. Do not read any other file, run a command, open a browser or search the web. Write to answer.json the JSON object the packet asks for and nothing else, and do not answer in the chat."
- The run conditions of template Section 9 are renamed AG1-AG7 (they were V1-V7, which clashed with the coder name V4); the script's comments cite AG ids.

Binding rules for you:
- Edit ONLY the file(s) your task names. Never create, edit or delete any other repository file. Scratch work only under ${SCR}/fix-v4/<your label>/.
- No network, no model/LLM/API calls, never read or print a .env file. Run Python as ${PY} -I. Never point --workspace or --out at a path inside the repository; for repository-guard tests, use a fake repository copy inside your scratch folder, or compute without creating.
- No git commands that change state.
- Write in the style of the surrounding text: plain, short declarative sentences, no marketing words. Keep the template's prompt (Section 2, between the lines "~~~~ prompt" and "~~~~") byte-identical: its SHA-256 must stay fd7e2f6b0d91cbc73567c272e354dfd210f0455b0bb8f50100d44353ca0c8bb4.
`

const REPORT = {
  type: 'object',
  properties: {
    done: { type: 'array', items: { type: 'string' }, description: 'each change made, one line each, with the finding ids it answers' },
    not_done: { type: 'array', items: { type: 'string' }, description: 'anything in your task you did not do, and why' },
    tests: { type: 'string', description: 'what you ran and the results (for the script: every behaviour in the rules list)' },
    open_questions: { type: 'array', items: { type: 'string' } },
  },
  required: ['done', 'not_done', 'tests', 'open_questions'],
}

const VERDICT = {
  type: 'object',
  properties: {
    problems: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] },
          where: { type: 'string', description: 'file:line' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['severity', 'where', 'problem', 'evidence', 'fix'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['problems', 'summary'],
}

const TASKS = [
  {
    key: 'script', label: 'fix-script',
    prompt: `${COMMON}
YOUR TASK: edit ${A}/23-am1-v4.py (and nothing else) so that it implements exactly the interface and rules above, and answers findings L1-11, L2-3, L2-6 (fact_id), L3-1, L3-2, L3-3 (comment only: the STANDARD is the loss trace's 23-loss-trace.md:148 wording, a condensed form of the adjudicator prompts of round 3 and the fixpoint; do NOT edit 23-loss-trace.md), L3-4, L3-5, L3-8, L3-9, L4-4 (INSTRUCTION), L4-12, L4-13, L5-7, L6-6 in ${FINDINGS}. Update the module docstring to describe the jobs as they now are (cases incl. the pilot channel trial, the fresh sample, revision re-runs and 3b; the audit), with no known-answer set, and V4 starting after item 4. Fix the contexts() docstring ("over every traced run"). Keep the code style of the file (small functions, argparse, plain comments). Then test every rule in scratch end to end with a test salt and mock inputs: audit-packets (with fact_id and status present, no role or label field), case-packets on a mock filled template, mock sub-cause list and mock pages that mirror the real formats, stage/collect valid, invalid, missing, non-UTF-8, non-string ids, --void, two-attempt limit, reject then re-ask, one-collect-per-staging, model change refused then allowed with --model-change, staging.log lines, workspace guards (extra file, case-variant and firmlink spellings of a fake repo root, symlink into the fake repo, a parent of the fake repo). Report every change and every test result.`,
    verify: `${COMMON}
YOU ARE THE VERIFIER for the edited ${A}/23-am1-v4.py. Read the whole file. Independently re-test every rule in the list above in ${SCR}/fix-v4/verify-script/ (fresh mock inputs; never inside the repository), and check each finding the fixer claims to answer (ids in its report below) against ${FINDINGS}. Look for regressions: anything that worked before and broke, a refusal that can be bypassed, a crash path, a path that deletes anything other than packet.txt/answer.json, a record field missing, a network call, an .env read, a packet field that leaks a v1 label or role. Report only real problems with a reproduction. Do not edit any file.`,
  },
  {
    key: 'template', label: 'fix-template',
    prompt: `${COMMON}
YOUR TASK: edit ${A}/23-am1-precoder-template.md (and nothing else). Rewrite Section 9 (from the heading "## 9. V4:" to the end of the file, but keep the two dated records at its end, "Main session sync (27 October 2026, late evening)" and anything after it, unchanged, then append one new dated record "Review round on draft 6 (28 October 2026)" listing what changed in this file and the finding ids) so that it matches the amendment as now edited and the agreed interface and rules above. Section 9 must cover: what V4 receives (cases; the 20-case pilot channel trial; the audit, with its fields id, fact_id, gold value, status, aliases, text, contexts; the instruction and its stored hash); timing (no V4 packet, case or audit, before item 4 is committed; the due date per decision sheet C2 and C67); run conditions AG1-AG7 (these replace R1-R6 and R9 for V4; R7 holds with voids, missing answers and rejections counted as attempts; R8 applies to the pre-codes only): AG1 workspace (say plainly that staging limits what the folder holds and does not confine the agent; blindness rests on AG2, AG4 and AG7; running Antigravity under a separate macOS user account that cannot read ~/Documents is the stronger option, recorded in a dated note if used), AG2 conversation and settings (terminal and browser execution set to require approval or off; rules, saved knowledge or memories and MCP servers empty or off; recorded with a dated screenshot at each session start and after any Antigravity update; the Antigravity version recorded with every answer), AG3 model (picker label fixed in a dated note before the first packet, which is the pilot trial; an answer under any other label is void; a change or withdrawal is recorded with collect --model-change and the packets after it are reported apart; 3b uses the same label if offered, otherwise the new label is recorded and 3b's kappa is reported as coded by a different V4 model), AG4 tools (mechanical void: any tool call other than listing the workspace folder, reading packet.txt and writing answer.json, and any approval prompt, which the author declines; decided from the conversation's tool-call list and recorded with collect --void REASON), AG5 answers (one collect per conversation; at most two attempts per packet with voids, missing answers and rejections counted; a chat-only answer is a failed attempt; collect's provisional checks; the shared validator on every stored case record before any agreement, a rejection recorded with reject; packets left without a code are excluded from the kappa and their number reported per job), AG6 blindness (what V4 never sees; blindness check 3 compares every V4 case packet's prompt hash with the pre-coder's record of the same case before any agreement is computed), AG7 the record (manifests, staging.log, model.json and the model note, every attempt incl. voids and rejections, settings screenshots, and every conversation's export or screenshots of its tool-call list; an attempt with neither is void; all committed and hashed before the reveal, item 7). Also cover: V4 does not re-code at item 8 (line 414); codebook revision re-runs, the fresh sample and 3b; the audit standard's provenance and what V4 gets compared with the v1 adjudicators (finding L3-3: condensed standard, no evidence lines or questions, at most three contexts, gold status but no kind, no file access; disclosed with the audit agreement); and "What this does not give" (no call-for-call reproducibility; Antigravity's own agent instructions and tool definitions cannot be recorded, so R2's record is not available for V4). Remove every mention of the known-answer set. Elsewhere in the template: line ~19 conventions should date amendment cites as of 28 October 2026 (draft 6; every line keeps its number); Section 4's "Candidate causes for Step 4 (line 406)" becomes "Candidate causes, reported only (line 406)"; Section 4's copy-check row becomes "the copy check (line 430) | class mapped to implementation versus not, blind codes, compared with V4's and the author's"; Section 5 R7/R8 and anything else that still says V4 re-codes, has a known-answer set, or that "R7 and R8 hold as written" for V4, aligned. Do not change the prompt (Section 2). Finally grep the whole template for "known-answer", "V1." .. "V7." run-condition ids, "re-code", "human", "fresh chat" and fix stale ones outside the prompt. Report every change.`,
    verify: `${COMMON}
YOU ARE THE VERIFIER for the edited ${A}/23-am1-precoder-template.md. Confirm the prompt hash is unchanged (recompute: SHA-256 of the lines between "~~~~ prompt" and the next "~~~~", each line ending in a newline). Read Section 9 and every other changed passage. Check it against the amendment lines as they now stand, the decisions C64-C67 above, the agreed interface and rules, and the findings in ${FINDINGS} it claims to answer (fixer's report below). Find anything wrong, ambiguous enough to be applied two ways, missing from the required coverage list, or contradicting another section of the template. Report only real problems. Do not edit any file.`,
  },
]

const results = await pipeline(
  TASKS,
  (t) => agent(t.prompt, { label: t.label, phase: 'Fix', schema: REPORT }),
  (rep, t) => agent(`${t.verify}\n\nFIXER'S REPORT:\n${JSON.stringify(rep, null, 1)}`, { label: `verify-${t.key}`, phase: 'Verify', schema: VERDICT })
    .then(v => ({ task: t.key, fixer: rep, verifier: v })),
)

phase('Cross-check')
const cross = await agent(`${COMMON}
YOU ARE THE CROSS-CHECKER. Both ${A}/23-am1-v4.py and ${A}/23-am1-precoder-template.md Section 9 have just been edited by two different agents. Check that they agree with each other and with the amendment (${A}/23-plan-amendment-1-ceilings-and-root-cause.md lines 3, 116, 305, 310-312, 399-440, 480, 572, 583, 612): every command, option, refusal, record field, file name (staging.log, model.json, attempt and rejected files), attempt rule, the instruction text Section 9 describes vs the script's INSTRUCTION, the audit packet fields, AG ids cited by the script, timing, re-code and 3b rules. Run the script's --help for each subcommand (offline) to compare. Report only real mismatches or contradictions. Do not edit any file.`, { label: 'cross-check', phase: 'Cross-check', schema: VERDICT })

return { results: results.filter(Boolean), cross }
