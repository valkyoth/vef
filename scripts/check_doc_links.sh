#!/usr/bin/env sh
set -eu

failed=0
find . -path './target' -prune -o -path './.git' -prune -o -name '*.md' -type f -print |
while IFS= read -r file; do
    sed -n 's/.*](\([^)]*\.md\)\(#.*\)\{0,1\}).*/\1/p' "$file" |
    while IFS= read -r link; do
        case "$link" in
            http://*|https://*) continue ;;
            /*) target=".$link" ;;
            *) target="$(dirname "$file")/$link" ;;
        esac
        if [ ! -f "$target" ]; then
            echo "missing markdown link target: $file -> $link" >&2
            failed=1
        fi
    done
done

if [ "$failed" -ne 0 ]; then
    exit 1
fi
