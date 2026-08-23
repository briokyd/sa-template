#!/usr/bin/env python3
"""Validate a newly initialized Kyd project without duplicating Runtime rules."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


RUNTIME_DATA_START = "<!-- KYD_RUNTIME_DATA_START -->"
RUNTIME_DATA_END = "<!-- KYD_RUNTIME_DATA_END -->"

REQUIRED_PATHS = (
    "AGENTS.md",
    "KYD_BOOTSTRAP_MANIFEST.json",
    "docs/PROJECT_INDEX.md",
    "docs/CURRENT_STATE.md",
    "docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_R3.md",
    "docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_EXECUTION_PLAYBOOK_R3.md",
    "docs/kyd-runtime/Kyd_Project_Runtime_V1_Minimal_Spec_R1.md",
    "docs/product/FEATURE_MATRIX.md",
    "docs/tasks/TASK_INDEX.md",
    "docs/tasks/CURRENT_TASK.md",
    "docs/execution/IMPLEMENTATION_TRACE.md",
    "tools/kyd_runtime_validate.py",
    "tools/kyd_bootstrap_validate.py",
)

STATIC_ENTRIES = {
    "KPS-DP-R3": {
        "authority_id": "KPS-DP-R3",
        "area": "execution",
        "name": "Kyd Delivery Protocol R3",
        "path": "docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_R3.md",
        "kind": "AUTHORITY",
        "version": "R3",
        "status": "FROZEN",
        "sha256": "5dddfe4baf827be59e3b730a45642503d74b5913131606f2b60f6a2d4ec7bea0",
        "purpose": "Frozen project lifecycle, Gate, freeze, release, and closeout rules",
    },
    "KPS-DP-PLAYBOOK-R3": {
        "authority_id": "KPS-DP-PLAYBOOK-R3",
        "area": "execution",
        "name": "Kyd Delivery Protocol Execution Playbook R3",
        "path": "docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_EXECUTION_PLAYBOOK_R3.md",
        "kind": "AUTHORITY",
        "version": "R3",
        "status": "FROZEN",
        "sha256": "e4039755860173a5bfb409f737710be0b9ad0e8a5654e22329ff23970372a02c",
        "purpose": "Frozen operational role, review, registration, and evidence procedures",
    },
    "RUNTIME-001": {
        "authority_id": "RUNTIME-001",
        "area": "execution",
        "name": "Kyd Project Runtime V1 R1",
        "path": "docs/kyd-runtime/Kyd_Project_Runtime_V1_Minimal_Spec_R1.md",
        "kind": "AUTHORITY",
        "version": "R1",
        "status": "FROZEN",
        "sha256": "fe78677830b5a24c0eeea43a70c6fc266687f9f37cec1e747ad679ebaa12e10a",
        "purpose": "Frozen repository execution eligibility, Authority routing, dependency, scope, and verification rules",
    },
}

DYNAMIC_ENTRIES = {
    "KYD-CURRENT-STATE": {
        "authority_id": "KYD-CURRENT-STATE",
        "area": "execution",
        "name": "Current State",
        "path": "docs/CURRENT_STATE.md",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Current repository execution truth and task pointer",
    },
    "KYD-FEATURE-MATRIX": {
        "authority_id": "KYD-FEATURE-MATRIX",
        "area": "product",
        "name": "Feature Matrix",
        "path": "docs/product/FEATURE_MATRIX.md",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Project feature state initialized without product claims",
    },
    "KYD-TASK-INDEX": {
        "authority_id": "KYD-TASK-INDEX",
        "area": "execution",
        "name": "Task Index",
        "path": "docs/tasks/TASK_INDEX.md",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Registered project task contracts and dependency state",
    },
    "KYD-CURRENT-TASK": {
        "authority_id": "KYD-CURRENT-TASK",
        "area": "execution",
        "name": "Current Task",
        "path": "docs/tasks/CURRENT_TASK.md",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Current task boundary or canonical no-task sentinel",
    },
    "KYD-IMPLEMENTATION-TRACE": {
        "authority_id": "KYD-IMPLEMENTATION-TRACE",
        "area": "execution",
        "name": "Implementation Trace",
        "path": "docs/execution/IMPLEMENTATION_TRACE.md",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Project implementation and verification trace evidence",
    },
    "KYD-BOOTSTRAP-MANIFEST": {
        "authority_id": "KYD-BOOTSTRAP-MANIFEST",
        "area": "bootstrap",
        "name": "Bootstrap Manifest",
        "path": "KYD_BOOTSTRAP_MANIFEST.json",
        "kind": "EVIDENCE",
        "version": "v1",
        "status": "ACTIVE",
        "sha256": "",
        "purpose": "Pinned Bootstrap provenance and validation state",
    },
}

PINNED_ASSETS = {
    "KPS-DP-R3": ("R3", STATIC_ENTRIES["KPS-DP-R3"]["path"], STATIC_ENTRIES["KPS-DP-R3"]["sha256"]),
    "KPS-DP-PLAYBOOK-R3": ("R3", STATIC_ENTRIES["KPS-DP-PLAYBOOK-R3"]["path"], STATIC_ENTRIES["KPS-DP-PLAYBOOK-R3"]["sha256"]),
    "RUNTIME-001": ("R1", STATIC_ENTRIES["RUNTIME-001"]["path"], STATIC_ENTRIES["RUNTIME-001"]["sha256"]),
    "KPR-V1-R1-VALIDATOR": (
        "R1",
        "tools/kyd_runtime_validate.py",
        "aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7",
    ),
}

ACTIVE_TASK_FIELDS = {
    "task_id",
    "status",
    "authority_inputs",
    "depends_on",
    "touches",
    "allowed_changes",
    "forbidden_changes",
    "acceptance",
    "verification",
    "contract",
}

DYNAMIC_SCAN_PATHS = (
    "AGENTS.md",
    "KYD_BOOTSTRAP_MANIFEST.json",
    "docs/PROJECT_INDEX.md",
    "docs/CURRENT_STATE.md",
    "docs/product/FEATURE_MATRIX.md",
    "docs/tasks/TASK_INDEX.md",
    "docs/tasks/CURRENT_TASK.md",
    "docs/execution/IMPLEMENTATION_TRACE.md",
)


class ValidationError(RuntimeError):
    """A fail-closed Bootstrap validation error."""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"expected a JSON object at {path}")
    return value


def load_runtime_document(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationError(f"cannot read Runtime document {path}: {exc}") from exc
    pattern = re.escape(RUNTIME_DATA_START) + r"\s*(.*?)\s*" + re.escape(RUNTIME_DATA_END)
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        raise ValidationError(f"Runtime data block is missing: {path}")
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Runtime data block is invalid at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"Runtime data block must be an object: {path}")
    return value


def validate_required_structure(root: Path) -> None:
    missing = [relative for relative in REQUIRED_PATHS if not (root / relative).is_file()]
    if missing:
        raise ValidationError(f"missing mandatory Bootstrap files: {missing}")


def validate_manifest(root: Path) -> dict[str, Any]:
    manifest = load_json(root / "KYD_BOOTSTRAP_MANIFEST.json")
    if manifest.get("schema") != "kyd.bootstrap-manifest.v1":
        raise ValidationError("Bootstrap manifest schema is invalid")
    if manifest.get("validation_state") not in {"PENDING", "PASS"}:
        raise ValidationError("Bootstrap manifest validation_state must be PENDING or PASS")
    pack = manifest.get("bootstrap_pack")
    if not isinstance(pack, dict) or {
        "authority_id": pack.get("authority_id"),
        "version": pack.get("version"),
        "sha256": pack.get("sha256"),
    } != {
        "authority_id": "KPS-BS-PACK-SPEC-R3",
        "version": "R3",
        "sha256": "3d86588d1f0f2d8c0b94279540220558166a5ca6fee8b27b2929e7b12d316caa",
    }:
        raise ValidationError("Bootstrap manifest pack identity is not pinned to R3")
    initializer = manifest.get("initializer")
    if not isinstance(initializer, dict) or initializer.get("identity") != "kyd.bootstrap.init-project":
        raise ValidationError("Bootstrap manifest initializer identity is invalid")
    if not isinstance(manifest.get("project_id"), str) or not manifest["project_id"]:
        raise ValidationError("Bootstrap manifest project_id is missing")

    raw_assets = manifest.get("pinned_assets")
    if not isinstance(raw_assets, list):
        raise ValidationError("Bootstrap manifest pinned_assets must be a list")
    assets: dict[str, dict[str, Any]] = {}
    for item in raw_assets:
        if not isinstance(item, dict):
            raise ValidationError("Bootstrap manifest pinned asset is not an object")
        asset_id = item.get("asset_id")
        if not isinstance(asset_id, str) or asset_id in assets:
            raise ValidationError(f"invalid or duplicate pinned asset ID: {asset_id!r}")
        assets[asset_id] = item

    expected_ids = set(PINNED_ASSETS) | {"KPS-BS-R3-VALIDATOR"}
    if set(assets) != expected_ids:
        raise ValidationError(
            f"Bootstrap manifest pinned asset IDs mismatch: expected={sorted(expected_ids)} actual={sorted(assets)}"
        )
    for asset_id, (version, target_path, expected_hash) in PINNED_ASSETS.items():
        expected = {
            "asset_id": asset_id,
            "version": version,
            "target_path": target_path,
            "sha256": expected_hash,
        }
        if assets[asset_id] != expected:
            raise ValidationError(f"Bootstrap manifest metadata mismatch: {asset_id}")
    validator_asset = assets["KPS-BS-R3-VALIDATOR"]
    if validator_asset.get("version") != "R3" or validator_asset.get("target_path") != "tools/kyd_bootstrap_validate.py":
        raise ValidationError("Bootstrap validator manifest metadata is invalid")
    validator_hash = validator_asset.get("sha256")
    if not isinstance(validator_hash, str) or len(validator_hash) != 64:
        raise ValidationError("Bootstrap validator manifest hash is invalid")

    for asset_id, item in assets.items():
        path = root / item["target_path"]
        actual = sha256_file(path)
        if actual != item["sha256"]:
            raise ValidationError(
                f"pinned asset SHA-256 mismatch for {asset_id}: expected={item['sha256']} actual={actual}"
            )
    return manifest


def validate_project_index(root: Path, project_id: str) -> None:
    index = load_runtime_document(root / "docs/PROJECT_INDEX.md")
    if index.get("runtime_schema") != "kyd.project-index.v1" or index.get("project") != project_id:
        raise ValidationError("PROJECT_INDEX identity does not match Bootstrap manifest")
    raw_entries = index.get("authorities")
    if not isinstance(raw_entries, list):
        raise ValidationError("PROJECT_INDEX authorities must be a list")
    entries: dict[str, dict[str, Any]] = {}
    for item in raw_entries:
        if not isinstance(item, dict):
            raise ValidationError("PROJECT_INDEX entry is not an object")
        authority_id = item.get("authority_id")
        if not isinstance(authority_id, str) or authority_id in entries:
            raise ValidationError(f"duplicate or invalid PROJECT_INDEX ID: {authority_id!r}")
        entries[authority_id] = item
    expected = {**STATIC_ENTRIES, **DYNAMIC_ENTRIES}
    if set(entries) != set(expected):
        raise ValidationError(
            f"PROJECT_INDEX routes mismatch: expected={sorted(expected)} actual={sorted(entries)}"
        )
    for authority_id, metadata in expected.items():
        if entries[authority_id] != metadata:
            raise ValidationError(f"PROJECT_INDEX metadata mismatch: {authority_id}")
        if not (root / metadata["path"]).is_file():
            raise ValidationError(f"PROJECT_INDEX route does not resolve: {authority_id}")


def validate_zero_state(root: Path, project_id: str) -> None:
    state = load_runtime_document(root / "docs/CURRENT_STATE.md")
    tasks = load_runtime_document(root / "docs/tasks/TASK_INDEX.md")
    current_task = load_runtime_document(root / "docs/tasks/CURRENT_TASK.md")
    features = load_runtime_document(root / "docs/product/FEATURE_MATRIX.md")
    traces = load_runtime_document(root / "docs/execution/IMPLEMENTATION_TRACE.md")
    expected_state = {
        "runtime_schema": "kyd.current-state.v1",
        "project": project_id,
        "starter_version": "NONE",
        "delivery_profile": "UNSELECTED",
        "runtime_version": "KPR-V1",
        "product_freeze_version": "NONE",
        "ui_freeze_version": "NONE",
        "current_phase": "PROJECT_BOOTSTRAP",
        "current_task": "NONE",
        "last_verified_commit": None,
        "blocked": {"status": False, "blocker_ids": []},
        "gates": [],
        "known_deviations": [],
        "next_task": "NONE",
        "release_status": "NOT_READY",
    }
    if state != expected_state:
        raise ValidationError("CURRENT_STATE is not the canonical clean zero-state")
    expected_core = {
        "project": project_id,
        "runtime_version": "KPR-V1",
    }
    if tasks != {
        "runtime_schema": "kyd.task-index.v1",
        **expected_core,
        "tasks": [],
    }:
        raise ValidationError("TASK_INDEX is not the canonical empty task state")
    unsafe_fields = ACTIVE_TASK_FIELDS.intersection(current_task)
    if unsafe_fields:
        raise ValidationError(
            f"CURRENT_TASK no-task sentinel contains active task fields: {sorted(unsafe_fields)}"
        )
    if current_task != {
        "runtime_schema": "kyd.current-task.v1",
        **expected_core,
    }:
        raise ValidationError("CURRENT_TASK no-task sentinel contains non-canonical fields")
    if features != {
        "runtime_schema": "kyd.feature-matrix.v1",
        **expected_core,
        "features": [],
    }:
        raise ValidationError("FEATURE_MATRIX is not the canonical empty feature state")
    if traces != {
        "runtime_schema": "kyd.implementation-trace.v1",
        **expected_core,
        "traces": [],
    }:
        raise ValidationError("IMPLEMENTATION_TRACE is not the canonical empty trace state")


def validate_agents(root: Path) -> None:
    text = (root / "AGENTS.md").read_text(encoding="utf-8")
    required = (
        "1. AGENTS.md",
        "2. docs/PROJECT_INDEX.md",
        "3. docs/CURRENT_STATE.md",
        "4. docs/tasks/CURRENT_TASK.md",
        "Task-declared Authority inputs",
        "Runtime validation and execution-eligibility",
        "Repository-controlled Authority takes precedence over chat or model memory",
        "Planner Memory and chat history are not Runtime Authority",
        "Deny-by-default",
        "Dependencies must be explicit",
        "BLOCKED",
        "Do not silently expand task scope",
        "Do not invent product, design, business, or acceptance semantics",
        "Frozen Authority must not be silently modified",
        "IMPLEMENTED != VERIFIED",
        "Replacement executors recover state",
    )
    missing = [clause for clause in required if clause not in text]
    if missing:
        raise ValidationError(f"AGENTS entry contract clauses are missing: {missing}")
    prohibited = ("AUD-", "STS-", "sa-template", "Codex", "ChatGPT", "OpenAI", "Anthropic", "Claude", "Gemini")
    found = [value for value in prohibited if value.casefold() in text.casefold()]
    if found:
        raise ValidationError(f"AGENTS contains non-neutral or project-specific bindings: {found}")


def validate_no_stale_state(root: Path) -> None:
    prohibited = ("AUD-", "STS-", "sa-template")
    for relative in DYNAMIC_SCAN_PATHS:
        text = (root / relative).read_text(encoding="utf-8")
        found = [value for value in prohibited if value.casefold() in text.casefold()]
        if found:
            raise ValidationError(f"stale project-state marker in {relative}: {found}")


def run_runtime_validation(root: Path) -> None:
    validator = root / "tools/kyd_runtime_validate.py"
    for mode in ("structure", "closeout"):
        result = subprocess.run(
            [sys.executable, str(validator), "--root", ".", "--mode", mode],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0 or "KYD_RUNTIME_VALIDATE: PASS" not in result.stdout:
            detail = (result.stdout + result.stderr).strip()
            raise ValidationError(f"Runtime {mode} validation failed: {detail}")
    execution = subprocess.run(
        [sys.executable, str(validator), "--root", ".", "--mode", "execution"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    output = execution.stdout + execution.stderr
    expected = "[TASK_GAP] execution mode requires current_task"
    if execution.returncode == 0 or expected not in output or "EXECUTION_ALLOWED = FALSE" not in output:
        raise ValidationError(f"Runtime execution did not reject the canonical zero-state as expected: {output.strip()}")


def validate(root: Path) -> None:
    validate_required_structure(root)
    manifest = validate_manifest(root)
    project_id = manifest["project_id"]
    validate_project_index(root, project_id)
    validate_zero_state(root, project_id)
    validate_agents(root)
    validate_no_stale_state(root)
    run_runtime_validation(root)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a bootstrapped Kyd project.")
    parser.add_argument("--root", type=Path, default=Path("."), help="Generated project root")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.expanduser().resolve()
    try:
        validate(root)
    except (ValidationError, OSError) as exc:
        print("KYD_BOOTSTRAP_VALIDATE: FAIL", file=sys.stderr)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print("KYD_BOOTSTRAP_VALIDATE: PASS")
    print("RUNTIME_STRUCTURE = PASS")
    print("RUNTIME_CLOSEOUT = PASS")
    print("RUNTIME_EXECUTION_ELIGIBLE = FALSE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
