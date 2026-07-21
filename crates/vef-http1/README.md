<p align="center">
  <b>deterministic HTTP/0.9, HTTP/1.0, and HTTP/1.1 engines for VEF.</b><br>
  Small auditable boundaries, no_std operation, explicit limits, and security-gated release evidence.
</p>

<div align="center">
  <a href="https://crates.io/crates/vef">vef crate</a>
  |
  <a href="https://docs.rs/vef-http1">Docs.rs</a>
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

# vef-http1

Support crate for `vef`: deterministic HTTP/0.9, HTTP/1.0, and HTTP/1.1 engines.

Most users should depend on the facade crate:

```toml
[dependencies]
vef = "0.1.0"
```

This package is published separately so VEF can preserve small review,
dependency, capability, and trust boundaries. It is a lower-level building
block until the facade documentation declares its public surface stable.

## Responsibility

Incremental start-line, field, framing, body, persistence, CONNECT, Upgrade, and legacy-profile state machines.

HTTP/0.9 is explicit and disabled by default; malformed HTTP/1 input is never reinterpreted as HTTP/0.9.

## Foundation status

Version 0.1.0 establishes the crate boundary and compilation policy only. It
does not claim completed HTTP behavior. The crate is dependency-free except
for first-party VEF workspace crates, uses `no_std`, forbids unsafe Rust, and
supports Rust 1.90.0 through 1.97.1.

Every later capability is introduced by a narrow release-plan milestone with
positive, negative, fragmentation, resource-limit, adversarial, and regression
evidence plus an exact-commit pentest before tagging.
