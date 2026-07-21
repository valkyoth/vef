# Reference Material Policy

Tracked, redistributable, immutable standards belong under `rfc/` with source
and checksum manifests. VEF-authored requirement data belongs under `spec/`.

Use these ignored local directories for material that should not be committed:

- `references/private/`: licensed, confidential, or redistribution-restricted
  documents;
- `references/cache/`: mutable IANA/API/website downloads and temporary source
  inspection.

When a mutable registry becomes release evidence, normalize the smallest
needed snapshot into a reviewed `spec/generated/` artifact with source URL,
retrieval time, checksum, generator version, and licensing/provenance note.
