export const meta = {
  name: 'am1-step0-reverify',
  description: 'Second adversarial pass on the revised Rule M, the owner-claim definition and the decision sheet; apply surviving defects; final consistency',
  phases: [
    { title: 'Review', detail: 'Rule M integrity, Rule M as code, owner definition as code, decision sheet accuracy' },
    { title: 'Skeptic', detail: 'one skeptic per reviewer' },
    { title: 'Fix', detail: 'claims; probe note + template (with X7, X10); then the sheet' },
  ],
}

const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const S = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad/step0'
const RUNS = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/data/ami_eval/a1_smoke'

const RULES = `
Hard rules:
- No model, embedding or network calls. Do not open, print or source .env. Do not import the \`app\` package. Python: \`python3 -I\` or \`/Users/wesselvansommeren/Documents/Project-Context-Protocol/.venv/bin/python -I\`, stdlib/yaml only.
- No state-changing git commands. \`git show\`/\`git log\` are fine.
- Never edit: the amendment ${A}/23-plan-amendment-1-ceilings-and-root-cause.md (SHA-256 0236ef0385b96012d08e7bcd10a8ec71e436253cb58948d85da4ba563fb81889), plan 23 ${A}/23-plan-development-and-confirmation.md, ${A}/22-bug-list.md, ${A}/23-am1-design-text-94c049d.md, ${A}/23-am1-audit-list.py/.json, ${A}/23-am1-prompts.py, ${A}/23-am1-prompts-evaluated.md, any .tex, anything under app/ or data/.
- Do not compute, look up or report any endpoint, family, verdict or owner-claim result from run data. You may read run files for their format (keys, field names) only.
- Scratch work under ${S}/reverify/ (create it). Keep findings out of memory files.
Context: Step 0 package of plan 23 amendment 1, to be signed by the author together with the amendment. Today is 27 October 2026. This is the SECOND review round. The first round already applied 34 findings to Rule M and 9 to the probe note and template. To converge, report only DEFECTS:
  (1) a contradiction with the amendment, plan 23 or another package file;
  (2) a verdict, test, count or condition a script could not compute without a guess;
  (3) a wrong or unverifiable quote or path:line cite;
  (4) a stale cross-reference or a decision-sheet entry that misstates a package file.
Do NOT propose new options, alternatives, disclosures or improvements unless their absence is one of those defects. Mark anything else 'nit'.`

const FINDINGS = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    findings: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, file: { type: 'string' }, where: { type: 'string' },
      defect_type: { type: 'string', enum: ['contradiction', 'undecidable', 'quote-or-cite', 'stale-or-misstated', 'nit'] },
      problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' },
      severity: { type: 'string', enum: ['blocks-signing', 'should-fix', 'nit'] },
    }, required: ['id', 'file', 'where', 'defect_type', 'problem', 'evidence', 'fix', 'severity'] } },
    signing_triage: { type: 'array', description: 'Only for the decision-sheet reviewer: one item per C entry', items: { type: 'object', properties: {
      entry: { type: 'string' }, needs_author_fact: { type: 'boolean' }, why: { type: 'string' }, recommendation_sound: { type: 'boolean' }, note: { type: 'string' },
    }, required: ['entry', 'needs_author_fact', 'why', 'recommendation_sound'] } },
  },
  required: ['summary', 'findings'],
}
const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'string' }, survives: { type: 'boolean' }, reason: { type: 'string' }, better_fix: { type: 'string' } }, required: ['id', 'survives', 'reason'] } } }, required: ['verdicts'] }
const FIX_SCHEMA = { type: 'object', properties: {
  summary: { type: 'string' }, files_written: { type: 'array', items: { type: 'string' } },
  applied: { type: 'array', items: { type: 'string' } },
  not_applied: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, reason: { type: 'string' } }, required: ['id', 'reason'] } },
  checks: { type: 'string' }, open_for_author: { type: 'array', items: { type: 'string' } },
}, required: ['summary', 'files_written', 'applied', 'not_applied', 'checks', 'open_for_author'] }

