#!/usr/bin/env python3
"""Initialize a repository with the pinned Kyd Runtime control layer."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


RUNTIME_VERSION = "KPR-V1"
INITIALIZER_ID = "kyd.bootstrap.init-project"
INITIALIZER_VERSION = "R1"
MANIFEST_RELATIVE_PATH = PurePosixPath(
    "tools/kyd-bootstrap/bootstrap_pack_r3.json"
)
AGENTS_TEMPLATE_RELATIVE_PATH = PurePosixPath(
    "tools/kyd-bootstrap/templates/AGENTS.md"
)
PROJECT_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")

STATIC_AUTHORITY_IDS = {
    "KPS-DP-R3",
    "KPS-DP-PLAYBOOK-R3",
    "RUNTIME-001",
}
REQUIRED_PINNED_ASSET_IDS = STATIC_AUTHORITY_IDS | {"KPR-V1-R1-VALIDATOR"}
PROTECTED_DIRECTORY_PATHS = {
    PurePosixPath("docs/delivery-protocol"),
    PurePosixPath("docs/kyd-runtime"),
    PurePosixPath("docs/tasks"),
}

RUNTIME_DATA_START = "<!-- KYD_RUNTIME_DATA_START -->"
RUNTIME_DATA_END = "<!-- KYD_RUNTIME_DATA_END -->"


class BootstrapError(RuntimeError):
    """A fail-closed Bootstrap initialization error."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install a pinned Kyd control layer into a target repository."
    )
    parser.add_argument(
        "--project-id",
        required=True,
        help="Stable project identifier (letters, digits, dot, underscore, hyphen).",
    )
    parser.add_argument(
        "--target",
        required=True,
        type=Path,
        help="Target repository path. Managed control paths must not already exist.",
    )
    return parser.parse_args(argv)


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def validate_project_id(project_id: str) -> str:
    if not PROJECT_ID_PATTERN.fullmatch(project_id):
        raise BootstrapError(
            "project ID must be 1-128 characters and contain only letters, "
            "digits, dot, underscore, or hyphen"
        )
    return project_id


