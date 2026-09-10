# Building Block Catalog

Building Blocks are reusable, domain-neutral mechanics that can be selected by Solution Profiles and bound to a target Domain Pack.

## V0.5 blocks

| Block | Purpose | UNKNOWN policy |
|---|---|---|
| `aging` | elapsed-time pressure and SLA risk | abstain when required timestamps are unavailable |
| `coverage` | compare known requirement vs known eligible capacity/supply | preserve unknowns |
| `deficit-propagation` | propagate a known shortage to affected entities/decisions | preserve unknowns |
| `dead-reckoning` | project state from last observed state and explicit assumptions | abstain without required baseline |
| `constraint-propagation` | trace how constraints affect candidate actions | preserve unknowns |
| `baseline-deviation` | compare observed value against a governed baseline | abstain without valid baseline |
| `rate-of-change` | detect meaningful directional change | abstain without sufficient observations |
| `bottleneck-detection` | identify constrained flow/capacity points | preserve unknowns |
| `capacity-risk` | turn capacity pressure into bounded decision support | abstain without sufficient evidence |
| `outcome-feedback` | retain decision/action/outcome feedback for Operational Memory | preserve unknowns |

## Binding contract

A block becomes usable in a product only after the product defines:
- exact domain inputs;
- grain/population;
- semantic meaning;
- Evidence requirements;
- thresholds/parameters;
- confidence policy;
- UNKNOWN behavior;
- prohibited interpretations;
- Golden Cases.

A Building Block is reusable mechanics, not reusable business truth.
