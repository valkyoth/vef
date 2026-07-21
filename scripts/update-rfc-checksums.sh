#!/usr/bin/env bash
set -euo pipefail

expected="$(sed -n 's/^\([0-9][0-9]*\) https:\/\/www\.rfc-editor\.org\/rfc\/rfc[0-9][0-9]*\.txt [a-z0-9-][a-z0-9-]*$/rfc\1.txt/p' rfc/SOURCES | sort)"
actual="$(find rfc -maxdepth 1 -type f -name 'rfc*.txt' -printf '%f\n' | sort)"
if [[ -z "$expected" || "$expected" != "$actual" ]]; then
    echo "fetch every allowlisted RFC before updating checksums" >&2
    exit 1
fi

temporary="$(mktemp "${TMPDIR:-/tmp}/vef-rfc-sums.XXXXXX")"
trap 'rm -f "$temporary"' EXIT HUP INT TERM
(
    cd rfc
    sha256sum rfc*.txt
) > "$temporary"
mv "$temporary" rfc/SHA256SUMS
scripts/verify-rfcs.sh
scripts/lock-rfcs.sh
