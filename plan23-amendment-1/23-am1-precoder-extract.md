# The register sheets: pre-coder extract

This text holds the five register sheets of the design-and-controls register, one per caused-at boundary: extraction (E), key assignment at extraction (K1), key resolution and expansion (K2), state rules (S) and reading (R). After each sheet come three parts: the text of every 94c049d paragraph the sheet names, sentence by sentence; the conformance requirements the sheet names; and the register's implementation entries the sheet points to.

How to read it:
- "Amendment line N" cites line N of the study plan quoted in Parts B and D of the instructions.
- A pointer such as (E.6) or (K2.6c) names the register section that holds an entry. The sections that a sheet points to for implementation entries follow the sheet. Pointers to other sections, such as (E.3), only give the source of a gloss; those sections are not part of this text. A pointer is not a finding.
- Checklist items carry an id in square brackets, one item per line: candidate causes ([E-cause-1], ...), further implementation entries ([E-entry-1], ...), and conformance requirements under their register ids ([E-C1], ...). The conformance requirements are listed after each sheet. An item's text is the rest of its line after the id. Indented lines under an item are notes on it, not items.
- Each sheet lists, under "94c049d text a page may quote", the only sentences that may ground a design code on that sheet: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. A sentence the register tags (B, C) counts under the list it appears in on that sheet. The paragraphs after the sheet repeat each listed sentence with that tag. Their other sentences are marked (L), a disclosed limitation, or (—), not listed on this sheet. Neither may ground a design code.
- For WD cases (surfaced at `carried:claims_without_the_value`), sheet E lists D4.p5 whole: any sentence of D4.p5 may be quoted, whatever its tag (amendment line 355). After sheet E these sentences are marked (WD, B) or (WD, C). On sheet E they ground nothing in any other case.
- Text marked Gloss is the register's own reading, not design text.

---

## Sheet E: extraction (admission and extraction)

**Scope.**
- Losses surface at `admitted`, `carried`, `polarity` or `modality`.
- Oracle evidence, amendment line 370: "recovered by E+R but not R, or by E+R\* but not E+R: extraction (the second is polarity);"
- Exception, amendment line 373: "where the page shows the deciding claim is a recorded wrong-modality carrier, or a positive carrier of a ruled-out value, that misreads its span, caused-at is extraction (listed);"
- Step type: the gatekeeper and the extractor are LLM steps (A.1, E.1). The extractor has a model condition, probe (i)(d). The gatekeeper has none.

