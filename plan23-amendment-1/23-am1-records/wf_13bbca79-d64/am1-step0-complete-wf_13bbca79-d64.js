export const meta = {
  name: 'am1-step0-complete',
  description: 'Draft the verdict rule (C43) and owner-or-role definition (C41), fix the naming clashes, adversarially review, update the decision sheet',
  phases: [
    { title: 'Draft', detail: 'verdict rule in claims mapping; definition + id rename in probe note; template alignment' },
    { title: 'Review', detail: 'two lenses on the verdict rule, one on the mechanical fixes and definition' },
    { title: 'Skeptic', detail: 'try to refute each finding' },
    { title: 'Fix', detail: 'apply surviving findings, per file' },
    { title: 'Sheet', detail: 'update the decision sheet and re-check consistency' },
  ],
}

const A = '/Users/wesselvansommeren/Documents/Project-Context-Protocol/thesis/notes/thesis_completion/artifacts'
const S = '/private/tmp/claude-501/-Users-wesselvansommeren-Documents-Project-Context-Protocol/8a52f676-3530-41e6-95d3-d845feff8a5a/scratchpad/step0'

const RULES = `
Hard rules for this task:
- No model, embedding or network calls. Do not open, print or source .env. Do not import the \`app\` package (it reads .env). Python: use \`python3 -I\` or \`/Users/wesselvansommeren/Documents/Project-Context-Protocol/.venv/bin/python -I\`, stdlib/yaml only.
- No git commands that change state (no add, commit, stash, checkout, reset). \`git show <commit>:<path>\` and \`git log\` are fine.
- Never edit these files: ${A}/23-plan-amendment-1-ceilings-and-root-cause.md (the amendment, final, SHA-256 0236ef03...), ${A}/23-plan-development-and-confirmation.md (plan 23), ${A}/22-bug-list.md, ${A}/23-am1-design-text-94c049d.md, ${A}/23-am1-audit-list.py, ${A}/23-am1-audit-list.json, ${A}/23-am1-prompts.py, ${A}/23-am1-prompts-evaluated.md, any .tex file, any code under app/.
- Edit only the file(s) your task names. Scratch scripts go under ${S}/complete/ (create it).
- Write in plain, short sentences, matching the surrounding file's style (dated records, verbatim quotes in quotation marks with path:line cites).
- Keep findings out of any memory files.
Context: the package is the Step 0 package of plan 23 amendment 1 (the amendment). The author approved the amendment text as is and will sign it together with this package; the decision sheet ${A}/23-am1-decisions.md lists every open decision (classes C your call, B operational default, A settled). Today is 27 October 2026.
`

const FIX_SCHEMA = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    files_written: { type: 'array', items: { type: 'string' } },
    applied: { type: 'array', items: { type: 'string' } },
    not_applied: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, reason: { type: 'string' } }, required: ['id', 'reason'] } },
    checks: { type: 'string' },
    open_for_author: { type: 'array', items: { type: 'string' } },
  },
  required: ['summary', 'files_written', 'applied', 'not_applied', 'checks', 'open_for_author'],
}
const FINDINGS = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    findings: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, file: { type: 'string' }, where: { type: 'string' },
      problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' },
      severity: { type: 'string', enum: ['blocks-signing', 'should-fix', 'nit'] },
    }, required: ['id', 'file', 'where', 'problem', 'evidence', 'fix', 'severity'] } },
  },
  required: ['summary', 'findings'],
}
const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, survives: { type: 'boolean' }, reason: { type: 'string' }, better_fix: { type: 'string' },
    }, required: ['id', 'survives', 'reason'] } },
  },
  required: ['verdicts'],
}

