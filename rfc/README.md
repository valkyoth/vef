# RFC Reference Copies

This directory contains exact unmodified plain-text files from the
[RFC Editor](https://www.rfc-editor.org/). VEF uses them for requirement
extraction, implementation review, tests, errata decisions, and security work.

VEF claims no copyright in these documents. Every RFC retains its authorship,
status, notices, and IETF Trust terms. RFC files are not licensed under VEF's
MIT or Apache-2.0 software licenses and are excluded from crate packages.

## Baseline

| RFC | Role |
| --- | --- |
| 1945 | Historical HTTP/1.0 and simple-request compatibility profile |
| 2119, 8174 | Normative requirement language |
| 3986 | URI generic syntax |
| 7301 | ALPN |
| 7541 | HPACK |
| 8441 | HTTP/2 extended CONNECT |
| 8446 | TLS 1.3 context for adapter prerequisites |
| 9110 | HTTP semantics |
| 9111 | HTTP caching semantics preserved for external caches |
| 9112 | HTTP/1.1 messaging |
| 9113 | HTTP/2 |
| 9218 | Extensible HTTP priorities |
| 9651 | Structured Fields |
| 9931 | Current HTTP/1.1 optimistic-transition security update |

`SOURCES` is the reviewed allowlist. `SHA256SUMS` locks exact bytes.
`scripts/fetch-rfcs.sh` fetches missing sources, and
`scripts/verify-rfcs.sh` rejects drift. Published RFCs are immutable;
corrections are tracked in `spec/errata/`.
