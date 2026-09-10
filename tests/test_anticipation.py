from decimal import Decimal

from pyrax.runtime import aging, coverage, dead_reckoning, deficit, resolve_confidence
from pyrax.models import ConfidenceLevel


def test_coverage_and_deficit_preserve_unknown() -> None:
    assert coverage(None, 10) is None
    assert coverage(10, None) is None
    assert deficit(None, 10) is None
    assert deficit(10, None) is None


def test_coverage_and_deficit_are_deterministic() -> None:
    assert coverage(8, 10) == Decimal("0.8")
    assert deficit(8, 10) == Decimal("2")
    assert deficit(12, 10) == Decimal("0")


def test_aging_and_dead_reckoning() -> None:
    assert aging(100, 160) == Decimal("60")
    assert dead_reckoning(100, -2, 5) == Decimal("90")
    assert dead_reckoning(None, -2, 5) is None


def test_confidence_is_granular_and_conservative() -> None:
    assert resolve_confidence([ConfidenceLevel.CERTIFIED]) == ConfidenceLevel.CERTIFIED
    assert resolve_confidence([ConfidenceLevel.CERTIFIED, ConfidenceLevel.ASSISTED]) == ConfidenceLevel.ASSISTED
    assert resolve_confidence([ConfidenceLevel.INSUFFICIENT_DATA]) == ConfidenceLevel.INSUFFICIENT_DATA
    assert resolve_confidence([]) == ConfidenceLevel.INSUFFICIENT_DATA
