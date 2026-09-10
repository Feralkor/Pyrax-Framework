# Pyrax Framework — MCP Specification

## Purpose

The Pyrax MCP is the intelligent interface for applying the framework consistently across new products and domains.

The MCP must expose framework knowledge, templates and validation workflows without becoming the source of business truth.

## Responsibilities

The MCP should help agents and developers:
- start a new solution discovery;
- define a domain pack;
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

## Guardrails

The MCP must never:
- fabricate missing source semantics;
- certify a field because its name looks obvious;
- convert unknown values to zero;
- authorize destructive actions against production systems by default;
- copy product-specific rules into another domain without explicit validation;
- allow an LLM response to overwrite canonical facts.

## Readiness assessment

`assess_readiness` should evaluate at least:
- decision defined;
- decision owner defined;
- source(s) identified;
- entities/grain defined;
- semantic gaps explicit;
- first vertical slice defined;
- evidence requirements defined;
- guardrails defined;
- Golden Cases present.

Suggested states:
- `DISCOVERY_REQUIRED`
- `READY_FOR_TRUTH_MAPPING`
- `READY_FOR_VERTICAL_SLICE`
- `READY_FOR_ASSISTED_DEMO`
- `PRODUCTION_CERTIFICATION_REQUIRED`

## Architecture

The MCP should read framework assets from this repository and product/domain configuration from the target solution. It should return structured outputs that can be versioned in Git.

The MCP is an orchestration and knowledge interface. Runtime operational decisions remain inside the product's certified application architecture.
