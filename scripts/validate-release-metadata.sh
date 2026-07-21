#!/usr/bin/env sh
set -eu

version="${1:-0.1.0}"
test ! -f PENTEST.md
test -f LICENSE-MIT
test -f LICENSE-APACHE
test -f SECURITY.md
test -f CHANGELOG.md
test -f "release-notes/RELEASE_NOTES_${version}.md"
test -f docs/IMPLEMENTATION_PLAN.md
test -f docs/VERSION_PLAN.md
test -f docs/RELEASE_PLAN.md
test -f docs/CRATE_VERSION_MATRIX.md
test -f release-crates.toml
test -f rfc/SHA256SUMS
test -x scripts/release_0_1_gate.sh
grep -q 'license = "MIT OR Apache-2.0"' Cargo.toml
grep -q 'rust-version = "1.90"' Cargo.toml
grep -q 'channel = "1.97.1"' rust-toolchain.toml
grep -q 'workflow_dispatch:' .github/workflows/release.yml
! grep -q 'tags:' .github/workflows/release.yml
