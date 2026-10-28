# Plan 23, amendment 1: decision sheet for signing (Step 0)

Dated 27 October 2026; brought up to date after the completion pass, its review and the second review, the same day (record at the end). Status: **draft, for signing with the amendment.**

## What this sheet is

- It lists every open decision of the Step 0 package once. Where several files raise the same question, one entry names every source.
- Its sources:
  - the amendment's own "Decisions needed from you" (lines 603–617);
  - the decision lists of the design-and-controls register (decisions 1–17), the claims register (R-1 to R-22), the mechanism mapping (M-1 to M-21), the audit-list script (AL-1, AL-2, AL-3, AL-5, AL-7), the probe note (PN-1 to PN-14, and its proposals P6 and P11–P13) and the pre-coder template (points 1–24), as the files stand after the completion pass of 27 October, its review and the second review;
  - Rule M (claims mapping section 7a) and its listed choices (C43), and the probe note's section "Owner or role claim on EL2020 (C41, M-17)" and its choices (C41), both drafted in the completion pass;
  - the open points of the completion pass and its review (C28, C29, C30, C38, C41, C43, C44, C62, B26);
  - the cross-package check of 27 October, findings X1 to X14 (where each stands: section X);
  - two builder gaps that need a choice (C61, B8).
- Each entry has one class:
  - **C, your call.** It changes what is coded, claimed, admitted or written in the thesis; or it adds a rule or threshold the amendment does not contain; or it decides what can ground a design code; or it is one of the amendment's own signing decisions. Each entry gives the question, the options, a recommendation, and what each option changes.
  - **B, operational default.** A choice of procedure that cannot push a result in a known direction. The reason is given. The stated choice is adopted unless you object.
  - **A, settled by the amendment.** The amendment's text answers it. The lines are cited. No choice remains.
- **Signing the package adopts every A and B entry as written, and your answer to every C entry; a C entry you do not answer otherwise adopts its recommendation, except the entries listed in the subsection How to sign, below.** C entries marked *not needed for signing* may stay open.
- Where a builder's recommendation conflicts with the amendment or with another package file, the entry says so under **Correction**.

### How to sign

- Signing adopts every A and B entry as written, and the recommendation of every C entry you do not answer otherwise. Leaving open an entry marked *not needed for signing* (C3, C5, C6, C7) is such an answer.
- Except: the entries below need a fact or a preference that only you have. Their recommendation is not adopted by default; answer each yourself. C3 and C6 are not needed for signing and are answered by the point each entry names.
  - C1: signing is your consent; confirm that every pre-tag item is done.
  - C2: answered, machine V4 (Gemini in Antigravity). Still needed: the packet salt (B24), fixed at signing.
  - C3 (before the Step 0 plan-23 fixes): your go-ahead for about $20 against plan 23's budget (lines 582, 598, 601).
  - C4: whether the records are archived (line 63), and, if they are, the scan for secrets that the recommendation asks for first.
  - C6 (each decision before any score under it, line 137): the B3 gold decisions, which include the three author-confirmed corrections (line 140) and sending the V5 packet (line 147).
  - C25: under (a), your go-ahead for a higher Step 2b spend, (d) at its maximum of about $16.
  - C63: whether the other session's uncommitted hunks in plan 23 and `22-bug-list.md` are ready to commit (option (a)).
- **Moved to Phase F (author, 27 October):** all thesis rewriting happens once, at the end (plan 23, Phase F, item 1, as changed that day). The wording entries C43.3, C48, C50, C53, C55 and C56 are therefore *not needed for signing* and are answered in Phase F. The timing entries C46 and C47 keep their decisions but apply them in Phase F (their answers below).
- **Answered by the author (27 October):** C1, C4, C25 and C63, each with its recommendation. On 28 October, C67 with its recommendation (a). C2 is answered with a machine V4, Gemini, due seven days after the 3a pages and sub-cause list are frozen (its entry). Each entry's answer line says what remains before the tag.
- Recommendations to read before accepting: C64, C65 and C66. They come from the review round on draft 6 (28 October) and are already applied in the amendment and the template; answering otherwise means editing them back.

### Conventions and the files read

**Conventions.**
- *line N* is a line of `23-plan-amendment-1-ceilings-and-root-cause.md` (the amendment), which is final.
- *register* is `23-am1-register-design-and-controls.md`; *claims* is `23-am1-register-claims.md`; *mapping* is claims section 9; *Rule M* is mapping section 7a; *probe note* is `23-am1-probe-note.md`; *template* is `23-am1-precoder-template.md`; *audit script* is `23-am1-audit-list.py`.
- *PN-n* is the probe note's decision n. Its completion pass renamed D1–D14 to PN-1 to PN-14, because line 6 reserves "D1"–"D11" for the Ch. 4 decisions. A *Dn* or *Dn.pk* in this sheet is a Ch. 4 decision or one of its paragraphs.
- Text in quotation marks is verbatim. Everything else is this sheet's wording.

