export const meta = {
  name: 'review-draft6-v4',
  description: 'Defects-only adversarial review of amendment draft 6 (machine V4) and the V4 setup, with a skeptic per reviewer and a completeness critic',
  phases: [
    { title: 'Review', detail: 'five lenses on draft 6 and the V4 setup' },
    { title: 'Verify', detail: 'one skeptic per reviewer tries to refute each finding' },
    { title: 'Critic', detail: 'what the reviewers missed, then verified' },
  ],
}

const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const SCR = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad'
const PY = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/.venv/bin/python'

const CONTEXT = `
You are reviewing part of a master's-thesis evaluation package ("plan 23, amendment 1", Step 0) before the author signs it. Files are in ${A}.

Background, in brief:
- The amendment (23-plan-amendment-1-ceilings-and-root-cause.md) fixes, before any new output exists, how a root-cause study (Step 3) codes why gold values were lost by the system under test (ProjectMemory, run on gpt-5.4-mini; its judge is also GPT). The author codes cases blind (pass 1); a model pre-coder (claude-opus-5-5, the same model as the v1 loss-trace adjudications) pre-codes every case from the same page and template; a second coder "V4" codes blind; the agreement (Cohen's kappa, binary implementation-vs-not, lower 95% bound >= 0.40) gates any "design limit" claim; a repair cause needs author and V4 to agree on >= 3 distinct values (line 480). V4 also audits the v1 trace adjudications (item 6, the audit list 23-am1-audit-list.json).
- Draft 5 was approved and reviewed in four rounds. Draft 6 (27 October, evening; written by a different session, never reviewed) makes V4 a MACHINE coder: a Google Gemini model run by the author as an agent in Google Antigravity (an agent IDE with file, terminal and browser tools), one new conversation per packet, each packet staged alone into a clean workspace folder outside the repository by 23-am1-v4.py, using the pre-coder's prompt unchanged for cases and the loss trace's carry standard verbatim for the audit. A known-answer set (17 A0 cases flagged bug3_replaced_in_own_meeting, lost at state maintenance; V4 must get >= 14 as implementation at state maintenance) gates whether V4's codes count. The copy check was rewritten for a machine V4. On 28 October lines 405, 419 and 430 were edited again to align with draft 6.
- Approved draft 5: ${SCR}/step0/reverify/lc/23-plan-amendment-1-ceilings-and-root-cause.md . Draft 6 before the 28 October edit: ${SCR}/amendment-draft6-058d0a73.md . Diff either against the current file to see every change (changed lines: 3, 116, 405-407, 419, 430, 432, 583, 612).
- The V4 setup: 23-am1-v4.py; template 23-am1-precoder-template.md Section 9 (line 913 to the end; also Section 1 assembly, Section 2 the prompt between the lines "~~~~ prompt" and "~~~~", Section 4 agreement measures, Section 6 leak check); decision sheet 23-am1-decisions.md entries C1, C2 (line ~91), C4, C25, C63, B24 (line ~695), the "How to sign" section (line ~22) and the dated records at the end; index 23-am1-step0-index.md. The loss trace standard: 23-loss-trace.md; the trace data: 23-loss-trace.json (keys: decisions, runs, arms, ...). Bug list: 22-bug-list.md. Plan 23: 23-plan-development-and-confirmation.md (its Phase F item 1 was moved on 27 October by the same session).

Rules for you (binding):
- Do not edit, create, move or delete any file in the repository. If you need scratch files, use only ${SCR}/review-d6/<your label>/ (create it).
- No network and no model/LLM/API calls. Never read or print any .env file.
- You may run 23-am1-v4.py with ${PY} -I, only with --out/--workspace paths inside your scratch folder and a test salt such as TEST-review. It makes no API call. Do not run git commands that change state; git show/diff/log are fine.
- Repository memory may appear in your context; it is background only. Read the files themselves. Do not write memory.
- Amendment lines are cited by number throughout the package: any amendment fix you propose must be an in-place change of existing lines (no added or removed lines).
- Report DEFECTS only: something wrong, ambiguous enough to be decided two ways, inconsistent, unenforceable, or a validity threat an examiner would raise and the text does not answer. No praise, no style nits unless they change meaning. Each finding quotes its evidence verbatim with file:line. Prefer few solid findings over many weak ones.
- Severity: "blocks-signing" (the package cannot be signed as is: a rule that cannot be applied, a contradiction between signed files, a leak that breaks blindness), "major" (a validity threat or ambiguity that could change a result or a claim), "minor" (wrong or stale text that changes no result), "nit".
`

