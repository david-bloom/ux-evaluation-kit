#!/usr/bin/env python3
"""Dependency-free structural validator for UX Evaluation Kit artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/OPERATING_MODEL.md",
    "docs/ROLES.md",
    "docs/RUN_LIFECYCLE.md",
    "docs/EVIDENCE_MODEL.md",
    "docs/LENS_GUIDE.md",
    "prompts/UNIVERSAL_SESSION_PROMPT.md",
    "prompts/RUN_COORDINATOR.md",
    "prompts/EVALUATOR.md",
    "prompts/SKEPTIC.md",
    "prompts/SYNTHESIZER.md",
    "prompts/REPORTER.md",
    "config/lenses.json",
    "config/run-modes.json",
    "schemas/run-charter.schema.json",
    "schemas/ux-finding.schema.json",
    "schemas/synthesis.schema.json",
]

BASELINE_LENSES = {
    "cognitive_walkthrough",
    "interaction_state",
    "error_recovery",
    "core_heuristics",
    "accessibility_baseline",
}


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return None


def require_keys(data: dict, keys: set[str], label: str, errors: list[str]):
    missing = sorted(keys - set(data))
    if missing:
        errors.append(f"{label}: missing keys {', '.join(missing)}")


def validate_registry(errors: list[str]) -> set[str]:
    path = ROOT / "config/lenses.json"
    data = load_json(path, errors)
    if not data:
        return set()
    ids = [lens.get("id") for lens in data.get("lenses", [])]
    if len(ids) != len(set(ids)):
        errors.append("config/lenses.json: lens IDs must be unique")
    available = {item for item in ids if isinstance(item, str)}
    missing_baseline = BASELINE_LENSES - available
    if missing_baseline:
        errors.append(f"config/lenses.json: missing baseline lenses {sorted(missing_baseline)}")
    required = {"id", "name", "tier", "primary_question", "applies_when", "required_context", "procedure", "allowed_claims", "forbidden_claims", "output_types"}
    for index, lens in enumerate(data.get("lenses", [])):
        require_keys(lens, required, f"config/lenses.json lenses[{index}]", errors)
    return available


def validate_charter(path: Path, lens_ids: set[str], errors: list[str]):
    data = load_json(path, errors)
    if not data:
        return
    required = {"schema_version", "run_id", "status", "mode", "target", "boundaries", "users", "task", "usability_priorities", "lenses", "execution", "evidence", "excluded"}
    require_keys(data, required, str(path.relative_to(ROOT)), errors)
    selected = set(data.get("lenses", {}).get("baseline", [])) | set(data.get("lenses", {}).get("specialist", []))
    unknown = selected - lens_ids
    if unknown:
        errors.append(f"{path.relative_to(ROOT)}: unknown lens IDs {sorted(unknown)}")
    evidence = data.get("evidence", {})
    if evidence.get("distinguish_basis") is not True or evidence.get("preserve_disagreement") is not True:
        errors.append(f"{path.relative_to(ROOT)}: evidence safeguards must be true")


def validate_finding(path: Path, lens_ids: set[str], errors: list[str]):
    data = load_json(path, errors)
    if not data:
        return
    required = {"schema_version", "finding_id", "run_id", "claim", "user_model_ids", "task_id", "lens_ids", "evidence_basis", "evidence", "impact", "confidence", "alternative_interpretations", "validation_needed", "skeptic_review"}
    require_keys(data, required, str(path.relative_to(ROOT)), errors)
    unknown = set(data.get("lens_ids", [])) - lens_ids
    if unknown:
        errors.append(f"{path.relative_to(ROOT)}: unknown lens IDs {sorted(unknown)}")
    disposition = data.get("skeptic_review", {}).get("disposition")
    allowed = {"pending", "retain", "weaken", "reclassify_as_hypothesis", "reject"}
    if disposition not in allowed:
        errors.append(f"{path.relative_to(ROOT)}: invalid Skeptic disposition {disposition!r}")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in sorted(ROOT.rglob("*.json")):
        load_json(path, errors)

    lens_ids = validate_registry(errors)
    for path in sorted(ROOT.glob("examples/runs/*/run-charter.json")) + sorted(ROOT.glob("runs/*/run-charter.json")):
        validate_charter(path, lens_ids, errors)
    for path in sorted(ROOT.glob("examples/runs/*/findings/*.json")) + sorted(ROOT.glob("runs/*/findings/*.json")):
        validate_finding(path, lens_ids, errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("UX Evaluation Kit validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

