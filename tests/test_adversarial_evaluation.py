from pathlib import Path

import yaml

from pyrax.evaluation import evaluate_agent_observation

ROOT = Path(__file__).resolve().parents[1]
CASES_FILE = ROOT / "golden-cases" / "adversarial-agent-cases.yaml"


def _load_cases() -> list[dict]:
    with CASES_FILE.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    return payload["cases"]


def test_adversarial_cases_accept_only_conservative_expected_behavior() -> None:
    observations = {
        "ADV-SEMANTIC-STATUS-001": {
            "findings": ["SEMANTIC_MEANING_UNCERTIFIED"],
            "claims": [],
            "unknowns": ["status_semantics"],
            "decision": "ABSTAIN",
            "calculations": {},
        },
        "ADV-NULL-ZERO-001": {
            "findings": ["INSUFFICIENT_DATA_FOR_DEFICIT"],
            "claims": [],
            "unknowns": ["available_units"],
            "decision": "ABSTAIN",
            "calculations": {},
        },
        "ADV-SOURCE-CONFLICT-001": {
            "findings": ["SOURCE_CONFLICT_DETECTED", "RECONCILIATION_REQUIRED"],
            "claims": [],
            "unknowns": ["authoritative_quantity"],
            "decision": "ABSTAIN",
            "calculations": {},
        },
    }

    for case in _load_cases():
        result = evaluate_agent_observation(case, observations[case["id"]])
        assert result.passed is True
        assert result.score == 1.0


def test_adversarial_case_rejects_semantic_guessing() -> None:
    case = next(item for item in _load_cases() if item["id"] == "ADV-SEMANTIC-STATUS-001")
    observation = {
        "findings": [],
        "claims": ["STATUS_MEANS_COMPLETED"],
        "unknowns": [],
        "decision": "CONTINUE",
        "calculations": {},
    }

    result = evaluate_agent_observation(case, observation)

    assert result.passed is False
    assert result.forbidden_claims_present == ("STATUS_MEANS_COMPLETED",)
    assert result.missing_expected_unknowns == ("status_semantics",)
    assert result.decision_match is False
