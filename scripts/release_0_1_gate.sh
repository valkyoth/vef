#!/usr/bin/env sh
set -eu

test "$(rustc --version | awk '{ print $2 }')" = "1.97.1"
scripts/checks.sh
scripts/check_latest_tools.sh
scripts/check-rust-version-matrix.sh
cargo deny check
cargo audit
scripts/generate-sbom.sh --check
scripts/validate-release-metadata.sh 0.1.0
scripts/validate-release-readiness.sh v0.1.0
