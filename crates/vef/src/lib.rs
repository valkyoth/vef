#![no_std]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

/// Shared HTTP protocol types and policies.
pub use vef_core as core;

/// HTTP/1 family protocol support.
#[cfg(feature = "http1")]
pub use vef_http1 as http1;

/// HPACK support.
#[cfg(feature = "hpack")]
pub use vef_hpack as hpack;

/// HTTP/2 protocol support.
#[cfg(feature = "http2")]
pub use vef_http2 as http2;

/// Runtime-neutral byte-stream contracts.
#[cfg(feature = "io")]
pub use vef_io as io;
