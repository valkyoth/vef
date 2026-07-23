# VEF Scope

Status: policy

VEF 1.0.0 implements shared HTTP semantics, explicit HTTP/0.9 compatibility,
HTTP/1.0, HTTP/1.1, HPACK, and HTTP/2 for client, server, intermediary, proxy,
gateway, and tunnel roles. It provides protocol engines and runtime-neutral
I/O contracts, not an opinionated application framework.

## Normative scope

| Area | Specification | 1.0 disposition |
| --- | --- | --- |
| Requirement language | RFC 2119 and RFC 8174 | Applied to requirement ledger |
| HTTP/0.9 and HTTP/1.0 | RFC 1945 | Explicit historical profiles; HTTP/0.9 is an isolated package |
| URI syntax | RFC 3986 | Validated components without implicit normalization |
| Media types | RFC 2046 plus RFC 9110 | Bounded grammar and multipart boundary classification; no multipart body parser |
| WebSocket opening handshake | RFC 6455 | Optional isolated handshake extension; no frame protocol |
| ALPN | RFC 7301 | Adapter selection metadata |
| HPACK | RFC 7541 | Complete bounded encoder and decoder |
| TLS 1.3 context | RFC 8446 | Provider metadata and HTTP/2 prerequisite checks |
| Internet Message Format date semantics | RFC 5322 Section 3.3 | HTTP-date calendar semantics and year floor only |
| Shared HTTP semantics | RFC 9110 | Declared roles and message semantics |
| HTTP caching | RFC 9111 | Preserve required information; no cache store in core |
| HTTP/1.1 | RFC 9112 plus RFC 9931 | Full messaging and current transition security update |
| HTTP/1.1 CONNECT-UDP | RFC 9298 | Not applicable unless a dedicated profile enters scope |
| HTTP/2 | RFC 9113 | Frames, states, mapping, flow control, push, errors |
| Modern priorities | RFC 9218 | Optional scheduler information and wire behavior |
| Structured Fields | RFC 9651 | Required by modern priority support |
| Extended CONNECT | RFC 8441 | Optional HTTP/2 extension |

The conformance promise is requirement-specific: every applicable MUST and
MUST NOT is linked to code and tests; every applicable SHOULD and SHOULD NOT is
implemented or has a reviewed decision.

## Outside VEF 1.x

