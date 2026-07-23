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

Sans-I/O output has one irrevocable boundary: first non-empty exposure to the
caller. Private encoding before exposure may be replaced; exposure first freezes
the exact bytes and semantic identity in bounded engine storage. A sealed
generation-bound token owns one offered range, and consuming it acknowledges an
exact zero/short/full prefix. A zero write advances nothing but consumes that
token; invalid or replayed tokens are state-neutral. Acknowledgement governs
only suffix progress and reclamation—never byte mutation. Outstanding tokens
pin their record and owning protocol generation; connection failure records only
the acknowledged prefix.

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
Encoder work occurs in one serialized provisional transaction per field block.
Private rollback discards it; first frame exposure commits only framing; full
acknowledgement of the END_HEADERS frame atomically publishes encoder table
mutation as HpackCommitted. No later block encodes against provisional entries,
and partial output, retry, or cancellation cannot advance state ahead of the peer.
Every validated non-ACK SETTINGS frame owns one connection-wide
`InboundSettingsTransaction`: ordered entries, a generation, one reserved ACK,
participant obligations, and
`SettingsDisposition::{WaitingParticipants, AckEligible, AckFrozen {
acknowledged: 0..=8 }, AckCommitted, AbortedConnection}`. The whole frame
validates before ACK reservation or mutation; entries apply in wire order
without intervening dispatch. HPACK, windows, frame size, admission, push, and
extensions report generation-bound Effective/fatal results to this shared
owner. All-effective transactions become AckEligible, ACK output freezes the
exact nine-byte frame, and only final-byte commitment produces AckCommitted.
Transactions and dependent owner references remain live through that boundary,
with FIFO serialization and commitment across received frames. Fatal or
transport failure before byte nine abandons the connection without exposing
dependent output, so no component can race or overstate an ACK.
Peer HEADER_TABLE_SIZE uses
`PendingEncoderTableSizeTransition::{None, AwaitingSafeApply { .. },
AppliedAwaitingAckCommit { owners, smallest_seen, final_value }}` and never owns
ACK authority. Separately, linear `EncoderTableUpdateDebt {
smallest_since_last_exposed_block, final_value }` preserves every unsignaled
encoder-limit change. No-active applies the transition; Private first rolls
back its provisional transaction and returns any exact debt lease;
FramingCommitted drains/publishes first. Applying a transition makes HPACK
participants effective, but its values merge into existing debt only after all
owning ACKs commit, retaining the older minimum. ACK commitment never clears
debt. Private encoding leases—rather than consumes—the exact debt and emits its
one or smallest-then-final prefix. Rollback returns that lease before newer
settings merge. First non-empty initial-frame exposure irreversibly transfers
the debt to FramingCommitted, whose pre-reserved block must finish; settings
received after exposure create debt for the following block. Partial ACK output,
stale tokens, or transport failure cannot expose a dependent block, while
connection abandonment is the only escape after debt transfer.
Sensitive indexing uses typed directives and conservative defaults; received
never-indexed fields cannot be downgraded, secret values do not participate in
attacker-controlled indexing comparisons, and diagnostics remain redacted.
Caller-supplied compression-principal tokens tag private dynamic entries;
encoder lookup across principals is forbidden even for equal bytes, while
explicitly public entries may be shared and unknown provenance is non-indexed.
Provenance is immutable encoder-side metadata: it changes no entry size,
insertion, eviction, or index, skipped private entries retain their indices,
and eviction/reset removes entry data and provenance atomically.
Decoder ownership is split explicitly. `CompressionWorkspace` owns encoded
fragments, integer/Huffman scratch, and CONTINUATION assembly and is releasable
after HPACK synchronization. Independently preflighted `TerminalFieldSection`
storage owns immutable decoded bytes, ordered boundaries, duplicates/empty
values, pseudo classification, sensitivity/never-index provenance, and stream/
generation binding. Indexed fields are materialized or independently leased;
semantic spans never borrow dynamic-table entries, compression scratch, or
recyclable caller buffers, so eviction and table-size changes cannot alter them.

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
command lifecycle. Accepting an END_STREAM-bearing command seals the local
application send direction but does not mutate RFC wire state. Only full-frame
acknowledgement emits `LocalEndStreamComplete`: Open becomes half-closed(local),
or half-closed(remote) becomes Closed. Partial output and failure claim neither;
HEADERS completion performs the transition even when CONTINUATION/HPACK
ownership remains live until END_HEADERS.
Ordinary frames retain an explicit AcceptedPrivate/Frozen/Complete/
SupersededBeforeExposure disposition. Peer or completed local reset can discard
only AcceptedPrivate bytes that do not belong to a framing-committed field block and
release their unexposed credit. Before any initial HEADERS/PUSH_PROMISE byte is
exposed, the engine fully encodes the bounded field block and atomically
materializes/reserves every HEADERS/CONTINUATION slot and queue entry using the
checked minimum of 16,384, local `max_outbound_frame_payload`, and slot payload
capacity. The cap must fit each enabled initial-frame mandatory prefix;
`max_outbound_field_block_bytes`, checked ceiling division, and
`max_outbound_continuations_per_block` bound encoded bytes and entries. Any shortage
leaves the whole Private block supersedable with zero exposure. First non-empty
initial-frame exposure creates a connection-scoped FramingCommitted obligation
through END_HEADERS: every remaining CONTINUATION is already owned and
non-supersedable even while individually AcceptedPrivate, and RST_STREAM,
GOAWAY, required control replies, and other streams wait. Its provisional HPACK
encoder transaction remains unpublished and blocks later field-block encoding;
only full acknowledgement of the END_HEADERS frame publishes HpackCommitted.
Oversized locally generated fields fail as typed local capacity/validation,
never partial output or peer error.
Transport failure abandons that transaction/block only with the whole
connection and emits no interleaved GOAWAY. The initial HEADERS END_STREAM hook
still runs at that frame's full acknowledgement, independently of final HPACK
commit. Outside that obligation, first non-empty
exposure freezes the exact frame even after a zero acknowledgement; its suffix
owns connection framing and must finish before a same-connection RST_STREAM,
then its completion hook runs once without overwriting peer-first closure.
Outbound DATA uses an atomic dual ledger: exact payload including Pad Length and
padding, but excluding the nine-byte header, moves from stream+connection
available to reserved-unexposed before exposure and to committed-debited at
first exposure. Unexposed supersession or SETTINGS reconciliation releases both
reservations; frozen debit is never refunded. Negative stream windows block new
exposure, and zero-length END_STREAM DATA consumes zero credit. Exact DATA
frames are copied into exclusive generation-checked slots in one caller-provided
fixed-capacity `OutboundFrameArena`; source payload may be released after the
copy, but staged bytes cannot be accessed, mutated, or reused until
supersession, full acknowledgement, or connection cleanup. Segmentation uses
the minimum of peer MAX_FRAME_SIZE, nonzero local
`max_outbound_frame_payload`, both available credits, and remaining padded
payload, and every slot proves checked capacity for its nine-byte header plus
that local maximum. DATA derives application length only after checked
subtraction of the optional Pad Length octet and padding; padding that cannot
fit follows a deterministic reduction policy or local backpressure, never
overflow or silent data truncation. Peer limits never dictate local allocation.
Queue-byte and queue-entry capacity are independent, and exhaustion is typed local
`OutboundFrameStorageCapacity` backpressure rather than a peer error.
Every scalar or vectored offer token owns exactly one immutable frame-slot
suffix. Acknowledgement cannot cross into another slot or batch completion
hooks; overflow is `InvalidState` without mutation.
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
atomically. The validated request and trusted push-policy provenance remain in
an unpublished rollback-capable admission transaction. The v0.117.0 stream slot
contains its rejection/cutoff representation, so an accepted promised ID is
continuously tracked—never idle again—but policy rejection is orthogonal to its
RFC wire state and reset serialization. A rejected promise remains
reserved(remote) until normalized HEADERS moves it to half-closed(local), then a
separate END_STREAM event, peer reset, or acknowledgement of the complete local
RST_STREAM can close it.
HEADERS+END_STREAM performs both transitions even when END_HEADERS is absent;
the closed wire state does not release the remaining CONTINUATION/HPACK owner.
Rejected half-closed(local) DATA+END_STREAM accounts/discards its full payload
and padding before closure. Reserved(remote) DATA and reuse of its non-idle ID
are connection PROTOCOL_ERROR; DATA tolerated only after actual closure restores
only connection credit and never emits stream WINDOW_UPDATE. Terminal validation is
an independent sealed state machine: NotTerminal, PendingFieldBlock(disposition),
PendingSemantics { stage, fields: TerminalFieldSectionLease }, Valid, Malformed(code), or
AbortedByPeerReset. HPACK completion atomically seals and transfers the decoded
section while releasing only compression workspace, never directly marking
Valid; monotonic stages cover pseudo/connection fields, field and
context checks, request/response mapping, content/phase, and trailer/role rules.
Peer reset supersedes an unexposed reserved action, aborting pending semantics immediately
or after an active block finishes HPACK, with no later publication. END_STREAM
instead makes a reserved, unexposed policy CANCEL dormant through every stage;
only the
final semantic owner transfers the immutable section to the unpublished event,
while malformed/abort release it once and fatal shutdown owns cleanup. Reset
output is mutable only while reserved and unexposed. First non-empty exposure
freezes all 13 RST_STREAM bytes, reason, stream token, and output generation;
later semantic/peer events cannot replace it. Valid token acknowledgements move
one cursor, positive progress resumes at the exact suffix, and stream/tombstone
reuse waits for token completion or acknowledged-prefix failure cleanup.
A reserved reset and a frozen reset acknowledged through byte 12 leave the RFC
wire state unchanged, so every inbound frame still uses the prior
reserved/open/half-closed legality and credit rules. Acknowledging byte 13
records output completion and applies one local-reset transition to Closed only
if remote END_STREAM or peer RST_STREAM did not close it first. Remote closure
is retained independently. `FirstWireClosureCause` distinguishes completed
local reset, completed ordinary local END_STREAM, peer reset, and a remote
END_STREAM that actually performed the final close; an END_STREAM received in
Open only creates half-closed(remote). Immutable first-closure attribution is
never overwritten by later local completion; the frozen suffix still completes
while the connection is usable. Partial-prefix connection failure performs cleanup
without claiming reset completion or a local wire transition.
A generation-checked associated-stream tombstone
also accepts an in-flight PUSH_PROMISE after completed local reset: it completes
every CONTINUATION and validates/tracks the promised ID but publishes no request
or reconstructed authority. Missing recycled provenance selects safe rejection,
while illegal IDs and malformed HPACK preserve connection-error scope.
One total `RejectedPushFrameDisposition` matrix keys these decisions by policy,
wire state, reset progress/reason/reservation, terminal state/semantic stage,
closure cause, normalized event/END flags, header-section phase, and field-block
ownership; every cell fixes ordered transitions, HPACK/stage/abort action,
flow-credit, cleanup ownership, publication, and reset dormancy/re-arm/release/
serialization. Private constructors forbid terminal results with active blocks,
NotTerminal with dormant reset state, and caller-forged stage movement.

