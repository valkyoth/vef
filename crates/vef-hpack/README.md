<p align="center">
  <b>bounded HPACK encoding and decoding for VEF.</b><br>
  Small auditable boundaries, no_std operation, explicit limits, and security-gated release evidence.
</p>

<div align="center">
  <a href="https://crates.io/crates/vef">vef crate</a>
  |
  <a href="https://docs.rs/vef-hpack">Docs.rs</a>
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

# vef-hpack

Support crate for `vef`: bounded HPACK encoding and decoding.

Most users should depend on the facade crate:

```toml
[dependencies]
vef = "0.1.0"
```

This package is published separately so VEF can preserve small review,
dependency, capability, and trust boundaries. It is a lower-level building
block until the facade documentation declares its public surface stable.

## Responsibility

Checked prefix integers, string literals, Huffman coding, static and dynamic tables, representation codecs, and indexing policy.

It is independent of HTTP/2 connection state and applies separate encoded, decoded, table, field-count, and work limits.

## Foundation status

Version 0.1.0 establishes the crate boundary and compilation policy only. It
does not claim completed HTTP behavior. The crate is dependency-free except
for first-party VEF workspace crates, uses `no_std`, forbids unsafe Rust, and
supports Rust 1.90.0 through 1.97.1.

Every later capability is introduced by a narrow release-plan milestone with
positive, negative, fragmentation, resource-limit, adversarial, and regression
evidence plus an exact-commit pentest before tagging.
