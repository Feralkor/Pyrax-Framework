# Pyrax MCP v0.1.1 — Product Validation Protocol

Status: READY FOR BLINDED AGENT RUN

## Objective

Determine whether access to Pyrax MCP materially improves an AI agent's reliability when evaluating operational-intelligence cases.

The experiment measures behavior, not protocol connectivity. Technical MCP validation is already covered separately by CI.

## Experimental design

Each case is executed under two conditions:

1. `baseline` — the agent receives the case input and task instructions, but no Pyrax MCP tools and no expected-answer metadata.
2. `pyrax_mcp` — the same model receives the same case input and task instructions, with the six Pyrax MCP v0.1 tools available.

The agent producing observations must not receive:

- `expected.required_findings`;
- `expected.forbidden_claims`;
- `expected.expected_unknowns`;
- `expected.decision`;
- expected calculation values beyond those derivable from the case input;
- previous condition outputs.

A run is invalid if the agent has already seen the expected section for the case.

## Frozen case set

The initial validation set is:

- `GC-IO-D1-001` — deterministic D+1 deficit with blocked replenishment action;
- `ADV-SEMANTIC-STATUS-001` — ambiguous status semantics;
- `ADV-NULL-ZERO-001` — NULL must not become zero;
- `ADV-SOURCE-CONFLICT-001` — conflicting quantities without reconciled authority.

All cases are synthetic and company-neutral.

## Normalized observation contract

Every agent response must be normalized to:

```yaml
findings: []
claims: []
unknowns: []
decision: ABSTAIN
calculations: {}
```

Natural-language explanation may be retained separately for qualitative review, but the deterministic evaluation uses only the normalized observation.

## Minimum experiment

Run all four cases once under each condition with the same model/version and equivalent prompting.

Minimum sample:

- 4 baseline runs;
- 4 Pyrax MCP runs.

Recommended follow-up after the first pass:

- repeat each condition three times to measure variance;
- repeat using a second MCP-capable model/host.

## Deterministic gate

`evaluate_mcp_experiment()` produces a GO/NO-GO result.

Promotion requires all of the following for the `pyrax_mcp` condition:

- zero forbidden claims;
- zero missing required UNKNOWNs;
- zero decision mismatches;
- zero deterministic calculation mismatches;
- no regression versus baseline on any of the above;
- score delta greater than or equal to the configured minimum.

For the first internal experiment, use `minimum_score_delta=0.0` so safety/conformance is the hard gate. A positive score delta is desirable and should be reported separately.

## Metrics to retain

For every run record:

- model/host identifier;
- condition;
- case id;
- normalized observation;
- wall-clock duration when available;
- manual corrections required to normalize the output;
- MCP tool calls used, for the MCP condition;
- qualitative notes.

Do not record credentials, proprietary customer identifiers or production payloads.

## Interpretation

### GO for MCP v0.2

The experiment passes the deterministic gate and the MCP condition demonstrates at least one material benefit such as:

- fewer unsupported claims;
- better UNKNOWN preservation;
- more correct abstention;
- fewer manual corrections;
- more consistent answers across repeated runs.

### HOLD

The MCP condition passes safety gates but does not improve the workflow enough to justify adding side-effecting tools.

### NO-GO

The MCP condition introduces unsupported claims, loses UNKNOWNs, worsens decisions/calculations, or creates material workflow regressions.

## Scientific constraint

Do not use an agent that has already inspected the expected outputs as evidence for the blinded product experiment. Such a run may be used only as a protocol rehearsal and must be labeled accordingly.
