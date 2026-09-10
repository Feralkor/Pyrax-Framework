# Pyrax Framework — MCP Specification

Status: **DEFERRED / FUTURE INTERFACE**

This document intentionally does not define current release work. Pyrax Framework v0.2 focuses on the standalone framework, CLI, runtime, schemas, templates, patterns, readiness and QA. The MCP will be designed in a later phase.

## Purpose

The future Pyrax MCP is the intelligent interface for applying the framework consistently across new products and domains.

The MCP must expose framework knowledge, templates and validation workflows without becoming the source of business truth.

## Current non-MCP foundation

The following capabilities already exist without MCP and should be reused rather than reimplemented:

- `pyrax validate` — Domain Pack schema and cross-reference validation;
- `pyrax assess` — readiness assessment;
- `pyrax scaffold` — product scaffolding;
- machine-readable schemas under `schemas/`;
- reusable patterns under `patterns/`;
- runtime contracts under `src/pyrax/runtime/`.

A future MCP should orchestrate these capabilities where practical instead of creating a second implementation.

## Responsibilities

The MCP may later help agents and developers:
- start a new solution discovery;
- define a Domain Pack;
- map sources and systems of record;
- define entities, states and relationships;
- register known and unknown semantics;
- create data/query contracts;
- define signals and decisions;
- create evidence contracts;
- generate Golden Cases;
- assess readiness;
- scaffold a new product structure;
- inspect framework compliance.

## Candidate tools

- `pyrax.start_discovery`
- `pyrax.define_domain`
- `pyrax.map_sources`
- `pyrax.define_entity`
- `pyrax.define_signal`
- `pyrax.define_decision`
- `pyrax.create_contract`
- `pyrax.create_evidence_model`
- `pyrax.create_golden_cases`
- `pyrax.assess_readiness`
- `pyrax.scaffold_product`
- `pyrax.validate_domain_pack`

These names are provisional until MCP design begins.

## Guardrails

The MCP must never:
- fabricate missing source semantics;
- certify a field because its name looks obvious;
- convert unknown values to zero;
- authorize destructive actions against production systems by default;
- copy product-specific rules into another domain without explicit validation;
- allow an LLM response to overwrite canonical facts;
- weaken CLI/runtime validation merely to complete an agent task.

## Readiness assessment

A future MCP should consume the canonical Readiness Model rather than maintain a conflicting readiness vocabulary. `docs/READINESS-MODEL.md` and `src/pyrax/readiness.py` are the current source of truth.

## Architecture

The MCP should read framework assets from this repository and product/domain configuration from the target solution. It should return structured outputs that can be versioned in Git.

The MCP is an orchestration and knowledge interface. Runtime operational decisions remain inside the product's certified application architecture.

## Activation rule

Do not implement the MCP until an explicit project decision reactivates this work. Ordinary framework evolution must not treat this specification as an unfinished v0.2 requirement.
