# VEF Version Plan

Status: planning document

`1.0.0` is the first serious production-ready VEF release. The `0.x`
sequence deliberately assigns one primary security or protocol outcome to each
minor version. Patch releases may split a milestone or remediate findings, but
cannot silently move a required 1.0 behavior out of scope.

This file is the compact index. [`RELEASE_PLAN.md`](RELEASE_PLAN.md) is
authoritative and gives every version its goal, deliverables, verification,
exit criteria, dependency context, and exact-commit pentest stop.

## Why the sequence changed

The gap review found that the former 160-stop plan delayed caller-owned storage,
mixed HTTP/0.9 into the HTTP/1 package, under-specified parser progress and
transactional state, and grouped too many HTTP/2 denial-of-service controls.
Because no release tag exists, the plan is renumbered now rather than preserving
unsafe sequencing for compatibility.

| Gap closed | Versions | Binding plan consequence |
| --- | --- | --- |
| Standards and errata applicability | `0.23.0`, then each protocol phase exit | Disposition RFC 9112/9113 errata; record RFC 9298 non-applicability unless the profile changes; map RFC 3986, 7301, 8446, and 9111 preservation duties. |
| Impossible zero progress | `0.4.0` | Use a non-zero progress representation and distinguish input, output, event, transition, and blocked states. |
| Caller-owned bounded storage | `0.7.0`, `0.41.0`, `0.84.0`, `0.150.0` | Land fixed storage before protocol parsers and retain explicit capacity and partial-output behavior through public APIs. |
| HTTP/0.9 cross-protocol risk | `0.67.0`–`0.70.0` | Publish a separate package with explicit client/server/listener selection, exact grammar, default close, no forwarding, and no fallback. |
| HTTP/1 ambiguity and transition timing | `0.25.0`–`0.66.0` | Separate request/response parsers, strict line policy, one framing decision, typed close actions, and RFC 9931/WebSocket transition barriers. |
| Transactional HPACK/HTTP/2 state | `0.90.0`, `0.106.0`–`0.109.0` | Parse and validate into typed deltas, then commit atomically with generation-checked stream slots and connection-wide error isolation. |
| HTTP/2 denial of service | `0.119.0`–`0.130.0` | Bound stream admission, ACK obligations, control traffic, tombstones, work, and reserved outbound control capacity. |
| Application visibility and role safety | `0.132.0`–`0.157.0` | Expose messages only after validation and preserve authority, hop, cache, correlation, retry, transition, and half-close semantics. |
| Brynja and Aesynx readiness | `0.160.0`–`0.167.0` | Keep adapters separate, require authenticated ALPN metadata, prohibit TLS early data for 1.0, and define fixed-memory nonblocking capabilities. |
| Production evidence | `0.178.0`–`0.181.0`, RC1, RC2 | Require exact-commit pentests, an independent audit, verified remediation, packaging, SBOM, provenance, and repeated release-candidate gates. |

## Universal release gate

Every milestone must name its API or invariant, update applicable requirement
and errata evidence, add positive and negative tests, prove bounded work and
storage behavior, prevent partial application publication, update threat-model
and release-note deltas, pass the Rust `1.90.0`–`1.97.1` and supported-target
gates, and stop for a pentest of the exact implementation commit. A phase exit
adds full conformance review, stateful fuzzing, interoperability,
resource-exhaustion testing, and manual security review.

## Phase 1 — Foundation and shared semantics

