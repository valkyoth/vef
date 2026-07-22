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
- Numerical or target-relative CPU, stack, code-size, amplification,
  fragmentation-cost, and fairness ceilings are defined before parsers and
  measured as each hostile surface lands.
- Successful incremental calls make non-zero observable progress; input,
  output, event, transition, and blocked states remain distinguishable.
- Applications receive no request before framing/routing control data is
  complete and validated.
- Borrowed body events require acknowledgement. Connection reuse is impossible
  until the body/trailer lifecycle completes or a mandatory-close action wins.
- HTTP/2 receive credit is released only for application-acknowledged or
  explicitly discarded DATA octets, never merely because a frame was parsed.
- HTTP/2 outbound HEADERS, DATA, trailers, END_STREAM, partial output, and
  cancellation follow one generation-checked per-stream command lifecycle.
- Internal receive-credit accounting is distinct from bounded, coalesced
  WINDOW_UPDATE emission; padding cannot drive one control frame per DATA frame.
- Unknown HTTP/2 frames are bounded, incrementally drained, state-neutral, and
  unpublished unless an explicitly enabled extension owns their type.
- Outbound framing is validated as strictly as inbound framing, including
  declared lengths, body-forbidden contexts, trailers, and completion.
- Peer protocol violations, configured policy excess, insufficient caller
  storage, output backpressure, and mandatory-control exhaustion are distinct.
- Parsing and validation produce typed deltas before state is committed.
- HTTP/2 stream errors are typed deltas that cannot mutate unrelated streams,
  scheduler entries, flow windows, generations, compression state, or events;
  connection-fatal decisions stop all later application publication.
- Reusable storage and stream slots carry generations, and borrowed events are
  acknowledged before the underlying slot can be recycled.
- HPACK dynamic entries carry caller-supplied compression-principal provenance;
  shared/coalesced connections never look up a private entry across principals.
- Compression-principal provenance is immutable encoder-side metadata: it does
  not alter HPACK size or indices, skipped entries retain their wire index, and
  eviction/reset removes entry bytes and provenance in one operation.
- Stream/flood counters charge before work, use saturating arithmetic and
  injected-time refill, and can consult caller-shared cross-connection limits.
- No HTTP/0.9, CONNECT, Upgrade, ALPN, or cleartext HTTP/2 transition is guessed.
- Every behavior has a deterministic socket-free test oracle.
- Every parser milestone includes negative, truncation, all-single-split,
  capacity, arbitrary-input no-panic, adversarial, and regression coverage.

## 3. Crate authority

### `vef`

Feature-controlled re-exports only. It owns no parser or connection state.

### `vef-core`

Owns byte-oriented methods, status codes restricted to valid HTTP 100..=599,
typed invalid received status evidence, versions, URI/request-target forms,
ordered fields, message heads, roles, limits, policies, progress, and
structured diagnostics, including opaque generation-safe compression-principal
provenance supplied by callers without embedding identity policy in HPACK.

### `vef-http1`

Owns HTTP/1.0 and HTTP/1.1 parsing, serialization, framing, bodies,
persistence, transitions, and connection state. It cannot parse or select
HTTP/0.9.

### `vef-http09` (planned at `0.76.0`)

Owns the exact HTTP/0.9 grammar, explicit client and server roles, and the
dedicated-listener policy. It has no HTTP/1 fallback, pipelining, forwarding,
or persistent-connection mode and is not enabled by the facade's `http1` or
`full` features.

### `vef-websocket-handshake` (planned at `0.68.0`)

Owns the optional RFC 6455 opening handshake: key/version/token validation,
dependency-free accept generation, subprotocol/extension negotiation metadata,
Origin preservation, and the post-handshake publication barrier. It does not
implement WebSocket frames and is not part of `http1` or `full` by default.
Client handshakes require a caller/adapter-supplied fresh 16-byte nonce; core
code owns no RNG and never derives a nonce from time or deterministic state.

### `vef-hpack`

Owns checked prefix integers, strings, Huffman coding, static/dynamic tables,
representations, indexing policy, and compression budgets.

### `vef-http2`

Owns frame codecs, exhaustive connection/stream state, message mapping, flow
control, borrowed inbound DATA acknowledgement, outbound per-stream message
commands, push, errors, priority signals, and hostile-control budgets.

### `vef-structured-fields` (planned at `0.164.0`)

Owns the optional dependency-free RFC 9651 lexical cursor, item grammars,
complete bare-item dispatcher, parameters, lists, dictionaries, canonical
serialization, and caller-owned incremental storage. HTTP/2 and priority code
consume its typed results; this crate owns no connection or scheduling state.

### `vef-io`

Owns minimal synchronous and poll-based byte progress, injected time,
deadlines, cancellation, and backpressure contracts. Protocol crates do not
depend on it; drivers compose from outside.

