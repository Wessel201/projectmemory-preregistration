# Claims register

Plan 23, amendment 1, Step 0. **Draft for signing** with the amendment. Assembled 27 October 2026, offline: no API calls, no network access, and no existing file changed.

## 1. What this register is

- **What the amendment asks for.** It asks for the register in Step 0, second bullet:
  - "**Claims register.** One row per causal claim the thesis text now makes about where or why the system loses information. Each row gives:" (amendment:109);
  - "the claim and its location;" (amendment:110);
  - "the result here that would confirm it, and the one that would overturn it;" (amendment:111);
  - "the text action in either case." (amendment:112).
- **It carries the mechanism mapping** (section 9). "It also carries the mapping from boundaries and sub-causes to the mechanisms (complete decisions, change and supersession, rejection, evidence and provenance, and each contract). **The mapping signed here governs every Phase C verdict.** The Phase D3 registration may revise it for Phase D only, in a dated note." (amendment:114)
- **Rule** *(gloss of amendment:114)*:
  - The mapping in section 9, as signed with this register, governs every Phase C verdict.
  - The Phase D3 registration may revise it, for Phase D only, and only in a dated note.
  - Such a revision changes no Phase C verdict.
- **When it is filled in.** One output of Step 3 is "the claims register filled in." (amendment:449).
- **Line numbers.**
  - Every `file:line` below refers to commit `b4d6b6c42f1f67cea9c3ac842de8fbef87e73fd2` (b4d6b6c, HEAD on 27 October 2026).
  - `git diff --stat HEAD -- thesis/*.tex thesis/generated` is empty, so the working tree has the same lines.
  - Exception: notes files that are untracked or carry uncommitted edits are cited at their working-tree lines of 27 October 2026. These are the amendment, plan 23 (`23-plan-development-and-confirmation.md`, SHA-256 in section 9's inputs table), `22-bug-list.md` (SHA-256 2096a1f405c127dab59b821ce008bd840761973bc5a7511ed3ab3aa305bc8fd6), `23-loss-trace-results.md`, `23-el2020-arms.md`, and the codebook and script of the loss trace (`23-loss-trace.md`, `23-loss-trace.py`, hashes in section 9's inputs table). Lines 1–122 of `22-bug-list.md` are the same at b4d6b6c; its later lines and the cited lines of plan 23 are not. The design-and-controls register cites plan 23 and the bug list at their commits instead. (Added in the cross-package consistency pass of 27 October.)
  - A row's line is the line where its quote starts.
- **Not blind.** The amendment "is **not blind.**" (amendment:15).
  - Many rows cite figures from the frozen loss trace and from the reviewer counts listed under "Already read" (amendment:33–63). These are marked "Already read".
  - On those rows the outcome is partly known at signing, and the row says so.
  - The sweeps computed or took these figures. This assembly did not recompute them.
- **Two amendment rules limit every text action:**
  - "any statement that a loss comes from the design, made only where the codes say architectural or trade-off on 94c049d text, with the binary kappa's lower bound at or above 0.40" (amendment:572, which since 28 October adds that line 430's rule takes the lower of the author's two blind bounds);
  - "A retrospective entry can never ground architectural weakness or a trade-off, nor rule out an alternative." (amendment:347).

## 2. Sources and conventions

**Inputs.** Three sweeps of the live LaTeX at b4d6b6c, and the mechanism mapping:
- abstract and Ch. 1 (`thesis/main.tex`), Ch. 2 (`thesis/problem_domain.tex`), Ch. 3 (`thesis/background.tex`) and Ch. 6 (`thesis/conclusion.tex`): 59 rows, no dormant claims;
- Ch. 4 (`thesis/implementation_chapter.tex`) and the appendices (`thesis/appendix_reproducibility.tex` with the generated tables it inputs, `thesis/appendix_walkthrough.tex`, `thesis/appendix_design_evidence.tex`): 46 rows and 6 dormant entries;
- Ch. 5 (`thesis/eval.tex` with the generated tables it inputs): 48 rows, no dormant claims;
- the mechanism mapping, copied into section 9 unchanged in substance.

That makes 153 sweep rows. Nine pairs are merged, so the sweeps gave 144 rows. The review of 27 October added seven rows with suffixed ids (C37a, C75a, C98a, C130a, C133a, C136a, C138a), so the register has 151 rows (section 10).

**Not swept.** `thesis/discussion.tex` is not `\include`d. Its header says "% Retained as historical source. Its old claims and placeholders are not current." (thesis/discussion.tex:2). See decision R-17.

**Quotes.**
- Each quote is the LaTeX source, verbatim.
- Source line breaks are shown as single spaces, and `[...]` marks a cut.
- Quotes are printed in code blocks, so that LaTeX quotation marks (two backticks) survive.
- Dormant quotes keep their line breaks and `%` signs.
- Text in quotation marks outside the code blocks is verbatim too, cited as `path:line`.
- Proposed new wording is not a quote. It is labelled "proposed:" and carries no `path:line` after it.
- **Checked against the source.** On 27 October every quote (153) and every dormant entry (6) was checked against the files at b4d6b6c: each fragment between cuts was found in order, starting on the cited line. Ten quotes were also checked by hand with grep. Corrections against the sweeps:
  - four line numbers, where the quote starts at the end of the previous line or on the next line: main.tex:142 → 141 (C06), implementation_chapter.tex:607 → 608 (C46), conclusion.tex:236 → 235 (C121), implementation_chapter.tex:610 → 611 (C47, corrected in the review of 27 October);
  - four dormant quotes that the sweep had cut mid-line without a mark now carry `[...]` (dormant 1–4).
- The quotes added in the review of 27 October were checked the same way, with a check that also requires the first fragment of a row quote to start on the cited line (section 10).

**Glosses.** These are glosses, not quotes:
- each row's "Claim" line;
- the short titles in the index;
- the wording of the other fields (the sweeps' and this assembly's).

**Order and ids.**
- Rows C01–C144 are in thesis order: abstract, Ch. 1, Ch. 2, Ch. 3, Ch. 4, Ch. 5, Ch. 6, Appendix A, Appendix B, Appendix C. This is the `\include` order at thesis/main.tex:189–205.
- A suffixed id (C37a) is a row added in review. It sits in thesis order after the row with the same number.
- Within a file, rows follow the line order.
- A generated table sits at the line that `\input`s it.
- A merged row sits at its first location.

**Merged rows and repeated claims.**
- Nine pairs state the same claim with compatible tests. Each pair is one row listing both locations: C04, C05, C81, C83, C84, C85, C87, C88 and C93. The review of 27 October added a third location to C05 (eval.tex:1089).
- Some claims recur with a different scope, a stronger wording, or a test the sweeps set up differently. Those rows stay apart and carry an "Also stated at" line.
- Section 5 lists every claim stated in more than one place. The thesis aims at one home per claim, so each group there is a candidate for consolidation.

**Fields of a row:**
- location (file:line, label);
- claim (gloss), with the verbatim quote;
- where/why;
- boundaries: the amendment's components (admission, extraction, key assignment at extraction, key resolution and expansion, state rules, reading), plus "evaluation" or "transcript" where the sweeps used them;
- mechanisms: the names of the mapping (section 9, mapping section 1);
- confirms if; overturns if;
- text action if confirmed; text action if overturned;
- testable here (yes, partly, no);
- note; also stated at.

**Sizes.**
- The sizes in "confirms if" and "overturns if" ("most", "large", "few") are proposals. Decision R-1 asks how they bind.
- Two sizes are the amendment's own:
  - "at least 3 distinct values" net is the admission measure (amendment:516);
  - "unclear at most 10%" is the stopping rule (amendment:442).

**Abbreviations:**
- A0, A1, A2, WD, R, E+R, E+R\* and A1-ref are as in the amendment (amendment:5–10).
- Probes (i)(a)–(d), (ii-r), (ii-h) and (iii) are Step 2b's (amendment:233–281). (iv) is criterion (iv) of the implementation-choice class (amendment:325), applied by the WD-cases rule (amendment:350–356). The Step 2c rule is the one headed "WD rule, fixed here" (amendment:289–296).
- "Bug n" is row n of `22-bug-list.md`.
- P0-A to P0-E are in `22-fix-priorities.md`, each glossed by its heading:
  - P0-A: the restraint "gate";
  - P0-B: the validity of the restraint test;
  - P0-C: the transfer diagnosis;
  - P0-D: design consequences written after the outcomes;
  - P0-E: the "kept the intermediate records" claim and the flagship trace.
- "D4.p5" and similar ids are paragraphs of `23-am1-design-text-94c049d.md`, the Ch. 4 decisions as worded at 94c049d (9 September).
- **Retrospective** means written after 9 September. D10 and D11 entered at 5de9911 on 19 October.
- The **bug-11 coder** is the lexical failure coder behind `20-failure-funnel.json` and `20-failure-cases.json`. It is read through `20-transfer-pack.py:221-224`.

## 3. Index

Locations are relative to `thesis/`. Short titles are glosses.

| Id | Location | Short title (gloss) | Where/why | Testable |
|---|---|---|---|---|
| C01 | main.tex:70 (abstract) | Both arms fail every change and rejection list | where | partly |
| C02 | main.tex:72 (abstract) | Few evidence links fully support their fact | where | no |
| C03 | main.tex:73 (abstract) | Embedding candidates give restraint, not recall | why | partly |
| C04 | main.tex:74 (abstract); eval.tex:1084 | The traces locate the EL2020 loss in write-time normalisation | where and why | yes |
| C05 | main.tex:81 (abstract); eval.tex:1089; conclusion.tex:92 | Explicit state missed its accuracy aim; the records allow the losses to be traced | where and why | yes |
| C06 | main.tex:141 (Ch. 1) | The loss lies in the design's write-time normalisation | where and why | yes |
| C07 | problem_domain.tex:119 | The difficulty is what passages establish, not finding them | why | partly |
| C08 | problem_domain.tex:170 | Surface form underdetermines epistemic status | why | partly |
| C09 | problem_domain.tex:174 | Decisions settled by presupposition are hard to recover | why | partly |
| C10 | problem_domain.tex:188 | Recency does not identify supersession | why | partly |
| C11 | problem_domain.tex:225 | Selective retention loses state said once | why | partly |
| C12 | problem_domain.tex:452 | DR6: machine interpretation fails in the ways of Section 2.3 | why | partly |
| C13 | problem_domain.tex:471 | Forming the schema is the hardest part of capture | why | partly |
| C14 | problem_domain.tex:817 | Objectives compete: coverage, fragmentation, actionable answers | why | partly |
| C15 | background.tex:30 | Conversation makes meeting content hard to reuse | why | partly |
| C16 | background.tex:155 | Literature: fact extraction, reading strategy and overwriting lose information | where | partly |
| C17 | background.tex:272 | An equal-time rewording defect at supersession | where and why | partly |
| C18 | implementation_chapter.tex:140 | No decision is attributed an isolated effect | why | yes |
| C19 | implementation_chapter.tex:173 | Separate records allow diagnosing where information was lost | where | yes |
| C20 | implementation_chapter.tex:174 | Review cannot recover a claim never extracted | where | yes |
| C21 | implementation_chapter.tex:194 | Early admission loses state before extraction | where and why | yes |
| C22 | implementation_chapter.tex:210 | Local windows miss decisions completed elsewhere | where and why | partly |
| C23 | implementation_chapter.tex:219 | The gate drops little project content (development run) | where | partly |
| C24 | implementation_chapter.tex:223 | Restraint comes from what is not stored | why | partly |
| C25 | implementation_chapter.tex:248 | An asserted negation can retire a value | where | yes |
| C26 | implementation_chapter.tex:260 | Collections can mix matters and keep members unconfirmed | where | no |
| C27 | implementation_chapter.tex:263 | Extraction misreads modality or negation | where and why | yes |
| C28 | implementation_chapter.tex:291 | Scalar keys cost fragmentation and near-duplicates | where and why | yes |
| C29 | implementation_chapter.tex:303 | Registry shape alone did not cause retrieval misses | why | no |
| C30 | implementation_chapter.tex:305 | Label-based reuse merges matters under one key | where and why | partly |
| C31 | implementation_chapter.tex:338 | Conflicts arise only from exact ties of first claims | where and why | yes |
| C32 | implementation_chapter.tex:355 | No tie-to-conflict check once a fact exists | why | yes |
| C33 | implementation_chapter.tex:358 | An earlier positive claim can block a negation | why | yes |
| C34 | implementation_chapter.tex:364 | Resolution is winner-take-all per key | where and why | yes |
| C35 | implementation_chapter.tex:408 | Deferral and parking make correct facts unavailable | where | yes |
| C36 | implementation_chapter.tex:470 | Non-atomic projection can leave incomplete transitions | why | partly |
| C37 | implementation_chapter.tex:502 | An unknown answer can hide an upstream loss | where | partly |
| C37a | implementation_chapter.tex:505 | An open conflict reaches the unknown branch at reading | where and why | partly |
| C38 | implementation_chapter.tex:510 | Rejections and history need a projected state to be answerable | where | partly |
| C39 | implementation_chapter.tex:525 | The latest-addition heuristic misses changes | where | no |
| C40 | implementation_chapter.tex:530 | The reader prefers resolved keys over evidence text | where and why | yes |
| C41 | implementation_chapter.tex:557 | A proposal copies the triggering claim's evidence | where and why | yes |
| C42 | implementation_chapter.tex:564 | A demoted fact keeps its earlier evidence | where | no |
| C43 | implementation_chapter.tex:570 | Provenance answers pick the earliest linked artifact | where and why | partly |
| C44 | implementation_chapter.tex:577 | No justification-based retraction | why | partly |
| C45 | implementation_chapter.tex:606 | D10's intended benefit: scalar claims file more reliably | why | partly |
| C46 | implementation_chapter.tex:608 | D10's contract fragments decisions | where and why | yes |
| C47 | implementation_chapter.tex:611 | No type check at filing | where and why | yes |
| C48 | implementation_chapter.tex:635 | Abstention comes from the template's decline | why | partly |
| C49 | implementation_chapter.tex:637 | The template has no relevance filter and no route to evidence | where and why | partly |
| C50 | implementation_chapter.tex:730 | Claim-specific matching fixed topic hiding | where and why | partly |
| C51 | implementation_chapter.tex:921 | Confirmation limits what becomes answerable | where | partly |
| C52 | implementation_chapter.tex:926 | State-first selection shifts errors to write time | where | yes |
| C53 | implementation_chapter.tex:932 | Stored values need an explicit read route | where | partly |
| C54 | implementation_chapter.tex:939 | Cold start relocates schema work into operation | where and why | yes |
| C55 | eval.tex:455 | No PM–RAG difference isolates a component | why | no |
| C56 | eval.tex:745 | Coverage, not status, is the H1 shortfall | where | partly |
| C57 | eval.tex:750 | 1/20 on evidence questions is a scoring mismatch | why | partly |
| C58 | eval.tex:753 | The ES2009 checkpoint decline is not controlled forgetting | why | partly |
| C59 | eval.tex:771 | The provenance split does not show its cause | why | partly |
| C60 | eval.tex:783 | Change answers fail on missing values, not strict scoring | why | no |
| C61 | eval.tex:788 | Change and rejection fail in representation and selection | where and why | partly |
| C62 | eval.tex:793 | Unapplied gold corrections bound the later obligations | why | partly |
| C63 | eval.tex:808 | Four reference-informed answers lost to rendering | why | no |
| C64 | eval.tex:816 | Restraint costs answerable information (H4) | why | partly |
| C65 | eval.tex:826 | Restraint lies in the resolver's embedding candidates | where and why | no |
| C66 | eval.tex:847 | The reference-informed arm loses to delayed availability | why | no |
| C67 | eval.tex:852 | The autonomous value gate loses nothing | where | yes |
| C68 | eval.tex:886 | Low citation support comes from linking failures | why | partly |
| C69 | eval.tex:909 | The reading of unknown answers decides the ES2009 sign | why | partly |
| C70 | eval.tex:949 | Without candidates, noise questions attach to nearby keys | where and why | no |
| C71 | eval.tex:960 | The candidate generator is a restraint gate, not recall | why | no |
| C72 | eval.tex:966 | Noise failures arise at question-time resolution | where | no |
| C73 | eval.tex:979 | Semantic reuse neither costs nor gains facts | why | partly |
| C74 | eval.tex:997 | Restraint transfers to EL2020 | why | no |
| C75 | eval.tex:999 | Unknown-topic failures assert unrelated facts | where and why | partly |
| C75a | eval.tex:1010; eval.tex:1115 | Verified values re-asked later are lost (persistence) | where | yes |
| C76 | eval.tex:1014 | Evidence answers name the first meeting | why | partly |
| C77 | eval.tex:1018 | Vagueness does not explain the loss; normalisation does | why | partly |
| C78 | generated/eval_tr_funnel.tex:6 (input at eval.tex:1028) | Funnel: the stage at which each wrong answer was lost | where | yes |
| C79 | eval.tex:1033 | Admission and extraction volume did not fail | where | yes |
| C80 | eval.tex:1036 | Four mechanisms, each from a design choice | where and why | yes |
| C81 | eval.tex:1040; conclusion.tex:204 | Fragmenting extraction is the largest loss | where | yes |
| C82 | eval.tex:1047 | Fragmenting extraction is D10's contract | why | yes |
| C83 | eval.tex:1050; conclusion.tex:229 | Winner-take-all filing loses carriers | where and why | yes |
| C84 | eval.tex:1057; conclusion.tex:232 | Verified values overwritten by unrelated ones | where | yes |
| C85 | eval.tex:1060; conclusion.tex:226 | Uniform authority and undated transcripts reduce D5 to latest-wins | why | yes (eval.tex); partly (conclusion.tex) |
| C86 | eval.tex:1065 | D4's reuse supplies the overloaded keys | why | yes |
| C87 | eval.tex:1068; conclusion.tex:252 | Schema-first reading loses stored values | where and why | yes |
| C88 | eval.tex:1072; conclusion.tex:256 | Wrong-key resolution for about half the questions | where | already decided (bug 9) |
| C89 | eval.tex:1076 | RAG succeeded by re-reading the source | why | partly |
| C90 | eval.tex:1078 | The judge effect does not explain the gap | why | partly |
| C91 | eval.tex:1116 | Uniform authority overwrote state; dissent conflict unreachable | why | partly |
| C92 | eval.tex:1125 | D5's authority ordering never discriminated | why | partly |
| C93 | eval.tex:1130; conclusion.tex:117 | Review boundary and gatekeeper caused no loss | where and why | partly |
| C94 | eval.tex:1134 | The results test D1, D3, D4, D7–D11 | why | yes |
| C95 | eval.tex:1141 | Incomplete answers are the state layer's design tension | why | partly |
| C96 | eval.tex:1173 | Evidence-only reading answers at least as well | where | partly |
| C97 | eval.tex:1201 | Half the ES2009 missing occurrences lost at acquisition | where and why | yes |
| C98 | eval.tex:1210 | D5 lets a reworded reading displace a value | why | yes |
| C98a | eval.tex:1213 | At most 37/265 ES2009 misses are directly implicated in supersession | where | partly |
| C99 | eval.tex:1218 | A fifth of the ES2009 misses lost at read selection | where | partly |
| C100 | eval.tex:1229 | The remedies are future design work | why | partly |
| C101 | eval.tex:1263 | The EL2020 construct penalises one-clause answers | why | partly |
| C102 | conclusion.tex:15 | The records keep how interpretations became state | where | partly |
| C103 | conclusion.tex:34 | The payload is the read path's selection | where | yes |
| C104 | conclusion.tex:42 | Transitions recorded but not exposed | where | yes |
| C105 | conclusion.tex:47 | Rejected values sit under unreached keys or never became claims | where | yes |
| C106 | conclusion.tex:59 | Restraint is a property of the embedding generator | why | no |
| C107 | conclusion.tex:145 | Losses consistent with LongMemEval's loss through extraction | where | partly |
| C108 | conclusion.tex:159 | Central proposition: normalisation reduces answerability | where and why | yes |
| C109 | conclusion.tex:168 | Each principle pairs an observation with the decision that explains it | why | yes |
| C110 | conclusion.tex:185 | Principle 1: keep a decision whole (D10) | where and why | yes |
| C111 | conclusion.tex:186 | Principle 2: check a value against key, rivals and evidence | where and why | yes |
| C112 | conclusion.tex:187 | Principle 3: assemble broad answers deliberately | where and why | partly |
| C113 | conclusion.tex:188 | Principle 4: keep source evidence reachable | where and why | partly |
| C114 | conclusion.tex:189 | Principle 5: restraint as a declared outcome | why | no |
| C115 | conclusion.tex:196 | Half the ES2009 missing values never formed | where | partly |
| C116 | conclusion.tex:199 | Part of the ES2009 loss belongs to the benchmark | why | partly |
| C117 | conclusion.tex:202 | The difficulty applies to every architecture | why | partly |
| C118 | conclusion.tex:211 | Vagueness cannot explain the losses; D10 can | why | yes |
| C119 | conclusion.tex:217 | Flagship trace: three values on one span | where | partly |
| C120 | conclusion.tex:221 | D5 admits an equal-authority, equal-time challenger | why | yes |
| C121 | conclusion.tex:235 | On a reused key, whatever was said last becomes current | why | yes |
| C122 | conclusion.tex:248 | List and change losses at read selection over an open schema | where and why | partly |
| C123 | conclusion.tex:258 | Hub keys attract the resolver and hold wrong values | where and why | partly |
| C124 | conclusion.tex:267 | Not the embedding machinery; recall lost in acquisition and aggregation | where | partly |
| C125 | conclusion.tex:277 | Reference-informed arm: delayed availability | why | no |
| C126 | conclusion.tex:298 | The projection path copies evidence (D9) | why | no |
| C127 | conclusion.tex:308 | RAG's ES2009 wins: values lost before or in state | where | partly |
| C128 | conclusion.tex:322 | The templates split compound decisions | where and why | yes |
| C129 | conclusion.tex:326 | The construct favours RAG | why | partly |
| C130 | conclusion.tex:330 | RAG's advantage is what normalisation lost | why | yes |
| C130a | conclusion.tex:334 | The shared enumeration failure is tagged D4 and D8 | why | no |
| C131 | conclusion.tex:341 | The records locate losses at admission and lifecycle stages | where | yes |
| C132 | conclusion.tex:357 | An extraction and filing contract would recover the losses | why | yes |
| C133 | conclusion.tex:362 | A supersession contract would recover wrong supersessions | why | yes |
| C133a | conclusion.tex:366 | An aggregation and change contract (revising D8) is needed | why | partly |
| C134 | conclusion.tex:371 | A read contract would recover reading losses | why | partly |
| C135 | conclusion.tex:424 | The separation loses information; the record shows where | where and why | yes |
| C136 | generated/eval_abl_families.tex:6 (input at appendix_reproducibility.tex:212) | Embeddings-off arms lose only on noise; reuse within variation | why | partly |
| C136a | generated/eval_abl_writepath.tex:6 (input at appendix_reproducibility.tex:213) | Write-path table: the resolver attached the noise questions | where and why | no |
| C137 | appendix_walkthrough.tex:115 | Assent by acknowledgement is not a decision | why | partly |
| C138 | appendix_walkthrough.tex:193 | Commitment by absorption | why | partly |
| C138a | appendix_walkthrough.tex:201 | Recording a conditional proposal as a feature drops the condition | why | no |
| C139 | appendix_walkthrough.tex:266 | A passing, unowned risk is easily lost | why | no |
| C140 | appendix_walkthrough.tex:295 | Contested ideas are easily misclassified | why | partly |
| C141 | appendix_walkthrough.tex:415 | A decision in weak wording is easily lost | why | partly |
| C142 | appendix_walkthrough.tex:451 | Project state needs non-local interpretive work | where and why | partly |
| C143 | appendix_design_evidence.tex:81 | C7's blocked rejection is a documented limitation | why | yes |
| C144 | appendix_design_evidence.tex:169 | A silent fallback could change what is extracted | why | yes |

## 4. The claims

### 4.1 Abstract (`thesis/main.tex`)

#### C01 · `thesis/main.tex:70` · abstract

**Claim (gloss).** The change-and-supersession and rejection mechanisms fail on list questions in both architectures.

```tex
Both systems fail every change and rejection list.
```

- **Where/why:** where.
- **Boundaries:** state rules; reading; extraction.
- **Mechanisms:** change and supersession; rejection.
- **Confirms if:**
  - A1 (EL2020 loss trace, demoted and ruled-out rows), A1-ref and the final configuration (ES2009, Step 5) also fail every change and rejection list.
  - Step 3 and 3b code the demoted and ruled-out losses behind them as design, conversation or evaluation.
- **Overturns if:** either of these.
  - A1-ref or the final configuration answers list items that A0 fails.
  - The demoted and ruled-out cases are coded implementation: bugs 1, 2 and 4 in A0, or polarity cases coded to "a modality or negation instruction missing from the prompt". A0's failure is then defect-limited and shows nothing about the mechanism (plan 23).
- **Text action if confirmed:** keep as an observation. Add the boundary shares from the loss trace.
- **Text action if overturned:** qualify: "the evaluated system fails every list; with the repairs it answers X". Do not cite the failure as a mechanism result.
- **Testable here:** partly.
- **Note:**
  - The Step 1 B3 item fixes (rejection items with an expected status; more than three candidate values) and bug 7 change these items. Old runs keep their answers and are re-judged.
  - The "both systems" half concerns RAG and is not tested here.
- **Also stated at:** C61 (eval.tex:788), C104 (conclusion.tex:42), C105 (conclusion.tex:47); see section 5, group J. Also, in Ch. 6, with this row's text actions:
  - "focused questions are often answered correctly, complete current-state lists are weak, and no change or rejection answer is strictly correct" (conclusion.tex:20–22);
  - "Both systems fail cumulative enumeration on both series: neither answers a rejection list or a newly-decided list correctly." (conclusion.tex:336–337), under the heading registered as C130a;
  - "It also found incomplete lists, unsuccessful change and rejection answers" (conclusion.tex:419–420).

#### C02 · `thesis/main.tex:72` · abstract

**Claim (gloss).** The evidence-and-provenance mechanism fails: most links do not support their fact.

```tex
Only 16.0\% of the system's evidence links fully support their fact under machine screening, and 14.4\% under the author's reweighted sample.
```

- **Where/why:** where.
- **Boundaries:** state rules.
- **Mechanisms:** evidence and provenance; `filing_support_check`.
- **Confirms if:** not tested by this study.
  - The loss trace follows values, not evidence links.
  - Step 3's pass examinations record passes that rest on bug 2. A0 pass rows carry defect flags 17/11/20 per run, nearly all bug 2 (Already read). This bears on how much of the low rate is a defect.
- **Overturns if:** not tested here. A support rate measured under A1 (bug 2 repaired) would be needed, and no step of this amendment measures one.
- **Text action if confirmed:** n/a (not tested). Independently of this study, qualify by bug 2 (P0-E).
- **Text action if overturned:** n/a (not tested).
- **Testable here:** no.
- **Note:** the A2 contract `filing_support_check` checks a claim's own span at filing. It does not fix the copying at proposal creation (22-bug-list.md, "What the cycle-2 plan targets").
- **Also stated at:** eval.tex:1118, the DR5 cell of tab:eval-synthesis. It repeats the figures ("full support 16.0\% (autonomous facts)", eval.tex:1118) and adds "valid links are not supporting links" (eval.tex:1118). The independent bug-2 qualification applies there too. Also C111 (conclusion.tex:186, third clause); section 5, group I.

#### C03 · `thesis/main.tex:73` · abstract

**Claim (gloss).** The resolver's embedding candidates produce restraint on noise questions. No recall is lost or gained through them.

```tex
The embedding candidates act as a restraint gate on incidental questions rather than as a recall mechanism.
```

- **Where/why:** why.
- **Boundaries:** key resolution and expansion; reading.
- **Mechanisms:** none (restraint on incidental talk is removed from Phase D3 by Step 0).
- **Confirms if:** recall half only.
  - Probes (ii-r) and (iii) are not recovered on the applicable routing and `key_reached` cases.
  - The offline checks show the fitting or holding key was in the recorded pruned prompt.
  - No case is coded "the shortlist or prune excluded a fitting key", or "a reuse or similarity threshold merged a new matter into an existing key" (`expansion_reuse_threshold`=0.80, semantic).
- **Overturns if:** either of these. Either way, the embedding candidate parameters bear on recall.
  - (ii-r) or (iii) recover cases where the key was pruned out. Already read: at least 27 of 66 `key_reached` rows had the holding key outside the pruned question-time prompt.
  - At least 3 distinct values are coded to the shortlist, prune or reuse-threshold causes.
- **Text action if confirmed:** recall half: keep only as "no recall loss traced to the embedding candidates on EL2020". Restraint half: per P0-A.
- **Text action if overturned:** remove "rather than as a recall mechanism", and report the shortlist and reuse-threshold shares.
- **Testable here:** partly.
- **Note:**
  - The restraint half cannot be tested here. Bug 8 means the ablation switch also turned off answer-time retrieval and the relevance gate, and no per-component switches exist.
  - P0-A drops "restraint gate" whatever the outcome.
  - The ablation ran on ES2009 in cycle 1.
  - The Ch. 5 sweep judged the same recall clause at eval.tex:960 (C71) not testable here. See decision R-19.
- **Also stated at:** C71 (eval.tex:960, eval.tex:1150), C124 (conclusion.tex:267); section 5, group C.

#### C04 · `thesis/main.tex:74` (abstract) and `thesis/eval.tex:1084` (subsec:eval-transfer) · merged

**Claim (gloss).**
- On EL2020 the autonomous arm loses against RAG because of write-time normalisation. eval.tex:1084 adds "itself" and sets this against the corpus explanation used on ES2009.
- The traces place the losses at three steps: extraction that fragments decisions; filing in which one claim takes a reused scalar key; and key-first reading.

Quote at `thesis/main.tex:74`:

```tex
On the second series the same configuration scores 39.0\% against RAG's 74.0\% ($-34.9$ points, interval $[-39.0,-28.6]$), and the traces locate the loss in write-time normalisation: fragmenting extraction, winner-take-all filing under reused keys, and schema-first reading.
```

Quote at `thesis/eval.tex:1084`:

```tex
On ES2009 the comparison depended on the stance reading and the leading explanation for the autonomous losses was the corpus. On a clearer, real series the same configuration lost substantially to the same baseline, and the traces locate the loss in write-time normalisation itself: fragmenting extraction, winner-take-all filing under reused keys and schema-first reading.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession; WD; `filing_type_check`; `resolution_same_meeting_conflict`; `supersession_requires_new_evidence`.
- **Confirms if:** all of these hold.
  1. **Surfaced-at.** The A0/A1 first-loss tables keep extraction, filing plus state maintenance, and reading as the loss boundaries. Already read (frozen trace), A0: 46.0 / 21.7+24.0 / 9.3 of 133 current rows, so about 92 of 133 are lost before reading.
  2. **Caused-at.** Under E+R the extraction share stays large in A1. The two filing clauses are tested apart:
     - "under reused keys" (routing) is confirmed when R recovers a large part of the filing and overwrite rows;
     - "winner-take-all" (ranking) is confirmed only by `proposed:another_value_won` cases that neither R nor E+R\* recovers and that Step 3 codes on D5.p3 at 94c049d.
  3. **Step 3.** Most A1 cases at these boundaries are coded architectural weakness or design trade-off on quoted 94c049d text. The lower 95% bound of the binary kappa is at least 0.40.
  4. **For "itself" (eval.tex:1084).** Conversational difficulty is a small share of the coded cases.
- **Overturns if:** any one of these.
  - Step 3 codes most A1 cases at these boundaries implementation defect, unclear, model-limited or design-or-model-not-separated. Examples: probes (b)/(b2) recover extraction cases; (ii-r)/(ii-h) recover routing cases; (iii) recovers reading cases.
  - The kappa's lower bound is below 0.40, so no design statement is allowed.
  - WD works (Step 2c), so "fragmenting" is an implementation choice that a built contract repairs.
  - For the "winner-take-all" clause only: R recovers most `proposed:another_value_won` rows, so their cause is routing, not the ranking. The same result confirms "under reused keys".
- **If the bounded verdict of a mechanism concerned is *can't tell (defect-limited)*:** this is a third outcome, neither confirm nor overturn.
  - Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about that mechanism. The location (condition 1) and the codes may still be reported.
  - For complete decisions and change and supersession, this condition is decided by Rule M (mapping section 7a), drafted on 27 October 2026 for decision C43 on the decision sheet (mapping decision M-19). For WD it is decided by the Step 2c rule, and for the A2 contracts by the admission rule, each with the bound (amendment:289–296, :451–471, :512–520).
- **Text action if confirmed:**
  - Keep.
  - Name the 94c049d decisions (D4.p5, D5.p3, D8.p4) instead of the retrospective D10/D11.
  - Cite the Step 3 caused-at × class table and the kappa.
  - Bound the claim to one development series.
  - Move "schema-first reading" out of "write-time normalisation": it is a read-path mechanism.
  - If only the ranking clause is overturned: drop "winner-take-all", and keep filing under reused keys as a routing loss.
- **Text action if overturned:**
  - Rewrite as surfaced-at only. For main.tex:74, proposed: "the traces show where values are lost: extraction, filing, state maintenance and reading". For eval.tex:1084, proposed: "the traces locate the loss on the write path (extraction, filing, state maintenance); its causes are ...", completed from the codes.
  - Drop "write-time normalisation" as the cause, and remove "itself".
  - Report the shares of implementation, unclear and design-or-model cases, and the admitted repairs.
- **Testable here:** yes.
- **Note:**
  - P0-C (22-fix-priorities.md) already asks for this claim to be labelled exploratory and kept out of the abstract, whatever the outcome.
  - The surfaced-at table was read before signing.
  - The abstract leaves out state maintenance. `current:overwritten_by_non_gold_value` is about 19–20 rows per A0/A1 run, as large as filing.
  - Of the routing-lost rows, 134 of 203 had every carrier keyed by the extractor's hint (Already read). So the "reused keys" are mostly assigned at extraction.
  - eval.tex:1150–1152 repeats the claim ("with the loss located in write-time normalisation").
  - "clearer" (eval.tex:1085) is not tested.
- **Also stated at:** C06 (main.tex:141), C77 (eval.tex:1018), C108 (conclusion.tex:159), C130 (conclusion.tex:330), C135 (conclusion.tex:424); section 5, group A.

#### C05 · `thesis/main.tex:81` (abstract), `thesis/eval.tex:1089` (subsec:eval-transfer) and `thesis/conclusion.tex:92` (sec:conc-answers, RQ4) · merged

**Claim (gloss).**
- main.tex:81 only: the accuracy shortfall belongs to maintaining explicit state, a design property.
- All three: the records the system kept are enough to trace each loss.
- eval.tex:1089 only: the tracing is limited by D9's lineage, which credits the limit to D9's design.

Quote at `thesis/main.tex:81`:

```tex
a bounded empirical account: maintaining explicit state did not deliver the answer accuracy it was built for, but it kept the intermediate records from which the losses could be traced.
```

Quote at `thesis/eval.tex:1089` (added in the review of 27 October):

```tex
What survives the transfer is narrower. Both arms decline the incidental questions and keep their citations within the checkpoint, and the autonomous arm's retained records still allow its losses to be traced, within the lineage limits of \Dn{9}. Its recall and its abstention on unknown topics do not survive.
```

Quote at `thesis/conclusion.tex:92`:

```tex
What survives the transfer is narrower than an advantage: both systems decline the incidental questions and keep their citations within the checkpoint, and the autonomous arm's retained records still allow its losses to be traced.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** evidence and provenance.
- **Confirms if:**
  - **Records:** the Step 2 identity gate passes on the A0/A1/A2 runs. The conflict trail, proposals, settle counts and facts are rebuilt from the recorded trace. The Step 3 stopping rule is met with unclear caused-at at most 10%.
  - **Shortfall** (main.tex:81 only): Step 3 codes most A1 losses as design or conversation, not implementation.
- **Overturns if:**
  - **Records:** the identity gates fail, or unclear caused-at exceeds 10% because the records cannot decide the cause.
  - **Shortfall** (main.tex:81 only): most A1 losses are coded implementation defect, so the shortfall belongs to the implementation, not to maintaining state.
- **Text action if confirmed:**
  - main.tex:81: keep. Qualify "traced" as surfaced-at for all rows and caused-at for X% of cases, and cite the Step 2 gates.
  - conclusion.tex:92 and eval.tex:1089 (records clause): keep. Say "located" for surfaced-at, and give the caused-at share.
- **Text action if overturned:**
  - main.tex:81: qualify. Proposed: "kept records from which the location of most losses, but not always their cause, could be traced". Replace "maintaining explicit state" with "the evaluated implementation".
  - conclusion.tex:92 and eval.tex:1089 (records clause): qualify. Proposed: "still allow where its losses surfaced to be traced".
- **Text action for the D9 clause at eval.tex:1092, whatever the outcome:** conclusion.tex:92 lacks this clause. The action follows decision R-4.
  - Under R-4(b), the recommendation: replace "within the lineage limits of \Dn{9}" (eval.tex:1092) with the bug-2 qualification (P0-E), repaired in A1, as for C126.
  - Under R-4(a): keep it, citing D9.p4 at 94c049d ("proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation", D9.p4).
- **Testable here:** yes.
- **Note:**
  - P0-E asks for the records claim to be qualified by the bug-2 lineage defect: about 35–60% of current facts cite a span without their value.
  - The Step 0 instrument changes (judge inputs, rival values of conflicts) exist because the cycle-1 records lacked them.
  - The loss trace's `pack_check` (9551/9551) shows that the reader's packs can be rebuilt.
  - The restraint half of conclusion.tex:92 ("both systems decline the incidental questions") cannot be tested here. Nor can its counterpart at eval.tex:1089–1090 ("Both arms decline the incidental questions").
  - eval.tex:1152 restates the records claim: "Architectural inspectability, correctness against encoded obligations and semantic support verified from the source are three different properties: the evaluation establishes the first" (eval.tex:1152–1155). It takes the records actions above.
- **Also stated at:** C19 (implementation_chapter.tex:173), C102 (conclusion.tex:15), C131 (conclusion.tex:341), C135 (conclusion.tex:424); section 5, group B.

### 4.2 Chapter 1 (`thesis/main.tex`)

#### C06 · `thesis/main.tex:141` · chap:introduction

**Claim (gloss).** Ch. 1, contribution 3. The EL2020 losses come from the design itself, through write-time normalisation.

```tex
a pre-declared transfer check on a second, real series on which the retrieval baseline scored substantially higher and whose traces locate the loss in the design's write-time normalisation.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules.
- **Mechanisms:** complete decisions; change and supersession.
- **Confirms if:** as for C04, and "the design's" needs more:
  - most A1 caused-at cases at extraction, routing and the state rules are coded architectural weakness or trade-off, quoting 94c049d text;
  - the kappa's lower bound is at least 0.40;
  - admitted Step 4 repairs recover few cases.
- **Overturns if:** any of these.
  - A1 cases are coded implementation defect or unclear in the majority.
  - Admitted repairs (Step 4) or WD recover a material share.
  - The kappa's lower bound is below 0.40.
- **Text action if confirmed:** keep "the design's" only with the coded share, the 94c049d decisions and the kappa.
- **Text action if overturned:** replace "the design's write-time normalisation" with "the evaluated implementation's write path". Alternatively, say only where the loss surfaced.
- **Testable here:** yes.
- **Note:** the amendment's reporting rule allows a statement that a loss comes from the design "only where the codes say architectural or trade-off on 94c049d text, with the binary kappa's lower bound at or above 0.40" (amendment:572). P0-C also covers main.tex:142–144.
- **Also stated at:** C04 (main.tex:74, eval.tex:1084); section 5, group A.

### 4.3 Chapter 2 (`thesis/problem_domain.tex`)

Ch. 2 claims are problem-level. Their actions are limited to "keep" or "qualify" with no solution content. Any consequence for the system goes to Ch. 6 (plan 23, Phase F 2). See decision R-7.

#### C07 · `thesis/problem_domain.tex:119` · sec:pd-core

**Claim (gloss).** Problem-level. The difficulty lies in interpreting what passages establish, not in finding them.

```tex
Answering the questions above from a conversational record is not an information-retrieval problem in the narrow sense. The relevant passages are usually easy to find; the difficulty is what they \emph{establish}.
```

- **Where/why:** why.
- **Boundaries:** admission; extraction.
- **Mechanisms:** epistemic status.
- **Confirms if:**
  - Admission losses are small: `admitted:ignored` is 4–5 rows per run (Already read).
  - RAG's chunks hold the gold line (joint table).
  - Step 3 codes conversational difficulty at polarity and modality rather than at admission.
- **Overturns if:** Step 3 places most caused-at at routing, a step the architecture introduces. This does not overturn the problem claim, but the system's largest losses would then not come from interpretation.
- **Text action if confirmed:** keep. It is a Ch. 2 problem claim with no solution content.
- **Text action if overturned:** keep in Ch. 2. Ch. 6 states that the largest losses arose at steps the architecture introduces (plan 23, Phase F 2).
- **Testable here:** partly.

#### C08 · `thesis/problem_domain.tex:170` · subsec:pd-epistemic

**Claim (gloss).** Problem-level. Epistemic status is a conversational difficulty that causes status errors.

```tex
Surface form underdetermines epistemic status, and retrieval relevance does not recover it: the three battery statements are near-identical as retrieval targets. Any treatment that maps every mention of a value onto the same representation will manufacture decisions that were never made.
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** epistemic status; rejection.
- **Confirms if:** Step 3 codes the polarity and modality cases conversational difficulty. Already read:
  - A1 `modality:carried_only_proposed` is 8.7 rows, and `polarity:carried_only_positive` 5.7 ruled-out rows;
  - 12.2 of 45.2 extraction-lost rows are lost at polarity or modality.
- **Overturns if:** those cases are coded implementation ("a modality or negation instruction missing from the prompt"), or E+R\* recovers them. The system's status losses then come from the prompt.
- **Text action if confirmed:** keep in Ch. 2. Ch. 6 may cite the coded share.
- **Text action if overturned:** keep in Ch. 2. Ch. 6 must not attribute the status losses to the conversation.
- **Testable here:** partly.
- **Note:** the same point is made at these places, which take this row's actions:
  - "A process that reads the first utterance in isolation records an obligation nobody accepted." (problem_domain.tex:167–168), also listed in section 5, group R;
  - "A representation that treats every mention equivalently therefore promotes tentative or rejected information into apparent state." (problem_domain.tex:401–403), in DR1.

#### C09 · `thesis/problem_domain.tex:174` · subsec:pd-epistemic

**Claim (gloss).** Problem-level. Decisions settled by presupposition are hard to recover (ES2009b).

```tex
The converse difficulty is as real: in the meeting of Appendix~\ref{app:walkthrough}, the casing material is treated as settled by presupposition (``we're making the whole thing out of plastic anyway'') well before the turn in which anyone decides it.
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** epistemic status.
- **Confirms if:** in 3b, the casing-material case of the final configuration's r1 on ES2009 is coded conversational difficulty.
  - Only that run can confirm. The probes run on the sampled A1 and A2 runs, and in 3b only probe (i), on the final configuration's r1 (amendment:238). ES2009 A0 r1 gets "model pre-coding only, plus author coding of the ES2009b walkthrough cases" (amendment:312).
  - So an A0 r1 walkthrough extraction case with an applicable probe-type alternative can come out only implementation defect or unclear (amendment:338).
- **Overturns if:** 3b codes it implementation, or evaluation (the plastic-casing gold is one of the unapplied corrections), or A1-ref recovers it.
- **Text action if confirmed:** keep. Reference the implementation-side walkthrough.
- **Text action if overturned:** keep in Ch. 2 as a property of the meeting. Ch. 6 reports the coded cause.
- **Testable here:** partly.
- **Note:** Appendix B's line ranges stay stable for the 3b walkthrough.
- **Also stated at:** C138 (appendix_walkthrough.tex:193); section 5, group Q.

#### C10 · `thesis/problem_domain.tex:188` · subsec:pd-temporal

**Claim (gloss).** Problem-level. Change handling is hard because later mentions (recaps, asides) are not replacements.

```tex
Recency alone does not resolve this. Later text frequently mentions superseded values without reinstating them, in recaps, comparisons, and asides, so ``the most recent passage containing the value'' is not a reliable proxy for ``the current value''. Conversely, an old statement can remain the current truth for months. Whether a later statement supersedes an earlier one is a property of what the statements \emph{do} (replace, reject, merely refer), not of their timestamps.
```

- **Where/why:** why.
- **Boundaries:** state rules; extraction.
- **Mechanisms:** change and supersession.
- **Confirms if:** on the Step 3 case pages, the successors in overwrite cases are recaps or asides of the same matter, coded conversational difficulty.
- **Overturns if:** the overwrites mostly come from other matters, so R recovers them. Already read: 12 of 16 sampled A2 conflict keys mix matters (10 with unrelated values, 2 with two different gold values; 23-el2020-arms.md:77–79). The observed supersession losses are then routing, not recap recency.
- **Text action if confirmed:** keep in Ch. 2.
- **Text action if overturned:** keep in Ch. 2. Ch. 6's lifecycle paragraph reports which cause dominates.
- **Testable here:** partly.
- **Note:** the same point is made at these places, which take this row's actions:
  - "an externally imposed constraint reverses the previous meeting's decision, and it prevails because of its source, not its position in the record" (problem_domain.tex:195–197), introduced at problem_domain.tex:194;
  - "a reading that adjudicated by recency alone would reach the right answer for the wrong reason" (appendix_walkthrough.tex:53–54), in the sentence starting at appendix_walkthrough.tex:51; Appendix B stays unchanged (R-7).

#### C11 · `thesis/problem_domain.tex:225` · subsec:pd-noise

**Claim (gloss).** Problem-level trade-off. Admission selectivity loses state that is mentioned only once.

```tex
Selecting what becomes durable memory requires judgement, with costs in both directions. Discarding too eagerly loses state that was expressed only once and in passing, such as a risk raised briefly or an ownership handoff inside a digression.
```

- **Where/why:** why.
- **Boundaries:** admission.
- **Mechanisms:** none (restraint on incidental talk is removed from Phase D3 by Step 0).
- **Confirms if:** the `admitted:ignored` cases (4.0, 4.0 and 5.0 rows per run) are coded design trade-off on D2 at 94c049d, or conversational difficulty (said once, in passing).
- **Overturns if:** they are coded implementation ("the gatekeeper ignoring a span its own criteria admit") or design-or-model-not-separated.
- **Text action if confirmed:** keep. The loss is small on EL2020.
- **Text action if overturned:** keep in Ch. 2. Ch. 6 states that the admission losses were implementation, or were not separated from the model.
- **Testable here:** partly.
- **Note:** this row also covers DR8's "the countervailing risk, selectivity discarding real state, is the coverage side of the same dial" (problem_domain.tex:485).
- **Also stated at:** C21 (implementation_chapter.tex:194); section 5, group K.

#### C12 · `thesis/problem_domain.tex:452` · dr:6

**Claim (gloss).** Machine losses arise from the five conversational characteristics of Section 2.3.

```tex
\item[DR6 --- Controlled state formation.]\label{dr:6} Machine interpretation of conversational evidence is fallible in exactly the ways Section~\ref{sec:pd-core} describes, and a wrong stored fact influences every later answer until corrected;
```

- **Where/why:** why.
- **Boundaries:** extraction; state rules.
- **Mechanisms:** epistemic status; change and supersession; rejection; evidence and provenance.
- **Confirms if:** Step 3 caused-at falls mostly at extraction (polarity, modality) and at the state rules, and is coded conversational difficulty.
- **Overturns if:** most caused-at falls at routing or key assignment, which is not among the five characteristics, or is coded implementation.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite "in exactly the ways" as "in, among others, the ways". No solution content is added to Ch. 2.
- **Testable here:** partly.

#### C13 · `thesis/problem_domain.tex:471` · dr:7

**Claim (gloss).** Problem-level. Forming the schema and assigning keys is the hardest part of capture.

```tex
requiring the state schema in advance would presuppose the hardest part of the capture problem and limit the treatment to pre-modelled domains.
```

- **Where/why:** why.
- **Boundaries:** key assignment at extraction; key resolution and expansion.
- **Mechanisms:** none listed.
- **Confirms if:** R recovers the largest share of A1's lost rows, so routing is the largest caused-at boundary.
- **Overturns if:** extraction is the largest caused-at boundary (E+R against R).
- **Text action if confirmed:** keep. Ch. 6 may cite the share.
- **Text action if overturned:** keep in Ch. 2 as a premise. Ch. 6 reports that extraction, not the schema, cost most.
- **Testable here:** partly.

#### C14 · `thesis/problem_domain.tex:817` · sec:pd-brief

**Claim (gloss).** Problem-level trade-offs. Selectivity costs coverage, an online schema risks fragmentation, and preserving uncertainty costs actionable answers.

```tex
The problem analysis does not uniquely determine an architecture. It establishes capabilities and tensions, and several of the objectives compete: selective retention can reduce coverage; review can increase contestability while adding operational burden; a schema built during operation can improve cold-start coverage while risking fragmentation; and preserving uncertainty can reduce unsupported assertions while producing fewer immediately actionable answers.
```

- **Where/why:** why.
- **Boundaries:** admission; key assignment at extraction; key resolution and expansion; extraction.
- **Mechanisms:** epistemic status; complete decisions.
- **Confirms if:** Step 3 codes design trade-off on 94c049d text for three groups. The benefit is measured where the trace can.
  - `admitted:ignored` (selectivity);
  - routing cases where one matter is split across keys (D4.p5: "increasing fragmentation, near-duplicates");
  - `modality:carried_only_proposed` (D3.p3, unconfirmed values).
- **Overturns if:**
  - the routing losses are mostly over-merging, one key holding several matters (the A2 sample, hub keys; D4.p4 "Review may itself merge distinct meanings"), not fragmentation; or
  - the modality cases are coded implementation.
- **Text action if confirmed:** keep.
- **Text action if overturned:** keep in Ch. 2. Ch. 6 names over-merging as the observed cost of the online schema.
- **Testable here:** partly.

### 4.4 Chapter 3 (`thesis/background.tex`)

#### C15 · `thesis/background.tex:30` · sec:bg-meetings

**Claim (gloss).** Literature claim. Meeting content is hard to reuse because of how conversation works.

```tex
Communication research explains why their content is hard to reuse: participants build shared understanding incrementally through grounding \citep{clark1991grounding}, and media differ in how well they support conveyance versus convergence \citep{dennis2008synchronicity}. The record a meeting leaves is therefore conversational: tentative proposals, negations, and revisions appear alongside final decisions.
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** epistemic status; change and supersession.
- **Confirms if:** Step 3 codes a material share of A1 extraction cases (polarity, modality) as conversational difficulty.
- **Overturns if:** few cases are coded conversational difficulty.
- **Text action if confirmed:** keep. It is a literature claim.
- **Text action if overturned:** keep as literature. Ch. 6 must not cite it as the system's cause.
- **Testable here:** partly.
- **Note:** the literature claim stands either way. Only its use as an explanation of the system's losses is at stake.

#### C16 · `thesis/background.tex:155` · sec:bg-agent-memory

**Claim (gloss).** Literature claim, used as a parallel. Fact extraction, reading strategy and overwriting lose information.

```tex
Its experiments report two findings that Chapter~\ref{chap:evaluation} returns to: compressing a history into extracted facts loses information relative to storing dialogue rounds, except for questions that aggregate across sessions, and the reading strategy matters even under perfect retrieval, costing up to ten accuracy points. Its pilot on commercial memory features found that one tended to overwrite earlier information as the chat continued and another missed indirectly stated facts.
```

- **Where/why:** where.
- **Boundaries:** extraction; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession.
- **Confirms if:** the A1 loss trace and the oracles show the parallel losses: extraction under E+R, reading (`key_reached`), and overwriting (`current:overwritten_by_non_gold_value`).
- **Overturns if:** one of these boundaries is negligible in A1, so the parallel does not hold for it.
- **Text action if confirmed:** keep. Ch. 5 and Ch. 6 keep "consistent with".
- **Text action if overturned:** keep the literature. Drop the parallel for that boundary in Ch. 5 and Ch. 6.
- **Testable here:** partly.
- **Also stated at:** C107 (conclusion.tex:145).

#### C17 · `thesis/background.tex:272` · tab:bg-positioning

**Claim (gloss).** An implementation defect (equal-time rewording) exists at the supersession step.

```tex
ProjectMemory & Admitted evidence, claims, proposals, and facts with statuses & Registry grown from an empty start by reviewed expansion & Authority-and-time eligibility, then supersession with statuses; equal-time rewording defect documented & Proposal to confirmation, enforced at projection & Evidence identifiers on every fact\\
```

- **Where/why:** where and why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`.
- **Confirms if:** the A0 model pre-codes give state-rule cases to bug 3 or bug 4 (Phase B, counted as repaired).
- **Overturns if:** few A0 cases rest on the equal-time defect. Already read: the A0 and A1 overwrite rows are level (19.7 against 19.0).
- **Text action if confirmed:** keep. Add "repaired in A1 (bug 3)".
- **Text action if overturned:** keep the defect statement, which is true per bug 3, but do not imply that it drives the losses.
- **Testable here:** partly.
- **Note:** "Registry grown [...] by reviewed expansion" is contradicted for A0 by bug 5 (hints filed under unvalidated keys). That is a conformance fact, not a register row; see decision R-16.
- **Also stated at:** C98 (eval.tex:1210), C120 (conclusion.tex:221).

### 4.5 Chapter 4 (`thesis/implementation_chapter.tex`)

Under the amendment, text written after 9 September can never ground an architectural or trade-off code (amendment:347). That covers all of D10 and D11 and several sentences inside D2–D9. Such rows say "Retrospective" in their note. At most they can be confirmed as a location, or as an implementation choice. See decision R-5.

#### C18 · `thesis/implementation_chapter.tex:140` · sec:key-design-decisions

**Claim (gloss).** The evaluation attributes no loss or effect to a single design decision. Only complete configurations are compared.

```tex
[...] the evaluation compares complete configurations, so no decision is attributed an isolated effect (Section~\ref{subsec:eval-fairness}).
```

- **Where/why:** why.
- **Boundaries:** all boundaries (attribution scope).
- **Mechanisms:** all mechanisms (attribution scope).
- **Confirms if:**
  - in the Step 3 caused-at × class tables, no architectural-weakness or trade-off code resting on a single 94c049d decision survives both the bound rule and the 0.40 kappa rule; and
  - no A2 leave-one-out or Step 4 check isolates a contract or repair effect.
- **Overturns if:** any of these. Each is an isolated, bounded attribution.
  1. Step 3 codes losses as architectural or trade-off on named 94c049d decisions, with the binary kappa's lower bound at or above 0.40.
  2. An A2 leave-one-out gives a contract at least 3 distinct values net in every gate-passing run.
  3. A Step 4 repair passes its check.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite: scores compare complete configurations; the root-cause study and the leave-one-out attribute individual losses to boundaries, decisions and contracts.
- **Testable here:** yes.
- **Note:** retrospective sentence (5de9911, 19 October). It also bounds how the D-sections' "Expected consequence" lines may cite the Ch. 5 mechanisms.
- **Also stated at:** C55 (eval.tex:455, eval.tex:1257); see decision R-11.

#### C19 · `thesis/implementation_chapter.tex:173` · subsec:decision-boundaries (D1)

**Claim (gloss).** The separated records are enough to locate where a value was lost.

```tex
Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost.
```

- **Where/why:** where.
- **Boundaries:** all boundaries (location only).
- **Mechanisms:** evidence and provenance.
- **Confirms if:** both of these.
  - The loss trace assigns every gold row in the nine traced runs (A0, A1, A2; RAG is not traced) a first-loss step from the stored records (primary series complete, no open queue item).
  - The Step 2 identity gate reproduces the `conflict_detection` trail, the proposals, the settle expiries and the facts from the recorded inputs for the A0/A1 runs.
- **Overturns if:** the identity gates fail for lack of recorded inputs. Or Step 3 cases end with caused-at unclear because the records do not show the deciding step. Examples are the judge's inputs and the conflict rival values, which Step 0 adds as instruments.
- **Text action if confirmed:** keep. Add that the records locate a loss but do not give its cause.
- **Text action if overturned:** qualify: name the missing records, and say they were added as instruments for later runs.
- **Testable here:** yes.
- **Note:** 94c049d (D1.p4). The amendment's premise already limits the claim to location: "The trace gives the **location** of each loss, not its **cause**" (amendment:26).
- **Also stated at:** C05, C102, C131; section 5, group B.

#### C20 · `thesis/implementation_chapter.tex:174` · subsec:decision-boundaries (D1)

**Claim (gloss).** Review cannot reach values lost at admission or extraction. It can only delay or recover what was extracted.

```tex
The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review. A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal.
```

- **Where/why:** where.
- **Boundaries:** admission (`admitted`); extraction (`carried`, polarity, modality); state rules (`applied`).
- **Mechanisms:** complete decisions; epistemic status.
- **Confirms if:**
  - The loss-trace first-loss table puts about a third of current rows at extraction (46.0/44.3/39.7 of 133 per A0/A1/A2 run) and 4–5 at `admitted:ignored`.
  - The A2 reviewer ceiling recovers no row first lost at extraction or admission. It recovers only open-conflict rows that have the gold value among their rivals.
- **Overturns if:** the reviewer ceiling or the A1 settle recovers rows first lost at extraction. Such rows have no carrier, so this would point to a matcher or trace error.
- **Text action if confirmed:** keep, and cite the extraction and admission shares.
- **Text action if overturned:** investigate the trace or the matcher before changing any text.
- **Testable here:** yes.
- **Note:** 94c049d. The claim is near-definitional, so the study mainly gives its size. The review-wait part is covered by C35 (l.408).

#### C21 · `thesis/implementation_chapter.tex:194` · subsec:decision-admission (D2)

**Claim (gloss).** Early admission loses some state-bearing content before extraction. D2 accepts this as its cost.

```tex
Selective admission before extraction places the decision earlier, at the cost of losses before a claim is ever formed.
```

- **Where/why:** where and why.
- **Boundaries:** admission (`admitted:ignored`).
- **Mechanisms:** none (restraint on incidental talk is removed by the Step 0 plan-23 fixes; no other mechanism remains).
- **Confirms if:** the loss trace's current rows first lost at `admitted:ignored` (4.0/4.0/5.0 of 133 per A0/A1/A2 run) are coded design trade-off on D2's 94c049d text. Three conditions must hold:
  1. the candidate cause "the gatekeeper ignoring a span its own criteria admit" is ruled out on the page;
  2. the page shows that a correct gate output would still have excluded the span (the gate is an LLM step with no model condition);
  3. the code holds under the bound rule and the 0.40 rule.

  Step 5's ES2009 adapter gives a similar size.
- **Overturns if:** Step 3 codes the `admitted:ignored` cases as implementation defect (the gate ignored a span its own criteria admit), design-or-model-not-separated, or unclear. Then no admission loss is a demonstrated trade-off.
- **Text action if confirmed:** keep, and cite the measured size (about 3–4% of current rows).
- **Text action if overturned:** qualify: the observed admission losses are gate errors, or cannot be separated from the model. Keep the cost only as a design expectation.
- **Testable here:** yes.
- **Note:**
  - 94c049d (D2.p2).
  - The same claim appears at l.65–66 ("makes early omissions irrecoverable to the normal answer path"), in Table tab:design-rationale l.676 ("Lost evidence") and in Table tab:requirements-design l.999 ("Restraint can lose useful state"). The same action applies to all of them.
  - Recoverability rule: if RAG answered the value from a cited gold line in at least 2 of 3 runs, a conversational-difficulty code needs a written reason.
- **Also stated at:** C11 (problem_domain.tex:225); section 5, group K.

#### C22 · `thesis/implementation_chapter.tex:210` · subsec:decision-admission (D2)

**Claim (gloss).** Extraction loses decisions that are completed outside the local span window, and nothing repairs this.

```tex
Local transcript windows further bound interpretation: a commitment completed outside the window can be missed. The normal ingestion path does not invoke the separate discourse-linking mechanism to repair such omissions.
```

- **Where/why:** where and why.
- **Boundaries:** extraction (`carried`: `claims_without_the_value`, `split_across_claims`, `no_claims_from_cited_span`).
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** Step 3 has extraction cases where the gold line and its completion lie in different spans, and:
  - probe (i) conditions (b), (b2), (c) and (d) on the cited span do not recover them;
  - they are coded architectural weakness on this 94c049d passage under the bound rule and the 0.40 rule;
  - they are reported as their own sub-cause in the surfaced × caused tables.
- **Overturns if:** no coded case rests on a window boundary. Or such cases are recovered by probe (i) on the same span (registry or examples: implementation), or by WD in Step 2c.
- **Text action if confirmed:** keep, and cite the count.
- **Text action if overturned:** keep as an untested design limit. Do not cite it as a cause of the observed losses.
- **Testable here:** partly.
- **Note:**
  - 94c049d (D2.p4). Appendix design_evidence l.145–148 states the same. Appendix B l.216–219 and l.451–454 give the conversational side.
  - No window-size condition is run.
  - No listed candidate cause covers the window. A window case needs the burden rule like any other: conversational difficulty, model-limited, unclear and probe-recovered implementation codes all remain possible, and the pilot may add causes (amendment:380).
- **Also stated at:** C142 (appendix_walkthrough.tex:451); section 5, group R.

#### C23 · `thesis/implementation_chapter.tex:219` · subsec:decision-admission (D2)

**Claim (gloss).** The admission gate drops little project content, and what it drops is also present in admitted spans.

```tex
As a development observation from one run, the gate ignored 76 of 251 spans; 60 of those were social or logistical by its own classification, and a manual reading of the 16 unclassified fragments found project content in four (a price clarification, two remote-locating ideas, a casing property), all on topics also present in admitted spans.
```

- **Where/why:** where.
- **Boundaries:** admission (`admitted:ignored`).
- **Mechanisms:** none (restraint on incidental talk is removed by the Step 0 plan-23 fixes).
- **Confirms if:** in the Step 5 ES2009 loss trace (adapter), few rows are first lost at `admitted:ignored`, and the 3b pages show no ES2009 value whose only carrier span was ignored. This is consistent with EL2020's 4.0–5.0 current rows per run.
- **Overturns if:** Step 5 ES2009 runs show gold values first lost at `admitted:ignored` with no carrier elsewhere, or an ignored share clearly above EL2020's.
- **Text action if confirmed:** keep. Add the cycle-2 `admitted:ignored` counts beside the development observation.
- **Text action if overturned:** replace the observation with the Step 5 counts.
- **Testable here:** partly.
- **Note:** retrospective. It entered at b422b27 (14 September), after 94c049d, from a development run before cycle 1, so it can never ground a design code. That run is not re-read here.
- **Also stated at:** section 5, group K.

#### C24 · `thesis/implementation_chapter.tex:223` · subsec:decision-admission (D2)

**Claim (gloss).** Restraint on incidental talk comes from what the write path does not store, not from a read-side filter.

```tex
Expected consequence: fewer substantive answers about incidental content without excessive loss of required state; tested as \Hy{5} beside state recall. There is no read-side classifier for incidental content, so noise resistance is observable only as absent or non-matching maintained state.
```

- **Where/why:** why.
- **Boundaries:** admission; reading (noise questions).
- **Mechanisms:** none (restraint on incidental talk is removed by the Step 0 plan-23 fixes).
- **Confirms if:** in the Step 5 ES2009 runs on the post-B3 suite, if the noise items get forbidden content, noise questions are credited with no key resolved and no fact given, as recorded in the loss trace's question records.
- **Overturns if:** credited noise answers have keys resolved and facts given, or noise failures render stored facts. Restraint would then follow from the question-time thresholds (`answer_relevance_min_similarity`=0.42), not from what was stored.
- **Text action if confirmed:** keep as the H5 expectation. State that no restraint mechanism is judged.
- **Text action if overturned:** rewrite: noise restraint is a by-product of question-time retrieval thresholds.
- **Testable here:** partly.
- **Note:**
  - Retrospective wording (5de9911).
  - EL2020 cannot test it: "The 8 EL2020 noise items forbid nothing either." (22-bug-list.md:138). Compare "Restraint is a by-product of retrieval thresholds" (22-bug-list.md:155).
  - The same idea appears at l.208–210 ("Resolution and confirmation remain responsible for preventing inappropriate promotion").
- **Also stated at:** section 5, group C.

#### C25 · `thesis/implementation_chapter.tex:248` · subsec:decision-epistemic (D3)

**Claim (gloss).** The rejection path works at the state rules: an asserted negation becomes a rejected fact, and a current value can be retired by its negation.

```tex
In the evaluated configuration, an asserted negation of an alternative can create a proposal for a rejected fact. Negating the current value additionally passes the resolver's authority and affirmation checks.
```

- **Where/why:** where.
- **Boundaries:** state rules (`proposed`, `applied`, `current` for ruled-out and demoted rows); extraction (polarity) as the alternative.
- **Mechanisms:** rejection; epistemic status; change and supersession.
- **Confirms if:**
  - In A1, ruled-out rows that reach the state rules are stored as REJECTED.
  - Their losses concentrate at `polarity:carried_only_positive` (about 6 of 16 per run).
  - Stored demoted values retire (0 of 3 still current in A1).
  - Step 3 codes no A1 rejection case to a state-rule implementation defect.
- **Overturns if:**
  - A0 demoted cases that stay current (1.0 per run) or are never retired are model-pre-coded to bug 1. Under bug 1 the affirmation check always held, so the reject branch for a current value was unreachable.
  - Or A1 rejection cases are coded implementation at the state rules.
- **Text action if confirmed:** keep for the repaired system (A1-ref).
- **Text action if overturned:** rewrite "In the evaluated configuration": in the evaluated revision the current-value branch was unreachable (bug 1); it works only under the repair.
- **Testable here:** yes.
- **Note:**
  - 94c049d content, reworded from "Under current development defaults" at 5de9911.
  - Bug 1 is already recorded for A0: "Current value explicitly negated" occurs 0 times across 13 dumps (22-bug-list.md:17).
  - A0 cases resting on bug 1 count as repaired (amendment end state 1).
- **Also stated at:** C33 (l.358), C143 (appendix_design_evidence.tex:81); section 5, group M.

#### C26 · `thesis/implementation_chapter.tex:260` · subsec:decision-epistemic (D3)

**Claim (gloss).** Collection keys can keep members unconfirmed and can mix matters.

```tex
An agreeing positive claim adds support to an existing member without automatically upgrading an unconfirmed member. Membership still depends on correctly interpreted concept meaning, and heterogeneous content can enter the same broad collection.
```

- **Where/why:** where.
- **Boundaries:** state rules; key assignment at extraction.
- **Mechanisms:** epistemic status; change and supersession.
- **Confirms if:** none available. The evaluated configuration mints scalar keys only (`expansion_force_scalar`), so no EL2020 or ES2009 run has collection keys.
- **Overturns if:** none available, for the same reason.
- **Text action if confirmed:** keep.
- **Text action if overturned:** keep.
- **Testable here:** no.
- **Note:** 94c049d. It becomes testable only if a configuration with collection keys is run.

#### C27 · `thesis/implementation_chapter.tex:263` · subsec:decision-epistemic (D3)

**Claim (gloss).** Status is lost at extraction when modality or polarity is misread.

```tex
Extraction can misclassify modality or negation in either model, so \DR{1} and \DR{4} are only partially realised across the full lifecycle.
```

- **Where/why:** where and why.
- **Boundaries:** extraction (polarity, modality).
- **Mechanisms:** epistemic status; rejection.
- **Confirms if:**
  - Loss trace, per A0/A1/A2 run:
    - current rows lost at `modality:carried_only_proposed`: 10.3/8.7/6.0;
    - current rows lost at `polarity:negated_value_read_as_rejection`: 2.0/2.3/0.7;
    - ruled-out rows lost at `polarity:carried_only_positive`: 6.0/5.7/6.0 of 16.
  - E+R\* recovers rows that E+R does not (caused-at polarity).
  - Probe (i) (b), (b2) and (c) do not recover the cases.
  - Step 3 codes them model-limited (if (d) recovers), conversational difficulty, or design-or-model-not-separated.
- **Overturns if:** any of these.
  - Probe (i) (b) or (b2) recovers them (registry-conditioned extraction or out-of-domain examples).
  - The page shows "a modality or negation instruction missing from the prompt": an implementation defect.
  - B3 finds the gold status wrong: an evaluation defect.
- **Text action if confirmed:** keep, and cite the share (about 12 of 45 extraction-lost current rows per A0/A1 run).
- **Text action if overturned:** rewrite: the evaluated extraction prompt misread these values, not the status representation. Cite the probe.
- **Testable here:** yes.
- **Note:** 94c049d. Table tab:design-rationale l.678 ("Classification and transition errors") restates it.

#### C28 · `thesis/implementation_chapter.tex:291` · subsec:decision-schema (D4)

**Claim (gloss).** Scalar keys cost fragmentation and near-duplicate keys. These make filing and question-time key resolution lose values.

```tex
A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics. Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions.
```

- **Where/why:** where and why.
- **Boundaries:** key assignment at extraction; key resolution and expansion; reading (`key_reached`).
- **Mechanisms:** change and supersession; complete decisions; `filing_type_check`.
- **Confirms if:**
  - R recovers a large share of the A0/A1 rows lost at filing and state maintenance (caused-at routing).
  - Within routing, (ii-r) and (ii-h) do not recover the cases, and the page shows that the step lacked no input.
  - The cases are coded architectural weakness or trade-off on this 94c049d passage (D4.p5) under the bound rule and the 0.40 rule. This route is open only for cases caused at key resolution and expansion (sheet K2) or at reading (sheet R), where the design-and-controls register lists D4.p5 as quotable for architectural weakness. Sheet K1 (key assignment at extraction) lists only D4.p3, so a hint-routed case cannot be coded on this passage.
  - At an LLM step, the page also shows that a correct output would still have lost the value.
- **Overturns if:** any of these.
  - (ii-r) recovers: the shortlist or prune excluded a fitting key.
  - (ii-h) recovers under (b): registry-conditioned hinting.
  - The harness reviewer accepted a near-duplicate key: implementation.
  - The cases end design-or-model-not-separated, which is never a design limit.
- **Text action if confirmed:** keep, and cite the routing caused-at count.
- **Text action if overturned:** qualify: the observed routing losses rest on named implementation choices; these codes do not show the fragmentation cost.
- **Testable here:** yes.
- **Note:**
  - 94c049d (D4). Table tab:design-rationale l.680 ("Schema splits") restates it.
  - Already read: "134 of 203 routing-lost rows had every carrier keyed by the extractor's hint" (amendment:45). So (ii-h) decides most routing cases.

#### C29 · `thesis/implementation_chapter.tex:303` · subsec:decision-schema (D4)

**Claim (gloss).** Registry shape alone did not cause the retrieval misses.

```tex
[...] development diagnostics found that changing registry shape did not automatically remove retrieval misses (Section~\ref{sec:design-evolution}).
```

- **Where/why:** why.
- **Boundaries:** reading (`key_reached`).
- **Mechanisms:** none.
- **Confirms if:** none available. No registry-shape condition is run, and the August development archive is not re-analysed.
- **Overturns if:** none available.
- **Text action if confirmed:** keep as development history.
- **Text action if overturned:** keep as development history.
- **Testable here:** no.
- **Note:** the observation is at 94c049d (August development archive); the wording is from 5de9911.

#### C30 · `thesis/implementation_chapter.tex:305` · subsec:decision-schema (D4)

**Claim (gloss).** Reusing keys on label similarity merges different matters under one key. This is why gold values are overwritten on hub keys.

```tex
Semantic reuse treats a label match as concept identity, and the reference-informed reviewer can influence which concepts survive, so cold start is interpreted together with confirmation sensitivity rather than as unaided schema discovery. Expected consequence: useful state coverage from an empty registry; tested as \Hy{6}, with the cost of reuse on a larger schema examined in Section~\ref{subsec:eval-transfer} (mechanism~\ref{mech:hubs}) and taken up as construction insight~7.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution and expansion (surfaces at `current:overwritten_by_non_gold_value`).
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`; `filing_type_check`.
- **Confirms if:**
  - R recovers A0/A1 rows lost at `current:overwritten_by_non_gold_value` (19.7/19.0 per run).
  - The pages show that the successor's claim was routed by expansion reuse (semantic, threshold 0.80) into a key about another matter, so caused-at is key resolution and expansion.
  - Under the class rules this is an implementation choice (criterion (iii): a reuse threshold merged a new matter), not a property of D4.
- **Overturns if:**
  - R does not recover these rows: the successors are about the same matter, so the cause is the state rules.
  - Or the misrouted successors were hint-routed (key assignment at extraction), not reuse-routed.
- **Text action if confirmed:** rewrite: name the evaluated reuse policy and threshold as an implementation choice, and cite the count.
- **Text action if overturned:** qualify: hub overwrites come from hinting or the state rules, not from reuse.
- **Testable here:** partly.
- **Note:**
  - Retrospective (5de9911).
  - The reference-informed clause is not tested: no reference-informed arm runs here (bug 14).
  - Table tab:requirements-design l.997 ("Reuse by label") restates it.
- **Also stated at:** C86 (eval.tex:1065), C121 (conclusion.tex:235); section 5, group F.

#### C31 · `thesis/implementation_chapter.tex:338` · subsec:decision-resolution (D5)

**Claim (gloss).** In the evaluated arm, values are lost to conflicts only through exact ties among first claims, and those conflicts stay open.

```tex
The action threshold is the authority of a meeting decision, above the meeting-discussion authority every transcript receives, so on a transcript-only corpus dissent against a standing scalar fact is either an eligible replacement or a logged no-op. On such a corpus a conflict arises only when initial candidates tie on authority, time and extraction confidence. Chapter~\ref{chap:evaluation} records between none and thirteen such conflicts per autonomous repeat, all left open, [...]
```

- **Where/why:** where and why.
- **Boundaries:** state rules (`proposed`: `tie_left_as_conflict`, `outranked_dissent`, `current_value_ranks_higher`).
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`.
- **Confirms if:**
  - In the loss trace, A0/A1 current rows lost at `proposed:tie_left_as_conflict` stay at about 1 per run or fewer (A0 0, A1 1.0).
  - Dissent against a standing fact surfaces only as no-op sub-codes (`outranked_dissent`, `current_value_ranks_higher`), never as a conflict.
- **Overturns if:**
  - A0/A1 rows are lost to conflicts that are not first-claim ties.
  - Or the conflict contract is admitted (A2: 36.7 rows per run at `proposed:same_meeting_conflict`), which changes the configuration the text describes.
- **Text action if confirmed:** keep, and cite the cycle-2 tie counts beside the cycle-1 range.
- **Text action if overturned:** rewrite the "only when" clause. If the conflict contract is admitted, add the open conflict decision.
- **Testable here:** yes.
- **Note:**
  - Retrospective (9b96138, 38a0f4a, 19 October).
  - Per the amendment, this reports a Ch. 5 observation and is not a design entry (amendment:106).
  - A2 cases at open same-meeting conflicts are coded "held: conflict decision".

#### C32 · `thesis/implementation_chapter.tex:355` · subsec:decision-resolution (D5)

**Claim (gloss).** Once a current fact exists, tied incompatible challengers do not become a conflict. One of them replaces or keeps the value, depending on order.

```tex
In addition, the explicit tie-to-conflict check applies when no current fact exists. The supersession branch selects a maximum without an equivalent check for tied incompatible challengers, so conflict handling is not uniformly complete.
```

- **Where/why:** why.
- **Boundaries:** state rules (`proposed:another_value_won`; `current:overwritten_by_non_gold_value`, `current:displaced_by_other_gold_value`).
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`.
- **Confirms if:**
  - Step 3 has cases caused at the state rules (E+R\* does not recover them) in which tied same-meeting challengers decide a current value without a conflict.
  - The A2 leave-one-out of `resolution_same_meeting_conflict` recovers at least 3 distinct values net per gate-passing run.
- **Overturns if:**
  - R recovers such rows: the challenger was misrouted, so the cause is routing.
  - Or the A0 cases rest on bug 3, where the current value's own claims never competed.
  - Or the leave-one-out shows no gain.
- **If the bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome for the contract clause. Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about the contract. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** keep, and cite the count and the contract result.
- **Text action if overturned:** qualify: the incomplete tie check caused no observed loss. Name routing or bug 3 as the cause.
- **Testable here:** yes.
- **Note:**
  - 94c049d (D5). It overlaps bug 3's order dependence (22-bug-list.md:46).
  - Insight 3 (l.916–918, "uniform conflict and negation handling remain open") and Table tab:design-rationale l.682 ("incomplete conflicts") restate it.
  - Whether a 94c049d sentence that describes a later-found bug is a design entry is decision R-4.

#### C33 · `thesis/implementation_chapter.tex:358` · subsec:decision-resolution (D5)

**Claim (gloss).** Some rejections of a current value are lost because an earlier positive claim blocks them.

```tex
Negation uses different checks: its current-value branch lacks the positive-supersession temporal gate, and an earlier positive claim can block a relevant negation through the affirmation check.
```

- **Where/why:** why.
- **Boundaries:** state rules (demoted: `current:still_current`; ruled-out: `proposed`, `applied`).
- **Mechanisms:** rejection; change and supersession.
- **Confirms if:** in A0, some demoted or ruled-out cases are caused at the state rules by an earlier positive claim blocking the negation, while other negations of a current value take effect. A1 (bug-1 repair) has none.
- **Overturns if:** in A0 the block is universal: the current fact's own claim always affirms it (bug 1). Every A0 case of this kind is then a Phase B bug (repaired), not an occasional limitation.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite as a defect: in the evaluated revision the affirmation check blocked every negation of the current value (bug 1); it is repaired behind a switch.
- **Testable here:** yes.
- **Note:**
  - 94c049d. 22-bug-list.md:17 already reports 0 negations of a current value in 13 cycle-1 dumps (Already read in substance).
  - See also Appendix design_evidence l.81 (C7) and insight 3 (l.916–918). Decision R-4 applies.
- **Also stated at:** C25, C143; section 5, group M.

#### C34 · `thesis/implementation_chapter.tex:364` · subsec:decision-resolution (D5)

**Claim (gloss).** Losses at the proposal step and overwrites in state follow from the per-key ranking. On a one-authority corpus that ranking picks the latest or the most confident claim on the key.

```tex
Resolution is winner-take-all per key: evaluating a claim passes all claims under its key to the resolver, which projects only the top-ranked one, so same-meeting rivals under a scalar key are decided by extraction confidence and the losers never become facts, and on a corpus whose records all carry one authority level the policy reduces to the latest, or most confident, claim filed under a key.
```

- **Where/why:** where and why.
- **Boundaries:** state rules (`proposed:another_value_won`; `current:overwritten_by_non_gold_value`, `current:displaced_by_other_gold_value`); key assignment at extraction and key resolution and expansion (the alternative cause).
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`; `supersession_requires_new_evidence`.
- **Confirms if:** both of these.
  1. A0/A1 rows lost at `proposed:another_value_won` (21.3/15.0 per run) and at `current:overwritten_by_non_gold_value` (19.7/19.0), whose rival or successor is about the same matter (so R is not routing evidence), are coded at the state rules as architectural weakness on D5's 94c049d ranking text, under the bound rule and the 0.40 rule.
  2. The A2 leave-one-out shows `resolution_same_meeting_conflict` or `supersession_requires_new_evidence` recovering at least 3 distinct values net per gate-passing run.
- **Overturns if:**
  - R recovers most of these rows: the rivals and successors come from other matters, so caused-at is routing, and the per-key rule only exposes the misrouting.
  - Or A0's same-meeting replacements are bug-3 cases, where a lower-confidence rival superseded the current value. That contradicts "decided by extraction confidence" for the evaluated revision.
- **If the bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome for condition 2. Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about the contracts. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** keep, and cite the caused-at counts and the contract result.
- **Text action if overturned:** rewrite: these losses surface at the per-key rule but are caused by misrouting (cite R). State that "decided by extraction confidence" holds only with the bug-3 repair.
- **Testable here:** yes.
- **Note:**
  - Retrospective (5de9911). Only D5's 94c049d ranking text (D5.p3) can ground a design code.
  - 22-bug-list.md:47 lists this sentence as contradicted by bug 3.
  - The same claim appears in D10 l.611–613, in Table tab:requirements-design l.989 ("per-key winner-take-all under tied authority and time") and in Appendix design_evidence l.79–80 ("AMI transcripts share one authority level").
  - Already read: 4 of 16 sampled A2 conflict keys hold variants of one matter (amendment:52). Overwrites barely move from A0 to A1 (19.7 against 19.0), although A1 has real meeting dates (bug-6 repair).
- **Also stated at:** C83 (eval.tex:1050, conclusion.tex:229), C111, C120; section 5, group E.

#### C35 · `thesis/implementation_chapter.tex:408` · subsec:decision-review (D6)

**Claim (gloss).** Correctly extracted values are lost to parking and to proposals that wait or expire.

```tex
Deferral and parking can make a correctly extracted fact unavailable when needed.
```

- **Where/why:** where.
- **Boundaries:** key resolution and expansion (`filed`: parked, `no_key`); state rules (`applied`: `proposal_expired`, `proposal_pending_review`).
- **Mechanisms:** `filing_support_check`; `filing_type_check`; evidence and provenance.
- **Confirms if:**
  - Rows are first lost at `filed` (parked) or at `applied` while a correct carrier exists. Per run: A2 about 15 parked (14.0 unsupported by span, 1.0 no fitting key) and 5.3 expired; A1 4.0 expired.
  - Step 3 codes these as design trade-off on D6's 94c049d text, with "the settle expired a correct proposal" ruled out.
- **Overturns if:** any of these. The first is already met (Already read), so the row already points to overturn for the evaluated system.
  - A0 and A1 lose no current row at `filed` (0 per run in both; Already read), so parking costs nothing in the evaluated system on EL2020.
  - A1's expired proposals are coded implementation ("the settle expired a correct proposal").
  - A2's parks are coded to `filing_support_check` (a contract judged by its leave-one-out) or to design-or-model-not-separated.
- **Text action if confirmed:** keep, and cite the counts.
- **Text action if overturned:** qualify: in the evaluated system parking caused no first loss; delayed availability came from the A1 settle repair and the A2 park contracts.
- **Testable here:** yes.
- **Note:** 94c049d. These restate it, with the same action:
  - insight 2 (l.911, "Its cost is that preserved evidence can remain unavailable to questions indefinitely");
  - D1 l.176 ("an admitted claim can wait for concept or value review");
  - Table tab:design-rationale l.680 ("delayed availability").

#### C36 · `thesis/implementation_chapter.tex:470` · subsec:decision-temporal (D7)

**Claim (gloss).** A failed, non-atomic projection can lose or corrupt a state transition.

```tex
Projection is not enclosed in one transaction: review, supersession, creation, link completion, proposal status, and event recording can commit independently. Failure can therefore leave an incomplete transition.
```

- **Where/why:** why.
- **Boundaries:** state rules (`applied:fact_not_found`).
- **Mechanisms:** change and supersession.
- **Confirms if:** a case at `applied:fact_not_found`, or a case page showing a partly committed projection.
- **Overturns if:** no such case in the nine traced runs. Already read: the frozen loss trace has no `applied:fact_not_found` row in any A0/A1/A2 run, so the risk is latent here.
- **Text action if confirmed:** keep, and cite the case.
- **Text action if overturned:** keep as a latent risk. Do not cite it as a cause of observed loss.
- **Testable here:** partly.
- **Note:** 94c049d. Appendix design_evidence l.153–157 and Table tab:design-rationale l.686 ("Non-atomic transitions") restate it.

#### C37 · `thesis/implementation_chapter.tex:502` · subsec:decision-retrieval (D8)

**Claim (gloss).** A loss at any write boundary surfaces at question time as an unknown answer, which looks the same as genuine absence.

```tex
A retrieval gap is visible, but unknown alone cannot distinguish genuine absence from information lost during admission, extraction, review, or retrieval.
```

- **Where/why:** where.
- **Boundaries:** admission; extraction; state rules; reading.
- **Mechanisms:** epistemic status (abstention).
- **Confirms if:** in the nine traced runs, a substantial share of single-value questions whose row was first lost at admission, extraction, filing or state maintenance are answered "unknown" or declined. This comes from the answer records beside the loss trace's question records.
- **Overturns if:** lost rows mostly surface as a wrong value rather than as unknown. For example, `current:overwritten_by_non_gold_value` is the largest state-maintenance loss. Then the risk the text names is not the main one.
- **Text action if confirmed:** keep.
- **Text action if overturned:** qualify: on EL2020 most losses surface as another value, not as unknown.
- **Testable here:** partly.
- **Note:** 94c049d. Table tab:requirements-design l.991 ("Capture loss resembles genuine unknown") restates it. The loss trace records only credit per question, so the split between unknown answers and wrong values needs the answer records.

#### C37a · `thesis/implementation_chapter.tex:505` · subsec:decision-retrieval (D8)

Added in the review of 27 October.

**Claim (gloss).** An open conflict makes its values unanswerable (the unknown branch), unless a standing confirmed fact keeps its value with a caveat.

```tex
Although the public schema defines a disputed outcome, ambiguous facts are excluded by ordinary current-fact retrieval and normally reach the unknown branch; a standing confirmed fact can instead carry a conflict caveat.
```

- **Where/why:** where and why.
- **Boundaries:** reading; state rules (conflicts).
- **Mechanisms:** change and supersession (held: conflict decision); `resolution_same_meeting_conflict`.
- **Confirms if:** single-value questions whose rows were first lost at `proposed:tie_left_as_conflict` or `proposed:same_meeting_conflict` are answered unknown or declined. This needs the answer records beside the trace, as for C37.
- **Overturns if:** those questions are mostly answered with another value, or with a caveated standing value.
- **Text action if confirmed:** keep. Cite the A2 conflict counts as a description of the sentence only: A2's open same-meeting conflict cases are held and unclear in every bound (Rule V item 7), so they bear on no verdict.
- **Text action if overturned:** qualify the sentence with what open conflicts actually produce.
- **Testable here:** partly.
- **Note:**
  - 94c049d (D8.p3).
  - The trace and the sentence do not conflict. The loss trace records the surfaced-at step, filing (`proposed`), where the conflict is left open. The sentence says where the value becomes unanswerable, at reading. Caused-at is left to Step 3.
  - Under Rule V item 7 (amendment:359), A2's open same-meeting conflict cases are "held: conflict decision" and unclear in every bound.
  - The A0/A1 tie conflicts are few (5 rows over 3 values; mapping section 3.1), so the test is weak there.
- **Also stated at:** Table tab:requirements-design l.991 ("conflicts may retain a value"). Related: C31 (implementation_chapter.tex:338), on how the conflicts arise.

#### C38 · `thesis/implementation_chapter.tex:510` · subsec:decision-retrieval (D8)

**Claim (gloss).** Rejections and history are lost to the answer path unless they reach a projected lifecycle state.

```tex
Its cost is restricted answerability. Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims, or events. [...] Negative interpretations must first reach a representable, projected lifecycle state; rejected expansions and rejected state proposals do not become answerable merely because they persist.
```

- **Where/why:** where.
- **Boundaries:** reading; state rules (ruled-out: `applied`).
- **Mechanisms:** rejection; change and supersession.
- **Confirms if:**
  - Most ruled-out rows are lost before a REJECTED fact exists: `polarity:carried_only_positive` about 6 of 16, plus A2's parked negations at 3.3.
  - Few are lost at reading (`key_reached` about 1.3 per A0/A1 run).
  - No ruled-out value is credited without a projected REJECTED fact (`credit_without_state` on ruled-out rows).
- **Overturns if:** rejection questions are credited from negative claims that were never projected, or ruled-out losses concentrate at reading.
- **Text action if confirmed:** keep, and cite the ruled-out profile.
- **Text action if overturned:** qualify: name where rejections are actually lost.
- **Testable here:** partly.
- **Note:** 94c049d. Change-over-time and multi-value rejection questions are not traced, because reading is traced only for single-value questions. The same idea appears at l.112–115 and in Table tab:design-rationale l.688 ("Narrow history and change answering").
- **Also stated at:** section 5, group J.

#### C39 · `thesis/implementation_chapter.tex:525` · subsec:decision-retrieval (D8)

**Claim (gloss).** Change questions lose information that the latest-addition heuristic does not cover.

```tex
This latest-addition heuristic fits some checkpoint questions but is not a general temporal-difference engine.
```

- **Where/why:** where.
- **Boundaries:** reading.
- **Mechanisms:** change and supersession.
- **Confirms if:** none available. Change-over-time questions are excluded from the reading trace, and no probe or code targets them.
- **Overturns if:** none available.
- **Text action if confirmed:** keep.
- **Text action if overturned:** keep.
- **Testable here:** no.
- **Note:** 94c049d. Bug 2 also feeds this heuristic: the change template "sees only a fraction of new values" (22-bug-list.md:36).

#### C40 · `thesis/implementation_chapter.tex:530` · subsec:decision-retrieval (D8)

**Claim (gloss).** Reading loses stored or admitted values because it answers only from resolved keys, never from the evidence text.

```tex
The reader's preference for resolved keys over the admitted evidence text is examined in Section~\ref{subsec:eval-transfer} (mechanism~\ref{mech:reading}) and in the replay of Section~\ref{subsec:eval-replay}.
```

- **Where/why:** where and why.
- **Boundaries:** reading (`key_reached`, `in_payload`, `answered`).
- **Mechanisms:** evidence and provenance; read contract (`answer_evidence_fallback`, `answer_answerability_check`; not run in this amendment).
- **Confirms if:**
  - The offline reading analysis applies to rows lost at `key_reached:other_keys_resolved` (6.7/7.3/3.7 per A0/A1/A2 run). Probe (iii) applies to the A1 and A2 rows only: the probes run on the sampled A1 and A2 runs (amendment:238).
  - Where the holding key was in the recorded question-routing prompt and is about the asked matter, the shortlist alternative is ruled out.
  - Those rows are coded at reading: architectural only if the page shows that D8's 94c049d order would lose the value even with a correct routing output; otherwise design-or-model-not-separated.
- **Overturns if:**
  - Probe (iii) recovers the case: the question-time shortlist or prune (`resolver_prune_threshold`=12) excluded the holding key, an implementation choice at reading.
  - Or the holding key is about another matter: misrouted at write time, so caused-at is routing.
- **Text action if confirmed:** keep the pointer sentence as it is. Report the counts by class, with design-or-model-not-separated cases under their own label (amendment:331); they are never cited as a design limit.
- **Text action if overturned:** rewrite: reading losses come from the question-time shortlist (implementation) or from write-time routing, not from the state-first order.
- **Testable here:** yes.
- **Note:**
  - Retrospective sentence (5de9911). D8's 94c049d text is the only design ground.
  - Already read: "at least 27 of 66 `key_reached` rows had the holding key outside the pruned question-time prompt" (amendment:50).
  - Already read: "In A0 r1, about half of those hold the value under a key unrelated to the question's topic" (23-loss-trace-results.md:105).
- **Also stated at:** C87 (eval.tex:1068, conclusion.tex:252), C113; section 5, group G.

#### C41 · `thesis/implementation_chapter.tex:557` · subsec:decision-provenance (D9)

**Claim (gloss).** A stored value's evidence is lost or wrong because the proposal copies its lineage from the triggering claim, not from the winning claim.

```tex
Scalar resolution considers all claims for a concept, while proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation. If it differs from the selected winner, the projected value and recorded support can diverge.
```

- **Where/why:** where and why.
- **Boundaries:** state rules (proposal construction); reading (evidence questions).
- **Mechanisms:** evidence and provenance.
- **Confirms if:**
  - Loss-trace defect flags: `bug2_cites_span_without_value` on 31–36 current rows per A0 run (33–36 carry any defect flag), and 0 in A1/A2 (`repair_proposal_lineage`).
  - Step 3 pass examinations code A0 evidence passes as resting on this defect (A0 pass rows carry 17/11/20 flags per run, nearly all bug 2).
- **Overturns if:** A1 facts still cite spans without their value, so the divergence has another cause.
- **Text action if confirmed:** rewrite: present it as an implementation defect (bug 2) repaired behind a switch, with its A0 incidence; not as a limit of D9's design.
- **Text action if overturned:** keep as a D9 limitation, and name the remaining cause.
- **Testable here:** yes.
- **Note:**
  - 94c049d. Whether this documented sentence is a design entry or an implementation entry is decision R-4.
  - Table tab:design-rationale l.690 and Table tab:requirements-design l.993 ("Trigger/winner mismatch") restate it; l.582–584 generalises it.
  - The confirm half is largely Already read (the flags are in the frozen trace).
- **Also stated at:** C68, C126; section 5, group I.

#### C42 · `thesis/implementation_chapter.tex:564` · subsec:decision-provenance (D9)

**Claim (gloss).** A demoted fact's citations do not carry the evidence for its rejection.

```tex
Second, demoting an existing fact to rejected retains its earlier evidence rather than copying the rejection proposal's evidence onto it. A citation can therefore support the former positive value without explaining its rejection.
```

- **Where/why:** where.
- **Boundaries:** state rules; reading (evidence).
- **Mechanisms:** evidence and provenance; rejection.
- **Confirms if:** none available. This study has no citation-support measure on demoted facts.
- **Overturns if:** none available. The bug-2 repair deliberately keeps the adoption provenance on the demoted REJECTED fact (22-bug-list.md:190), so A0 and A1 do not differ here.
- **Text action if confirmed:** keep.
- **Text action if overturned:** keep.
- **Testable here:** no.
- **Note:** 94c049d. Appendix design_evidence l.164–166 restates it.

#### C43 · `thesis/implementation_chapter.tex:570` · subsec:decision-provenance (D9)

**Claim (gloss).** Evidence questions can name the wrong meeting because the earliest linked artifact is chosen.

```tex
A provenance question selects an earliest linked artifact using ingestion order, which need not be the original source of the decisive statement.
```

- **Where/why:** where and why.
- **Boundaries:** reading (evidence questions); state rules (lineage).
- **Mechanisms:** evidence and provenance.
- **Confirms if:** in A1 (lineage repaired), the loss trace's evidence-question records still show stored values whose cited meetings exclude the gold meeting, where the earliest-linked rule is the only cause.
- **Overturns if:** wrong meetings occur in A0 but not in A1. The cause was then bug 2's oldest-claim lineage, not the earliest-artifact rule.
- **Text action if confirmed:** keep, and cite the count.
- **Text action if overturned:** qualify: name bug 2 as the cause in the evaluated revision.
- **Testable here:** partly.
- **Note:** 94c049d. 22-bug-list.md:37 records "Evidence answers name the first meeting." as an effect of bug 2.
- **Also stated at:** C76 (eval.tex:1014); section 5, group I.

#### C44 · `thesis/implementation_chapter.tex:577` · subsec:decision-provenance (D9)

**Claim (gloss).** A value whose support lapses stays current unless an explicit rejection or replacement retires it.

```tex
ProjectMemory does not implement justification-based retraction: later support appends a claim identifier without extending the fact's evidence, and a demoted fact retains its earlier evidence. Retraction occurs only through a reviewed rejection or replacement proposal.
```

- **Where/why:** why.
- **Boundaries:** state rules (demoted: `current:still_current`); extraction (when the retirement is stated but not carried).
- **Mechanisms:** change and supersession; rejection; `supersession_requires_new_evidence`.
- **Confirms if:** demoted rows still current at the checkpoint (A0 1.0, A1 0, A2 2.3 per run) whose retirement has no carried negation or successor. Step 3 codes them at the state rules, or at extraction where the retirement was stated but not carried.
- **Overturns if:** still-current demoted rows have a carried successor or negation that a rule or contract blocked. For example, the A2 leave-one-out of `supersession_requires_new_evidence` retires them. The cause is then that rule, not the absence of justification-based retraction.
- **Text action if confirmed:** keep, and cite the count.
- **Text action if overturned:** qualify: name the blocking rule or contract.
- **Testable here:** partly.
- **Note:** retrospective (b422b27, 14 September). About 6 of 9 demoted values are never stored, so their loss lies upstream (23-loss-trace-results.md:74–75).

#### C45 · `thesis/implementation_chapter.tex:606` · subsec:decision-extraction (D10)

**Claim (gloss).** Short scalar claims file more reliably than whole decisions, and a split decision can be rebuilt at read time.

```tex
The benefit intended is coverage from an empty registry: short scalar claims match generated concepts more often than compound statements, and a missed decision can still be reconstructed from its parts at read time.
```

- **Where/why:** why.
- **Boundaries:** extraction; key assignment at extraction and key resolution (`filed`); reading.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:**
  - Step 2c: WD runs lose clearly more rows at filing than the fresh A1 runs (a rise above 13 rows, which fails the WD rule's filing condition) while carrying more values.
  - Rows lost at `carried:split_across_claims` are credited at reading (`credit_without_state`).
- **Overturns if:** WD carries more values with a filing rise of at most 13 rows (WD works under the Step 2c rule), and no split value is credited at reading.
- **Text action if confirmed:** keep, and cite Step 2c.
- **Text action if overturned:** remove the benefit claim, or state that it was not shown.
- **Testable here:** partly.
- **Note:** retrospective (5de9911). Testable only if Step 2c is run; otherwise it stays untested.
- **Also stated at:** section 5, group D.

#### C46 · `thesis/implementation_chapter.tex:608` · subsec:decision-extraction (D10)

**Claim (gloss).** Extraction loses decisions because the contract emits short fragments with no obligation to keep a decision whole.

```tex
The costs are fragmentation and mis-filing. A two-clause rule can be split across two keys, the neighbouring statement of a turn can be filed instead of the decision, [...] The contract places no obligation on keeping a stated decision whole and no check at filing, and both omissions surface in the evaluation.
```

- **Where/why:** where and why.
- **Boundaries:** extraction (`carried`: `claims_without_the_value`, `split_across_claims`).
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** the Step 2c WD rule is met, and (iv) holds on the coded `carried:claims_without_the_value` cases (26–28 rows per run). These are then implementation choices, repaired if WD is admitted. Probes (i) (b), (b2) and (c) do not recover the same cases. The WD rule:
  - every WD run is below every fresh A1 run in current rows lost at `carried`;
  - the mean is lower by more than 9 rows and 5 distinct values;
  - filing rises by at most 13 rows;
  - no owner or role claim is lost;
  - there is no new incidence.
- **Overturns if:** probe (i) (b) or (b2) recovers the cases (registry-conditioned extraction, out-of-domain examples). Or (c) recovers them (unclear, possibly implementation). Or WD is "not shown".
- **Text action if confirmed:** rewrite: the missing whole-decision obligation is an implementation choice (repaired by WD or not). It is not a demonstrated design cost unless D4's 94c049d scalar passage carries it.
- **Text action if overturned:** rewrite: extraction losses rest on registry-conditioned extraction or on the examples (cite the probe). Drop "both omissions surface in the evaluation" for fragmentation.
- **Testable here:** yes.
- **Note:**
  - Retrospective (5de9911). D10 can never ground architectural weakness or a trade-off. Under the WD-cases rule, architectural may be argued only from D4's 94c049d scalar-concept passage.
  - If Step 2c is not run, these cases are coded unclear.
  - Already read: "the first-checkpoint extraction loss rate rises from 27% at meeting a to 46–47% at c and d" (amendment:46).
  - Table tab:design-rationale l.692 and Table tab:requirements-design l.985 ("compound decisions fragment at extraction") restate the claim.
  - The sweeps read WD's outcome differently for the D10 claims; see decision R-20.
- **Also stated at:** C81, C82, C110, C118, C132; section 5, group D.

#### C47 · `thesis/implementation_chapter.tex:611` · subsec:decision-extraction (D10)

**Claim (gloss).** Values are lost because nothing checks a claim's type and cardinality at filing, so wrongly typed rivals compete on a key.

```tex
[...] and a date can land under a key defined as a percentage; once filed, the per-key rule of \Dn{5} decides between such rivals by extraction confidence. The contract places no obligation on keeping a stated decision whole and no check at filing, and both omissions surface in the evaluation.
```

- **Where/why:** where and why.
- **Boundaries:** key assignment at extraction; key resolution and expansion; state rules (`proposed:another_value_won`).
- **Mechanisms:** `filing_type_check`; change and supersession.
- **Confirms if:**
  - A2 leave-one-out: with `filing_type_check` on, every gate-passing A2 run gains at least 3 distinct values net, and none is net negative (works under the admission rule).
  - Step 3 routing cases show type-mismatched rivals.
- **Overturns if:**
  - The leave-one-out shows no gain or a net loss, for example type-check parks of gold carriers (`filed:cycle2_parked_no_fitting_key`, 1.0 per A2 run).
  - Or fewer than 2 runs pass the A2 gate, so the contract is not checkable.
- **If the bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome. Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about the type check. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** keep, and cite the leave-one-out.
- **Text action if overturned:** remove "both omissions surface in the evaluation" for the type check. Keep typed filing as an alternative not taken.
- **Testable here:** yes.
- **Note:** retrospective (5de9911). Table tab:requirements-design l.997 ("no type check at filing") restates it.

#### C48 · `thesis/implementation_chapter.tex:635` · subsec:decision-rendering (D11)

**Claim (gloss).** Abstention on unknown questions comes from the template's fixed decline when nothing resolves.

```tex
The benefit intended is restraint and provenance: a templated answer asserts only stored values and cites their evidence, and a question that resolves to nothing yields an explicit decline.
```

- **Where/why:** why.
- **Boundaries:** reading (unknown questions).
- **Mechanisms:** none (unknown family; decision M-4). Under M-4(b): epistemic status (abstention).
- **Confirms if:** in the loss-trace unknown-question records, credited unknown answers have no key resolved and no fact given.
- **Overturns if:** credited unknown answers had keys resolved and facts given, or failed unknown answers render a resolved key's facts. The decline then does not explain the abstention credit.
- **Text action if confirmed:** keep, and cite the counts.
- **Text action if overturned:** qualify: abstention follows from question-time resolution thresholds; the template only renders it.
- **Testable here:** partly.
- **Note:**
  - Retrospective (5de9911).
  - "Restraint" here is epistemic restraint (DR4), not restraint on incidental talk.
  - The study cannot separate the template from the question-time thresholds (`answer_relevance_min_similarity`=0.42, `answer_canonical_min_similarity`=0.80); see 22-bug-list.md:155.
  - Unknown items reward abstaining (22-bug-list.md section C), so answerable-only accuracy is reported beside them.
- **Also stated at:** C75 (eval.tex:999); section 5, group O.

#### C49 · `thesis/implementation_chapter.tex:637` · subsec:decision-rendering (D11)

**Claim (gloss).** Reading loses values because the template lists everything under the resolved keys and never falls back to the evidence text.

```tex
The cost is that the template has no relevance filter over the values it lists and no route back to the evidence text. A list template concatenates every value under the resolved keys, so a correct value can be buried among unrelated ones or absent while a neighbouring key holds it, and a hub key's current value is rendered whatever it is.
```

- **Where/why:** where and why.
- **Boundaries:** reading (`in_payload`, `answered`; `key_reached`).
- **Mechanisms:** read contract (`answer_evidence_fallback`, `answer_answerability_check`; not run in this amendment); evidence and provenance.
- **Confirms if:**
  - Rows are lost at `answered:answer_or_judge` or at `in_payload` where the case page shows the value present but buried among other values. They are coded at reading, with the scalar-focus-gate cause ruled out.
  - The joint table of first-loss step against RAG's outcome shows RAG credited on those rows.
- **Overturns if:**
  - Once the key is resolved and the fact given, the answer is credited in most cases (14.3 of 16.0 in A0; `answered` losses 1.7/2.7/1.0 per run; Already read).
  - And `key_reached` losses are recovered by probe (iii) or are write-time misroutes. The cost then lies at key resolution or routing, not in the template.
- **Text action if confirmed:** depends on the class of the coded cases.
  - Architectural or trade-off on 94c049d text (D8.p3–p4), with the kappa's lower bound at or above 0.40: keep the cost sentence as a description, name D8.p3–p4 as the ground, and cite the counts.
  - Design-or-model-not-separated, or no class: location only. Report the reading losses and their counts by class, with design-or-model cases under their own label. Do not present the D11 cost sentence as an observed trade-off (amendment:347).
  - In both branches, mark D11 as retrospective.
- **Text action if overturned:** qualify: for single-value questions the template lost at most about 3 rows per run; the reading loss lies at question-time key resolution. Mark D11 as retrospective.
- **Testable here:** partly.
- **Note:**
  - Retrospective (5de9911).
  - List questions are not traced, so the "buried among unrelated ones" case is only partly observable.
  - Table tab:design-rationale l.694 ("No relevance filter; no route back to evidence") restates it.
  - This is the Ch. 4 side of the RAG-gap explanation in mech:reading.
- **Also stated at:** section 5, group G.

#### C50 · `thesis/implementation_chapter.tex:730` · tab:design-evolution

**Claim (gloss).** Matching on the whole span lost values when one topic hid another. Claim-specific matching fixed this, with the span kept as fallback.

```tex
One topic could hide another in matching & Resolve a claim using its entire evidence span & 24 July diff and expansion-miss diagnostic & Matching needs the assertion's scope & Claim-specific matching; span retained as fallback \\
```

- **Where/why:** where and why.
- **Boundaries:** key resolution and expansion.
- **Mechanisms:** none.
- **Confirms if:** Step 3 routing cases at key resolution show no claim keyed by another topic of its span.
- **Overturns if:** routing cases where the span fallback, or another topic in the span, decided the key. The fix is then incomplete.
- **Text action if confirmed:** keep as development history.
- **Text action if overturned:** qualify: the span fallback still misroutes; cite the count.
- **Testable here:** partly.
- **Note:** 94c049d. The other rows of Table tab:design-evolution describe earlier versions and cannot be tested here.

#### C51 · `thesis/implementation_chapter.tex:921` · sec:design-knowledge (insight 4)

**Claim (gloss).** The confirmation step decides which extracted values become answerable, so it limits accuracy.

```tex
Confirmation governs what becomes answerable, so accuracy cannot be separated from admission policy and delayed availability.
```

- **Where/why:** where.
- **Boundaries:** state rules (confirmation; `proposed:same_meeting_conflict`; `applied`).
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`.
- **Confirms if:**
  - The A2 reviewer ceiling recovers a large share of the 36.7 current rows per run lost to open same-meeting conflicts, because the gold value is among the rivals.
  - A1's settle-expired proposals (4.0 per run) are coded at the state rules.
- **Overturns if:** the ceiling recovers few rows because the gold value is rarely among the rivals (the conflicts mix matters). The limiting step is then routing, not confirmation.
- **Text action if confirmed:** keep. Cite the ceiling as an upper bound, not as an estimate of a reviewer.
- **Text action if overturned:** qualify: in the autonomous arm, confirmation was not the limiting step.
- **Testable here:** partly.
- **Note:**
  - 94c049d. "Admission policy" here means the confirmation policy, not D2's gate.
  - The harness reviewer (`_reviewer_would_accept`) is an implementation entry.
  - Reference-informed review is not tested here.
  - Already read: 4 of 16 sampled A2 conflict keys hold variants of one matter (amendment:52).
- **Also stated at:** C67, C93; section 5, group H.

#### C52 · `thesis/implementation_chapter.tex:926` · sec:design-knowledge (insight 5)

**Claim (gloss).** Most losses arise at write time (admission, key formation, projection), not at question time.

```tex
Selecting lifecycle-qualified facts before evidence reduces interpretation at that stage but shifts errors to admission, schema formation, and projection.
```

- **Where/why:** where.
- **Boundaries:** admission; extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** all write-path mechanisms.
- **Confirms if:** in the loss-trace first-loss table, write-time boundaries hold most lost current rows. A0: extraction 46.0, filing 21.7, state maintenance 24.0, against reading 9.3 of asked rows (Already read). The caused-at tables keep most causes before reading.
- **Overturns if:** the caused-at tables move a large share of the write-time surfaced losses to reading.
- **Text action if confirmed:** keep, and cite the table. Replace "admission" with "extraction": admission loses only 4–5 rows per run.
- **Text action if overturned:** rewrite with the caused-at split.
- **Testable here:** yes.
- **Note:** 94c049d.

#### C53 · `thesis/implementation_chapter.tex:932` · sec:design-knowledge (insight 6)

**Claim (gloss).** Stored values are lost at reading when no read route reaches them.

```tex
Stored information needs an explicit read route. A citation to a retained value need not support its latest status. Traceable storage is insufficient for general history questions or claim-level evidence correctness (\Hy{8}; \RQ{2}).
```

- **Where/why:** where.
- **Boundaries:** reading (`key_reached`, `in_payload`, `answered`).
- **Mechanisms:** evidence and provenance; read contract (`answer_evidence_fallback`, `answer_answerability_check`; not run in this amendment).
- **Confirms if:** of the asked rows stored with the right status, 39–47% fail at reading, mostly at `key_reached` (Already read). Step 3 codes them as caused at reading.
- **Overturns if:** the reading losses are caused at write-time routing (the holding key is unrelated to the question's topic), or are recovered by probe (iii) (implementation).
- **Text action if confirmed:** keep, and cite the reading-loss share.
- **Text action if overturned:** qualify: name the cause (routing, or the question-time shortlist).
- **Testable here:** partly.
- **Note:** 94c049d. The citation half is covered by the D9 rows (C41, C43).
- **Also stated at:** section 5, group G.

#### C54 · `thesis/implementation_chapter.tex:939` · sec:design-knowledge (insight 7)

**Claim (gloss).** Cold start moves schema work into operation, and routing then loses values there.

```tex
Finer concepts can simplify transitions while preserving or increasing retrieval and review work. Cold start relocates schema design into operation rather than removing it (Section~\ref{subsec:eval-transfer}, mechanism~\ref{mech:hubs}).
```

- **Where/why:** where and why.
- **Boundaries:** key assignment at extraction; key resolution and expansion.
- **Mechanisms:** change and supersession; complete decisions.
- **Confirms if:** R recovers a large share of the A0/A1 rows lost at filing and state maintenance (caused-at routing), whatever class Step 3 then assigns.
- **Overturns if:** R recovers few rows. The losses are caused at extraction (recovered by E+R only) or at the state rules (not recovered by E+R\*).
- **Text action if confirmed:** keep, and cite R's recovered share.
- **Text action if overturned:** qualify: routing is not the main loss; name the boundary that is.
- **Testable here:** yes.
- **Note:** the core is 94c049d; the pointer to mech:hubs was added at 5de9911. The design-complexity section, l.80–82 ("An open schema moves modelling work into operation rather than removing it"), states the same.
- **Also stated at:** C122 (conclusion.tex:248); section 5, group S.

### 4.6 Chapter 5 (`thesis/eval.tex` and the generated tables it inputs)

Several Ch. 5 counts come from the bug-11 coder: 94 of 178, 37, 27, 35 of 51, 16–22 hub keys, and "three wrong answers". Plan 23 recounts only the extraction-stage cycle-1 numbers, and drops the later-stage ones (23-plan-development-and-confirmation.md:154). The rows replace these counts with loss-trace counts whatever the outcome (decision R-2).

#### C55 · `thesis/eval.tex:455` · subsec:eval-fairness

**Claim (gloss).** No difference between ProjectMemory and RAG in the chapter is attributed to a single component.

```tex
These are declared features of a complete-system comparison: a difference between the arms cannot be attributed to state maintenance, review, concept construction, retrieval order or context allocation in isolation, and no result below is read as isolating one of them.
```

- **Where/why:** why.
- **Boundaries:** all boundaries (the PM–RAG difference).
- **Mechanisms:** none specific (complete-system comparison).
- **Confirms if:** not testable. Every oracle, probe and code in this study varies ProjectMemory only; RAG is never varied. The Step 3 joint table (first-loss step × RAG outcome) locates PM's losses on values RAG got right. It does not isolate a component of the PM–RAG difference.
- **Overturns if:** no result in this study can overturn it.
- **Text action if confirmed:** keep. Make eval.tex:1036–1038, 1076–1078 and 1084–1089 consistent with it: they read the span-level trace as explaining the transfer gap.
- **Text action if overturned:** n/a (not testable here).
- **Testable here:** no.
- **Note:** the threats table states the same claim at eval.tex:1257 ("no result attributes a difference to one mechanism"). The tension is decision R-11.
- **Also stated at:** C18 (implementation_chapter.tex:140); "The comparison does not isolate a single mechanism (Section~\ref{subsec:eval-fairness})," (conclusion.tex:96–97). The same tension recurs within Ch. 6 against conclusion.tex:306 and :330 (C130); see decision R-11.

#### C56 · `thesis/eval.tex:745` · subsec:eval-current-state

**Claim (gloss).** The autonomous arm's shortfall on H1 lies in missing values, not in the status attached to the values it exposes.

```tex
Coverage, not status, is where the public state falls short of \Hy{1}: strict current-state prose is correct on 2/24 and then 4/40 list answers, while the focused candidate/decided questions are answered correctly 34/50 times against RAG's 41/50.
```

- **Where/why:** where.
- **Boundaries:** extraction (polarity, modality); state rules (`status` step); reading.
- **Mechanisms:** epistemic status; complete decisions.
- **Confirms if:**
  - EL2020 first-loss tables: about zero rows lost at `status` (A0 41.3→41.3, A1 41.0→41.0), and polarity and modality a small part of the extraction losses.
  - Step 3 codes few cases under the sub-cause "a modality or negation instruction missing from the prompt".
  - On ES2009, where the claim is made, the Step 5 trace with the adapter shows the same profile.
- **Overturns if:** status-type losses are substantial.
  - Already read: 12.2 of the 45.2 extraction-lost current rows per A0/A1 run are lost at polarity or modality, and `modality:carried_only_proposed` is 8.7–10.3 rows per run.
  - E+R\* over E+R, or the page, sets caused-at extraction (polarity) for many of these cases.
  - Step 5 shows the same on ES2009.
- **Text action if confirmed:** keep, and cite the status-step count.
- **Text action if overturned:** qualify: "mostly coverage; about a quarter of the values lost at extraction were extracted only as proposed or with the wrong polarity".
- **Testable here:** partly.
- **Note:** the sentence concerns answer-level mapped status on ES2009. The trace measures status at state level, on EL2020.

#### C57 · `thesis/eval.tex:750` · subsec:eval-current-state

**Claim (gloss).** The state layer's 1/20 on the ES2009 evidence questions is a scoring mismatch, not lost information.

```tex
the autonomous state layer scores 1/20 on them because the obligations name source meetings while structured values are project facts, a measurement mismatch rather than missing knowledge.
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** evidence and provenance.
- **Confirms if:** only indirectly. The Step 5 ES2009 trace with the adapter (A0, A1-ref) shows that the values behind the evidence items are stored with the right status and cite the gold meeting.
- **Overturns if:** the Step 5 trace shows those values are not stored, or cite no gold meeting, in A1-ref.
- **Text action if confirmed:** keep. State that the prose 20/20 beside it rests partly on bug 2, and give the bug-2-repaired Step 5 figure.
- **Text action if overturned:** qualify: part of the 1/20 is missing knowledge.
- **Testable here:** partly.
- **Note:** plan 23 records "bug 2 propped up the evidence answers" (23-plan-development-and-confirmation.md:352). The threats table repeats the mismatch at eval.tex:1251 ("meeting-identity obligations misfit the state layer").

#### C58 · `thesis/eval.tex:753` · subsec:eval-current-state

**Claim (gloss).** The ES2009 decline across checkpoints may come from the question mix and growing obligations rather than from stored values being lost.

```tex
Recorded autonomous accuracy falls from the first to the fourth checkpoint (Table~\ref{tab:eval-checkpoint-results} in Appendix~\ref{app:reproducibility}); the checkpoints carry different questions and expanding obligations, so this is not a controlled estimate of forgetting.
```

- **Where/why:** why.
- **Boundaries:** state rules (overwriting); extraction; evaluation (question mix).
- **Mechanisms:** change and supersession.
- **Confirms if:** in the Step 5 ES2009 trace per checkpoint, the losses at later checkpoints fall mostly on values new at that checkpoint and are lost at extraction. Few `current:overwritten_*` or `displaced_*` rows involve values that passed at an earlier checkpoint.
- **Overturns if:** a material number of rows (say 5 or more per run) pass at k−1 and are overwritten or displaced at k. That is forgetting at state maintenance. On EL2020, the trace's per-checkpoint rows show the same.
- **Text action if confirmed:** keep.
- **Text action if overturned:** add: "part of the decline is stored values overwritten at later checkpoints (n rows)".
- **Testable here:** partly.
- **Note:** Already read for EL2020: the first-checkpoint extraction loss rate rises from 27% at meeting a to 46–47% at c and d. Probes (i)(b) and (c) test registry-conditioned extraction as one driver. The ES2009 trace reaches reading for only 10 rows.

#### C59 · `thesis/eval.tex:771` · subsec:eval-current-state

**Claim (gloss).** The provenance split does not show its cause. Whether conversational vagueness drives the ES2009 loss is left to the transfer test.

```tex
The strata are entangled with family and list length, so the split records a difference, not its cause; Section~\ref{subsec:eval-transfer} tests the candidate explanation that conversational vagueness drives the loss.
```

- **Where/why:** why.
- **Boundaries:** transcript; evaluation (gold provenance).
- **Mechanisms:** complete decisions.
- **Confirms if:** in the Step 5 ES2009 trace, with each row's source recorded (summlinks, decision annotations, transcript lines), summary-only and transcript-grounded rows have similar first-loss profiles. The 3b codes give few cases of conversational difficulty or evaluation defect.
- **Overturns if:** summary-only rows (27 of the 87) are lost far more often at extraction, and 3b codes them as conversational difficulty or as an evaluation defect in the gold phrasing.
- **Text action if confirmed:** keep the forward reference, and add the Step 5 profile by source.
- **Text action if overturned:** rewrite: provenance or vagueness explains part of the ES2009 loss (n rows).
- **Testable here:** partly.
- **Note:** the transfer test the sentence points to is cross-suite and descriptive (eval.tex:1024–1026).

#### C60 · `thesis/eval.tex:783` · subsec:eval-change-rejection

**Claim (gloss).** The change answers fail because the values are missing, not because strict scoring rejects nearly complete lists.

```tex
Autonomous state change recall is 6.9\% and then 5.0\%, so the failure is not a strict threshold over nearly complete lists.
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** change and supersession.
- **Confirms if:** not tested. The claim follows from the reported recall, and change-over-time questions are outside the trace's reading view.
- **Overturns if:** no result in this study can overturn it.
- **Text action if confirmed:** keep.
- **Text action if overturned:** n/a.
- **Testable here:** no.
- **Note:** bug 2 limited the change filter in A0: it saw 13/51, 11/44 and 9/41 new values (22-bug-list.md:36).
- **Also stated at:** "Autonomous state change recall of 5.0\% shows omission beneath the strict list threshold." (conclusion.tex:44–45); section 5, group W.

#### C61 · `thesis/eval.tex:788` · subsec:eval-change-rejection

**Claim (gloss).** Change and rejection answers fail in how stored representations and the read-side selection rules serve the questions, not for lack of a change path.

```tex
The implemented system does contain a change path, which filters selected facts by whether their earliest supporting artifact is the latest meeting, and it stores rejected and superseded facts. The failures concern how those representations and selection rules fulfil the questions, which Section~\ref{subsec:eval-failure-cascade} examines.
```

- **Where/why:** where and why.
- **Boundaries:** extraction (polarity); state rules; reading.
- **Mechanisms:** change and supersession; rejection; evidence and provenance.
- **Confirms if:** the first-loss tables for ruled-out and change values show these values mostly stored with the right status at k and lost only at reading or list rendering. On ES2009, Step 5 shows the same.
- **Overturns if:**
  - Ruled-out values are mostly lost at extraction. Already read: 9.3/8.7/8.7 of 16 per run, of which 6.0/5.7/6.0 at `polarity:carried_only_positive`. E+R\* over E+R sets caused-at extraction (polarity).
  - For change values: A1, with the bug-2 repair, recovers the change filter's misses. The A0 failure was then a lineage defect, not the selection rule.
- **Text action if confirmed:** keep, and cite the trace.
- **Text action if overturned:** rewrite: "rejections are mostly lost at extraction, where the option is extracted only as a positive claim; the change filter's misses rested partly on a lineage defect (bug 2)".
- **Testable here:** partly.
- **Note:** bug 1 (an asserted negation of the current value never takes effect) and bug 7 (the judge is not told the rejection status) also bear on A0's rejection results. Change-list questions are outside the trace's reading view.
- **Also stated at:** section 5, group J.

#### C62 · `thesis/eval.tex:793` · subsec:eval-change-rejection

**Claim (gloss).** Gold errors (an evaluation defect) limit how the ES2009 feature and change failures at C3 and C4 can be read.

```tex
The three unapplied gold corrections bound the interpretation of the later feature and change obligations (Section~\ref{sec:eval-threats}).
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** change and supersession; complete decisions.
- **Confirms if:** the Step 5 ES2009 runs, scored on the new suite with the B3 corrections, change outcomes on the affected items, and 3b codes those cases as evaluation defects.
- **Overturns if:** applying the corrections changes no Step 5 outcome, and 3b codes no evaluation defect on them.
- **Text action if confirmed:** report the scores under both golds (Step 1 rule).
- **Text action if overturned:** shorten: applying the corrections did not change the outcomes.
- **Testable here:** partly.
- **Note:** the same point is made at eval.tex:238–240 ("so the affected scores are bounded but not corrected").
- **Also stated at:** Ch. 6 applies it to RAG's ES2009 wins: "four of them the plastic-casing question at $C_3$ whose gold status is one of the unapplied corrections" (conclusion.tex:313–315); see C127. Section 5, group X.

#### C63 · `thesis/eval.tex:808` · subsec:eval-restraint

**Claim (gloss).** Four reference-informed unknown answers were lost to an implementation defect in rendering.

```tex
The reference-informed arm's unknown answers are credited 30/30 by the parser and 26/30 by the screening, because four of them are empty strings, a rendering defect that the parser scores as abstention and the stance rule does not.
```

- **Where/why:** why.
- **Boundaries:** reading (rendering).
- **Mechanisms:** none (unknown family; decision M-4). Under M-4(b): epistemic status.
- **Confirms if:** not tested. The reference-informed arm is not run in this study.
- **Overturns if:** not tested.
- **Text action if confirmed:** follow plan 23's open decision on the arm (bug 14).
- **Text action if overturned:** follow plan 23's open decision on the arm (bug 14).
- **Testable here:** no.
- **Note:** plan 23 recommends dropping the arm from the comparisons (23-plan-development-and-confirmation.md:444; line 443 until the Phase F edit of 27 October).
- **Also stated at:** "the reference-informed arm's four empty unknown answers show that an internal unknown status is not the same as a communicated abstention" (conclusion.tex:73–75); section 5, group L.

#### C64 · `thesis/eval.tex:816` · subsec:eval-restraint

**Claim (gloss).** Through H4's wording, abstention comes with an excessive loss of answerable information, which implies a trade-off between restraint and coverage.

```tex
The condition that restraint costs no excessive answerable information does not hold: the previous two subsections record 4/40 correct current-state lists, 58.6\% temporal state recall and no correct strict change answer.
```

- **Where/why:** why.
- **Boundaries:** reading (`in_payload`, near-match); extraction; filing; state rules.
- **Mechanisms:** epistemic status; none for the restraint part (removed by Step 0).
- **Confirms if:** a substantial part of the reading losses are `in_payload:near_match_only`, or Step 3 codes them under the reading cause "the scalar focus gate demoted a correct fact to a near match". In that case, withholding did cost answerable values.
- **Overturns if:** the answerable losses lie upstream of reading (A0/A1: extraction 44–46, filing 22–26, state maintenance 22–24 of 133 rows), and few reading losses are near-match demotions. Then the coverage shortfall is not a cost of restraint.
- **Text action if confirmed:** keep, and cite the near-match count.
- **Text action if overturned:** qualify: H4's loss condition fails, but the loss does not come from abstention. Name where it arises.
- **Testable here:** partly.
- **Note:** the sentence itself names no cause; the implication comes from H4's wording. The claim is about ES2009. EL2020 and Step 5 test where the loss is.
- **Also stated at:** "Restraint also coexists with omitted answerable content, so \Hy{4} holds for abstention and not for its loss condition" (conclusion.tex:70–72); section 5, group Y.

#### C65 · `thesis/eval.tex:826` · subsec:eval-restraint

**Claim (gloss).** The noise-question passes come from the resolver's embedding candidates at question time, not from the admission gate.

```tex
it says nothing about what entered storage, and the ablation of Section~\ref{subsec:eval-ablation} locates the behaviour in the resolver's embedding candidates rather than in the admission gate.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution (question time); extraction (`admitted` step, gatekeeper).
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable.
  - Restraint is removed from the Phase D3 mechanisms, no per-component switches are built (plan 23, bug 8, decided 22 October), and no step re-runs the ablation.
  - The trace records keys resolved and facts given per noise question for A0/A1/A2. That shows whether noise questions resolve to keys, not what makes them pass.
- **Overturns if:** nothing in the study. Known defects already weaken the claim:
  - bug 8: the switch also turned off answer-time retrieval and the relevance gate;
  - bug 10: the resolved counts were read from another checkpoint's trace.
- **Text action if confirmed:** not decided by this study; see decision R-9.
- **Text action if overturned:** not decided by this study; see decision R-9.
- **Testable here:** no.
- **Note:** the DR8 row at eval.tex:1121 makes the same attribution ("the pass depends on the resolver's embedding candidates"; "attributed to the resolver's embedding candidates"). The bug list records restraint as "a by-product of retrieval thresholds" (22-bug-list.md:155). See 22-bug-list.md:101 and :111.
- **Also stated at:** section 5, group C.

#### C66 · `thesis/eval.tex:847` · subsec:eval-confirmation-policy

**Claim (gloss).** The reference-informed arm scores lower because its gate leaves values pending, so fewer facts become answerable.

```tex
The direction is consistent with delayed availability rather than better review. [...] The reviewer rejects or defers concept proposals and the gold-overlap gate leaves values pending, so fewer facts reach the answerable state.
```

- **Where/why:** why.
- **Boundaries:** filing (`applied` step; value confirmation); key resolution and expansion (concept review).
- **Mechanisms:** none specific (review policy).
- **Confirms if:** not tested. The arm is not run. Bug 14 shows that the gate confirms on wording, not on gold values (22-bug-list.md:123).
- **Overturns if:** not tested.
- **Text action if confirmed:** follow plan 23's open decision on the arm.
- **Text action if overturned:** follow plan 23's open decision on the arm.
- **Testable here:** no.
- **Note:** related sentences: eval.tex:855–857 ("gating admission with reference knowledge did not raise task accuracy"), the DR6 row at eval.tex:1119, and eval.tex:1148.
- **Also stated at:** C125 (conclusion.tex:277); section 5, group L.

#### C67 · `thesis/eval.tex:852` · subsec:eval-confirmation-policy

**Claim (gloss).** Value confirmation loses no values in the autonomous arm.

```tex
The autonomous value gate, by contrast, was inert: its traces record 334, 331 and 304 accepted value proposals with five, ten and six pending and none terminally rejected, so admission is not where the autonomous losses arise.
```

- **Where/why:** where.
- **Boundaries:** filing (`applied` step; value confirmation).
- **Mechanisms:** none specific (confirmation).
- **Confirms if:** EL2020 first-loss tables show no A0 rows lost at `applied` (65.3→65.3). Step 3 codes no case caused at confirmation. The Step 5 ES2009 trace for A0 and A1-ref shows the same.
- **Overturns if:** either of these. The first is already met (Already read), so the row already points to overturn for the repaired arm, while A0 meets the confirm condition.
  - Rows are lost at `applied` in the repaired arm: A1 already loses 4.0 rows per run at `applied:proposal_expired`, from the bug-13 settle. Whether Step 3 codes these under "the settle expired a correct proposal" sets their cause, not their location.
  - Or Step 5 shows `applied` losses on ES2009.
- **Text action if confirmed:** keep for A0, and write "value confirmation", not "admission".
- **Text action if overturned:** qualify: in the repaired arm, the settle step loses n rows before application.
- **Testable here:** yes.
- **Note:**
  - "Admission" here means value confirmation, not the gatekeeper of eval.tex:1033 (decision R-12).
  - The same claim is at eval.tex:1223–1224 (ES2009 cascade: "so admission is not the stage at which these losses arise") and in the DR6 row at eval.tex:1119 ("The structural gate rejected nothing").
  - At eval.tex:410–411 the gate "can exclude legitimate short values". The trace's `applied` step tests that too.
- **Also stated at:** C93; section 5, group H.

#### C68 · `thesis/eval.tex:886` · subsec:eval-provenance

**Claim (gloss).** The low citation support comes from failures in linking facts to their evidence.

```tex
\Hy{8} is assessed by both readings, which agree that most emitted evidence links do not fully support the fact they are attached to, consistent with the linking failures in Section~\ref{subsec:eval-failure-cascade}.
```

- **Where/why:** why.
- **Boundaries:** state rules (proposal lineage).
- **Mechanisms:** evidence and provenance; `filing_support_check`.
- **Confirms if:**
  - Already computed: the loss trace's `bug2_cites_span_without_value` flags appear on 31–36 current rows per A0 run (33–36 carry any defect flag) and on none in A1/A2.
  - Step 3's pass examination finds A0 passes resting on bug 2.
  - Together these place the unsupported links in lineage copying (bug 2, repaired in A1). The citation audit itself is not re-run.
- **Overturns if:** A1 facts, with lineage repaired, still cite spans that do not hold their value at a similar rate in the trace's support texts. That would point to another cause, such as the extracted span.
- **Text action if confirmed:** rewrite: "consistent with a lineage defect (bug 2) of the evaluated implementation, repaired in A1". Cite the A0/A1 flag counts.
- **Text action if overturned:** keep "linking failures", and name the other cause.
- **Testable here:** partly.
- **Note:** the 94c049d text documents the divergence: "If it differs from the selected winner, the projected value and recorded support can diverge." (D9.p4). See decision R-4.
- **Also stated at:** C41, C126; section 5, group I.

#### C69 · `thesis/eval.tex:909` · subsec:eval-rag-comparison

**Claim (gloss).** The sign of the ES2009 PM–RAG difference is set by how the unknown-family answers are scored (the evaluation), not by the answerable questions.

```tex
The comparison therefore depends on how abstention is read: the five-repeat difference runs from $+10.2$ points under the recorded reading through $+1.9$ under the machine screening to $-4.2$ under the author's labels, and a small set of contested unknown answers decides the sign (Figure~\ref{fig:eval-forest}).
```

- **Where/why:** why.
- **Boundaries:** evaluation (stance); reading.
- **Mechanisms:** none (unknown family; decision M-4). Under M-4(b): epistemic status.
- **Confirms if:** Step 5's answerable-only analysis on ES2009 (A0, A1-ref and RAG in the same period) shows a PM–RAG difference near zero on answerable questions, so the overall difference comes from the unknown family.
- **Overturns if:** Step 5 answerable-only accuracy shows a clear PM lead or deficit on its own.
- **Text action if confirmed:** keep, and add the answerable-only figures.
- **Text action if overturned:** rewrite the sign statement: the answerable questions also differ by n points.
- **Testable here:** partly.
- **Note:** the same claim is at eval.tex:804–807 ("the recorded advantage depends on how the evaluator recognises stance") and eval.tex:1147–1148. The cycle-1 answerable-only figures are 40.0% for autonomous and 41.4% for RAG (22-bug-list.md:144). Step 5 uses new runs, so it is a consistency check.
- **Also stated at:** these take this row's text actions; section 5, group V.
  - "a lead that depends on how unknown-answer stance is read: it falls to 1.9 points under a machine stance screening and reverses to $-4.2$ under the author's own labels, so the series favours neither architecture" (main.tex:67–70);
  - "A small set of contested unknown answers decides the sign" (conclusion.tex:82–83);
  - "One series whose outcome depends on the stance instrument" (conclusion.tex:89–90).

#### C70 · `thesis/eval.tex:949` · subsec:eval-ablation

**Claim (gloss).** Without embedding candidates, the incidental questions fail because the resolver attaches them to lexically nearby keys.

```tex
The answer texts show the mechanism. Without embedding candidates the resolver attached every one of the 24 incidental questions to a lexically nearby state key, and in 10 of the 13 failures the read path reported an unrelated confirmed fact or fragment.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution (question time); reading.
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable. The ablation is not re-run, and noise questions carry no gold value, so they are not Step 3 cases.
- **Overturns if:** nothing in the study. Bug 10 (22-bug-list.md:111) names the "Resolved 24/24" and "8 of 24" figures as read from another checkpoint. Bug 8 (22-bug-list.md:101): in the traces the resolver gave keys for 1 of 24 questions, while 22 of 24 answers carried keys.
- **Text action if confirmed:** not decided by this study; see decision R-9.
- **Text action if overturned:** not decided by this study; see decision R-9.
- **Testable here:** no.
- **Note:** bug 8 contradicts the claim that the resolver "attached" the questions. The keys came through answer-time retrieval, which the same switch turned off.
- **Also stated at:** C136a (generated/eval_abl_writepath.tex:6, the write-path table's caption and "Resolved" column); section 5, group C.

#### C71 · `thesis/eval.tex:960` · subsec:eval-ablation

**Claim (gloss).** The resolver's embedding candidates produce the restraint, an undeclared role, and do not raise recall.

```tex
The embedding candidate generator therefore functions as a restraint gate on off-topic questions, a role \Dn{8} never assigned to it. It does not raise value recall or list coverage, and the current-state, change and rejection outcomes are unchanged in kind across all five arms.
```

- **Where/why:** why.
- **Boundaries:** key resolution (question time).
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable. Probe (i)(b) uses embedding candidates to cut the extraction registry; it is not a test of the read-side embeddings.
- **Overturns if:** nothing in the study. Bug 8 means the ablation did not isolate the generator.
- **Text action if confirmed:** not decided by this study; see decision R-9.
- **Text action if overturned:** not decided by this study; see decision R-9.
- **Testable here:** no (Ch. 5 sweep). The Ch. 6 sweep treated the recall clause of the same claim at main.tex:73 (C03) as partly testable; see decision R-19.
- **Note:**
  - The summary repeats it at eval.tex:1150 ("The embedding switches contribute restraint, not recall").
  - D8's main intended benefit at 94c049d includes "Current semantics and restraint" (design-rationale table), so "a role D8 never assigned to it" needs checking against 94c049d.
- **Also stated at:** C03, C124; section 5, group C.

#### C72 · `thesis/eval.tex:966` · subsec:eval-ablation

**Claim (gloss).** The ablation's noise failures arise at question-time resolution, but the ablation cannot separate this from filing.

```tex
The failures arise when questions are resolved; because switching the candidates off also changes claim filing, the ablation does not separate the two uses.
```

- **Where/why:** where.
- **Boundaries:** key resolution (question time); key resolution and expansion (filing).
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable here.
- **Overturns if:** nothing in the study. Bug 8: the switch also turned off answer-time retrieval and the relevance gate, so there are three uses, not two.
- **Text action if confirmed:** not decided by this study; see decision R-9.
- **Text action if overturned:** not decided by this study; see decision R-9.
- **Testable here:** no.
- **Note:** if the attribution is kept, the caveat should name answer-time retrieval and the relevance gate (bug 8).
- **Also stated at:** section 5, group C.

#### C73 · `thesis/eval.tex:979` · subsec:eval-ablation

**Claim (gloss).** Semantic concept reuse neither costs nor gains answerable facts; fewer merges only add keys.

```tex
Fewer merges produce more keys, not fewer answerable facts. At this scale the results support neither improved accuracy from semantic reuse nor improved recall from embedding matching; they support the narrower statement about restraint.
```

- **Where/why:** why.
- **Boundaries:** key resolution and expansion.
- **Mechanisms:** none specific (routing); change and supersession.
- **Confirms if:** Step 3 codes few EL2020 routing cases (caused-at key resolution and expansion, set by R) under the sub-cause "a reuse or similarity threshold merged a new matter into an existing key".
- **Overturns if:** many routing-caused cases carry that sub-cause, meaning merges lose answerable values by mixing matters on one key. One sign is R recovering rows whose misrouted claim came through expansion reuse at `expansion_reuse_threshold`=0.80.
- **Text action if confirmed:** keep, bounded to ES2009 and three clusters.
- **Text action if overturned:** rewrite: on EL2020, reuse merges cost n answerable values through misfiling; the ES2009 contrast was too small to show it.
- **Testable here:** partly.
- **Note:** the claim comes from the ES2009 ablation; the study codes EL2020. The sentence's restraint clause falls under decision R-9.
- **Also stated at:** C136 (generated/eval_abl_families.tex:6).

#### C74 · `thesis/eval.tex:997` · subsec:eval-transfer

**Claim (gloss).** The restraint mechanism works on EL2020 too.

```tex
Restraint on incidental questions transfers for both arms, which pass all 24 noise controls.
```

- **Where/why:** why.
- **Boundaries:** key resolution (question time); reading.
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable. Restraint is removed from the Phase D3 mechanisms, and noise questions are not Step 3 cases.
- **Overturns if:** nothing in the study. The EL2020 noise items forbid nothing (22-bug-list.md:138).
- **Text action if confirmed:** not decided by this study; see decision R-9.
- **Text action if overturned:** not decided by this study; see decision R-9.
- **Testable here:** no.
- **Note:** the Ch. 5 sweep recommends stating the noise pass as an observation, without calling it a mechanism that transfers.
- **Also stated at:** section 5, group C.

#### C75 · `thesis/eval.tex:999` · subsec:eval-transfer

**Claim (gloss).** On EL2020, unknown-topic questions fail because the question resolves to a key and an unrelated confirmed fact is asserted.

```tex
Abstention on unknown topics does not: the autonomous arm withholds on 22/30 against RAG's 26/30 [...] and each of its other answers asserts an unrelated confirmed fact, the failure mode the ablation exposed.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution (question time); reading.
- **Mechanisms:** none (unknown family; decision M-4). Under M-4(b): epistemic status.
- **Confirms if:** the loss trace's unknown-question records for A0, A1 and A2 (keys resolved, facts given, credited) show that each wrong unknown answer had a resolved key and a fact given. A1 (bug-10 diagnostics repaired) shows the same.
- **Overturns if:** wrong unknown answers had no key resolved, so the failure lies in rendering or judging. Or A1/A2 abstain where A0 did not, so a defect was the cause.
- **Text action if confirmed:** keep the cause, citing the trace counts. Drop "the failure mode the ablation exposed" (bug 8).
- **Text action if overturned:** rewrite the cause from the trace records.
- **Testable here:** partly.
- **Note:** unknown questions carry no gold value, so Step 3 does not code them. The DR4 row at eval.tex:1117 says "undermined on the transfer series by confident false assertions".
- **Also stated at:** C48 (implementation_chapter.tex:635); "and its other answers assert state the evidence does not support" (conclusion.tex:68); section 5, group O.

#### C75a · `thesis/eval.tex:1010` (subsec:eval-transfer) and `thesis/eval.tex:1115` (tab:eval-synthesis, DR2) · merged

Added in the review of 27 October.

**Claim (gloss).**
- On EL2020 the autonomous arm loses verified values between meetings (persistence), and its accuracy declines from $C_1$ to $C_4$.
- eval.tex:1115 reads the re-ask failure as negative evidence on persistence. The claim is that the loss happens between establishment and re-ask.

Quote at `thesis/eval.tex:1010`:

```tex
Table~\ref{tab:eval-transfer-types} locates the loss. Single-value current-state questions are answered 39/138 times against 95/138, focused rejections 4/24 against 18/24, and a verified fact re-asked two meetings later 4/24 against 20/24. Autonomous accuracy falls from 60.0\% at $C_1$ to 27.8\% at $C_4$ while RAG stays between 70.7\% and 80.0\%.
```

Quote at `thesis/eval.tex:1115`:

```tex
\DR{2} & Low current-list accuracy; every strict change answer fails on both series; verified values re-asked two meetings later 4/24 on EL2020 & Negative evidence on tested completeness, change and persistence; arbitrary history untested\\
```

- **Where/why:** where.
- **Boundaries:** state rules; key resolution and expansion; reading; extraction (if never stored).
- **Mechanisms:** change and supersession; complete decisions (the persist items are in its endpoint, mapping section 6.1).
- **Population.** The failing persist rows per arm: F01–F04 (established at a, re-asked at c) and F20–F23 (established at b, re-asked at d), in the A0 and A1 loss trace. The two conditions below divide this one population.
- **Confirms if:** persistence clause: most failing persist rows passed `status` at the establishing checkpoint and were lost by the re-ask checkpoint, at state maintenance (`current:overwritten_by_non_gold_value`, `current:displaced_by_other_gold_value`) or at reading.
- **Overturns if:** either of these.
  - Persistence clause: most failing persist rows never passed `status` at the establishing checkpoint (lost at `carried:*`, `proposed:*` or another earlier step). Then 4/24 reflects acquisition, not persistence.
  - Decline clause: the $C_1$ to $C_4$ decline comes mostly from values new at c and d that are lost at extraction ("the first-checkpoint extraction loss rate rises from 27% at meeting a to 46–47% at c and d", amendment:46).
- **Already read; the row already points to overturn.** The frozen trace, strict series, gives for the 24 persist rows per arm (figures from the review of 27 October; the Step 3 script recomputes them, and this register is not their source):
  - A0: 14 never pass `status` at either checkpoint, 5 pass it at establishment and not at the re-ask, 4 at both, 1 only at the re-ask;
  - A1: 12, 7, 5 and 0.
- **Text action if confirmed:** keep. Cite n of 8 persist values stored and later lost, with the step. Add that the $C_1$ to $C_4$ decline mixes new and re-asked values.
- **Text action if overturned:**
  - DR2 cell (eval.tex:1115): replace "persistence". Proposed: "re-asked values were mostly never stored (n of 8)".
  - eval.tex:1013: add C58's caveat: the checkpoints carry different questions, so the decline is not a controlled estimate of forgetting.
- **Testable here:** yes. F01–F04@a,c and F20–F23@b,d are endpoint rows (mapping section 6.1).
- **Note:**
  - Mapping decision M-5 concerns the same items. This row moves no item between families.
  - The probe is defined as re-asking a verified fact two meetings after it was established (generated/eval_tr_types.tex:6). "Verified" means gold-verified, not stored.
- **Also stated at:** "Persistence probe (two meetings later)" (generated/eval_tr_types.tex:13), a row of the table this sentence cites; "4/24 persistence probes" (conclusion.tex:37). Related: C58 (eval.tex:753), the ES2009 decline, which carries the caveat "this is not a controlled estimate of forgetting" (eval.tex:756–757). Section 5, group U.

#### C76 · `thesis/eval.tex:1014` · subsec:eval-transfer

**Claim (gloss).** The EL2020 evidence answers fail because the template names the first meeting.

```tex
Evidence questions score 15/21 against 21/21: the autonomous template names the first meeting for every probe, right for the five facts established there and wrong for the two established later.
```

- **Where/why:** why.
- **Boundaries:** state rules (proposal lineage); reading (template).
- **Mechanisms:** evidence and provenance.
- **Confirms if:** the loss trace's evidence-question view (stored value, meetings cited, gold meeting among them) for A0 against A1 shows A0 facts citing only the first meeting and A1 facts, with the bug-2 repair, citing the establishing meeting. The cause is then lineage (bug 2).
- **Overturns if:** A1 still names the first meeting for every probe. The cause is then the earliest-artifact rule, which the 94c049d text documents (D9.p5: "A provenance question selects an earliest linked artifact using ingestion order").
- **Text action if confirmed:** rewrite: "facts cited their key's oldest claim (bug 2), so the template named the first meeting". Report A1.
- **Text action if overturned:** keep, and cite D9.p5 at 94c049d as the documented rule.
- **Testable here:** partly.
- **Note:** plan 23 estimates that corrected lineage moves the EL2020 evidence answers from 15 to 9 of 20 (23-plan-development-and-confirmation.md:100), so the repair cuts both ways.
- **Also stated at:** C43 (implementation_chapter.tex:570); section 5, group I.

#### C77 · `thesis/eval.tex:1018` · subsec:eval-transfer

**Claim (gloss).** Conversational vagueness does not explain the autonomous loss. Write-time normalisation does.

```tex
The clarity explanation suggested by the provenance split did not: on questions whose gold is a verified transcript span, autonomous value recall was 63.6\% on ES2009 and is 30.9\% on EL2020, while RAG's is 77.6\% and 77.9\% [...]. The clearer, real series helped the architecture that re-reads the transcript and hurt the one that normalises it at write time; the comparison across suites is descriptive, since gold construction, question mix and denominators differ.
```

- **Where/why:** why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; transcript.
- **Mechanisms:** complete decisions; change and supersession; WD.
- **Confirms if:**
  - The Step 3 caused-at × class tables (A1, A2; A0 pre-codes) show conversational difficulty as a small share at every boundary.
  - The write-path boundaries hold most of the cases, coded architectural weakness or trade-off on 94c049d text, with the binary kappa's lower bound at least 0.40.
  - On ES2009, 3b also codes little conversational difficulty.
- **Overturns if:** any of these.
  - Conversational difficulty is a large share on EL2020 (a third or more).
  - The write-path cases are coded mainly implementation defect or unclear.
  - 3b codes the ES2009 losses mainly as conversational difficulty.
- **If the bounded verdict of a mechanism concerned is *can't tell (defect-limited)*:** a third outcome, neither confirm nor overturn.
  - Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about that mechanism. The code shares may still be reported.
  - For complete decisions and change and supersession, this condition is decided by Rule M (mapping section 7a), drafted on 27 October 2026 for decision C43 on the decision sheet (mapping decision M-19). For WD it is decided by the Step 2c rule with the bound (amendment:289–296, :451–471, :512–514).
- **Text action if confirmed:** keep, add the code shares, and keep the descriptive caveat.
- **Text action if overturned:** depending on the result:
  - restore vagueness as a partial cause;
  - or rewrite as "hurt the evaluated implementation of write-time normalisation";
  - or say that the corpus explanation is not refuted on ES2009.
- **Testable here:** partly.
- **Note:**
  - "clearer" and the cross-suite comparison are not tested.
  - Step 3's recoverability rule bars conversational difficulty for values that RAG answered from a gold-line chunk in 2 of 3 runs, or that another run passed. A low share is therefore partly by construction. The informative cases are values every run misses.
- **Also stated at:** C04, C118 (conclusion.tex:211, vagueness clause); section 5, group A.

#### C78 · `thesis/generated/eval_tr_funnel.tex:6` (input at `thesis/eval.tex:1028`) · tab:eval-transfer-funnel

**Claim (gloss).** The table assigns each wrong EL2020 answer a loss stage: gatekeeper 3, extraction 94, never a fact 37, overwritten 4, superseded 4, resolver 27, rendered or judged 9.

```tex
Where the 57 verified EL2020 values went in the autonomous arm, per repeat (upper block), and the pipeline stage at which each wrong positive-family answer was lost (lower block). Both are lexical, span-traced codes read from the state and trace dumps [...]; they under-count paraphrases and misclassify some compound values, and are indicative.
```

- **Where/why:** where.
- **Boundaries:** extraction; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession.
- **Confirms if:** the loss-trace v3.1 first-loss tables give the same ordering of boundaries.
- **Overturns if:** the trace already orders them differently in part (Already read): state maintenance is 24.0 rows per A0 run, against the table's 8 (overwritten plus superseded). The units also differ (rows against wrong answers).
- **Text action if confirmed:** replace the table with the loss trace's first-loss table, as plan 23 decides (23-plan-development-and-confirmation.md:154).
- **Text action if overturned:** replace the table with the loss trace's first-loss table, and revise the mechanism counts that cite it.
- **Testable here:** yes.
- **Note:** generated by `20-transfer-tables.py` from `20-failure-funnel.json` and `20-failure-cases.json` (the bug-11 coder). Both actions replace the table, so the text action does not depend on the outcome.

#### C79 · `thesis/eval.tex:1033` · subsec:eval-transfer

**Claim (gloss).** Few values are lost at the gatekeeper, and extraction volume is not the problem.

```tex
Admission and volume did not fail. The gatekeeper admitted 101 of 139 spans as core project signal (ES2009: 61 of 251), extraction produced 588--657 claims per run (ES2009: 622) at a similar rate per thousand characters, and only three wrong answers trace to an ignored span.
```

- **Where/why:** where.
- **Boundaries:** extraction (`admitted` step, gatekeeper); extraction (`carried`).
- **Mechanisms:** none specific (admission).
- **Confirms if:**
  - First-loss tables: `admitted:ignored` is 4.0/4.0/5.0 rows per run (A0/A1/A2) of 133, and `carried:no_claims_from_cited_span` is 0.7–2.0 (Already read).
  - Step 3 codes few cases caused at the gatekeeper ("the gatekeeper ignoring a span its own criteria admit", or design-or-model for `admitted:ignored`).
- **Overturns if:** Step 3 codes a material number of cases (say 10 or more distinct values) caused at admission. Or E+R often has to create evidence spans because the cited span was never admitted.
- **Text action if confirmed:** keep. Replace "three wrong answers" with trace counts (rows and distinct values).
- **Text action if overturned:** qualify: admission causes n values.
- **Testable here:** yes.
- **Note:**
  - "Three wrong answers" comes from the bug-11 coder (`20-transfer-pack.py:221-224` reads `20-failure-cases.json`), and its units differ from the trace's rows.
  - conclusion.tex:204 repeats the first clause ("admission and extraction volume held"); that location is merged into C81.
- **Also stated at:** C81 (conclusion.tex:204); section 5, group K.

#### C80 · `thesis/eval.tex:1036` · subsec:eval-transfer

**Claim (gloss).** The EL2020 loss lies in four mechanisms after admission, and each is caused by a Chapter 4 design decision.

```tex
The loss lies in four mechanisms downstream of admission, each attributable to a design choice of Chapter~\ref{chap:implementation}.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession; evidence and provenance; WD; `resolution_same_meeting_conflict`; `supersession_requires_new_evidence`.
- **Confirms if:** in the Step 3 surfaced × caused tables per arm, for each of the four mechanisms, most sampled cases at its boundary are coded architectural weakness or design trade-off on quoted 94c049d text, under the bound rule. The binary kappa's lower 95% bound is at least 0.40, and there are few unrepaired implementation or unclear cases.
- **Overturns if:** any of these.
  - Implementation defect (including Phase B bugs in A0), unclear, model-limited or design-or-model codes dominate at a boundary.
  - The kappa's lower bound is below 0.40. Then no loss may be reported as a design limit on these codes.
  - A large caused-at share falls outside the four mechanisms, for example evaluation defects.
- **Text action if confirmed:** keep. Cite the code shares per mechanism and the 94c049d paragraphs (not D10 or D11).
- **Text action if overturned:** rewrite as "The loss surfaces at four boundaries downstream of admission", with causes per boundary from the codes. Remove "each attributable to a design choice".
- **Testable here:** yes.
- **Note:** the amendment allows a statement that a loss comes from the design only where the codes say architectural or trade-off on 94c049d text, with the kappa's lower bound at or above 0.40 (amendment:572).
- **Also stated at:** C55 (the tension with eval.tex:455; decision R-11).

#### C81 · `thesis/eval.tex:1040` (mech:extraction) and `thesis/conclusion.tex:204` (par:conc-acquisition) · merged

**Claim (gloss).** The largest group of losses happens at extraction: the admitted span yields claims, but none carries the value (fragments, neighbouring statements, a missing number, a garbled or inverted reading). conclusion.tex:204 adds that admission and extraction volume held.

Quote at `thesis/eval.tex:1040`:

```tex
\emph{Fragmenting extraction} (94 of the 178 wrong positive-family answers). The verified span was admitted and produced claims, a median of five, none of which carries the asked value: the extractor kept fragments of a two-clause rule under separate keys, the neighbouring statements of the same turn, or a garbled or inverted reading.
```

Quote at `thesis/conclusion.tex:204`:

```tex
The transfer check tested that boundary directly. On EL2020 admission and extraction volume held, yet in 94 of the 178 wrong positive-family answers the admitted span produced claims that did not carry the decision (Section~\ref{subsec:eval-transfer}, mechanism~\ref{mech:extraction}). They kept fragments of a two-clause rule under two keys, the neighbouring instruction from the same turn, a number that appears in no claim, or an inverted reading.
```

- **Where/why:** where.
- **Boundaries:** admission; extraction (`carried`, polarity).
- **Mechanisms:** complete decisions; epistemic status; WD.
- **Confirms if:** in the first-loss tables, adjudicated series:
  - extraction is the largest boundary (A0 46.0, A1 44.3 of 133);
  - `carried:claims_without_the_value` is the largest sub-code (28.3/26.3), and `admitted:ignored` is small (4.0 rows);
  - this holds under v2 after the V4 audit;
  - E+R recovers these rows where R does not, which sets caused-at extraction.

  Already read: 71 of 130 rejected texts state one part of a multi-part value.
- **Overturns if:** any of these.
  - Under v2 (audit agreement below 0.80), extraction is no longer the largest boundary. In the raw strict series it is level with filing in A1 (30.0 against 29.3). Or v2 turns many "does not carry" decisions into carriers, moving rows from extraction to filing.
  - E+R adds few rows beyond R.
  - Many cases are caused at routing despite surfacing at extraction.
- **Text action if confirmed:** keep the location. In both places, replace "94 of the 178" with loss-trace counts (rows and distinct values per run), labelled adjudicated.
- **Text action if overturned:** qualify: extraction is the largest boundary only in the adjudicated series; under perfect routing its share is n. Rewrite the location per v2 and the oracle.
- **Testable here:** yes.
- **Note:**
  - The 94/178 comes from the bug-11 coder. P0-C drops or recomputes it whatever the outcome. Plan 23 recounts the cycle-1 extraction-stage numbers (23-plan-development-and-confirmation.md:154).
  - "Garbled or inverted reading" overlaps the polarity sub-codes.
  - Adjudication moves 11–14 rows per run to extraction.
  - "A number that appears in no claim" may partly be bug 11, which drops tokens of two characters or fewer.
- **Also stated at:** C46 (implementation_chapter.tex:608), C79 (eval.tex:1033); section 5, group D.

#### C82 · `thesis/eval.tex:1047` · mech:extraction

**Claim (gloss).** Fragmenting extraction is caused by D10's contract: scalar claims, with no obligation to keep a decision whole.

```tex
This is the extraction contract of \Dn{10}: scalar claims under generated keys, with no obligation to keep a stated decision whole.
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** Steps 2c, 2b (i) and 3 together:
  - WD and fresh A1 both carry the value in at most 1 of 3 runs, with WD in 0;
  - probes (b), (b2) and (c) do not recover;
  - the case is coded architectural weakness from D4's scalar-concept passage at 94c049d ("The September defaults favour scalar concept generation", D4.p5), never from D10, which is retrospective.
- **Overturns if:** any of these.
  - (iv) holds (WD carries the value in 2 of 3 runs, fresh A1 in at most 1): implementation choice.
  - (b) or (b2) recovers: registry-conditioned extraction or out-of-domain examples (implementation).
  - Only (c) recovers: unclear.
  - Only (d) recovers: model-limited.
  - Step 2c is not run: every such case is unclear.
- **Text action if confirmed:** rewrite the ground as D4.p5 at 94c049d, and mark D10 as a description written after the runs.
- **Text action if overturned:** remove "This is the extraction contract of D10". Rewrite as an implementation choice of the extraction prompt (with its sub-cause), or as not separated from the model, or as unclear.
- **Testable here:** yes.
- **Note:**
  - D10 entered at 5de9911 (19 October). Already read: the extraction prompt grows from 2.5k to about 39k characters.
  - This row reads WD working as overturning the claim; C46, C110 and C118 read it as confirming the missing obligation as the cause. The text actions agree; see decision R-20.
- **Also stated at:** C46, C110, C118; section 5, group D.

#### C83 · `thesis/eval.tex:1050` (mech:filing) and `thesis/conclusion.tex:229` (par:conc-lifecycle) · merged

**Claim (gloss).** Carriers are lost at filing because D5 ranks all claims under a key and, with authority and time tied inside one meeting, the most confident claim takes the scalar key and its rivals are never projected.

Quote at `thesis/eval.tex:1050`:

```tex
\emph{Winner-take-all filing} (37 cases). A claim that carried the value never became a fact because the resolution engine ranks all claims under a key by authority, source time and extraction confidence (\Dn{5}); with authority and time tied inside one meeting the highest-confidence claim takes a scalar key and its rivals are never projected. A page limit filed under a key defined as a percentage lost to a date filed under the same key with higher confidence.
```

Quote at `thesis/conclusion.tex:229`:

```tex
The engine ranks all claims under a key, so inside one meeting the highest-confidence claim takes a scalar key and its rivals are never projected (mechanism~\ref{mech:filing}).
```

- **Where/why:** where and why.
- **Boundaries:** state rules (filing: `proposed` step); key assignment at extraction; key resolution and expansion.
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`; `filing_type_check`.
- **Confirms if:**
  - Rows surfaced at `proposed:another_value_won` (A0 21.3, A1 15.0 per run) are not recovered by R or E+R\*, and the page shows the displaced rival is about the same matter. Caused-at is then the state rules.
  - They are coded architectural or trade-off on D5.p3 at 94c049d: "Eligible challengers are ranked by authority, source time, and extraction confidence." and "The same ranking selects an initial asserted positive candidate."
  - Supporting (Ch. 6 sweep): the reviewer ceiling is large, and `resolution_same_meeting_conflict` "works" in the leave-one-out.
- **Overturns if:** any of these.
  - R recovers most of these rows: the rival was another matter misfiled on the key, so the cause is routing, by hint or by resolver. Already read: 12 of the 16 sampled A2 conflict keys mix different matters (10 with unrelated values, 2 with two different gold values; 23-el2020-arms.md:77–79).
  - A0 cases are model-coded to bug 3 or bug 13. They count as repaired (Phase B rule). This bullet concerns only what Step 3 codes to those bugs. Already read: A1 replaces about 6 `another_value_won` losses with `proposal_expired` (4.0) and `current_value_ranks_higher` (3.3), the bug-13 and bug-3 repairs at work (23-loss-trace-results.md:90). So for that part the row already points to overturn.
  - The `filing_type_check` leave-one-out recovers the type-mismatch class (a date under a percentage key). The cause is then filing without a type check, coded implementation or unclear (D10 is retrospective).
  - `resolution_same_meeting_conflict` does not work (A2 left 36.7 rows per run in unresolved conflicts).
- **Text action if confirmed:** keep. Cite D5.p3 at 94c049d, and replace "37 cases" with trace counts.
- **Text action if overturned:**
  - Routing (first bullet), type check or conflict contract: rewrite as a routing loss that surfaces at resolution. Proposed for eval.tex:1050: "a claim about another matter, filed under the key, outranked it". Proposed for conclusion.tex:229: "rivals from other matters filed under the same key displaced the value; the ranking only chose between them".
  - Bugs 3 and 13 (second bullet): state that part of A0's `another_value_won` rested on bugs 3 and 13, repaired in A1.
- **Testable here:** yes.
- **Note:** the "winner-take-all" wording of the current D5 entered at 5de9911 (implementation_chapter.tex:363–372) and is retrospective. D5.p3 at 94c049d is the admissible basis. "37 cases" comes from the bug-11 coder.
- **Also stated at:** C34 (implementation_chapter.tex:364), C111 (conclusion.tex:186), C120 (conclusion.tex:221); section 5, group E.

#### C84 · `thesis/eval.tex:1057` (mech:hubs) and `thesis/conclusion.tex:232` (par:conc-lifecycle) · merged

**Claim (gloss).** Many verified values were stored and later replaced by unrelated values under heavily used keys. The loss surfaces at state maintenance; conclusion.tex:232 implies routing as the cause.

Quote at `thesis/eval.tex:1057`:

```tex
\emph{Overwriting under reused keys}. In each repeat 16--22 generated keys held five or more facts, and among superseded facts that carried a verified value the successor was an unrelated value in 35 of 51 cases in the first repeat (18 of 39 and 41 of 64 in the others).
```

Quote at `thesis/conclusion.tex:232`:

```tex
Among superseded facts that carried a verified value, the successor was an unrelated value in 35 of 51 cases in the first repeat (mechanism~\ref{mech:hubs}): a call length replaced by a session limit from a different tool, a submission deadline by a different deadline.
```

- **Where/why:** where.
- **Boundaries:** state rules (`current` step); key assignment at extraction; key resolution and expansion.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`; `filing_type_check`.
- **Confirms if:**
  - First-loss tables: `current:overwritten_by_non_gold_value` is the main state-maintenance sub-code, 19.7 (A0) and 19.0 (A1) rows per run, and it stays in A1 after the bug-3 and bug-6 repairs (Already read).
  - For the routing implied at conclusion.tex:232: R recovers most of those rows.
- **Overturns if:**
  - The trace already gives the location as surfaced-at. It is overturned only if v2 (after the V4 audit) moves these rows elsewhere.
  - For "unrelated": neither R nor E+R\* recovers the rows, and the case pages show the successor is the same matter (a legitimate later value or a recap). "Unrelated" would then be overstated.
- **Text action if confirmed:** keep the location. Replace "35 of 51" and "16--22" (bug-11 coder) with trace counts.
- **Text action if overturned:** qualify with the v2 counts. Replace "unrelated" with the coded share.
- **Testable here:** yes.
- **Note:** P0-C lists 35 of 51 among the counts to drop or recompute. The cause is in C85 and C86.
- **Also stated at:** section 5, group F.

#### C85 · `thesis/eval.tex:1060` (mech:hubs) and `thesis/conclusion.tex:226` (par:conc-lifecycle) · merged

**Claim (gloss).** Overwriting happens because uniform authority and undated transcripts reduce D5's supersession rule to "the latest asserted claim wins". Both places attribute the fallback to ingestion time to the corpus.

Quote at `thesis/eval.tex:1060`:

```tex
Every record of a transcript-only corpus carries the same authority level, so the authority ordering of \Dn{5} has no effect, and source time falls back to ingestion order because the transcripts carry no date, so the supersession rule reduces to the latest asserted claim filed under a key whatever its content.
```

Quote at `thesis/conclusion.tex:226`:

```tex
On EL2020 the rule's effect is measured rather than illustrated. Every transcript carries the same authority level, so the authority half of the gate never discriminates, and the temporal half compares ingestion times, because the transcripts carry no source date.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`.
- **Confirms if:** authority clause only.
  - The overwrite rows are not recovered by R or E+R\*, so caused-at is the state rules.
  - They are coded design trade-off on D5.p6 at 94c049d, which states the uniform authority: "The AMI workflow normally assigns the same discussion authority to every transcript" (D5.p6). Sheet S of the design-and-controls register lists D5.p6 for a trade-off only, not for architectural weakness.
  - D5.p5 ("Two participants in one meeting therefore normally inherit the same authority. Source time is the artifact timestamp, falling back to ingestion time", D5.p5) is a disclosed limitation in that register (its decision 2). It grounds no code unless that decision is signed as (b) or (c).
- **Overturns if:**
  - **Date clause: already contradicted.** The EL2020 transcripts are dated (eval.tex:295–296); the runner did not pass the dates (bug 6, 22-bug-list.md:65). A0 cases model-coded to bug 6 count as repaired. A1 passes the dates and still loses about as many overwrite rows (19.0 against 19.7; Already read), so the dates are not the cause.
  - R recovers these rows: the overwriting value is another matter misfiled on the key, so caused-at is routing.
  - The `supersession_requires_new_evidence` leave-one-out in A2 measures the alternative.
- **Text action if confirmed:** remove "because the transcripts carry no (source) date" in both places (the defect was the runner's, bug 6). Keep the authority part, citing D5.p6, and D5.p5 only if design-and-controls decision 2 is signed as (b) or (c).
- **Text action if overturned:** rewrite as routing: "a value about another matter, filed under the key, replaced it". Rewrite the date clause: "the evaluated runner did not pass the recorded meeting dates (bug 6, repaired in A1), so source time fell back to ingestion time".
- **Testable here:** yes (eval.tex:1060); partly (conclusion.tex:226).
- **Note:**
  - The date clause is contradicted by the Phase B record whatever this study shows (section 6.2; decision R-3). The front sweep's decision cites it at conclusion.tex:229, where the clause ends.
  - Bug 3 (a same-meeting rival supersedes the current value) also feeds the A0 overwrites. A0 cases resting on a Phase B bug count as repaired.
- **Also stated at:** C91 (eval.tex:1116), C92 (eval.tex:1125); section 5, group F.

#### C86 · `thesis/eval.tex:1065` · mech:hubs

**Claim (gloss).** D4's concept reuse creates the overloaded keys under which values are overwritten.

```tex
The history \Dn{7} preserves is intact, which is what made this analysis possible, but the current value it exposes is wrong; the reuse behaviour of \Dn{4} supplies the keys.
```

- **Where/why:** why.
- **Boundaries:** key resolution and expansion; key assignment at extraction.
- **Mechanisms:** none specific (routing); change and supersession.
- **Confirms if:**
  - In the routing cases (those R recovers), the misrouted claim mostly came through the resolver or expansion path, with the sub-cause "a reuse or similarity threshold merged a new matter into an existing key" or "the harness reviewer accepted a near-duplicate or over-broad key".
  - R-resolver also exceeds R-hint against base rates.
  - Both sub-causes are implementation entries in the register, so even a confirm moves the cause from D4 to the implementation.
- **Overturns if:** the path is mostly the extractor's hint, so caused-at is key assignment at extraction. Already read: 134 of 203 routing-lost rows had every carrier keyed by the hint. If (ii-h) recovers under (b), the sub-cause is registry-conditioned hinting.
- **Text action if confirmed:** rewrite: "the reuse threshold and the harness reviewer supply the keys" (implementation). Cite D4.p4 at 94c049d only if it is the coded ground ("Review may itself merge distinct meanings").
- **Text action if overturned:** rewrite: "the extractor's key hints supply the keys".
- **Testable here:** yes.
- **Note:** the DR7 row at eval.tex:1120 states the same claim ("concept reuse formed 16--22 hub keys").
- **Also stated at:** C30 (implementation_chapter.tex:305), C121 (conclusion.tex:235, a related claim with a different test); section 5, group F.

#### C87 · `thesis/eval.tex:1068` (mech:reading) and `thesis/conclusion.tex:252` (par:conc-aggregation) · merged

**Claim (gloss).** Stored values are lost at reading because question-time resolution ranks a generic key with an overlapping label above the holding key, or finds no key, and the template reader does not fall back to the evidence (D8, D11).

Quote at `thesis/eval.tex:1068`:

```tex
\emph{Schema-first reading} (27 cases with a live carrier). Where a live fact carrying the value existed, question-time resolution ranked a generic key with an overlapping label above it, or found no key, and the templated reader rendered that key's values or declined without consulting the admitted evidence text (\Dn{8}, \Dn{11});
```

Quote at `thesis/conclusion.tex:252`:

```tex
The transfer check adds the single-value case. Where a live fact carrying the verified value existed, question-time resolution ranked a generic key with an overlapping label above it, or found no key, and the templated reader of \Dn{11} rendered that key's contents or declined.
```

- **Where/why:** where and why.
- **Boundaries:** reading.
- **Mechanisms:** none (reading; no Phase D3 mechanism).
- **Confirms if:**
  - For `key_reached:other_keys_resolved` rows (A0 6.7, A1 7.3 per run), the Step 2 offline reading check finds the holding key in the question-time prompt, ranked below a chosen key with label overlap.
  - Probe (iii) does not apply, or is not recovered. It runs only on the sampled A1 and A2 runs (amendment:238), so it never applies to the A0 rows.
  - At this LLM step there is no model condition. The code is therefore design-or-model-not-separated, unless the page shows that a correct resolver output would still lose the value.
  - An architectural code needs 94c049d text (D8.p4: "Its cost is restricted answerability"), not D11.
- **Overturns if:**
  - The offline check finds the holding key pruned out of the prompt, and (iii) recovers those cases. The cause is then the shortlist parameter (`resolver_prune_threshold`=12, `embedding_top_k`=8), an implementation choice at reading. Already read: at least 27 of 66 `key_reached` rows had the holding key outside the pruned question-time prompt.
  - Or the `in_payload` losses are coded under the scalar focus gate.
- **Text action if confirmed:** depends on the class of the coded cases.
  - Architectural or trade-off on D8.p3–p4 at 94c049d, with the kappa's lower bound at or above 0.40: eval.tex:1068: rewrite with D8.p3/p4 as the ground. conclusion.tex:252: keep, with counts from the offline analysis.
  - Design-or-model-not-separated, or no class: location only in both places, with no design ground. Proposed: "lost at question-time key resolution; design and model not separated". Report these cases under their own label (amendment:331).
  - In both branches: drop D11 as a ground, and mark it as retrospective.
- **Text action if overturned:** rewrite. Proposed: "the question-time shortlist excluded the holding key in X of Y cases (an implementation parameter)". Mark D11 as retrospective.
- **Testable here:** yes.
- **Note:** D11 entered at 5de9911 and is retrospective; the admissible 94c049d basis is D8.p3–p4. "27 cases" comes from the bug-11 coder.
- **Also stated at:** C40 (implementation_chapter.tex:530), C113 (conclusion.tex:188); section 5, group G.

#### C88 · `thesis/eval.tex:1072` (mech:reading) and `thesis/conclusion.tex:256` (par:conc-aggregation) · merged

**Claim (gloss).** The runner's diagnosis supports schema-first reading: about half of all questions resolve to a wrong key.

Quote at `thesis/eval.tex:1072`:

```tex
the runner's own diagnosis records a wrong-key resolution for 54--57 of the 105 questions per repeat.
```

Quote at `thesis/conclusion.tex:256`:

```tex
The runner diagnosed a wrong-key resolution for about half of all questions on both series, over a larger schema on EL2020 (mechanism~\ref{mech:reading}).
```

- **Where/why:** where.
- **Boundaries:** reading.
- **Mechanisms:** none (reading).
- **Confirms if:** cannot be confirmed. The figure is the bug-9 diagnosis, which is true by construction in cold-start runs.
- **Overturns if:** already overturned.
  - Bug 9 (22-bug-list.md:106). Only 10 of 166 EL2020 wrong-key diagnoses had a resolved key holding a gold value (plan 23, bug-effect table).
  - The frozen loss trace puts `key_reached` at 6.7–7.3 of 133 current rows per A0/A1 run, about 30% of the asked rows stored with the right status.
- **Text action if confirmed:** n/a.
- **Text action if overturned:** remove the count (P0-C). If a figure is needed, use the loss trace's `key_reached` counts, or A1's repaired diagnostic (`repair_dump_diagnostics`).
- **Testable here:** already decided before signing. The Ch. 6 sweep marked it "yes" (the frozen trace overturns it); the Ch. 5 sweep marked it "no" (the figure is defective). Either way, the text action does not depend on this study.
- **Note:** this is an evaluation defect in the instrument (bug 9, repaired by `repair_dump_diagnostics`), not an outcome of this study. Principle 3 repeats the figure (C112, conclusion.tex:187).
- **Also stated at:** C112; section 5, group G; section 6.2.

#### C89 · `thesis/eval.tex:1076` · subsec:eval-transfer

**Claim (gloss).** The RAG gap arises because ProjectMemory never re-reads the source text, the step through which RAG succeeded.

```tex
RAG succeeded by the step these mechanisms omit: in 120 of the 124 answers it got right where the autonomous arm was wrong, a cited chunk contained the verified gold line and free generation restated the whole sentence.
```

- **Where/why:** why.
- **Boundaries:** extraction; state rules; reading.
- **Mechanisms:** complete decisions; evidence and provenance.
- **Confirms if:** in the Step 3 joint table (first-loss step × RAG outcome), the values RAG answered from a gold-line chunk are lost by PM at extraction, filing or state maintenance. They are coded architectural or trade-off (no in-design alternative recovers them). Already read: 75 of 119 single-value extraction-lost rows had a credited RAG answer citing a gold line in 2 of 3 runs.
- **Overturns if:** those values are coded implementation by probe (b), (b2), (ii-r), (ii-h) or (iii), or by WD (iv). The gap then reflects the evaluated implementation, not the missing re-reading step. The same applies if many are reading losses with the holding key pruned.
- **Text action if confirmed:** keep as a description of RAG's success, and add PM's losing boundary from the joint table.
- **Text action if overturned:** qualify: "RAG re-read the line; ProjectMemory lost these values mostly to implementation choices at [boundary]".
- **Testable here:** partly.
- **Note:** RAG is not varied. This is in tension with eval.tex:455–458 (decision R-11).
- **Also stated at:** C128 (conclusion.tex:322), C130 (conclusion.tex:330); section 5, group N.

#### C90 · `thesis/eval.tex:1078` · subsec:eval-transfer

**Claim (gloss).** Evaluation errors do not explain the EL2020 gap.

```tex
A judge effect is present in both arms and larger for RAG, since 23 RAG and 8 autonomous wrong answers lexically cover every required value (Section~\ref{sec:eval-threats}); it does not explain the gap.
```

- **Where/why:** why.
- **Boundaries:** evaluation (judge).
- **Mechanisms:** none specific (evaluation).
- **Confirms if:** Step 3 codes evaluation defects (gold, suite, adjudication or judge) on a small share of EL2020 PM losses, well below the gap, and the pass examination finds few judge false positives.
- **Overturns if:** evaluation-defect codes cover a share of PM losses comparable to the gap (tens of points).
- **Text action if confirmed:** keep, and add the evaluation-defect count.
- **Text action if overturned:** qualify the direction claim, and give the size of the evaluation effect.
- **Testable here:** partly.
- **Note:** RAG's answers are not coded. The bug-7 rescoring already moved the gap from −35.0 to −33.0 (23-plan-development-and-confirmation.md:228). The focused-rejection counts at eval.tex:1012 (4/24 against 18/24) become 6/24 against 17/24 under the bug-7 repair.
- **Also stated at:** C101 (eval.tex:1263).

#### C91 · `thesis/eval.tex:1116` · tab:eval-synthesis

**Claim (gloss).** Uniform authority made the supersession rule overwrite state and left the dissent conflict unreachable.

```tex
under uniform authority the supersession rule overwrote current state, and the conflict outcome \DR{3} requires for dissent against standing state was unreachable on these corpora because transcript authority sits below the dissent threshold; the recorded conflicts are tied first claims
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; rejection; `resolution_same_meeting_conflict`.
- **Confirms if:**
  - Overwriting: as in C85 (overwrite rows not recovered by R or E+R\*, coded design trade-off on D5.p6; no code on D5.p5 unless design-and-controls decision 2 is signed as (b) or (c)).
  - Conflicts: `outranked_dissent` and `tie_left_as_conflict` are at most 1 row per run in A0/A1 (not listed in the results table), consistent with an unreachable dissent conflict.
- **Overturns if:**
  - R recovers the overwrite rows, so the cause is routing.
  - For conflicts: A2's `resolution_same_meeting_conflict` shows that conflicts are reachable for same-meeting rivals (36.7 rows per run), so "unreachable on these corpora" holds only for the evaluated rule.
- **Text action if confirmed:** keep, and add "under the evaluated rule".
- **Text action if overturned:** rewrite the overwrite cause as routing, and limit "unreachable" to the A0 rule.
- **Testable here:** partly.
- **Also stated at:** C85, C92; section 5, group F.

#### C92 · `thesis/eval.tex:1125` · sec:eval-interpretation

**Claim (gloss).** D5's authority ordering and conflict outcome were never exercised, because transcript authority is uniform.

```tex
The authority ordering of \Dn{5} never discriminated, because every transcript carries the same authority, and for the same reason its conflict outcome was unreachable once a fact existed; the conflicts the runs recorded, between none and thirteen per autonomous repeat, are tied first claims that stayed open and surfaced as a caveat on twenty answers.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; `resolution_same_meeting_conflict`.
- **Confirms if:**
  - The run property holds in the state dumps (one authority level).
  - Trace sub-codes `outranked_dissent` and `tie_left_as_conflict` are about zero in A0/A1.
  - In A2, the reviewer ceiling bounds what resolving the open same-meeting conflicts could recover.
- **Overturns if:** A0/A1 rows lost at `tie_left_as_conflict` or `outranked_dissent` are material. Or Step 3 codes a state-rule case in which authority decided the outcome: a challenger made ineligible, or outranked, by a different authority level. The first confirm condition (one authority level) makes this event unlikely. A code on the uniform-authority clause (D5.p5, D5.p6) supports this row, as in C85.
- **Text action if confirmed:** keep.
- **Text action if overturned:** qualify with the counts.
- **Testable here:** partly.
- **Note:** 94c049d D5.p5 and D5.p6 already state that the AMI workflow assigns one authority.
- **Also stated at:** C31 (implementation_chapter.tex:338), C85, C91; section 5, group F.

#### C93 · `thesis/eval.tex:1130` (sec:eval-interpretation) and `thesis/conclusion.tex:117` (sec:conc-contributions) · merged

**Claim (gloss).** Neither the review boundary (D6) nor the gatekeeper (D2) caused losses in the autonomous arm; both were barely exercised. conclusion.tex:117: review's effect on corruption was not observed, because the autonomous gate accepted everything.

Quote at `thesis/eval.tex:1130`:

```tex
The review boundary of \Dn{6} was inert in the autonomous arm, whose structural gate accepted every value it did not leave pending, and the one policy that varied it used a model reviewer. The admission gate of \Dn{2} classified spans, but its evidence-only policy does not limit extraction.
```

Quote at `thesis/conclusion.tex:117`:

```tex
The review boundary is an implemented invariant whose effect on corruption was not observed, since the autonomous gate rejected nothing and the only policy contrast used a model reviewer (Section~\ref{subsec:eval-confirmation-policy}).
```

- **Where/why:** where and why.
- **Boundaries:** filing (`applied` step; value confirmation); extraction (`admitted` step, gatekeeper); key resolution and expansion; state rules.
- **Mechanisms:** `resolution_same_meeting_conflict`; none specific (review, admission).
- **Confirms if:**
  - No A0 rows are lost at `applied`; `admitted:ignored` is 4–5 rows per run.
  - The Step 2 reviewer ceiling on A2 is small: a perfect reviewer at the open same-meeting conflicts recovers little.
  - Few Step 3 routing cases are coded "the harness reviewer accepted a near-duplicate or over-broad key" (`_reviewer_would_accept`).
- **Overturns if:** any of these.
  - A1's settle losses (`applied:proposal_expired`, 4.0 per run) are coded as a review-boundary loss.
  - The reviewer ceiling recovers a large part of A2's `proposed:same_meeting_conflict` rows (36.7 per run): open conflicts cost many rows, so a reviewer would matter.
  - At least 3 distinct values are coded to the harness reviewer's acceptances. The automatic acceptance of concepts is then itself a locus of loss.
- **Text action if confirmed:** keep. Add the reviewer ceiling as "the most a perfect reviewer could recover, not an estimate of a reviewer".
- **Text action if overturned:**
  - eval.tex:1130: qualify: in A2 the absent reviewer leaves n rows open, and the ceiling bounds what review could recover.
  - conclusion.tex:117: add that the harness reviewer's acceptances are an implementation cause of X routing losses, and give the ceiling.
- **Testable here:** partly.
- **Note:**
  - The threats row at eval.tex:1264 says the same ("\Dn{5} and \Dn{6} were not tested in their intended roles, and \Dn{2} only partly").
  - conclusion.tex:404 (DR6 "remains untested in either half") is covered by this row too: the ceiling is not a human-review result.
  - Under the amendment, A2 cases left open by D5's "leaving unresolved cases reviewable" are coded "held: conflict decision".
- **Also stated at:** C51, C67; section 5, group H.

#### C94 · `thesis/eval.tex:1134` · sec:eval-interpretation

**Claim (gloss).** The losses bear on these design decisions, so the results test them.

```tex
The results therefore test record separation, epistemic status, concept construction, supersession, state-first reading, evidence linking, the extraction contract and templated rendering (\Dn{1}, \Dn{3}, \Dn{4}, \Dn{7}--\Dn{11}); they say little about authority-gated resolution or review.
```

- **Where/why:** why.
- **Boundaries:** all boundaries.
- **Mechanisms:** epistemic status; change and supersession; rejection (mapping section 1: D3.p3, D7.p4, D8.p4); evidence and provenance; complete decisions.
- **Confirms if:** the Step 3 bound rule gives definite verdicts (works or doesn't work, not "can't tell") for the mechanisms listed under Mechanisms, and the cases are grounded on 94c049d text, not in the retrospective-design column.
- **Overturns if:** the cases rest only on D10/D11, which are retrospective.
- **If the bounded verdict of a mechanism concerned is *can't tell (defect-limited)*:** a third outcome. Plan 23's principle applies: a result limited by a defect shows nothing.
  - Text action: report the recorded and the bounded verdicts (amendment:471), make no works or doesn't-work statement, and do not list the decisions mapped to that mechanism as tested.
  - This condition is decided by Rule M (mapping section 7a), drafted on 27 October 2026 for decision C43 on the decision sheet (mapping decision M-19).
- **If the bounded verdict of a mechanism concerned is *can't tell (within the instrument range)*:** neither confirm nor overturn. (Added in the review of the completion pass, 27 October.)
  - Text action: report the recorded and the bounded verdicts and IR, make no works or doesn't-work statement, and do not list the decisions mapped to that mechanism as tested by the RAG comparison.
  - This condition is also decided by Rule M (mapping section 7a, item 4).
- **Text action if confirmed:** keep, and list the decisions per verdict.
- **Text action if overturned:** rewrite: "the results test ... only where implementation defects do not limit them; D10 and D11 were written after the runs".
- **Testable here:** yes.

#### C95 · `thesis/eval.tex:1141` · sec:eval-interpretation

**Claim (gloss).** The incomplete answers are the cost of a design trade-off of the explicit state layer.

```tex
The evidence shows the principal design tension. An explicit state layer permits inspected values, lifecycle records and trace links, but those facilities do not deliver complete public answers.
```

- **Where/why:** why.
- **Boundaries:** all boundaries.
- **Mechanisms:** complete decisions; evidence and provenance.
- **Confirms if:** Step 3 codes the coverage losses as design trade-offs whose benefit the 94c049d text states, with the benefit measured where the trace can. Examples: D4.p4, "Parking preserves an interpretation without force-classifying it, but delays answer availability"; the D1 row of the design-rationale table, benefit "Inspectable commitments", cost "More workflow stages".
- **Overturns if:** the coverage losses are coded implementation defect or unclear, or the kappa's lower bound is below 0.40.
- **Text action if confirmed:** keep, and cite the trade-off codes.
- **Text action if overturned:** qualify: "in the evaluated implementation, those facilities did not deliver ...". Do not call it a design tension.
- **Testable here:** partly.

#### C96 · `thesis/eval.tex:1173` · subsec:eval-replay

**Claim (gloss).** Reading the admitted evidence answers at least as well as reading the state. This implies the information is kept in admitted evidence and lost after admission. The sentence disclaims isolating state storage.

```tex
The screened replay therefore shows no state-first advantage in either dump group; [...] Retrieval, context construction and generation also change together, so the contrast is a bundle of read operations under a disclosed approximation, not an isolated effect of state storage.
```

- **Where/why:** where.
- **Boundaries:** extraction; filing; state rules; reading.
- **Mechanisms:** none specific (read policy).
- **Confirms if:** the Step 5 ES2009 trace shows few losses at admission and most after it, as on EL2020 (`admitted:ignored` 4–5 of 133 rows).
- **Overturns if:** the Step 5 ES2009 trace shows many losses at admission (`admitted:ignored`, `span_not_seen`).
- **Text action if confirmed:** keep the hedge; optionally cite the trace.
- **Text action if overturned:** keep the hedge, and note that the evidence-only advantage is not about the path after admission.
- **Testable here:** partly.
- **Note:** the replay used cycle-1 dumps. Step 5 uses new runs.
- **Also stated at:** "Reading the same admitted evidence as text also scored higher than reading the state built from it under the screened replay" (conclusion.tex:318–320); section 5, group Z.

#### C97 · `thesis/eval.tex:1201` · subsec:eval-failure-cascade

**Claim (gloss).** On ES2009, half the missing occurrences are lost at or before extraction, and not only because of summary-phrased gold.

```tex
\paragraph{Acquisition.} For 134 occurrences (50.6\%) the matcher finds no representation at all, 19 reach an evidence match without a claim and 13 a claim without a fact. [...] so the absence is not confined to summary phrasing.
```

- **Where/why:** where and why.
- **Boundaries:** extraction (`admitted`, `carried`); evaluation (gold phrasing).
- **Mechanisms:** complete decisions.
- **Confirms if:** in the Step 5 ES2009 trace with the adapter, most rows are first lost at `admitted` or `carried`, including transcript-line and decision-annotation rows (the source is recorded per row). 3b codes few evaluation defects on summary-only rows.
- **Overturns if:** the extraction losses concentrate in summary-only rows (27 of 87), and 3b codes them as evaluation defects (gold phrasing).
- **Text action if confirmed:** replace the lexical counts (final dumps, 0.6 overlap) with Step 5 trace counts, or label both.
- **Text action if overturned:** rewrite: the absence is mostly gold phrasing, an evaluation cause.
- **Testable here:** yes.
- **Note:** Step 5 runs are new runs under the B3 gold, so this is a consistency check on cycle 1. eval.tex:1223 is covered under C67.
- **Also stated at:** C115 (conclusion.tex:196); section 5, group T.

#### C98 · `thesis/eval.tex:1210` · subsec:eval-failure-cascade

**Claim (gloss).** D5's equal-time allowance lets a reworded reading of the same evidence displace a stored value.

```tex
Sharing a span does not make a replacement wrong, but the resolver permits replacement at equal authority and equal source time (\Dn{5}), so a differently worded interpretation of the same evidence can displace an existing value without a later source.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`.
- **Confirms if:**
  - The `bug3_replaced_in_own_meeting` flags of A0 vanish in A1 (plan 23 table: 97 facts on ES2009, 147 on EL2020). A0 rows resting on bug 3 count as repaired (Phase B).
  - Step 5 ES2009, A0 against A1-ref, shows the same.
  - The `supersession_requires_new_evidence` leave-one-out in A2 measures the alternative.
- **Overturns if:** A1 (bug 3 repaired) still shows same-meeting or same-evidence replacements at a similar rate, so the cause lies elsewhere.
- **Text action if confirmed:** rewrite: "the evaluated resolver let a same-meeting rival supersede the current value (bug 3), repaired in A1". Cite D5.p3 and D5.p5 at 94c049d as the documented rule. Add that bug 4 inflates the counts (25/20/21 self-supersessions in r1–r3).
- **Text action if overturned:** keep the D5 wording, and cite D5.p3 and D5.p5.
- **Testable here:** yes.
- **Note:** 94c049d D5.p3 makes a challenger eligible with "a source time no earlier than the fact's validity start", which admits equal time. D5.p5 records the missing tie check. Whether bug 3 is design or defect is decision R-4. Whether D5.p3's equal-time eligibility belongs in R-4's list at all is decision R-22.
- **Also stated at:** C17 (background.tex:272), C120 (conclusion.tex:221); "Whether that condition operated in each replacement is not recorded in the trace" (conclusion.tex:223–224), see C120's note; C98a (eval.tex:1213), the share this paragraph goes on to state; section 5, group E.

#### C98a · `thesis/eval.tex:1213` · subsec:eval-failure-cascade

Added in the review of 27 October.

**Claim (gloss).** On ES2009, at most 37 of 265 missing occurrences (14.0%) are directly implicated in supersession.

```tex
The 37 occurrences whose only match is superseded bound the directly implicated group at 37/265 (14.0\%); this is an investigation set, not a predicted gain from a stricter rule.
```

- **Where/why:** where.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession.
- **Confirms if:** in the Step 5 ES2009 trace (A0), the share of rows of the cascade's families (current state, change and rejection) first lost at state maintenance (`current:overwritten_by_non_gold_value`, `current:displaced_by_other_gold_value`) is of that order and does not materially exceed it.
- **Overturns if:** that share is materially larger in the Step 5 A0 trace.
- **Text action if confirmed:** keep, labelled final-dump lexical, and add the trace count.
- **Text action if overturned:** replace the share with the trace count.
- **Testable here:** partly (Step 5 only; decision R-13).
- **Note:**
  - The section disclaims a causal reading of its categories: "The categories describe where the matcher finds a representation, not causal stages" (eval.tex:1192–1193). The share is still registered, as the acquisition share (C97) and the read-selection share (C99) are.
  - Whether the group rests on bugs 3 and 4 is C98's and C100's test, not this row's.
  - The cascade table repeats the count: "Only superseded fact matches & 37 & 14.0\%" (generated/eval_cascade.tex:15).
- **Also stated at:** C98 (eval.tex:1210). In Ch. 6: "the 37 occurrences whose only match is superseded are candidates for examination" (conclusion.tex:224–225); "The 37 superseded-only and 62 unresolved-or-unexposed diagnostic occurrences" (conclusion.tex:377–378), shared with C99. Section 5, group E.

#### C99 · `thesis/eval.tex:1218` · subsec:eval-failure-cascade

**Claim (gloss).** About a fifth of the ES2009 missing occurrences are stored but lost at reading, and the existing widening and change filter did not help.

```tex
\paragraph{Read selection.} Forty-seven occurrences match live facts under keys not resolved for the answer and fifteen more match facts under resolved keys yet remain flagged. The implementation already contains family-sibling widening and the latest-meeting change filter; their existence did not produce complete cross-concept lists or a checkpoint delta.
```

- **Where/why:** where.
- **Boundaries:** reading.
- **Mechanisms:** change and supersession; complete decisions.
- **Confirms if:** the Step 5 ES2009 trace shows stored values lost at `key_reached` (the trace reaches reading for only 10 ES2009 rows). The EL2020 offline reading check and probe (iii) test the mechanism.
- **Overturns if:** Step 5 shows these values were not stored with the right status at k (a final-dump artefact). Or A1-ref (bug-2 repair) produces the checkpoint delta.
- **Text action if confirmed:** keep, labelled final-dump lexical.
- **Text action if overturned:** rewrite: lost before reading; or the change filter's misses rested on bug 2.
- **Testable here:** partly.
- **Note:** the change filter saw only a fraction of new values because of bug 2 (22-bug-list.md:36).
- **Also stated at:** "The 37 superseded-only and 62 unresolved-or-unexposed diagnostic occurrences of Section~\ref{subsec:eval-failure-cascade} identify different investigation sets, not additive recoverable accuracy." (conclusion.tex:377–379), shared with C98a; C133a (conclusion.tex:366) on the existing widening and latest-meeting filter.

#### C100 · `thesis/eval.tex:1229` · subsec:eval-failure-cascade

**Claim (gloss).** The remedies for these losses are design changes, which implies design causes.

```tex
The production artifact was fixed before evaluation and was not modified after these observations; proposed changes to supersession, aggregation and change reconstruction are future design work.
```

- **Where/why:** why.
- **Boundaries:** state rules; reading.
- **Mechanisms:** change and supersession; complete decisions.
- **Confirms if:** Step 3 codes the supersession, aggregation and change cases architectural or trade-off on 94c049d text.
- **Overturns if:** these cases are coded implementation: bugs 3 and 4 (supersession) and bug 2 (change reconstruction), already repaired in Phase B, or probe-recovered.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite: "part of these losses rested on defects repaired since (bugs 2–4); the rest ...".
- **Testable here:** partly.
- **Note:** "not modified" still holds for the evaluated artifact. The repairs are default-off switches.

#### C101 · `thesis/eval.tex:1263` · tab:eval-threats

**Claim (gloss).** The EL2020 construct (strict, compound gold) is one cause of losses in both arms, but not of the gap's direction.

```tex
Transcript-grounded, often compound gold judged strictly favours a system that re-reads the transcript and penalises one-clause answers in both arms (23 RAG and 8 autonomous wrong answers cover every required value, about 7 and 2.5 points); [...] & The bound is reported and does not change the direction
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** complete decisions.
- **Confirms if:** Step 3 codes few EL2020 PM losses as evaluation defects, and the pass examination finds few. V4's audit agreement is at least 0.80, so the trace's compound-value standard holds.
- **Overturns if:** many PM losses are coded evaluation defects (gold or adjudication wrong). Or the audit agreement is below 0.80, and v2 moves rows away from extraction.
- **Text action if confirmed:** keep.
- **Text action if overturned:** qualify the size of the effect, and report the evaluation-defect count.
- **Testable here:** partly.
- **Note:** the trace's adjudication standard (one part of a compound value does not carry it) is stricter than the gold aliases (23-loss-trace-results.md, Limits).
- **Also stated at:** C90, C129 (conclusion.tex:326).

### 4.7 Chapter 6 (`thesis/conclusion.tex`)

Rows for conclusion.tex:92, :117, :204, :226, :229, :232, :252 and :256 are merged into C05, C93, C81, C85, C83, C84, C87 and C88.

#### C102 · `thesis/conclusion.tex:15` · sec:conc-answers

**Claim (gloss).** The records keep how each interpretation became state, so the path from claim to fact is preserved.

```tex
ProjectMemory demonstrates that an initially empty system can construct an explicit project-state representation from meeting evidence, record how its interpretations become accepted state, and expose values, statuses and supporting links through a public answer contract.
```

- **Where/why:** where.
- **Boundaries:** state rules.
- **Mechanisms:** evidence and provenance.
- **Confirms if:** the Step 2 identity gates pass: proposals (key, value, type, final status, phase) and facts with supersession links are rebuilt from the recorded claims and key timeline.
- **Overturns if:** the identity gates fail on the recorded keys, or the rebuilt lineage differs from the recorded one. Bug 2's copying of the oldest claim's evidence already means that, in A0, the recorded link is not the winning claim's.
- **Text action if confirmed:** keep, qualified by bug 2 for A0 (P0-E).
- **Text action if overturned:** qualify "record how its interpretations become accepted state": the records keep the transitions but not, in the evaluated runs, the claim that supplied each value.
- **Testable here:** partly.
- **Note:** P0-E lists conclusion.tex:15–17.
- **Also stated at:** C05 (main.tex:81, conclusion.tex:92); section 5, group B.

#### C103 · `thesis/conclusion.tex:34` · sec:conc-answers (RQ1)

**Claim (gloss).** Some stored values are lost at reading, because the payload holds only what the read path selected.

```tex
The public payload represents the read path's selection rather than all stored knowledge.
```

- **Where/why:** where.
- **Boundaries:** reading.
- **Mechanisms:** none (reading; no Phase D3 mechanism).
- **Confirms if:** in the loss-trace reading rows, a large share of asked rows stored with the right status fail at `key_reached` or `in_payload`, and Step 3 sets caused-at at reading for those cases. Already read: 39–47%; `key_reached` 6.7 (A0), 7.3 (A1) and 3.7 (A2) rows per run.
- **Overturns if:** Step 3 and the offline reading check put caused-at upstream for most `key_reached` cases: the value sits under a key about another matter (routing, R). The payload then reflects mis-stored knowledge more than selection.
- **Text action if confirmed:** keep, and add the loss-trace reading share.
- **Text action if overturned:** qualify: "the payload omits stored values mostly because they are stored under keys about other matters".
- **Testable here:** yes.
- **Note:** Already read: in A0 r1, about half of the `key_reached` rows hold the value under a key unrelated to the question's topic (23-loss-trace-results.md).

#### C104 · `thesis/conclusion.tex:42` · sec:conc-answers (RQ2)

**Claim (gloss).** Change information is kept in state and lost at reading.

```tex
The system records lifecycle transitions but does not expose them as correct answers (\Hy{2}, \Hy{3}): every ProjectMemory policy and RAG score 0/15 on change and 0/20 on rejection.
```

- **Where/why:** where.
- **Boundaries:** state rules; reading.
- **Mechanisms:** change and supersession; rejection.
- **Confirms if:** in the loss trace, most demoted and ruled-out rows are stored with the right status at k and first lost at `key_reached`, `in_payload` or `answered`.
- **Overturns if:** most demoted rows are never stored. Already read: about 6 of 9 demoted values per run were never stored, and of the stored ones 1.0 of 3.3 is still current in A0. The transitions were then mostly not recorded, and the loss is at extraction or filing, not at reading.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite: "most changed values never reached state, so no transition was recorded; of those that did, ...". Give the loss-trace boundary shares.
- **Testable here:** yes.
- **Note:**
  - The frozen loss trace, read before signing, already points to overturn on EL2020.
  - Bug 1 (a negation of the current value never takes effect) and bug 4 (self-supersession) affect what A0 records.
  - Plan 23 notes that change answers fail first at question-to-key resolution.
  - The ES2009 figures come from cycle 1, and Step 5's trace reaches reading for only 10 ES2009 rows.
- **Also stated at:** C01, C61; section 5, group J.

#### C105 · `thesis/conclusion.tex:47` · sec:conc-answers (RQ2)

**Claim (gloss).** Rejected options are lost either at reading (wrong key) or because no claim was formed.

```tex
Several of the rejected values exist as rejected facts in the autonomous state under keys the reader did not reach, and others never became claims (Section~\ref{subsec:eval-transfer}, mechanism~\ref{mech:reading}).
```

- **Where/why:** where.
- **Boundaries:** extraction; reading.
- **Mechanisms:** rejection; epistemic status.
- **Confirms if:** in the loss trace, the ruled-out rows lost at extraction are mostly `admitted:ignored` or `carried:no_claims_from_cited_span` (they never became claims), and the rest are stored as rejected and lost at `key_reached`.
- **Overturns if:** the ruled-out rows lost at extraction are mostly `polarity:carried_only_positive`. Already read: 6.0, 5.7 and 6.0 of the 9.3, 8.7 and 8.7 extraction-lost rows (of 16) in A0, A1 and A2. The option did become a claim, but as a positive mention, not as its rejection. E+R\* and the Step 3 codes then set the cause: the candidate "a modality or negation instruction missing from the prompt", or conversational difficulty.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite "others never became claims" as "most were extracted only as positive mentions, not as their rejection". Add the Step 3 cause.
- **Testable here:** yes.
- **Note:** already pointed to by the frozen trace. The Ch. 5 counts behind mechanism~\ref{mech:reading} come from the bug-11 coder. Bug 7 changes the focused rejection counts (6/24 against 17/24, corrected).
- **Also stated at:** section 5, group J.

#### C106 · `thesis/conclusion.tex:59` · sec:conc-answers (RQ3)

**Claim (gloss).** Restraint comes from the embedding candidate generator, not from maintained state.

```tex
The ablation attributes the noise result to one component. With the resolver's embedding candidates switched off, 11 to 13 of 24 incidental questions receive an unrelated confirmed fact instead of a decline (Table~\ref{tab:eval-ablation-paired}). Restraint on incidental questions is therefore a property of the evaluated configuration's embedding candidate generator, not of maintaining state, and the comparator shows it too.
```

- **Where/why:** why.
- **Boundaries:** key resolution and expansion; reading.
- **Mechanisms:** none (restraint on incidental talk is removed from Phase D3 by Step 0).
- **Confirms if:** not tested by this study. There is no restraint arm or per-component switch, and the noise items forbid nothing.
- **Overturns if:** not tested by this study.
- **Text action if confirmed:** n/a. Independently, rewrite under P0-A and P0-B: the switch turned off three callers (resolver, answer-time value retrieval, relevance gate), and the counts are 10 of 13 and 9 of 11.
- **Text action if overturned:** n/a.
- **Testable here:** no.
- **Note:** bug 8 is not repaired; the restraint claim was dropped from the verdict list on 22 October.
- **Also stated at:** section 5, group C.

#### C107 · `thesis/conclusion.tex:145` · sec:conc-contributions

**Claim (gloss).** ProjectMemory's losses are consistent with loss through representation: content is lost when it is replaced by extracted facts.

```tex
Together they locate specific obstacles between source evidence and useful answers. The information-loss concern is consistent with LongMemEval's finding that replacing conversation content with extracted facts or summaries can impair question answering, with an exception for its multi-session reasoning tasks \citep{wu2025longmemeval}.
```

- **Where/why:** where.
- **Boundaries:** extraction.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** E+R against R shows that under perfect routing a large extraction share remains in A1: most of the roughly 44 extraction-lost rows per run are not recovered by R and are recovered by E+R. The joint table shows that RAG answered many of them. Already read: 75 of 119 single-value extraction-lost rows.
- **Overturns if:** probes (b)/(b2)/(c) recover most extraction cases, or WD works, so the loss is an implementation choice in how claims are extracted, not compression as such. Or V4's audit is below 0.80 and v2 moves many "does not carry" rows out of extraction.
- **Text action if confirmed:** keep. It is already hedged: "consistent with", "neither estimates [...] nor proves".
- **Text action if overturned:** qualify: the loss sits at extraction but was largely recoverable by a different extraction prompt or contract. LongMemEval stays as context only.
- **Testable here:** partly.
- **Note:** the sentence already disclaims causation.
- **Also stated at:** C16 (background.tex:155).

#### C108 · `thesis/conclusion.tex:159` · sec:conc-implications

**Claim (gloss).** Write-time normalisation, a design property, causes answerability losses at extraction, filing and reading. The records show where.

```tex
The evidence of Chapter~\ref{chap:evaluation} supports one central proposition: \emph{write-time normalisation makes the formation of project state inspectable, but it reduces answerability wherever extraction, filing or reading loses information that the source still holds.} A value must become a claim, keep its meaning through filing and lifecycle updates, remain reachable under the generated concepts and be selected for the question; a loss at an earlier boundary survives every later step, and the final score alone cannot say where the chain broke. The retained records can.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession; evidence and provenance.
- **Confirms if:**
  - The first-loss tables show losses at every boundary (Already read).
  - Step 3 codes most A1 cases architectural or trade-off on 94c049d text, with the kappa's lower bound at least 0.40.
  - "The source still holds" is supported by the joint table: RAG credits most of the lost values.
  - The identity gates pass.
- **Overturns if:** Step 3 codes most A1 cases implementation defect or unclear, so the proposition holds only for the evaluated implementation. Separately, Already read: the list leaves out state maintenance, which loses 22–24 rows per A0/A1 run.
- **Text action if confirmed:** keep. Add "state maintenance" to the list of boundaries, and cite the coded shares and the kappa.
- **Text action if overturned:** rewrite: "in the evaluated implementation, extraction, filing, state maintenance and reading lose information the source still holds; X% of coded losses are implementation defects". Drop it as a general design proposition.
- **Testable here:** yes.
- **Note:** "A loss at an earlier boundary survives every later step" is true by construction for the loss trace's first-loss unit, and is not tested.
- **Also stated at:** C04, C135; section 5, group A.

#### C109 · `thesis/conclusion.tex:168` · sec:conc-implications

**Claim (gloss).** Each observed loss is explained by a named design decision.

```tex
Table~\ref{tab:conc-principles} condenses what they show into five design principles, each pairing an observation with the decision whose behaviour explains it and the contract of Section~\ref{sec:conc-future} that would test it. No contract has been implemented, so the principles are diagnosed requirements for the next design cycle rather than established results.
```

- **Where/why:** why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** complete decisions; change and supersession; evidence and provenance.
- **Confirms if:** for each principle, Step 3 codes the cases behind its observation architectural or trade-off, quoting the named decision as worded at 94c049d. Only D1–D9 qualify. The A2 leave-one-out and WD give the contract results.
- **Overturns if:** the named decision is retrospective: D10 and D11 cannot ground architecture under the retrospective-design rule. Or the cases are coded implementation or unclear.
- **Text action if confirmed:** keep "explains" row by row, with the code share and the 94c049d paragraph.
- **Text action if overturned:** replace "the decision whose behaviour explains it" with "the decision it bears on". Mark D10 and D11 as retrospective.
- **Testable here:** yes.
- **Note:**
  - P0-D asks for D10 and D11 to be marked retrospective whatever the outcome.
  - "No contract has been implemented" is out of date: `cycle2_flags.BUILT` at 3320375 holds seven contracts, and four ran as A2 on EL2020. That is a factual fix, not an outcome (decision R-16).

#### C110 · `thesis/conclusion.tex:185` · tab:conc-principles

**Claim (gloss).** The extraction loss comes from D10, the absence of a whole-decision obligation. It is untested.

```tex
1. Keep a stated decision whole when extracting it & On EL2020, in 94 of 178 wrong answers the admitted span yielded claims that did not carry the decision & \Dn{10} & Extraction and filing & Diagnosed; untested\\
```

- **Where/why:** where and why.
- **Boundaries:** extraction.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** WD works under the Step 2c rule, and (iv) holds for most `carried:claims_without_the_value` cases. Those cases are then coded implementation choice, repaired if WD is admitted. The Step 2c rule:
  - every WD run has fewer `carried` losses than every fresh A1 run;
  - the mean is lower by more than 9 rows and 5 distinct values;
  - filing losses rise by no more than 13 rows;
  - "no owner or role claim is lost;" (amendment:293). On EL2020 the term is defined in the probe note (`23-am1-probe-note.md`), under its heading "Owner or role claim on EL2020 (C41, M-17)"; see mapping decision M-17;
  - there is no new incidence.
- **Overturns if:**
  - WD is "not shown".
  - Or the fresh A1 runs carry the values in 2–3 of 3 runs (sampling instability).
  - Or (b)/(b2) recover the cases (registry-conditioned extraction or out-of-domain examples, not the whole-decision contract).
  - If WD and fresh A1 both carry a value in at most 1 of 3, with WD in 0, architectural weakness can be argued only from D4.p5's scalar passage.
- **Text action if confirmed:** status becomes "tested on EL2020 development; WD works (bounded)". Decision column: the evaluated extraction prompt (implementation), with D10 marked retrospective.
- **Text action if overturned:** status becomes "tested; not shown". Replace D10 with the coded cause, or with D4 (94c049d D4.p5) if the WD-cases rule allows the argument.
- **Testable here:** yes.
- **Note:** the 94/178 count comes from the bug-11 coder (P0-C). Replace it with the loss-trace count (`carried:claims_without_the_value`, 28.3/26.3 rows per A0/A1 run). If Step 2c is not run, these cases are coded unclear and the row stays untested. Decision R-20 applies.
- **Also stated at:** section 5, group D.

#### C111 · `thesis/conclusion.tex:186` · tab:conc-principles

**Claim (gloss).** Filing and supersession losses come from the absence of checks against the key (type), the rivals and the evidence (D5, D7, D9, D10).

```tex
2. Check a value against its key, its rivals and its evidence before it becomes a fact & 37 claims carrying the value never became facts; verified values were replaced by unrelated ones in 35 of 51 supersessions of one repeat; 16.0\% (machine) or 14.4\% (author) of evidence links fully support their fact & \Dn{5}, \Dn{7}, \Dn{9}, \Dn{10} & Extraction and filing; supersession & Diagnosed; untested\\
```

- **Where/why:** where and why.
- **Boundaries:** key assignment at extraction; key resolution and expansion; state rules.
- **Mechanisms:** `filing_type_check`; `resolution_same_meeting_conflict`; `supersession_requires_new_evidence`; `filing_support_check`; change and supersession; evidence and provenance.
- **Confirms if:**
  - The A2 leave-one-out shows each contract "works": at least 3 distinct values net in every gate-passing run, no run net negative, and no rise in parked or conflict rows among values that A1 stores.
  - R shows that the `current:overwritten_by_non_gold_value` rows are routing, which fits a check against the key.
- **Overturns if:** the leave-one-out gives "doesn't work". Already read: A2 scores below A0, and its filing losses rose by 36–40 rows per run, mostly unresolved same-meeting conflicts and parked claims.
- **If the bounded verdict is *can't tell (defect-limited)*:** a third outcome, per contract. Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement. Proposed status: "tested on EL2020 development; can't tell (defect-limited)". While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** status becomes "tested on EL2020 development: contract X works (bounded)".
- **Text action if overturned:** status becomes "tested; the contracts as built did not work: losses moved from state maintenance to filing". Name the decision the codes support: D4 (key reuse, D4.p4 at 94c049d) rather than D5/D7 if R recovers the overwrites.
- **Testable here:** yes.
- **Note:** the 37 and the 35 of 51 come from the bug-11 coder (P0-C). The 16.0%/14.4% figures concern evidence links, which no step here measures (see C02). D10 is retrospective.
- **Also stated at:** C02, C83, C84; section 5, groups E and I.

#### C112 · `thesis/conclusion.tex:187` · tab:conc-principles

**Claim (gloss).** List and change answers fail at reading or aggregation, because of the open schema (D4) and the read path (D8). About half of all questions resolve the wrong key.

```tex
3. Assemble broad answers across concepts deliberately & Current-state lists 4/40 and every change list wrong on both series; wrong-key resolution on about half of all questions & \Dn{4}, \Dn{8} & Aggregation and change & Diagnosed; untested\\
```

- **Where/why:** where and why.
- **Boundaries:** reading; key resolution and expansion.
- **Mechanisms:** change and supersession.
- **Confirms if:** Step 2's offline reading analysis and probe (iii) (A1 and A2 rows only) place the `key_reached` losses at question-time ranking under D8 (D8.p4 at 94c049d: "Its cost is restricted answerability"). In ES2009 Step 5, A1-ref and the final configuration still fail the lists (Step 5 scores). Where the list failures arise is not testable here: list questions are not cases, and 3b codes the final configuration's r1 cases, not list answers.
- **Overturns if:**
  - The "about half" figure is the bug-9 diagnosis, true by construction in cold-start runs. The loss trace puts `key_reached` at 6.7–7.3 of 133 current rows per A0/A1 run.
  - (iii) recovers cases where the shortlist excluded the holding key (an implementation parameter).
  - A1-ref answers change lists (bug 2 affected the change template).
- **Text action if confirmed:** keep the principle. Replace the count with loss-trace shares. Decision column: follow C109's rule. Keep "\Dn{4}, \Dn{8}" only where Step 3 codes the cases behind the observation architectural or trade-off on the named decision as worded at 94c049d, with the kappa's lower bound at or above 0.40. For design-or-model-not-separated cases, or cases with no class, the column names the decision the observation bears on, not one that explains it (C109's overturned action).
- **Text action if overturned:** drop "wrong-key resolution on about half of all questions" (P0-C). Attribute to the shortlist parameter or to bug 2, as coded.
- **Testable here:** partly.
- **Note:** list questions fall outside the loss trace's per-value row unit. ES2009's trace reaches reading for only 10 rows. The wrong-key clause is already decided (C88, section 6.2).
- **Also stated at:** C88; section 5, group G.

#### C113 · `thesis/conclusion.tex:188` · tab:conc-principles

**Claim (gloss).** Values are lost at reading because the reader never consults the admitted evidence (D8, D11).

```tex
4. Keep source evidence reachable when the state cannot answer & 27 live facts sat under keys the reader did not pick; RAG's cited chunk held the gold line in 120 of 124 contrasting answers & \Dn{8}, \Dn{11} & Read & Diagnosed; the replay gives indirect support\\
```

- **Where/why:** where and why.
- **Boundaries:** reading.
- **Mechanisms:** none (reading). The read contracts `answer_evidence_fallback` and `answer_answerability_check` are built but are in no arm of this study.
- **Confirms if:** the Step 3 joint table (first-loss step against RAG's outcome) shows many RAG-credited values lost by the autonomous arm after admission, at reading in particular. The offline reading check shows the holding key was in the prompt but out-ranked.
- **Overturns if:**
  - The joint table puts the RAG-credited losses mostly at extraction or filing. The principle may still hold, since a fallback reads any admitted span, but the observation then does not support "Read" as the locus.
  - Or (iii) recovers the `key_reached` cases: the cause is the shortlist, not the absence of a fallback.
- **Text action if confirmed:** keep. Replace the counts with loss-trace and joint-table counts. Decision column: follow C109's rule.
  - Keep D8 only where Step 3 codes the cases behind the observation architectural or trade-off on D8.p3–p4 as worded at 94c049d, with the kappa's lower bound at or above 0.40.
  - For design-or-model-not-separated cases, or cases with no class: location only; the column names the decision the observation bears on, not one that explains it.
  - In both branches, mark D11 as retrospective.
- **Text action if overturned:** reword the observation to the coded locus, and mark D11 as retrospective.
- **Testable here:** partly.
- **Note:** the 27 and the 120/124 come from the bug-11 coder (P0-C). D11 entered at 5de9911; the 94c049d basis is D8.p3–p4.
- **Also stated at:** C40, C87; section 5, group G.

#### C114 · `thesis/conclusion.tex:189` · tab:conc-principles

**Claim (gloss).** Restraint is a by-product of the embedding candidates (D4, D8).

```tex
5. Make restraint a declared outcome, not a by-product & Without embedding candidates, correct noise answers fall from 24/24 to 11/24; on EL2020, 8 of 30 unknown answers asserted unrelated facts & \Dn{4}, \Dn{8} & Read & Component measured by the ablation; contract untested\\
```

- **Where/why:** why.
- **Boundaries:** key resolution and expansion; reading.
- **Mechanisms:** none (restraint on incidental talk is removed from Phase D3 by Step 0).
- **Confirms if:** not tested by this study.
- **Overturns if:** not tested by this study.
- **Text action if confirmed:** n/a. Independently, P0-A applies.
- **Text action if overturned:** n/a.
- **Testable here:** no.
- **Note:** bug 8: "Component measured by the ablation" is not supported, because the switch reached three callers.
- **Also stated at:** section 5, group C.

#### C115 · `thesis/conclusion.tex:196` · par:conc-acquisition

**Claim (gloss).** On ES2009 about half of the missing values were lost before any representation formed, at admission or extraction.

```tex
On the development series, 134 of the 265 gold-phrase occurrences flagged as missing have no lexical match anywhere in the final dumps (Table~\ref{tab:eval-failure-cascade}): later resolution cannot select a representation that was never formed.
```

- **Where/why:** where.
- **Boundaries:** admission; extraction.
- **Mechanisms:** complete decisions; epistemic status.
- **Confirms if:** the Step 5 ES2009 loss trace (adapter), for A0 and A1-ref, puts the first loss at `admitted`, `carried`, polarity or modality for about half of the lost rows.
- **Overturns if:** ES2009's first losses fall mostly at filing or state maintenance, or the adapter's summlink provenance finds most of the "no match" values carried by paraphrase.
- **Text action if confirmed:** keep. Replace the lexical count with the ES2009 loss-trace shares.
- **Text action if overturned:** rewrite with the ES2009 boundary shares.
- **Testable here:** partly.
- **Note:** ES2009 is the weaker series: 87 rows, 27 of them summary-only, and no oracle ceiling.
- **Also stated at:** C97 (eval.tex:1201); section 5, group T.

#### C116 · `thesis/conclusion.tex:199` · par:conc-acquisition

**Claim (gloss).** Part of the ES2009 loss is an evaluation effect, because the gold is phrased from summaries.

```tex
Part of that loss belongs to the benchmark, since most gold entries are phrased from AMI's abstractive summaries and every arm scores lower on them (Table~\ref{tab:eval-extension-grounding}).
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** none.
- **Confirms if:** 3b codes a material share of ES2009 losses on the summary-only rows (27 of 87) as evaluation defect. The B3 decisions (Step 1) change these items' scores.
- **Overturns if:** 3b codes few evaluation defects on summary-only rows, coding them instead at extraction or filing under other classes.
- **Text action if confirmed:** keep, and cite the 3b evaluation-defect share.
- **Text action if overturned:** remove the sentence, or narrow it to the coded share.
- **Testable here:** partly.
- **Note:** under the amendment, evaluation defects change no gold or score within the study; corrections go through B3.

#### C117 · `thesis/conclusion.tex:202` · par:conc-acquisition

**Claim (gloss).** The ES2009 acquisition difficulty is shared with RAG, so it is not specific to this system.

```tex
But the difficulty applies to every architecture that read these transcripts, and handling it at write time was the design's own claim.
```

- **Where/why:** why.
- **Boundaries:** extraction; evaluation.
- **Mechanisms:** none.
- **Confirms if:** in the ES2009 joint table (Step 5 runs), RAG also misses most of the values that the autonomous arm loses at extraction.
- **Overturns if:** RAG credits most of them. The recoverability rule then bars the conversational-difficulty code for those values.
- **Text action if confirmed:** keep, and cite the joint table.
- **Text action if overturned:** rewrite: "the difficulty did not stop RAG on X of Y values".
- **Testable here:** partly.

#### C118 · `thesis/conclusion.tex:211` · par:conc-acquisition

**Claim (gloss).** The extraction losses come from the extraction contract (scalar claims, no whole-decision obligation), not from vague conversation.

```tex
Conversational vagueness cannot explain these losses; the extraction contract of \Dn{10} can, because it asks for scalar claims under generated concepts and places no obligation on keeping a stated decision whole.
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** all of these.
  - Step 3 codes few A1 extraction cases as conversational difficulty. Under the recoverability rule, 75 of 119 single-value extraction-lost rows already had a credited RAG answer.
  - WD works (Step 2c), and (iv) holds for most `carried:claims_without_the_value` cases.
  - Probes (b) and (b2) are not recovered.
- **Overturns if:** any of these.
  - (b) or (b2) recover many cases (registry-conditioned extraction or AMI examples, not the scalar contract).
  - Only (d) recovers (model-limited).
  - WD is "not shown", and fresh A1 carries the values in 2–3 of 3 runs.
  - Many cases are coded conversational difficulty.
- **Text action if confirmed:** rewrite the second clause: "the evaluated extraction prompt can, because it places no obligation on keeping a stated decision whole; a whole-decision contract recovered X". Mark D10 as retrospective. Keep the first clause only with the Step 3 share of conversational difficulty.
- **Text action if overturned:** remove both clauses. State the coded causes and shares: registry-conditioned extraction, examples, model-limited, unclear.
- **Testable here:** yes.
- **Note:**
  - P0-C removes the first clause whatever the outcome.
  - D10 entered at 5de9911 (19 October). Under the retrospective-design rule it cannot ground architectural weakness. The 94c049d candidate is D4.p5: "The September defaults favour scalar concept generation" (23-am1-design-text-94c049d.md, D4.p5).
  - Decision R-20 applies.
- **Also stated at:** C77 (vagueness clause), C82; section 5, group D.

#### C119 · `thesis/conclusion.tex:217` · par:conc-lifecycle

**Claim (gloss).** Values were replaced with no new evidence: a loss in the state rules.

```tex
In one autonomous run an ownership concept successively held ``Project Manager'', ``Finance'' and ``Sarah'', all three facts citing the same evidence span and each replacing its predecessor: three competing values attached to one cited passage with no new evidence between them.
```

- **Where/why:** where.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; evidence and provenance; `supersession_requires_new_evidence`.
- **Confirms if:** in the ES2009 Step 5 runs (A1-ref, bug 2 repaired), replacements still cite one span with no new evidence.
- **Overturns if:** already contradicted by the disproof review (P0-E). The shared span is bug 2's copying of the oldest claim's evidence; new evidence did arrive, as `valid_from` shows.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite per P0-E: the three facts share a span because each proposal copied the oldest claim's evidence (bug 2). New evidence did arrive.
- **Testable here:** partly.
- **Note:** the specific run is from cycle 1. The correction is a conformance fact that this study's outcomes do not decide (section 6.2; decision R-3).
- **Also stated at:** section 5, group I.

#### C120 · `thesis/conclusion.tex:221` · par:conc-lifecycle

**Claim (gloss).** D5's eligibility rule, a design element, lets a value from the same evidence replace the current one.

```tex
The rule of \Dn{5} admits a challenger of equal authority and equal source time, which permits a later value drawn from the same evidence to replace the current one.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`; `resolution_same_meeting_conflict`.
- **Confirms if:** Step 3 codes the A1 state-rule cases (`current:overwritten_by_non_gold_value` rows not recovered by R or E+R\*) as architectural weakness, quoting D5.p3 at 94c049d ("a source time no earlier than the fact's validity start"). The A2 leave-one-out shows that `supersession_requires_new_evidence` works.
- **Overturns if:**
  - R recovers most overwrite rows: the cause is routing, a rival of another matter on the key.
  - Or the A0 cases are coded conformance, repaired in A1: bug 3 (the current value's own claims did not compete) or bug 6 (no meeting dates).
  - Or `supersession_requires_new_evidence` does not work.
- **If the bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome for the contract clause. Text action: report the recorded and the bounded verdicts (amendment:471), and make no works or doesn't-work statement about the contract. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** keep. Quote D5.p3 (94c049d), and cite the code share and the leave-one-out.
- **Text action if overturned:** rewrite: the replacements came from claims of other matters filed under the key (routing), or from bugs 3 and 6, which contradict D5. They did not come from D5's rule.
- **Testable here:** yes.
- **Note:**
  - Already read: A0 and A1 overwrite rows are level (19.7 against 19.0), so the bug-3 and bug-6 repairs did not change them. That points away from those defects, towards routing or the rule itself. Decision R-4 applies.
  - This row's only route to confirmation quotes D5.p3. Decision R-22 asks whether D5.p3's equal-time eligibility stays a design entry; under R-22(b) together with R-4(b), this route closes.
  - The next sentence says: "Whether that condition operated in each replacement is not recorded in the trace" (conclusion.tex:223–224). It refers to the cycle-1 trace. The v3.1 loss trace's state-rule sub-codes are what Step 3 tests. Group B's claim that the records allow the losses to be traced is tested against this sentence too (section 5).
- **Also stated at:** C17, C98; conclusion.tex:223–224 (above); section 5, groups B and E.

#### C121 · `thesis/conclusion.tex:235` · par:conc-lifecycle

**Claim (gloss).** Wrong current values come from the implemented rule acting on reused keys. The history is intact.

```tex
The history \Dn{7} preserves is intact and made the diagnosis possible, but the current value the read path exposes is wrong. Under uniform authority the implemented rule makes the current value of a reused key whatever was said last about anything filed there.
```

- **Where/why:** why.
- **Boundaries:** key assignment at extraction; key resolution and expansion; state rules.
- **Mechanisms:** change and supersession; `supersession_requires_new_evidence`; `filing_type_check`.
- **Confirms if:**
  - R recovers most `current:overwritten_by_non_gold_value` rows, which sets caused-at at routing, consistent with "reused key".
  - Step 3 codes them architectural or trade-off at key assignment or resolution, quoting D4.p4 at 94c049d ("Review may itself merge distinct meanings").
  - The identity gates pass, consistent with "intact".
- **Overturns if:**
  - The routing cases are coded implementation: (ii-r) or (ii-h) recover them; the 0.80 reuse threshold merged matters; or the harness reviewer accepted an over-broad key.
  - Or the gates fail.
- **Text action if confirmed:** keep, and attribute explicitly to key reuse (D4.p4).
- **Text action if overturned:** rewrite: "claims of other matters were filed under one key; X% of these routing losses had implementation causes". Qualify "intact" by bug 2 and bug 4 (P0-E).
- **Testable here:** yes.
- **Note:**
  - Of the routing-lost rows, 134 of 203 had every carrier keyed by the extractor's hint (Already read), so the reuse is mostly made at extraction, which (ii-h) probes.
  - C86 (eval.tex:1065) makes the same point about D4's reuse, but its sweep counts the reuse-threshold path as confirming the location and as an implementation cause; this row counts it as overturning a design reading. They stay apart for that reason.
- **Also stated at:** C30, C86; section 5, group F.

#### C122 · `thesis/conclusion.tex:248` · par:conc-aggregation

**Claim (gloss).** On ES2009 the list and change losses arise at reading, from poor key selection over an open schema (D4, D8).

```tex
The latest-meeting filter exists; applied to a poorly selected set it cannot reconstruct the delta. This is construction insight~7 of Section~\ref{sec:design-knowledge}: an open schema relocates modelling work into operation, and local concepts need a deliberate aggregation contract for current lists and historical changes.
```

- **Where/why:** where and why.
- **Boundaries:** reading; key resolution and expansion.
- **Mechanisms:** change and supersession.
- **Confirms if:** in the ES2009 Step 5 runs, A1-ref (bug 2 repaired) and the final configuration still return few newly decided items (Step 5 scores). The design reading, D8.p5 at 94c049d ("not a general temporal-difference engine") or D4.p5 ("the work required to resolve broad questions"), is not testable here: change-list failures are not cases, and 3b codes the final configuration's r1 cases, not list answers.
- **Overturns if:** A1-ref answers the newly decided items much better. The A0 failure then rested on bug 2: the change template counts facts whose earliest evidence is the latest meeting, and the lineage defect gave them the oldest claim's evidence.
- **Text action if confirmed:** keep. D8.p5 and D4.p5 (94c049d) may be cited as the documented heuristic and cost, not as a coded cause (amendment:572).
- **Text action if overturned:** rewrite: the change answer failed because facts carried the oldest claim's evidence (bug 2). Qualify construction insight 7.
- **Testable here:** partly.
- **Note:** list questions fall outside the loss trace's per-value unit, and ES2009's trace reaches reading for only 10 rows.
- **Also stated at:** C54 (implementation_chapter.tex:939); C133a (conclusion.tex:366), which reuses this row's test; section 5, group S.

#### C123 · `thesis/conclusion.tex:258` · par:conc-aggregation

**Claim (gloss).** Reused hub keys both attract the resolver and hold wrong values, so reading and state-maintenance losses compound.

```tex
The reader never consults the admitted evidence text, although the evidence records exist and RAG answered from their content; concept reuse produced hub keys whose labels attract the resolver while their current value is whatever arrived last. Aggregation and lifecycle therefore compound: the key most likely to be resolved is the key most likely to hold the wrong value.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution and expansion; state rules; reading.
- **Mechanisms:** change and supersession; `filing_type_check`.
- **Confirms if:** in the offline reading check, the keys chosen in `key_reached` losses are high-fact-count keys that also carry `current:overwritten_by_non_gold_value` rows, and R recovers the overwrite rows on those keys.
- **Overturns if:** the chosen keys are not hubs; or the holding key was pruned (a shortlist cause, not hub attraction); or the overwrites are not concentrated on resolved keys.
- **Text action if confirmed:** keep, with counts.
- **Text action if overturned:** remove the "therefore compound" sentence. Keep the evidence-text clause as a description.
- **Testable here:** partly.
- **Note:**
  - Testing hub status needs a count of facts per key over the frozen states, which no listed step computes. It could be added to the offline reading analysis at $0.
  - The "never consults the admitted evidence text" clause describes A0 and A1. `answer_evidence_fallback` is built but is in no arm.
- **Also stated at:** section 5, groups F and G.

#### C124 · `thesis/conclusion.tex:267` · par:conc-embedding

**Claim (gloss).** No recall is lost in the embedding machinery. Recall is lost at acquisition (admission and extraction) and at aggregation (reading).

```tex
The pre-declared ablation (Section~\ref{subsec:eval-ablation}) shows that the embedding machinery is not where the advantage was lost: removing the resolver's embedding candidates leaves the non-noise pairs within repeat variation, and the reuse contrasts stay within intervals that include zero. What the candidates contribute is restraint on off-topic questions (principle~5), a role the architecture never assigned to them; the recall losses lie in acquisition and aggregation.
```

- **Where/why:** where.
- **Boundaries:** extraction; key resolution and expansion; reading.
- **Mechanisms:** none (restraint on incidental talk is removed from Phase D3 by Step 0).
- **Confirms if:**
  - Probes (b), (ii-r) and (iii) are not recovered where they apply.
  - No case is coded to the shortlist or prune, or to the reuse threshold (`expansion_reuse_threshold`=0.80).
  - The loss trace puts the recall losses at extraction and reading.
- **Overturns if:**
  - (ii-r) or (iii) recover cases under the shortlist sub-cause, or at least 3 distinct values are coded to the reuse threshold.
  - Already read: filing plus state maintenance (A0 21.7 + 24.0 rows) is as large as extraction (46.0), so "acquisition and aggregation" leaves out half the loss.
- **Text action if confirmed:** keep "not where" for EL2020. Add filing and state maintenance to the loss list.
- **Text action if overturned:** remove "the embedding machinery is not where the advantage was lost". Report the shortlist and reuse shares.
- **Testable here:** partly.
- **Note:** the ablation ran on ES2009 and is affected by bug 8 (P0-A). The restraint half cannot be tested here. Decision R-19 applies to the recall half.
- **Also stated at:** C03, C71; section 5, group C.

#### C125 · `thesis/conclusion.tex:277` · par:conc-policy

**Claim (gloss).** The reference-informed arm scores lower because of delayed availability: values are held pending.

```tex
The policy contrast provides no evidence that more informed admission repairs these losses. [...] The counts point to delayed availability, with values held pending rather than rejected, and the arms differ in more than the value gate.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** none.
- **Confirms if:** not tested by this study. The reference-informed arm is not run.
- **Overturns if:** not tested by this study.
- **Text action if confirmed:** n/a.
- **Text action if overturned:** n/a. Independently: bug 14 (the gate confirms on wording) means its cycle-1 results show nothing about review. Follow the open decision in plan 23 on dropping the arm.
- **Testable here:** no.
- **Note:** this row also covers the abstract's "The reference-informed policy scores below the autonomous one." (main.tex:71).
- **Also stated at:** C66 (eval.tex:847); section 5, group L.

#### C126 · `thesis/conclusion.tex:298` · par:conc-links

**Claim (gloss).** Weak evidence links come from the projection path, which copies the triggering claim's evidence. The parenthesis attributes this to D9.

```tex
Two properties of the projection path make such mismatches likely rather than accidental: a proposal copies the evidence of the claim that triggered resolution, which need not be the winning claim, and a demoted fact keeps its earlier evidence (\Dn{9}). Whether they account for the low support rate was not measured.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** evidence and provenance; `filing_support_check`.
- **Confirms if:** not tested for the support rate. Step 3's pass examinations record passes that rest on bug 2.
- **Overturns if:** not tested for the support rate.
- **Text action if confirmed:** n/a.
- **Text action if overturned:** n/a. Independently, describe the copying as an implementation defect that contradicts D9 (bug 2), repaired in A1 (P0-E), not as a property of D9.
- **Testable here:** no.
- **Note:** bug 2 records that the copying contradicts D9, so the attribution to D9 is a conformance error whatever this study shows (section 6.2; decisions R-3 and R-4).
- **Also stated at:** C41, C68; section 5, group I.

#### C127 · `thesis/conclusion.tex:308` · par:conc-readpaths

**Claim (gloss).** On ES2009, RAG's wins come from values that the autonomous arm lost before or in state, not at reading.

```tex
RAG avoids requiring every answerable value to survive a persistent fact representation. Across the five paired repeats on ES2009, ten focused-answer instances were scored correct for RAG and incorrect for ProjectMemory. In seven, the final autonomous dump contained no lexical fact match for the required value, and in three, matches occurred only among superseded or rejected facts.
```

- **Where/why:** where.
- **Boundaries:** extraction; state rules; evaluation (gold correction; C62).
- **Mechanisms:** change and supersession.
- **Confirms if:** the ES2009 joint table (Step 5) puts RAG-credited losses mostly at extraction or state maintenance.
- **Overturns if:** either of these.
  - The joint table puts them mostly at reading.
  - Under the B3 gold, the plastic-casing obligation changes, and the RAG-only wins on that question vanish or reverse in the Step 5 runs.
- **Text action if confirmed:** keep. Replace the lexical counts with loss-trace counts.
- **Text action if overturned:** rewrite with the coded locus, or with the B3 outcome for the plastic-casing question.
- **Testable here:** partly.
- **Note:**
  - The ten instances are from cycle 1.
  - The next sentence puts four of the ten on an unapplied gold correction: "four of them the plastic-casing question at $C_3$ whose gold status is one of the unapplied corrections" (conclusion.tex:313–315). 3b codes cases of the Step 5 run, not these instances. Evaluation defects change no gold within this study; corrections go through B3 (amendment:319), and the author-confirmed corrections are a B3 decision (amendment:140).
- **Also stated at:** section 5, group N.

#### C128 · `thesis/conclusion.tex:322` · par:conc-readpaths

**Claim (gloss).** Part of the gap comes from compound decisions being split by ProjectMemory's templates, at reading.

```tex
The transfer check shows the same access-path difference at scale. In 120 of the 124 EL2020 answers that RAG got right where the autonomous arm was wrong, a cited chunk contained the verified gold line, and free generation restated the whole sentence, keeping compound decisions that the templates split.
```

- **Where/why:** where and why.
- **Boundaries:** reading; extraction.
- **Mechanisms:** complete decisions; WD.
- **Confirms if:** the loss trace finds compound values lost at `answered`, in template rendering, and not earlier.
- **Overturns if:** compound values are lost at `carried`, where claims state one part (Already read: 71 of 130 rejected texts), and `answered` loses only 1.7–2.7 rows per run. WD working (Step 2c) would confirm that extraction is the place.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite "that the templates split" as "that ProjectMemory's extraction split". Replace the 120/124 bug-11 count with the joint table.
- **Testable here:** yes.
- **Note:** the frozen trace, read before signing, already points to overturn.
- **Also stated at:** C89 (eval.tex:1076); section 5, group N.

#### C129 · `thesis/conclusion.tex:326` · par:conc-readpaths

**Claim (gloss).** Part of the RAG gap comes from the evaluation construct, an evaluation cause.

```tex
The construct favours this path, since transcript-grounded gold is transcript phrasing and hybrid retrieval over whole turns is close to an oracle for single-value questions that paraphrase one sentence.
```

- **Where/why:** why.
- **Boundaries:** evaluation.
- **Mechanisms:** none.
- **Confirms if:** on ProjectMemory's side, Step 3 codes a material share of losses as evaluation defect. Or V4's audit agreement is below 0.80, and v2 moves "does not carry" rows. The amendment notes that the adjudication standard (one part of a compound value does not carry it) is stricter than the gold aliases.
- **Overturns if:** few evaluation-defect codes, and v1 equals v2 on the oracle rows.
- **Text action if confirmed:** keep. Cite the evaluation-defect share and v2.
- **Text action if overturned:** qualify: the construct may favour RAG, but no ProjectMemory loss in the coded sample is an evaluation defect.
- **Testable here:** partly.
- **Note:** the half about RAG's retrieval concerns RAG's internals and is not tested.
- **Also stated at:** C101 (eval.tex:1263).

#### C130 · `thesis/conclusion.tex:330` · par:conc-readpaths

**Claim (gloss).** The RAG gap is explained by values lost through write-time normalisation, a design property.

```tex
Its advantage is not general competence at project memory; it is that re-reading the source does not lose what write-time normalisation lost.
```

- **Where/why:** why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules.
- **Mechanisms:** complete decisions; change and supersession.
- **Confirms if:** in the joint table (Step 3), RAG-credited values lost by the autonomous arm are lost mostly at write-time boundaries, not at reading. Step 3 codes them architectural or trade-off on 94c049d text, with the kappa's lower bound at least 0.40.
- **Overturns if:** they are mostly reading losses, which is "schema-first reading", not write time. Or they are coded implementation and recovered by admitted repairs.
- **Text action if confirmed:** keep, with the joint-table shares.
- **Text action if overturned:** rewrite: "re-reading the source does not lose what the evaluated write path lost; X% of those losses were implementation defects".
- **Testable here:** yes.
- **Also stated at:** C04, C89; section 5, groups A and N. Decision R-11 covers this row (Ch. 6 side).

#### C130a · `thesis/conclusion.tex:334` · par:conc-shared

Added in the review of 27 October.

**Claim (gloss).** The enumeration failure that ProjectMemory shares with RAG is attributed to D4 and D8 by the paragraph heading.

```tex
\paragraph{Shared failure (\Dn{4}, \Dn{8}).} \label{par:conc-shared} Both systems fail cumulative enumeration on both series: neither answers a rejection list or a newly-decided list correctly.
```

- **Where/why:** why.
- **Boundaries:** reading.
- **Mechanisms:** change and supersession; rejection.
- **Confirms if:** not testable here. List questions are outside the trace's per-value unit, and RAG is not varied.
- **Overturns if:** not testable here.
- **Text action (either case):** not decided by this study; see decision R-21. The observation (conclusion.tex:336–337) takes C01's actions.
- **Testable here:** no.
- **Note:** the other decision-tagged headings of sec:conc-implications follow their paragraphs' rows (section 5, note on headings). This heading differs: it attributes to two ProjectMemory decisions a failure that RAG shares.
- **Also stated at:** C01 (main.tex:70); section 5, group J.

#### C131 · `thesis/conclusion.tex:341` · par:conc-shared

**Claim (gloss).** The records locate the losses at the admission and lifecycle stages.

```tex
Both systems leave records to inspect, but ProjectMemory's include the admission and lifecycle stages at which a value was formed, kept or replaced, and the preceding paragraphs located the losses at those stages.
```

- **Where/why:** where.
- **Boundaries:** admission; extraction; state rules.
- **Mechanisms:** evidence and provenance.
- **Confirms if:** the identity gates pass, and Step 3 resolves caused-at for at least 90% of cases, mostly at the same stage as surfaced-at.
- **Overturns if:** the gates fail, or unclear caused-at exceeds 10%. Or caused-at differs from surfaced-at for many cases (for example, R moves filing and overwrite losses to routing), so the paragraphs located only where losses surfaced.
- **Text action if confirmed:** keep.
- **Text action if overturned:** qualify: "located where the losses surfaced; their cause was located for X%".
- **Testable here:** yes.
- **Also stated at:** C05, C19, C102; section 5, group B.

#### C132 · `thesis/conclusion.tex:357` · sec:conc-future

**Claim (gloss).** These three contracts would recover extraction and filing losses. Implied: the losses arise where the contracts act.

```tex
\item An \emph{extraction and filing contract} (revising \Dn{10} and \Dn{4}) that keeps a stated decision whole and files it once, checks a claim's value against the key's declared type and cardinality before filing, and treats same-meeting rivals under a scalar key as a conflict rather than a confidence contest (revising the per-key rule of \Dn{5}).
```

- **Where/why:** why.
- **Boundaries:** extraction; key assignment at extraction; state rules.
- **Mechanisms:** WD; `filing_type_check`; `resolution_same_meeting_conflict`; complete decisions.
- **Confirms if:** WD works (Step 2c), and the A2 leave-one-out gives "works" for `filing_type_check` and `resolution_same_meeting_conflict`.
- **Overturns if:** WD is "not shown", or the leave-one-out gives "doesn't work". Already read: A2 scores below A0, and its filing losses rose by 36–40 rows per run.
- **If a bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome for that contract. Text action: report the recorded and the bounded verdicts (amendment:471), make no works or doesn't-work statement, and keep the contract as future work. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** move from future work to a development result (EL2020, bounded verdict). The held-out test remains Phase D.
- **Text action if overturned:** rewrite as tested on EL2020 development, with the result: WD "not shown", or the contract did not work in the leave-one-out. Keep only a revised contract as future work.
- **Testable here:** yes.
- **Note:** all three are built (`cycle2_flags` at 3320375), and two ran as A2.
- **Also stated at:** section 5, group D.

#### C133 · `thesis/conclusion.tex:362` · sec:conc-future

**Claim (gloss).** Wrong supersessions come from reinterpretations of the same span, and a stricter rule would recover them.

```tex
\item A \emph{supersession contract} (revising \Dn{5} and \Dn{7}) that distinguishes genuinely new source information from another interpretation of an existing span; the proposed equal-authority, equal-time conformance case should be executed before a stricter rule is treated as a repair.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** `supersession_requires_new_evidence`; change and supersession.
- **Confirms if:** the A2 leave-one-out gives "works" for `supersession_requires_new_evidence`.
- **Overturns if:** "doesn't work". Or R shows the overwrites are routing, so another-matter rivals, not reinterpretations, drive them.
- **If the bounded leave-one-out verdict is *can't tell (defect-limited)*:** a third outcome. Text action: report the recorded and the bounded verdicts (amendment:471), make no works or doesn't-work statement, and keep the contract as future work. While the conflict decision is open, this is the expected A2 outcome (mapping section 6.2; decision M-21).
- **Text action if confirmed:** report as a development result.
- **Text action if overturned:** rewrite as tested; the contract did not work. Name routing as the coded cause if R shows it.
- **Testable here:** yes.
- **Note:** the conformance case is now executed: the bug-3 repair in A1 keeps the current value on an exact tie.

#### C133a · `thesis/conclusion.tex:366` · sec:conc-future

Added in the review of 27 October.

**Claim (gloss).** List and change losses come from D8's aggregation and change selection. The existing family widening and latest-meeting filter are not shown to be sufficient.

```tex
\item An \emph{aggregation and change contract} (revising \Dn{8}) tested on complete current lists, with change queries built on validity intervals and evidence meetings that return the newly decided items; the existing family widening and latest-meeting filter are starting points whose sufficiency must be demonstrated or whose contracts must be replaced.
```

- **Where/why:** why.
- **Boundaries:** reading; state rules (change).
- **Mechanisms:** change and supersession (D8.p5, change answering). The list half has none: reading (D8), per Rule A and decision R-8.
- **Confirms if:** as C122's ES2009 Step 5 test: A1-ref (bug 2 repaired) and the final configuration still return few newly decided items.
- **Overturns if:** as C122: A1-ref answers the newly decided items much better. The latest-meeting filter's failure in A0 then rested on bug 2.
- **Text action if confirmed:** keep as future work.
- **Text action if overturned:** keep as future work. Qualify the latest-meeting filter clause: its observed failure rested on a lineage defect (bug 2), as in C122's overturned action.
- **Testable here:** partly. Only the change half, through C122's test. List questions fall outside the trace's per-value unit (C112, C122 notes), and no aggregation or change switch exists at 3320375.
- **Note:**
  - It is the one future-work contract with no switch at 3320375. `app/core/config.py:154–160` at 3320375 lists seven contract switches, none for aggregation or change. When C109's "No contract has been implemented" is corrected (R-3(a)), state that this contract is not built.
  - The "existing family widening" is `concept_families_enabled`, on by default (3320375:app/core/config.py:144), so it is part of A0.
- **Also stated at:** C99 (eval.tex:1218), C112 (conclusion.tex:187), C122 (conclusion.tex:248); section 5, group S.

#### C134 · `thesis/conclusion.tex:371` · sec:conc-future

**Claim (gloss).** Reading losses are recoverable from the admitted evidence. Restraint is a by-product of the embedding candidates.

```tex
\item A \emph{read contract} (revising \Dn{8} and \Dn{11}) that falls back to the admitted evidence text when the resolved keys carry no value of the required kind, and that makes restraint on off-topic questions a declared no-match outcome of resolution rather than a by-product of the embedding candidate generator.
```

- **Where/why:** why.
- **Boundaries:** reading.
- **Mechanisms:** none (reading; restraint is removed by Step 0). The read contract is built but is in no arm.
- **Confirms if:** an indirect bound only: the Step 3 joint table counts values admitted but lost later that RAG answered.
- **Overturns if:** the joint table shows few values that were admitted, lost after admission and answered by RAG.
- **Text action if confirmed:** keep as future work, and cite the bound.
- **Text action if overturned:** narrow the contract's expected benefit to the bound.
- **Testable here:** partly.
- **Note:** `answer_evidence_fallback` and `answer_answerability_check` are built at 3320375 but are in no arm of this amendment (mapping decision M-1). The restraint half cannot be tested here (P0-A).
- **Also stated at:** section 5, group C.

#### C135 · `thesis/conclusion.tex:424` · sec:conc-closing

**Claim (gloss).** The design, the separation itself, loses information, and the record shows where.

```tex
Its software-engineering contribution is the implemented separation of evidence, interpretation and commitment, together with a measurement and diagnostic record that shows where that separation loses the information it was built to keep.
```

- **Where/why:** where and why.
- **Boundaries:** extraction; key assignment at extraction; key resolution and expansion; state rules; reading.
- **Mechanisms:** evidence and provenance.
- **Confirms if:** as for C108: the losses are located (identity gates, loss trace), and Step 3 codes them to the design on 94c049d text, with the kappa's lower bound at least 0.40.
- **Overturns if:** most cases are coded implementation or unclear.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite: "shows where the evaluated implementation of that separation loses information".
- **Testable here:** yes.
- **Note:** P0-E lists conclusion.tex:424–427.
- **Also stated at:** C04, C05, C108; section 5, groups A and B.

### 4.8 Appendix A (`thesis/appendix_reproducibility.tex` and the generated tables it inputs)

#### C136 · `thesis/generated/eval_abl_families.tex:6` (input at `thesis/appendix_reproducibility.tex:212`) · tab:eval-ablation-families

**Claim (gloss).** Resolver embeddings drive restraint on noise questions, and the reuse policy causes no measurable loss.

```tex
Embeddings-off arms lose almost only in the noise family; the reuse arms move within repeat variation.
```

- **Where/why:** why.
- **Boundaries:** reading (noise questions); key resolution and expansion (reuse).
- **Mechanisms:** none for the noise half (restraint on incidental talk is removed by the Step 0 plan-23 fixes); change and supersession.
- **Confirms if:** reuse half: Step 3 codes few EL2020 cases to "a reuse or similarity threshold merged a new matter into an existing key" (criterion (iii)).
- **Overturns if:** reuse half: Step 3 codes many routing cases to the reuse threshold, so reuse does cost values on EL2020. The noise half is not tested here. Bug 8 already bars reading it as a resolver-embedding effect, because the ablation switch reaches beyond the resolver.
- **Text action if confirmed:** keep the reuse half; qualify the noise half with bug 8.
- **Text action if overturned:** qualify the reuse half: on EL2020 the reuse threshold merges matters; cite the count.
- **Testable here:** partly.
- **Note:** the caption is written by the generator `15-ablation-tables.py` (committed a01eaef, 24 September), so any text change goes through the generator (decision R-14). The ablation ran on ES2009 with cycle-1 code (bugs 2–6 present).
- **Also stated at:** C73 (eval.tex:979); section 5, group C. Ch. 5 states the noise half at eval.tex:945: "Switching the resolver's embedding candidates off costs 7.8 points overall with an interval that excludes zero. The loss lies entirely in the noise family, 11/24 against 24/24" (eval.tex:945–947). Its text action follows decision R-9, as this row's noise half does:
  - under R-9(a), name the intervention correctly (the switch turned the embedding client off, which also disabled answer-time retrieval and the relevance gate, bug 8), and keep the noise-family location as an observation;
  - under R-9(b), add the bug-8 caveat.

#### C136a · `thesis/generated/eval_abl_writepath.tex:6` (input at `thesis/appendix_reproducibility.tex:213`) · tab:eval-ablation-writepath

Added in the review of 27 October.

**Claim (gloss).** Without embedding candidates, the resolver attaches every noise question to a key, and the failures report unrelated facts.

```tex
Write-path diagnostics from the state dumps (means over three repeats, counts rounded) and the noise-family mechanism. [...] Resolved gives how many of the 24 noise questions the resolver attached to a state key; failed gives how many were scored incorrect; the last two columns classify the failed answers by wording: an unrelated confirmed fact or fact fragment, versus an unrelated proposal list or raw evidence excerpt.
```

- **Where/why:** where and why.
- **Boundaries:** key resolution (question time); reading.
- **Mechanisms:** none (restraint on incidental talk is removed by Step 0).
- **Confirms if:** not testable. The ablation is not re-run, and noise items carry no gold value.
- **Overturns if:** nothing in the study. Known defects already weaken it:
  - bug 10 names "Resolved 24/24" (22-bug-list.md:114) among the figures read from another checkpoint;
  - bug 8: "In the traces, the resolver gave keys for 1 of 24 questions, but 22 of 24 answers carried keys." (22-bug-list.md:104).
- **Text action if confirmed:** not decided by this study; see decisions R-9 and R-14.
- **Text action if overturned:** not decided by this study; see decisions R-9 and R-14.
- **Testable here:** no.
- **Note:**
  - The table rows hold the Resolved figures: "Baseline & 110 & 23.7 & 83 & 141.7 & 8/24" (generated/eval_abl_writepath.tex:12) and "Embeddings off & 106.7 & 8.7 & 85.3 & 140 & 24/24" (generated/eval_abl_writepath.tex:13).
  - The caption is written by `15-ablation-tables.py` (l.101). Regenerating the caption alone does not fix the 8/24 and 24/24 figures, which come from the generator's data path (bug 10).
  - Ch. 5 refers to the table at eval.tex:975–976.
- **Also stated at:** C70 (eval.tex:949); C136; section 5, group C.

### 4.9 Appendix B (`thesis/appendix_walkthrough.tex`)

By its own rule, Appendix B describes the record, never the system: "% to DR1-DR8. RULE: what is happening in the record, never what the artifact" (thesis/appendix_walkthrough.tex:4). Its rows are conversational-difficulty claims tested through the 3b codes on ES2009b gold rows. Appendix B's text does not change whatever the outcome; outcomes go to the implementation-side walkthrough. Its line ranges and episodes stay stable. See decision R-7.

#### C137 · `thesis/appendix_walkthrough.tex:115` · app:walkthrough (Lines 16--18)

**Claim (gloss).** Acknowledgements and passing mentions look like decisions, so status is easily misread. This is a conversational difficulty.

```tex
The responses (``Fair enough'', ``Fine'') are the kind of assent-by-acknowledgement that a reader cannot safely count as a decision (\DR{1}, \DR{4}).
```

- **Where/why:** why.
- **Boundaries:** extraction (modality).
- **Mechanisms:** epistemic status.
- **Confirms if:** in 3b, ES2009b values decided only by acknowledgement, or decided values carried only as proposed, are coded conversational difficulty, with the recoverability rules met. Only the final configuration's r1 on ES2009 can confirm. The author-coded ES2009b walkthrough cases of A0 r1 can come out only implementation defect or unclear at extraction: no probe runs on A0 r1 (amendment:238, :312), so an applicable probe-type alternative stays open (amendment:338).
- **Overturns if:** those cases are coded implementation (probe (i) recovers, or a modality instruction is missing from the prompt) or model-limited. Or the value passed in another run of its arm group.
- **Text action if confirmed:** keep Appendix B unchanged, and cite it in the implementation-side walkthrough.
- **Text action if overturned:** keep Appendix B unchanged, since it describes the record. Report the actual cause in the implementation-side walkthrough.
- **Testable here:** partly.
- **Note:** the ES2009 suite has no candidate-status expectations (22-bug-list.md:139), so over-promotion is observable only through status rows. The same point is made at l.78–79 ("A reading that treats mention as proposal already goes wrong here") and at l.189–190 ("a reader who stopped here would be wrong to record it as decided" (appendix_walkthrough.tex:189–190)).

#### C138 · `thesis/appendix_walkthrough.tex:193` · app:walkthrough (Lines 48--53)

**Claim (gloss).** Decisions made by absorption are hard to recover from wording. This conversational difficulty lies behind status losses.

```tex
And ``we're constrained to plastics'' moves plastic from proposal towards presupposition without any turn in which it was decided --- commitment by absorption, which is exactly what makes status hard to recover from wording (\DR{1}, \DR{6}).
```

- **Where/why:** why.
- **Boundaries:** extraction (`carried`, modality).
- **Mechanisms:** epistemic status; complete decisions.
- **Confirms if:** in 3b, the ES2009b gold row "plastic as their casing material" (and any other absorbed decision) is lost at extraction or modality and coded conversational difficulty, with the recoverability rules met: RAG did not answer it from a cited gold line in at least 2 of 3 runs, and no other run of the arm group passed the step. Only the final configuration's r1 can confirm; A0 r1 walkthrough extraction cases can come out only implementation defect or unclear (amendment:238, :312, :338).
- **Overturns if:** the value passes in some run of its arm group, or RAG recovers it, or it is coded implementation (probe (i) recovers). Absorption was then not what lost it.
- **Text action if confirmed:** keep Appendix B, and cite it in the implementation-side walkthrough.
- **Text action if overturned:** keep Appendix B unchanged. Report the actual cause in the implementation-side walkthrough.
- **Testable here:** partly.
- **Note:** l.307–310 repeats it ("the strongest form of commitment-by-absorption"). ES2009 gold is weaker (27 of 87 rows summary-only), and the ES2009 trace reaches reading for only 10 rows.
- **Also stated at:** C09 (problem_domain.tex:174); section 5, group Q.

#### C138a · `thesis/appendix_walkthrough.tex:201` · app:walkthrough (Lines 54--57)

Added in the review of 27 October.

**Claim (gloss).** Record-level. A conditional proposal loses its condition when it is recorded as a plain feature.

```tex
Recording ``voice control'' as a feature would drop the condition; recording nothing would drop the proposal (\DR{1}, \DR{4}).
```

- **Where/why:** why.
- **Boundaries:** extraction.
- **Mechanisms:** complete decisions.
- **Confirms if:** none available. No reviewed ES2009b gold row carries the conditional voice proposal (a search of `data/ami_eval/gold/reviewed/ES2009.reviewed.yaml` for "voice" on 27 October found only the locating-device and later voice-recognition rows), so the loss trace cannot follow it.
- **Overturns if:** none available.
- **Text action if confirmed:** keep Appendix B unchanged (R-7).
- **Text action if overturned:** keep Appendix B unchanged.
- **Testable here:** no. It becomes testable only if B3 adds a gold row for it; it would then be tested through 3b like C137.
- **Note:** the conversational counterpart of C46 and C118 (a decision not kept whole).

#### C139 · `thesis/appendix_walkthrough.tex:266` · app:walkthrough (Lines 98--105)

**Claim (gloss).** Passing, unowned risks are easily lost at admission or extraction.

```tex
This is the kind of statement that is easy to lose and important to keep: it is state-bearing (an open risk), it has no owner, and it recurs as the decisive constraint in later meetings. Discarding it as chatter would be a coverage failure; recording ``cost investigation: assigned'' would be a false assignment (\DR{4}, \DR{8}).
```

- **Where/why:** why.
- **Boundaries:** admission; extraction.
- **Mechanisms:** epistemic status; none for the restraint part (removed by the Step 0 plan-23 fixes).
- **Confirms if:** none available. The reviewed ES2009 gold has no row for the cost risk, so the loss trace cannot follow it.
- **Overturns if:** none available.
- **Text action if confirmed:** keep Appendix B unchanged.
- **Text action if overturned:** keep Appendix B unchanged.
- **Testable here:** no.
- **Note:** it becomes testable only if B3 adds an item for it (B3 lists "unknown items on discussed-but-unsettled topics").

#### C140 · `thesis/appendix_walkthrough.tex:295` · app:walkthrough (Lines 109--124)

**Claim (gloss).** Contested ideas, and rejections stated only by hedges, are hard to classify, so their status is easily lost or invented.

```tex
Faceplates, an idea the first meeting liked, are now contested. No one rejects them. A reading that promoted ``gimmick'' to a rejection would be manufacturing a decision; one that still reported faceplates as a liked idea would be reporting stale status.
```

- **Where/why:** why.
- **Boundaries:** extraction (polarity, modality); state rules (status).
- **Mechanisms:** rejection; epistemic status.
- **Confirms if:** in 3b, the gold row "interchangeable faceplates" is lost or mis-stated at the ES2009b checkpoint and coded conversational difficulty, with the recoverability rules met. Only the final configuration's r1 can confirm; A0 r1 walkthrough extraction cases can come out only implementation defect or unclear (amendment:238, :312, :338).
- **Overturns if:** it is coded implementation (probe (i) recovers, or a negation instruction is missing) or evaluation defect (B3 changes its gold status).
- **Text action if confirmed:** keep Appendix B, and cite it in the implementation-side walkthrough.
- **Text action if overturned:** keep Appendix B unchanged. Report the actual cause in the implementation-side walkthrough.
- **Testable here:** partly.
- **Note:** the parallel hedged-rejection claim at l.393–396 (downloadable skins) has no ES2009 gold row and cannot be tested. ES2009 rejection values are machine-only gold (amendment:159), so they are evaluation-defect candidates. l.357–358 describes another implied rejection: "the docking base is implicitly ruled out by the reasoning against plug-in remotes (a rejection that is never stated)" (appendix_walkthrough.tex:357–358). It describes the record and makes no loss claim, so it is not a row; it matters only for what 3b and the implementation-side walkthrough check.

#### C141 · `thesis/appendix_walkthrough.tex:415` · app:walkthrough (Lines 168--184)

**Claim (gloss).** A decision stated in weak, drifting wording is easily lost or mis-stated.

```tex
The record is ambiguous about what appears on the screen, and an honest representation must carry that ambiguity rather than pick one word (\DR{1}, \DR{5}). The deciding utterance is also the weakest-sounding sentence in the exchange (\DR{1}).
```

- **Where/why:** why.
- **Boundaries:** extraction (`carried`, modality).
- **Mechanisms:** epistemic status; complete decisions.
- **Confirms if:** in 3b, the gold row "company logo will appear in a brief flash in the boot-up screen of the device" is lost at extraction or modality and coded conversational difficulty, with the recoverability rules met. Only the final configuration's r1 can confirm; A0 r1 walkthrough extraction cases can come out only implementation defect or unclear (amendment:238, :312, :338).
- **Overturns if:** the value passes in another run of its arm group, or RAG recovers it, or it is coded implementation.
- **Text action if confirmed:** keep Appendix B, and cite it in the implementation-side walkthrough.
- **Text action if overturned:** keep Appendix B unchanged. Report the actual cause in the implementation-side walkthrough.
- **Testable here:** partly.
- **Note:** line ranges and episodes stay stable, because the walkthrough is the base for the 3b implementation-side walkthrough.

#### C142 · `thesis/appendix_walkthrough.tex:451` · app:walkthrough (What the meeting established)

**Claim (gloss).** Project state can be recovered only by linking statements that lie far apart, carrying hedges across meetings and withholding unsupported rejections. Failing at this work is where a memory loses state.

```tex
Producing it required connecting a proposal at line~58 to its decision at line~148, carrying ``provisionally'' from line~130 into the next meeting, refusing to promote ``gimmick'' to a rejection, and holding the solar proposal open because nobody closed it. A project memory must perform that work for every meeting and keep the result current as later meetings revise it;
```

- **Where/why:** where and why.
- **Boundaries:** extraction (window, modality); key assignment at extraction; state rules (status across checkpoints).
- **Mechanisms:** complete decisions; epistemic status; rejection; change and supersession.
- **Confirms if:** in 3b, the ES2009b gold rows for the locating device (proposed at line 58, decided at line 148) and for the touch screen interface (provisional, superseded at ES2009c) are lost at extraction, filing or status. They are coded conversational difficulty, or architectural on D2's 94c049d window passage, with the recoverability rules met. Only the final configuration's r1 can confirm; A0 r1 walkthrough extraction cases can come out only implementation defect or unclear (amendment:238, :312, :338).
- **Overturns if:** these values pass in the ES2009 runs, or are coded implementation: probe (i), an A1 repair, or an admitted contract recovers them. In 3b only probe (i) runs (amendment:238), and a contract such as the type check acts only if admitted.
- **Text action if confirmed:** keep Appendix B, and cite it in the implementation-side walkthrough.
- **Text action if overturned:** keep Appendix B unchanged. Report the actual causes in the implementation-side walkthrough.
- **Testable here:** partly.
- **Note:** the same non-local point is made at l.216–219 (line 58 settled by line 148) and at l.330–332 ("provisionally"). The ES2009 trace reaches reading for only 10 rows, so mainly the write path is tested.
- **Also stated at:** C22 (implementation_chapter.tex:210); section 5, group R.

### 4.10 Appendix C (`thesis/appendix_design_evidence.tex`)

#### C143 · `thesis/appendix_design_evidence.tex:81` · app:authority-conformance

**Claim (gloss).** The blocked rejection is a documented limitation, caused by the missing temporal test, not a defect.

```tex
Case C7 reproduces a documented limitation (an earlier affirmation blocks a later rejection because the affirmation check has no temporal test); it is counted as conformant to the documented behaviour, not as correct behaviour.
```

- **Where/why:** why.
- **Boundaries:** state rules.
- **Mechanisms:** rejection.
- **Confirms if:** A0 rejection cases caused at the state rules show blocking only where an older affirmation exists. This is consistent with a missing temporal test.
- **Overturns if:** in A0 the affirmation check blocks every negation of the current value, whether or not an older affirmation exists (bug 1). Step 3's A0 model pre-codes code these cases as a Phase B bug.
- **Text action if confirmed:** keep.
- **Text action if overturned:** rewrite: C7 shows bug 1, a defect repaired behind a switch. Regenerate the conformance table under the repair, and report both versions.
- **Testable here:** yes.
- **Note:** retrospective wording (c6fbdc0, 19 October). Same mechanism as Ch. 4 l.358–361 (C33). Decision R-4 applies.
- **Also stated at:** C25, C33; section 5, group M.

#### C144 · `thesis/appendix_design_evidence.tex:169` · app:design-evidence (Operational Details Retained for Reproducibility)

**Claim (gloss).** A silent fallback could change what is extracted.

```tex
Model-provider or validation failure can substitute a deterministic rule path, including a narrow-domain fallback extractor. Strict-live admission must therefore be interpreted from the actual runner version and report.
```

- **Where/why:** why.
- **Boundaries:** extraction; every LLM seam.
- **Mechanisms:** none.
- **Confirms if:** a run report among the twelve has `fallback_count` above 0, or a run is not strict-live.
- **Overturns if:** the twelve runs report `fallback_count` 0 under `strict_live`, so no observed loss rests on a fallback.
- **Text action if confirmed:** keep, and name the affected runs.
- **Text action if overturned:** keep as a validity caveat, and cite the zero counts.
- **Testable here:** yes.
- **Note:** 94c049d. The Ch. 4 sweep checked a0_r1 and a2_r1: their `coldstart.json` has `fallback_count` 0 and `config.strict_live` true. The other ten runs were not checked then. Checked on 28 October 2026 (decision B8): a0_r2, a0_r3, the A1 smoke run, a1_r2, a1_r3, a2_r2b and a2_r3 (`coldstart.json`), and rag_r1, rag_r2 and rag_r3 (`.rag.json`, the RAG runs' report), each at its manifest hash, all have `fallback_count` 0 and `config.strict_live` true. So all twelve runs report `fallback_count` 0 under `strict_live`. No verdict is recorded here. The commented-out Ch. 4 l.876–882 makes the same point (section 7, dormant 3).
- **Also stated at:** section 5, group P.

## 5. Claims stated in more than one place

The thesis aims at one home per claim. Each group below states one claim, or one causal reading, in several places. A group is a candidate for consolidation when the text actions are applied. The locations inside a row's note (tables, insights, threats rows) are listed there and are not repeated here.

| Group | Claim (gloss) | Rows (locations) |
|---|---|---|
| A | The EL2020 loss lies in write-time normalisation, or in the design | C04 (main.tex:74, eval.tex:1084, eval.tex:1150), C06 (main.tex:141), C77 (eval.tex:1018), C108 (conclusion.tex:159), C130 (conclusion.tex:330), C135 (conclusion.tex:424) |
| B | The retained records allow the losses to be traced | C05 (main.tex:81, eval.tex:1089, conclusion.tex:92, eval.tex:1152), C19 (implementation_chapter.tex:173), C102 (conclusion.tex:15), C131 (conclusion.tex:341), C135; tested against conclusion.tex:223 (the trace does not record whether D5's condition operated; C120's note) |
| C | Restraint comes from the resolver's embedding candidates, not recall | C03 (main.tex:73), C24 (implementation_chapter.tex:223), C65 (eval.tex:826, eval.tex:1121), C70 (eval.tex:949), C71 (eval.tex:960, eval.tex:1150), C72 (eval.tex:966), C74 (eval.tex:997), C106 (conclusion.tex:59), C114 (conclusion.tex:189), C124 (conclusion.tex:267), C134 (conclusion.tex:371), C136 (generated/eval_abl_families.tex:6, eval.tex:945), C136a (generated/eval_abl_writepath.tex:6, eval.tex:975) |
| D | Fragmenting extraction, and D10 as its cause | C45 (implementation_chapter.tex:606), C46 (implementation_chapter.tex:608), C81 (eval.tex:1040, conclusion.tex:204), C82 (eval.tex:1047), C110 (conclusion.tex:185), C118 (conclusion.tex:211), C132 (conclusion.tex:357) |
| E | Winner-take-all filing under D5's per-key ranking | C34 (implementation_chapter.tex:364), C83 (eval.tex:1050, conclusion.tex:229), C98 (eval.tex:1210), C98a (eval.tex:1213, conclusion.tex:224, conclusion.tex:377), C111 (conclusion.tex:186), C120 (conclusion.tex:221, conclusion.tex:223) |
| F | Overwriting under reused or hub keys, and uniform authority | C30 (implementation_chapter.tex:305), C84 (eval.tex:1057, conclusion.tex:232), C85 (eval.tex:1060, conclusion.tex:226), C86 (eval.tex:1065, eval.tex:1120), C91 (eval.tex:1116), C92 (eval.tex:1125), C121 (conclusion.tex:235), C123 (conclusion.tex:258) |
| G | Schema-first reading | C40 (implementation_chapter.tex:530), C49 (implementation_chapter.tex:637), C53 (implementation_chapter.tex:932), C87 (eval.tex:1068, conclusion.tex:252), C88 (eval.tex:1072, conclusion.tex:256), C112 (conclusion.tex:187), C113 (conclusion.tex:188), C123 |
| H | Review and value confirmation caused no loss in the autonomous arm | C51 (implementation_chapter.tex:921), C67 (eval.tex:852, eval.tex:1119, eval.tex:1223), C93 (eval.tex:1130, conclusion.tex:117, eval.tex:1264) |
| I | Evidence links and lineage (bug 2) | C02 (main.tex:72, eval.tex:1118), C41 (implementation_chapter.tex:557), C43 (implementation_chapter.tex:570), C68 (eval.tex:886), C76 (eval.tex:1014), C111, C119 (conclusion.tex:217), C126 (conclusion.tex:298) |
| J | Change and rejection answers fail | C01 (main.tex:70, conclusion.tex:20, conclusion.tex:336, conclusion.tex:419), C38 (implementation_chapter.tex:510), C61 (eval.tex:788), C104 (conclusion.tex:42), C105 (conclusion.tex:47), C130a (conclusion.tex:334, the heading's decision tags) |
| K | Admission losses are small, or a deliberate cost | C11 (problem_domain.tex:225, problem_domain.tex:485), C21 (implementation_chapter.tex:194), C23 (implementation_chapter.tex:219), C79 (eval.tex:1033) |
| L | The reference-informed arm | C63 (eval.tex:808, conclusion.tex:73), C66 (eval.tex:847, eval.tex:1119, eval.tex:1148), C125 (conclusion.tex:277, main.tex:71) |
| M | An earlier affirmation blocks a negation (bug 1) | C25 (implementation_chapter.tex:248), C33 (implementation_chapter.tex:358), C143 (appendix_design_evidence.tex:81) |
| N | RAG's gap is explained by re-reading the source | C89 (eval.tex:1076), C127 (conclusion.tex:308), C128 (conclusion.tex:322), C130 |
| O | Abstention on unknown topics | C48 (implementation_chapter.tex:635), C75 (eval.tex:999, eval.tex:1117, conclusion.tex:68) |
| P | Fallbacks could change what is extracted | C144 (appendix_design_evidence.tex:169), dormant 3 (implementation_chapter.tex:876) |
| Q | Commitment by absorption | C09 (problem_domain.tex:174), C138 (appendix_walkthrough.tex:193, :307) |
| R | Decisions completed outside the local window | C08 (problem_domain.tex:167, in its note), C22 (implementation_chapter.tex:210), C142 (appendix_walkthrough.tex:451, :216, :330) |
| S | Cold start relocates schema work into operation | C54 (implementation_chapter.tex:939), C122 (conclusion.tex:248), C133a (conclusion.tex:366) |
| T | ES2009 losses at acquisition | C97 (eval.tex:1201), C115 (conclusion.tex:196) |
| U | Verified values are lost between meetings (persistence) | C75a (eval.tex:1010, eval.tex:1115, generated/eval_tr_types.tex:13, conclusion.tex:37); related: C58 (eval.tex:753, ES2009, with the caveat that the decline is not a controlled estimate of forgetting) |
| V | The stance reading of unknown answers decides the ES2009 sign | C69 (eval.tex:909, main.tex:67, conclusion.tex:82, conclusion.tex:89) |
| W | Change answers fail on missing values, not strict scoring | C60 (eval.tex:783, conclusion.tex:44) |
| X | Unapplied gold corrections bound the ES2009 later obligations | C62 (eval.tex:793, conclusion.tex:313), C127 (conclusion.tex:308, evaluation boundary) |
| Y | H4's loss condition fails: restraint coexists with omitted answerable content | C64 (eval.tex:816, conclusion.tex:70) |
| Z | Evidence-only reading scored at least as well as state-first reading | C96 (eval.tex:1173, conclusion.tex:318) |
| AA | No result isolates one mechanism or decision | C18 (implementation_chapter.tex:140), C55 (eval.tex:455, conclusion.tex:96); see decision R-11 |

Groups A, C, D and F hold rows whose sweeps set up the test differently. C03 and C71 disagree on whether the recall clause is testable (decision R-19). C46, C82, C110 and C118 read a WD result differently (decision R-20). C86 and C121 read the reuse-threshold path differently (see C121's note). Those rows were therefore not merged.

Groups U to AA were added in the review of 27 October, for rows whose other locations had been unlisted.

**Note on the decision-tagged headings of sec:conc-implications** (added in the review of 27 October).
- Each paragraph heading there names Ch. 4 decisions. The file header says the mechanisms are "attributed to the Chapter 4 decisions" (conclusion.tex:4). The tags include the retrospective D10 (l.194) and D11 (l.241).
- Each heading follows the text actions of its paragraph's rows. Decision R-5 covers its D10 and D11 tags.
  - l.194, `Acquisition (\Dn{2}, \Dn{3}, \Dn{10})`: C115–C118 and C81;
  - l.215, `Lifecycle (\Dn{5}, \Dn{7})`: C119–C121 and C83–C85;
  - l.241, `Aggregation and reading (\Dn{4}, \Dn{8}, \Dn{11})`: C122–C123 and C87–C88;
  - l.265, `Embedding matching (\Dn{4}, \Dn{8})`: C124;
  - l.275, `Confirmation policy (\Dn{6})`: C125;
  - l.288, `Evidence links (\Dn{9})`: C126;
  - l.306, `Alternative read paths (\Dn{8}; Section~\ref{subsec:eval-fairness})`: C127–C130, and decision R-11;
  - l.334, `Shared failure (\Dn{4}, \Dn{8})`: its own row, C130a (decision R-21), with C131.

## 6. Claims this study cannot test

### 6.1 Rows marked "not testable here"

| Row | Location | Proposed text action |
|---|---|---|
| C02 | main.tex:72; eval.tex:1118 | Qualify by bug 2 (P0-E), independently of this study. |
| C26 | implementation_chapter.tex:260 | Leave unchanged (no collection keys run). |
| C29 | implementation_chapter.tex:303 | Leave unchanged, as development history. |
| C39 | implementation_chapter.tex:525 | Leave unchanged. |
| C42 | implementation_chapter.tex:564 | Leave unchanged. |
| C55 | eval.tex:455 | Keep. Make the transfer attributions (eval.tex:1036–1038, 1076–1078, 1084–1089) consistent with it (decision R-11). |
| C60 | eval.tex:783 | Keep. |
| C63 | eval.tex:808 | Follow plan 23's open decision on the reference-informed arm (bug 14; decision R-10). |
| C65 | eval.tex:826 | Remove the attribution to the resolver's embedding candidates; keep the noise passes as an observation; disclose bugs 8 and 10 (P0-A, P0-B; decision R-9). |
| C66 | eval.tex:847 | Follow the bug-14 decision (decision R-10). |
| C70 | eval.tex:949 | As C65. The keys came through answer-time retrieval (bug 8), so "the resolver attached" is not supported. |
| C71 | eval.tex:960 | As C65 for the restraint clause. Check "a role D8 never assigned to it" against 94c049d. For the recall clause, see decision R-19. |
| C72 | eval.tex:966 | As C65. If kept, name answer-time retrieval and the relevance gate (bug 8). |
| C74 | eval.tex:997 | State the noise pass as an observation, not as a mechanism that transfers. The EL2020 noise items forbid nothing. |
| C106 | conclusion.tex:59 | Rewrite under P0-A and P0-B (three callers; counts 10 of 13 and 9 of 11). |
| C114 | conclusion.tex:189 | P0-A. Remove "Component measured by the ablation" (bug 8). |
| C125 | conclusion.tex:277 | Follow the bug-14 decision (decision R-10). |
| C126 | conclusion.tex:298 | Describe the copying as an implementation defect that contradicts D9 (bug 2), repaired in A1 (P0-E). |
| C130a | conclusion.tex:334 | Keep the observation (C01). The heading's D4 and D8 tags follow decision R-21. |
| C136a | generated/eval_abl_writepath.tex:6 | As C70; caption and Resolved column per decisions R-9 and R-14 (bugs 8 and 10). |
| C138a | appendix_walkthrough.tex:201 | Keep Appendix B unchanged. |
| C139 | appendix_walkthrough.tex:266 | Keep Appendix B unchanged. |

### 6.2 Text actions that Phase B records fix whatever this study shows

These do not wait for an outcome. Decisions R-2 and R-3 ask when to apply them.
- **C85** (eval.tex:1060, conclusion.tex:226–229): "because the transcripts carry no (source) date". The meetings are dated (eval.tex:295–296); the runner did not pass the dates (bug 6).
- **C88** (eval.tex:1072, conclusion.tex:256) and the same clause in C112: the wrong-key figure. Bug 9.
- **C119** (conclusion.tex:217): the flagship ownership trace. Bug 2 (P0-E).
- **C126** (conclusion.tex:298): the copying cited as D9. Bug 2.
- **C05** (eval.tex:1092): "within the lineage limits of \Dn{9}". Bug 2; the action follows decision R-4 (see C05).
- **C109** (conclusion.tex:168): "No contract has been implemented". Seven contracts are built at 3320375; four ran as A2.
- **The bug-11 counts** (P0-C): C78 (the funnel table), C79, C81, C83, C84, C87, C110, C111, C113.
- **The restraint attributions** (P0-A): group C.

### 6.3 Testable rows with an untestable part

- C01: "both systems" (the RAG half).
- C03, C124: the restraint half.
- C05: conclusion.tex:92's clause on declining incidental questions, and eval.tex:1089's counterpart.
- C30: the reference-informed clause (no such arm runs; bug 14).
- C77: "clearer" and the cross-suite comparison.
- C108: "a loss at an earlier boundary survives every later step" (true by construction).
- C129: RAG's retrieval half.
- C133a: the list half (no aggregation switch; list questions are outside the trace's unit).
- C134: the restraint half.
- C136: the noise half.
- C140: the parallel claim at appendix_walkthrough.tex:393–396 (no gold row).

## 7. Dormant (commented-out) claims

The front-and-Ch. 6 sweep and the Ch. 5 sweep found none in their files: the only commented-out lines there are file headers and editorial notes. All six entries are in `thesis/implementation_chapter.tex`, in the commented-out passages at l.866–890 and l.1003–1035. None is a register row. Each note says what applies if the passage is restored.

**Dormant 1** · `thesis/implementation_chapter.tex:869`

```tex
% Typed responses, structural validation, and constrained choices limit malformed
% model outputs and invented registry identifiers. [...]
```

- Live at 94c049d, in "Operational Limits", outside D1–D9. It claims that the mechanism stops invented keys.
- For A0 it is contradicted by bug 5: key hints were filed unvalidated, including the literal key "null" (22-bug-list.md:59–63). A1 repairs it (`repair_undefined_key_filing`).
- If restored: qualify it with bug 5, and test it against the Step 3 key-assignment cases.

**Dormant 2** · `thesis/implementation_chapter.tex:872`

```tex
% [...] The grounding instruction prohibits unsupported additions,
% but schema validation does not prove that revised prose obeys it; the rule
% fallback can mark a draft grounded without an entailment test.
```

- A reading and evidence claim about the grounding pass.
- This study has no grounding audit, so it cannot be tested here.

**Dormant 3** · `thesis/implementation_chapter.tex:876`

```tex
% Fallback changes the evaluated condition. The offline extractor recognises a
% narrow database-technology example and is not evidence of open-domain
% extraction. [...]
```

- Same point as C144 (appendix_design_evidence.tex:169).
- The frozen runs checked (a0_r1, a2_r1) report `fallback_count` 0 under `strict_live`. If restored, cite the counts.

**Dormant 4** · `thesis/implementation_chapter.tex:884`

```tex
% Deduplication is similarly local. Artifact hashes, evidence reuse,
% already-processed extraction, proposal content keys, and parked-claim status
% avoid selected repeated operations. They do not establish global idempotency:
% proposal reuse spans terminal statuses, and lower-level application accepts
% an already accepted proposal. Incomplete idempotency and independent commits
% can affect the state presented to later questions. [...]
```

- Live at 94c049d, outside D1–D9.
- "proposal reuse spans terminal statuses" is the mechanism of bug 12, found in Phase B (22-bug-list.md:75–80). The dormant text therefore documented it before cycle 1, but not as a design decision.
- If restored: cite bug 12 and `repair_open_proposal_dedup`. It can be tested as A0 against A1 at the `proposed` step.

**Dormant 5** · `thesis/implementation_chapter.tex:1008`

```tex
% and projection; and state-first answers. Several limitations remain:
% information can be lost or delayed, review is fallible, authority is coarse,
% concepts can fragment, and preserved history and citations can support fewer
% questions than their storage suggests.
```

- A summary of the live loss claims: lost (D2/D1: C20, C21), delayed (D6: C35), coarse authority (D5: C85, C92), fragmenting concepts (D4: C28), and history and citations (D8/D9: C38, C41).
- If restored, it takes the actions of those rows.

**Dormant 6** · `thesis/implementation_chapter.tex:1016`

```tex
% making obsolete alternatives current (D3, D5, D7, D8); unknown and incidental
% topics should elicit restraint without excessive omission (D2, D3, D8); and
```

- A restraint hypothesis. Restraint on incidental talk is removed from the Phase D3 mechanisms.
- If restored: align it with the live D2 restraint row (C24), and note that the EL2020 noise items forbid nothing.

## 8. Decisions for signing (claims part)

These merge the three sweeps' decisions; R-18 to R-20 are this assembly's own. R-21 and R-22 were added in the review of 27 October, and R-4, R-5, R-11, R-13, R-14 and R-16 were extended there (section 10). The mapping's decisions M-1 to M-21 are in section 9 (mapping section 8) and are not repeated here.

- **R-1. How the sizes in "confirms if" and "overturns if" bind.**
  - *Context:* rows use "most", "large", "few", "at least 3 distinct values" and "unclear at most 10%". The amendment fixes the bound rule, the admission measures and the 0.40 rule, but no rule for when a thesis sentence counts as confirmed. The front sweep recommended treating sizes as indicative; the Ch. 5 sweep recommended one binding rule.
  - *Options:* (a) bind every row's sizes as written; (b) indicative only: the text action follows the amendment's own rules, and the sizes only guide wording; (c) sign one global text-action rule with the register and treat the per-row sizes as indicative. Under (c), a sentence that says X causes losses at boundary B is kept when the bounded share of B's coded cases with that cause is a majority; it is qualified between about 20% and 50%, and removed below 20%. Any design attribution also needs 94c049d text and a kappa lower bound at or above 0.40. "at least 3 distinct values" (amendment:516) and "at most 10%" (amendment:442) stay as the amendment's own numbers.
  - *Recommendation:* (c). It fixes the text actions before the outcomes exist, which is what amendment:111–112 asks for, and it adds one rule rather than 144. Disclose that the 20% and 50% thresholds were proposed in Step 0 and were not checked by the four review rounds.
- **R-2. When to apply the P0 text fixes (P0-A to P0-E), including the bug-11 counts.**
  - *Options:* (a) apply P0 before signing, and re-sweep the changed sentences; (b) sign the register on the current text, mark the P0 rows "rewritten regardless", and apply P0 before any Step 2 output exists. Under (b), the bug-11 counts are replaced by loss-trace v3.1 first-loss counts (rows and distinct values, A0 and A1), labelled surfaced-at, with causes left to Step 3. (c) Defer P0 to the reveal.
  - *Recommendation:* (b). It ties the register to the text as signed, makes clear that those actions do not depend on outcomes, and follows plan 23, Phase F, item 1, which listed the P0 text fixes as independent of Phases B–E until 27 October (plan 23:375 now records the move). Avoid (c): edits made after the outcomes are read would look steered.
  - *Answered (author, 27 October; decision sheet C46):* (b), with the P0 fixes applied in Phase F after Phase E. Plan 23 moved Phase F, item 1, there that day. The P0 content stays as `22-fix-priorities.md` fixes it at ce75b1f. Any change to that wording made after the outcomes are read is disclosed.
- **R-3. Conformance corrections that Phase B records already decide** (section 6.2): C85's date clause (bug 6), C126's D9 attribution (bug 2), C119's flagship trace (bug 2, P0-E), C88's wrong-key figure (bug 9), and C109's "No contract has been implemented".
  - *Options:* (a) correct them now as conformance fixes, recorded here as "decided before signing"; (b) leave them for the reveal.
  - *Recommendation:* (a). They are facts about the code, not outcomes.
- **R-4. 94c049d limitation sentences that describe behaviour Phase B later classed as a bug.**
  - *Context:* D3 l.248–250 and D5 l.358–361 (bug 1); D9 l.557–560 (bug 2); D5 l.355–358 and D5.p3's equal-time eligibility (bug 3; whether this item belongs here is decision R-22); D5.p5's fallback to ingestion time, where the runner withheld the dates (bug 6); dormant 4 (bug 12, outside D1–D9). Rows affected: C05 (the D9 clause at eval.tex:1092), C25, C32, C33, C41, C68, C85, C98, C120, C143. If the design-and-controls register quotes whole D-sections, these sentences become design entries that could ground an architectural code for a bug.
  - *Options:* (a) design entries (architectural weakness possible); (b) implementation entries: documented gaps between the stated policy and the code. A0 losses resting on a Phase B bug count as repaired; otherwise they are conformance defects. The text notes that Ch. 4 had disclosed the limitation. (c) Decide case by case on the page.
  - *Recommendation:* (b). It matches Phase B's classification. It also puts behaviour that contradicts the stated policy in the amendment's conformance class, "**(1) Conformance:** the code contradicts the register." (amendment:325), rather than letting a documented gap ground an architectural code for a bug. Settle it before signing, because it decides codes, and the design-and-controls register should list these sentences the same way.
- **R-5. Retrospective text cited as a design cause.**
  - *Context:* D10 and D11 (5de9911); D5's winner-take-all paragraph (implementation_chapter.tex:363–372); D4's reuse-by-label sentence (l.305); D8's reader-preference sentence (l.530); the D5 conflict sentences (l.338–346); l.140; the truth-maintenance paragraph (b422b27); and the D10/D11 rows and DR limitation cells of the two Ch. 4 tables. Ch. 5 and Ch. 6 cite several as causes (C82, C83, C87, C110, C113, C118). The decision tags in the paragraph headings of sec:conc-implications (conclusion.tex:194, 215, 241, 265, 275, 288, 306, 334) include D10 (l.194) and D11 (l.241); each heading follows its paragraph's rows (section 5, note on headings), and l.334 is decision R-21.
  - *Options:* (a) in the register, name for each claim the 94c049d paragraph that could ground it (D4.p4, D4.p5, D5.p3, D5.p5, D5.p6, D8.p3, D8.p4, D8.p5, D9.p4, D9.p5). Re-ground only where the codes support it, otherwise make the claim location-only. (b) Also mark D10, D11 and the other post-9 September sentences in Ch. 4 now, as made explicit after cycle 1, with dates (P0-D). (c) Move D10 and D11 to Ch. 6 as design lessons.
  - *Recommendation:* (a) and (b). The rows already name the 94c049d paragraphs. (b) states the provenance the amendment already relies on. Settle the exact Ch. 4 wording from the codes at the reveal.
- **R-6. Which configuration Ch. 4's "evaluated configuration" sentences describe** (D3 l.248, D4 l.296, D5 l.364). A0 at 3320375 with every switch off is the evaluated behaviour; some sentences are true only under the A1 repairs.
  - *Options:* (a) Ch. 4 describes A0, the revision behind the Ch. 5 cycle-1 results, and marks each repaired behaviour with its switch; (b) Ch. 4 describes the final configuration (A1-ref plus admitted contracts), with A0's behaviour as a defect note.
  - *Recommendation:* (a). It keeps Ch. 4 matched to the evaluated results, and turns each bug-contradicted sentence into a qualification rather than a silent change.
- **R-7. Problem-level (Ch. 2) and record-level (Appendix B) claims in the register.**
  - *Options:* (a) include them, as here. Their actions are restricted to "keep" or "qualify without solution content" (Ch. 2) and "unchanged" (Appendix B); consequences for the system go to Ch. 6 or to the implementation-side walkthrough. (b) Exclude them, and register only the Ch. 5 and Ch. 6 sentences that use them as causes.
  - *Recommendation:* (a). Plan 23, Phase F 2, asks Ch. 2 to keep the difficulties that come from conversation apart from those the architecture introduces. The register is where that separation is checked against the codes. Appendix B's line ranges and episodes stay stable.
- **R-8. Claims with no remaining Phase D3 mechanism:** admission (C11, C21, C23, C79), restraint (group C, C24, dormant 6) and reading (C40, C49, C53, C87, C103, C113).
  - *Options:* (a) account per the mapping's Rule A ("none: admission (D2)", "none: reading (D8)"; restraint removed), with the reading rows naming the read contract as built, in no arm, and not tested; (b) map reading to evidence and provenance; (c) add the read contract as a Phase D3 mechanism (Phase D only, in a dated note).
  - *Recommendation:* (a) for Phase C, consistent with mapping decisions M-1 and M-10; revisit at the Phase D3 registration. The Ch. 4 sweep had proposed mapping reading to the read contract; under (a) the contract is named in the rows but carries no verdict.
- **R-9. Restraint claims** (group C). They rest on the ablation switch that also disabled answer-time retrieval and the relevance gate (bug 8), and on resolved-key counts read from another checkpoint (bug 10). The amendment removes restraint from the Phase D3 mechanisms.
  - *Options:* (a) remove the attribution to the resolver's embedding candidates and "a role D8 never assigned to it"; keep the noise-family passes as an observation, disclosing bugs 8 and 10; (b) keep the attribution with bug-8 and bug-10 caveats; (c) build per-component switches, which reverses the 22 October decision.
  - *Recommendation:* (a). It follows P0-A and the 22 October decision. Do not add sentences about internal plans that were not carried out.
- **R-10. Reference-informed arm claims** (C30's clause, C63, C66, C125).
  - *Options:* (a) mark them "untested here; the text follows the bug-14 decision" (plan 23's open decision on the arm); (b) add a rebuilt-gate arm, which is outside this amendment.
  - *Recommendation:* (a).
- **R-11. Internal tension in Ch. 5, recurring in Ch. 6.** eval.tex:455 and eval.tex:1257 say that no result attributes a difference to one mechanism. eval.tex:1036–1038, 1076–1078 and 1084–1089 attribute the transfer gap to named mechanisms, and l.1086–1089 list schema-first reading under write-time normalisation. Ch. 6 repeats the tension: conclusion.tex:96 says "The comparison does not isolate a single mechanism" (conclusion.tex:96), while conclusion.tex:330 (C130), under the heading at conclusion.tex:306 that cites the fairness section, says RAG's advantage "is that re-reading the source does not lose what write-time normalisation lost" (conclusion.tex:331–332).
  - *Options:* (a) keep eval.tex:455 and conclusion.tex:96, and rewrite the transfer attributions as locations of ProjectMemory's losses (surfaced-at, then caused-at from Step 3), not as an explanation of the PM–RAG gap. In Ch. 6 this rewrites C130 (conclusion.tex:330) and C89 (eval.tex:1076) and the rest of group N, whose actions then read as locations of ProjectMemory's losses. (b) qualify eval.tex:455 and conclusion.tex:96 to exempt the span-level trace.
  - *Recommendation:* (a), settled after Step 3. It affects how Ch. 6 frames the comparison: under (a), conclusion.tex:96, :306 and :330 are edited together.
- **R-12. Two meanings of "admission" in Ch. 5:** the gatekeeper (eval.tex:1033) and value confirmation (eval.tex:852–855, 1223–1224).
  - *Options:* (a) map eval.tex:852 and 1223 to the loss-trace step `applied`, and eval.tex:1033 to `admitted`; reword the former to "value confirmation"; (b) map both to admission.
  - *Recommendation:* (a). The rows already do this (C67, C79).
- **R-13. ES2009 claims** (C56–C59, C61, C62, C69, C97, C98a, C99, C115–C117, C122, C127). They can be checked only on Step 5's new runs (A0, A1-ref, RAG) under the B3 gold, with no oracle ceiling, and the trace reaches reading for only 10 rows.
  - *Options:* (a) keep the cycle-1 numbers, and qualify their causal readings by the Step 5 results, framed as a consistency check, not a replication; (b) mark the ES2009 causal readings untested.
  - *Recommendation:* (a). It matches the amendment's framing of ES2009 as a weaker second series (amendment:157–160).
- **R-14. The generated ablation tables C136 and C136a** (`thesis/generated/eval_abl_families.tex:6` and `thesis/generated/eval_abl_writepath.tex:6`, both written by `15-ablation-tables.py`). C136's noise half conflicts with bug 8 and the dropped restraint claim. C136a's caption says "the resolver attached" the noise questions, which bug 8 contradicts, and its Resolved column holds the 8/24 and 24/24 figures that bug 10 names as wrong.
  - *Options for the captions:* (a) qualify both captions through the generator (bug 8: the switch reaches beyond the resolver); (b) remove the ablation tables from the appendix; (c) leave them.
  - *Options for C136a's Resolved column* (only if the table stays): (i) re-derive it per checkpoint after the bug-10 repair; (ii) drop the column; (iii) remove the table.
  - Regenerating the caption alone does not fix the 8/24 and 24/24 figures. They come from the generator's data path (bug 10), not from the caption string.
  - *Recommendation:* (a) for the captions: regenerate them, and keep the families table as a cycle-1 development record. For the Resolved column: (ii). Under bug 10 a question asked at four checkpoints keeps only its earliest checkpoint's log (22-bug-list.md:114), and every noise item is such a question, so the saved dumps cannot give per-checkpoint counts. (i) would need the ablation re-run, which reverses the 22 October decision. (iii) removes the rest of a cycle-1 record that only this column makes wrong.
- **R-15. Rows not testable here** (section 6.1).
  - *Options:* (a) leave the text unchanged unless an independent fix applies (P0, a conformance fix, the bug-14 decision), and list the rows as not tested; (b) qualify each one now as untested.
  - *Recommendation:* (a). This study cites no result for them, so it gives no reason to change them.
- **R-16. Sentences outside the register's scope that Phase B contradicts:** main.tex:124, "new concepts admitted only through review" (bug 5); background.tex:195, "validity fields set from meeting time" (bug 6); background.tex:272, "Registry grown [...] by reviewed expansion" (bug 5; see C17); conclusion.tex:171, "No contract has been implemented" (seven contracts are built at 3320375, four ran as A2; see C109); and eval.tex:932, which describes the ablation switch as resolver-only: "embedding-nearest state keys added to the candidate set of the state-key resolver" (eval.tex:932–933). Bug 8 says "the switch also turns off answer-time retrieval and the relevance gate" (22-bug-list.md:103).
  - *Options:* (a) add them to the P1-3 or P0 conformance fixes; (b) add them to the register as rows.
  - *Recommendation:* (a). They describe the system; they do not say where or why information is lost.
- **R-17. `thesis/discussion.tex`.** It is not `\include`d, and its header says its claims are not current.
  - *Options:* (a) exclude it; (b) sweep it as dormant.
  - *Recommendation:* (a). Sweep it only if it is restored.
- **R-18. Merging and one home per claim.** This assembly merged nine pairs that state the same claim with compatible tests. It kept other repeats apart with "Also stated at" (section 5).
  - *Options:* (a) as here; consolidate each section 5 group when the text actions are applied; (b) one row per location (no merges); (c) one row per section 5 group, which forces a single test on claims the sweeps tested differently.
  - *Recommendation:* (a). When the register is filled in, check that every listed location was edited.
- **R-19. The sweeps disagree on the recall clause of the embedding claim.**
  - *Context:* C03 (main.tex:73) and C124 (conclusion.tex:267) treat it as partly testable through (ii-r), (iii) and the offline checks. C71 (eval.tex:960) treats it as not testable, because probe (i)(b) cuts the extraction registry and is no test of the read-side embeddings.
  - *Gloss of the code:* at 3320375, `_prompt_registry` (app/services/state_key_resolution_service.py:676–705) leaves a registry of at most `resolver_prune_threshold` keys whole. A larger one is pruned to the embedding candidates (at most `embedding_top_k`=8 keys with similarity at least 0.30; l.641–643) plus keys that are lexically present or intent-primary. Probes (ii-r) and (iii) re-resolve with the unpruned registry. They can show that the prune excluded a fitting key, but not whether the embedding candidates or the lexical rule failed to keep it.
  - *Options:* (a) treat the recall clause as partly testable in all three rows, and limit the text to "no recall loss traced to the resolver's pruned shortlist on EL2020" or its reverse; (b) treat it as not testable anywhere, and leave the recall clause to P0-A.
  - *Recommendation:* (a). The test is real, but it bears on the shortlist as a whole, so the wording must not credit or blame the embedding candidates alone.
- **R-20. What a WD result means for the D10 claims.**
  - *Context:* C46, C110 and C118 treat (iv) holding as confirming that the missing whole-decision obligation causes the losses (coded implementation choice). C82 treats (iv) holding as overturning "This is the extraction contract of D10", and only an architectural code on D4.p5 as confirming. The text actions agree. If (iv) holds, the text says the evaluated extraction prompt lost the values and WD recovered X, with D10 marked retrospective. If WD and fresh A1 both carry a value in at most 1 of 3, with WD in 0, and the probes do not recover it, only D4.p5 may ground an architectural statement.
  - *Options:* (a) when filling in the register, split each D10 claim into a location-and-remedy part (confirmed by (iv)) and a design part (overturned by (iv); confirmed only by an architectural code on D4.p5); (b) leave the rows as written, since the text actions agree.
  - *Recommendation:* (a). "Confirmed" and "overturned" then mean the same thing in every row, which matters when the register reports how many claims held.
- **R-21. The decision tags of the "Shared failure" heading** (C130a, conclusion.tex:334). Added in the review of 27 October.
  - *Context:* the heading attributes to D4 and D8 a failure that RAG shares. The row is not testable here: list questions are outside the trace's unit, and RAG is not varied. The amendment allows a statement that a loss comes from the design "only where the codes say architectural or trade-off on 94c049d text" (amendment:572). R-15(a) leaves untestable text unchanged unless an independent fix applies.
  - *Options:* (a) keep the observation (conclusion.tex:336–337) and drop the D4 and D8 tags from the heading; (b) keep the tags, marked as untested.
  - *Recommendation:* (a). No code can ever support the tags in this study, and the observation needs no decision tag. It is consistent with R-5(a).
- **R-22. Does "D5.p3's equal-time eligibility" belong in R-4's list?** Added in the review of 27 October.
  - *Context:* R-4 lists it among 94c049d sentences that describe a later-found bug (bug 3). D5.p3 is the governing commitment: a challenger needs "a source time no earlier than the fact's validity start" (D5.p3), and the code's eligibility matches it. Bug 3 is about the current value's own claims, which do not compete; its repair leaves equal-time eligibility in place. Plan 23 decides only that "The current value's own claims compete, and an exact tie keeps the current value." (plan 23:221). The design-and-controls register tags D5.p3 as a commitment and lists it as quotable for architectural weakness on sheet S. C120's only route to confirmation quotes D5.p3.
  - *Options:* (a) remove "D5.p3's equal-time eligibility" from R-4's list; D5.p3 stays a design entry, as in the design-and-controls register; (b) keep R-4 as written, and change sheet S of the design-and-controls register and rows C17, C98 and C120 to match.
  - *Recommendation:* (a). In the bug list the defect is that "the current value's own claims never compete" (22-bug-list.md:43), and what bug 3 contradicts is the 5de9911 per-key sentence (22-bug-list.md:47), not D5.p3.

## 9. Mechanism mapping

What follows is the mechanism mapping, copied unchanged in substance from its Step 0 part. Its headings are moved down one level. Its own section numbers are kept, so "section 6.2" inside it means mapping section 6.2. One sentence about the builder's structured output is left out of its section 8. The review of 27 October changed it in these places, listed in section 10: Rule A's scope ("What this part fixes", item 2; section 3's account column; the complete-decisions note in section 6.1), the account of two state-maintenance sub-codes (section 3.1), the held-case consequence (section 6.2), decisions M-8, M-16 and M-19, and a new decision M-21. The completion pass of 27 October (section 10) added Rule M (mapping section 7a), renamed Rule V's items V1–V10 to the form Rule V item N, and changed M-17 and M-19. The review of the completion pass (section 10) changed Rule M, mapping section 7 (items 1, 3 and 4) and decisions M-4, M-19 and M-20. Its second review (section 10) changed Rule M, mapping section 7 (items 1, 3, 4 and 6, and a definition before item 3), the alternative in section 5, the citation in item 2 of "What this part fixes", and decisions M-19 and M-20. The signing rule is in section 1 above: "**The mapping signed here governs every Phase C verdict.** The Phase D3 registration may revise it for Phase D only, in a dated note." (amendment:114)

### Mechanism mapping (claims register, part)

Plan 23, amendment 1, Step 0. **Draft for signing** with the amendment. Built 27 October 2026, offline: no API calls; the only run output used is the frozen loss trace, which is listed under "Already read" (amendment:33–40). Rule M (section 7a, added 27 October) was written after the family results in `23-el2020-arms.md` had been read, and it read the key structure of rag_r1's report, with no values.

**Conventions.**
- Text in quotation marks is verbatim, cited as `path:line` or `commit:path:line`.
- "amendment" = `thesis/notes/thesis_completion/artifacts/23-plan-amendment-1-ceilings-and-root-cause.md`; "plan 23" = `…/23-plan-development-and-confirmation.md`; "codebook" = `…/23-loss-trace.md`; "script" = `…/23-loss-trace.py`; "design text" = `…/23-am1-design-text-94c049d.md` (paragraph ids such as D3.p5).
- Everything else is this draft's own wording. Where a sentence interprets a source, it is marked *(gloss)*.
- Points that need your judgement are marked **[decision M-n]** and listed in section 8.

**What the amendment asks for.** "It also carries the mapping from boundaries and sub-causes to the mechanisms (complete decisions, change and supersession, rejection, evidence and provenance, and each contract). **The mapping signed here governs every Phase C verdict.** The Phase D3 registration may revise it for Phase D only, in a dated note." (amendment:114)

**Inputs.**

| File | SHA-256 | Note |
|---|---|---|
| `23-loss-trace.json` | da4576242eda6fc181352eb8a4f74172c2961b187ca5e1b5391142c554c9e8a9 | matches the frozen-input table (amendment:71) |
| `23-loss-trace.py` | 4c12ccef9f7f788806b36eb8f71da25902cf755f8567c7be38f1fb052a52ffb1 | matches (amendment:69) |
| `data/ami_eval/suites/transfer_el2020.yaml` | 2361f17cdb14a64dbe77c99115bfddb3c3e615188799d632feb76fb59d8121d4 | matches (amendment:72) |
| `data/ami_eval/gold/reviewed/EL2020.reviewed.yaml` | 6b963af028fb6f318218a4bd0bca2d532e4db446b5a4f31d18f136b5bfdc0ac8 | matches (amendment:73) |
| amendment | 0236ef0385b96012d08e7bcd10a8ec71e436253cb58948d85da4ba563fb81889 | as read, unchanged |
| plan 23 | 1c8ec3a49ffa79c8f11e7297c892dcb3b20bb343b3a4dfe9c4ae82eb450d9881 | as read (working tree, uncommitted edits present) |
| codebook | d9a922f1822ea4ef0f97dd3eb28ee230a5492adb8a5ddbe3446118b8da0d1014 | |
| design text | b54e67f6b3fea3f54b1da3a3536f2059ce212a9632d34677640a770986262759 | |

Code was read at 3320375 (`git show`). `app/core/config.py`, `app/core/cycle2_flags.py`, `app/services/state_key_resolution_service.py` and `app/evaluation/ami/informed_reviewer.py` have no diff between 3320375 and the working tree.

**What this part fixes:**
1. **Rule V** (section 2): which cases and pass rows enter each mechanism's verdict and its bound. **Only Rule V governs verdict membership.** (Changed in the completion pass of 27 October, when Rule M was added: it said that Rule V governs verdicts.)
2. **Rule A** (section 3, last column, and section 4): to which mechanism a loss is attributed in the boundary account ("at which boundary their failures arise", plan 23:348). Rule A sets no verdict, and it is a location account only. The claims register's causal statements rest on Step 3 codes alone: "The trace gives the **location** of each loss, not its **cause**" (amendment:26), and "No loss becomes a design limit by default" (amendment:31). (Scope narrowed in the review of 27 October.)
3. Each contract's on/off contrast, endpoint, population and measured effect (section 6.2).
4. The rule for a case that touches more than one mechanism (section 5).
5. **Rule M** (section 7a): the *works*, *doesn't work* or *can't tell* rule for the architectural mechanisms, drafted for decision C43 on the decision sheet (added in the completion pass of 27 October).

Per-mechanism loss counts are deliberately **not** computed here, so the mapping is signed without a new view of outcomes. All population sizes below come from the suite and gold alone.

---

### 1. The mechanisms

Plan 23 lists them: "each contract in the final configuration;" (plan 23:342) and "the architecture's mechanisms for the conversational difficulties: epistemic status, change and supersession, rejection, restraint on incidental talk, complete decisions, evidence and provenance." (plan 23:343). It states how they are judged: "Switchable mechanisms are judged by an on/off contrast:" (plan 23:345) and "Architectural mechanisms are judged by their family endpoint against RAG. The loss trace shows at which boundary their failures arise." (plan 23:348).

| Mechanism | Type | Design text (94c049d paragraph ids) | Verdict form |
|---|---|---|---|
| Epistemic status (polarity, modality, lifecycle status) | architectural | D3.p2–D3.p5 | family endpoint against RAG |
| Change and supersession | architectural | D5.p2–D5.p6; D7.p2–D7.p6; D8.p5 (change answering) | family endpoint against RAG |
| Rejection | architectural | D3.p3 (negation sentences); D7.p4; D8.p4 | family endpoint against RAG |
| Complete decisions | architectural | No 94c049d decision of its own. The amendment names only "D4's scalar-concept passage" (amendment:355), i.e. D4.p5. D10 is retrospective (amendment:103). | family endpoint against RAG **[decision M-3]** |
| Evidence and provenance | architectural | D9.p2–D9.p6; D1.p4 | family endpoint against RAG |
| Restraint on incidental talk | **removed** | — | nothing is mapped to it |
| `filing_type_check` | A2 contract | "D10", "D4" (3320375:app/core/cycle2_flags.py:66) | on/off: leave-one-out in the A2 harness |
| `resolution_same_meeting_conflict` | A2 contract | "D5" (3320375:app/core/cycle2_flags.py:71) | on/off: leave-one-out in the A2 harness |
| `supersession_requires_new_evidence` | A2 contract | "D5", "D7" (3320375:app/core/cycle2_flags.py:76) | on/off: leave-one-out in the A2 harness |
| `filing_support_check` | A2 contract | "D9" (3320375:app/core/cycle2_flags.py:81) | on/off: leave-one-out in the A2 harness |
| WD (`extraction_whole_decisions`) | contract | "D10", "D4" (3320375:app/core/cycle2_flags.py:62) | on/off: Step 2c, WD against fresh A1 |
| Read contract (`answer_evidence_fallback`, `answer_answerability_check`) | contract | "D8", "D11" (3320375:app/core/cycle2_flags.py:51, :56) | **no Phase C contrast exists [decision M-1]** |

**Restraint on incidental talk.**
- It is removed by a Step 0 plan-23 fix: "remove "restraint on incidental talk" from the Phase D3 mechanisms;" (amendment:122).
- The removal was decided on 22 October: "**Bug 8:** decided 22 October: the restraint claim is dropped from the verdict list, so no per-component switches are built." (plan 23:229).
- **Nothing is mapped to it.** Its natural families map to no mechanism:
  - `noise_resistance` (8 questions, no gold rows);
  - `unknown` (10 questions, no gold rows). Plan 23 calls the unknown items' abstention "the same restraint behaviour that is now off the verdict list" (plan 23:116). **[decision M-4]**
- The loss-trace step most tied to admission, `admitted:ignored`, gets no account mechanism (section 3). Its cases still enter the verdicts of the families whose rows they cover (Rule V).

**Epistemic status and amendment:114.** The amendment's parenthesis lists "complete decisions, change and supersession, rejection, evidence and provenance, and each contract" and omits epistemic status. Plan 23:343 lists it, and only restraint is removed (amendment:122). This draft reads the parenthesis as non-exhaustive and maps epistemic status. **[decision M-2]**

**A1 repair switches** (the ten `repair_*` flags, 3320375:app/core/cycle2_flags.py:87–151) define arm A1. They are not mechanisms. Where a loss rests on one of them, it is a state-rule or conformance cause (section 4).

---

### 2. Rule V: which cases and passes enter which verdict

**Rule V item 1. Endpoint rows of an architectural mechanism.** Its endpoint is its question family against RAG (plan 23:348). Its endpoint rows are the gold rows those questions ask for, as the suite defines them. The family labels are the frozen suite's, unchanged.

| Mechanism | Suite family | Questions | Endpoint rows | Distinct values |
|---|---|---:|---:|---:|
| Complete decisions | `current_state` | 58 | 60 | 48 |
| Epistemic status | `candidate_decided` | 7 | 7 | 7 |
| Change and supersession | `change_over_time` | 3 | 24 | 24 |
| Rejection | `rejection` | 12 | 16 | 8 |
| Evidence and provenance | `evidence` | 7 | 7 | 4 |
| (none) | `unknown`, `noise_resistance` | 18 | 0 | 0 |

The pairing of families with mechanisms is this draft's proposal *(gloss: it follows the 94c049d text, which names "Status and unknown questions" for D3 (94c049d:thesis/implementation_chapter.tex:268), "Checkpoint and change questions" for D5 (94c049d:thesis/implementation_chapter.tex:366), and "evidence" / "questions partially test source identification" for D9 (94c049d:thesis/implementation_chapter.tex:575–576)).* See **[decisions M-3, M-5]** for the two weak pairings.

The question-to-row lists are taken from the loss trace's `questions` view, which is built from the suite and is identical in all nine runs (checked).

**Rule V item 2. Case coverage and membership.**
- A case is "one gold value in one run at each distinct loss step it reaches, taken at that step's earliest failing checkpoint, with its step and sub-code." (amendment:301)
- A case **covers** every row of its value, in its run, whose first loss is at the case's step *(gloss: this fixes which checkpoints a case stands for)*. **[decision M-14]**
- A case **belongs to** a mechanism when it covers at least one of that mechanism's endpoint rows.
- A pass row belongs to a mechanism when it is one of its endpoint rows.

**Rule V item 3. Step and sub-code do not decide verdict membership for an architectural mechanism.**
- Reason: a family endpoint is moved by a loss at any step on its rows. Plan 23 gives *can't tell* "when a known defect affects the mechanism." (plan 23:352).
- A mapping by boundary alone would leave, for example, an implementation defect in routing on a rejection row outside the rejection verdict, while that defect lowers the rejection family's score against RAG.
- The amendment's phrase "mapping from boundaries and sub-causes to the mechanisms" (amendment:114) is therefore met in two parts: Rule V maps by rows for verdicts, and Rule A maps boundaries and sub-causes for the account. **[decision M-6]**

**Rule V item 4. A case touching several mechanisms** is counted for each (section 5). **[decision M-7]**

**Rule V item 5. Contracts** take membership from their own endpoint rows and steps (section 6.2), not from the families.

**Rule V item 6. Measured effect.** "**Cases coded implementation because the mechanism under test is their alternative are that mechanism's measured effect.** They are left out of the shares, and never counted as recovered on the comparator side." (amendment:460). They are left out of **that** mechanism's shares only. They stay, with their codes, in every other population they belong to.

**Rule V item 7. Held cases.** "Such cases are coded **held: conflict decision.** They are scored as unclear in the agreement measures, and count as unclear in every bound." (amendment:359). This draft applies that in every population the case belongs to, including the conflict contract's own. **[decision M-8]**

**Rule V item 8. Known-bug incidence.** "Known-bug incidence enters both bounds the same way." (amendment:468). It enters a mechanism's bound through the gold rows that the loss trace's defect flags mark (codebook:63–70), under Rule V item 2. Incidence on facts that hold no gold value moves no endpoint; it is reported, not bounded. **[decision M-15]**

**Rule V item 9. New sub-causes from the pilot** ("the pilot may add new ones, but may not split or merge these", amendment:380) take membership by Rule V items 1–8 and their account by the boundary they name. They add no mechanism. Their mapping is recorded when the sub-cause list is frozen (Step 3, item 2), before pass 1.

**Rule V item 10. ES2009 (Step 3b, Step 5).** The same rules apply, with the adapter's row kinds and the ES2009 suite's families. The ES2009 pilot suite uses the same seven family names (`data/ami_eval/suites/pilot_es2009.yaml`, protocol `ami_milestone1@v7`). After B3 the suite version in force defines the endpoint rows.

---

### 3. Steps and sub-codes: what each one weakens, and to which mechanism it is attributed

**Columns.**
- *Occurs on*: row kind, then rows over the nine frozen runs / distinct values / arms. Source: `23-loss-trace.json`, strict series (the lenient series is identical, cell for cell).
- *Verdicts it can weaken (Rule V)*: by the covered rows. The kind-level result is:
  - **ruled_out rows**: rejection. All 16 are asked by rejection questions.
  - **current rows**: the families asking for the covered rows. On EL2020 these are complete decisions (60 rows), change and supersession (24), epistemic status (7) and evidence and provenance (7), with overlaps (section 5). **71 of the 133 current rows are asked by no question.** Their cases enter no architectural verdict; they do enter contract populations (section 6.2).
  - **demoted rows** (9): none. No question asks for a demoted row. They enter change and supersession's state account. **[decision M-9]**
  - **candidate row** (F36@b): none. No question asks for it. It enters epistemic status's state account.
- *Account (Rule A)*: the mechanism whose design acts at that step, for uncoded losses. This is a location account; it sets no cause, and the claims register's causal statements use Step 3 codes only. "Unattributed" means the sub-code does not identify the design element; only a coded case's caused-at and sub-cause attribute it (section 4). "None" means the step belongs to no listed mechanism. **[decision M-10]**
- *Contract or repair acting there*: informational. A contract's measured effect is set only by its own contrast (section 6.2), never by a sub-code.

#### 3.1 Pairs present in the frozen trace

| Boundary | Step:sub-code | Occurs on | Verdicts it can weaken (V) | Account (A) | Contract or repair acting there |
|---|---|---|---|---|---|
| extraction | `admitted:ignored` | current 39 / 2 / A0 A1 A2 | by row | none: admission (D2); restraint removed | — (candidate cause: the gatekeeper ignoring a span its own criteria admit) |
| extraction | `carried:claims_without_the_value` | current 242 / 25 / A0 A1 A2; ruled_out 9 / 3 / A0 A1 A2 | by row; ruled_out → rejection | complete decisions (current); rejection (ruled_out) | WD: its (iv) cases are WD's measured effect **[decision M-12]** |
| extraction | `carried:extracted_after_checkpoint` | current 4 / 1 / A0 A2 | by row | none: extraction timing | — |
| extraction | `carried:no_claims_from_cited_span` | current 12 / 2 / A0 A1 A2 | by row | none: capture (no listed mechanism) | — |
| extraction | `polarity:negated_value_read_as_rejection` | current 15 / 2 / A0 A1 A2 | by row | epistemic status (D3.p5: "Extraction can misclassify modality or" / "negation in either model", 94c049d:thesis/implementation_chapter.tex:264–265) | — |
| extraction | `polarity:carried_only_positive` | ruled_out 53 / 4 / A0 A1 A2 | rejection | rejection | — |
| extraction | `modality:carried_only_proposed` | current 75 / 11 / A0 A1 A2; ruled_out 18 / 1 / A0 A1 A2 | by row; ruled_out → rejection | epistemic status (current); rejection (ruled_out) | — |
| extraction | `modality:carried_only_hedged` | current 3 / 1 / A1 | by row | epistemic status | — |
| filing | `filed:cycle2_parked_unsupported_by_span` | current 42 / 13 / A2; ruled_out 10 / 2 / A2 | by row; ruled_out → rejection | evidence and provenance (D9) | `filing_support_check` |
| filing | `filed:cycle2_parked_no_fitting_key` | current 3 / 2 / A2 | by row | none: key model (D4) | `filing_type_check` |
| filing | `filed:no_key` | current 2 / 1 / A2; ruled_out 2 / 1 / A2 | by row; ruled_out → rejection | none: key model (D4.p3, parking) | — |
| filing | `filed:not_evaluated` | current 1 / 1 / A2; ruled_out 1 / 1 / A2 | by row; ruled_out → rejection | none | — |
| filing | `proposed:another_value_won` | current 116 / 26 / A0 A1 A2; candidate 4 / 1 / A0 A1 | by row; candidate → none | unattributed: misrouting (key model, D4) or a same-matter rival winning on D5's ranking | `filing_type_check`, `resolution_same_meeting_conflict`, `filing_support_check` (A2) |
| filing | `proposed:same_meeting_conflict` | current 110 / 28 / A2; candidate 1 / 1 / A2 | by row; candidate → none | change and supersession (D5; held cases: D5.p2) | `resolution_same_meeting_conflict`; held rule (amendment:357–360) |
| filing | `proposed:tie_left_as_conflict` | current 5 / 3 / A1 A2 | by row | change and supersession ("Different initial values tied on all three dimensions produce a conflict.", 94c049d:thesis/implementation_chapter.tex:342) | — |
| filing | `proposed:current_value_ranks_higher` | current 10 / 9 / A1 | by row | change and supersession (D5) | A1 repair, bug 3 (`repair_same_meeting_supersession`) |
| filing | `proposed:judged_same_as_current` | current 2 / 1 / A1 | by row | change and supersession (D5, supports branch) | — |
| filing | `proposed:outranked_dissent` | current 4 / 3 / A1 A2 | by row | change and supersession (D5.p4) | `supersession_requires_new_evidence` (A2) |
| filing | `proposed:own_value_not_matched` | current 4 / 4 / A0 A1; ruled_out 6 / 3 / A0 A1 A2 | by row; ruled_out → rejection | none: instrument (the wording pair goes to adjudication, codebook:39); evaluation-defect candidate | — |
| filing | `applied:proposal_expired` | current 28 / 5 / A1 A2 | by row | change and supersession (the settle re-evaluates keys under D5's policy; D6) *(gloss)* | A1 repair, bug 13 (`repair_settle_before_confirm`); in A2 "often a later same-meeting conflict" (codebook:192) |
| filing | `applied:proposal_pending_review` | ruled_out 2 / 1 / A2 | rejection | none: confirmation (D6) | A2 review gates |
| state maintenance | `current:overwritten_by_non_gold_value` | current 125 / 31 / A0 A1 A2 | by row | unattributed: misrouting (a rival of another matter filed under the key; the codebook notes it "usually means unrelated content was filed under the same key (wrong routing)" (codebook:195)) or a same-matter successor under D5's and D7's rules (changed from "change and supersession" in the review of 27 October) | `supersession_requires_new_evidence`, `filing_type_check` (A2) |
| state maintenance | `current:displaced_by_other_gold_value` | current 23 / 8 / A0 A1 A2 | by row | unattributed: two gold values on one misrouted key (for example F06 and F38), or a legitimate same-matter successor under D5's and D7's rules (changed from "change and supersession" in the review of 27 October) | as above |
| state maintenance | `current:still_current` | demoted 10 / 4 / A0 A2 | none (no question asks a demoted row) | change and supersession; also rejection for the no-successor values **[decision M-9]** | A1 repair, bug 1 (`repair_negation_affirmation`) |
| reading | `key_reached:other_keys_resolved` | current 53 / 16 / A0 A1 A2; ruled_out 9 / 3 / A0 A1 A2 | by row; ruled_out → rejection | none: reading (D8) | read contract |
| reading | `key_reached:no_key_resolved` | current 3 / 2 / A0 A1 A2; ruled_out 1 / 1 / A1 | by row; ruled_out → rejection | none: reading (D8) | read contract |
| reading | `in_payload:near_match_only` | current 5 / 3 / A0 A1 A2 | by row | none: reading (D8.p3, near matches) | read contract |
| reading | `answered:answer_or_judge` | current 16 / 5 / A0 A1 A2; ruled_out 2 / 2 / A1 | by row; ruled_out → rejection | none: answer generation or judge; evaluation-defect candidate | read contract |

**Pass outcomes** (they enter Rule V as pass rows; "passes that rest on a defect, or whose defect status is unclear" weaken, amendment:454):

| Outcome | Occurs on | Verdicts it can weaken (V) |
|---|---|---|
| `ok:None` (read and credited) | current 104 / 25; ruled_out 12 / 3 | by row |
| `ok:stored_not_asked` | current 151 / 26; ruled_out 19 / 3; candidate 4 / 1 | by row. Such a row has no single-value question at k, but it can still be asked by a multi-value question (`rejected_so_far`, `dates_current`, `change_over_time`). Otherwise none. |
| demoted `ok:demoted` | demoted 18 / 5 | none (state account: change and supersession) |
| demoted `ok:never_stored` | demoted 53 / 5 | none (state account). The amendment's own example of a pass resting on a defect is "a demoted row passing only because the value was never stored" (amendment:317). |

No `status` step fails anywhere in the frozen trace, so no `status:stored_as_<status>` pair is present.

#### 3.2 Pairs the script can emit that are absent on the frozen EL2020 runs

They are mapped now, because the 2c, C, A1′, leave-one-out and Step 5 runs may produce them. The emitting lines are in the script (`fail(...)` calls at script:825–989; reason prefixes at script:97–108; parking reasons at script:860–871).

| Step:sub-code | Verdicts (V) | Account (A) |
|---|---|---|
| `admitted:span_not_seen` | by row | none: provenance join or gold line; evaluation-defect candidate |
| `carried:sibling_value_only` | by row | complete decisions *(gloss: the decision is captured only as another row's value)* |
| `carried:split_across_claims` | by row | complete decisions |
| `polarity:carried_only_negative` (current) | by row | epistemic status |
| `modality:carried_only_<other modalities>` | by row; ruled_out → rejection | epistemic status (current, candidate); rejection (ruled_out) |
| `filed:undefined_key` | by row | none: key model (D4); A1 repair, bug 5 |
| `filed:cycle2_parked_<other reason>` | by row | the contract that parked it |
| `proposed:hedged_same_value` | by row | change and supersession; A1 repair, bug 4 |
| `proposed:hedged_negation` | by row | rejection (collection keys only; none on EL2020, codebook:196) |
| `proposed:no_positive_claim_left` | by row | rejection (D3.p3, negation branch) |
| `proposed:<raw result type>` | by row | unattributed |
| `applied:fact_not_found` | by row | none: projection (D6, D7); conformance candidate |
| `current:rejected` (current row) | by row | rejection (D7.p4: "Applying rejection can demote", 94c049d:thesis/implementation_chapter.tex:451) |
| `current:rejection_after_checkpoint` (ruled_out) | rejection | rejection |
| `current:not_current` | — | "cannot occur under the replay" (codebook:41) |
| `status:stored_as_<status>` | by row; ruled_out → rejection | epistemic status (lifecycle status, D3.p2) for current and candidate rows; rejection for ruled_out rows |
| `in_payload:key_resolved_fact_not_given` | by row | none: reading (D8) |

#### 3.3 The 94c049d decisions, for the account of coded cases

A case coded architectural weakness or design trade-off quotes a 94c049d paragraph (amendment:326–327). Its account goes to the mechanism of that paragraph:

| Decision | Account mechanism |
|---|---|
| D1 | evidence and provenance (D1.p4); otherwise the account of the case's caused-at boundary |
| D2 | none (admission; restraint removed) |
| D3 | epistemic status; its negation sentences (D3.p3) → rejection |
| D4 | none (key model), except D4.p5 → complete decisions |
| D5 | change and supersession; D5.p2 "leaving unresolved cases reviewable" (94c049d:thesis/implementation_chapter.tex:333) → held: conflict decision |
| D6 | none (proposal and confirmation) |
| D7 | change and supersession; D7.p4 → rejection |
| D8 | none (reading), except D8.p4 → rejection and D8.p5 → change and supersession |
| D9 | evidence and provenance |

---

### 4. Candidate implementation causes

The causes are the amendment's (amendment:382–388). "Surfaces at" is where a coded case with that cause can appear in the trace *(gloss)*. Rule V for every cause is "by the covered rows" (Rule V item 2); it is not repeated per row.

| Boundary | Candidate cause | Surfaces at | Account (A) | Measured effect of |
|---|---|---|---|---|
| Extraction | registry-conditioned extraction | `carried:*`, `polarity:*`, `modality:*` | complete decisions (`carried`); epistemic status (polarity, modality on current and candidate rows); rejection (ruled_out rows) | a (b) repair of this cause (Step 4) |
| Extraction | out-of-domain prompt examples | as above | as above | a (b) repair |
| Extraction | a modality or negation instruction missing from the prompt | `polarity:*`, `modality:*` | epistemic status; rejection (ruled_out rows) | a (b) repair; an (a) repair if the prompt contradicts the register |
| Extraction | the gatekeeper ignoring a span its own criteria admit | `admitted:ignored` | none (admission) | a (b) repair |
| Extraction | no whole-decision contract (WD rule only) | `carried:claims_without_the_value` | complete decisions | WD only: its (iv) cases (amendment:461). "This sub-cause is never eligible under Step 4(b) and takes no repair slot." (amendment:351) |
| Key assignment at extraction | a hint to a registered key about another matter | `filed:*`, `proposed:another_value_won`, `current:overwritten_by_non_gold_value`, `current:displaced_by_other_gold_value`, `key_reached:*` (through a misfiled rival) | none: key model (routing) | a (b) repair |
| Key assignment at extraction | registry-conditioned hinting | as above | none: routing | a (b) repair |
| Key resolution and expansion | the shortlist or prune excluded a fitting key | as above | none: routing | a (b) repair |
| Key resolution and expansion | the harness reviewer accepted a near-duplicate or over-broad key | as above | none: routing (the harness reviewer is an implementation entry) | a (b) repair |
| Key resolution and expansion | a reuse or similarity threshold merged a new matter into an existing key | as above | none: routing | a (b) repair |
| State rules | the settle expired a correct proposal | `applied:proposal_expired` | change and supersession | a state-logic repair (Step 4) |
| State rules | any state behaviour contradicting the register | `proposed:*`, `applied:*`, `current:*`, `status:*` | the mechanism of the register entry it contradicts | an (a) conformance repair (acceptance is admission, amendment:477) |
| Reading | the question-time shortlist excluded the holding key | `key_reached:*` | none: reading | a read-path repair (Step 4) |
| Reading | the scalar focus gate demoted a correct fact to a near match | `in_payload:near_match_only` | none: reading | a read-path repair |

**Non-implementation codes** (architectural, trade-off, conversational difficulty, evaluation defect, model-limited, design or model, not separated) take membership by Rule V like any case. They do not weaken a verdict. Their account follows section 3.3 (architectural, trade-off) or the caused-at boundary (the others).

**Routing and reading.** About a quarter to a third of rows surface as other values winning or overwriting (amendment:24), and reading losses are 9–11 rows per run (amendment:38). No listed mechanism owns routing or reading. Under Rule V these losses still weaken every family whose rows they cover. Under Rule A they are reported as "none: key model (D4)" and "none: reading (D8)". **[decision M-10]**

---

### 5. A case that touches more than one mechanism

**Proposal: counted for each.** A case or pass row enters the population, the shares and the bound of every mechanism it belongs to under Rule V.

**Reasons:**
- Plan 23 gives *can't tell* "when a known defect affects the mechanism" (plan 23:352). A defect on a row asked by two families affects both endpoints.
- The bound is a worst-case rule: "**Doesn't work** stands only if it still holds when the weakening losses are counted as recovered." (amendment:466). Counting a case for only one mechanism would leave the other endpoint unbounded against a defect that moves it.

**Exceptions:**
- Within one mechanism a case counts once, however many of its covered rows are endpoint rows.
- A measured-effect case is left out of that mechanism's shares only (Rule V item 6).

**Costs, disclosed:**
- Verdicts sharing cases are not independent. No claim of independence across mechanisms is made.
- More verdicts can come out *can't tell*.

**How much overlap there is on EL2020** (suite only): 31 of the 78 endpoint rows belong to two or three families.

| Families of the row | Rows |
|---|---:|
| complete decisions only | 29 |
| complete decisions + change and supersession | 20 |
| complete decisions + change and supersession + epistemic status | 4 |
| complete decisions + evidence and provenance | 5 |
| complete decisions + evidence and provenance + epistemic status | 1 |
| complete decisions + epistemic status | 1 |
| evidence and provenance only (F01@b) | 1 |
| epistemic status only (F66@c) | 1 |
| rejection only | 16 |

Every change and supersession endpoint row is also a complete decisions endpoint row.

**Alternative: primary only.** Each case goes to one mechanism by a fixed precedence: rejection, evidence and provenance, epistemic status, change and supersession, complete decisions (Rule M item 9; the order was given as an example until the second review of 27 October). Not recommended, for the reasons above. **[decision M-7]**

---

### 6. Endpoint populations

#### 6.1 Architectural mechanisms

For each: the question endpoint (the verdict, against RAG), the endpoint rows (Rule V), and the state account rows (PM only, reported beside the verdict; they enter no verdict under the proposal).

**Complete decisions** *(family `current_state`)* **[decision M-3]**
- Questions (58): the 46 `*_cs_F*` items; the 8 persist items (`EL2020c_persist_F01`–`F04`, `EL2020d_persist_F20`–`F23`); the 4 `*_dates_current` items (one value at a and b, three at c and d).
- Endpoint rows (60 over 48 values): F01@a,c; F02@a–d; F03@a,c; F04@a,c; F05, F06, F08–F12@a; F20–F23@b,d; F24–F31@b; F50, F53, F56–F65@c; F67@c,d; F69@c,d; F81–F86, F88, F89, F91–F93@d.
- State account: all 133 current rows *(gloss: the mechanism concerns every stated decision; 71 current rows are asked by no question)*.
- Note: this family's score reflects the whole chain for current values, not only completeness. The loss trace locates where its failures arise (plan 23:348). Location statements about completeness rest on Rule A (`carried:claims_without_the_value`, `split_across_claims`); causal statements rest on Step 3 codes and on the WD contrast (changed in the review of 27 October, with Rule A's scope).

**Epistemic status** *(family `candidate_decided`)*
- Questions (7): `EL2020a_yesno_F01`, `EL2020a_yesno_F02`, `EL2020b_yesno_F20`, `EL2020b_yesno_F24`, `EL2020c_yesno_F66`, `EL2020d_yesno_F82`, `EL2020d_yesno_F85`.
- Endpoint rows (7): F01@a, F02@a, F20@b, F24@b, F66@c, F82@d, F85@d.
- State account: these rows plus the candidate row F36@b (expected `current_unconfirmed`, codebook:24).
- Note: all seven expect `current_confirmed` (suite). No EL2020 status item can fail on a value that is only proposed; B3 plans "status items that can fail" (amendment:143). Until then this endpoint tests confirmed values only.

**Change and supersession** *(family `change_over_time`)* **[decision M-5]**
- Questions (3): `EL2020b_changed_since_previous`, `EL2020c_changed_since_previous`, `EL2020d_changed_since_previous`, eight values each.
- Endpoint rows (24): F20–F27@b; F50, F53, F56–F61@c; F81–F86, F88, F89@d. These are the values newly decided at each checkpoint, including the successors F58@c and F59@c.
- State account: the endpoint rows; the 9 demoted rows (F25@c,d; F27@c,d; F35@c,d; F36@c,d; F56@d); the unasked successor rows F58@d and F59@d.
- Note: three multi-value questions are a thin endpoint, and they test novelty more than supersession *(gloss)*. The 94c049d text names "Checkpoint and change questions" (94c049d:thesis/implementation_chapter.tex:366) and "Checkpoint recall and change accuracy" (94c049d:thesis/implementation_chapter.tex:468). The suite's checkpoint-recall items are the persist items, labelled `current_state`.

**Rejection** *(family `rejection`)*
- Questions (12): `EL2020{a..d}_rejected_so_far` (1, 2, 5 and 8 values); `EL2020a_rej_R01`, `EL2020b_rej_R02`, `EL2020c_rej_R03`–`R05`, `EL2020d_rej_R06`–`R08` (one value each).
- Endpoint rows (16): R01@a–d; R02@b–d; R03, R04, R05@c,d; R06, R07, R08@d.
- State account: the same rows, plus the no-successor demoted rows if **[decision M-9]** takes option (b).

**Evidence and provenance** *(family `evidence`)* **[decision M-11]**
- Questions (7): `EL2020a_evidence_F01`, `EL2020b_evidence_F01`, `EL2020b_evidence_F02`, `EL2020c_evidence_F01`, `EL2020c_evidence_F02`, `EL2020d_evidence_F20`, `EL2020d_evidence_F21`.
- Endpoint rows (7 over 4 values): F01@a,b,c; F02@b,c; F20@d; F21@d.
- Provenance outcome: the trace's question view records whether the value was stored, which meetings the stored fact cites, and whether one of them is the gold's meeting (codebook:72–75). A stored value citing the wrong meeting is not a loss-trace case.
- Known-bug link: bug 2 (`bug2_cites_span_without_value`, codebook:64) marks pass rows; it enters the bound under Rule V item 8.

#### 6.2 Contracts

**Each A2 contract** (`filing_type_check`, `resolution_same_meeting_conflict`, `supersession_requires_new_evidence`, `filing_support_check`)
- **Contrast:** A2 against A2 with that contract off. "**Leave-one-out:** each of the four contracts is switched off in turn." (amendment:223). It runs in the A2 harness, paired, on runs that pass the A2 gate (amendment:222, :515). "The contracts were tested in the A2 context only, with no one-contract-on variants over A1." (amendment:231)
- **Endpoint rows:** all 159 gold rows, at the status step (stored with the right status at k; for a demoted row, no longer current). *(Gloss: the harness does not re-run reading; the oracles' endpoint is likewise "stored with the right status at k", amendment:203.)*
- **Admission measures:** "switching the contract on gains at least 3 distinct values net in every gate-passing run;" (amendment:516); "no run is net negative;" (amendment:517); "parked or open-conflict rows do not increase among the values that at least 2 of 3 A1 runs store with the right status." (amendment:518). **[decision M-13]**
- **Population for the bound:** cases at the steps `filed` to `status`, all row kinds, in both variants. Extraction cases are left out on both sides, because the harness replays the same claims in both variants. **[decision M-16]**
- **Measured effect:** "for an A2 contract, the cases its leave-one-out recovers." (amendment:463) *(gloss: rows lost with the contract on that pass with it off)*. "**A2 cases:** a contract whose leave-one-out recovers the row sets caused-at to the state rules (that contract)." (amendment:376)
- **Shares:** "the A2 leave-one-out variants take A2's;" (amendment:458).
- **Where each contract shows in the trace** (descriptive only):
  - `filing_support_check`: `filed:cycle2_parked_unsupported_by_span`.
  - `filing_type_check`: `filed:cycle2_parked_no_fitting_key`, and re-routes logged only to `filing_type_check` (codebook:57).
  - `resolution_same_meeting_conflict`: `proposed:same_meeting_conflict`; in A2 also `applied:proposal_expired` (codebook:192).
  - `supersession_requires_new_evidence`: no sub-code of its own. It removes challengers resting on the current fact's evidence or meeting (3320375:app/services/resolution_service.py:274–279, `_eligible_challengers`). The loss then shows as `outranked_dissent` or a raw conflict result, or not at all.
- **Held cases:** an open same-meeting conflict case is held (Rule V item 7). It is unclear in the conflict contract's own bound too. **[decision M-8]**
- **Expected consequence, disclosed** (added in the review of 27 October). **[decision M-21]**
  - Under Rule V items 4 and 7 and M-16(a), the open same-meeting conflict cases enter all four A2 contracts' populations, and the leave-one-out variants borrow A2's shares (amendment:458).
  - Already read (27 October review, frozen trace, strict series): in the A2 runs, 17 of 33, 11 of 28 and 22 of 37 distinct value × step cases at `filed` to `status` are at `proposed:same_meeting_conflict` (none in A0 or A1). This is an upper indication of the held share, since held status follows caused-at (amendment:358), and some of these cases may be caused at routing. Routing cases coded implementation or unclear weaken too.
  - *Works* must also hold "when the comparator's weakening losses are counted as recovered" (amendment:467). A weakening share of this size, on a population of about 30 cases per run, would erase a margin of "at least 3 distinct values" (amendment:516). The same share on the on-variant blocks *doesn't work*.
  - So, while the conflict decision is open, every A2 contract is expected to come out *can't tell (defect-limited)* and not be admitted. Rows C32, C34, C47, C111, C120, C132 and C133 say so.

**WD**
- **Contrast:** "three A1 + `extraction_whole_decisions` runs, interleaved with three fresh A1 runs at the same commit, after the Step 0 instrument changes." (amendment:286)
- **Endpoint:** "current rows lost at `carried`, per run, in rows and distinct values." (amendment:288). Further conditions: filing losses, "no owner or role claim is lost;" (amendment:293), and no new incidence. **[decision M-17]**
- **Population for the bound:** current-row cases at `carried`, and current rows passing `carried`, in the six runs; filing-boundary cases (`filed`, `proposed`, `applied`) for the filing condition.
- **Measured effect:** "for WD, its (iv) cases;" (amendment:461). (iv) is defined at amendment:352.
- **Shares:** "the 2c, C and A1′ runs take A1's 3a shares;" (amendment:457).
- **If Step 2c is not run:** "Cases whose only named remedy is WD are coded unclear." (amendment:297). They then weaken every family their rows belong to.

**Read contract** (`answer_evidence_fallback`, `answer_answerability_check`) **[decision M-1]**
- **Contrast:** none in the amendment. Plan 23 asks to settle "whether the read contract (evidence fallback, answerability) is on." (plan 23:267), and says the partial batch R "cannot decide the read contract on its own." (plan 23:272). None of the EL2020 cycle-2 runs had it on (each run's `coldstart.json` config).
- **Population, if a contrast is defined:** the evidence fallback can answer any question from admitted evidence, so the population is every case on a row asked by a single-value question, at any step; the answerability check adds the `unknown` family as a secondary endpoint *(gloss)*.
- **Measured effect, if a contrast is defined:** the questions whose outcome changes between on and off.

**(b) repairs** (not mechanisms, but their admission uses the bounded verdict, amendment:512)
- Endpoint: "the rows of the distinct values coded with the cause, at its boundary, paired by value and checkpoint." (amendment:499).
- Measured effect: "for a (b) repair, the cases of the cause it repairs;" (amendment:462).

**Step 5 joint contract verdict** (final configuration against A1-ref, amendment:533–534): no endpoint is fixed. **[decision M-18]**

---

### 7. How the bound uses these populations (proposal)

The amendment fixes the bound (amendment:451–471) but not its arithmetic on a question endpoint. Proposed, **[decisions M-14, M-19, M-20]**:

1. **Shares.** For each mechanism and arm, the share of weakening cases among the sampled cases in its population, pooled over the arm's author-coded runs, with a bootstrap over values. The upper end of the 95% interval is used (amendment:456). Measured-effect cases are left out (Rule V item 6). *(Gloss: the sample is "the first 30 lost cases, in the order of sha256(run_id|fact_id|k), of each A1 and A2 run" (amendment:308); it is not stratified by mechanism, so a per-run share for a small family rests on very few cases.)* The bootstrap resamples values with replacement, with seed 23 and 50,000 draws. The upper end is the sorted draw at index int(0.975 × 50,000) − 1, as in `23-el2020-a0-a1.py` (lines 34–35 and 83). (Pinned in the review of the completion pass, 27 October.)
   - **The share's base** (added in the second review, 27 October). A case share's base is the cases of the mechanism's population among the 30 author-coded cases per run (amendment:308); for the shares that Step 5's runs borrow, among the cases of 3b's coded run, all of which 3b codes (amendment:312, :460). Pilot cases count toward nothing (amendment:310) and enter as uncoded. Fresh-sample cases (amendment:311) are outside the base, but those whose final code weakens are coded weakening cases and are taken first in item 3 (amendment:29).
   - **The bootstrap in full** (added in the second review, 27 October). The values are the distinct fact_ids that have at least one item in the share's base (a sampled case; for item 4's pass share, a sampled pass row in that share's base), sorted as strings. A fresh random.Random(23) is used for each share (mechanism × arm × kind, the kind being cases or pass rows). Each draw is [rng.choice(values) for _ in values], as at `23-el2020-a0-a1.py:80`. It pools every item in the base of each drawn value, over the runs the share comes from, once for each time the value is drawn (as the script scores a question drawn twice twice, `23-el2020-a0-a1.py:69`), and the draw's share is weakening items over all items. Shares and counts are computed in exact fractions (Python's `fractions.Fraction`) before rounding up. The script's fresh generator and sorted list are at `23-el2020-a0-a1.py:76` and `:122`.
2. **Count per run.** The number of weakening cases is the share's upper bound times the run's population, rounded up.

**Single- and multi-value questions** (items 3 and 4; added in the second review, 27 October). A question that asks exactly one row (one entry in its `rows` in the loss trace's `questions` view) is single-value, whatever its family. This includes an evidence question, whose row is given by its id suffix, as in the script's `question_map` (script:314–332). A question that asks two or more rows is multi-value. This is Rule M's definition, not the codebook's definition of the questions that reading is traced through (codebook:52).

3. **"Counted as recovered"** (the *doesn't work* bound):
   - every row the case covers passes the whole chain;
   - a single-value question asking such a row is scored correct;
   - a recorded-wrong multi-value question flips to correct exactly when at least one row it asks for is counted recovered, and every other row it asks for has outcome `ok:None` or `ok:stored_not_asked` or is counted recovered. Every other question keeps its recorded score.
   - Coded weakening cases are taken first: every coded weakening case of the run is taken, even where their number exceeds the count; the count is then their number and nothing is filled. Otherwise the rest of the count is filled in each run by a deterministic greedy rule at the question level. It repeatedly takes the recorded-wrong question of the mechanism's endpoint family that needs the fewest further uncoded cases to flip, given those already taken, with ties going to the lowest sha256(run_id|fact_id|k) among its cases, and takes those cases. A question that no uncoded cases can flip is skipped. When the count left is smaller than the next question needs, or no question is left, the rest is spent on the remaining uncoded cases in hash order, lowest first. The fill stops when the count is reached.
4. **"Counted as lost"** (the *works* bound): each question crediting a weakening pass row is scored wrong, single- or multi-value.
   - **Pass share.** For each mechanism and arm, the share of weakening rows among the pass rows of the mechanism's population in the 20% pass sample (seed 23, amendment:315), pooled over the arm's author-coded runs, with the bootstrap of item 1. A pass row weakens when it rests on a defect or its defect status is unclear (amendment:454). That is, a pass weakens when its implementation answer (amendment:317) is yes or unclear (added in the second review, 27 October). A recorded evaluation defect alone does not weaken; it goes through B3 (amendment:319). Rows examined in full, because their question is flagged `credit_without_state` or under decision C35 (b), weaken by their own codes and are left out of the share and of its base.
   - **Rows examined in full that the trace records as lost.** A row examined in full (its question flagged `credit_without_state`, or under decision C35 (b)) whose examination finds that it weakens counts as a weakening pass row in this bound, even when the trace records it as lost, since amendment:315 examines it as a pass. Each question crediting it is scored wrong. In the doesn't-work bound it stays a case.
   - **Count per run.** The share's upper bound times the run's other pass rows of the population (those not examined in full), rounded up. Examined weakening rows of the sample are taken first: every examined weakening sample row of the run is taken, even where their number exceeds the count; the count is then their number and nothing is filled. Otherwise the rest is filled by a greedy rule: it repeatedly takes an unexamined pass row on a recorded-correct question of the mechanism's endpoint family not yet scored wrong, ties by the lowest sha256(run_id|fact_id|k). When no such row is left, it takes the remaining unexamined pass rows in hash order. The fill stops when the count is reached.
   - Items 3 and 4 were completed in the review of the completion pass (27 October): the multi-value rule, the greedy fill, and the pass share with its count. The second review (27 October) added the definition of single- and multi-value questions above, the endpoint-family scope of both fills, the rule that every coded weakening case and every examined weakening sample row is taken, the pass test (implementation answer), and the rows examined in full that the trace records as lost.
5. **Contracts** have row endpoints, so rows are counted directly.
6. **RAG** has no case population. Its scores enter as recorded, under the gold that Rule M item 7 names for the verdict being computed (on EL2020 the frozen gold, amendment:96). B3 corrections apply to RAG as to every arm: "Corrections go through B3 and apply to every arm and to RAG." (amendment:319)

---

### 7a. Rule M: verdicts for the architectural mechanisms (drafted 27 October 2026 for C43)

Drafted for decision C43 option (a). If C43 is answered (b), this text moves unchanged into a dated note before the Step 3 reveal.

In Rule M, "decision Cn" and "decision An" are entries of the decision sheet (`23-am1-decisions.md`), not claims rows; claims rows are called rows.

**What it answers.** Plan 23 asks for "an endpoint and a pre-registered rule for *works*, *doesn't work* or *can't tell*" (plan 23:344). For the contracts it says "Write the rule down before the last development comparison." (plan 23:269); Rule M applies the same timing to the architectural mechanisms. For these mechanisms it says "Architectural mechanisms are judged by their family endpoint against RAG. The loss trace shows at which boundary their failures arise." (plan 23:348). The rest of this mapping fixes the populations (Rule V, section 6.1) and the bound arithmetic (section 7). Rule M adds the test and the verdict. Decision M-19 records the gap; decision C43 decides when the rule is fixed.

**Not blind, and when it is fixed.**
- The amendment "is **not blind.**" (amendment:15). Rule M was written after the EL2020 family-level results of the twelve cycle-2 runs (`23-el2020-arms.md`) and the items under "Already read" (amendment:33–63) had been read.
- So the recorded EL2020 verdicts (Rule M item 4), set under the frozen gold (item 7), can be computed from runs that were read before the rule existed. The bounded verdicts (Rule M item 5) depend on the Step 3 codes and on the Step 2, 2b and 2c outputs.
- When it is fixed depends on decision C43:
  - (a): it is signed with the package, "**before any Step 2, 2b or 2c output exists.**" (amendment:14). The Step 3 codes and the Step 2, 2b and 2c outputs that the bounded verdicts need do not exist yet; the frozen loss trace, whose defect flags enter the bound directly (item 5), does.
  - (b): it is fixed in a dated note before the Step 3 reveal. By then the Step 2, 2b and 2c outputs may exist in hashed files, unopened (amendment:411), and the blind codes of Step 3 items 4 and 5 may exist.
  - (c): it is fixed in a dated note before the Step 5 runs, after those outputs and the codes are open.
  - Under (b) and (c) the dated note carries this text unchanged and says what had been read by then (amendment:16).
- This draft computed and looked up no family-level or endpoint result. It read the key structure of one RAG run report (rag_r1), with no values, to check that the endpoint can be computed: each entry of `scorecard.scores` carries `family` and a boolean `correct`, as in the ProjectMemory reports that `23-el2020-arms.py` reads.
- Its one fixed number, an exact one-sided p of 1/20, follows from three runs per arm, as in the WD rule (amendment:290). The instrument range is computed later, from the runs compared.

**Scope.**
- The five architectural mechanisms of section 1: epistemic status, change and supersession, rejection, complete decisions, evidence and provenance.
- Restraint on incidental talk is removed (amendment:122). It gets no verdict.
- The contracts are outside Rule M. WD keeps the Step 2c rule, and each A2 contract the leave-one-out admission rule. The read contract has no Phase C contrast (decision A5). Rule M changes nothing fixed for them.
- Rule M is part of the mapping. "The Phase D3 registration may revise it for Phase D only, in a dated note." (amendment:114). No such revision changes a Phase C verdict.

**Rule M item 1. Which comparisons get a verdict.** Each compares one configuration under test, X, with RAG, on one series, with both arms run in the same period. Every verdict is a development verdict: "Development results claim nothing beyond development." (plan 23:260).
- **EL2020: A1 against RAG,** on the twelve cycle-2 runs of the run manifest (amendment:75–90). X is the A1 smoke run, a1_r2 and a1_r3. RAG is rag_r1, rag_r2 and rag_r3. This is the only EL2020 set with RAG in the same period. The 2c, C and A1′ runs have no same-period RAG and get no Rule M verdict.
- **ES2009, Step 5: the final configuration against RAG,** three runs each, in the same period (amendment:531–536). Where no contract is admitted, the final configuration is A1-ref. Where the two differ, Rule M is also applied to A1-ref and both verdicts are reported; the final configuration's is the mechanism's ES2009 verdict. If the final configuration has no Step 5 runs, A1-ref's verdict is the ES2009 verdict, and this is disclosed. That happens, for example, when the only admitted contract is the conflict contract: "it waits for the conflict decision" (amendment:534). There is then no 3b coded run; A1-ref's shares are then 1 under item 5's gap rule, and this is disclosed (added in the second review, 27 October).
- **A later same-period comparison** of the final configuration against RAG in Phase C, such as the dress rehearsal (plan 23:271), applies Rule M unchanged. Its runs borrow shares within their series: on ES2009 the shares of 3b's coded run, as Step 5's runs do (amendment:460); on EL2020 A1's 3a shares, as the C and A1′ runs do (amendment:457). This is Rule M's own extension: amendment:456–460 does not name these runs.
- **No verdict** for A0 or A2. A0's results are defect-limited. "A0 enters no admission verdict." (amendment:309) concerns admission only; extending it to Rule M is Rule M's choice. A2 is the contracts' arm. Their family scores are reported as context.
- **Series are never pooled.** Each series gives its own verdict, and one never overrides the other. On ES2009, "Agreement with EL2020 is a consistency check, not a replication." (amendment:164).
- **The series verdict.** Every comparison's recorded and bounded verdicts are reported. A series' verdict is that of A1 on EL2020 and of the final configuration in Step 5 on ES2009 (or A1-ref's, as above). A later same-series comparison is reported beside it and never replaces it.
- **Computed once.** Each verdict is computed once, from the final codes (Step 3, item 8) of the coding its shares come from (item 5), and is not recomputed. On EL2020 these are the final 3a codes, which precede Step 4. With the reading of "repaired" in item 5, no Step 4 decision can move the EL2020 verdict.

**Rule M item 2. The endpoint.**
- For each mechanism, the endpoint is its question family (Rule V item 1). Section 6.1 lists the questions and rows. Rule M adds no endpoint.
- The per-run measure is the number of the family's questions scored correct: the scorecard's `correct` (prose layer), as `23-el2020-arms.py` reads it. A family question with no scored answer in a counted run counts as not correct. RAG has no state layer, so the state layer is not used.
- For a gold other than the one a run was scored under, the count is that run's prose `correct` from the B3 rescoring output (amendment:150–152).
- All counted runs of a comparison use the same questions. "Comparisons across suite versions use the common items." (amendment:152).

| Mechanism | Endpoint (Rule V item 1) | Questions (frozen EL2020 suite) | Rests on | Under the alternatives |
|---|---|---:|---|---|
| Complete decisions | `current_state` family | 58 | decision C28 (a) | (b): the subset classified from the gold text alone, committed with the package or, if Rule M is not signed with the package (decision C43 (b) or (c)), before any Step 2, 2b or 2c output exists (M-3), and disclosed as made after the EL2020 results were read. (c): no Rule M verdict; WD's Step 2c rule is its only test. |
| Epistemic status | `candidate_decided` family | 7 | decisions A6 and C29 (a) | C29 (b): the 10 `unknown` questions join the count (17 questions); see Rule M item 7. (b) is chosen after the unknown family's EL2020 outcomes were read (23-el2020-arms.md:33), and those questions cannot be bounded (item 7). |
| Change and supersession | `change_over_time` family | 3 | decision C30 (a), with (c) reported beside it | (b): the 8 persist items join (11 questions), and their rows join the bound population. (c) inside the verdict: see Rule M item 7. |
| Rejection | `rejection` family | 12 | no open decision | — |
| Evidence and provenance | `evidence` family | 7 | no open decision on the endpoint; decision C35 (b) for its passes | C35 (a): no added examination of evidence pass rows. A wrong-meeting value then weakens only through the 20% pass sample: if its pass row is sampled and coded as resting on a defect, or through the pass share (section 7, item 4). |

**Rule M item 3. Counted runs.**
- A run counts when its report is valid and its switches match its arm, as `23-el2020-arms.py` checks.
- A run that ended without a valid report, or with switches that do not match its arm, is replaced once, by a re-run in the same period, which counts in its place. Both are named. A run that counts is never replaced or dropped.
- On EL2020, a2_r2 crashed and a2_r2b counts in its place, as in the run manifest (amendment:86). A2 gets no Rule M verdict, so this bears only on the context.
- If the re-run also fails, the arm has fewer counted runs. Rule M item 4 then uses the runs it has, and its exact p rises.
- This item is for Phase C only. In Phase D, plan 23 sets the default for failures other than infrastructure: "The default: such a run is reported, not re-run, and counted as a failure." (plan 23:363).

**Rule M item 4. The test on the recorded outcomes.** Write x for X's per-run counts (n counted runs) and r for RAG's (m counted runs), on one endpoint.
- **Instrument range (IR).** The larger of the two within-arm ranges on that endpoint, in that comparison. A within-arm range is the highest count minus the lowest, over the arm's counted runs.
  - It is computed from the recorded counts, after the runs exist. It is never carried to another series, period or endpoint. So it is per series, as the cycle-1 ranges were (plan 23:361), and per comparison.
  - Unlike the WD rule, whose margins are fixed numbers from runs already read (amendment:40, :291–292), IR here is computed after the runs, from the compared arms. It measures run-to-run spread, not the judge or a reading.
  - Cycle 1's ranges measured how three readings moved a series' main contrast. No second reading exists for these families in Phase C, and "The cycle-1 ranges were per series (ES2009 14.4 points, EL2020 0) and do not transfer." (plan 23:361).
- ***Works:*** both of these hold.
  1. Every x is strictly greater than every r. The exact one-sided permutation p of this ordering is 1/C(n+m, n): 1/20 at three runs per arm, 1/252 at five. This p must be at most 1/20.
  2. The mean of x exceeds the mean of r by more than IR.
- ***Doesn't work:*** the mirror. Every x is strictly smaller than every r, with p at most 1/20, and the mean of r exceeds the mean of x by more than IR.
- ***Can't tell (within the instrument range):*** otherwise. This is how Rule M decides that the effect lies "within the instrument range" (plan 23:351): it does, unless *works* or *doesn't work* holds. That covers:
  - any tie or overlap between a run of X and a run of RAG;
  - equal means, or a mean difference of at most IR;
  - too few counted runs for p ≤ 1/20 (against three runs, fewer than three: two against three give 1/10);
  - an endpoint with no questions in the suite version in force (every count is 0).
- *Works* and *doesn't work* cannot both hold, so exactly one verdict results.

**Rule M item 5. The bound: the known-defect clause, in both directions.**
- Plan 23 gives *can't tell* "when a known defect affects the mechanism. This cuts both ways" (plan 23:352). Whether a mechanism is affected "is decided by a rule fixed here, from the incidence checks and the attribution coding" (plan 23:354). Rule M's rule is the amendment's bound rule (amendment:451–471), applied to item 4.
- **The mechanical test.** A known defect affects the mechanism exactly when its recorded verdict (item 4) is *works* or *doesn't work* and does not survive the bound below. The verdict is then *can't tell (defect-limited)*. A recorded *can't tell* stays as it is: the bound never turns it into *works* or *doesn't work*.
- **What weakens,** within the mechanism's population under Rule V (items 2, 4, 6, 7 and 8):
  - from the attribution coding: implementation cases, including those whose cause a later repair addresses (see below); unclear cases, including "an unclear caused-at, and coder disagreement on implementation versus not" (amendment:361), and held cases, which "count as unclear in every bound" (amendment:359); passes that rest on a defect, or whose defect status is unclear;
  - from the incidence checks: endpoint rows that carry a loss-trace defect flag (codebook:63–70) in a counted run of X (Rule V item 8). A lost flagged row is a weakening loss; a passing flagged row is a weakening pass. They are counted directly in every counted run of X, not scaled. "Known-bug incidence enters both bounds the same way." (amendment:468)
  - Flagged rows and the scaled count: flagged rows are applied first, as rows, and each row counts at most once in a bound. A case or pass row whose endpoint rows are all flagged leaves the uncoded pool. The share's count (section 7, items 2 and 4) is then filled from the rest of the pool, with the population unchanged.
  - Incidence on facts that hold no gold value is reported, not bounded, under decision C38 (a).
  - Other incidence counts (plan 23:261), such as bug 12's, which the loss trace does not flag, reach the bound only through the Step 3 codes of the cases they cause.
  - Under decision C35 (b), every examined evidence pass row coded as resting on a provenance defect is a weakening pass.
- **A later repair does not exempt a case.** A case weakens as an unrepaired implementation case even when a later repair addresses its cause: no counted run of X carried a repair that changed its own loss. On EL2020 the counted A1 runs carry no Step 4 repair; on ES2009 a loss in a run with the repair on was not repaired by it. Rule M thus reads the end state "Repaired" (amendment:27) as a state of the cause, which does not change the losses of X's counted runs. This applies the known-defect clause (plan 23:352) to the runs being judged.
- **What does not weaken:** cases coded architectural weakness, design trade-off, conversational difficulty, evaluation defect, model-limited, or design or model, not separated (section 4); examined passes whose implementation answer is no, whatever evaluation defect is recorded (section 7, item 4; added in the second review, 27 October).
- **The two bounds** (amendment:466–467), each applied to X's counts:
  - *Doesn't work* stands only if item 4's *doesn't work* test still holds when X's weakening losses are counted as recovered (section 7, item 3).
  - *Works* stands only if item 4's *works* test still holds when X's weakening passes are counted as lost (section 7, item 4).
  - In both, RAG's counts and IR stay as recorded. RAG has no case population (section 7, item 6). Rule M is not an on/off contrast, so the clause on "the comparator's weakening losses" (amendment:467) does not apply.
- **The arithmetic** is section 7's, as decision C44 settles it. Uncoded cases enter "through their arm's sample shares" (amendment:26), taken at "the upper end of its 95% bootstrap interval" (amendment:456). On EL2020, A1's own 3a shares apply. In Step 5 the runs take "the shares of 3b's coded run" (amendment:460). Section 7 fixes the bootstrap, the pass share, the fill for both bounds and the multi-value rule (items 1, 3 and 4). One gap is filled here:
  - where a share's base (section 7, item 1 for cases; item 4 for pass rows, rows examined in full not counting) is empty in the run or runs the share comes from (item 1; amendment:456–460), while the mechanism's population in the run being bounded has uncoded cases or unexamined pass rows of that kind, that share is 1. The gap is judged on the runs the share comes from, not on the arm being judged, so a borrowing arm takes the borrowed share. If every item in a share's base is clean, even a single one, the bootstrap's upper end is 0, so the share drops from 1 to 0 with the first clean item in its base. This is listed among the choices; decision M-20 offers a floor. (Keyed on the share's base and its source runs in the second review, 27 October.)
- **Inputs.** Rows, cases, pass rows and flags come from the loss trace's primary series (codebook:155): under v1 on EL2020, the frozen input (amendment:70), and under the ES2009 adjudication file on ES2009 (amendment:171). A case re-coded at Step 3 item 8 because its row result differs under v2 enters by its final code.
- **A bounded verdict needs the loss trace** (primary series) for every counted run of X. Without it the bounded verdict is *can't tell (defect-limited)*.
- **Both verdicts are reported.** "**The bounded one counts, including for admission.** It is the dry run of the rule the registration carries into Phase D3." (amendment:471). Through the bound, Rule M reads plan 23's rule "A failure coded as an implementation defect makes its mechanism *can't tell*." (plan 23:358) as the amendment does (amendment:26, :451–471): an implementation-coded failure makes the mechanism *can't tell* only when the verdict does not survive the bound.

**Rule M item 6. Unclear and design-or-model cases.**
- Unclear cases, held cases and coder disagreements weaken the doesn't-work bound (item 5); passes whose defect status is unclear weaken the works bound. A definite verdict that does not survive them becomes *can't tell (defect-limited)*.
- Cases coded design or model, not separated do not weaken, and a verdict may stand on them. Their count on the endpoint rows is reported beside the verdict. They are "Never cited as a design limit or as model-limited" (amendment:331).
- So *doesn't work* states only that X scored below RAG on that endpoint, beyond the instrument range and the bound. A statement that the loss comes from the design needs the codes: it is "made only where the codes say architectural or trade-off on 94c049d text" (amendment:572). The 0.40 rule (amendment:430) limits such statements; it does not change a Rule M verdict.

**Rule M item 7. Gold versions, empty populations and unasked rows.**
- **Two gold versions.** "Steps 2–4 use the frozen EL2020 suite and gold. Post-B3 scores are reported beside them." (amendment:96).
  - On EL2020 the verdict, recorded and bounded, is set under the frozen gold only. The recorded verdict under the post-B3 gold is reported beside it and changes nothing. (The EL2020 B3 decisions are taken after the EL2020 comparisons were read, amendment:155.)
  - Where B3 precedes the runs (ES2009 Step 5 and any later comparison) and a comparison is scored under both an old and a new gold, item 4 is applied under each. If the two recorded verdicts differ, the verdict is *can't tell (defect-limited)*: a gold defect known through B3 then decides it. If they agree, the bound (item 5) is applied under the gold that the loss trace and the Step 3 codes use, the new gold on ES2009 (amendment:173). Both recorded verdicts are reported.
- **The unknown family (decision C29).** Under (a) it maps to no mechanism and gets no verdict. Under (b) its 10 questions join epistemic status's count. They have no gold rows, so no case, pass row or flag can weaken them, and the bound never moves them. This is disclosed beside the verdict.
- **An empty bound population** (no weakening case, pass row or flagged row): the bounded verdict equals the recorded one.
- **An empty endpoint:** *can't tell (within the instrument range)*, by item 4.
- **Rows no question asks** (the demoted rows, the candidate row F36@b, the 71 unasked current rows): RAG has no answer on them, so they enter no comparison. They stay in the state account beside the verdict. If decision C30 or C33 is answered (c) with a state endpoint inside the verdict, Rule M has no comparator for it. Its rule is then fixed with Rule M (decision C43). If none is fixed then, the state endpoint is reported beside the family verdict and enters none.

**Rule M item 8. Reported beside each verdict.**
- both arms' per-run counts, IR and the exact p;
- the recorded and the bounded verdicts, with the weakening counts by kind;
- the count of design-or-model-not-separated cases on the endpoint rows;
- the family difference with its question-resampled interval, as context only: "Per-family differences are context for the verdicts." (plan 23:355), and "Intervals come from resampling questions or meetings, not from three repeat clusters." (plan 23:360);
- the Rule A account of the endpoint rows' first losses by boundary, which sets no verdict.

Verdicts share cases (section 5), so they are not independent.

**For claims rows,** a mechanism's verdict on a series is its bounded series verdict (item 1): A1's on EL2020; the final configuration's on ES2009, or A1-ref's where item 1 says so. A row reads the verdict of the series its claim is about. A row about both series reads both, and a *can't tell* branch of the row applies when either verdict is the *can't tell* that the branch names.

**Rule M item 9. Under the alternatives of the decisions it uses.** Item 2 gives the endpoint decisions (decisions C28, C29, C30 and C35). The others:
- Decisions C31 (b), C32 (b) or C37 (b) change the populations only; items 4 to 7 are unchanged. Under C31 (b), a routing or reading defect on a family's rows no longer weakens its verdict.
  - Under C31 (b), a coded case joins the mechanism of its caused-at and sub-cause (section 4). An uncoded case joins the mechanism in section 3's account column; where that column marks the step unattributed or none, it joins no mechanism, as the sentence above on routing and reading defects implies.
  - Under C32 (b), the precedence is exactly section 5's order: rejection, evidence and provenance, epistemic status, change and supersession, complete decisions.
  - (Both sub-items added in the second review, 27 October.)
- Decision C33 (c): item 7.
- Decision C34: any answer changes the account only.
- Decision C38 (b): any incidence on facts holding no gold value, in a counted run of X, makes each mechanism of that bug *can't tell (defect-limited)*. The mechanisms are fixed now, for each bug of `22-bug-list.md` section A (bugs in the evaluated system, 22-bug-list.md:10) that the incidence checks count (plan 23:261), and a bug counts for every mechanism listed. A decision that `22-bug-list.md` names without a paragraph gives its decision-level mechanism in section 3.3.
  - bug 1 (D3 and D5, 22-bug-list.md:16): epistemic status (D3); rejection, because bug 1 concerns D3.p3's negation sentences; change and supersession (D5);
  - bug 2 (D9, 22-bug-list.md:30): evidence and provenance;
  - bug 3: the bug list names "Chapter 4's D5" (22-bug-list.md:47), but the sentence it quotes is 5de9911 text, not 94c049d text (decision R-22). Chosen here: change and supersession, D5's decision-level mechanism;
  - bug 4 (no decision named, 22-bug-list.md:53–58). Chosen here: change and supersession, because its flag marks a supersession by the same value (codebook:66);
  - bug 5 (D4, 22-bug-list.md:62): none (key model);
  - bug 6 (D7, 22-bug-list.md:68): change and supersession;
  - bugs 12 and 13 (D6, 22-bug-list.md:78, :87): none (proposal and confirmation).
- Decision C44 (b) or (c) change the bounded counts only. Under (c) the counts can be fractional. C44 (c) can be chosen only if its fill, including how a fractional recovery scores a question, is written into section 7 when Rule M is fixed (with the package under C43 (a), in the same dated note under (b) or (c)). (Changed in the second review, 27 October.)
- Decision C43 (b): this text moves unchanged into a dated note before the Step 3 reveal. C43 (c): the same text, in a dated note before the Step 5 runs; the note then states that the codes and the Step 2 to 2c outputs were open (amendment:16).
- Rule M does not use decisions C27, C36 or C39 to C42.

**Choices made in this draft.** Neither the amendment nor plan 23 fixes Rule M's test (item 4) or the choices below; answering decision C43 adopts them (under (b) or (c), in the later dated note). Choice 12 is in mapping section 7, so it is also decision C44's. The completion pass listed six choices; the review of the completion pass (27 October) extended the list to fifteen. The second review (27 October) widened choices 11, 12 and 15 and kept the count at fifteen.
1. The comparisons that get a verdict (item 1): A1 against RAG on EL2020, and the final configuration against RAG in Step 5. None for A0, A2, or the 2c, C and A1′ runs. Amendment:309 excludes A0 from admission verdicts only.
2. The series verdict (item 1): A1's on EL2020; on ES2009 the final configuration's, with A1-ref's reported beside it where they differ, and A1-ref's where the final configuration has no Step 5 runs. A later same-series comparison is reported beside it and never replaces it.
3. The dress rehearsal and its shares (item 1): shares borrowed within the series, which amendment:456–460 does not cover.
4. A family question with no scored answer counts as not correct (item 2).
5. One replacement for a run without a valid report, or with switches that do not match its arm (item 3).
6. The test form (item 4): every run of X strictly above (or below) every RAG run, an exact one-sided p of at most 1/20, and a mean difference larger than IR. Plan 23 asks only for "a pre-registered rule" (plan 23:344).
7. IR as the run-to-run range of the two compared arms, computed after the runs and kept as recorded in the bound (items 4 and 5). It was chosen after the EL2020 family results were read. IR from every same-period arm would be at least as large, and would give more *can't tell*.
8. The reading of the end state "Repaired" (amendment:27) in item 5: a later repair does not exempt a case of X's counted runs. With it, each verdict is computed once, from the final codes (item 1).
9. Flagged rows (item 5): counted directly and first, each row once, and an item whose endpoint rows are all flagged leaves the uncoded pool.
10. The inputs (item 5): the loss trace's primary series, under v1 on EL2020. A bounded verdict needs the loss trace for every counted run.
11. Share 1 where a share's base is empty in the run or runs the share comes from (item 5), and the drop to 0 with the first clean item in the base. Where the final configuration has no Step 5 runs, this gives A1-ref share 1 (item 1). Decision M-20 offers a floor as option (d).
12. In mapping section 7: the pinned bootstrap, with its values, draw, statistic and exact arithmetic, and the share's base (item 1: pilot cases uncoded; fresh-sample cases outside the base but taken first when they weaken); the definition of single- and multi-value questions; the multi-value rule and the greedy fill for the doesn't-work bound, within the mechanism's endpoint family, with every coded weakening case taken (item 3); the pass share, its count and its fill for the works bound, the pass test (implementation answer yes or unclear), and rows examined in full that weaken, counted as weakening passes even when the trace records them as lost (item 4).
13. The two-gold rule, narrowed (item 7): on EL2020 the frozen gold sets the verdict. Where B3 precedes the runs, recorded verdicts that differ between the two golds give *can't tell (defect-limited)*, and the bound uses the gold of the loss trace and the codes.
14. The default for a state endpoint under decision C30 (c) or C33 (c) (item 7): its rule is fixed with Rule M, or it enters no verdict.
15. The readings under the alternatives (item 9): the bug-to-mechanism list under decision C38 (b), for the bugs in the evaluated system, with the choices for bugs 1, 3 and 4; under C31 (b), the membership of uncoded cases by section 3's account column; under C32 (b), section 5's order as the precedence; and the condition on choosing C44 (c).

---

### 8. Gaps and decisions for you

Each item gives the options and a recommendation.

- **M-1. Read contract has no Phase C contrast.** Options: (a) state that it has no development verdict and is not admitted ("**Only *works* is admitted.**", amendment:522); (b) add, by a dated note before Step 4, a paired answer replay (state_first, read contract on against off) on the A1 dumps, at about the read-path screen's cost (amendment:497). Recommendation: (a) for this package; (b) only if you want the read contract in the final configuration.
- **M-2. Epistemic status missing from amendment:114.** Options: (a) map it, reading the parenthesis as non-exhaustive; (b) drop it from Phase C verdicts. Recommendation: (a).
- **M-3. Complete decisions has no family of its own.** Options: (a) the `current_state` family, as proposed; (b) the `current_state` questions whose gold value has two or more independent parts, classified from the gold text alone before any further output; (c) no architectural verdict, only the WD contrast. Recommendation: (a), because it uses the frozen suite labels and needs no new judgement after the EL2020 results were read; disclose that it measures the whole chain for current values.
- **M-4. The `unknown` family.** Options: (a) no mechanism, following plan 23:116; (b) epistemic status, following D3.p5 ("Status and unknown questions directly target", 94c049d:thesis/implementation_chapter.tex:268). It has no gold rows, so no case can bound it either way. Recommendation: (a). (b) would be chosen after the unknown family's EL2020 outcomes were read (23-el2020-arms.md:33), and those questions cannot be bounded (Rule M item 7). (Added in the review of the completion pass, 27 October.)
- **M-5. Change and supersession's endpoint is three multi-value questions.** Options: (a) `change_over_time` only; (b) add the 8 persist items, which the 94c049d text calls checkpoint recall; (c) add a PM-only state endpoint (demoted rows no longer current, successor rows stored). Recommendation: (a) with (c) reported beside it, not entering the verdict. Moving persist items between families after their outcomes were read is open to the charge of steering.
- **M-6. Verdict membership by rows, not by boundary.** The amendment's wording suggests boundary-based membership. Options: (a) Rule V by rows plus Rule A by boundary, as proposed; (b) membership by boundary and sub-cause. Recommendation: (a). Under (b) a routing or reading defect on a family's rows would not limit that family's verdict.
- **M-7. Several mechanisms.** Options: (a) counted for each; (b) primary only, by fixed precedence. Recommendation: (a).
- **M-8. Held cases in the conflict contract's own bound.** Amendment:359 says held cases count as unclear "in every bound"; amendment:463 makes leave-one-out-recovered cases the contract's measured effect, left out of its shares. Options: (a) held wins everywhere, including the contract's own bound; (b) measured effect wins for the conflict contract only. Recommendation: (a), the literal and more specific rule, consistent with the open conflict decision. Consequence (added in the review of 27 October): held cases are in all four A2 contracts' populations (Rule V item 4, M-16), so while the conflict decision is open the A2 contracts are expected to come out *can't tell*, not only the conflict contract (section 6.2; decision M-21).
- **M-9. Demoted and candidate rows are asked by no question.** Options: (a) state account only; (b) also map the no-successor demoted values (F27, F35, F56: their pass needs a negation of the current value) to rejection's state account; (c) let state endpoints enter the verdicts. Recommendation: (a) plus (b) for the account; not (c), because RAG has no answer on unasked rows.
- **M-10. Routing and reading belong to no listed mechanism.** Options: (a) report them as "none: key model (D4)" and "none: reading (D8)" in the account; (b) ask the Phase D3 registration to add them as mechanisms (plan 23 allows revision "for Phase D only, in a dated note", amendment:114). Recommendation: (a) for Phase C; consider (b) for Phase D.
- **M-11. Provenance failures are not cases.** A stored value citing the wrong meeting is not a loss-trace case, so it can weaken evidence and provenance only as a pass (Rule M item 2). Options: (a) accept and disclose; (b) fixed at signing (decision C35), examine every evidence-question row that passes the status step as a pass examination. Recommendation: (b); it is 7 rows per run.
- **M-12. WD's (iv) cases on non-current rows.** Amendment:350 names only the sub-code; the 2c endpoint counts current rows. 9 ruled_out rows (3 values) carry `carried:claims_without_the_value`. Options: (a) (iv) applies to every case with the sub-code, while the 2c endpoint stays current rows; (b) (iv) applies to current rows only. Recommendation: (a), with ruled_out (iv) cases listed apart.
- **M-13. "Distinct values net" is undefined.** Options: (a) per run, values with more status-step passing rows with the contract on, minus values with fewer, over all row kinds; (b) values passing at their last checkpoint only. Recommendation: (a).
- **M-14. Which rows a case covers.** Options: (a) every row of the value in the run whose first loss is at the case's step; (b) only the row at the earliest failing checkpoint. Recommendation: (a); (b) would leave later checkpoints' rows outside every bound.
- **M-15. Incidence on facts that hold no gold value.** Options: (a) reported, not bounded; (b) every such event makes the mechanism of its bug *can't tell*. Recommendation: (a) for Phase C; under A1 and A2 the system-bug incidence counts are zero (plan 23:243, :248).
- **M-16. A2 contract populations.** Options: (a) cases at `filed` to `status` only, as proposed; (b) every write-path case, as the literal reading gives. Recommendation: (a); extraction is identical in both harness variants by construction. Under either option the open same-meeting conflict cases (held, Rule V item 7) are in every A2 contract's population; section 6.2 and decision M-21 give the expected consequence (added in the review of 27 October).
- **M-17. "Owner or role claim" on EL2020.** The EL2020 gold has no owner or role items. Options: (a) define it before Step 2c, on claims (for example a claim whose predicate assigns a person or role), fixed in the probe note; (b) drop the condition on EL2020 and disclose. Recommendation: (a). The definition is drafted in the probe note (`23-am1-probe-note.md`), under its heading "Owner or role claim on EL2020 (C41, M-17)". This register does not define the term. C110 points there, and section 6.2 points at this decision. The choice is decision C41 on the decision sheet. (Pointer added in the completion pass of 27 October.)
- **M-18. Step 5 joint contract verdict.** No endpoint is fixed for final configuration against A1-ref. Options: (a) the admission endpoint (status-step rows, distinct values net) with the family endpoints as context; (b) the family endpoints. Recommendation: (a), fixed before Step 5 runs.
- **M-19. The verdict rule for architectural mechanisms.** It is drafted in Rule M (section 7a, 27 October 2026), for option (a). The choice left is decision C43 on the decision sheet: when the rule is fixed. Plan 23 requires "an endpoint and a pre-registered rule for *works*, *doesn't work* or *can't tell*" (plan 23:344). For the contracts it asks to "Write the rule down before the last development comparison." (plan 23:269); Rule M applies that timing to the architectural mechanisms. The rest of this mapping fixes populations, not thresholds. Options: (a) sign Rule M with this Step 0 package; (b) move Rule M unchanged into a dated note before the Step 3 reveal (amendment:411, item 7); (c) a dated note before the Step 5 runs. Recommendation (changed in the review of 27 October): (a). Failing that, (b), not (c): under (c) the rule could be set after the codes and the Step 2 to 2c outputs that drive the bounds are open, and the amendment "fixes decision rules that their own outcomes must not steer" (amendment:14). Disclose in every case that the EL2020 family results were read first; Rule M does. Neither the amendment nor plan 23 fixes Rule M's test (item 4) or the 15 choices listed at its end; answering decision C43 adopts them (under (b) or (c), in the later dated note). Rows C04, C77 and C94 point at Rule M. (Changed in the completion pass of 27 October; the choices were extended from six to 15 in the review of the completion pass.)
- **M-20. Bound arithmetic on question endpoints.** Options: (a) as in section 7, with shares pooled per arm and the remainder filled by section 7's deterministic greedy fill (items 3 and 4), which approximates, and does not guarantee, the fill least favourable to the recorded verdict; (b) per-run shares; (c) a proportional (expected-value) fill, which no section of this mapping defines yet, and which can be chosen only on the condition in Rule M item 9. Recommendation: (a); it is deterministic and follows amendment:456. It is not conservative on small bases (Rule M item 5; option (d)). Added in the review of the completion pass (27 October): option (d), as (a) but with share 1 wherever fewer than 5 items are in that share's base (coded cases, or examined pass rows in the pass share's base; Rule M item 5) in the run or runs the share comes from. (Options (a), (c) and (d) reworded in the second review, 27 October.) It removes the drop from share 1 to share 0 at the first clean coded item (Rule M item 5). No recommendation is made on (d).
- **M-21. Held conflict cases in the A2 contract bounds** (added in the review of 27 October). Section 6.2 discloses that, while the conflict decision is open, every A2 contract is expected to come out *can't tell*. Options:
  - (a) disclose only: keep M-16 and Rule V item 4 as they are, and report the expected *can't tell* verdicts;
  - (b) limit each contract's population to the sub-codes it acts on. This is a new option, not M-16(b). It conflicts with the reasoning of M-6 and Rule V item 3: a defect that moves a row endpoint must enter that endpoint's bound. It also leaves `supersession_requires_new_evidence`, which has no sub-code of its own, with no population;
  - (c) under M-20's arithmetic, stratify the borrowed A2 shares, so that the held share applies only to a variant's own open same-meeting-conflict cases. The conflict-off variant then borrows no held share.
  - Recommendation: (a) in any case, which this register now does. Consider (c) if decidable A2 verdicts are wanted. Do not adopt (b).

## 10. Review record (27 October 2026)

**Workflow.** am1-step0-verify. Three review sweeps read this register against the thesis at b4d6b6c, the amendment and the other Step 0 files:
- "claims: sweep Ch5": findings Ch5-F1, Ch5-F2, Ch5-F3, Ch5-F4 and Ch5-F7 survived;
- "claims: sweep other chapters": findings OC-F1 to OC-F8;
- "claims: rows and mapping": findings RM-F1 to RM-F12.

The sweeps each numbered their findings from F1, so the ids here carry a prefix. A skeptic tried and failed to refute each finding. Where the skeptic gave a better fix, that fix was applied. The register before this fix has SHA-256 490c8f383115dc6ea64b144ff033214a27f06b46aacb1c23131b779ee6d3c82e. No model, embedding or network call was made, and no other file was changed.

**Figures checked again.** The fix recomputed these Already-read figures from `23-loss-trace.json` (strict series) before citing them. All matched the reviewers' figures. No other outcome figure was computed into this register.
- Persist rows (C75a): A0 14 / 5 / 4 / 1; A1 12 / 7 / 5 / 0.
- A2 cases at `proposed:same_meeting_conflict` among distinct value × step cases at `filed` to `status` (mapping section 6.2): 17 of 33, 11 of 28, 22 of 37.
- Bug-2 flags per A0 run (C41, C68): 36, 31, 32; any defect flag: 36, 34, 33.
- Filing rows (RM-F6, C04): A0 21.7 per run, of which `another_value_won` 21.3; A1 25.7 and 15.0.

**Findings.**

| Id | Outcome | What was done |
|---|---|---|
| Ch5-F1 | applied (skeptic's fix) | New row C75a (eval.tex:1010 and :1115, merged), id per thesis order. Complementary conditions over the failing persist rows; the $C_1$ to $C_4$ clause kept with amendment:46; marked Already read (points to overturn); conclusion.tex:37 under "Also stated at"; M-5 note kept. Index; group U. |
| Ch5-F2 | applied (skeptic's fix) | eval.tex:945 listed under C136 ("Also stated at", with its R-9 actions) and in group C; no separate row. eval.tex:932 added to R-16, citing bug 8 (22-bug-list.md:103). |
| Ch5-F3 | applied (skeptic's fix) | eval.tex:1089 is C05's third location, quoted from l.1089. The D9 clause (eval.tex:1092) has its own action tied to R-4 (also in section 6.2 and R-4's row list). The restraint clause is noted as untestable (C05 note, section 6.3). eval.tex:1152 is in C05's note and group B. The evidence correction ("inspectab" has one hit, C108) concerns the finding, not this file. |
| Ch5-F4 | applied (skeptic's fix) | New row C98a. C127 not listed; the A1-ref overturn condition dropped; the section's "not causal stages" disclaimer recorded; R-13 and group E updated. conclusion.tex:224 and :377 added under it (from OC-F6). |
| Ch5-F7 | applied, narrowed (skeptic's fix) | eval.tex:1118 under C02 ("Also stated at"), group I and section 6.1. Not added: eval.tex:800/801, :812 and :875, which restate no registered loss claim and which no row's text action would edit. |
| OC-F1 | applied (skeptic's fix) | New row C133a: testable partly, through C122's test; mechanisms per R-8 and Rule A (list half "none: reading (D8)"). Index, group S, section 6.3, C99's and C122's "Also stated at". The switch facts were checked at 3320375 (`app/core/config.py:144`, `:154–160`). |
| OC-F2 | applied (skeptic's fix) | New row C136a, text actions deferred to R-9 and R-14. R-14 widened to both generated tables, with options for the captions and for the Resolved column, and the note that the caption alone does not fix 8/24 and 24/24. eval.tex:975–976 cited; C70's "Also stated at"; group C; section 6.1. |
| OC-F3 | applied (skeptic's fix) | New row C37a. Its note separates the surfaced-at step (filing) from where the exclusion acts (reading), leaves caused-at to Step 3, and records the Rule V item 7 limit and the weak A0/A1 test. |
| OC-F4 | applied (skeptic's fix) | Note on the decision-tagged headings in section 5 (l.194 maps to C115–C118 and C81), and R-5's context. New row C130a; its tags are decision R-21, not routed through R-11. conclusion.tex:336–337 under C01 and in group J. |
| OC-F5 | applied | conclusion.tex:96 under C55. R-11's context and options now name conclusion.tex:96, :306 and :330 (C130), and C89 with group N. Group AA added for C18 and C55. |
| OC-F6 | applied (skeptic's fix) | Every listed location added to the named row's "Also stated at" and to a section 5 group; groups V, W, X, Y and Z added for rows that had none. C127: boundary "evaluation (gold correction; C62)" and a B3-based overturn condition. C120: note that conclusion.tex:223 refers to the cycle-1 trace, and that the v3.1 sub-codes are what Step 3 tests; group B. The "37 occurrences" clause (conclusion.tex:224) and conclusion.tex:377 sit under C98a and C99. |
| OC-F7 | applied (skeptic's fix) | Restatements added as notes: C08 (problem_domain.tex:167, :401), C10 (problem_domain.tex:194, appendix_walkthrough.tex:51), C137 (appendix_walkthrough.tex:189). problem_domain.tex:167 in group R. New row C138a for appendix_walkthrough.tex:201; testable "no", because a search of the reviewed ES2009 gold found no row for the conditional voice proposal. l.357 is a note under C140, not a row. |
| OC-F8 | applied | C47 cited at implementation_chapter.tex:611 in the index and heading; added to the line-number corrections in section 2. The quote check now requires every row quote's first fragment to start on the cited line, including quotes that open with `[...]`. |
| RM-F1 | applied (skeptic's fix) | C87, C49, C112 and C113: the confirmed branch is split into architectural or trade-off on 94c049d text with the kappa's lower bound at or above 0.40 (design ground may be kept) and design-or-model-not-separated or no class (location only). C112's and C113's decision column follows C109's rule. D11 is marked retrospective in both branches of C87, C49 and C113. C40 keeps its pointer sentence; counts are reported by class. |
| RM-F2 | applied (skeptic's fix) | The consequence is written into mapping section 6.2, M-8 and M-16. C32, C34, C47, C111, C120, C132 and C133 note the expected *can't tell*. The options are a new decision M-21, with the conflicts of the own-sub-code option stated; recommendation: disclose, and consider stratified shares. |
| RM-F3 | applied as a decision, plus the parts for either case | Decision R-22 (remove "D5.p3's equal-time eligibility" from R-4's list, or keep it and change sheet S and C17, C98, C120); recommendation (a). R-4, C98 and C120 point to it. For either case: C85 and C91 follow design-and-controls decision 2 (D5.p6 for a trade-off only; D5.p5 only if that decision is signed (b) or (c)); C28's design route is limited to sheets K2 and R. |
| RM-F4 | applied (skeptic's fix) | A third branch, *can't tell (defect-limited)*, in C32, C34, C47, C111, C120, C132, C133, C04, C77 and C94: report the recorded and the bounded verdicts, no works or doesn't-work statement. C111, C132 and C133 no longer fold *can't tell* into "did not work" or "not shown"; "not shown" stays for WD only. |
| RM-F5 | applied (skeptic's fix) | C35 ("any of these"; already points to overturn), C67 (already points to overturn for the repaired arm; the coding clause is now a note on cause), C83 (the bugs 3 and 13 bullet restricted to Step 3 codes, with its own action; Already read cited at 23-loss-trace-results.md:90, where the finding had :89). |
| RM-F6 | applied (skeptic's fix) | C04: "under reused keys" (routing) and "winner-take-all" (ranking) tested apart, with an action for the case where only the ranking clause is overturned. C92: the overturn bullet names a case in which authority decided the outcome, with a note that one authority level makes it unlikely. |
| RM-F7 | applied (skeptic's fix) | C09, C137, C138, C140, C141 and C142: confirmation only on the final configuration's r1; A0 r1 walkthrough extraction cases can come out only implementation or unclear (amendment:238, :312, :338). Probe (iii) limited to A1 and A2 rows in C40, C87 and C112. C112 and C122 use Step 5 scores; their design reading is marked untestable. C142 names probe (i), the A1 repairs and admitted contracts. |
| RM-F8 | applied | Rule A limited to the location account (mapping "What this part fixes" item 2, section 3's account column, the complete-decisions note in section 6.1). `current:overwritten_by_non_gold_value` and `current:displaced_by_other_gold_value` are now "unattributed". |
| RM-F9 | applied (skeptic's fix) | C48, C63, C69 and C75: "none (unknown family; decision M-4)", with the M-4(b) reading given. C37 unchanged, because it is not about the unknown family. |
| RM-F10 | applied | M-19: new option (b), a dated note before the Step 3 reveal; recommendation now (a), failing that (b), not (c). C04, C77 and C94 state their dependency on M-19. |
| RM-F11 | applied, except one refuted sub-item | "nine runs" in C19, C36 and C37; bug-2 flags "31–36 (33–36 with any defect flag)" in C41 and C68; the missing WD condition in C110; C22 cites D2.p4 and its note now applies the burden rule. Not changed: "12 of 16" in C10 and C83, which the skeptic showed is correct; the 10 + 2 split is added there. |
| RM-F12 | applied | C47 at l.611; "clearer" lower-cased in C04 (now cited at eval.tex:1085) and C77; R-1's quote lower-cased; proposed wordings in C04 and C83 labelled "proposed:" with no `path:line` after them, and the convention added to section 2. Proposed wordings written during this fix (C05, C75a, C87, C111) follow it. |

**Open decisions added or changed by this fix:** R-21 and R-22 (new); M-21 (new); M-19 (recommendation changed); R-14 (widened, with a recommendation for the Resolved column); R-4, R-5, R-11, R-13 and R-16 (context or locations extended).

**Checks after the fix.**
- Quote check (scratch script `qcheck_claims.py`, no model or network): 168 row and dormant quote blocks verified at b4d6b6c, each fragment in order and the first fragment starting on the cited line; 162 inline quotes with a recognised citation verified. Before the fix: 158 blocks, 102 inline quotes, 7 errors. After: 1 error, outside the findings: mapping section 6.1 cites amendment:144 for "status items that can fail", which is at amendment:143. It was left for the author, and corrected to amendment:143 in the cross-package consistency pass of 27 October.
- A start-line check of inline quotes found, besides that citation, only C04's "itself" cited at the row location eval.tex:1084 (the word is at l.1087). It is a reference to the row's quote and is left as it was.
- `23-am1-check-register.py` checks the design-and-controls register, which this fix did not change: 0 errors, exit 0. Run on this file, only its design-paragraph check applies: 7 quotes governed by a D-paragraph id, none failing. Its other checks assume that register's citation format.
- 151 row headings match the index in order and location.

**Observed, not changed (outside the findings).** C22 and C142 allow an architectural code on D2's window passage (D2.p4). The design-and-controls register lists that passage among the disclosed limitations of its decision 2. If that decision is signed (a), the route closes, as for D5.p5 in C85.

**Cross-package consistency pass (27 October 2026).** Four edits: section 8's opening now names the mapping's decisions as M-1 to M-21 (M-21 was added in the review); the citation amendment:144 in mapping section 6.1 is corrected to amendment:143 (the error left open above); the label "design or model, not separated" in mapping section 4 now has the amendment's comma; section 1, Line numbers, now states that the notes files with uncommitted edits or no commit (the amendment, plan 23, `22-bug-list.md`, `23-loss-trace-results.md`, `23-el2020-arms.md`, the loss-trace codebook and script) are cited at their working-tree lines of 27 October, which every such citation in this file follows.

**Completion pass (27 October 2026).** Offline: no model, embedding or network call, and no other file was changed. The register before this pass has SHA-256 05f4aacac73043f6c4dd099ad671d45cdf1c3c97242205f766ccb2a83e96a7ce. What changed:
- **Rule M** (new mapping section 7a, before mapping section 8): the *works*, *doesn't work* or *can't tell* rule for the architectural mechanisms, drafted for decision C43 option (a) on the decision sheet. No family-level or endpoint result was computed or looked up for it. The key structure of one RAG run report was read, with no values, to check that the endpoint can be computed. Its six choices that neither the amendment nor plan 23 fixes are listed at its end.
- **Pointers to Rule M.** M-19 now says that the rule is drafted in Rule M and that the choice left is decision C43. Rows C04, C77 and C94 say that their third outcome is decided by Rule M. In the mapping's "What this part fixes", item 1 now says that Rule V governs verdict membership, and a new item 5 names Rule M. The opening of section 9 names this pass.
- **M-17 and C110** point at the probe note's heading "Owner or role claim on EL2020 (C41, M-17)", which another agent drafts in parallel. This register does not define the term.
- **Rule V's items (X4).** Every `\bV[0-9]+\b` token was classified. 27 tokens refer to Rule V's items and now read Rule V item N: the ten item headings and three references inside them, C37a (two), mapping sections 4, 5, 6.1, 6.2 and 7, M-8, M-16, M-21 (two) and the review record (OC-F3). Five tokens are the second coder V4 (C81, C84, C101, C107, C129) and are unchanged.
- **Ranges (X14).** "(iv) is the WD rule" in section 2 now cites amendment:350–356, because "No WD run covers the value: unclear." (amendment:356) belongs to the WD-cases rule. "Already read" in section 1 now cites amendment:33–63: the block runs from its heading (l.33) to the paragraph on archiving the records (l.63). The mapping's citation amendment:33–40 (the heading and the loss-trace item) is left as it is.
- **Probe-note decisions.** This file cites none of the probe note's decisions D1–D14, so nothing is renamed to PN-n. Every D-number here is a Ch. 4 decision or one of its paragraph ids.
- **Quote check** (`qcheck_claims.py`, the review's scratch script, run unchanged): before this pass 168 row and dormant blocks, 163 inline quotes, 0 errors; after it 168 blocks, 196 inline quotes, 0 errors, and the same 35 quotes with a citation it does not parse (one of them now reads "Rule V item 2" for "V2"). The new quotes it cannot check are the probe-note heading (three times), which does not exist yet, and this entry's quotes of this file's own wording.
- **Not changed, outside this file.** The decision sheet's C43 still says the rule is not drafted, and its C1 lists "the M-19 rule if C43 takes option (a)" (23-am1-decisions.md:55) as a pre-tag item.
  - Second review (27 October 2026): since mirrored in the decision sheet's update after the completion pass (23-am1-decisions.md:791–799); the quoted C1 wording is now at 23-am1-decisions.md:62 in changed form, so the quote above is of the sheet as it then read and can no longer be checked against it.
- **X14 wording replaced (27 October 2026).** The X14 line in section 2, "(iv) is the WD rule", now reads: (iv) is criterion (iv) of the implementation-choice class (amendment:325), applied by the WD-cases rule (amendment:350–356). The Step 2c rule is named as the one headed "WD rule, fixed here" (amendment:289–296). The bare term "the WD rule" gets no register-wide meaning (finding MX-F6).
- **Probe-note heading (27 October 2026).** The probe-note heading now exists (23-am1-probe-note.md:354) and matches the three pointers (C110, M-17, this record) (finding MX-F9).

**Review of the completion pass (27 October 2026).** A review of this pass found gaps in Rule M and in mapping section 7 (findings VI-RM-n, VD-RM-n, MX-Fn). Offline: no model, embedding or network call, and no other file was changed. The register before this review has SHA-256 1b07ccad6df0041c1fa4f15a94f20e3f50f5308cb66f9c0aec9eb9b2d22b0eb4. Where a finding gave a better fix, that fix was applied. To check two citations (VI-RM-6, VI-RM-10), the review read the family table of `23-el2020-arms.md` (lines 26–36), which Rule M already lists as read. No result was computed, and no value is written into this file.
- **VI-RM-1 and VD-RM-1** (blocked signing): applied, with VI-RM-1's wording. "Repaired" is dropped from "What does not weaken"; item 5 adds "A later repair does not exempt a case"; item 1 adds "Computed once": each verdict comes from the final codes and is not recomputed. It is choice 8. VD-RM-1's point on the old "do not exist yet" sentence is met through VD-RM-9 (the frozen gold sets the EL2020 verdict).
- **VI-RM-3 and VD-RM-12:** applied. C94 has a branch for *can't tell (within the instrument range)*. Item 8 now says which verdict a claims row reads. The third branches of C04 and C77 are unchanged, as the better fixes ask.
- **VI-RM-4:** applied. C04 and C77 send complete decisions and change and supersession to Rule M, WD to the Step 2c rule and (C04 only) the A2 contracts to the admission rule, each with the bound.
- **VI-RM-5 and VD-RM-11:** applied. The choices header and M-19 are reworded; the list has 15 choices (six before); M-19 gives the new count. "A recorded *can't tell* is never bounded" is not listed: it follows amendment:451 and :466–469. The completion pass entry above is kept as written.
- **VI-RM-6, VD-RM-10 and MX-F6:** applied. Item 4's IR bullet no longer says it follows the WD rule; choice 7 says IR was chosen after the EL2020 family results were read. The per-run range sentence of the first fix is not added, as the better fix asks.
- **VI-RM-7 and VD-RM-9:** applied, option (a). On EL2020 the frozen gold sets the verdict and the post-B3 recorded verdict is reported beside it. The two-gold rule applies only where B3 precedes the runs (choice 13).
- **VI-RM-8:** applied, in item 1 ("The series verdict").
- **VI-RM-9:** applied, in the C28 (b) cell of item 2. The cell covers C43 (c) as well as (b), since M-3 (b) asks for "before any further output" whatever C43's answer.
- **VI-RM-10:** applied as disclosure only, in item 2's epistemic status row and in M-4, the source of decision C29. No "cannot be *works*" rule is added, and the change and supersession row is unchanged, as the better fix asks.
- **VI-RM-11:** applied. "Not blind, and when it is fixed" states the timing under C43 (a), (b) and (c). Under (b) it also says that the blind codes of Step 3 items 4 and 5 may exist.
- **VI-RM-13 and VD-RM-6:** applied, with VD-RM-6's wording, in item 5 (choice 9).
- **VI-RM-14 and VD-RM-14:** applied. Item 9 fixes the mechanisms of bugs 1–6, 12 and 13 under C38 (b). Bug 1 also gets rejection (D3.p3's negation sentences); bugs 3 and 4 are stated as choices (choice 15). Bug 12 is listed because plan 23:261 names its incidence script; it maps to none.
- **VI-RM-15:** applied, in the mapping header.
- **VI-RM-16:** applied, in item 7 (choice 14).
- **VD-RM-2, VD-RM-4 and VD-RM-5:** applied, in mapping section 7, items 3 and 4: the multi-value rule, the greedy fill for both bounds, and the pass share with its count. Rule M item 5's own fill-order gap fill is removed, since section 7 now fixes it. Rows examined under C35 (b) are left out of the share, like `credit_without_state` rows.
- **VD-RM-3:** applied. The bootstrap is pinned in section 7, item 1. The drop from share 1 to 0 is disclosed in item 5 and choice 11. A floor is offered as M-20 option (d), with no recommendation; it is not a settled rule.
- **VD-RM-7:** applied, in items 2 and 5. Item 5 also names the ES2009 adjudication file (amendment:171) for ES2009, since v1 is EL2020's.
- **VD-RM-8:** applied. Item 5 requires the loss trace for a bounded verdict. Item 1 borrows the dress rehearsal's shares within its series and marks this as Rule M's extension (choice 3).
- **VD-RM-13:** applied. "What it answers" and M-19 cite plan 23:269 as said for the contracts. Item 5 now says Rule M reads plan 23:358 as the amendment does.
- **VD-RM-15:** applied. (a) A1-ref's verdict stands in when the final configuration has no Step 5 runs (item 1). (b) Item 3 replaces a run with switches that do not match its arm. (c) The C35 (a) cell is reworded, and item 5 adds the C35 (b) line. The (a) cell also names the pass share, which VD-RM-2 adds.
- **MX-F9:** applied (dated line above).
- **Checks after the review.** Quote check (`qcheck_claims.py`, unchanged): 168 row and dormant blocks and 202 inline quotes verified, 0 errors (before this review: 168, 196, 0). The 35 quotes with a citation it does not parse are the same as before. The 11 new quotes with no citation are this entry's quotes of this file's own wording and labels. `23-am1-check-register.py` on this file: 7 design-paragraph quotes, none failing. The 151 row headings are unchanged. The amendment's SHA-256 is unchanged.
- **Not changed, outside this file.** The decision sheet does not mirror this review: its C43 does not give the number of Rule M's choices (now 15) and still says the rule is not drafted; its C29 "Changes" lacks the disclosure added to M-4; its C44 lacks option (d) of M-20.
  - Second review (27 October 2026): since mirrored in the decision sheet's update after the completion pass (23-am1-decisions.md:791–799): C43 now says the rule is drafted and names its 15 choices (23-am1-decisions.md:362, :375), C29 carries the disclosure (:263), and C44 has option (d) (:407).

**Second review (27 October 2026).** A second review of Rule M and mapping section 7 reported defects only (findings m-integrity:R2-n, m-code:RM2-n and sheet:R2-4). Offline: no model, embedding or network call; `.env` not opened; the `app` package not imported; git state not changed; no other file was changed. The register before this review has SHA-256 8a68e49c8637d703eff941f53a99531ee252179a7371fd2770a55a4376b0aa95. Where a finding gave a better fix, that fix was applied. To check citations, the review read the cited lines of `23-el2020-a0-a1.py` and `23-bug-incidence.py`, the script's `question_map` (script:314–332), the section headings of `22-bug-list.md`, and the key names of one strict question record of `23-loss-trace.json` (`correct`, `family`, `k`, `question_id`, `rows`), with no values. No result was computed, and no value is written into this file.
- **m-integrity:R2-01:** applied (better fix). Section 7 item 6: RAG's scores enter under the gold that Rule M item 7 names for the verdict; the amendment:319 quote stays as context for B3.
- **m-integrity:R2-02 and m-code:RM2-3:** applied, in section 7 items 3 and 4, where R2-02's better fix places it: every coded weakening case, and every examined weakening sample row, of the run is taken even beyond the count; the count is then their number and nothing is filled.
- **m-integrity:R2-03, m-code:RM2-5 and m-code:RM2-7 (gap rule):** applied in this file with RM2-5's better fix, which also carries R2-03's point and RM2-7's keying on the source runs. The gap rule (Rule M item 5), choice 11 and M-20 (d) now turn on the share's base in the run or runs the share comes from. Not applied: the same change in the decision sheet's C43 item 11 (23-am1-decisions.md:386) and C44 (d) (:407), which are outside this file.
- **m-code:RM2-7 (item 1):** applied (better fix). If the final configuration has no Step 5 runs, there is no 3b coded run, and A1-ref's shares are 1 under the gap rule, disclosed. 3b's scope (amendment:312) is not widened.
- **m-integrity:R2-04 and m-code:RM2-4:** applied in this file, in section 7 item 1 under "The bootstrap in full": the values and their order, a fresh generator per share, the draw as at `23-el2020-a0-a1.py:80`, pooling once per draw of a value (as the script's :69), the statistic, and exact fractions. The values are taken over the share's base rather than over the arm, so that the borrowed shares (RM2-7) are covered. Not applied: C44's "as `23-el2020-a0-a1.py` does" (23-am1-decisions.md:408), which is outside this file.
- **m-integrity:R2-06 and sheet:R2-4:** applied, with R2-06's wording, in the choices header and in M-19.
- **m-integrity:R2-07:** applied in this file, under "Not blind, and when it is fixed", option (a). Not applied: the same sentence in the decision sheet's C43 (23-am1-decisions.md:371), which is outside this file.
- **m-integrity:R2-09:** applied (better fix): the citation is dropped.
- **m-integrity:R2-10:** applied (better fix): C94's Mechanisms field lists rejection, and its confirm condition reads the mechanisms listed there.
- **m-integrity:R2-11:** applied (better fix), in Rule M item 9; choice 15 names the bugs in the evaluated system. C38 is unchanged.
- **m-integrity:R2-12 and m-code:RM2-10:** applied in this file, in M-20 (a), with both wordings combined. Section 5's worst-case sentence is unchanged. Not applied: C44 (a) (23-am1-decisions.md:407), which is outside this file.
- **m-integrity:R2-13:** applied, in section 7 items 3 and 4.
- **m-integrity:R2-14:** applied (better fix).
- **m-integrity:R2-15:** applied, as dated lines under both bullets, with the better fix's range 791–799. The quote of the sheet's former C1 wording (23-am1-decisions.md:55) is left as the record of what was read then; its dated line says it can no longer be checked.
- **m-code:RM2-1:** applied, as a definition placed before section 7 item 3.
- **m-code:RM2-2:** applied (better fix), in section 7 item 4.
- **m-code:RM2-6:** applied (better fix), in section 7 item 4 and in Rule M item 5's "What does not weaken".
- **m-code:RM2-8:** applied (better fix), in section 7 item 1, with one correction: for the shares that Step 5's runs borrow, the base is the cases of 3b's coded run, which 3b codes in full (amendment:312, :460). The better fix's base of 30 author-coded cases per run would contradict amendment:312 there.
- **m-code:RM2-9:** applied, in Rule M item 6.
- **m-code:RM2-12:** applied (better fix), in Rule M item 9: the C32 (b) precedence is section 5's order, now stated there without "for example"; the C31 (b) membership of coded and uncoded cases; the condition on C44 (c), to which M-20 (c) points. Choice 15 is widened to these readings.
- **Counts.** Rule M still lists 15 choices; choices 11, 12 and 15 are widened, as its choices header says. M-19's count (15) is unchanged. The mapping header names this review.
- **Checks after this review.** Quote check (`qcheck_claims.py`, unchanged): before this review 168 row and dormant blocks and 201 inline quotes verified, 1 error; after it 168 blocks and 202 inline quotes, 1 error. The error, before and after, is the quote of the sheet's former C1 wording (23-am1-decisions.md:55). It has failed since the sheet's update, and its dated line (R2-15) explains it. The 35 quotes with a citation the check does not parse are the same as before. R2-14's new quote (plan 23:348) is verified. `23-am1-check-register.py` on this file: 7 design-paragraph quotes, none failing; its other checks assume the design register's citation format, as before. The 151 row headings are unchanged. The amendment's SHA-256 is unchanged.
- **Not changed, outside this file.** The decision sheet does not mirror this review: C43's option (a) sentence (23-am1-decisions.md:371), its brief choices 11, 12 and 15 (:386, :387, :390), and C44's options (a) and (d) and its bootstrap sentence (:407–408).
- **Main session, 27 October 2026.** Two second-review findings left open by the fixers are applied here: M-11 now says a wrong-meeting value can weaken evidence and provenance only as a pass (Rule M item 2), and its option (b) is fixed at signing (decision C35), not by a dated note (m-integrity:R2-05, m-code:RM2-11). M-20's recommendation no longer calls option (a) conservative, since a base whose items are all clean gives share 0 (Rule M item 5).

**Pre-tag pass (28 October 2026), decision B8.** Offline: no model, embedding or network call; `.env` not opened; git state not changed; no other file was changed. The register before this pass has SHA-256 5e406560ef5509936687b2280d2790a28c80178f8b7ede7ba9c247124262f23f.
- **B8 (1):** the amendment has "status items that can fail" at amendment:143. Mapping section 6.1 already cites amendment:143, since the cross-package consistency pass of 27 October. No edit was needed.
- **B8 (2):** C144's two checked runs were a0_r1 and a2_r1 (the Ch. 4 sweep). The other ten were checked in the run folders under `data/ami_eval/a1_smoke` (read-only). `23-am1-run-manifest.py` found all twelve runs at their manifest hashes. a0_r2, a0_r3, the A1 smoke run, a1_r2, a1_r3, a2_r2b and a2_r3 have `fallback_count` 0 and `config.strict_live` true in `coldstart.json`. rag_r1, rag_r2 and rag_r3 have no `coldstart.json`; their `.rag.json` has `fallback_count` 0 and `config.strict_live` true. No run has a fallback or is not strict-live, so no open item arises. C144's note records this; no verdict was changed. Section 7, dormant 3, still names only the two runs checked by the sweep; B8 does not ask for it to change.
- **Checks after this pass.** Quote check (`qcheck_claims.py`, unchanged): 168 row and dormant blocks, 1 error, the known quote of the sheet's former C1 wording (23-am1-decisions.md:55).
