from decimal import Decimal

import pytest

from pyrax.models import ConfidenceLevel
from pyrax.runtime import DecisionEngine, QualityGate, ReconciliationGate, SignalEngine, TruthEngine, build_evidence


def test_unknown_fact_requires_reason() -> None:
    with pytest.raises(ValueError):
        TruthEngine.fact("missing", None, confidence=ConfidenceLevel.INSUFFICIENT_DATA)


def test_signal_and_decision_preserve_confidence_and_evidence() -> None:
    evidence = build_evidence(source="ops-db", grain="entity", rule_version="1")
    fact = TruthEngine.fact(
        "capacity_gap",
        5,
        confidence=ConfidenceLevel.CERTIFIED,
        evidence=(evidence,),
    )
    signal = SignalEngine.evaluate(
        "capacity-risk",
        (fact,),
        predicate=lambda facts: facts[0].value > 0,
        severity="CRITICAL",
    )
    recommendation = DecisionEngine.recommend(
        signal,
        decision_id="review-capacity",
        action="Review capacity before accepting more workload",
    )
    assert signal is not None
    assert recommendation is not None
    assert recommendation.confidence == ConfidenceLevel.CERTIFIED
    assert recommendation.evidence == (evidence,)
    assert recommendation.human_approval_required is True


def test_insufficient_signal_abstains_from_recommendation() -> None:
    fact = TruthEngine.fact(
        "capacity",
        None,
        confidence=ConfidenceLevel.INSUFFICIENT_DATA,
        unknown_reason="source unavailable",
    )
    signal = SignalEngine.evaluate("capacity-risk", (fact,), predicate=lambda _: True)
    assert signal is not None
    assert DecisionEngine.recommend(signal, decision_id="x", action="act") is None


def test_quality_and_reconciliation_gates() -> None:
    quality = QualityGate([lambda record: record.get("value", 0) >= 0])
    assert quality.evaluate({"value": 1}) == (True, [])
    assert quality.evaluate({"value": -1})[0] is False
    passed, delta = ReconciliationGate.compare(Decimal("10"), Decimal("10.01"), tolerance=Decimal("0.02"))
    assert passed is True
    assert delta == Decimal("-0.01")
