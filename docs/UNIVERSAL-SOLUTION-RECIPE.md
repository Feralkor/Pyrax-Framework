# Pyrax Framework — Universal Solution Recipe

Status: CANONICAL
Version: 0.5

## Purpose

This is the reusable recipe for starting an operational intelligence solution in any organization: industry, services, logistics, manufacturing, startup, SaaS, finance, retail, healthcare, public sector or another domain.

The framework does not assume a WMS, ERP, CRM, cloud provider, programming language, database or UI stack. It standardizes the reasoning, engineering and product-composition sequence.

## Universal sequence

`Organization Context -> Problem Discovery -> Decision Discovery -> Data Discovery -> Semantic Mapping -> Domain Pack -> Validation -> Profile/Composition -> Readiness -> Scaffold -> Vertical Slice -> Evidence -> Decision Support -> Outcome -> Iteration`

## Phase 0 — Organization context

Understand before designing:
- business model;
- operating model;
- products/services;
- customers/users;
- critical processes;
- decision makers;
- systems and data landscape;
- regulatory/security constraints;
- deployment constraints;
- current pains and opportunities.

Output: `organization-profile.yaml`.

## Phase 1 — Problem and decision discovery

Do not ask first “what dashboard should we build?”. Ask:
- Which decision is currently late, manual, reactive or poorly informed?
- Who owns that decision?
- What happens when the decision is wrong or late?
- What action can the owner actually take?
- What is the desired outcome?

Output: Discovery Worksheet + initial Product Charter.

## Phase 2 — Data discovery

Map:
- Systems of Record;
- reference sources;
- external sources;
- event streams;
- files/spreadsheets;
- ownership;
- grain;
- keys;
- timestamps;
- freshness;
- retention;
- access mode;
- semantic unknowns.

Output: Source Map + Data Inventory.

## Phase 3 — Domain model

Define:
- entities;
- relationships;
- operational grain;
- states;
- events;
- timestamps;
- invariants;
- candidate and certified semantics.

Output: Domain Pack draft.

## Phase 4 — Anticipation model

Select the smallest appropriate patterns first:
- aging;
- coverage;
- deficit propagation;
- rate of change;
- baseline deviation;
- capacity risk;
- bottleneck detection;
- dead reckoning;
- constraint propagation;
- scenario projection.

ML is optional and never a substitute for unresolved source semantics.

Output: Signal Catalog.

## Phase 5 — Decision model

For every signal define:
- candidate action;
- decision owner;
- constraints;
- evidence required;
- confidence policy;
- approval policy;
- expected impact;
- abstention conditions.

Output: Decision Catalog + Evidence Contract.

## Phase 6 — Validation

Run:

```bash
pyrax validate domain-pack.yaml
```

A valid model is not automatically production-ready.

## Phase 7 — Product composition

Choose a reusable product shape only after the domain problem is understood.

Inspect available pieces:

```bash
pyrax profiles
pyrax catalog blocks
pyrax catalog adapters
pyrax catalog ui
```

Then either:
- select a Solution Profile;
- create a Solution Manifest;
- compose an approved base Domain Pack with organization-specific overlays.

Examples:

```bash
pyrax manifest solution-manifest.yaml
pyrax compose base-domain-pack.yaml --overlay organization.yaml --output domain-pack.yaml
```

Composition reduces repeated engineering. It never certifies inherited business semantics.

## Phase 8 — Readiness and maturity

Run:

```bash
pyrax assess domain-pack.yaml
pyrax maturity domain-pack.yaml
```

Readiness and intelligence maturity are separate concepts.

## Phase 9 — Scaffold

Generate the implementation skeleton from a Domain Pack plus optional profile/manifest:

```bash
pyrax scaffold my-solution --profile decision-intelligence --domain-pack domain-pack.yaml
```

or:

```bash
pyrax scaffold my-solution --manifest solution-manifest.yaml --domain-pack domain-pack.yaml
```

## Phase 10 — Smallest vertical slice

Implement one complete chain:

`Source -> Contract -> Quality -> Reconciliation -> State -> Signal -> Decision -> Evidence -> UX -> Outcome`

Do not expand horizontally before one vertical is demonstrably trustworthy.

## Phase 11 — Outcome learning

Capture:

`Observation -> Signal -> Recommendation -> Action -> Outcome`

Only then calibrate rules, thresholds, statistics or ML.

## Core rule

> Reconstruct reality first. Calculate second. Explain third. Recommend last.

## Reuse boundary

Reuse architecture, contracts, validation, runtime primitives, Solution Profiles, Building Blocks, adapter classes, UI composition contracts, patterns and QA. Never reuse another company's domain semantics without local validation.