Once partial assembly exists at v0.181.0, a receiving client completes
PUSH_PROMISE/CONTINUATION and HPACK/semantic/authority/cacheability validation,
then atomically preflights the slot, correlation-bound invalidation handle,
independent pushed provenance, and rejection/cutoff capacity before publication.
The provenance copies or independently leases minimal immutable target/
principal/partition/tenant/navigation/policy/arena-generation evidence from the
promised request and associated caller policy; it never borrows recyclable
associated-stream storage. Associated-stream teardown/reuse and later policy
changes cannot mutate it, and each promised stream owns its lifetime. Handle/
provenance failure changes only policy disposition to rejecting and queues
CANCEL under the same wire/reset matrix. If rejection tracking cannot be
represented, the slot remains tracked through typed bounded connection
shutdown. Pushed response metadata forbids storage when non-cacheable.

Frame codecs validate their complete wire envelope before exposing fragments:
payload length, stream-zero rules, known/unknown flags, reserved bits, padding,
and optional-field minima. The connection then applies a typed RFC 9113 error
delta. Policy disposition, RFC wire state, and reset-output progress are separate
generation-checked dimensions; every frame validates/commits its wire transition
before policy controls publication. A stream-scoped delta may touch only its
target stream; compression errors and connection-scoped violations stop
publication and enqueue exactly one bounded GOAWAY action.
Terminal stream validation can replace an uncommitted policy reset but cannot
alter partially committed bytes; connection-fatal compression errors override
future stream actions without rolling back HPACK or wire state.
For field-block frames, undersized mandatory priority/promised-ID layouts are
connection FRAME_SIZE_ERROR, invalid padding/identifiers are connection
PROTOCOL_ERROR, and HEADERS self-dependency is stream PROTOCOL_ERROR.

