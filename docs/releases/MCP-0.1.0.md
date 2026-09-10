# Pyrax MCP 0.1.0 — Internal Agent Interface

Status: **TECHNICALLY VALIDATED / XPM PRODUCT VALIDATION PENDING**

## Objective

Expose the proven Pyrax Framework through a native MCP interface so AI agents can apply validation, readiness, maturity and product-composition knowledge without reimplementing the methodology in prompts.

## Architecture

`Pyrax Core -> pyrax.api -> MCP adapter`

The MCP server is not a second implementation of Pyrax. `src/pyrax/api.py` is the public programmatic source of truth shared with future protocol adapters.

## Delivered

- public `pyrax.api` v0.1.0 boundary;
- official MCP Python SDK v2 dependency;
- `pyrax-mcp` console entry point;
- local stdio MCP server;
- six read-only tools;
- structured validation/error results;
- framework/API version metadata in public results;
- public API regression tests;
- in-memory MCP protocol tests using the official client;
- internal usage and security-boundary documentation.

## Tool surface

1. `pyrax_validate_domain_pack`
2. `pyrax_assess_readiness`
3. `pyrax_assess_maturity`
4. `pyrax_validate_solution_manifest`
5. `pyrax_get_solution_profile`
6. `pyrax_get_catalog`

## Safety and scope

All tools are read-only and closed-world. V0.1 does not access operational systems or external data sources and does not write files.

Not included:

- Domain Pack composition via MCP;
- scaffold generation via MCP;
- Streamable HTTP;
- authentication/OAuth;
- multi-tenancy;
- billing/quotas;
- marketplace/registry distribution;
- Oracle/Senior WMS or other provider connections.

## Technical validation

The framework quality workflow completed successfully on the v0.1 implementation baseline:

- Ruff passed;
- the complete Pyrax pytest suite passed on Python 3.11 and 3.12;
- the exact six-tool MCP public surface passed protocol tests;
- read-only/closed-world annotations passed;
- in-memory MCP calls returned structured output;
- invalid artifacts returned structured validation data rather than protocol failures;
- existing V0.5 CLI/composition smoke tests remained green;
- package build succeeded with the MCP SDK dependency and `pyrax-mcp` console entry point.

Technical validation proves implementation integrity, not product value.

## Product-validation gate

Before expanding scope, run the internal XPM Golden Case and compare agent performance with and without MCP.

Track at least:

- time to correct assessment;
- unsupported assumptions introduced by the agent;
- Pyrax invariant violations;
- manual corrections required;
- usefulness of readiness/maturity outputs;
- correct preservation of UNKNOWN, Evidence and abstention behavior.

Proceed toward MCP v0.2 only if native Pyrax tools materially improve the agent workflow.