const base = `${RULES}
You are an adversarial reviewer. Do not edit package files. Each finding needs file, location, defect type, problem, evidence (verbatim quotes with path:line), a concrete fix, severity. An empty list is a valid answer.`

phase('Review')
const reviewers = [
  { key: 'm-integrity', label: 'review: Rule M (integrity)', prompt: `${base}
Read ${A}/23-am1-register-claims.md section 9 (the mechanism mapping, from the line '## 9. Mechanism mapping' to '## 10.'), with special attention to section 7 (the bound, revised in round 1: pinned bootstrap seed 23 and 50,000 draws, multi-value flip rule, greedy fill, pass share) and section 7a (Rule M and its 15 choices). Also read that file's 'Completion pass (27 October 2026)' entry and its 'Review of the completion pass' list (end of file), the amendment (all of it; especially lines 6-16, 104-125, 160-180, 280-300, 323-378, 400-475), and plan 23 lines 255-365.
Check that Rule M and section 7 contradict nothing in the amendment, plan 23, the class rules, the WD rule, the contracts' contrast, Rule V or section 6; that each verdict is fixed before any Step 2/2b/2c output exists (as far as the text can make it); that 'can't tell' for a known defect cuts both ways (plan 23 line 352); that every quote and cite is verbatim and correct (check them all); and that the round-1 fixes did not introduce inconsistencies between items, choices list, M-19, rows C04/C77/C94, and M-20.` },
  { key: 'm-code', label: 'review: Rule M as code', prompt: `${base}
Implement Rule M (${A}/23-am1-register-claims.md, mapping section 7a, together with section 7's bound and Rule V in section 2 as far as Rule M uses them) as a Python function in ${S}/reverify/rule_m.py that takes SYNTHETIC inputs (per-run endpoint counts for the configuration under test and RAG; within-arm ranges; coded cases with class, mechanism, boundary, and defect flags; pass rows; uncoded counts) and returns exactly one of works / doesn't work / can't tell (with its sub-label) per mechanism. Write synthetic test cases covering: 3 vs 3 and 5 vs 5 runs, a crashed run replaced once, ties, overlap, an instrument range of 0, an empty population (the unknown family), a mechanism with no coded case, rows coded unclear and 'design or model, not separated', a known defect in each direction, flagged rows inside a counted weakening case, multi-value questions, and the ES2009 A1-ref fallback. Do NOT use real run outcomes. Every point where you had to guess because the text is silent or ambiguous, or where two parts of the text give different answers, is a finding (type undecidable or contradiction), quoting the text. Also check the run file formats under ${RUNS} (keys only) and ${A}/23-loss-trace.py for whether every input Rule M names exists. Report the script path in your summary.` },
  { key: 'owner-code', label: 'review: owner-claim definition as code', prompt: `${base}
Read ${A}/23-am1-probe-note.md, section "Owner or role claim on EL2020 (C41, M-17)" and its completion-pass entries, the WD rule (amendment lines 280-297) and amendment line 352. Implement the definition as Python in ${S}/reverify/owner_rule.py against the recorded trace format (read the keys and field names of a frozen run's artifacts under ${RUNS}/el2020_batch_20261022T214813Z/a1_r2/artifacts/ and of ${A}/23-loss-trace.py's span placement; do not count or report owner claims in any real run), and run it only on synthetic fixtures you write. Every guess the text forces, every field it names that does not exist, and every contradiction with the WD rule or with the probe note's other sections is a finding. Also check the probe note's remaining cites (path:line) in that section and its rename table (D->PN) for correctness, and that ${A}/23-am1-precoder-template.md has no stale reference to probe-note decisions.` },
  { key: 'sheet', label: 'review: decision sheet', prompt: `${base}
Read the decision sheet ${A}/23-am1-decisions.md in full. For each entry, check that it states the package files and the amendment correctly (quotes verbatim; options, recommendations and 'Changes' match what the files say; cites resolve). Focus on the entries changed today: C1 (pre-tag list), C2, C28, C29, C30, C38, C41, C43 (and C43.1-C43.3, and its list of Rule M's 15 choices against mapping section 7a's list in ${A}/23-am1-register-claims.md), C44, C62, C63, B26, section X, the file-hash table (recompute every SHA-256 listed with shasum -a 256 and report any mismatch except for files edited after the table's stated time), and the counts line.
Also fill signing_triage: one item for EVERY C entry (C1 to C63, and C43.1-C43.3). needs_author_fact = true only if a sound answer needs something only the author knows or prefers (a person's name, a date, readiness of other uncommitted work, a preference about thesis wording or archiving, consent), not merely a judgment the sheet's analysis already makes. recommendation_sound = false if the recommendation contradicts the amendment or plan 23 or rests on a misstated fact; explain in note.` },
]
const reviewed = await pipeline(reviewers,
  r => agent(r.prompt, { label: r.label, phase: 'Review', schema: FINDINGS }),
  (rev, r) => {
    const fs = (rev?.findings ?? []).filter(f => f.severity !== 'nit').map(f => ({ ...f, id: `${r.key}:${f.id}` }))
    if (!fs.length) return { rev, fs, verdicts: [] }
    return agent(`${RULES}
You are a skeptic. For each finding, check the cited sources yourself and try hard to refute it. survives=false if it is wrong, already handled in the file, not one of the four defect types, or its fix would break the amendment or another package file. If it survives but the fix is not the best, give better_fix (a fix that adds no new author choice where possible). Do not edit files.
Findings:
${JSON.stringify(fs, null, 1)}`, { label: `skeptic: ${r.key}`, phase: 'Skeptic', schema: VERDICTS }).then(v => ({ rev, fs, verdicts: v?.verdicts ?? [] }))
  },
)

