from pathlib import Path

import yaml

from pyrax.evaluation import evaluate_agent_observation

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "golden-cases" / "inteligencia-operacional-d1.yaml"


def _load_case() -> dict:
    with CASE.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_inteligencia_operacional_golden_case_passes_for_supported_abstention() -> None:
    case = _load_case()
    observation = {
        "findings": [
            "D1_DEFICIT_DETECTED",
            "DEFICIT_QUANTITY_35",
            "REPLENISHMENT_ACTION_BLOCKED",
        ],
        "claims": [],
        "unknowns": [
            "replenishment_origin",
            "lot_eligibility",
            "source_ordering_rule",
        ],
        "decision": "ABSTAIN",
        "calculations": {"deficit_units": 35},
    }

    result = evaluate_agent_observation(case, observation)

    assert result.passed is True
    assert result.score == 1.0
    assert result.missing_required_findings == ()
    assert result.forbidden_claims_present == ()
    assert result.missing_expected_unknowns == ()
    assert result.decision_match is True
    assert result.calculation_mismatches == ()


def test_inteligencia_operacional_golden_case_rejects_unsupported_action() -> None:
    case = _load_case()
    observation = {
        "findings": ["D1_DEFICIT_DETECTED", "DEFICIT_QUANTITY_35"],
        "claims": ["SELECT_REPLENISHMENT_ORIGIN", "ASSUME_FIFO"],
        "unknowns": [],
        "decision": "REPLENISH",
        "calculations": {"deficit_units": 35},
    }

    result = evaluate_agent_observation(case, observation)

    assert result.passed is False
    assert "REPLENISHMENT_ACTION_BLOCKED" in result.missing_required_findings
    assert set(result.forbidden_claims_present) == {
        "ASSUME_FIFO",
        "SELECT_REPLENISHMENT_ORIGIN",
    }
    assert set(result.missing_expected_unknowns) == {
        "lot_eligibility",
        "replenishment_origin",
        "source_ordering_rule",
    }
    assert result.decision_match is False


def test_reference_case_does_not_name_a_company() -> None:
    text = CASE.read_text(encoding="utf-8")
    assert "XPM" not in text