def validate_relative_path(value: Any, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise BootstrapError(f"{field} must be a non-empty relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise BootstrapError(f"{field} is not a safe relative path: {value!r}")
    return path


def filesystem_path(root: Path, relative: PurePosixPath) -> Path:
    return root.joinpath(*relative.parts)


def load_source_manifest(source_root: Path) -> dict[str, Any]:
    path = filesystem_path(source_root, MANIFEST_RELATIVE_PATH)
    if not path.is_file():
        raise BootstrapError(f"source manifest is missing: {path}")
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BootstrapError(f"source manifest is invalid: {exc}") from exc

    if manifest.get("schema") != "kyd.bootstrap-pack.source-manifest.v1":
        raise BootstrapError("source manifest schema is not supported")
    resolution = manifest.get("resolution")
    if resolution != {
        "mode": "LOCAL_PINNED_ONLY",
        "network_allowed": False,
        "mutable_aliases": [],
    }:
        raise BootstrapError("source manifest must use local pinned-only resolution")
    return manifest


def verify_bootstrap_pack_source(
    source_root: Path, manifest: dict[str, Any]
) -> None:
    pack = manifest.get("bootstrap_pack")
    if not isinstance(pack, dict):
        raise BootstrapError("source manifest bootstrap_pack must be an object")
    source_relative = validate_relative_path(
        pack.get("source_path"), "bootstrap_pack.source_path"
    )
    expected_hash = pack.get("sha256")
    source_path = filesystem_path(source_root, source_relative)
    if not source_path.is_file():
        raise BootstrapError(f"Bootstrap Pack Authority is missing: {source_path}")
    actual_hash = sha256_file(source_path)
    if not isinstance(expected_hash, str) or actual_hash != expected_hash:
        raise BootstrapError(
            "Bootstrap Pack Authority SHA-256 mismatch: "
            f"expected={expected_hash!r} actual={actual_hash}"
        )


def load_pinned_assets(
    source_root: Path, manifest: dict[str, Any]
) -> tuple[list[dict[str, Any]], dict[PurePosixPath, bytes], dict[PurePosixPath, int]]:
    raw_assets = manifest.get("pinned_assets")
    if not isinstance(raw_assets, list):
        raise BootstrapError("source manifest pinned_assets must be a list")

    assets: list[dict[str, Any]] = []
    content_by_target: dict[PurePosixPath, bytes] = {}
    mode_by_target: dict[PurePosixPath, int] = {}
    seen_ids: set[str] = set()

    for item in raw_assets:
        if not isinstance(item, dict):
            raise BootstrapError("each pinned asset must be an object")
        asset_id = item.get("asset_id")
        if not isinstance(asset_id, str) or not asset_id or asset_id in seen_ids:
            raise BootstrapError(f"invalid or duplicate pinned asset ID: {asset_id!r}")
        seen_ids.add(asset_id)
        source_relative = validate_relative_path(
            item.get("source_path"), f"{asset_id}.source_path"
        )
        target_relative = validate_relative_path(
            item.get("target_path"), f"{asset_id}.target_path"
        )
        if target_relative in content_by_target:
            raise BootstrapError(f"duplicate pinned target path: {target_relative}")

        expected_hash = item.get("sha256")
        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            raise BootstrapError(f"{asset_id} does not have an exact SHA-256")
        source_path = filesystem_path(source_root, source_relative)
        if not source_path.is_file():
            raise BootstrapError(f"pinned source is missing: {source_path}")
        content = source_path.read_bytes()
        actual_hash = sha256_bytes(content)
        if actual_hash != expected_hash:
            raise BootstrapError(
                f"{asset_id} source SHA-256 mismatch: "
                f"expected={expected_hash} actual={actual_hash}"
            )

        normalized = dict(item)
        normalized["source_path"] = source_relative.as_posix()
        normalized["target_path"] = target_relative.as_posix()
        assets.append(normalized)
        content_by_target[target_relative] = content
        mode_by_target[target_relative] = stat.S_IMODE(source_path.stat().st_mode)

    missing = REQUIRED_PINNED_ASSET_IDS - seen_ids
    if missing:
        raise BootstrapError(f"source manifest is missing pinned assets: {sorted(missing)}")
    return assets, content_by_target, mode_by_target


def markdown_runtime_document(
    title: str, data: dict[str, Any], note: str
) -> bytes:
    text = (
        f"# {title}\n\n"
        f"{RUNTIME_DATA_START}\n"
        f"{json.dumps(data, indent=2, ensure_ascii=False)}\n"
        f"{RUNTIME_DATA_END}\n\n"
        f"{note}\n"
    )
    return text.encode("utf-8")


def project_index_data(
    project_id: str, assets: list[dict[str, Any]]
) -> dict[str, Any]:
    static_names = {
        "KPS-DP-R3": "Kyd Delivery Protocol R3",
        "KPS-DP-PLAYBOOK-R3": "Kyd Delivery Protocol Execution Playbook R3",
        "RUNTIME-001": "Kyd Project Runtime V1 Minimal Spec R1",
    }
    static_purposes = {
        "KPS-DP-R3": "Frozen generic project delivery lifecycle Authority",
        "KPS-DP-PLAYBOOK-R3": "Frozen agent-neutral delivery execution playbook",
        "RUNTIME-001": "Frozen deterministic repository execution Runtime",
    }
    authorities: list[dict[str, Any]] = []
    for asset in assets:
        asset_id = asset["asset_id"]
        if asset_id not in STATIC_AUTHORITY_IDS:
            continue
        authorities.append(
            {
                "authority_id": asset_id,
                "area": "runtime"
                if asset_id == "RUNTIME-001"
                else "delivery-protocol",
                "name": static_names[asset_id],
                "path": asset["target_path"],
                "kind": "AUTHORITY",
                "version": asset["version"],
                "status": "FROZEN",
                "sha256": asset["sha256"],
                "purpose": static_purposes[asset_id],
            }
        )

    authorities.extend(
        [
            {
                "authority_id": "KYD-CURRENT-STATE",
                "area": "execution",
                "name": "Current State",
                "path": "docs/CURRENT_STATE.md",
                "kind": "AUTHORITY",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Current repository execution truth and task pointer",
            },
            {
                "authority_id": "KYD-FEATURE-MATRIX",
                "area": "product",
                "name": "Feature Matrix",
                "path": "docs/product/FEATURE_MATRIX.md",
                "kind": "AUTHORITY",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Project feature state initialized without product claims",
            },
            {
                "authority_id": "KYD-TASK-INDEX",
                "area": "execution",
                "name": "Task Index",
                "path": "docs/tasks/TASK_INDEX.md",
                "kind": "AUTHORITY",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Registered project task contracts and dependency state",
            },
            {
                "authority_id": "KYD-CURRENT-TASK",
                "area": "execution",
                "name": "Current Task",
                "path": "docs/tasks/CURRENT_TASK.md",
                "kind": "AUTHORITY",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Current task boundary or canonical no-task sentinel",
            },
            {
                "authority_id": "KYD-IMPLEMENTATION-TRACE",
                "area": "execution",
                "name": "Implementation Trace",
                "path": "docs/execution/IMPLEMENTATION_TRACE.md",
                "kind": "EVIDENCE",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Project implementation and verification trace evidence",
            },
            {
                "authority_id": "KYD-BOOTSTRAP-MANIFEST",
                "area": "bootstrap",
                "name": "Bootstrap Manifest",
                "path": "KYD_BOOTSTRAP_MANIFEST.json",
                "kind": "EVIDENCE",
                "version": "v1",
                "status": "ACTIVE",
                "sha256": None,
                "purpose": "Pinned Bootstrap provenance and validation state",
            },
        ]
    )
    return {
        "runtime_schema": "kyd.project-index.v1",
        "project": project_id,
        "runtime_version": RUNTIME_VERSION,
        "authorities": authorities,
    }


def dynamic_outputs(
    project_id: str,
    assets: list[dict[str, Any]],
    source_manifest: dict[str, Any],
    agents_template: bytes,
    initialized_at: str,
) -> dict[PurePosixPath, bytes]:
    current_state = {
        "runtime_schema": "kyd.current-state.v1",
        "project": project_id,
        "starter_version": "NONE",
        "delivery_profile": "UNSELECTED",
        "runtime_version": RUNTIME_VERSION,
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
    task_index = {
        "runtime_schema": "kyd.task-index.v1",
        "project": project_id,
        "runtime_version": RUNTIME_VERSION,
        "tasks": [],
    }
    current_task_sentinel = {
        "runtime_schema": "kyd.current-task.v1",
        "project": project_id,
        "runtime_version": RUNTIME_VERSION,
    }
    feature_matrix = {
        "runtime_schema": "kyd.feature-matrix.v1",
        "project": project_id,
        "runtime_version": RUNTIME_VERSION,
        "features": [],
    }
    implementation_trace = {
        "runtime_schema": "kyd.implementation-trace.v1",
        "project": project_id,
        "runtime_version": RUNTIME_VERSION,
        "traces": [],
    }

    bootstrap_pack = source_manifest["bootstrap_pack"]
    provenance = {
        "schema": "kyd.bootstrap-manifest.v1",
        "bootstrap_pack": {
            "authority_id": bootstrap_pack["authority_id"],
            "version": bootstrap_pack["version"],
            "sha256": bootstrap_pack["sha256"],
            "source_manifest": MANIFEST_RELATIVE_PATH.as_posix(),
        },
        "initialized_at": initialized_at,
        "project_id": project_id,
        "pinned_assets": [
            {
                "asset_id": asset["asset_id"],
                "version": asset["version"],
                "target_path": asset["target_path"],
                "sha256": asset["sha256"],
            }
            for asset in assets
        ],
        "initializer": {
            "identity": INITIALIZER_ID,
            "version": INITIALIZER_VERSION,
            "path": "tools/kyd-bootstrap/init_project.py",
        },
        "validation_state": "PENDING",
    }

    return {
        PurePosixPath("AGENTS.md"): agents_template,
        PurePosixPath("docs/PROJECT_INDEX.md"): markdown_runtime_document(
            "PROJECT_INDEX",
            project_index_data(project_id, assets),
            "This single-level index routes the pinned control Authorities and "
            "project-local Runtime state.",
        ),
        PurePosixPath("docs/CURRENT_STATE.md"): markdown_runtime_document(
            "CURRENT_STATE",
            current_state,
            "No task is selected. Implementation execution is not eligible.",
        ),
        PurePosixPath("docs/tasks/TASK_INDEX.md"): markdown_runtime_document(
            "TASK_INDEX",
            task_index,
            "No project tasks are registered.",
        ),
        PurePosixPath("docs/tasks/CURRENT_TASK.md"): markdown_runtime_document(
            "CURRENT_TASK",
            current_task_sentinel,
            "No current task is selected. This is not an executable task contract.",
        ),
        PurePosixPath("docs/product/FEATURE_MATRIX.md"): markdown_runtime_document(
            "FEATURE_MATRIX",
            feature_matrix,
            "No project features are registered or claimed as implemented.",
        ),
        PurePosixPath(
            "docs/execution/IMPLEMENTATION_TRACE.md"
        ): markdown_runtime_document(
            "IMPLEMENTATION_TRACE",
            implementation_trace,
            "No implementation or verification traces are registered.",
        ),
        PurePosixPath("KYD_BOOTSTRAP_MANIFEST.json"): (
            json.dumps(provenance, indent=2, ensure_ascii=False) + "\n"
        ).encode("utf-8"),
    }


def validate_output_set(
    outputs: dict[PurePosixPath, bytes], manifest: dict[str, Any]
) -> None:
    raw_targets = manifest.get("generated_target_paths")
    if not isinstance(raw_targets, list):
        raise BootstrapError("source manifest generated_target_paths must be a list")
    declared = {
        validate_relative_path(value, "generated_target_paths entry")
        for value in raw_targets
    }
    if len(declared) != len(raw_targets):
        raise BootstrapError("source manifest has duplicate generated target paths")
    actual = set(outputs)
    if actual != declared:
        missing = sorted(path.as_posix() for path in declared - actual)
        extra = sorted(path.as_posix() for path in actual - declared)
        raise BootstrapError(
            f"generated target set mismatch: missing={missing} extra={extra}"
        )


def collision_paths(target: Path, outputs: dict[PurePosixPath, bytes]) -> list[str]:
    collisions: set[str] = set()
    if target.exists() and not target.is_dir():
        return [str(target)]
    for relative in set(outputs) | PROTECTED_DIRECTORY_PATHS:
        path = filesystem_path(target, relative)
        if path.exists() or path.is_symlink():
            collisions.add(relative.as_posix())
        parent = path.parent
        while parent != target and target in parent.parents:
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                collisions.add(parent.relative_to(target).as_posix())
            parent = parent.parent
    return sorted(collisions)


def ensure_directory(path: Path, created_directories: list[Path]) -> None:
    if path.exists():
        if not path.is_dir() or path.is_symlink():
            raise BootstrapError(f"required directory path is unsafe: {path}")
        return
    ensure_directory(path.parent, created_directories)
    path.mkdir()
    created_directories.append(path)


def rollback(created_files: list[Path], created_directories: list[Path]) -> None:
    for path in reversed(created_files):
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    for path in reversed(created_directories):
        try:
            path.rmdir()
        except (FileNotFoundError, OSError):
            pass


def write_outputs(
    target: Path,
    outputs: dict[PurePosixPath, bytes],
    modes: dict[PurePosixPath, int],
) -> None:
    collisions = collision_paths(target, outputs)
    if collisions:
        raise BootstrapError(f"managed control paths already exist: {collisions}")

    created_files: list[Path] = []
    created_directories: list[Path] = []
    try:
        ensure_directory(target, created_directories)
        second_check = collision_paths(target, outputs)
        if second_check:
            raise BootstrapError(
                f"managed control paths appeared during preflight: {second_check}"
            )
        for relative in sorted(outputs, key=lambda item: item.as_posix()):
            destination = filesystem_path(target, relative)
            ensure_directory(destination.parent, created_directories)
            with destination.open("xb") as handle:
                created_files.append(destination)
                handle.write(outputs[relative])
            if relative in modes:
                destination.chmod(modes[relative])

        for relative, expected_content in outputs.items():
            destination = filesystem_path(target, relative)
            if sha256_file(destination) != sha256_bytes(expected_content):
                raise BootstrapError(f"post-write SHA-256 mismatch: {relative}")
    except BaseException:
        rollback(created_files, created_directories)
        raise


def build_initialization(
    source_root: Path, project_id: str, target: Path
) -> tuple[dict[PurePosixPath, bytes], dict[PurePosixPath, int]]:
    manifest = load_source_manifest(source_root)
    verify_bootstrap_pack_source(source_root, manifest)
    assets, outputs, modes = load_pinned_assets(source_root, manifest)

    template_path = filesystem_path(source_root, AGENTS_TEMPLATE_RELATIVE_PATH)
    if not template_path.is_file():
        raise BootstrapError(f"AGENTS template is missing: {template_path}")
    agents_template = template_path.read_bytes()

    initialized_at = (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )
    for relative, content in dynamic_outputs(
        project_id, assets, manifest, agents_template, initialized_at
    ).items():
        if relative in outputs:
            raise BootstrapError(f"generated target collides with pinned asset: {relative}")
        outputs[relative] = content

    validate_output_set(outputs, manifest)
    return outputs, modes


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        project_id = validate_project_id(args.project_id)
        source_root = Path(__file__).resolve().parents[2]
        target = args.target.expanduser().resolve()
        if target == Path(target.anchor):
            raise BootstrapError("target repository path cannot be a filesystem root")
        outputs, modes = build_initialization(source_root, project_id, target)
        write_outputs(target, outputs, modes)
    except (BootstrapError, OSError) as exc:
        print("KYD_BOOTSTRAP_INIT: FAIL", file=sys.stderr)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print("KYD_BOOTSTRAP_INIT: COMPLETE")
    print(f"PROJECT_ID = {project_id}")
    print(f"TARGET = {target}")
    print("VALIDATION_STATE = PENDING")
    return 0


if __name__ == "__main__":
    sys.exit(main())
