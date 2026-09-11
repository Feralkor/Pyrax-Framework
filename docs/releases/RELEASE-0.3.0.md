# Pyrax Framework v0.3.0 — Universal Solution Recipe

Status: RELEASE CANDIDATE — awaiting CI completion for stable certification.

## Purpose

v0.3.0 establishes Pyrax Framework as a reusable, industry-agnostic recipe for starting and structuring evidence-driven operational intelligence solutions in companies, industries, startups and other operating contexts.

## Canonical workflow

`Organization Context -> Bootstrap -> Discovery -> Data Inventory -> Decision Discovery -> Semantic Mapping -> Domain Pack -> Validate -> Assess -> Scaffold -> Vertical Slice -> Evidence -> Decision Support -> Outcome -> Iteration`

## Included capabilities

- `pyrax bootstrap` for unknown/new-company contexts;
- `pyrax validate` for structural and cross-reference Domain Pack validation;
- `pyrax assess` for readiness assessment;
- `pyrax scaffold` for domain-aware project generation;
- reusable Truth, State, Quality, Reconciliation, Evidence, Confidence, Signal, Anticipation, Decision and Memory primitives;
- Source/Snapshot ports and domain-neutral observability;
- Universal Solution Recipe;
- Discovery Playbook;
- Data Acquisition Playbook;
- Solution Archetypes;
- Technology Profiles;
- Pattern Library;
- Product/Source/Signal/Decision/Data Contract/Query Manifest/Evidence/Outcome/Golden Case templates;
- machine-readable Domain Pack and Evidence schemas;
- reference examples from Inteligência Operacional, Route Engineer and NeuroGear;
- hypothetical Strategicos example demonstrating fine-tuning without fabricated certification;
- automated tests, Golden Cases and GitHub Actions quality workflow.

## Core invariants

- UNKNOWN, unavailable and null are never silently converted to zero.
- Field existence is not semantic certification.
- Evidence is required for published decision support.
- Insufficient data causes abstention instead of fabricated recommendation.
- Confidence is granular and conservative.
- Human approval is the default for operational actions.
- Deterministic methods are preferred before ML when sufficient.
- AI/LLM capability remains downstream of canonical truth and evidence.
- Generic runtime mechanics must remain domain-agnostic.

## Release certification gate

This release candidate may be considered STABLE only after the `Pyrax Framework Quality` workflow for the v0.3.0 HEAD completes successfully, including:

1. Ruff on supported Python versions;
2. pytest regression suite;
3. canonical Domain Pack validation;
4. hypothetical fine-tuning example validation;
5. production-ready fixture assessment;
6. scaffold smoke test;
7. bootstrap smoke test;
8. Python package build.

Until that workflow is green, the code is versioned as 0.3.0 but release certification remains pending.

## MCP

MCP implementation is intentionally deferred. `docs/MCP-SPECIFICATION.md` remains a future interface contract and is not part of v0.3.0 release acceptance.

## Intended use

Use v0.3.0 as the canonical starting point whenever a new operational intelligence solution is required. Start with `pyrax bootstrap` when the organization/domain is not yet understood; promote knowledge into a validated Domain Pack only when supported by discovery and evidence; scaffold implementation only after the domain contract is structurally coherent.
