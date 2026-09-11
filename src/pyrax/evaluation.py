from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    passed: bool
    score: float
    passed_checks: int
    total_checks: int
    missing_required_findings: tuple[str, ...]
    forbidden_claims_present: tuple[str, ...]
    missing_expected_unknowns: tuple[str, ...]
    decision_match: bool
    calculation_mismatches: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _string_set(value: object) -> set[str]:
    if value is None:
        return set()
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError("Evaluation lists must contain only strings")
    return set(value)


def evaluate_agent_observation(case: dict[str, Any], observation: dict[str, Any]) -> EvaluationResult:
    """Score a structured agent observation against one deterministic Golden Case.

    The harness deliberately evaluates normalized identifiers instead of natural-language
    similarity. This keeps the benchmark deterministic and avoids using an LLM as judge.
    """
    if not isinstance(case, dict):
        raise ValueError("Evaluation case must be a mapping/object")
    if not isinstance(observation, dict):
        raise ValueError("Agent observation must be a mapping/object")

    case_id = case.get("id")
    expected = case.get("expected")
    if not isinstance(case_id, str) or not case_id:
        raise ValueError("Evaluation case requires a non-empty id")
    if not isinstance(expected, dict):
        raise ValueError("Evaluation case requires an expected mapping/object")

    findings = _string_set(observation.get("findings", []))
    claims = _string_set(observation.get("claims", []))
    unknowns = _string_set(observation.get("unknowns", []))

    required_findings = _string_set(expected.get("required_findings", []))
    forbidden_claims = _string_set(expected.get("forbidden_claims", []))
    expected_unknowns = _string_set(expected.get("expected_unknowns", []))

    missing_required = tuple(sorted(required_findings - findings))
    forbidden_present = tuple(sorted(forbidden_claims & claims))
    missing_unknowns = tuple(sorted(expected_unknowns - unknowns))

    expected_decision = expected.get("decision")
    observed_decision = observation.get("decision")
    decision_match = expected_decision is None or observed_decision == expected_decision

    expected_calculations = expected.get("calculations", {})
    observed_calculations = observation.get("calculations", {})
    if not isinstance(expected_calculations, dict) or not isinstance(observed_calculations, dict):
        raise ValueError("Evaluation calculations must be mapping/objects")

    calculation_mismatches = tuple(
        sorted(
            key
            for key, expected_value in expected_calculations.items()
            if observed_calculations.get(key) != expected_value
        )
    )

    total_checks = (
        len(required_findings)
        + len(forbidden_claims)
        + len(expected_unknowns)
        + len(expected_calculations)
        + (1 if expected_decision is not None else 0)
    )
    failed_checks = (
        len(missing_required)
        + len(forbidden_present)
        + len(missing_unknowns)
        + len(calculation_mismatches)
        + (0 if decision_match else 1)
    )
    passed_checks = total_checks - failed_checks
    score = 1.0 if total_checks == 0 else passed_checks / total_checks

    return EvaluationResult(
        case_id=case_id,
        passed=failed_checks == 0,
        score=score,
        passed_checks=passed_checks,
        total_checks=total_checks,
        missing_required_findings=missing_required,
        forbidden_claims_present=forbidden_present,
        missing_expected_unknowns=missing_unknowns,
        decision_match=decision_match,
        calculation_mismatches=calculation_mismatches,
    )
