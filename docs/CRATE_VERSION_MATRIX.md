# VEF Crate Version Matrix

Status: 0.1.0 foundation planning

VEF support crates use independent versioning after the foundation release.
The facade is the main user entry point; support crates are republished only
when their own code, API, documentation, or published dependency requirements
change. `release-crates.toml` is the machine-readable release set.

| Crate | Planned version | Change | Publish | Reason |
| --- | --- | --- | --- | --- |
| `vef-core` | `0.1.0` | foundation | Yes | Establish shared semantic and policy boundary |
| `vef-hpack` | `0.1.0` | foundation | Yes | Establish HPACK boundary |
| `vef-http1` | `0.1.0` | foundation | Yes | Establish HTTP/1-family boundary |
| `vef-http2` | `0.1.0` | foundation | Yes | Establish HTTP/2 boundary |
| `vef-io` | `0.1.0` | foundation | Yes | Establish runtime-neutral I/O boundary |
| `vef` | `0.1.0` | foundation | Yes | Establish feature-controlled facade |

Update this table and `release-crates.toml` together. A dependency-only
manifest change receives the smallest compatible patch bump; unchanged crates
are not republished.
