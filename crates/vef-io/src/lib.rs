#![no_std]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

/// The result of a non-blocking byte operation.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum Progress {
    /// The operation made progress by this many bytes.
    Advanced(usize),
    /// The operation cannot currently make progress.
    Pending,
    /// The byte stream reached an orderly end.
    End,
}

#[cfg(test)]
mod tests {
    use super::Progress;

    #[test]
    fn progress_states_are_distinct() {
        assert_ne!(Progress::Advanced(0), Progress::Pending);
        assert_ne!(Progress::Pending, Progress::End);
    }
}
