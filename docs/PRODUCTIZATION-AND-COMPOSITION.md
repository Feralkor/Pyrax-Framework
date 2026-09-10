# Pyrax V0.5 — Productization & Composition

## Purpose

V0.5 turns Pyrax from a reusable engineering method into a reusable product-composition system.

The goal is not to copy prior products. The goal is to reuse proven mechanics while forcing each new organization to revalidate its own data, semantics, constraints and decision context.

## Composition equation

`Solution Profile + Building Blocks + Adapter Set + UI Composition + Domain Pack + Organization Overrides = Product Starting Point`

## Layers

### Solution Profile
A reusable starting configuration for a recurring problem shape, such as fleet intelligence, predictive maintenance or industrial performance.

A profile may suggest:
- analytical/decision building blocks;
- adapter classes;
- UI components;
- maturity target.

A profile never certifies customer-specific semantics.

### Building Blocks
Composable mechanics such as dead reckoning, baseline deviation, coverage, constraint propagation and outcome feedback.

Every block preserves:
- explicit UNKNOWN behavior;
- Evidence requirements;
- deterministic-first behavior where applicable;
- domain-neutral implementation boundaries.

### Solution Manifest
The manifest records how one product is composed. It is intentionally separate from the Domain Pack.

- Domain Pack = what the business/domain means.
- Solution Manifest = which reusable Pyrax pieces are selected.

### Domain Pack composition
A base Domain Pack may be combined with organization-specific overlays. The overlay replaces lists and scalar values and recursively merges mappings.

This mechanism exists to reduce duplication, not to transplant unvalidated semantics between companies.

## Composition workflow

1. `pyrax bootstrap` the organization.
2. Complete discovery and data inventory.
3. Select or create a Solution Profile.
4. Create the Domain Pack from observed evidence.
5. Optionally compose a reusable base Domain Pack with local overlays using `pyrax compose`.
6. Create a Solution Manifest.
7. Validate Domain Pack and manifest.
8. Scaffold using profile or manifest.
9. Bind selected blocks to certified domain semantics.
10. Add Golden Cases, reconciliation and integration tests.
11. Reassess readiness and maturity.

## CLI

```bash
pyrax profiles
pyrax profiles fleet-intelligence
pyrax catalog blocks
pyrax catalog adapters
pyrax catalog ui
pyrax manifest solution-manifest.yaml
pyrax compose base-domain-pack.yaml --overlay customer.yaml --output domain-pack.yaml
pyrax scaffold new-product --profile fleet-intelligence --domain-pack domain-pack.yaml
pyrax scaffold new-product --manifest solution-manifest.yaml --domain-pack domain-pack.yaml
```

## Guardrails

- Profiles are hypotheses, not semantic truth.
- Composition must never turn UNKNOWN into ZERO.
- Reused blocks require domain-specific Evidence.
- Scenario output remains hypothetical and must not mutate canonical state.
- Decision Graph integrity rules remain mandatory.
- Human approval remains the default for consequential actions.
- Customer-specific rules must not leak back into generic catalogs unless generalized and independently justified.

## V0.5 proof criterion

V0.5 is successful when representative products can be recreated as minimal reference compositions using the same framework primitives without copying their original implementations.
