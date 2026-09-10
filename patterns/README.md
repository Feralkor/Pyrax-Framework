# Pyrax Pattern Library

Reusable problem-solving patterns extracted from operational intelligence products. Patterns are not domain rules; they are composable analytical/decision primitives.

## Catalog

- `aging` — elapsed time against an operational reference.
- `coverage` — available capability/resources divided by known demand.
- `deficit-propagation` — propagate shortage through dependent entities/workflows.
- `dead-reckoning` — deterministic projection from current state, velocity/rate and constraints.
- `constraint-propagation` — propagate limiting conditions through a dependency graph.
- `baseline-deviation` — compare observed state against a certified/accepted baseline.
- `rate-of-change` — identify acceleration, deterioration or recovery.
- `bottleneck-detection` — identify accumulation, wait, saturation or throughput restriction.
- `capacity-risk` — compare known/expected workload against available capacity.
- `outcome-feedback` — compare recommendation, action and realized result.

## Rule

Every pattern must declare inputs, outputs, assumptions, UNKNOWN behavior, evidence requirements and prohibited interpretations before production use.