phase('Draft')
const drafts = await parallel([
  () => agent(`${RULES}
Task: draft the verdict rule for the architectural mechanisms, and fix two naming items, in ${A}/23-am1-register-claims.md (the claims register; its section 9 is the mechanism mapping). Edit only that file.

1. THE VERDICT RULE (decision sheet C43; mapping decision M-19, claims register around line 4330). Plan 23 requires, for each mechanism, "an endpoint and a pre-registered rule for *works*, *doesn't work* or *can't tell*" (plan 23 line 344) and "Write the rule down before the last development comparison." (plan 23 line 269). Read plan 23 lines 255-365 (development and Phase D sections), the amendment in full (especially lines 6-16, 104-125, 280-300 for the WD rule as a model of a pre-registered rule with an exact permutation p and within-arm ranges, 323-378 for classes and pending results, 400-475 for Step 3 sequence and the bound, 555-620), the mapping (claims register section 9, all of it, especially the per-mechanism populations and endpoints, section 6, Rule A, and the bound arithmetic proposal near line 4293 with M-14 and M-20), and the decision sheet entries C27-C44 (they choose endpoints and populations; your rule must work under the recommended answers and say what changes under the alternatives).
   The architectural mechanisms are: epistemic status, change and supersession, rejection, complete decisions, evidence and provenance. Restraint is removed. Contracts are NOT in scope (they have their own on/off contrast); do not redefine anything already fixed for contracts or for WD.
   Plan 23 says: "Architectural mechanisms are judged by their family endpoint against RAG. The loss trace shows at which boundary their failures arise." and "Can't tell applies: when the effect lies within the instrument range; when a known defect affects the mechanism. This cuts both ways" and "The instrument range for the new series is defined here" (plan 23 line 361, in the Phase D registration).
   Draft a rule that:
   - names, per mechanism, its endpoint by pointing at the mapping's fixed endpoint/population (do not invent a new endpoint where the mapping has one; where the mapping leaves it to a C decision, write the rule conditionally and name the decision);
   - compares the configuration under test with RAG on that endpoint over repeats, with an exact test that is achievable at the development repeat count (3 per arm on EL2020, so an all-runs-ordered one-sided rule gives p = 1/20, as in the WD rule) and at registration (5 per arm, plan 23);
   - defines the instrument range per series operationally and before outcomes (for example from within-arm ranges of the endpoint across repeats, as the WD rule uses "the largest within-arm range"), and says how "within the instrument range" is decided;
   - applies the known-defect clause in both directions, with a mechanical test for "a known defect affects the mechanism" (for example bug incidence on the mechanism's population from the loss trace / known-bug records, fixed now);
   - says how the loss-trace bound (amendment lines 451-471) enters, if at all, and how cases coded "unclear" or "design or model, not separated" affect the verdict;
   - gives exactly one of works / doesn't work / can't tell for every possible outcome, including ties, empty populations (the unknown family, C29), crashed or missing runs (a2_r2 crashed and was replaced by a2_r2b), and RAG having no answer on unasked rows;
   - says which verdicts are development verdicts (EL2020, A1 or the final configuration vs RAG) and that the Phase D3 registration may revise the rule for Phase D only in a dated note (amendment line 114);
   - states plainly that the rule was written after the EL2020 family-level results under "Already read" had been read (the amendment is "not blind"), and that it is fixed before any Step 2, 2b or 2c output exists.
   While drafting, DO NOT compute or look up family-level or endpoint results from run data to choose thresholds: thresholds must follow from structure (repeat counts, exact p, within-arm ranges computed later). You may read run file formats only to check the endpoint is computable.
   Placement: a new mapping subsection right before section 8 (the decisions list) or wherever the mapping's rule sections sit (look at how "Rule A" and "Rule V" are placed), titled "Rule M: verdicts for the architectural mechanisms (drafted 27 October 2026 for C43)". Open it with: drafted for decision C43 option (a); if C43 is answered (b), this text moves unchanged into a dated note before the Step 3 reveal. Update M-19's text to say the rule is drafted in Rule M and the choice left is C43. Update the dependency lines of rows C04, C77 and C94 (near lines 377, 2070, 2538) to point at Rule M.
2. M-17 (near line 4328) and the row near line 2879: the definition of "owner or role claim" is being drafted in parallel in ${A}/23-am1-probe-note.md under the fixed heading "Owner or role claim on EL2020 (C41, M-17)". Update M-17 and that row to point at that heading. Do not draft the definition yourself.
3. X4: in the mapping, Rule V's items are V1-V10, but "V4" is also the second coder (amendment usage; claims register lines ~2166, ~2272). Rename every reference to Rule V's items to the form "Rule V item N" (or a similar unambiguous form; be consistent), leaving every V4-the-coder use unchanged. Check every occurrence of \\bV[0-9]+\\b in the file and classify each.
4. X14: '(iv) is the WD rule (amendment:350–355)' — check amendment lines 350-356 and correct the range if line 356 belongs to the WD-cases rule. 'Already read' is cited as amendment:33–61 here and 33–63 in the template: check the amendment's actual 'Already read' block and correct this file's range (the template is fixed by another agent; report the correct range in your summary).
5. Probe-note decision ids: the probe note's own decisions D1-D14 are being renamed PN-1..PN-14 by another agent (Ch. 4 decisions D1-D11 and paragraph ids like D4.p3 keep their names). Update any reference in this file to the probe note's decisions (for example "probe note D7", "probe-note decision D2") to PN-n. Do not touch references to Ch. 4 decisions.
6. Run the quote checker ${S}/verify/qcheck_claims.py (read it first; adapt a copy under ${S}/complete/ if paths need it) and fix any error you introduced. Append a dated entry "Completion pass (27 October 2026)" at the end of the file listing what changed.
Return what you did; list in open_for_author anything the author must decide that your draft cannot settle.`, { label: 'draft: verdict rule (claims)', phase: 'Draft', schema: FIX_SCHEMA }),

  () => agent(`${RULES}
Task: in ${A}/23-am1-probe-note.md only.
1. DEFINITION (decision sheet C41; mapping decision M-17). The amendment's WD rule (amendment lines 286-296) requires "no owner or role claim is lost;" (line 293). The EL2020 gold has no owner or role items, so the condition must be defined on claims. Draft a definition under a new heading exactly "Owner or role claim on EL2020 (C41, M-17)", placed with the note's other Step 2c / WD material (read the whole note first). It must be mechanical and decidable without gold and without model calls, from what the Step 2c runs record. Read the WD arm description (amendment lines 280-297; plan 23 around line 264, "P23:264"), the extraction output schema and how claims are recorded in the run files (look at a frozen A1 run's trace.json / state.json under /Users/wesselvansommeren/Documents/Project-Context-Protocol/data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/a1_r2/artifacts/ to see the claim fields; read the code that writes them under app/ by reading files, without importing), and the WD switch (extraction_whole_decisions, in app/core/cycle2_flags.py or wherever it lives; read only). Define: (a) which claims are owner or role claims (on recorded claim fields: for example a claim whose predicate or key assigns a person, team or role to a matter; be explicit about the fields and the test, and about borderline cases such as a speaker attribution or a "who will do X" action item); (b) what "lost" means for the WD rule (relative to which run, at which boundary, matched how across runs, given that whole-decision extraction may merge claims); (c) the decision: the condition fails if ... . Give a worked example from the recorded claim format (no outcome numbers: do not count owner or role claims in any run, and do not report any result). If the recorded fields cannot support a mechanical test, say so and give the closest decidable definition with its limitation.
2. X3, rename: the amendment says '"D1"–"D11" mean only the design decisions of Ch. 4' (amendment line 6). This note numbers its own decisions D1-D14 (for example "(decision D2)", "[D7]"). Rename every one of this note's own decisions to PN-1..PN-14 (keep sub-item wording like "D3, second item" -> "PN-3, second item"). Do NOT rename references to Ch. 4 design decisions (D1-D11 meaning Ch. 4, or paragraph ids like D4.p3, D9.p4). Inspect every match of \\bD[0-9]+\\b and classify it. Proposals P6, P11-P13 keep their names.
3. If any §1.4 code or printed static text changes (it should not), recompute the note's hashes the way the note itself does and update them.
4. Append a dated entry "Completion pass (27 October 2026)" at the end listing what changed, including the full rename table (old id -> new id).
Return what you did; in open_for_author list any choice in the definition the author must confirm.`, { label: 'draft: owner-or-role definition, PN rename (probe note)', phase: 'Draft', schema: FIX_SCHEMA }),

  () => agent(`${RULES}
Task: in ${A}/23-am1-precoder-template.md only. These are consistency fixes found by the cross-package check of 27 October. The template's prompt block is hashed; nothing is signed yet, so changing it is fine, but you must recompute and record the hashes.
1. X5, step names: Template A5 uses 'extractor' where the design-and-controls register ${A}/23-am1-register-design-and-controls.md E.1 'Chain' line says 'extraction (LLM, system)'; it uses 'conflict evaluation and resolution engine' where S.1 says 'conflict evaluation and the resolution engine'; 'key hint' and 'hint filing' do not appear in K1.1. Read the register's Chain lines for E.1, K1.1, K2.1, S.1 and R.1 and align every step name in the template (prompt and non-prompt parts) to the register's names verbatim. Template section 3 requires this alignment before signing.
2. X6, scope of the line-340 condition: the amendment (lines 331 and 340) applies "design or model, not separated" and the extra requirement to "an LLM step with no model condition". The register sheets apply it step by step (sheet K2: "for the resolver, the condition of line 340 applies"; sheet R: "for question routing and grounding"). The template's A5, E6 and output schema apply it to whole K1, K2 and R boundaries, deterministic steps included. Align the template with the register sheets and with the amendment's per-step wording: the condition and the class "design or model, not separated" apply only to the LLM steps the sheets name. Quote amendment lines 331 and 340 where you state it. If you find that the sheets themselves contradict the amendment, do not change the sheets: report it.
3. X12: prompt A1 says the harness reviewer 'accepts or rejects new keys'. Register K2.6c says no reject is submitted under quality, and none occurred. Reword A1 to match K2.6c.
4. The probe note's own decisions D1-D14 are being renamed PN-1..PN-14 by another agent (Ch. 4 decisions D1-D11 and paragraph ids keep their names). Update every reference in this template to the probe note's decisions to PN-n. Do not touch Ch. 4 references.
5. 'Already read' range: the template cites amendment 33-63, the claims register 33-61. Check the amendment's 'Already read' block and correct this file if needed.
6. Recompute the prompt SHA-256 (text before substitution) and the schema SHA-256 exactly as before: read ${S}/verify/pt/hashes.py and run it (or a copy under ${S}/complete/). Update Section 1 (lines ~24-25) with the new hashes and character count, keeping the history note style ("recomputed 27 October 2026 after the completion pass; previous 65d423b0…"). Re-run ${S}/verify/pt/vq.py (the verbatim-part check against the amendment) and ${S}/verify/pt/check_schema2.py if the schema changed; all must pass.
7. Do NOT resolve X7 (probe (i) on admitted:span_not_seen, depends on probe-note decision PN-8) or X10 (depends on AL-7): instead make sure each is listed in the template's own open-points section (Section 7) as dependent on that decision, if it is not already.
8. Append a dated entry "Completion pass (27 October 2026)" at the end.
Return what you did, with the new hashes in checks.`, { label: 'draft: template alignment', phase: 'Draft', schema: FIX_SCHEMA }),
])
const [dClaims, dProbe, dTemplate] = drafts
log(`drafts: claims ${dClaims ? 'ok' : 'FAILED'}, probe ${dProbe ? 'ok' : 'FAILED'}, template ${dTemplate ? 'ok' : 'FAILED'}`)