### `vef-brynja` (planned at `0.203.0`)

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
RFC 6455 is an optional opening-handshake extension. RFC 9298 is locked but
not applicable unless HTTP/1.1 CONNECT-UDP enters scope. Via maps to RFC 9110;
RFC 7239 `Forwarded` transformation remains outside 1.0.
Forward-proxy Max-Forwards and HTTP/1 TE request-field behavior map to RFC
9110/9112. RFC 9651 and RFC 9218 are implemented as bounded incremental
micro-stops rather than one aggregate parser milestone.

## 5. Phase sequence

### Phase 1 — Foundation and shared semantics (`0.1.0`–`0.27.0`)

Establish repository integrity, non-zero progress, checked parsing primitives,
independent budgets, caller-owned storage, shared byte-oriented HTTP types,
initial measurable resource profiles, capacity-versus-protocol dispositions,
role policies, sync/poll I/O capabilities, fake transports, the complete
event/command/acknowledgement/publication contract, and executable
requirements/errata evidence before accepting a complete message.
URI types retain distinct raw path and optional-query spans, preserve absent
versus empty query and percent-encoded bytes, and expose normalization only as
a non-authoritative view. Authority parsing covers IPv6/IPvFuture, ports,
userinfo rejection, and malformed brackets explicitly.
Role policy defines generation-bound TrustedRequestContext scheme evidence and
precedence/conflict handling, staged CONNECT authorization types that bind a
lexical authority, attempt token, caller-resolved endpoint, actual peer, and
request/policy generations without resolver/socket authority, plus a distinct
hop/connection/generation-bound sensitive proxy-credential type; socket/runtime
types never imply transport security and proxy credentials are not end-to-end
Authorization.

### Phase 2 — HTTP/1 and isolated HTTP/0.9 (`0.28.0`–`0.81.0`)

Implement distinct request and response state machines, strict octet parsing,
all inbound framing/body modes, a unified outbound message state machine,
borrowed body acknowledgement and drain/discard/cancel/reuse actions, bounded
pipelines, typed error/close actions, RFC 9931, ordered Upgrade validation, an
isolated WebSocket handshake crate with caller-supplied entropy, safe
reframing, hardened HTTP/1.0, and an isolated `vef-http09` package.
Host parsing accepts the RFC-required empty value but yields only a non-routable
artifact. The next stop authorizes target form by origin/forward/reverse role,
derives the full effective scheme/authority/path/query under explicit trusted
context/reject/default policy, and only then publishes a request. CONNECT uses
a distinct bracket-safe authority with explicit port 1..=65535 and no default.
Later translation reuses those typed decisions.
Request transfer codings require final chunked; responses may instead become
close-delimited, with repeated chunked and unsupported coding kept distinct.
RFC 9931 binds CONNECT wait-or-close forwarding and mandatory reject-close;
HTTP/1 CONNECT 407 includes a valid challenge, destroys credentials/pending
bytes, closes, and retries only on a fresh connection. No failed optimistic
transition bytes are reparsed as HTTP.
CONNECT first authorizes lexical authority, then each caller-resolved endpoint
before dial, then validates the caller-certified actual peer and all attempt,
request, and policy generations before output/success/tunnel publication.
Builders attach no request content, hardened inbound framing rejects and
closes, successful server responses emit no length/transfer fields, and all
responses are non-cacheable.
HTTP/1 205 output is provably zero content; inbound 205 still follows ordinary
framing so nonzero content is drained-or-closed without pipeline desynchrony
and cannot be forwarded as a valid 205.
Informational responses exclude 101: an exchange ends through either ordinary
1xx then one final response, or one validated terminal 101 after complete
request processing (and required 100), after which every HTTP operation fails.
Chunk extensions implement the exact BWS-delimited RFC grammar while charging
raw whitespace and stripping it only for semantic interpretation.

### Phase 3 — HPACK and HTTP/2 (`0.82.0`–`0.154.0`)

Implement bounded HPACK with encoder-output atomicity, every HTTP/2 frame,
activation and graceful shutdown, malformed publication barriers before
mapping, generation-checked streams, and explicit cancellation/flow credit.
Every frame codec owns exact length, stream-ID, flag, reserved-bit, padding,
and error-scope contracts. A dedicated error-delta stop proves stream failures
cannot mutate unrelated connection state before HPACK/header publication.
HEADERS/PUSH_PROMISE distinguish undersized mandatory layouts from invalid
padding and identifier errors. Concurrency counts open/half-closed but not
reserved streams, and local table capacity remains distinct from peer excess.
Sensitive HPACK indexing, fail-closed ALPN/prior-knowledge selection,
field-block-contiguous scheduling, reserved mandatory-control capacity,
credit-update coalescing, and commit-time frame-limit transitions are explicit.
Rapid Reset and flood charges are independent and non-refundable; required
ACK/control output either remains reserved or produces one bounded shutdown.
Refusal/reset/cancellation never abandons an inbound HPACK block: a refused
stream finishes synchronization without application publication, or lack of
remaining HPACK/CONTINUATION capacity forces bounded connection shutdown.
Parse SETTINGS early but integrate header-table, initial-window, admission, and
frame-size effects only after their owning components exist. Add borrowed DATA
events with partial acknowledgement and credit release, then the outbound
HEADERS/DATA/trailers/END_STREAM command lifecycle before general scheduling.
Native HTTP/2 CONNECT staging respects milestone ownership: v0.130 classifies
post-initial-HEADERS DATA into fixed-capacity PendingConnect while
AwaitingConnectOutcome and emits a local-capacity CANCEL when full, without
claiming flow credit, DNS, dial, or socket behavior; v0.133–v0.134 charge stream
and connection windows; v0.136 adds borrowed acknowledgement/discard and credit
release; v0.137 adds tunnel output/FIN commands. No bytes forward before the
generation-matched caller outcome, connected frames are constrained, and
caller transport failures map to typed CONNECT_ERROR/TCP-reset actions.
HTTP/2 205 rejects outbound DATA and drains/resets malicious inbound DATA under
ordinary stream framing without disturbing other streams.
Integrate ENABLE_PUSH in push ownership and apply MAX_FRAME_SIZE atomically
before emitting its SETTINGS ACK. Retain independent budgets, mandatory ACK
tracking, reserved output, and flood defenses.

