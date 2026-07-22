# VEF Implementation Plan

Status: planning document

This document turns the reviewed final architecture into implementation rules
and phase outcomes. [`VERSION_PLAN.md`](VERSION_PLAN.md) is the compact
index. [`RELEASE_PLAN.md`](RELEASE_PLAN.md) is the authoritative per-version
contract with goal, deliverables, verification, exit criteria, and pentest stop.

## 1. Product outcome

`1.0.0` is the first serious production-ready HTTP crate. It implements
HTTP/1.0, HTTP/1.1 plus RFC 9931, HPACK, and HTTP/2 for client, origin-server,
intermediary, proxy, gateway, and tunnel roles. Explicit HTTP/0.9 compatibility
lives in a separate package and cannot be selected through an HTTP/1 fallback.
The protocol engines are sans-I/O, runtime-neutral, `no_std`, safe Rust, and
dependency-free in their protocol and I/O-contract crates.

HTTP/3 is reserved for a later QUIC-native 2.x architecture. No 1.x abstraction
pretends byte-stream HTTP/1 and HTTP/2 can transport HTTP/3.

## 2. Non-negotiable implementation rules

### Rust and dependencies

- Rust edition 2024 and resolver 3.
- MSRV Rust 1.90.0; current full-gate pin Rust 1.97.1.
- Every stable release and patch in the supported interval is checked.
- No nightly requirement for builds or releases.
- No third-party Rust crates, including build and dev dependencies.
- External fuzzers, model checkers, TLS libraries, and runtime implementations
  may be used as tools or interoperability peers without entering Cargo's
  production dependency graph.

### Core and storage

- Every workspace crate is `no_std` and forbids unsafe Rust at foundation.
- Caller-owned fixed-capacity storage lands before optional `alloc` ownership.
- Allocation can never define protocol correctness or be derived directly from
  an untrusted length.
- No socket, DNS, filesystem, runtime, TLS-library, or OS clock type enters a
  protocol crate.

### Modularity

- `vef` remains a facade.
- Shared semantics, HTTP/1, HPACK, HTTP/2, and I/O contracts remain separate.
- Rust source files never exceed 500 lines and receive split review near 300.
- Tests are split with the same care as implementation.
- A crate boundary represents a trust, dependency, capability, publication, or
  platform boundary; ordinary organization uses focused modules.

### Security and testability

- Every accepted message has one framing and routing interpretation.
- Every peer-controlled length, count, table, queue, response, and work unit is
  bounded independently.
- Successful incremental calls make non-zero observable progress; input,
  output, event, transition, and blocked states remain distinguishable.
- Applications receive no request before framing/routing control data is
  complete and validated.
- Parsing and validation produce typed deltas before state is committed.
- Reusable storage and stream slots carry generations, and borrowed events are
  acknowledged before the underlying slot can be recycled.
- No HTTP/0.9, CONNECT, Upgrade, ALPN, or cleartext HTTP/2 transition is guessed.
- Every behavior has a deterministic socket-free test oracle.
- Every parser milestone includes negative, truncation, all-single-split,
  capacity, arbitrary-input no-panic, adversarial, and regression coverage.

## 3. Crate authority

### `vef`

Feature-controlled re-exports only. It owns no parser or connection state.

### `vef-core`

Owns byte-oriented methods, status codes, versions, URI/request-target forms,
ordered fields, message heads, roles, limits, policies, progress, and
structured diagnostics.

### `vef-http1`

Owns HTTP/1.0 and HTTP/1.1 parsing, serialization, framing, bodies,
persistence, transitions, and connection state. It cannot parse or select
HTTP/0.9.

### `vef-http09` (planned at `0.67.0`)

Owns the exact HTTP/0.9 grammar, explicit client and server roles, and the
dedicated-listener policy. It has no HTTP/1 fallback, pipelining, forwarding,
or persistent-connection mode and is not enabled by the facade's `http1` or
`full` features.

### `vef-hpack`

Owns checked prefix integers, strings, Huffman coding, static/dynamic tables,
representations, indexing policy, and compression budgets.

### `vef-http2`

Owns frame codecs, exhaustive connection/stream state, message mapping, flow
control, push, errors, priority signals, and hostile-control budgets.

### `vef-io`

Owns minimal synchronous and poll-based byte progress, injected time,
deadlines, cancellation, and backpressure contracts. Protocol crates do not
depend on it; drivers compose from outside.

### `vef-brynja` (planned at `0.161.0`)

Owns the optional first-party Brynja TLS integration after its separate
admission review. It points inward to `vef-io` and protocol crates, returns
authenticated ALPN and peer metadata after the handshake, and does not add a
TLS dependency to the facade or protocol crates.

### External integrations

