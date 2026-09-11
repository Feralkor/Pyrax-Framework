from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PATHS = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs",
    ROOT / "golden-cases",
    ROOT / "examples",
)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
FORBIDDEN_COMPANY_MARKER = "XPM"


def _public_text_files() -> list[Path]:
    files: list[Path] = []
    for root in PUBLIC_PATHS:
        if root.is_file():
            files.append(root)
            continue
        files.extend(
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
        )
    return files


def test_public_reference_material_remains_company_neutral() -> None:
    offenders = [
        str(path.relative_to(ROOT))
        for path in _public_text_files()
        if FORBIDDEN_COMPANY_MARKER in path.read_text(encoding="utf-8")
    ]

    assert offenders == []
