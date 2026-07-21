#!/usr/bin/env python3
"""Check that the compact and detailed plans cover exactly v0.1.0..v0.160.0."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def versions(pattern: str, text: str) -> list[int]:
    return [int(value) for value in re.findall(pattern, text, flags=re.MULTILINE)]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    detailed = (root / "docs/RELEASE_PLAN.md").read_text(encoding="utf-8")
    compact = (root / "docs/VERSION_PLAN.md").read_text(encoding="utf-8")
    expected = list(range(1, 161))
    detailed_versions = versions(r"^### v0\.(\d+)\.0 — ", detailed)
    compact_versions = versions(r"^\| `0\.(\d+)\.0` \|", compact)
    failures: list[str] = []
    if detailed_versions != expected:
        failures.append("detailed plan does not cover v0.1.0 through v0.160.0 exactly")
    if compact_versions != expected:
        failures.append("version index does not cover v0.1.0 through v0.160.0 exactly")
    for heading in ("Goal", "Deliverables", "Verification", "Exit criteria"):
        if detailed.count(f"#### {heading}") != 160:
            failures.append(f"expected 160 {heading} sections")
    if detailed.count("implementation stop reached. Run pentest for this exact commit.") != 162:
        failures.append("expected one pentest stop for each milestone and release candidate")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("release plan: 160 detailed milestones plus two release candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