const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'short id like L1-3' },
          severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] },
          file: { type: 'string' },
          line: { type: 'integer' },
          title: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string', description: 'verbatim quotes with file:line' },
          proposed_fix: { type: 'string', description: 'minimal concrete fix; amendment fixes in place only' },
        },
        required: ['id', 'severity', 'file', 'line', 'title', 'problem', 'evidence', 'proposed_fix'],
      },
    },
    checked: { type: 'string', description: 'what you checked and found sound, one short paragraph, so the critic knows the coverage' },
  },
  required: ['findings', 'checked'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          refuted: { type: 'boolean' },
          reason: { type: 'string', description: 'why it is or is not a real defect, with the evidence you checked (file:line)' },
          severity: { type: 'string', enum: ['blocks-signing', 'major', 'minor', 'nit'] },
          fix: { type: 'string', description: 'the fix you would apply, corrected if the reviewer\'s is wrong or too broad; amendment fixes in place only' },
        },
        required: ['id', 'refuted', 'reason', 'severity', 'fix'],
      },
    },
  },
  required: ['verdicts'],
}

const LENSES = [
  { key: 'validity', label: 'L1-validity', prompt: `LENS: validity of a machine V4, as an examiner would attack it.
Check at least: (1) independence: V4 uses the pre-coder's prompt unchanged, so the instrument is shared; is the copy check (line 430) as now worded applicable and sufficient, and is "clearly above the author's" decidable? (2) the known-answer set (line 407): verify from 23-loss-trace.json and 23-loss-trace.md that there are exactly 17 A0 cases lost at state maintenance with the bug3_replaced_in_own_meeting flag under the case definition (amendment "Unit", line ~299); check whether the flag makes "implementation defect caused at state maintenance" the known answer (22-bug-list.md bug 3, the Phase B reproduction), whether the pages could give the answer away or make it trivially easy, whether 14 of 17 is a meaningful bar, and whether the set's cases are coded by anyone else; (3) the 0.40 design-limit rule and line 480's per-cause agreement with a machine V4; (4) reproducibility (Antigravity does not pin model versions) and what is recorded; (5) whether the disclosure ("independent machine coder, not human inter-rater reliability") matches what the procedure actually gives; (6) whether the fallback (line 432) is triggered correctly by a failed known-answer set and what happens to items 6 and 8 and 3b then.` },
  { key: 'blindness', label: 'L2-blindness', prompt: `LENS: blindness, sealing and timing for a machine V4.
Check at least: (1) order of work (amendment items 1-8, lines ~399-421) and the tag rule (line 14): when can V4 run, what exists at that time, and can any V4 packet contain or be built from a Step 2/2b/2c output, a pass-1 code, a pre-code or a v1 label? (2) items 7-8 after the reveal: V4's forced re-codes and 3b coding — what does a V4 re-code packet contain, is V4 then blind to the other's codes as line ~416 requires, and does 23-am1-v4.py / template Section 9 say how re-code and 3b packets are built? (3) Antigravity as a channel: an agent with file, terminal and browser tools, Google account-level memory/"knowledge", rules, MCP; does Section 9 make violations detectable (conversation export kept only "where offered"?), what voids an answer, and can the agent read outside the workspace? (4) the audit packets: run audit-packets into your scratch folder and inspect them for anything that reveals the v1 label or role (field names, ordering, ids, context counts, grouping by role); (5) the leak check of template Section 6 — does it cover V4's packets as well as the pre-coder's?` },
  { key: 'code', label: 'L3-code', prompt: `LENS: code review of 23-am1-v4.py (read all of it).
Check correctness and safety: (1) stage empties the workspace folder — can it delete anything the author did not intend (symlinks, a folder that resolves into the repository or the home directory, a folder holding other files, relative paths, a folder that is a parent of the repository)? (2) the refusals (folder inside the repository, extra file, uncollected answer): test each one in your scratch folder; (3) collect: does it verify the staged packet is unchanged, validate the answer against the real schema (the template's schema between BEGIN/END OUTPUT SCHEMA) for cases and against the audit format for audit packets, handle invalid JSON, duplicate or missing ids, extra fields, and keep every attempt with hashes and the recorded model name? (4) ordering and determinism: ascending sha256("<salt>|<id>") per B24, packet sizes, every audit item exactly once, the carry-standard verbatim check against 23-loss-trace.md; (5) case-packets: literal single replacement of the three placeholders as template Section 1 requires, refusal if a placeholder is missing or the extract is unfilled; (6) any network or API call, any read of .env, any path outside its inputs. Build packets and exercise stage/collect end to end in scratch with a test salt and mock answers (valid and invalid). Report only real defects with a reproduction.` },
  { key: 'consistency', label: 'L4-consistency', prompt: `LENS: consistency of draft 6 and the author's recorded answers across the whole package.
Check at least: (1) every mention of V4 in the amendment, template (all sections), decision sheet, claims register (23-am1-register-claims.md), probe note (23-am1-probe-note.md), index and 23-am1-v4.py: does any still assume a human V4, a subsample of cases, hours of a person's work, "their" codes, or V4 being "asked how it was produced"? (2) numbers: 180 cases + 17 known-answer cases, audit list 430 now and 474/479 after decisions C18/C20, 8 packets of about 60, the cost/time table (line 583), the V4 due date in C2 vs line 116/432; (3) the sheet's How to sign, C1's pre-tag list, C2, C4, C25, C63 answers, and the Phase F move (plan 23 Phase F item 1, sheet C46/C47, claims R-2): do they agree with each other and with the amendment; are any items left unstated before the tag (the packet salt, V4 due date fixed by a dated note)? (4) line-cite integrity: diff draft 5 vs the current amendment and confirm no line moved; then check that every package citation of a changed line (3, 116, 405-407, 419, 430, 432, 583, 612) still points at text that says what the citing file claims. (5) the index's hash table and check rows vs the files on disk (compute SHA-256).` },
  { key: 'coldread', label: 'L5-coldread', prompt: `LENS: a cold read of the draft-6 lines as the signer and as a thesis examiner would read them.
Read amendment lines 1-20, 95-120, 299-460, 475-485, 550-623 in context, then template Section 9 and sheet C2. For every sentence draft 6 changed or added, ask: can it be applied mechanically by someone who was not in the conversation, with one outcome? Look for undefined terms ("fails the known-answer set", "gate nothing", "reported only", "clearly above", "a failed answer gets one retry", "void"), missing rules (what if Gemini refuses, times out, returns an invalid answer twice, the model picker changes model mid-study, the author used the wrong model; what if fewer than 17 known-answer cases exist under the final page builder; how known-answer cases are mixed among the 180 so V4 cannot tell them apart), and contradictions between draft 6 and the unchanged lines around it (e.g. item 5's "Hashed and committed" and "Only the blind kappa (items 4-5) can trigger a codebook revision", item 8, 3b at line ~305/312, the stopping rule, line 559, decision 2 at line 612).` },
]

