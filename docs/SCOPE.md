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
| WebSocket opening handshake | RFC 6455 | Optional isolated handshake extension; no frame protocol |
| ALPN | RFC 7301 | Adapter selection metadata |
| HPACK | RFC 7541 | Complete bounded encoder and decoder |
| TLS 1.3 context | RFC 8446 | Provider metadata and HTTP/2 prerequisite checks |
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
received multipart/byteranges bodies remain opaque bytes that can be preserved
and forwarded without boundary or part validation. VEF parses entity tags,
HTTP dates, conditional fields, Range, and Content-Range and evaluates them
against explicit caller-supplied representation evidence; it does not own a
representation store, cache, wall clock, or multipart assembler.

RFC 7239 `Forwarded` transformation is also outside 1.0. Via parsing,
preservation, and generation are covered by RFC 9110 instead.

Future Aesynx integration implements VEF I/O and timing contracts; it does not
change protocol validity or require protocol-engine forks.
