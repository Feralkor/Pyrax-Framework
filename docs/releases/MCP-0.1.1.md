# Pyrax MCP 0.1.1 — Validation Instrumentation

Status: **RELEASE CANDIDATE / PRODUCT EXPERIMENT PENDING**

## Objective

Add deterministic measurement, privacy-safe auditability and contract protection around the technically validated Pyrax MCP v0.1 before expanding the MCP tool surface or deployment model.

V0.1.1 does **not** add new business tools. The public MCP surface remains exactly six read-only tools over local stdio.

## Delivered

- deterministic evaluation harness (`src/pyrax/evaluation.py`);
- synthetic company-neutral Inteligência Operacional D+1 Golden Case;
- adversarial benchmark cases for:
  - uncertified semantic meaning;
  - NULL/unavailable values incorrectly treated as zero;
  - conflicting sources without authoritative reconciliation;
- optional metadata-only JSONL audit through `PYRAX_MCP_AUDIT_LOG`;
- public API v0.1 contract snapshot;
- exact MCP tool-surface snapshot;
- vendor-neutral stdio host examples;
- automated company-neutral public-reference guard;
- documentation for baseline-vs-MCP product evaluation.

## Evaluation contract

Agent observations are normalized into:

```yaml
findings: []
claims: []
unknowns: []
decision: ABSTAIN
calculations: {}
```

Golden Cases define deterministic expectations:

```yaml
expected:
  required_findings: []
  forbidden_claims: []
  expected_unknowns: []
  decision: ABSTAIN
  calculations: {}
```

The canonical benchmark score is produced by deterministic matching, not by another LLM.

## Privacy boundary

Public benchmark/reference material is company-neutral.

- Internal operational references use the neutral name **Inteligência Operacional**.
- Reference values are synthetic or minimized.
- Company/customer names, credentials, proprietary identifiers and private operational values must not enter public fixtures.
- CI scans public docs/examples/Golden Cases and fails if the forbidden company marker reappears.

## Audit boundary

Audit is opt-in and disabled by default.

When configured, the JSONL audit captures:

- UTC timestamp;
- tool name;
- framework version;
- public API version;
- duration;
- outcome;
- small whitelisted result summary or exception type.

It does not capture tool arguments, Domain Packs, Solution Manifests or full results.

## Contract stability

`tests/fixtures/public-api-contract.yaml` pins the API v0.1 response-key surface and MCP tool names.

Backward-incompatible changes require an explicit API-version decision.

## Product experiment gate

The next milestone is not MCP v0.2 implementation. It is a controlled comparison of the same synthetic/neutral operational cases under two conditions:

1. agent without Pyrax MCP;
2. the same class of agent with Pyrax MCP available.

Track:

- deterministic harness score;
- forbidden claims;
- missed required findings;
- lost UNKNOWNs;
- decision/abstention correctness;
- deterministic calculation correctness;
- time to correct assessment;
- manual corrections;
- variance across compatible agent hosts/models.

Only consider v0.2 if evidence shows that MCP-assisted runs materially improve reliability or workflow efficiency without weakening Pyrax invariants.

## Candidate v0.2 scope after validation

- Domain Pack composition through MCP;
- controlled scaffold generation;
- internal Streamable HTTP transport.

OAuth, billing, multi-tenancy, public marketplace distribution and operational-system connectivity remain outside this gate.
