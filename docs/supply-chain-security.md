# VEF Supply-Chain Security

Status: enforced policy

VEF currently admits no third-party Rust crates. The lockfile may contain only
workspace packages. `scripts/check_dependency_policy.py` checks Cargo metadata
and fails if any package has a registry or git source.

Defense in depth still includes:

- `cargo deny check` for licenses, advisories, sources, and duplicates;
- `cargo audit` for RustSec advisories;
- a committed SBOM compared with freshly generated content;
- Dependabot visibility for Cargo and GitHub Actions;
- full-SHA GitHub Action pins;
- live stable Rust, cargo-tool, and action-tag checks before release;
- checksum-locked RFC sources fetched only from the RFC Editor.

Any future third-party proposal must be requested explicitly by the maintainer,
remain outside protocol cores, and document necessity, latest version, license,
maintenance, source, features, `std`/unsafe/native-code impact, attack surface,
alternatives, tests, and removal strategy before admission.
