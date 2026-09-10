# Pyrax Framework — Universal Solution Recipe

Status: CANONICAL
Version: 0.3

## Purpose

This is the reusable recipe for starting an operational intelligence solution in any organization: industry, services, logistics, manufacturing, startup, SaaS, finance, retail, healthcare, public sector or another domain.

The framework does not assume a WMS, ERP, CRM, cloud provider, programming language, database or UI stack. It standardizes the reasoning and engineering sequence.

## Universal sequence

`Organization Context -> Problem Discovery -> Decision Discovery -> Data Discovery -> Semantic Mapping -> Domain Pack -> Validation -> Readiness -> Scaffold -> Vertical Slice -> Evidence -> Decision Support -> Outcome -> Iteration`

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

## Phase 6 — Validation and readiness

Run:

```bash
pyrax validate domain-pack.yaml
pyrax assess domain-pack.yaml
```

A valid model is not automatically production-ready.

## Phase 7 — Scaffold

Generate the implementation skeleton:

```bash
pyrax scaffold my-solution --domain-pack domain-pack.yaml
```

## Phase 8 — Smallest vertical slice

Implement one complete chain:

`Source -> Contract -> Quality -> Reconciliation -> State -> Signal -> Decision -> Evidence -> UX -> Outcome`

Do not expand horizontally before one vertical is demonstrably trustworthy.

## Phase 9 — Outcome learning

Capture:

`Observation -> Signal -> Recommendation -> Action -> Outcome`

Only then calibrate rules, thresholds, statistics or ML.

## Core rule

> Reconstruct reality first. Calculate second. Explain third. Recommend last.

## Reuse boundary

Reuse architecture, contracts, validation, runtime primitives, patterns and QA. Never reuse another company's domain semantics without validation.