The plan defines adapter contracts and conformance kits without adding Tokio,
Rustls, OpenSSL, s2n, or another crate. Downstream integrations can implement
those contracts. Adding an official dependency-bearing adapter to this
repository requires an explicit future policy change and cannot affect core.

## 4. Standards and conformance workflow

1. Fetch exact RFC Editor text through the allowlist and verify SHA-256.
2. Review RFC status, updates/obsoletes relationships, and errata.
3. Add paragraph-addressable requirements with role and applicability.
4. Resolve SHOULD decisions before implementation depends on them.
5. Implement a small requirement batch behind explicit limits.
6. Add named positive, negative, fragmentation, adversarial, and interop tests.
7. Generate requirement-to-code/test evidence.
8. Run the full gate, stop implementation, and pentest the exact commit.

RFC 9112 and RFC 9931 are one effective HTTP/1.1 set. RFC 1945 is an explicit
historical compatibility profile, not a modern standards-track claim. The
ledger also records verified/held RFC 9112 and RFC 9113 errata, the RFC 9298
non-applicability decision unless HTTP/1.1 CONNECT-UDP is added, RFC 9111
cache-preservation duties, and the RFC 3986, RFC 7301, and RFC 8446 mappings.

## 5. Phase sequence

### Phase 1 — Foundation and shared semantics (`0.1.0`–`0.24.0`)

Establish repository integrity, non-zero progress, checked parsing primitives,
independent budgets, caller-owned storage, shared byte-oriented HTTP types,
role policies, sync/poll I/O capabilities, fake transports, and executable
requirements/errata evidence before accepting a complete message.

### Phase 2 — HTTP/1 and isolated HTTP/0.9 (`0.25.0`–`0.72.0`)

Implement distinct request and response state machines, strict octet parsing,
all framing and body modes, bounded pipelines, typed connection-close actions,
RFC 9931 and WebSocket opening-transition barriers, safe reframing, hardened
HTTP/1.0, and an isolated `vef-http09` package. End with smuggling,
cross-protocol, conformance, and pentest campaigns.

### Phase 3 — HPACK and HTTP/2 (`0.73.0`–`0.131.0`)

Implement bounded HPACK, every HTTP/2 frame and semantic mapping, typed
validate-then-commit deltas, generation-checked streams and tombstones, atomic
header blocks, independent flow-control and work budgets, mandatory ACK
tracking, reserved control output, and focused rapid-reset and flood defenses.

### Phase 4 — Proxy, client, server, and public APIs (`0.132.0`–`0.157.0`)

Complete HTTP/1↔HTTP/2 translation, authority and effective-URI validation,
hop stripping, Via and cache preservation, CONNECT/WebSocket bridges,
Structured Fields and priorities, explicit client correlation and retry
tokens, role facades, half-close behavior, caller-storage and optional `alloc`
APIs, diagnostics, interop, compile-fail tests, fuzzing, and soak campaigns.

### Phase 5 — OS, Aesynx readiness, and 1.0 evidence (`0.158.0`–`0.181.0`)

Add standard blocking/nonblocking adapters, admit Brynja only through a
separate first-party adapter, require authenticated ALPN, prohibit TLS 1.3
early data for 1.0, and prove the fixed-memory Aesynx capability model. Finish
the target/architecture matrix, Kani and stateful fuzz campaigns,
interoperability, whole-project pentest, independent audit, remediation, API
freeze, packaging, SBOM, provenance, and release-candidate readiness.

## 6. Release candidates and 1.0

`1.0.0-rc.1` freezes APIs and runs public interoperability, documentation, and
package dry runs. `rc.2` remediates findings and repeats every conformance,
fuzz, pentest, portability, dependency, and provenance gate.

`1.0.0` requires no unresolved critical/high findings; verified applicable
MUST/MUST NOT requirements; reviewed SHOULD decisions; no-allocation core
operation; no unsafe core; deterministic HTTP/1 framing; exhaustive HTTP/2
state evidence; bounded HPACK; independent role coverage; published platform
matrices; verified independent-audit remediation; and signed release evidence.

## 7. Mandatory release loop

Every `0.N.0`, patch, and release candidate follows the same loop:

1. Reach the documented implementation stop.
2. Run local checks, MSRV matrix, live tool checks, policy, audit, SBOM, and
   release-specific verification.
3. Pentest the exact implementation commit using temporary ignored
   `PENTEST.md` for findings.
4. Remediate, add regression tests, update documentation, and rerun all gates.
5. Commit a permanent passing report as the only change in the direct child of
   the reviewed commit.
6. Verify CI and CodeQL default setup on both commits.
7. Run release readiness before tagging; never tag or publish implicitly.

Every phase-ending release adds a full-repository review, stateful fuzz
campaign, corpus minimization, interoperability campaign, resource-exhaustion
assessment, manual review, and conformance-decision audit. The pre-1.0 audit is
independent of the primary implementers.
