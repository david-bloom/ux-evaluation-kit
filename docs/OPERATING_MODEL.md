# Operating Model

**Status:** Proposed  
**Owner / Done Decider:** David Bloom

## Design principles

1. **Usability is contextual.** The unit of evaluation is product × task × user model × context × lens.
2. **Method, condition, and observer stay separate.** Lenses define how to inspect; user models define for whom; models/runs provide independent observations.
3. **One run is coherent.** A capable model executes the complete sequenced protocol against one frozen Run Charter.
4. **Observation precedes interpretation.** Record states, actions, and outcomes before applying critique lenses.
5. **Claims carry provenance.** Observed, analytical, simulated, and human-validated evidence are labeled distinctly.
6. **Criticism is local; synthesis is cross-run.** Every run gets a Skeptic. A Synthesizer exists only when multiple reviewed runs exist.
7. **Disagreement is information.** Synthesis preserves variance instead of resolving it by majority vote.
8. **Depth is adaptive.** Start broad and escalate high-impact or uncertain claims to specialist lenses, repeated runs, different models, or human research.
9. **Outputs are advisory.** The kit proposes findings and investigations. The human owner decides what matters and when work is done.

## Evaluation equation

```text
EvaluationRun = ProductContext
              × TaskModel
              × UserModel
              × SelectedLenses
              × EvaluatorModel
              × Repetition
```

Changing any dimension creates a meaningfully different run and must be recorded in the Run Charter or manifest.

## Roles are epistemic responsibilities

| Role | Responsibility | Does not do |
|---|---|---|
| Run Coordinator | Scopes the investigation and freezes the charter | Evaluate the interface or invent missing product facts |
| Evaluator | Executes the task and applies selected methods sequentially | Claim to be a real user or decide truth |
| Skeptic | Audits support for each finding | Receive a persona or generate unrelated new critique |
| Synthesizer | Compares reviewed independent runs | Vote, average, or erase provenance |
| Reporter | Renders a view for a particular audience | Change finding status or analytical conclusions |
| Human Owner | Sets scope, accepts risk, prioritizes, and decides Done | Delegate final judgment silently to an AI score |

See [ROLES.md](ROLES.md) for detailed contracts.

## Standard topology

```text
Run Coordinator
  -> Frozen Run Charter
  -> Evaluator (observation, then lenses)
  -> Fresh-context Skeptic
  -> Reviewed Run Result
  -> Reporter
```

When independent reviewed runs exist:

```text
Reviewed Run Results
  -> Synthesizer
  -> Convergence + disagreement + model/run-sensitive hypotheses
  -> Reporter views
```

## Model use

Do not permanently assign GPT to OOUX, Claude to behavioral UX, or Gemini to cognitive walkthrough. That confounds model variance with method variance. For replication, independent models receive the same frozen charter and lens procedure. For diagnostic escalation, selected models receive the same added specialist lens.

Repeated runs of the same model can expose stochastic uncertainty. Cross-model runs can expose observer/model sensitivity. Neither is human validation.