const all = reviewed.filter(Boolean)
const survivors = all.flatMap(x => x.fs.map(f => ({ f, v: x.verdicts.find(v => v.id === f.id) })).filter(y => !y.v || y.v.survives).map(y => ({ ...y.f, better_fix: y.v?.better_fix ?? '' })))
const refuted = all.flatMap(x => x.fs.filter(f => x.verdicts.some(v => v.id === f.id && !v.survives)).map(f => ({ id: f.id, reason: x.verdicts.find(v => v.id === f.id).reason })))
const nits = all.flatMap(x => (x.rev?.findings ?? []).filter(f => f.severity === 'nit').map(f => ({ id: f.id, file: f.file, problem: f.problem })))
const triage = (all.find(x => x.rev && x.rev.signing_triage)?.rev?.signing_triage) ?? []
const inFile = (f, n) => (f.file || '').includes(n)
const fClaimsList = survivors.filter(f => inFile(f, 'register-claims'))
const fPTList = survivors.filter(f => inFile(f, 'probe-note') || inFile(f, 'precoder-template'))
const fSheetList = survivors.filter(f => inFile(f, 'decisions'))
const fOther = survivors.filter(f => !fClaimsList.includes(f) && !fPTList.includes(f) && !fSheetList.includes(f))
log(`surviving: claims ${fClaimsList.length}, probe/template ${fPTList.length}, sheet ${fSheetList.length}, other ${fOther.length}; refuted ${refuted.length}; nits ${nits.length}`)