Unknown frames are bounded, incrementally drained, and state-neutral unless an
enabled extension owns their type; they cannot interleave an active field
block. Receive-credit accounting is separate from WINDOW_UPDATE emission so
discarded padding can be credited internally while output is coalesced under
rate and amplification limits. The scheduler preserves inbound field-block
contiguity and treats a FramingCommitted outbound field block as its highest
framing obligation through final END_HEADERS acknowledgement; its complete
slot/entry set was pre-reserved, while mandatory-control capacity remains reserved
while serialization waits. Outside that obligation it preserves
unrelated-stream progress and bounded starvation across cancellation and
SETTINGS changes.
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
Before output or correlation creation, assembly-enabled locally initiated
requests reserve an engine-only, non-Copy/non-Clone target/principal/partition/
navigation invalidation handle bound to that exact correlation; accepted push
reserves the same capability plus independent immutable
`PushedAssemblyProvenance` at its post-HPACK prepublication gate. Optional
peer-driven work and other shards cannot consume its fixed per-shard pool.
Local exhaustion returns AssemblyInvalidationCapacity with zero request bytes/
no correlation and ordinary Sans-I/O backpressure; push capacity failure
publishes no promised request/correlation and uses the continuously tracked
rejection/shutdown path above. Neither rotates an arena or admits an untracked
request. The handle/provenance survives informational responses and terminal-
event backpressure, releases exactly once at final completion/cancellation/reset/
connection failure/retry disposition, and cannot be duplicated or rebound for a
retry. Associated-stream closure or storage reuse cannot affect pushed evidence.
Per-shard/per-connection admission limits bound stalled handles. When a
completed 200 lacks an exact variant key because of Vary `*`, capacity,
normalization, or released storage,
the handle invalidates every Vary/validator sibling in that namespace; absent
coding/domain refinement widens only across those children. Whole-arena rotation
is limited to an internal invariant/trusted-storage integrity failure or explicit
caller policy. Malformed, semantically invalid, or conflicting peer input and
capacity never mint a corruption cause, and arenas are principal/tenant sharded.
Intentionally disabling assembly first
rotates/clears the shard generation before any untracked request is admitted.
Key loss never leaves an older potentially replaced context usable. Semantic
invalidation immediately rejects
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
