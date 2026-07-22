#!/usr/bin/env sh
set -eu

cargo fmt --all --check
scripts/check_shell_syntax.sh
scripts/check_doc_links.sh
python3 scripts/validate-release-plan.py
if ! cmp -s README.md crates/vef/README.md; then
    echo "README.md and crates/vef/README.md must remain identical" >&2
    diff -u README.md crates/vef/README.md >&2 || true
    exit 1
fi
scripts/verify-rfcs.sh
scripts/validate-modularity-policy.sh check
scripts/validate-security-policy.sh
python3 scripts/check_dependency_policy.py
scripts/check_packages.sh
scripts/generate-sbom.sh --check
cargo check --workspace --all-targets --all-features --locked
cargo clippy --workspace --all-targets --all-features --locked -- -D warnings
cargo test --workspace --all-features --locked