phase('Fix')
const fixBase = `${RULES}
Apply the surviving findings below (use better_fix where given). Do not add new author choices: if a defect can only be fixed by a choice, state the defect plainly in the text where it sits, record it in open_for_author, and leave the rest unchanged. Append to the file's existing "Completion pass (27 October 2026)" entry a dated "Second review (27 October 2026)" list: each finding id, applied or not, and why. Re-run the relevant checks.`
const [fixC, fixPT] = await parallel([
  () => fClaimsList.length ? agent(`${fixBase}
Edit only ${A}/23-am1-register-claims.md. Re-run the quote check ${S}/complete/qcheck_claims.py (python3 -I). Keep M-19's and the choices list's count in step with Rule M.
Findings:
${JSON.stringify(fClaimsList, null, 1)}`, { label: 'fix: claims register', phase: 'Fix', schema: FIX_SCHEMA }) : Promise.resolve(null),
  () => agent(`${fixBase}
Edit only ${A}/23-am1-probe-note.md and ${A}/23-am1-precoder-template.md.
Also apply two edits that follow from decision-sheet entries already settled (A11 = probe-note PN-8; B25 = AL-7), listed as template Section 7 points 22 and 23 and in the decision sheet's C1 pre-tag list:
- X7: template table C2 also excepts \`admitted:span_not_seen\` cases from probe (i), as PN-8 lists them apart with no probe output. Mark point 22 done.
- X10: template blindness check 1 (Section 5) names \`23-am1-audit-list.json\` among the files that fail. Mark point 23 done.
After all edits, recompute the prompt and schema SHA-256 with ${S}/verify/pt/hashes.py and record them in Section 1 (keep earlier hashes as history); re-run ${S}/verify/pt/vq.py and the latest schema test in ${S}/verify/pt/ or ${S}/complete/ if the schema changed.
Findings (may be empty):
${JSON.stringify(fPTList, null, 1)}`, { label: 'fix: probe note + template', phase: 'Fix', schema: FIX_SCHEMA }),
])

const sheetFix = await agent(`${fixBase}
Edit only the decision sheet ${A}/23-am1-decisions.md.
1. Apply these surviving sheet findings: ${JSON.stringify(fSheetList, null, 1)}
2. Mirror what the other fixers changed: claims register ${JSON.stringify(fixC ? { summary: fixC.summary, open: fixC.open_for_author } : 'no changes')}; probe note and template ${JSON.stringify(fixPT ? { summary: fixPT.summary, open: fixPT.open_for_author } : 'no changes')}. In particular: C1's pre-tag list no longer lists X7 and X10 as to-do (they are applied now; say so), and its line-pointer item is resolved (the probe note now cites M-17 by heading, not line, done by the main session). Keep C43's list of Rule M's choices equal to mapping section 7a's list.
3. Refresh the file-hash table with current SHA-256 of every listed file (shasum -a 256) and the time; update the counts line to the real counts.
4. Add near the top, under 'What this sheet is', a short subsection 'How to sign' that says: signing adopts every A and B entry and the recommendation of every C entry the author does not answer otherwise, EXCEPT the entries that need a fact only the author has, which must be answered: list them, using this triage from the sheet reviewer (keep only entries where needs_author_fact is true; check each yourself; add C2's V4 name and date if missing): ${JSON.stringify(triage.filter(t => t.needs_author_fact))}. Then list, as 'recommendations to read before accepting', the entries the reviewer marked recommendation_sound=false, with the reason, if any remain after the fixes: ${JSON.stringify(triage.filter(t => t.recommendation_sound === false))}. If a recommendation is unsound and you can correct it from the files without a new choice, correct the entry instead and say so. Do not change any other recommendation.
5. Re-run the sheet's quote check ${S}/verify/decisions/qcheck.py and the id-resolution script ${S}/complete/sheet/ids.py (read them first), and \`python3 -I ${A}/23-am1-check-register.py\`; confirm the amendment hash; recompute the template hashes with ${S}/verify/pt/hashes.py and compare with the template's Section 1. Report all results in checks.
Other surviving findings that no fixer owned (report them in open_for_author if still true): ${JSON.stringify(fOther)}
Append a dated record at the end of the sheet.`, { label: 'fix: decision sheet + final checks', phase: 'Fix', schema: FIX_SCHEMA })

return { surviving: survivors.map(f => ({ id: f.id, file: f.file, severity: f.severity, problem: f.problem })), refuted, nits, triage, fixes: { claims: fixC, probe_template: fixPT, sheet: sheetFix }, reviews: all.map(x => ({ summary: x.rev?.summary })) }
