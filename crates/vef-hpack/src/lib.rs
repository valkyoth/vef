#![no_std]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

/// Returns the shared foundation version used by this codec crate.
#[must_use]
pub const fn foundation_version() -> &'static str {
    vef_core::FOUNDATION_VERSION
}

#[cfg(test)]
mod tests {
    #[test]
    fn uses_workspace_foundation() {
        assert_eq!(super::foundation_version(), "0.1.0");
    }
}
