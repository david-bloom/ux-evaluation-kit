# Run Lifecycle

## 1. Session start

Trigger: `SESSION START` or `SESSION START: <run-id>`.

The working agent reads the repository guidance listed in `AGENTS.md`, checks the latest Session Close entry, and reports current state, pending decisions, risks, and next action. A session is a work boundary; it is not an evaluation run.

## 2. UX run start

Trigger: `UX RUN START`.

Select an intake mode:

- **Quick:** infer reasonable defaults, show one proposed charter, request approval/corrections.
- **Guided:** ask the adaptive scoping questions with recommendations.
- **Custom:** expose all user, task, priority, lens, depth, model, repetition, and evidence choices.

### Guided intake questions

Ask only unresolved questions:

1. What product surface or workflow is in scope, and where does it start/end?
2. Which user model is primary, and are conflicting secondary users important?
3. What specific outcome must the user accomplish?
4. What starting state, information, constraints, environment, and consequences matter?
5. Which usability qualities are primary versus secondary?
6. Which baseline and specialist lenses fit, and why?
7. What run depth and replication policy fit the decision risk?
8. What evidence sources are available, and what must remain explicitly unobserved?
9. What is excluded?

Every question includes a recommendation and a short reason. Approval creates `run-charter.json`; evaluation cannot begin before it is frozen.

## 3. Preflight

The Coordinator verifies:

- the charter validates against `schemas/run-charter.schema.json`;
- the interface/build/reference version is identifiable;
- access and starting state are available;
- sensitive or destructive actions are excluded or explicitly authorized;
- artifact paths exist;
- selected lenses exist and their required context is present;
- the run is labeled as static review, interactive execution, trace review, or mixed.

If observed interaction is unavailable, downgrade claims accordingly; never simulate having executed the product.

## 4. Execute without critique

Attempt the task from the defined starting state. Capture step number, state, action, expectation, result, artifact reference, and whether completion criteria were reached. Log detours, backtracking, waiting, ambiguity, errors, recovery, and dead ends without explaining why they are bad.

## 5. Apply lenses sequentially

Run baseline lenses, then selected specialist lenses. Each lens follows its registry procedure and allowed-claim boundary. Specialist lenses may produce structural hypotheses in addition to surface findings.

## 6. Form candidate findings

Every finding includes affected user/task, observation or state reference, impact type, evidence basis, confidence band, lens, competing interpretations, and suggested validation. Do not create composite numeric usability scores.

## 7. Skeptic pass

Quick mode may use a clearly separated inline pass. Standard and Deep use a fresh context. The Skeptic records a disposition and rationale for every candidate finding. Rejected findings remain in the audit trail but are excluded from reports by default.

## 8. Adaptive escalation

Escalate only when useful:

- medium/high-impact structural ambiguity → relevant specialist lens;
- high-impact low/medium-confidence claim → independent repeated or cross-model run;
- persona-dependent claim → contrasting user model;
- behavioral claim without behavioral evidence → human study proposal;
- apparent accessibility barrier → accessibility specialist/manual assistive-technology testing;
- conflicting interpretations → preserve both and define a discriminating experiment.

## 9. Synthesis, if applicable

Synthesize only reviewed runs with compatible or explicitly contrasted charters. Classify claims as convergent, divergent interpretation, condition-sensitive, model/run-sensitive, or unresolved. Do not average confidence or severity.

## 10. UX run close

Trigger: `UX RUN CLOSE: <run-id>`.

Before closing:

- validate required artifacts and schemas;
- confirm the charter was not silently changed;
- confirm every reported claim has provenance;
- list rejected and unresolved findings;
- record selected/non-selected lenses and reasons;
- record completion status: `completed`, `completed_with_limitations`, or `blocked`;
- state recommended next action and human decisions needed;
- append the run to `runs/INDEX.md`.

Closing a run does not approve product changes or mark UX Done.

## 11. Session close

Trigger: `SESSION CLOSE` or `SESSION CLOSE: <run-id>`.

Validate, commit/push when authorized, and append an entry to `docs/SESSION_LOG.md` with summary, changed artifacts, pending decisions, risks, and next action.

