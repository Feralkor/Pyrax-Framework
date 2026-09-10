from decimal import Decimal
from pathlib import Path

import yaml

from pyrax.models import ConfidenceLevel
from pyrax.runtime import DecisionEngine, SignalEngine, TruthEngine, coverage, deficit

ROOT = Path(__file__).resolve().parents[1]
CASES = yaml.safe_load((ROOT / "golden-cases" / "framework-core.yaml").read_text(encoding="utf-8"))["cases"]


def _case(case_id: str) -> dict:
    return next(case for case in CASES if case["id"] == case_id)


def test_unknown_never_zero_golden_case() -> None:
    case = _case("GC-UNKNOWN-001")
    assert coverage(case["input"]["available"], case["input"]["demand"]) is None
    assert deficit(case["input"]["available"], case["input"]["demand"]) is None


def test_coverage_golden_case() -> None:
    case = _case("GC-COVERAGE-001")
    assert coverage(case["input"]["available"], case["input"]["demand"]) == Decimal("0.8")
    assert deficit(case["input"]["available"], case["input"]["demand"]) == Decimal("2")


def test_decision_abstention_golden_case() -> None:
    fact = TruthEngine.fact(
        "required_input",
        None,
        confidence=ConfidenceLevel.INSUFFICIENT_DATA,
        unknown_reason="not observed",
    )
    signal = SignalEngine.evaluate("risk", (fact,), predicate=lambda _: True)
    assert signal is not None
    assert DecisionEngine.recommend(signal, decision_id="review", action="Review") is None