phase('Review')
const reviewBase = `${RULES}
You are an adversarial reviewer. Do not edit any file. Report concrete, checkable findings only, each with file, location, the problem, evidence (quotes with path:line), a proposed fix, and a severity. Do not report style preferences. An empty list is a valid answer.`
const reviews = await parallel([
  () => agent(`${reviewBase}
Review "Rule M: verdicts for the architectural mechanisms" just drafted in ${A}/23-am1-register-claims.md (find it by its heading), and the M-19, C04, C77, C94 updates. Drafter's report: ${JSON.stringify(dClaims?.summary ?? 'missing')}.
LENS: pre-registration integrity. Check against plan 23 (${A}/23-plan-development-and-confirmation.md lines 255-365) and the amendment (${A}/23-plan-amendment-1-ceilings-and-root-cause.md, especially lines 6-16, 104-125, 280-300, 323-378, 400-475): Is any threshold or choice one that the already-read EL2020 family results could have steered, and is that disclosed? Does any verdict still depend on a judgment made after outcomes are open? Is "can't tell" applied in both directions for known defects, with a test fixed now? Is the instrument range defined before outcomes and per series (plan 23 line 361)? Does the rule contradict the mapping's fixed populations/endpoints, the WD rule, the contracts' contrast, the class rules or the bound? Does it overreach (e.g. reintroduce restraint, judge contracts, or claim cross-domain generality)? Does it handle the open C decisions (C27-C44) conditionally and correctly?`, { label: 'review: verdict rule (integrity)', phase: 'Review', schema: FINDINGS }),
  () => agent(`${reviewBase}
Review "Rule M: verdicts for the architectural mechanisms" just drafted in ${A}/23-am1-register-claims.md (find it by its heading). Drafter's report: ${JSON.stringify(dClaims?.summary ?? 'missing')}.
LENS: decidability. Could a script compute exactly one of works / doesn't work / can't tell for every mechanism from registered outputs, with no judgment? Work through edge cases concretely: exact p achievable at 3 vs 3 runs (one-sided, all-ordered = 1/20) and at 5 vs 5 (1/252); ties between arms; a run that crashed (a2_r2 crashed and was replaced by a2_r2b); an empty population (the unknown family, decision C29); RAG with no answer on unasked rows (C33); rows coded unclear or "design or model, not separated"; a family whose endpoint is in rows vs distinct values; the instrument range being zero (EL2020 cycle-1 range was 0, plan 23 line 361); bug incidence measured how. Check every quantity the rule uses exists in the run files or the loss trace (look at ${A}/23-loss-trace.py and a run's artifacts under /Users/wesselvansommeren/Documents/Project-Context-Protocol/data/ami_eval/a1_smoke/ for formats only; do not compute endpoint results). Also check every quote and path:line cite in Rule M against its source.`, { label: 'review: verdict rule (decidability)', phase: 'Review', schema: FINDINGS }),
  () => agent(`${reviewBase}
Review the completion-pass changes in three files (each file ends with a "Completion pass (27 October 2026)" entry listing them):
(a) ${A}/23-am1-probe-note.md: the new section "Owner or role claim on EL2020 (C41, M-17)" — is it mechanical, decidable from recorded claim fields (check the fields exist in a frozen run, e.g. /Users/wesselvansommeren/Documents/Project-Context-Protocol/data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/a1_r2/artifacts/), independent of gold and model calls, faithful to amendment line 293's intent in the WD rule (lines 286-296), and does it avoid reporting any outcome? And the D->PN rename: list any of the probe note's own decisions still named Dn, and any Ch. 4 reference (D1-D11 as design decisions, Dn.pk paragraph ids) wrongly renamed. Use git-free comparisons: the pre-pass text is not saved, so check by reading every \\bD[0-9]+\\b and \\bPN-[0-9]+\\b occurrence in context.
(b) ${A}/23-am1-precoder-template.md: do the step names now match the register's Chain lines (E.1, K1.1, K2.1, S.1, R.1 in ${A}/23-am1-register-design-and-controls.md) verbatim? Does the line-340 / "design or model, not separated" scope now match the register sheets and amendment lines 331 and 340? Is the A1 gloss accurate against register K2.6c? Recompute the prompt and schema SHA-256 with ${S}/verify/pt/hashes.py (copy it to ${S}/complete/review/ if needed) and confirm they equal what Section 1 records. Are PN references correct?
(c) ${A}/23-am1-register-claims.md: the Rule V renaming (every V-number: coder vs rule item correctly classified?), the amendment ranges for the WD rule and 'Already read', the PN references, and the M-17 pointer to the probe-note heading.
Also check that no reference anywhere in ${A}/23-am1-*.md (other than the decision sheet ${A}/23-am1-decisions.md, which is updated later) still points at probe-note decisions as Dn.`, { label: 'review: definition + mechanical fixes', phase: 'Review', schema: FINDINGS }),
])
const [rInt, rDec, rMech] = reviews
const vrFindings = [...(rInt?.findings ?? []).map(f => ({ ...f, id: 'VI-' + f.id })), ...(rDec?.findings ?? []).map(f => ({ ...f, id: 'VD-' + f.id }))]
const mechFindings = (rMech?.findings ?? []).map(f => ({ ...f, id: 'MX-' + f.id }))
log(`findings: verdict rule ${vrFindings.length}, mechanical/definition ${mechFindings.length}`)

