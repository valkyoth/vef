# Security Policy

VEF is security-sensitive protocol software. Treat every parser, serializer,
framing decision, state transition, compression operation, flow-control
calculation, adapter boundary, test tool, release script, and CI change as
hostile-input-facing until reviewed and tested.

## Reporting

Do not publish exploitable details in a public issue. Use GitHub private
security advisories once the public repository is configured, or contact the
maintainer privately. Include the affected version, role, byte sequence,
fragmentation, limits, and state when safe to do so.

## Routine checks

```bash
scripts/checks.sh
scripts/check_latest_tools.sh
scripts/check-rust-version-matrix.sh
cargo deny check
cargo audit
scripts/generate-sbom.sh --check
```

GitHub CodeQL default setup is required. VEF intentionally has no advanced
CodeQL workflow while default setup is active.

## Release gate

Every release requires a pentest of the exact implementation commit. The final
tag points to a direct child commit that adds only the permanent passing report
under `security/pentest/vX.Y.Z.md`. Critical and high findings block release.
See [`docs/RELEASE_PLAN.md`](docs/RELEASE_PLAN.md).

## Dependency policy

VEF currently permits no third-party Rust crates, including build and dev
dependencies. Workspace path dependencies are first-party only. A future
exception requires explicit maintainer approval, a dedicated adapter boundary,
a license/source/feature/security review, and a release-plan amendment. Core
protocol crates remain dependency-free except for other first-party VEF crates.
