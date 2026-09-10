from pathlib import Path

from pyrax.api import (
    API_VERSION,
    assess_maturity,
    assess_readiness,
    get_catalog,
    get_solution_profile,
    validate_domain_pack,
    validate_solution_manifest,
)
from pyrax.validation import load_document

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"


def test_public_api_validates_and_assesses_domain_pack() -> None:
    pack = load_document(FIXTURE)

    validation = validate_domain_pack(pack)
    readiness = assess_readiness(pack)
    maturity = assess_maturity(pack)

    assert validation["valid"] is True
    assert validation["framework_version"] == "0.5.0"
    assert validation["api_version"] == API_VERSION
    assert readiness["valid"] is True
    assert readiness["production_ready"] is True
    assert maturity["valid"] is True
    assert maturity["level"] == "P3_ASSISTED_INTELLIGENCE"


def test_public_api_returns_structured_validation_failures() -> None:
    result = validate_domain_pack({})

    assert result["valid"] is False
    assert result["errors"]
    assert result["framework_version"] == "0.5.0"


def test_public_api_exposes_profiles_catalogs_and_manifest_validation() -> None:
    profiles = get_solution_profile()
    fleet = get_solution_profile("fleet-intelligence")
    missing = get_solution_profile("does-not-exist")
    blocks = get_catalog("blocks")
    manifest = validate_solution_manifest({"profile": "fleet-intelligence"})

    assert profiles["found"] is True
    assert "fleet-intelligence" in profiles["profiles"]
    assert fleet["found"] is True
    assert fleet["profile"]["maturity_target"] == "P4_PREDICTIVE_OPERATIONS"
    assert missing["found"] is False
    assert blocks["found"] is True
    assert "dead-reckoning" in blocks["items"]
    assert manifest["valid"] is True
