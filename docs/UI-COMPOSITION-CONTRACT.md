# UI Composition Contract

Pyrax V0.5 treats recurring UI patterns as composable presentation contracts, not as sources of business truth.

## Canonical components

- `control-tower` — exception-first overview for operational attention.
- `andon` — severity-oriented visual management.
- `heatmap` — concentration of pressure, loss, risk or activity.
- `timeline` — chronological state/event context.
- `object-360` — entity-centered operational context.
- `evidence-drawer` — source, lineage, rule version, quality and confidence inspection.
- `scenario-panel` — hypothetical comparisons isolated from canonical state.
- `decision-card` — signal, recommendation, constraints, confidence and approval state.

## Required boundaries

1. UI components consume domain/runtime outputs; they do not invent business semantics.
2. A displayed zero must be a real zero, not UNKNOWN/UNAVAILABLE/NULL coercion.
3. Decision-support views must expose Evidence and confidence at a useful level of granularity.
4. Scenario views must be visibly distinguishable from observed/canonical state.
5. Consequential actions must reflect the product's approval policy and default to human approval.
6. Vocabulary, units, severity labels and workflow actions are Domain Pack concerns.

## Composition guidance

A product may combine components according to the decision context. For example:

- Fleet intelligence: control tower + Object360 + timeline + scenario panel + evidence drawer.
- Industrial performance: control tower + Andon + heatmap + timeline + evidence drawer.
- Decision intelligence: decision cards + scenario panel + evidence drawer + timeline.

These are reusable layouts, not mandatory screens.
