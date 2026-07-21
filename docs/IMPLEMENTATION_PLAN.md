# VEF Implementation Plan

Status: planning document

This document turns the reviewed final architecture into implementation rules
and phase outcomes. [`VERSION_PLAN.md`](VERSION_PLAN.md) is the compact
index. [`RELEASE_PLAN.md`](RELEASE_PLAN.md) is the authoritative per-version
contract with goal, deliverables, verification, exit criteria, and pentest stop.

## 1. Product outcome

`1.0.0` is the first serious production-ready HTTP crate. It implements
explicit HTTP/0.9 compatibility, HTTP/1.0, HTTP/1.1 plus RFC 9931, HPACK, and
HTTP/2 for client, origin-server, intermediary, proxy, gateway, and tunnel
roles. It is sans-I/O, runtime-neutral, `no_std`, safe Rust, and dependency-free
in its protocol and I/O-contract crates.

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
- Successful incremental calls make observable progress.
- Applications receive no request before framing/routing control data is
  complete and validated.
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

Owns explicit HTTP/0.9, HTTP/1.0, and HTTP/1.1 parsing, serialization, framing,
bodies, persistence, transitions, and connection state.

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
historical compatibility profile, not a modern standards-track claim.

## 5. Phase sequence

### Phase 1 — Foundation and shared types (`0.1.0`–`0.16.0`)

Establish repository integrity, checked parsing primitives, budgets, errors,
and shared byte-oriented HTTP types before accepting a complete message. The
phase exit is a full foundation audit and executable conformance harness.

### Phase 2 — HTTP/1 heads (`0.17.0`–`0.32.0`)

Implement role-aware start lines and field sections with strict CRLF,
whitespace/control rejection, Host validation, Content-Length and
Transfer-Encoding grammar, one TE/CL decision, and serializer round trips.

### Phase 3 — HTTP/1 bodies (`0.33.0`–`0.48.0`)

Centralize message-body length, fixed/close/chunked bodies, trailers,
persistence, bounded pipelining, informational responses, 100-continue, EOF,
and truncation. End with a full smuggling and body-framing audit.

### Phase 4 — Roles, transitions, and legacy (`0.49.0`–`0.64.0`)

Complete HEAD/status body rules, CONNECT/Upgrade, RFC 9931 behavior,
hop-by-hop forwarding, HTTP/1.0, explicit HTTP/0.9, cross-protocol rejection,
and the full HTTP/0.9–1.1 pentest.

### Phase 5 — I/O and secure adapter contracts (`0.65.0`–`0.80.0`)

Build dependency-free sync/poll I/O, clocks, cancellation, fake transports,
generic drivers, TLS/ALPN metadata and prerequisite contracts, and downstream
adapter conformance kits. Concrete third-party runtime/TLS crates remain out of
the workspace under the current policy.

### Phase 6 — HPACK (`0.81.0`–`0.96.0`)

Implement the complete checked integer/string/Huffman/table/representation
stack with caller storage, independent limits, sensitive indexing policy,
official vectors, differential evidence, fuzzing, and pentest.

### Phase 7 — HTTP/2 framing and state (`0.97.0`–`0.112.0`)

Implement every core frame, unknown extension handling, stream ID rules,
exhaustive stream state, connection sequencing, and header-block atomicity.

### Phase 8 — HTTP/2 semantics and flow (`0.113.0`–`0.128.0`)

Integrate HPACK, pseudo-field rules, message mapping, trailers, Cookie mapping,
connection/stream flow control, settings, admission, scheduling, push, GOAWAY,
ALPN/prior knowledge, and full RFC 9113 conformance.

### Phase 9 — HTTP/2 hardening and translation (`0.129.0`–`0.144.0`)

Add independent flood/work/output budgets, rapid-reset defenses, decompression
bomb controls, H1/H2 translation, authority consistency, CONNECT, Structured
Fields, RFC 9218 priority, hostile-peer campaigns, and intermediary audit.

### Phase 10 — Stable APIs and release hardening (`0.145.0`–`0.160.0`)

Stabilize role facades, owned and fixed-capacity APIs, diagnostics, features,
MSRV/no-default builds, 32-bit/big-endian/architecture/platform matrices,
long-running soak, independent audit, remediation, and API freeze.

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

Phase boundaries every 16 releases add a full-repository review, stateful fuzz
campaign, corpus minimization, interoperability campaign, resource-exhaustion
assessment, manual review, and conformance-decision audit. The pre-1.0 audit is
independent of the primary implementers.