HTTP/3, QUIC, TCP/UDP implementations, TLS implementations, certificate
validation, DNS, cache storage, cookie jars, redirect policy, connection-pool
policy, proxy discovery, content compression, WebSocket frames, HTML/forms,
general-purpose multipart parsing/generation, routers, templates, server
binaries, and CLIs are out of scope. VEF 1.0 generates only single-range 206;
its reusable bounded media-type syntax preserves ordered duplicate parameters
and empty slots; separate generated-content and partial-response policies later
classify Content-Type, including required RFC 2046 boundary grammar, while
received multipart/byteranges bodies remain opaque bytes that can be preserved
and forwarded without boundary or part validation. VEF parses entity tags,
HTTP dates, conditional fields, Range, and Content-Range and evaluates them
against explicit caller-supplied representation evidence; it does not own a
representation store, cache, wall clock, or multipart assembler. It can consume
checked caller/adapter civil-time evidence (including an explicit unavailable
state) independently of monotonic deadlines. Built-in client handling validates
single-range 206 and keeps multipart opaque as NeedsMultipartConsumer. Its
fixed-capacity partial-combination plan handles validated byte-range segments
and incomplete-200 prefixes from multiple request generations. Standalone 206
bodies accept a public StreamOnly, RetainOnly, or StreamAndRetain preference but
require an engine-selected permit and can stream without retention. Optional
combination requires safely
frozen transfer-decoded/content-encoded storage, trailer-finalized strong
validators, an engine-derived semantic exact-request/Vary/principal/privacy/
navigation identity plus separately fresh provenance evidence. Unnormalized
equality bytes may use immutable exact-value request leases; normalized output
uses exclusive-slice/sealed-arena caller storage. Storage is
anti-aliased and DMA-fenced; sensitive canonical values remain redacted and
caller-scrubbed after release. Normalization occurs once under profile caps,
retains canonical bytes plus provenance without a redundant sensitive raw copy,
and
no truncation, digest equality, token substitution, or comparison-time reparsing
is allowed; capacity/release locally downgrades to NoRecombine. A caller-
requested overlap budget becomes usable
only through a resource-profile-capped engine permit.
Equal overlap deduplicates; conflicting bytes publish nothing and
quarantine the context under a dedicated comparison budget until complete 200
replacement or a destroyed-and-new different-validator representation context.
Every assembly-enabled local correlation reserves a linear engine-only target/
principal/partition/navigation invalidation namespace from isolated per-shard
capacity before request output. Accepted HTTP/2 push finishes its complete
PUSH_PROMISE/CONTINUATION and semantic validation, derives identity only from
the associated local request/caller policy, and atomically preflights its
promised slot, the same handle, independent minimal immutable pushed provenance,
and rejection/cutoff tracking before publication. The provenance is arena/
generation-bound, never borrows recyclable associated-stream storage, and
survives associated-stream teardown and later identity/policy changes. Local
exhaustion returns zero-byte/no-correlation `AssemblyInvalidationCapacity`
backpressure. Pushed-provenance exhaustion returns
`PushedAssemblyProvenanceCapacity`; other push capacity failure likewise stays
HPACK-synchronized, publishes no promised request/correlation or partial
authority, marks the already tracked slot rejecting without changing its RFC
wire state, and schedules stream-local CANCEL through mandatory control
capacity. Reserved(remote) HEADERS synchronizes and transitions to half-closed
(local); its separate END_STREAM event can immediately close while fragmented
CONTINUATION/HPACK ownership remains active. Rejected half-closed(local)
DATA+END_STREAM accounts/discards full payload and padding before closure.
Reserved(remote) DATA and duplicate promised IDs are connection PROTOCOL_ERROR.
Peer reset can supersede an unexposed reserved action. END_STREAM makes an unexposed policy
CANCEL dormant but retains its reset slot through fragmented HPACK and sealed
monotonic semantic stages. HPACK completion atomically seals an immutable
generation-bound decoded field-section lease and releases only compression
workspace; the lease preserves exact bytes/order/duplicates/empty values and
sensitivity/never-index metadata without borrowing dynamic-table or recyclable
caller storage. Only the final applicable owner transfers it and releases the
slot, while malformed status/fields/
trailers/Content-Length/body phase re-arms PROTOCOL_ERROR. Peer reset aborts
pending semantics without publication, after finishing active HPACK; GOAWAY
alone preserves validation, and fatal failure transfers cleanup to bounded
connection shutdown. GOAWAY admission seal, graceful/fatal intent,
application-published peer-stream high-water, output prefix, timer, and
wire-committed sent cutoff are distinct. Only first application publication
advances the high-water; final-cutoff exposure snapshots it, after which higher
streams may synchronize HPACK and connection credit but never publish. First
GOAWAY exposure freezes its exact `17 + owned_debug_len` bytes. Prefixes commit
no cutoff; full acknowledgement alone commits it and starts the initial
max-ID/NO_ERROR grace timer. Fatal intent can replace only ReservedPrivate
graceful output; Frozen output is immutable and finishes before one
non-increasing fatal successor, or the connection is abandoned. Ranked fatal
causes plus event order choose one record without duplicates. Minimum 17-byte
storage is guaranteed independently of optional owned/redacted debug; inbound
and outbound caps are separate and unretained input drains. Partial failure
at zero acknowledged bytes is NotVisible; a positive incomplete prefix leaves
peer cutoff visibility unknown. Received cutoffs never increase: an
increase retains the prior cutoff and produces typed connection PROTOCOL_ERROR.
The connection scheduler has one total order: Frozen suffix, FramingCommitted
continuation, fatal GOAWAY, PING ACK, SETTINGS ACK, graceful GOAWAY, RST_STREAM,
WINDOW_UPDATE, outbound non-ACK SETTINGS, ordinary output. Fatal GOAWAY is the
explicit exception to PING priority; graceful GOAWAY ranks before resets.
Classes are FIFO with
generation-safe enqueue-ordinal ties. Positive per-record bypass bounds
temporarily gate unexposed higher nonfatal classes, and an injected SETTINGS
deadline closes that gate without reordering committed framing or fatal output.
Later outbound SETTINGS receives the same finite bypass service; initial
SETTINGS is a hard activation prerequisite before any other frame.
After fatal GOAWAY commits, every remaining unexposed required control receives
typed AbandonedByConnectionFatal, no later frame is exposed, no ACK/debt,
credit, reset, PING, or graceful-timer completion is fabricated, ownership
releases once, and tokens become stale. Graceful GOAWAY leaves existing-stream
controls operational.
Malformed/abort release the section once; shutdown owns
fatal cleanup with redaction and caller-scrub rules intact. Reset reason changes
only before non-empty output exposure. Exposure freezes the exact 13-byte frame,
stream/reason/generation, and a token-acknowledged cursor; zero/short writes never
unfreeze it, positive progress resumes only at the suffix, and invalid tokens are
state-neutral. Reserved or Frozen output through acknowledged byte 12 does not
close the RFC stream: inbound frames still use its prior wire state. Only
acknowledged byte 13 completes local reset and closes once; an earlier peer
reset or remote END_STREAM that actually performed the final transition remains
the first closure cause, while local output completion is recorded without a
second transition. Remote END_STREAM received in Open creates
half-closed(remote), so a later completed local reset performs the close and owns
its cause. Connection failure records only acknowledged bytes and no incomplete
local-reset transition; tolerated DATA
after actual closure reclaims only connection credit without stream
WINDOW_UPDATE. Each valid non-ACK PING owns a separate bounded transaction that
copies its eight opaque bytes before caller input can be recycled. ACK-bearing
PINGs produce no reply; identical non-ACK payloads still produce distinct
17-byte ACK records and are never coalesced. First exposure freezes the exact
record, offsets through 16 retain it, and only byte 17 completes/releases its
slot. Stale/cross-record acknowledgement and partial transport failure cannot
release or substitute it. PING ACK follows the connection-wide order after an
existing frozen suffix and mandatory CONTINUATION sequence; exhaustion selects
bounded connection shutdown instead of silent loss or an input borrow. Locally
originated PINGs use a monotonic connection-local `u64` opaque key that is never
reissued within the connection, bounded live records, and bounded recent
tombstones. Exact live-key lookup completes once in any arrival order and
classifies in-order/reordered match. Recent duplicate/stale ACKs hit tombstones;
evicted/unknown keys are unsolicited and remain state-neutral rather than RFC
errors. Reclaimed receive credit is never the advertised receive window:
each stream and the connection separately track advertised remaining,
reclaimed-unadvertised, and update-in-flight credit. DATA including padding
decrements advertised remaining immediately. Acknowledgement or discard changes
only reclaimed-unadvertised credit until a generation-bound, exact 13-byte
WINDOW_UPDATE has been acknowledged in full. Prefixes through byte 12 restore
nothing; byte 13 atomically restores only its frozen increment. Further
reclamation accumulates for a later update, and checked arithmetic prevents a
result above `2^31 - 1`. An unexposed stream update may be cancelled on closure
without losing independent connection credit; an exposed update cannot change
target or increment and either completes exactly or is abandoned with the
connection. Stale tokens and partial transport failure fabricate no credit.
For normal outbound HEADERS, DATA, trailers, or empty DATA carrying END_STREAM,
command acceptance seals later application sends but leaves wire state intact.
Only acknowledgement of the complete carrying frame emits
`LocalEndStreamComplete`; partial/failing output cannot claim half-close or
close, peer-first closure remains authoritative, and fragmented HEADERS retain
CONTINUATION/HPACK ownership after their directional transition.
Ordinary output is AcceptedPrivate, Frozen, Complete, or
SupersededBeforeExposure. Peer/completed local reset suppresses only unexposed
private output outside a framing-committed outbound field block. Before initial
exposure, fully encode the bounded HEADERS/PUSH_PROMISE block and atomically
reserve every slot/entry required to drain it using the checked minimum of
16,384, local payload cap, and slot payload capacity plus its provisional HPACK
transaction. Mandatory initial prefixes, maximum encoded field-block bytes,
checked continuation division/count, and total arena/entry arithmetic are
bounded; oversized local fields fail before exposure. A Private block linearly
leases any unsignaled encoder-table debt while materializing its update prefix.
Whole-block rollback returns that exact lease with zero exposure; first exposure
transfers it into FramingCommitted, making every CONTINUATION non-supersedable
through END_HEADERS despite later local exhaustion. Connection debt then records
only settings received after that exposure for the following field block.
Reset, GOAWAY, required controls, and other streams wait. Full final-frame
acknowledgement alone publishes HpackCommitted; transport failure abandons it
only with the connection, while an initial HEADERS END_STREAM hook remains tied
to that frame's completion. Any ordinary non-empty exposure
freezes its exact arena slot even if zero bytes are acknowledged; finish its
suffix before RST_STREAM and run its hook once. DATA reserves exact payload,
Pad Length, and padding—but not the frame header—atomically against stream and
connection available credit, then copies the exact frame into an exclusive
caller-provided `OutboundFrameArena` slot. Segmentation is bounded by peer
MAX_FRAME_SIZE, local `max_outbound_frame_payload`, both credits, and remaining
payload; checked slot capacity covers `9 + payload`, and data length is chosen
only after subtracting checked padding overhead. Impossible padding is reduced
by explicit deterministic policy or returns local backpressure, never overflow
or silent truncation. Peer limits never require peer-sized storage. Queue bytes and entries
have separate limits. Unexposed reservation/slot may revoke on reset, SETTINGS,
or resegmentation; frozen debit and staged bytes remain owned through full
acknowledgement, negative stream windows block new DATA, and zero-length
END_STREAM DATA charges zero.
Each scalar or vectored output token owns one frame-slot suffix; acknowledgement
cannot cross a slot boundary, release several records, or batch hooks.
Each fully validated non-ACK SETTINGS frame reserves one connection-owned
transaction and one ACK before mutation. Ordered entries attach generation-bound
HPACK/window/frame-size/admission/push/extension participants; all must be
effective before FIFO ACK eligibility. The frozen nine-byte ACK retains its
transaction and owner references through offsets 0..=8, and only final-byte
commitment produces AckCommitted; fatal or partial-output failure abandons the
connection without dependent output. HEADER_TABLE_SIZE keeps peer-received,
peer-wire-acknowledged, locally selected, and checked physical capacities
distinct. Selected never exceeds received/profile/storage limits; increases also
wait for the acknowledged ceiling. Peer reductions clamp and evict immediately,
peer increases do not enlarge selection, local reductions create debt without
SETTINGS, and initial selection below 4096 starts indebted. Per-frame transition
obligations retain ceiling snapshots and selected deltas, never ACK authority.
AckCommitted advances the acknowledged snapshot and merges only selected changes
into linear `EncoderTableUpdateDebt`, never raw peer ceilings or a replacement
for its older minimum. Private encoding only leases this debt; rollback restores it exactly,
and first non-empty initial-frame exposure alone transfers it to the
guaranteed-to-finish block. New settings after exposure accrue debt for the next
HEADERS/PUSH_PROMISE block.
Each locally emitted non-ACK SETTINGS command separately prevalidates a
generation-bound commit plan and atomically reserves exact
`9 + 6 * entry_count` bytes, an output entry, future outstanding-ACK FIFO slot,
and timeout state before acceptance. Its outbound transaction is
ReservedPrivate, Frozen, CommittedAwaitingAck, PeerAcked,
AbandonedBeforeExposure, or AbandonedConnection. Exposure freezes ordered
entries and bytes; prefixes change no local advertisement. Full-frame
acknowledgement applies all local effects, promotes the pre-reserved FIFO slot in
wire order, and starts its timeout. Peer ACK consumes the oldest committed
record without reapplication. A bounded early ACK observed while its possible
match is Frozen waits for local commitment rather than becoming an automatic
peer fault. Client preface byte zero and the server's first SETTINGS byte both
require the complete initial transaction already reserved.
Locally reset associated streams retain bounded tombstones that decode in-flight PUSH_PROMISE/
CONTINUATION and track/reject the promised ID without recreating application or
assembly authority; illegal IDs and malformed HPACK retain connection scope.
Tracking survives through reset serialization,
active field blocks, and peer cutoff; unrepresentable tracking retains the slot
through typed bounded shutdown. Neither path rotates an arena or admits an
untracked request. The exact correlation holds its non-Copy/non-Clone handle and
pushed provenance across informational responses and terminal-event
backpressure, releases each once at a terminal disposition, and a retry reserves
independently. Every completed framing- and
semantics-valid 200 invalidates by exact key or across all Vary/validator
siblings in that namespace, widening only across
its coding/domain children when refinement is unavailable. Peer input and all
capacity exhaustion cannot select arena rotation; it is limited to an internal
invariant/trusted-storage integrity failure or explicit caller policy, never a
peer semantic violation or conflicting partial content. Principal/tenant
sharding bounds the blast radius. Disabling assembly requires clearing the shard
generation before admitting an untracked request.
Physical arena generations affect leases, not semantic replacement. Semantic
invalidation rejects stale operations at once, but physical reuse waits for all
body/identity/output leases and otherwise returns local LeaseHeld/capacity.
`Vary: *`,
input/output aliasing, in-place transformation, multipart, and unknown units
never enter combination.

RFC 7239 `Forwarded` transformation is also outside 1.0. Via parsing,
preservation, and generation are covered by RFC 9110 instead.

Future Aesynx integration implements VEF I/O and timing contracts; it does not
change protocol validity or require protocol-engine forks.