phase('Skeptic')
const skepticBase = `${RULES}
You are a skeptic. For each finding below, try hard to refute it by checking the cited sources yourself. survives=false if the finding is wrong, already handled elsewhere in the file, out of scope for Step 0, or its fix would itself break the amendment or another package file. When the finding survives but the proposed fix is not the best one, give better_fix. Do not edit any file.`
const [sVR, sMX] = await parallel([
  () => vrFindings.length ? agent(`${skepticBase}
Findings on Rule M in ${A}/23-am1-register-claims.md:
${JSON.stringify(vrFindings, null, 1)}`, { label: 'skeptic: verdict rule', phase: 'Skeptic', schema: VERDICTS }) : Promise.resolve({ verdicts: [] }),
  () => mechFindings.length ? agent(`${skepticBase}
Findings on the completion pass (probe note definition and rename, template alignment, claims renames):
${JSON.stringify(mechFindings, null, 1)}`, { label: 'skeptic: definition + mechanical', phase: 'Skeptic', schema: VERDICTS }) : Promise.resolve({ verdicts: [] }),
])
const keep = (fs, s) => fs.map(f => ({ f, v: (s?.verdicts ?? []).find(v => v.id === f.id) })).filter(x => !x.v || x.v.survives).map(x => ({ ...x.f, better_fix: x.v?.better_fix ?? '' }))
const killed = (fs, s) => fs.filter(f => (s?.verdicts ?? []).some(v => v.id === f.id && !v.survives)).map(f => ({ id: f.id, reason: (s.verdicts.find(v => v.id === f.id) || {}).reason }))
const survivors = [...keep(vrFindings, sVR), ...keep(mechFindings, sMX)]
const refuted = [...killed(vrFindings, sVR), ...killed(mechFindings, sMX)]
const byFile = (name) => survivors.filter(f => (f.file || '').includes(name))
const claimsFix = byFile('register-claims')
const ptFix = survivors.filter(f => (f.file || '').includes('probe-note') || (f.file || '').includes('precoder-template'))
const otherFix = survivors.filter(f => !claimsFix.includes(f) && !ptFix.includes(f))
log(`surviving: claims ${claimsFix.length}, probe/template ${ptFix.length}, other ${otherFix.length}; refuted ${refuted.length}`)

