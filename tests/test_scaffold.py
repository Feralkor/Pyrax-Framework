from pathlib import Path

from pyrax.scaffold import scaffold_project
from pyrax.validation import load_document

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"


def test_scaffold_generates_domain_aware_project(tmp_path: Path) -> None:
    pack = load_document(FIXTURE)
    root = scaffold_project("demo-solution", tmp_path, domain_pack=pack)

    assert (root / "README.md").exists()
    assert (root / "domain-pack.yaml").exists()
    assert (root / "domain-pack.json").exists()
    assert (root / "docs" / "PRODUCT-CHARTER.md").exists()
    assert (root / "docs" / "SOURCE-MAP.md").exists()
    assert (root / "docs" / "SIGNAL-CATALOG.md").exists()
    assert (root / "docs" / "DECISION-CATALOG.md").exists()
    assert (root / "src" / "demo_solution" / "__init__.py").exists()

    charter = (root / "docs" / "PRODUCT-CHARTER.md").read_text(encoding="utf-8")
    assert "Prioritize operational attention" in charter
    assert "Operations Lead" in charter
