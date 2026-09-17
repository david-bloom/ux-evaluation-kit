# Evidence Model

## Epistemic levels

| Basis | Meaning | Allowed phrasing |
|---|---|---|
| Observed | The evaluator interacted with the product or inspected a supplied trace and recorded the event | “The action produced…” |
| Analytical | A named UX method supports an interpretation | “The cognitive walkthrough indicates…” |
| Simulated | A configured user model might react in a particular way | “A first-time teacher may…” |
| Human-validated | Actual participants demonstrated or reported behavior in a documented study | “Four of six participants…” |

Analytical and simulated claims do not become observed through repetition across models. Convergence increases the priority of a hypothesis; it does not turn simulation into research.

## Finding anatomy

Every canonical finding must contain:

- stable finding ID and run ID;
- concise claim;
- affected task and user model IDs;
- lens IDs;
- evidence basis;
- artifact/state/action/result references;
- impact types: block, error, backtracking, decision burden, delay, loss of confidence, accessibility barrier, or minor;
- confidence: high, medium, low, or speculative;
- alternative interpretations;
- validation need;
- Skeptic disposition and rationale.

## Confidence guidance

- **High:** direct, reproducible evidence tightly supports the bounded claim.
- **Medium:** evidence supports the phenomenon but impact or population inference remains uncertain.
- **Low:** plausible but weakly supported or dependent on assumptions.
- **Speculative:** useful hypothesis without sufficient evidence.

Confidence is not probability and must not be averaged.

## Severity is contextual

Impact depends on frequency, criticality, affected users, recoverability, and consequences of failure. Record those inputs rather than emitting a universal 1–10 score.

## Calibration with human evidence

Link later studies back to AI hypothesis IDs and record `supported`, `partially_supported`, `not_supported`, or `inconclusive`. Never rewrite the original hypothesis as if it had been human-validated at creation time.