No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.1.0` | Workspace, crate boundaries, licenses, security policy, and release evidence | Repository foundation; Unlocks Core module skeleton and authority boundaries. |
| `0.2.0` | Core module skeleton and authority boundaries | Requires Workspace, crate boundaries, licenses, security policy, and release evidence; Unlocks Checked byte cursor with no unchecked indexing. |
| `0.3.0` | Checked byte cursor with no unchecked indexing | Requires Core module skeleton and authority boundaries; Unlocks Non-zero parser progress and explicit blocked states. |
| `0.4.0` | Non-zero parser progress and explicit blocked states | Requires Checked byte cursor with no unchecked indexing; Unlocks Checked protocol-size domains. |
| `0.5.0` | Checked protocol-size domains | Requires Non-zero parser progress and explicit blocked states; Unlocks Decode, work, transition, and response budgets. |
| `0.6.0` | Decode, work, transition, and response budgets | Requires Checked protocol-size domains; Unlocks Caller-owned arenas and fixed-capacity stores. |
| `0.7.0` | Caller-owned arenas and fixed-capacity stores | Requires Decode, work, transition, and response budgets; Unlocks Structured errors and error-scope taxonomy. |
| `0.8.0` | Structured errors and error-scope taxonomy | Requires Caller-owned arenas and fixed-capacity stores; Unlocks Case-sensitive extension-capable Method. |
| `0.9.0` | Case-sensitive extension-capable Method | Requires Structured errors and error-scope taxonomy; Unlocks Validated StatusCode with unknown-code preservation. |
| `0.10.0` | Validated StatusCode with unknown-code preservation | Requires Case-sensitive extension-capable Method; Unlocks HTTP version and wire-version representation. |
| `0.11.0` | HTTP version and wire-version representation | Requires Validated StatusCode with unknown-code preservation; Unlocks Case-insensitive validated FieldName. |
| `0.12.0` | Case-insensitive validated FieldName | Requires HTTP version and wire-version representation; Unlocks Byte-oriented FieldValue with raw and semantic views. |
| `0.13.0` | Byte-oriented FieldValue with raw and semantic views | Requires Case-insensitive validated FieldName; Unlocks Ordered FieldLine and FieldSection storage. |
| `0.14.0` | Ordered FieldLine and FieldSection storage | Requires Byte-oriented FieldValue with raw and semantic views; Unlocks Request-target, URI, and authority types. |
| `0.15.0` | Request-target, URI, and authority types | Requires Ordered FieldLine and FieldSection storage; Unlocks Request and response control-data types. |
| `0.16.0` | Request and response control-data types | Requires Request-target, URI, and authority types; Unlocks Role, profile, and policy types. |
| `0.17.0` | Role, profile, and policy types | Requires Request and response control-data types; Unlocks Minimal synchronous I/O contracts. |
| `0.18.0` | Minimal synchronous I/O contracts | Requires Role, profile, and policy types; Unlocks Runtime-neutral readiness and poll contracts. |
| `0.19.0` | Runtime-neutral readiness and poll contracts | Requires Minimal synchronous I/O contracts; Unlocks Injected monotonic clock and deadline contracts. |
| `0.20.0` | Injected monotonic clock and deadline contracts | Requires Runtime-neutral readiness and poll contracts; Unlocks Cancellation, close, and bounded-backpressure contracts. |
| `0.21.0` | Cancellation, close, and bounded-backpressure contracts | Requires Injected monotonic clock and deadline contracts; Unlocks Deterministic fake transport and driver harness. |
| `0.22.0` | Deterministic fake transport and driver harness | Requires Cancellation, close, and bounded-backpressure contracts; Unlocks Requirement, applicability, and errata evidence system. |
| `0.23.0` | Requirement, applicability, and errata evidence system | Requires Deterministic fake transport and driver harness; Unlocks Foundation Kani campaign, audit, and pentest. |
| `0.24.0` | Foundation Kani campaign, audit, and pentest | Requires Requirement, applicability, and errata evidence system; Unlocks HTTP/1 role and parser profiles. |

## Phase 2 — HTTP/1 and isolated HTTP/0.9

HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.25.0` | HTTP/1 role and parser profiles | Requires Foundation Kani campaign, audit, and pentest; Unlocks Incremental HTTP/1 request-line parser. |
| `0.26.0` | Incremental HTTP/1 request-line parser | Requires HTTP/1 role and parser profiles; Unlocks Incremental HTTP/1 status-line parser. |
| `0.27.0` | Incremental HTTP/1 status-line parser | Requires Incremental HTTP/1 request-line parser; Unlocks Every-byte fragmentation support. |
| `0.28.0` | Every-byte fragmentation support | Requires Incremental HTTP/1 status-line parser; Unlocks Strict CRLF and separately named LF compatibility. |
| `0.29.0` | Strict CRLF and separately named LF compatibility | Requires Every-byte fragmentation support; Unlocks Incremental HTTP/1 field-line parser. |
| `0.30.0` | Incremental HTTP/1 field-line parser | Requires Strict CRLF and separately named LF compatibility; Unlocks Explicit OWS handling with raw-value preservation. |
| `0.31.0` | Explicit OWS handling with raw-value preservation | Requires Incremental HTTP/1 field-line parser; Unlocks Injection-proof HTTP/1 serialization. |
| `0.32.0` | Injection-proof HTTP/1 serialization | Requires Explicit OWS handling with raw-value preservation; Unlocks obs-fold, bad colon whitespace, and control-byte rejection. |
| `0.33.0` | obs-fold, bad colon whitespace, and control-byte rejection | Requires Injection-proof HTTP/1 serialization; Unlocks Field count, line, and section caps. |
| `0.34.0` | Field count, line, and section caps | Requires obs-fold, bad colon whitespace, and control-byte rejection; Unlocks HTTP/1.1 Host validation and duplicate rejection. |
| `0.35.0` | HTTP/1.1 Host validation and duplicate rejection | Requires Field count, line, and section caps; Unlocks Method and request-target-form coherence. |
| `0.36.0` | Method and request-target-form coherence | Requires HTTP/1.1 Host validation and duplicate rejection; Unlocks Checked Content-Length grammar. |
| `0.37.0` | Checked Content-Length grammar | Requires Method and request-target-form coherence; Unlocks Repeated and comma-list Content-Length resolution. |
| `0.38.0` | Repeated and comma-list Content-Length resolution | Requires Checked Content-Length grammar; Unlocks Transfer-Encoding grammar and ordering. |
| `0.39.0` | Transfer-Encoding grammar and ordering | Requires Repeated and comma-list Content-Length resolution; Unlocks TE/CL conflict resolution and mandatory close action. |
| `0.40.0` | TE/CL conflict resolution and mandatory close action | Requires Transfer-Encoding grammar and ordering; Unlocks Central HTTP/1 message-body-length algorithm. |
| `0.41.0` | Central HTTP/1 message-body-length algorithm | Requires TE/CL conflict resolution and mandatory close action; Unlocks Fixed-length body decoder. |
| `0.42.0` | Fixed-length body decoder | Requires Central HTTP/1 message-body-length algorithm; Unlocks Close-delimited response decoder. |
| `0.43.0` | Close-delimited response decoder | Requires Fixed-length body decoder; Unlocks Checked chunk-size parser. |
| `0.44.0` | Checked chunk-size parser | Requires Close-delimited response decoder; Unlocks Incremental chunk-data state. |
| `0.45.0` | Incremental chunk-data state | Requires Checked chunk-size parser; Unlocks Bounded chunk-extension parser. |
| `0.46.0` | Bounded chunk-extension parser | Requires Incremental chunk-data state; Unlocks Last-chunk and trailer transition. |
| `0.47.0` | Last-chunk and trailer transition | Requires Bounded chunk-extension parser; Unlocks Trailer declarations and prohibited-trailer policy. |
| `0.48.0` | Trailer declarations and prohibited-trailer policy | Requires Last-chunk and trailer transition; Unlocks Chunked encoder with partial-output state. |
| `0.49.0` | Chunked encoder with partial-output state | Requires Trailer declarations and prohibited-trailer policy; Unlocks HTTP/1.1 persistence and Connection semantics. |
| `0.50.0` | HTTP/1.1 persistence and Connection semantics | Requires Chunked encoder with partial-output state; Unlocks Sequential request/response connection state. |
| `0.51.0` | Sequential request/response connection state | Requires HTTP/1.1 persistence and Connection semantics; Unlocks Optional bounded pipelining queue. |
| `0.52.0` | Optional bounded pipelining queue | Requires Sequential request/response connection state; Unlocks Informational response lifecycle. |
| `0.53.0` | Informational response lifecycle | Requires Optional bounded pipelining queue; Unlocks Expect: 100-continue state. |
| `0.54.0` | Expect: 100-continue state | Requires Informational response lifecycle; Unlocks EOF, truncation, and incomplete-message rules. |
| `0.55.0` | EOF, truncation, and incomplete-message rules | Requires Expect: 100-continue state; Unlocks HEAD response-framing context. |
| `0.56.0` | HEAD response-framing context | Requires EOF, truncation, and incomplete-message rules; Unlocks 1xx, 204, 304, and body-forbidden response handling. |
| `0.57.0` | 1xx, 204, 304, and body-forbidden response handling | Requires HEAD response-framing context; Unlocks CONNECT request and successful tunnel transition. |
| `0.58.0` | CONNECT request and successful tunnel transition | Requires 1xx, 204, 304, and body-forbidden response handling; Unlocks RFC 9931 optimistic-data protections. |
| `0.59.0` | RFC 9931 optimistic-data protections | Requires CONNECT request and successful tunnel transition; Unlocks 101 Switching Protocols transition. |
| `0.60.0` | 101 Switching Protocols transition | Requires RFC 9931 optimistic-data protections; Unlocks RFC 6455 WebSocket opening handshake only. |
| `0.61.0` | RFC 6455 WebSocket opening handshake only | Requires 101 Switching Protocols transition; Unlocks Connection-nominated and hop-by-hop field handling. |
| `0.62.0` | Connection-nominated and hop-by-hop field handling | Requires RFC 6455 WebSocket opening handshake only; Unlocks Safe forwarding and explicit reframing plan. |
| `0.63.0` | Safe forwarding and explicit reframing plan | Requires Connection-nominated and hop-by-hop field handling; Unlocks RFC 1945 HTTP/1.0 parser and hardened profile. |
| `0.64.0` | RFC 1945 HTTP/1.0 parser and hardened profile | Requires Safe forwarding and explicit reframing plan; Unlocks HTTP/1.0 default-close lifecycle. |
| `0.65.0` | HTTP/1.0 default-close lifecycle | Requires RFC 1945 HTTP/1.0 parser and hardened profile; Unlocks Explicit HTTP/1.0 keep-alive extension profile. |
| `0.66.0` | Explicit HTTP/1.0 keep-alive extension profile | Requires HTTP/1.0 default-close lifecycle; Unlocks Separate vef-http09 package and exact grammar. |
| `0.67.0` | Separate vef-http09 package and exact grammar | Requires Explicit HTTP/1.0 keep-alive extension profile; Unlocks Explicit HTTP/0.9 client API. |
| `0.68.0` | Explicit HTTP/0.9 client API | Requires Separate vef-http09 package and exact grammar; Unlocks Explicit HTTP/0.9 server and dedicated-listener API. |
| `0.69.0` | Explicit HTTP/0.9 server and dedicated-listener API | Requires Explicit HTTP/0.9 client API; Unlocks HTTP/0.9 cross-protocol rejection corpus. |
| `0.70.0` | HTTP/0.9 cross-protocol rejection corpus | Requires Explicit HTTP/0.9 server and dedicated-listener API; Unlocks HTTP/1 smuggling and ambiguity corpus. |
| `0.71.0` | HTTP/1 smuggling and ambiguity corpus | Requires HTTP/0.9 cross-protocol rejection corpus; Unlocks HTTP/1 and HTTP/0.9 conformance audit and pentest. |
| `0.72.0` | HTTP/1 and HTTP/0.9 conformance audit and pentest | Requires HTTP/1 smuggling and ambiguity corpus; Unlocks HPACK prefix-integer decoder. |

