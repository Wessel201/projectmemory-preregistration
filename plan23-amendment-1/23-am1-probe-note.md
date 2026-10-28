# Plan 23, amendment 1: the probe note (Step 0)

Dated **27 October 2026.** Status: **draft, for signing with the amendment.**

**What it fixes.** The amendment leaves two inputs of Step 2b's probe (i) to this note (`23-plan-amendment-1-ceilings-and-root-cause.md:117`, `:244`, `:246`):
- Part 1: the neutral example text for condition (b2), "in place of the AMI role examples";
- Part 2: gpt-5.4's settings for condition (d).

Part 3 lists the other probe inputs that the amendment does not fix, each with a proposal. The amendment requires that "All conditions are fixed here or in the dated probe note" (`:239`).

The section "Owner or role claim on EL2020 (C41, M-17)", after Part 3, defines one condition of Step 2c's WD rule on claims (decision sheet C41; mapping decision M-17). It is not a probe input.

**How it is bound.** It is signed and committed with the amendment. After signing it changes only by a dated note that says what had been read by then (amendment `:16`).

**How it was made.** Offline only. No LLM, embedding or other API call was made, and no test call. The code was read at 3320375 with `git show`. The working tree's `app/` does not differ from 3320375. The recorded prompts were read from the trace files of the nine EL2020 cycle-2 runs (a0_r1–r3, a1_r1 (the A1 smoke run), a1_r2, a1_r3, a2_r1, a2_r2b, a2_r3). The RAG runs keep no trace file and make no extraction call.

---

## Part 1. The neutral examples for (b2)

### 1.1 What the AMI role examples are

