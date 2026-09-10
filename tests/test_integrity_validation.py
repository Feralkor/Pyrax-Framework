from pathlib import Path

from pyrax.validation import load_document, validate_domain_pack

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"


def test_signal_cannot_reference_unknown_source() -> None:
    pack = load_document(FIXTURE)
    pack["signals"][0]["evidence_required"] = ["missing-source"]
    errors = validate_domain_pack(pack)
    assert any("missing-source" in error for error in errors)


def test_decision_cannot_reference_unknown_signal() -> None:
    pack = load_document(FIXTURE)
    pack["decisions"][0]["triggered_by"] = ["missing-signal"]
    errors = validate_domain_pack(pack)
    assert any("missing-signal" in error for error in errors)


def test_semantic_states_are_mutually_exclusive() -> None:
    pack = load_document(FIXTURE)
    pack["semantics"]["unknowns"] = ["capacity"]
    errors = validate_domain_pack(pack)
    assert any("CERTIFIED and UNKNOWN" in error for error in errors)


def test_identifiers_must_be_unique() -> None:
    pack = load_document(FIXTURE)
    pack["sources"].append(dict(pack["sources"][0]))
    errors = validate_domain_pack(pack)
    assert any("duplicate identifier 'ops-db'" in error for error in errors)
