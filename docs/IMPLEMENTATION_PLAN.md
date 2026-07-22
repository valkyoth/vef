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
- Conditional origin requests expose only a read-only selection view until
  sealed content/execution permits exist; 100 Continue, body publication, and
  method side effects cannot cross that gate.
- Borrowed body events require acknowledgement. Connection reuse is impossible
  until the body/trailer lifecycle completes or a mandatory-close action wins.
- HTTP/2 receive credit is released only for application-acknowledged or
  explicitly discarded DATA octets, never merely because a frame was parsed.
- HTTP/2 outbound HEADERS, DATA, trailers, END_STREAM, partial output, and
  cancellation follow one generation-checked per-stream command lifecycle.
  END_STREAM command acceptance seals the application send direction; only
  complete carrying-frame acknowledgement changes wire state, while partial
  output/failure does not and fragmented HEADERS retain CONTINUATION ownership.
  AcceptedPrivate ordinary output may be superseded by reset only when it is
  outside a committed outbound field block. A whole Private HEADERS/
  PUSH_PROMISE block may roll back before initial exposure; first exposure
  commits its connection-scoped obligation through END_HEADERS, so no reset,
  control, GOAWAY, or other stream can supersede/interleave its CONTINUATIONs.
  Transport failure abandons the connection, while the initial HEADERS
  completion hook remains frame-scoped. First ordinary exposure freezes its
  exact slot, commits stream+connection debit, and forces suffix completion.
- Outbound DATA atomically reserves exact payload/padding credit—not its frame
  header—from the signed stream and nonnegative connection ledgers before
  exposure.
  Available, reserved-unexposed, and committed-debited states are distinct;
  WINDOW_UPDATE and SETTINGS/resegmentation reconcile only unexposed state,
  frozen debit never refunds, and negative windows block later exposure. Copy
  each exact frame into an exclusive generation-checked slot in a caller-owned
  fixed-capacity `OutboundFrameArena`; a nonzero local
  `max_outbound_frame_payload` caps segmentation independently of peer
  MAX_FRAME_SIZE. Slot bytes remain unavailable until supersession, full
  acknowledgement, or connection cleanup, while queue-byte and queue-entry
  exhaustion produce distinct typed local backpressure.
- Internal receive-credit accounting is distinct from bounded, coalesced
  WINDOW_UPDATE emission; padding cannot drive one control frame per DATA frame.
- Unknown HTTP/2 frames are bounded, incrementally drained, state-neutral, and
  unpublished unless an explicitly enabled extension owns their type.
- Outbound framing is validated as strictly as inbound framing, including
  declared lengths, body-forbidden contexts, trailers, and completion.
- Typed and generic outbound conditional/range fields share one final frozen
  validation; client partial recombination requires terminal request-bound
  Content-Type, Content-Range, body-length, and strong-validator evidence.
- Partial Content-Type classification comes only from the bounded sealed
  `vef-media-type` result; multipart never grants top-level range authority.
- Generic media-type syntax preserves RFC-valid duplicate parameters and empty
  slots; generated OPTIONS and partial responses apply separate policies over
  the same v0.157.5 parser. Engines and role code cannot carry temporary grammars.
- A public delivery preference or requested work budget confers no authority;
  engine-selected delivery and profile-capped active-work permits are fixed
  before body consumption or combination work. Retention commits before
  publication/acknowledgement, and unequal overlaps quarantine the assembly
  context without publishing bytes or synthesized metadata.
- Vary identity copies use the same exclusive-storage, anti-aliasing, generation,
  DMA-fencing, semantic-invalidation, and caller-scrub rules as retained bytes;
  normalization runs once under profile caps, retains canonical bytes without a
  redundant sensitive raw copy, and comparisons never reparse. Physical reuse
  waits for every body/identity/output lease despite semantic invalidation.