**Where the prompt comes from.** The extraction system message is the instructions plus the registry (`3320375:app/services/extraction_service.py:285-296`). The instructions are `EXTRACTION_BASE_INSTRUCTIONS` (`:177-211`), with two switches applied (`:271-282`):
- `expansion_force_scalar` defaults to `True` (`3320375:app/core/config.py:137`). It replaces `_COLLECTION_PREFERENCE` by `_SCALAR_PREFERENCE` (`extraction_service.py:224-233`, `:278-279`).
- `extraction_whole_decisions` was off in all nine runs (`cycle2_flags` in each run's `coldstart.json`). So `_whole_decision_instructions` was not applied (`:280-281`).

**What the prompt contains.** It has no worked example. There is no example transcript and no example JSON output. Its examples are short quoted phrases inside the instructions.

**The AMI role examples** are in one instruction, the assignment and ownership rule. As rendered in every recorded extraction system message (built from `3320375:app/services/extraction_service.py:201-207`):

> "Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager'), predicate 'owns'. Capture the owner even when phrased as 'The <Role> will <task>'. Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner."

So the AMI role examples are **three phrasing examples and four role titles.** Facts about them:
- They are the four roles of the AMI scenario meetings.
- The four titles are the four ES2009a gold values of `action.workstream.owner`: `data/ami_eval/gold/reviewed/ES2009.reviewed.yaml:201` ("value: Industrial Designer"), `:222` ("value: Marketing Expert"), `:242` ("value: User Interface Designer"), `:262` ("value: Project Manager").
- Two phrasing examples follow the wording of two gold summary sentences: "The Industrial Designer will prepare a definition of the basic functions" (`ES2009.reviewed.yaml:209`) and "The Marketing Expert will define the needs and desires of the user." (`:230`).
- The phrasing examples and 'Industrial Designer' entered at f8770f1 (23 June 2026, "p3-p5"); the list of four titles entered at 3f297c4 (24 June 2026, "hybid pre"); both by `git log -S`. Both are unchanged at 94c049d (`94c049d:app/services/extraction_service.py:202`, `:204`).
  - Check: `EXTRACTION_BASE_INSTRUCTIONS`, evaluated with `ast` at each commit, contains S1 and S2 of §1.4 this often: f8770f1 once and never; 3f297c4, 94c049d and 3320375 once and once; the parent of f8770f1 never and never.
  - At f8770f1 the phrasing example with 'User Interface Designer' is split across two source lines (`f8770f1:app/services/extraction_service.py:202-203`). So `git log -S` on that title alone points to 3f297c4. The `ast` count is the reliable evidence.
- They are prompt text, so they are an implementation entry (amendment `:107`). They are also older than cycle 1.

**Cross-check against the recorded prompts.** The static part of the system message is the text before the separator `"\n\nRegistry of state keys (the domain definition):\n"` (`extraction_service.py:290`).

| Check | Result |
|---|---|
| Extraction calls in the nine runs | 1,152 (a0: 129, 124, 129; a1: 128, 127, 130; a2: 128, 129, 128) |
| Model, as recorded per step | `mode` "llm", `model` "gpt-5.4-mini", `served_model` "gpt-5.4-mini-2026-03-17", in all 1,152 |
| `fallback` or `error` recorded | none |
| Recorded input | a JSON object with `messages` (one system, one user message) and `response_schema` "LLMExtractionResponse" |
| Distinct static parts | **one**, in all nine runs and all three arms |
| Static part rebuilt from the code at 3320375 (base instructions with the scalar preference) | identical to the recorded one |
| Length; SHA-256 (UTF-8) | 2,385 characters; `780d420c96f39522e48d2b824e6e7e5158d9156ebac357889c933fae6105bd0c` |
| The two old strings of §1.4 | each exactly once in every static part; never in a registry part or a user message |

The design-and-controls register's companion file `23-am1-prompts-evaluated.md` hashes the same text with `⟦registry⟧` in place of the registry. Under that convention the hash is `725f1c00a2d188376cc361f2a939d1e564b1d6ba810a277d276962e95843663f`, the hash that file lists.

### 1.2 What the examples teach, and what (b2) leaves alone

The prompt has no polarity, modality, rejection or supersession case tied to the role examples, and no supersession example at all (gloss, from reading `extraction_service.py:177-211`). So "the same cases" reduces to the roles each example plays. The column "Teaches" is my gloss.

| Id | Old (verbatim) | Teaches | New (verbatim) |
|---|---|---|---|
| E1 | 'The Industrial Designer will prepare X' | a future assignment, "The <Role> will <task>", to a two-word title | 'The Payroll Specialist will prepare X' |
| E2 | 'Marketing will define Y' | a role named only by its function word | 'Legal will define Y' |
| E3 | 'the User Interface Designer is responsible for Z' | the "is responsible for" form; a three-word title; lower-case "the" inside the sentence | 'the Vehicle Fleet Specialist is responsible for Z' |
| T1 | 'Industrial Designer' | the owner value for E1 | 'Payroll Specialist' |
| T2 | 'Marketing Expert' | the full title behind E2's function word, which begins with that word | 'Legal Counsel' |
| T3 | 'User Interface Designer' | the owner value for E3 | 'Vehicle Fleet Specialist' |
| T4 | 'Project Manager' | a fourth role, the coordinating one, which no phrasing example uses | 'Facilities Coordinator' |

**Structure kept:**
- the count: three phrasing examples and four titles, in the same order and the same two places;
- E1 and E3 share a head noun, as before ('Designer' becomes 'Specialist');
- T2 begins with E2's function word, as before;
- the placeholders X, Y and Z, and the verbs 'prepare', 'define' and 'is responsible for', are unchanged;
- the length: the static part stays at 2,385 characters (E-string 121 to 117 characters, T-string 94 to 98).

The verbs 'prepare' and 'define' also occur in the two ES2009 gold summary sentences quoted in §1.1. They are kept because they belong to the phrasing, not to the domain (decision PN-2).

**Unchanged by (b2), verbatim in the static part:**
- the owner rule around the examples, including "Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner.";
- the output fields and values: `state_key_hint`, `object_value`, `subject`, `predicate` (with 'owns'), `polarity`, `modality`, `extraction_confidence`, and "the owner/assignment registry key";
- the polarity cues ("'off the table', 'ruled out', 'not going with', \"won't use\"") and the modality cues ("'decided', 'locked in', 'going with'"; "'leaning', 'not locked in'"; "'option', 'considering'"). They are domain-neutral (gloss).

**Product wording that stays** (not role examples; decision PN-1):
- "object_value: the specific value — a decided feature, a chosen option, an owner's name, etc." (`extraction_service.py:184`);
- "For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value." (`:194-195`);
- "Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively." (`:199-200`).

### 1.3 The neutral domain and the overlap check

**Domain:** the support functions of any organisation (payroll, legal, vehicle fleet, facilities). It is neither AMI product design nor the ELITR project's domain (speech, annotation, language data, research). Gloss: these roles belong to no particular project type, so they add no new domain to the prompt (but see "Topical proximity" below). A precedent in the code: the whole-decision rule's examples "are generic on purpose: no development or test series supplies them." (`3320375:app/services/extraction_service.py:238-239`).

**Overlap check.** Whole-word, case-insensitive, with plural forms, over:
- the gold: `data/ami_eval/gold/reviewed/EL2020.reviewed.yaml` and `ES2009.reviewed.yaml` (every key, value, alias, topic, question, summary and note; transcript quotes are covered by the transcripts), `data/ami_eval/gold/generated/ES2009.timeline.json`, and the four files in `data/ami_eval/gold/audits/`;
- the suites: `transfer_el2020.yaml` (questions and the embedded EL2020a–d transcripts), `cold_start_es2009.yaml`, `pilot_es2009.yaml`, `dev_selection_es2009.yaml`, `lifecycle_probes.yaml`;
- the transcripts `data/ami_eval/transcripts/ES2009a.txt`–`ES2009d.txt`, and the span texts of all 1,152 recorded extraction user messages;
- the key definitions in the nine runs' `state.json`, the registry parts of the 1,152 recorded extraction system messages, and the AMI reference ontology `data/ami_eval/registry.yaml`.

| Word or title | Gold and suites | Transcripts | Run registries and ontology |
|---|---:|---:|---:|
| payroll, legal, counsel, vehicle, fleet, specialist, facilities, coordinator | 0 | 0 | 0 |
| 'Payroll Specialist', 'Legal Counsel', 'Vehicle Fleet Specialist', 'Facilities Coordinator' | 0 | 0 | 0 |

Rejected during the check, because a word occurred: 'Procurement' (a run registry key `procurement.headphones.order_status` in a0_r3 and a key description in a2_r3), 'Operations' (keys `operations.post_office` in a2_r3), 'Maintenance' (a0_r3 registry), 'Fire Safety' ("the possibility of the remote catching on fire", `data/ami_eval/transcripts/ES2009b.txt:14`), 'Team', 'Officer', 'Quality', 'Human', 'Manager' (gold or suite text).

**Near-forms.** The rule covers whole words and plural forms only. Near-forms of 'Coordinator' fall outside it, and they do occur:
- 'coordinated' in the span text (`data/ami_eval/suites/transfer_el2020.yaml:603`, and in recorded user messages);
- 'coordinate', 'coordinates', 'coordinating' or 'coordination' in key definitions in the `state.json` of six of the nine runs (a0_r2, a0_r3, a1_r1, a1_r3, a2_r2b, a2_r3).

The result of the check does not change.

**Topical proximity (not covered by the lexical check).** Two of the four new titles name office and logistics functions ('Facilities Coordinator', 'Vehicle Fleet Specialist'). EL2020 has this topic as content that the suite expects the system to ignore:
- "there is twenty headphones in a box now in our room and I put it to secretary yet." (`data/ami_eval/suites/transfer_el2020.yaml:489`);
- the noise question `EL2020a_noise_N2`, family `noise_resistance`, "Has a decision been made about sending headphones by post?", with `expected_status: unknown` (`transfer_el2020.yaml:3337-3346`).

The runs registered keys on this topic, for example:
- `organization9.inventory.headphones.owner` in a1_r1, an owner key, defined as "The person or role currently responsible for owning the headphones inventory at the organization.";
- `logistics.headphones.postage_method` and `operations.post_office.queue_length` in a2_r3;
- `procurement.headphones.order_status` in a0_r3.

The static part itself says "ignore social, logistics, and unrelated content." No EL2020 gold value is about this topic; the gold names it only in noise item N2 (`data/ami_eval/gold/reviewed/EL2020.reviewed.yaml:1627-1628`). So any effect on (b2) scoring is indirect. See decision PN-2.

### 1.4 The substitution, exactly

**Input:** the system message of a case's condition (b) prompt, that is, the recorded system message after its registry cut (Part 3, P5).

**Steps:**
1. Split the system message at `SEP = "\n\nRegistry of state keys (the domain definition):\n"`. It occurs exactly once. The static part is the text before it.
2. Check the static part's SHA-256: `780d420c96f39522e48d2b824e6e7e5158d9156ebac357889c933fae6105bd0c`.
3. In the static part only, replace S1 and S2. Each old string must occur exactly once.
4. Check the new static part's SHA-256: `a3b0de5b259faaf1fa76352531ce7263c73803a42ebd1e70ab2fc2bf1acc02cf`.
5. Rejoin: new static part + `SEP` + the (b) registry part. The user message is unchanged.

If a check fails, (b2) is not run on that prompt, and the probe stops for a dated note.

| | Old text (verbatim) | New text (verbatim) |
|---|---|---|
| S1 | `('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z')` | `('The Payroll Specialist will prepare X', 'Legal will define Y', 'the Vehicle Fleet Specialist is responsible for Z')` |
| S2 | `(e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager')` | `(e.g. 'Payroll Specialist', 'Legal Counsel', 'Vehicle Fleet Specialist', 'Facilities Coordinator')` |

The same, as Python:

```python
import hashlib

SEP = "\n\nRegistry of state keys (the domain definition):\n"
S1_OLD = "('The Industrial Designer will prepare X', 'Marketing will define Y', 'the User Interface Designer is responsible for Z')"
S1_NEW = "('The Payroll Specialist will prepare X', 'Legal will define Y', 'the Vehicle Fleet Specialist is responsible for Z')"
S2_OLD = "(e.g. 'Industrial Designer', 'Marketing Expert', 'User Interface Designer', 'Project Manager')"
S2_NEW = "(e.g. 'Payroll Specialist', 'Legal Counsel', 'Vehicle Fleet Specialist', 'Facilities Coordinator')"
RECORDED = "780d420c96f39522e48d2b824e6e7e5158d9156ebac357889c933fae6105bd0c"
NEUTRAL = "a3b0de5b259faaf1fa76352531ce7263c73803a42ebd1e70ab2fc2bf1acc02cf"

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def to_b2(system_message: str) -> str:
    parts = system_message.split(SEP)
    assert len(parts) == 2
    static, registry = parts
    assert sha256(static) == RECORDED
    for old, new in ((S1_OLD, S1_NEW), (S2_OLD, S2_NEW)):
        assert static.count(old) == 1
        static = static.replace(old, new)
    assert sha256(static) == NEUTRAL
    return static + SEP + registry
```

**Hashes** (UTF-8, no trailing newline):

| Static part | Characters | SHA-256 | SHA-256 with `SEP` + `⟦registry⟧` appended (convention of `23-am1-prompts-evaluated.md`) |
|---|---:|---|---|
| Recorded (A0, A1, A2) | 2,385 | `780d420c96f39522e48d2b824e6e7e5158d9156ebac357889c933fae6105bd0c` | `725f1c00a2d188376cc361f2a939d1e564b1d6ba810a277d276962e95843663f` |
| (b2) | 2,385 | `a3b0de5b259faaf1fa76352531ce7263c73803a42ebd1e70ab2fc2bf1acc02cf` | `c6961c4451327bd81f9f86858925ef0311f32cc4ed9ac0815cacb0b5cf0f4e27` |

**The (b2) static part, in full:**

```text
You extract project-state claims from meeting transcripts and project documents. Return ONLY valid JSON matching LLMExtractionResponse — no preamble, no markdown fences.

The project's state is defined by the registry of state keys below. Extract every claim the text supports about those keys; ignore social, logistics, and unrelated content.

For each claim emit an LLMClaim with:
  state_key_hint: the registry state_key the claim is about, or null if none fits.
  object_value: the specific value — a decided feature, a chosen option, an owner's name, etc.
  subject: a short subject for the claim.
  predicate: 'decided' | 'selected' | 'rejected' | 'proposed' | 'considered' | 'owns' | similar.
  polarity: NEGATIVE when the value is explicitly or implicitly rejected or ruled out — paraphrase negation counts ('off the table', 'ruled out', 'not going with', "won't use"). POSITIVE otherwise.
  modality: ASSERTED for firm decisions ('decided', 'locked in', 'going with'); HEDGED for tentative ('leaning', 'not locked in'); PROPOSED for candidates ('option', 'considering'); HYPOTHETICAL for future speculation.
  extraction_confidence: 0.0–1.0.
For a collection-valued key (e.g. a list of decided features or owners), emit one claim per value.
Key selection: map each claim to the MOST SPECIFIC matching registry key — the key about exactly this item/attribute, never a broad catch-all key. One claim per independent item. Extract a feature even when it is only proposed or considered (set modality accordingly); meetings often decide features tentatively.
Assignment / ownership: when the text assigns a task or responsibility to a ROLE ('The Payroll Specialist will prepare X', 'Legal will define Y', 'the Vehicle Fleet Specialist is responsible for Z'), ALSO emit a claim keyed to the owner/assignment registry key with object_value = the ROLE/title (e.g. 'Payroll Specialist', 'Legal Counsel', 'Vehicle Fleet Specialist', 'Facilities Coordinator'), predicate 'owns'. Capture the owner even when phrased as 'The <Role> will <task>'. Prefer the role/title; do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner.

Also populate decisions, action_items, risks, and open_questions when the text contains them, tagging each with the most relevant registry state_key (or null).
Return empty lists when the span carries no project state.
```

**On ES2009 (the 3b run).** There the role examples are in-domain: they are four ES2009a gold values (§1.1). A (b2) result on that run therefore tests the role examples, not out-of-domain examples (decision PN-3, which also covers how such a result is labelled). If Step 4 or 2c changes the extraction instructions before Step 5, the hash checks of steps 2 and 4 no longer hold for the 3b run; see Part 3, P12.

---

## Part 2. gpt-5.4's settings for (d)

### 2.1 The recorded gpt-5.4-mini call

**Code path at 3320375:**
- `_extract_with_llm` builds the messages and calls `llm_or_rules` with `LLMExtractionResponse` (`app/services/extraction_service.py:539-543`). That calls `llm_client.structured_completion(messages, response_schema)` (`app/llm/guarded.py:103`).
- The client comes from the factory: `model = settings.llm_seam_models.get(seam, settings.llm_model)`, with `temperature=settings.llm_temperature`, `max_attempts=settings.llm_max_attempts`, `request_timeout=settings.llm_request_timeout` and `sdk_max_retries=settings.llm_sdk_max_retries` (`app/llm/factory.py:77-87`).
- Defaults: `llm_model: str = "gpt-5.4-mini"` (`app/core/config.py:21`), `llm_temperature: float = 0.0` (`:22`), `llm_max_attempts: int = 3` (`:26`), `llm_request_timeout: float = 120.0` (`:31`), `llm_sdk_max_retries: int = 4` (`:37`).
- The batch launch scripts pass "--temperature 0.0", "--model gpt-5.4-mini" and "--judge-model gpt-5.4-2026-03-05 --base-url https://api.openai.com/v1" (`data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/run_lane.sh:6`, `:8`, `:9`; `data/ami_eval/a1_smoke/el2020_a2_rag_20261023T061545Z/run_lane.sh:7`, `:9`, `:10`). They set no timeout or retry setting. The runner writes `LLM_TEMPERATURE` from the run config (`app/evaluation/ami/runner.py:602`).
- `.env` sets none of `LLM_MAX_ATTEMPTS`, `LLM_REQUEST_TIMEOUT` and `LLM_SDK_MAX_RETRIES` (checked by the main session; this note did not open `.env`). At 3320375, `git grep` finds no other setter of these settings in `app/` or `scripts/`, apart from `scripts/run_concept_experiments.py:107` and the rescoring contract (`app/evaluation/ami/rescore.py:446-447`). The launch scripts call `app.cli.main run-ami-eval`, not those. So the code defaults applied.
- The A1 smoke run keeps no launch script. Its report, like the other eight, records model "gpt-5.4-mini" and judge model "gpt-5.4-2026-03-05" in its `config` block. Every trace lists one served model, "gpt-5.4-mini-2026-03-17" (`served_models`), so no seam ran on another model.

**The request** (`3320375:app/llm/openai_llm.py:163-177`):

```python
                kwargs: dict = {
                    "model": self._model,
                    "response_format": {
                        "type": "json_schema",
                        "json_schema": {
                            "name": response_schema.__name__,
                            "schema": schema,
                            "strict": strict,
                        },
                    },
                    "messages": oai_messages,
                }
                if send_temperature:
                    kwargs["temperature"] = self._temperature
                response = self._client.chat.completions.create(**kwargs)
```

- `schema` is the pydantic schema of `LLMExtractionResponse` (`app/schemas/llm_extraction.py:47-52`), made strict by `_strictify_schema` (`openai_llm.py:26-51`, `:134`). `strict` is `_is_strict_safe(schema)` (`:54-67`, `:139`).
- Computed offline (pydantic 2.13.4 in the project `.venv`): `strict` is `True` for this schema. The `response_format` object, as sorted-key compact JSON, has SHA-256 `39b5548a5b67b3b1da180dd7fb86635ec1e1328d25567fd8b1c5957ff9f09f99`. The pydantic version of the runs is not recorded.
- No other parameter is sent. `openai_llm.py:177` is the only completion call in `app/` at 3320375, and no code sets a reasoning, token-limit, seed or sampling parameter (`git grep`; gloss).
- The trace records neither the shed parameters nor the attempt metadata of these calls. It records only `response_schema`, the messages, the served model and the response id.

### 2.2 How the judge calls gpt-5.4

- The judge builds the same client class, `self._client = OpenAILLMClient(` with `temperature=0.0,` (`3320375:app/evaluation/ami/judge.py:73-80`, the temperature at `:75`). It calls `self._client.structured_completion(messages, JudgeResponse)` (`:97`). So its request has the same shape as §2.1: model, a strict `json_schema` response format, messages and temperature 0.0.
- The model id is `gpt-5.4-2026-03-05`:
  - every run's report records `"judge_model": "gpt-5.4-2026-03-05"` (for example `data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/a1_r2/artifacts/project-memory-cold-start-live_20261022T214829Z_15995a72.coldstart.json:23`);
  - the rescoring code pins `MODEL = "gpt-5.4-2026-03-05"` (`3320375:app/evaluation/ami/rescore.py:41`);
  - the CLI default "gpt-5.4" (`app/cli/main.py:189`) was not used by these runs.
- **Working calls on record.** The bug-7 rescoring of 22 October 2026 used this client through `DurableJudge` (`app/evaluation/ami/rejection_rescore.py:55-56`). `DurableJudge` refuses a call unless "actual_model" equals the contract's model and `actual.get("temperature_sent") is True and actual.get("temperature") == 0.0` and `actual.get("strict_schema") is True` (`3320375:app/evaluation/ami/rescore.py:414-419`). Its records (`data/ami_eval/rejection_rescores/bug7_20261022T194724Z/judgments/`, 132 files; `status.json`: "status": "COMPLETE", 132 of 132) show for every call:
  - one provider attempt, with `validation_outcome` "ok";
  - `intended_model` and `actual_model` both "gpt-5.4-2026-03-05";
  - `actual_parameters` with `strict_schema` true, `temperature` 0.0 and `temperature_sent` true;
  - `reasoning_tokens` 0;
  - `sdk_max_retries` 0. The rescoring contract set it (`3320375:app/evaluation/ami/rescore.py:446-447`). (d) runs with the default of 4 (§2.3). This is a client setting, not a request parameter, so the request is not affected.
- `openai_llm.py` and `judge.py` last changed at c2109bf (19 September 2026), so the bug-7 calls ran the client code of 3320375.
- **Limit of this evidence:** those calls used the short judge prompt and the `JudgeResponse` schema, not the long extraction prompt and `LLMExtractionResponse`.
- **Bound on a (d) result:** (d) sends no reasoning setting, so gpt-5.4 runs at its default. In the 132 bug-7 calls that default produced no reasoning tokens. A (d) result is therefore bounded to this setting. A (d) *not recovered* does not show that gpt-5.4 with reasoning would fail. The (d) report gives each output's reasoning tokens (§2.3).

**Conclusion.** The judge's working calls send to gpt-5.4 exactly the parameter set of the recorded gpt-5.4-mini call. So the code gives no evidence that gpt-5.4 needs a different parameter. Condition (d) changes the model only.

### 2.3 The settings for (d), fixed

| Item | Condition (a), the recorded call | Condition (d) |
|---|---|---|
| Endpoint | `chat.completions.create`, `https://api.openai.com/v1` | same |
| `model` | "gpt-5.4-mini" (served gpt-5.4-mini-2026-03-17) | **"gpt-5.4-2026-03-05"** |
| `messages` | the recorded system and user messages, verbatim, with the recorded registry | same as (a) (the amendment's "recorded prompt", `:246`) |
| `response_format` | `json_schema`, name "LLMExtractionResponse", strict schema, `"strict": true` | same (SHA-256 above) |
| `temperature` | 0.0 | 0.0 |
| Any other parameter | none | none |
| Client | `OpenAILLMClient.structured_completion` at 3320375; 3 attempts, 120 s timeout, 4 SDK retries (code defaults, §2.1) | same |
| Repeats | three | three (amendment `:241`) |

**Run and record.** (d) is issued through `OpenAILLMClient.structured_completion` at 3320375, unchanged. Each output keeps its attempt envelope (`last_call_attempts`; `openai_llm.py:251-335`): the actual model, the response id, the usage including reasoning tokens, and `actual_parameters`.

### 2.4 Rule for a parameter the model rejects (fixed now; no test call was made)

1. **The client's own shedding applies, unchanged** (`openai_llm.py:194-215`):
   - on a 400 whose message contains "temperature", the call is re-sent without `temperature` (`:208-210`);
   - on any other 400 while the schema is strict, it is re-sent with `"strict": false` (`:211-213`);
   - otherwise the error is raised (`:214-215`).
2. **No other change is made at run time,** whatever the error. No parameter is added, such as a reasoning setting, a token limit or a seed. The model id is not changed.
3. **An output produced after shedding counts.** It is listed in the (d) report with the shed parameter. The report gives the number of (d) outputs with `temperature_sent` false or `strict_schema` false. On the bug-7 record no shedding is expected (§2.2).
4. **The served model must be "gpt-5.4-2026-03-05".** If another model is served, that output is not used, and the probe stops for a dated note.
5. **A call that still fails** follows the missing-output rule (P10).

---

## Part 3. Other inputs the amendment leaves to the note

### 3.1 Already fixed by the amendment (repeated here, not changed)

- **Cases:** every extraction-lost case except `admitted:ignored`, which is listed apart (`:241`).
- **Runs:** the author-sampled A1 and A2 runs, and on 3b's Step 5 run only probe (i) (`:238`).
- **Conditions:**
  - (a) to (d), three repeats each (`:241-246`);
  - (b) at `embedding_top_k`=8 and `embedding_min_similarity`=0.30, without the lexical part of `_prompt_registry` (`:243`);
  - (d) only on cases that (b) and (b2) do not recover (`:246`); the reading of "do not recover" is P8.
- **Scoring:** at the case's own boundary, with the loss-trace matcher and an adjudication batch file (`:237`).
- **Rules:** the recovery rule (`:262-269`) and the mapping (`:271-281`).
- **Blindness:** outputs are computed only into hashed files until Step 3 item 4 is committed (`:411`).

### 3.2 Left open; proposed here for signing

Each item is a proposal, decided at signing. The matching decision in the list below is named in brackets.

- **P1. Which recorded call is "the recorded prompt" [PN-7].** A span whose extraction returned nothing is extracted again at the next meeting (`23-loss-trace.md:82`), so one span can have several recorded calls. Proposal:
  - the last recorded extraction call on the cited span made by the case's checkpoint k;
  - with several cited spans, each is re-extracted under every condition, and output j of the case is the union of the j-th outputs over its cited spans;
  - a span that two or more cases of the same run cite at the same recorded call is re-extracted once per condition and repeat, and that output serves each of those cases. On the six A1 and A2 runs, the 184 cited spans of the probed cases are 161 distinct (run, span) pairs (P8);
  - spans next to the cited span are not re-extracted (amendment `:241`: "The cited span is re-extracted").
- **P2. `admitted:span_not_seen` cases [PN-8].** They have no recorded extraction call on a cited span (`23-loss-trace.md:34`). Proposal: list them apart with `admitted:ignored`, with no probe output. Probe (i) does not apply to them.
- **P3. When an output passes [PN-9].** The output's claims are the only claims, and all of them are local. Proposal: an output passes when it passes every extraction step up to and including the case's step (`carried`, `polarity`, `modality`; `23-loss-trace.md:34-37`), under the matcher and the sibling rule. A strong match counts. Any other candidate text goes to the adjudication batch file, under the two-adjudicator protocol.
- **P4. The control model [PN-4].** Proposal: (a), (b), (b2) and (c) send "gpt-5.4-mini", as recorded. Each output's served model must be the served model recorded in the case's own run ("gpt-5.4-mini-2026-03-17" for every EL2020 run, in all 1,152 recorded calls). Otherwise the probe stops for a dated note.
- **P5. The registry cut of (b), and so of (b2) [PN-5, PN-6].**
  - The base is the key lines of the recorded prompt, kept in their recorded order.
  - The query text is the span: the user message after "Extract project-state claims from:\n\n".
  - Each key is embedded with its `_key_profile` text (`3320375:app/services/state_key_resolution_service.py:663-674`):
    - its aliases come from the recorded prompt line;
    - its other fields come from the run's `state.json`.

    Gloss: the only code that changes a definition after creation appends aliases (`_add_aliases`, `3320375:app/services/registry_expansion_review_service.py:331-341`). In all nine runs, the recorded key lines differ from the final definitions only in their aliases, which are a subset of the final ones, on 0–9 keys per run.
  - The model is `text-embedding-3-small` (`config.py:77`), sent as `embeddings.create(model=self.model, input=texts)` (`app/llm/embeddings.py:80`).
  - Candidates: cosine ≥ 0.30, sorted by (−similarity, key), first 8 (`state_key_resolution_service.py:637-643`).
  - The other branches of `_prompt_registry` apply, and the range `:696-704` is removed [PN-5]:
    - no candidate keeps the whole registry (`:689-690`), so (b) equals (a) for that case, and this is listed;
    - a registry of at most 12 keys (`resolver_prune_threshold`) is kept whole (`:691-692`). The amendment's parameter list for (b) does not name this threshold (`:243`). It is included under the same reading as the no-candidate branch. No A1 or A2 extraction call had 1–12 keys, so this changes nothing on EL2020. It may on the 3b run.
    - The removed range holds the lexical clause and also the intent-primary keep (`:703`: `definition.supported_intents_json.get(intent.value) == "primary"`), which the amendment's "lexical part" does not name. Proposal: drop it too, so that the cut adds no key beyond the embedding candidates. On the claim path the resolver passes the fixed intent `QueryIntent.CURRENT_STATE_QUESTION` (`3320375:app/services/state_key_resolution_service.py:370-372`). In all nine runs every key definition in `state.json` has empty `supported_intents` (`{}`), so this keep adds no key on EL2020.
  - An empty registry is written as `_format_registry` writes it: "(no registry keys provided — use state_key_hint: null)" (`extraction_service.py:215-216`). That is also condition (c)'s registry part.
  - On 107 to 111 of the 127 to 130 extraction calls per A1/A2 run, the recorded registry is not empty. On the other 18 to 21 it is empty, so (a), (b) and (c) send the same prompt there.
- **P6. (b2) reuses (b)'s cut.** The cut is computed once per case and recorded with its embedding vectors (`RecordingEmbeddingClient`, `3320375:app/llm/embeddings.py:147-183`). (b) and (b2) then differ only by the substitution of §1.4, and (b2) needs no embedding call of its own.
- **P7. "A key holding the gold value" (recorded with the cut size, `:243`) [PN-11].** Proposal: a key of the recorded prompt under which the recorded run's final dump stores a fact carrying the gold value (matcher strong, or adjudicated). If there is none, "none in the run". This is a descriptor; it decides no result.
- **P8. The reading of "do not recover" in `:246` [PN-10].** The amendment fixes that (d) runs "only on cases that (b) and (b2) do not recover" (`:246`; §3.1). Proposal: read this as the result *not recovered* for both (b) and (b2) (k = 0 for each; k0 ≤ 1 is implied by the row order, `:262`), with an output for the control (a) (P10). Only these cases can reach a mapping row that uses (d): "Model-limited" (`:279`) and "Every applicable condition not recovered" (`:280`). In every other case (d) can only add to "no probe evidence" (`:281`). (c)'s result does not gate (d), as the amendment states.
  - **Cost bound for (d) (offline estimate, not a measurement).**
    - Cases: the lenient series of `23-loss-trace.json`; a case is (fact, loss step) at its earliest checkpoint, without `admitted:ignored`. There is no `admitted:span_not_seen` case. The six A1 and A2 runs have 139 probed cases (a1_r1 25, a1_r2 22, a1_r3 26, a2_r1 22, a2_r2b 24, a2_r3 20), with 184 cited spans. With (d) on every case at three repeats, that is 552 gpt-5.4 calls.
    - Basis: for each cited span, the median size of the recorded extraction prompt (system and user message) and of the recorded output at the span's meeting in its own run; about 4.0 characters per input token and about 3.1 per output token (the 22 October batch ledger, `data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/usage.json`, against the recorded traces of its five runs); the ledger prices for "gpt-5.4-2026-03-05" ($2.5 per million input tokens, $15 per million output tokens). The traces record the messages of 3,582 of the ledger's 4,371 gpt-5.4-mini calls, so the ratios, if anything, overstate the tokens.
    - Result: about $16 for (d) on every probed case. About $14 if each of the 161 distinct (run, span) pairs is re-extracted once (P1, PN-7), assuming every repeated pair is at the same recorded call.
    - Calibration: the same method, at the ledger's gpt-5.4-mini prices ($0.75 and $4.5 per million) and with the (b) and (c) registries cut as in P5, gives about $8.7 for (a)–(c), close to the amendment's "about $8" (`:581`).
    - The amendment estimates (d) at about $5–11 (`:581`). Under P8 the cost is lower than the maximum by a share that is unknown until (b) and (b2) are scored (PN-10, PN-14).
- **P9. Who computes the gating.** The probe script computes (b) and (b2)'s results from the scored, adjudicated outputs and writes the (d) case list to a hashed file. The author does not see it before Step 3 item 7 (`:411`).
  - Proposal on the list's size [PN-14]: the Step 2b go-ahead covers (d) at its maximum (P8), so no count of the (d) list is shown before item 7. Under the amendment, "the go-aheads for 2b and 2c rest on estimates. Any early read is logged with its date and contents." (`:411`). A second go-ahead based on the list's size would be such an early read.
- **P10. Missing outputs [PN-12].**
  - A *valid output* parses as `LLMExtractionResponse` and passes the seam guard of the recorded calls, `validate=lambda r: all(c.object_value for c in r.claims)` (`3320375:app/services/extraction_service.py:545`). In the recorded pipeline a failed guard fails the call (`3320375:app/llm/guarded.py:106-107`). The probe issues its calls through `structured_completion` directly (§2.3), so the probe script applies the guard itself, to every condition alike. An output that fails the guard counts as no output for that attempt. The recorded (a) calls all passed it (all 1,152 are recorded with `mode` "llm" and no error, §1.1), so applying it to (a) also reproduces the recorded condition.
  - A repeat without a valid output after the client's attempts is re-issued up to three times. If it still has none, that condition has *no output* for the case. Under the mapping that means no probe evidence (`:281`). It is never counted as a failing or passing repeat.
  - If the control (a) has no output for a case, k0 is undefined. The case has no probe evidence (`:281`), and (d) is not run for it (P8).
- **P11. Order of calls.** Cases are taken in the order of sha256(run_id|fact_id|k), as in the Step 3 sample. Within a case, the conditions are interleaved, repeat by repeat: (a), (b), (b2), (c), three times; (d) follows after gating. All conditions of a run are issued in one period.
- **P12. Prompts other than the evaluated one.** The substitution of §1.4 checks the recorded hash. If a Step 4 or 2c change alters the extraction instructions of the 3b run, the probe does not run (b2) on that run until a dated note records:
  - the new static part's hash;
  - that each old string occurs exactly once;
  - the hash after substitution.
- **P13. Budget guard.** If the probe runs under the study budget guard, its price table lists exactly the requested model ids ("gpt-5.4-mini", "gpt-5.4-2026-03-05", "text-embedding-3-small"). Otherwise the guard stops the call (`3320375:app/llm/study_budget.py:53-54`). The run ledgers of 22–23 October list these three (`data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/usage.json`). If the guard is used, its cap covers the probe's maximum with (d) on every probed case (P8) [PN-14]. Otherwise a guard stop during (d) would show the size of the (d) list, which is an early read under `:411`.

---

## Owner or role claim on EL2020 (C41, M-17)

Added 27 October 2026, before signing. Parts 1–3 fix Step 2b's probe (i). This section belongs to Step 2c.

**What it fixes.** The WD rule requires: "no owner or role claim is lost;" (amendment `:293`). The EL2020 gold has no owner or role items (decision sheet C41; mapping decision M-17, in `23-am1-register-claims.md` section 9, mapping section 8 "Gaps and decisions for you"; cited by heading, not line, so later edits do not move it). So the condition is defined here on claims. It is decided from what the six Step 2c runs record, and the suite's transcripts for placing spans, with no gold, no adjudication and no model call.

**How it was made.** Offline. The code was read at 3320375 with `git show`. Field names and types were checked in the frozen run a1_r2 (`data/ami_eval/a1_smoke/el2020_batch_20261022T214813Z/a1_r2/artifacts/`, its `trace.json` and `state.json`). No owner or role claim was counted in any run, and no claim of any run is quoted. The worked example is constructed.

**Where the condition comes from.**
- Plan 23 says of the whole-decision contract's build failures: "only the lost role claims were real." (`23-plan-development-and-confirmation.md:264`).
- The build diagnosis: "Under the variant, the role claims "Project Manager" and "Industrial Designer" disappear: the whole-decision rule swallows the separate owner claim that the assignment rule asks for." (`21-build-report.md:47`).
- In the prompt (gloss): WD treats parts that "answer one question (which languages, what the rule is, who does what by when)" as "one decision" (`3320375:app/services/extraction_service.py:258-259`). The assignment rule, which WD leaves unchanged, asks to "ALSO emit a claim keyed to the owner/assignment registry key" (`:203`), with "predicate 'owns'" (`:205`). WD only swaps the per-value sentence and appends its rule (`:264-268`, applied at `:280-281`).

### What the runs record

- Each extraction call is a `trace.json` step with `seam` "extraction". A successful call has `mode` "llm", and its `output` is the parsed response as returned, `parsed.model_dump()` (`3320375:app/llm/guarded.py:114`, `:116`). A failed call has `mode` "llm_error", the error, and an empty output (`:127-130`).
- The step's `input.messages[-1].content` is the user message: "Extract project-state claims from:\n\n" followed by the span text (`extraction_service.py:295`).
- Each item of `output.claims` has the fields of `LLMClaim`: `subject`, `predicate`, `object_value`, `polarity`, `modality`, `state_key_hint`, `extraction_confidence` (`3320375:app/schemas/llm_extraction.py:14-21`). Each item of `output.action_items` has `description` and `owner` (`:30-32`).
- WD changes the instructions only. The response schema is the same, so both arms record the same fields.
- A run's arm is read from `config.cycle2_flags` in its `coldstart.json`: `extraction_whole_decisions` true for a WD run, false for a fresh A1 run.
- The test uses the trace, not the `claims` of `state.json`, for two reasons:
  - there a claim's `state_key` is its key at the end of the run, not the extractor's hint, because filing reassigns it (`3320375:app/services/claim_reevaluation_service.py:84`; `3320375:app/services/conflict_service.py:911`);
  - `create_claim` returns the existing claim when a claim key repeats (`3320375:app/db/repositories.py:164-173`), so the dump folds repeated claims.

### (a) Which claims are owner or role claims

An item of an extraction call's `output.claims` is an **owner or role claim** if (P) or (K) holds.
- **(P) Predicate.** Take `predicate`, lower-case it, and replace "_" and "-" by spaces. It passes if one of its words (runs of letters) is in OWN, or if it contains one of the phrases "take over", "takes over", "took over", "taking over", "in charge".
- **(K) Hinted key.** `state_key_hint` is a string. Take the text after its last "." (the whole hint if it has no "."), lower-case it, and split it at "_" and "-". It passes if one of the pieces is in OWN.
- **OWN** = {own, owns, owned, owner, owners, ownership, assign, assigns, assigned, assignee, assignees, assignment, assignments, responsible, responsibility, responsibilities}.

Sources of the words: the prompt asks for "predicate 'owns'" and a claim "keyed to the owner/assignment registry key" (`extraction_service.py:203-205`). The code's own ownership words are "owner", "responsible", "owns", "will take over", "will own", "took over" (`3320375:app/services/memory_gatekeeper_service.py:66`). Its ownership patterns are "will take over", "owns", "is responsible for" and "is the owner of" (`extraction_service.py:134-137`). The expansion generator adds "lead" and "assigned to" (`3320375:app/llm/expansion_generator.py:116`); "lead" is left out of OWN (see Borderline cases). OWN adds the inflected forms (gloss).

The other fields are not tested: `subject`, `object_value`, `polarity`, `modality`, `extraction_confidence`. Whether the value names a person, a team or a role is not tested. That would need a judgement.

**Borderline cases, decided:**
- **Speaker attribution.** The span text carries speaker labels, such as "PERSON9:" at the start of a line (recorded user messages). A claim with a speaker as subject or value, and a predicate such as 'proposed', is not an owner claim unless (P) or (K) holds.
- **"Who will do X" as a claim.** A claim with predicate 'will prepare' and a person as subject is not an owner claim unless (P) or (K) holds. For that case the prompt asks for a separate claim: "Capture the owner even when phrased as 'The <Role> will <task>'." (`extraction_service.py:205-206`). That separate claim is the one the condition protects.
- **"Who will do X" as an action item.** An `action_items` entry with an `owner` is not a claim, and is not counted. It is stored as an action item (`extraction_service.py:587`), not filed into state. Gloss: at 3320375, `git grep` finds action items outside the extraction service only in the database layer, the projects API route, the state dump, artifact deletion and an intent label of the resolver prompt; no filing or answer code reads them. WD leaves the instruction that asks for action items unchanged (`:208-209`).
- **Vague groups.** An owner part (see (b)) equal to "team", "we" or "everyone" after normalisation does not form a unit. The prompt forbids these as owners: "do NOT emit a bare personal first name or a vague group ('the team', 'we', 'everyone') as the owner." (`extraction_service.py:206-207`). A named team counts, for example "ORGANIZATION9" or "the annotation team".
- **Negative, hedged and proposed owner claims** count. Polarity and modality are not tested.
- **Owner claims on noise topics** count. An example is a claim on an owner key about headphones (§1.3 records such a key, `organization9.inventory.headphones.owner`, in a1_r1). The test has no topic filter, because a topic filter needs a judgement.
- **"lead", "leads", "led", "handles"** are not in OWN, because "leads" also occurs in causal predicates such as "leads to" (gloss). A claim with such a predicate is an owner claim only through (K).

### (b) What "lost" means

- **Runs compared.** The three WD runs against the three fresh A1 runs of Step 2c, which is the WD rule's own contrast (amendment `:286`). The frozen 22 October A1 runs are not used: they ran at another commit, before the Step 0 instrument changes.
- **Boundary.** The extraction call's output. This is the boundary of the WD endpoint, `carried` (`:288`). Every extraction call of a run counts, up to its last checkpoint, re-extractions included (`23-loss-trace.md:82`). What happens to the claim after extraction (routing, filing, status) is not part of this condition.
- **Span.** An extraction call is placed on a span like `23-loss-trace.py` (which leaves an unmatched call unplaced instead of stopping). Its user message after "Extract project-state claims from:\n\n" is compared with the spans of the system's own segmentation of the suite transcripts (`render_spans`, `23-loss-trace.py:284-297`; the span table at `:409-414`; the lookup at `:436-439`):
  1. The call is placed on the span whose text it equals.
  2. Failing that, it is placed on the span whose text it equals after the same run's recorded redactions for that span are applied. These are the `output.redactions` of the run's `memory_gatekeeper` step on the span, found as at `23-loss-trace.py:416-419`. They are applied as `_apply_redactions` does: each fragment present is replaced once, in order (`3320375:app/services/evidence_service.py:78-85`). The extraction call receives the evidence text, which is made this way (`evidence_service.py:46`; `3320375:app/services/extraction_service.py:398`).
  3. A call that matches no span either way, or more than one, stops the computation for a dated note. A span whose gatekeeper step has no record with `mode` "llm" would land here. At 3320375 a failed gatekeeper call records an empty output and raises; it does not fall back to rules (`3320375:app/llm/guarded.py:14-15`, `:124-130`).

  This uses the suite's transcripts only, not its gold. The segmentation is the same in all six runs at one commit, so a span is one (meeting, index) in all of them.
- **Coverage.** A run covers a span if it has at least one extraction step on it, with `mode` "llm" or "llm_error". A failed call carries nothing, so a failure under WD counts as a miss, not as a gap in coverage. The gatekeeper decides which spans are extracted, and its prompt holds the span text only (`memory_gatekeeper_service.py:311-314`). So WD cannot change the gatekeeper's input, and coverage differs between runs by sampling (gloss).
- **Owner value.** An owner or role claim's value is its `object_value`, normalised:
  1. lower-case;
  2. delete the characters `[` `]` `(` `)` `"` `'`;
  3. collapse whitespace, and strip spaces and the characters `.` `,` `;` `:` at both ends;
  4. remove one leading "the ".

  Steps 1 and 3 extend `_norm` (`23-loss-trace.py:278-279`), which lower-cases, collapses whitespace and strips spaces and dots.
- **Owner parts.** The normalised value is split at ",", ";", "/", "&" and " and ". Each part is normalised again (steps 3 and 4), and empty parts are dropped.
- **Unit.** A pair (span, owner part) such that at least one fresh A1 run emits an owner or role claim with that part in an extraction call on that span. Units come from the fresh A1 runs only, because "lost" is relative to them.
- **Carried.** A run carries a unit if one of its extraction calls on the unit's span emits an owner or role claim that has the unit's part among its parts. So, where WD merges:
  - an owner or role claim whose value lists several owners ('PERSON7 and PERSON3') carries each of them;
  - an owner named inside a claim that is not an owner or role claim is not carried. A whole-decision value such as 'PERSON7 prepares the guidelines by Friday', with predicate 'decided', carries no unit. This is the loss the build diagnosis found (`21-build-report.md:47`, quoted above);
  - text containment is never used: a part is carried only by an equal part.
- **Counts per unit:**
  - *a*: the fresh A1 runs that carry it (0–3);
  - *w*: the WD runs that carry it;
  - *m*: the WD runs that cover its span and do not carry it.
- **Lost.** A unit is lost when *a* ≥ 2 and *m* ≥ 2. In words: at least 2 of the 3 fresh A1 runs carry the owner claim, and at least 2 of the 3 WD runs extract the span without it. *m* ≥ 2 implies *w* ≤ 1. This is criterion (iv) mirrored, with WD runs that do not cover the span left out. Under (iv), WD gains a value when it carries it "in at least 2 of 3 WD runs, while the fresh A1 runs carry it in at most 1 of 3" (`:352`), so a fresh A1 run that never extracts the span counts as not carrying. The exact mirror is *a* ≥ 2 and *w* ≤ 1, with only the units that no WD run covers set apart ("No WD run covers the value: unclear.", `:356`). The draft sets apart every unit with *a* ≥ 2, *w* ≤ 1 and *m* ≤ 1 (choices 5 and 6).
- **Not covered by WD.** One rule holds under every threshold of choice 5. A unit whose span no WD run covers is not lost; otherwise a unit the threshold counts as lost is lost. Listed apart are the units with *a* ≥ 2 and *w* ≤ 1 that are not lost and whose span at least one WD run does not cover (*w* + *m* ≤ 2). Each is listed with each WD run's gatekeeper policy for the span (`extraction_policy` of its `memory_gatekeeper` step). Such a unit does not decide the condition, because at least one WD run never extracted the span. Under the drafted threshold the units listed apart are those with *a* ≥ 2, *w* ≤ 1 and *m* ≤ 1, so fewer than 2 WD runs can show a loss.

### (c) The decision

- The condition "no owner or role claim is lost" (`:293`) **fails if at least one unit is lost.** Otherwise it holds.
- If no unit has *a* ≥ 2, the condition holds, and the Step 2c report says that no unit could be lost.
- The Step 2c report lists every unit with its span, *a*, *w* and *m*, and lists the units not covered by WD apart.
- The computation is mechanical. It runs with the other conditions of the WD rule into the hashed Step 2c outputs, which are opened at the reveal (`:411`, item 7).

### Worked example (constructed, not from any run)

A span, as the user message of an extraction call would hold it:

```text
Extract project-state claims from:

PERSON3: Okay, so [PERSON7] will prepare the annotation guidelines by Friday.
PERSON7: Yes, I will do it.
```

**Fresh A1 run 1.** Two items of the call's `output.claims`:

```json
{"subject": "annotation guidelines", "predicate": "will prepare", "object_value": "annotation guidelines by Friday", "polarity": "positive", "modality": "asserted", "state_key_hint": null, "extraction_confidence": 0.9}
{"subject": "annotation guidelines", "predicate": "owns", "object_value": "[PERSON7]", "polarity": "positive", "modality": "asserted", "state_key_hint": "project.annotation_guidelines.owner", "extraction_confidence": 0.9}
```

- First item: the words "will" and "prepare" are not in OWN, and there is no hint. It is not an owner or role claim.
- Second item: "owns" is in OWN under (P), and "owner" is in OWN under (K). Its value normalises to "person7". This gives the unit (this span, "person7").
- Suppose fresh A1 runs 2 and 3 emit the same owner claim with value "PERSON7". Then *a* = 3.

**WD run 1:**

```json
{"subject": "annotation guidelines", "predicate": "decided", "object_value": "PERSON7 prepares annotation guidelines by Friday", "polarity": "positive", "modality": "asserted", "state_key_hint": "project.annotation_guidelines.deadline", "extraction_confidence": 0.9}
```

"decided" is not in OWN, and neither is "deadline". So this is not an owner or role claim. The run covers the span and does not carry "person7". The value contains "PERSON7", but containment does not count.

**WD run 2:**

```json
{"subject": "annotation guidelines", "predicate": "assigned_to", "object_value": "PERSON7 and PERSON3", "polarity": "positive", "modality": "asserted", "state_key_hint": null, "extraction_confidence": 0.9}
```

"assigned_to" becomes "assigned to", and "assigned" is in OWN. Its parts are "person7" and "person3". It carries the unit. ("person3" is not a unit, since no fresh A1 run emits it.)

**WD run 3,** two alternatives:
- The gatekeeper gave the span another policy, so there is no extraction call on it. Then *w* = 1 and *m* = 1. The unit is listed as not covered by WD and does not fail the condition.
- Run 3 extracts the span and emits only a claim like WD run 1's. Then *w* = 1 and *m* = 2. The unit is lost, and the condition fails.

### Limits

- The unit is the owner within a span, not the matter owned. If one span assigns two matters to one person, and WD keeps the owner claim for one matter only, the loss is not seen. Matching the matter (`subject`) would need a judgement.
- Parts must be equal. If WD writes a kept owner in another form ('PM' against 'Project Manager'), it counts as lost. If the fresh A1 runs write one owner in different forms, no form may reach *a* ≥ 2, and the unit is not formed.
- A claim that puts the owner in `subject` and the task in `object_value` forms a unit whose part is the task. If the arms differ in this, a kept owner can count as lost.
- An owner claim that WD emits only from a neighbouring span counts as not carried.
- (P) is a closed word list, and (K) depends on each run's own key names. An owner claim with another predicate and a key without an OWN word is missed, in both arms alike. (P) can also catch a non-ownership use of an OWN word (gloss).
- The thresholds do not see a loss in a single WD run.

### Choices for the author (C41)

Each choice is drafted as above. The alternative is given.
1. **The test.** Drafted: (P) or (K), with OWN and the phrases. Alternative: the prompt's literal predicate 'owns' only.
2. **Action items.** Drafted: not counted. Alternative: count an `action_items` entry with a non-null `owner` as an owner claim.
3. **Boundary.** Drafted: the extraction output. Alternative: also require the owner claim to be filed under a key by the last checkpoint.
4. **Merges.** Drafted: an owner named only inside a claim that is not an owner or role claim counts as lost; an owner claim listing several owners carries each. Alternative: containment of the owner part in any claim value of the span counts as carried.
5. **Thresholds.** Drafted: lost when *a* ≥ 2 and *m* ≥ 2, which is (iv) mirrored, with WD runs that do not cover the span left out. Alternatives: *a* ≥ 2 and *m* ≥ 1 (any WD miss); *a* ≥ 2 and *w* = 0; or *a* ≥ 2 and *w* ≤ 1, with units no WD run covers listed apart (the exact mirror of (iv) and `:356`).
6. **Spans not covered by WD.** Drafted: listed apart, never deciding, by the one rule of "Not covered by WD" above, under every threshold of choice 5. A unit whose span no WD run covers is not lost; otherwise a unit the threshold counts as lost is lost. Listed apart are the units with *a* ≥ 2 and *w* ≤ 1 that are not lost and whose span at least one WD run does not cover (*w* + *m* ≤ 2). Under the drafted threshold these are the units with *w* ≤ 1 and *m* ≤ 1; under *m* ≥ 1, those with *w* ≤ 1 and *m* = 0; under *w* = 0, the units that no WD run covers and those with *w* = 1 and *m* ≤ 1; under choice 5's exact mirror, only the units that no WD run covers. Alternative: count such a unit as lost.
7. **Scope.** Drafted: owner claims on noise topics and negative or hedged owner claims count, and the condition holds when no unit has *a* ≥ 2. Alternative: none drafted; a topic filter would need a judgement.

---

## Decisions for the author

- **PN-1. Scope of (b2).**
  - Options: (a) the role examples only, as drafted; (b) also neutralise the product wording of §1.2 ("a decided feature", "a list of decided features or owners", "Extract a feature … features tentatively").
  - Recommendation: (a). The amendment names "the AMI role examples" (`:244`) and the register's "example roles" (`:107`). Disclose that the product wording is tested by no probe, so a *not recovered* (b2) rules out the role examples only.
- **PN-2. The neutral text.**
  - Options: (a) domain-general support roles, as drafted; (b) one concrete third domain (for example construction: 'Site Engineer', 'Structural Engineer', 'Site Supervisor'). For the verbs, keep 'prepare' and 'define' (drafted), or change them too.
  - Recommendation: (a), and keep the verbs. A concrete third domain would add a new out-of-domain bias. The verbs are phrasing, not domain.
  - Second item: office and logistics functions. Two drafted titles name such functions ('Facilities Coordinator', 'Vehicle Fleet Specialist'). EL2020 has logistics noise content and run keys on it, one of them an owner key, and the static part says "ignore social, logistics, and unrelated content." (§1.3, "Topical proximity").
    - Options: (i) keep the drafted titles, and disclose this in the (b2) report; (ii) replace these two titles by titles with no office or logistics function, which needs a new overlap check (§1.3) and new hashes (§1.4) before signing.
    - Recommendation: (i). The lexical check is clean, no EL2020 gold value is about this topic, and the instruction to ignore logistics is the same in every condition.
- **PN-3. (b2) on the 3b run (ES2009).**
  - Options: (a) run it as the amendment requires, and disclose that there the role examples are in-domain and equal four ES2009a gold values; (b) leave (b2) out on 3b.
  - Recommendation: (a). Leaving it out would change the amendment's conditions.
  - Second item: the label of a (b2)-only recovery on 3b. The mapping gives a (b2) recovery the sub-cause "out-of-domain examples" (`:272`). 3b is coded under the frozen codebook "with no revision" (`:305`). On ES2009 the role examples are in-domain (§1.4).
    - Options: (i) code the class by the mapping, and count the case among "the share of cases that fit no frozen sub-cause" (`:305`), with disclosure; (ii) apply `:272` as written, disclose in the 3b report that the label there names the AMI role examples, which are in-domain on ES2009, and list such cases apart.
    - Recommendation: (ii). The mapping and its sub-causes are fixed (`:271`, `:554`), and 3b allows no revision. Option (i) would override the sub-cause that the mapping assigns.
- **PN-4. Control model id (P4).**
  - Options: (a) "gpt-5.4-mini" as recorded, with the served-model check; (b) the dated "gpt-5.4-mini-2026-03-17".
  - Recommendation: (a). It is the recorded request, and the check catches a snapshot change. The dated id has never been requested in this repository's records.
- **PN-5. No embedding candidate, and the other branches of `_prompt_registry` (P5).**
  - The amendment defines (b) as "the recorded prompt with the registry cut to the resolver's embedding candidates for the span text, at the evaluated parameters (`embedding_top_k`=8, `embedding_min_similarity`=0.30), without the lexical part of `_prompt_registry`." (`:243`). With no embedding candidate, two readings are possible:
    - the leading words ("cut to the resolver's embedding candidates") give an empty cut, so (b) equals (c);
    - the closing words ("without the lexical part of `_prompt_registry`") leave the rest of `_prompt_registry` in force, including its no-candidate branch (`3320375:app/services/state_key_resolution_service.py:689-690`), which keeps the whole registry, so (b) equals (a).
  - The choice changes codes. Take a case where an empty registry recovers the value and the recorded registry does not. If (b) equals (a), (b) adds nothing beyond the control, and without a (b2) recovery the case falls under `:278` (caused at extraction, class unclear). If (b) equals (c), (b) most likely recovers too, and the case then falls under `:272` (implementation choice at extraction).
  - Options: (a) keep the whole registry, as `_prompt_registry` does, so (b) equals (a); (b) an empty registry, so (b) equals (c).
  - Recommendation: (a). The amendment removes only the lexical part, so the code's own no-candidate branch applies. A (c)-only recovery then stays *unclear* (`:278`). List such cases.
  - Second item: the ≤12 branch (`:691-692`). It follows the reading chosen above. It changes nothing on EL2020 (P5).
  - Third item: the intent-primary keep (`:703`), which is in the removed range but is not lexical.
    - Options: (i) drop it with the lexical clause, as drafted in P5; (ii) keep it, at the fixed intent `CURRENT_STATE_QUESTION` of the claim path (`:370-372`).
    - Recommendation: (i). The keys it keeps are not embedding candidates. On EL2020 it keeps no key (P5).
- **PN-6. Key profiles for the cut (P5).**
  - Options: (a) aliases from the recorded line, other fields from `state.json`; (b) the final `state.json` definitions throughout.
  - Recommendation: (a). It is the definition at the moment of the call, as far as the trace records it.
- **PN-7. The recorded call per case (P1).**
  - Options: (a) the last call on each cited span by k, and the union over cited spans; (b) the first call; (c) every call by k as a separate input.
  - Recommendation: (a).
  - Second item: a span that two or more cases of the same run cite at the same recorded call.
    - Options: (i) re-extract it once per condition and repeat, and let that output serve each of those cases (P1); (ii) re-extract it once per case.
    - Recommendation: (i). The input is the same. It lowers the (d) maximum from about $16 to about $14 (P8).
- **PN-8. `admitted:span_not_seen` cases (P2).**
  - Options: (a) list them apart, no probe; (b) probe a neighbouring span.
  - Recommendation: (a).
- **PN-9. Pass criterion (P3).**
  - Options: (a) every extraction step up to the case's step, with strong matches or adjudication; (b) the case's step alone; (c) the strict bound only.
  - Recommendation: (a).
- **PN-10. The reading of "do not recover" in `:246`: (d) gating (P8).**
  - Options: (a) read it as the result *not recovered* for both (b) and (b2) (k0 ≤ 1 implied by the row order, `:262`), with an output for (a); (b) read it as any result other than *recovered*, inconclusive and not reproduced included.
  - Recommendation: (a). Only the cases of option (a) can reach `:279` or `:280`. Option (b) adds calls that cannot change any mapping row.
  - Cost: (d) on every probed EL2020 case would cost about $16 (estimate from recorded prompt sizes, P8), or about $14 under PN-7's second item. Under option (a) it costs less, by an unknown share. The amendment's estimate for (d) is about $5–11 (`:581`). See PN-14.
- **PN-11. "A key holding the gold value" (P7).**
  - Options: (a) as proposed; (b) any registry key whose definition the adjudicators judge to fit the value.
  - Recommendation: (a). It is mechanical, and it is only a descriptor.
- **PN-12. Missing outputs (P10).**
  - Options: (a) re-issue up to three times, then *no output* (no probe evidence); (b) count a missing output as a failing repeat.
  - Recommendation: (a). Option (b) would let a transport failure produce *not recovered*, or lower k0.
- **PN-13. A (d) output after shedding (§2.4, rule 3).**
  - Options: (a) it counts, and is listed; (b) it is excluded.
  - Recommendation: (a). It is gpt-5.4 at the settings it accepts. The bug-7 record suggests that none will be shed.
- **PN-14. The size of the (d) list, and blindness (P9, P13).** The (d) list stays sealed until Step 3 item 7 (`:411`). Its cost may exceed the amendment's estimate for (d) (P8).
  - Options: (a) the Step 2b go-ahead covers (d) at its maximum (about $16, or about $14 under PN-7's second item), so no count of the list is shown before item 7. At $16 this raises Step 2b's estimate of about $24–37 (`:581`) by about $5–11. (b) the probe script stops at a fixed spend ceiling, and a stop is logged as an early read under `:411`.
  - Recommendation: (a). It keeps the list blind. If the study budget guard is used, its cap covers this maximum (P13).

---

## Review record (27 October 2026)

**Workflow.** Review workflow am1-step0-verify. A reviewer raised findings F1–F10 on this note. A skeptic tried to refute each and failed. The fixer applied them on 27 October 2026, offline: no LLM, embedding or other API call; `.env` not opened; git state not changed. Code was read with `git show` at f8770f1, 3f297c4, 94c049d and 3320375. The counts were recomputed from `23-loss-trace.json`, the recorded traces, the nine runs' `state.json`, the bug-7 judgments and the 22 October ledger.

| Finding | Severity | Outcome |
|---|---|---|
| F1. The dating of the role examples | minor | Applied (§1.1). The phrasing examples and 'Industrial Designer' date from f8770f1, the four-title list from 3f297c4. The `ast` count is cited as the reliable evidence. The conclusion is unchanged. |
| F2. The (d) cost claim, and blindness of the (d) list | minor | Applied. The cost sentence of PN-10 is replaced by the bound and its basis (P8). A shared-span rule is added to P1 and PN-7. P9 and P13 are tied to the (d) maximum. The size rule is a new decision, PN-14. |
| F3. Office and logistics functions among the neutral roles | minor | Applied. A "Topical proximity" paragraph is added to §1.3, and a second item to PN-2. The choice is left to the author. |
| F4. The two readings of (b) with no candidate | minor | Applied. PN-5 quotes `:243` in full and gives both readings and their codes (`:272` against `:278`). P5 states the ≤12 branch and the intent-primary keep (`:703`). The keep is a third item in PN-5, because its drop is a reading, not a fact. The reason "span text has no query intent" in the skeptic's fix is not used: the claim path passes a fixed intent (`state_key_resolution_service.py:370-372`). The fact used instead is that every key in the nine runs has empty `supported_intents`. |
| F5. "Valid output", and a control with no output | minor | Applied (P10, P8). The seam guard defines a valid output for every condition. A control with no output gives no probe evidence and no (d). |
| F6. The label of a (b2)-only recovery on 3b | minor | Applied as a second item in PN-3. The recommendation follows the skeptic's better fix (apply `:272` as written, with disclosure), not the finding's option. |
| F7. The served model in P4; "Step 4 or 2c" in §1.4 | nit | Applied. |
| F8. The reason for the implementation entry; the overlap list | nit | Applied (§1.1, §1.3). `lifecycle_probes.yaml` and the recorded user and registry texts are added to the list; near-forms of 'Coordinator' are noted. The finding's list of runs with 'coordinat-' forms in key definitions omits a0_r2. The note gives the six runs found on recount. |
| F9. Client settings, SDK retries and reasoning tokens | nit | Applied (§2.1, §2.2, §2.3). |
| F10. The (d) gating as a reading of `:246` | nit | Applied (§3.1, P8, PN-10). "k0 ≤ 1" is kept, marked as implied by the row order (`:262`). |

**Cross-package consistency pass (27 October 2026).** One wording edit in §1.1: `23-am1-prompts-evaluated.md` is called the design-and-controls register's companion file, as that register names it, not a register file.

**Completion pass (27 October 2026).** Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. Code was read with `git show` at 3320375. Scratch scripts, not committed: `rename.py`, `hashcheck.py` and `owner_rule_selftest.py`. The self-test runs the owner test on the constructed example only and reads no run file.

What changed:
1. **New section** "Owner or role claim on EL2020 (C41, M-17)", after Part 3, and one sentence under "What it fixes" that points to it. It defines the WD rule's condition "no owner or role claim is lost;" (amendment `:293`) on the claims the Step 2c runs record: which claims count (a), what "lost" means (b), and when the condition fails (c). It has a constructed worked example, its limits, and seven choices for the author under C41. No owner or role claim was counted in any run, and no result is reported.
2. **Rename (X3).** The amendment says '"D1"–"D11" mean only the design decisions of Ch. 4' (`:6`). So this note's own decisions are renamed from D1–D14 to PN-1 to PN-14.
   - All 44 matches of `\bD[0-9]+\b`, on 38 lines, were checked in context. Every one named a decision of this note. None named a Ch. 4 decision or a paragraph id such as D4.p3, so none was kept.
   - The renames cover §1.2, §1.3, §1.4 (the paragraph on ES2009), Part 3, the decision list and the review record above. Sub-items follow the new ids, for example "PN-7's second item" and "[PN-5, PN-6]".
   - Proposals P1–P13 keep their names, P6 and P11–P13 included.
   - The new section uses no D-number.
3. **§1.4 is unchanged** apart from that one prose paragraph. Its Python code and its printed (b2) static part did not change. The hashes were re-derived from the note's own printed text and code, and none changed:
   - (b2) static part: 2,385 characters, `a3b0de5b259faaf1fa76352531ce7263c73803a42ebd1e70ab2fc2bf1acc02cf`;
   - recorded static part, rebuilt by the reverse substitution: 2,385 characters, `780d420c96f39522e48d2b824e6e7e5158d9156ebac357889c933fae6105bd0c`;
   - with `SEP` + `⟦registry⟧`: `725f1c00a2d188376cc361f2a939d1e564b1d6ba810a277d276962e95843663f` (recorded) and `c6961c4451327bd81f9f86858925ef0311f32cc4ed9ac0815cacb0b5cf0f4e27` ((b2));
   - `to_b2` run on the rebuilt recorded part returns the printed (b2) part.
4. **Not edited here.** The decision sheet `23-am1-decisions.md` still uses the old ids: "probe note (D1–D14, and its proposals P6 and P11–P13)" (`23-am1-decisions.md:10`), and the sources of C21–C25 (`:189`, `:195`, `:201`, `:207`, `:213`), B9–B13 (`:488`, `:492`, `:496`, `:500`, `:504`) and A9–A12 (`:599`, `:603`, `:607`, `:611`). It also lists this note's earlier SHA-256, `06b97f5586f01e1a41a11755802e5508672d1297cdee0f745f770e68d4574cdf`, which no longer holds.

Rename table:

| Old id | New id | Decision |
|---|---|---|
| D1 | PN-1 | Scope of (b2) |
| D2 | PN-2 | The neutral text |
| D3 | PN-3 | (b2) on the 3b run (ES2009) |
| D4 | PN-4 | Control model id (P4) |
| D5 | PN-5 | No embedding candidate, and the other branches of `_prompt_registry` (P5) |
| D6 | PN-6 | Key profiles for the cut (P5) |
| D7 | PN-7 | The recorded call per case (P1) |
| D8 | PN-8 | `admitted:span_not_seen` cases (P2) |
| D9 | PN-9 | Pass criterion (P3) |
| D10 | PN-10 | The reading of "do not recover" in `:246`: (d) gating (P8) |
| D11 | PN-11 | "A key holding the gold value" (P7) |
| D12 | PN-12 | Missing outputs (P10) |
| D13 | PN-13 | A (d) output after shedding (§2.4, rule 3) |
| D14 | PN-14 | The size of the (d) list, and blindness (P9, P13) |

**Review of the completion pass (27 October 2026).** Findings MX-F1 to MX-F11 of the workflow review of the Step 0 package. Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. This file has MX-F1, MX-F2, MX-F4, MX-F5, MX-F10 and MX-F11. MX-F3, MX-F7 and MX-F8 concern the pre-coder template and are recorded there.
- **MX-F1** (a redacted span stopped the computation). Applied, as the better fix, with one clause changed. The "Span" bullet now places a call by an exact match first, then by a match after the run's recorded gatekeeper redactions for the span are applied (`3320375:app/services/evidence_service.py:78-85`), and stops only if neither matches, or if more than one span matches. It says how `23-loss-trace.py` differs: it leaves an unmatched call unplaced. The better fix said that a gatekeeper rules fallback, whose redactions are not recorded, would reach the stop. At 3320375 a failed gatekeeper call raises and does not fall back to rules (`3320375:app/llm/guarded.py:14-15`). So the bullet says instead that a span whose gatekeeper step has no record with `mode` "llm" reaches the stop. Offline check: in the nine frozen EL2020 runs every extraction call equals a span text exactly, except one call of a2_r2b (1 of 129). That call equals its span's text after the span's two recorded redactions are applied (policy extract_as_candidate). The check read user messages and gatekeeper outputs only. No claim was counted or quoted.
- **MX-F2** (M-17 cited at the wrong register line). Applied. The pointer is now `23-am1-register-claims.md:4451`, with its place: the register's section 9, mapping section 8 ("Gaps and decisions for you"). The better fix's "section 10" is not used: section 10 is the register's review record. The line must be checked again at signing.
  - Later the same day (main session): the line pointer was replaced by a cite of the heading ("What it fixes" in the owner-claim section), so later edits of the register do not move it. The `:4451` cites in this record and in the checks below are history.
- **MX-F4** ("the mirror of (iv)"). Applied, as the better fix. The "Lost" bullet and choice 5 now call the draft "(iv) mirrored, with WD runs that do not cover the span left out". The "Lost" bullet states the exact mirror. Choice 5 adds it as a third alternative: *a* ≥ 2 and *w* ≤ 1, with units no WD run covers listed apart (`:352`, `:356`). Choice 6 says what is listed apart under it. The drafted threshold is unchanged; the choice stays with the author (C41).
- **MX-F5** (the "only other WD material" sentence). Applied: the sentence is deleted, the better fix's first option.
- **MX-F10** (the span table's lines). Applied: `:409-414`.
- **MX-F11** ("lead" in the expansion generator's words). Applied, as proposed.
- **Checks** (working files in the session scratchpad, folder `step0/complete/`, not part of the package):
  - Every line reference added or changed here was checked against its source: `23-loss-trace.py:284` (`render_spans`), `:409-414`, `:416-419` and `:436-439`; at 3320375, `evidence_service.py:46` and `:78-85`, `extraction_service.py:398`, `guarded.py:14-15` and `:124-130`, and `expansion_generator.py:116`; `23-am1-register-claims.md:4431` and `:4451`. The quotes of amendment lines 352 and 356 are verbatim.
  - §1.4 is unchanged. `hashcheck.py` re-derives its hashes from the note's printed text and code, and all match as recorded above.
  - `owner_rule_selftest.py` runs on the constructed example as before. It reads no run file.
  - Line 311 still holds P2's sentence "They have no recorded extraction call on a cited span", which the pre-coder template quotes (its Section 7, point 22). All edits of this review are below that line.

**Second review (27 October 2026).** Second review round of the Step 0 package; findings R2-OWN-1 to R2-OWN-3 concern this file. Only defects were applied. Made offline: no LLM, embedding or other API call; `.env` not opened; the `app` package not imported; git state not changed. No run file was read in this round, and no owner or role claim was counted.
- **R2-OWN-1** (test (K) did not say whether the hint segment is lower-cased). Applied, merged with R2-OWN-2 into one edit of (K), as the better fix: "Take the text after its last "." (the whole hint if it has no "."), lower-case it, and split it at "_" and "-"." This is what `owner_rule_selftest.py` already computed (`h.rsplit(".", 1)[-1].lower()`), so the self-test needs no change. The decision sheet's gloss of (K), "an OWN word in its last segment" (C41), needs none either.
- **R2-OWN-2** (a hint with no "." had no text after its last "."). Applied in the same edit: the whole hint is taken.
- **R2-OWN-3** (under choice 5's alternatives *m* ≥ 1 and *w* = 0, a unit could be both lost and listed apart). Applied, as the better fix. "Not covered by WD" and choice 6 now state one rule for every threshold of choice 5: a unit whose span no WD run covers is not lost; otherwise a unit the threshold counts as lost is lost; listed apart, never deciding, are the units with *a* ≥ 2 and *w* ≤ 1 that are not lost and whose span at least one WD run does not cover (*w* + *m* ≤ 2). Choice 6 gives the set listed apart under each threshold. Choice 6's alternative is unchanged. The drafted threshold and the drafted set (*a* ≥ 2, *w* ≤ 1, *m* ≤ 1) are unchanged. In the same place, the last sentence of the "Lost" bullet now names that set; before, it said "every unit with *m* ≤ 1", which also takes in units with *w* ≥ 2 that "Not covered by WD" never listed apart. Not applied here: the decision sheet's C41, choice 6 (`23-am1-decisions.md:346`), still gives only the drafted set. This file may not edit the sheet, so it is left for the author.
- **Checks** (working files in the session scratchpad, folder `step0/reverify/`, not part of the package):
  - `choice56_rule.py` enumerates every (*a*, *w*, *m*) with *a* ≥ 2 and *w* + *m* ≤ 3 under the four thresholds of choice 5. Under each, no unit is both lost and listed apart, and the set listed apart equals the set choice 6 states. Without the clause *w* + *m* ≤ 2, the threshold *w* = 0 would also list apart (2, 1, 2) and (3, 1, 2), units that all three WD runs cover. The same script runs (K) on synthetic hints: 'project.guidelines.Owner', 'OWNER', 'guidelines_owner' and 'owner' pass; 'project.a.deadline' and a null hint do not. It reads no run file.
  - `owner_rule_selftest.py` runs on the constructed example as before: *a* = 3, *w* = 1 and *m* = 1 (listed apart), or *m* = 2 (lost).
  - §1.4 is unchanged: `hashcheck.py` re-derives its hashes from the note's printed text and code, all as recorded under the completion pass, and the section's text hash is the same before and after this round.
  - Line 311 still holds P2's sentence, which the pre-coder template quotes (its Section 7, point 22, and its Section 3, row C2). All edits of this round are below that line.
