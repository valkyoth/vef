#!/usr/bin/env python3
"""Check that the compact and detailed plans cover exactly v0.1.0..v0.225.0."""

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
    failures: list[str] = []
    if detailed_versions != expected:
        failures.append("detailed plan does not cover v0.1.0 through v0.225.0 exactly")
    if compact_versions != expected:
        failures.append("version index does not cover v0.1.0 through v0.225.0 exactly")
    for heading in ("Goal", "Deliverables", "Verification", "Exit criteria"):
        if detailed.count(f"#### {heading}") != 225:
            failures.append(f"expected 225 {heading} sections")
    if detailed.count("implementation stop reached. Run pentest for this exact commit.") != 227:
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
        "Retry safety, idempotency, and body-replayability contract",
        "Exact CONNECT, Upgrade, and tunnel byte-handoff ownership",
        "HTTP/2 TLS admission prerequisites and authenticated metadata",
        "Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge",
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
        ("Connection-field stripping, Via, and cache preservation", "Normative HTTP/1 and HTTP/2 translation matrix"),
        ("Max-Forwards TRACE and OPTIONS intermediary semantics", "Normative HTTP/1 and HTTP/2 translation matrix"),
        ("HTTP/1 TE request-field and trailers forwarding semantics", "Normative HTTP/1 and HTTP/2 translation matrix"),
        ("Normative HTTP/1 and HTTP/2 translation matrix", "CONNECT translation across HTTP versions"),
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
    ):
        failures.append("superseded or generic acceptance wording remains in detailed plan")
    required_contract_text = (
        "borrowed BodyChunk whose acknowledged prefix alone may be released",
        "encoded header-block bytes, decoded bytes, field count",
        "Host/:authority disagreement",
        "flow-controlled payload length (including Pad Length and padding)",
        "before emitting its ACK",
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
        "never silently ignore them when the ACK/output budget is exhausted",
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
        "require 100 to commit before 101 whenever Expect: 100-continue applies",
        "make every later HTTP response parse, serialization, body, trailer, pipeline, or reuse operation an InvalidState",
        "advertises 1 only with an available native endpoint or fully configured bridge/entropy capability",
        "For HTTP/1 downstream to HTTP/2 upstream",
        "for HTTP/2 downstream to HTTP/1 upstream",
        "without processing key/accept upstream",
        "no WebSocket byte crosses until both sides commit",
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
        "before DNS, dialing, upstream bytes, or tunnel publication",
        "outbound CONNECT builders reject request content, Content-Length, and Transfer-Encoding",
        "bounded 400 plus mandatory close and never reparses following bytes",
        "successful server responses forbid Content-Length and Transfer-Encoding",
        "every CONNECT response carries typed non-cacheable metadata",
        "never synthesize it when absent, handle zero locally without forwarding",
        "TRACE client builders reject content, Cookie, Authorization, Proxy-Authorization",
        "bounded sanitized reflection representation excluding sensitive fields",
        "OPTIONS client content requires a valid Content-Type",
        "shared validated ConnectAuthority between HTTP/1 authority-form and HTTP/2",
        "same ConnectTargetPolicy authorization before DNS, dialing, upstream output, or tunnel publication",
        "RST_STREAM, TCP reset/error, fatal TLS alert",
        "TrustedRequestContext carrying authenticated transport-security state",
        "never infer TLS from Aesynx handle or socket types",
        "1xx, 204, 205, 304, and body-forbidden response handling",
        "outbound HTTP/1 205 permit only zero-content serialization",
        "inbound 205 still uses the ordinary HTTP/1 body-length algorithm",
        "never misclassify following octets as a new response",
        "bounded PendingConnect while target authorization/dialing is incomplete",
        "no forwarding before authorization plus successful connection",
        "once connected allow only DATA and applicable stream-management frames",
        "map TCP failure/reset to RST_STREAM(CONNECT_ERROR)",
        "map stream/connection failure to upstream TCP reset",
        "route CONNECT PendingConnect/connected ranges only to stream-local bounded tunnel ownership",
        "for 205 require initial response HEADERS with END_STREAM and optional Content-Length: 0",
        "established HTTP/2 CONNECT or RFC 8441 stream expose separate tunnel DATA/finish commands",
        "ServerWideOptionsCandidate",
        "convert it to asterisk-form only at the final origin-facing hop",
        "present-but-empty query, `OPTIONS /`, and every resource path remain distinct",
        "map its empty-path/absent-query target to HTTP/1 `OPTIONS *` or HTTP/2 `:path: *`",
        "treat HTTP/2 DATA after initial CONNECT HEADERS as tunnel bytes",
        "Http1DrainingAfterClose",
        "HTTP/2 CONNECT and applicable RFC 8441 END_STREAM enter genuine local/remote half-closed states",
        "map upstream TCP FIN to final DATA plus END_STREAM",
        "close normally only after both directions finish",
        "END_STREAM alone never closes the opposite direction",
        "an injected idle/half-close timeout may abort a stuck tunnel",
    )
    for contract_text in required_contract_text:
        if contract_text not in detailed:
            failures.append(f"missing concrete security contract: {contract_text}")
    if "after acknowledgement while retaining independent inbound hard limits" in detailed:
        failures.append("MAX_FRAME_SIZE is still applied after acknowledgement")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("release plan: 225 detailed milestones plus two release candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
