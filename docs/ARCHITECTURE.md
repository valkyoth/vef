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
  |-- vef-http1 -----> vef-core
  |-- vef-http2 -----> vef-core
  |       `----------> vef-hpack -----> vef-core
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

## Shared model

`vef-core` will own byte-oriented methods, status codes, versions, schemes,
authorities, four explicit request-target forms, ordered field lines, message
heads, trailers, limits, policies, roles, and structured diagnostics. Ordered
field lines remain authoritative: duplicate order is preserved and values are
never combined automatically.

## HTTP/1 family

`vef-http1` contains HTTP/0.9, HTTP/1.0, and HTTP/1.1 because they share a
line-oriented messaging family. HTTP/0.9 has dedicated constructors, no
automatic fallback, no proxy forwarding by default, and no persistent
connection. Framing is decided exactly once after complete field validation.

The parser is an incremental byte-state machine. It does not decode the whole
message as UTF-8, reparse accepted bytes, scan without limits, allocate from a
peer length, or continue indefinitely without progress.

## HPACK and HTTP/2

`vef-hpack` owns checked integer, string, Huffman, table, and representation
codecs. It has no HTTP/2 stream or transport knowledge.

`vef-http2` separates frame codec, connection/stream state, and HTTP semantic
mapping. Stream transitions are exhaustive. Header blocks are atomic across
CONTINUATION frames. Flow-control arithmetic uses protocol-domain integers,
never unchecked `usize` calculations. Independent budgets cover hostile
control-frame rates, compression work, stream churn, and outbound responses.

## Roles and transitions

Client, origin server, forward proxy, reverse proxy, gateway, tunnel endpoint,
and intermediary policies are explicit. CONNECT and Upgrade do not expose
post-transition bytes until success is confirmed. TLS adapters return
authenticated protocol-selection metadata; they never mutate an established
HTTP engine into a different protocol.

## Third-party boundary

The repository currently permits no third-party Rust crates. Planned Tokio,
Rustls, OpenSSL, and s2n integration names describe future boundaries, not
current dependencies. Admission requires explicit maintainer approval and a
release-plan update. Such crates remain optional, separately published, and
outward-facing so `vef`, `vef-core`, `vef-http1`, `vef-hpack`, `vef-http2`, and
the base `vef-io` remain independent.