- First non-empty Sans-I/O output exposure freezes exact bytes and semantic
  identity in engine storage. One non-Copy/non-Clone generation token owns each
  offered range; zero/short/full acknowledgement consumes it once, invalid
  tokens do nothing, and only acknowledged prefixes count as written. Frozen
  output resumes at its suffix and pins owning state through failure cleanup.
- A live/reserved HTTP/2 slot preflights cutoff storage before release and is
  never untracked. Rejection disposition, RFC wire state, and reset-output
  progress/reason/reservation, remote-closure record, immutable first-closure
  cause, terminal state/stage, compression workspace, immutable field-section
  lease, and block ownership remain independent. HPACK atomically transfers a
  sealed non-Copy/non-Clone section lease into monotonic PendingSemantics while
  releasing only compression scratch. END_STREAM can make a reserved, unexposed
  policy reset dormant but no intermediate stage releases it; peer reset aborts
  publication after required HPACK drain, and connection failure transfers
  cleanup to shutdown ownership.
  A reset reason is replaceable only before exposure; a frozen 13-byte frame,
  output token/cursor, and owning tombstone remain immutable and unrecyclable.
  Reserved/Frozen acknowledgement 0..=12 leaves wire state unchanged; byte 13
  closes locally exactly once unless remote closure already won, in which case
  completion cannot overwrite its cause. Partial-prefix failure never closes.
- Assembly-enabled local correlation reserves a linear engine-only target/
  principal/partition/navigation invalidation handle before request output.
  Accepted push atomically preflights its slot, handle, independent minimal
  immutable `PushedAssemblyProvenance`, and rejection/cutoff tracking after
  complete HPACK/semantic validation and before publication. Local exhaustion
  returns zero-byte/no-correlation AssemblyInvalidationCapacity backpressure;
  push capacity failure marks the provisional slot rejecting without changing
  its wire state, publishes nothing, and reserves exact policy/error reset
  arbitration through every terminal semantic stage or tracked shutdown if
  state is unavailable. Hold the handle/provenance through terminal
  backpressure, release it once at a terminal disposition, and reserve
  independently for retries. A completed valid 200 invalidates by exact key or
  within that namespace; absent coding/domain refinement widens only its
  children. Arena rotation is internal invariant/trusted-storage corruption or
  caller policy only, never peer invalidity, conflict, or capacity.
- Mandatory generated responses retain engine-only semantic-validation slots
  and frozen-head storage that application work cannot consume; total reserve
  failure commits one deterministic close/shutdown action with no partial head.
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
It owns raw protocol-neutral response heads, trailer-permission evidence, and
checked generic `UtcCivilTime` plus generation-bound Available/Unavailable
complete-instant evidence; validated HTTP dates have a separate 1900 year
floor. Civil time is distinct from monotonic deadlines and grants no clock
ownership.
Raw heads grant no emission and core exposes no serializer.

### `vef-auth` (planned at `0.157.2`)

Depends only on `vef-core`. Owns bounded scheme-neutral challenge,
credentials, token68, auth-param, authentication field, sensitive-storage, and
scheme-certified authentication-trailer permission behavior. It implements no
Basic, Digest, application credential validation, or physical buffer erasure.

### `vef-media-type` (planned at `0.157.5`, partial integration at `0.180.5`)

Depends only on `vef-core`. Owns bounded incremental media type, subtype,
parameter, empty-slot, quoted-string, and escape syntax that preserves ordered
duplicates, forbids whitespace around `=`, and distinguishes empty quoted from
missing values. Separate sealed generated-media validation is used by OPTIONS;
at `0.180.5` a media-specific RFC 2046 boundary policy adds partial-response
classification. It neither parses multipart bodies nor grants range authority.

### `vef-conditions` (planned at `0.180.1`–`0.181.2`)

