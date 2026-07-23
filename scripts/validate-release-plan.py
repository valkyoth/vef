#!/usr/bin/env python3
"""Check 225 minor milestones, thirteen patch stops, and two release candidates."""

from __future__ import annotations
import re
import sys
from pathlib import Path
def versions(pattern: str, text: str) -> list[int]:
    return [int(value) for value in re.findall(pattern, text, flags=re.MULTILINE)]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    detailed = (root / "docs/RELEASE_PLAN.md").read_text(encoding="utf-8")
    compact = (root / "docs/VERSION_PLAN.md").read_text(encoding="utf-8")
    expected = list(range(1, 226))
    detailed_versions = versions(r"^### v0\.(\d+)\.0 — ", detailed)
    compact_versions = versions(r"^\| `0\.(\d+)\.0` \|", compact)
    patch_stops = (
        "0.157.1",
        "0.157.2",
        "0.157.3",
        "0.157.4", "0.157.5",
        "0.180.1",
        "0.180.2",
        "0.180.3",
        "0.180.4", "0.180.5",
        "0.181.1",
        "0.181.2",
        "0.182.1",
    )
    failures: list[str] = []
    if detailed_versions != expected:
        failures.append("detailed plan does not cover v0.1.0 through v0.225.0 exactly")
    if compact_versions != expected:
        failures.append("version index does not cover v0.1.0 through v0.225.0 exactly")
    for patch_stop in patch_stops:
        if detailed.count(f"### v{patch_stop} — ") != 1:
            failures.append(f"detailed plan does not contain exactly one v{patch_stop} patch stop")
        if compact.count(f"| `{patch_stop}` |") != 1:
            failures.append(f"version index does not contain exactly one {patch_stop} patch stop")
    for heading in ("Goal", "Deliverables", "Verification", "Exit criteria"):
        if detailed.count(f"#### {heading}") != 238:
            failures.append(f"expected 238 {heading} sections")
    if detailed.count("implementation stop reached. Run pentest for this exact commit.") != 240:
        failures.append("expected one pentest stop for each milestone and release candidate")
    required_markers = (
        "Non-zero parser progress",
        "Separate vef-http09 package",
        "Engine event, command, acknowledgement, and publication contract",
        "Unified HTTP/1 outbound message state machine",
        "Inbound body acknowledgement, drain, discard, cancellation, and reuse",
        "HPACK synchronization, publication barrier, and error scope",
        "HTTP/2 malformed initial-field-block publication barrier",
        "HTTP/2 inbound DATA ownership, acknowledgement, and credit release",
        "HTTP/2 outbound per-stream message command lifecycle",
        "HTTP/2 body cancellation, reset, and flow-credit lifecycle",
        "Authenticated origin authorization and HTTP/2 coalescing metadata",
        "Deterministic CPU, stack, code-size, and amplification budgets",
        "Generation-checked stream table",
        "TLS 1.3 early-data prohibition",
        "Independent security audit",
        "Initial deterministic resource profiles and measurement hooks",
        "Capacity exhaustion and protocol-violation disposition taxonomy",
        "Caller-supplied WebSocket nonce and entropy boundary",
        "HPACK encoder output commit and indexing policy",
        "SETTINGS syntax, role, directional values, and ACK rules",
        "SETTINGS initial-window active-stream integration and atomic rollback",
        "HTTP/2 activation preface, first-SETTINGS, and deadline sequencing",
        "HTTP/2 error scope, typed deltas, and isolated stream mutation",
        "HTTP/2 graceful GOAWAY and bounded shutdown sequencing",
        "Normative HTTP/1 and HTTP/2 translation matrix",
        "Max-Forwards TRACE and OPTIONS intermediary semantics",
        "HTTP/1 TE request-field and trailers forwarding semantics",
        "vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton",
        "Structured Fields complete bare-item dispatcher",
        "SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration",
        "Priority update flood budgeting",
        "Dependency-free conditional semantics crate and validators",
        "Conditional request fields and ordered precondition evaluation",
        "Bounded byte ranges and single-range response planning",
        "Retry safety, idempotency, and body-replayability contract",
        "Exact CONNECT, Upgrade, and tunnel byte-handoff ownership",
        "HTTP/2 TLS admission prerequisites and authenticated metadata",
        "Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge",
        "Via grammar, append, privacy, and loop policy",
        "Dependency-free generic authentication grammar and sensitive storage",
        "Proxy-authentication hop ownership and 407 lifecycle",
        "Injected civil time and HTTP-date policy", "Dependency-free media-type grammar",
        "Outbound conditional and range request validation", "Partial-response media-type classification integration",
        "Streaming partial-response and retained-prefix validation",
        "Cross-request partial assembly and header synthesis",
        "Role-aware outbound response semantic validator",
    )
    for marker in required_markers:
        if marker not in detailed or marker not in compact:
            failures.append(f"missing gap-closure milestone: {marker}")
    ordering = (
        ("Connection-option, Upgrade, and hop-by-hop field grammar", "101 Switching Protocols transition and publication barrier"),
        ("SETTINGS frame codec", "SETTINGS syntax, role, directional values, and ACK rules"),
        ("Fixed-capacity caller-storage public API", "Optional alloc-backed convenience API"),
        ("Initial deterministic resource profiles and measurement hooks", "HTTP/1 role and parser profiles"),
        ("SETTINGS syntax, role, directional values, and ACK rules", "Generation-checked stream table and tombstones"),
        ("HTTP/2 frame legality and fragmented-header-block sequencing", "HTTP/2 error scope, typed deltas, and isolated stream mutation"),
        ("HTTP/2 error scope, typed deltas, and isolated stream mutation", "HTTP/2 graceful GOAWAY and bounded shutdown sequencing"),
        ("HTTP/2 error scope, typed deltas, and isolated stream mutation", "Atomic HPACK header-block integration"),
        ("Atomic HPACK header-block integration", "SETTINGS header-table encoder and header-list policy coupling"),
        ("Connection flow control", "SETTINGS initial-window active-stream integration and atomic rollback"),
        ("SETTINGS initial-window active-stream integration and atomic rollback", "HTTP/2 inbound DATA ownership, acknowledgement, and credit release"),
        ("HTTP/2 inbound DATA ownership, acknowledgement, and credit release", "HTTP/2 outbound per-stream message command lifecycle"),
        ("HTTP/2 outbound per-stream message command lifecycle", "HTTP/2 body cancellation, reset, and flow-credit lifecycle"),
        ("Bounded stream admission", "SETTINGS max-concurrent-streams admission integration"),
        ("Bounded outbound scheduling", "SETTINGS max-frame-size outbound integration"),
        ("HTTP/2 malformed initial-field-block publication barrier", "HTTP/2 request mapping"),
        ("Protocol-neutral HTTP translation representation", "Effective URI and authority consistency"),
        ("Connection-field stripping and cache-metadata preservation", "Via grammar, append, privacy, and loop policy"),
        ("Via grammar, append, privacy, and loop policy", "Dependency-free generic authentication grammar and sensitive storage"),
        ("Dependency-free generic authentication grammar and sensitive storage", "Proxy-authentication hop ownership and 407 lifecycle"),
        ("Proxy-authentication hop ownership and 407 lifecycle", "Injected civil time and HTTP-date policy"),
        ("Injected civil time and HTTP-date policy", "Dependency-free media-type grammar"), ("Dependency-free media-type grammar", "Max-Forwards TRACE and OPTIONS intermediary semantics"),
        ("Max-Forwards TRACE and OPTIONS intermediary semantics", "Normative HTTP/1 and HTTP/2 translation matrix"),
        ("HTTP/1 TE request-field and trailers forwarding semantics", "Normative HTTP/1 and HTTP/2 translation matrix"),
        ("Normative HTTP/1 and HTTP/2 translation matrix", "CONNECT translation across HTTP versions"),
        ("Client request builder and target forms", "Dependency-free conditional semantics crate and validators"),
        ("Dependency-free conditional semantics crate and validators", "Conditional request fields and ordered precondition evaluation"),
        ("Conditional request fields and ordered precondition evaluation", "Bounded byte ranges and single-range response planning"),
        ("Bounded byte ranges and single-range response planning", "Outbound conditional and range request validation"),
        ("Outbound conditional and range request validation", "Partial-response media-type classification integration"), ("Partial-response media-type classification integration", "Client correlation, cancellation, and retry tokens"),
        ("Client correlation, cancellation, and retry tokens", "Streaming partial-response and retained-prefix validation"),
        ("Streaming partial-response and retained-prefix validation", "Cross-request partial assembly and header synthesis"),
        ("Cross-request partial assembly and header synthesis", "Retry safety, idempotency, and body-replayability contract"),
        ("Retry safety, idempotency, and body-replayability contract", "Role-aware outbound response semantic validator"),
        ("Role-aware outbound response semantic validator", "Origin-server role API"),
        ("vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton", "Structured Fields integer and decimal ranges"),
        ("Structured Fields strings, tokens, bytes, booleans, dates, and display strings", "Structured Fields complete bare-item dispatcher"),
        ("Structured Fields complete bare-item dispatcher", "Structured Fields parameters"),
        ("Priority field semantics", "SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration"),
        ("SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration", "Priority scheduling hints and fairness"),
        ("HTTP/2 TLS admission prerequisites and authenticated metadata", "TLS transport termination, resumption, alert, and EOF mapping"),
    )
    for first, second in ordering:
        if compact.find(first) >= compact.find(second):
            failures.append(f"unsafe milestone ordering: {first} must precede {second}")
    if (
        "Transactional HPACK context" in detailed
        or "RFC 7239 where Via" in detailed
        or "Acceptance contract: Expose " in detailed
        or re.search(r"Acceptance contract: Define the .* state graph", detailed)
        or re.search(r"Acceptance contract: Bind .* to the exact cited HTTP/1 octet grammar and role matrix", detailed)
        or re.search(r"Acceptance contract: Bind .* to the exact RFC 7541 representation and table rules", detailed)
        or re.search(r"Acceptance contract: Bind .* to the exact RFC 9113 wire/state rule by endpoint role", detailed)
        or re.search(r"Acceptance contract: The .* outcome must enumerate", detailed)
        or "status digits in 100..=999" in detailed
        or "reject missing, empty, comma-combined" in detailed
        or "absolute-form only where the role permits proxy requests" in detailed
        or "Parse each chunk extension as semicolon token" in detailed
        or "Permit zero or more 100..199 responses before exactly one final response" in detailed
        or "WebSocket HTTP/1 to HTTP/2 handshake bridge" in detailed
        or "HTTP/2 2xx back to HTTP/1 101 with validated accept" in detailed
        or "parse scheme/authority/path with checked byte ranges" in detailed
        or "deferring empty effective-authority accept/reject policy to v0.156.0" in detailed
        or "accept origin-form and absolute-form for ordinary requests at every receiving server role" in detailed
        or "Permit extended CONNECT only after the peer's SETTINGS_ENABLE_CONNECT_PROTOCOL" in detailed
        or "Accept CONNECT only with authority-form and role authorization" in detailed
        or "Parse one valid Max-Forwards value, decrement on forwarded TRACE/OPTIONS" in detailed
        or "local-half-closed, peer-half-closed" in detailed
        or "derive effective authority from the authorized target, Host, and explicit context" in detailed
        or "DrainingAfterPeerClose" in detailed
        or "Reconcile content-length with DATA octets and enforce final-response" in detailed
        or "reject request content/framing according to source protocol" in detailed
        or "1xx, 204, 304, and body-forbidden response handling" in detailed
        or "caller storage or flow-control backpressure without peer-sized allocation" in detailed
        or "bounded PendingConnect while target authorization/dialing is incomplete" in detailed
        or "same ConnectTargetPolicy authorization before DNS, dialing, upstream output, or tunnel publication" in detailed
        or "Connection-field stripping, Via, and cache preservation" in detailed
        or "Connection fields, Via, proxy authentication, and cache preservation" in detailed
        or "promised-request validation" in detailed
        or "forbid trailer fields that affect framing, routing, request method/target, authentication" in detailed
        or "Content-Type multipart/byteranges whose bounded parts" in detailed
        or "require 401 to carry at least one valid WWW-Authenticate challenge, 405 to carry Allow, and 426 to carry Upgrade" in detailed
        or "Authentication-Info and Proxy-Authentication-Info additionally require caller-supplied scheme-specific AuthenticationTrailerPermission" in detailed
        or "shared v0.52.0 TrailerFieldPermission/AuthenticationTrailerPermission policy" in detailed
        or "separate dependency-free, no_std `vef-semantics` crate depending only on `vef-core` and `vef-auth`" in detailed
        or "require HTTP/1 401 to carry at least one valid WWW-Authenticate challenge" in detailed
        or "normalize comparisons without a wall clock" in detailed
        or "before method execution or range selection" in detailed
        or "selected-representation metadata, and cache validators" in detailed
        or "request serialization remains independently usable" in detailed
    ):
        failures.append("superseded or generic acceptance wording remains in detailed plan")
    required_contract_text = (
        "borrowed BodyChunk whose acknowledged prefix alone may be released",
        "encoded header-block bytes, decoded bytes, field count",
        "Host/:authority disagreement",
        "flow-controlled payload length (including Pad Length and padding)",
        "make the ACK eligible only after every participant reports Effective",
        "SETTINGS_ENABLE_PUSH directionally",
        "initial SETTINGS frame",
        "never automatically retry an unsafe request",
        "protocol processing status separately from application replay permission",
        "authenticated SNI, certificate identity, scheme, port, remote endpoint",
        "Accept every RFC 7541-valid prefix integer representation",
        "Reject the EOS symbol as data, padding longer than seven bits",
        "smallest observed maximum followed by the final maximum",
        "index zero and every reference beyond the combined table",
        "payload length divisible by six",
        "exactly eight payload bytes",
        "exactly four payload bytes",
        "nonzero reserved-bit-masked 31-bit increment",
        "exactly five payload bytes",
        "at least eight payload bytes",
        "effective locally advertised inbound limit governing received frames (initially 16,384)",
        "bounded FIFO only after each complete frame's bytes commit",
        "every unrelated stream, scheduler entry, flow window",
        "typed Index, WithoutIndexing, and NeverIndexed directives",
        "never let an intermediary downgrade a received never-indexed representation",
        "prohibit indexing decisions based on secret-value comparisons",
        "Ignore an unknown frame unless an explicitly enabled extension owns its type",
        "drain its payload incrementally without allocation from the declared length",
        "immediately add padding the application never sees to internal consumed-credit accounting",
        "coalesce WINDOW_UPDATE emission under independent threshold, rate, and amplification budgets",
        "Once HEADERS or PUSH_PROMISE begins without END_HEADERS",
        "application-independent capacity for RST_STREAM, SETTINGS ACK, PING ACK, WINDOW_UPDATE, and GOAWAY",
        "larger local inbound limit becomes enforceable no later than commitment",
        "reduction never retroactively invalidates an already accepted or partially received frame",
        "peer limit effective when each frame's bytes commit",
        "exact authenticated post-handshake ALPN value h2",
        "no sniffing or guessed HTTP/1 fallback",
        "protocol choice immutable once preface processing begins",
        "undersized priority layout to connection FRAME_SIZE_ERROR",
        "undersized promised-stream layout to connection FRAME_SIZE_ERROR",
        "generation-safe CompressionPrincipal provenance token",
        "prohibit encoder lookup across principals",
        "Count open, half-closed-local, and half-closed-remote streams",
        "do not terminate existing streams solely because a later setting reduces the limit",
        "independent saturating budgets for streams opened/reset",
        "caller-supplied shared admission/budget hook",
        "never refund those charges for immediate RST_STREAM",
        "Never silently ignore a valid frame when transaction/ACK/output budget is exhausted",
        "valid non-ACK PING cannot be ignored",
        "overwrite the existing value in place so all but the final value are ignored",
        "at least 1,024 members and 64-character keys",
        "every Date from year 1 through 9999",
        "only HTTP/2 PRIORITY_UPDATE type 0x10",
        "by fixed policy, ignore a malformed update",
        "Construct StatusCode only from exactly three decimal digits in 100..=599",
        "typed InvalidStatusCode result carrying its raw digits",
        "for requests require chunked as the final coding",
        "for responses select chunk framing when chunked is final",
        "proxy client either waits for the CONNECT 2xx",
        "rejecting CONNECT closes the transport and processes no later request",
        "encoder-only sidecar metadata that never changes HPACK entry size",
        "skipped cross-principal entries still occupy their normal indices",
        "immediate RST_STREAM, refusal, application cancellation",
        "REFUSED_STREAM remains available only before application processing",
        "every target state expressed from the receiving server's perspective",
        "for push streams accept reserved-local or half-closed-remote",
        "including the grammar-valid empty value required when the target URI has no authority",
        "regenerate forwarding Host",
        "Parse exactly *(BWS \";\" BWS token [BWS \"=\" BWS (token / quoted-string)])",
        "two exclusive response branches",
        "require full acknowledgement of the complete 100 response head",
        "make every later HTTP response parse, serialization, body, trailer, pipeline, or reuse operation an InvalidState",
        "advertises 1 only with an available native endpoint or fully configured bridge/entropy capability",
        "For HTTP/1 downstream to HTTP/2 upstream",
        "for HTTP/2 downstream to HTTP/1 upstream",
        "without processing key/accept upstream",
        "`BridgeTransaction::{Reserved, DownstreamRequestValidated, UpstreamRequestCommitted, UpstreamSuccessValidated, DownstreamSuccessFrozen, ActiveAfterDownstreamSuccessCommitted",
        "raw path, and optional raw query into distinct checked spans",
        "preserve `/resource` versus `/resource?`",
        "any decoded or normalized view is separate",
        "accept well-formed bracketed IPv6/IPvFuture",
        "accept and preserve a grammar-valid empty port",
        "reject userinfo for HTTP authority use",
        "reject malformed/mismatched brackets",
        "publish only a typed non-routable Host/parser artifact",
        "explicit forward proxies require absolute-form for ordinary proxy requests",
        "never infer a forward-proxy destination from origin-form plus Host",
        "applying configured reject-or-explicit-default empty-authority policy",
        "Reuse the already validated v0.40.0 EffectiveTarget",
        "split :path on its first question mark into raw path and optional raw query",
        "preserve an empty query's trailing `?`",
        "proxies never otherwise modify path/query",
        "peer_enabled_outbound_connect separately from local_advertised_inbound_connect",
        "only a client receiving peer value 1 may initiate outbound extended CONNECT",
        "local server's SETTINGS value 1 bytes commit, not when queued",
        "peer 0-after-1 to connection PROTOCOL_ERROR and a local attempt to InvalidState",
        "later transient endpoint, nonce, or capacity failure becomes a bounded HTTP failure",
        "ws mapped to :scheme http and wss to https",
        "lowercase every emitted HTTP/2 field name",
        "Origin, Sec-WebSocket-Version, Sec-WebSocket-Protocol, and Sec-WebSocket-Extensions",
        "ordinary end-to-end cookies/authorization through the normal matrix",
        "ignore received HTTP/2 key/accept fields for key generation",
        "generation- and connection-bound TrustedRequestContext",
        "optional fixed-listener scheme, authenticated trusted-gateway scheme",
        "precedence fixed-listener then trusted-gateway then transport-derived http/https",
        "reject stale/cross-connection context",
        "caller-supplied ConnectTargetPolicy",
        "distinct ConnectAuthority from authority-form",
        "explicit nonempty decimal port in 1..=65535",
        "complete EffectiveTarget of trusted scheme",
        "generation-matched TrustedRequestContext",
        "generation-bound ConnectAttemptToken and AuthorizedConnectOutcome types",
        "bind requested authority, resolved endpoint, connected peer, attempt/request/policy generations",
        "seal their fields/constructors, make them neither Copy nor Clone",
        "engine-owned opaque attempt identity independent of caller endpoint values",
        "outcome to be consumed once by only its matching request state",
        "engine-issued exchange identity as well as inbound hop",
        "authorize every candidate endpoint before its dial",
        "consume exactly once only an AuthorizedConnectOutcome whose opaque attempt identity",
        "cancellation, rejection, policy-generation change, non-2xx completion, or tunnel commitment invalidates every remaining attempt/outcome",
        "duplicate outcome/success commands are InvalidState before output",
        "VEF performs no DNS, dialing, or socket inspection",
        "rejects stale, alternate, mismatched, or policy-revoked outcomes before 2xx",
        "outbound builders reject request content, Content-Length, and Transfer-Encoding",
        "hardened inbound framing rejects either field with bounded 400 plus mandatory close and no reparse",
        "successful server responses forbid both fields while clients ignore received ones",
        "every response is non-cacheable",
        "HTTP/1 CONNECT 407 carries a valid Proxy-Authenticate challenge",
        "authentication retry only on a fresh connection/generation",
        "never synthesize it when absent, handle zero locally without forwarding",
        "TRACE client builders reject content, Cookie, Authorization, Proxy-Authorization",
        "bounded sanitized reflection representation excluding all credential fields and sensitive values",
        "OPTIONS client content requires exact current v0.157.5 `ValidatedGeneratedMediaType` evidence",
        "shared validated ConnectAuthority between HTTP/1 authority-form and HTTP/2",
        "RST_STREAM, TCP reset/error, fatal TLS alert",
        "TrustedRequestContext carrying authenticated transport-security state",
        "never infer TLS from Aesynx handle or socket types",
        "1xx, 204, 205, 304, and body-forbidden response handling",
        "outbound HTTP/1 205 permit only zero-content serialization",
        "inbound 205 still uses the ordinary HTTP/1 body-length algorithm",
        "never misclassify following octets as a new response",
        "fixed caller-capacity PendingConnect while the stream is AwaitingConnectOutcome",
        "no peer-sized allocation, WINDOW_UPDATE, credit-release, DNS, dial, or socket claim at this milestone",
        "typed local-capacity disposition plus RST_STREAM(CANCEL), not a peer protocol violation",
        "consume one matching opaque AuthorizedConnectOutcome and forward nothing until it passes",
        "once connected allow only DATA and applicable stream-management frames",
        "map caller-reported TCP failure/reset to RST_STREAM(CONNECT_ERROR)",
        "typed caller action to reset upstream TCP",
        "including DATA received while AwaitingConnectOutcome",
        "including PendingConnect/AwaitingConnectOutcome bytes",
        "route CONNECT PendingConnect/AwaitingConnectOutcome/connected ranges only to stream-local bounded tunnel ownership",
        "replace v0.130.0 capacity-reset-only handling with credit-aware backpressure",
        "receipt of PUSH_PROMISE from a client is connection PROTOCOL_ERROR",
        "recognized method classified both safe and cacheable",
        "invalid promised semantics produce promised-stream PROTOCOL_ERROR without resetting or mutating the associated stream",
        "connection-/generation-bound PushAuthorityEvidence carrying caller-certified authenticated TLS origin metadata",
        "outbound servers require the associated stream open/half-closed(remote), while receiving clients observe the equivalent open/half-closed(local)",
        "`FirstWireClosureCause::{LocalResetComplete, LocalEndStreamComplete, PeerReset, RemoteEndStream}`", "`ResetOutput::Reserved` and `Frozen { acknowledged: 0..=12 }` leave `WireStreamState` unchanged", "`Complete` requires acknowledgement of all 13 bytes and atomically emits normalized `LocalResetComplete`", "if peer reset or remote END_STREAM already closed it, retain that first cause and record output completion without a second transition", "Connection failure at prefix 0..=12 performs acknowledged-prefix cleanup without `Complete` or `LocalResetComplete`", "Inject every inbound frame at acknowledged offsets 0..=13", "Only DATA after `ResetOutput::Complete` caused local closure",
        "Accepting a command that carries END_STREAM irreversibly seals the application-facing local send direction", "Only acknowledgement of the complete frame emits normalized `LocalEndStreamComplete`", "Open becomes HalfClosedLocal", "HalfClosedRemote becomes Closed and selects `FirstWireClosureCause::LocalEndStreamComplete`", "Connection failure before full acknowledgement records only the written prefix and never claims local half-close, closure, or END_STREAM completion", "completion of that entire HEADERS frame—not command acceptance, the first exposed byte, or final CONTINUATION—emits the directional transition", "The same full-frame rule covers DATA, empty DATA, and initial/trailing HEADERS carrying END_STREAM",
        "`OrdinaryFrameOutput::{AcceptedPrivate { slot: OutboundFrameSlot, completion, credit }, Frozen { slot: FrozenOutboundFrameSlot, offered, acknowledged, generation, completion, debit }, Complete, SupersededBeforeExposure}`", "Peer RST_STREAM, completed local reset, or cancellation may select `SupersededBeforeExposure` only from AcceptedPrivate", "First non-empty exposure—including a later zero acknowledgement—atomically freezes the exact slot bytes and converts DATA reservation to committed debit", "finish its exact suffix before any same-connection RST_STREAM", "Reserve one exact DATA frame's flow-controlled length atomically against both its stream and the connection", "the nine-byte frame header is not charged", "Before committing any valid delta, atomically revoke every affected unexposed DATA reservation and release its paired connection reservation", "Frozen/exposed DATA retains its committed debit", "Zero-length DATA carrying END_STREAM reserves/debits zero credit", "Make FramingCommitted `OutboundFieldBlock` the scheduler's highest framing obligation", "apply its directional transition—Open to HalfClosedRemote or HalfClosedLocal to Closed", "`OutboundFieldBlock::{Private { stream, generation, hpack: HpackEncoderTransaction, initial, continuations }, FramingCommitted { stream, generation, hpack: HpackEncoderTransaction, remaining_continuations }, HpackCommitted, AbandonedWithConnection}`", "Before any initial HEADERS/PUSH_PROMISE exposure, fully encode the bounded block", "First non-empty initial-frame exposure moves only to FramingCommitted", "every remaining CONTINUATION is non-supersedable and its resources are already owned", "No RST_STREAM, GOAWAY, PING ACK, SETTINGS ACK, WINDOW_UPDATE, or other-stream output can interleave", "An END_STREAM completion hook on initial HEADERS still runs when that frame is fully acknowledged", "caller-provided fixed-capacity `OutboundFrameArena`", "`ResourceProfile::max_outbound_frame_payload` is checked, nonzero, independent of peer MAX_FRAME_SIZE", "typed local `OutboundFrameStorageCapacity` backpressure", "queue byte capacity and queue-entry capacity are measured and exhausted independently", "atomically reserve/materialize the exact initial slot, every CONTINUATION slot", "`field_fragment_cap = min(16_384, ResourceProfile::max_outbound_frame_payload, checked_sub(slot_capacity, 9))`", "Full acknowledgement of the frame carrying END_HEADERS atomically publishes `HpackCommitted`", "No later field block is encoded against the provisional transaction", "`slot_capacity >= checked_add(9, ResourceProfile::max_outbound_frame_payload)`", "use checked arithmetic for `payload = data + optional_pad_length_octet + padding`", "Derive data length only after subtracting checked padding overhead", "Each `OutputToken` offered by HTTP/2 owns exactly one frame-slot suffix", "`ResourceProfile::max_outbound_field_block_bytes`", "`continuation_count = checked_ceil_div(remaining_encoded_block_bytes, field_fragment_cap)`", "`ResourceProfile::max_outbound_continuations_per_block`", "`OutboundFieldBlockCapacity`/validation failure", "`PendingEncoderTableSizeTransition::{None, Pending { smallest_seen, final_value, owners: SettingsTransactionSet }}`", "With Private unexposed HPACK, roll back provisional encoder mutations and complete field-block slots", "With FramingCommitted, retain owner references while the pre-reserved block drains without interleaving", "retain the smallest observed maximum and final maximum in receive order", "each generation-bound owner is the v0.108.0 frame-wide `InboundSettingsTransaction`", "No later field block may encode while either a provisional transaction or pending encoder-size transition is unresolved", "`InboundSettingsTransaction { frame_generation, ordered_entries: SettingsEntryLease, ack: ReservedSettingsAck, pending_participants: SettingsParticipantSet, disposition: SettingsDisposition }`", "first validate every ordered entry with zero component mutation", "The single ACK belongs to the complete frame regardless of entry count, duplicates, unknowns, or later participating subsystems", "Process its entries in wire order without intervening frame dispatch", "ACK eligibility requires every participant effective", "Maintain transactions and ACK eligibility in received-frame FIFO order", "cancels that transaction's ACK", "prevents every component from emitting it independently", "It never owns, counts, queues, or serializes SETTINGS ACKs", "Local post-effect work such as re-encoding a rolled-back Private field block is not a participant",
        "separate bounded reserved-push-slot/work budget before reservation", "preflight tombstone and cutoff capacity before releasing its slot or convert that slot in place", "continuously represented as a generation-bound slot, tombstone, or connection-shutdown record", "Store policy disposition, current RFC wire state, generation-checked reset output/lease/acknowledged-prefix state, remote-closure cause, terminal-validation state/stage, compression-workspace ownership, immutable terminal-field-section lease, and active field-block ownership independently", "Normalize END_STREAM separately from its carrying HEADERS or DATA event", "`HeadersStart { end_stream, end_headers }`", "CONTINUATION never changes wire state", "`ResetOutput::{Reserved { reason, disposition }, Frozen { stream: StreamToken, reason: ResetReason, frame: [u8; 13], offered: u8, acknowledged: u8, generation: OutputGeneration }, Complete, SupersededBeforeExposure}`", "Returning a non-empty output slice is the irrevocable byte-exposure boundary", "A zero-capacity poll returns NeedOutput and creates no lease/exposure", "`OutputToken { generation, record, start, offered_end }`", "Zero is a valid no-progress write that leaves the cursor unchanged but invalidates that offer token", "Duplicate, oversized—including an acknowledgement extending beyond this record—stale-generation, cross-record/output, or out-of-order acknowledgement returns `InvalidState` without cursor/state mutation", "Connection failure consumes or invalidates the token through connection-owned cleanup and records only the acknowledged prefix", "`ResetReason::{PolicyCancel, StreamError(StreamErrorCode)}`", "`TerminalValidation::{NotTerminal, PendingFieldBlock(PendingBlockDisposition), PendingSemantics { stage: SemanticStage, fields: TerminalFieldSectionLease }, Valid, Malformed(StreamErrorCode), AbortedByPeerReset}`", "`CompressionWorkspace` owns encoded fragments, integer/Huffman scratch, and CONTINUATION assembly state", "`TerminalFieldSection` owns immutable decoded name/value bytes, ordered boundaries, pseudo/ordinary classification, sensitivity/never-index provenance, and generation/stream binding", "exactly one non-Copy/non-Clone generation/stream-bound immutable `TerminalFieldSectionLease`", "No semantic consumer reparses encoded HPACK or reconstructs fields from mutable table/scratch state", "A one-byte shortage cannot truncate, partially validate, or publish", "`PendingBlockDisposition::{ValidateSemantics, AbortAfterHpackByPeerReset}`", "`SemanticStage::{PseudoFields, ConnectionFields, FieldAndContext, RequestMapping, ResponseMapping, ContentAndPhase, TrailerAndRoleRules}`", "Permit only sealed/private transition constructors", "HEADERS+END_STREAM without END_HEADERS sets `PendingFieldBlock(ValidateSemantics)`", "On successful HPACK completion, atomically seal a non-Copy/non-Clone `TerminalFieldSectionLease` and transfer it to `PendingSemantics { stage: PseudoFields, fields }`, never directly to `Valid`", "Each stage uses pre-reserved bounded work/storage", "Peer reset during fragmentation changes the disposition to abort-after-HPACK", "semantic-storage shortage after table mutation finishes bounded synchronization and transfers workspace, partial section storage, reset reservation, and cleanup exactly once to connection shutdown", "`RemoteClosureCause::{Reset, EndStream}`", "Any informational 1xx HEADERS carrying END_STREAM is terminal `Malformed(PROTOCOL_ERROR)` and requires stream RST_STREAM(PROTOCOL_ERROR)", "HEADERS with END_STREAM but without END_HEADERS records closed wire state immediately", "A valid terminal DATA for which this is the final applicable owner marks `TerminalValidation::Valid` and releases a dormant policy-reset slot only after credit", "another terminal message violation marks `Malformed(PROTOCOL_ERROR)` and re-arms that slot", "A policy-CANCEL reservation can become dormant only before output exposure", "`StreamError(code)` may replace/re-arm `PolicyCancel` only while `ResetOutput::Reserved` has never exposed bytes", "`Frozen` frame identity and bytes always win over later reason changes", "resumable pressure leaves the same stage, lease, and reservation intact", "typed bounded `StreamTrackingUnavailable` connection shutdown", "validated promised request, trusted authority/push-policy provenance, and reserved slot unpublished and rollback-capable", "promised slot includes or pre-reserves its v0.117.0 in-place rejection-tombstone/cutoff representation", "At v0.145.0 the transaction's participants are the promised-stream slot/work and rejection tracking", "Rejected promised streams use the v0.118.0 orthogonal model", "total auditable `RejectedPushFrameDisposition` matrix", "normalized event/END flags", "header phase", "terminal state/stage", "with no wildcard/default cell", "every ResetOutput state/reason/generation/offered/acknowledged value and outstanding-token state", "Every cell declares protocol/error scope, wire transitions, output exposure/freeze/offer/ack/suffix action, HPACK/lease action, application visibility, credit, reset arbitration, peer-reset abort, redaction, and fatal cleanup owner", "Implement RFC 9113's in-flight PUSH_PROMISE exception for an associated stream with a locally initiated reset", "accept and completely decode PUSH_PROMISE plus every CONTINUATION", "publish no promised request, and recreate no application, authority, push-policy, invalidation, or assembly provenance", "Missing recycled associated-request provenance selects safe promised-stream rejection", "Illegal promised IDs remain connection PROTOCOL_ERROR and malformed HPACK remains connection-fatal", "No v0.145.0-only pushed response has partial-retention or cross-request assembly authority",
        "reserved streams do not count against SETTINGS_MAX_CONCURRENT_STREAMS and reservation remains legal at zero",
        "opening the promised response enforces the then-current concurrent-stream limit",
        "every non-cacheable response is marked forbidden for cache storage",
        "for 205 require initial response HEADERS with END_STREAM and optional Content-Length: 0",
        "established HTTP/2 CONNECT or RFC 8441 stream expose separate tunnel DATA/finish commands",
        "ServerWideOptionsCandidate",
        "convert it to asterisk-form only at the final origin-facing hop",
        "present-but-empty query, `OPTIONS /`, and every resource path remain distinct",
        "map its empty-path/absent-query target to HTTP/1 `OPTIONS *` or HTTP/2 `:path: *`",
        "treat HTTP/2 DATA through v0.130.0 PendingConnect/AwaitingConnectOutcome",
        "reuse the completed lexical authorization → ConnectAttemptToken → caller resolution/per-endpoint authorization → generation-matched AuthorizedConnectOutcome lifecycle",
        "full ordered Via member grammar under explicit member/comment/value/work limits",
        "append exactly one caller-configured received-protocol plus pseudonym entry without replacement or combination",
        "record the inbound protocol/version rather than the outbound version",
        "self-pseudonym loop hook that never derives identity from peer bytes",
        "have `vef-core` define `TrailerFieldPermission`",
        "keep local Authentication-Info and Proxy-Authentication-Info generation unavailable until v0.157.2",
        "Received trailers carry no local Rust permission",
        "classify authentication-info as RequiresSchemeAuthorization",
        "typed semantic/policy disposition after message synchronization rather than automatically as a framing error",
        "Outbound generation and every safe merge require explicit generation-bound permission",
        "separate dependency-free, no_std `vef-auth` crate",
        "bounded incremental scheme-neutral parser/serializer for challenge, credentials, token68, and auth-param",
        "compare authentication scheme and parameter names case-insensitively while preserving raw scheme spelling",
        "reject duplicate parameter names within one challenge",
        "require generated realm values to use quoted-string",
        "reject any token68 data after terminal `=` padding",
        "introduce caller-supplied scheme-specific `AuthenticationTrailerPermission`",
        "integrate the positive outbound authentication-trailer and explicitly safe-merge paths into both HTTP/1 and HTTP/2",
        "disambiguate comma-separated auth parameters from subsequent challenges without unsafe normalization",
        "support WWW-Authenticate, Authorization, Authentication-Info, Proxy-Authenticate, Proxy-Authorization, and Proxy-Authentication-Info",
        "does not promise optimizer-resistant physical zeroization—the caller must scrub its owned buffers",
        "Consume one validated HopScopedProxyCredential at the first expecting proxy",
        "remove Proxy-Authorization before origin forwarding",
        "explicit generation-bound cooperative policy naming the next hop",
        "require at least one v0.157.2-valid Proxy-Authenticate challenge on every generated 407",
        "Proxy-Authorization, Proxy-Authenticate, Proxy-Authentication-Info",
        "apply v0.65.0 fresh-connection closure to HTTP/1 CONNECT 407",
        "checked no_std `UtcCivilTime` and generation-bound `CivilTimeEvidence::{Available, Unavailable}`",
        "optional `vef-io::CivilClock` provider",
        "roll a candidate back by 100 years only when its complete timestamp is more than 50 years in the future",
        "complete supplied current `UtcCivilTime` instant—not only its year",
        "rejecting every HTTP date earlier than 1900",
        "origin with Available evidence must generate Date on 2xx/3xx/4xx",
        "origin with Unavailable evidence must not generate Date",
        "clamp a future application Last-Modified to message-origination Date",
        "inbound received-protocol/pseudonym Via entry for every HTTP-to-HTTP gateway-forwarded request",
        "including an Upgrade field received with status 426",
        "HTTP/2 426 without Upgrade is framing-valid but produces a typed RFC 9110 received-semantic violation",
        "local HTTP/2 status 426 as InvalidState",
        "HTTP/1 426 with valid Upgrade is untranslatable to HTTP/2",
        "preserve received multipart/byteranges 206 content opaquely across versions",
        "separate dependency-free, no_std `vef-conditions` crate depending only on `vef-core`",
        "distinct RFC strong/weak comparison",
        "Evaluate RFC 9110 preconditions in order",
        "Evaluate preconditions only for an origin server or authorized cache",
        "read-only `PendingConditionalRequest`",
        "before processing request content, method execution, or range selection",
        "sealed generation-bound `CurrentRepresentationEvidence`",
        "sealed retrieval-only `WouldBe200Snapshot`",
        "exact ordered fields that the corresponding 200 would contain",
        "unsafe PUT/POST/DELETE admission never requires hypothetical-200 metadata",
        "parse bounded Range byte-range, open-ended range, and suffix-range members",
        "cap raw bytes, decimal digits, member count, normalization work, and output before arithmetic",
        "first-pos <= last-pos",
        "malformed and unknown remain distinct",
        "Ignore Range except on GET",
        "dates require caller-certified strong-validator status and exact equality with Last-Modified",
        "sealed `SingleRangePlan` only for one normalized satisfiable range",
        "non-forgeable one-shot `RequestContentPermit` and `MethodExecutionPermit`",
        "Terminal 304/412 produces neither permit",
        "final `vef-conditions` validation pass over the exact frozen ordered client request",
        "v0.180.4 must replace its raw entry with frozen `ValidatedConditionalRequest`",
        "If-Range without Range, weak entity-tag If-Range",
        "no ETag is available for that stored representation",
        "separate dependency-free, no_std `vef-media-type` crate depending only on `vef-core`", "ordered parameter and empty-parameter-slot events", "Reject whitespace on either side of `=`", "syntactically empty quoted value `name=\"\"`", "sealed `ParsedMediaType` syntax evidence bound to the exact field bytes and message generation", "`ValidatedGeneratedMediaType`", "`PartialContentTypeClassification::{Absent, NonMultipart, MultipartByteRanges}`", "at most 70 characters", "can never fall through to `Absent` or `NonMultipart`", "`PartialResponseDisposition` bound permanently to the exact v0.180.4 validated locally initiated request or v0.181.0 validated promised request", "pushed disposition also requires the exact independent `PushedAssemblyProvenance`", "A pushed 206 without the exact admitted promised-request correlation, handle, and provenance cannot stream into retention or assembly",
        "generation-bound inclusive body accounting",
        "`ValidatedPartialResponseHead`", "`StandaloneOnly`/`NoRecombine`", "`PartialDeliveryPreference::{StreamOnly, RetainOnly, StreamAndRetain}`", "`SelectedPartialDelivery`", "retention write commits", "`VariantFieldLease<'a>`", "`VariantIdentityStorage<'a>`", "only from exclusive `&mut [u8]` or a sealed fixed-arena slot", "DMA/device-backed request and identity buffers remain quiesced and fenced", "caller owns scrubbing copied sensitive bytes", "`VariantIdentityCapacity`", "digest/hash as equality authority", "Raw names/values from sensitive entries never enter Debug", "`ActiveVariantNormalizationBudget`", "exactly once while constructing `VariantSelectionIdentity`", "Never retain a second raw copy merely for identity equality", "Temporary copied raw sensitive bytes are scrubbed", "Comparisons use stored canonical bytes and never parse or normalize again", "`VariantSelectionEvidence`", "Per-response generations never participate in identity equality",
        "`ValidatedIncomplete200Prefix`",
        "against an exclusive `&mut [u8]` or sealed fixed-arena slot", "`TransferDecodedContentEncoded` domain",
        "Clean HTTP/2 END_STREAM length disagreement is malformed stream PROTOCOL_ERROR",
        "successfully completed, framing- and semantics-valid correlated ordinary or pushed 200",
        "opaque `NeedsMultipartConsumer`",
        "well-formed unknown range unit even though a VEF client returns UnsupportedRangeUnit/NoRecombine",
        "generation-safe, fixed-capacity `PartialAssemblyContext`",
        "stored inputs from different Range requests",
        "`CombinablePartialSegment`",
        "`CombinableIncomplete200Prefix`",
        "`AssemblyReplacementKey`",
        "fixed-capacity `PartialCombinationPlan`",
        "safe non-overlapping slice splitting",
        "generation-bound `ReceiptOrderSource`",
        "checked monotonic local `ResponseHeadReceiptOrdinal`",
        "when the complete validated header section is atomically published",
        "permitted trailer ETag can supply final strong-validator evidence", "`Vary: *` is never eligible for cross-request assembly",
        "A full union yields complete 200 with corrected Content-Length", "`ConflictingPartialContent`", "`RequestedOverlapBudget`", "`ActiveOverlapBudget`", "before sorting, output acquisition, or comparison", "cannot reset, clone, enlarge, or be replaced", "A 304, successful revalidation retaining the conflicting validator", "A new navigation or variant-selection identity creates a separate context", "`FullRepresentationFallback::{Keyed, Unkeyed}`", "For a locally initiated request when assembly is enabled, before serializing any request byte or creating its correlation", "engine-only fixed per-shard reserve that Vary fields", "typed local `AssemblyInvalidationCapacity`, emits zero request bytes, creates no correlation, never rotates or clears an existing arena", "ordinary Sans-I/O backpressure until capacity is released", "cannot continue as NoRecombine", "mandatory caller-supplied principal/tenant shard identity", "after the complete promised field block and all CONTINUATION input have decoded", "Atomically preflight/commit the existing promised-stream slot, matching `AssemblyInvalidationHandle`, independent pushed-provenance storage, and mandatory rejection-tombstone/cutoff tracking", "retain the provisional slot, set only `PolicyDisposition::Rejecting`, leave its RFC wire state reserved(remote), queue `ResetReason::PolicyCancel`", "ID is never momentarily untracked", "Apply the exact v0.145.0 terminal/lease pipeline", "END_STREAM leaves policy reset dormant and the sealed section leased through every stage", "valid transfers it into the unpublished promised-message lifecycle", "malformed re-arms and releases once", "fatal failure transfers all cleanup to bounded shutdown", "Reserved(remote) DATA and duplicate promised ID remain connection PROTOCOL_ERROR", "a frozen CANCEL remains the sole immutable frame and continues from its acknowledged suffix", "peer reset aborts after HPACK and releases once", "wire, credit, HPACK, token, and acknowledged-prefix state remain exact", "For push floods independently exhaust all admission/tracking capacities", "typed bounded `PushRejectionTrackingUnavailable` shutdown", "Every provisional slot, handle, provenance lease, reset reservation/command, terminal state/stage, compression workspace, field-section lease, field-block owner, tombstone, and shutdown record releases or transfers exactly once", "sealed non-Copy/non-Clone `PushedAssemblyProvenance`", "Copy into engine-owned fixed storage or independently lease only the minimal immutable", "must not borrow associated-stream application/request buffers", "Associated-stream completion/reset/terminal delivery and buffer recycling cannot release, mutate, or rebind it", "Multiple promised streams from one associated request own independent provenance lifetimes", "linear non-Copy/non-Clone capability bound to exactly one ordinary or promised-request correlation", "terminal-event backpressure", "Release each exactly once only after final completion", "A retry cannot duplicate or rebind the old handle/provenance", "Fixed per-shard and per-connection assembly-admission limits", "one shard's exhaustion cannot borrow or consume another shard's reserve", "concurrent HTTP/2 requests, accepted pushes, and stalled streams", "close/reset/terminally deliver the associated stream immediately", "recycle and overwrite buffers", "every reset/validation record release once", "distinct principal/tenant shards never share an arena", "`ConservativeInvalidationScope::Reserved { handle: AssemblyInvalidationHandle", "`ConservativeInvalidationScope::AssemblyArenaGeneration(ArenaRotationCause)`", "`ArenaRotationCause::{DetectedSemanticCorruption, DetectedStorageCorruption, ExplicitCallerPolicy}`", "internal invariant breach or trusted-storage integrity failure", "malformed/semantic/conflicting peer input cannot mint a corruption cause", "before local request output or promised-request publication", "ordinary and pushed full-200 terminal evidence", "pushed evidence consumes only its immutable `PushedAssemblyProvenance`", "associated-stream teardown, storage reuse, and later caller-policy changes are irrelevant", "`AssemblyInvalidationCapacity`, `PushedAssemblyProvenanceCapacity`, `StreamTrackingUnavailable`, `PushRejectionTrackingUnavailable`, `LeaseHeld`", "invalidation handle and pushed provenance remain non-Copy/non-Clone", "independently leased from associated-stream storage", "Distinguish local `AssemblyInvalidationCapacity`, `PushedAssemblyProvenanceCapacity`, `StreamTrackingUnavailable`, `PushRejectionTrackingUnavailable`, and `OutboundFrameStorageCapacity`", "associated-stream-borrowed provenance or reuse after associated-stream teardown", "promised publication without atomic slot/handle/provenance/rejection-tracking reservation", "tombstone release before cancellation/classification horizon", "`SemanticallyInvalid`", "`PhysicallyReclaimable`", "typed local `LeaseHeld`/capacity", "cannot rotate the arena or evict outside the reserved namespace", "no slot reuse or new mutable alias until every lease drops/acknowledges",
        "`vef-semantics` crate depending only on `vef-core`, `vef-auth`, `vef-media-type`, and `vef-conditions`",
        "`ValidatedResponse` owns or immutably borrows the exact ordered response head, framing plan, sensitivity/indexing metadata, body plan, and trailer permissions",
        "internal `ResponseEmissionPermit` cannot be extracted or paired with caller-supplied data",
        "`vef-http1` and `vef-http2` consume the complete object exactly once",
        "no API accepts `(raw_head, permit)`",
        "raw response heads have no public serialization path",
        "complete role/method/status/field/content semantic matrix before issuing `ValidatedResponse`",
        "Require every generated 401 in HTTP/1 or HTTP/2 to carry at least one valid WWW-Authenticate challenge",
        "normal lowercase HTTP/2 field serialization",
        "reject every locally generated HTTP/2 426 as InvalidState",
        "permit generated 206 only from one matching `SingleRangePlan`",
        "if Date, Cache-Control, ETag, Expires, Content-Location, or Vary exists in its `WouldBe200Snapshot`, require it in 206",
        "require every snapshot 200 field among Content-Location, Date, ETag, Vary, Cache-Control, and Expires",
        "successful unsafe execution instead consumes its admission permit",
        "Permit 304 only from the matching conditional GET/HEAD `PreconditionOutcome`",
        "Bind 416 to the matching unsatisfied range context",
        "Reserve engine-only semantic-validation slots and frozen-head storage",
        "prohibit application validation from consuming that reserve",
        "commit exactly one deterministic close/shutdown action with no partial response output",
        "Invalid locally constructed responses return InvalidState with a typed semantic-construction cause, issue no permit, and serialize zero bytes",
        "invalid received responses—including HTTP/2 426 without Upgrade—remain framing-synchronized and produce a typed SemanticViolation",
        "forwarded responses preserve end-to-end fields—including unmodified WWW-Authenticate and Authentication-Info",
        "same-generation head substitution, mutable-buffer aliasing, field replacement/reordering",
        "keep raw request/response serializers and separable capability/data pairings non-public",
        "owned response builders must obtain and consume the same frozen `ValidatedResponse` object",
        "no facade feature can disable conditional/range/response/trailer validation or the mandatory semantic reserve while retaining serialization",
        "callers cannot construct/clone/copy/reuse/rebind civil-time evidence",
        "Http1DrainingAfterClose",
        "HTTP/2 CONNECT and applicable RFC 8441 END_STREAM enter genuine local/remote half-closed states",
        "map upstream TCP FIN to final DATA plus END_STREAM",
        "close normally only after both directions finish",
        "END_STREAM alone never closes the opposite direction",
        "an injected idle/half-close timeout may abort a stuck tunnel",
    )
    required_contract_text = tuple(text for text in required_contract_text if text not in ("make the ACK eligible only after every participant reports Effective", "`PendingEncoderTableSizeTransition::{None, Pending { smallest_seen, final_value, owners: SettingsTransactionSet }}`", "No later field block may encode while either a provisional transaction or pending encoder-size transition is unresolved", "ACK eligibility requires every participant effective", "Maintain transactions and ACK eligibility in received-frame FIFO order", "cancels that transaction's ACK", "Local post-effect work such as re-encoding a rolled-back Private field block is not a participant", "`OutboundFieldBlock::{Private { stream, generation, hpack: HpackEncoderTransaction, initial, continuations }, FramingCommitted { stream, generation, hpack: HpackEncoderTransaction, remaining_continuations }, HpackCommitted, AbandonedWithConnection}`", "Before any initial HEADERS/PUSH_PROMISE exposure, fully encode the bounded block", "First non-empty initial-frame exposure moves only to FramingCommitted", "every remaining CONTINUATION is non-supersedable and its resources are already owned", "No later field block is encoded against the provisional transaction", "With Private unexposed HPACK, roll back provisional encoder mutations and complete field-block slots", "With FramingCommitted, retain owner references while the pre-reserved block drains without interleaving", "retain the smallest observed maximum and final maximum in receive order", "smallest observed maximum followed by the final maximum", "each generation-bound owner is the v0.108.0 frame-wide `InboundSettingsTransaction`")) + ("`SettingsDisposition::{WaitingParticipants, AckEligible, AckFrozen { acknowledged: 0..=8 }, AckCommitted, AbortedConnection}`", "Every-participant Effective moves WaitingParticipants to AckEligible", "`EncoderTableLimits { peer_received_ceiling: u32, peer_wire_acknowledged_ceiling: u32, selected_capacity: u32, physical_capacity: usize }`", "`PendingEncoderTableSizeTransition::{None, AwaitingSafeApply { obligations: EncoderLimitAckObligationSet }, AppliedAwaitingAckCommit { obligations: EncoderLimitAckObligationSet }}`", "`EncoderLimitAckObligation { transaction_generation, peer_received_ceiling_after_frame, selected_update: Option<EncoderTableUpdateDebt> }`", "`selected_capacity <= peer_received_ceiling`", "`usize::try_from(selected_capacity) <= physical_capacity`", "A peer reduction below selected atomically clamps selection, evicts immediately, and creates a matching selected-capacity update obligation", "a peer increase changes only `peer_received_ceiling` and never enlarges selection", "A local policy reduction creates an update obligation without SETTINGS", "local increase is allowed only within the received, wire-acknowledged, profile, and physical minimum", "If initial selected capacity is below 4096, initialize an obligation", "Encoder update history contains selected-capacity changes only, never raw peer-ceiling changes", "Derive decoder advertised SETTINGS_HEADER_TABLE_SIZE no higher than checked caller storage/profile capacity", "set peer_wire_acknowledged_ceiling to that obligation's frame snapshot and merge only its optional selected_update", "`EncoderTableUpdateDebt { smallest_since_last_exposed_block: u32, final_value: u32 }`", "Private encoding obtains one non-Copy/non-Clone `EncoderTableUpdateDebtLease`", "rollback/capacity/cancellation restores the identical lease before any newer change merges", "ACK commitment never clears or replaces older debt", "first non-empty initial-frame exposure atomically transfers the lease into FramingCommitted", "SETTINGS_HEADER_TABLE_SIZE received after that boundary cannot alter the transferred prefix", "acknowledged offsets 0..=8 remain uncommitted", "only acknowledgement of all nine bytes moves to AckCommitted", "Retain each transaction and every dependent HPACK owner reference until AckCommitted", "No later HEADERS/PUSH_PROMISE block may encode or expose while AwaitingSafeApply or AppliedAwaitingAckCommit remains unresolved", "partial ACK output, stale tokens, or transport failure abandons the connection", "0→4096 and 4096→0→4096", "encoder/decoder table equivalence", "no eviction without a selected-capacity update obligation")
    required_contract_text += ("`ReceiveCredit { advertised_remaining: i32,", "`WindowUpdateOutput::{None, Private { target, generation,", "DATA already decremented both advertised ledgers before publication", "First exposure atomically subtracts that increment", "Acknowledgements 0..=12 retain the slot", "`advertised_remaining` nor the frozen record", "advertised credit changes once and only at byte 13", "immutable target/increment/suffix", "Keep `ReceiveCredit`, `WindowUpdateOutput`, target/generation binding", "all output offsets 0..=13", "31-bit-window", "`PingAckOutput::{ReservedPrivate { transaction_generation, opaque: [u8; 8] }, Frozen { transaction_generation, frame: [u8; 17], acknowledged: 0..=16 }, Complete}`", "Identical payloads remain separate one-for-one RFC obligations and cannot be coalesced or deduplicated", "key is never reissued during the connection", "choose the oldest eligible PING", "charge syntax handling, local-correlation lookup", "Never coalesce or deduplicate replies, including identical payloads", "Acknowledged offsets 0..=16 retain the transaction and slot", "acknowledgement of all 17 bytes produces Complete", "every output split/acknowledged offset 0..=17", "explicit PING priority SHOULD disposition", "Keep `InboundPingTransaction`, `PingAckOutput`, copied opaque bytes", "all output offsets 0..=17", "Size the inbound PING FIFO")
    required_contract_text += ("checked exact output length `17 + debug_len`", "`GoawayOutput::{None, ReservedPrivate { generation, stage,", "`PublishedPeerStreamHighWater` only at first non-empty exposure", "higher peer streams may finish required HPACK synchronization", "`FatalCauseClass` order:", "CompressionSynchronization (COMPRESSION_ERROR)", "REFUSED_STREAM and", "CANCEL remain stream-scoped and never enter this table", "Frozen frame suffix and FramingCommitted", "`ReceivedGoawayCutoffIncrease` connection PROTOCOL_ERROR", "Acknowledged offsets below `total_len` retain the slot", "Only acknowledgement of all `total_len`", "`PeerVisibleCutoff::UnknownAfterPartial`", "`PeerVisibleCutoff::NotVisible`", "overwrite caller debug after command acceptance", "publication high-water", "Above-cutoff “possibly unprocessed” is classification only", "Keep `ShutdownIntent`, `PublishedPeerStreamHighWater`, `GoawayOutput`", "all offsets 0..=`17 + debug_len`", "Size the guaranteed 17-byte GOAWAY minimum slot", "atomically advance the v0.122.0", "Use one connection-wide total order:", "`ControlServiceProfile` provides positive `max_consecutive_ping_acks`", "`ControlDisposition::{Private, Frozen, Complete,", "`AbandonedByConnectionFatal { connection_generation }`", "On full fatal GOAWAY commitment, atomically transition every remaining", "SETTINGS performs no ACK commitment", "GOAWAY performs none of this cleanup", "Exercise every pair of scheduler classes")
    required_contract_text += ("`OutboundSettingsTransaction::{ReservedPrivate { generation,", "`9 + 6 * entry_count`", "future outstanding-ACK FIFO slot", "Track `locally_requested`", "sole eligible frame until its full commitment", "Full-frame acknowledgement atomically applies the prevalidated commit", "Peer ACK consumes the oldest CommittedAwaitingAck record exactly once", "before exposure selects AbandonedBeforeExposure", "commit plan is the sole wire-commit authority", "outbound non-ACK SETTINGS", "no allocator or fallible capacity step", "Audit `OutboundSettingsTransaction`", "adapters obey the same rule", "`advance_io(output_ack, input)`", "`DriverCommitOrderViolation`", "accept peer input as implicit acknowledgement", "any ACK with no committed transaction is unsolicited", "Never retain, defer, or later consume an ACK", "ReservedPrivate/Frozen transaction exists", "speculative SETTINGS ACK at every", "A local correlation becomes ACK-matchable only after full acknowledgement", "A response or dependent frame on a locally initiated stream cannot be consumed", "Audit Sans-I/O causality", "While any `OutputToken` is", "caller-provided dependent/independent flag or trait", "oversized acknowledgement is state-neutral", "A valid zero acknowledgement invalidates the offer", "Subsequent input failure never", "never bytes merely queued in caller-controlled memory", "`AcceptedPrivate -> Frozen -> HeadCommitted -> MessageCommitted` or `Abandoned`", "outstanding-response FIFO populated only by v0.54.0 `HeadCommitted`", "full acknowledgement of the complete 100 response head", "Partial 2xx acknowledgement followed by transport failure closes", "full acknowledgement of the complete 101 response head", "`EarlyFinalBodyDisposition::{ContinueToDelimiterForReuse, SuppressRemainingAndClose, AlreadyMessageCommitted, TransportAborted}`", "releases only bytes certified not consumed by the transport", "partially transmitted fixed-length request or chunked request lacking its terminating zero chunk", "A 417 retry obtains a fresh exchange generation", "`AlreadyMessageCommitted` is automatic and cannot be requested", "`ContinueToDelimiterForReuse` is legal only while persistence remains", "`Connection: close`, HTTP/1.0 default-close", "`EarlyFinalTransportAction::{SealHttpOutputAndDrainResponse,", "core never assumes TCP half-close exists through TLS", "Map `SealHttpOutputAndDrainResponse`", "`BridgeTransaction::{Reserved, DownstreamRequestValidated, UpstreamRequestCommitted, UpstreamSuccessValidated, DownstreamSuccessFrozen, ActiveAfterDownstreamSuccessCommitted", "`OutboundHeadCommit::{Http1(HeadCommitted), Http2(OutboundFieldBlockHpackCommitted)}`", "`InboundHeadValidation::{Http1(ValidatedInboundHead), Http2(ValidatedInboundFieldSection)}`", "complete HEADERS/CONTINUATION compression synchronization", "`TerminalValidation::Valid`, final-2xx classification, exact upstream request/stream-generation correlation", "never contains, requires, or fabricates outbound `HpackCommitted`", "`BridgeInputLease::{Http1(OverreadLease), Http2(PendingConnectLease)}`", "linear reference to the existing v0.130.0/v0.136.0 PendingConnect ranges", "creates no second byte store, copy, discard, or credit owner", "Application acknowledgement or policy discard remains the sole reclamation path", "padding-only and mixed padded DATA", "Never expose downstream 101/2xx before complete upstream inbound validation", "Failure after any downstream success exposure closes downstream", "Over-read/PendingConnect bytes remain owned by their original leg")
    required_contract_text = tuple(text for text in required_contract_text if text not in ("`OutboundHeadCommit::{Http1(HeadCommitted), Http2(OutboundFieldBlockHpackCommitted)}`", "`InboundHeadValidation::{Http1(ValidatedInboundHead), Http2(ValidatedInboundFieldSection)}`", "`TerminalValidation::Valid`, final-2xx classification, exact upstream request/stream-generation correlation")) + ("`ValidatedDownstreamRequest`, `CommittedUpstreamRequest`, `ValidatedUpstreamSuccess`, and `CommittedDownstreamSuccess`", "bridge generation, connection and leg identity, client/server role, request/response kind, exchange or stream generation, and exact HTTP/1 or HTTP/2 head identity", "`ValidatedDownstreamRequest` requires complete request semantic validation", "`CommittedUpstreamRequest` requires final HTTP/1 request-head acknowledgement or outbound HTTP/2 whole-field-block commitment", "`ValidatedUpstreamSuccess` requires complete inbound head validation", "`CommittedDownstreamSuccess` requires final HTTP/1 success-head acknowledgement or outbound HTTP/2 whole-field-block commitment", "no phase accepts another phase's capability even when connection, generation, or numeric stream identifiers coincide", "`AwaitingConnectOutcome -> AwaitingBridgeActivation { bridge_generation } -> ActiveTunnel`", "all existing DATA ranges in exact order", "semantic length versus padding charge", "stream and connection receive-credit ownership", "END_STREAM/remote-half-close state", "immutable first-terminal-cause attribution", "Success HEADERS followed in the same input buffer by DATA", "upstream END_STREAM before downstream success exposure fails the handshake", "preserves it as a pending remote half-close published immediately after Active", "RST_STREAM or fatal failure before downstream success exposure remains an HTTP-framed downstream failure", "after any success exposure it selects close-plus-abort and never another HTTP response", "Feed success HEADERS followed in the same input buffer by DATA, padded DATA, DATA plus END_STREAM, and RST_STREAM", "cross every downstream-success output offset", "pending directional FIN exactly once")
    failures.extend(f"missing concrete security contract: {contract_text}" for contract_text in required_contract_text if contract_text not in detailed)
    if "after acknowledgement while retaining independent inbound hard limits" in detailed:
        failures.append("MAX_FRAME_SIZE is still applied after acknowledgement")
    failures.extend(["unsafe SETTINGS ACK banking remains"] if "EarlyPeerAckPending" in detailed + compact else []); failures.extend(["unsafe bridge evidence or ownership remains"] if any(text in detailed + compact for text in ("HandshakeBarrier", "TransitionBarrier", "DownstreamCommitted", "UpstreamCommitted", "both barrier orders", "both completion orders", "`UpstreamSuccessValidated` requires the complete HTTP/1 success head or complete HTTP/2 HEADERS/CONTINUATION block at `HpackCommitted`", "both legs' bounded over-read capacity", "both bounded over-read stores", "request/success commitment is complete field-block `HpackCommitted`")) else [])
    failures.extend(["message-kind-ambiguous bridge evidence remains"] if any(text in detailed + compact for text in ("OutboundHeadCommit", "InboundHeadValidation")) else [])
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("release plan: 225 minor milestones, thirteen patch stops, and two release candidates")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
