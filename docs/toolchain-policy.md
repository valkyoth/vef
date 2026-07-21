# VEF Toolchain Policy

Status: enforced policy

VEF pins stable Rust `1.97.1` and supports every stable release from Rust
`1.90.0` through `1.97.1`, including patch releases in that interval.

Rules:

- `workspace.package.rust-version` remains `1.90` until a reviewed MSRV change.
- The release gate compares the pin with Rust's official stable manifest.
- `scripts/check-rust-version-matrix.sh` checks every supported toolchain.
- The full release gate runs on the pinned stable patch.
- Normal builds and releases never require nightly.
- Tool and GitHub Action pins are checked live before each release.
- A newly released stable patch extends the upper bound after its full gate
  passes; it does not change the MSRV automatically.

The current matrix is `1.90.0`, `1.91.0`, `1.91.1`, `1.92.0`, `1.93.0`,
`1.93.1`, `1.94.0`, `1.94.1`, `1.95.0`, `1.96.0`, `1.96.1`, `1.97.0`, and
`1.97.1`.
