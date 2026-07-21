<p align="center">
  <b>Security-first, dependency-free, no_std HTTP protocol engines for Rust.</b><br>
  Built in small audited releases with deterministic framing, explicit limits, and exact RFC-to-test evidence.
</p>

<div align="center">
  <a href="https://crates.io/crates/vef">Crates.io</a>
  |
  <a href="https://docs.rs/vef">Docs.rs</a>
  |
  <a href="https://github.com/valkyoth/vef/blob/main/docs/RELEASE_PLAN.md">Release Plan</a>
  |
  <a href="https://github.com/valkyoth/vef/blob/main/docs/threat-model.md">Threat Model</a>
  |
  <a href="https://github.com/valkyoth/vef/blob/main/SECURITY.md">Security</a>
</div>

<br>

<p align="center">
  <a href="https://github.com/valkyoth/vef">
    <img src="https://raw.githubusercontent.com/valkyoth/vef/main/.github/images/vef.webp" alt="VEF Rust HTTP crate overview">
  </a>
</p>

# vef

Security-first, dependency-free, `no_std` HTTP protocol engines for Rust.

VEF is being built as a runtime-independent, incremental HTTP implementation.
The protocol crates consume bytes, emit events, accept commands, and serialize
into caller-provided buffers. They do not own sockets, runtimes, TLS sessions,
clocks, tasks, or application handlers.

> VEF is at the repository-foundation milestone. Version 0.1.0 does not claim
> working HTTP support. The detailed path to the first production release is
> tracked in the release plan.

## 1.0 target

VEF 1.0.0 targets:

- explicit HTTP/0.9 compatibility, disabled by default;
- HTTP/1.0 and HTTP/1.1, including RFC 9931 security updates;
- HTTP/2 and HPACK;
- shared HTTP semantics for clients, origin servers, intermediaries, proxies,
  gateways, and tunnel endpoints;
- deterministic sans-I/O engines with caller-controlled backpressure;
- dependency-free `no_std` protocol crates;
- both caller-owned storage and optional future allocation-backed APIs;
- Linux, Windows, BSD, macOS, Android, and iOS integration paths;
- a future Aesynx adapter without changing protocol engines;
- traceability from applicable RFC requirements to code, tests, and evidence.

HTTP/3 and QUIC are explicitly outside VEF 1.x.

## Workspace

| Crate | Responsibility | Default environment |
| --- | --- | --- |
| `vef` | Small feature-controlled facade | `no_std` |
| `vef-core` | Shared semantics, types, limits, policies, diagnostics | `no_std` |
| `vef-http1` | HTTP/0.9, HTTP/1.0, and HTTP/1.1 engines | `no_std` |
| `vef-hpack` | Bounded HPACK encoder and decoder | `no_std` |
| `vef-http2` | HTTP/2 framing, stream state, flow control, semantics | `no_std` |
| `vef-io` | Runtime-neutral I/O, polling, clock, and deadline contracts | `no_std` |

The current workspace contains no third-party Rust crates. Runtime and TLS
integrations described in the roadmap are separate future trust boundaries;
they cannot be admitted without an explicit policy decision and never become
dependencies of the protocol crates.

## Rust version support

VEF uses Rust edition 2024 and resolver 3. The MSRV is Rust `1.90.0`.
Development and full release gates are pinned to current stable Rust `1.97.1`.

| Rust | Required evidence |
| --- | --- |
| `1.90.0` | MSRV build, tests, all targets, and all features |
| `1.91.0`-`1.96.1` | Workspace compatibility checks for every stable patch release |
| `1.97.0` | Compatibility check covering the superseded stable patch |
| `1.97.1` | Full formatting, lint, test, policy, audit, package, and release gate |

The networked release preflight compares the pin against Rust's official
stable manifest and verifies the versions of security tools and GitHub Actions.

## Security invariants

- One deterministic framing and routing interpretation for accepted input.
- Explicit bounds for every peer-controlled length, count, queue, table, and
  unit of work.
- No peer-induced panic, integer wrap, hidden allocation, or silent truncation.
- No request becomes application-visible before all control data and fields
  needed for framing and routing are validated.
- No protocol transition, HTTP/0.9 fallback, or TLS selection is guessed.
- Stream errors cannot corrupt unrelated HTTP/2 streams.
- Protocol crates forbid unsafe Rust and third-party dependencies.
- Every release is pentested at the exact implementation commit before tag.

See the [threat model](https://github.com/valkyoth/vef/blob/main/docs/threat-model.md),
[security controls](https://github.com/valkyoth/vef/blob/main/docs/security-controls.md), and
[security policy](https://github.com/valkyoth/vef/blob/main/SECURITY.md).

## Standards

Exact RFC Editor text copies are tracked under `rfc/`, locked by SHA-256, and
excluded from crate packages. Requirements and errata decisions are separate
from the immutable RFC text. See the
[source policy](https://github.com/valkyoth/vef/blob/main/docs/rfc-source-policy.md)
and [conformance plan](https://github.com/valkyoth/vef/blob/main/docs/CONFORMANCE.md).

## Checks

```bash
scripts/checks.sh
```

Networked maintenance and release checks:

```bash
scripts/check_latest_tools.sh
scripts/fetch-rfcs.sh
scripts/check-rust-version-matrix.sh
cargo deny check
cargo audit
```

## Documentation

- [Architecture](https://github.com/valkyoth/vef/blob/main/docs/ARCHITECTURE.md)
- [Scope](https://github.com/valkyoth/vef/blob/main/docs/SCOPE.md)
- [Implementation plan](https://github.com/valkyoth/vef/blob/main/docs/IMPLEMENTATION_PLAN.md)
- [Version index](https://github.com/valkyoth/vef/blob/main/docs/VERSION_PLAN.md)
- [Authoritative release plan](https://github.com/valkyoth/vef/blob/main/docs/RELEASE_PLAN.md)
- [Testing strategy](https://github.com/valkyoth/vef/blob/main/docs/TESTING.md)
- [Platform support](https://github.com/valkyoth/vef/blob/main/docs/platform-support.md)
- [Toolchain policy](https://github.com/valkyoth/vef/blob/main/docs/toolchain-policy.md)
- [Modularity policy](https://github.com/valkyoth/vef/blob/main/docs/modularity-policy.md)

## License

VEF source code is licensed under either the
[MIT License](https://github.com/valkyoth/vef/blob/main/LICENSE-MIT) or the
[Apache License, Version 2.0](https://github.com/valkyoth/vef/blob/main/LICENSE-APACHE), at your option. RFC copies retain
their own IETF notices and are not covered by the software license.
