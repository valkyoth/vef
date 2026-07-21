#!/usr/bin/env sh
set -eu

ci_file=".github/workflows/ci.yml"
stable_manifest="${RUST_STABLE_MANIFEST_URL:-https://static.rust-lang.org/dist/channel-rust-stable.toml}"

pinned_rust="$(sed -n 's/^channel = "\([0-9][0-9.]*\)"$/\1/p' rust-toolchain.toml | head -n 1)"
latest_rust="$(curl -fsSL "$stable_manifest" | sed -n '/^\[pkg\.rust\]$/,/^\[/ { s/^version = "\([0-9][0-9.]*\) .*/\1/p; }' | head -n 1)"
if [ -z "$pinned_rust" ] || [ "$pinned_rust" != "$latest_rust" ]; then
    echo "Rust pin is stale: pinned ${pinned_rust:-missing}, latest ${latest_rust:-unknown}" >&2
    exit 1
fi

if [ "${CHECK_LATEST_TOOLS_RUST_ONLY:-0}" = "1" ]; then
    exit 0
fi

for tool in cargo-deny cargo-audit cargo-sbom; do
    pinned="$(sed -n "s/.*cargo install --locked ${tool} --version \([0-9][^ ]*\).*/\1/p" "$ci_file" | head -n 1)"
    latest="$(cargo info "$tool" | sed -n 's/^version: //p' | head -n 1)"
    if [ -z "$pinned" ] || [ "$pinned" != "$latest" ]; then
        echo "${tool} pin is stale: pinned ${pinned:-missing}, latest ${latest:-unknown}" >&2
        exit 1
    fi
done

failed=0
for workflow in .github/workflows/*.yml; do
    while IFS= read -r ref; do
        if ! printf '%s\n' "$ref" | grep -Eq '^[0-9a-f]{40}$'; then
            echo "GitHub Action is not pinned to a full SHA in ${workflow}: ${ref}" >&2
            failed=1
        fi
    done <<EOF
$(sed -n 's/^[[:space:]]*uses: [^@][^@]*@\([^[:space:]]*\).*/\1/p' "$workflow")
EOF
done
test "$failed" -eq 0

pin_line="$(sed -n 's/.*uses: actions\/checkout@\([0-9a-f]\{40\}\) # \(v[0-9][0-9.]*\).*/\1 \2/p' "$ci_file" | head -n 1)"
pinned_sha="$(printf '%s\n' "$pin_line" | awk '{ print $1 }')"
pinned_tag="$(printf '%s\n' "$pin_line" | awk '{ print $2 }')"
latest_tag="$(git ls-remote --tags --refs https://github.com/actions/checkout.git 'refs/tags/v*' | awk '{ sub("refs/tags/", "", $2); print $2 }' | grep -E '^v[0-9]+(\.[0-9]+)*$' | sort -V | tail -n 1)"
latest_sha="$(git ls-remote --tags --refs https://github.com/actions/checkout.git "refs/tags/${latest_tag}" | awk '{ print $1 }')"

if [ -z "$pin_line" ] || [ "$pinned_tag" != "$latest_tag" ] || [ "$pinned_sha" != "$latest_sha" ]; then
    echo "actions/checkout pin is stale or invalid: ${pin_line:-missing}; latest ${latest_sha} ${latest_tag}" >&2
    exit 1
fi
