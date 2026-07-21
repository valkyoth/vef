# VEF Version Plan

Status: planning document

`1.0.0` is the first serious production-ready HTTP crate. The `0.x`
sequence uses one narrow primary outcome per minor release. Patch releases may
split work, remediate findings, or correct an already shipped milestone.
Nothing required by the declared 1.0 profiles is silently postponed.

This is the compact index. [`RELEASE_PLAN.md`](RELEASE_PLAN.md) is
authoritative and gives every version a goal, deliverables, verification, exit
criteria, and exact-commit pentest stop.

## Release rules

Every version updates applicable requirement evidence, positive and negative
tests, fragmentation/capacity behavior, documentation, release notes, and the
threat-model delta. The full repository gate and a pentest of the exact
implementation commit are mandatory before tagging.

## Phase 1 — Foundation and shared types

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.1.0` | Workspace, crate boundaries, licenses, security policy, and release evidence | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.2.0` | Empty vef-core with strict no_std and unsafe prohibition | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.3.0` | Checked byte cursor with no unchecked indexing | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.4.0` | Parser progress contract and NeedMore model | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.5.0` | Configurable limits and checked size domains | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.6.0` | Work, transition, and allocation budget counters | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.7.0` | Structured error and diagnostic taxonomy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.8.0` | Case-sensitive extension-capable Method | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.9.0` | Validated StatusCode with unknown-code preservation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.10.0` | Version and wire-version representation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.11.0` | Case-insensitive validated FieldName | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.12.0` | Byte-oriented FieldValue with raw and semantic views | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.13.0` | Ordered FieldLine and FieldSection | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.14.0` | Four request-target forms without normalization | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.15.0` | Request and response control-data types | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.16.0` | Requirement manifest, conformance harness, and full foundation audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 2 — HTTP/1 start lines and field sections

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.17.0` | Client, server, and intermediary role types and parser profiles | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.18.0` | Incremental request-line state machine | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.19.0` | Incremental status-line state machine | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.20.0` | Every-byte-boundary fragmentation support | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.21.0` | Strict CRLF and incomplete-line handling | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.22.0` | Incremental field-line parser | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.23.0` | Explicit OWS removal with raw-value preservation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.24.0` | obs-fold, whitespace-before-colon, and control-byte rejection | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.25.0` | Field count, line, and section limit enforcement | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.26.0` | HTTP/1.1 Host validation and duplicate rejection | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.27.0` | Method and request-target-form coherence | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.28.0` | Checked Content-Length grammar | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.29.0` | Repeated and comma-list Content-Length resolution | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.30.0` | Transfer-Encoding grammar and ordering | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.31.0` | TE/CL conflict resolution and mandatory close action | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.32.0` | Head serialization, round-trip properties, and full phase audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 3 — HTTP/1 body framing and persistence

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.33.0` | Central message-body-length decision algorithm | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.34.0` | Fixed-length body decoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.35.0` | Close-delimited response decoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.36.0` | Checked hexadecimal chunk-size parser | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.37.0` | Incremental chunk-data and CRLF state | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.38.0` | Bounded chunk-extension parser | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.39.0` | Last-chunk and trailer transition | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.40.0` | Trailer declarations and prohibited-trailer policy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.41.0` | Chunked encoder and caller-owned output buffering | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.42.0` | HTTP/1.1 persistence and Connection semantics | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.43.0` | Sequential request/response connection state | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.44.0` | Optional bounded pipelining queue | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.45.0` | Informational response lifecycle | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.46.0` | Expect: 100-continue state | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.47.0` | EOF, truncation, and incomplete-message rules | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.48.0` | Full framing, persistence, and body audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 4 — HTTP/1 roles, transitions, and legacy profiles

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.49.0` | HEAD request response-framing context | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.50.0` | 1xx, 204, 304, and body-forbidden response handling | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.51.0` | CONNECT request and successful tunnel transition | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.52.0` | RFC 9931 optimistic CONNECT protections | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.53.0` | 101 Switching Protocols transition | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.54.0` | Connection-nominated and hop-by-hop field handling | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.55.0` | Safe forwarding and connection-close action API | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.56.0` | RFC 1945 HTTP/1.0 parser and serializer | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.57.0` | HTTP/1.0 default connection-close lifecycle | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.58.0` | Explicit HTTP/1.0 keep-alive extension profile | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.59.0` | Explicit HTTP/0.9 client | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.60.0` | Explicit HTTP/0.9 server | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.61.0` | HTTP/0.9 dedicated-listener and disabled-default policy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.62.0` | HTTP/0.9 cross-protocol attack corpus | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.63.0` | Full CL.TE, TE.CL, duplicate, and whitespace smuggling corpus | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.64.0` | Full HTTP/0.9–1.1 pentest and conformance audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 5 — I/O and secure adapter contracts

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.65.0` | Minimal synchronous vef-io traits | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.66.0` | Runtime-neutral poll traits | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.67.0` | External clock and deadline abstraction | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.68.0` | Cancellation and bounded backpressure contract | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.69.0` | Standard blocking-stream adapter | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.70.0` | Standard nonblocking-stream adapter | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.71.0` | Generic async-poll driver and downstream runtime conformance contract | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.72.0` | Generic connection driver and deterministic fake transport | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.73.0` | TLS metadata, peer identity, and ALPN interface | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.74.0` | Dependency-free TLS provider adapter contract | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.75.0` | ALPN and provider-capability validation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.76.0` | TLS session and certificate-metadata policy boundary | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.77.0` | Downstream TLS adapter conformance kit | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.78.0` | HTTP/1 TLS and ALPN selection policy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.79.0` | HTTP/2 TLS prerequisites and rejection policy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.80.0` | Adapter, cancellation, timeout, and platform-boundary audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 6 — HPACK

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.81.0` | Prefix-integer decoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.82.0` | Prefix-integer encoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.83.0` | Integer overflow, overlong encoding, and proof harnesses | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.84.0` | Bounded string-literal codec | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.85.0` | Reproducibly generated Huffman tables | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.86.0` | Constant-memory Huffman decoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.87.0` | Huffman encoder | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.88.0` | Static table | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.89.0` | Bounded dynamic table | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.90.0` | Correct table eviction and size updates | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.91.0` | Indexed representation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.92.0` | Literal with incremental indexing | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.93.0` | Literal without indexing | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.94.0` | Never-indexed representation and sensitive-field policy | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.95.0` | Encoded, decoded, table, count, and work limits | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.96.0` | Full HPACK interoperability, fuzzing, and pentest audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 7 — HTTP/2 framing and state

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.97.0` | Client and server connection prefaces | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.98.0` | Nine-octet frame header and size validation | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.99.0` | DATA frames and padding | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.100.0` | HEADERS frames | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.101.0` | CONTINUATION and field-block atomicity | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.102.0` | SETTINGS parsing, validation, and acknowledgement | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.103.0` | PING | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.104.0` | GOAWAY | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.105.0` | RST_STREAM | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.106.0` | WINDOW_UPDATE and checked window arithmetic | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.107.0` | Legacy PRIORITY wire elements | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.108.0` | PUSH_PROMISE | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.109.0` | Unknown and extension-frame handling | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.110.0` | Stream-ID allocation, parity, and exhaustion | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.111.0` | Exhaustive stream-state machine | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.112.0` | Connection state, frame sequencing, and full phase audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 8 — HTTP/2 semantics and flow control

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.113.0` | HPACK and field-block integration | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.114.0` | Pseudo-field ordering, uniqueness, and context rules | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.115.0` | Connection-specific field rejection and TE exception | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.116.0` | HTTP request mapping | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.117.0` | HTTP response mapping | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.118.0` | Informational responses and trailers | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.119.0` | HTTP/2 Cookie splitting and HTTP/1 joining | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.120.0` | Stream-level flow control | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.121.0` | Connection-level flow control | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.122.0` | SETTINGS synchronization and outstanding-state tracking | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.123.0` | Concurrent-stream admission and refusal | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.124.0` | Outbound scheduling and queue backpressure | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.125.0` | Graceful shutdown and retry-safe GOAWAY behavior | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.126.0` | Complete server-push lifecycle | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.127.0` | TLS h2 ALPN and cleartext prior-knowledge integration | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.128.0` | Full RFC 9113 core conformance and pentest audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 9 — HTTP/2 hardening, translation, and extensions

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.129.0` | Frame-rate and state-transition budgets | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.130.0` | Rapid-reset and recently-closed-stream defenses | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.131.0` | SETTINGS and PING acknowledgement amplification defenses | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.132.0` | CONTINUATION and decompressed-header bomb defenses | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.133.0` | Tiny WINDOW_UPDATE and flow-control churn defenses | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.134.0` | Hard outbound queue ceilings | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.135.0` | First-class HTTP/1 to HTTP/2 translation engine | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.136.0` | Host, :authority, and effective-URI consistency | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.137.0` | HTTP/1-to-HTTP/2 connection-field stripping | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.138.0` | CONNECT and tunnel translation across HTTP versions | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.139.0` | Optional RFC 8441 extended CONNECT | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.140.0` | RFC 9651 Structured Fields parser | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.141.0` | RFC 9218 Priority field | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.142.0` | PRIORITY_UPDATE and priority-settings behavior | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.143.0` | Stateful hostile-peer and multi-implementation interop campaign | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.144.0` | Full intermediary, extension, and denial-of-service audit | Full phase audit, complete regression gate, and exact-commit pentest |

