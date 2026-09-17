# UX Evaluation Kit

A model-agnostic protocol for producing disciplined, evidence-bearing UX evaluations without pretending AI simulation is user research.

The kit evaluates a specific **user × task × context × interface** through explicit UX lenses. One capable model can execute a complete run. Repeated runs or different models are independent observations used for replication—not permanent role assignments.

## What this kit is

- A short, adaptive intake that produces a frozen Run Charter.
- A sequenced evaluation protocol that separates observation from interpretation.
- A registry of baseline and specialist UX lenses.
- A fresh-context Skeptic pass that retains, weakens, reclassifies, or rejects findings.
- Optional cross-run synthesis that preserves convergence, disagreement, and provenance.
- Multiple report views over the same evidence.

## What this kit is not

- An AI oracle that declares a product usable.
- A replacement for observing real users.
- A score generator that turns uncertain judgments into false precision.
- A society of role-playing agents that must be distributed across AI vendors.

## Start here

1. Read [Operating model](docs/OPERATING_MODEL.md) and [Run lifecycle](docs/RUN_LIFECYCLE.md).
2. Start a session with `SESSION START`.
3. Start an evaluation with `UX RUN START` and choose Quick, Guided, or Custom intake.
4. Save the approved charter as `runs/<run-id>/run-charter.json`.
5. Execute the relevant prompts in `prompts/` in protocol order.
6. Validate the artifacts with `python scripts/validate.py`.
7. Close the evaluation with `UX RUN CLOSE`, then the working session with `SESSION CLOSE`.

The complete invocation text is in [prompts/UNIVERSAL_SESSION_PROMPT.md](prompts/UNIVERSAL_SESSION_PROMPT.md).

## Normal and deep runs

| Mode | Shape | Use when |
|---|---|---|
| Quick | 1 evaluator, baseline lenses, inline skeptic | Early design checks and narrow questions |
| Standard | 1 evaluator, selected lenses, fresh-context skeptic | Default for meaningful workflow evaluation |
| Deep | Independent runs across models/repetitions, local skeptics, synthesis | High-impact redesigns or uncertain findings |

Deep is not automatically more correct. It produces more observations and makes disagreement visible.

## Repository map

```text
config/       run modes and lens registry
docs/         architecture, roles, evidence rules, lifecycle, start/end processes
prompts/      coordinator, evaluator, skeptic, synthesizer, and reporter protocols
schemas/      machine-readable contracts for run artifacts
examples/     one complete illustrative run
runs/         real run folders (index only until used)
scripts/      dependency-free repository validation
```

## Core rule

Every claim must say what supports it:

- **Observed** — encountered in an actual product interaction or trace.
- **Analytical** — derived through a named UX method.
- **Simulated** — a hypothesis about a configured user model.
- **Human-validated** — demonstrated by actual participants.

These categories never collapse into one score. David remains the Done Decider; all AI output is advisory.