### Phase 4 — Proxy, client, server, and public APIs (`0.155.0`–`0.199.0`)

Build a representation-only translation IR, then effective URI, hop stripping,
exact append-only Via and hop-scoped proxy authentication, and a normative
HTTP/1↔HTTP/2 matrix before emitting destination bytes. Via parses bounded
ordered members/comments, records the inbound protocol/version, appends a
caller pseudonym after capacity preflight, never replaces/combines, applies to
every proxy-forwarded message and gateway inbound forwarded request, and uses
caller-owned privacy/loop policy without input-derived identity. Proxy
credentials are consumed by the expecting hop, removed before origins,
relayed only by named-next-hop cooperative policy, never confused with
Authorization, scoped back only to the next client, challenged on every 407,
redacted/never-indexed/TRACE-excluded, and erased across authentication retry.
Add Max-Forwards, TE: trailers, bounded Structured Fields micro-stops, complete
bare-item dispatch in the optional `vef-structured-fields` crate,
ENABLE_CONNECT_PROTOCOL and NO_RFC7540_PRIORITIES owner integration, complete
priority/intermediary/flood behavior, replayability-aware retry tokens,
RFC 9651 duplicate-overwrite and mandatory-minimum profiles, exact HTTP/2
PRIORITY_UPDATE rules, compression-principal-aware coalescing,
authenticated coalescing inputs, exact transition byte handoff, role facades,
fixed storage before `alloc`, diagnostics, interop, fuzzing, and soak.
The matrix carries raw path plus optional query into/out of `:path`, preserves
empty-query and percent-encoded identity, and only inserts `/` for an empty path
where the RFC requires it.
TRACE/OPTIONS completes Max-Forwards without synthesis, safe zero handling,
content/sensitive-field builder rules, bounded sanitized reflection, required
OPTIONS Content-Type, and non-cacheable responses.
Absolute-form OPTIONS with empty path and absent query remains absolute through
intermediate proxies and becomes `*` only at the final origin-facing hop;
present-empty query and `/` never convert, including HTTP/2 `:path` mapping.
Extended CONNECT keeps peer-enabled outbound initiation separate from locally
advertised inbound acceptance. Advertisement becomes effective at SETTINGS
byte commit, accepts only 0/1, cannot be withdrawn after 1, and never rolls
back because a later endpoint request fails.
The v0.163 bridge is bidirectional: HTTP/1-side key/accept processing never
leaks into RFC 8441, ws/wss and retained negotiation/end-to-end fields map
exactly with lowercase HTTP/2 names, hostile HTTP/2 key/accept fields cannot
influence fresh HTTP/1 keys, the reverse direction consumes caller entropy,
and no WebSocket data crosses before both handshakes commit.
Tunnel closure is protocol-specific: HTTP/1 EOF drains already-owned bytes then
closes both sides, while HTTP/2/RFC8441 END_STREAM forwards a directional FIN
and preserves reverse traffic until both directions finish. Reset, TCP error,
fatal alert, cancellation, or connection error aborts both; half-close timeout
is injected and no tunnel returns to HTTP reuse.
PRIORITY_UPDATE request and push targets use one receiver-server-relative state
convention, including reserved-local and half-closed-remote push targets.

### Phase 5 — OS, Aesynx readiness, and 1.0 evidence (`0.200.0`–`0.225.0`)

Add standard blocking/nonblocking adapters, admit Brynja only through a
separate first-party adapter, enforce concrete RFC 9113 TLS admission and
termination/alert/EOF mapping, prohibit TLS 1.3 early data for 1.0, prove
short-I/O/readiness/deadline/alignment/scatter-gather Aesynx behavior, and
enforce deterministic CPU, stack, code-size, amplification,
fragmentation-cost, and scheduler-fairness budgets. Brynja and Aesynx adapters
inject authenticated, connection-generation-bound TrustedRequestContext rather
than allowing core to infer TLS from handles. Finish the
target/architecture matrix, replay and expand the Kani and stateful fuzz
harnesses created with each component,
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
