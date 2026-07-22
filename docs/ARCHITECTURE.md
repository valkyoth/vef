# VEF Architecture

Status: foundation contract

## Design center

VEF is a family of deterministic sans-I/O protocol engines. A protocol call
must consume input, produce output, emit an event, or make an observable state
transition. Partial input and partial output are ordinary states. The caller
owns transport, scheduling, storage, backpressure, clocks, deadlines, TLS, and
application dispatch.

HTTP/1 and HTTP/2 deliberately do not share one universal connection trait.
They share semantic types, event and command conventions, limits, policies,
and diagnostics while retaining protocol-appropriate state machines.

## Dependency direction

```text
vef facade
  |-- vef-http09 ----> vef-core  (planned isolated compatibility package)
  |-- vef-websocket-handshake --> vef-core  (planned optional extension)
  |-- vef-http1 -----> vef-core + vef-media-type + vef-conditions + vef-semantics
  |-- vef-http2 -----> vef-core + vef-media-type + vef-conditions + vef-semantics
  |       `----------> vef-hpack -----> vef-core
  |       `-- priority feature --> vef-structured-fields --> vef-core
  `-- vef-io --------> vef-core

vef-auth -----------> vef-core
vef-media-type -----> vef-core
vef-conditions -----> vef-core + vef-media-type
vef-semantics ------> vef-core + vef-auth + vef-media-type + vef-conditions

