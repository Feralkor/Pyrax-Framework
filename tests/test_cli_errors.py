import sys
from pathlib import Path

import pytest

from pyrax import cli


def _run_validate(monkeypatch: pytest.MonkeyPatch, path: Path | str) -> None:
    monkeypatch.setattr(sys, "argv", ["pyrax", "validate", str(path)])
    with pytest.raises(SystemExit) as exc_info:
        cli.main()
    assert exc_info.value.code == 1


def test_validate_missing_file_reports_clean_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    missing = tmp_path / "does-not-exist.yaml"

    _run_validate(monkeypatch, missing)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"Error: file not found: {missing}\n"
    assert "Traceback (most recent call last)" not in captured.err


def test_validate_malformed_yaml_reports_clean_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    malformed = tmp_path / "bad.yaml"
    malformed.write_text("not: [valid: yaml: broken", encoding="utf-8")

    _run_validate(monkeypatch, malformed)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.startswith(f"Error: invalid YAML in {malformed}: ")
    assert captured.err.count("\n") == 1
    assert "Traceback (most recent call last)" not in captured.err


def test_validate_non_mapping_yaml_reports_clean_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    scalar = tmp_path / "string.yaml"
    scalar.write_text("hello world\n", encoding="utf-8")

    _run_validate(monkeypatch, scalar)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "Error: Domain Pack must be a mapping/object\n"
    assert "Traceback (most recent call last)" not in captured.err


def test_unexpected_value_error_is_not_swallowed(monkeypatch: pytest.MonkeyPatch) -> None:
    def raise_unexpected(_: object) -> int:
        raise ValueError("unexpected bug")

    parser = cli.build_parser()
    args = parser.parse_args(["profiles"])
    args.func = raise_unexpected

    class ParserStub:
        def parse_args(self) -> object:
            return args

    monkeypatch.setattr(cli, "build_parser", lambda: ParserStub())

    with pytest.raises(ValueError, match="unexpected bug"):
        cli.main()
