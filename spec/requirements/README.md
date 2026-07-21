# Requirement Ledger

Normative requirements are introduced in small reviewed batches by the release
plan. Each TOML record follows `spec/schema/requirement-example.toml`; records
must bind to the checksum-locked RFC bytes and cannot become `verified` unless
their named implementation symbols and tests exist and run in CI.
