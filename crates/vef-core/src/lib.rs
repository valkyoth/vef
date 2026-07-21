#![no_std]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

/// The initial workspace/API milestone represented by this crate.
pub const FOUNDATION_VERSION: &str = env!("CARGO_PKG_VERSION");

#[cfg(test)]
mod tests {
    use super::FOUNDATION_VERSION;

    #[test]
    fn foundation_version_matches_workspace_release() {
        assert_eq!(FOUNDATION_VERSION, "0.1.0");
    }
}
