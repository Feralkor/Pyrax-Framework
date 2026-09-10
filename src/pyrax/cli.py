from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from pyrax.bootstrap import bootstrap_discovery
from pyrax.catalogs import ADAPTER_CATALOG, BUILDING_BLOCKS, SOLUTION_PROFILES, UI_COMPONENTS, get_solution_profile
from pyrax.composition import compose_domain_pack, load_solution_manifest, materialize_solution_manifest, validate_solution_manifest
from pyrax.maturity import assess_domain_maturity
from pyrax.readiness import assess_domain_pack
from pyrax.scaffold import scaffold_project
from pyrax.validation import load_canonical_schema, load_document, load_schema, validate_domain_pack


def cmd_validate(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    schema = load_schema(args.schema) if args.schema else load_canonical_schema()
    errors = validate_domain_pack(pack, schema)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


def cmd_assess(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    errors = validate_domain_pack(pack)
    if errors:
        payload = {"valid": False, "production_ready": False, "validation_errors": errors, "items": []}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 1
    report = assess_domain_pack(pack)
    payload = {
        "valid": True,
        "production_ready": report.production_ready,
        "items": [{"area": item.area, "status": item.status.value, "reason": item.reason} for item in report.items],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if report.production_ready else 2


def cmd_maturity(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    errors = validate_domain_pack(pack)
    if errors:
        print(json.dumps({"valid": False, "validation_errors": errors}, ensure_ascii=False, indent=2))
        return 1
    assessment = assess_domain_maturity(pack)
    print(json.dumps({"valid": True, "level": assessment.level.name, "level_value": int(assessment.level), "reasons": list(assessment.reasons)}, ensure_ascii=False, indent=2))
    return 0


def cmd_bootstrap(args: argparse.Namespace) -> int:
    root = bootstrap_discovery(args.organization, args.destination, archetype=args.archetype, force=args.force)
    print(root)
    return 0


def cmd_profiles(args: argparse.Namespace) -> int:
    if args.profile:
        print(yaml.safe_dump({args.profile: get_solution_profile(args.profile)}, sort_keys=False, allow_unicode=True))
        return 0
    print(yaml.safe_dump(SOLUTION_PROFILES, sort_keys=False, allow_unicode=True))
    return 0


def cmd_catalog(args: argparse.Namespace) -> int:
    catalogs = {"blocks": BUILDING_BLOCKS, "adapters": ADAPTER_CATALOG, "ui": UI_COMPONENTS}
    print(yaml.safe_dump(catalogs[args.kind], sort_keys=False, allow_unicode=True))
    return 0


def cmd_manifest(args: argparse.Namespace) -> int:
    manifest = load_solution_manifest(args.manifest)
    errors = validate_solution_manifest(manifest)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(yaml.safe_dump(materialize_solution_manifest(manifest), sort_keys=False, allow_unicode=True))
    return 0


def cmd_compose(args: argparse.Namespace) -> int:
    base = load_document(args.base)
    overlays = [load_document(path) for path in args.overlay]
    result = compose_domain_pack(base, *overlays)
    text = yaml.safe_dump(result, sort_keys=False, allow_unicode=True)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


def cmd_scaffold(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack) if args.domain_pack else None
    manifest = load_solution_manifest(args.manifest) if args.manifest else None
    if pack:
        errors = validate_domain_pack(pack)
        if errors and not args.allow_invalid:
            print("Domain Pack is invalid; scaffold aborted.")
            for error in errors:
                print(f"- {error}")
            return 1
    if manifest:
        manifest_errors = validate_solution_manifest(manifest)
        if manifest_errors:
            print("Solution Manifest is invalid; scaffold aborted.")
            for error in manifest_errors:
                print(f"- {error}")
            return 1
    root = scaffold_project(
        args.name,
        args.destination,
        domain_pack=pack,
        solution_profile=args.profile,
        solution_manifest=manifest,
        force=args.force,
    )
    print(root)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pyrax", description="Pyrax Framework CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    bootstrap = sub.add_parser("bootstrap", help="Create a discovery workspace for a new organization before a Domain Pack exists")
    bootstrap.add_argument("organization")
    bootstrap.add_argument("--destination", default=".")
    bootstrap.add_argument("--archetype", default="to-be-discovered")
    bootstrap.add_argument("--force", action="store_true")
    bootstrap.set_defaults(func=cmd_bootstrap)

    validate = sub.add_parser("validate", help="Validate a Domain Pack against canonical contracts")
    validate.add_argument("domain_pack")
    validate.add_argument("--schema")
    validate.set_defaults(func=cmd_validate)

    assess = sub.add_parser("assess", help="Assess production readiness for a valid Domain Pack")
    assess.add_argument("domain_pack")
    assess.set_defaults(func=cmd_assess)

    maturity = sub.add_parser("maturity", help="Assess Pyrax maturity level P0-P5 for a valid Domain Pack")
    maturity.add_argument("domain_pack")
    maturity.set_defaults(func=cmd_maturity)

    profiles = sub.add_parser("profiles", help="List or inspect reusable solution profiles")
    profiles.add_argument("profile", nargs="?")
    profiles.set_defaults(func=cmd_profiles)

    catalog = sub.add_parser("catalog", help="Inspect reusable blocks, adapters or UI components")
    catalog.add_argument("kind", choices=["blocks", "adapters", "ui"])
    catalog.set_defaults(func=cmd_catalog)

    manifest = sub.add_parser("manifest", help="Validate and materialize a Solution Manifest")
    manifest.add_argument("manifest")
    manifest.set_defaults(func=cmd_manifest)

    compose = sub.add_parser("compose", help="Compose a base Domain Pack with one or more overlays")
    compose.add_argument("base")
    compose.add_argument("--overlay", action="append", default=[], required=True)
    compose.add_argument("--output")
    compose.set_defaults(func=cmd_compose)

    scaffold = sub.add_parser("scaffold", help="Generate a new Pyrax-based solution skeleton")
    scaffold.add_argument("name")
    scaffold.add_argument("--destination", default=".")
    scaffold.add_argument("--domain-pack")
    scaffold.add_argument("--profile")
    scaffold.add_argument("--manifest")
    scaffold.add_argument("--allow-invalid", action="store_true")
    scaffold.add_argument("--force", action="store_true")
    scaffold.set_defaults(func=cmd_scaffold)
    return parser


def _input_path(args: argparse.Namespace) -> str | None:
    for name in ("domain_pack", "manifest", "base", "schema"):
        value = getattr(args, name, None)
        if value:
            return str(value)
    overlays = getattr(args, "overlay", None)
    if overlays:
        return str(overlays[0])
    return None


def _yaml_error_reason(exc: yaml.YAMLError) -> str:
    problem = getattr(exc, "problem", None)
    if problem:
        return str(problem).replace("\n", " ").strip()
    return str(exc).splitlines()[0].strip() or exc.__class__.__name__


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        exit_code = args.func(args)
    except FileNotFoundError as exc:
        path = exc.filename or _input_path(args) or str(exc)
        print(f"Error: file not found: {path}", file=sys.stderr)
        raise SystemExit(1) from None
    except yaml.YAMLError as exc:
        path = _input_path(args)
        location = f" in {path}" if path else ""
        print(f"Error: invalid YAML{location}: {_yaml_error_reason(exc)}", file=sys.stderr)
        raise SystemExit(1) from None
    except IsADirectoryError as exc:
        path = exc.filename or _input_path(args) or str(exc)
        print(f"Error: expected a file but found a directory: {path}", file=sys.stderr)
        raise SystemExit(1) from None
    except PermissionError as exc:
        path = exc.filename or _input_path(args) or str(exc)
        print(f"Error: permission denied: {path}", file=sys.stderr)
        raise SystemExit(1) from None
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