**Candidate causes listed by the amendment** (amendment line 384). The page addresses each.
- [E-cause-1] "registry-conditioned extraction" (amendment line 384)
   - Decided by: probe (i), conditions (b) (the registry cut to the resolver's embedding candidates, at `embedding_top_k`=8 and `embedding_min_similarity`=0.30) and (c) (an empty registry). Probe (i) covers every extraction-lost case except `admitted:ignored`.
   - Entries to check: the whole active registry in the extraction prompt, one key set per meeting, the empty-registry sentinel at meeting a (E.6, How the registry enters); re-extraction of spans that gave no claims, with the larger registry (E.6; mapped to this cause at signing).
- [E-cause-2] "out-of-domain prompt examples" (amendment line 384)
   - Decided by: probe (i), condition (b2): the neutral examples of the probe note in place of the AMI role examples.
   - Entries to check: the AMI role examples of the extraction prompt, and the session check that none of the four titles occurs in any EL2020 span (E.6, Examples); the ownership sentence (K1.6).
- [E-cause-3] "a modality or negation instruction missing from the prompt" (amendment line 384)
   - Decided by: criterion (ii) and the page. Gloss: no Step 2b condition tests this cause.
   - Entries to check: the polarity and modality instructions (E.6, Examples); `extraction_confidence` requested without a definition (E.6, Not shown); the claim-status mapping (E.6, Parameters).
   - Design to compare: E-C2 and E-C3 (D3.p2); the non-asserted modalities named in D3.p3 (E.2).
- [E-cause-4] "the gatekeeper ignoring a span its own criteria admit" (amendment line 384)
   - Only for `admitted:ignored` cases. No probe applies, amendment line 241: "Those are gatekeeper losses with no extraction call, and are listed apart."
   - Decided by: criteria (ii)–(iv) and the page (line 339 names `admitted:ignored` cases among those with no probe-type alternative).
   - Entries to check: the gatekeeper prompt's classes and examples; the span sent alone (five lines, no neighbouring spans); the three admitting policies treated alike (A.6).
   - Design to compare: A-C5, the admission criterion of D2.p5 (A.4).
   - If implementation is rejected: the gatekeeper is an LLM step with no model condition, so the class *design or model, not separated* is available, amendment line 331: "the gatekeeper for `admitted:ignored` cases"
   - At the gatekeeper, architectural weakness or a trade-off also needs the argument of line 340 (quoted on sheet K1). Both this condition and the class apply at the gatekeeper only for `admitted:ignored` cases, as line 331 scopes them.
- [E-cause-5] "no whole-decision contract (WD rule only)" (amendment line 384)
   - Only for `carried:claims_without_the_value`. Amendment line 351: "WD is judged and admitted only by the Step 2c rule. This sub-cause is never eligible under Step 4(b) and takes no repair slot."
   - Decided by: the WD rule (amendment lines 352–356; criterion (iv)).
   - Entries to check: the WD instructions, run in no evaluated arm (E.6, Arm-specific; X.4, WD).
   - Design: an architectural code may be argued only from D4.p5's scalar-concept passage (amendment line 355; E.2), quoted whole below. D10 and the WD specification are retrospective (E-R1, E-R4 to E-R6).

**Further implementation entries at this boundary** (not in the amendment's list; the pilot may add a cause that rests on one, amendment line 380):
- [E-entry-1] Segmentation into spans of five transcript lines, with a remainder under three lines joined to the last span (A.6, Parameters). Gloss: this fixes the local window of D2.p4.
- [E-entry-2] Redactions replace the first occurrence of each fragment before the evidence text is stored; the gatekeeper prompt does not say that a redaction removes the fragment from the extractor's text (A.6).
- [E-entry-3] Re-extraction of zero-claim spans at later meetings, with the claims keeping their own meeting's source time (E.6; mapped to cause 1).
- [E-entry-4] Claim identity: two claims of one span with the same hint, value and polarity are stored once (E.6, Parameters).
- [E-entry-5] `extraction_confidence` has a schema default of 0.8, reachable only after an unrecorded strict-to-non-strict downgrade (E.6, Parameters).
- [E-entry-6] The guard that fails the call when a claim has an empty `object_value` (E.6, Parameters).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Gatekeeper.
  - Design gives: the stored, segmented span, and D2.p5's criterion: keep potentially useful project context, exclude clearly incidental material (A.3). Not specified: anything beyond the span.
  - Prompt shows: the span alone, with the classes and examples of A.6. No registry, no project description, no neighbouring span.
- Extractor.
  - Design gives: admitted evidence with redactions applied, one local window at a time, no discourse linking (E.3). Whether the extractor sees the registry is not specified (E.3).
  - Prompt shows: the span; the whole active registry (key name, value type, cardinality, label, description, aliases); the instructions and examples of E.6. Not shown: meeting identity, date, neighbouring span, current state (E.6).

**Conformance checklist** (class (1)): A-C1 to A-C4, A-C6 and A-C7 (A.4); E-C1 to E-C5 (E.4); X-C1 and X-C3 (X.2). A-C5, D2.p5's admission balance, is not on this list: it is compared under criterion (ii) and cause 4 (A.4 gloss).

**Disclosed limitations at 94c049d:** window-bounded interpretation without discourse linking (D2.p4, its last two sentences); fallible classification and no privacy guarantee (D2.p5, its third and fourth sentences); misclassified modality or negation (D3.p5). Listed here before as limitations, but tagged (B) or (C) and quotable below: loss before a claim is formed (D2.p2, B); a model-assisted gate (D1.p3, C); no downstream recovery (D1.p4, B). The disclosed limitations cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D1.p3** (C) "ProjectMemory selects the third architecture:" "raw source $\rightarrow$ approved evidence $\rightarrow$ extracted interpretation \\[3pt] $\rightarrow$ proposed change $\rightarrow$ reviewed state." "A source artifact records what was received; approved evidence records what was admitted for further use; a claim records an interpretation; a proposal records a candidate change; a state fact records the outcome projected by the confirmation workflow." "``Approved evidence'' means admitted by the implemented gate, which may itself be model-assisted." "It does not mean that a person verified the statement or that its content is true."
  - **D2.p3** (C) "ProjectMemory chooses early admission." "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created." "Approved redactions are applied before extraction." "Ignored spans and sensitive spans routed for review produce no evidence record through this path." "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts." "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."
  - **D2.p4** (C) "The implemented threshold is permissive within the admitted set." "Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction." "Evidence-only is therefore \emph{not} an enforced prohibition on state extraction."
  - **D2.p5** (C) "The selected balance favours retaining potentially useful project context while excluding clearly incidental material." "It does not settle how selective admission should be."
  - **D3.p2** (C) "ProjectMemory instead represents polarity and modality separately from review status and fact lifecycle." "Positive asserted claims are classified as accepted interpretations, positive non-asserted claims as proposed interpretations, and negative claims as rejected interpretations." "These extraction labels are not acceptance of state." "Extraction confidence likewise describes interpretation, not the probability that a project commitment is true."
  - **D3.p3** (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values." "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value." "Confirmation can accept that proposal while preserving its unconfirmed epistemic status." "Explicit negation does not justify inventing a replacement." "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D2.p2** (B) "Processing everything preserves opportunities for capture but exposes all content to interpretation and review." "Filtering only at answer time retains a broad searchable record and can tailor exclusions to a question, but allows incidental material into durable interpretations first." "Selective admission before extraction places the decision earlier, at the cost of losses before a claim is ever formed."
  - **D2.p4** (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - **D2.p5** (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
  - **D3.p2** (B) "For DR1 and DR4, a simple alternative is to treat every extracted claim as an asserted fact, perhaps weighted by confidence." "This retains mentions but collapses considering a battery into selecting it."
  - **T.rationale** (B) "D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\" "D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- For WD cases (surfaced at `carried:claims_without_the_value`), only D4.p5, quoted whole, whatever the tag of its sentences (amendment line 355):
  - **D4.p5** (B) "The representation choice within an open schema remains substantial." "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics." "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
- Model-limited needs probe (i)(d).
- Conversational difficulty is limited by the recoverability rules (amendment lines 363–364).

**Retrospective entries here** (cannot ground a design code): A-R1 to A-R4, E-R1 to E-R6, X-R1, X-R6.

### Sheet E: the 94c049d paragraphs this sheet names

**D1.p3**
- (C) "ProjectMemory selects the third architecture:"
- (—) "\begin{center} \small"
- (C) "raw source $\rightarrow$ approved evidence $\rightarrow$ extracted interpretation \\[3pt] $\rightarrow$ proposed change $\rightarrow$ reviewed state."
- (—) "\end{center} These are epistemic and governance boundaries."
- (C) "A source artifact records what was received; approved evidence records what was admitted for further use; a claim records an interpretation; a proposal records a candidate change; a state fact records the outcome projected by the confirmation workflow."
- (C) "``Approved evidence'' means admitted by the implemented gate, which may itself be model-assisted."
- (C) "It does not mean that a person verified the statement or that its content is true."

**D1.p4**
- (B) "The rationale is to make commitments inspectable before their consequences persist."
- (B) "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost."
- (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- (B) "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."

**D2.p2**
- (—) "The DR8 tension is where selectivity should operate."
- (B) "Processing everything preserves opportunities for capture but exposes all content to interpretation and review."
- (B) "Filtering only at answer time retains a broad searchable record and can tailor exclusions to a question, but allows incidental material into durable interpretations first."
- (B) "Selective admission before extraction places the decision earlier, at the cost of losses before a claim is ever formed."

**D2.p3**
- (C) "ProjectMemory chooses early admission."
- (C) "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created."
- (C) "Approved redactions are applied before extraction."
- (C) "Ignored spans and sensitive spans routed for review produce no evidence record through this path."
- (C) "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts."
- (C) "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."

**D2.p4**
- (C) "The implemented threshold is permissive within the admitted set."
- (C) "Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction."
- (C) "Evidence-only is therefore \emph{not} an enforced prohibition on state extraction."
- (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
- (L) "Local transcript windows further bound interpretation: a commitment completed outside the window can be missed."
- (L) "The normal ingestion path does not invoke the separate discourse-linking mechanism to repair such omissions."

**D2.p5**
- (C) "The selected balance favours retaining potentially useful project context while excluding clearly incidental material."
- (C) "It does not settle how selective admission should be."
- (L) "Raw artifacts remain stored, redaction and classification are fallible, and evidence access checks do not constitute production authentication or retention policy."
- (L) "Thus DR8 is only partly addressed, and the gate supplies no privacy guarantee."
- (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
- (—) "Noise questions and state recall partially test that balance."
- (—) "Organisational privacy, sensitive-data retention, and an optimal admission threshold are not evaluated in Chapter~\ref{chap:evaluation}."

**D3.p2**
- (B) "For DR1 and DR4, a simple alternative is to treat every extracted claim as an asserted fact, perhaps weighted by confidence."
- (B) "This retains mentions but collapses considering a battery into selecting it."
- (C) "ProjectMemory instead represents polarity and modality separately from review status and fact lifecycle."
- (C) "Positive asserted claims are classified as accepted interpretations, positive non-asserted claims as proposed interpretations, and negative claims as rejected interpretations."
- (C) "These extraction labels are not acceptance of state."
- (C) "Extraction confidence likewise describes interpretation, not the probability that a project commitment is true."

**D3.p3**
- (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values."
- (C) "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value."
- (C) "Confirmation can accept that proposal while preserving its unconfirmed epistemic status."
- (C) "Explicit negation does not justify inventing a replacement."
- (C) "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
- (—) "Negating the current value additionally passes the resolver's authority and affirmation checks."
- (L) "With the legacy negation policy, exclusion instead makes the current fact ambiguous and opens a question for review."

**D3.p5**
- (—) "Member-level status reduces one ambiguity without making collections equivalent to scalar resolution."
- (—) "An agreeing positive claim adds support to an existing member without automatically upgrading an unconfirmed member."
- (L) "Membership still depends on correctly interpreted concept meaning, and heterogeneous content can enter the same broad collection."
- (L) "Extraction can misclassify modality or negation in either model."
- (—) "DR1 and DR4 are therefore only partially realised across the full lifecycle."
- (—) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
- (—) "Status and unknown questions directly target this behavior; rejection questions and development lifecycle probes cover only the negative transitions represented in their inputs."

**D4.p3**
- (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion."
- (C) "Open extraction can leave the concept unassigned."
- (C) "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples."
- (C) "An expansion contains a candidate definition and its triggering evidence."
- (C) "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution."
- (C) "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence."
- (C) "Concept review and value confirmation are separate decisions."

**D4.p4**
- (—) "This supports an empty initial registry without treating generated labels as research outcomes."
- (—) "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
- (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- (L) "Review may itself merge distinct meanings or fail to recognise synonyms."

**D4.p5**
- (WD, B) "The representation choice within an open schema remains substantial."
- (WD, B) "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics."
- (WD, B) "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
- (WD, C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions."
- (WD, C) "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."

**T.rationale**
- (—) "\begingroup \small \setlength{\tabcolsep}{3pt} \renewcommand{\arraystretch}{1.15} \begin{longtable}{@{} >{\raggedright\arraybackslash}p{0.14\textwidth} >{\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}p{0.21\textwidth} >{\raggedright\arraybackslash}p{0.10\textwidth} >{\raggedright\arraybackslash}p{0.15\textwidth} >{\raggedright\arraybackslash}p{0.13\textwidth}@{}} \caption{Design-decision summary: alternatives and costs, not a ranking of architectures.} \label{tab:design-rationale}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endfirsthead \multicolumn{6}{l}{\tablename\ \thetable\ continued}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endhead \bottomrule \endfoot D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\"
- (—) "\addlinespace"
- (B) "D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"
- (—) "\addlinespace"
- (B) "D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- (—) "\addlinespace D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- (—) "\addlinespace D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\"
- (—) "\addlinespace D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\"
- (—) "\addlinespace D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- (—) "\addlinespace D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- (—) "\addlinespace D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"
- (—) "\end{longtable} \endgroup"

### Sheet E: the conformance requirements this sheet names

Each is a checklist item of this sheet, under its id.
- [A-C1] One persisted gate decision per span decides whether an evidence span is created (D2.p3).
- [A-C2] Ignored spans, and sensitive spans routed for review, create no evidence record (D2.p3).
- [A-C3] Approved redactions are applied before extraction (D2.p3).
- [A-C4] Spans under state extraction, candidate extraction and evidence-only all become evidence that reaches extraction; evidence-only does not block extraction (D2.p4).
- [A-C6] Gate decisions and redactions stay inspectable and linked (D2.p3, D9.p3).
- [A-C7] Raw artifacts remain stored (D2.p5).
- [E-C1] Form claims only from admitted evidence, each linked to its evidence (D1.p3, D2.p3, D9.p3).
- [E-C2] Represent polarity and modality separately from review status and fact lifecycle (D3.p2).
- [E-C3] Classify: positive asserted as accepted interpretation; positive non-asserted as proposed; negative as rejected (D3.p2).
- [E-C4] Extraction labels are not acceptance of state; confidence describes interpretation (D3.p2).
- [E-C5] Extraction may leave the concept unassigned (D4.p3).
- [X-C1] Each boundary writes its own record: evidence, claim, proposal, fact (D1.p3).
- [X-C3] Admission is not verification (D1.p3).

Named on the sheet, but not a checklist item (the sheet's conformance line says why):
- A-C5. The admission balance, in D2.p5's own words. D2.p5: "The selected balance favours retaining potentially useful project context while excluding clearly incidental material. It does not settle how selective admission should be."

### Sheet E: the implementation entries this sheet points to

#### A.6 Implementation entries

##### Evaluated prompt

- **Builder:** `_build_gate_prompt`, `app/services/memory_gatekeeper_service.py:311-315`; system text `GATEKEEPER_SYSTEM_PROMPT`, l.272-308; user template `"Classify this span:\n\n{text}"` (l.314).
- **Hashes:** system `6b8c0ba94772`, user template `188dbe98e53d`; the same in A0, A1, A2.
- **Response schema:** `GateClassificationResponse`. It is sent with `strict: false`, because the redaction items are open dictionaries (`app/llm/openai_llm.py:134-139`; checked in this session with that module's `_strictify_schema` and `_is_strict_safe`).
- **Examples the prompt carries** (text as sent; l.272-308):
  - "POSSIBLE_PROJECT_SIGNAL: hedged proposals ('considering', 'leaning toward', 'option')"
  - "MEETING_LOGISTICS: audio/video issues, greetings, 'can everyone hear me', joining/leaving"
  - "SOCIAL_SMALLTALK: lunch, weather, personal chat, parties, celebrations unrelated to the project"
  - "A project keyword ('decided', 'launch', 'approved', 'confirmed') inside clearly social or personal content is NOISE, not signal."
  - "'The weather decided to ruin our launch party' is SOCIAL_SMALLTALK + IGNORE"
  - "HUMAN_REVIEW: ONLY for sensitive content (credentials, personal, medical, financial)."
- **Registry:** none. The prompt carries no registry and no project description.
- **Not shown that later steps need** (gloss): the span alone is sent (five transcript lines, see Parameters), with no neighbouring spans. The prompt offers three admitting policies, but the system treats them the same (all three are extracted). The prompt does not say that a redaction removes the fragment from the text the extractor later reads.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `_GROUP_TARGET` | 5 lines | `app/services/segmentation_service.py:20` | a transcript span is five consecutive lines |
| `_GROUP_MIN` | 3 lines | `segmentation_service.py:21`, used l.55-57 | a remainder under three lines joins the last span |
| `_TRANSCRIPT_THRESHOLD` | 0.30 | `segmentation_service.py:19`, l.39-43 | share of speaker lines (pattern `_TRANSCRIPT_LINE`, l.15) at which a text is segmented as a transcript |
| admitting policies | `EXTRACT_TO_STATE`, `EXTRACT_AS_CANDIDATE`, `EVIDENCE_ONLY` | `memory_gatekeeper_service.py:240-244` | these create an evidence span; `IGNORE` and `HUMAN_REVIEW` do not |
| redactions | as returned by the model | `app/services/evidence_service.py:46`, l.78-85 | each fragment is replaced (first occurrence) before the evidence text is stored |
| guard | every redaction has `fragment` and `replacement` | `memory_gatekeeper_service.py:344-347` | otherwise the call fails (`LLMSeamError`, `app/llm/guarded.py:120-132`) |

- `_SCORE_MAP` (l.35-45) sets a stored relevance score. Gloss: nothing on the evaluated path filters on it.

##### Deterministic logic

- One decision per span, idempotent (`memory_gatekeeper_service.py:334-336`).
- Evidence is created for every admitted decision of the artifact (`evidence_service.py:63-75`).
- Gloss: what decides extraction is admitted (three policies) versus not admitted (two policies). The extractor runs on every evidence span (E).

##### Arm-specific

- No A1, A2 or WD switch acts here, and the prompt is the same in every arm. The A1 meeting-dates repair sets each artifact's source time at ingest (`_ingest_meeting` (`3320375:app/evaluation/ami/runner.py:744`), `_repair_source_times` (`3320375:app/evaluation/ami/runner.py:750`)); S uses that value.

#### E.6 Implementation entries

##### Evaluated prompt

- **Builder:** `_build_extraction_prompt`, `app/services/extraction_service.py:285-296`. Instructions: `extraction_instructions()`, l.271-282, from `EXTRACTION_BASE_INSTRUCTIONS`, l.177-211; the scalar key-selection sentence replaces the collection one (l.278-279). The registry is appended to the system message (l.288-292). User template `"Extract project-state claims from:\n\n{text}"` (l.295).
- **Hashes:** system template `725f1c00a2d1`, user template `c3635f7bb986`; the same in A0, A1, A2.
- **Response schema:** `LLMExtractionResponse`, strict (checked as above). Fields of a claim: `app/schemas/llm_extraction.py:14-21`.
- **Examples and example roles the prompt carries** (text as sent; l.177-211 with l.230-233):
  - "predicate: 'decided' | 'selected' | 'rejected' | 'proposed' | 'considered' | 'owns' | similar."
  - "polarity: NEGATIVE when the value is explicitly or implicitly rejected or ruled out — paraphrase negation counts ('off the table', 'ruled out', 'not going with', \"won't use\"). POSITIVE otherwise."
  - "modality: ASSERTED for firm decisions ('decided', 'locked in', 'going with'); HEDGED for tentative ('leaning', 'not locked in'); PROPOSED for candidates ('option', 'considering'); HYPOTHETICAL for future speculation."
  - "For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value."
  - "Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively."
  - The AMI role examples (l.201-207): "Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager'), predicate 'owns'."
  - "Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner."
  - Gloss: the four titles are the roles of the AMI scenario. Session check: none of them occurs in any EL2020 span, and the claims extracted with predicate `owns` carry values such as `PERSON14`.
- **How the registry enters:**
  - The whole active registry, not pruned. `self._registry()` (`extraction_service.py:565-569`) calls `StateKeyRegistryService.list_keys()` (`app/services/state_key_registry_service.py:42-49`: active keys, ordered by `state_key`).
  - Loaded once per `ExtractionService` instance (`_registry_cache`, l.375, l.566-568). The extraction endpoint makes one instance per call (`app/api/routes_projects.py:99-102`), and the harness calls it once per meeting (`app/evaluation/ami/runner.py:804`). So one registry per meeting: the traces show one key set per meeting in every run ("Registry carried per meeting", column "Ex key sets").
  - Line format, verbatim `app/services/extraction_service.py:217-220`:
    ```python
        return "\n".join(
            f"  - {k.state_key} [{k.value_type}, {k.key_cardinality}]: {k.label}. "
            f"{k.description} aliases: {k.aliases_json}"
            for k in registry
    ```
    Fields shown: key name, value type, cardinality, label, description, aliases. Not shown: negative aliases, example questions, family (`parent_key`), related keys, the values a key holds.
  - Empty registry (meeting a): the sentinel "(no registry keys provided — use state_key_hint: null)" (l.216).
- **Re-extraction of spans that gave no claims.** Idempotency skips only evidence that already has claims (l.389-392), and `extract_for_project` runs over all evidence of the project (l.635-637). So a span with no claims is sent again at every later meeting, with the larger registry. Their claims keep the source time of their own meeting (l.394-396). The docstring of `_said_at` notes this case (`app/services/resolution_service.py:288-293`).
- **Not shown that later steps need** (gloss):
  - The prompt asks for "extraction_confidence: 0.0–1.0." and says nothing more. The state rules use it as the last ranking key within a meeting and for tie conflicts (S).
  - No meeting identity, date, neighbouring span or current state is shown.
  - All keys are scalar (K2), but the prompt keeps the collection sentence quoted above.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `expansion_force_scalar` | True (default; confirmed by the sent text, see *Code check* in the Overview) | `app/core/config.py:137`; used `extraction_service.py:278-279` | which key-selection sentence the prompt carries |
| claim status | NEGATIVE → `REJECTED`; ASSERTED → `ACCEPTED`; otherwise `PROPOSED` | `extraction_service.py:654-659` | the stored claim status |
| claim identity | `make_claim_key(evidence_id, state_key or "", object_value, polarity)` | `extraction_service.py:667-672`; `app/db/repositories.py:164-173` | gloss: two claims of one span with the same hint, value and polarity are stored once |
| `extraction_confidence` default | 0.8 schema default. Unreachable under the strict schema, which makes every property required (`openai_llm.py:44-45`), except after a strict-to-non-strict downgrade on a 400 (`openai_llm.py:211-213`). Such a downgrade is not recorded: a 400 records no usage (`openai_llm.py:265-272`), `run.log` logs per call, not per attempt, and `trace.json` keeps no attempt envelope (a known limit, H) | `app/schemas/llm_extraction.py:21` | ranking input (S) |
| guard | every claim has a non-empty `object_value` | `extraction_service.py:545` | otherwise the call fails |
| source time | `artifact.created_at_source or artifact.ingested_at` | `extraction_service.py:396` | A0: ingestion clock (bug 6); A1, A2: meeting date (`repair_meeting_dates`) |
| source authority | `MEETING_DISCUSSION` = 30 for meeting transcripts | `app/core/enums.py:128`, `:137`; `app/services/artifact_ingestion_service.py:85-91` | the authority every claim carries (S) |

##### Deterministic logic

- Claims are persisted per span (`extraction_service.py:643-686`). Decisions, action items, risks and open questions are stored too (l.571-633). Gloss: these four are not on the state path.

##### Arm-specific

- **By arm:**
  - WD (`extraction_whole_decisions`) rewrites the instructions (`_whole_decision_instructions` (`3320375:app/services/extraction_service.py:264`)). No new call. Off in A0, A1 and A2.
  - `expansion_force_scalar` (`3320375:app/core/config.py:137`), on in every arm, also swaps a key-selection sentence of the extraction prompt (`expansion_force_scalar` (`3320375:app/services/extraction_service.py:278`)). Gloss: so the generator preference of D4.p5 reaches this prompt too.
  - A1 and A2 do not change this step. A2's support check later tests claims against their spans (S).
- **The WD instructions** (`extraction_whole_decisions`, `extraction_service.py:236-268`, applied l.280-281): `_PER_VALUE_SENTENCE` is replaced by `_PER_DECISION_SENTENCE` and `_WHOLE_DECISION_RULE` is appended. Code-derived system template hash `daf30b70d954…`. Its examples (l.248-260, verbatim): "(e.g. 'English and French at launch' rather than separate claims 'English' and 'French'; 'design freeze on Friday, bug fixes only afterwards' rather than 'Friday')" and "('40 dollars', not 'charge forty dollars for it')". The source comment (l.238-239, one comment joined across its line break): "The examples are generic on purpose: no development or test series supplies them."

#### K1.6 Implementation entries

##### Evaluated prompt

- **Seam and builder:** the extraction call of E; the same hashes.
- **Instructions** (text as sent; l.183, l.231-232):
  - "state_key_hint: the registry state_key the claim is about, or null if none fits."
  - "Key selection: map each claim to the MOST SPECIFIC matching registry key — the key about exactly this item/attribute, never a broad catch-all key. One claim per independent item."
  - The ownership sentence quoted in E.6 asks for a claim "keyed to the owner/assignment registry key". Gloss: a cold-start registry has no such key unless one was minted.
- **Registry:** as in E.6 (the whole registry, with the fields listed there).
- **Not shown** (gloss): the values each key already holds. So the hint cannot take into account whether the claim would rival a key's current value about another matter.

##### Deterministic logic

- The hint becomes the claim's key unchanged; nothing checks that it is registered (`extraction_service.py:661`, `:673`).
- A claim whose key is registered is never resolved again: the cold-start mapping skips it (`app/evaluation/ami/registry_expansion_eval.py:248-249`, `active_only=False`), and so does `resolve_state_key_for_claim` (`app/services/state_key_resolution_service.py:472-473`). Gloss: a hint to a registered key about another matter is kept whatever its matter.
- A hint to an unregistered key:
  - A0: the claim is filed under that key by the conflict pass (`app/services/conflict_service.py:134-158`; no definition, scalar path) and later mapped or parked by the expansion step (bug 5).
  - A1, A2: `repair_undefined_key_filing` returns noop instead (`conflict_service.py:152-153`, l.823-838).
  - Traces: the model also writes the literal key `null`. Conflict rows then give "Stage-23 repair (bug 5): no concept definition for 'null'; not filed".

##### Arm-specific

- **Under A1, A2, WD:** no prompt change. WD changes the extraction instructions, not the hint sentence.
- **Filing, by arm:**
  - A1: the bug-5 repair stops filing under a key with no definition (`_repair_undefined_key` (`3320375:app/services/conflict_service.py:823`)). No new call.
  - A2: the type check (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`), deterministic) can strip a hint whose key's type the value does not fit and send the claim back to the resolver (`_c2_reroute` (`3320375:app/services/conflict_service.py:899`)). No call at this step.
  - WD: none.

#### X.4 Arm-specific implementation across components

##### A1: the ten repair switches

Table: `app/core/cycle2_flags.py:86-151`; Settings fields `config.py:162-171`; RunConfig `runner.py:341-350`; the runner writes every switch to the environment (`runner.py:615-618`). In the runs, A0 already had the last two switches on.

| Switch | Bug | What it changes (summary from `cycle2_flags.py`) | Main code |
|---|---|---|---|
| `repair_negation_affirmation` | 1 | a value is ruled out when none of its positive claims survives the asserted negations; a ruled-out current value is superseded or rejected; a negation is never appended as support (l.87-97) | `resolution_service.py:288-375`, l.495-517, l.519-523, l.547-550; `conflict_service.py:208-225`, l.261-262, l.372, l.691-804, l.811-821, l.880-883 |
| `repair_proposal_lineage` | 2 | a proposal takes evidence, confidence and authority from the claim that supplied the winning value (l.98-103) | `conflict_service.py:359`, l.576-578, l.648-650, l.680-689, l.877-879; `repositories.py:409-420` |
| `repair_same_meeting_supersession` | 3 | the current value's own claims compete with its challengers (l.104-108) | `resolution_service.py:378-389`, l.662-673 |
| `repair_hedged_same_value` | 4 | with only hedged claims, a value equal to the current one changes nothing (l.109-113) | `resolution_service.py:392-396`, l.555-565 |
| `repair_undefined_key_filing` | 5 | a claim whose key has no definition is not filed (l.114-118) | `conflict_service.py:152-153`, l.823-838 |
| `repair_meeting_dates` | 6 | the meeting's date becomes the artifact's source time (l.119-124) | `runner.py:87-109`, l.744-778 |
| `repair_open_proposal_dedup` | 12 | an applied or expired proposal no longer blocks a new one with the same key (l.125-132) | `repositories.py:354-393`, l.436-438; `conflict_service.py:358`, l.605, l.671 |
| `repair_settle_before_confirm` | 13 | every key is evaluated again before confirmation; a pending proposal not produced again expires (l.133-140) | `runner.py:111-136`, l.833-836; `conflict_service.py:806-809`; `repositories.py:396-406`, l.439-440 |
| `repair_judge_rejection_status` | 7 (instrument) | the judge's gold string for rejection items states the expected status (l.141-144) | `app/evaluation/ami/judge_repairs.py:19-58`; on in A0, A1, A2 and RAG |
| `repair_dump_diagnostics` | 9, 10 (instrument) | state-dump traces matched per checkpoint; wrong-key diagnosis corrected (l.145-151) | `app/evaluation/ami/state_dump.py:99`, `:109`, `:124`, `:222`; on in A0, A1, A2 |

- Gloss: no repair changes a prompt text. The repairs change which claims are filed, what the engine returns, which proposals are raised and kept, and the source times.

##### A2: the four write contracts

| Contract | What it changes | Seam or LLM call added | Code |
|---|---|---|---|
| `filing_type_check` | before filing, a value that does not fit the key's declared type (numbers, dates, booleans, or a ';' enumeration under a scalar key) leaves the key; it is resolved again without that key, and parked for good after a second misfit | no LLM call; deterministic, logged as `filing_type_check` | `conflict_service.py:154-157`, l.899-924; `app/services/cycle2_filing.py:101-123`; `state_key_resolution_service.py:475-485`, l.508 |
| `resolution_same_meeting_conflict` | rival asserted values of equal authority from the same meeting become an open conflict, not a confidence contest | no LLM call; uses embeddings for value equivalence (cosine ≥ `answer_canonical_min_similarity` 0.80) | `resolution_service.py:472-475`, l.608-620, l.674-686; `conflict_service.py:403-406`, l.858-862, l.926-949; `cycle2_filing.py:54-76`; read side `answer_service.py:899-915` |
| `supersession_requires_new_evidence` | a challenger supersedes only with evidence and a meeting the current fact does not rest on | none; embeddings for equivalence as above | `resolution_service.py:274-279`, l.345-348; `conflict_service.py:850-856` |
| `filing_support_check` | a claim becomes a fact only if its own span establishes its value, status and time; an unsupported winner is parked and the key resolved again (up to 8 times) | the `claim_support_check` LLM seam, one call per claim, cached on the claim | `conflict_service.py:185-191`, l.213-218, l.270-284, l.643-646; `cycle2_filing.py:149-210` |

- The support-check prompt is under S.6.

##### WD: `extraction_whole_decisions`

- It changes only the extraction instructions (E.6): the per-value sentence is replaced, and the whole-decision rule is appended (`extraction_service.py:236-268`, l.280-281).
- No new seam. Code-derived system template hash `daf30b70d954…`. Not run in any evaluated arm (config blocks: `"extraction_whole_decisions": false`).
- Plan role: `cycle2_flags.py:61-64`, decisions D10 and D4.

---

## Sheet K1: key assignment at extraction

**Scope.**
- Routing losses whose misrouted claim, carrier or rival, was keyed by the extractor's hint. Amendment line 375: "Its path gives the boundary: a hint means key assignment at extraction; the resolver or expansion means key resolution and expansion."
- Oracle evidence, amendment line 369: "recovered by R: routing;" R-hint and R-resolver are evidence only, amendment line 204: "they do not set caused-at."
- Exception, amendment line 374: "where the displaced rival was about the same matter, R is not routing evidence, and caused-at is set from the page (listed)."
- Path undecided, amendment line 375: "If the page cannot decide, the code is *routing, path unclear* (possible implementation at both)." Use sheet K2 as well.
- Step type: an LLM output (the hint field of the extraction call) filed deterministically (K1.1). Routing has no model condition (amendment line 331).

**Candidate causes listed by the amendment** (amendment line 385):
- [K1-cause-1] "a hint to a registered key about another matter" (amendment line 385)
   - Decided by: criteria (ii) and (iii) and the page. Gloss: Step 2b gives this cause no condition by name; a recovery under (ii-h) maps to cause 2.
   - Entries to check: the hint becomes the claim's key unchecked, and a claim whose key is registered is never resolved again (K1.6, Deterministic logic); the instruction to map each claim to the most specific matching key, and the values each key holds not being shown (K1.6, Evaluated prompt).
- [K1-cause-2] "registry-conditioned hinting" (amendment line 385)
   - Decided by: probe (ii-h), the spans of hint-routed carriers and rivals re-extracted under (a) (control) and (b) (registry cut). The offline check, amendment line 250: "Hint-routed carriers have no resolver prompt; their check uses the registry in that meeting's extraction prompt."
   - Applicability: a case whose misfiled claims all lie on one path takes only that path's probe (line 257). A case with misfiled claims on both paths takes the joint condition (line 258).
   - Entries to check: the registry in the extraction prompt (E.6, How the registry enters).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- [K1-entry-1] The ownership sentence asks for a claim keyed to an owner or assignment key, which a cold-start registry lacks unless one was minted (K1.6).
- [K1-entry-2] The model also writes the literal key `null`; conflict rows record that no concept definition exists for it (K1.6).
- [K1-entry-3] A0 files a claim under an unregistered hint (bug 5); A1 and A2 do not (K1.6). A0 cases resting on a Phase B bug count as repaired, amendment line 309: "A0 cases model-coded to a Phase B bug count as repaired (Phase B) and enter no bound." Bug 5's design ground is 94c049d D4.p3 (K1-C2): filing a claim under a key with no concept definition contradicts the register, so bug 5 is a conformance defect, and its repair a conformance repair.
- [K1-entry-4] A2's type check can strip a hint and send the claim to the resolver (K1.6; X.4).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Design gives: the claim's content, and the existing concepts' descriptions, aliases, values and question examples (D4.p3; K1.3). D4.p3's matching covers the hint path, so criterion (ii) applies here. Values means the concept definition's canonical values (K1.3).
- Prompt shows: the span, and the whole registry with key name, value type, cardinality, label, description and aliases (E.6). Not shown: negative aliases, example questions, family, related keys, the values a key holds (E.6; K1.6).
- Gloss: question examples are a D4.p3 input that the hint prompt does not show. Canonical values are another: the hint prompt does not show them, and none exists in these runs, because the harness clears them on accept (K2.6c). That clearing is the implementation entry that empties the input. The values a key holds are not a D4.p3 input; the hint prompt does not show them either (K1.6, an implementation note).

**Conformance checklist:** K1-C1 to K1-C3 (K1.4); X-C2 (X.2).

**Disclosed limitation at 94c049d:** D4.p4: "neither establishes equivalence". This sentence cannot ground architectural weakness or a trade-off. A loss resting on it is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
- For a trade-off (B):
  - **D4.p2** (B) "DR7 makes an unmatched claim a normal case." "Discarding it keeps the schema coherent but loses novel state." "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning." "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition." "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
  - **D4.p4** (B) "This supports an empty initial registry without treating generated labels as research outcomes." "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
  - **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- The hint field of the extraction call is an LLM step with no model condition, so the page must also meet the condition of line 340, amendment line 340: "At an LLM step with no model condition," "architectural weakness or trade-off also requires the page to show that a correct output of that step, given its recorded inputs, would still have lost the value." "Otherwise the case is design or model, not separated."

**Retrospective entries here:** K1-R1 to K1-R4; D10 (E-R1); X-R6.

### Sheet K1: the 94c049d paragraphs this sheet names

**D4.p2**
- (B) "DR7 makes an unmatched claim a normal case."
- (B) "Discarding it keeps the schema coherent but loses novel state."
- (B) "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning."
- (B) "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition."
- (B) "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."

**D4.p3**
- (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion."
- (C) "Open extraction can leave the concept unassigned."
- (C) "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples."
- (C) "An expansion contains a candidate definition and its triggering evidence."
- (C) "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution."
- (C) "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence."
- (C) "Concept review and value confirmation are separate decisions."

**D4.p4**
- (B) "This supports an empty initial registry without treating generated labels as research outcomes."
- (B) "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
- (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- (L) "Review may itself merge distinct meanings or fail to recognise synonyms."

**T.rationale**
- (—) "\begingroup \small \setlength{\tabcolsep}{3pt} \renewcommand{\arraystretch}{1.15} \begin{longtable}{@{} >{\raggedright\arraybackslash}p{0.14\textwidth} >{\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}p{0.21\textwidth} >{\raggedright\arraybackslash}p{0.10\textwidth} >{\raggedright\arraybackslash}p{0.15\textwidth} >{\raggedright\arraybackslash}p{0.13\textwidth}@{}} \caption{Design-decision summary: alternatives and costs, not a ranking of architectures.} \label{tab:design-rationale}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endfirsthead \multicolumn{6}{l}{\tablename\ \thetable\ continued}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endhead \bottomrule \endfoot D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\"
- (—) "\addlinespace D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"
- (—) "\addlinespace D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- (—) "\addlinespace"
- (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- (—) "\addlinespace D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\"
- (—) "\addlinespace D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\"
- (—) "\addlinespace D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- (—) "\addlinespace D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- (—) "\addlinespace D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"
- (—) "\end{longtable} \endgroup"

### Sheet K1: the conformance requirements this sheet names

Each is a checklist item of this sheet, under its id.
- [K1-C1] A claim that fits no existing concept is neither forced into the nearest one nor discarded: it is retained, parked and proposed for expansion (D4.p2, D4.p3).
- [K1-C2] A claim enters ordinary state resolution under an existing concept, or after its concept is accepted or merged (D4.p3). Gloss: the register's reading of the release sentence. Filing a claim under a key with no concept definition contradicts it, so bug 5 is a conformance defect and its repair a conformance repair. The bug list quoted D10's wording for it (K1-R2).
- [K1-C3] Extraction may leave the concept unassigned (D4.p3).
- [X-C2] Records stay linked by evidence identifiers across boundaries; review and event records are kept (D9.p2, D9.p3).

### Sheet K1: the implementation entries this sheet points to

#### E.6 Implementation entries

##### Evaluated prompt

- **Builder:** `_build_extraction_prompt`, `app/services/extraction_service.py:285-296`. Instructions: `extraction_instructions()`, l.271-282, from `EXTRACTION_BASE_INSTRUCTIONS`, l.177-211; the scalar key-selection sentence replaces the collection one (l.278-279). The registry is appended to the system message (l.288-292). User template `"Extract project-state claims from:\n\n{text}"` (l.295).
- **Hashes:** system template `725f1c00a2d1`, user template `c3635f7bb986`; the same in A0, A1, A2.
- **Response schema:** `LLMExtractionResponse`, strict (checked as above). Fields of a claim: `app/schemas/llm_extraction.py:14-21`.
- **Examples and example roles the prompt carries** (text as sent; l.177-211 with l.230-233):
  - "predicate: 'decided' | 'selected' | 'rejected' | 'proposed' | 'considered' | 'owns' | similar."
  - "polarity: NEGATIVE when the value is explicitly or implicitly rejected or ruled out — paraphrase negation counts ('off the table', 'ruled out', 'not going with', \"won't use\"). POSITIVE otherwise."
  - "modality: ASSERTED for firm decisions ('decided', 'locked in', 'going with'); HEDGED for tentative ('leaning', 'not locked in'); PROPOSED for candidates ('option', 'considering'); HYPOTHETICAL for future speculation."
  - "For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value."
  - "Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively."
  - The AMI role examples (l.201-207): "Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager'), predicate 'owns'."
  - "Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner."
  - Gloss: the four titles are the roles of the AMI scenario. Session check: none of them occurs in any EL2020 span, and the claims extracted with predicate `owns` carry values such as `PERSON14`.
- **How the registry enters:**
  - The whole active registry, not pruned. `self._registry()` (`extraction_service.py:565-569`) calls `StateKeyRegistryService.list_keys()` (`app/services/state_key_registry_service.py:42-49`: active keys, ordered by `state_key`).
  - Loaded once per `ExtractionService` instance (`_registry_cache`, l.375, l.566-568). The extraction endpoint makes one instance per call (`app/api/routes_projects.py:99-102`), and the harness calls it once per meeting (`app/evaluation/ami/runner.py:804`). So one registry per meeting: the traces show one key set per meeting in every run ("Registry carried per meeting", column "Ex key sets").
  - Line format, verbatim `app/services/extraction_service.py:217-220`:
    ```python
        return "\n".join(
            f"  - {k.state_key} [{k.value_type}, {k.key_cardinality}]: {k.label}. "
            f"{k.description} aliases: {k.aliases_json}"
            for k in registry
    ```
    Fields shown: key name, value type, cardinality, label, description, aliases. Not shown: negative aliases, example questions, family (`parent_key`), related keys, the values a key holds.
  - Empty registry (meeting a): the sentinel "(no registry keys provided — use state_key_hint: null)" (l.216).
- **Re-extraction of spans that gave no claims.** Idempotency skips only evidence that already has claims (l.389-392), and `extract_for_project` runs over all evidence of the project (l.635-637). So a span with no claims is sent again at every later meeting, with the larger registry. Their claims keep the source time of their own meeting (l.394-396). The docstring of `_said_at` notes this case (`app/services/resolution_service.py:288-293`).
- **Not shown that later steps need** (gloss):
  - The prompt asks for "extraction_confidence: 0.0–1.0." and says nothing more. The state rules use it as the last ranking key within a meeting and for tie conflicts (S).
  - No meeting identity, date, neighbouring span or current state is shown.
  - All keys are scalar (K2), but the prompt keeps the collection sentence quoted above.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `expansion_force_scalar` | True (default; confirmed by the sent text, see *Code check* in the Overview) | `app/core/config.py:137`; used `extraction_service.py:278-279` | which key-selection sentence the prompt carries |
| claim status | NEGATIVE → `REJECTED`; ASSERTED → `ACCEPTED`; otherwise `PROPOSED` | `extraction_service.py:654-659` | the stored claim status |
| claim identity | `make_claim_key(evidence_id, state_key or "", object_value, polarity)` | `extraction_service.py:667-672`; `app/db/repositories.py:164-173` | gloss: two claims of one span with the same hint, value and polarity are stored once |
| `extraction_confidence` default | 0.8 schema default. Unreachable under the strict schema, which makes every property required (`openai_llm.py:44-45`), except after a strict-to-non-strict downgrade on a 400 (`openai_llm.py:211-213`). Such a downgrade is not recorded: a 400 records no usage (`openai_llm.py:265-272`), `run.log` logs per call, not per attempt, and `trace.json` keeps no attempt envelope (a known limit, H) | `app/schemas/llm_extraction.py:21` | ranking input (S) |
| guard | every claim has a non-empty `object_value` | `extraction_service.py:545` | otherwise the call fails |
| source time | `artifact.created_at_source or artifact.ingested_at` | `extraction_service.py:396` | A0: ingestion clock (bug 6); A1, A2: meeting date (`repair_meeting_dates`) |
| source authority | `MEETING_DISCUSSION` = 30 for meeting transcripts | `app/core/enums.py:128`, `:137`; `app/services/artifact_ingestion_service.py:85-91` | the authority every claim carries (S) |

##### Deterministic logic

- Claims are persisted per span (`extraction_service.py:643-686`). Decisions, action items, risks and open questions are stored too (l.571-633). Gloss: these four are not on the state path.

##### Arm-specific

- **By arm:**
  - WD (`extraction_whole_decisions`) rewrites the instructions (`_whole_decision_instructions` (`3320375:app/services/extraction_service.py:264`)). No new call. Off in A0, A1 and A2.
  - `expansion_force_scalar` (`3320375:app/core/config.py:137`), on in every arm, also swaps a key-selection sentence of the extraction prompt (`expansion_force_scalar` (`3320375:app/services/extraction_service.py:278`)). Gloss: so the generator preference of D4.p5 reaches this prompt too.
  - A1 and A2 do not change this step. A2's support check later tests claims against their spans (S).
- **The WD instructions** (`extraction_whole_decisions`, `extraction_service.py:236-268`, applied l.280-281): `_PER_VALUE_SENTENCE` is replaced by `_PER_DECISION_SENTENCE` and `_WHOLE_DECISION_RULE` is appended. Code-derived system template hash `daf30b70d954…`. Its examples (l.248-260, verbatim): "(e.g. 'English and French at launch' rather than separate claims 'English' and 'French'; 'design freeze on Friday, bug fixes only afterwards' rather than 'Friday')" and "('40 dollars', not 'charge forty dollars for it')". The source comment (l.238-239, one comment joined across its line break): "The examples are generic on purpose: no development or test series supplies them."

#### K1.6 Implementation entries

##### Evaluated prompt

- **Seam and builder:** the extraction call of E; the same hashes.
- **Instructions** (text as sent; l.183, l.231-232):
  - "state_key_hint: the registry state_key the claim is about, or null if none fits."
  - "Key selection: map each claim to the MOST SPECIFIC matching registry key — the key about exactly this item/attribute, never a broad catch-all key. One claim per independent item."
  - The ownership sentence quoted in E.6 asks for a claim "keyed to the owner/assignment registry key". Gloss: a cold-start registry has no such key unless one was minted.
- **Registry:** as in E.6 (the whole registry, with the fields listed there).
- **Not shown** (gloss): the values each key already holds. So the hint cannot take into account whether the claim would rival a key's current value about another matter.

##### Deterministic logic

- The hint becomes the claim's key unchanged; nothing checks that it is registered (`extraction_service.py:661`, `:673`).
- A claim whose key is registered is never resolved again: the cold-start mapping skips it (`app/evaluation/ami/registry_expansion_eval.py:248-249`, `active_only=False`), and so does `resolve_state_key_for_claim` (`app/services/state_key_resolution_service.py:472-473`). Gloss: a hint to a registered key about another matter is kept whatever its matter.
- A hint to an unregistered key:
  - A0: the claim is filed under that key by the conflict pass (`app/services/conflict_service.py:134-158`; no definition, scalar path) and later mapped or parked by the expansion step (bug 5).
  - A1, A2: `repair_undefined_key_filing` returns noop instead (`conflict_service.py:152-153`, l.823-838).
  - Traces: the model also writes the literal key `null`. Conflict rows then give "Stage-23 repair (bug 5): no concept definition for 'null'; not filed".

##### Arm-specific

- **Under A1, A2, WD:** no prompt change. WD changes the extraction instructions, not the hint sentence.
- **Filing, by arm:**
  - A1: the bug-5 repair stops filing under a key with no definition (`_repair_undefined_key` (`3320375:app/services/conflict_service.py:823`)). No new call.
  - A2: the type check (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`), deterministic) can strip a hint whose key's type the value does not fit and send the claim back to the resolver (`_c2_reroute` (`3320375:app/services/conflict_service.py:899`)). No call at this step.
  - WD: none.

#### K2.6 Implementation entries (part)

##### K2.6c Review: the harness reviewer, validation and release

- **Harness reviewer** (deterministic, harness). Acceptance `quality` (`registry_expansion_eval.py:290-295`, l.420-429). Verbatim, `app/evaluation/ami/informed_reviewer.py:74-90`:
  ```python
  #: What a reviewer expects a state key to look like: dotted snake_case, >= 2 segments.
  _KEY_SHAPE = re.compile(r"[a-z0-9_]+(\.[a-z0-9_]+)+")


  def _reviewer_would_accept(proposal) -> tuple[bool, str]:
      """Structural gate shared by the 'quality' arm and informed Tier 1: would a
      reasonable human reviewer approve this proposal on sight? Checks only what a
      reviewer can see on the review card — key shape, a label, and supporting
      evidence — never the gold ontology. Returns (accept, reject_reason)."""
      key = (proposal.proposed_state_key or "").strip()
      if not _KEY_SHAPE.fullmatch(key):
          return False, f"malformed state key {key!r} (want dotted snake_case, >= 2 segments)"
      if not (proposal.proposed_label or "").strip():
          return False, "no label"
      if not [t for t in (proposal.triggered_by_texts or []) if (t or "").strip()]:
          return False, "no supporting evidence text"
      return True, ""
  ```
  - A rejected proposal is only recorded; under `quality` no reject is submitted (`registry_expansion_eval.py:293-295`).
  - Accepted proposals go to `_accept_self_organized` (l.431-462): canonical values are cleared and unlisted values allowed (l.446-447). If the key already exists it is a merge, otherwise an accept.
  - Every pending proposal is reviewed again at every meeting (l.267).
- **Validation** (deterministic, system): `RegistryExpansionReviewService._validate_definition`, `app/services/registry_expansion_review_service.py:268-303`. Rules: a key of 2–4 segments (l.31-32); at most 10 canonical values; at least one alias, defaulted to the label (l.136-141); a valid cardinality; a known domain, or one named in the review note. A new key that duplicates an active key is refused (l.147-151). A failure leaves the proposal pending and is recorded as `accept_error` (`registry_expansion_eval.py:307-308`).
- **From the `coldstart.json` expansion logs:** accept errors were all `STATE_KEY_INVALID_FORMAT` on keys of five or more segments. Gloss: `_KEY_SHAPE` admits such keys and the validator refuses them, so the proposal stays pending and its parked claims are never released.
  - The records count reviews, not proposals: a stuck proposal is reviewed again at every meeting.
- **Merge** adds the proposal's aliases to the target key (`registry_expansion_review_service.py:217-262`, l.326-341). Merge recommendations carry no aliases (`registry_expansion_service.py:462`).
- **Release:** `ClaimReEvaluationService.release_parked_claims` (`app/services/claim_reevaluation_service.py:26-75`) sets each waiting claim's key and runs `ConflictService.evaluate_claim` (l.77-90).
- **Not on this path:** the informed reviewer's LLM tier (acceptance `informed` only, `registry_expansion_eval.py:320-327`); `expansion_auto_accept` (used only by `resolve_unmapped_claims`, `state_key_resolution_service.py:1006`, which the step endpoints the harness calls do not run; `app/api/routes_artifacts.py:135` is the `/process` endpoint); `expire_stale_proposals` (`registry_expansion_service.py:320`, no caller).

#### X.4 Arm-specific implementation across components

##### A1: the ten repair switches

Table: `app/core/cycle2_flags.py:86-151`; Settings fields `config.py:162-171`; RunConfig `runner.py:341-350`; the runner writes every switch to the environment (`runner.py:615-618`). In the runs, A0 already had the last two switches on.

| Switch | Bug | What it changes (summary from `cycle2_flags.py`) | Main code |
|---|---|---|---|
| `repair_negation_affirmation` | 1 | a value is ruled out when none of its positive claims survives the asserted negations; a ruled-out current value is superseded or rejected; a negation is never appended as support (l.87-97) | `resolution_service.py:288-375`, l.495-517, l.519-523, l.547-550; `conflict_service.py:208-225`, l.261-262, l.372, l.691-804, l.811-821, l.880-883 |
| `repair_proposal_lineage` | 2 | a proposal takes evidence, confidence and authority from the claim that supplied the winning value (l.98-103) | `conflict_service.py:359`, l.576-578, l.648-650, l.680-689, l.877-879; `repositories.py:409-420` |
| `repair_same_meeting_supersession` | 3 | the current value's own claims compete with its challengers (l.104-108) | `resolution_service.py:378-389`, l.662-673 |
| `repair_hedged_same_value` | 4 | with only hedged claims, a value equal to the current one changes nothing (l.109-113) | `resolution_service.py:392-396`, l.555-565 |
| `repair_undefined_key_filing` | 5 | a claim whose key has no definition is not filed (l.114-118) | `conflict_service.py:152-153`, l.823-838 |
| `repair_meeting_dates` | 6 | the meeting's date becomes the artifact's source time (l.119-124) | `runner.py:87-109`, l.744-778 |
| `repair_open_proposal_dedup` | 12 | an applied or expired proposal no longer blocks a new one with the same key (l.125-132) | `repositories.py:354-393`, l.436-438; `conflict_service.py:358`, l.605, l.671 |
| `repair_settle_before_confirm` | 13 | every key is evaluated again before confirmation; a pending proposal not produced again expires (l.133-140) | `runner.py:111-136`, l.833-836; `conflict_service.py:806-809`; `repositories.py:396-406`, l.439-440 |
| `repair_judge_rejection_status` | 7 (instrument) | the judge's gold string for rejection items states the expected status (l.141-144) | `app/evaluation/ami/judge_repairs.py:19-58`; on in A0, A1, A2 and RAG |
| `repair_dump_diagnostics` | 9, 10 (instrument) | state-dump traces matched per checkpoint; wrong-key diagnosis corrected (l.145-151) | `app/evaluation/ami/state_dump.py:99`, `:109`, `:124`, `:222`; on in A0, A1, A2 |

- Gloss: no repair changes a prompt text. The repairs change which claims are filed, what the engine returns, which proposals are raised and kept, and the source times.

##### A2: the four write contracts

| Contract | What it changes | Seam or LLM call added | Code |
|---|---|---|---|
| `filing_type_check` | before filing, a value that does not fit the key's declared type (numbers, dates, booleans, or a ';' enumeration under a scalar key) leaves the key; it is resolved again without that key, and parked for good after a second misfit | no LLM call; deterministic, logged as `filing_type_check` | `conflict_service.py:154-157`, l.899-924; `app/services/cycle2_filing.py:101-123`; `state_key_resolution_service.py:475-485`, l.508 |
| `resolution_same_meeting_conflict` | rival asserted values of equal authority from the same meeting become an open conflict, not a confidence contest | no LLM call; uses embeddings for value equivalence (cosine ≥ `answer_canonical_min_similarity` 0.80) | `resolution_service.py:472-475`, l.608-620, l.674-686; `conflict_service.py:403-406`, l.858-862, l.926-949; `cycle2_filing.py:54-76`; read side `answer_service.py:899-915` |
| `supersession_requires_new_evidence` | a challenger supersedes only with evidence and a meeting the current fact does not rest on | none; embeddings for equivalence as above | `resolution_service.py:274-279`, l.345-348; `conflict_service.py:850-856` |
| `filing_support_check` | a claim becomes a fact only if its own span establishes its value, status and time; an unsupported winner is parked and the key resolved again (up to 8 times) | the `claim_support_check` LLM seam, one call per claim, cached on the claim | `conflict_service.py:185-191`, l.213-218, l.270-284, l.643-646; `cycle2_filing.py:149-210` |

- The support-check prompt is under S.6.

##### WD: `extraction_whole_decisions`

- It changes only the extraction instructions (E.6): the per-value sentence is replaced, and the whole-decision rule is appended (`extraction_service.py:236-268`, l.280-281).
- No new seam. Code-derived system template hash `daf30b70d954…`. Not run in any evaluated arm (config blocks: `"extraction_whole_decisions": false`).
- Plan role: `cycle2_flags.py:61-64`, decisions D10 and D4.

---

## Sheet K2: key resolution and expansion

**Scope.**
- Routing losses whose misrouted claim was routed by the resolver or by expansion (line 375, quoted on sheet K1). Oracle evidence and the same-matter exception as on sheet K1.
- Amendment line 251: "Expansion-routed misfilings (the resolver returned no key, and expansion reused or created one) are not probed. They are coded from the trace, under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry."
- Gloss: losses where a claim stays parked because its concept is never accepted (D4.p4's delayed availability) also belong here when the page shows it.
- Step type: mixed (K2.1). The resolver and candidate generation are LLM steps with no model condition (amendment line 331; for candidate generation, line 251: expansion-routed misfilings are not probed).

**Candidate causes listed by the amendment** (amendment line 386):
- [K2-cause-1] "the shortlist or prune excluded a fitting key" (amendment line 386)
   - Decided by: the offline check whether the gold-holding key, or a fitting one, was in the resolver prompt; and probe (ii-r), the resolver-routed carriers and rivals re-resolved with the unpruned registry against the recorded prompt as control.
   - Entries to check: `_prompt_registry` (the embedding part at 8 and 0.30, the lexical part with `STOPWORDS`, the whole registry at or below 12 keys) (K2.6a); the parameter table (K2.6, Parameters).
- [K2-cause-2] "the harness reviewer accepted a near-duplicate or over-broad key" (amendment line 386)
   - Decided by: the trace and the page (line 251).
   - Entries to check: `_reviewer_would_accept` checks only key shape, a label and evidence text; no reject is submitted under `quality`; accepted keys have canonical values cleared; a merge adds the proposal's aliases to the target key; every pending proposal is reviewed again at every meeting (K2.6c).
- [K2-cause-3] "a reuse or similarity threshold merged a new matter into an existing key" (amendment line 386)
   - Decided by: criterion (iii), from the trace (line 251).
   - Entries to check: semantic reuse at `expansion_reuse_threshold` 0.80 (K2.6b, step 3); the alias merge, plain substring containment on the whole span with the first match in key-name order (K2.6b, step 1; mapped to this cause at signing).
   - Design to read it against: D4.p4 (K2.2 gloss). K2-R3's sentence on semantic reuse is retrospective.

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- [K2-entry-1] `_KEY_SHAPE` admits keys of five or more segments that the validator refuses; such proposals stay pending and their parked claims are never released (K2.6c; no listed cause, left to the pilot).
- [K2-entry-2] A claim parked at an earlier meeting is never routed again, even when the registry later gains a fitting key; it reaches state only through its own proposal's acceptance or merge (K2.1).
- [K2-entry-3] At meeting a every write-path resolver call lists no key, so every claim goes to expansion (K2.6a; no listed cause, left to the pilot).
- [K2-entry-4] The first remaining primary key is taken; supporting keys, `needs_clarification` and `confidence` are not used on the write path (K2.6a). On the read path broad questions append the supporting keys (R.6).
- [K2-entry-5] The routed text is the claim's subject and value; the span is sent only when both are empty; polarity, modality and the values each key holds are not shown (K2.6a).
- [K2-entry-6] The expansion generator sees only key names, domains and families (K2.6b). Criterion (ii) does not apply to it (see below); a page can still note this entry.
- [K2-entry-7] A2's type-check re-routes (K2.6, Arm-specific; X.4).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Resolver.
  - Design gives: the claim's content; the existing concepts' descriptions, aliases, values and question examples (D4.p3; K2.3). Values means the concept definition's canonical values (K1.3).
  - Prompt shows: the claim's subject and value; for the pruned registry, key name, label, description, aliases, negative aliases and value type (K2.6a). Not shown: cardinality, family, example questions, the values a key holds.
  - Example questions never reach the prompt. They enter only deterministically: through the embedding profile behind the shortlist, and, for a text that `is_broad_list_question` accepts, through the rule candidates (K2.6a).
  - Values: the prompt does not show canonical values, and none exists in these runs, because the harness clears them on accept (K2.6c). That clearing is the implementation entry that empties the input. The input would also reach the embedding profile, empty in these runs (K2.6a).
  - The values a key holds are not a D4.p3 input. Claim routing never sees them (the context digest is off, K2.6a); an implementation note.
- Expansion generator. Criterion (ii) does not apply to expansion-routed misfilings, which amendment line 251 codes "under criterion (iii) (reuse or similarity threshold) or the harness-reviewer entry", and a generator merge reaches the registry only through the harness reviewer's acceptance. The lines below are an implementation entry a page can note.
  - Design gives: the claim and its triggering evidence; the preference for scalar concepts with family metadata (D4.p5; K2.3).
  - Prompt shows: the claim's value, subject and predicate, the evidence as context only, and the names of all keys, domains and families. Not shown: the labels, descriptions, aliases and values of existing keys (K2.6b). Neither canonical nor held values are shown.
- Concept review.
  - Design gives: the expansion, a candidate definition with its triggering evidence; acceptance criteria are not specified (K2.3).
  - The harness reviewer checks: key shape, a label, supporting evidence text (K2.6c).

**Conformance checklist:** K2-C1 to K2-C6 (K2.4); X-C1 and X-C2 (X.2). D4.p4's sentence that matching does not establish equivalence is a disclosed limitation (K2.4), not a checklist item; criterion (iii) is read against it (cause 3).

**Disclosed limitations at 94c049d:** matching does not establish equivalence, and review may merge distinct meanings or miss synonyms (D4.p4, its last two sentences); the reviewer shapes which concepts survive (D4.p6, its last two sentences). They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies. Stated costs, which are (B) and quotable below: parking delays availability (D4.p4); fragmentation and near-duplicates (D4.p5); waiting for concept review (D1.p4, D6.p4).

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D4.p3** (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion." "Open extraction can leave the concept unassigned." "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples." "An expansion contains a candidate definition and its triggering evidence." "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution." "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence." "Concept review and value confirmation are separate decisions."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D4.p2** (B) "DR7 makes an unmatched claim a normal case." "Discarding it keeps the schema coherent but loses novel state." "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning." "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition." "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."
  - **D4.p4** (B) "This supports an empty initial registry without treating generated labels as research outcomes." "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
  - **D4.p5** (B) "The representation choice within an open schema remains substantial." "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics." "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
  - **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation." "It does not establish that fine-grained concepts are universally better."
  - **D6.p4** (B) "The costs are intrinsic." "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error." "Deferral and parking can make a correctly extracted fact unavailable when needed."
  - **T.rationale** (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- The resolver and candidate generation are LLM steps with no model condition. At either step the page must also meet the condition of line 340 (quoted on sheet K1); otherwise the case is design or model, not separated.

**Retrospective entries here:** K2-R1 to K2-R7; D10 (K2-R4); X-R1; X-R6.

### Sheet K2: the 94c049d paragraphs this sheet names

**D1.p4**
- (B) "The rationale is to make commitments inspectable before their consequences persist."
- (B) "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost."
- (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- (B) "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."

**D4.p2**
- (B) "DR7 makes an unmatched claim a normal case."
- (B) "Discarding it keeps the schema coherent but loses novel state."
- (B) "Forcing it into the nearest concept preserves a value at the risk of giving it the wrong meaning."
- (B) "Requiring an externally authored schema provides stable concepts and clear membership rules, but adds prior modelling work and violates the study's cold-start condition."
- (B) "Generating a concept immediately avoids those costs but can make every model-generated category authoritative."

**D4.p3**
- (C) "ProjectMemory chooses delayed commitment: retain the claim, park it, and propose a reviewed expansion."
- (C) "Open extraction can leave the concept unassigned."
- (C) "Matching uses the claim's content and existing concepts' descriptions, aliases, values, and question examples."
- (C) "An expansion contains a candidate definition and its triggering evidence."
- (C) "Concept review can accept, edit, reject, or merge it; acceptance or merging releases waiting claims into ordinary state resolution."
- (C) "A rejected expansion discards waiting claims from this release workflow without erasing their source evidence."
- (C) "Concept review and value confirmation are separate decisions."

**D4.p4**
- (B) "This supports an empty initial registry without treating generated labels as research outcomes."
- (B) "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
- (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- (L) "Review may itself merge distinct meanings or fail to recognise synonyms."

**D4.p5**
- (B) "The representation choice within an open schema remains substantial."
- (B) "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics."
- (B) "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
- (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions."
- (C) "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."

**D4.p6**
- (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation."
- (B) "It does not establish that fine-grained concepts are universally better."
- (—) "Development diagnostics found that changing registry shape did not automatically remove retrieval misses (Section~\ref{sec:design-evolution})."
- (—) "The intended consequence is useful state coverage from an empty registry, assessed by the cold-start protocol in Section~\ref{subsec:eval-cold-start}."
- (—) "Fragmentation and family quality remain diagnostic properties; reference key-name agreement is not a correctness endpoint."
- (L) "Moreover, the gold-informed reviewer can influence which concepts survive."
- (L) "Cold start must therefore be interpreted together with confirmation sensitivity, rather than as fully unaided schema discovery."

**D6.p4**
- (B) "The costs are intrinsic."
- (B) "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error."
- (B) "Deferral and parking can make a correctly extracted fact unavailable when needed."
- (L) "An edited proposal is projected without rerunning authority and temporal resolution, so the reviewer's correction can bypass parts of that policy."
- (—) "Neither the review record nor the presence of evidence establishes that the evidence was actually inspected."

**T.rationale**
- (—) "\begingroup \small \setlength{\tabcolsep}{3pt} \renewcommand{\arraystretch}{1.15} \begin{longtable}{@{} >{\raggedright\arraybackslash}p{0.14\textwidth} >{\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}p{0.21\textwidth} >{\raggedright\arraybackslash}p{0.10\textwidth} >{\raggedright\arraybackslash}p{0.15\textwidth} >{\raggedright\arraybackslash}p{0.13\textwidth}@{}} \caption{Design-decision summary: alternatives and costs, not a ranking of architectures.} \label{tab:design-rationale}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endfirsthead \multicolumn{6}{l}{\tablename\ \thetable\ continued}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endhead \bottomrule \endfoot D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\"
- (—) "\addlinespace D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"
- (—) "\addlinespace D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- (—) "\addlinespace"
- (B) "D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- (—) "\addlinespace D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\"
- (—) "\addlinespace D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\"
- (—) "\addlinespace D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- (—) "\addlinespace D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- (—) "\addlinespace D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"
- (—) "\end{longtable} \endgroup"

### Sheet K2: the conformance requirements this sheet names

Each is a checklist item of this sheet, under its id.
- [K2-C1] An unmatched claim is retained and parked against a proposed expansion; it is neither discarded nor force-matched (D4.p2, D4.p3).
- [K2-C2] An expansion carries a candidate definition and its triggering evidence (D4.p3).
- [K2-C3] Concept review can accept, edit, reject or merge; acceptance or merging releases the waiting claims into ordinary state resolution (D4.p3).
- [K2-C4] A rejected expansion discards its waiting claims from release but keeps their source evidence (D4.p3).
- [K2-C5] Concept review is separate from value confirmation (D4.p3).
- [K2-C6] The generator prefers scalar concepts and attaches family metadata; collections stay possible (D4.p5).
- [X-C1] Each boundary writes its own record: evidence, claim, proposal, fact (D1.p3).
- [X-C2] Records stay linked by evidence identifiers across boundaries; review and event records are kept (D9.p2, D9.p3).

### Sheet K2: the implementation entries this sheet points to

#### K2.6 Implementation entries

##### K2.6a Resolver, write path

- **Seam:** `state_key_resolution`. Read path in R.
- **Builder:** `_build_resolution_prompt`, `state_key_resolution_service.py:224-249`; system `RESOLUTION_SYSTEM_PROMPT`, l.108-133. Called from `resolve()` (l.272-357) via `resolve_state_key_for_claim` (l.441-531).
- **Hashes:** system `fb29d2fadfef`, user template `6e907422766a`; the same in A0, A1, A2 and on both paths. The user message starts with "Resolve this text to registry keys." in every call, so no context digest was sent (`context_digest`, pinned off by `runner.py:607-609`).
- **Example the prompt carries** (text as sent; l.126-128): "Example: 'Redis is the datastore for session state' uses 'datastore' (an alias for architecture.database.primary) but Redis-as-session-store is NOT the primary operational database." Gloss: an example from the database worked example of the rule baseline (`extraction_service.py:8-12`), not from the meeting domain.
- **Text sent:** the claim's subject and value joined by " — " (l.487-492); the evidence span only when both are empty. The intent hint comes from keyword rules (`detect_intent`, l.533-549).
- **How the registry enters:** `_prompt_registry` (l.676-705) over `list_keys()`. Verbatim, l.689-705:
  ```python
        if not embedding_candidates:
            return registry_keys
        if len(registry_keys) <= get_settings().resolver_prune_threshold:
            return registry_keys
        keep = {key for key, _ in embedding_candidates}
        normalized_text = self._normalize(text)
        tokens = self._tokens(normalized_text)
        for definition in registry_keys:
            if definition.state_key in keep:
                continue
            lexical = (
                self._alias_score(definition.aliases_json, normalized_text, tokens)[0] > 0
                or bool(self._key_tokens(definition) & set(tokens) - STOPWORDS)
            )
            if lexical or definition.supported_intents_json.get(intent.value) == "primary":
                keep.add(definition.state_key)
        return [d for d in registry_keys if d.state_key in keep]
  ```
  - **Embedding part** (`_embedding_candidates`, l.625-643): the cosine between the text and each key's profile; keys at or above `embedding_min_similarity` (0.30), best first, at most `embedding_top_k` (8). Key profile (l.663-674): key name with dots as spaces, label, description, domain, aliases, example questions, canonical values. Key vectors are cached per registry signature (l.645-661).
  - **Lexical part:** a positive alias score (the normalised alias is a substring of the text, or all its tokens are text tokens; l.829-845), or any shared token between the text and the key's name, label, description and domain (`_key_tokens`, l.876-878) outside `STOPWORDS` (l.42-65), or the key declares the intent primary.
  - **Whole registry** when no key reaches 0.30, or when the registry has at most `resolver_prune_threshold` (12) keys.
  - Gloss: `STOPWORDS` (l.42-65) does not contain common words such as "and", "in", "on", "with" or "this", so the lexical part admits any key whose description shares such a word with the claim text.
  - Line format, verbatim l.230-235:
    ```python
    registry_lines = "\n".join(
        f"  - {k.state_key}: {k.label}. {k.description} "
        f"[aliases: {k.aliases_json}; negative_aliases: {k.negative_aliases_json}; "
        f"value_type: {k.value_type}]"
        for k in registry
    )
    ```
    Fields shown: key name, label, description, aliases, negative aliases, value type. Not shown: cardinality, family, example questions, the values a key holds.
    - Example questions are present on every minted key (`state.json`). They never reach the prompt; no trace holds the field. They enter only deterministically, in two ways: through the embedding profile behind the shortlist (`_key_profile`, l.663-674), and, for a text that `is_broad_list_question` accepts (l.88-94), through the rule candidates (`_example_overlap`, l.777-780, l.869-874; reached through l.347-355; R.6).
    - Canonical values: no key in these runs has any, because the harness clears them on accept (K2.6c). They are the values D4.p3 names as a matching input (K1.3), so the clearing empties that input.
  - At meeting a every write-path call lists no key (the registry is empty, so the model cannot return a key and every claim goes to expansion).
- **Use of the output:** keys outside the registry are dropped (l.313, l.898-915). The first remaining primary key is taken (l.508-510). Gloss: on the write path, supporting keys, `needs_clarification` and `confidence` are not used. On the read path, supporting keys are used: broad questions append them to the context pack (R.6, Retrieval).
- **Not shown that later steps need** (gloss): the span, the claim's polarity and modality, and the values each key holds. Filing then puts the claim among that key's claims (S).

##### K2.6b Expansion: what happens to a claim the resolver did not map

Order in `handle_unmapped_claim` (`app/services/registry_expansion_service.py:117-166`):

1. **Alias merge** (deterministic). `find_by_alias` runs on the claim's whole evidence span (l.127-135, span from `_evidence_text`, l.474-478). Verbatim, `state_key_registry_service.py:57-64`:
   ```python
       def find_by_alias(self, text: str) -> list[models.StateKeyDefinition]:
           normalized_text = self._normalize(text)
           matches: list[models.StateKeyDefinition] = []
           for definition in self.list_keys():
               aliases = definition.aliases_json + [definition.label, definition.state_key.replace(".", " ")]
               if any(self._normalize(alias) in normalized_text for alias in aliases):
                   matches.append(definition)
           return matches
   ```
   The first match, in key-name order, gets a merge recommendation (`registry_expansion_service.py:132-135`, l.439-472). It runs under every reuse policy except `disabled` (l.127-131).
   - Gloss: plain substring containment on the whole span, not on the claim. A short alias also matches inside other words; for example, `organization.document.audience` in a0_r1 has the alias "for".
   - A generated candidate that names an existing key is merged by the harness (K2.6c).
2. **Candidate generation** (LLM). Seam `registry_expansion_generation`. Its messages are not recorded in the trace.
   - Calls: all `llm_assisted`, all served by gpt-5.4-mini-2026-03-17.
   - Builder: `LLMExpansionGenerator.generate_expansion_candidate`, `app/llm/expansion_generator.py:387-411`. System text `expansion_system_prompt(force_scalar=True, families=True)`, l.354-365, from l.321-335, l.339-344, l.345-351 (both flags at their defaults, `config.py:137`, `:144`; every key in every `state.json` is scalar and has a family). Code-derived hash `f570f53ad992…`.
   - Examples it carries (verbatim, l.339-344): "Never propose a collection — a list of independent items (features, owners, options) is one key PER ITEM (e.g. 'product.feature.voice_control', not 'product.features')." And l.345-348: "(e.g. 'product.feature', 'project.action', 'product.spec', 'project.risk')". Gloss: AMI product-design examples.
   - Instruction (l.326-328): "Prefer an existing key from existing_state_keys over inventing a new one; if one fits, set proposed_state_key to it and list it in proposed_related_keys so the reviewer can MERGE."
   - User template (claim-scoped branch), verbatim l.438-450:
     ```python
                return (
                    "Propose a state key for THIS single claim (one concept only):\n"
                    f"  value:     {request.claim_value}\n"
                    f"  subject:   {request.claim_subject or '(none)'}\n"
                    f"  predicate: {request.claim_predicate or '(none)'}\n\n"
                    f"{digest}"
                    f"{granularity}\n\n"
                    "Supporting evidence — CONTEXT ONLY:\n"
                    f"{evidence}\n\n"
                    f"Existing state keys: {keys}\n"
                    f"Existing domains: {domains}\n"
                    f"{families_line}"
                )
     ```
     The granularity sentence (`expansion_concept_level` pinned off, `runner.py:610-612`), l.430-433: "Do NOT widen the key to cover other topics mentioned in the evidence; the key must be about the claim above."
   - How the registry enters: the names of all active keys, all domains and all families (`registry_expansion_service.py:363`, l.374-386). Not shown: the labels, descriptions and aliases of existing keys, and the values they hold. Gloss: the generator is asked to prefer an existing key, but it sees only key names.
   - On failure the generator silently falls back to rules (`expansion_generator.py:406-411`), and the method is still logged as `llm_assisted` (`registry_expansion_service.py:388-389`).
   - Schema: `ExpansionCandidateWithFamilyResponse`, strict. Cardinality is forced to scalar after the call (`expansion_generator.py:304-318`).
3. **Semantic reuse** (deterministic, embeddings). `_dedup_match` (`registry_expansion_service.py:269-296`): the cosine between the candidate's profile and each pending proposal's and registry key's profile (key, label, description, aliases; l.262-267). The best match at or above `expansion_reuse_threshold` (0.80) is reused: the claim joins that proposal (l.217-220), or a merge recommendation into that key is made (l.221-223).
4. **Exact attach**: a pending proposal with the same proposed key takes the claim (l.226-231).
5. **New proposal** (l.233-246). The claim is parked against the proposal in every case (l.141-151).

##### K2.6c Review: the harness reviewer, validation and release

- **Harness reviewer** (deterministic, harness). Acceptance `quality` (`registry_expansion_eval.py:290-295`, l.420-429). Verbatim, `app/evaluation/ami/informed_reviewer.py:74-90`:
  ```python
  #: What a reviewer expects a state key to look like: dotted snake_case, >= 2 segments.
  _KEY_SHAPE = re.compile(r"[a-z0-9_]+(\.[a-z0-9_]+)+")


  def _reviewer_would_accept(proposal) -> tuple[bool, str]:
      """Structural gate shared by the 'quality' arm and informed Tier 1: would a
      reasonable human reviewer approve this proposal on sight? Checks only what a
      reviewer can see on the review card — key shape, a label, and supporting
      evidence — never the gold ontology. Returns (accept, reject_reason)."""
      key = (proposal.proposed_state_key or "").strip()
      if not _KEY_SHAPE.fullmatch(key):
          return False, f"malformed state key {key!r} (want dotted snake_case, >= 2 segments)"
      if not (proposal.proposed_label or "").strip():
          return False, "no label"
      if not [t for t in (proposal.triggered_by_texts or []) if (t or "").strip()]:
          return False, "no supporting evidence text"
      return True, ""
  ```
  - A rejected proposal is only recorded; under `quality` no reject is submitted (`registry_expansion_eval.py:293-295`).
  - Accepted proposals go to `_accept_self_organized` (l.431-462): canonical values are cleared and unlisted values allowed (l.446-447). If the key already exists it is a merge, otherwise an accept.
  - Every pending proposal is reviewed again at every meeting (l.267).
- **Validation** (deterministic, system): `RegistryExpansionReviewService._validate_definition`, `app/services/registry_expansion_review_service.py:268-303`. Rules: a key of 2–4 segments (l.31-32); at most 10 canonical values; at least one alias, defaulted to the label (l.136-141); a valid cardinality; a known domain, or one named in the review note. A new key that duplicates an active key is refused (l.147-151). A failure leaves the proposal pending and is recorded as `accept_error` (`registry_expansion_eval.py:307-308`).
- **From the `coldstart.json` expansion logs:** accept errors were all `STATE_KEY_INVALID_FORMAT` on keys of five or more segments. Gloss: `_KEY_SHAPE` admits such keys and the validator refuses them, so the proposal stays pending and its parked claims are never released.
  - The records count reviews, not proposals: a stuck proposal is reviewed again at every meeting.
- **Merge** adds the proposal's aliases to the target key (`registry_expansion_review_service.py:217-262`, l.326-341). Merge recommendations carry no aliases (`registry_expansion_service.py:462`).
- **Release:** `ClaimReEvaluationService.release_parked_claims` (`app/services/claim_reevaluation_service.py:26-75`) sets each waiting claim's key and runs `ConflictService.evaluate_claim` (l.77-90).
- **Not on this path:** the informed reviewer's LLM tier (acceptance `informed` only, `registry_expansion_eval.py:320-327`); `expansion_auto_accept` (used only by `resolve_unmapped_claims`, `state_key_resolution_service.py:1006`, which the step endpoints the harness calls do not run; `app/api/routes_artifacts.py:135` is the `/process` endpoint); `expire_stale_proposals` (`registry_expansion_service.py:320`, no caller).

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `resolver_embeddings_enabled` | true (`--resolver-embeddings`; config block `"resolver_embeddings": true`) | `config.py:65`; set by `runner.py:604-606` | the embedding part of the shortlist is on |
| `embedding_top_k` | 8 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:82`; `state_key_resolution_service.py:643` | at most eight embedding candidates |
| `embedding_min_similarity` | 0.30 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:83`; `state_key_resolution_service.py:641` | a key below this cosine is not an embedding candidate; with none above it, the whole registry is sent |
| `resolver_prune_threshold` | 12 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:86`; `state_key_resolution_service.py:691` | at or below 12 keys the whole registry is sent |
| `STOPWORDS` | 22 words | `state_key_resolution_service.py:42-65` | words that do not count as shared tokens in the lexical part |
| first primary key | `fitting[0]` | `state_key_resolution_service.py:508-510` | the key the claim is filed under |
| `expansion_reuse_policy` | `semantic` (config block) | `config.py:70`; `registry_expansion_eval.py:218-230` | alias merge, semantic reuse and exact attach are all on |
| `expansion_reuse_threshold` | 0.80 (config block `0.8`) | `config.py:71`; `runner.py:298`; `registry_expansion_service.py:44`, l.296 | cosine at which a candidate reuses a proposal or merges into a key |
| alias merge target | first matching key in name order | `state_key_registry_service.py:42-49`, l.57-64; `registry_expansion_service.py:133-135` | which key an alias-matched claim goes to |
| `_KEY_SHAPE` | two or more dotted segments | `informed_reviewer.py:75` | harness accept test |
| `_STATE_KEY_RE` | 2–4 segments | `registry_expansion_review_service.py:31-32` | validator accept test |
| canonical values on accept | cleared | `registry_expansion_eval.py:446-447` | keys are open-vocabulary, so `canonical_match` is never called (no such trace step) |
| `expansion_force_scalar`, `concept_families_enabled` | true, true | `config.py:137`, `:144` | scalar keys only; every key gets a family |
| `_MERGE_CONFIDENCE` | 0.4 | `registry_expansion_service.py:36` | stored on merge recommendations; gloss: not used to decide |

##### Deterministic logic (checklist)

- Shortlist and pruning: `_embedding_candidates` (l.625-643), `_key_profile` (l.663-674), `_prompt_registry` (l.676-705).
- Output filtering: `_strip_out_of_registry` (l.898-915); first fitting key (l.508-510).
- Parked claims skipped at later meetings: `registry_expansion_eval.py:231`, l.246-247, l.493-498 (K2.1).
- Parking and expansion: `handle_unmapped_claim` (`registry_expansion_service.py:117-166`), `find_by_alias` (`state_key_registry_service.py:57-64`), `_dedup_match` (l.269-296), `find_or_create_proposal` (l.196-246).
- Harness reviewer: `_reviewer_would_accept` (`informed_reviewer.py:78-90`), `_accept_self_organized` (`registry_expansion_eval.py:431-462`).
- Validation, merge and release: `registry_expansion_review_service.py:119-182`, l.217-262, l.268-303; `claim_reevaluation_service.py:26-90`.

##### Arm-specific

- **A1:** no new call, and no change to the resolver prompt or logic. In every arm the cold-start step already sends claims whose key is not registered to the resolver; the bug-5 repair only stops their filing under the undefined key (K1).
- **A2** (`filing_type_check`): type-check re-routes come back here with the rejected keys excluded (`type_rejected` (`3320375:app/services/state_key_resolution_service.py:485`), `fitting` (`3320375:app/services/state_key_resolution_service.py:508`)). Keys the claim's value did not fit are removed from the result, and a claim parked for good is not resolved (`state_key_resolution_service.py:475-485`, l.508). This adds resolver calls.
- **WD:** none.

#### R.6 Implementation entries

##### Evaluated prompts

- **Question resolution:** the resolver of K2.6a with the question as text. Same hashes (`fb29d2fadfef`, `6e907422766a`). Registry via `_prompt_registry` with the intent from `detect_intent`.
- **Grounding:** seam `question_answering_grounding`. Builder `_build_grounding_prompt`, `app/services/answer_service.py:90-118`; system `GROUNDING_SYSTEM_PROMPT`, l.53-87. Hashes: system `76eb844f30d6`, user template `163a9efe1ef6`; the same in A0, A1, A2.
  - It is skipped for provenance questions (l.202-203).
  - It sees the question, the drafted answer, the citations (evidence texts) and the current facts (key, value, status, review state).
  - Its `revised_answer` replaces the answer prose (l.249-253). Gloss: an LLM step after the state that can remove asserted values from the prose; the structured payload is kept.
  - Example (text as sent; l.79-81): "An abstaining answer ('I do not see a confirmed…', 'I was unable to find relevant project state…') asserts nothing and is trivially grounded (grounded=true, unsupported_sentences=[])."
  - `review_state_present` was False in every call.
- **Not shown** (gloss): the resolver sees key definitions but not their values, so a question about a value held under an oddly named key depends on the widening steps below. Nor does it see the keys' example questions; they enter only deterministically (K2.6a; Deterministic widening below).

##### Deterministic widening and answer logic (checklist)

- **After the LLM**, in `resolve()`:
  - Change questions add the keys that declare `change_explanation` primary (`state_key_resolution_service.py:322-336`). Gloss: minted keys declare no intents (every key in every `state.json` has empty `supported_intents`), so this adds nothing here.
  - Broad list questions (`is_broad_list_question`, l.88-94) add the rule-based candidates after the LLM's own picks, up to `BROAD_LIST_MAX_KEYS` = 10 (l.76, l.347-355).
    - The candidates are every key with a positive rule score (`_compute_rule_based_response`, l.551-621; `_score_key`, l.745-807), plus the embedding candidates with a bonus of cosine × `embedding_score_weight` 5.0 (`config.py:84`; l.707-743). They are sorted by score, with no other minimum. A negative alias with no positive alias disqualifies a key (l.758-760, l.725-731).
    - Score parts live in these runs: alias match, 4.5–5.5 for a substring match and 3.4–4.2 for a token-subset match (l.829-845); key-token overlap, 0.75 per token, at most 3 (l.771-775); example-question overlap, 0.5 per token, at most 2 (l.777-780, l.869-874); the decision-domain bonus 3.5 for DECISION_LOOKUP (l.803-805).
    - Inert in these runs: the intent bonuses 2.5 and 1.0 (l.794-801; minted keys declare no intents) and the canonical score 2.5 (l.766-769, l.847-856; no key has canonical values).
    - Gloss: so example questions reach question routing here, deterministically, and never through the prompt (K2.6a).
- **Retrieval** (`app/services/retrieval_service.py:97-203`):
  - Broad questions pass the resolver's candidate list to `_widen_broad_primary_keys` (l.114-117, l.290-308): candidates scoring at least `_BROAD_CANDIDATE_RATIO` 0.25 of the top, up to `_BROAD_MAX_KEYS` 10 (l.41-42).
    - On the LLM path the response's `candidate_keys` is empty: the field is internal and is not in the schema sent to the model (`app/schemas/llm_resolution.py:8-11`, l.33-40). `_to_resolve_result` then substitutes the primary keys and the supporting keys, all at one score, the LLM confidence (`state_key_resolution_service.py:918-923`). For a broad question the primary keys already include the rule candidates, capped at 10 (l.347-355 of that file).
    - So the 0.25 ratio is inert. The net effect is that the resolver LLM's supporting keys are appended until there are 10 keys.
  - Keys whose current values match the question focus at cosine ≥ `_VALUE_MATCH_COSINE` 0.55 are added, up to 6 (l.47-48, l.210-260). Focus terms are words of three or more characters outside `_FOCUS_STOP` (l.60-75).
  - Broad questions add family siblings, up to `_FAMILY_MAX_SIBLINGS` 10 per family (l.264-287).
  - Facts: the current fact of each scalar key (l.142-154).
- **Answer** (`_generate_answer`, `answer_service.py:644-984`):
  - The focus key (l.580-586).
  - Broad versus specific (l.676-678). Focus terms: words of four or more characters outside `_FOCUS_STOPWORDS` (l.355-369, l.389-413), which include AMI words ("product", "feature", "device", "remote", "control").
    - The focus key's own label and alias words are removed from the focus terms (`_question_focus_terms`, l.405-413).
    - A question with no focus terms left counts as broad (l.676-678). The scalar focus gate runs only for a specific question that keeps focus terms (l.937-939). So this removal decides both broad versus specific and whether the gate runs.
  - The relevance filter for list-like answers: cosine ≥ `answer_relevance_min_similarity` 0.42 (`config.py:89`; l.416-455).
  - Canonicalisation of near-duplicates at `answer_canonical_min_similarity` 0.80 (`config.py:95`; l.463-524), with no cap (`answer_canonical_max_items` 0, `config.py:101`).
  - Rejection questions read REJECTED facts (l.734-788). Change questions read the facts first established in the latest meeting (l.589-634, l.794-822).
    - When `_REJECTION_Q_RE` matches (l.376-380, l.739), the current facts of any resolved key whose name contains `reject` are read as ruled-out values too (l.750-754). `get_current_collection` filters by status only (`app/db/repositories.py:294-305`), so scalar keys qualify.
  - **Scalar focus gate** (l.930-952): a specific question whose focus matches no candidate value is answered "unknown", and the held facts move to `near_matches` (l.319-321).
  - Answer status (l.260-280); mapped to the scorer's status by `runner.py:1067-1071`.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `embedding_top_k`, `embedding_min_similarity`, `resolver_prune_threshold` | 8, 0.30, 12 | as in K2.6 | the question-time shortlist |
| `BROAD_LIST_MAX_KEYS` | 10 | `state_key_resolution_service.py:76` | cap on the keys a broad question resolves to |
| `embedding_score_weight` | 5.0 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:84` | weight of embedding similarity in the rule candidates used for widening |
| rule-scorer weights | alias 4.5–5.5 (substring) or 3.4–4.2 (token subset); key-token overlap 0.75 per token, at most 3; example overlap 0.5 per token, at most 2; decision-domain bonus 3.5 (DECISION_LOOKUP); intent bonuses 2.5 and 1.0 and canonical score 2.5, inert here | `state_key_resolution_service.py:745-807`, l.829-874 | which keys fill the broad-question slots |
| `_BROAD_CANDIDATE_RATIO`, `_BROAD_MAX_KEYS` | 0.25, 10 | `retrieval_service.py:41-42` | broad-question widening; the 0.25 ratio is inert on the LLM path, where all candidates share one score |
| `_VALUE_MATCH_COSINE`, `_VALUE_MATCH_MAX_KEYS` | 0.55, 6 | `retrieval_service.py:47-48` | keys pulled in by value match |
| `_FAMILY_MAX_SIBLINGS` | 10 | `retrieval_service.py:264` | family widening cap |
| `answer_relevance_min_similarity` | 0.42 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:89`; `answer_service.py:454` | which held values count as relevant; drives the scalar focus gate |
| `answer_canonical_min_similarity` | 0.80 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:95`; `answer_service.py:490` | near-duplicate values merged in answers; also A2's value equivalence (X.4) |
| `answer_canonical_max_items` | 0 (no cap; default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:101` | cap on listed values |
| `_FOCUS_STOPWORDS` | as listed | `answer_service.py:355-369` | which question words count as focus |

##### Arm-specific

- No arm adds a model call here. The read contracts (`answer_evidence_fallback`; `answer_answerability_check`, with its key_answerability seam) are off in A0, A1 and A2.
- **Under A1, A2, WD:** no prompt change. A2 adds a disputed answer for open same-meeting conflicts (`answer_service.py:899-915`).

#### X.4 Arm-specific implementation across components

##### A1: the ten repair switches

Table: `app/core/cycle2_flags.py:86-151`; Settings fields `config.py:162-171`; RunConfig `runner.py:341-350`; the runner writes every switch to the environment (`runner.py:615-618`). In the runs, A0 already had the last two switches on.

| Switch | Bug | What it changes (summary from `cycle2_flags.py`) | Main code |
|---|---|---|---|
| `repair_negation_affirmation` | 1 | a value is ruled out when none of its positive claims survives the asserted negations; a ruled-out current value is superseded or rejected; a negation is never appended as support (l.87-97) | `resolution_service.py:288-375`, l.495-517, l.519-523, l.547-550; `conflict_service.py:208-225`, l.261-262, l.372, l.691-804, l.811-821, l.880-883 |
| `repair_proposal_lineage` | 2 | a proposal takes evidence, confidence and authority from the claim that supplied the winning value (l.98-103) | `conflict_service.py:359`, l.576-578, l.648-650, l.680-689, l.877-879; `repositories.py:409-420` |
| `repair_same_meeting_supersession` | 3 | the current value's own claims compete with its challengers (l.104-108) | `resolution_service.py:378-389`, l.662-673 |
| `repair_hedged_same_value` | 4 | with only hedged claims, a value equal to the current one changes nothing (l.109-113) | `resolution_service.py:392-396`, l.555-565 |
| `repair_undefined_key_filing` | 5 | a claim whose key has no definition is not filed (l.114-118) | `conflict_service.py:152-153`, l.823-838 |
| `repair_meeting_dates` | 6 | the meeting's date becomes the artifact's source time (l.119-124) | `runner.py:87-109`, l.744-778 |
| `repair_open_proposal_dedup` | 12 | an applied or expired proposal no longer blocks a new one with the same key (l.125-132) | `repositories.py:354-393`, l.436-438; `conflict_service.py:358`, l.605, l.671 |
| `repair_settle_before_confirm` | 13 | every key is evaluated again before confirmation; a pending proposal not produced again expires (l.133-140) | `runner.py:111-136`, l.833-836; `conflict_service.py:806-809`; `repositories.py:396-406`, l.439-440 |
| `repair_judge_rejection_status` | 7 (instrument) | the judge's gold string for rejection items states the expected status (l.141-144) | `app/evaluation/ami/judge_repairs.py:19-58`; on in A0, A1, A2 and RAG |
| `repair_dump_diagnostics` | 9, 10 (instrument) | state-dump traces matched per checkpoint; wrong-key diagnosis corrected (l.145-151) | `app/evaluation/ami/state_dump.py:99`, `:109`, `:124`, `:222`; on in A0, A1, A2 |

- Gloss: no repair changes a prompt text. The repairs change which claims are filed, what the engine returns, which proposals are raised and kept, and the source times.

##### A2: the four write contracts

| Contract | What it changes | Seam or LLM call added | Code |
|---|---|---|---|
| `filing_type_check` | before filing, a value that does not fit the key's declared type (numbers, dates, booleans, or a ';' enumeration under a scalar key) leaves the key; it is resolved again without that key, and parked for good after a second misfit | no LLM call; deterministic, logged as `filing_type_check` | `conflict_service.py:154-157`, l.899-924; `app/services/cycle2_filing.py:101-123`; `state_key_resolution_service.py:475-485`, l.508 |
| `resolution_same_meeting_conflict` | rival asserted values of equal authority from the same meeting become an open conflict, not a confidence contest | no LLM call; uses embeddings for value equivalence (cosine ≥ `answer_canonical_min_similarity` 0.80) | `resolution_service.py:472-475`, l.608-620, l.674-686; `conflict_service.py:403-406`, l.858-862, l.926-949; `cycle2_filing.py:54-76`; read side `answer_service.py:899-915` |
| `supersession_requires_new_evidence` | a challenger supersedes only with evidence and a meeting the current fact does not rest on | none; embeddings for equivalence as above | `resolution_service.py:274-279`, l.345-348; `conflict_service.py:850-856` |
| `filing_support_check` | a claim becomes a fact only if its own span establishes its value, status and time; an unsupported winner is parked and the key resolved again (up to 8 times) | the `claim_support_check` LLM seam, one call per claim, cached on the claim | `conflict_service.py:185-191`, l.213-218, l.270-284, l.643-646; `cycle2_filing.py:149-210` |

- The support-check prompt is under S.6.

##### WD: `extraction_whole_decisions`

- It changes only the extraction instructions (E.6): the per-value sentence is replaced, and the whole-decision rule is appended (`extraction_service.py:236-268`, l.280-281).
- No new seam. Code-derived system template hash `daf30b70d954…`. Not run in any evaluated arm (config blocks: `"extraction_whole_decisions": false`).
- Plan role: `cycle2_flags.py:61-64`, decisions D10 and D4.

---

## Sheet S: state rules (with A2's contracts and support check)

**Scope.**
- Losses that surface at `filed` (A2 parks), `proposed`, `applied`, `current` or `status`, where the page or an oracle puts the cause in the state rules.
- Oracle evidence, amendment line 371: "not recovered by E+R\*: state rules, transcript or evaluation."
- A2, amendment line 376: "a contract whose leave-one-out recovers the row sets caused-at to the state rules (that contract)."
- No probe-type alternative applies, amendment line 339: "Where no probe-type alternative applies, alternatives are ruled out under (ii)–(iv) and the page as above."
- Step type: deterministic (S.1). A2's support check is an LLM step with no model condition (amendment line 331).

**Candidate causes listed by the amendment** (amendment line 387):
- [S-cause-1] "the settle expired a correct proposal" (amendment line 387)
   - A1 and A2 only. Decided by: the trace and the page.
   - Entries to check: `repair_settle_pending`, one pass before each confirmation with no time window; a pending proposal the pass does not return again expires (S.6, Rules and Parameters; X.4, `repair_settle_before_confirm`).
- [S-cause-2] "any state behaviour contradicting the register" (amendment line 387)
   - Decided by: the conformance checklist below, against the rules of S.6.

**Conformance checklist** (S.4; the rule of S.6 to compare is a gloss):
- Promotion and negation: S-C1 to S-C4. Compare E1, Rule 1 and Rule 2 (S.6).
- Collections: S-C5. Not reached; every key in these runs is scalar.
- Resolution: S-C6 to S-C11. Compare the ranking key, Rules 3 to 5, `DISSENT_THRESHOLD` (S.6).
- Proposal and confirmation: S-C12 to S-C15. Compare Proposals and Confirmation (S.6).
- Projection: S-C16 to S-C18. Compare Projection (S.6).
- Records and links: X-C1 and X-C2 (X.2).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- [S-entry-1] Within one meeting, authority and source time are equal, so `extraction_confidence` decides, and equal confidences make a tie conflict; the extraction prompt does not define it (S.6, Rule 3; E.6).
- [S-entry-2] Value identity in the engine is the exact raw string for every key in these runs, since no key has canonical values; case and version tokens are not normalised. Lower case is compared only in E1, in reject projection and on the unused collection path. A2's equivalence (normalised equality or cosine ≥ 0.80) does not reach rule 3's tie test (S.6, Rules).
- [S-entry-3] Proposals are deduplicated by key, value and type; in A0 any earlier proposal with the same key blocks a new one (bug 12) (S.6).
- [S-entry-4] The structural value confirmation: `scrub_gold_value`, the rule of a word of at least four characters, and `_STOPWORDS` with AMI words (S.6). It is an implementation entry, marked harness, like the concept reviewer; no listed cause, left to the pilot.
- [S-entry-5] A reject proposal demotes a current fact with the same value compared by lower case; the current fact is the most recently updated current fact of the key (S.6, Projection).
- [S-entry-6] Source time: the ingestion clock in A0 (bug 6), the meeting date in A1 and A2 (E.6; X.4).
- [S-entry-7] The order of evaluation: the repaired settle is the only pass that evaluates every key with all its claims just before confirmation (S.6).
- [S-entry-8] The A1 repair rules (X.4). Bug 3's rule (the current value's own claims compete; an exact tie keeps the current value) is retrospective design: its wording rests on the 5de9911 per-key sentence (S-R3). An A1 state-rule loss whose only design ground is this rule is implementation choice if an alternative consistent with the 94c049d text meets (i)–(iv), and unclear otherwise; it is tallied in the retrospective column (amendment lines 348–349).

**A0.** Line 309 (quoted on sheet K1) applies. The Phase B bugs whose repairs act at this boundary are 1, 2, 3, 4, 6, 12 and 13 (gloss; X.4; S-R10, S-R11).

**A2's contracts** (retrospective design, S-R9; implementation, X.4):
- Each contract's leave-one-out can set caused-at (line 376 above).
- An open same-meeting conflict is coded held: conflict decision (S-R12).
- [S-entry-9] Support check (`filing_support_check`), an LLM step with no model condition:
  - Specified (retrospective, S-R9): that the linked span establishes the claim's value, commitment status and time.
  - Prompt shows: the span, the key's label only, the value and a status phrase. Not shown: the key's description, the rival values, the meeting (S.6).
  - Criterion (ii) compares this prompt with the contract's retrospective wording too, so the meeting missing from the prompt is a checklist item. The alternative must still be consistent with the 94c049d text (amendment line 348).
- [S-entry-10] Type check: deterministic (K1.6; X.4).
- [S-entry-11] Same-meeting conflict and new-evidence rules: deterministic, with embedding equivalence at 0.80 (S.6, Arm-specific; X.4).

**Disclosed limitations at 94c049d:** D3.p3 (the affirmation check: the sentence on negating the current value, and the legacy-policy sentence), D5.p5, D5.p6's first sentence, D6.p4's edited-proposal sentence, D6.p5, D7.p3's fallback sentences, D7.p5's non-atomic projection, D9.p4, D9.p5. They are listed in S.4. They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies.

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence. The sentence of D3.p3 on negating the current value is a commitment, but it is a disclosed limitation here (above), so it is not listed.
- For architectural weakness (C) (D3.p4 and D3.p5's collection rules bind no evaluated key; D7.p4's first sentence binds collections only):
  - **D3.p3** (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values." "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value." "Confirmation can accept that proposal while preserving its unconfirmed epistemic status." "Explicit negation does not justify inventing a replacement." "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
  - **D5.p2** (C) "ProjectMemory selects an authority-gated temporal policy, leaving unresolved cases reviewable."
  - **D5.p3** (C) "The governing principle is that authority determines eligibility to supersede and recency orders temporally eligible evidence." "In the scalar policy, a challenger must have at least the current fact's authority and a source time no earlier than the fact's validity start." "Eligible challengers are ranked by authority, source time, and extraction confidence." "Authority thus retains precedence within the eligible set; recency does not override a higher eligible authority." "The same ranking selects an initial asserted positive candidate." "Different initial values tied on all three dimensions produce a conflict."
  - **D5.p4** (C) "Checking eligibility before ranking matters." "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered." "Lower-authority dissent does not overwrite current state." "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict." "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat." "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."
  - **D6.p2** (C) "ProjectMemory instead routes new values, replacements, and current-default rejection outcomes through a reviewable proposal and a separate confirmation operation:" "machine interpretation $\rightarrow$ proposal $\rightarrow$ confirmation $\rightarrow$ projection."
  - **D6.p3** (C) "The project-specific application is to expose the proposed value, concept, prior value, target status, evidence, and reason before projection." "Confirmation can accept, reject, edit, defer, or request more evidence." "Its review record is stored separately from the proposal and before the requested projection." "An existing fact can also be placed under review without immediately deleting it." "Review identifies a responsibility and contestability boundary; its occurrence does not establish truth."
  - **D7.p2** (C) "ProjectMemory instead preserves current and superseded facts, validity bounds, and replacement links."
  - **D7.p3** (C) "An accepted scalar replacement closes the prior fact's validity interval, marks it superseded, creates a successor with a backward supersession link, and completes the predecessor's forward link." "The winning claim's source time is carried as the proposal's effective time and becomes the new validity start; the predecessor's validity end uses the same boundary."
  - **D7.p4** (C) "Collections retain independent members instead of superseding siblings." "Rejection also differs from positive replacement." "Applying rejection can demote a matching current row to rejected and close its validity, or record a ruled-out alternative without displacing another current value." "This branch does not construct the predecessor--successor pair of a scalar replacement." "A rejected proposal, by contrast, records a review decision without creating a rejected fact about the project."
  - **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts." "Normal projection copies proposal evidence identifiers to the fact." "Application events connect proposals with facts and record the actor." "Citations expose stored evidence text and source identifiers." "This adapts provenance principles; it is not a claim of PROV conformance."
- For a trade-off (B):
  - **D1.p4** (B) "The rationale is to make commitments inspectable before their consequences persist." "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost." "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review." "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."
  - **D2.p4** (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
  - **D5.p2** (B) "Newest-statement-wins is transparent but treats later mentions as replacements." "Highest-extraction-confidence-wins confuses interpretation confidence with authority." "Highest-authority-wins preserves priority but can privilege stale evidence." "Human-only resolution permits contextual judgement at the cost of reviewing every contradiction."
  - **D5.p6** (B) "The intended consequence is stable state under casual dissent, replacement by eligible later commitments, and exposed unresolved conflicts."
  - **D6.p2** (B) "Direct model mutation minimises delay." "Confidence-threshold approval retains automation but uses an admission rule whose reliability must be established." "Manual entry keeps responsibility explicit while moving capture and maintenance back to the user."
  - **D6.p4** (B) "The costs are intrinsic." "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error." "Deferral and parking can make a correctly extracted fact unavailable when needed."
  - **D6.p6** (B) "The intended consequence is that changing confirmation policy changes which interpretations become answerable, making quality and availability trade-offs observable."
  - **D7.p2** (B) "For DR2 and DR3, overwriting a value makes current retrieval simple but loses its prior validity." "Appending every value without status preserves the record while making each question reconstruct currency."
  - **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
  - **D7.p5** (B) "It costs additional transitions and consistency obligations."
  - **T.rationale** (B) "D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\" "D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\" "D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- For conflicts, D5.p2's sentence on leaving unresolved cases reviewable (above; S-R4 gloss).
- A2's support check is an LLM step with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1).

**Retrospective entries here:** S-R1 to S-R12; X-R1; X-R2; X-R3; X-R4; X-R6.

### Sheet S: the 94c049d paragraphs this sheet names

**D1.p4**
- (B) "The rationale is to make commitments inspectable before their consequences persist."
- (B) "Separate records also preserve the evidence needed to challenge an answer or diagnose where information was lost."
- (B) "The cost is additional storage, coordination, processing latency, and two forms of unavailability: evidence can fail admission, and an admitted claim can wait for concept or value review."
- (B) "A claim that is never extracted cannot be recovered by reviewing its nonexistent proposal."

**D2.p4**
- (—) "The implemented threshold is permissive within the admitted set."
- (—) "Policies named state extraction, candidate extraction, and evidence-only all create evidence that reaches extraction."
- (—) "Evidence-only is therefore \emph{not} an enforced prohibition on state extraction."
- (B) "This avoids making retained context unusable, a problem documented during development, but leaves resolution and confirmation responsible for preventing inappropriate promotion."
- (L) "Local transcript windows further bound interpretation: a commitment completed outside the window can be missed."
- (L) "The normal ingestion path does not invoke the separate discourse-linking mechanism to repair such omissions."

**D3.p3**
- (C) "For scalar concepts, asserted positive claims are eligible to propose confirmed current values."
- (C) "Where no asserted positive candidate exists, a proposed, hedged, or hypothetical positive claim can instead propose an unconfirmed value."
- (C) "Confirmation can accept that proposal while preserving its unconfirmed epistemic status."
- (C) "Explicit negation does not justify inventing a replacement."
- (C) "Under current development defaults, an asserted negation of an alternative can create a proposal for a rejected fact."
- (—) "Negating the current value additionally passes the resolver's authority and affirmation checks."
- (L) "With the legacy negation policy, exclusion instead makes the current fact ambiguous and opens a question for review."

**D3.p4**
- (—) "There is a consequential version boundary for collections."
- (—) "The earlier mechanism gave proposed and negative material a confirmed membership target and relied on concept meaning and confirmation to prevent incorrect promotion."
- (—) "That limitation is evidenced in the earlier code and subsequent test changes; it does not describe the current branch."
- (—) "Current collection proposals distinguish asserted positive members, unconfirmed positive members, and asserted negative members targeting rejected status."
- (—) "Hedged negation is dissent; rejection of an existing member also requires sufficient authority."

**D3.p5**
- (—) "Member-level status reduces one ambiguity without making collections equivalent to scalar resolution."
- (—) "An agreeing positive claim adds support to an existing member without automatically upgrading an unconfirmed member."
- (L) "Membership still depends on correctly interpreted concept meaning, and heterogeneous content can enter the same broad collection."
- (L) "Extraction can misclassify modality or negation in either model."
- (—) "DR1 and DR4 are therefore only partially realised across the full lifecycle."
- (—) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
- (—) "Status and unknown questions directly target this behavior; rejection questions and development lifecycle probes cover only the negative transitions represented in their inputs."

**D4.p4**
- (—) "This supports an empty initial registry without treating generated labels as research outcomes."
- (—) "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
- (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- (L) "Review may itself merge distinct meanings or fail to recognise synonyms."

**D5.p2**
- (—) "DR2 and DR3 require a response to newer evidence contradicting accepted state."
- (B) "Newest-statement-wins is transparent but treats later mentions as replacements."
- (B) "Highest-extraction-confidence-wins confuses interpretation confidence with authority."
- (B) "Highest-authority-wins preserves priority but can privilege stale evidence."
- (B) "Human-only resolution permits contextual judgement at the cost of reviewing every contradiction."
- (C) "ProjectMemory selects an authority-gated temporal policy, leaving unresolved cases reviewable."

**D5.p3**
- (C) "The governing principle is that authority determines eligibility to supersede and recency orders temporally eligible evidence."
- (C) "In the scalar policy, a challenger must have at least the current fact's authority and a source time no earlier than the fact's validity start."
- (C) "Eligible challengers are ranked by authority, source time, and extraction confidence."
- (C) "Authority thus retains precedence within the eligible set; recency does not override a higher eligible authority."
- (C) "The same ranking selects an initial asserted positive candidate."
- (C) "Different initial values tied on all three dimensions produce a conflict."

**D5.p4**
- (C) "Checking eligibility before ranking matters."
- (C) "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered."
- (C) "Lower-authority dissent does not overwrite current state."
- (C) "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict."
- (C) "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat."
- (C) "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."

**D5.p5**
- (—) "The policy is reproducible but incomplete."
- (L) "Authority is assigned at source artifact level, not inferred reliably per statement."
- (L) "Two participants in one meeting therefore normally inherit the same authority."
- (L) "Source time is the artifact timestamp, falling back to ingestion time; it need not identify when a reported decision took effect."
- (L) "In addition, the explicit tie-to-conflict check applies when no current fact exists."
- (L) "The supersession branch selects a maximum without an equivalent check for tied incompatible challengers, so conflict handling is not uniformly complete."
- (L) "Negation uses different checks: its current-value branch lacks the positive-supersession temporal gate, and an earlier positive claim can block a relevant negation through the affirmation check."

**D5.p6**
- (L) "These limitations qualify both requirements."
- (B) "The intended consequence is stable state under casual dissent, replacement by eligible later commitments, and exposed unresolved conflicts."
- (—) "Checkpoint and change questions partially evaluate those consequences."
- (—) "The AMI workflow normally assigns the same discussion authority to every transcript, so it does not substantively test organisational authority hierarchies."
- (—) "Resolver tests provide diagnostic evidence for selected authority and time cases; they do not establish that this model matches real project governance."

**D6.p2**
- (—) "DR6 concerns the transition from fallible interpretation to accepted state."
- (B) "Direct model mutation minimises delay."
- (B) "Confidence-threshold approval retains automation but uses an admission rule whose reliability must be established."
- (B) "Manual entry keeps responsibility explicit while moving capture and maintenance back to the user."
- (C) "ProjectMemory instead routes new values, replacements, and current-default rejection outcomes through a reviewable proposal and a separate confirmation operation:"
- (—) "\begin{center} \small"
- (C) "machine interpretation $\rightarrow$ proposal $\rightarrow$ confirmation $\rightarrow$ projection."
- (—) "\end{center}"

**D6.p3**
- (—) "Human--AI interaction guidance supports making errors correctable and limiting system action under uncertainty \citep{amershi2019guidelines}."
- (C) "The project-specific application is to expose the proposed value, concept, prior value, target status, evidence, and reason before projection."
- (C) "Confirmation can accept, reject, edit, defer, or request more evidence."
- (C) "Its review record is stored separately from the proposal and before the requested projection."
- (C) "An existing fact can also be placed under review without immediately deleting it."
- (C) "Review identifies a responsibility and contestability boundary; its occurrence does not establish truth."

**D6.p4**
- (B) "The costs are intrinsic."
- (B) "Review adds workload and latency, requires reviewers to be available, and can introduce disagreement or error."
- (B) "Deferral and parking can make a correctly extracted fact unavailable when needed."
- (L) "An edited proposal is projected without rerunning authority and temporal resolution, so the reviewer's correction can bypass parts of that policy."
- (—) "Neither the review record nor the presence of evidence establishes that the evidence was actually inspected."

**D6.p5**
- (—) "There is also an enforcement gap."
- (L) "Normal confirmation records review before application, but the separately exposed apply operation accepts pending, drafted, deferred, and already accepted proposals without checking for an accepting review."
- (L) "The legacy exclusion branch also changes a fact to ambiguous during resolution."
- (L) "The repository therefore supports a controlled workflow but does not enforce a universal invariant that every state mutation has passed review."
- (—) "DR6 is partially satisfied; claims about the evaluated workflow must not be extended to every caller."

**D6.p6**
- (B) "The intended consequence is that changing confirmation policy changes which interpretations become answerable, making quality and availability trade-offs observable."
- (—) "Section~\ref{subsec:eval-oracle-confirmation} and the paired-system protocol define autonomous and privileged-review comparisons and acceptance-policy sensitivity."
- (—) "These partially evaluate the mediation hypothesis."
- (—) "Review counts, model calls, and tokens are available as workload diagnostics, but they do not measure human reading time, reviewer accuracy, acceptable delay, or the cost of keeping a review process staffed."

**D7.p2**
- (B) "For DR2 and DR3, overwriting a value makes current retrieval simple but loses its prior validity."
- (B) "Appending every value without status preserves the record while making each question reconstruct currency."
- (C) "ProjectMemory instead preserves current and superseded facts, validity bounds, and replacement links."
- (—) "Temporal database research distinguishes validity in the modelled domain from the history of its database representation \citep{anselma2026bitemporal}."
- (L) "The artifact adopts this distinction without implementing a complete bitemporal query system."

**D7.p3**
- (C) "An accepted scalar replacement closes the prior fact's validity interval, marks it superseded, creates a successor with a backward supersession link, and completes the predecessor's forward link."
- (C) "The winning claim's source time is carried as the proposal's effective time and becomes the new validity start; the predecessor's validity end uses the same boundary."
- (—) "Creation, update, review, and event timestamps record transaction or audit chronology."
- (L) "Missing or unusable effective times fall back to projection time."
- (L) "Source time is thus a proxy for domain validity, whereas audit timestamps record when the system processed the change."
- (—) "Distinct fields do not make the proxy an exact effective date or provide full transaction-time versioning."

**D7.p4**
- (C) "Collections retain independent members instead of superseding siblings."
- (C) "Rejection also differs from positive replacement."
- (C) "Applying rejection can demote a matching current row to rejected and close its validity, or record a ruled-out alternative without displacing another current value."
- (C) "This branch does not construct the predecessor--successor pair of a scalar replacement."
- (C) "A rejected proposal, by contrast, records a review decision without creating a rejected fact about the project."

**D7.p5**
- (B) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
- (B) "It costs additional transitions and consistency obligations."
- (L) "Projection is not enclosed in one transaction: review, supersession, creation, link completion, proposal status, and event recording can commit independently."
- (L) "Failure can therefore leave an incomplete transition."
- (—) "Events are audit records alongside direct fact storage; they are not the source of truth for replay, and rebuilding records a request rather than reconstructing state."
- (—) "Auditability is not atomicity or event sourcing."

**D9.p3**
- (—) "The PROV data model supplies the general distinction between entities, activities, derivations, and responsible agents \citep{moreau2013provdm}."
- (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts."
- (C) "Normal projection copies proposal evidence identifiers to the fact."
- (C) "Application events connect proposals with facts and record the actor."
- (C) "Citations expose stored evidence text and source identifiers."
- (C) "This adapts provenance principles; it is not a claim of PROV conformance."

**D9.p4**
- (L) "Three limitations distinguish lineage from evidential correctness."
- (L) "First, a new fact does not store the winning claim identifier, and proposals lack a complete claim-to-fact foreign-key chain."
- (L) "Scalar resolution considers all claims for a concept, while proposal construction copies evidence, authority, and confidence from the claim that triggered evaluation."
- (L) "If it differs from the selected winner, the projected value and recorded support can diverge."
- (L) "Later agreement appends a supporting claim identifier without adding its evidence identifier to the fact's citation list."

**D9.p5**
- (L) "Second, demoting an existing fact to rejected retains its earlier evidence rather than copying the rejection proposal's evidence onto it."
- (L) "A citation can therefore support the former positive value without explaining its rejection."
- (L) "Recovering who reviewed a change likewise requires review or event records: the standard apply path does not populate the fact's confirming-actor fields."
- (L) "Third, public citations expose evidence spans but not stored locators or an exact mapping from answer sentences to supporting spans."
- (L) "A provenance question selects an earliest linked artifact using ingestion order, which need not be the original source of the decisive statement."

**T.rationale**
- (—) "\begingroup \small \setlength{\tabcolsep}{3pt} \renewcommand{\arraystretch}{1.15} \begin{longtable}{@{} >{\raggedright\arraybackslash}p{0.14\textwidth} >{\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}p{0.21\textwidth} >{\raggedright\arraybackslash}p{0.10\textwidth} >{\raggedright\arraybackslash}p{0.15\textwidth} >{\raggedright\arraybackslash}p{0.13\textwidth}@{}} \caption{Design-decision summary: alternatives and costs, not a ranking of architectures.} \label{tab:design-rationale}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endfirsthead \multicolumn{6}{l}{\tablename\ \thetable\ continued}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endhead \bottomrule \endfoot D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\"
- (—) "\addlinespace D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"
- (—) "\addlinespace D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- (—) "\addlinespace D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- (—) "\addlinespace"
- (B) "D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\"
- (—) "\addlinespace"
- (B) "D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\"
- (—) "\addlinespace"
- (B) "D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- (—) "\addlinespace D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- (—) "\addlinespace D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"
- (—) "\end{longtable} \endgroup"

### Sheet S: the conformance requirements this sheet names

Each is a checklist item of this sheet, under its id.
- [S-C1] Scalar: an asserted positive claim may propose a confirmed current value. Without an asserted positive candidate, a proposed, hedged or hypothetical positive claim may propose an unconfirmed value (D3.p3).
- [S-C2] Confirmation can accept an unconfirmed proposal and keep it unconfirmed (D3.p3).
- [S-C3] A negation does not invent a replacement (D3.p3).
- [S-C4] Under the default policy, an asserted negation of an alternative can propose a rejected fact; negating the current value must pass the authority and affirmation checks (D3.p3).
- [S-C5] Collections: member statuses as in D3.p4–p5 (no collection key in the evaluated runs).
- [S-C6] A challenger needs at least the current fact's authority and a source time no earlier than its validity start (D5.p3).
- [S-C7] Eligibility is checked before ranking (D5.p4).
- [S-C8] Eligible challengers are ranked by authority, source time and extraction confidence; the same ranking picks an initial asserted positive candidate (D5.p3).
- [S-C9] Different initial values tied on all three produce a conflict (D5.p3).
- [S-C10] Lower-authority dissent does not overwrite; ineligible dissent below the action threshold changes nothing; other unresolved dissent produces a conflict (D5.p4).
- [S-C11] Unresolved cases stay reviewable (D5.p2); a conflict need not retract the standing value (D5.p4).
- [S-C12] New values, replacements and current-default rejections pass through a proposal and a separate confirmation before projection (D6.p2).
- [S-C13] A proposal exposes value, concept, prior value, target status, evidence and reason; confirmation can accept, reject, edit, defer or request evidence; the review record is stored before projection (D6.p3).
- [S-C14] Value confirmation is separate from concept review (D4.p3).
- [S-C15] Resolution and confirmation are where admitted but inappropriate content is kept out of state (D2.p4).
- [S-C16] A scalar replacement closes the predecessor's validity, marks it superseded, links both ways, and starts at the winning claim's source time (D7.p3).
- [S-C17] A rejection can demote a matching current fact or record a ruled-out alternative without displacing the current value; a rejected proposal creates no rejected fact (D7.p4).
- [S-C18] Projection copies the proposal's evidence identifiers to the fact; application events record the actor (D9.p3).
- [X-C1] Each boundary writes its own record: evidence, claim, proposal, fact (D1.p3).
- [X-C2] Records stay linked by evidence identifiers across boundaries; review and event records are kept (D9.p2, D9.p3).

The disclosed limitations that the sheet says are listed in S.4 (they are not checklist items):
- D3.p3: negation of the current value is gated by the affirmation check.
- D5.p5: authority per artifact; source time from the artifact or ingestion; no tie check in the supersession branch; negation lacks the temporal gate and can be blocked by an earlier positive claim.
- D5.p6's first sentence: D5.p5's limitations qualify both requirements.
- D6.p4: an edited proposal bypasses resolution. D6.p5: the apply operation does not check for a review; the legacy exclusion branch.
- D7.p3: fallback to projection time. D7.p5: non-atomic projection.
- D9.p4: support taken from the triggering claim, not the winner. D9.p5: a demoted fact keeps its earlier evidence; no confirming actor on the fact.

### Sheet S: the implementation entries this sheet points to

#### E.6 Implementation entries

##### Evaluated prompt

- **Builder:** `_build_extraction_prompt`, `app/services/extraction_service.py:285-296`. Instructions: `extraction_instructions()`, l.271-282, from `EXTRACTION_BASE_INSTRUCTIONS`, l.177-211; the scalar key-selection sentence replaces the collection one (l.278-279). The registry is appended to the system message (l.288-292). User template `"Extract project-state claims from:\n\n{text}"` (l.295).
- **Hashes:** system template `725f1c00a2d1`, user template `c3635f7bb986`; the same in A0, A1, A2.
- **Response schema:** `LLMExtractionResponse`, strict (checked as above). Fields of a claim: `app/schemas/llm_extraction.py:14-21`.
- **Examples and example roles the prompt carries** (text as sent; l.177-211 with l.230-233):
  - "predicate: 'decided' | 'selected' | 'rejected' | 'proposed' | 'considered' | 'owns' | similar."
  - "polarity: NEGATIVE when the value is explicitly or implicitly rejected or ruled out — paraphrase negation counts ('off the table', 'ruled out', 'not going with', \"won't use\"). POSITIVE otherwise."
  - "modality: ASSERTED for firm decisions ('decided', 'locked in', 'going with'); HEDGED for tentative ('leaning', 'not locked in'); PROPOSED for candidates ('option', 'considering'); HYPOTHETICAL for future speculation."
  - "For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value."
  - "Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively."
  - The AMI role examples (l.201-207): "Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager'), predicate 'owns'."
  - "Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner."
  - Gloss: the four titles are the roles of the AMI scenario. Session check: none of them occurs in any EL2020 span, and the claims extracted with predicate `owns` carry values such as `PERSON14`.
- **How the registry enters:**
  - The whole active registry, not pruned. `self._registry()` (`extraction_service.py:565-569`) calls `StateKeyRegistryService.list_keys()` (`app/services/state_key_registry_service.py:42-49`: active keys, ordered by `state_key`).
  - Loaded once per `ExtractionService` instance (`_registry_cache`, l.375, l.566-568). The extraction endpoint makes one instance per call (`app/api/routes_projects.py:99-102`), and the harness calls it once per meeting (`app/evaluation/ami/runner.py:804`). So one registry per meeting: the traces show one key set per meeting in every run ("Registry carried per meeting", column "Ex key sets").
  - Line format, verbatim `app/services/extraction_service.py:217-220`:
    ```python
        return "\n".join(
            f"  - {k.state_key} [{k.value_type}, {k.key_cardinality}]: {k.label}. "
            f"{k.description} aliases: {k.aliases_json}"
            for k in registry
    ```
    Fields shown: key name, value type, cardinality, label, description, aliases. Not shown: negative aliases, example questions, family (`parent_key`), related keys, the values a key holds.
  - Empty registry (meeting a): the sentinel "(no registry keys provided — use state_key_hint: null)" (l.216).
- **Re-extraction of spans that gave no claims.** Idempotency skips only evidence that already has claims (l.389-392), and `extract_for_project` runs over all evidence of the project (l.635-637). So a span with no claims is sent again at every later meeting, with the larger registry. Their claims keep the source time of their own meeting (l.394-396). The docstring of `_said_at` notes this case (`app/services/resolution_service.py:288-293`).
- **Not shown that later steps need** (gloss):
  - The prompt asks for "extraction_confidence: 0.0–1.0." and says nothing more. The state rules use it as the last ranking key within a meeting and for tie conflicts (S).
  - No meeting identity, date, neighbouring span or current state is shown.
  - All keys are scalar (K2), but the prompt keeps the collection sentence quoted above.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `expansion_force_scalar` | True (default; confirmed by the sent text, see *Code check* in the Overview) | `app/core/config.py:137`; used `extraction_service.py:278-279` | which key-selection sentence the prompt carries |
| claim status | NEGATIVE → `REJECTED`; ASSERTED → `ACCEPTED`; otherwise `PROPOSED` | `extraction_service.py:654-659` | the stored claim status |
| claim identity | `make_claim_key(evidence_id, state_key or "", object_value, polarity)` | `extraction_service.py:667-672`; `app/db/repositories.py:164-173` | gloss: two claims of one span with the same hint, value and polarity are stored once |
| `extraction_confidence` default | 0.8 schema default. Unreachable under the strict schema, which makes every property required (`openai_llm.py:44-45`), except after a strict-to-non-strict downgrade on a 400 (`openai_llm.py:211-213`). Such a downgrade is not recorded: a 400 records no usage (`openai_llm.py:265-272`), `run.log` logs per call, not per attempt, and `trace.json` keeps no attempt envelope (a known limit, H) | `app/schemas/llm_extraction.py:21` | ranking input (S) |
| guard | every claim has a non-empty `object_value` | `extraction_service.py:545` | otherwise the call fails |
| source time | `artifact.created_at_source or artifact.ingested_at` | `extraction_service.py:396` | A0: ingestion clock (bug 6); A1, A2: meeting date (`repair_meeting_dates`) |
| source authority | `MEETING_DISCUSSION` = 30 for meeting transcripts | `app/core/enums.py:128`, `:137`; `app/services/artifact_ingestion_service.py:85-91` | the authority every claim carries (S) |

##### Deterministic logic

- Claims are persisted per span (`extraction_service.py:643-686`). Decisions, action items, risks and open questions are stored too (l.571-633). Gloss: these four are not on the state path.

##### Arm-specific

- **By arm:**
  - WD (`extraction_whole_decisions`) rewrites the instructions (`_whole_decision_instructions` (`3320375:app/services/extraction_service.py:264`)). No new call. Off in A0, A1 and A2.
  - `expansion_force_scalar` (`3320375:app/core/config.py:137`), on in every arm, also swaps a key-selection sentence of the extraction prompt (`expansion_force_scalar` (`3320375:app/services/extraction_service.py:278`)). Gloss: so the generator preference of D4.p5 reaches this prompt too.
  - A1 and A2 do not change this step. A2's support check later tests claims against their spans (S).
- **The WD instructions** (`extraction_whole_decisions`, `extraction_service.py:236-268`, applied l.280-281): `_PER_VALUE_SENTENCE` is replaced by `_PER_DECISION_SENTENCE` and `_WHOLE_DECISION_RULE` is appended. Code-derived system template hash `daf30b70d954…`. Its examples (l.248-260, verbatim): "(e.g. 'English and French at launch' rather than separate claims 'English' and 'French'; 'design freeze on Friday, bug fixes only afterwards' rather than 'Friday')" and "('40 dollars', not 'charge forty dollars for it')". The source comment (l.238-239, one comment joined across its line break): "The examples are generic on purpose: no development or test series supplies them."

#### K1.6 Implementation entries

##### Evaluated prompt

- **Seam and builder:** the extraction call of E; the same hashes.
- **Instructions** (text as sent; l.183, l.231-232):
  - "state_key_hint: the registry state_key the claim is about, or null if none fits."
  - "Key selection: map each claim to the MOST SPECIFIC matching registry key — the key about exactly this item/attribute, never a broad catch-all key. One claim per independent item."
  - The ownership sentence quoted in E.6 asks for a claim "keyed to the owner/assignment registry key". Gloss: a cold-start registry has no such key unless one was minted.
- **Registry:** as in E.6 (the whole registry, with the fields listed there).
- **Not shown** (gloss): the values each key already holds. So the hint cannot take into account whether the claim would rival a key's current value about another matter.

##### Deterministic logic

- The hint becomes the claim's key unchanged; nothing checks that it is registered (`extraction_service.py:661`, `:673`).
- A claim whose key is registered is never resolved again: the cold-start mapping skips it (`app/evaluation/ami/registry_expansion_eval.py:248-249`, `active_only=False`), and so does `resolve_state_key_for_claim` (`app/services/state_key_resolution_service.py:472-473`). Gloss: a hint to a registered key about another matter is kept whatever its matter.
- A hint to an unregistered key:
  - A0: the claim is filed under that key by the conflict pass (`app/services/conflict_service.py:134-158`; no definition, scalar path) and later mapped or parked by the expansion step (bug 5).
  - A1, A2: `repair_undefined_key_filing` returns noop instead (`conflict_service.py:152-153`, l.823-838).
  - Traces: the model also writes the literal key `null`. Conflict rows then give "Stage-23 repair (bug 5): no concept definition for 'null'; not filed".

##### Arm-specific

- **Under A1, A2, WD:** no prompt change. WD changes the extraction instructions, not the hint sentence.
- **Filing, by arm:**
  - A1: the bug-5 repair stops filing under a key with no definition (`_repair_undefined_key` (`3320375:app/services/conflict_service.py:823`)). No new call.
  - A2: the type check (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`), deterministic) can strip a hint whose key's type the value does not fit and send the claim back to the resolver (`_c2_reroute` (`3320375:app/services/conflict_service.py:899`)). No call at this step.
  - WD: none.

#### S.6 Implementation entries

##### Evaluated prompts

- A0, A1: none. The canonical-match seam (`app/services/resolution_service.py:144-170`) is never called, because every key is open-vocabulary (K2.6c).
  - The conflict service builds a canonical-match model client (`canonical_match` (`3320375:app/services/conflict_service.py:68`)), but no canonical_match step is recorded in the traces. Gloss: the harness pins no canonical vocabulary on accepted keys (`proposed_canonical_values` (`3320375:app/evaluation/ami/registry_expansion_eval.py:446`)).
- **A2, support check** (seam `claim_support_check`, contract `filing_support_check`; X.4): builder `support_messages`, `cycle2_filing.py:175-180`; system l.149-160; hashes `15fb33bbdef2` (system) and `5a787f081939` (user template).
  - It shows the span, the key's label only (l.198), the value and a status phrase (l.163-172).
  - Not shown (gloss): the key's description, the rival values, the meeting.
  - It carries no examples.

##### Order of evaluation

- `conflicts/evaluate` runs the engine over every claim of the project after extraction (`app/api/routes_proposals.py:28-33`; `conflict_service.py:324-326`; order by source time, then creation).
- Mapped and released claims are evaluated again one at a time during expansion (K2).
- Gloss: the repaired settle (A1, A2) is the only pass that evaluates every key with all its claims just before confirmation.

##### Rules (checklist, with `path:line`)

- **Entry** (`conflict_service.py:124-322`): a claim with no key is skipped (l.134-140). The collection path (l.164-180, l.427-506) is unused, since every key is scalar.
- **E1, a ruled-out alternative** (`scalar_negation_rejects` = True, `config.py:129`): an asserted negation of a value that is not current becomes a `reject` proposal (`conflict_service.py:200-254`). Traces show "Ruled-out value recorded as rejected-fact proposal." in every arm.
- **Engine** (`resolve_state_key`, `resolution_service.py:406-727`):
  - Ranking key, verbatim l.251-252:
    ```python
    def _sort_key(c: ClaimView):
        return (c.authority, c.source_time or _EPOCH, c.extraction_confidence)
    ```
  - Rule 1, negation of the current value (l.480-544).
  - Rule 2, only asserted positive claims can be confirmed; otherwise the most recent hedged claim becomes unconfirmed (l.546-588; `_most_recent`, l.259-260, ranks by source time, then confidence).
  - Rule 3, no current fact: the best claim wins. If another claim ties on all three ranking keys with a different value, the result is a conflict and no proposal (l.590-607). Gloss: within one meeting, authority (30) and source time are equal, so the model's `extraction_confidence` decides, and equal confidences make a conflict. Traces: "Tied authority and time with different values; human review required."
  - Rule 4, supersession: a challenger is eligible with authority at least the fact's and source time at or after the fact's `valid_from` (l.263-280); the best eligible challenger supersedes (l.659-697).
  - Rule 5: with no eligible challenger, dissent below `DISSENT_THRESHOLD` = `MEETING_DECISION` (50) is a noop (l.403, l.699-711). Gloss: transcript claims carry 30, so rule 6 (l.713-727) cannot occur for them.
  - Value identity in the engine: the exact raw string, for keys with no canonical values. That is every key in these runs (cleared at `registry_expansion_eval.py:446`).
    - `make_to_canonical` uses only the baseline when a key has no canonical values (`resolution_service.py:198-201`). The baseline then returns the raw `surface` (l.121-134). `C(v)` is `to_canonical(v) or v` (l.459-460), so it is the raw string whether or not unlisted values are allowed.
    - Gloss: the baseline's docstring (l.116) says the normalised surface is returned, but l.133-134 return `surface`.
    - Rule 3's tie test compares `C()` directly (l.594-597). Under A2, `differs` adds `normalise_value` and embedding cosine ≥ 0.80 (`cycle2_filing.py:54-76`) when `same_meeting_conflict` or `require_new_evidence` is on (`resolution_service.py:462-467`), but the tie test does not use `differs`.
    - Lower-case comparison occurs only in E1 (`conflict_service.py:207`), in reject projection (`projection_service.py:107-109`), and on the collection path (`conflict_service.py:447-457`; not reached, since no key is a collection).
- **Proposals** (`conflict_service.py:614-674`, l.556-608): deduplicated by `make_proposal_key(state_key, value, type)` (l.651-653; `repositories.py:423-445`). A0: any earlier proposal with the same key, in any status, blocks a new one (bug 12). A1, A2: see `repair_open_proposal_dedup` and `repair_settle_before_confirm` in X.4.
- **Settle** (A1, A2 only): `repair_settle_pending` (`runner.py:111-136`, called l.833-836).
- **Confirmation** (harness; `value_policy` `structural`, config block): `_internal_confirm_structural` (`runner.py:900-938`) accepts every pending proposal whose value passes `_confirmable_value` (l.170-190). A proposal that fails stays pending; it is never rejected (l.925-928).
  - `scrub_gold_value` (`app/evaluation/ami/question_set.py:113-138`) runs with an empty denylist: it fails a value that ends in an ellipsis or is a discourse fragment, and a value with a narration lead-in counts as wrapped.
  - The value then needs a word of at least four characters (`_content_words`, `runner.py:151-155`) that is not in `_STOPWORDS` (l.143-148) and not in `_VALUE_FILLER` (l.161-167).
  - Verbatim `runner.py:143-148`:
    ```python
    _STOPWORDS = {
        "the", "and", "that", "this", "with", "have", "they", "them", "from",
        "will", "group", "decided", "decide", "would", "could", "should", "about",
        "into", "than", "then", "were", "which", "while", "feature", "features",
        "device", "remote", "control",
    }
    ```
  - Gloss: a value whose words all have fewer than four characters (an acronym such as ASR, or a bare number) can never be confirmed. The list contains AMI words ("feature", "device", "remote", "control").
- **Projection** (`app/services/projection_service.py:41-184`):
  - A proposal needs an accepting review (l.61-66).
  - `valid_from` is the proposal's `effective_time` (l.86-97).
  - A `reject` proposal demotes a current fact with the same value, compared by lower case (l.105-128); otherwise it creates a REJECTED fact next to the current one.
  - Scalar supersession (l.130-140).
  - The current fact is the most recently updated current fact of the key (`repositories.py:219-229`).
- **Review responses:** `app/services/confirmation_service.py:45-104`.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| authority of transcript claims | 30 | `enums.py:128`, `:137` | eligibility and dissent gates |
| `DISSENT_THRESHOLD` | 50 | `resolution_service.py:403` | below it, ineligible dissent is a noop |
| ranking key | (authority, source time, extraction confidence) | `resolution_service.py:251-252` | which claim wins; ties make conflicts |
| source time | A0: ingestion clock; A1, A2: meeting date | `extraction_service.py:396`; `runner.py:744-778` | ordering across meetings; eligibility |
| `scalar_negation_rejects` | True (default; traces show the E1 branch) | `config.py:129` | ruled-out values become REJECTED facts |
| proposal identity | (key, value, type) | `conflict_service.py:651-653`; `repositories.py:423-445` | deduplication |
| `_STOPWORDS`, `_VALUE_FILLER`, word length ≥ 4 | as quoted | `runner.py:143-167` | which proposals the harness confirms |
| `claim_multi_key_facets` | False (default; no `claim_key_mapping` step in any trace) | `config.py:149` | one key per claim |
| settle (A1, A2) | one pass before each confirmation; no time window | `runner.py:111-136`, l.833-836 | a pending proposal the pass does not return again expires |
| `auto_approve_threshold` | 0.85 | `runner.py:268` | gloss: written to reports only; it decides nothing on this path |

##### Arm-specific

- **By arm:**
  - A1: the repairs change deterministic rules: the settle pass (`repair_settle_pending` (`3320375:app/evaluation/ami/runner.py:111`)), the engine repairs inside `resolve_state_key`, the lineage repair (`_repair_lineage` (`3320375:app/services/conflict_service.py:680`)), and the meeting dates set at ingest (A). No model call.
  - A2: adds the LLM seam claim_support_check (`ClaimSupportChecker` (`3320375:app/services/cycle2_filing.py:183`); calls at `supported` (`3320375:app/services/conflict_service.py:213`), `supported` (`3320375:app/services/conflict_service.py:279`) and `supported` (`3320375:app/services/conflict_service.py:752`)).
  - A2: the same-meeting conflict and new-evidence rules are deterministic, with embedding equivalence at 0.80 (`make_equivalence` (`3320375:app/services/cycle2_filing.py:54`), `_c2_equivalence` (`3320375:app/services/conflict_service.py:858`), `_create_cycle2_conflict` (`3320375:app/services/conflict_service.py:926`)).
  - A2: the type check is deterministic (`value_fits_type` (`3320375:app/services/cycle2_filing.py:101`); no model call).
  - WD: none.
- The full A1 switch table and A2 contract table are in X.4.

#### X.4 Arm-specific implementation across components

##### A1: the ten repair switches

Table: `app/core/cycle2_flags.py:86-151`; Settings fields `config.py:162-171`; RunConfig `runner.py:341-350`; the runner writes every switch to the environment (`runner.py:615-618`). In the runs, A0 already had the last two switches on.

| Switch | Bug | What it changes (summary from `cycle2_flags.py`) | Main code |
|---|---|---|---|
| `repair_negation_affirmation` | 1 | a value is ruled out when none of its positive claims survives the asserted negations; a ruled-out current value is superseded or rejected; a negation is never appended as support (l.87-97) | `resolution_service.py:288-375`, l.495-517, l.519-523, l.547-550; `conflict_service.py:208-225`, l.261-262, l.372, l.691-804, l.811-821, l.880-883 |
| `repair_proposal_lineage` | 2 | a proposal takes evidence, confidence and authority from the claim that supplied the winning value (l.98-103) | `conflict_service.py:359`, l.576-578, l.648-650, l.680-689, l.877-879; `repositories.py:409-420` |
| `repair_same_meeting_supersession` | 3 | the current value's own claims compete with its challengers (l.104-108) | `resolution_service.py:378-389`, l.662-673 |
| `repair_hedged_same_value` | 4 | with only hedged claims, a value equal to the current one changes nothing (l.109-113) | `resolution_service.py:392-396`, l.555-565 |
| `repair_undefined_key_filing` | 5 | a claim whose key has no definition is not filed (l.114-118) | `conflict_service.py:152-153`, l.823-838 |
| `repair_meeting_dates` | 6 | the meeting's date becomes the artifact's source time (l.119-124) | `runner.py:87-109`, l.744-778 |
| `repair_open_proposal_dedup` | 12 | an applied or expired proposal no longer blocks a new one with the same key (l.125-132) | `repositories.py:354-393`, l.436-438; `conflict_service.py:358`, l.605, l.671 |
| `repair_settle_before_confirm` | 13 | every key is evaluated again before confirmation; a pending proposal not produced again expires (l.133-140) | `runner.py:111-136`, l.833-836; `conflict_service.py:806-809`; `repositories.py:396-406`, l.439-440 |
| `repair_judge_rejection_status` | 7 (instrument) | the judge's gold string for rejection items states the expected status (l.141-144) | `app/evaluation/ami/judge_repairs.py:19-58`; on in A0, A1, A2 and RAG |
| `repair_dump_diagnostics` | 9, 10 (instrument) | state-dump traces matched per checkpoint; wrong-key diagnosis corrected (l.145-151) | `app/evaluation/ami/state_dump.py:99`, `:109`, `:124`, `:222`; on in A0, A1, A2 |

- Gloss: no repair changes a prompt text. The repairs change which claims are filed, what the engine returns, which proposals are raised and kept, and the source times.

##### A2: the four write contracts

| Contract | What it changes | Seam or LLM call added | Code |
|---|---|---|---|
| `filing_type_check` | before filing, a value that does not fit the key's declared type (numbers, dates, booleans, or a ';' enumeration under a scalar key) leaves the key; it is resolved again without that key, and parked for good after a second misfit | no LLM call; deterministic, logged as `filing_type_check` | `conflict_service.py:154-157`, l.899-924; `app/services/cycle2_filing.py:101-123`; `state_key_resolution_service.py:475-485`, l.508 |
| `resolution_same_meeting_conflict` | rival asserted values of equal authority from the same meeting become an open conflict, not a confidence contest | no LLM call; uses embeddings for value equivalence (cosine ≥ `answer_canonical_min_similarity` 0.80) | `resolution_service.py:472-475`, l.608-620, l.674-686; `conflict_service.py:403-406`, l.858-862, l.926-949; `cycle2_filing.py:54-76`; read side `answer_service.py:899-915` |
| `supersession_requires_new_evidence` | a challenger supersedes only with evidence and a meeting the current fact does not rest on | none; embeddings for equivalence as above | `resolution_service.py:274-279`, l.345-348; `conflict_service.py:850-856` |
| `filing_support_check` | a claim becomes a fact only if its own span establishes its value, status and time; an unsupported winner is parked and the key resolved again (up to 8 times) | the `claim_support_check` LLM seam, one call per claim, cached on the claim | `conflict_service.py:185-191`, l.213-218, l.270-284, l.643-646; `cycle2_filing.py:149-210` |

- The support-check prompt is under S.6.

##### WD: `extraction_whole_decisions`

- It changes only the extraction instructions (E.6): the per-value sentence is replaced, and the whole-decision rule is appended (`extraction_service.py:236-268`, l.280-281).
- No new seam. Code-derived system template hash `daf30b70d954…`. Not run in any evaluated arm (config blocks: `"extraction_whole_decisions": false`).
- Plan role: `cycle2_flags.py:61-64`, decisions D10 and D4.

---

## Sheet R: reading

**Scope.**
- Rows stored with the right status in the recorded run; losses surface at `key_reached`, `in_payload` or `answered`.
- Caused-at, amendment line 377: "from the offline reading analysis, probe (iii) and the page."
- Step type: mixed (R.1). Question routing and the grounding pass are LLM steps with no model condition (amendment line 331).

**Candidate causes listed by the amendment** (amendment line 388):
- [R-cause-1] "the question-time shortlist excluded the holding key" (amendment line 388)
   - Applies only where the offline reading check shows the holding key was pruned out. Amendment line 337: "Where the key was in the recorded question-routing prompt, that check rules it out."
   - Decided by: probe (iii), re-resolution with the unpruned registry.
   - Entries to check: question resolution through `_prompt_registry` (R.6); the shortlist parameters (K2.6, Parameters).
- [R-cause-2] "the scalar focus gate demoted a correct fact to a near match" (amendment line 388)
   - Decided by: the page. Gloss: no probe tests this cause.
   - Entries to check: the scalar focus gate; the relevance filter at `answer_relevance_min_similarity` 0.42; focus terms of four or more characters outside `_FOCUS_STOPWORDS`, which include AMI words (R.6; an implementation entry with no listed cause, left to the pilot); the removal of the focus key's own label and alias words from the focus terms, which decides broad versus specific and whether the gate runs at all (R.6).
   - Design to read it against: D8.p3 (the gate's outcome: an explicit unknown, with nearby facts kept as near matches) and D8.p4 (its stated cost, restricted answerability) (R.3). The relevance test itself is implementation (R.3).

**Further implementation entries at this boundary** (the pilot may add a cause that rests on one, amendment line 380):
- [R-entry-1] Widening after the resolver (R.6):
  - broad questions take the rule candidates after the LLM's picks, up to 10 keys, ranked by the rule-scorer weights and the embedding bonus at `embedding_score_weight` 5.0;
  - they then append the resolver LLM's supporting keys up to 10; the 0.25 candidate ratio is inert on the LLM path;
  - value-matched keys at cosine 0.55, up to 6; family siblings up to 10.
- [R-entry-2] Rejection questions also read the current facts of resolved keys whose names contain `reject` (R.6).
- [R-entry-3] Change questions add keys that declare `change_explanation` primary; minted keys declare no intents (R.6).
- [R-entry-4] Near-duplicate values are canonicalised at 0.80, with no cap (R.6).
- [R-entry-5] The grounding pass's revised answer replaces the prose; it is skipped for provenance questions (R.6).
- [R-entry-6] A2 adds a disputed answer for open same-meeting conflicts (R.6, Arm-specific).

**Criterion (ii): inputs the design gives, against what the prompt shows** (gloss):
- Question routing.
  - Design gives: the question, and the concepts' descriptions, aliases, examples and observed values (D8.p3; R.3).
  - Prompt shows: the question with its intent, and the pruned registry with key name, label, description, aliases, negative aliases and value type (K2.6a). Not shown: example questions, the values each key holds (R.6). Observed values enter only through the deterministic value-match widening (R.6). Example questions enter only deterministically: through the embedding profile behind the shortlist, and, for broad questions, through the rule candidates (K2.6a; R.6).
- Answer context and grounding.
  - Design gives: current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions and decision records (D8.p3; R.3).
  - The grounding pass sees: the question, the drafted answer, the citations and the current facts (key, value, status, review state). `review_state_present` was False in every call (R.6).
  - The grounding pass has no 94c049d design entry: Chapter 4 text outside D1–D9 is context only (amendment line 102; R.3; Annex).

**Conformance checklist:** R-C1 to R-C9 (R.4), which include D1.p5's requirement on answers (X.1).

**Disclosed limitations at 94c049d:** unknown cannot tell absence from loss (D8.p3, its sixth sentence); the latest-addition change heuristic (D8.p5, its last three sentences); citation granularity and provenance by ingestion order (D9.p5); links need not support the value (D9.p6, its first two sentences). They cannot ground architectural weakness or a trade-off. A loss resting on one of these sentences is coded: conformance where the code contradicts a 94c049d principle sentence on the register; implementation choice where an alternative meets (i)–(iv); otherwise unclear, or design or model, not separated, where line 331 applies. For A0, line 309 applies. Stated costs, which are (B) and quotable below: restricted answerability (D8.p4); weaker historical coverage (D8.p6).

**94c049d text a page may quote**, after implementation is rejected. Only the sentences listed below may ground a design code, each under its tag: a commitment (C) may ground architectural weakness, and a stated benefit or cost (B) may ground a trade-off. No other sentence of these paragraphs may ground either. A sentence that states a shortfall (L) never may, and neither may D4.p4's sentence that matching does not establish equivalence.
- For architectural weakness (C):
  - **D1.p5** (C) "If it behaves as intended, tentative or rejected interpretations should not appear as settled answers, and returned facts should carry inspectable evidence."
  - **D2.p3** (C) "ProjectMemory chooses early admission." "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created." "Approved redactions are applied before extraction." "Ignored spans and sensitive spans routed for review produce no evidence record through this path." "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts." "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."
  - **D3.p5** (C) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
  - **D4.p5** (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions." "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."
  - **D5.p4** (C) "Checking eligibility before ranking matters." "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered." "Lower-authority dissent does not overwrite current state." "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict." "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat." "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."
  - **D7.p5** (B, C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
  - **D8.p2** (C) "ProjectMemory selects a different context-construction order for DR2, DR4, and DR5: resolve concepts and facts first, then follow evidence links."
  - **D8.p3** (C) "Concept descriptions, aliases, examples, and observed values associate a question with generated concepts." "Broad list questions may aggregate candidate concepts and family siblings; specific questions remain narrower." "Normal context contains current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions, and decision records." "Templates distinguish confirmed from proposed values." "If no concept, current fact, or relevant value answers a specific question, the service can return an explicit unknown outcome and retain nearby facts only as near matches." "Although the public schema defines a disputed outcome, ambiguous facts are excluded by ordinary current-fact retrieval and normally reach the unknown branch; a standing confirmed fact can instead carry a conflict caveat."
  - **D8.p4** (C) "Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims, or events." "Current code adds a bounded exception: rejection-phrased questions can retrieve rejected facts for resolved concepts, including scalar alternatives never previously current." "Negative interpretations must first reach a representable, projected lifecycle state; rejected expansions and rejected state proposals do not become answerable merely because they persist."
  - **D8.p5** (C) "For collection-like or multi-concept questions, it selects current facts whose earliest linked source artifact is the most recently ingested artifact."
  - **D9.p3** (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts." "Normal projection copies proposal evidence identifiers to the fact." "Application events connect proposals with facts and record the actor." "Citations expose stored evidence text and source identifiers." "This adapts provenance principles; it is not a claim of PROV conformance."
- For a trade-off (B):
  - **D2.p5** (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
  - **D4.p6** (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation." "It does not establish that fine-grained concepts are universally better."
  - **D8.p2** (B) "The read-side alternative is to retrieve transcript passages first and ask a model to infer state for the question." "This keeps broad source access and avoids a write-time schema, but repeatedly places temporal and epistemic interpretation at the question boundary."
  - **D8.p4** (B) "The narrower context is intended to reduce exposure to superseded alternatives and attach evidence to the selected state." "Its cost is restricted answerability."
  - **D8.p6** (B) "The expected behavior is current-value accuracy with meaningful abstention and evidence support, alongside weaker historical coverage."
  - **D9.p6** (B) "The intended consequence is an answer whose evidence permits verification and correction."
  - **T.rationale** (B) "D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- Question resolution and grounding are LLM steps with no model condition, so the page must also meet the condition of line 340 (quoted on sheet K1).

**Retrospective entries here:** R-R1 to R-R7; D11 (R-R1); A-R1's read-side sentence (R-R4); X-R2; X-R4; X-R6.

### Sheet R: the 94c049d paragraphs this sheet names

**D1.p5**
- (L) "The normal write workflow realises these distinctions, but enforcement is incomplete across all callable operations, as D6 explains."
- (—) "D1 therefore responds to all four requirements without proving their full satisfaction."
- (C) "If it behaves as intended, tentative or rejected interpretations should not appear as settled answers, and returned facts should carry inspectable evidence."
- (—) "Chapter~\ref{chap:evaluation} examines these consequences through state, rejection, unknown, and evidence questions; the aggregate comparison cannot attribute an effect to record separation alone."

**D2.p3**
- (C) "ProjectMemory chooses early admission."
- (C) "Source text is stored and segmented; a persisted gate decision determines whether an evidence span is created."
- (C) "Approved redactions are applied before extraction."
- (C) "Ignored spans and sensitive spans routed for review produce no evidence record through this path."
- (C) "Extraction enumerates admitted evidence, and ordinary answer citations use evidence records rather than searching raw artifacts."
- (C) "The gate also supports DR5: admission and redaction remain inspectable parts of the derivation."

**D2.p5**
- (—) "The selected balance favours retaining potentially useful project context while excluding clearly incidental material."
- (—) "It does not settle how selective admission should be."
- (L) "Raw artifacts remain stored, redaction and classification are fallible, and evidence access checks do not constitute production authentication or retention policy."
- (L) "Thus DR8 is only partly addressed, and the gate supplies no privacy guarantee."
- (B) "The expected consequence is fewer substantive answers about incidental content without excessive loss of required state."
- (—) "Noise questions and state recall partially test that balance."
- (—) "Organisational privacy, sensitive-data retention, and an optimal admission threshold are not evaluated in Chapter~\ref{chap:evaluation}."

**D3.p5**
- (—) "Member-level status reduces one ambiguity without making collections equivalent to scalar resolution."
- (—) "An agreeing positive claim adds support to an existing member without automatically upgrading an unconfirmed member."
- (L) "Membership still depends on correctly interpreted concept meaning, and heterogeneous content can enter the same broad collection."
- (L) "Extraction can misclassify modality or negation in either model."
- (—) "DR1 and DR4 are therefore only partially realised across the full lifecycle."
- (C) "If the mechanism behaves as intended, answers should preserve current, proposed, and ruled-out distinctions and abstain when no current value is established."
- (—) "Status and unknown questions directly target this behavior; rejection questions and development lifecycle probes cover only the negative transitions represented in their inputs."

**D4.p4**
- (—) "This supports an empty initial registry without treating generated labels as research outcomes."
- (—) "Parking preserves an interpretation without force-classifying it, but delays answer availability and can leave useful state permanently unavailable if its concept is never accepted."
- (L) "Alias-based and optional semantic matching can reduce duplicate proposals; neither establishes equivalence."
- (L) "Review may itself merge distinct meanings or fail to recognise synonyms."

**D4.p5**
- (—) "The representation choice within an open schema remains substantial."
- (—) "A broad feature collection uses fewer concepts and supports direct enumeration, but places greater weight on coherent membership and member lifecycle semantics."
- (—) "Fine-grained concepts make conflicts and statuses more local, while increasing fragmentation, near-duplicates, and the work required to resolve broad questions."
- (C) "The September defaults favour scalar concept generation and attach family metadata so related concepts can be aggregated for broad list questions."
- (C) "This is a preference of the generator, not a universal ban on collections: registry, review, and projection retain collection support."

**D4.p6**
- (B) "The rationale for the current preference is a more local lifecycle combined with explicit read-side aggregation."
- (B) "It does not establish that fine-grained concepts are universally better."
- (—) "Development diagnostics found that changing registry shape did not automatically remove retrieval misses (Section~\ref{sec:design-evolution})."
- (—) "The intended consequence is useful state coverage from an empty registry, assessed by the cold-start protocol in Section~\ref{subsec:eval-cold-start}."
- (—) "Fragmentation and family quality remain diagnostic properties; reference key-name agreement is not a correctness endpoint."
- (L) "Moreover, the gold-informed reviewer can influence which concepts survive."
- (L) "Cold start must therefore be interpreted together with confirmation sensitivity, rather than as fully unaided schema discovery."

**D5.p4**
- (C) "Checking eligibility before ranking matters."
- (C) "Otherwise an older, higher-authority objection can prevent a newer eligible replacement from being considered."
- (C) "Lower-authority dissent does not overwrite current state."
- (C) "Ineligible dissent below the action threshold produces no mutation; other unresolved dissent produces a conflict."
- (C) "A conflict need not retract the standing value: the ordinary answer can retain it with a caveat."
- (C) "Keeping uncertainty visible does not imply abstaining whenever disagreement exists."

**D7.p5**
- (C) "Supersession preserves evidence and makes ordinary current-state queries exclude obsolete scalar values."
- (—) "It costs additional transitions and consistency obligations."
- (L) "Projection is not enclosed in one transaction: review, supersession, creation, link completion, proposal status, and event recording can commit independently."
- (L) "Failure can therefore leave an incomplete transition."
- (—) "Events are audit records alongside direct fact storage; they are not the source of truth for replay, and rebuilding records a request rather than reconstructing state."
- (—) "Auditability is not atomicity or event sourcing."

**D8.p2**
- (B) "The read-side alternative is to retrieve transcript passages first and ask a model to infer state for the question."
- (—) "Retrieved passages conditioning generation are the relevant principle borrowed from RAG \citep{lewis2020retrieval}."
- (B) "This keeps broad source access and avoids a write-time schema, but repeatedly places temporal and epistemic interpretation at the question boundary."
- (C) "ProjectMemory selects a different context-construction order for DR2, DR4, and DR5: resolve concepts and facts first, then follow evidence links."

**D8.p3**
- (C) "Concept descriptions, aliases, examples, and observed values associate a question with generated concepts."
- (C) "Broad list questions may aggregate candidate concepts and family siblings; specific questions remain narrower."
- (C) "Normal context contains current confirmed or unconfirmed facts, their evidence, and relevant conflicts, pending proposals, review sessions, and decision records."
- (C) "Templates distinguish confirmed from proposed values."
- (C) "If no concept, current fact, or relevant value answers a specific question, the service can return an explicit unknown outcome and retain nearby facts only as near matches."
- (L) "This makes a retrieval gap visible, although unknown alone cannot distinguish genuine absence from information lost during admission, extraction, review, or retrieval."
- (C) "Although the public schema defines a disputed outcome, ambiguous facts are excluded by ordinary current-fact retrieval and normally reach the unknown branch; a standing confirmed fact can instead carry a conflict caveat."

**D8.p4**
- (B) "The narrower context is intended to reduce exposure to superseded alternatives and attach evidence to the selected state."
- (B) "Its cost is restricted answerability."
- (C) "Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims, or events."
- (C) "Current code adds a bounded exception: rejection-phrased questions can retrieve rejected facts for resolved concepts, including scalar alternatives never previously current."
- (—) "This extends the earlier artifact but is not a general search over rejection history."
- (C) "Negative interpretations must first reach a representable, projected lifecycle state; rejected expansions and rejected state proposals do not become answerable merely because they persist."

**D8.p5**
- (—) "Change answering is narrower still."
- (C) "For collection-like or multi-concept questions, it selects current facts whose earliest linked source artifact is the most recently ingested artifact."
- (L) "It does not traverse supersession links, compare arbitrary snapshots, or reconstruct all removals and replacements."
- (L) "A single scalar change question normally follows the current-value template."
- (L) "This latest-addition heuristic fits some checkpoint questions but is not a general temporal-difference engine."

**D8.p6**
- (B) "The expected behavior is current-value accuracy with meaningful abstention and evidence support, alongside weaker historical coverage."
- (—) "Chapter~\ref{chap:evaluation} directly targets current and unknown outcomes and partially tests change and rejection through selected obligations."
- (—) "The paired comparator is specifically cumulative transcript RAG: ProjectMemory maintains reviewed state between questions, whereas that baseline reconstructs answers from retrieved transcript context."
- (—) "This neither characterises every RAG architecture nor establishes that maintained state is inherently more accurate."
- (—) "A complete-system difference also cannot isolate retrieval order from review and write-time work."

**D9.p3**
- (—) "The PROV data model supplies the general distinction between entities, activities, derivations, and responsible agents \citep{moreau2013provdm}."
- (C) "ProjectMemory applies traceability through source identity and locators, admitted evidence and gate decisions, evidence-linked claims, evidence-bearing proposals, reviews, and facts."
- (C) "Normal projection copies proposal evidence identifiers to the fact."
- (C) "Application events connect proposals with facts and record the actor."
- (C) "Citations expose stored evidence text and source identifiers."
- (C) "This adapts provenance principles; it is not a claim of PROV conformance."

**D9.p5**
- (L) "Second, demoting an existing fact to rejected retains its earlier evidence rather than copying the rejection proposal's evidence onto it."
- (L) "A citation can therefore support the former positive value without explaining its rejection."
- (L) "Recovering who reviewed a change likewise requires review or event records: the standard apply path does not populate the fact's confirming-actor fields."
- (L) "Third, public citations expose evidence spans but not stored locators or an exact mapping from answer sentences to supporting spans."
- (L) "A provenance question selects an earliest linked artifact using ingestion order, which need not be the original source of the decisive statement."

**D9.p6**
- (L) "The normal path thus stores and returns linked evidence identifiers when available, but does not guarantee that every link supports the selected value and lifecycle status."
- (L) "Claim-level support, state derivation, and auditability are related but distinct."
- (B) "The intended consequence is an answer whose evidence permits verification and correction."
- (—) "Chapter~\ref{chap:evaluation}'s evidence questions partially test source identification."
- (—) "Its specified claim-level citation precision and coverage are not yet implemented as the complete claim-to-span assessment described there: existing scoring primarily checks meeting availability and judge flags."
- (—) "Full semantic support and complete lineage therefore remain unevaluated conditions of a stronger provenance claim."

**T.rationale**
- (—) "\begingroup \small \setlength{\tabcolsep}{3pt} \renewcommand{\arraystretch}{1.15} \begin{longtable}{@{} >{\raggedright\arraybackslash}p{0.14\textwidth} >{\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}p{0.21\textwidth} >{\raggedright\arraybackslash}p{0.10\textwidth} >{\raggedright\arraybackslash}p{0.15\textwidth} >{\raggedright\arraybackslash}p{0.13\textwidth}@{}} \caption{Design-decision summary: alternatives and costs, not a ranking of architectures.} \label{tab:design-rationale}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endfirsthead \multicolumn{6}{l}{\tablename\ \thetable\ continued}\\"
- (—) "\toprule \textbf{Tension} & \textbf{Alternatives} & \textbf{Selected design} & \textbf{DRs} & \textbf{Main benefit intended} & \textbf{Main cost} \\"
- (—) "\midrule \endhead \bottomrule \endfoot D1 Evidence / state & Raw answering; immediate structured facts & Distinct evidence, claims, proposals, and facts & 1, 5, 6, 8 & Inspectable commitments & More workflow stages \\"
- (—) "\addlinespace D2 Selectivity / coverage & Process all; answer-time filter & Gate before extraction; permissive admitted context & 8, 5 & Deliberate admission & Lost evidence; review load \\"
- (—) "\addlinespace D3 Status / simplicity & Treat every claim as asserted & Polarity, modality, lifecycle status & 1, 4 & Status-sensitive answers & Classification and transition errors \\"
- (—) "\addlinespace D4 Structure / openness & Fixed schema; discard; force-match & Park claims; review expansion; scalar generation with families & 7 & Cold-start capture & Schema splits; delayed availability \\"
- (—) "\addlinespace D5 Recency / authority & Newest; most confident; authority only; manual & Authority and time eligibility before ranking & 2, 3 & Controlled replacement & Coarse authority; incomplete conflicts \\"
- (—) "\addlinespace D6 Automation / review & Direct mutation; threshold approval; manual entry & Proposal, confirmation, projection workflow & 6 & Contestable changes & Effort, delay, incomplete enforcement \\"
- (—) "\addlinespace D7 Currency / history & Overwrite; append without status & Supersession and separate clocks & 2, 3 & Preserved replacement history & Non-atomic transitions \\"
- (—) "\addlinespace"
- (B) "D8 Focus / answerability & Transcript-first reconstruction & State first, then evidence; bounded rejected-fact branch & 2, 4, 5 & Current semantics and restraint & Narrow history and change answering \\"
- (—) "\addlinespace D9 Traceability / complexity & Source title only; full derivation graph & Evidence links, reviews, audit events & 5 & Checkable source support & Incomplete lineage and attribution \\"
- (—) "\end{longtable} \endgroup"

### Sheet R: the conformance requirements this sheet names

Each is a checklist item of this sheet, under its id.
- [R-C1] Resolve concepts and facts first, then follow evidence links (D8.p2).
- [R-C2] Associate a question with concepts by descriptions, aliases, examples and observed values (D8.p3).
- [R-C3] Broad list questions may aggregate candidate concepts and family siblings; specific questions stay narrower (D8.p3, D4.p5, D4.p6).
- [R-C4] Templates distinguish confirmed from proposed values; answers keep current, proposed and ruled-out apart; tentative or rejected interpretations do not appear as settled (D8.p3, D3.p5, D1.p5).
- [R-C5] If no concept, current fact or relevant value answers a specific question, the service can return an explicit unknown and retain nearby facts only as near matches (D8.p3); answers should abstain when no current value is established (D3.p5).
- [R-C6] Ambiguous facts are excluded by ordinary retrieval; a standing confirmed fact can carry a conflict caveat (D8.p3, D5.p4).
- [R-C7] Ordinary current-state questions do not retrieve superseded facts, rejected proposals, all negative claims or events; rejection-phrased questions may retrieve rejected facts of resolved concepts (D8.p4, D7.p5).
- [R-C8] Change answering as in D8.p5.
- [R-C9] Citations use evidence records and expose the stored evidence text and source identifiers; returned facts carry inspectable evidence (D2.p3, D9.p3, D1.p5).

### Sheet R: the implementation entries this sheet points to

#### K2.6 Implementation entries (part)

##### K2.6a Resolver, write path

- **Seam:** `state_key_resolution`. Read path in R.
- **Builder:** `_build_resolution_prompt`, `state_key_resolution_service.py:224-249`; system `RESOLUTION_SYSTEM_PROMPT`, l.108-133. Called from `resolve()` (l.272-357) via `resolve_state_key_for_claim` (l.441-531).
- **Hashes:** system `fb29d2fadfef`, user template `6e907422766a`; the same in A0, A1, A2 and on both paths. The user message starts with "Resolve this text to registry keys." in every call, so no context digest was sent (`context_digest`, pinned off by `runner.py:607-609`).
- **Example the prompt carries** (text as sent; l.126-128): "Example: 'Redis is the datastore for session state' uses 'datastore' (an alias for architecture.database.primary) but Redis-as-session-store is NOT the primary operational database." Gloss: an example from the database worked example of the rule baseline (`extraction_service.py:8-12`), not from the meeting domain.
- **Text sent:** the claim's subject and value joined by " — " (l.487-492); the evidence span only when both are empty. The intent hint comes from keyword rules (`detect_intent`, l.533-549).
- **How the registry enters:** `_prompt_registry` (l.676-705) over `list_keys()`. Verbatim, l.689-705:
  ```python
        if not embedding_candidates:
            return registry_keys
        if len(registry_keys) <= get_settings().resolver_prune_threshold:
            return registry_keys
        keep = {key for key, _ in embedding_candidates}
        normalized_text = self._normalize(text)
        tokens = self._tokens(normalized_text)
        for definition in registry_keys:
            if definition.state_key in keep:
                continue
            lexical = (
                self._alias_score(definition.aliases_json, normalized_text, tokens)[0] > 0
                or bool(self._key_tokens(definition) & set(tokens) - STOPWORDS)
            )
            if lexical or definition.supported_intents_json.get(intent.value) == "primary":
                keep.add(definition.state_key)
        return [d for d in registry_keys if d.state_key in keep]
  ```
  - **Embedding part** (`_embedding_candidates`, l.625-643): the cosine between the text and each key's profile; keys at or above `embedding_min_similarity` (0.30), best first, at most `embedding_top_k` (8). Key profile (l.663-674): key name with dots as spaces, label, description, domain, aliases, example questions, canonical values. Key vectors are cached per registry signature (l.645-661).
  - **Lexical part:** a positive alias score (the normalised alias is a substring of the text, or all its tokens are text tokens; l.829-845), or any shared token between the text and the key's name, label, description and domain (`_key_tokens`, l.876-878) outside `STOPWORDS` (l.42-65), or the key declares the intent primary.
  - **Whole registry** when no key reaches 0.30, or when the registry has at most `resolver_prune_threshold` (12) keys.
  - Gloss: `STOPWORDS` (l.42-65) does not contain common words such as "and", "in", "on", "with" or "this", so the lexical part admits any key whose description shares such a word with the claim text.
  - Line format, verbatim l.230-235:
    ```python
    registry_lines = "\n".join(
        f"  - {k.state_key}: {k.label}. {k.description} "
        f"[aliases: {k.aliases_json}; negative_aliases: {k.negative_aliases_json}; "
        f"value_type: {k.value_type}]"
        for k in registry
    )
    ```
    Fields shown: key name, label, description, aliases, negative aliases, value type. Not shown: cardinality, family, example questions, the values a key holds.
    - Example questions are present on every minted key (`state.json`). They never reach the prompt; no trace holds the field. They enter only deterministically, in two ways: through the embedding profile behind the shortlist (`_key_profile`, l.663-674), and, for a text that `is_broad_list_question` accepts (l.88-94), through the rule candidates (`_example_overlap`, l.777-780, l.869-874; reached through l.347-355; R.6).
    - Canonical values: no key in these runs has any, because the harness clears them on accept (K2.6c). They are the values D4.p3 names as a matching input (K1.3), so the clearing empties that input.
  - At meeting a every write-path call lists no key (the registry is empty, so the model cannot return a key and every claim goes to expansion).
- **Use of the output:** keys outside the registry are dropped (l.313, l.898-915). The first remaining primary key is taken (l.508-510). Gloss: on the write path, supporting keys, `needs_clarification` and `confidence` are not used. On the read path, supporting keys are used: broad questions append them to the context pack (R.6, Retrieval).
- **Not shown that later steps need** (gloss): the span, the claim's polarity and modality, and the values each key holds. Filing then puts the claim among that key's claims (S).

#### K2.6 Implementation entries (part)

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `resolver_embeddings_enabled` | true (`--resolver-embeddings`; config block `"resolver_embeddings": true`) | `config.py:65`; set by `runner.py:604-606` | the embedding part of the shortlist is on |
| `embedding_top_k` | 8 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:82`; `state_key_resolution_service.py:643` | at most eight embedding candidates |
| `embedding_min_similarity` | 0.30 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:83`; `state_key_resolution_service.py:641` | a key below this cosine is not an embedding candidate; with none above it, the whole registry is sent |
| `resolver_prune_threshold` | 12 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:86`; `state_key_resolution_service.py:691` | at or below 12 keys the whole registry is sent |
| `STOPWORDS` | 22 words | `state_key_resolution_service.py:42-65` | words that do not count as shared tokens in the lexical part |
| first primary key | `fitting[0]` | `state_key_resolution_service.py:508-510` | the key the claim is filed under |
| `expansion_reuse_policy` | `semantic` (config block) | `config.py:70`; `registry_expansion_eval.py:218-230` | alias merge, semantic reuse and exact attach are all on |
| `expansion_reuse_threshold` | 0.80 (config block `0.8`) | `config.py:71`; `runner.py:298`; `registry_expansion_service.py:44`, l.296 | cosine at which a candidate reuses a proposal or merges into a key |
| alias merge target | first matching key in name order | `state_key_registry_service.py:42-49`, l.57-64; `registry_expansion_service.py:133-135` | which key an alias-matched claim goes to |
| `_KEY_SHAPE` | two or more dotted segments | `informed_reviewer.py:75` | harness accept test |
| `_STATE_KEY_RE` | 2–4 segments | `registry_expansion_review_service.py:31-32` | validator accept test |
| canonical values on accept | cleared | `registry_expansion_eval.py:446-447` | keys are open-vocabulary, so `canonical_match` is never called (no such trace step) |
| `expansion_force_scalar`, `concept_families_enabled` | true, true | `config.py:137`, `:144` | scalar keys only; every key gets a family |
| `_MERGE_CONFIDENCE` | 0.4 | `registry_expansion_service.py:36` | stored on merge recommendations; gloss: not used to decide |

#### R.6 Implementation entries

##### Evaluated prompts

- **Question resolution:** the resolver of K2.6a with the question as text. Same hashes (`fb29d2fadfef`, `6e907422766a`). Registry via `_prompt_registry` with the intent from `detect_intent`.
- **Grounding:** seam `question_answering_grounding`. Builder `_build_grounding_prompt`, `app/services/answer_service.py:90-118`; system `GROUNDING_SYSTEM_PROMPT`, l.53-87. Hashes: system `76eb844f30d6`, user template `163a9efe1ef6`; the same in A0, A1, A2.
  - It is skipped for provenance questions (l.202-203).
  - It sees the question, the drafted answer, the citations (evidence texts) and the current facts (key, value, status, review state).
  - Its `revised_answer` replaces the answer prose (l.249-253). Gloss: an LLM step after the state that can remove asserted values from the prose; the structured payload is kept.
  - Example (text as sent; l.79-81): "An abstaining answer ('I do not see a confirmed…', 'I was unable to find relevant project state…') asserts nothing and is trivially grounded (grounded=true, unsupported_sentences=[])."
  - `review_state_present` was False in every call.
- **Not shown** (gloss): the resolver sees key definitions but not their values, so a question about a value held under an oddly named key depends on the widening steps below. Nor does it see the keys' example questions; they enter only deterministically (K2.6a; Deterministic widening below).

##### Deterministic widening and answer logic (checklist)

- **After the LLM**, in `resolve()`:
  - Change questions add the keys that declare `change_explanation` primary (`state_key_resolution_service.py:322-336`). Gloss: minted keys declare no intents (every key in every `state.json` has empty `supported_intents`), so this adds nothing here.
  - Broad list questions (`is_broad_list_question`, l.88-94) add the rule-based candidates after the LLM's own picks, up to `BROAD_LIST_MAX_KEYS` = 10 (l.76, l.347-355).
    - The candidates are every key with a positive rule score (`_compute_rule_based_response`, l.551-621; `_score_key`, l.745-807), plus the embedding candidates with a bonus of cosine × `embedding_score_weight` 5.0 (`config.py:84`; l.707-743). They are sorted by score, with no other minimum. A negative alias with no positive alias disqualifies a key (l.758-760, l.725-731).
    - Score parts live in these runs: alias match, 4.5–5.5 for a substring match and 3.4–4.2 for a token-subset match (l.829-845); key-token overlap, 0.75 per token, at most 3 (l.771-775); example-question overlap, 0.5 per token, at most 2 (l.777-780, l.869-874); the decision-domain bonus 3.5 for DECISION_LOOKUP (l.803-805).
    - Inert in these runs: the intent bonuses 2.5 and 1.0 (l.794-801; minted keys declare no intents) and the canonical score 2.5 (l.766-769, l.847-856; no key has canonical values).
    - Gloss: so example questions reach question routing here, deterministically, and never through the prompt (K2.6a).
- **Retrieval** (`app/services/retrieval_service.py:97-203`):
  - Broad questions pass the resolver's candidate list to `_widen_broad_primary_keys` (l.114-117, l.290-308): candidates scoring at least `_BROAD_CANDIDATE_RATIO` 0.25 of the top, up to `_BROAD_MAX_KEYS` 10 (l.41-42).
    - On the LLM path the response's `candidate_keys` is empty: the field is internal and is not in the schema sent to the model (`app/schemas/llm_resolution.py:8-11`, l.33-40). `_to_resolve_result` then substitutes the primary keys and the supporting keys, all at one score, the LLM confidence (`state_key_resolution_service.py:918-923`). For a broad question the primary keys already include the rule candidates, capped at 10 (l.347-355 of that file).
    - So the 0.25 ratio is inert. The net effect is that the resolver LLM's supporting keys are appended until there are 10 keys.
  - Keys whose current values match the question focus at cosine ≥ `_VALUE_MATCH_COSINE` 0.55 are added, up to 6 (l.47-48, l.210-260). Focus terms are words of three or more characters outside `_FOCUS_STOP` (l.60-75).
  - Broad questions add family siblings, up to `_FAMILY_MAX_SIBLINGS` 10 per family (l.264-287).
  - Facts: the current fact of each scalar key (l.142-154).
- **Answer** (`_generate_answer`, `answer_service.py:644-984`):
  - The focus key (l.580-586).
  - Broad versus specific (l.676-678). Focus terms: words of four or more characters outside `_FOCUS_STOPWORDS` (l.355-369, l.389-413), which include AMI words ("product", "feature", "device", "remote", "control").
    - The focus key's own label and alias words are removed from the focus terms (`_question_focus_terms`, l.405-413).
    - A question with no focus terms left counts as broad (l.676-678). The scalar focus gate runs only for a specific question that keeps focus terms (l.937-939). So this removal decides both broad versus specific and whether the gate runs.
  - The relevance filter for list-like answers: cosine ≥ `answer_relevance_min_similarity` 0.42 (`config.py:89`; l.416-455).
  - Canonicalisation of near-duplicates at `answer_canonical_min_similarity` 0.80 (`config.py:95`; l.463-524), with no cap (`answer_canonical_max_items` 0, `config.py:101`).
  - Rejection questions read REJECTED facts (l.734-788). Change questions read the facts first established in the latest meeting (l.589-634, l.794-822).
    - When `_REJECTION_Q_RE` matches (l.376-380, l.739), the current facts of any resolved key whose name contains `reject` are read as ruled-out values too (l.750-754). `get_current_collection` filters by status only (`app/db/repositories.py:294-305`), so scalar keys qualify.
  - **Scalar focus gate** (l.930-952): a specific question whose focus matches no candidate value is answered "unknown", and the held facts move to `near_matches` (l.319-321).
  - Answer status (l.260-280); mapped to the scorer's status by `runner.py:1067-1071`.

##### Parameters

| Parameter | Value in runs | Where | What it decides |
|---|---|---|---|
| `embedding_top_k`, `embedding_min_similarity`, `resolver_prune_threshold` | 8, 0.30, 12 | as in K2.6 | the question-time shortlist |
| `BROAD_LIST_MAX_KEYS` | 10 | `state_key_resolution_service.py:76` | cap on the keys a broad question resolves to |
| `embedding_score_weight` | 5.0 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:84` | weight of embedding similarity in the rule candidates used for widening |
| rule-scorer weights | alias 4.5–5.5 (substring) or 3.4–4.2 (token subset); key-token overlap 0.75 per token, at most 3; example overlap 0.5 per token, at most 2; decision-domain bonus 3.5 (DECISION_LOOKUP); intent bonuses 2.5 and 1.0 and canonical score 2.5, inert here | `state_key_resolution_service.py:745-807`, l.829-874 | which keys fill the broad-question slots |
| `_BROAD_CANDIDATE_RATIO`, `_BROAD_MAX_KEYS` | 0.25, 10 | `retrieval_service.py:41-42` | broad-question widening; the 0.25 ratio is inert on the LLM path, where all candidates share one score |
| `_VALUE_MATCH_COSINE`, `_VALUE_MATCH_MAX_KEYS` | 0.55, 6 | `retrieval_service.py:47-48` | keys pulled in by value match |
| `_FAMILY_MAX_SIBLINGS` | 10 | `retrieval_service.py:264` | family widening cap |
| `answer_relevance_min_similarity` | 0.42 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:89`; `answer_service.py:454` | which held values count as relevant; drives the scalar focus gate |
| `answer_canonical_min_similarity` | 0.80 (default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:95`; `answer_service.py:490` | near-duplicate values merged in answers; also A2's value equivalence (X.4) |
| `answer_canonical_max_items` | 0 (no cap; default; not recorded; not set in `.env`, the runner or the lane scripts) | `config.py:101` | cap on listed values |
| `_FOCUS_STOPWORDS` | as listed | `answer_service.py:355-369` | which question words count as focus |

##### Arm-specific

- No arm adds a model call here. The read contracts (`answer_evidence_fallback`; `answer_answerability_check`, with its key_answerability seam) are off in A0, A1 and A2.
- **Under A1, A2, WD:** no prompt change. A2 adds a disputed answer for open same-meeting conflicts (`answer_service.py:899-915`).