future runtime/TLS/Aesynx adapters -----> vef-io and protocol crates
```

The facade contains re-exports, not protocol implementation. Adapters point
inward; protocol crates never point outward. OS socket types, async-runtime
types, TLS-library types, boxed standard errors, and wall-clock provider types
cannot enter protocol APIs; only checked core civil-time evidence crosses that
boundary.

## Storage modes

The first implementation path uses caller-provided buffers and fixed-capacity
stores with no global allocator. An `alloc` feature may later add owned values
after the caller-storage behavior is complete and audited. `std` belongs only
in explicitly separated adapters and convenience layers.

Phase 1 defines measurable stack, code-size, work, amplification,
fragmentation-cost, and fairness profiles. Components must fit an active
profile when introduced; final release campaigns replay whole-system limits.
Capacity exhaustion remains distinct from malformed peer input.

## Shared model

`vef-core` will own byte-oriented methods, status codes, versions, schemes,
authorities, four explicit request-target forms, ordered field lines, message
heads, trailers, limits, policies, roles, and structured diagnostics. Ordered
field lines remain authoritative: duplicate order is preserved and values are
never combined automatically.
Request-target and URI identity stores raw path separately from an optional raw
query. It distinguishes no query from an empty query, splits only on the first
`?`, preserves percent-encoded octets, and keeps decoded/normalized views out
of routing, forwarding, cache-key, and signature identity. Authority parsing
has explicit IPv6/IPvFuture, empty-port, userinfo, and malformed-bracket paths.
`ConnectAuthority` is stricter: bracket-aware host plus an explicit checked
port in 1..=65535, never a scheme default or Host-derived destination.
`StatusCode` represents only 100..=599, including unregistered valid codes;
received 600..=999 digits survive only in typed invalid wire evidence for
client 5xx handling and can never enter valid server/serializer output.
`vef-core` also owns protocol-neutral trailer-permission, raw message-head,
checked generic `UtcCivilTime`, narrower validated HTTP dates, and
available-or-unavailable complete-instant evidence types, but raw response
heads confer no serialization capability. Civil time is distinct from
monotonic deadlines and is always caller/adapter supplied.

`vef-auth` owns bounded scheme-neutral authentication grammar and sensitive
borrowed/caller storage. `vef-media-type` owns bounded dependency-free media
type/subtype/parameter syntax that preserves ordered duplicates and empty slots,
then separate generated-media and partial-response policies. Generic syntax
never assigns duplicate meaning; the generated policy validates OPTIONS content,
and neither layer parses multipart bodies. `vef-conditions` owns entity tags,
civil-evidence-aware HTTP dates, conditional-field evaluation, checked range
planning, final client request validation, individual partial segments, and bounded combination
plans. Its sealed pre-action evidence, retrieval-only snapshot, and outcomes
bind the exact request/exchange generation, civil time, and caller
representation evidence.
`vef-semantics` owns the full role/protocol response matrix. Its sealed
`ValidatedResponse` owns or immutably borrows the exact ordered head, framing,
sensitivity/indexing, body, and trailer plan; the internal emission capability
cannot be separated or paired with another raw head. Both HTTP engines consume
that complete frozen object before response-head output, every mutation needs
revalidation, no public raw-head serialization path exists, and body/trailer
commands remain bound to that response generation.

## HTTP/0.9 and HTTP/1 boundaries

The planned `vef-http09` package owns only the exact HTTP/0.9 grammar, explicit
client/server construction, and dedicated-listener policy. It has no automatic
fallback, proxy forwarding, pipelining, or persistent connection and is not
enabled by the facade's `http1` or `full` features.

`vef-http1` contains HTTP/1.0 and HTTP/1.1. Framing is decided exactly once
after complete field validation; malformed HTTP/1 is never reinterpreted as
HTTP/0.9.

The parser is an incremental byte-state machine. It does not decode the whole
message as UTF-8, reparse accepted bytes, scan without limits, allocate from a
peer length, or continue indefinitely without progress.
HTTP/1.1 requires exactly one syntactically valid Host, including an empty Host
when the target URI has no authority, but syntax alone is non-routable. Before
application publication, role policy authorizes target form and derives an
effective authority: origins accept origin/absolute, forward proxies require
absolute for ordinary requests, and reverse/interception origin-form requires
explicit destination context. Defaults are explicit and never inferred.
The same gate forms a complete EffectiveTarget using generation-bound
TrustedRequestContext: fixed listener, authenticated gateway, then adapter
transport security under explicit conflict policy. CONNECT admission is staged:
lexical ConnectAuthority authorization issues a ConnectAttemptToken; the caller
resolves and obtains per-endpoint policy; AuthorizedConnectOutcome then binds
the selected endpoint, actual peer, and attempt/request/policy generations
before output, 2xx, or tunnel publication. Core performs no DNS, dial, or socket
inspection. These capabilities have sealed fields, engine-issued identities,
are non-Copy/non-Clone and consumed once; every terminal/policy transition
invalidates outstanding values. Proxy credentials use a separate sensitive
hop/connection/generation/exchange type and can never become Authorization.

Inbound body chunks remain borrowed until acknowledged. For origin handling,
head validation publishes only a read-only `PendingConditionalRequest` for
representation selection; no 100 Continue, body publication/processing, or
method side effect occurs until matching pre-action evidence produces
non-forgeable content and execution permits. Terminal 304/412
drains-with-limits or closes without application body delivery, including bytes
already buffered behind the head. Drain, discard/close, and cancellation are commands with explicit
connection-reuse consequences.
Outbound request/response framing uses one state machine that checks body byte
counts, trailers, body-forbidden contexts, and completion before reuse.
Trailer admission uses a field-definition allowlist and generation-bound
permission from `vef-core`; authentication-info generation remains unavailable
until `vef-auth` introduces caller-certified scheme permission. Received
trailers never possess local Rust capabilities: they stay separate, receive a
post-synchronization semantic/policy disposition (including
RequiresSchemeAuthorization), never retroactively affect prior decisions, and
can be translated or merged only after destination-side authorization.
Transfer-Encoding selection is role-specific: requests require final chunked,
whereas responses can be delimited by close when chunked is non-final or a
different coding is final. Repeated chunked is malformed; an unsupported valid
coding is a separate policy outcome. RFC 9931 CONNECT rejection always closes;
a CONNECT 407 requires a valid proxy challenge, discards VEF-owned pending
bytes, logically invalidates/releases credential references, and retries only
on a fresh HTTP/1 connection; caller-owned buffer scrubbing remains external.
Optimistic bytes never re-enter HTTP parsing after failure.
CONNECT builders carry no content/framing fields; hardened inbound ambiguity
rejects and closes, successful server responses omit length/transfer fields,
clients ignore received ones, and every CONNECT response is non-cacheable.
205 serializers emit zero content. Inbound 205 retains ordinary framing, so
malicious nonzero content is boundedly discarded or forces close/reset before
reuse, emits a typed semantic violation, and is not forwarded as valid 205.
An HTTP response lifecycle has two terminal shapes: non-101 informational
responses followed by one final response, or one validated 101 after the full
request (and any required 100) commits. After 101, only the selected protocol
can consume or emit bytes. Chunk extensions accept RFC 9112 BWS around `;` and
`=`, charge raw BWS to limits, and trim it only for extension semantics.

The optional `vef-websocket-handshake` package owns RFC 6455 opening-handshake
mechanics and the success publication barrier, but no WebSocket frame protocol.
The cross-version gateway is bidirectional. HTTP/1-to-HTTP/2 retains the key
and generates the downstream accept locally after the RFC 8441 2xx; the reverse
direction obtains fresh caller entropy and validates the HTTP/1 upstream 101.
HTTP/2 never processes key/accept fields. ws/wss maps to http/https; Origin,
version, negotiation, cookies, and authorization remain validated end-to-end;
HTTP/2 names are lowercase. Settings advertisement requires an available
endpoint/bridge, failures stay independently HTTP-framed, and data handoff
waits for both sides to commit.

## HPACK and HTTP/2

`vef-hpack` owns checked integer, string, Huffman, table, and representation
codecs. It has no HTTP/2 stream or transport knowledge. Valid compression
state updates are never rolled back because later HTTP semantics reject a
stream; unsafe incomplete decoding closes the connection.
Encoder table mutation occurs only when the corresponding output bytes commit;
partial output, retry, or cancellation cannot advance it ahead of the peer.
Sensitive indexing uses typed directives and conservative defaults; received
never-indexed fields cannot be downgraded, secret values do not participate in
attacker-controlled indexing comparisons, and diagnostics remain redacted.
Caller-supplied compression-principal tokens tag private dynamic entries;
encoder lookup across principals is forbidden even for equal bytes, while
explicitly public entries may be shared and unknown provenance is non-indexed.
Provenance is immutable encoder-side metadata: it changes no entry size,
insertion, eviction, or index, skipped private entries retain their indices,
and eviction/reset removes entry data and provenance atomically.

`vef-http2` separates frame codec, connection/stream state, and HTTP semantic
mapping. Stream transitions are exhaustive. Header blocks are atomic across
CONTINUATION frames. Flow-control arithmetic uses protocol-domain integers,
never unchecked `usize` calculations. Independent budgets cover hostile
control-frame rates, compression work, stream churn, and outbound responses.
SETTINGS wire values are validated early, but mutations are integrated only
after the HPACK encoder, stream/window, admission, or scheduler owner exists.
Initial HTTP semantics validate before request/response mapping is published.
That initial barrier includes checked Content-Length and duplicates,
Host/:authority agreement, request-form pseudo-field matrices, three-digit
status validation, status 101 rejection, and trailer pseudo-field rejection.
Inbound DATA remains borrowed and releases stream and connection credit only
when acknowledged or explicitly discarded. Outbound HEADERS, DATA, trailers,
END_STREAM, partial HPACK/frame output, and cancellation share one per-stream
command lifecycle.
HTTP/2 `:path` is decomposed into the same raw path/optional-query identity and
reconstructed without normalization; an empty HTTP(S) path becomes `/` only in
the RFC-required contexts.
Native CONNECT DATA is never request content. v0.130 keeps it in fixed-capacity
PendingConnect while AwaitingConnectOutcome and uses a local-capacity CANCEL
when full, without flow-control, resolver, dialer, or socket claims. v0.133 and
v0.134 add stream/connection accounting, v0.136 adds acknowledgement/credit,
and only a generation-matched authorized endpoint/peer outcome permits tunnel
publication. Connected streams allow DATA/applicable management frames; caller
TCP failure produces CONNECT_ERROR and HTTP/2 failure requests upstream TCP
reset without unrelated-stream mutation.
Server push publishes only a complete known-safe/cacheable content-free and
trailer-free request under connection/generation-bound TLS, cleartext endpoint,
or configured-proxy authority evidence independent of coalescing. Client push
is connection PROTOCOL_ERROR; promised semantic failures reset only the
promised stream. Reserved pushes use their own slot/work budget and do not
count against MAX_CONCURRENT_STREAMS until the response opens; sender and
receiver associated-state perspectives, promised ID, GOAWAY and opening commit
atomically. Pushed response metadata forbids storage when non-cacheable.

Frame codecs validate their complete wire envelope before exposing fragments:
payload length, stream-zero rules, known/unknown flags, reserved bits, padding,
and optional-field minima. The connection then applies a typed RFC 9113 error
delta. A stream-scoped delta may touch only its target stream; compression
errors and connection-scoped violations stop publication and enqueue exactly
one bounded GOAWAY action.
For field-block frames, undersized mandatory priority/promised-ID layouts are
connection FRAME_SIZE_ERROR, invalid padding/identifiers are connection
PROTOCOL_ERROR, and HEADERS self-dependency is stream PROTOCOL_ERROR.

Unknown frames are bounded, incrementally drained, and state-neutral unless an
enabled extension owns their type; they cannot interleave an active field
block. Receive-credit accounting is separate from WINDOW_UPDATE emission so
discarded padding can be credited internally while output is coalesced under
rate and amplification limits. The scheduler preserves field-block
contiguity, mandatory-control capacity, unrelated-stream progress, and bounded
starvation across cancellation and SETTINGS changes.
Flood budgets independently charge streams/resets, SETTINGS, PING,
CONTINUATION, WINDOW_UPDATE, unknown frames, HPACK work, and control output
before work, never refund Rapid Reset, refill from injected monotonic time, and
optionally consult a caller-shared cross-connection admission hook.
An inbound HPACK block always reaches a synchronization-safe terminal state.
RST_STREAM, refusal, or cancellation cannot abandon it; synchronization-only
decode exposes no fields, and insufficient continuation/work/storage capacity
selects bounded connection shutdown instead of REFUSED_STREAM.

The planned dependency-free `vef-structured-fields` crate owns RFC 9651
lexing, item/container grammars, canonical serialization, and bounded
caller-owned incremental storage. Its lexical dispatcher skeleton precedes
the item grammars; complete bare-item dispatch is claimed only after every
item type exists. HTTP/2 priority code consumes its typed output.
RFC-conformant profiles implement duplicate overwrite and mandatory RFC 9651
minimum capacities; smaller bare-metal profiles are explicitly constrained and
capacity exhaustion is never reported as malformed syntax. HTTP/2
PRIORITY_UPDATE owns only type 0x10 and its request/push stream state matrix.
That matrix is receiver-server-relative throughout: valid push targets are
reserved-local and half-closed-remote, closed targets are discarded, and idle
push targets are connection PROTOCOL_ERROR.

SETTINGS mutations occur atomically before the corresponding ACK is emitted.
ENABLE_PUSH is integrated by push ownership, ENABLE_CONNECT_PROTOCOL by the
extended CONNECT boundary, and NO_RFC7540_PRIORITIES by the priority-mode
state machine with its initial-SETTINGS-only rule.
Extended CONNECT owns two directional states: peer-enabled outbound initiation
and committed local inbound advertisement. Only 0/1 is valid, server receipt
does not enable outbound use, local advertisement takes effect at byte commit,
and value 1 is irreversible for the connection; later service failure is an
HTTP outcome, never SETTINGS rollback.
Authenticated exact `h2` ALPN is the only encrypted HTTP/2 selector. Cleartext
prior knowledge requires explicit caller policy or a dedicated endpoint; the
engine never sniffs, guesses a fallback, reuses failed-selection bytes, or
changes protocol after preface processing begins.

## Roles and transitions

Client, origin server, forward proxy, reverse proxy, gateway, tunnel endpoint,
and intermediary policies are explicit. CONNECT and Upgrade do not expose
post-transition bytes until success is confirmed. TLS adapters return
authenticated protocol-selection metadata; they never mutate an established
HTTP engine into a different protocol.
TLS/runtime adapters also expose authenticated origin inputs needed for safe
HTTP/2 coalescing; connection-pool policy remains outside VEF.
Brynja and Aesynx adapters additionally supply generation/connection-bound
TrustedRequestContext transport-security and configured scheme metadata; core
never derives TLS state from an adapter, handle, or socket type.
Translation first builds a protocol-neutral representation and emits no
destination bytes until effective URI, hop stripping, and the full framing
matrix validate. CONNECT/Upgrade handoff returns over-read bytes exactly once.
Checked civil-time evidence is injected directly or through optional
`vef-io::CivilClock`; origins and forwarding recipients apply explicit
Available/Unavailable Date and Last-Modified rules, including RFC 850 rollover,
without reading a global clock. Aesynx systems without an RTC report
Unavailable, while monotonic deadlines remain independently usable.
The dependency-free `vef-auth` crate parses/serializes bounded scheme-neutral
challenge, credentials, token68 and auth-param grammar for all origin/proxy
authentication fields, preserving field/challenge boundaries and resolving
comma/parameter ambiguity without Basic/Digest logic. Values remain borrowed
or caller-owned; invalidation releases references and guarantees no diagnostic
or HPACK disclosure, while physical buffer scrubbing remains the caller's duty.
Via is a bounded ordered grammar and always appends—never replaces or combines—
the inbound protocol/version plus caller-configured privacy pseudonym after
capacity preflight; every forwarded proxy message and gateway inbound request
uses caller-owned self-pseudonym loop policy. The expecting proxy consumes
hop-scoped Proxy-Authorization before origin forwarding; only explicit named
cooperative next-hop policy can relay it. Proxy challenges/info return only to
the next client, every generated 407 has a `vef-auth`-validated challenge, and
all proxy-auth fields are sensitive, redacted, never-indexed, and TRACE-excluded.
Before any generated response bytes, `vef-conditions` parses entity tags and
HTTP dates, evaluates conditional fields in RFC order before request content,
and performs bounded checked Range/Content-Range arithmetic. Sealed
`CurrentRepresentationEvidence` records pre-action existence, identity,
validator, and modification time for every conditional method; retrieval-only
`WouldBe200Snapshot` adds exact 200 selection, Date, and ordered metadata for
GET/HEAD range, 206, and 304 validation. A consumed one-shot execution permit
survives the mutation it authorizes, while response construction uses fresh
post-action evidence. A role-aware semantic gate then consumes those sealed
generation-bound outcomes and validates the complete
method/status/field/content matrix: 401 challenges over both protocols, 405
Allow, protocol-specific 426, and contextual 206/304/416 are explicit. HTTP/2
cannot generate 426; HTTP/1 426 cannot translate by stripping Upgrade.
Generated 206 is single-range only for 1.0; the shared bounded media-type parser
classifies received multipart/byteranges, which remains opaque and forwardable,
never parsed or generated. Exact multipart with a missing/invalid RFC 2046
boundary, malformed/duplicate Content-Type, or stale field evidence grants no
partial capability, and multipart never grants top-level Content-Range authority.
Outbound conditional/range requests receive the same final frozen validation
over typed or generic fields before either engine serializes them. Client 206
classification consumes the sealed media-type result, checks Content-Range and
request/validator identity, then publishes a generation-bound validated head.
Before body consumption the caller supplies a freely constructible delivery
preference; the engine validates it and issues the sealed generation-bound
StreamOnly, RetainOnly, or StreamAndRetain permit. Retention commits before publication and acknowledgement.
Borrowed accounted chunks can stream to the application with no retained
storage; terminal standalone proof does not require a strong validator. Optional retention safely converts an
exclusive slice/sealed-arena write into an immutable transfer-decoded but
content-encoded `StoredPartialSegment`; only this stored form can combine.
Combination eligibility waits through validated trailers, which may supply
ETag but cannot change range/domain or the head-published ordinal. A
generation-safe assembly context compares an engine-derived semantic variant
identity from bounded Vary, exact original-request values, principal, privacy
partition, and navigation identity. Unnormalized equality bytes can live in an
immutable original-request lease; normalized canonical output lives in engine-
written exclusive-slice/sealed-arena caller storage;
there is no alias/trust constructor, truncation, digest authority, or opaque-token
substitution. DMA remains fenced for the lease, sensitive values stay redacted,
and callers scrub copied values after release. Sealed semantic normalizers run
once under profile-capped work/output accounting and store complete canonical
bytes plus provenance; unnormalized raw bytes are already canonical, and no
second sensitive raw copy is retained merely for equality. Candidate
comparisons never parse again. Each segment
separately carries fresh request/response/storage provenance evidence; releasing
storage invalidates admission, while generations
never enter identity equality. Coding/domain, length, and strong-validator
constraints still apply, and `Vary: *` never matches. Physical storage
generation stays in leases, not semantic replacement identity. Output comes
from safe non-overlapping splitting or a separate arena, and completed same-key
200 invalidates across arena generations. A public requested overlap budget is
validated before work into a sealed plan-bound active budget capped by the
resource profile; sort/comparison charging cannot reset or enlarge. Equal
overlaps deduplicate, while unequal bytes
emit no output, return `ConflictingPartialContent`, and quarantine the full
context and validator association. Only complete same-key 200 replacement or
destruction followed by a different-validator/new-generation empty context can
clear it; 304, unchanged revalidation, and separate selection contexts cannot.
At correlation admission, assembly-enabled requests reserve an engine-only,
non-forgeable target/principal/partition/navigation invalidation handle that
optional peer-driven work cannot consume. When a completed 200 lacks an exact
variant key because of Vary `*`, capacity, normalization, or released storage,
the handle invalidates every Vary/validator sibling in that namespace; absent
coding/domain refinement widens only across those children. Whole-arena rotation
is limited to mandatory-reserve failure, internal corruption, or explicit caller
policy, and arenas are principal/tenant sharded. Key loss never leaves an older
potentially replaced context usable. Semantic invalidation immediately rejects
stale capabilities, but arena rotation never ends a Rust lifetime: storage is
physically reclaimable only after all body, identity, and output leases drop or
acknowledge, otherwise allocation returns local LeaseHeld/capacity.
Multipart and unknown units remain outside recombination.
The gate freezes the exact validated response; serialization never accepts a
raw head beside a permit. Engine-only semantic slots and frozen-head storage
are reserved for mandatory responses and cannot be consumed by application
work; reserve failure commits one deterministic close/shutdown action without
partial response output.
Local invalid construction is zero-output InvalidState; received semantic
violations remain framing-synchronized under recipient policy; intermediaries
preserve end-to-end response fields except already-authorized transformations.
TRACE/OPTIONS applies Max-Forwards without synthesis, keeps zero local, blocks
generated TRACE content/secrets, bounds and sanitizes reflection, validates
OPTIONS Content-Type with content, and marks both response types non-cacheable.
Absolute empty-path/no-query OPTIONS stays absolute through intermediate
forward proxies and maps to `*` only at the final origin-facing hop; an empty
query or `/` stays resource-specific across HTTP/1 and HTTP/2.
Tunnel closure is protocol-specific. HTTP/1 EOF drains already-owned bytes then
closes both connections; HTTP/2/RFC8441 END_STREAM forwards directional FIN and
keeps reverse traffic legal until both directions finish. Resets/fatal errors
abort both, injected half-close timeout bounds stalls, and HTTP reuse is never
restored.

## Third-party boundary

The repository currently permits no third-party Rust crates. Planned Tokio,
Rustls, OpenSSL, and s2n integration names describe future boundaries, not
current dependencies. Admission requires explicit maintainer approval and a
release-plan update. Such crates remain optional, separately published, and
outward-facing so `vef`, `vef-core`, `vef-http09`, `vef-http1`, `vef-hpack`,
`vef-http2`, `vef-auth`, `vef-semantics`, `vef-structured-fields`, and the base
`vef-io` remain independent.