phase('Fix')
const fixBase = `${RULES}
Apply the surviving review findings below. Use better_fix where given. Where a finding needs an author decision, do not decide it: record it in open_for_author. After editing, re-run the relevant checks and append to the file's "Completion pass (27 October 2026)" entry a short "Review of the completion pass" list: each finding id with applied / not applied and why.`
const [fClaims, fPT] = await parallel([
  () => claimsFix.length ? agent(`${fixBase}
Edit only ${A}/23-am1-register-claims.md. Re-run the quote check (${S}/verify/qcheck_claims.py or the copy under ${S}/complete/).
Findings:
${JSON.stringify(claimsFix, null, 1)}`, { label: 'fix: claims register', phase: 'Fix', schema: FIX_SCHEMA }) : Promise.resolve(null),
  () => ptFix.length ? agent(`${fixBase}
Edit only ${A}/23-am1-probe-note.md and ${A}/23-am1-precoder-template.md. If the template's prompt block changes, recompute and record the prompt and schema SHA-256 with ${S}/verify/pt/hashes.py and re-run vq.py.
Findings:
${JSON.stringify(ptFix, null, 1)}`, { label: 'fix: probe note + template', phase: 'Fix', schema: FIX_SCHEMA }) : Promise.resolve(null),
])

phase('Sheet')
const sheet = await agent(`${RULES}
Task: bring the decision sheet ${A}/23-am1-decisions.md up to date after the completion pass, then re-check cross-package consistency. You may edit only the decision sheet. Report (do not fix) anything wrong in other files.
Inputs:
- Completion-pass reports: claims ${JSON.stringify(dClaims?.summary ?? 'missing')}; probe note ${JSON.stringify(dProbe?.summary ?? 'missing')}; template ${JSON.stringify(dTemplate?.summary ?? 'missing')}.
- Drafters' open points: ${JSON.stringify([...(dClaims?.open_for_author ?? []), ...(dProbe?.open_for_author ?? []), ...(dTemplate?.open_for_author ?? [])])}
- Fixers: ${JSON.stringify({ claims: fClaims && { summary: fClaims.summary, open: fClaims.open_for_author, not_applied: fClaims.not_applied }, probe_template: fPT && { summary: fPT.summary, open: fPT.open_for_author, not_applied: fPT.not_applied } })}
- Surviving findings not routed to a fixer (report them): ${JSON.stringify(otherFix)}
Edits to the sheet:
1. C43: Rule M is now drafted in the claims register (give its heading). Option (a) no longer delays signing; the author signs Rule M with the package or picks (b) (it moves unchanged into a dated note before the Step 3 reveal). Restate the recommendation and what each option changes. Add any open point the Rule M drafter or fixer raised as sub-questions of C43, each with a recommendation, only if it truly needs the author.
2. C41: the definition is now drafted in the probe note under "Owner or role claim on EL2020 (C41, M-17)". The question becomes: sign the definition as drafted (recommended) or revise. List any open point the probe drafter raised.
3. Rename every reference to the probe note's own decisions D1-D14 to PN-1..PN-14 (use the rename table in the probe note's completion-pass entry). Do not rename Ch. 4 design decisions (D1-D11 as design decisions, Dn.pk paragraph ids). Inspect each \\bD[0-9]+\\b occurrence.
4. Add entries for the cross-package findings still open:
   - X6 (line-340 scope): resolved by aligning the template to the register sheets and the amendment's per-step wording: record as class A citing amendment lines 331 and 340, unless the template drafter reported that the sheets contradict the amendment, in which case make it a C entry.
   - X7 (template probe (i) for admitted:span_not_seen depends on PN-8) and X10 (AL-7 and template blindness check 1): add each to C1's pre-tag items as an edit that follows from the named decision.
   - X11 (new entry, class C): the claims register and the template cite working-tree lines of ${A}/22-bug-list.md and plan 23, both modified and uncommitted (they also carry another session's uncommitted work), and amendment line 124 edits bug-list row 11 before Step 2, which would shift lines. Question: how are these citations frozen at the tag? Options: (a) the signing commit includes both files at their cited states (the author must first check the other uncommitted hunks are ready to commit); (b) record each file's SHA-256 in the signing record and keep a byte copy in the off-repository run archive, citing lines at that hash; (c) re-cite each line at a committed version where the same text exists, and use (b) for the rest. Recommendation: (a) if the hunks are ready, else (c). Say what each changes.
   - X13 and X14: note as resolved or open per the completion pass.
5. Refresh the "Files as read for this sheet" table with the current SHA-256 of every listed file (compute them with shasum -a 256 now) and the time; add ${A}/23-am1-run-manifest.py and ${A}/23-am1-design-text.py and ${A}/23-am1-prompts.py if absent. Update the counts line (C, B, A) to the real counts.
6. Make sure C2 (V4 coder and due date) states the audit-list size: 430 decisions now (dfef6f31…), 474 under C18 (b), 481 under C18 (b) plus C20 a_shared (compute: the audit script's docstring or JSON says what each option adds; do not run it in place, run a copy in ${S}/complete/ if you need to).
7. Re-run the sheet's quote check (${S}/verify/decisions/qcheck.py; read it first) and fix any error.
Then the consistency check, reporting only: (i) every Cn/Bn/An/R-/M-/AL-/PN-/decision-n id cited anywhere in ${A}/23-am1-*.md resolves; (ii) \`python3 -I ${A}/23-am1-check-register.py\` exits 0 with 0 errors; (iii) the template's recorded prompt and schema hashes recompute (${S}/verify/pt/hashes.py); (iv) the amendment still hashes 0236ef0385b96012d08e7bcd10a8ec71e436253cb58948d85da4ba563fb81889; (v) no leftover probe-note Dn reference in any package file. Put the results in checks.`, { label: 'sheet + consistency', phase: 'Sheet', schema: FIX_SCHEMA })

return {
  drafts: { claims: dClaims, probe: dProbe, template: dTemplate },
  reviews: { integrity: rInt, decidability: rDec, mechanical: rMech },
  refuted, survivors_routed: { claims: claimsFix.map(f => f.id), probe_template: ptFix.map(f => f.id), other: otherFix },
  fixes: { claims: fClaims, probe_template: fPT },
  sheet,
}
