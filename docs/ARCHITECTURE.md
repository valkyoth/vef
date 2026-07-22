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
  |-- vef-http1 -----> vef-core
  |-- vef-http2 -----> vef-core
  |       `----------> vef-hpack -----> vef-core
  |       `-- priority feature --> vef-structured-fields --> vef-core
  `-- vef-io

future runtime/TLS/Aesynx adapters -----> vef-io and protocol crates
```

The facade contains re-exports, not protocol implementation. Adapters point
inward; protocol crates never point outward. OS socket types, async-runtime
types, TLS-library types, boxed standard errors, and wall clocks cannot enter
protocol APIs.

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
`StatusCode` represents only 100..=599, including unregistered valid codes;
received 600..=999 digits survive only in typed invalid wire evidence for
client 5xx handling and can never enter valid server/serializer output.

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

Inbound body chunks remain borrowed until acknowledged. Drain, discard/close,
and cancellation are commands with explicit connection-reuse consequences.
Outbound request/response framing uses one state machine that checks body byte
counts, trailers, body-forbidden contexts, and completion before reuse.
Transfer-Encoding selection is role-specific: requests require final chunked,
whereas responses can be delimited by close when chunked is non-final or a
different coding is final. Repeated chunked is malformed; an unsupported valid
coding is a separate policy outcome. RFC 9931 CONNECT rejection always closes
and optimistic protocol bytes never re-enter HTTP parsing after failed handoff.
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
Translation first builds a protocol-neutral representation and emits no
destination bytes until effective URI, hop stripping, and the full framing
matrix validate. CONNECT/Upgrade handoff returns over-read bytes exactly once.

## Third-party boundary

The repository currently permits no third-party Rust crates. Planned Tokio,
Rustls, OpenSSL, and s2n integration names describe future boundaries, not
current dependencies. Admission requires explicit maintainer approval and a
release-plan update. Such crates remain optional, separately published, and
outward-facing so `vef`, `vef-core`, `vef-http09`, `vef-http1`, `vef-hpack`,
`vef-http2`, `vef-structured-fields`, and the base `vef-io` remain independent.
