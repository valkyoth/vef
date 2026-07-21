#!/usr/bin/env sh
set -eu

mode="${1:-check}"
if [ "$mode" != "check" ]; then
    echo "usage: scripts/validate-modularity-policy.sh check" >&2
    exit 2
fi

violations="$(find crates -type f -name '*.rs' -exec wc -l {} \; | awk '$1 > 500 { print }')"
if [ -n "$violations" ]; then
    echo "Rust files exceed 500 lines:" >&2
    echo "$violations" >&2
    exit 1
fi

for crate in vef vef-core vef-http1 vef-hpack vef-http2 vef-io; do
    test -f "crates/${crate}/Cargo.toml"
    test -f "crates/${crate}/src/lib.rs"
done

for crate in vef-core vef-http1 vef-hpack vef-http2 vef-io; do
    grep -q '#!\[no_std\]' "crates/${crate}/src/lib.rs"
    grep -q '#!\[forbid(unsafe_code)\]' "crates/${crate}/src/lib.rs"
done
