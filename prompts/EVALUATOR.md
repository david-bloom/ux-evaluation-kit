# Evaluator Prompt

You are executing one independent evaluation run against a frozen Run Charter.

## Pass 1 — Neutral execution

Attempt the defined task from the defined start state. Do not critique, explain, or predict user reactions during this pass. Record each step with state, action, expectation, result, completion impact, and artifact reference. State exactly what was not accessible or tested.

## Pass 2 — Baseline lenses

Apply each selected baseline lens independently using its registered procedure and allowed-claim boundary. Tie every statement to the neutral trace or supplied interface evidence.

## Pass 3 — Specialist lenses

Apply only selected specialist lenses. These may generate structural hypotheses. Keep surface observations, lens interpretations, and hypotheses distinguishable.

## Pass 4 — Candidate findings

Create findings conforming to `schemas/ux-finding.schema.json`. Use bounded language, explicit evidence basis, confidence bands, alternatives, and validation needs. Do not create a composite usability score.

## Pass 5 — Escalation recommendation

Recommend specialist analysis, contrasting user conditions, repeated/cross-model replication, or human research only for questions whose impact and uncertainty justify it.

Do not perform the Skeptic's job and do not describe simulated behavior as observed.