Depends on `vef-core` and, starting at `0.180.5`, `vef-media-type`. Owns bounded
entity-tag and HTTP-date validators, strong/weak comparison, conditional-field
parsing and RFC-ordered evaluation, checked Range/Content-Range arithmetic,
pre-action representation evidence,
retrieval-only hypothetical-200 snapshots, staged content/execution permits,
final outbound request validation, single-range planning, individual partial
head/chunk/completion streaming, optional retained-prefix validation,
generation-safe cross-request assembly contexts, structurally safe stored-byte/
output leases, exact redacted Vary identity leases/fixed storage, trailer-
finalized combination refinement, one-time canonical normalization, reserved-
namespace/keyed full-200 replacement evidence, independently leased immutable
pushed-assembly provenance, borrow-aware reclamation,
requested/profile-capped
active work budgets, and bounded copy/header-synthesis plans. Its sealed
outcomes bind exact request/exchange/correlation generations, civil time, and
caller-supplied representation existence, metadata, length, validator, and
modification evidence without retroactively revoking a consumed mutation
permit.

### `vef-semantics` (planned at `0.182.1`)

Depends only on `vef-core`, `vef-auth`, `vef-media-type`, and `vef-conditions`. Owns
received/forwarded/generated role and protocol response semantics and is the
sole constructor of sealed `ValidatedResponse`. That object owns or immutably
borrows the precise ordered head, framing, sensitivity/indexing, body, and
trailer plan plus an unextractable internal `ResponseEmissionPermit`; it is
non-Copy/non-Clone and consumed whole exactly once by an outbound engine. No
API pairs a raw head with a permit, and every mutation requires revalidation.

### `vef-http1`

Owns HTTP/1.0 and HTTP/1.1 parsing, serialization, framing, bodies,
persistence, transitions, and connection state. It cannot parse or select
HTTP/0.9. Starting at v0.157.5 it depends on `vef-media-type`; it later depends
on `vef-conditions` and `vef-semantics`, consumes frozen validated requests/responses, and has no public head-output entry accepting a
raw `vef-core` request or response.

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
commands, push, errors, priority signals, and hostile-control budgets. It
depends on `vef-media-type` from v0.157.5 and later on `vef-conditions` and
`vef-semantics`, in addition to `vef-hpack`;
request/response HEADERS require their exact frozen validated object, and
HTTP/2 status 426 has no local emission path.

### `vef-structured-fields` (planned at `0.164.0`)

Owns the optional dependency-free RFC 9651 lexical cursor, item grammars,
complete bare-item dispatcher, parameters, lists, dictionaries, canonical
serialization, and caller-owned incremental storage. HTTP/2 and priority code
consume its typed results; this crate owns no connection or scheduling state.

### `vef-io`

Depends on `vef-core`. Owns minimal synchronous and poll-based byte progress,
monotonic deadline providers, optional civil-clock evidence providers,
cancellation, and backpressure contracts. Protocol crates do not depend on it;
drivers compose from outside and may instead pass civil evidence directly.

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

