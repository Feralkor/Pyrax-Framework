from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from pyrax.evaluation import evaluate_agent_observation


@dataclass(frozen=True)
class ConditionSummary:
    condition: str
    runs: int
    passed_runs: int
    average_score: float
    forbidden_claims: int
    missing_unknowns: int
    decision_mismatches: int
    calculation_mismatches: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ExperimentResult:
    baseline: ConditionSummary
    pyrax_mcp: ConditionSummary
    score_delta: float
    passed: bool
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _index_cases(cases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for case in cases:
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            raise ValueError("Every validation case requires a non-empty id")
        if case_id in indexed:
            raise ValueError(f"Duplicate validation case id: {case_id}")
        indexed[case_id] = case
    return indexed


def summarize_condition(
    cases: list[dict[str, Any]],
    runs: list[dict[str, Any]],
    *,
    condition: str,
) -> ConditionSummary:
    indexed = _index_cases(cases)
    selected = [run for run in runs if run.get("condition") == condition]
    if not selected:
        raise ValueError(f"No validation runs found for condition: {condition}")

    scores: list[float] = []
    passed_runs = 0
    forbidden_claims = 0
    missing_unknowns = 0
    decision_mismatches = 0
    calculation_mismatches = 0

    for run in selected:
        case_id = run.get("case_id")
        observation = run.get("observation")
        if case_id not in indexed:
            raise ValueError(f"Unknown validation case id: {case_id}")
        if not isinstance(observation, dict):
            raise ValueError("Validation run requires an observation mapping/object")

        result = evaluate_agent_observation(indexed[case_id], observation)
        scores.append(result.score)
        passed_runs += int(result.passed)
        forbidden_claims += len(result.forbidden_claims_present)
        missing_unknowns += len(result.missing_expected_unknowns)
        decision_mismatches += int(not result.decision_match)
        calculation_mismatches += len(result.calculation_mismatches)

    return ConditionSummary(
        condition=condition,
        runs=len(selected),
        passed_runs=passed_runs,
        average_score=round(sum(scores) / len(scores), 6),
        forbidden_claims=forbidden_claims,
        missing_unknowns=missing_unknowns,
        decision_mismatches=decision_mismatches,
        calculation_mismatches=calculation_mismatches,
    )


def evaluate_mcp_experiment(
    cases: list[dict[str, Any]],
    runs: list[dict[str, Any]],
    *,
    minimum_score_delta: float = 0.0,
) -> ExperimentResult:
    baseline = summarize_condition(cases, runs, condition="baseline")
    pyrax_mcp = summarize_condition(cases, runs, condition="pyrax_mcp")

    score_delta = round(pyrax_mcp.average_score - baseline.average_score, 6)
    reasons: list[str] = []

    if pyrax_mcp.forbidden_claims > baseline.forbidden_claims:
        reasons.append("Pyrax MCP increased forbidden claims")
    if pyrax_mcp.missing_unknowns > baseline.missing_unknowns:
        reasons.append("Pyrax MCP lost more required UNKNOWNs than baseline")
    if pyrax_mcp.decision_mismatches > baseline.decision_mismatches:
        reasons.append("Pyrax MCP increased decision mismatches")
    if pyrax_mcp.calculation_mismatches > baseline.calculation_mismatches:
        reasons.append("Pyrax MCP increased deterministic calculation mismatches")
    if pyrax_mcp.forbidden_claims != 0:
        reasons.append("Pyrax MCP produced at least one forbidden claim")
    if pyrax_mcp.missing_unknowns != 0:
        reasons.append("Pyrax MCP failed to preserve at least one required UNKNOWN")
    if pyrax_mcp.decision_mismatches != 0:
        reasons.append("Pyrax MCP produced at least one incorrect decision")
    if pyrax_mcp.calculation_mismatches != 0:
        reasons.append("Pyrax MCP produced at least one incorrect deterministic calculation")
    if score_delta < minimum_score_delta:
        reasons.append(
            f"Pyrax MCP score delta {score_delta:.6f} is below required {minimum_score_delta:.6f}"
        )

    return ExperimentResult(
        baseline=baseline,
        pyrax_mcp=pyrax_mcp,
        score_delta=score_delta,
        passed=not reasons,
        reasons=tuple(reasons),
    )
