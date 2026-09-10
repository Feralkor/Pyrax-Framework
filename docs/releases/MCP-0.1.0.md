# Pyrax MCP 0.1.0 — Internal Agent Interface

Status: RELEASE CANDIDATE / INTERNAL VALIDATION

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

## Release gates

MCP 0.1.0 may be called internally validated only when:

1. Ruff passes;
2. the complete Pyrax pytest suite passes;
3. the six expected MCP tools are the exact public v0.1 tool surface;
4. each tool advertises read-only and closed-world annotations;
5. in-memory MCP calls return structured output;
6. invalid artifacts return structured validation data instead of protocol failure;
7. existing CLI/framework tests remain green;
8. package build succeeds with the MCP dependency and console script.

## Product-validation gate

Technical green CI is necessary but not sufficient for v0.2. Before expanding scope, run the internal XPM Golden Case and compare agent performance with and without MCP.

Proceed only if native Pyrax tools materially reduce unsupported assumptions, manual corrections, or time-to-correct-assessment.
