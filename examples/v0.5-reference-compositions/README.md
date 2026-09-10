# V0.5 Reference Compositions

These files prove that Pyrax can recreate representative product shapes from reusable profiles and composition contracts without copying prior product implementations.

Each reference has two artifacts:
- `*.solution.yaml` — reusable product composition (profile, blocks, adapters, UI and maturity target);
- `*.domain-pack.yaml` — minimal non-customer Domain Pack used to prove structural compatibility and scaffolding.

Included references:
- Route Engineer — fleet/route decision intelligence;
- Asset Radar — asset visibility and telemetry confidence;
- Predictive Maintenance — condition and intervention prioritization;
- OEE Intelligence — industrial/OEE performance intelligence;
- Decision Engine — generic evidence-backed decision support.

## What these references are

They demonstrate:

`Profile + Blocks + Adapters + UI Components + Domain Pack + Local Overrides`

They are intended for regression, learning and productization proof.

## What they are not

They are not customer deployments or production-certified Domain Packs. They intentionally omit credentials, proprietary source mappings, confidential business rules and customer-specific semantics.

The reference Domain Packs preserve candidate/UNKNOWN semantics where no real organization source exists. Passing `pyrax validate` proves contract integrity only; it does not imply production readiness.

A real deployment must still perform organization discovery, data mapping, semantic certification, Golden Cases, reconciliation, integration tests and readiness assessment.
