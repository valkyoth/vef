#!/usr/bin/env python3
"""Check that the compact and detailed plans cover exactly v0.1.0..v0.193.0."""

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
    expected = list(range(1, 194))
    detailed_versions = versions(r"^### v0\.(\d+)\.0 — ", detailed)
    compact_versions = versions(r"^\| `0\.(\d+)\.0` \|", compact)
    failures: list[str] = []
    if detailed_versions != expected:
        failures.append("detailed plan does not cover v0.1.0 through v0.193.0 exactly")
    if compact_versions != expected:
        failures.append("version index does not cover v0.1.0 through v0.193.0 exactly")
    for heading in ("Goal", "Deliverables", "Verification", "Exit criteria"):
        if detailed.count(f"#### {heading}") != 193:
            failures.append(f"expected 193 {heading} sections")
    if detailed.count("implementation stop reached. Run pentest for this exact commit.") != 195:
        failures.append("expected one pentest stop for each milestone and release candidate")
    required_markers = (
        "Non-zero parser progress",
        "Separate vef-http09 package",
        "Engine event, command, acknowledgement, and publication contract",
        "Unified HTTP/1 outbound message state machine",
        "Inbound body acknowledgement, drain, discard, cancellation, and reuse",
        "HPACK synchronization, publication barrier, and error scope",
        "SETTINGS semantic application and negotiated-state lifecycle",
        "HTTP/2 malformed initial-field-block publication barrier",
        "HTTP/2 body cancellation, reset, and flow-credit lifecycle",
        "Authenticated origin authorization and HTTP/2 coalescing metadata",
        "Deterministic CPU, stack, code-size, and amplification budgets",
        "Generation-checked stream table",
        "TLS 1.3 early-data prohibition",
        "Independent security audit",
    )
    for marker in required_markers:
        if marker not in detailed or marker not in compact:
            failures.append(f"missing gap-closure milestone: {marker}")
    ordering = (
        ("Connection-option, Upgrade, and hop-by-hop field grammar", "101 Switching Protocols transition and publication barrier"),
        ("SETTINGS frame codec", "SETTINGS semantic application and negotiated-state lifecycle"),
        ("Fixed-capacity caller-storage public API", "Optional alloc-backed convenience API"),
    )
    for first, second in ordering:
        if compact.find(first) >= compact.find(second):
            failures.append(f"unsafe milestone ordering: {first} must precede {second}")
    if "Transactional HPACK context" in detailed or "RFC 7239 where Via" in detailed:
        failures.append("superseded HPACK or Via wording remains in detailed plan")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("release plan: 193 detailed milestones plus two release candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
