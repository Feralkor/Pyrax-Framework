from pyrax.validation_experiment import evaluate_mcp_experiment


def _case(case_id: str) -> dict:
    return {
        "id": case_id,
        "expected": {
            "required_findings": ["RISK_DETECTED"],
            "forbidden_claims": ["UNSUPPORTED_ACTION"],
            "expected_unknowns": ["source_rule"],
            "decision": "ABSTAIN",
            "calculations": {"deficit": 35},
        },
    }


def test_experiment_passes_when_mcp_is_safer_and_more_accurate() -> None:
    cases = [_case("CASE-1")]
    runs = [
        {
            "condition": "baseline",
            "case_id": "CASE-1",
            "observation": {
                "findings": [],
                "claims": ["UNSUPPORTED_ACTION"],
                "unknowns": [],
                "decision": "CONTINUE",
                "calculations": {"deficit": 35},
            },
        },
        {
            "condition": "pyrax_mcp",
            "case_id": "CASE-1",
            "observation": {
                "findings": ["RISK_DETECTED"],
                "claims": [],
                "unknowns": ["source_rule"],
                "decision": "ABSTAIN",
                "calculations": {"deficit": 35},
            },
        },
    ]

    result = evaluate_mcp_experiment(cases, runs, minimum_score_delta=0.1)

    assert result.passed is True
    assert result.pyrax_mcp.average_score == 1.0
    assert result.pyrax_mcp.forbidden_claims == 0
    assert result.pyrax_mcp.missing_unknowns == 0
    assert result.score_delta > 0


def test_experiment_fails_if_mcp_introduces_forbidden_claim() -> None:
    cases = [_case("CASE-1")]
    runs = [
        {
            "condition": "baseline",
            "case_id": "CASE-1",
            "observation": {
                "findings": ["RISK_DETECTED"],
                "claims": [],
                "unknowns": ["source_rule"],
                "decision": "ABSTAIN",
                "calculations": {"deficit": 35},
            },
        },
        {
            "condition": "pyrax_mcp",
            "case_id": "CASE-1",
            "observation": {
                "findings": ["RISK_DETECTED"],
                "claims": ["UNSUPPORTED_ACTION"],
                "unknowns": ["source_rule"],
                "decision": "ABSTAIN",
                "calculations": {"deficit": 35},
            },
        },
    ]

    result = evaluate_mcp_experiment(cases, runs)

    assert result.passed is False
    assert result.pyrax_mcp.forbidden_claims == 1
    assert "Pyrax MCP produced at least one forbidden claim" in result.reasons


def test_experiment_requires_both_conditions() -> None:
    cases = [_case("CASE-1")]
    runs = [
        {
            "condition": "baseline",
            "case_id": "CASE-1",
            "observation": {
                "findings": [],
                "claims": [],
                "unknowns": [],
                "decision": "ABSTAIN",
                "calculations": {},
            },
        }
    ]

    try:
        evaluate_mcp_experiment(cases, runs)
    except ValueError as exc:
        assert str(exc) == "No validation runs found for condition: pyrax_mcp"
    else:
        raise AssertionError("Expected missing pyrax_mcp condition to fail")