RFC 9112 and RFC 9931 are one effective HTTP/1.1 set. RFC 5322 Section 3.3 is
source-locked only for the calendar and year semantics inherited by HTTP-date.
RFC 1945 is an explicit
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
hop/connection/generation/exchange-bound sensitive proxy-credential type.
Capability constructors/fields are sealed, identities are engine-issued,
tokens are non-Copy/non-Clone and one-shot, and terminal/policy transitions
invalidate them even within the same generation; socket/runtime types never
imply transport security and proxy credentials are not Authorization.

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
HTTP/1 CONNECT 407 includes a validated challenge, discards owned pending
bytes, logically invalidates/releases credential capabilities, closes, and
retries only on a fresh connection; caller buffers remain caller-scrubbed. No
failed optimistic transition bytes are reparsed as HTTP.
CONNECT first authorizes lexical authority, then each caller-resolved endpoint
before dial, then validates the caller-certified actual peer and all attempt,
request, and policy generations before output/success/tunnel publication.
Builders attach no request content, hardened inbound framing rejects and
closes, successful server responses emit no length/transfer fields, and all
responses are non-cacheable.
HTTP/1 205 output is provably zero content; inbound 205 still follows ordinary
framing so nonzero content is drained-or-closed without pipeline desynchrony
and cannot be forwarded as a valid 205.
Trailers use a field-definition allowlist rather than a semantic-category ban:
`vef-core` provides ETag/Accept-Ranges field permission early, while local
authentication-info generation remains unavailable until `vef-auth` adds
scheme permission at v0.157.2. Received trailers possess no local capability,
stay separate/non-retroactive, receive a post-synchronization semantic/policy
disposition, and require destination-side permission before translation or
safe merge.
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
Preflight semantic field-section storage independently from compression
workspace and dynamic-table capacity. Materialize indexed/literal output into
immutable ordered bytes plus boundaries and sensitivity/never-index metadata;
never let it borrow table entries, scratch, or recyclable input/output. A
one-byte shortage finishes synchronization and selects bounded shutdown, never
truncation or partial semantics.
Parse SETTINGS early but integrate header-table, initial-window, admission, and
frame-size effects only after their owning components exist. Add borrowed DATA
events with partial acknowledgement and credit release, then the outbound
HEADERS/DATA/trailers/END_STREAM command lifecycle before general scheduling.
Stream flow control introduces signed available/reserved/committed accounting;
connection flow control composes one atomic dual reservation; INITIAL_WINDOW_SIZE
changes revoke paired unexposed reservations before an all-or-nothing delta;
outbound commands choose exact payload/padding then reserve before exposure.
Keep policy disposition orthogonal to the RFC stream state and reset-output
progress/reason/reservation, remote-closure record, first-closure cause,
terminal state/semantic stage, and active block. Normalize HEADERS/DATA,
remote END_STREAM, peer reset, fully acknowledged local END_STREAM, and fully
acknowledged local reset separately. Local END_STREAM command acceptance seals
later application sends without changing wire state; full carrying-frame
acknowledgement moves Open to half-closed(local) or half-closed(remote) to Closed.
Normalized inbound HEADERS+END_STREAM or a fully acknowledged outbound carrying
HEADERS can transition while fragmented CONTINUATION still owns HPACK;
half-closed(local) rejected DATA+END_STREAM uses
normal discard credit before closure; reserved(remote) DATA remains connection
PROTOCOL_ERROR. HPACK completion transfers PendingFieldBlock plus one sealed
`TerminalFieldSectionLease` to the first semantic stage, never Valid, and frees
only `CompressionWorkspace`; v0.125.0–v0.131.0 carry the exact lease without
reparse. Only the final owner transfers it to unpublished message state. Any stage can
re-arm the same slot as PROTOCOL_ERROR only before reset exposure. Peer reset
aborts pending semantics, but an active block first drains HPACK; GOAWAY alone
does not abort. First non-empty reset exposure freezes frame identity/bytes;
acknowledge by generation token, resume only at the exact suffix, and never emit
another reset. Prefixes 0..=12 do not change wire state; acknowledgement 13
applies one local close only if the stream is not already remotely closed.
For ordinary output, peer/local reset supersedes only AcceptedPrivate outside a
committed block. Before initial exposure, supersede the entire Private HEADERS/
PUSH_PROMISE block or none of it. First initial exposure commits every remaining
CONTINUATION through END_HEADERS; controls and other streams wait even when the
next continuation is still AcceptedPrivate. Frozen output—including zero
acknowledged—retains its arena slot/debit, finishes the exact frame before reset
serialization, and executes its completion hook once. Transport failure may
abandon the block only with the connection; an initial HEADERS END_STREAM hook
still fires at that frame's completion.
Malformed/abort release semantic leases once and fatal input owns
acknowledged-prefix cleanup without an incomplete close. Drive every
ownership/stage/event/output product through the model/fuzz table.
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
before emitting its SETTINGS ACK. Push admission requires a complete known-safe
and cacheable content/trailer-free request plus connection-bound TLS,
caller-certified cleartext, or configured-proxy authority evidence;
client-originated push is a connection error, promised semantic failure is
isolated to the promised stream, reserved slots/work are bounded separately,
reservation is legal at peer concurrency zero, and concurrency applies only
when the promised response opens. Sender/receiver associated-state,
ID/GOAWAY/opening commit is atomic. Keep validated promised input/provenance and
the slot rollback-capable until publication; rejection changes policy in place
without pretending its reserved(remote) wire state is closed. Retain a locally
reset associated stream's tombstone long enough to decode and reject an
in-flight PUSH_PROMISE without recreating application authority; illegal IDs and
HPACK failures retain connection scope. v0.181.0 atomically adds the invalidation
handle, independently leased pushed provenance, and rejection/cutoff capacity at
this gate. Non-cacheable responses are unstorable.
Retain independent budgets, mandatory ACK tracking, reserved output, and flood
defenses.