**Files as read for this sheet** (refreshed 28 October 2026 after the pre-tag pass; first 27 October 2026, 17:11 CET, after the completion pass, its review and the second review; the claims register and probe note rows updated after the main session's sync edits of the same evening). Their hashes change when your answers are applied; the tag records the final ones (C1, B25). The template's prompt and schema hashes are recorded in its Section 1 (prompt fd7e2f6b…0c8bb4 since 27 October, late evening; schema e790d1a6…fbd96d) and recompute from its text.

| File | SHA-256 |
|---|---|
| amendment | b9c8c50b1f9b202d01a886670ba17c2788306ea26598b656ba34224a5e2dbef4 |
| `23-am1-register-design-and-controls.md` | 9c7af4e0f7a96103ecc0fb423236a64e21559bad7a6f1b2c2f44cb28a3a8e0da |
| `23-am1-register-claims.md` | a3d77cd94466b6c366a57001d669c525c71974d486168950571bb3339098ea1c |
| `23-am1-probe-note.md` | 056dda5a96e30b6108d3eb64169a35bb1a116717688cdf3b8728c417ed8d0e07 |
| `23-am1-precoder-template.md` | 71ba1072dcc014617d67c53eb123e0bfd34ceb998f70b4e3a007dc62e22931da |
| `23-am1-audit-list.py` | e81946e65a66a69ec49beaaade249828d77990d70bfbd40f1758fbb8ee56188f |
| `23-am1-audit-list.json` | 493bc6e931f3a59af9e5f5ade4c24802dbc483083ecc22884a4e50c3093c9bcf |
| `23-am1-design-text-94c049d.md` | b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759 |
| `23-am1-design-text.py` | 84cdd77e726d7813b810505965023797c777d94f0897fb13edf6baebc6e3707b |
| `23-am1-prompts-evaluated.md` | b02a7f70494ec5c447bc77f0bc39d84c2915c9df6bfd09a2b4489b2412e295cf |
| `23-am1-prompts.py` | c26e6170418f2eb7ae4dcfda040bde0886afdeac903d035ec402964f4a1ba3a6 |
| `23-am1-check-register.py` | 794743e3b5b8c7c2f2f5d3de81a3da77207c5cf6ef68d88e959a0b71db1d7bb9 |
| `23-am1-run-manifest.py` | c1d8d2f525c702bfa6aa960161c62e22b967e73dd9c6e4133b46e6d20f1fc743 |
| `23-am1-v4.py` | 1d550b32813435025996eb1ddaabee21668cb8c6b7179ab2b89ca784aed513f9 |
| `23-am1-precoder-extract.md` | 09036929cd59dc0eb37ba14c3f3f068c9825177a0ee0b0210a95ce51399b4d78 |
| `23-am1-precoder-extract.py` | 2b1a0d29cb9c8015814698515bcae2b193126e5f1e8755ef8ab614a0dfcf4f2a |
| `23-am1-check-package.py` | dd08cb8b07b04e026abe75ab18b536c6eec418761a260ec0086cd1f8d02650bc |
| `23-am1-author-tasks.md` | 78b32be0633f42e8ebc326795b951cda98edadb1a090d2def4edc15b09222ee1 |

The run manifest is the table at lines 75–90, committed with the amendment. The run archive that `23-am1-run-manifest.py --zip` writes is recorded with its SHA-256 at the tag (C1; line 93). Neither is listed here.

**Counts.** C: 67 (C64 to C67 added on 28 October, from the review round on draft 6). B: 26. A: 21. C43 has three sub-questions (C43.1 to C43.3), which are answered with it.

---

## C. Your decisions

### The amendment's own decisions

**C1. Sign the amendment with this package** (amendment decision 1).
- Question: Do you sign the amendment with its Step 0 registers, notes, template and audit list, as changed by your answers below?
- Options: (a) sign once the pre-tag items below are done; (b) revise the package first.
- Recommendation: (a). Line 14 requires the tag "before any Step 2, 2b or 2c output exists". After signing, changes need a dated note (line 16).
- Pre-tag items:
  - your answers to C2, C4 and C8–C67, except the entries moved to Phase F (How to sign);
  - every package edit or check that an entry of this sheet places before signing, at signing or with the package, among them: the register's decision pointers resolved in the sheets (B22) and its sentence tags applied (C8); template check 6 and the prompt text it governs limited to C and B sentences, with new hashes (C8, Correction 2, under (a)); the E.2/K2.2 tag alignment of D4.p5 (C17); the coldstart check of B8; the audit list re-run with your AL-1 and AL-3 choices (C18, C20); the pre-coder extract built and filled in, the schema value of B18 added, and the template hashes recorded (B21); new §1.4 text, overlap check and probe-note hashes if C21 takes (b), (c) or (ii); Rule M (claims mapping section 7a), drafted, with its review fixes applied, if C43 takes option (a); the probe note's owner-claim section revised if C41 changes any of its choices; sheet K2, template A5 and the schema if C62 takes option (b); the citations of C63;
  - already done, in the template's second review (27 October): the two template edits that follow from entries already answered here (cross-package findings X7 and X10). Nothing is left to do for them at signing:
    - X7: template table C2 also excepts `admitted:span_not_seen` cases from probe (i), since A11 (PN-8) lists them apart with no probe output. The prompt hash changed; the schema hash did not (template Section 7, point 22, marked done);
    - X10: template blindness check 1 names `23-am1-audit-list.json` among the files that fail, as B25 adopts. No hash changed (template Section 7, point 23, marked done);
  - the line pointers between package files checked again after the last edit. The probe note now cites M-17 by heading (claims section 9, mapping section 8; probe note:358), so that pointer needs no line check;
  - the check scripts committed (B3);
  - the hashes and the V4 packet salt recorded in the signing commit message and the tag annotation (B24, B25);
  - the run manifest and the run archive with its SHA-256 (lines 75, 93).
  - **Status on 28 October:** done, each with its recommendation: B22, C8 and C17 (register sheets and tags), C62 (b) (sheet K2, template A5 and schema), C8's Correction 2 (template check 6 and the prompt), B18 (schema), B21 (extract built by the committed `23-am1-precoder-extract.py`, filled in, hashes in template Section 1), C18 (b) and C20 a_shared (audit list re-run: 479 decisions), B8 (all twelve runs: fallback_count 0 under strict_live), B3 (`23-am1-check-package.py`), C4 (records archived). C21 (a)(i), C41 (a), C43 (a) and C63 (a) needed no further edit. Left for the tag: the V4 packet salt and the hashes, in the signing record.
- Changes: (a) the tag holds the whole package; (b) delays the tag, and no Step 2 output may exist before it (line 14).
- **Answer (author, 27 October): (a).** Consent to sign once the pre-tag items are done. They are not all done yet: the V4 packet salt, C4's scan for secrets and archiving, and the package edits and checks above are still open. The tag is made only when every one is.

**C2. The V4 second coder and the due date** (amendment decision 2; line 116).
- Question: Who is V4, and by what date are their blind codes due?
- Options: (a) name V4 and a date; (b) no V4, so the fallback of lines 432–437 applies from the start.
- Recommendation (superseded by the answer below): (a). Size the date to about 120–170 cases plus the audit list, which draft 5's line 583 put at about 420 audit decisions (2–3 h). The list's size depends on C18 and C20:
  - 430 decisions now (`23-am1-audit-list.json`, SHA-256 dfef6f31…49436, no option adopted);
  - 474 under C18 (b);
  - 479 under C18 (b) with C20 a_shared, the recommended pair. a_shared adds 7 decisions to the list as it stands, but 2 of them (on F25) are among C18 (b)'s 44, so it adds 5 here;
  - for the other pairs: 437 under C18 (a) with a_shared, 452 under C18 (b′) with a_shared, and up to 530 under C18 (b) with C20 b_all.
  - The counts come from the JSON's `open_decisions` and were checked on 27 October 2026 by running a copy of the audit script with each option set, outside the repository. The list in the repository was not rewritten.
- Changes: if the codes are late or absent, Step 4(b) is skipped, the oracles stay on v1, and only conformance repairs proceed among the repairs (lines 432–437).
- **Answer (author, 27 October, evening): a machine V4,** a new option beyond (a) and (b). No human second coder is available, and coding these pages needs PhD-level knowledge of the system. V4 is a Google Gemini model run as an agent in Google Antigravity, one new conversation per packet, on a clean workspace outside the repository; Gemini is neither the pre-coder's family (Claude) nor the system's (GPT). Amendment draft 6 records this at lines 116, 405–407, 430, 432, 583 and 612, with no line moved. The review round of 28 October changed lines 116, 405–407, 411, 414, 419, 430, 432, 572 and 583, again in place:
  - V4 codes all 180 cases, after a channel trial on the 20 pilot cases (line 407), and starts only after pass 1 is committed (line 405; C67);
  - the known-answer set of 27 October is dropped (C64);
  - V4 does not re-code at item 8 (line 414; C65);
  - the copy check switches nothing, and the 0.40 rule takes the lower of the author's two blind bounds (line 430; C66).

  The procedure is template Section 9 and `23-am1-v4.py`. **Due date (author, 27 October): seven days after the commit that freezes both the 3a case pages and the sub-cause list (order of work, items 1 and 2), whichever of the two is committed later.** **Changed by the author on 28 October (C67 (a)): the seven days start at item 4's commit,** because V4 cannot start before item 4 is committed. That commit's date is stated in a dated note, which fixes the calendar date. The work is about 4–8 h of staging, running and collecting (amendment line 583).

**C3. Step 2c (WD): yes or no** (amendment decision 5; lines 283–297). Not needed for signing; needed before the Step 0 plan-23 fixes (line 125, before Step 2).
- Question: Is Step 2c (WD) run?
- Options: (a) yes, about $20 (line 582), on its own estimate and go-ahead; (b) no.
- Recommendation: (a). `carried:claims_without_the_value` is the largest extraction sub-cause (line 285). Without 2c, "Cases whose only named remedy is WD are coded unclear." (line 297)
- Changes: (a) WD can be admitted, and criterion (iv) can code those cases (line 352); spend reaches about $99–115 against plan 23's $60–100 (line 598). (b) WD leaves Phase C, P23:264 is withdrawn, and the cases stay unclear (lines 297, 356). They then weaken every family their rows belong to (mapping section 6.2).

**C4. Archive the review and verification records** (amendment decision 7; lines 58–63). Line 63: "Whether they are archived in the repository is a decision for signing."
- Question: Are the review and verification records archived in the repository?
- Options: (a) archive the ten records named under "Already read", with their hashes; (b) as (a), plus the Step 0 build and review records of 27 October (review workflow am1-step0-verify), and the records of the completion pass and its review the same day, which the package files cite; (c) do not archive.
- Recommendation: (b), after a scan for secrets. The transcripts carry session attachments, such as the memory index (template, R4).
- Changes: (a) and (b) make the "Already read" list checkable from the repository; (c) leaves it resting on records outside it.
- **Answer (author, 27 October): (b).** The records are archived after the scan for secrets. The scan and the archiving are pre-tag items. **Done 28 October:** no secret was found; each record's script and journal are in `23-am1-records/` (its README lists them with hashes), and the full transcripts are zipped outside the repository with their SHA-256 (`data/ami_eval/a1_smoke/archive/plan23-am1-workflow-records.zip`).

**C5. The open conflict decision for the autonomous arm** (amendment decision 6). Not needed for signing.
- Question: When is the open conflict decision for the autonomous arm taken?
- Options: (a) take it now; (b) take it later, before Step 5 if the conflict contract is admitted (line 534).
- Recommendation: (b). Line 360: "Signing the open decision later does not reclassify losses observed before it." So taking it now changes no Phase C code of the frozen runs.
- Changes: none for the codes of the frozen runs under either option. While it is open, every A2 contract is expected to come out *can't tell* (C40).

**C6. The B3 gold decisions, P1-8 first** (amendment decision 3; lines 137–148). Not needed for signing; each is due before any score under it (line 137).
- Question: Which B3 gold decisions are taken, and in what order?
- Options: per decision, as listed at lines 138–147.
- Recommendation: start with P1-8, as the amendment orders.
- Changes: gold and scores for every arm and for RAG, reported under the old and the new gold (line 137).

**C7. The ES2009 adapter choices** (amendment decision 4; lines 166–171). Not needed for signing; due before any ES2009 adjudication (line 166).
- Question: Are the ES2009 adapter choices of lines 167–171 confirmed?
- Options: (a) confirm the choices listed at lines 167–171; (b) change them.
- Recommendation: (a).
- Changes: the ES2009 loss trace used by Step 3b and Step 5.

### What can ground a code (design-and-controls register)

**C8. Which 94c049d sentences may ground architectural weakness or a trade-off.** Sources: register decision 2, with its note on D4.p4; claims R-4; claims section 10, "Observed, not changed" (C22, C142); the register sheets' lists of quotable text; template validation check 6.
- Question: May a 94c049d sentence that discloses a shortfall (tagged L in the register) ground architectural weakness or a trade-off?
- Options: (a) no: such sentences are disclosed implementation limitations; (b) yes, like any 94c049d text; (c) case by case on the page.
- Recommendation: (a) for sentences that state a shortfall: the L-tagged sentences, R-4's list, and D4.p4's sentence that matching does not establish equivalence (now in K2.4). Sentences that state a deliberate choice with its benefit (B tags) may ground a trade-off; commitments (C tags) may ground architectural weakness. Settle it before signing, because it decides codes.
- Changes:
  - (a) closes the design routes of the rows that rest on L sentences: C22 and C142 (D2.p4's window sentence), C85 (D5.p5), and R-4's rows (C05, C25, C32, C33, C41, C68, C85, C98, C120, C143).
  - (b) lets a documented gap ground an architectural code for a behaviour that Phase B classed as a bug.
  - (c) leaves the ground to each page, which is harder to check and to agree on.
- Correction 1. Register decision 2 (a) says "A loss resting on one is an implementation defect". Under line 325, implementation defect needs conformance or an alternative that counts. So, under (a), such a loss is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.
- Correction 2. Template check 6 tests a quote against the whole paragraph of a listed id. But the tags are per sentence: D2.p4 is listed under C on sheet E, while its window sentence is tagged L (register E.2); D6.p4 and D7.p5 are listed under B on sheet S and carry L sentences. Under (a), the extract carries the sentence tags, and check 6 accepts a quote only from a C sentence (architectural weakness) or a B sentence (trade-off). WD cases keep D4.p5 whole (line 355; C17). This changes the template hash.
- Signing this entry also adopts the sheets' C and B lists. They were added at the merge of 27 October (register, Limits, "From the merge").

**C9. Is D5.p3's equal-time eligibility in R-4's list?** Source: claims R-22.
- Question: Does D5.p3's equal-time eligibility belong in R-4's list of 94c049d sentences that describe a later-found bug?
- Options: (a) remove it from R-4's list; D5.p3 stays a design entry, as on sheet S; (b) keep R-4 as written, and change sheet S and rows C17, C98 and C120 to match.
- Recommendation: (a). Bug 3 is that "the current value's own claims never compete" (`3320375:thesis/notes/thesis_completion/artifacts/22-bug-list.md:43`). What it contradicts is the 5de9911 sentence (same file, line 47), not D5.p3.
- Changes: (a) D5.p3 may ground architectural weakness on sheet S, and C120 keeps its route to confirmation. (b) D5.p3's eligibility becomes an implementation gap, and C120 loses its only route to confirmation.

**C10. The A1 rule for bug 3.** Source: register decision 4 (updated at review).
- Question: Is A1's rule (the current value's own claims compete; an exact tie keeps the current value) a design entry or an implementation entry?
- Options: (a) an implementation entry consistent with D5.p3; (b) retrospective design.
- Recommendation: (b). Its wording rests on the 5de9911 sentence of 19 October. The readings that call it the Ch. 4 rule are later still (plan 23 at b4d6b6c, line 118; the bug list at 3320375, line 170). Line 104 makes "any design text written or signed after 9 September" retrospective. D9.p4's "Scalar resolution considers all claims for a concept" sits in a disclosed limitation (C8). It does not by itself rank the current value's claims against challengers.
- Changes: (b) an A1 state-rule loss whose only design ground is this rule is implementation choice if an alternative consistent with 94c049d meets (i)–(iv), and unclear otherwise; it is tallied in the retrospective column (lines 348–349). (a) such a loss is coded against D5.p3, so a design code becomes possible.

**C11. Bug 5's design ground.** Source: register decision 3.
- Question: Is filing under an undefined key grounded in 94c049d D4.p3, or in D10's wording of 19 October, which the bug list quotes?
- Options: (a) D4.p3: claims enter ordinary state resolution only after concept acceptance or merging, so filing under an undefined key contradicts the register; (b) retrospective (D10).
- Recommendation: (a), and record that the bug list quoted D10.
- Changes: (a) bug 5 is a conformance defect, and its repair (`repair_undefined_key_filing`) a conformance repair. (b) a case resting on it has only a retrospective ground (line 348). For A0, line 309 applies either way (A21).

**C12. D4.p3's matching inputs on the hint path.** Source: register decision 1.
- Question: Do D4.p3's matching inputs apply to the extractor's key hint as well as to the resolver?
- Options: (a) yes, so criterion (ii) can apply to hint-routed cases; (b) no: the hint path has no design inputs.
- Recommendation: (a). D4.p3 describes one matching step without naming a path, and both code paths perform it.
- Changes: (a) a hint prompt that omits a D4.p3 input (sheet K1) can make an alternative count under "the prompt omits information the register gives that step" (line 325). (b) hint-routed cases count only under (i), (iii) or conformance.

**C13. What D4.p3's "values" means.** Source: register decision 17 (new at review).
- Question: In "existing concepts' descriptions, aliases, values, and question examples" (D4.p3), which values are meant?
- Options: (a) the concept definition's canonical values; (b) the values a key holds; (c) both.
- Recommendation: (a). The 94c049d matcher scored definition fields, canonical values included (`94c049d:app/services/state_key_resolution_service.py:651-661`, `:753`). D8.p3 uses a separate term, "observed values", for held values.
- Changes: neither the resolver nor the hint prompt shows either kind, so the omission holds under every reading. (a) the omitted input is empty in these runs, because the harness clears canonical values on accept (register K2.6c), and a page names that clearing. (b) and (c) the input is not empty, and a page names the prompts' line formats (K2.6a, E.6).

**C14. Criterion (ii) and retrospective entries.** Source: register decision 15.
- Question: Does criterion (ii) compare a prompt with the retrospective register entries for its step too?
- Options: (a) yes; the alternative must still be consistent with the 94c049d text (line 348); (b) only with 94c049d entries.
- Recommendation: (a). Line 347: "A retrospective entry can never ground architectural weakness or a trade-off, nor rule out an alternative." It does not bar such an entry from showing that a contract's prompt omits what the contract was built to check.
- Changes: (a) for A2's support check and for rendering (D11), whose only specification is retrospective, an omission such as the meeting missing from the support-check prompt (sheet S) can count. (b) it cannot, and such cases go to the other criteria or to unclear.

**C15. Harness-side code that decides which proposals become keys and facts.** Source: register decision 5.
- Question: Is harness-side code that decides which proposals become keys and facts an implementation entry, or part of the evaluation?
- Options: (a) list the concept reviewer, the value confirmation (`_internal_confirm_structural`, `_confirmable_value`) and the A1 settle as implementation entries marked harness; keep the judge as a held-constant control, and the bug-7 wrapper as an instrument repair; (b) move the value confirmation and the judge wrapper to the evaluation side (evaluation defect).
- Recommendation: (a). Line 107 already names the harness reviewer an implementation entry, and the confirmation and the settle decide which proposals become facts in the same way.
- Changes: (a) losses resting on them can be implementation defects, and repairable. (b) they become evaluation defects, which change no gold, suite or score within this study (line 319).

**C16. Implementation entries that the candidate-cause list does not name.** Source: register decision 13.
- Question: How do five implementation entries that the candidate-cause list does not name enter the sheets and the causes?
- The entries: (i) the alias-substring merge; (ii) `_KEY_SHAPE` against the validator, which leaves parked claims never released; (iii) AMI-specific stopword constants in value confirmation and reading; (iv) re-extraction of zero-claim spans with a larger registry; (v) write-path resolver calls at meeting a against an empty registry.
- Options: (a) record all five; map (i) to "a reuse or similarity threshold merged a new matter into an existing key" (line 386) and (iv) to "registry-conditioned extraction" (line 384); leave (ii), (iii) and (v) to the pilot, which "may add new ones, but may not split or merge these" (line 380); (b) record them, and let the pilot map all; (c) map all now.
- Recommendation: (a). Note on (i): it is a substring rule, active whenever expansion reuse is not disabled. The code describes it as testing "would an existing key's alias have matched at a looser" threshold (`3320375:app/services/registry_expansion_service.py:124`). Mapping it reads it as a reuse rule under criterion (iii).
- Changes: (a) cases resting on (i) or (iv) take a listed cause, so they can count toward a Step 4(b) cause's 3 values (line 480). (b) the pilot decides. (c) adds or assigns causes before the pilot.

**C17. "D4's scalar-concept passage"** (line 355). Source: template point 9.
- Question: Which 94c049d paragraph is "D4's scalar-concept passage" (line 355)?
- Options: (a) D4.p5; (b) D4.p5 and D4.p6, which gives the rationale for the scalar preference.
- Recommendation: (a). D4.p5 states the preference ("The September defaults favour scalar concept generation"). D4.p6's sentences are tagged B, E and L in the register; none is a commitment.
- Changes: it fixes the only design ground a WD case can take (line 355; template check 6). (b) adds D4.p6's rationale and cost sentences.
- Note: register E.2 tags D4.p5's scalar sentence B, while K2.2 tags it C. Line 355 governs WD cases either way; align the tags at signing.

### The audit list

**C18. Carrier decisions on A0/A1 rows lost at polarity or modality.** Source: AL-1.
- Question: Do the 44 v1 carrier decisions on A0/A1 rows lost at polarity or modality join the audit list?
- Options: (a) keep line 115's enumeration, and disclose that E+R, E+R\* and the line-373 exceptions on these rows rest on unaudited v1 decisions; (b) add all 44 (role `e_wrong_form_carrier`), and three listed decisions (F30, F38 twice) gain the role; (b′) add only the 15 on ruled-out or negated-value rows.
- Recommendation: (b). Line 115's criterion is "every v1 decision that decides an oracle row result", and line 206 names "any remaining wrong-modality carriers and positive carriers of ruled-out values" as losses under E+R\*.
- Changes: (b) the list grows from 430 to 474 (479 with C20's recommendation), above the about 420 audit decisions that draft 5's line 583 planned, and v2 can change these rows (line 95). (a) v2 equals v1 on them.

**C19. Rival decisions on successor values.** Source: AL-2 (applied by the fixer; for confirmation).
- Question: Do you confirm that r_rival also takes the successor values of A0/A1 rows lost at state maintenance?
- Options: (a) confirm: r_rival also takes the successor values of A0/A1 rows lost at state maintenance (4 decisions, two on F01 and two on F06, 17 rows; one listed decision on F62 gains the role); (b) revert to rivals from wording pairs only, and disclose the gap.
- Recommendation: (a). R removes non-carriers from the gold key (line 214), so a rival's decision decides R. On 6 rows the decision also sets the recorded loss.
- Changes: (a) 430 decisions (16 with role r_rival; 6 with two roles); (b) 426, and R's removal of successor values rests on unaudited v1 decisions.

**C20. Carrier decisions on A0/A1 rows that passed or were lost at reading.** Source: AL-3.
- Question: Do the 56 v1 carrier decisions on A0/A1 rows that passed or were lost at reading join the audit list?
- Options: (a) keep the exclusion, and disclose that the v2 figures are biased toward recovery; (a_shared) as (a), plus the shared-key carriers: 5 F36 decisions, and 2 F25 decisions if C18 is not (b); (b_sole) a_shared plus the 27 sole-carrier decisions; (b_all) a_shared plus all 56.
- Recommendation: a_shared, with the disclosure. The F36 decisions decide R on lost rows of F59, which shares F36's gold key (line 203). Other pass carriers set no caused-at boundary (line 368).
- Changes: a_shared adds 5 to 7 decisions. The b options add up to 56 more and let the audit turn passes into losses. (a) leaves F59's R result on lost rows (44a72348 F59@2, f03636da F59@3) on unaudited decisions.

### The probes

**C21. The neutral text for (b2).** Source: probe note PN-2, both items.
- Question: Which neutral text replaces the AMI role examples in condition (b2)?
- Options: (a) domain-general support roles with the verbs kept, as drafted (probe note §1.4); (b) one concrete third domain; (c) also replace the verbs. Second item: (i) keep 'Facilities Coordinator' and 'Vehicle Fleet Specialist', and disclose their office and logistics functions; (ii) replace them.
- Recommendation: (a) and (i). The lexical check is clean, no EL2020 gold value is about these functions, and the instruction to ignore logistics is the same in every condition.
- Changes: the text fixes what a (b2) result can show under line 272. (b) adds a new out-of-domain bias. (c) changes phrasing too, so (b2) tests more than the examples. (ii) needs a new overlap check and new hashes before signing.

**C22. The (b) registry cut with no embedding candidate.** Source: probe note PN-5, all three items.
- Question: What does the (b) cut keep when no key reaches the similarity floor, and which other branches of `_prompt_registry` apply?
- Options: no candidate: (a) keep the whole registry, as the code's no-candidate branch does, so (b) equals (a); (b) an empty registry, so (b) equals (c). The branch for registries of 12 keys or fewer follows the same reading. Intent-primary keep: (i) drop it; (ii) keep it at the claim path's fixed intent.
- Recommendation: (a) and (i). Line 243 removes only "the lexical part of `_prompt_registry`", so the rest of the function applies.
- Changes: under (a), a no-candidate case can recover only through (b2), and a (c)-only recovery stays unclear (line 278), so it cannot support a Step 4(b) repair. Under (b), the same case is an implementation choice (line 272). The 12-key branch and the intent keep change nothing on EL2020 (probe note P5); they may on the 3b run. List the no-candidate cases.

**C23. When a probe output passes.** Source: probe note PN-9.
- Question: When does a probe output pass at the case's boundary?
- Options: (a) it passes every extraction step up to and including the case's step; strong matches count, other candidate texts are adjudicated; (b) the case's step alone; (c) the strict bound only.
- Recommendation: (a). It scores the case at its own step (line 301), within its boundary (line 237).
- Changes: (b) is more lenient: an output can pass while failing an earlier step, so more recoveries. (c) gives fewer, and drops the adjudication batch file that line 237 requires.

**C24. A (d) output after the client shed a parameter.** Source: probe note PN-13.
- Question: Does a (d) output count when the client shed a parameter?
- Options: (a) it counts, listed with the shed parameter; (b) it is excluded.
- Recommendation: (a). It is gpt-5.4 at the settings it accepts, and the bug-7 record suggests nothing will be shed.
- Changes: (b) turns such outputs into no output, so fewer cases can be model-limited (line 279) and more stay unclear.

**C25. The cost of (d), and the blindness of its case list.** Source: probe note PN-14 (with P9, P13).
- Question: How is the cost of (d) covered without showing the size of its sealed case list before the reveal?
- Options: (a) the Step 2b go-ahead covers (d) at its maximum, about $16 (about $14 under B11), so no count of the sealed list is shown before Step 3 item 7; (b) the probe script stops at a fixed spend ceiling, and a stop is logged as an early read (line 411).
- Recommendation: (a). If the study budget guard is used, its cap covers this maximum (probe note P13).
- Changes: (a) raises Step 2b's estimate of about $24–37 (line 581) by about $5–11; with Step 2c the total may pass plan 23's $100, which needs its own go-ahead (lines 596–601). (b) a stop leaves (d) incomplete, so fewer cases can be model-limited, and it is an early read.
- **Answer (author, 27 October): (a).** Step 2b's go-ahead will cover (d) at its maximum of about $16. This does not start Step 2b: that step still needs its own estimate and go-ahead (line 233). Going past plan 23's $100 also still needs its own go-ahead.

### The pre-coder

**C26. The pre-coder model.** Source: template point 1 (R5).
- Question: Which model pre-codes the cases?
- Options: (a) `claude-opus-5-5`, the model of the v1 loss-trace adjudications; (b) another Claude model.
- Recommendation: (a). Disclose that the surfacing steps (v1) and the pre-codes come from one model, and record the served model per call.
- Changes: the pre-codes are A0's only codes (lines 309, 459) and feed the candidate causes (line 406) and the copy check (line 430). Under (a) their errors may correlate with v1's; (b) avoids that.

**C27. Runs shown for recoverability.** Source: template point 14 (widened at review).
- Question: Which runs does a case page show for recoverability?
- Options: (a) "the value's first loss in every other run of its arm group" only (line 395); (b) every ProjectMemory run, labelled by arm group, with its step, sub-code and checkpoint, and whether the value passed the case's step at the case's checkpoint.
- Recommendation: (b), as the template is written. The other-run bar still uses the arm group only (line 364).
- Changes: (b) lets the coder apply line 365 ("A value every run of both systems misses") from the page; coders also see runs outside the arm group, which may lower conversational-difficulty codes beyond line 364's bar. Under (a), the validator sets the line-365 flag from the frozen trace, and template parts A4 and E8 change.

### The mechanism mapping

The mapping governs every Phase C verdict (line 114), so each of its open choices is yours.

**C28. The endpoint of complete decisions.** Source: M-3.
- Question: Which endpoint judges complete decisions?
- Options: (a) the `current_state` family (58 questions, 60 rows); (b) the `current_state` questions whose gold value has two or more parts, classified from the gold text alone; (c) no architectural verdict, only the WD contrast.
- Recommendation: (a). Disclose that it measures the whole chain for current values.
- Changes: (b) needs a new classification after the EL2020 results were read. It is committed with the package or, if Rule M is not signed with it (C43 (b) or (c)), before any Step 2, 2b or 2c output exists, and is disclosed as made after those results were read (Rule M item 2). (c) leaves complete decisions without a verdict against RAG; WD's Step 2c rule is then their only test.

**C29. The unknown family.** Source: M-4.
- Question: Does the unknown family map to a mechanism?
- Options: (a) no mechanism, following plan 23:116 (restraint, removed at line 122); (b) epistemic status (D3.p5).
- Recommendation: (a). It has no gold rows, so no case can bound it either way.
- Changes: (b) adds the unknown family's 10 questions to epistemic status's endpoint against RAG (17 questions). It would be chosen after the unknown family's EL2020 outcomes were read (`23-el2020-arms.md:33`), and those questions cannot be bounded (Rule M item 7); M-4 and Rule M item 2 disclose this.

**C30. The endpoint of change and supersession.** Source: M-5.
- Question: What is the endpoint of change and supersession?
- Options: (a) `change_over_time` only (3 questions, 24 rows); (b) add the 8 persist items; (c) add a ProjectMemory-only state endpoint (demoted rows no longer current, successor rows stored).
- Recommendation: (a), with (c) reported beside it and outside the verdict.
- Changes: (b) moves items between families after their outcomes were read. (c) inside the verdict would have no RAG counterpart: Rule M then needs a rule for it, fixed with Rule M, or the state endpoint is reported beside the family verdict and enters none (Rule M item 7, choice 14). The same holds for C33 (c).

**C31. Verdict membership by rows.** Source: M-6.
- Question: Is verdict membership decided by rows, with boundaries and sub-causes used only for the account?
- Options: (a) Rule V by rows for verdicts, and Rule A by boundary and sub-cause for the account; (b) membership by boundary and sub-cause.
- Recommendation: (a).
- Changes: (b) leaves a routing or reading defect on a family's rows outside that family's bound.

**C32. A case that touches several mechanisms.** Source: M-7.
- Question: Does a case that touches several mechanisms count for each?
- Options: (a) counted for each; (b) primary only, by a fixed precedence.
- Recommendation: (a).
- Changes: (a) verdicts share cases, are not independent, and more can come out *can't tell*. (b) leaves the other endpoints unbounded against a defect that moves them.

**C33. Demoted and candidate rows, which no question asks.** Source: M-9.
- Question: Where do demoted and candidate rows, which no question asks, enter?
- Options: (a) state account only; (b) also map the no-successor demoted values (F27, F35, F56) to rejection's account; (c) let state endpoints enter the verdicts.
- Recommendation: (a) plus (b) for the account; not (c), because RAG has no answer on unasked rows.
- Changes: (a) and (b) change the account only; (c) changes verdicts.

**C34. Losses that no listed mechanism owns: routing, reading, admission.** Sources: M-10; claims R-8.
- Question: How are routing, reading and admission losses, which no listed mechanism owns, accounted?
- Options: (a) account them as "none" under Rule A (key model D4, reading D8, admission D2); the reading rows name the read contract as built, in no arm and not tested; (b) map reading to evidence and provenance; (c) ask the Phase D3 registration to add them, for Phase D only, in a dated note (line 114).
- Recommendation: (a) for Phase C; revisit at the Phase D3 registration.
- Changes: under Rule V these losses still weaken every family whose rows they cover (C31). So the options change the account and the text of the rows R-8 names (C11, C21, C23, C79; group C, C24; C40, C49, C53, C87, C103, C113).

**C35. Stored values that cite the wrong meeting.** Source: M-11.
- Question: Are stored values that cite the wrong meeting examined, given that they are not loss-trace cases?
- Options: (a) accept and disclose that they are not cases; (b) examine every evidence-question row that passes the status step as a pass examination (7 rows per run).
- Recommendation: (b).
- Changes: (b) examines, beyond line 315, every evidence row that passes the status step. Under (a) a wrong-meeting value weakens only if its pass row falls in the 20% pass sample and is coded as resting on a defect, or through the pass share (Rule M item 2; mapping section 7, item 4). In both, it can move only a credited evidence question (the works bound).

**C36. "Distinct values net"** in the A2 admission measure (line 516). Source: M-13.
- Question: What does "distinct values net" mean in line 516?
- Options: (a) per run, the values with more status-step passing rows with the contract on, minus the values with fewer, over all row kinds; (b) values passing at their last checkpoint only.
- Recommendation: (a).
- Changes: it defines the admission margin of every A2 contract.

**C37. Which rows a case covers.** Source: M-14.
- Question: Which rows does a case cover?
- Options: (a) every row of the value in the run whose first loss is at the case's step; (b) only the row at the earliest failing checkpoint.
- Recommendation: (a).
- Changes: (b) leaves the rows of later checkpoints outside every bound.

**C38. Known-bug incidence on facts that hold no gold value.** Source: M-15.
- Question: Does known-bug incidence on facts that hold no gold value enter a bound?
- Options: (a) reported, not bounded; (b) each such event makes its bug's mechanism *can't tell*.
- Recommendation: (a) for Phase C. It moves no endpoint, and system-bug incidence is zero under A1 and A2 (plan 23:243, :248).
- Changes: (b) can make a verdict *can't tell* with no endpoint row moving. Under (b), each bug's mechanisms are the ones Rule M item 9 fixes now (choice 15). Three of them are choices: bug 1 also maps to rejection (D3.p3's negation sentences); bugs 3 and 4 map to change and supersession (bug 3's quoted sentence is 5de9911 text, R-22; bug 4 names no decision). Bug 12 is listed and maps to none.

**C39. The bound population of an A2 contract.** Source: M-16.
- Question: Which cases enter an A2 contract's bound population?
- Options: (a) cases at `filed` to `status`; (b) every write-path case.
- Recommendation: (a). The harness replays the same claims in both variants (lines 177–180), so extraction is identical by construction.
- Changes: (b) adds extraction cases that no leave-one-out can move, which raises the weakening count.

**C40. Held conflict cases in the A2 contract bounds.** Source: M-21 (new at review), with M-8 (A7) and M-16 (C39).
- Question: Held same-meeting-conflict cases enter all four A2 contracts' populations, so every A2 contract is expected to come out *can't tell* while the conflict decision is open; what is done about it?
- Options: (a) disclose only, as mapping section 6.2 now does; (b) limit each contract's population to the sub-codes it acts on; (c) under C44's arithmetic, stratify the borrowed A2 shares, so that the held share applies only to a variant's own open-conflict cases.
- Recommendation: (a) in any case. Consider (c) if decidable A2 verdicts are wanted. Not (b).
- Changes: under (a), no A2 contract is likely to be admitted, since only *works* is admitted (line 522). (b) conflicts with Rule V (C31) and leaves `supersession_requires_new_evidence` with no population. (c) adds an arithmetic rule the amendment does not contain, and may make the A2 verdicts decidable.

**C41. "Owner or role claim"** in the WD rule (line 293): the drafted definition. Sources: M-17; the probe note's section "Owner or role claim on EL2020 (C41, M-17)", drafted in its completion pass and changed in that pass's review and in the second review (27 October).
- Question: Do you sign the definition of an owner or role claim on EL2020, and of its loss, as drafted in the probe note, with its seven choices?
- Options: (a) sign it as drafted; (b) revise one or more of its choices, using the alternatives below, before the tag or in a dated note before Step 2c.
- Recommendation: (a). It needs no gold, no adjudication and no model call. It is computed mechanically from the extraction steps of the six Step 2c runs and the suite's transcripts, into the hashed Step 2c outputs, which are opened at the reveal (line 411).
- Correction: M-17's option (b), dropping the condition on EL2020, would drop a condition of the WD rule, which is fixed (lines 289–296, 555). It is not offered.
- What the draft fixes (gloss):
  - An owner or role claim is an item of an extraction call's `output.claims` whose predicate has a word in a closed list OWN (forms of own, assign and responsible), or a phrase such as "take over" or "in charge" (test P); or whose `state_key_hint` has an OWN word in its last segment (test K).
  - A unit is a pair (span, owner part) that a fresh A1 run emits. A run carries a unit only through an owner or role claim with an equal part.
  - A unit is lost when at least 2 of the 3 fresh A1 runs carry it and at least 2 of the 3 WD runs extract the span without it. The condition fails if one unit is lost. It holds otherwise, also when no unit is formed, and the Step 2c report then says so.
- The seven choices, with the alternatives the probe note names:
  1. The test: (P) or (K), as above. Alternative: the literal predicate 'owns' only.
  2. Action items with an owner: not counted. They are not claims, and they are never filed or read by the answer path. Alternative: count them.
  3. The boundary: the extraction output, which is the `carried` boundary of WD's endpoint. Losses after extraction (routing, filing, status) are outside the condition. Alternative: also require the owner claim to be filed under a key by the last checkpoint.
  4. Merges: an owner named only inside a claim of another kind (for example a whole-decision value) is not carried; an owner claim that lists several owners carries each; parts match only when equal, never by containment. Alternative: containment counts as carried.
  5. The threshold: a ≥ 2 and m ≥ 2, "(iv) mirrored, with WD runs that do not cover the span left out". Alternatives: a ≥ 2 and m ≥ 1; a ≥ 2 and w = 0; or the exact mirror of (iv) and line 356, a ≥ 2 and w ≤ 1, with only the units that no WD run covers set apart. The review of the completion pass left this choice open. The exact mirror counts as lost every unit with w ≤ 1 that at least one WD run covers, so the condition fails more often.
  6. Spans not covered by WD: one rule under every threshold of choice 5. A unit whose span no WD run covers is not lost; otherwise a unit the threshold counts as lost is lost. Listed apart, with each WD run's gatekeeper policy, and never deciding, are the units with a ≥ 2 and w ≤ 1 that are not lost and whose span at least one WD run does not cover (w + m ≤ 2). Under the drafted threshold these are the units with w ≤ 1 and m ≤ 1; under m ≥ 1, those with w ≤ 1 and m = 0; under w = 0, the units that no WD run covers and those with w = 1 and m ≤ 1; under the exact mirror, only the units that no WD run covers. Alternative: count such a unit as lost.
  7. The scope: owner claims on noise topics, and negative, hedged or proposed owner claims, count. No alternative is drafted, since a topic filter would need a judgement.
- Smaller drafted details, signed with the definition:
  - an owner part equal to 'team', 'we' or 'everyone' forms no unit, since the prompt forbids such owners;
  - 'lead', 'leads', 'led' and 'handles' are not in OWN, because 'leads' also occurs in causal predicates; such a claim counts only through (K);
  - a failed extraction call, with `mode` "llm_error", covers its span, so a failure under WD counts as a miss;
  - a call is placed on a span by its exact text, and failing that by the text after the run's recorded gatekeeper redactions; a call that matches no span, or more than one, stops the computation for a dated note.
- Changes: (a) keeps the condition testable on EL2020 and fixes it before any Step 2c output exists. A revision edits the probe note before the tag (C1), or needs a dated note before Step 2c. Containment (choice 4) makes the condition hold more often; a lower threshold (choice 5) makes it fail more often.

**C42. The endpoint of Step 5's joint contract verdict** (final configuration against A1-ref; lines 533–534). Source: M-18.
- Question: Which endpoint does Step 5's joint contract verdict use?
- Options: (a) the admission endpoint (status-step rows, distinct values net), with the family endpoints as context; (b) the family endpoints.
- Recommendation: (a), fixed before the Step 5 runs.
- Changes: it decides the only verdict on the admitted contracts taken together.

**C43. When Rule M, the verdict rule for the architectural mechanisms, is fixed.** Sources: M-19 (changed in the completion pass, its review and the second review); the claims register's mapping section 7a, "Rule M: verdicts for the architectural mechanisms (drafted 27 October 2026 for C43)"; the open points of its drafter and of the review's fixer.
- Question: Plan 23 asks for "an endpoint and a pre-registered rule for *works*, *doesn't work* or *can't tell*" (plan 23:344). That rule is now drafted as Rule M. When is it fixed?
- Options: (a) sign Rule M with this package; (b) move it unchanged into a dated note before the Step 3 reveal (line 411, item 7); (c) move it unchanged into a dated note before the Step 5 runs.
- Recommendation: (a). The rule is drafted, so (a) no longer delays signing. Failing that (b), not (c). The amendment "fixes decision rules that their own outcomes must not steer" (line 14). Disclose in every case that the EL2020 family results were read first (C43.3).
- What Rule M fixes (gloss):
  - verdicts for the five architectural mechanisms only, each against RAG on one series, with both arms run in the same period: A1 on EL2020; on ES2009 the final configuration in Step 5, which is A1-ref where no contract is admitted. A0 and A2 get none, and series are never pooled;
  - the endpoint: per run, the number of the mechanism's family questions scored correct (C28–C30, C35);
  - *works*: every run of the arm under test scores above every RAG run (exact one-sided p at most 1/20), and the mean difference is larger than the instrument range, the larger within-arm range of the two arms. *Doesn't work* is the mirror. Otherwise the verdict is *can't tell (within the instrument range)*;
  - the bound: the amendment's bound rule (lines 451–471) applied to that test. A verdict that does not survive it is *can't tell (defect-limited)*. Each verdict is computed once, from the final codes.
- Changes:
  - (a) fixes the rule "**before any Step 2, 2b or 2c output exists.**" (line 14). The Step 3 codes and the Step 2, 2b and 2c outputs that the bounded verdicts need do not exist yet; the frozen loss trace, whose defect flags enter the bound directly, does.
  - (b) fixes it when the Step 2–2c outputs may exist in hashed files, unopened (line 411), and the blind codes of Step 3 items 4 and 5 may exist. The note says what had been read by then (line 16).
  - (c) fixes it after the codes and the Step 2–2c outputs that drive the bounds are open, so they could steer it.
  - Under every option, rows C04, C77 and C94 depend on it. C94 has a text action for *can't tell (within the instrument range)*. C04 and C77 have a third branch only for *can't tell (defect-limited)*; the claims review of the completion pass kept them so (VI-RM-3).
- Answering C43 adopts Rule M's test (its item 4) and the 15 choices listed at its end; under (b) or (c), in the later note. Neither the amendment nor plan 23 fixes them. In brief:
  1. the comparisons that get a verdict, as above. Line 309 excludes A0 from admission verdicts only;
  2. the series verdict: A1's on EL2020; on ES2009 the final configuration's, with A1-ref's beside it where they differ, and A1-ref's where the final configuration has no Step 5 runs;
  3. a later same-period comparison, such as the dress rehearsal, borrows shares within its series;
  4. a family question with no scored answer counts as not correct;
  5. one same-period replacement for a run without a valid report, or with switches that do not match its arm (Phase C only);
  6. the test form: strict ordering, exact p at most 1/20, and a mean difference larger than the instrument range;
  7. the instrument range (C43.1);
  8. a later repair does not exempt a case in the counted runs (the end state "Repaired", line 27). With choice 8, no Step 4 decision can move the EL2020 verdict;
  9. rows with a loss-trace defect flag are counted directly and first, each row once, and an item whose endpoint rows are all flagged leaves the uncoded pool;
  10. the inputs: the loss trace's primary series, under v1 on EL2020 and under the ES2009 adjudication file on ES2009 (lines 171, 173). A bounded verdict needs the loss trace for every counted run;
  11. share 1 where a share's base is empty in the run or runs the share comes from, so that a borrowing arm takes the borrowed share, and the drop to share 0 with the first clean item in the base; where the final configuration has no Step 5 runs, this gives A1-ref share 1. C44, option (d), offers a floor;
  12. mapping section 7: the pinned bootstrap (seed 23, 50,000 draws), with its values, draw, statistic and exact arithmetic; the share's base (the mechanism's cases among the 30 author-coded cases per run; for the shares Step 5 borrows, among the cases of 3b's coded run; pilot cases enter as uncoded; fresh-sample cases are outside the base but taken first when they weaken); the definition of single- and multi-value questions; the multi-value rule and the greedy fill for the doesn't-work bound, within the mechanism's endpoint family, with every coded weakening case taken; the pass share, its count and its fill for the works bound, the pass test (implementation answer yes or unclear), and rows examined in full that weaken, counted as weakening passes even when the trace records them as lost. These are also C44's;
  13. the two gold versions (C43.2);
  14. a state endpoint under C30 (c) or C33 (c) gets its rule with Rule M, or enters no verdict;
  15. the readings under the alternatives (Rule M item 9): the bug-to-mechanism list under C38 (b), for the bugs in the evaluated system (`22-bug-list.md` section A), with the choices for bugs 1, 3 and 4; under C31 (b), the membership of uncoded cases by mapping section 3's account column; under C32 (b), mapping section 5's order as the precedence; and the condition on choosing C44 (c).
- Sub-questions, answered with C43. The draft follows each recommendation.
  - **C43.1 The instrument range** (choice 7).
    - Options: (i) the larger within-arm range of the two compared arms, computed from the recorded counts after the runs; (ii) the largest within-arm range over all same-period arms.
    - Recommendation: (i). Under either, disclose that the form was chosen after the EL2020 family results were read, as Rule M does.
    - Changes: (ii) is at least as large as (i), so it gives more *can't tell*.
  - **C43.2 The two gold versions on EL2020** (choice 13).
    - Options: (i) the frozen gold alone sets the EL2020 verdict, recorded and bounded, and the recorded verdict under the post-B3 gold is reported beside it; (ii) as where B3 precedes the runs: if the recorded verdicts under the two golds differ, the EL2020 verdict is *can't tell (defect-limited)*, with disclosure.
    - Recommendation: (i). Line 96: "Steps 2–4 use the frozen EL2020 suite and gold. Post-B3 scores are reported beside them." The EL2020 B3 decisions are taken after the EL2020 comparisons were read (line 155).
    - Changes: under (ii), a gold decision taken after those reads can turn the EL2020 verdict into *can't tell*.
  - **C43.3 How Ch. 5 discloses the timing.** The recorded EL2020 verdicts (A1 against RAG) can be computed from runs that were read before Rule M was written. Only the bounded verdicts depend on outputs that do not exist yet. Rule M says so under "Not blind, and when it is fixed".
    - Options: (i) say so beside each EL2020 Rule M verdict in Ch. 5, with the date Rule M was fixed; (ii) say so once, in Ch. 5's method section.
    - Recommendation: (i). A reader then sees the limit where the verdict is stated.
    - Changes: Ch. 5 text only.
    - **Moved to Phase F (author, 27 October): not needed for signing.** C43.3 is answered when Ch. 5 is written. The disclosure is required under either option, so Rule M is unaffected.

**C44. The bound arithmetic on a question endpoint.** Source: M-20.
- Question: How is the bound computed on a question endpoint?
- Options: (a) shares pooled per arm, with a bootstrap over values and the upper end of the 95% interval; the remainder filled by mapping section 7's deterministic greedy fill (items 3 and 4), which approximates, and does not guarantee, the fill least favourable to the recorded verdict; (b) per-run shares; (c) a proportional (expected-value) fill, which no section of the mapping defines yet, and which can be chosen only if its fill, including how a fractional recovery scores a question, is written into mapping section 7 when Rule M is fixed (Rule M item 9); (d) as (a), but with share 1 wherever fewer than 5 items are in that share's base (coded cases, or examined pass rows in the pass share's base; Rule M item 5) in the run or runs the share comes from (M-20, added in the review of the completion pass and reworded in the second review).
- Mapping section 7 now pins (a): the bootstrap resamples values, with the seed (23), draw count (50,000) and upper-end index of `23-el2020-a0-a1.py`, which resamples questions; it fixes the bootstrap's values, draw and exact arithmetic, the share's base, the definition of single- and multi-value questions, the multi-value rule, a deterministic greedy fill for both bounds within the mechanism's endpoint family, and the pass share with its count and its pass test. These are Rule M's choice 12.
- Recommendation: (a). It is deterministic and follows line 456. It is not conservative on small bases (see Changes); choose (d) to close that, at the cost of a threshold the amendment does not contain. The register makes no recommendation on (d).
- Changes: it decides how far the bound moves each verdict; (c) is less conservative; (b) rests each share on about 30 cases. Under (a), a share whose base is empty in the run or runs it comes from is 1, but if every item in its base is clean, even a single one, the bootstrap's upper end is 0, so the share drops from 1 to 0. This is lenient for the small families (epistemic status, change and supersession, evidence and provenance). (d) removes that drop. It adds a threshold, 5, that the amendment does not contain, and it departs from line 456's "upper end of its 95% bootstrap interval" on small samples.

### The claims register: text actions

**C45. How the sizes in "confirms if" and "overturns if" bind.** Source: R-1.
- Question: How do the sizes in each row's "confirms if" and "overturns if" bind?
- Options: (a) bind every row's sizes as written; (b) indicative only; (c) one global text-action rule signed with the register: a causal sentence is kept when the bounded share of its boundary's coded cases with that cause is a majority, qualified between about 20% and 50%, and removed below 20%; a design attribution also needs 94c049d text and the kappa's lower bound at or above 0.40; the per-row sizes are indicative.
- Recommendation: (c). Disclose that the 20% and 50% thresholds were proposed in Step 0 and were not checked in the four review rounds.
- Changes: (c) adds two thresholds the amendment does not contain. It stays within line 31 only because a design statement still needs the codes (line 572: "made only where the codes say architectural or trade-off on 94c049d text"). (b) leaves the text actions open after the outcomes, against lines 14 and 111–112. (a) binds 144 rows' own size words.

**C46. When the P0 text fixes are applied** (P0-A to P0-E, with the bug-11 counts). Source: R-2.
- Question: When are the P0 text fixes applied?
- Options: (a) before signing, with a re-sweep; (b) after signing and before any Step 2 output exists, with the bug-11 counts replaced by loss-trace v3.1 first-loss counts labelled surfaced-at; (c) at the reveal.
- Recommendation: (b). Plan 23 then listed the P0 fixes as independent of Phases B–E (plan 23:375, which now records the move). Not (c).
- Changes: (b) signs the register on the current text, with the P0 rows marked "rewritten regardless". (c) would edit after the outcomes are read.
- **Answer (author, 27 October): (b), but applied in Phase F.** Plan 23 now places the P0 fixes in Phase F, item 1, after Phase E (the recommendation describes that item's former place). The register is signed on the current text, with the P0 rows marked "rewritten regardless". The P0 content stays as `22-fix-priorities.md` fixes it at ce75b1f, before any outcome. Any change to that wording made after the outcomes are read is disclosed as such. The bug-11 counts are replaced in Phase F by the loss-trace v3.1 first-loss counts, labelled surfaced-at, as under (b).

**C47. Corrections that Phase B records already decide.** Sources: R-3; R-16; R-4's extension to C05.
- Question: Are the corrections that Phase B records already decide made now, as conformance fixes?
- Items: rows C85 (date clause; bug 6), C126 (the copying cited as D9; bug 2), C119 (flagship trace; bug 2), C88 (wrong-key figure; bug 9), C109 ("No contract has been implemented"), and C05's D9 clause at eval.tex:1092 (bug 2). Outside the register (R-16): main.tex:124, background.tex:195, background.tex:272, conclusion.tex:171 and eval.tex:932.
- Options: (a) correct them now as conformance fixes, recorded "decided before signing"; the out-of-scope sentences go to the P1-3 or P0 fixes; C05's clause is replaced by the bug-2 qualification (P0-E); (b) leave them for the reveal; add the R-16 sentences as register rows; keep C05's clause, citing D9.p4.
- Recommendation: (a). They are facts about the code, not outcomes. For C05, (a) matches C126.
- Changes: thesis text at these locations, before any outcome.
- **Answer (author, 27 October): (a) as a decision, applied in Phase F.** Each correction is recorded here as "decided before signing". The thesis text is edited in Phase F, item 1, with the same content.

**C48. Text written after 9 September and cited as a design cause.** Source: R-5.
- Question: How is text written after 9 September, which Ch. 5 and Ch. 6 cite as a design cause, handled?
- Options: (a) name, per claim, the 94c049d paragraph that could ground it; re-ground only where the codes support it, otherwise make the claim location-only; (b) also mark D10, D11 and the other post-9-September Ch. 4 sentences now as made explicit after cycle 1, with dates (P0-D); (c) move D10 and D11 to Ch. 6.
- Recommendation: (a) and (b). Settle the exact Ch. 4 wording from the codes at the reveal.
- Changes: rows C82, C83, C87, C110, C113 and C118, the decision-tagged headings of sec:conc-implications, and the Ch. 4 sentences.
- **Moved to Phase F (author, 27 October): not needed for signing.** The P0-D marking that (b) asks for is part of the P0 fixes and is applied in Phase F with them (C46).

**C49. How a WD result reads for the D10 claims** (C46, C82, C110, C118). Source: R-20.
- Question: How does a WD result read for the D10 claims?
- Options: (a) split each into a location-and-remedy part, confirmed by (iv), and a design part, overturned by (iv) and confirmed only by an architectural code on D4.p5; (b) leave the rows as written.
- Recommendation: (a), so that "confirmed" means the same in every row.
- Changes: the count of claims reported as held.

**C50. Which configuration Ch. 4's "evaluated configuration" sentences describe.** Source: R-6.
- Question: Which configuration do Ch. 4's "evaluated configuration" sentences describe?
- Options: (a) A0, marking each repaired behaviour with its switch; (b) the final configuration, with A0's behaviour as defect notes.
- Recommendation: (a). It keeps Ch. 4 matched to the evaluated results.
- Changes: Ch. 4's D3, D4 and D5 sentences.
- **Moved to Phase F (author, 27 October): not needed for signing.**

**C51. Ch. 2 and Appendix B claims in the register.** Source: R-7.
- Question: Do Ch. 2's problem-level claims and Appendix B's record-level claims stay in the register?
- Options: (a) include them; Ch. 2 actions are limited to keep or qualify without solution content, and Appendix B stays unchanged (line 448); (b) exclude them.
- Recommendation: (a). Plan 23, Phase F 2, asks Ch. 2 to keep conversational difficulties apart from architectural ones.
- Changes: (b) leaves those claims unchecked against the codes.

**C52. The restraint claims** (group C), which rest on the bug-8 ablation switch and the bug-10 counts. Source: R-9.
- Question: What happens to the restraint claims of group C?
- Options: (a) remove the attribution to the resolver's embedding candidates and the phrase on D8's role (eval.tex:962); keep the noise passes as an observation; disclose bugs 8 and 10; (b) keep the attribution with caveats; (c) build per-component switches, which reverses the decision of 22 October.
- Recommendation: (a), following P0-A. Add no sentence about internal plans that were not carried out.
- Changes: Ch. 5 and Ch. 6 text in group C. (c) adds runs.

**C53. The generated ablation tables C136 and C136a.** Source: R-14 (widened at review).
- Question: What happens to the generated ablation tables C136 and C136a?
- Options: captions: (a) qualify them through the generator; (b) remove the tables; (c) leave them. C136a's Resolved column: (i) re-derive it per checkpoint; (ii) drop the column; (iii) remove the table.
- Recommendation: (a) and (ii). Under bug 10 the dumps keep only the earliest checkpoint's log for a repeated question, so (i) needs a re-run that reverses the decision of 22 October.
- Changes: Appendix A's two generated tables (`15-ablation-tables.py`).
- **Moved to Phase F (author, 27 October): not needed for signing.**

**C54. The reference-informed arm claims** (C30's clause, C63, C66, C125). Source: R-10.
- Question: How are the reference-informed arm claims handled?
- Options: (a) mark them "untested here; the text follows the bug-14 decision"; (b) add a rebuilt-gate arm, which is outside this amendment.
- Recommendation: (a).
- Changes: (b) adds an arm the amendment does not contain.

**C55. The fairness disclaimers against the transfer attributions.** Source: R-11 (extended to Ch. 6 at review).
- Question: Which side gives way: the sentences that deny that a single mechanism is isolated (eval.tex:455, eval.tex:1257, conclusion.tex:96), or the attributions of the gap to RAG to named mechanisms (eval.tex:1036–1038, 1076–1078, 1084–1089; conclusion.tex:306, :330)?
- Options: (a) keep eval.tex:455 and conclusion.tex:96, and rewrite the attributions in Ch. 5 and Ch. 6 as locations of ProjectMemory's losses (surfaced-at, then caused-at); (b) qualify eval.tex:455 and conclusion.tex:96 to exempt the span-level trace.
- Recommendation: (a). Settle the wording after Step 3, and edit conclusion.tex:96, :306 and :330 together.
- Changes: how Ch. 5 and Ch. 6 frame the comparison with RAG (C55, C89, C130, group N).
- **Moved to Phase F (author, 27 October): not needed for signing.**

**C56. Two meanings of "admission" in Ch. 5.** Source: R-12.
- Question: Are eval.tex:852 and :1223, which use "admission" for value confirmation, reworded?
- Options: (a) map eval.tex:1033 to `admitted`, and eval.tex:852 and :1223 to `applied`, rewording the latter two to "value confirmation"; (b) treat both as admission.
- Recommendation: (a).
- Changes: two Ch. 5 sentences.
- **Moved to Phase F (author, 27 October): not needed for signing.**

**C57. The ES2009 causal claims** (C56–C59, C61, C62, C69, C97, C98a, C99, C115–C117, C122, C127). Source: R-13.
- Question: How are the ES2009 causal claims handled?
- Options: (a) keep the cycle-1 numbers, and qualify their causal readings by the Step 5 results, as a consistency check, not a replication (lines 157–164); (b) mark them untested.
- Recommendation: (a).
- Changes: the ES2009 text of Ch. 5 and Ch. 6, after Step 5.

**C58. Rows this study cannot test** (claims section 6.1). Source: R-15.
- Question: What happens to the rows this study cannot test?
- Options: (a) leave the text unchanged unless an independent fix applies (P0, a conformance fix, the bug-14 decision); (b) qualify each row now as untested.
- Recommendation: (a). The study cites no result for them.
- Changes: (b) edits up to 22 locations with no result behind them.

**C59. The recall clause of the embedding claim** (C03, C71, C124). Source: R-19.
- Question: Is the recall clause of the embedding claim testable here?
- Options: (a) partly testable in all three rows; the text is limited to "no recall loss traced to the resolver's pruned shortlist on EL2020" or its reverse (claims, R-19); (b) not testable; left to P0-A.
- Recommendation: (a). Probes (ii-r) and (iii) test the pruned shortlist as a whole, not the embedding candidates alone (`_prompt_registry` at 3320375).
- Changes: the three rows and their text.

**C60. The D4 and D8 tags of the "Shared failure" heading** (conclusion.tex:334; C130a). Source: R-21 (new at review).
- Question: Do the D4 and D8 tags stay on the "Shared failure" heading?
- Options: (a) keep the observation (conclusion.tex:336–337) and drop the tags; (b) keep the tags, marked as untested.
- Recommendation: (a). No code in this study can support them, and a design statement needs codes on 94c049d text (line 572).
- Changes: one Ch. 6 heading.

**C61. A facts-per-key count for C123.** Source: claims row C123 (note); claims builder gaps.
- Question: Is a count of facts per key over the frozen states added, so that C123's hub clause can be tested?
- Options: (a) add it to the offline reading analysis ($0), computed and sealed with the Step 2 outputs (line 411); (b) mark the hub clause untestable.
- Recommendation: (a).
- Changes: (a) adds an analysis that lines 216–219 do not list. Under (b), C123's confirm condition cannot be met.

### Cross-package findings still open

**C62. The line-340 condition at "candidate generation", and at the gatekeeper.** Sources: cross-package finding X6; template Section 7, point 24; the template's review of the completion pass (MX-F8).
- Background. The completion pass aligned the template with the register sheets: the line-340 condition and the class "design or model, not separated" now apply per step, at the six LLM steps the sheets name (the "gatekeeper", the hint field of the extraction call, the "resolver", the "support check", "question resolution" and "grounding"). Before, they applied to whole boundaries, deterministic steps included. Line 331 names the boundaries "routing, reading, A2's support check, the gatekeeper for `admitted:ignored` cases", and line 340 covers any "LLM step with no model condition".
- Why C: the template drafter reports that the sheets and the amendment's wording differ at one step. The register's K2.1 Chain line marks "candidate generation (LLM)", and no probe gives that step a model condition: "Expansion-routed misfilings (the resolver returned no key, and expansion reused or created one) are not probed." (line 251). Sheet K2 names only the resolver: "for the resolver, the condition of line 340 applies."
- Question: Do the line-340 condition and the class "design or model, not separated" also apply at "candidate generation"?
- Options: (a) as the sheets: no, and the template stays as written; (b) as line 340's wording: yes. Sheet K2 names the step, and template A5 and the schema add it.
- Recommendation: (b), unless the register records why the step is left out, as template point 24 recommends. Few codes move, since line 251 codes expansion-routed misfilings "under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry".
- Changes: (b) is a register edit and changes both template hashes. Architectural weakness or a trade-off at that step then needs line 340's argument; without it the case is design or model, not separated. (a) lets those codes stand there without the argument line 340 asks of an LLM step.
- Second item: the gatekeeper. The schema requires line 340's argument at the "gatekeeper" only for `admitted:ignored` cases, and allows "design or model, not separated" there only for those cases. This follows line 331 and sheet E, cause 4 ("Only for `admitted:ignored` cases").
  - Options: (i) as written; (ii) require the argument at the gatekeeper for every surfacing step, the stricter reading of line 340.
  - Recommendation: (i). It is line 331's own scope.
  - Changes: (ii) changes the schema and both template hashes, and asks the argument also for a gatekeeper-caused case that surfaced at a later step.

**C63. How the working-tree citations of plan 23 and the bug list are frozen at the tag.** Source: cross-package finding X11.
- Background:
  - The claims register, the template, the probe note (plan 23:264) and this sheet (C29, C38, C43, C46, A6) cite working-tree lines of plan 23 and of `22-bug-list.md`. Claims section 1 says so for the claims register, and the template's Conventions for the bug list. The design-and-controls register cites both files at commits.
  - Both files are modified and uncommitted, and their uncommitted hunks include another session's work.
  - Against b4d6b6c, plan 23's working-tree lines from 75 on are shifted, by up to about 40 lines (its line 344 is one). `22-bug-list.md` equals 3320375 up to line 122; its later lines are shifted, and the template's `22-bug-list.md:195` does not exist at 3320375.
  - Line 124 asks to "update `22-bug-list.md` row 11" before Step 2. Row 11 starts at line 116 and also has a row in the repair-status table near the end, so the edit moves the lines after it. The claims register cites lines 123–190 there, and the template line 195.
  - SHA-256 now: plan 23 `1c8ec3a49ffa79c8f11e7297c892dcb3b20bb343b3a4dfe9c4ae82eb450d9881`; `22-bug-list.md` `2096a1f405c127dab59b821ce008bd840761973bc5a7511ed3ab3aa305bc8fd6`.
- Question: How are these citations frozen at the tag?
- Options:
  - (a) the signing commit includes both files at their cited states. First check that the other uncommitted hunks are ready to commit;
  - (b) record each file's SHA-256 in the signing record, keep a byte copy in the off-repository run archive, and read every such citation at that hash;
  - (c) re-cite each line at a committed version where the same text exists, as the design-and-controls register does, and use (b) for the rest.
- Recommendation: (a) if the hunks are ready; otherwise (c).
- **Answer (author, 27 October): (a).** The uncommitted hunks are ready to commit: bug 14, the answerable-only and informed-gate records, and the Phase F change of 27 October. The signing commit includes both files at their cited states. The Phase F change in plan 23 replaced lines 375–377 by 375–378, so every later line moved down by one. The one later cite in the package, the claims register's note on the reference-informed arm, was moved from line 443 to 444 on 28 October. Plan 23's SHA-256 above is from before that change; the signing record gives the final one (B24).
- Changes:
  - (a) makes every citation checkable from the tag. It commits the other session's hunks with the package. The row-11 update before Step 2 then shifts lines after the tag, so later readers must read those citations at the tag.
  - (b) keeps the repository's copies free to change; the cited lines can then be checked only against the archive copy.
  - (c) edits the claims register, the probe note, the template and this sheet before the tag. The template's citations of the bug list are outside the prompt, so its hashes do not change; the probe note's §1.4 hashes do not change either. The citations whose text exists at no commit fall back to (b).

**C64. The known-answer set for V4** (amendment line 407; review of 28 October, findings L1-1, L1-4, L2-2, L4-1, L4-2, L5-1, L5-4, L5-5, L6-5).
- Question: Does a known-answer set gate V4's codes?
- Background: draft 6 gated V4 on the A0 cases lost at state maintenance with the bug-3 flag, at least 14 of 17 coded as implementation defect at state maintenance. Under the case unit (line 301) the frozen trace holds 11 such cases; 17 is the number of trace rows. So 14 could never be met, and the fallback would always have applied. The expected answer is not established either. The flag marks any replacement in the same meeting, and plan 23 calls such flags can't-tell markers. 10 of the 11 cases are overwritten by a non-gold value, which the loss trace reads as usually wrong routing, so a coder who follows lines 375 and 378 can rightly give routing as caused-at. A gate on class alone is passed by a coder that always answers implementation.
- Options: (a) drop it; V4's competence shows in the kappa, and a weak V4 only makes design-limit statements and repair eligibility harder; (b) keep it on the 11 cases, scoring class only (implementation defect with Phase B bug 3), each case confirmed by the author from its page in a dated note before V4 starts, with a bar of 9; (c) keep the 11 as a reported diagnostic that gates nothing.
- Recommendation: (a). Applied: line 407 now holds the channel trial on the pilot cases, line 432 drops the second trigger, and template Section 9 no longer mentions the set.
- Changes: (a) nothing tests V4 against an answer fixed apart from the author; (b) adds an author judgement before V4 runs and a threshold no review has checked; (c) costs 11 conversations and reports a number whose key is doubtful.

**C65. V4 at item 8** (line 414; findings L1-3, L2-5, L4-5, L5-3).
- Question: How does V4 take part in item 8's forced re-codes?
- Background: line 414 had each coder re-code class and sub-cause where an oracle or a leave-one-out moves a boundary, or where v1 and v2 differ. V4's only instrument is the fixed prompt, which tells the coder it will never see the sealed outputs, and no re-code packet existed. A re-code input written after the reveal would be designed with the results known.
- Options: (a) V4 does not re-code: its mechanically resolved blind code is its final code, the author re-codes, and these cases are reported apart; (b) fix a re-code packet now (the case packet plus a fixed block naming the moved boundary or the v2 row result) and a script command for it.
- Recommendation: (a). Applied at lines 411, 414 and 583. It is decidable now, and conservative: on a moved case V4's final code keeps its blind class and sub-cause, with the caused-at the oracle or leave-one-out sets mechanically, and it agrees with the author's under line 480 only where all three match.
- Changes: (a) fewer moved cases may meet line 480, and the final kappa on them compares the author's re-codes with V4's blind codes (reported apart); (b) keeps the symmetric design but adds an instrument that needs its own review before signing.
- Also: the author runs V4 and may see its blind codes. Every change the author makes after V4's first packet, at a codebook revision or at item 8, is disclosed as made after that (line 414).

**C66. The copy check and the 0.40 rule** (lines 430 and 572; findings L1-7, L4-7, L5-6).
- Question: What does the copy check do for a machine V4?
- Background: draft 6's trigger (the two models agreeing far more, or clearly above the author's) had no threshold and named no measure, yet it chose which kappa the 0.40 rule used, and it would have been read after the kappas were known.
- Options: (a) no trigger: V4's agreement with the pre-codes is reported, and the 0.40 rule always takes the lower of the two lower bounds of the author's blind binary kappa with V4 and with the pre-codes; (b) the 0.40 rule on the author–V4 kappa only, the rest reported; (c) keep a trigger with a number fixed now, for example 95% blind binary agreement between the two models, or 10 points above the higher of the author's two.
- Recommendation: (a). Applied at lines 430 and 572. It is fixed before any kappa and is the strictest of the three.
- Changes: (a) a design-limit statement needs both machine readings to agree with the author; (b) rests on one model; (c) keeps a switch whose threshold no review has checked.

**C67. When V4 starts, and the due date** (line 405; findings L1-2, L2-1, L5-2, L4-6).
- Question: When may V4 run, and when are its codes due?
- Background: draft 6 let V4 code at any time after item 3. The author runs V4 and sees its answers, so pass 1 could have been anchored on V4's codes, and nothing sealed them. C2's due date runs from the freeze of items 1 and 2.
- Options: (a) no V4 packet, case or audit, before item 4 is committed, and the due date is seven days after item 4's commit; (b) as (a), but C2's date is kept as answered, so the seven days also have to cover pass 1.
- Recommendation: (a). The start rule is applied at line 405 and in template Section 9; line 411 keeps the sealed outputs in hashed files until items 4 and 5 are committed. The due date covers the channel trial, the 180 cases and their re-asks; the audit, a revision re-run and the fresh sample are due before item 7, and an audit not done by then leaves v2 equal to v1. 3b's V4 codes are due seven days after 3b's item-4 commit; if they are late, 3b's probe results are opened on the author's codes alone. The due date waits for your answer.
- Changes: (a) moves the due date by the length of pass 1 (about 10–18 h of work, line 583); (b) makes the fallback likely if pass 1 takes more than a few days.
- **Answer (author, 28 October): (a).** V4's seven days start at item 4's commit.

---

## B. Operational defaults (adopted unless you object)

**B1. Rename plan 23's "D1" for the whole-decision contract to WD.** Source: register decision 8.
- Adopted: write WD in the Step 0 plan-23 fix that already replaces that line's metric (line 125).
- Why B: a label. Line 6 reserves D1–D11 for the Ch. 4 decisions.

**B2. Post-9-September sentences that report observations.** Source: register decision 9.
- Adopted: mark the b422b27 sentence on the gate ignoring 76 of 251 spans, and any like it, "not a design entry", as line 106 does for the 38a0f4a sentence.
- Why B: under either label it can ground no design code and rule out no alternative (line 347).

**B3. Commit the remaining check scripts before the tag.** Sources: register decision 10 (partly resolved); claims section 10; probe note gaps; template section 1.
- Adopted: a committed script, or scripts, that reads only git objects and files and re-derives:
  - the code-derived prompt hashes, the prompt-to-constant equality and the schema checks, and the alias-merge check (register);
  - the merge's completeness check (register);
  - the claims register's quote check (`qcheck_claims.py`, scratch);
  - the probe note's substitution hashes and overlap check (`compute.py`, `overlap.py`, `overlap_reg.py`, scratch);
  - the template's schema test.
- `23-am1-prompts.py` stays trace-only. The template's post-call validator (section 4) is needed before Step 3 item 3, not at signing.
- Why B: it reproduces numbers the files already cite and changes none.
- Done (28 October): `23-am1-check-package.py` re-derives all of the above from repository files, plus the extract's byte-identical rebuild (`23-am1-precoder-extract.py --check`), the audit list's re-run and every hash row of the index, and it fails on a package file with no index row. The merge's completeness check is closed as a one-time historical check, whose result is in the register's Checks section (register decision 10).

**B4. The eight unpinned thresholds.** Source: register decision 11. **Settled by the main session's `.env` check.**
- The record: `.env` was last modified on 6 August 2026, before the runs. Checked by variable name, it sets none of `embedding_top_k`, `embedding_min_similarity`, `resolver_prune_threshold`, `embedding_score_weight`, `answer_relevance_min_similarity`, `answer_canonical_min_similarity`, `answer_canonical_max_items` and `llm_max_attempts`. It sets `EMBEDDING_MODEL=text-embedding-3-small`. The runner at 3320375 and the lane scripts set none of the eight. So the code defaults were in effect.
- Adopted: option (a), the record as made, with the residual limit kept in the register's Limits: the process environment at run time is not recorded, and it would take precedence over `.env`. This weighs more for a1_r1, which has no lane script.
- Why B: it is a provenance record. The probe parameters are fixed by the amendment itself (lines 107, 243), whatever the record shows.

**B5. The wording of A0.** Source: register decision 12.
- Adopted: state the as-run switch sets. A0 ran with `repair_judge_rejection_status` and `repair_dump_diagnostics` on, so A1 differs from A0 by eight system repairs. The amendment text is unchanged.
- Why B: it records what ran.

**B6. Known limits of the held-constant controls.** Source: register decision 14.
- Adopted: record them as known limits, not as blocking: whether temperature 0.0 was sent, and the served snapshots of the judge, the embeddings and the RAG generator.
- Why B: a record. The nine runs show no fallback or error.

**B7. The claims register's merge rule.** Source: R-18.
- Adopted: keep the nine merged pairs and the separate rows with "Also stated at"; consolidate each section 5 group when the text actions are applied, and check that every listed location was edited.
- Why B: it arranges rows; every row keeps its own test.

**B8. Two corrections of record.** Sources: claims section 10 (checks); claims row C144.
- Adopted: in mapping section 6.1, cite line 143, not 144, for "status items that can fail". Before signing, check `fallback_count` and `strict_live` in the `coldstart.json` of the ten runs not yet checked for C144.
- Why B: corrections of record; no rule or code changes.

**B9. The model id sent for the controls (a), (b), (b2) and (c).** Source: probe note PN-4 (P4).
- Adopted: send "gpt-5.4-mini" as recorded. Each output must be served as the run's recorded snapshot ("gpt-5.4-mini-2026-03-17"); otherwise the probe stops for a dated note.
- Why B: the served-model check fixes which model produced each output, whatever id is sent.

**B10. Key profiles for the (b) cut.** Source: probe note PN-6 (P5).
- Adopted: `_key_profile`, with the aliases from the recorded prompt line and the other fields from the run's `state.json`.
- Why B: it rebuilds each definition as it stood at the call, as far as the trace records it. Aliases are the only field the code changes after creation. The alternative adds later aliases, which can add or remove candidates in either direction.

**B11. The recorded call per case.** Source: probe note PN-7, both items (P1).
- Adopted: the last extraction call on each cited span by checkpoint k; with several cited spans, output j is the union of their j-th outputs; a span that several cases of one run cite at the same recorded call is re-extracted once per condition and repeat, and serves each case.
- Why B: the control and every condition use the same recorded call, so the choice fixes the case's input, not the comparison. The union follows the `carried` step, which passes on any claim (`23-loss-trace.md:35`). A shared input re-extracted once is the same input.

**B12. Which cases (d) runs on.** Source: probe note PN-10 (P8).
- Adopted: (d) runs where (b) and (b2) are both *not recovered* (k = 0), and the control has an output.
- Why B: only these cases can reach the mapping rows that use (d) (lines 279, 280). On any other case, (d) gives "no probe evidence" (line 281). The reading changes spend, not codes.

**B13. "A key holding the gold value".** Source: probe note PN-11 (P7).
- Adopted: a key of the recorded prompt under which the run's final dump stores a fact carrying the value (strong match or adjudicated); otherwise "none in the run".
- Why B: a descriptor recorded with the cut size (line 243). It decides no result.

**B14. Probe procedure.** Source: probe note P6, P11, P12, P13.
- Adopted:
  - (b2) reuses (b)'s cut and its recorded vectors (P6);
  - cases in sha256(run_id|fact_id|k) order; within a case, conditions interleaved repeat by repeat; all conditions of a run in one period (P11);
  - (b2) runs on a changed 3b prompt only after a dated note with the new hashes (P12);
  - if the budget guard is used, its price table lists exactly the three requested model ids (P13).
- Why B: each keeps the conditions' inputs and timing equal, or keeps the run from stopping on an unpriced id. None can favour a condition.

**B15. The pre-coder's channel.** Source: template point 2.
- Adopted: a workflow subagent started in a clean directory outside the repository, with every transcript audited (blindness check 4). The fallback is the Messages API, on its own estimate and go-ahead.
- Not available: the adjudication channel as configured. Its transcripts show the memory index, git status and tool calls (template, R4), against line 402: "The model pre-codes every case from the page only, in a fresh context with no repository memory or result reports."
- Why B: any channel that passes the audit gives the same input; the audit secures line 402.

**B16. Arm and series on the case page.** Source: template point 3.
- Adopted: state them explicitly.
- Why B: the arm is not a sealed output, the rules need it (lines 309, 357–359, 364, 368, 376), and the neutralised reasons already show it (template 6.1).

**B17. How "held: conflict decision" is recorded.** Source: template point 7.
- Adopted: a separate field `held`, with `class` forced to "unclear" by the schema.
- Why B: a representation. Held cases are scored as unclear either way (line 359).

**B18. Sub-causes for non-implementation classes.** Source: template point 12.
- Adopted: add "not applicable" to the schema's sub-cause values for non-implementation classes before the template hash is recorded. The pilot may still give sub-causes for every class.
- Correction: the builder recommends (a), with "not applicable" added before signing only if the pilot list does not cover every class. The pilot comes after signing (lines 400–401), so that is not known when the template is fixed.
- Why B: it only keeps non-implementation codes out of 3b's "share of cases that fit no frozen sub-cause" (line 305), as either builder option intends. It changes no class.

**B19. Where the Phase B bug descriptions live.** Source: template point 13.
- Adopted: Part F of the prompt only, verbatim from the code summaries at 3320375.
- Why B: it keeps the result figures of `22-bug-list.md` out of the pre-coder's input (line 402) and changes no rule.

**B20. Pre-codes after a codebook revision.** Source: template point 15.
- Adopted: re-run all pre-codes with the revised sub-cause list, and keep both sets hashed.
- Why B: the candidate causes (line 406) and the copy check (line 430) then compare codes made under one codebook. It favours no class.

**B21. How the register sheets reach the pre-coder.** Source: template point 16.
- Adopted: a fixed pre-coder extract, filled into the template at signing and covered by its hash; record the hashes of the extract and of the filled template.
- Why B: both forms carry the same text. This one keeps line 402's "frozen sub-cause list is its only added input" literal, and the coder still quotes the design text in its record (line 326).
- Note for building the extract: sheet K1 pointed to line 340's condition as quoted above. That quote is in the register's block of rules for every sheet, which the extract does not carry. The prompt quotes line 340 in its Part A5, so the pre-coder still gets the text; the extract should not point "above".

**B22. Decision pointers on the sheets.** Source: template point 17.
- Adopted: resolve every "decision N" pointer by the signed answer in the signed register sheets themselves, before hashing; build the page checklist (line 397) from the same text, so the author, V4 and the pre-coder see one text.
- Why B: it writes the signed answers into the sheets; the outcomes are the same, and the pre-coder applies no conditionals.

**B23. "Cases with no pending alternative"** (line 428). Source: template point 21.
- Adopted: report as primary the measure that counts only pending entries that do not set caused-at alone, and report beside it the measure that counts any pending entry.
- Why B: both are reported, and neither enters a decision rule. The 0.60 target applies to the author's blind binary kappa with V4, and the 0.40 rule to the lower of two lower 95% bounds, the author's blind binary kappa with V4 and with the pre-codes (line 430 as changed on 28 October; C66).

**B24. V4's packet rule for the audit.** Source: AL-5.
- Adopted: fix it now, in the signing note: fields id, fact_id, gold value, its gold status, aliases, text, contexts; roles, decides_rows and recorded_result_rows excluded; order by ascending SHA-256 of "<salt>|<id>", with a fixed salt stated in the signing note; no repository access for V4 (template Section 9, AG1 and AG2). The gold status was added on 28 October, so that the standard's ruled-out bullet can be applied (review finding L3-3).
- Note: the pages V4 codes at Step 3 item 5 show steps and sub-codes that rest on v1, so the audit at item 6 is partly exposed. The order is fixed (lines 399–410); disclose it with the agreement.
- Why B: it implements "shuffled and unmarked, blind to the v1 label" (line 410); fixing it early favours no result.

**B25. Where the audit list's hash is recorded.** Source: AL-7.
- Adopted: in the signing commit message and the annotation of tag `plan23-amendment-1`, with the script's hash beside it (now: list dfef6f31…49436, script 5ac36e22…debff; both change if C18 or C20 adds decisions). Not in the run manifest or the register files, whose hashes the template's page-provenance check admits. Also name the audit list in that check's exclusion of "any audit or v2 file" (template, "How blindness is checked", item 1); done in the template's second review (finding X10; template Section 7, point 23).
- Why B: a record location. Every later output cites the tag (line 14).

**B26. Validation check 9 of the pre-coder output.** Sources: the template's review of the completion pass (MX-F7); its second review (R2-5).
- Adopted: keep the template's Section 4, validation check 9, which is outside the prompt: a pre-code names no "settle" step on A0, and no "type check", "same-meeting conflict and new-evidence rules" or "support check" on A0, A1 or A1-ref, which runs no contract (line 533). For the final configuration the check tests none of the three steps, since the page states which contracts were admitted. Template A5 marks "settle" as not in A0, and the three contract steps as in A2, and in the final configuration where the page states that the step's contract was admitted. The check covers the settle mark and the contract steps' marks on A0, A1 and A1-ref; MX-F7 named only the settle step on A0.
- Why B: it rejects a record that names a step its arm did not run. Such a record is invalid under A5, and R7 repeats the call once. It changes no class. The check itself changes neither the prompt hash nor the schema hash; R2-5's edit of A5 changed the prompt hash (template Section 1).

---

## A. Settled by the amendment

**A1. Chapter 4 text outside D1–D9** (Annex: Final Artifact, Operational Limits, the domain-records and requirements tables). Source: register decision 6.
- Answer: not design entries; context only. The model grounding pass therefore has no 94c049d design entry (sheet R).
- Lines: 102 (design entries are "the Ch. 4 decisions"); 6 (D1–D11 name those decisions).

**A2. Code docstrings and comments.** Source: register decision 7.
- Answer: not design entries; the register records them as implementation entries. Conformance is applied through the sheets' conformance checklists, which hold design requirements only (register, "What a sheet is", item 5).
- Lines: 102.

**A3. The expansion generator and D4.p3's inputs.** Source: register decision 16.
- Answer: criterion (ii) does not apply to expansion-routed misfilings. The generator's inputs stay on sheet K2 as an implementation entry.
- Lines: 251: "They are coded from the trace, under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry."

**A4. `thesis/discussion.tex`.** Source: R-17.
- Answer: excluded. It is not `\include`d, and its header marks its claims as not current.
- Lines: 109: "One row per causal claim the thesis text now makes about where or why the system loses information."

**A5. The read contract in Phase C.** Source: M-1.
- Answer: no Phase C contrast, no development verdict, not admitted. Adding a contrast would need a dated note (line 16).
- Lines: 512–525 (the admission rule gives it no route); 522 (only *works* is admitted).

**A6. Epistemic status as a mechanism.** Source: M-2.
- Answer: mapped. Line 114's parenthesis does not remove it.
- Lines: 13: "Everything not changed here is unchanged."; 122 removes only restraint from plan 23's list (plan 23:343).

**A7. Held cases in the conflict contract's own bound.** Source: M-8.
- Answer: held cases count as unclear in every bound, the conflict contract's included. The consequence is C40.
- Lines: 359: "count as unclear in every bound"; 460: "Cases coded implementation because the mechanism under test is their alternative are that mechanism's measured effect." A held case is not coded implementation.

**A8. WD's criterion (iv) on non-current rows.** Source: M-12.
- Answer: (iv) applies to every case with the sub-code, ruled-out rows included; the Step 2c endpoint stays current rows. Ruled-out (iv) cases are listed apart.
- Lines: 350–352 (WD cases are defined by the sub-code alone); 288 (the endpoint).

**A9. The scope of (b2).** Source: probe note PN-1.
- Answer: (b2) replaces the AMI role examples only. Disclose that no probe tests the product wording.
- Lines: 244: "in place of the AMI role examples".

**A10. (b2) on the 3b run, and the label of a (b2)-only recovery there.** Source: probe note PN-3, both items.
- Answer: (b2) runs on the 3b run. A (b2)-only recovery takes the mapping's sub-cause "out-of-domain examples"; the 3b report discloses that the role examples are in-domain on ES2009, and lists such cases apart.
- Lines: 238: "On the Step 5 run that 3b codes, only probe (i) runs."; 244 ((b2) is part of probe (i)); 272: "The sub-cause is registry-conditioned extraction, or out-of-domain examples."; 305: "with no revision".

**A11. `admitted:span_not_seen` cases.** Source: probe note PN-8 (P2).
- Answer: listed apart, with no probe output. None exists in the probed EL2020 runs. The template's table C2 was aligned in its second review (finding X7; template Section 7, point 22).
- Lines: 241: "The cited span is re-extracted"; 242 (the control is the recorded prompt, which these cases lack); 281 (no probe evidence).

**A12. Missing probe outputs.** Source: probe note PN-12 (P10).
- Answer: a repeat with no valid output after the client's attempts and three re-issues is *no output*, never a failing repeat. The re-issue count is procedure.
- Lines: 338 ("no output" means not ruled out); 344: "inconclusive, not reproduced or no output, for a probe or WD alternative: the code is implementation defect or unclear".

**A13. Loss-trace defect flags on A0 pages.** Source: template point 4.
- Answer: withheld from the page, and compared with the pre-codes afterwards.
- Lines: 390–397 (the page items; the blind page prints no flags, template 6.1); 309 (model pre-coding and defect flags are separate A0 inputs).

**A14. The status "not ruled out: no output".** Source: template point 5.
- Answer: adopted for an alternative that applies but whose sealed output will never exist (for example, any probe on A0).
- Lines: 341 (pending only where a sealed output decides); 238 (no probe on A0); 338: "it is not ruled out, and the code is implementation defect or unclear."

**A15. Which sealed outputs exist for which case** (template C2). Source: template point 6.
- Answer: the three readings stand: the offline reading check covers `key_reached` cases in every arm; the routing probes cover cases whose page shows a misfiled carrier or rival, except expansion-routed ones; the four leave-one-outs are pending for EL2020 A2 cases surfaced at or before status.
- Lines: 216 (no arm named); 251–252, 257; 222–223, 376.
- Note: the third reading includes extraction-surfaced A2 cases, which no leave-one-out can move (C39). This changes only the second measure of B23.

**A16. Key definitions on the page.** Source: template point 8.
- Answer: the key history shows each involved key's registered definition at the time.
- Lines: 375: "the one whose matter does not fit the key's definition"; 392 ("the key history" is a page item).

**A17. Pre-codes sealed until pass 1 is committed.** Source: template point 10.
- Answer: sealed.
- Lines: 403: "Author pass 1, blind"; 430: "V4's blind binary agreement and kappa with the model pre-codes are reported beside the author's with each", which needs the author's codes made without them.

**A18. Which A0 cases are pre-coded.** Source: template point 11.
- Answer: all lost cases of the three A0 runs.
- Lines: 402 ("every case"); 459 (A0's shares come only from the pre-codes).
- Note: no probe runs on A0, so A0 pre-codes at extraction and routing will mostly be unclear by construction (template section 7, closing note).

**A19. Counts and mapping quotes in the extract.** Source: template point 18.
- Answer: the extract carries no run counts, incidence figures or "Already read" items; parameter values stay. It also omits the probe mapping (lines 271–281), which cannot change a pre-code, since probe-decided items are pending (line 341).
- Lines: 402 (no result reports in the pre-coder's context); 54 ("313 of 534" is on the sheets and on the "Already read" list); 107 (parameter values are implementation entries).

**A20. The burden for evaluation-defect and transcript cases.** Source: template point 19.
- Answer: as the template now does. Evaluation defect is decided first, and only items on the caused-at sheet can make a case unclear for lack of output. The stricter earlier rule would need a dated note.
- Lines: 334, 338, 16.

**A21. An A0 case resting on a Phase B bug whose design ground is retrospective.** Source: template point 20.
- Answer: line 309 takes precedence: implementation defect, basis "Phase B bug".
- Lines: 309: "A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound."; 27 (repaired, for A0 only); 348 is the general rule.

---

## X. The cross-package check of 27 October: where each finding stands

The check raised findings X1 to X14 across the package files. The completion pass, its review and the second review resolved some of them. The others are entries above.

| Finding | Where it stands |
|---|---|
| X1. No package file lists the V4 coder as open. | Entry C2. |
| X2. No file records the audit list's hash. | Entry B25. Now: list dfef6f31…49436, script 5ac36e22…debff. |
| X3. The probe note's decision ids D1–D14 clash with line 6. | Resolved in the probe note's completion pass: they are PN-1 to PN-14. This sheet uses the new ids. |
| X4. The label V4 names both a Rule V item and the second coder. | Resolved in the claims completion pass: the items read "Rule V item N". |
| X5. Template step names differ from the register's Chain lines. | Resolved in the template's completion pass. |
| X6. The scope of the line-340 condition. | Aligned per step in the template's completion pass. One step is left: entry C62. |
| X7. Probe (i) and `admitted:span_not_seen` cases. | Follows A11 (PN-8). Resolved in the template's second review: table C2 excepts these cases from probe (i) (template Section 7, point 22). |
| X8. Register decision 2 and R-4 decide one question. | Signed together as C8. |
| X9. M-17 needs a definition the probe note lacked. | Resolved: the definition is drafted in the probe note. Entry C41. |
| X10. The audit list in template blindness check 1. | Follows B25 (AL-7). Resolved in the template's second review: check 1 names `23-am1-audit-list.json` among the files that fail (template Section 7, point 23). |
| X11. Working-tree citations of plan 23 and the bug list. | Entry C63. |
| X12. Template A1's gloss on the harness reviewer. | Resolved in the template's completion pass (register K2.6c). |
| X13. Mode notation. | Open; the completion pass did not touch it. The register writes mode `—` for trace steps whose mode is JSON null (its lines 97, 143, 469, 470, 712 and 993). `23-am1-prompts-evaluated.md` prints "none" for the same steps. It is notation only and decides no code. Align it, or state in the register that the two mean the same, when B22's sheet edits are made. |
| X14. Two line ranges. | Resolved in the claims completion pass: "Already read" is amendment:33–63, and the WD-cases rule is amendment:350–356. The template's 33-63 was already right. |

Reported by the template's completion pass, not a decision: sheet R says "question routing" where the register's R.1 Chain line says "question resolution". The template uses the Chain name. Align sheet R when B22's sheet edits are made.

---

## Record

**Update after the completion pass (27 October 2026).** Made offline: no model, embedding or network call; `.env` not opened; the `app` package not imported; git state not changed. Only this sheet was edited. Its SHA-256 before this update was 5134ce959aaadd41e1e9ff0d47ec6372f17d0aab7cbff546b04774fdeca91627. What changed:
- C43 is rewritten (findings VI-RM-12, VD-RM-16): Rule M is drafted, the question is when it is fixed, and the entry lists Rule M's 15 choices and three sub-questions, C43.1 to C43.3.
- C41 is rewritten: the question is whether to sign the probe note's drafted definition, with its seven choices and its smaller details.
- The probe note's decisions are cited by their new ids, from the rename table in the probe note's completion pass: line 10, C21–C25, B9–B13 and A9–A12. Every other D-number in this sheet is a Ch. 4 decision, one of its paragraphs, or plan 23's "D1" for WD (B1), and is unchanged.
- C1: the M-19 item now names Rule M; new pre-tag items for C41, C62, C63, findings X7 and X10, and the line pointers.
- C2: the audit-list size under each option of C18 and C20.
- Mirrors of the claims review: C28 (VI-RM-9), C29 (VI-RM-10), C30 (VI-RM-16), C38 (VI-RM-14), C44 (VD-RM-3, option (d), and the pinned arithmetic).
- New entries: C62 (finding X6, with MX-F8), C63 (finding X11), B26 (MX-F7), and section X. A note under B21; C4 (b) and A11 extended.
- The file table, the template's hashes and the counts are refreshed.

Checks (scratch scripts in the session scratchpad, folder `step0/verify/decisions/` and `step0/complete/sheet/`, not part of the package):
- Quote check (`qcheck.py`, run unchanged): every quotation of six or more characters is found verbatim in the amendment, the design text, the register, the claims register, the probe note, the template, the audit script, plan 23 or the scratch copies of the bug list and the expansion service; 0 missing. Two quotes of this update failed at first and were reworded.
- Line checks (`linecheck.py`, `linecheck2.py`): every quote attributed to an amendment line occurs at that line. The loose pattern of `linecheck2.py` also pairs some line numbers with quotes from the register, the template or another line; each such pair was read, and none is a misattribution.
- Every Cn, Bn, An, R-n, M-n, AL-n and PN-n id, and every register decision and template point, cited in the package's Markdown files resolves (`ids.py`).

**Second review (27 October 2026, 17:11 CET).** Second review round of the Step 0 package; only defects were applied. Made offline: no model, embedding or network call; `.env` not opened; the `app` package not imported; git state not changed; no endpoint, family, verdict or owner-claim result computed or looked up. Only this sheet was edited. Its SHA-256 before this round was 7b63c96eac159b8dc780c0d2787a46f5321f0e765fe157fcf26fb3443d5dfa7f.
- Findings on this sheet:
  - **m-integrity:R2-05** (C35 and M-11 said a wrong-meeting value cannot weaken evidence and provenance under C35 (a)). Applied in C35, merged with RM2-11: under (a) such a value weakens only through the 20% pass sample and the pass share (Rule M item 2). The M-11 part is not applied, because this round could edit only this sheet; C35 now states the mismatch, and it is left for the author.
  - **m-code:RM2-11** (the same contradiction, and the reach of (b)). Applied, as the better fix, in C35: (b) examines every evidence row that passes the status step; in both options a wrong-meeting value can move only a credited evidence question (the works bound). The M-11 part, including its "by a dated note", is not applied, for the same reason.
  - **owner-code:R2-OWN-4** (C1 said the probe note cites M-17 at a register line). Applied in C1, merged with R2-1: the probe note cites M-17 by heading (probe note:358), so that pointer needs no line check. The proposed dated line under the probe note's MX-F2 record is not applied, because this round could edit only this sheet.
  - **sheet:R2-1** (the same stale item, and the probe-note hash row). Applied in C1, as above. The probe-note row of the file table is refreshed. The dated line under MX-F2 in the probe note is not applied, for the same reason.
  - **sheet:R2-2** (C1's list of package edits was presented as closed and missed edits other entries place before signing). Applied, as the better fix: the item now covers every package edit or check that an entry places before signing, at signing or with the package, and names C8's Correction 2 (under (a)), C17's tag alignment and B8's coldstart check; C21's item now reads (b), (c) or (ii). No new author choice.
  - **sheet:R2-3** (C63's list of entries citing working-tree lines of plan 23 omitted C43). Applied: C43 is added. Its line, plan 23:344, has the same text at b4d6b6c line 305, which option (c) would re-cite.
- Mirrors of the other files' second review:
  - Claims register (Rule M and M-20): C43 option (a) now says that the Step 3 codes and the Step 2, 2b and 2c outputs do not exist yet and that the frozen loss trace does; C43's brief choices 9, 11, 12 and 15 now match mapping section 7a's list (9 gains the uncoded-pool clause, 11 is keyed on the share's base and its source runs, 12 names the share's base, the full bootstrap, the single- and multi-value definition, the pass test and the rows examined in full, and 15 the readings under C31 (b), C32 (b) and C44 (c)); C44 options (a), (c) and (d), its bootstrap sentence and its sentence on share 1 follow M-20 and Rule M item 5; C43's sources name the second review. The claims fixer's reading of the base for Step 5's borrowed shares (the cases of 3b's coded run) is shown in choice 12, so it is adopted by answering C43.
  - Probe note: C41's choice 6 now gives the one rule of "Not covered by WD" and the set listed apart under each threshold of choice 5; C41's sources name the second review.
  - Template: B26 now gives A5's marks of the three contract steps (A2, and the final configuration where the page states the contract was admitted) and check 9's exclusion of those steps on A0, A1 and A1-ref; C1, A11, B25 and section X (rows X7 and X10) record findings X7 and X10 as done in the template's second review; the template's prompt hash in the file-table line is 5345f42e…b7aea2.
- New: the subsection How to sign, with the thirteen entries that need the author's own fact or preference (C1, C2, C3, C4, C6, C25, C43.3, C48, C50, C53, C55, C56, C63), from the second review's triage, each checked against its entry and the amendment lines it cites (582, 598, 601, 63, 137, 140, 147). The bullet on signing under What this sheet is now says the same. The second review marked no recommendation unsound, so none is listed to read before accepting, and no recommendation was changed.
- The file table is refreshed at 17:11 CET. Changed since 16:16: the claims register, the probe note and the template; the other ten files are unchanged. Counts unchanged: C 63, B 26, A 21.
- Checks (scratch scripts as above; working copies in `step0/reverify/`):
  - Quote check (`qcheck.py`, unchanged): 150 quotations, this record's included, 0 missing. One failed at first, the name of this sheet's own new subsection in quotation marks, and was reworded.
  - Line checks: `linecheck.py` pairs 18 quotes with amendment lines, all at their line. `linecheck2.py` gives the same seven loose pairs as the copy of this sheet from before this round; none is new.
  - `ids.py`: every id resolves; the sheet defines 63 C entries (66 ids with C43.1 to C43.3), 26 B and 21 A.
  - `23-am1-check-register.py`: exit 0, errors 0, output identical to its previous run.
  - The amendment's SHA-256 is 0236ef0385b96012d08e7bcd10a8ec71e436253cb58948d85da4ba563fb81889, unchanged.
  - `hashes.py` recomputes the template's prompt hash as 5345f42e645a3a7e10687ad7447d0bece39f38f0e84993c7b0e18b39dfb7aea2 (60,362 characters) and its schema hash as e790d1a6c0f3e213ac3676c26605b379c74278bde5c6bbe96b0d9ded09bfd96d, both equal to its Section 1.
- Left for the author (outside this file): the claims register's M-11 wording; a dated line under the probe note's MX-F2 record, which still names the former line pointer.

**Main session sync (27 October 2026, evening).** C35's 'Not mirrored yet' bullet is removed: the claims register's M-11 now matches C35 and Rule M item 2. C44's recommendation no longer calls option (a) conservative (it gives share 0 on a small base whose items are all clean). The file table's rows for the claims register and the probe note carry their hashes after these edits.

**Author's answers (27 October 2026, evening).** Only this sheet, the claims register (one answer line under R-2) and plan 23 (Phase F, item 1) were edited. Made offline: no model or network call, and git state not changed. This sheet's SHA-256 before this update was f7ed611a05c9848703ffbbbadca1aeabe9c166cef06837dcc822ba28f4cfdc6f.
- C1 (a), C2 (a), C4 (b), C25 (a) and C63 (a) are answered with their recommendations. C2's name and date, and C4's scan for secrets and archiving, are still open, so the pre-tag items are not complete.
- Plan 23, Phase F, item 1, now runs after Phase E, so the thesis is rewritten once, at the end. In consequence:
  - C43.3, C48, C50, C53, C55 and C56 are not needed for signing and are answered in Phase F;
  - C46 keeps (b), but its fixes are applied in Phase F;
  - C47 keeps (a) as a decision, applied in Phase F.
  - The integrity point of R-2 is met by the P0 content being fixed at ce75b1f, before any outcome.
- No cited line moved: the package cites no plan 23 line after 375, and the edit replaced lines 375–377.

**V4 decided (27 October 2026, evening).** C2 is answered with a machine V4: Google Gemini in the Gemini app. Amendment draft 6 changes lines 3, 116, 405–407, 430, 432, 583 and 612 in place, so every cited amendment line keeps its number. Template Section 9 is new; the prompt and schema hashes are unchanged. `23-am1-v4.py` is new: it builds the packets and collects the answers. It was tested on the real audit list (430 decisions, 8 packets, every one with a context) with a test salt, and on mock case pages, in the session scratchpad. No API call was made.

**V4 due date (27 October 2026, evening).** The author set it: seven days after the 3a case pages and the sub-cause list are both frozen. A relative date is the date set at signing (amendment line 432); a dated note fixes the calendar date.

**V4 channel (27 October 2026, evening).** The author will run V4 in Google Antigravity, an agent environment, not the Gemini chat app. Antigravity agents have file, terminal and browser tools, so each packet is staged alone into a clean workspace outside the repository (`23-am1-v4.py stage`, which refuses any other location or file). The conversation's only message is a fixed instruction, and any other tool use voids the answer. Template Section 9, amendment lines 3, 116 and 583 (in place) and the script were changed. The stage and collect refusals were tested in the session scratchpad.

**Main session sync after draft 6 (27 October 2026, late evening).** Checked against draft 6. C26 and B-entry text on V4's selection now names the candidate causes of line 406, since V4 codes every case. A17 now quotes draft 6's line 430. The template's prompt no longer calls V4 human (its Section 9 record; prompt hash `fd7e2f6b…`). C46's recommendation and the claims register's R-2 recommendation no longer quote plan 23's former Phase F heading. No answer changed. Three amendment lines are left for the author, because the amendment is the author's text: line 405 still says each case is coded in a fresh chat; line 419 still sends pass-2 implementation cases to V4, which has already coded every case blind; line 430 still weights for over-sampled strata, which V4 no longer has, and does not say whether the lower of the two author agreements replaces the author–V4 kappa in the 0.40 rule.

**Amendment lines 405, 419 and 430 (28 October 2026, author's go-ahead).** Edited in place, line count unchanged: line 405 says a new Antigravity conversation per case; line 419 says that cases pass 2 newly codes as implementation already carry V4's blind code and are reported apart; line 430 drops the weighting for over-sampled strata, which no sample has any longer (line 308 takes 30 cases per run, line 311 ten), and says the 0.40 rule then takes the author's binary kappa with V4 or with the pre-codes, whichever has the lower 95% bound. Line 3 lists the changed lines.

**Review round on draft 6 (28 October 2026).** Five reviewers (validity, blindness, the script, consistency, a cold read), a skeptic for each and a completeness critic (workflow run `wf_17dc1094-fbf`, 12 agents). 54 findings: 46 survived, 8 refuted. 10 survivors blocked signing, and they came down to three faults: the known-answer set counted 17 trace rows where the case unit gives 11 cases, so its bar of 14 could never be met, and its expected answer was not established; V4 could run before pass 1 while the author, who runs it, sees its answers; V4 had no instrument for item 8's re-codes. The main session decided these as C64 to C67 (recommendations, applied, open to the author) and edited the amendment in place (lines 3, 116, 405–407, 411, 414, 430, 432, 572 and 583; 623 lines, none moved). Fix pass (`wf_d914f894-e2d`, 5 agents): the script and template Section 9 were rewritten to one agreed interface, each checked by a verifier and both by a cross-check; their follow-ups were applied by a second script pass (`wf_7901e997-9ae`, a fixer and a verifier; 248 end-to-end checks pass) and by the main session in the template, the amendment (lines 414, 583) and this sheet (C65, C67). Also corrected: C63's answer said no cited plan 23 line moved; the Phase F edit moved later lines by one, and the claims register's cite of the reference-informed arm now reads line 444. No API call was made.

**C67 answered (28 October 2026).** The author chose (a): V4's due date is seven days after item 4's commit. C2's due-date paragraph, How to sign, C1's open items and template Section 9's Timing are updated.

**Pre-tag pass (28 October 2026).** The author asked that every remaining decision take its recommendation. The main session re-ran the audit list (C18 (b), C20 a_shared: 479 decisions); a workflow (`wf_12f53368-49a`, 10 agents) applied B22, C8, C17 and C62 to the register, B8 to the claims register, C8's Correction 2, C62, B18 and B21 to the template with the new extract, and wrote the package check (B3), each verified by a reviewer and a skeptic; a follow-up pass (`wf_55666b1e-eee`) made V4's check 7 accept "not applicable" (B18), committed the extract builder, and hardened the package check. C4's records are archived. The author's own jobs are listed in `23-am1-author-tasks.md`. No API call was made.
