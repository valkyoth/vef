# VEF Modularity Policy

Status: enforced policy

- `vef` is a facade, not an implementation home.
- Shared semantics, HTTP/1, HPACK, HTTP/2, and I/O contracts remain separate
  crates.
- `lib.rs` files are wiring and public API shape.
- Non-generated Rust source files may never exceed 500 lines.
- Files approaching 300 lines receive a split review.
- Tests should live beside focused modules or in equally focused test files.
- Adapters depend inward; core crates never depend on adapters.
- Feature flags cannot silently enable allocation, `std`, networking, TLS,
  runtimes, filesystem access, clocks, or thread-local storage.
- A new crate must represent a real trust, dependency, publication, platform,
  or capability boundary.

Run `scripts/validate-modularity-policy.sh check` locally and in CI.
