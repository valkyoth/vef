#!/usr/bin/env sh
set -eu

find rfc -maxdepth 1 -type f -name 'rfc*.txt' -exec chmod a-w {} \;