## Phase 10 — Stable APIs, portability, and production hardening

| Version | Primary outcome | Completion gate |
| --- | --- | --- |
| `0.145.0` | Stable client facade | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.146.0` | Stable origin-server facade | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.147.0` | Stable proxy, gateway, and tunnel facade | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.148.0` | Ergonomic owned API under alloc | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.149.0` | Fixed-capacity caller-storage API without allocator | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.150.0` | Standard-error integration and stable diagnostics | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.151.0` | Facade feature matrix and accidental-dependency tests | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.152.0` | Minimal and no-default-feature build matrix | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.153.0` | Full 32-bit arithmetic and capacity matrix | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.154.0` | Big-endian, unaligned-access, and serialization matrix | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.155.0` | x86, Arm, AArch64, and RISC-V target campaign | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.156.0` | Linux, Windows, BSD, macOS, Android, iOS, and future Aesynx adapter contract | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.157.0` | Long-running HTTP/1 soak and fault-injection campaign | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.158.0` | Long-running HTTP/2 multiplexing and cancellation soak | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.159.0` | Independent whole-project security and conformance audit | Named behavior, limits, tests, evidence, and exact-commit pentest |
| `0.160.0` | Audit remediation, API freeze, and 1.0 release-candidate readiness | Full phase audit, complete regression gate, and exact-commit pentest |

## Release candidates

| Version | Outcome | Gate |
| --- | --- | --- |
| `1.0.0-rc.1` | Public API freeze, public interop, documentation review, package dry runs | No new features after cut; complete independent pentest |
| `1.0.0-rc.2` | RC1 remediation and repeated full assurance campaign | Final dependency, provenance, conformance, portability, and security evidence |
| `1.0.0` | First serious production-ready HTTP crate | Every declared acceptance criterion verified; exact approved RC artifacts promoted unchanged |
