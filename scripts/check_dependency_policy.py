#!/usr/bin/env python3
"""Fail if Cargo resolves any package outside the VEF workspace."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        ["cargo", "metadata", "--format-version", "1", "--locked"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    metadata = json.loads(result.stdout)
    workspace_ids = set(metadata["workspace_members"])
    failures: list[str] = []
    for package in metadata["packages"]:
        package_id = package["id"]
        if package_id not in workspace_ids or package.get("source") is not None:
            failures.append(f"{package['name']} {package['version']} ({package.get('source')})")
        for dependency in package["dependencies"]:
            if dependency.get("source") is not None:
                failures.append(
                    f"{package['name']} depends on external {dependency['name']}"
                )
    if failures:
        print("third-party Cargo packages are forbidden:", file=sys.stderr)
        for failure in sorted(set(failures)):
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("dependency policy: workspace path packages only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
