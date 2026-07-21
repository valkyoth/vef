# RFC Source Policy

Status: enforced policy

VEF uses exact RFC Editor plain-text publications as local normative
references. They are fetched explicitly, checked into `rfc/`, and bound to
`rfc/SHA256SUMS`. Builds and tests never download them.

Requirements:

- only HTTPS RFC Editor URLs listed in `rfc/SOURCES` are accepted;
- RFC text remains byte-for-byte unmodified;
- missing, extra, empty, changed, or source-mismatched files fail verification;
- `.gitattributes` prevents line-ending normalization;
- errata and engineering decisions never edit source RFC text;
- source and checksum changes are reviewed together;
- current assignments use reviewed IANA snapshots, not memory;
- RFC files are excluded from every published crate archive;
- mutable caches and redistribution-restricted documents remain local and
  gitignored under `references/`.

RFC 9931, published in March 2026, updates RFC 9112 and is part of the initial
HTTP/1.1 baseline rather than a later extension.
