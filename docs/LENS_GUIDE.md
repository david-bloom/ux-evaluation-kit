# Lens Guide

The canonical machine-readable definitions live in `config/lenses.json`.

## Baseline lenses

- **Cognitive walkthrough:** can this configured user identify the next action, perform it, and interpret feedback?
- **Interaction and state:** are controls, state transitions, feedback, persistence, and system status understandable?
- **Error and recovery:** can users prevent, recognize, escape, undo, retry, and recover from mistakes?
- **Core heuristics:** what established usability principles are implicated, stated as bounded analytical claims?
- **Accessibility baseline:** are obvious semantic, keyboard, contrast, target, labeling, and motion barriers present? This is not a conformance audit.

## Specialist lenses

- **OOUX:** do objects, relationships, attributes, and actions match the domain model users need?
- **Information architecture:** can users predict where things live, how they are grouped, and how labels map to content?
- **Behavioral UX:** do motivation, ability, prompts, timing, feedback, and ethical constraints support the intended behavior?
- **Expert efficiency:** does learned/repeated use remain fast without damaging novice comprehension?
- **Trust and comprehension:** does the system support appropriately calibrated confidence and understandable consequences?
- **Accessibility deep:** deeper inclusive-design and assistive-technology investigation requiring relevant expertise and evidence.
- **Service journey:** do cross-channel, handoff, backstage, and recovery dependencies create journey-level failure?
- **Jobs to Be Done:** does the workflow advance the user's progress in a situation, including functional, social, and emotional dimensions?

## Selection rules

Run baseline lenses unless the charter documents why one is irrelevant. Select specialist lenses based on the task and product structure, not personal preference. Record both selections and intentional exclusions.

Examples:

- manipulating Questions, Assessments, Classes, and Assignments → OOUX + IA;
- recurring practice or onboarding behavior → Behavioral UX;
- repeated high-volume professional work → Expert efficiency;
- identity, money, grades, health, or irreversible consequences → Trust and comprehension;
- journeys across email, mobile, support, and offline steps → Service journey.

