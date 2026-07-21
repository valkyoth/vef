# Contributing to VEF

VEF is security-sensitive HTTP protocol infrastructure. Contributions must
preserve deterministic framing, explicit resource limits, `no_std` operation,
dependency-free protocol crates, and the documented crate boundaries.

## License

By contributing, you agree that your contribution is licensed under
`MIT OR Apache-2.0`.

## Development

Use the pinned toolchain and run:

```bash
scripts/checks.sh
```

Protocol changes must identify applicable requirement IDs, add positive,
negative, fragmentation, and adversarial tests, and update the threat model.
Do not publish exploitable details in a public issue; follow
[`SECURITY.md`](../SECURITY.md).

VEF currently admits no third-party Rust crates. Any proposal to change that
policy requires explicit maintainer approval and a dedicated trust-boundary
crate; it must never silently expand a core crate.
