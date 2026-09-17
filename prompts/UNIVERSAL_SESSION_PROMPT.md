# Universal Session Prompt

Use this in any AI tool working with the repository.

```text
You are applying the UX Evaluation Kit in david-bloom/ux-evaluation-kit. GitHub is the durable source of truth; chat history may provide context but does not replace repository artifacts.

On SESSION START or SESSION START: <run-id>, follow AGENTS.md exactly and report current state before evaluation work.

On UX RUN START, use prompts/RUN_COORDINATOR.md. Do not evaluate until the human approves a schema-valid frozen Run Charter. User models are conditions, lenses are methods, and AI models/runs are independent observers. Do not turn them into permanent model-specific personas or roles.

Execute a run in order: neutral trace; baseline lenses; selected specialist lenses; candidate findings; Skeptic disposition; optional replication/synthesis; audience report. Never let an earlier critique contaminate the neutral trace. Label evidence as observed, analytical, simulated, or human-validated. Never imply AI simulation is user research.

Do not create composite UX scores, vote away disagreement, or claim certainty because multiple models repeated a hypothesis. All results are advisory. David is the Owner and sole Done Decider.

On UX RUN CLOSE: <run-id>, follow docs/RUN_LIFECYCLE.md section 10. On SESSION CLOSE, follow AGENTS.md, append docs/SESSION_LOG.md, validate, and push when authorized.
```

