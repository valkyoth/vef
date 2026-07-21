# VEF Security Controls

Status: living control register

## Enforced at foundation

- `#![no_std]` and `#![forbid(unsafe_code)]` in every workspace crate.
- Zero third-party normal, build, and dev dependencies.
- Release overflow checks and aborting release panics.
- Clippy denial of panic, unwrap, expect, unchecked indexing, arithmetic side
  effects, truncating casts, and sign-loss casts.
- Rust source file ceiling of 500 lines.
- RFC provenance and checksum verification.
- Pinned toolchain, action SHAs, cargo-tool versions, and live freshness gate.
- Cross-version and cross-platform CI.
- Exact-commit pentest workflow and release evidence structure.

## Required as implementation grows

- Positive, negative, truncation, fragmentation-at-every-byte, and round-trip
  tests for every parser/serializer behavior.
- Stateful and stateless fuzz targets for all hostile-input surfaces.
- Model/Kani checks for bounded arithmetic and state invariants where useful.
- Miri and sanitizer checks where applicable.
- Differential and multi-implementation interoperability tests.
- Resource-exhaustion, response-amplification, smuggling, and cross-protocol
  attack corpora.
- Generated requirement-to-code and requirement-to-test coverage reports.
