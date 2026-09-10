# Pyrax Framework 0.5.0 — Productization & Composition

Status: RELEASE CANDIDATE / ACTIVE VALIDATION

## North Star

> From reusable methodology to reusable product composition.

V0.5 proves that recurring operational-intelligence product shapes can be recreated from the same Pyrax origin without copying prior implementations or customer-specific semantics.

## Scope delivered

### Product composition
- Solution Profiles/presets;
- composable Building Block catalog;
- Solution Manifest contract;
- Domain Pack composition/overlay mechanism;
- profile/manifest-driven scaffolding;
- reusable UI Composition Contract;
- Integration Adapter Catalog.

### CLI
- `pyrax profiles`;
- `pyrax catalog blocks|adapters|ui`;
- `pyrax manifest`;
- `pyrax compose`;
- `pyrax scaffold --profile`;
- `pyrax scaffold --manifest`.

### Reference compositions
Minimal non-customer references exist for:
- Route Engineer;
- Asset Radar;
- Predictive Maintenance;
- OEE Intelligence;
- Decision Engine.

Each reference includes a Solution Manifest and a minimal valid Domain Pack. They are architectural/productization proofs, not certified customer deployments.

## Preserved V0.4 invariants

- deterministic-first;
- Truth before intelligence;
- Evidence required for published decision support;
- UNKNOWN/UNAVAILABLE/NULL are never silently converted to zero;
- human approval default for consequential actions;
- Scenario Engine isolation from canonical state;
- Ontology and Decision Graph integrity;
- maturity remains separate from production readiness;
- AI/LLM remains downstream of validated context;
- MCP remains deferred.

## Release gates

V0.5 may be called STABLE only when:

1. Ruff passes on framework sources/tests.
2. Pytest passes including V0.5 composition tests.
3. Canonical and packaged schemas remain synchronized.
4. The five reference Domain Packs validate.
5. The five reference Solution Manifests validate/materialize.
6. Profile and catalog CLI smoke tests pass.
7. Domain Pack composition smoke test passes.
8. Profile-driven scaffold smoke test passes.
9. Manifest-driven scaffold smoke test passes.
10. Python package build succeeds.

## Non-goals

V0.5 does not:
- certify any reference product for production;
- copy proprietary/customer implementation details from portfolio projects;
- infer source semantics from reusable profiles;
- introduce autonomous consequential actions;
- implement the deferred MCP server.

## Success criterion

The version is successful if a new product can start from:

`Organization Discovery + Domain Pack + Solution Profile/Manifest + Local Fine-Tuning`

instead of rebuilding architecture, reusable mechanics, adapter boundaries, UI composition and QA structure from scratch.
