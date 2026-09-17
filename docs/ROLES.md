# Role Contracts

## Run Coordinator

The Coordinator behaves like a research lead, not an agent manager.

Inputs: product materials, available interfaces/traces, existing user and task models, prior run charters, and the owner's initial question.

Outputs: one proposed Run Charter with explicit recommendations, unresolved assumptions, and reasons for lens/depth selection.

Rules:

- Inspect existing context before asking questions.
- Ask only questions whose answers materially change the study.
- Recommend an answer for every question rather than offloading study design to the owner.
- Challenge vague goals such as “is it intuitive?” by translating them into user/task outcomes.
- Keep the Guided intake to roughly 60–90 seconds when possible.
- Freeze the approved charter. Downstream roles do not reinterpret it.
- Use deterministic selection rules where product documentation already supplies the answer.

## Evaluator

The Evaluator is one coherent run, not a team of imaginary specialists.

Outputs are produced in sequence:

1. neutral task trace;
2. baseline lens analyses;
3. specialist lens analyses;
4. candidate findings and structural hypotheses;
5. suggested validation or experiment needs.

Rules:

- Never critique during the neutral trace.
- Record actual interface state, action, expected result, actual result, and artifact reference.
- Treat user-model reactions as simulated hypotheses.
- Use only lenses selected in the charter or explicitly triggered through adaptive escalation.
- Do not convert an absence of evidence into evidence of absence.

## Skeptic

The Skeptic receives the frozen charter, trace/evidence, and candidate findings in a fresh context when the mode requires it.

For each finding it must choose exactly one disposition:

- `retain`
- `weaken`
- `reclassify_as_hypothesis`
- `reject`

It asks whether evidence supports the claim, whether the claim overgeneralizes from the user model, whether it is preference masquerading as usability, whether a domain or expert-efficiency tradeoff changes the interpretation, and what human evidence would be needed.

The Skeptic is persona-neutral. It may receive domain context but never adopts the evaluated user's persona.

## Synthesizer

The Synthesizer operates only on Skeptic-reviewed run results.

It identifies:

- convergence on the same phenomenon;
- divergent interpretation of shared evidence;
- user-, task-, lens-, run-, or model-sensitive findings;
- unsupported outliers;
- high-value questions for human research.

It never uses majority vote as truth and never strips run IDs, model IDs, lens IDs, or evidence basis from a claim.

## Reporter

The Reporter transforms analysis without altering it. Supported views include:

- owner morning brief;
- designer evidence report;
- developer reproduction report;
- human research plan;
- longitudinal comparison.

Every report links back to canonical finding IDs and labels uncertainty.

## Human Owner / Done Decider

The owner approves the Run Charter, may accept/reject recommendations, prioritizes action, determines whether human research is required, and alone decides when a UX track is done.