### Phase 4 — Proxy, client, server, and public APIs (`0.155.0`–`0.199.0`)

Build a representation-only translation IR, then effective URI and cache-safe
hop stripping as v0.157.0. v0.157.1 adds exact append-only Via; it parses bounded
ordered members/comments, records the inbound protocol/version, appends a
caller pseudonym after capacity preflight, never replaces/combines, applies to
every proxy-forwarded message and gateway inbound forwarded request, and uses
caller-owned privacy/loop policy without input-derived identity. v0.157.2 adds
the separate dependency-free, no_std `vef-auth` crate for scheme-neutral
challenge, credentials, token68, auth-param and six origin/proxy fields,
including comma ambiguity, BWS, quoted escapes and strict limits without
Basic/Digest implementations. Secrets remain borrowed/caller-owned; VEF
guarantees logical invalidation/reference release/redaction/non-indexing, while
the caller scrubs physical buffers. v0.157.3 consumes proxy credentials at the
expecting hop, removes them before origins, and relays them only by named-next-hop
cooperative policy. They are never confused with Authorization; proxy
challenges/info are scoped back only to the next client and every 407 is
challenged. All proxy-auth fields are redacted/never-indexed/TRACE-excluded,
and credentials are logically invalidated across retry.
v0.157.4 adds checked civil time in core and an optional I/O provider, keeps it
separate from monotonic deadlines, defines Available/Unavailable origin and
forwarding Date policy, Last-Modified clamping/external assignment, and the RFC
850 complete-instant 50-year rule without global clock ownership; generic
civil years precede 1900 but validated HTTP dates do not. No-RTC Aesynx stays
supported. v0.157.5 then creates dependency-free `vef-media-type`; generic
syntax preserves duplicate parameters and empty slots, while v0.158.0 consumes
separate conservative generated field/generation evidence for OPTIONS content,
so no interim Content-Type parser enters HTTP or role code.
Then build the normative HTTP/1↔HTTP/2 matrix before destination bytes and add
Max-Forwards, TE: trailers, bounded Structured Fields micro-stops, complete
bare-item dispatch in the optional `vef-structured-fields` crate,
ENABLE_CONNECT_PROTOCOL and NO_RFC7540_PRIORITIES owner integration, complete
priority/intermediary/flood behavior, replayability-aware retry tokens,
RFC 9651 duplicate-overwrite and mandatory-minimum profiles, exact HTTP/2
PRIORITY_UPDATE rules, compression-principal-aware coalescing,
authenticated coalescing inputs, exact transition byte handoff, role facades,
fixed storage before `alloc`, diagnostics, interop, fuzzing, and soak.
Before the origin role facade, v0.180.1–v0.181.2 create dependency-free
`vef-conditions` and v0.180.5 integrates the existing `vef-media-type`:
civil-aware validators, RFC-ordered evaluation before request
content, separate pre-action evidence and retrieval-only 200 snapshots, bounded
range parsing, sealed content/execution permits, final frozen client request
validation, exact RFC 2046-aware Content-Type classification, individual partial
segments, and fixed-capacity interval/header combination plans. Standalone 206
accepts a public preference but requires an engine-selected delivery permit; it
can stream without storage or a strong validator. Only opt-in exclusive-slice/
sealed-arena retention freezes bytes for assembly.
Trailer processing finalizes stored validators without changing head decisions.
Assembly contexts retain canonical Vary-selected equality bytes in immutable
request leases or structurally safe fixed caller storage with redaction, DMA
fencing, caller scrub ownership, and no digest/token substitution. They normalize once into
complete canonical storage plus provenance under profile caps, avoid redundant
sensitive raw copies, compare
semantic request/Vary/principal/privacy/navigation identities only after
validating request/response/storage provenance, reject `Vary: *`, acquire
non-aliasing output safely, and compare sorted overlaps only after activating a
profile-capped non-resettable budget. Conflicting bytes are quarantined with
zero output until complete replacement or a
destroyed-and-new different-validator representation context. Correlation
admission reserves a non-Copy/non-Clone target/principal/partition/navigation
invalidation handle from isolated per-shard capacity before local output. Push
admission instead finishes PUSH_PROMISE/CONTINUATION synchronization and all
semantics, derives identity only from the associated local request/caller policy,
then atomically preflights the promised slot, handle, independent minimal
immutable provenance lease/copy, and rejection/cutoff tracking before publication.
Local exhaustion produces zero-byte AssemblyInvalidationCapacity backpressure;
push capacity failure publishes no correlation, changes the provisional slot's
policy to rejecting, and queues mandatory-control stream-local CANCEL without
changing its wire state. Apply the Phase 3 frame matrix: synchronize legal
HEADERS and apply END_STREAM as a second transition while retaining fragmented
block ownership, make reserved(remote) DATA/duplicate IDs connection errors,
credit and terminal-validate half-closed(local) DATA before END_STREAM closure,
keep an unexposed policy reset dormant until valid release or malformed re-arm,
freeze it at first non-empty offer, continue only its acknowledged-cursor
suffix, preserve pre-completion wire legality through prefix 12, and give
tolerated closed-stream DATA connection credit only after remote closure or
full local-reset acknowledgement.
Unrepresentable tracking retains the slot through typed bounded shutdown.
Neither rotates an arena. The exact correlation holds its handle and
provenance independently of associated-stream teardown, buffer reuse, or later
policy changes through terminal-event backpressure and releases once; a retry
reserves independently. Completed 200
fallbacks invalidate by exact key or that namespace, widening only its coding/
domain children when refinement is unavailable; whole-arena rotation is limited
to internal invariant/trusted-storage corruption or caller policy, never peer
invalidity, conflict, or capacity, and is principal/tenant sharded. Disabling
assembly clears the shard before untracked admission.
Invalidation is immediately semantic, while slot reuse waits for all live body,
identity, and output leases and otherwise returns LeaseHeld. Header selection
uses the ordinal
minted when the correlation engine publishes each validated head. v0.183.0
exposes only the
read-only pending selection view before those permits and suppresses early 100,
body delivery, and method effects. A consumed unsafe execution permit survives
the mutation it authorized; its response uses fresh evidence. v0.182.1 consumes
the applicable evidence and retrieval snapshot and
validates the complete generated response matrix, including 401 over HTTP/1
and HTTP/2, 405, HTTP/1-only 426, hypothetical-200 metadata for 206/304, and
contextual 416.
It creates `vef-semantics`; both engines consume its exact frozen
`ValidatedResponse`, never a raw head beside a permit, so same-generation head
substitution, mutable aliasing, and facade/fixed/alloc/feature bypasses are
impossible. Engine-only validation/head reserve keeps mandatory responses
available after ordinary exhaustion or commits one zero-partial-output close.
Generated 206 is single-range only; received multipart remains opaque. Local
failure is zero-output InvalidState, received violations stay synchronized
under recipient policy, and forwarded responses preserve required fields.
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
closes both sides, while HTTP/2/RFC8441 FIN acceptance seals local sends and
only full acknowledgement of its END_STREAM-carrying frame enters wire
half-close; reverse traffic continues until both wire directions finish. Reset,
TCP error,
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
