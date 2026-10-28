export const meta = {
  name: 'loss-trace-adjudicate',
  description: 'Fixpoint round of loss-trace adjudication: two independent adjudicators plus a tie-break on an items file',
  phases: [
    { title: 'Adjudicate', detail: 'two independent adjudicators' },
    { title: 'Tie-break', detail: 'third adjudicator on disagreements' },
  ],
}
const CTX = `Repository root: /Users/wesselvansommeren/Documents/Project-Context-Protocol. Suite (gold block, transcripts, questions): data/ami_eval/suites/transfer_el2020.yaml. Run dirs (EL2020) are named in the contexts; full paths: ${JSON.stringify(args.runs)}. Offline only; do not edit repository files; do not read other adjudicators' outputs.`
const STANDARD = `ADJUDICATION STANDARD. For each item, decide whether the TEXT carries the GOLD VALUE of its fact_id. "Carries" means: a careful coder would say the text states that gold value, so that an answer built from this text would be judged correct for a question asking for that value. Specifically:
- A paraphrase, a more specific or a more complete statement of the same value carries it.
- For a value made of two or more independent parts, a text stating only one part does NOT carry it, even if that part is listed as a gold alias. A text that states the main decision and leaves out a minor qualifier DOES carry it.
- A text about the same topic that states a different value, a rival option, another gold value (a sibling fact), or only the topic words, does NOT carry it.
- For ruled-out values (kind ruled_out): the text carries it if it names the ruled-out option (its polarity is judged elsewhere).
- For demoted values: as for current values (the text names that same earlier value).
- Use the contexts (claim subject | predicate | object, the key it was filed under or the key of a fact/proposal) to understand what the text means; a fact's or proposal's text is read with its key. If the same text means different things in different contexts, decide by its most common context and say so.`
const SCHEMA = { type: 'object', properties: { decisions: { type: 'array', items: { type: 'object', properties: {
  fact_id: { type: 'string' }, text: { type: 'string' }, carries: { type: 'boolean' }, reason: { type: 'string' } },
  required: ['fact_id', 'text', 'carries', 'reason'] } } }, required: ['decisions'] }
const p = who => `${CTX}

TASK (adjudicator ${who}, independent): ${STANDARD}

Items: every entry of ${args.items} (gold value, aliases, kind, evidence lines, questions, contexts). Read the suite or run files for more context if needed. Return a decision for every item with the exact fact_id and text strings.`
phase('Adjudicate')
const [a, b] = await parallel([() => agent(p('A'), { label: 'adj:A', phase: 'Adjudicate', schema: SCHEMA }), () => agent(p('B'), { label: 'adj:B', phase: 'Adjudicate', schema: SCHEMA })])
const A = new Map(((a && a.decisions) || []).map(d => [d.fact_id + '\u0000' + d.text, d]))
const B = new Map(((b && b.decisions) || []).map(d => [d.fact_id + '\u0000' + d.text, d]))
const dis = []
for (const k of new Set([...A.keys(), ...B.keys()])) {
  const x = A.get(k), y = B.get(k)
  if (!x || !y || x.carries !== y.carries) dis.push({ fact_id: (x || y).fact_id, text: (x || y).text, A: x || null, B: y || null })
}
let tie = []
if (dis.length) {
  phase('Tie-break')
  const t = await agent(`${CTX}

TASK (tie-break adjudicator): two independent adjudicators disagreed on these items. ${STANDARD}

Items with both decisions (more context in ${args.items}): ${JSON.stringify(dis)}

Return your decision for every item.`, { label: 'tie', phase: 'Tie-break', schema: SCHEMA })
  tie = (t && t.decisions) || []
}
return { a: [...A.values()], b: [...B.values()], disagree: dis.length, tie }