const reviewPrompt = (l) => `${CONTEXT}\n\n${l.prompt}\n\nReturn your findings (ids prefixed ${l.label.split('-')[0]}-) and a short note of what you checked and found sound.`

const verifyPrompt = (l, r) => `${CONTEXT}

You are the SKEPTIC for reviewer ${l.label}. Below are its findings. For EACH finding, try hard to refute it: re-read the cited lines yourself, check whether the text elsewhere already answers it, whether the reviewer misread, whether it is outside what draft 6 / the V4 setup changed and was already settled in draft 5's four review rounds (then it is refuted unless draft 6 made it worse or it blocks applying a rule), or whether the severity is inflated. Default to refuted=true if, after checking, you are not convinced it is a real defect. If it survives, give the severity you believe and the minimal fix you would apply (amendment fixes in place only, no added or removed lines). For code findings, reproduce them in ${SCR}/review-d6/${l.label}-skeptic/ before accepting.

FINDINGS:
${JSON.stringify(r.findings, null, 1)}`

const results = await pipeline(
  LENSES,
  (l) => agent(reviewPrompt(l), { label: l.label, phase: 'Review', schema: FINDINGS }),
  (r, l) => {
    if (!r || !r.findings || r.findings.length === 0) return { lens: l.label, review: r, verdicts: [] }
    return agent(verifyPrompt(l, r), { label: `${l.label}-skeptic`, phase: 'Verify', schema: VERDICTS })
      .then(v => ({ lens: l.label, review: r, verdicts: v ? v.verdicts : null }))
  },
)

const ok = results.filter(Boolean)
const coverage = ok.map(x => `${x.lens}: ${x.review ? x.review.checked : '(no result)'}\nFindings: ${x.review ? x.review.findings.map(f => f.id + ' ' + f.title).join('; ') : ''}`).join('\n\n')

phase('Critic')
const critic = await agent(`${CONTEXT}

You are the COMPLETENESS CRITIC. Five reviewers (validity, blindness, code, consistency, cold read) have reviewed draft 6 and the V4 setup. Their coverage notes and finding titles are below. Find what they MISSED: a file not read, a draft-6 sentence nobody tested, a V4 job (cases, known-answer set, audit, re-codes after the reveal, fresh sample, 3b on ES2009) whose procedure is not specified end to end, a rule with no owner, a hash or record the signing note will need but nothing produces. Do not repeat their findings. Return only new defects, same rules and severities.

COVERAGE:
${coverage}`, { label: 'critic', phase: 'Critic', schema: FINDINGS })

let criticVerdicts = []
if (critic && critic.findings && critic.findings.length) {
  const v = await agent(verifyPrompt({ label: 'critic' }, critic), { label: 'critic-skeptic', phase: 'Critic', schema: VERDICTS })
  criticVerdicts = v ? v.verdicts : null
}

return { results: ok, critic: { review: critic, verdicts: criticVerdicts } }
