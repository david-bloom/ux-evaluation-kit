# Agent Instructions

This repository is a UX evaluation methodology. Do not reinterpret it as a multi-agent role-play system.

## On `SESSION START`

Read, in order:

1. `README.md`
2. `docs/OPERATING_MODEL.md`
3. `docs/RUN_LIFECYCLE.md`
4. `docs/EVIDENCE_MODEL.md`
5. `config/lenses.json`
6. `config/run-modes.json`
7. the latest entry in `docs/SESSION_LOG.md`

If a run ID is supplied, also read every existing artifact in `runs/<run-id>/` and report its current lifecycle state before acting.

## Boundaries

- User models are evaluation conditions, not personalities to improvise.
- Lenses are methods, not personas and not permanent AI assignments.
- AI models are independent evaluators/replication mechanisms.
- Observation must occur before critique when the product can be exercised.
- The Skeptic is persona-neutral and modifies findings; it does not add a second pile of critique.
- Preserve disagreement. Do not vote, average scores, or manufacture consensus.
- Never represent simulated behavior as observed human behavior.
- Never mark a product, workflow, or UX track Done. The human owner decides.
- Do not edit prior run artifacts to make a new run look consistent; create a new run or a versioned amendment.

## On `SESSION CLOSE`

Append a concise entry to `docs/SESSION_LOG.md` containing date, summary, artifacts changed, decisions pending, open risks, and next action. Validate before committing.