## Phase 3 — HPACK and HTTP/2

HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.73.0` | HPACK prefix-integer decoder | Requires HTTP/1 and HTTP/0.9 conformance audit and pentest; Unlocks HPACK prefix-integer encoder. |
| `0.74.0` | HPACK prefix-integer encoder | Requires HPACK prefix-integer decoder; Unlocks HPACK integer overflow and minimality proofs. |
| `0.75.0` | HPACK integer overflow and minimality proofs | Requires HPACK prefix-integer encoder; Unlocks HPACK string representation codec. |
| `0.76.0` | HPACK string representation codec | Requires HPACK integer overflow and minimality proofs; Unlocks HPACK Huffman tables. |
| `0.77.0` | HPACK Huffman tables | Requires HPACK string representation codec; Unlocks HPACK Huffman decoder. |
| `0.78.0` | HPACK Huffman decoder | Requires HPACK Huffman tables; Unlocks HPACK Huffman encoder. |
| `0.79.0` | HPACK Huffman encoder | Requires HPACK Huffman decoder; Unlocks HPACK static table. |
| `0.80.0` | HPACK static table | Requires HPACK Huffman encoder; Unlocks HPACK dynamic table storage. |
| `0.81.0` | HPACK dynamic table storage | Requires HPACK static table; Unlocks HPACK eviction and oversize-entry behavior. |
| `0.82.0` | HPACK eviction and oversize-entry behavior | Requires HPACK dynamic table storage; Unlocks HPACK table-size update and SETTINGS coupling. |
| `0.83.0` | HPACK table-size update and SETTINGS coupling | Requires HPACK eviction and oversize-entry behavior; Unlocks HPACK caller-owned ring lookup. |
| `0.84.0` | HPACK caller-owned ring lookup | Requires HPACK table-size update and SETTINGS coupling; Unlocks HPACK indexed representation. |
| `0.85.0` | HPACK indexed representation | Requires HPACK caller-owned ring lookup; Unlocks HPACK incremental-indexing literal. |
| `0.86.0` | HPACK incremental-indexing literal | Requires HPACK indexed representation; Unlocks HPACK non-indexing and never-indexed literal. |
| `0.87.0` | HPACK non-indexing and never-indexed literal | Requires HPACK incremental-indexing literal; Unlocks Sensitive-field indexing policy. |
| `0.88.0` | Sensitive-field indexing policy | Requires HPACK non-indexing and never-indexed literal; Unlocks Independent HPACK decode limits. |
| `0.89.0` | Independent HPACK decode limits | Requires Sensitive-field indexing policy; Unlocks Transactional HPACK context and error scope. |
| `0.90.0` | Transactional HPACK context and error scope | Requires Independent HPACK decode limits; Unlocks HPACK conformance audit and pentest. |
| `0.91.0` | HPACK conformance audit and pentest | Requires Transactional HPACK context and error scope; Unlocks HTTP/2 client and server prefaces. |
| `0.92.0` | HTTP/2 client and server prefaces | Requires HPACK conformance audit and pentest; Unlocks HTTP/2 frame-header codec. |
| `0.93.0` | HTTP/2 frame-header codec | Requires HTTP/2 client and server prefaces; Unlocks DATA frame codec. |
| `0.94.0` | DATA frame codec | Requires HTTP/2 frame-header codec; Unlocks HEADERS frame codec. |
| `0.95.0` | HEADERS frame codec | Requires DATA frame codec; Unlocks CONTINUATION frame codec. |
| `0.96.0` | CONTINUATION frame codec | Requires HEADERS frame codec; Unlocks SETTINGS frame codec. |
| `0.97.0` | SETTINGS frame codec | Requires CONTINUATION frame codec; Unlocks PING frame codec. |
| `0.98.0` | PING frame codec | Requires SETTINGS frame codec; Unlocks GOAWAY frame codec. |
| `0.99.0` | GOAWAY frame codec | Requires PING frame codec; Unlocks RST_STREAM frame codec. |
| `0.100.0` | RST_STREAM frame codec | Requires GOAWAY frame codec; Unlocks WINDOW_UPDATE codec and checked windows. |
| `0.101.0` | WINDOW_UPDATE codec and checked windows | Requires RST_STREAM frame codec; Unlocks Legacy PRIORITY frame handling. |
| `0.102.0` | Legacy PRIORITY frame handling | Requires WINDOW_UPDATE codec and checked windows; Unlocks PUSH_PROMISE frame handling. |
| `0.103.0` | PUSH_PROMISE frame handling | Requires Legacy PRIORITY frame handling; Unlocks Unknown-frame extension policy. |
| `0.104.0` | Unknown-frame extension policy | Requires PUSH_PROMISE frame handling; Unlocks HTTP/2 stream-identifier rules. |
| `0.105.0` | HTTP/2 stream-identifier rules | Requires Unknown-frame extension policy; Unlocks Generation-checked stream table and tombstones. |
| `0.106.0` | Generation-checked stream table and tombstones | Requires HTTP/2 stream-identifier rules; Unlocks Exhaustive stream-state graph. |
| `0.107.0` | Exhaustive stream-state graph | Requires Generation-checked stream table and tombstones; Unlocks Connection sequencing and error-scope deltas. |
| `0.108.0` | Connection sequencing and error-scope deltas | Requires Exhaustive stream-state graph; Unlocks Atomic HPACK header-block integration. |
| `0.109.0` | Atomic HPACK header-block integration | Requires Connection sequencing and error-scope deltas; Unlocks Pseudo-field ordering and uniqueness. |
| `0.110.0` | Pseudo-field ordering and uniqueness | Requires Atomic HPACK header-block integration; Unlocks Connection-specific field and TE validation. |
| `0.111.0` | Connection-specific field and TE validation | Requires Pseudo-field ordering and uniqueness; Unlocks HTTP/2 request mapping. |
| `0.112.0` | HTTP/2 request mapping | Requires Connection-specific field and TE validation; Unlocks HTTP/2 response mapping. |
| `0.113.0` | HTTP/2 response mapping | Requires HTTP/2 request mapping; Unlocks Informational responses and trailers. |
| `0.114.0` | Informational responses and trailers | Requires HTTP/2 response mapping; Unlocks Cookie field combination and Set-Cookie preservation. |
| `0.115.0` | Cookie field combination and Set-Cookie preservation | Requires Informational responses and trailers; Unlocks Stream flow control. |
| `0.116.0` | Stream flow control | Requires Cookie field combination and Set-Cookie preservation; Unlocks Connection flow control. |
| `0.117.0` | Connection flow control | Requires Stream flow control; Unlocks SETTINGS outstanding-ACK accounting. |
| `0.118.0` | SETTINGS outstanding-ACK accounting | Requires Connection flow control; Unlocks Bounded stream admission. |
| `0.119.0` | Bounded stream admission | Requires SETTINGS outstanding-ACK accounting; Unlocks Bounded outbound scheduling. |
| `0.120.0` | Bounded outbound scheduling | Requires Bounded stream admission; Unlocks GOAWAY cutoff and retry classification. |
| `0.121.0` | GOAWAY cutoff and retry classification | Requires Bounded outbound scheduling; Unlocks Server-push lifecycle. |
| `0.122.0` | Server-push lifecycle | Requires GOAWAY cutoff and retry classification; Unlocks ALPN and cleartext prior-knowledge selection. |
| `0.123.0` | ALPN and cleartext prior-knowledge selection | Requires Server-push lifecycle; Unlocks Independent HTTP/2 rate and work budgets. |
| `0.124.0` | Independent HTTP/2 rate and work budgets | Requires ALPN and cleartext prior-knowledge selection; Unlocks Rapid-reset defenses. |
| `0.125.0` | Rapid-reset defenses | Requires Independent HTTP/2 rate and work budgets; Unlocks SETTINGS amplification defenses. |
| `0.126.0` | SETTINGS amplification defenses | Requires Rapid-reset defenses; Unlocks PING flood defenses. |
| `0.127.0` | PING flood defenses | Requires SETTINGS amplification defenses; Unlocks CONTINUATION bomb defenses. |
| `0.128.0` | CONTINUATION bomb defenses | Requires PING flood defenses; Unlocks WINDOW_UPDATE churn defenses. |
| `0.129.0` | WINDOW_UPDATE churn defenses | Requires CONTINUATION bomb defenses; Unlocks Reserved control-output queues. |
| `0.130.0` | Reserved control-output queues | Requires WINDOW_UPDATE churn defenses; Unlocks HTTP/2 conformance audit and pentest. |
| `0.131.0` | HTTP/2 conformance audit and pentest | Requires Reserved control-output queues; Unlocks HTTP/1 and HTTP/2 translation model. |

## Phase 4 — Proxy, client, server, and public APIs

Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.132.0` | HTTP/1 and HTTP/2 translation model | Requires HTTP/2 conformance audit and pentest; Unlocks Effective URI and authority consistency. |
| `0.133.0` | Effective URI and authority consistency | Requires HTTP/1 and HTTP/2 translation model; Unlocks Connection-field stripping, Via, and cache preservation. |
| `0.134.0` | Connection-field stripping, Via, and cache preservation | Requires Effective URI and authority consistency; Unlocks CONNECT translation across HTTP versions. |
| `0.135.0` | CONNECT translation across HTTP versions | Requires Connection-field stripping, Via, and cache preservation; Unlocks RFC 8441 extended CONNECT. |
| `0.136.0` | RFC 8441 extended CONNECT | Requires CONNECT translation across HTTP versions; Unlocks WebSocket HTTP/1 to HTTP/2 handshake bridge. |
| `0.137.0` | WebSocket HTTP/1 to HTTP/2 handshake bridge | Requires RFC 8441 extended CONNECT; Unlocks Structured Fields. |
| `0.138.0` | Structured Fields | Requires WebSocket HTTP/1 to HTTP/2 handshake bridge; Unlocks RFC 9218 priority semantics. |
| `0.139.0` | RFC 9218 priority semantics | Requires Structured Fields; Unlocks PRIORITY_UPDATE frame support. |
| `0.140.0` | PRIORITY_UPDATE frame support | Requires RFC 9218 priority semantics; Unlocks Client request builder and target forms. |
| `0.141.0` | Client request builder and target forms | Requires PRIORITY_UPDATE frame support; Unlocks Client correlation, cancellation, and retry tokens. |
| `0.142.0` | Client correlation, cancellation, and retry tokens | Requires Client request builder and target forms; Unlocks Origin-server role API. |
| `0.143.0` | Origin-server role API | Requires Client correlation, cancellation, and retry tokens; Unlocks Forward-proxy role API. |
| `0.144.0` | Forward-proxy role API | Requires Origin-server role API; Unlocks Reverse-proxy and gateway role API. |
| `0.145.0` | Reverse-proxy and gateway role API | Requires Forward-proxy role API; Unlocks Tunnel lifecycle and half-close semantics. |
| `0.146.0` | Tunnel lifecycle and half-close semantics | Requires Reverse-proxy and gateway role API; Unlocks Upgrade transformation boundary. |
| `0.147.0` | Upgrade transformation boundary | Requires Tunnel lifecycle and half-close semantics; Unlocks GOAWAY, 421, and retry coordination. |
| `0.148.0` | GOAWAY, 421, and retry coordination | Requires Upgrade transformation boundary; Unlocks Optional alloc-backed convenience API. |
| `0.149.0` | Optional alloc-backed convenience API | Requires GOAWAY, 421, and retry coordination; Unlocks Fixed-capacity caller-storage public API. |
| `0.150.0` | Fixed-capacity caller-storage public API | Requires Optional alloc-backed convenience API; Unlocks Stable diagnostics and security events. |
| `0.151.0` | Stable diagnostics and security events | Requires Fixed-capacity caller-storage public API; Unlocks Feature and dependency-policy surface. |
| `0.152.0` | Feature and dependency-policy surface | Requires Stable diagnostics and security events; Unlocks Multi-implementation interoperability. |
| `0.153.0` | Multi-implementation interoperability | Requires Feature and dependency-policy surface; Unlocks Adversarial and stateful fuzz campaign. |
| `0.154.0` | Adversarial and stateful fuzz campaign | Requires Multi-implementation interoperability; Unlocks Compile-fail state and lifetime tests. |
| `0.155.0` | Compile-fail state and lifetime tests | Requires Adversarial and stateful fuzz campaign; Unlocks Long-running soak and exhaustion campaign. |
| `0.156.0` | Long-running soak and exhaustion campaign | Requires Compile-fail state and lifetime tests; Unlocks Role and API conformance audit and pentest. |
| `0.157.0` | Role and API conformance audit and pentest | Requires Long-running soak and exhaustion campaign; Unlocks Standard blocking-stream adapter. |

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence

Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.158.0` | Standard blocking-stream adapter | Requires Role and API conformance audit and pentest; Unlocks Standard nonblocking-stream adapter. |
| `0.159.0` | Standard nonblocking-stream adapter | Requires Standard blocking-stream adapter; Unlocks Brynja TLS provider contract and admission review. |
| `0.160.0` | Brynja TLS provider contract and admission review | Requires Standard nonblocking-stream adapter; Unlocks Separate vef-brynja adapter crate. |
| `0.161.0` | Separate vef-brynja adapter crate | Requires Brynja TLS provider contract and admission review; Unlocks Authenticated ALPN and HTTP/2 TLS prerequisites. |
| `0.162.0` | Authenticated ALPN and HTTP/2 TLS prerequisites | Requires Separate vef-brynja adapter crate; Unlocks TLS 1.3 early-data prohibition and close semantics. |
| `0.163.0` | TLS 1.3 early-data prohibition and close semantics | Requires Authenticated ALPN and HTTP/2 TLS prerequisites; Unlocks Aesynx fixed-memory capability profile. |
| `0.164.0` | Aesynx fixed-memory capability profile | Requires TLS 1.3 early-data prohibition and close semantics; Unlocks Aesynx transport and readiness adapter. |
| `0.165.0` | Aesynx transport and readiness adapter | Requires Aesynx fixed-memory capability profile; Unlocks Aesynx timer and deadline adapter. |
| `0.166.0` | Aesynx timer and deadline adapter | Requires Aesynx transport and readiness adapter; Unlocks Aesynx kernel integration tests. |
| `0.167.0` | Aesynx kernel integration tests | Requires Aesynx timer and deadline adapter; Unlocks 32-bit target campaign. |
| `0.168.0` | 32-bit target campaign | Requires Aesynx kernel integration tests; Unlocks Big-endian target campaign. |
| `0.169.0` | Big-endian target campaign | Requires 32-bit target campaign; Unlocks Cross-architecture campaign. |
| `0.170.0` | Cross-architecture campaign | Requires Big-endian target campaign; Unlocks Linux, Windows, BSD, macOS, Android, and iOS matrix. |
| `0.171.0` | Linux, Windows, BSD, macOS, Android, and iOS matrix | Requires Cross-architecture campaign; Unlocks Kani shared-core proofs. |
| `0.172.0` | Kani shared-core proofs | Requires Linux, Windows, BSD, macOS, Android, and iOS matrix; Unlocks Kani HTTP/1 proofs. |
| `0.173.0` | Kani HTTP/1 proofs | Requires Kani shared-core proofs; Unlocks Kani HPACK proofs. |
| `0.174.0` | Kani HPACK proofs | Requires Kani HTTP/1 proofs; Unlocks Kani HTTP/2 proofs. |
| `0.175.0` | Kani HTTP/2 proofs | Requires Kani HPACK proofs; Unlocks Stateful cargo-fuzz campaign. |
| `0.176.0` | Stateful cargo-fuzz campaign | Requires Kani HTTP/2 proofs; Unlocks Differential and interoperability campaign. |
| `0.177.0` | Differential and interoperability campaign | Requires Stateful cargo-fuzz campaign; Unlocks Whole-project conformance audit and pentest. |
| `0.178.0` | Whole-project conformance audit and pentest | Requires Differential and interoperability campaign; Unlocks Independent security audit. |
| `0.179.0` | Independent security audit | Requires Whole-project conformance audit and pentest; Unlocks Audit remediation and API freeze. |
| `0.180.0` | Audit remediation and API freeze | Requires Independent security audit; Unlocks Documentation, packaging, SBOM, provenance, and RC readiness. |
| `0.181.0` | Documentation, packaging, SBOM, provenance, and RC readiness | Requires Audit remediation and API freeze; Unlocks the 1.0 release candidates. |

## Release candidates and 1.0

| Version | Primary outcome | Exit context |
| --- | --- | --- |
| `1.0.0-rc.1` | Public API freeze, interoperability, documentation, and package review | No features after the freeze; repeat the full gate and exact-commit pentest. |
| `1.0.0-rc.2` | RC1 remediation and complete evidence replay | No unreviewed behavior change or unresolved critical/high finding. |
| `1.0.0` | First serious production-ready VEF HTTP release | All applicable requirements, platform claims, audit remediation, and release evidence are verified. |
