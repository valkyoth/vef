#!/usr/bin/env sh
set -eu

for package in vef-core vef-hpack vef-http1 vef-http2 vef-io vef; do
    listing="$(cargo package -p "$package" --list --allow-dirty)"
    printf '%s\n' "$listing" | grep -q '^Cargo.toml$'
    printf '%s\n' "$listing" | grep -q '^README.md$'
    printf '%s\n' "$listing" | grep -q '^LICENSE-MIT$'
    printf '%s\n' "$listing" | grep -q '^LICENSE-APACHE$'
    if printf '%s\n' "$listing" | grep -Eq '^(rfc|spec|security|references)/'; then
        echo "non-package evidence leaked into ${package}" >&2
        exit 1
    fi
done
