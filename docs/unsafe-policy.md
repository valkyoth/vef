# VEF Unsafe Policy

Status: enforced policy

All current first-party crates use `#![forbid(unsafe_code)]`; unsafe Rust is not
admitted in the workspace.

If a future FFI or platform adapter cannot be built safely, it requires a
dedicated crate, explicit maintainer approval, a threat-model amendment, a
release milestone, a safety invariant for every block, Miri or sanitizer
coverage where applicable, differential tests against a safe reference, and a
focused pentest. Unsafe code can never coexist with parser policy, message
framing, compression validity, or protocol-state decisions.
