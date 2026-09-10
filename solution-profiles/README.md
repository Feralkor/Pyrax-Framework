# Solution Profiles

Solution Profiles are reusable product starting points. They package recurring Pyrax composition choices without packaging customer-specific truth.

A profile may select:
- Building Blocks;
- adapter classes;
- UI composition contracts;
- a suggested maturity target.

Current V0.5 profiles:
- `fleet-intelligence`
- `asset-radar`
- `predictive-maintenance`
- `industrial-performance`
- `decision-intelligence`

## Rules

1. Profiles are hypotheses, not certified Domain Packs.
2. Profiles must remain industry/problem-shape oriented and avoid customer names, credentials and proprietary semantics.
3. A profile may accelerate architecture and composition, but local source semantics, ontology, thresholds, rules, decisions and constraints must be validated again.
4. If a recurring configuration cannot be generalized without leaking customer-specific assumptions, it does not belong in a Solution Profile.
5. Profile evolution must preserve Pyrax guardrails: Evidence, explicit UNKNOWN, scenario isolation and human approval defaults.
