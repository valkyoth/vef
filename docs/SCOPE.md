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
connection shutdown. Malformed/abort release the section once; shutdown owns
fatal cleanup with redaction and caller-scrub rules intact. Reset reason changes
only before non-empty output exposure. Exposure freezes the exact 13-byte frame,
stream/reason/generation, and a token-acknowledged cursor; zero/short writes never
unfreeze it, positive progress resumes only at the suffix, and invalid tokens are
state-neutral. Connection failure records only acknowledged bytes; tolerated
post-reset DATA restores connection credit without stream WINDOW_UPDATE.
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
