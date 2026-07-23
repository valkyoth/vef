# VEF Release Plan to 1.0

Status: planning document

This is the authoritative implementation sequence. VEF processes hostile
traffic, so each milestone has one primary capability and a dependency-correct
acceptance boundary that can be implemented, reviewed, tested, pentested, and
stopped independently. Split work into patch releases when its security
argument no longer fits one review pass.

## Release principles

Every release requires applicable RFC/errata evidence, explicit applicability,
bounded resource behavior against the active profile, focused positive and
negative tests, relevant fragmentation/cancellation/capacity coverage,
documentation, release notes, portability, dependency-policy proof, SBOM,
full-SHA CI pins, CodeQL default-setup review, and exact-commit pentest. Tests
cover the new outcome and earlier behavior, never future features.

Protocol and I/O-contract crates remain `no_std`, safe Rust, and free of
third-party Rust crates. Tool-only fuzzers, model checkers, and interop peers do
not enter the production dependency graph.

## Rules binding every milestone

- Valid peer input exceeding policy, insufficient caller storage, temporary
  output backpressure, and exhausted mandatory-control capacity are distinct
  from peer protocol violations and receive role-specific dispositions.
- Success makes non-zero observable progress; borrowed events require
  acknowledgement before backing storage is recycled.
- Resource ceilings are defined in Phase 1 and enforced as each parser, HPACK
  operation, stream transition, scheduler action, and adapter lands.
- Parsing and semantic validation withhold application publication until the
  relevant barrier passes. Translation emits no destination bytes until its
  complete head/framing decision validates.
- HPACK encoder state follows HpackCommitted field blocks: encoding/table changes
  remain provisional through FramingCommitted and publish only after complete
  END_HEADERS-frame acknowledgement. Decoder compression state is never rolled
  back for a later semantic stream error.
- SETTINGS syntax/value storage is early, but state integration waits for the
  HPACK, stream, flow-control, admission, or scheduler component it mutates.
- Each HTTP/2 frame codec validates length, stream identifier, flags, reserved
  bits, padding arithmetic, optional-field minima, and exact RFC error scope.
- Stream-error deltas cannot mutate unrelated streams or connection state;
  connection-fatal decisions stop application publication and reserve exactly
  one bounded GOAWAY action.
- Every source file remains below 500 lines.
- Fuzz/model harnesses begin with hostile surfaces; final campaigns replay and
  expand them rather than creating them for the first time.

## Pentest flow

At each implementation stop, do not tag. Pentest the exact commit, remediate
with regression tests, repeat all gates, then add the permanent passing report
as the only file in the direct child of the reviewed commit. Critical/high
findings block release. Phase exits add manual review, stateful fuzzing, corpus
minimization, multi-peer interop, exhaustion assessment, and conformance review.

## Phase 1 — Foundation and shared semantics

Phase contract: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.

### v0.1.0 — Workspace, crate boundaries, licenses, security policy, and release evidence

Status: foundation implementation in progress

#### Goal

Deliver **Workspace, crate boundaries, licenses, security policy, and release evidence** as the sole primary capability in this stop. It builds
on the repository foundation and must be independently trustworthy before v0.2.0 (Core module skeleton and authority boundaries) begins.

#### Deliverables

- Acceptance contract: Require the committed workspace to contain only the declared path crates, dual MIT/Apache-2.0 licensing, security/release policies, pinned CI actions, deterministic release evidence, and no undeclared generated or third-party production input; package and policy checks must agree before publication.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Workspace, crate boundaries, licenses, security policy, and release evidence and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Workspace, crate boundaries, licenses, security policy, and release evidence contract and all previously implemented relevant behavior have
reproducible evidence; the repository foundation still passes; no behavior assigned to v0.2.0 (Core module skeleton and authority boundaries) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 — Core module skeleton and authority boundaries

Status: planned

#### Goal

Deliver **Core module skeleton and authority boundaries** as the sole primary capability in this stop. It builds
on v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) and must be independently trustworthy before v0.3.0 (Checked byte cursor with no unchecked indexing) begins.

#### Deliverables

- Acceptance contract: Assign every public type and module to one documented crate authority, keep the facade state-free, reject dependency cycles and platform/runtime types in protocol crates, and make every empty foundation module compile as no_std with unsafe forbidden.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Core module skeleton and authority boundaries and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Core module skeleton and authority boundaries contract and all previously implemented relevant behavior have
reproducible evidence; v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) still passes; no behavior assigned to v0.3.0 (Checked byte cursor with no unchecked indexing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 — Checked byte cursor with no unchecked indexing

Status: planned

#### Goal

Deliver **Checked byte cursor with no unchecked indexing** as the sole primary capability in this stop. It builds
on v0.2.0 (Core module skeleton and authority boundaries) and must be independently trustworthy before v0.4.0 (Non-zero parser progress and explicit blocked states) begins.

#### Deliverables

- Acceptance contract: Provide checked peek/read/advance/slice operations whose successful advances are nonzero, whose bounds arithmetic cannot wrap, and whose NeedInput result consumes nothing; prove equivalence against direct slicing for every offset/length pair without unchecked indexing.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Checked byte cursor with no unchecked indexing and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked byte cursor with no unchecked indexing contract and all previously implemented relevant behavior have
reproducible evidence; v0.2.0 (Core module skeleton and authority boundaries) still passes; no behavior assigned to v0.4.0 (Non-zero parser progress and explicit blocked states) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 — Non-zero parser progress and explicit blocked states

Status: planned

#### Goal

Deliver **Non-zero parser progress and explicit blocked states** as the sole primary capability in this stop. It builds
on v0.3.0 (Checked byte cursor with no unchecked indexing) and must be independently trustworthy before v0.5.0 (Checked protocol-size domains) begins.

#### Deliverables

- Acceptance contract: Represent successful byte advancement with a non-zero type or checked constructor and distinguish input, output, event, transition, NeedInput, NeedOutput, and CapacityExceeded outcomes.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Non-zero parser progress and explicit blocked states and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Non-zero parser progress and explicit blocked states contract and all previously implemented relevant behavior have
reproducible evidence; v0.3.0 (Checked byte cursor with no unchecked indexing) still passes; no behavior assigned to v0.5.0 (Checked protocol-size domains) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 — Checked protocol-size domains

Status: planned

#### Goal

Deliver **Checked protocol-size domains** as the sole primary capability in this stop. It builds
on v0.4.0 (Non-zero parser progress and explicit blocked states) and must be independently trustworthy before v0.6.0 (Decode, work, transition, and response budgets) begins.

#### Deliverables

- Acceptance contract: Use distinct checked newtypes for wire lengths, stream identifiers, window deltas, counts, and storage indices; reject out-of-domain conversion before mutation, preserve exact wire width, and prohibit unchecked target-usize narrowing on 32-bit systems.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Checked protocol-size domains and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked protocol-size domains contract and all previously implemented relevant behavior have
reproducible evidence; v0.4.0 (Non-zero parser progress and explicit blocked states) still passes; no behavior assigned to v0.6.0 (Decode, work, transition, and response budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 — Decode, work, transition, and response budgets

Status: planned

#### Goal

Deliver **Decode, work, transition, and response budgets** as the sole primary capability in this stop. It builds
on v0.5.0 (Checked protocol-size domains) and must be independently trustworthy before v0.7.0 (Initial deterministic resource profiles and measurement hooks) begins.

#### Deliverables

- Acceptance contract: Give decode bytes, work units, transitions, queued events, and generated response bytes independent saturating counters with explicit charge/refill points; exhaustion returns a typed policy/capacity action and cannot wrap, allocate, or masquerade as malformed peer input.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Decode, work, transition, and response budgets and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Decode, work, transition, and response budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.5.0 (Checked protocol-size domains) still passes; no behavior assigned to v0.7.0 (Initial deterministic resource profiles and measurement hooks) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 — Initial deterministic resource profiles and measurement hooks

Status: planned

#### Goal

Deliver **Initial deterministic resource profiles and measurement hooks** as the sole primary capability in this stop. It builds
on v0.6.0 (Decode, work, transition, and response budgets) and must be independently trustworthy before v0.8.0 (Caller-owned arenas and fixed-capacity stores) begins.

#### Deliverables

- Acceptance contract: Define numerical or target-relative stack, code-size, work-per-byte/frame, output-amplification, one-byte-fragmentation, lookup-complexity, and scheduler-fairness ceilings plus reproducible measurement hooks before parser layouts land.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Initial deterministic resource profiles and measurement hooks contract and all previously implemented relevant behavior have
reproducible evidence; v0.6.0 (Decode, work, transition, and response budgets) still passes; no behavior assigned to v0.8.0 (Caller-owned arenas and fixed-capacity stores) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 — Caller-owned arenas and fixed-capacity stores

Status: planned

#### Goal

Deliver **Caller-owned arenas and fixed-capacity stores** as the sole primary capability in this stop. It builds
on v0.7.0 (Initial deterministic resource profiles and measurement hooks) and must be independently trustworthy before v0.9.0 (Structured errors and error-scope taxonomy) begins.

#### Deliverables

- Acceptance contract: Define fixed stores, borrowed views, generation-safe recycling, explicit capacity failures, and no hidden growth before any complete protocol parser.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Caller-owned arenas and fixed-capacity stores and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Caller-owned arenas and fixed-capacity stores contract and all previously implemented relevant behavior have
reproducible evidence; v0.7.0 (Initial deterministic resource profiles and measurement hooks) still passes; no behavior assigned to v0.9.0 (Structured errors and error-scope taxonomy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 — Structured errors and error-scope taxonomy

Status: planned

#### Goal

Deliver **Structured errors and error-scope taxonomy** as the sole primary capability in this stop. It builds
on v0.8.0 (Caller-owned arenas and fixed-capacity stores) and must be independently trustworthy before v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) begins.

#### Deliverables

- Acceptance contract: Separate syntax, policy, capacity, transport, connection, stream, and application errors so adapters cannot mistake a fatal condition for a recoverable one.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Structured errors and error-scope taxonomy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured errors and error-scope taxonomy contract and all previously implemented relevant behavior have
reproducible evidence; v0.8.0 (Caller-owned arenas and fixed-capacity stores) still passes; no behavior assigned to v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 — Capacity exhaustion and protocol-violation disposition taxonomy

Status: planned

#### Goal

Deliver **Capacity exhaustion and protocol-violation disposition taxonomy** as the sole primary capability in this stop. It builds
on v0.9.0 (Structured errors and error-scope taxonomy) and must be independently trustworthy before v0.11.0 (Case-sensitive extension-capable Method) begins.

#### Deliverables

- Acceptance contract: Distinguish invalid input, valid policy excess, insufficient caller storage, temporary output backpressure, and exhausted mandatory-control capacity; map each role to explicit local error, reject, close, or retry behavior without converting local capacity into peer PROTOCOL_ERROR.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Capacity exhaustion and protocol-violation disposition taxonomy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Capacity exhaustion and protocol-violation disposition taxonomy contract and all previously implemented relevant behavior have
reproducible evidence; v0.9.0 (Structured errors and error-scope taxonomy) still passes; no behavior assigned to v0.11.0 (Case-sensitive extension-capable Method) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 — Case-sensitive extension-capable Method

Status: planned

#### Goal

Deliver **Case-sensitive extension-capable Method** as the sole primary capability in this stop. It builds
on v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) and must be independently trustworthy before v0.12.0 (Validated StatusCode with unknown-code preservation) begins.

#### Deliverables

- Acceptance contract: Represent standard and extension methods as case-sensitive validated bytes, preserve unknown tokens exactly, compare and hash by exact octets, reject separators/control/non-ASCII bytes, and serialize without normalization or allocation.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Case-sensitive extension-capable Method and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-sensitive extension-capable Method contract and all previously implemented relevant behavior have
reproducible evidence; v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) still passes; no behavior assigned to v0.12.0 (Validated StatusCode with unknown-code preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 — Validated StatusCode with unknown-code preservation

Status: planned

#### Goal

Deliver **Validated StatusCode with unknown-code preservation** as the sole primary capability in this stop. It builds
on v0.11.0 (Case-sensitive extension-capable Method) and must be independently trustworthy before v0.13.0 (HTTP version and wire-version representation) begins.

#### Deliverables

- Acceptance contract: Construct StatusCode only from exactly three decimal digits in 100..=599, preserve unregistered values such as 471 as valid extension codes, compare by numeric code, and serialize exactly three ASCII digits; retain a received 600..=999 wire value only in a typed InvalidStatusCode result carrying its raw digits so client policy can process the response as 5xx, while server builders and every serializer reject that value and can never emit it as a valid HTTP status.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Validated StatusCode with unknown-code preservation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Validated StatusCode with unknown-code preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.11.0 (Case-sensitive extension-capable Method) still passes; no behavior assigned to v0.13.0 (HTTP version and wire-version representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 — HTTP version and wire-version representation

Status: planned

#### Goal

Deliver **HTTP version and wire-version representation** as the sole primary capability in this stop. It builds
on v0.12.0 (Validated StatusCode with unknown-code preservation) and must be independently trustworthy before v0.14.0 (Case-insensitive validated FieldName) begins.

#### Deliverables

- Acceptance contract: Distinguish semantic HTTP versions from exact wire tokens, preserve supported HTTP/0.9, 1.0, 1.1, and 2 selection without guessed fallback, reject malformed tokens, and serialize only role/protocol-legal wire versions.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HTTP version and wire-version representation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP version and wire-version representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.12.0 (Validated StatusCode with unknown-code preservation) still passes; no behavior assigned to v0.14.0 (Case-insensitive validated FieldName) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 — Case-insensitive validated FieldName

Status: planned

#### Goal

Deliver **Case-insensitive validated FieldName** as the sole primary capability in this stop. It builds
on v0.13.0 (HTTP version and wire-version representation) and must be independently trustworthy before v0.15.0 (Byte-oriented FieldValue with raw and semantic views) begins.

#### Deliverables

- Acceptance contract: Validate nonempty HTTP field-name bytes against the token grammar, preserve original spelling for serialization, provide allocation-free ASCII-case-insensitive equality/hash, and reject uppercase only in HTTP/2-specific validation rather than the shared type.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Case-insensitive validated FieldName and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-insensitive validated FieldName contract and all previously implemented relevant behavior have
reproducible evidence; v0.13.0 (HTTP version and wire-version representation) still passes; no behavior assigned to v0.15.0 (Byte-oriented FieldValue with raw and semantic views) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 — Byte-oriented FieldValue with raw and semantic views

Status: planned

#### Goal

Deliver **Byte-oriented FieldValue with raw and semantic views** as the sole primary capability in this stop. It builds
on v0.14.0 (Case-insensitive validated FieldName) and must be independently trustworthy before v0.16.0 (Ordered FieldLine and FieldSection storage) begins.

#### Deliverables

- Acceptance contract: Preserve field values as bytes plus validated semantic views, reject NUL/CR/LF and forbidden controls at the owning protocol boundary, never assume UTF-8, and keep raw order/octets stable across equality-independent parsing and serialization.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Byte-oriented FieldValue with raw and semantic views and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Byte-oriented FieldValue with raw and semantic views contract and all previously implemented relevant behavior have
reproducible evidence; v0.14.0 (Case-insensitive validated FieldName) still passes; no behavior assigned to v0.16.0 (Ordered FieldLine and FieldSection storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 — Ordered FieldLine and FieldSection storage

Status: planned

#### Goal

Deliver **Ordered FieldLine and FieldSection storage** as the sole primary capability in this stop. It builds
on v0.15.0 (Byte-oriented FieldValue with raw and semantic views) and must be independently trustworthy before v0.17.0 (Request-target, URI, and authority types) begins.

#### Deliverables

- Acceptance contract: Store field lines in insertion order with duplicates intact, expose index and case-insensitive-name lookup without implicit combination, fail atomically on caller capacity, and keep borrowed values generation-valid until acknowledgement.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Ordered FieldLine and FieldSection storage and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Ordered FieldLine and FieldSection storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.15.0 (Byte-oriented FieldValue with raw and semantic views) still passes; no behavior assigned to v0.17.0 (Request-target, URI, and authority types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.16.0 implementation stop reached. Run pentest for this exact commit.`

### v0.17.0 — Request-target, URI, and authority types

Status: planned

#### Goal

Deliver **Request-target, URI, and authority types** as the sole primary capability in this stop. It builds
on v0.16.0 (Ordered FieldLine and FieldSection storage) and must be independently trustworthy before v0.18.0 (Request and response control-data types) begins.

#### Deliverables

- Acceptance contract: Represent origin, absolute, authority, and asterisk request targets separately; parse scheme, authority, raw path, and optional raw query into distinct checked spans, split on only the first question mark, preserve `/resource` versus `/resource?`, reject fragments, and preserve every percent-encoded octet byte-for-byte; any decoded or normalized view is separate and can never replace routing, forwarding, cache-key, or signature identity; accept well-formed bracketed IPv6/IPvFuture, accept and preserve a grammar-valid empty port while resolving its scheme default only in a separate semantic view, reject userinfo for HTTP authority use, and reject malformed/mismatched brackets; preserve raw URI/authority octets and serialize only method/role-coherent forms.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test empty/absent query distinction, first-question-mark splitting, percent-encoded identity, fragment rejection, empty path, bracketed IPv6 and IPvFuture, empty port, userinfo rejection, malformed brackets, and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request-target, URI, and authority types contract and all previously implemented relevant behavior have
reproducible evidence; v0.16.0 (Ordered FieldLine and FieldSection storage) still passes; no behavior assigned to v0.18.0 (Request and response control-data types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 — Request and response control-data types

Status: planned

#### Goal

Deliver **Request and response control-data types** as the sole primary capability in this stop. It builds
on v0.17.0 (Request-target, URI, and authority types) and must be independently trustworthy before v0.19.0 (Role, profile, and policy types) begins.

#### Deliverables

- Acceptance contract: Represent request and response control data with ordered fields, explicit method/target or status/version context, borrowed ownership, and a single validated framing slot; construction and publication fail atomically on invalid components or capacity.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Request and response control-data types and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request and response control-data types contract and all previously implemented relevant behavior have
reproducible evidence; v0.17.0 (Request-target, URI, and authority types) still passes; no behavior assigned to v0.19.0 (Role, profile, and policy types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 — Role, profile, and policy types

Status: planned

#### Goal

Deliver **Role, profile, and policy types** as the sole primary capability in this stop. It builds
on v0.18.0 (Request and response control-data types) and must be independently trustworthy before v0.20.0 (Minimal synchronous I/O contracts) begins.

#### Deliverables

- Acceptance contract: Use exhaustive client, origin, intermediary, proxy, gateway, and tunnel roles plus named strict/compatibility profiles; define generation- and connection-bound TrustedRequestContext with optional fixed-listener scheme, authenticated trusted-gateway scheme, and adapter-supplied authenticated transport-security state; apply explicit precedence fixed-listener then trusted-gateway then transport-derived http/https, reject disagreement by default unless an immutable named policy authorizes the higher-priority source, reject stale/cross-connection context, and never infer security from socket or runtime types; define caller-supplied ConnectTargetPolicy with generation-bound ConnectAttemptToken and AuthorizedConnectOutcome types that bind requested authority, resolved endpoint, connected peer, attempt/request/policy generations, and no socket/resolver ownership; seal their fields/constructors, make them neither Copy nor Clone, issue an engine-owned opaque attempt identity independent of caller endpoint values, and permit an outcome to be consumed once by only its matching request state; define a distinct sensitive HopScopedProxyCredential bound to an engine-issued exchange identity as well as inbound hop, next-hop policy, connection, and generation so equal generations cannot rebind it to another exchange; make every policy choice immutable for a message, reject unsupported combinations, and never infer role from input bytes.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every TrustedRequestContext source/absence/precedence/conflict, TLS-termination override policy, stale generation and cross-connection reuse, socket-type noninference, sealed/non-Copy/non-Clone capability construction, opaque identity independence, ConnectTargetPolicy lexical/resolved/peer generations, duplicate/cross-attempt/same-generation outcome rejection, HopScopedProxyCredential hop/generation/exchange separation from Authorization, every role/profile combination, and all previously implemented relevant behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role, profile, and policy types contract and all previously implemented relevant behavior have
reproducible evidence; v0.18.0 (Request and response control-data types) still passes; no behavior assigned to v0.20.0 (Minimal synchronous I/O contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 — Minimal synchronous I/O contracts

Status: planned

#### Goal

Deliver **Minimal synchronous I/O contracts** as the sole primary capability in this stop. It builds
on v0.19.0 (Role, profile, and policy types) and must be independently trustworthy before v0.21.0 (Runtime-neutral readiness and poll contracts) begins.

#### Deliverables

- Acceptance contract: Define short reads/writes, zero-length calls, clean versus truncated EOF, temporary starvation, scalar fallback, alignment requirements, non-reentrancy, and optional vectored/scatter-gather progress without owning sockets. One engine offer and acknowledgement covers exactly one immutable protocol-record suffix; an adapter may map that suffix to scalar or vectored OS buffers but cannot combine multiple records under one acknowledgement.
- Treat bytes offered by a Sans-I/O engine separately from bytes the caller acknowledges as written. A zero-length or short write advances only the acknowledged prefix; it never permits regeneration of already exposed output from changed protocol state. Exact lease/token rules and the irrevocable exposure boundary are fixed at v0.25.0.
- Define the content-independent per-connection driver invariant: while an
  `OutputToken` is outstanding, nonempty input is accepted only by a combined
  call that consumes that exact token before parsing. Valid zero, short, and
  full acknowledgements resolve the offer and establish the state in which
  input is parsed; invalid acknowledgement and input-only delivery leave all
  input unconsumed, with the latter returning typed local
  `DriverCommitOrderViolation`. No dependency classifier exists, peer input
  never proves output commitment, and vectored/DMA queuing is not transport
  consumption. Apply the rule to HTTP/1 response correlation and transition
  heads, SETTINGS/PING ACKs, locally initiated HTTP/2 responses, advertised
  extensions/features, GOAWAY, and every later output/input boundary.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Minimal synchronous I/O contracts and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross input-only and combined calls with invalid/stale/oversized and valid zero/short/full output acknowledgement, subsequent parse failure, scalar/vectored/DMA delivery, and every call order; prove acknowledgement-first ordering, state-neutral invalid acknowledgement, preserved committed prefixes, zero input consumption/mutation on `DriverCommitOrderViolation`, and no peer-input-derived or caller-queue-derived output commitment.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Minimal synchronous I/O contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.19.0 (Role, profile, and policy types) still passes; no behavior assigned to v0.21.0 (Runtime-neutral readiness and poll contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.20.0 implementation stop reached. Run pentest for this exact commit.`

### v0.21.0 — Runtime-neutral readiness and poll contracts

Status: planned

#### Goal

Deliver **Runtime-neutral readiness and poll contracts** as the sole primary capability in this stop. It builds
on v0.20.0 (Minimal synchronous I/O contracts) and must be independently trustworthy before v0.22.0 (Injected monotonic clock and deadline contracts) begins.

#### Deliverables

- Acceptance contract: Define WouldBlock, spurious readiness, edge/level triggering, wake coalescing, interest changes, cancellation races, and the requirement that readiness never implies byte progress.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Runtime-neutral readiness and poll contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.20.0 (Minimal synchronous I/O contracts) still passes; no behavior assigned to v0.22.0 (Injected monotonic clock and deadline contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 — Injected monotonic clock and deadline contracts

Status: planned

#### Goal

Deliver **Injected monotonic clock and deadline contracts** as the sole primary capability in this stop. It builds
on v0.21.0 (Runtime-neutral readiness and poll contracts) and must be independently trustworthy before v0.23.0 (Cancellation, close, and bounded-backpressure contracts) begins.

#### Deliverables

- Acceptance contract: Use caller-supplied monotonic instants with checked deadline arithmetic, wrap handling, expiration ordering, no wall-clock assumptions, and deterministic timeout tests.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injected monotonic clock and deadline contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.21.0 (Runtime-neutral readiness and poll contracts) still passes; no behavior assigned to v0.23.0 (Cancellation, close, and bounded-backpressure contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 — Cancellation, close, and bounded-backpressure contracts

Status: planned

#### Goal

Deliver **Cancellation, close, and bounded-backpressure contracts** as the sole primary capability in this stop. It builds
on v0.22.0 (Injected monotonic clock and deadline contracts) and must be independently trustworthy before v0.24.0 (Deterministic fake transport and driver harness) begins.

#### Deliverables

- Acceptance contract: The Cancellation, close, and bounded-backpressure contracts outcome must name its representation and ownership invariants, valid and invalid construction paths, publication/commit point, typed policy/capacity failures, bounded work/storage, portability evidence, and deterministic tests; no later milestone may be required to make this foundation safe.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cancellation, close, and bounded-backpressure contracts and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cancellation, close, and bounded-backpressure contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.22.0 (Injected monotonic clock and deadline contracts) still passes; no behavior assigned to v0.24.0 (Deterministic fake transport and driver harness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 — Deterministic fake transport and driver harness

Status: planned

#### Goal

Deliver **Deterministic fake transport and driver harness** as the sole primary capability in this stop. It builds
on v0.23.0 (Cancellation, close, and bounded-backpressure contracts) and must be independently trustworthy before v0.25.0 (Engine event, command, acknowledgement, and publication contract) begins.

#### Deliverables

- Acceptance contract: The Deterministic fake transport and driver harness outcome must name its representation and ownership invariants, valid and invalid construction paths, publication/commit point, typed policy/capacity failures, bounded work/storage, portability evidence, and deterministic tests; no later milestone may be required to make this foundation safe.
- Model output exposure and transport acknowledgement independently. Interleave zero/short/full writes, stale/duplicate/out-of-order tokens, cancellation, connection failure, and caller-buffer reuse; retain the exact offered bytes until the acknowledgement/revocation contract resolves them.
- Model ordering independently from peer-byte contents. Permute offered bytes,
  invalid/zero/short/full acknowledged prefixes, adapter reads, input-only and
  combined delivery, parse failure, connection failure, retry, and scalar,
  vectored, or DMA transport progress. Any nonempty input-only delivery with an
  outstanding token produces only `DriverCommitOrderViolation`; a combined
  call consumes the exact token first and never acknowledges bytes merely
  queued in caller-controlled memory.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Deterministic fake transport and driver harness and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Include deterministic HTTP/1 response/FIFO and transition-head traces plus SETTINGS/PING ACK, locally initiated response HEADERS, advertised-extension frame, and GOAWAY input at every output prefix and call order. Make all expected outcomes independent of input classification.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic fake transport and driver harness contract and all previously implemented relevant behavior have
reproducible evidence; v0.23.0 (Cancellation, close, and bounded-backpressure contracts) still passes; no behavior assigned to v0.25.0 (Engine event, command, acknowledgement, and publication contract) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.24.0 implementation stop reached. Run pentest for this exact commit.`

### v0.25.0 — Engine event, command, acknowledgement, and publication contract

Status: planned

#### Goal

Deliver **Engine event, command, acknowledgement, and publication contract** as the sole primary capability in this stop. It builds
on v0.24.0 (Deterministic fake transport and driver harness) and must be independently trustworthy before v0.26.0 (Requirement, applicability, and errata evidence system) begins.

#### Deliverables

- Acceptance contract: Choose one generation-bound outstanding-event/output-lease model; define acknowledgements, command acceptance, reentrancy prohibition, input/output ownership, cancellation aftermath, publication barriers, and capacity reserved for mandatory responses. Returning a non-empty output slice is the irrevocable byte-exposure boundary: VEF must first freeze the exact bytes and their semantic identity in private bounded storage. Private encoding before exposure remains replaceable; later transport acknowledgement controls only prefix progress/reclamation and never permits mutation of exposed bytes. A zero-capacity poll returns NeedOutput and creates no lease/exposure.
- Each non-empty offer returns a sealed `OutputToken { generation, record, start, offered_end }` bound to exactly one outstanding immutable protocol-record suffix. Acknowledgement consumes that token exactly once and reports a delta in `0..=offered_end-start`; it cannot cross into a later record, batch completion hooks, or release another slot. Zero is a valid no-progress write that leaves the cursor unchanged but invalidates that offer token. Duplicate, oversized—including an acknowledgement extending beyond this record—stale-generation, cross-record/output, or out-of-order acknowledgement returns `InvalidState` without cursor/state mutation. The caller certifies that the unacknowledged suffix from a consumed lease will not later be written; VEF may re-offer it under a fresh token from the unchanged frozen record.
- While a token is outstanding, prohibit reentrant offers, mutation/replacement of its frozen record, caller-buffer reuse through the safe borrow, and owning stream/record reclamation. Connection failure consumes or invalidates the token through connection-owned cleanup and records only the acknowledged prefix. Require every later semantic-validation layer to preserve independent engine-only validation slots and head storage that application response work cannot consume, with one deterministic close/shutdown action and zero partial response output if even the reserve cannot proceed.
- Expose a combined causal operation conceptually equivalent to
  `advance_io(output_ack, input)` and process its optional output token/delta
  completely before parsing one input byte. While any `OutputToken` is
  outstanding, accept nonempty input only through this combined call consuming
  that exact token; make no peer-controlled content inspection and accept no
  caller-provided dependent/independent flag or trait. Invalid, stale,
  cross-record, or oversized acknowledgement is state-neutral and leaves input
  wholly unconsumed. A valid zero acknowledgement invalidates the offer without
  advancing output, then parses against unchanged protocol state; a short
  acknowledgement commits only its prefix, and a full acknowledgement runs
  infallible completion hooks, before parsing. Subsequent input failure never
  rolls back already acknowledged output. Input-only nonempty delivery with a
  live token returns `DriverCommitOrderViolation` before parsing, with token,
  cursor, input, and protocol state unchanged. Scalar, vectored, and DMA
  adapters obey the same rule and may acknowledge only bytes consumed by the
  transport, never bytes merely queued in caller-controlled memory. Never
  accept peer input as implicit acknowledgement.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Engine event, command, acknowledgement, and publication contract and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cover private encoding before exposure, first non-empty exposure, zero-length and every short acknowledgement, exact one-record completion, attempted acknowledgement across a record boundary, stale/duplicate/oversized/cross-record/out-of-order tokens, failure with an outstanding lease, caller-buffer reuse attempts, and generation rollover; prove only acknowledged prefixes count as written, every exposed byte remains immutable, and no token completes or releases another record. Cross output-only/input-only/combined calls at every prefix and call order with empty/nonempty input: invalid acknowledgement leaves all input unconsumed, zero parses against unchanged state, short parses against prefix-committed state, full runs hooks before parsing, parse failure preserves commitment, and input-only with a live token is wholly state-neutral local failure. Prove no input classifier or vectored/DMA queue can bypass transport-consumption evidence.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Engine event, command, acknowledgement, and publication contract contract and all previously implemented relevant behavior have
reproducible evidence; v0.24.0 (Deterministic fake transport and driver harness) still passes; no behavior assigned to v0.26.0 (Requirement, applicability, and errata evidence system) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.25.0 implementation stop reached. Run pentest for this exact commit.`

### v0.26.0 — Requirement, applicability, and errata evidence system

Status: planned

#### Goal

Deliver **Requirement, applicability, and errata evidence system** as the sole primary capability in this stop. It builds
on v0.25.0 (Engine event, command, acknowledgement, and publication contract) and must be independently trustworthy before v0.27.0 (Foundation Kani campaign, audit, and pentest) begins.

#### Deliverables

- Acceptance contract: The Requirement, applicability, and errata evidence system outcome must name its representation and ownership invariants, valid and invalid construction paths, publication/commit point, typed policy/capacity failures, bounded work/storage, portability evidence, and deterministic tests; no later milestone may be required to make this foundation safe.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Requirement, applicability, and errata evidence system and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Requirement, applicability, and errata evidence system contract and all previously implemented relevant behavior have
reproducible evidence; v0.25.0 (Engine event, command, acknowledgement, and publication contract) still passes; no behavior assigned to v0.27.0 (Foundation Kani campaign, audit, and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 — Foundation Kani campaign, audit, and pentest

Status: planned

#### Goal

Deliver **Foundation Kani campaign, audit, and pentest** as the sole primary capability in this stop. It builds
on v0.26.0 (Requirement, applicability, and errata evidence system) and must be independently trustworthy before v0.28.0 (HTTP/1 role and parser profiles) begins.

#### Deliverables

- Acceptance contract: The Foundation Kani campaign, audit, and pentest outcome must name its representation and ownership invariants, valid and invalid construction paths, publication/commit point, typed policy/capacity failures, bounded work/storage, portability evidence, and deterministic tests; no later milestone may be required to make this foundation safe.
- Model-check the v0.25.0 output lease/token state machine: no frozen byte changes after exposure, acknowledgements advance one exact prefix at most once, zero writes preserve the cursor, invalid tokens are state-neutral, and record/generation reuse is impossible with an outstanding lease or acknowledged-prefix obligation.
- Model-check the content-independent driver order over offered token,
  invalid/zero/short/full acknowledgement, empty/nonempty input, parse result,
  and call-order permutations. Combined calls consume the exact token and
  commit first, subsequent parse failure preserves the committed prefix,
  input-only calls with a live token preserve every byte/state/token, and
  neither peer content, a dependency flag, nor caller-controlled vectored/DMA
  queuing can select an output-completion transition.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Foundation Kani campaign, audit, and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Foundation Kani campaign, audit, and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.26.0 (Requirement, applicability, and errata evidence system) still passes; no behavior assigned to v0.28.0 (HTTP/1 role and parser profiles) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.27.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 2 — HTTP/1 and isolated HTTP/0.9

Phase contract: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.

### v0.28.0 — HTTP/1 role and parser profiles

Status: planned

#### Goal

Deliver **HTTP/1 role and parser profiles** as the sole primary capability in this stop. It builds
on v0.27.0 (Foundation Kani campaign, audit, and pentest) and must be independently trustworthy before v0.29.0 (Incremental HTTP/1 request-line parser) begins.

#### Deliverables

- Acceptance contract: Fix ClientResponse, OriginServerRequest, and IntermediaryRequest/Response profiles: each accepts only its role's start-line, applies immutable per-message line/field/section/work ceilings, returns NeedInput only without consumption, and maps peer syntax, local capacity, and required close actions to distinct typed outcomes before head publication.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 role and parser profiles contract and all previously implemented relevant behavior have
reproducible evidence; v0.27.0 (Foundation Kani campaign, audit, and pentest) still passes; no behavior assigned to v0.29.0 (Incremental HTTP/1 request-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 — Incremental HTTP/1 request-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 request-line parser** as the sole primary capability in this stop. It builds
on v0.28.0 (HTTP/1 role and parser profiles) and must be independently trustworthy before v0.30.0 (Incremental HTTP/1 status-line parser) begins.

#### Deliverables

- Acceptance contract: Accept method SP request-target SP HTTP-version CRLF with exactly one SP at each separator; reject HTAB, empty components, extra separators, controls, bare CR/LF, and component-limit overflow; retain checked component spans across splits and publish a request line only after the terminating CRLF commits.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 request-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.28.0 (HTTP/1 role and parser profiles) still passes; no behavior assigned to v0.30.0 (Incremental HTTP/1 status-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 — Incremental HTTP/1 status-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 status-line parser** as the sole primary capability in this stop. It builds
on v0.29.0 (Incremental HTTP/1 request-line parser) and must be independently trustworthy before v0.31.0 (Every-byte fragmentation support) begins.

#### Deliverables

- Acceptance contract: Accept HTTP-version SP three-digit status-code SP optional reason-phrase CRLF; permit only HTAB, SP, VCHAR, and obs-text in the reason phrase, reject controls, malformed spacing, invalid status syntax, bare CR/LF, and configured line overflow, and publish no status line before its final CRLF.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 status-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.29.0 (Incremental HTTP/1 request-line parser) still passes; no behavior assigned to v0.31.0 (Every-byte fragmentation support) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 — Every-byte fragmentation support

Status: planned

#### Goal

Deliver **Every-byte fragmentation support** as the sole primary capability in this stop. It builds
on v0.30.0 (Incremental HTTP/1 status-line parser) and must be independently trustworthy before v0.32.0 (Strict CRLF and separately named LF compatibility) begins.

#### Deliverables

- Acceptance contract: For every request/status/field line and every byte boundary, parsing the same octets in one slice or all possible fragmentations produces the same value, consumed count, error offset, and close action; empty or incomplete input returns NeedInput without mutation, and each successful nonterminal call consumes bytes or records a distinct state transition.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Every-byte fragmentation support and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Every-byte fragmentation support contract and all previously implemented relevant behavior have
reproducible evidence; v0.30.0 (Incremental HTTP/1 status-line parser) still passes; no behavior assigned to v0.32.0 (Strict CRLF and separately named LF compatibility) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 — Strict CRLF and separately named LF compatibility

Status: planned

#### Goal

Deliver **Strict CRLF and separately named LF compatibility** as the sole primary capability in this stop. It builds
on v0.31.0 (Every-byte fragmentation support) and must be independently trustworthy before v0.33.0 (Incremental HTTP/1 field-line parser) begins.

#### Deliverables

- Acceptance contract: In the default strict profile accept only CRLF line termination, reject bare CR, bare LF, and premature EOF before head publication with the role-specific close action; a separately named opt-in LF profile may accept one LF terminator but never enables obs-fold or automatic fallback, and the selected profile is immutable for the connection.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Strict CRLF and separately named LF compatibility and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Strict CRLF and separately named LF compatibility contract and all previously implemented relevant behavior have
reproducible evidence; v0.31.0 (Every-byte fragmentation support) still passes; no behavior assigned to v0.33.0 (Incremental HTTP/1 field-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.32.0 implementation stop reached. Run pentest for this exact commit.`

### v0.33.0 — Incremental HTTP/1 field-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 field-line parser** as the sole primary capability in this stop. It builds
on v0.32.0 (Strict CRLF and separately named LF compatibility) and must be independently trustworthy before v0.34.0 (Explicit OWS handling with raw-value preservation) begins.

#### Deliverables

- Acceptance contract: Parse field-name colon OWS field-value OWS CRLF incrementally, reject empty/invalid names, whitespace before the colon, NUL and forbidden controls, bare CR/LF, and undeclared continuation lines; preserve ordered raw bytes plus validated semantic spans and publish a field only after CRLF and capacity checks succeed.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 field-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.32.0 (Strict CRLF and separately named LF compatibility) still passes; no behavior assigned to v0.34.0 (Explicit OWS handling with raw-value preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 — Explicit OWS handling with raw-value preservation

Status: planned

#### Goal

Deliver **Explicit OWS handling with raw-value preservation** as the sole primary capability in this stop. It builds
on v0.33.0 (Incremental HTTP/1 field-line parser) and must be independently trustworthy before v0.35.0 (Injection-proof HTTP/1 head serialization) begins.

#### Deliverables

- Acceptance contract: Keep the exact raw field-value octets and a semantic view that removes only leading/trailing SP or HTAB; preserve interior whitespace and obs-text byte-for-byte, never normalize quoted or comma syntax here, and reject NUL/CR/LF before either view becomes observable.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit OWS handling with raw-value preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.33.0 (Incremental HTTP/1 field-line parser) still passes; no behavior assigned to v0.35.0 (Injection-proof HTTP/1 head serialization) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 — Injection-proof HTTP/1 head serialization

Status: planned

#### Goal

Deliver **Injection-proof HTTP/1 head serialization** as the sole primary capability in this stop. It builds
on v0.34.0 (Explicit OWS handling with raw-value preservation) and must be independently trustworthy before v0.36.0 (Role-specific obs-fold and invalid-field disposition) begins.

#### Deliverables

- Acceptance contract: Serialize only validated method, target, version, status, reason, field-name, and field-value types; emit canonical SP and CRLF delimiters, reject any component containing CR, LF, NUL, invalid field-name bytes, or a length above the output profile before writing, and resume partial output without duplicating committed bytes.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injection-proof HTTP/1 head serialization contract and all previously implemented relevant behavior have
reproducible evidence; v0.34.0 (Explicit OWS handling with raw-value preservation) still passes; no behavior assigned to v0.36.0 (Role-specific obs-fold and invalid-field disposition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 — Role-specific obs-fold and invalid-field disposition

Status: planned

#### Goal

Deliver **Role-specific obs-fold and invalid-field disposition** as the sole primary capability in this stop. It builds
on v0.35.0 (Injection-proof HTTP/1 head serialization) and must be independently trustworthy before v0.37.0 (Field count, line, and section caps) begins.

#### Deliverables

- Acceptance contract: Implement the RFC 9112 role matrix for server requests, proxy/gateway responses, and user-agent responses rather than one blanket rejection rule.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role-specific obs-fold and invalid-field disposition contract and all previously implemented relevant behavior have
reproducible evidence; v0.35.0 (Injection-proof HTTP/1 head serialization) still passes; no behavior assigned to v0.37.0 (Field count, line, and section caps) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.36.0 implementation stop reached. Run pentest for this exact commit.`

### v0.37.0 — Field count, line, and section caps

Status: planned

#### Goal

Deliver **Field count, line, and section caps** as the sole primary capability in this stop. It builds
on v0.36.0 (Role-specific obs-fold and invalid-field disposition) and must be independently trustworthy before v0.38.0 (Typed HTTP/1 protocol-error response and close actions) begins.

#### Deliverables

- Acceptance contract: Enforce independent saturating maxima for start-line bytes, field-line bytes, field count, total section bytes, and parse work; charge before scan/copy/publication, return typed peer-limit or caller-capacity outcomes without partial field insertion, and require the role policy to select a bounded error response and mandatory close where applicable.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Field count, line, and section caps and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Field count, line, and section caps contract and all previously implemented relevant behavior have
reproducible evidence; v0.36.0 (Role-specific obs-fold and invalid-field disposition) still passes; no behavior assigned to v0.38.0 (Typed HTTP/1 protocol-error response and close actions) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 — Typed HTTP/1 protocol-error response and close actions

Status: planned

#### Goal

Deliver **Typed HTTP/1 protocol-error response and close actions** as the sole primary capability in this stop. It builds
on v0.37.0 (Field count, line, and section caps) and must be independently trustworthy before v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) begins.

#### Deliverables

- Acceptance contract: Map failures to mandatory typed actions such as RejectAndClose(400/414/431), BadGatewayAndCloseUpstream, DiscardResponseAndClose, ConnectionError, or StreamError without unsafe continuation; define minimal bounded response templates and required semantic inputs so v0.182.1 can validate them from the engine-only reserve even when ordinary application response capacity is exhausted, otherwise commit one deterministic close/shutdown action with no partial response bytes.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Typed HTTP/1 protocol-error response and close actions contract and all previously implemented relevant behavior have
reproducible evidence; v0.37.0 (Field count, line, and section caps) still passes; no behavior assigned to v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 — HTTP/1.1 Host validation and duplicate rejection

Status: planned

#### Goal

Deliver **HTTP/1.1 Host validation and duplicate rejection** as the sole primary capability in this stop. It builds
on v0.38.0 (Typed HTTP/1 protocol-error response and close actions) and must be independently trustworthy before v0.40.0 (Method and request-target-form coherence) begins.

#### Deliverables

- Acceptance contract: For every HTTP/1.1 request require exactly one syntactically valid Host field, including the grammar-valid empty value required when the target URI has no authority; reject missing, comma-combined, duplicate even when values match, and otherwise malformed Host; publish only a typed non-routable Host/parser artifact that role and application request APIs cannot consume until v0.40.0 authority validation succeeds; HTTP/1.0 retains Host as an ordinary optional field under its separate profile; named vectors cover missing, duplicate, combined, malformed, and empty Host with targets both with and without authority.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 Host validation and duplicate rejection contract and all previously implemented relevant behavior have
reproducible evidence; v0.38.0 (Typed HTTP/1 protocol-error response and close actions) still passes; no behavior assigned to v0.40.0 (Method and request-target-form coherence) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 — Method and request-target-form coherence

Status: planned

#### Goal

Deliver **Method and request-target-form coherence** as the sole primary capability in this stop. It builds
on v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) and must be independently trustworthy before v0.41.0 (Checked Content-Length grammar) begins.

#### Deliverables

- Acceptance contract: Let the generic parser recognize all four target forms, then authorize them by role before any routable or application-visible request event: origin servers accept origin-form and absolute-form; explicit forward proxies require absolute-form for ordinary proxy requests; reverse/interception proxies accept origin-form only with explicit connection/listener destination context and never infer a forward-proxy destination from origin-form plus Host; require asterisk-form only for server-wide OPTIONS; for CONNECT construct a distinct ConnectAuthority from authority-form with bracket-aware host plus an explicit nonempty decimal port in 1..=65535, rejecting zero, overflow, truncation, empty/invalid port, scheme-default substitution, and Host-based routing; derive a complete EffectiveTarget of trusted scheme, effective authority or ConnectAuthority, raw path, and optional raw query from the generation-matched TrustedRequestContext, authorized target, Host, and explicit context, applying configured reject-or-explicit-default empty-authority policy; for absolute-form use only target authority, ignore Host, and regenerate forwarding Host; reject stale context, scheme-source conflict, fragments, empty targets, unauthorized forms, ambiguity, and method/form mismatch before routing/application publication.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test trusted scheme sources/precedence/conflicts and context generations; bracketed IPv6 CONNECT with explicit port; empty, zero, nondecimal, overflow, >65535, and default-substitution ports; CONNECT Host mismatch proving authority-form wins; origin/absolute-form role policy, explicit reverse context, empty-authority reject/default, regenerated Host, every unauthorized form/method mismatch, and zero application events before EffectiveTarget success.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Method and request-target-form coherence contract and all previously implemented relevant behavior have
reproducible evidence; v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) still passes; no behavior assigned to v0.41.0 (Checked Content-Length grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 — Checked Content-Length grammar

Status: planned

#### Goal

Deliver **Checked Content-Length grammar** as the sole primary capability in this stop. It builds
on v0.40.0 (Method and request-target-form coherence) and must be independently trustworthy before v0.42.0 (Repeated and comma-list Content-Length resolution) begins.

#### Deliverables

- Acceptance contract: Accept Content-Length only as one or more ASCII digits with optional surrounding field OWS handled by field parsing, allow leading zeroes, reject sign, empty value, embedded whitespace, non-digit, and checked decimal overflow, and publish the numeric length only after the complete field value validates with role-specific reject/close disposition.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked Content-Length grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.40.0 (Method and request-target-form coherence) still passes; no behavior assigned to v0.42.0 (Repeated and comma-list Content-Length resolution) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 — Repeated and comma-list Content-Length resolution

Status: planned

#### Goal

Deliver **Repeated and comma-list Content-Length resolution** as the sole primary capability in this stop. It builds
on v0.41.0 (Checked Content-Length grammar) and must be independently trustworthy before v0.43.0 (Transfer-Encoding grammar and ordering) begins.

#### Deliverables

- Acceptance contract: Parse every Content-Length field and comma member as a nonempty decimal value with checked arithmetic; accept duplicates only when every parsed value is numerically identical, reject empty members, signs, overflow, or unequal values as unrecoverable framing errors with mandatory close, and publish one canonical length without silently selecting a first or last value.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Repeated and comma-list Content-Length resolution contract and all previously implemented relevant behavior have
reproducible evidence; v0.41.0 (Checked Content-Length grammar) still passes; no behavior assigned to v0.43.0 (Transfer-Encoding grammar and ordering) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 — Transfer-Encoding grammar and ordering

Status: planned

#### Goal

Deliver **Transfer-Encoding grammar and ordering** as the sole primary capability in this stop. It builds
on v0.42.0 (Repeated and comma-list Content-Length resolution) and must be independently trustworthy before v0.44.0 (TE/CL conflict resolution and mandatory close action) begins.

#### Deliverables

- Acceptance contract: Parse Transfer-Encoding as a case-insensitive comma list of transfer-coding tokens and bounded parameters, reject empty elements, invalid token/quoted syntax, and repeated chunked as malformed; for requests require chunked as the final coding or return bounded 400 plus mandatory close, while for responses select chunk framing when chunked is final and otherwise select close-delimited framing for non-final chunked or another final transfer coding; outbound responses may use such non-final/non-chunked transfer coding only with committed Connection: close termination, and unsupported-but-well-formed coding remains distinct from malformed ordering before framing publication.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Transfer-Encoding grammar and ordering contract and all previously implemented relevant behavior have
reproducible evidence; v0.42.0 (Repeated and comma-list Content-Length resolution) still passes; no behavior assigned to v0.44.0 (TE/CL conflict resolution and mandatory close action) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 — TE/CL conflict resolution and mandatory close action

Status: planned

#### Goal

Deliver **TE/CL conflict resolution and mandatory close action** as the sole primary capability in this stop. It builds
on v0.43.0 (Transfer-Encoding grammar and ordering) and must be independently trustworthy before v0.45.0 (Central HTTP/1 message-body-length algorithm) begins.

#### Deliverables

- Acceptance contract: Treat any inbound Transfer-Encoding plus Content-Length as ambiguous framing: servers reject with a bounded 400 and close, clients mark the response connection unusable, and intermediaries may forward only after fully decoding or explicitly reframing and removing the received Content-Length; no conflicting message reaches application or routing publication.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test TE/CL conflict resolution and mandatory close action and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TE/CL conflict resolution and mandatory close action contract and all previously implemented relevant behavior have
reproducible evidence; v0.43.0 (Transfer-Encoding grammar and ordering) still passes; no behavior assigned to v0.45.0 (Central HTTP/1 message-body-length algorithm) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 — Central HTTP/1 message-body-length algorithm

Status: planned

#### Goal

Deliver **Central HTTP/1 message-body-length algorithm** as the sole primary capability in this stop. It builds
on v0.44.0 (TE/CL conflict resolution and mandatory close action) and must be independently trustworthy before v0.46.0 (Fixed-length body decoder) begins.

#### Deliverables

- Acceptance contract: Produce exactly one framing decision with checked arithmetic across method/status context, TE/CL ambiguity, body-forbidden responses, and mandatory-close behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- Run Kani proofs for framing arithmetic and exhaustive method/status/field decisions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Central HTTP/1 message-body-length algorithm contract and all previously implemented relevant behavior have
reproducible evidence; v0.44.0 (TE/CL conflict resolution and mandatory close action) still passes; no behavior assigned to v0.46.0 (Fixed-length body decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 — Fixed-length body decoder

Status: planned

#### Goal

Deliver **Fixed-length body decoder** as the sole primary capability in this stop. It builds
on v0.45.0 (Central HTTP/1 message-body-length algorithm) and must be independently trustworthy before v0.47.0 (Close-delimited response decoder) begins.

#### Deliverables

- Acceptance contract: Yield borrowed body slices totaling exactly the selected Content-Length, release bytes only on acknowledgement, report premature EOF as truncation with no reuse, leave octets after the exact boundary for the next message, and distinguish destination capacity/backpressure from peer length violations without republishing acknowledged data.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Fixed-length body decoder and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-length body decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.45.0 (Central HTTP/1 message-body-length algorithm) still passes; no behavior assigned to v0.47.0 (Close-delimited response decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 — Close-delimited response decoder

Status: planned

#### Goal

Deliver **Close-delimited response decoder** as the sole primary capability in this stop. It builds
on v0.46.0 (Fixed-length body decoder) and must be independently trustworthy before v0.48.0 (Checked chunk-size parser) begins.

#### Deliverables

- Acceptance contract: Use close-delimited decoding only for response contexts selected by the central length algorithm; yield and acknowledge bounded slices until clean transport EOF completes the body, treat cancellation or transport failure as incomplete, and permanently disable connection reuse because EOF is the delimiter.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Close-delimited response decoder and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Close-delimited response decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.46.0 (Fixed-length body decoder) still passes; no behavior assigned to v0.48.0 (Checked chunk-size parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 — Checked chunk-size parser

Status: planned

#### Goal

Deliver **Checked chunk-size parser** as the sole primary capability in this stop. It builds
on v0.47.0 (Close-delimited response decoder) and must be independently trustworthy before v0.49.0 (Incremental chunk-data state) begins.

#### Deliverables

- Acceptance contract: Require one or more hexadecimal digits for chunk-size before optional extension or CRLF, use checked arithmetic against body/profile limits, reject signs, 0x prefixes, whitespace, invalid digits, overflow, and bare line endings, and publish neither size nor body state until the complete size line commits.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked chunk-size parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.47.0 (Close-delimited response decoder) still passes; no behavior assigned to v0.49.0 (Incremental chunk-data state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.48.0 implementation stop reached. Run pentest for this exact commit.`

### v0.49.0 — Incremental chunk-data state

Status: planned

#### Goal

Deliver **Incremental chunk-data state** as the sole primary capability in this stop. It builds
on v0.48.0 (Checked chunk-size parser) and must be independently trustworthy before v0.50.0 (Bounded chunk-extension parser) begins.

#### Deliverables

- Acceptance contract: After a committed nonzero chunk size, expose exactly that many borrowed data octets, wait for acknowledgement before release, then require the following CRLF; premature EOF, missing CRLF, excess arithmetic, or cancellation is terminal and cannot reinterpret data as a new chunk or message.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental chunk-data state contract and all previously implemented relevant behavior have
reproducible evidence; v0.48.0 (Checked chunk-size parser) still passes; no behavior assigned to v0.50.0 (Bounded chunk-extension parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 — Bounded chunk-extension parser

Status: planned

#### Goal

Deliver **Bounded chunk-extension parser** as the sole primary capability in this stop. It builds
on v0.49.0 (Incremental chunk-data state) and must be independently trustworthy before v0.51.0 (Last-chunk and trailer transition) begins.

#### Deliverables

- Acceptance contract: Parse exactly *(BWS ";" BWS token [BWS "=" BWS (token / quoted-string)]) after chunk-size, including quoted-pair rules; count every raw BWS octet against line and work limits but remove BWS before extension-semantic interpretation; reject obs-fold, CR/LF injection, empty names, malformed quotes/escapes, cap extension count, name/value bytes, total line bytes, and work independently, and ignore unknown extension semantics without allocating from peer lengths; named vectors cover BWS around each delimiter at every split, semantic trimming, injection, quoting, empty names, and each independent limit.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded chunk-extension parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.49.0 (Incremental chunk-data state) still passes; no behavior assigned to v0.51.0 (Last-chunk and trailer transition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.50.0 implementation stop reached. Run pentest for this exact commit.`

### v0.51.0 — Last-chunk and trailer transition

Status: planned

#### Goal

Deliver **Last-chunk and trailer transition** as the sole primary capability in this stop. It builds
on v0.50.0 (Bounded chunk-extension parser) and must be independently trustworthy before v0.52.0 (Trailer declarations and prohibited-trailer policy) begins.

#### Deliverables

- Acceptance contract: A zero chunk commits the transition from chunk data to the trailer section, accepts no further chunk data, parses the terminating trailer block through the field parser, and completes only at its empty-line CRLF; partial trailers, cancellation, or EOF cannot publish message completion or permit reuse.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Last-chunk and trailer transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.50.0 (Bounded chunk-extension parser) still passes; no behavior assigned to v0.52.0 (Trailer declarations and prohibited-trailer policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 — Trailer declarations and prohibited-trailer policy

Status: planned

#### Goal

Deliver **Trailer declarations and prohibited-trailer policy** as the sole primary capability in this stop. It builds
on v0.51.0 (Last-chunk and trailer transition) and must be independently trustworthy before v0.53.0 (Chunked encoder with partial-output state) begins.

#### Deliverables

- Acceptance contract: Parse Trailer as a case-insensitive bounded name list and have `vef-core` define `TrailerFieldPermission`: unconditionally reject locally generated fields required for framing, routing, request method/target, or pre-content response control, but accept fields such as ETag or Accept-Ranges only when their field definition permits trailer use; keep local Authentication-Info and Proxy-Authentication-Info generation unavailable until v0.157.2 owns scheme authorization. Received trailers carry no local Rust permission: preserve them in a separate ordered section published only with body completion, classify authentication-info as RequiresSchemeAuthorization and other forbidden fields with a typed semantic/policy disposition after message synchronization rather than automatically as a framing error, never let them retroactively change routing/framing/authentication/representation decisions, and merge a permitted non-authentication field only after a new destination/message-generation-bound `TrailerFieldPermission` explicitly certifies safe merging. Outbound generation and every safe merge require explicit generation-bound permission.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every unconditional local prohibition and permitted ETag/Accept-Ranges case, absent/wrong/correct field permission, unavailable local authentication-info generation, received authentication-info RequiresSchemeAuthorization, received forbidden-field semantic/policy classification after synchronization, declared/undeclared policy, separate ordered storage, no retroactive decision mutation, denied/allowed non-authentication safe merge with fresh destination binding, and all earlier positive/negative/boundary/truncation/cancellation/capacity/no-panic behavior; positive authentication-trailer and authentication safe-merge tests belong to v0.157.2.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Trailer declarations and prohibited-trailer policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.51.0 (Last-chunk and trailer transition) still passes; no behavior assigned to v0.53.0 (Chunked encoder with partial-output state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 — Chunked encoder with partial-output state

Status: planned

#### Goal

Deliver **Chunked encoder with partial-output state** as the sole primary capability in this stop. It builds
on v0.52.0 (Trailer declarations and prohibited-trailer policy) and must be independently trustworthy before v0.54.0 (Unified HTTP/1 outbound message state machine) begins.

#### Deliverables

- Acceptance contract: Emit canonical hexadecimal chunk-size CRLF, exactly the supplied data, and trailing CRLF; finish with zero CRLF, only v0.52.0 `TrailerFieldPermission`-authorized non-authentication trailers, and final CRLF; retain offsets for every partially written segment, never repeat committed bytes after backpressure, reject permission reuse across message generations, keep authentication-info generation unavailable until v0.157.2, and forbid trailers or completion until all declared data commits.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Chunked encoder with partial-output state and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Chunked encoder with partial-output state contract and all previously implemented relevant behavior have
reproducible evidence; v0.52.0 (Trailer declarations and prohibited-trailer policy) still passes; no behavior assigned to v0.54.0 (Unified HTTP/1 outbound message state machine) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 — Unified HTTP/1 outbound message state machine

Status: planned

#### Goal

Deliver **Unified HTTP/1 outbound message state machine** as the sole primary capability in this stop. It builds
on v0.53.0 (Chunked encoder with partial-output state) and must be independently trustworthy before v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) begins.

#### Deliverables

- Acceptance contract: Serialize a head followed by exactly no body, fixed-length bytes, or chunked bytes; reject length disagreement, illegal trailers, post-completion commands, and sender-side HEAD/CONNECT/1xx/204/304 violations under one-byte output fragmentation. Track every generation-bound outbound message as `AcceptedPrivate -> Frozen -> HeadCommitted -> MessageCommitted` or `Abandoned`: acceptance remains replaceable until first nonempty exposure, exposure freezes exact bytes, and only acknowledgement of the complete head's final octet enters `HeadCommitted`. For a client request, only `HeadCommitted` creates response-correlation authority; its body may remain in progress because an early final response is legal. Partial-head failure never creates that authority. Define `EarlyFinalBodyDisposition::{ContinueToDelimiterForReuse, SuppressRemainingAndClose, AlreadyMessageCommitted, TransportAborted}` over the request generation, framing mode, exact promised length/delimiter/trailers, committed prefix, current record/token, and unsent suffix. A received final response resolves the live `OutputToken` through the v0.25.0 combined call before parsing, preserving exactly its zero/short/full acknowledged body prefix. `SuppressRemainingAndClose` releases only bytes certified not consumed by the transport, abandons the unsent record/future fixed or chunked data/zero chunk/trailers, rejects every later body/trailer command, and permanently prohibits reuse. `ContinueToDelimiterForReuse` must emit the exact remaining fixed body or chunked data, terminating zero chunk, and trailers despite the early response; no successor becomes eligible before request `MessageCommitted`. Cancellation/failure reports committed versus unsent progress once without reinterpreting bytes. Keep raw locally generated head constructors and framing-only serializer entries crate-private/unstable so they cannot become a final public bypass. Request framing remains internally testable but v0.180.4 must replace its raw entry with frozen `ValidatedConditionalRequest`; v0.182.1 replaces the response entry with frozen `ValidatedResponse` carrying an unextractable sealed permit before public API stabilization.
- Make disposition selection a total engine-owned legality matrix.
  `AlreadyMessageCommitted` is automatic and cannot be requested.
  `ContinueToDelimiterForReuse` is legal only while persistence remains
  possible, output transport remains writable, every remaining body/trailer
  source is available, and a bounded continuation deadline/work budget was
  reserved before selection. `Connection: close`, HTTP/1.0 default-close,
  close-delimited response framing, transport write closure, or unavailable
  body source forces suppression/abort. `SuppressRemainingAndClose` returns
  `EarlyFinalTransportAction::{SealHttpOutputAndDrainResponse,
  CloseTransportNow}` so an adapter can boundedly finish response input or
  close immediately; core never assumes TCP half-close exists through TLS.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Split every request/response head and fixed/chunked body record at all offsets; cross zero/short/full acknowledgement, early final response, each `EarlyFinalBodyDisposition`, terminating zero chunk, trailers, failure, cancellation, and body progress. Cross every persistence/write/source/budget condition and both transport actions. Prove response-correlation authority appears exactly at final-head-octet acknowledgement, committed body progress is exact, AlreadyMessageCommitted is automatic, illegal continuation cannot be selected, suppression releases only certified-unsent bytes and forces non-reuse, and legal continuation reaches the promised delimiter before reuse.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unified HTTP/1 outbound message state machine contract and all previously implemented relevant behavior have
reproducible evidence; v0.53.0 (Chunked encoder with partial-output state) still passes; no behavior assigned to v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 — Inbound body acknowledgement, drain, discard, cancellation, and reuse

Status: planned

#### Goal

Deliver **Inbound body acknowledgement, drain, discard, cancellation, and reuse** as the sole primary capability in this stop. It builds
on v0.54.0 (Unified HTTP/1 outbound message state machine) and must be independently trustworthy before v0.56.0 (HTTP/1.1 persistence and Connection semantics) begins.

#### Deliverables

- Acceptance contract: Publish a borrowed BodyChunk whose acknowledged prefix alone may be released; retain over-read bytes and every unacknowledged suffix; drain or discard only under byte, work, and injected-deadline caps; preserve exact chunked/trailer framing while draining; and mandate connection close on cap exhaustion, malformed remainder, cancellation ambiguity, or incomplete framing before storage reuse.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Inbound body acknowledgement, drain, discard, cancellation, and reuse and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Inbound body acknowledgement, drain, discard, cancellation, and reuse contract and all previously implemented relevant behavior have
reproducible evidence; v0.54.0 (Unified HTTP/1 outbound message state machine) still passes; no behavior assigned to v0.56.0 (HTTP/1.1 persistence and Connection semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 — HTTP/1.1 persistence and Connection semantics

Status: planned

#### Goal

Deliver **HTTP/1.1 persistence and Connection semantics** as the sole primary capability in this stop. It builds
on v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) and must be independently trustworthy before v0.57.0 (Sequential request/response connection state) begins.

#### Deliverables

- Acceptance contract: HTTP/1.1 is persistent by default only after a self-delimited complete message. Implement the sole bounded, version-neutral `Connection` field parser here and return sealed `ValidatedConnectionOptions` bound to the exact ordered field set, exact HTTP version, role, message/request generation, and connection generation. Parse repeated field lines and comma lists once under field/value/element/work limits, compare token values case-insensitively after permitted OWS handling, tolerate bounded empty list elements only as non-evidence, let `close` override `keep-alive`, and retain ordered nominated hop-field names for later consumers. Quoted, substring-like, or otherwise malformed values never count as `close`; any malformed field invalidates the whole evidence object; `Proxy-Connection` is not an alias and grants no option evidence. No later milestone may reparse or independently normalize `Connection`. At this stop activate only the HTTP/1.1 persistence interpretation; the HTTP/1.0 parser later invokes the same lexical component and applies only its separately sealed version-specific semantics. Apply close and mark reuse impossible after close-delimited bodies, framing errors, incomplete bodies, failed transitions, cancellation, or mandatory-close policy. For an early final response, `SuppressRemainingAndClose` and `TransportAborted` permanently prohibit reuse, including when the response omits `Connection: close`; a partially transmitted fixed-length request or chunked request lacking its terminating zero chunk can never precede another request. `ContinueToDelimiterForReuse` permits later reuse only after the exact request body/trailers reach `MessageCommitted` and the response lifecycle independently completes.
- Treat close-delimited response selection and every peer/local close token as
  an input to the v0.54.0 early-final legality matrix. If suppression selects
  `SealHttpOutputAndDrainResponse`, bound response drain bytes/work/time and
  then close; `CloseTransportNow` closes immediately. Neither action restores
  persistence, and neither requires or implies a transport half-close.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Cross repeated `Connection` fields and comma lists, mixed casing and OWS, `keep-alive` plus `close` with close winning, bounded empty elements, quoted/substr-like close values, `Proxy-Connection: close`, malformed fields containing a recognizable close token, and substitution across HTTP versions and request/message/connection generations. Require one version-neutral lexical result, exact version retention, no partial evidence from malformed input, and exact ordered nominations. Cross early final responses with/without validated `Connection: close`, each request framing mode and partial prefix, continuation/suppression, response-body parsing, EOF/failure, and attempted reuse; prove only two fully delimited completed HTTP/1.1 lifecycles permit reuse.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 persistence and Connection semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) still passes; no behavior assigned to v0.57.0 (Sequential request/response connection state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 — Sequential request/response connection state

Status: planned

#### Goal

Deliver **Sequential request/response connection state** as the sole primary capability in this stop. It builds
on v0.56.0 (HTTP/1.1 persistence and Connection semantics) and must be independently trustworthy before v0.58.0 (Optional bounded pipelining queue) begins.

#### Deliverables

- Acceptance contract: Without pipelining, admit one request and its ordered informational/final response lifecycle at a time; represent the client side as a one-entry generation-bound outstanding-response FIFO populated only by v0.54.0 `HeadCommitted`. Associate every 1xx and final response only with its oldest committed request. If response input arrives with no committed request, close as ambiguous under RFC 9112 without publishing a response or borrowing an accepted/private/frozen request identity. An early final retains the original exchange generation until `ContinueToDelimiterForReuse` reaches request `MessageCommitted` or a close/abort terminal state owns all unsent bytes. Reject or backpressure a second request until body acknowledgement, early-final disposition, and response completion make reuse legal, bind cancellation to that exchange generation, and never attach late bytes/events to the next exchange.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Sequential request/response connection state and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Feed response prefixes before request exposure, at every acknowledged request-head/body offset, after exact head commitment while the body remains in progress, and after cancellation/failure; require ambiguous close with no committed request, oldest-generation correlation only after final-head-octet acknowledgement, and no successor until the early-final disposition reaches its reuse-safe or terminal-close outcome.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sequential request/response connection state contract and all previously implemented relevant behavior have
reproducible evidence; v0.56.0 (HTTP/1.1 persistence and Connection semantics) still passes; no behavior assigned to v0.58.0 (Optional bounded pipelining queue) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 — Optional bounded pipelining queue

Status: planned

#### Goal

Deliver **Optional bounded pipelining queue** as the sole primary capability in this stop. It builds
on v0.57.0 (Sequential request/response connection state) and must be independently trustworthy before v0.59.0 (Informational response lifecycle) begins.

#### Deliverables

- Acceptance contract: When explicitly enabled, queue at most the configured number and bytes of fully validated requests, but populate the outstanding-response FIFO only as each outbound request reaches v0.54.0 `HeadCommitted`; accepted/private/frozen requests are not response-correlatable. Preserve request-head commitment and response association order, stop parsing at capacity without partial enqueue, associate bodies/cancellation by generation, and match every 1xx/final response only to the oldest committed request. An early final freezes successor admission/output until the original request either reaches `MessageCommitted` under `ContinueToDelimiterForReuse` or selects mandatory close/abort; no already queued successor may follow a partial fixed/chunked request. Close rather than accept a response with no committed request or emit an out-of-order, ambiguous, or post-error response.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Optional bounded pipelining queue and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Permute several accepted, frozen, partially acknowledged, head-committed, body-active, completed, and abandoned request generations with response input and every early-final disposition; prove FIFO insertion occurs once at HeadCommitted, no response skips an older committed request, and no queued successor is exposed after an incomplete predecessor or before safe delimiter completion.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional bounded pipelining queue contract and all previously implemented relevant behavior have
reproducible evidence; v0.57.0 (Sequential request/response connection state) still passes; no behavior assigned to v0.59.0 (Informational response lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 — Informational response lifecycle

Status: planned

#### Goal

Deliver **Informational response lifecycle** as the sole primary capability in this stop. It builds
on v0.58.0 (Optional bounded pipelining queue) and must be independently trustworthy before v0.60.0 (Expect: 100-continue state) begins.

#### Deliverables

- Acceptance contract: Model two exclusive response branches: zero or more informational responses in 100..=199 excluding 101 followed by exactly one final response, or one validated 101 that terminally ends HTTP and is followed only by the selected protocol. On the client side, both branches require and remain attached to the oldest `HeadCommitted` request in the outstanding-response FIFO; response input with no committed request closes as ambiguous without publication. A 100 resumes ordinary request-body transmission. Any final response received before request `MessageCommitted` atomically selects the v0.54.0 `EarlyFinalBodyDisposition` after the combined call resolves its live output token; simultaneous response-body parsing cannot hide or rewrite request-body progress. HTTP/1.0 servers never emit any 1xx, informational responses after a final/101 and invalid 1xx framing are rejected, and every event remains correlated to the active committed request without premature completion or recycling.
- Before selecting continuation, reserve its deadline/work budget and prove the
  current response framing/persistence, transport write state, and remaining
  source satisfy v0.54.0. Otherwise select suppression/abort and its typed
  transport action. Response draining may continue only within the reserved
  bounds and can never make the connection reusable.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test the informational-then-final and terminal-101 branches separately at every opening-request head/body acknowledgement offset, including absent FIFO authority, oldest committed selection, 100 resumption, an active fixed/chunked request body and trailers, simultaneous response-body parsing, every early-final disposition, HTTP/1.0 1xx emission rejection, post-final/post-101 invalid states, and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational response lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.58.0 (Optional bounded pipelining queue) still passes; no behavior assigned to v0.60.0 (Expect: 100-continue state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 — Expect: 100-continue state

Status: planned

#### Goal

Deliver **Expect: 100-continue state** as the sole primary capability in this stop. It builds
on v0.59.0 (Informational response lifecycle) and must be independently trustworthy before v0.61.0 (EOF, truncation, and incomplete-message rules) begins.

#### Deliverables

- Acceptance contract: Recognize exact 100-continue, emit 417 for unsupported expectations by policy, withhold client bodies, accept caller timeout decisions through injected time, handle final-before-100 and server pre-body rejection, bound drain-or-close behavior, and preserve pipeline ordering around interim responses. A client accepts received 100 or an early final only for the oldest committed request head; no response becomes valid from command acceptance or partial head output. Resolve any live request-body `OutputToken` first, then let 100 resume ordinary body output or let a final response select `EarlyFinalBodyDisposition` with the exact committed/unsent prefix. A 417 retry obtains a fresh exchange generation, never overlaps the incomplete original request, and uses a fresh connection unless the original request safely reached `MessageCommitted` and the response/reuse contract also completed. Server-side inbound request-body acceptance never depends on acknowledgement of an outbound 100 because a client may send after its own timeout. If Upgrade will succeed, require full acknowledgement of the complete 100 response head before any 101 exposure whenever Expect applies, and forbid 101 until the complete request message has been sent or received.
- A caller may configure early-final policy preference before output but cannot
  select `AlreadyMessageCommitted`, override a forced suppression/abort
  condition, fabricate continuation budget/source/writability, choose transport
  half-close, or restore reuse after either typed close action.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test final-before-100 and 100-before-body at every request-head/body output acknowledgement offset; fixed-length/chunked/trailer output; response with/without `Connection: close`; simultaneous response-body input; suppress/continue/already-committed/transport-aborted disposition; cancellation; mandatory complete-100-head acknowledgement before 101 exposure; and rejection of 101 before request completion. Exercise 417 retry on the same/fresh connection, stale/original versus fresh exchange generations, attempted overlap and pipelined successors, timeout/drain/close choices, and all previously implemented relevant behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Expect: 100-continue state contract and all previously implemented relevant behavior have
reproducible evidence; v0.59.0 (Informational response lifecycle) still passes; no behavior assigned to v0.61.0 (EOF, truncation, and incomplete-message rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 — EOF, truncation, and incomplete-message rules

Status: planned

#### Goal

Deliver **EOF, truncation, and incomplete-message rules** as the sole primary capability in this stop. It builds
on v0.60.0 (Expect: 100-continue state) and must be independently trustworthy before v0.62.0 (HEAD response-framing context) begins.

#### Deliverables

- Acceptance contract: EOF completes only a selected close-delimited response or an already complete message; EOF inside a start line, field section, fixed body, chunk-size/data/trailers, or required transition is typed truncation, publishes no synthetic completion, and makes the connection non-reusable, with transport failure distinct from clean EOF.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test EOF, truncation, and incomplete-message rules and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The EOF, truncation, and incomplete-message rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.60.0 (Expect: 100-continue state) still passes; no behavior assigned to v0.62.0 (HEAD response-framing context) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 — HEAD response-framing context

Status: planned

#### Goal

Deliver **HEAD response-framing context** as the sole primary capability in this stop. It builds
on v0.61.0 (EOF, truncation, and incomplete-message rules) and must be independently trustworthy before v0.63.0 (1xx, 204, 205, 304, and body-forbidden response handling) begins.

#### Deliverables

- Acceptance contract: For a response to HEAD, consume and validate the head using the corresponding GET metadata rules but select no message body regardless of Content-Length or Transfer-Encoding; any following octets belong to the next protocol state, and the response remains correlated to the original HEAD request before framing selection.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HEAD response-framing context and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEAD response-framing context contract and all previously implemented relevant behavior have
reproducible evidence; v0.61.0 (EOF, truncation, and incomplete-message rules) still passes; no behavior assigned to v0.63.0 (1xx, 204, 205, 304, and body-forbidden response handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 — 1xx, 204, 205, 304, and body-forbidden response handling

Status: planned

#### Goal

Deliver **1xx, 204, 205, 304, and body-forbidden response handling** as the sole primary capability in this stop. It builds
on v0.62.0 (HEAD response-framing context) and must be independently trustworthy before v0.64.0 (CONNECT request and successful tunnel transition) begins.

#### Deliverables

- Acceptance contract: Select no body for every 1xx, 204, and 304 response and for successful CONNECT according to its tunnel rule; for outbound HTTP/1 205 permit only zero-content serialization—canonical Content-Length: 0, an explicitly selected chunked body containing only the terminating zero chunk, or connection close immediately after the head—and reject every nonzero body command; inbound 205 still uses the ordinary HTTP/1 body-length algorithm, so nonzero fixed/chunked/close-delimited content is boundedly consumed/discarded to its delimiter or forces close before reuse, produces a typed semantic violation, and cannot be forwarded as a valid 205; reject forbidden 204 transfer coding and invalid framing metadata, allow HEAD/304 Content-Length only as representation metadata, and never misclassify following octets as a new response.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test 1xx/204/304 body prohibition plus outbound 205 Content-Length: 0, zero-chunked, close-delimited-zero, and nonzero-command rejection; pipeline malicious fixed/chunked/close-delimited nonzero 205 content and prove bounded discard-or-close, typed violation, no false next response, no forwarding, and all previously implemented relevant behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 1xx, 204, 205, 304, and body-forbidden response handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.62.0 (HEAD response-framing context) still passes; no behavior assigned to v0.64.0 (CONNECT request and successful tunnel transition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 — CONNECT request and successful tunnel transition

Status: planned

#### Goal

Deliver **CONNECT request and successful tunnel transition** as the sole primary capability in this stop. It builds
on v0.63.0 (1xx, 204, 205, 304, and body-forbidden response handling) and must be independently trustworthy before v0.65.0 (RFC 9931 optimistic-data protections) begins.

#### Deliverables

- Acceptance contract: Accept CONNECT only with the v0.40.0 validated ConnectAuthority and staged Sans-I/O admission: authorize its lexical host plus explicit 1..=65535 port, issue a request/policy-generation-bound ConnectAttemptToken, let the caller resolve, authorize every candidate endpoint before its dial, and consume exactly once only an AuthorizedConnectOutcome whose opaque attempt identity, authority, authorized resolved endpoint, actual connected peer, attempt/request/policy generations, and token all match; cancellation, rejection, policy-generation change, non-2xx completion, or tunnel commitment invalidates every remaining attempt/outcome, and duplicate outcome/success commands are InvalidState before output; VEF performs no DNS, dialing, or socket inspection, and rejects stale, alternate, mismatched, or policy-revoked outcomes before 2xx, upstream bytes, or tunnel publication; use no Host routing or scheme default; outbound builders reject request content, Content-Length, and Transfer-Encoding; hardened inbound framing rejects either field with bounded 400 plus mandatory close and no reparse; successful server responses forbid both fields while clients ignore received ones, and every response is non-cacheable. A client accepts a received 2xx only for its oldest committed CONNECT request head. A server publishes the tunnel and hands over over-read bytes only after full acknowledgement of the complete 2xx response head. Partial 2xx acknowledgement followed by transport failure closes without tunnel publication or reinterpretation of tunnel bytes; non-2xx remains ordinary HTTP.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test lexical rejection before resolution, every resolved endpoint allow/deny, alternate-address and connected-peer mismatch, stale attempt/request/policy generations, revocation after resolution, single consumption, duplicate outcome/success, replay after cancellation/non-2xx/commit and same-generation reuse, caller-certified success without socket inspection, safe/unsafe ports, bracketed IPv6, Host disagreement, content/framing rejection with close/no-reparse, successful field prohibition/client ignore, non-cacheability, and all earlier behavior. For 2xx/non-2xx, cross every CONNECT request-head and response-head acknowledgement offset, over-read boundary, and transport failure; require client correlation only after request HeadCommitted and server publication only after complete 2xx-head acknowledgement, with partial failure closing without handoff or reparse.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT request and successful tunnel transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.63.0 (1xx, 204, 205, 304, and body-forbidden response handling) still passes; no behavior assigned to v0.65.0 (RFC 9931 optimistic-data protections) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.64.0 implementation stop reached. Run pentest for this exact commit.`

### v0.65.0 — RFC 9931 optimistic-data protections

Status: planned

#### Goal

Deliver **RFC 9931 optimistic-data protections** as the sole primary capability in this stop. It builds
on v0.64.0 (CONNECT request and successful tunnel transition) and must be independently trustworthy before v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) begins.

#### Deliverables

- Acceptance contract: For an untrusted downstream TCP client, a proxy client either waits for the CONNECT 2xx before forwarding payload or sends Connection: close; a proxy server rejecting CONNECT closes the transport and processes no later request regardless of Connection; specifically, HTTP/1 CONNECT 407 carries a valid Proxy-Authenticate challenge, mandates connection close, discards owned optimistic/tunnel bytes, logically invalidates attempt/credential capabilities and releases their references without promising caller-buffer zeroization, and permits authentication retry only on a fresh connection/generation. Seal `OptimisticConnectCloseProof::{ReceivedValidatedCloseOption, LocallyCommittedCloseHead}` to the exact HTTP/1.1 request, exchange, connection/leg, and head generation. `ReceivedValidatedCloseOption` can be refined only from the exact v0.56.0 `ValidatedConnectionOptions` containing a valid `close` token for that request; it never reparses raw fields. Locally generated requests prove the exact serialized close-bearing request head reached v0.54.0 `HeadCommitted`; queued bytes or configured intention alone grant no authority. Neither proof supports HTTP/1.0, and no later HTTP/1.0 default-close evidence may be rebound to it. Only then mint `PermittedOptimisticConnectInput`. If early ordinary CONNECT input arrives without proof, classify `UnpermittedOptimisticConnectInput { reason: MissingCommittedCloseProof }`, discard it exactly once, close, never reparse, and never later promote it even if CONNECT succeeds. Permitted input transfers once on success or discards/closes once on non-2xx/failure. `ForbiddenOptimisticWebSocketInput` and `ForbiddenHttp1ConnectUdpInput` always terminate without a lease.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test wait-or-close and both close-proof constructors: refine received proof only from exact v0.56.0 `ValidatedConnectionOptions`; reject raw-field reparsing, malformed/partial evidence, `Proxy-Connection`, and request/message/connection-generation substitution; test a locally generated close-bearing request at every acknowledgement offset before/at HeadCommitted, configured intent with no serialized/committed close, stale/cross-head proof, and early bytes followed by 2xx/non-2xx. Require uncommitted/missing proof to select strict unpermitted discard/close/no-reparse/no-later-promotion, permitted proof to transfer once on success or discard once on failure, and all rejected CONNECT/407/fresh-generation/caller-scrub behavior to remain intact. Compile-fail any attempt to construct either proof from HTTP/1.0 default-close state. Also test HTTP/1 request head plus premature WebSocket bytes, CONNECT-UDP prohibition, positive/negative boundaries, truncation, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 9931 optimistic-data protections contract and all previously implemented relevant behavior have
reproducible evidence; v0.64.0 (CONNECT request and successful tunnel transition) still passes; no behavior assigned to v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 — Connection-option, Upgrade, and hop-by-hop field grammar

Status: planned

#### Goal

Deliver **Connection-option, Upgrade, and hop-by-hop field grammar** as the sole primary capability in this stop. It builds
on v0.65.0 (RFC 9931 optimistic-data protections) and must be independently trustworthy before v0.67.0 (101 Switching Protocols transition and publication barrier) begins.

#### Deliverables

- Acceptance contract: Reuse the exact sealed v0.56.0 `ValidatedConnectionOptions`; do not parse, split, case-fold, trim, or normalize `Connection` again. Add only bounded `Upgrade` field-value grammar and the semantic pairing that requires an exact validated `upgrade` connection option before any 101 or WebSocket publication. Bind the pair to the same message/request/connection generations and derive explicit hop-by-hop handling from the ordered option evidence.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Upgrade grammar and Connection/Upgrade pairing against the v0.56.0 corpus: repeated fields/comma lists, mixed casing/OWS, empty elements, close-over-keep-alive, quoted/substr-like tokens, `Proxy-Connection`, malformed input containing recognizable tokens, and cross-generation evidence substitution. Require byte-for-byte reuse of one `ValidatedConnectionOptions` decision, no second parser/normalizer path, exact pairing, and all earlier positive/negative/boundary/truncation/cancellation/capacity/no-panic behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-option, Upgrade, and hop-by-hop field grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.65.0 (RFC 9931 optimistic-data protections) still passes; no behavior assigned to v0.67.0 (101 Switching Protocols transition and publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.66.0 implementation stop reached. Run pentest for this exact commit.`

### v0.67.0 — 101 Switching Protocols transition and publication barrier

Status: planned

#### Goal

Deliver **101 Switching Protocols transition and publication barrier** as the sole primary capability in this stop. It builds
on v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) and must be independently trustworthy before v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) begins.

#### Deliverables

- Acceptance contract: Validate a 101 only after its Connection/Upgrade prerequisites and selected protocol validate and the complete request message has been sent or received. A client may accept it only for its oldest committed opening-request head. A server activates the transition and hands buffered post-handshake bytes exactly once only after full acknowledgement of the complete 101 response head; partial output plus failure closes without publication or reparse. Treat committed 101 as the terminal HTTP response branch and make every later HTTP response parse, serialization, body, trailer, pipeline, or reuse operation an InvalidState without consuming or emitting bytes.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test complete-request gating, client receipt before/at opening-request HeadCommitted, invalid Connection/Upgrade selection, every 101 response-head acknowledgement offset, partial-output failure, exactly-once over-read handoff, and every HTTP parse/serialize/body/trailer/pipeline operation after committed 101 returning InvalidState without byte progress, plus all previously implemented relevant behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 101 Switching Protocols transition and publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) still passes; no behavior assigned to v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 — Separate WebSocket handshake crate, key, version, and token validation

Status: planned

#### Goal

Deliver **Separate WebSocket handshake crate, key, version, and token validation** as the sole primary capability in this stop. It builds
on v0.67.0 (101 Switching Protocols transition and publication barrier) and must be independently trustworthy before v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) begins.

#### Deliverables

- Acceptance contract: Create an optional no_std handshake boundary that validates Sec-WebSocket-Key base64 shape, version 13, Upgrade/Connection tokens, and distinct client/server rules without implementing frames.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Separate WebSocket handshake crate, key, version, and token validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate WebSocket handshake crate, key, version, and token validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.67.0 (101 Switching Protocols transition and publication barrier) still passes; no behavior assigned to v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 — Caller-supplied WebSocket nonce and entropy boundary

Status: planned

#### Goal

Deliver **Caller-supplied WebSocket nonce and entropy boundary** as the sole primary capability in this stop. It builds
on v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) and must be independently trustworthy before v0.70.0 (WebSocket accept generation and client/server validation) begins.

#### Deliverables

- Acceptance contract: Require a validated WebSocketNonce([u8; 16]) from the caller or adapter-only entropy capability for every client handshake, including each HTTP/2-downstream to HTTP/1-upstream bridge attempt; core code rejects missing/reused-policy input and never creates deterministic, time-derived, repeated, or weak keys.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Caller-supplied WebSocket nonce and entropy boundary and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Caller-supplied WebSocket nonce and entropy boundary contract and all previously implemented relevant behavior have
reproducible evidence; v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) still passes; no behavior assigned to v0.70.0 (WebSocket accept generation and client/server validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 — WebSocket accept generation and client/server validation

Status: planned

#### Goal

Deliver **WebSocket accept generation and client/server validation** as the sole primary capability in this stop. It builds
on v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) and must be independently trustworthy before v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) begins.

#### Deliverables

- Acceptance contract: Implement and vector-test the RFC 6455 SHA-1 plus base64 accept calculation, server generation, client validation, invalid padding/length rejection, and bounded dependency-free operation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WebSocket accept generation and client/server validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket accept generation and client/server validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) still passes; no behavior assigned to v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 — WebSocket negotiation, origin metadata, and byte-publication barrier

Status: planned

#### Goal

Deliver **WebSocket negotiation, origin metadata, and byte-publication barrier** as the sole primary capability in this stop. It builds
on v0.70.0 (WebSocket accept generation and client/server validation) and must be independently trustworthy before v0.72.0 (Safe forwarding and explicit reframing plan) begins.

#### Deliverables

- Acceptance contract: Define subprotocol and extension selection, preserve Origin metadata for caller policy, reject unsolicited negotiation, and publish no post-handshake bytes before success. WebSocket uses the v0.67.0 wire boundary: client receipt of 101 requires its opening request head to be committed, while a server handshake and every post-handshake byte remain unpublished until the complete 101 response head is acknowledged. Distinguish legal success-following client input—101 and WebSocket bytes in one read—from forbidden server-side request-following input before full 101 transport commitment. Only legal success-following over-read can become transition-owned. In `advance_io(output_ack, input)`, full 101 acknowledgement commits success before parsing input; zero or short acknowledgement makes WebSocket input premature and terminal, while invalid acknowledgement leaves input wholly unconsumed. Premature input is discarded once with no lease, reparse, Active state, or later forwarding.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WebSocket negotiation, origin metadata, and byte-publication barrier and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross every opening-request and 101-response acknowledgement offset, including zero/short/full acknowledgement combined with input, HTTP/1 request plus premature WebSocket bytes in one buffer, legal upstream 101 plus data, over-read bytes, and partial failure. Prove only success-following input becomes transition-owned; premature input produces one terminal cleanup, no transferable lease, no reparse, no Active, and no later publication.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket negotiation, origin metadata, and byte-publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.70.0 (WebSocket accept generation and client/server validation) still passes; no behavior assigned to v0.72.0 (Safe forwarding and explicit reframing plan) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 — Safe forwarding and explicit reframing plan

Status: planned

#### Goal

Deliver **Safe forwarding and explicit reframing plan** as the sole primary capability in this stop. It builds
on v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) and must be independently trustworthy before v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) begins.

#### Deliverables

- Acceptance contract: Forward only a fully validated message with one selected body length; remove hop-by-hop fields and received framing metadata, choose exactly one destination framing, serialize a complete destination head before body bytes, and on unsupported coding, capacity failure, cancellation, or output backpressure emit no partially reinterpretable downstream message.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Safe forwarding and explicit reframing plan and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Safe forwarding and explicit reframing plan contract and all previously implemented relevant behavior have
reproducible evidence; v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) still passes; no behavior assigned to v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.72.0 implementation stop reached. Run pentest for this exact commit.`

### v0.73.0 — RFC 1945 HTTP/1.0 parser and hardened profile

Status: planned

#### Goal

Deliver **RFC 1945 HTTP/1.0 parser and hardened profile** as the sole primary capability in this stop. It builds
on v0.72.0 (Safe forwarding and explicit reframing plan) and must be independently trustworthy before v0.74.0 (HTTP/1.0 default-close lifecycle) begins.

#### Deliverables

- Acceptance contract: In the explicit HTTP/1.0 profile accept only RFC 1945 request/status lines and fields under strict configured CRLF/obs-fold policy, do not require Host, reject chunked framing and HTTP/1.1-only transfer semantics, preserve unknown methods/statuses within shared valid domains, and apply hardened size/work ceilings before publication. Invoke the sole v0.56.0 version-neutral `Connection` lexer and retain `ValidatedConnectionOptions` with exact HTTP/1.0 version binding; do not yet grant keep-alive semantics. CONNECT classification precedence is total and preserves earlier typed failures. Local storage, response-reserve, or local work-capacity failure returns its local capacity action or the existing deterministic zero-partial-output close and never becomes a peer error. Before target/field classification, aggregate start-line byte or parse-work exhaustion and overlong method token select typed `StartLinePeerLimitAndClose::{AggregateBytes, AggregateWork, MethodBytes}`; a role may emit the existing bounded 400 only when a complete trusted HTTP/1.0 version and mandatory reserve are already available, otherwise it closes with zero response bytes. Overlong or malformed version selects `StartLineVersionAndClose` and never emits a version-assuming response. A request target within its own limit that makes the complete start line exceed its aggregate limit remains `AggregateBytes`, not 414. Request-target byte/work limit alone selects the existing 414-and-close disposition. Field-line, field-count, field-section, or field-parse-work limit selects the existing 431-and-close disposition. Other syntax, invalid target form, malformed fields/framing, or CONNECT-content violation selects the existing bounded 400-and-close path. Only a completely bounded and syntactically recognized HTTP/1.0 head with method CONNECT and valid authority-form target mints typed `UnsupportedHttp10ConnectDisposition`. Authority-form recognition exists solely to classify this unsupported method and does not add CONNECT or authority-form to the RFC 1945 application-visible request grammar. Mint before application publication, authority resolution, forwarding, tunnel state, or optimistic-input ownership. A local client builder returns zero-output `UnsupportedVersionMethod`. A receiving server or proxy, and an intermediary or gateway acting on its downstream leg, freeze exactly the 70-byte HTTP/1.0-compatible response `HTTP/1.0 501 Not Implemented\r\nConnection: close\r\nContent-Length: 0\r\n\r\n` plus mandatory transport close; never add Transfer-Encoding, chunking, trailers, variable fields, or an application body, and never resolve or forward the authority. Reserve all 70 bytes and the close action before disposition publication. Model the terminal output action as `UnsupportedHttp10ConnectAction::{Flush501ThenClose, CloseTransportNow}`. Rejection starts in `Flush501ThenClose`; first non-empty exposure freezes the exact image, acknowledgement offsets 0..=69 retain the record, and final-byte acknowledgement at 70 alone records response commitment, after which close remains mandatory. If optimistic bytes accompany the original request, discard them exactly once and never HTTP-reparse them. An invalid, stale, cross-record, or oversized acknowledgement is completely state-neutral: retain `Flush501ThenClose`, cursor, token, response record, close obligation, and all accompanying input unchanged and wholly unconsumed. Input-only delivery with a live 501 token likewise returns `DriverCommitOrderViolation` state-neutrally. After a valid zero, short, or full acknowledgement is applied first, any accompanying new peer input remains wholly unconsumed and selects `CloseTransportNow`; accept/retain/enqueue/parse/publish none of it and create no bounded-input backpressure state. A short acknowledgement followed by this close never fabricates response commitment. Partial 501 output followed by EOF/cancellation/transport failure also selects `CloseTransportNow` with no successor or tunnel publication. If the complete response reserve cannot be acquired before exposure, select the zero-partial close action. This profile creates no CONNECT proof and cannot consume either HTTP/1.1 `OptimisticConnectCloseProof` variant.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Cross local storage/reserve/work capacity; aggregate start-line byte/work; method, target, and version component limits; target-within-cap plus aggregate overflow; target byte/work; field-line/count/section/work; syntax/framing/content; and fully valid authority-form HTTP/1.0 CONNECT in precedence order. At one-under, exact, and one-over every start-line/component boundary require the exact local, `StartLinePeerLimitAndClose`, `StartLineVersionAndClose`, 414, 431, 400, or 501 outcome; start-line peer limits and malformed/overlong version never fall through to 501, and authority-form is never application-visible. Test local-builder zero-output rejection and receiving server/proxy/intermediary/gateway outcomes, including request plus optimistic bytes in one buffer, default-close, explicit `Connection: close`, `Connection: keep-alive`, and `Proxy-Connection: close`. Assert the exact 70 bytes, absence of Transfer-Encoding/chunking/trailers/body variability, pre-reservation, immutable first exposure, offsets 0..=70, and final-byte-only commitment. At every cursor inject invalid/stale/cross-record/oversized acknowledgement plus additional input and prove `Flush501ThenClose`, token, cursor, record, close obligation, and input are state-neutral. Cross input-only delivery with the live token. Then inject input after every valid zero/short/full acknowledgement and require `CloseTransportNow`, all input wholly unconsumed, no parse/retain/enqueue/publication/backpressure, and no fabricated commitment at a short offset. Cross mandatory-response capacity failure, EOF, cancellation, and transport failure; attempt application publication, authority resolution, forwarding, successor parsing, and tunnel creation. Require one original optimistic-byte discard, complete 501 or zero-partial/immediate close, mandatory close, no fabricated completion, and no HTTP/1.1 close-proof construction or rebinding.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 1945 HTTP/1.0 parser and hardened profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.72.0 (Safe forwarding and explicit reframing plan) still passes; no behavior assigned to v0.74.0 (HTTP/1.0 default-close lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 — HTTP/1.0 default-close lifecycle

Status: planned

#### Goal

Deliver **HTTP/1.0 default-close lifecycle** as the sole primary capability in this stop. It builds
on v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) and must be independently trustworthy before v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) begins.

#### Deliverables

- Acceptance contract: Treat every supported HTTP/1.0 exchange as connection-close by default, delimit an unlengthened response by EOF, never pipeline, and permit no reuse merely because a message is self-delimited or carries an unrecognized Connection token. Define sealed `Http10PersistenceDisposition` over role, received message kind/direction, connection generation, and newest-message generation. Default-close client request generation emits `Connection: close`; default-close origin/server, proxy, or gateway response generation emits `Connection: close`. A proxy or gateway receiving an HTTP/1.0 request selects `IntermediaryDownstreamClose` and can never preserve that downstream client connection. An origin receiving a request records only `OriginRequestCandidate` for possible v0.75.0 refinement. A client receiving a response records `ClientUpstreamCandidate`; a proxy or gateway receiving an upstream response records its distinct `IntermediaryUpstreamCandidate`; role/message-kind combinations outside these directions are `InvalidRoleDirection` and grant no persistence. Admission of any newer received message generation atomically invalidates the prior persistence disposition and every refinement before parsing/publication of the newer message; no older keep-alive evidence can be consumed afterward. Cancellation, error, EOF, invalid framing, budget expiry, incomplete body, early-final non-reuse, or a message without permitted persistence selects close deterministically through the outbound phase boundary. At `AcceptedPrivate`, replace the current private head with a revalidated head containing `Connection: close` before exposure. At `Frozen`, including first exposure with zero acknowledged bytes, never mutate the head; finish only its immutable current message when transport and framing permit, prohibit every successor, then close. `HeadCommitted` and `MessageCommitted` likewise prohibit successors and close after the current message's required completion; cancellation or unusable transport closes immediately without claiming completion. A client that receives an HTTP/1.0 response without valid keep-alive closes and emits no next request. Consume the exact HTTP/1.0-bound v0.56.0 `ValidatedConnectionOptions` only as input to this lifecycle; default-close is transport-lifecycle evidence only and never authorizes CONNECT, optimistic input, or refinement into `ReceivedValidatedCloseOption`. Rejected CONNECT retains the complete v0.73.0 exact 70-byte `UnsupportedHttp10ConnectDisposition` output/input/capacity/failure/action table.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Exhaust the role × received-request/response matrix for client, origin/server, proxy, and gateway, including invalid directions; assert proxy/gateway downstream request prohibition, distinct upstream candidates, correct default-close field generation by clients and response-generating roles, immediate prior-evidence invalidation on every newer received generation, and no pipelining. Cause persistence loss through peer omission/close, budget expiry, cancellation, incomplete body, framing/error, and every early-final disposition at `AcceptedPrivate`, `Frozen` with every head prefix including zero acknowledged, `HeadCommitted`, and `MessageCommitted`; prove only private heads are rewritten, exposed heads remain immutable, successors are sealed, current completion is exact when possible, unusable transport closes immediately, and a client never emits a next request after a non-keep-alive response. Replay rejected HTTP/1.0 CONNECT under every disposition and v0.73.0 error/action transition; require state-neutral invalid acknowledgement, valid-acknowledgement-first close selection, additional input wholly unconsumed, discard/close once, and no reparse/publication/resolution/forwarding or optimistic/HTTP/1.1 proof authority.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.0 default-close lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) still passes; no behavior assigned to v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 — Explicit HTTP/1.0 keep-alive extension profile

Status: planned

#### Goal

Deliver **Explicit HTTP/1.0 keep-alive extension profile** as the sole primary capability in this stop. It builds
on v0.74.0 (HTTP/1.0 default-close lifecycle) and must be independently trustworthy before v0.76.0 (Separate vef-http09 package and exact grammar) begins.

#### Deliverables

- Acceptance contract: Enable HTTP/1.0 keep-alive only through explicit policy and two-sided, per-hop evidence; never reparse `Connection`. Refine the exact HTTP/1.0-bound v0.56.0 `ValidatedConnectionOptions` plus matching current v0.74.0 `Http10PersistenceDisposition` into sealed received-peer evidence `ValidatedHttp10KeepAlive`. Independently generate `Connection: keep-alive` on the corresponding local HTTP/1.0 head and mint sealed non-Copy/non-Clone `CommittedHttp10KeepAliveHead` only when that exact request or response head reaches `HeadCommitted`; bind it to role, direction, hop, connection, exchange, and head generation. For a client or proxy-upstream response, ordering is mandatory: first correlate the response with the oldest matching v0.57.0 `HeadCommitted` request; move that exact request's `CommittedHttp10KeepAliveHead` into a sealed `CorrelatedHttp10KeepAliveRequest` owned by the response lifecycle; then revoke every other stale or unmatched local signal. Missing, duplicate, or generation-mismatched correlation closes as ambiguous before response publication or keep-alive refinement. The matched signal survives admission of its response and cannot be used by another response. An origin/server may generate and commit the response signal only after accepting the matching received-request candidate and proving self-delimited response framing. Positive HTTP/1.0 reuse framing is restricted to a semantically bodyless message or exact fixed-length Content-Length message at `MessageCommitted`. Transfer-Encoding, chunked coding, trailers, and HTTP/1.1 transfer semantics remain rejected by v0.73.0 and can mint no peer evidence, local signal, permit, or successor. A valid close-delimited HTTP/1.0 response may complete only by closure and can never preserve the connection or mint reuse authority.
- Maintain one engine-owned `Http10ReuseLedger { connection_generation, hop, configured_max, remaining }`, initialized once and monotonically non-increasing for that connection/hop. Immutable `configured_max` distinguishes a disabled extension from an exhausted allowance; mutable `remaining` means exactly the number of future successor admissions still authorized, excluding the currently active exchange. Store immutable `Http10LocalPersistenceMode::{Negotiable, LastUseMustClose}` in every active exchange. Configured zero installs `LastUseMustClose` for the initial exchange. If admission decrements one to zero, that successor is admitted and atomically receives `LastUseMustClose`; no server response must exist. For a client/proxy-upstream exchange, validate the exact successor command into sealed non-Copy/non-Clone `PendingHttp10SuccessorRequest`, bound to its method, target, ordered fields, framing, local persistence mode, connection/exchange/head generations, and exact serialized head plan. Validation rejects malformed syntax, illegal framing, semantic conflicts, and caller-supplied `Connection` values that conflict with mandatory close; close injection and output preflight finish before the command can enter a reservation or become visible. For an origin/server exchange, the mode survives request admission and the later response builder injects or validates close before exposure. If a local head already exists in `AcceptedPrivate`, apply the v0.74.0 rewrite and revalidation immediately; if no head exists, retain the mandatory-close mode until one is built. No builder under `LastUseMustClose` can create `CommittedHttp10KeepAliveHead`, regardless of peer signaling or a zero `reuse_remaining_snapshot`. Thus configured maximum one means exactly one successor whose local head eventually announces close, then no second permit.
- Define total reuse resolution after both lifecycles terminate over optional generation-bound evidence. Its fixed precedence remains correlation, policy, framing, configured-zero, exhausted ledger, missing negotiation, deadline arithmetic, then reuse. Record the result independently as `Http10ReuseResolutionRecord::{Reuse { provisional_permit: Http10ReusePermit }, ReuseRevokedByInterrupt { resolved: ResolvedHttp10ReuseIdentity }, Close { reason: Http10ReuseCloseReason }, SkippedByInterrupt}`. Only `Reuse` consumes both signals; `ReuseRevokedByInterrupt` destroys all permit/deadline authority while retaining non-authoritative identity for diagnostics. Every close reason remains reachable. Resolution never constructs Reusable. A proxy resolves each hop independently; received keep-alive evidence is never forwarded or rebound.
- `Http10TerminalDecision { reuse_resolution, terminal_interrupt: Option<Http10CompletionFirstCause> }` stores only the two independent facts. It has no final-state field, cache, constructor input, or mutable shadow authority. Its sealed `planned_final_state(&self) -> Http10PlannedFinalState` exhaustively matches both fields immediately before publication; `Http10PlannedFinalState::{PublishReuse, PublishClose}` is an ephemeral result, never retained authority, and only `Reuse { provisional_permit }` plus `None` returns `PublishReuse`. Every Close, SkippedByInterrupt, ReuseRevokedByInterrupt, or accepted interrupt returns `PublishClose`. A Close(NegotiationUnavailable) followed by TransportFailure retains both facts. An interrupt after successful resolution records ReuseRevokedByInterrupt rather than erasing success. Only final publication consumes that exhaustive result to construct the actual connection state.
- The role × direction matrix remains exact. `IntermediaryDownstreamClose` for a proxy or gateway received request can never refine. `OriginRequestCandidate` may refine only for the origin's downstream connection. `ClientUpstreamCandidate` may refine only for the client's server connection. `IntermediaryUpstreamCandidate` may refine only for the proxy/gateway upstream connection after a received response. `InvalidRoleDirection` never refines. Every allowed received path additionally requires recognized `keep-alive` with no winning `close`, explicit local support, self-delimited framing and completed message lifecycle, Content-Length where closure would otherwise delimit, remaining request-count/idle-time budget, and exact connection/message generations. After the correlation transfer above, admission of a newer received message atomically revokes the prior disposition, `ValidatedHttp10KeepAlive`, every unmatched committed-local signal, and any unrelated unconsumed reuse permit; the correlated signal owned by that exact response remains until pairing or terminal cleanup. Loss of persistence uses the exact v0.74.0 `AcceptedPrivate`/`Frozen`/`HeadCommitted`/`MessageCommitted` close boundary; never defer close signaling to a hypothetical successor. No HTTP/1.0 keep-alive path enables pipelining. These types authorize only their exact HTTP/1.0 per-hop lifecycle. They cannot construct `ReceivedValidatedCloseOption`, authorize optimistic CONNECT, bind HTTP/1.1 Upgrade, or substitute evidence across roles, directions, hops, versions, connections, exchanges, heads, or generations. HTTP/1.0 CONNECT retains the v0.73.0 typed rejection in every matrix cell.
- Define the sole successor-admission edge as `Http10ConnectionState::Reusable { permit: Http10ReusePermit } -> ActiveExchange { next_exchange_generation, completion_binding, reuse_remaining_snapshot, local_persistence_mode, admission_attempt_work_consumed }`. Its total result is `Http10SuccessorAdmissionOutcome::{Admitted, RejectedLocalCommand { reason: Http10LocalCommandReason }, RetryableCapacity { reason: Http10CapacityReason }, CloseLocal { reason }}`. Each call creates private `AdmissionAttempt<'command> { cursors: AdmissionProgressCursors, command: PhantomData<&'command Command> }`, binding every validation cursor to that exact borrowed command and call. `RejectedLocalCommand` covers invalid method/target/ordered fields, illegal framing, semantic invalidity, and conflicting caller `Connection`; `RetryableCapacity` remains capacity-only. Before either reason-only result returns, the attempt destroys every cursor and releases the command borrow. The permit/deadline/ledger/output/structural state remains in `Reusable`, but a retry always creates new zeroed cursors and recharges every repeated unit against the unchanged permit budget and non-resetting cumulative ledger, even if the caller reuses or mutates the same buffer. Cross-call progress retention is forbidden unless the engine owns an immutable exact command copy; this reason-only API intentionally retains no such copy.
- Store non-Copy `Http10AdmissionAttemptBudget { permit_generation, configured_max, remaining, consumed }` inside each provisional/published permit. Initialize it exactly once when the provisional permit is created, transfer it unchanged into `Reusable`, and never reset it across rejection or capacity retries. Also maintain engine-owned connection-lifetime `Http10AdmissionCumulativeLedger { connection_generation, configured_max, remaining, consumed }`, initialized once when the connection is created and never reset by a new permit. Preserve `configured_max == remaining + consumed` for each ledger with checked arithmetic.
- Define sealed granular `AdmissionWorkKind::{CommandBase, MethodByte, TargetByte, FieldEntry, FieldByte, FramingStep, SemanticRule, CloseInjectionByte, OutputPreflightByte, ReservationComponent}` and engine-only `AdmissionWorkChargeSpec { kind, units }`. The fixed schedule maps each kind to checked `(base_cost, per_unit_cost)` and derives `cost = base_cost + per_unit_cost * units`; callers can construct neither kind nor spec and select neither units nor cost. Unit derivation is itself O(1): it reads only attempt-local stored bounded lengths/counts and monotonic cursors, never traverses an iterator or scans bytes to discover a future charge. Access to each field entry is charged before that entry is inspected. Each bounded processing step selects `n` from stored metadata and charges `n`; it may process `0..=n` units and advances the attempt cursor exactly once by actual processed units, never planned units. Early rejection never refunds unprocessed charged units. A retry has new zeroed cursors and cannot reuse any prior attempt's work authority. No scan, field traversal, output byte, reservation component, unit-discovery traversal, or repeated retry may occur outside a charge.
- Atomic `try_charge_admission_work(spec) -> Result<AdmissionWorkPermit, AdmissionWorkChargeError>` retains errors `PermitBudgetExhausted`, `ConnectionBudgetExhausted`, `InvalidZeroCost`, `GenerationMismatch`, `LedgerInvariantFailure`, and `ArithmeticOverflow` with existing precedence/classification. It checks unit bounds and multiplication/addition before both ledgers, then mutates both or neither. Every error performs no governed work. Private non-Copy/non-Clone `AdmissionWorkPermit { kind, charged_units, cost, permit_generation, connection_generation, permit_consumed_after, connection_consumed_after, attempt_generation }` is an internal authorization capability, not protocol authority or diagnostics; exactly one governed step must consume it. That step alone calls checked `finish(processed_units) -> Result<AdmissionWorkReceipt, AdmissionWorkFinishError>`. For `processed_units <= charged_units`, it advances only its bound attempt cursor by `processed_units` and yields non-authoritative `AdmissionWorkReceipt { kind, charged_units, processed_units, cost, permit_generation, connection_generation, permit_consumed_after, connection_consumed_after }`. `AdmissionWorkFinishError::ProcessedUnitsExceeded` is a local security-invariant closure: it consumes the permit, advances no cursor, emits no receipt, and does not refund the already consumed charge. Unprocessed charged units remain consumed but grant no later work. A stale, cross-attempt, duplicated, or reused permit cannot inspect data, finish, advance a cursor, or produce a receipt. Successful admission transfers ledger totals without recharge; receipts never authorize work or state transitions.
- Before transition, transactionally assemble role-specific `Http10NextExchangeReservation::{Client { request: PendingHttp10SuccessorRequest, private_output, correlation, resources }, Server { parser, local_persistence_mode, correlation, resources }}`. Shared resources include records, parser/event/output leases, tentative count debit, parser reserve, deadline snapshot, checked exchange generation, and a checked non-wrapping completion generation. The reservation seals both into `Http10CompletionBinding { connection_generation, exchange_generation, completion_generation }`. The event lease covers the largest terminal event. Initial construction uses `Http10InitialExchangeReservation::{Client { request: PendingHttp10InitialRequest, private_output, resources }, Server { parser, resources }}` and reserves the identical slot and completion binding before initial Active publication, including configured-zero/default-close.
- Initial failure is role-total: Client retains no command borrow, accepts/exposes no request byte, leaves private output unchanged, and publishes no connection/exchange/completion generation; Server leaves input wholly unconsumed and likewise publishes no generation. Both release every tentative record, lease, count/work reservation, event slot, completion binding, and connection-ledger owner exactly once. Every reservation is all-or-nothing; completion-generation exhaustion fails before command/input acceptance or output exposure, and no Active state exists without its future completion binding. Cancellation or abandonment invalidates the reserved binding before slot reuse; a later occupant receives a distinct non-wrapping generation, so every stale binding remains neutral. One-short capacity preserves preexisting state apart from already atomically charged work. Successor construction also validates policy, deadline/binding, ledger count, and checked generations; terminal reasons close locally without peer blame.
- On `Admitted`, atomically consume the reservation and permit; commit only the tentative request/exchange-count debit; install records, leases, and the parser-work reserve; transfer the already-consumed admission-attempt total into `ActiveExchange { next_exchange_generation, completion_binding, reuse_remaining_snapshot, local_persistence_mode, admission_attempt_work_consumed }` without recommit or recharge; decrement the reuse ledger once; install generation/mode; then publish. Initial admission installs the same reserved binding. Capacity rollback retains the exact deadline and modified attempt budget but invalidates any abandoned reservation binding. No structural fallibility remains after publication.
- `ActiveExchange` exclusively owns its records/evidence/leases and the already-reserved `Http10CompletionBinding`. Entering Completing moves that binding infallibly; it performs no generation allocation. `Http10CompletingPhase::{Resolving, DecisionHeld { terminal_decision }, Reclaiming { terminal_decision, reclamation_state }, PublicationPending { publication }}` retains it in every phase. Define `Http10CompletionInterrupt { binding, cause: Http10CompletionInterruptCause }`, where causes are `IdleDeadlineReached { permit_generation, deadline_generation, observed_now }`, `PolicyRevoked { policy_generation }`, `TransportFailure { transport_generation, cause }`, `LocalClose { close_command_generation }`, and `Cancellation { cancellation_generation }`. Every cause must match the common binding before cause-specific evidence is inspected or latched. Stale/wrong-binding LocalClose, Cancellation, PolicyRevoked, deadline, and transport notifications are state-neutral during every phase, after final publication, after successor admission, and after reservation-slot reuse.
- The first exact valid interrupt is immutably latched in `Http10CompletionFirstCause`; same-call ties retain precedence TransportFailure, PolicyRevoked, IdleDeadlineReached, LocalClose, Cancellation. Exact deadline equality expires. In Resolving, an accepted interrupt records SkippedByInterrupt. In DecisionHeld/Reclaiming, Close reasons remain unchanged while the interrupt is added; Reuse is destroyed and becomes ReuseRevokedByInterrupt. PublicationPending updates the two fact records and its reserved event in place, then calls the exhaustive final-state method again; it stores no planned-state authority. Every phase remains capacity-infallible, never reruns resolution/reclamation, and cannot publish expired/revoked reuse.
- The combined-call fast path exists only when acknowledgement causes exact outbound HTTP/1.0 `MessageCommitted`: the final promised fixed-length body byte or semantically bodyless final head. Chunked/trailered and nonfinal records have no positive path. Same-call successor input remains wholly unconsumed throughout `Completing`; only an infallibly published `Reusable` may run role-specific admission. Invalid, zero, short, or nonfinal acknowledgement is `PrematureHttp10Successor`; close also leaves input unconsumed. Across resolution, pending-publication backpressure, immediate admission, cancellation, and repeated hooks there is at most one decision, permit, ledger decrement, terminal event/state publication, and successor publication. `ActiveExchange` never rolls back.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Test every work kind at zero, one, and maximum charged units; every actual processed count `0..=n` after charging `n`; maximum method/target/field bytes and field count; one-byte fragmentation; malformed/capacity retry; and all checked multiplication/addition/error boundaries. Use instrumented iterators that fail if traversed merely to derive units. Prove O(1) length/count/cursor derivation, charge-before-field-inspection, processed-not-planned cursor advancement, no refund or residual authority after early malformed bytes, and rejection of processed greater than charged, stale/cross-attempt/duplicated/reused work permits, and receipts used as authority. On every `RejectedLocalCommand` and `RetryableCapacity`, mutate every command byte before retry and prove the old borrow/cursors/permit cannot skip validation; new cursors start at zero and all repeated work is charged again against unchanged/non-resetting ledgers. Require cumulative ceilings and no quadratic/unpriced traversal.
- For both initial and successor reservations, test completion generation at maximum-minus-one, maximum, and exhaustion. Require exhaustion before command/input acceptance or output exposure, no Active state without its reserved binding, cancellation/abandonment invalidation, and stale neutrality after reservation-slot reuse. Cross every interrupt with exact and stale common bindings, every cause-specific generation, each phase, after publication, and after successor admission. Cross every resolution/interrupt pair and exhaustively assert that the non-stored `planned_final_state()` returns PublishReuse only for live Reuse plus None and PublishClose otherwise, including after every interrupt rewrite. Retain all initial-role ownership tests.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/1.0 keep-alive extension profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.74.0 (HTTP/1.0 default-close lifecycle) still passes; no behavior assigned to v0.76.0 (Separate vef-http09 package and exact grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 — Separate vef-http09 package and exact grammar

Status: planned

#### Goal

Deliver **Separate vef-http09 package and exact grammar** as the sole primary capability in this stop. It builds
on v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) and must be independently trustworthy before v0.77.0 (Explicit HTTP/0.9 client API) begins.

#### Deliverables

- Acceptance contract: The separate vef-http09 package accepts only GET SP nonempty request-target CRLF on a dedicated configured endpoint, rejects version tokens, fields, other methods, controls, fragments, and over-limit targets, emits no HTTP/1 types, and can never be entered through fallback from rejected HTTP/1 bytes.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Separate vef-http09 package and exact grammar and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-http09 package and exact grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) still passes; no behavior assigned to v0.77.0 (Explicit HTTP/0.9 client API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 — Explicit HTTP/0.9 client API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 client API** as the sole primary capability in this stop. It builds
on v0.76.0 (Separate vef-http09 package and exact grammar) and must be independently trustworthy before v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) begins.

#### Deliverables

- Acceptance contract: The explicit HTTP/0.9 client serializes GET SP target CRLF, treats all response octets as a borrowed body until clean EOF, has no status/field/trailer interpretation or persistence, and reports cancellation/transport failure separately from successful EOF completion.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 client API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 client API contract and all previously implemented relevant behavior have
reproducible evidence; v0.76.0 (Separate vef-http09 package and exact grammar) still passes; no behavior assigned to v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 — Explicit HTTP/0.9 server and dedicated-listener API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 server and dedicated-listener API** as the sole primary capability in this stop. It builds
on v0.77.0 (Explicit HTTP/0.9 client API) and must be independently trustworthy before v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) begins.

#### Deliverables

- Acceptance contract: The explicit HTTP/0.9 server exists only on a dedicated-listener policy, accepts one valid simple GET, sends raw response body bytes followed by close, processes no second request, and closes without HTTP/1 error serialization on invalid, ambiguous, or over-capacity input.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 server and dedicated-listener API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 server and dedicated-listener API contract and all previously implemented relevant behavior have
reproducible evidence; v0.77.0 (Explicit HTTP/0.9 client API) still passes; no behavior assigned to v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.78.0 implementation stop reached. Run pentest for this exact commit.`

### v0.79.0 — HTTP/0.9 cross-protocol rejection corpus

Status: planned

#### Goal

Deliver **HTTP/0.9 cross-protocol rejection corpus** as the sole primary capability in this stop. It builds
on v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) and must be independently trustworthy before v0.80.0 (HTTP/1 smuggling and ambiguity corpus) begins.

#### Deliverables

- Acceptance contract: The rejection corpus covers HTTP/1 versioned lines, PRI prefaces, TLS records, SSH/SMTP prefixes, control bytes, overlong targets, malformed CRLF, and split variants; every case is rejected without protocol fallback, response reflection, unbounded scan, or publication under both HTTP/0.9 and HTTP/1 entry points.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HTTP/0.9 cross-protocol rejection corpus and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/0.9 cross-protocol rejection corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) still passes; no behavior assigned to v0.80.0 (HTTP/1 smuggling and ambiguity corpus) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 — HTTP/1 smuggling and ambiguity corpus

Status: planned

#### Goal

Deliver **HTTP/1 smuggling and ambiguity corpus** as the sole primary capability in this stop. It builds
on v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) and must be independently trustworthy before v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: The smuggling corpus fixes expected framing and close outcomes for conflicting/duplicate Content-Length, TE/CL, repeated or non-final chunked, obs-fold, whitespace-before-colon, bare line endings, malformed chunks, Host ambiguity, and transition over-read across every split and intermediary role.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 smuggling and ambiguity corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) still passes; no behavior assigned to v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.80.0 implementation stop reached. Run pentest for this exact commit.`

### v0.81.0 — HTTP/1 and HTTP/0.9 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/0.9 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.80.0 (HTTP/1 smuggling and ambiguity corpus) and must be independently trustworthy before v0.82.0 (HPACK prefix-integer decoder) begins.

#### Deliverables

- Acceptance extension: Audit v0.75.0 as one causal product: initial/successor reservation of the future completion binding before Active publication; exact common binding plus cause evidence for every interrupt; independent reuse-resolution record and optional first interrupt with a non-stored exhaustive final-state method; command-borrow-bound per-call attempts whose cursors die before reason-only returns; and private linear work permits separated from diagnostic receipts. Treat cross-command cursor retention, retry without zeroed cursors/full recharge, receipt-as-authority, work without a permit, processed-over-charged progress, planned rather than actual cursor advancement, residual unused authority, stale/cross-attempt/reused permits, uncharged iterator traversal, or quadratic traversal as release-blocking.
- Acceptance contract: Close every applicable RFC 1945/6455/9110/9112/9931 requirement and erratum with a named passing test or recorded disposition, replay the HTTP/0.9 cross-protocol and HTTP/1 smuggling corpora against client/server/intermediary profiles, and block exit on divergent framing, publication, close, capacity, or bounded-work results. Audit the complete HTTP/1 causal product: the sole version-neutral `Connection` lexer; v0.74.0/v0.75.0 role × direction persistence matrix; two-sided per-hop signals and response-correlation-first transfer; configured-max/remaining ledger; delayed-role persistence mode; total exactly-once reuse resolution; validated client command and role-specific successor reservation; reason-only rejection/capacity with irreversible attempt work; permit-exclusive deadline; atomic completion event/state publication and terminal reclamation; checked generation exhaustion; bodyless/fixed-only same-call boundary; negative framing; cancellation/duplicate-hook serialization; and no pipelining. Also audit the HTTP/1 commitment/FIFO/100/early-final/disposition product, HTTP/1.1 CONNECT/Upgrade/WebSocket transitions, and v0.73.0 HTTP/1.0 local-capacity/start-line/414/431/400/501 precedence and fixed terminal action.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus. Replay the complete `Connection` corpus and HTTP/1.0 causal product. Cross initial/successor completion-generation exhaustion, cancellation, abandonment, and slot reuse; common/cause bindings in every phase and after publication/successor; every resolution/interrupt pair through the exhaustive final-state method; and every charged `n` with actual progress `0..=n`, instrumented iterators, maximum fields/bytes, one-byte fragmentation, early malformed bytes, retries/rescans, command mutation, and arithmetic boundaries. Require per-call cursor destruction, zeroed/full-charge retry, work-permit consumption, receipt non-authority, actual-progress cursor movement, no residual unused authority, stale/cross-attempt/reuse rejection, bounded linear work, and one reclamation/publication. Preserve all earlier HTTP/1 lifecycle, transition, and rejection corpora.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 and HTTP/0.9 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.80.0 (HTTP/1 smuggling and ambiguity corpus) still passes; no behavior assigned to v0.82.0 (HPACK prefix-integer decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.81.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 3 — HPACK and HTTP/2

Phase contract: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.

### v0.82.0 — HPACK prefix-integer decoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer decoder** as the sole primary capability in this stop. It builds
on v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) and must be independently trustworthy before v0.83.0 (HPACK prefix-integer encoder) begins.

#### Deliverables

- Acceptance contract: Accept every RFC 7541-valid prefix integer representation, including non-shortest encodings, while rejecting checked overflow and truncation with exact incremental progress; decoding never invents a canonicality error that the RFC does not define.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) still passes; no behavior assigned to v0.83.0 (HPACK prefix-integer encoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 — HPACK prefix-integer encoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer encoder** as the sole primary capability in this stop. It builds
on v0.82.0 (HPACK prefix-integer decoder) and must be independently trustworthy before v0.84.0 (HPACK integer overflow and canonical encoder proofs) begins.

#### Deliverables

- Acceptance contract: Emit the shortest RFC 7541 prefix-integer representation for every accepted value under partial output, with checked size preflight and no state advancement before bytes commit.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.82.0 (HPACK prefix-integer decoder) still passes; no behavior assigned to v0.84.0 (HPACK integer overflow and canonical encoder proofs) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 — HPACK integer overflow and canonical encoder proofs

Status: planned

#### Goal

Deliver **HPACK integer overflow and canonical encoder proofs** as the sole primary capability in this stop. It builds
on v0.83.0 (HPACK prefix-integer encoder) and must be independently trustworthy before v0.85.0 (HPACK string representation codec) begins.

#### Deliverables

- Acceptance contract: Prove the decoder accepts every in-range RFC representation and rejects only overflow or truncation, while the encoder emits one shortest representation; cover every prefix width, continuation boundary, maximal value, excessive continuation chain, and one-byte output split.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK integer overflow and canonical encoder proofs contract and all previously implemented relevant behavior have
reproducible evidence; v0.83.0 (HPACK prefix-integer encoder) still passes; no behavior assigned to v0.85.0 (HPACK string representation codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 — HPACK string representation codec

Status: planned

#### Goal

Deliver **HPACK string representation codec** as the sole primary capability in this stop. It builds
on v0.84.0 (HPACK integer overflow and canonical encoder proofs) and must be independently trustworthy before v0.86.0 (HPACK Huffman tables) begins.

#### Deliverables

- Acceptance contract: Decode the Huffman flag and seven-bit-prefixed string length incrementally, accept raw or RFC Huffman payload of exactly that encoded length, cap encoded bytes, decoded bytes, and work before output, reject truncated/invalid Huffman as COMPRESSION_ERROR, and publish the string only after complete validation and capacity preflight.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK string representation codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.84.0 (HPACK integer overflow and canonical encoder proofs) still passes; no behavior assigned to v0.86.0 (HPACK Huffman tables) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 — HPACK Huffman tables

Status: planned

#### Goal

Deliver **HPACK Huffman tables** as the sole primary capability in this stop. It builds
on v0.85.0 (HPACK string representation codec) and must be independently trustworthy before v0.87.0 (HPACK Huffman decoder) begins.

#### Deliverables

- Acceptance contract: Store exactly the 257 RFC 7541 Appendix B symbol codes and bit lengths, verify every constant against the locked source at build/test time, decode all 256 octets plus EOS-prefix padding vectors, and reject duplicate/prefix-conflicting table entries or any generated decoder state that can accept EOS as data.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman tables contract and all previously implemented relevant behavior have
reproducible evidence; v0.85.0 (HPACK string representation codec) still passes; no behavior assigned to v0.87.0 (HPACK Huffman decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 — HPACK Huffman decoder

Status: planned

#### Goal

Deliver **HPACK Huffman decoder** as the sole primary capability in this stop. It builds
on v0.86.0 (HPACK Huffman tables) and must be independently trustworthy before v0.88.0 (HPACK Huffman encoder) begins.

#### Deliverables

- Acceptance contract: Reject the EOS symbol as data, padding longer than seven bits, and terminal padding that is not the high-order bits of EOS; accept every valid split without over-read, cap decode work/output, and classify every malformed Huffman string as a compression error.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.86.0 (HPACK Huffman tables) still passes; no behavior assigned to v0.88.0 (HPACK Huffman encoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 — HPACK Huffman encoder

Status: planned

#### Goal

Deliver **HPACK Huffman encoder** as the sole primary capability in this stop. It builds
on v0.87.0 (HPACK Huffman decoder) and must be independently trustworthy before v0.89.0 (HPACK static table) begins.

#### Deliverables

- Acceptance contract: Encode each input octet with its exact Appendix B code, concatenate most-significant bits, pad the final byte with at most seven one bits, never emit EOS, preflight worst-case output/work, and resume partial output by bit/byte offset without changing or duplicating committed bytes.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.87.0 (HPACK Huffman decoder) still passes; no behavior assigned to v0.89.0 (HPACK static table) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 — HPACK static table

Status: planned

#### Goal

Deliver **HPACK static table** as the sole primary capability in this stop. It builds
on v0.88.0 (HPACK Huffman encoder) and must be independently trustworthy before v0.90.0 (HPACK dynamic table storage) begins.

#### Deliverables

- Acceptance contract: Provide exactly the 61 RFC 7541 static entries at one-based indices 1..=61 in normative order, reject index zero/out-of-range access without mutation, preserve empty values where specified, and test every index in both lookup directions including duplicate-name selection.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK static table contract and all previously implemented relevant behavior have
reproducible evidence; v0.88.0 (HPACK Huffman encoder) still passes; no behavior assigned to v0.90.0 (HPACK dynamic table storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 — HPACK dynamic table storage

Status: planned

#### Goal

Deliver **HPACK dynamic table storage** as the sole primary capability in this stop. It builds
on v0.89.0 (HPACK static table) and must be independently trustworthy before v0.91.0 (HPACK eviction and oversize-entry behavior) begins.

#### Deliverables

- Acceptance contract: Index dynamic entries newest-first immediately after the 61 static entries, account each as name length plus value length plus 32 with checked arithmetic, store exact insertion order in exclusive caller-provided encoder/decoder arenas, and make lookup/index numbering deterministic across wrap, eviction, and every table-size setting. Derive `physical_capacity: usize` as the safely representable HPACK logical byte capacity after checked ring metadata/alignment/entry overhead, never as the raw slice length or a peer-advertised value; reject an unusable layout as typed local capacity before mutation.
- Decoder consumers never borrow name/value bytes from a dynamic-table slot beyond the lookup operation. Any decoded field that outlives that operation is materialized into independent fixed output storage or a stable generation-checked lease whose lifetime pins its own bytes, not the table entry; later eviction, overwrite, or size reduction cannot mutate prior decoded output or change HPACK index/eviction behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Cross zero/small/exact/one-byte-short/maximum caller arenas, metadata and entry
  overhead, wrap, checked conversion, and separate encoder/decoder storage;
  prove the published physical capacity never exceeds representable storage.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK dynamic table storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.89.0 (HPACK static table) still passes; no behavior assigned to v0.91.0 (HPACK eviction and oversize-entry behavior) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.90.0 implementation stop reached. Run pentest for this exact commit.`

### v0.91.0 — HPACK eviction and oversize-entry behavior

Status: planned

#### Goal

Deliver **HPACK eviction and oversize-entry behavior** as the sole primary capability in this stop. It builds
on v0.90.0 (HPACK dynamic table storage) and must be independently trustworthy before v0.92.0 (HPACK table-size update and SETTINGS coupling) begins.

#### Deliverables

- Acceptance contract: Before insertion evict oldest entries until the new entry fits; if its size exceeds the selected capacity, empty the table and do not insert it; a selected capacity of zero clears all entries. A selected-capacity reduction and every required eviction form one atomic transition: failure cannot leave partial bytes, provenance, size totals, index order, or limit state out of sync, and no physical eviction may occur without a matching selected-capacity update obligation for the encoder wire state introduced at v0.92.0/v0.98.0.
- Test eviction, wrap, overwrite, and maximum-size reduction immediately after a lookup that contributes part or all of a decoded field; prove the independently materialized output remains byte-identical and no stale table lease exists.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Cross selected limits 0, exact current size, one below, physical maximum, and
  oversized entries; prove clamp/eviction atomicity and independent decoded
  output, while the later update-obligation hook cannot be omitted.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK eviction and oversize-entry behavior contract and all previously implemented relevant behavior have
reproducible evidence; v0.90.0 (HPACK dynamic table storage) still passes; no behavior assigned to v0.92.0 (HPACK table-size update and SETTINGS coupling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 — HPACK table-size update and SETTINGS coupling

Status: planned

#### Goal

Deliver **HPACK table-size update and SETTINGS coupling** as the sole primary capability in this stop. It builds
on v0.91.0 (HPACK eviction and oversize-entry behavior) and must be independently trustworthy before v0.93.0 (HPACK caller-owned ring lookup) begins.

#### Deliverables

- Acceptance contract: Define `EncoderTableLimits { peer_received_ceiling: u32, peer_wire_acknowledged_ceiling: u32, selected_capacity: u32, physical_capacity: usize }`, initialized for HTTP/2 with both peer ceilings at 4096 and selected capacity chosen by local policy no higher than the checked profile/storage limit. Maintain `selected_capacity <= peer_received_ceiling`, checked `usize::try_from(selected_capacity) <= physical_capacity`, and the active resource-profile cap; any local increase additionally requires `selected_capacity <= peer_wire_acknowledged_ceiling`. A peer reduction below selected atomically clamps selection, evicts immediately, and creates a matching selected-capacity update obligation whose wire exposure remains ACK-gated; a peer increase changes only `peer_received_ceiling` and never enlarges selection. A local policy reduction creates an update obligation without SETTINGS; a local increase is allowed only within the received, wire-acknowledged, profile, and physical minimum. If initial selected capacity is below 4096, initialize an obligation so the first field block communicates the reduction. Encoder update history contains selected-capacity changes only, never raw peer-ceiling changes. Apply decoder size updates only at field-block start and within VEF's safely advertised limit. Derive decoder advertised SETTINGS_HEADER_TABLE_SIZE no higher than checked caller storage/profile capacity; because the peer may initially encode against 4096 before processing a reduction, HTTP/2 activation requires a safely representable initial decoder state rather than overstating a smaller arena. For multiple selected-limit changes between field blocks, emit at most two updates—the smallest selected value followed by the final selected value—before the next representation, with table mutation tied to committed output bytes. v0.108.0 stores frame snapshots, v0.124.0 applies peer transitions, and v0.139.0 advances the wire-acknowledged ceiling.
- Attach every locally advertised decoder HEADER_TABLE_SIZE value and its
  checked physical/profile proof to the v0.139.0 outbound SETTINGS commit plan.
  Reservation or partial exposure changes no advertised decoder capacity; full
  frame acknowledgement alone activates the frozen local advertisement, while
  peer ACK merely confirms it and does not apply it again.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Cross physical/profile capacities below/equal/above 4096, peer ceilings 0,
  4096, and `u32::MAX`, local reductions/increases without SETTINGS, increases
  awaiting ACK, and initial selected capacity below 4096. Prove all four limit
  inequalities, no automatic selection increase, safe decoder advertisement,
  and no eviction without a selected-capacity update obligation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK table-size update and SETTINGS coupling contract and all previously implemented relevant behavior have
reproducible evidence; v0.91.0 (HPACK eviction and oversize-entry behavior) still passes; no behavior assigned to v0.93.0 (HPACK caller-owned ring lookup) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 — HPACK caller-owned ring lookup

Status: planned

#### Goal

Deliver **HPACK caller-owned ring lookup** as the sole primary capability in this stop. It builds
on v0.92.0 (HPACK table-size update and SETTINGS coupling) and must be independently trustworthy before v0.94.0 (HPACK indexed representation) begins.

#### Deliverables

- Acceptance contract: Resolve the combined static/dynamic index space with checked generation and ring arithmetic; index zero and every reference beyond the combined table are compression errors, and failed lookup publishes no field or partial table mutation.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK caller-owned ring lookup contract and all previously implemented relevant behavior have
reproducible evidence; v0.92.0 (HPACK table-size update and SETTINGS coupling) still passes; no behavior assigned to v0.94.0 (HPACK indexed representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 — HPACK indexed representation

Status: planned

#### Goal

Deliver **HPACK indexed representation** as the sole primary capability in this stop. It builds
on v0.93.0 (HPACK caller-owned ring lookup) and must be independently trustworthy before v0.95.0 (HPACK incremental-indexing literal) begins.

#### Deliverables

- Acceptance contract: Decode an indexed field from the one-bit pattern and seven-bit prefix, require a nonzero index within the current combined table, return the exact referenced name/value without table mutation, and map zero, stale, or out-of-range indices to connection COMPRESSION_ERROR before field publication.
- Copy or independently lease the resolved name/value into the unpublished decoded-section sink before the table lookup can be invalidated. Preserve its exact boundary and order; an indexed representation never leaves a semantic span pointing into static/dynamic lookup scratch, caller input, or an evictable ring entry.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK indexed representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.93.0 (HPACK caller-owned ring lookup) still passes; no behavior assigned to v0.95.0 (HPACK incremental-indexing literal) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 — HPACK incremental-indexing literal

Status: planned

#### Goal

Deliver **HPACK incremental-indexing literal** as the sole primary capability in this stop. It builds
on v0.94.0 (HPACK indexed representation) and must be independently trustworthy before v0.96.0 (HPACK non-indexing and never-indexed literal) begins.

#### Deliverables

- Acceptance contract: Decode the 01 incremental-indexing representation with a six-bit name index or bounded literal name followed by a bounded literal value; validate the full representation and insertion capacity, then insert exactly once in wire order even if later HTTP semantics reject the field, with no field publication before block completion.
- Materialize literal and indexed-name output into the same independent decoded-section sink before input/scratch reuse. Dynamic-table insertion and later eviction are compression-state actions only and cannot become semantic storage or invalidate an already decoded field.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK incremental-indexing literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.94.0 (HPACK indexed representation) still passes; no behavior assigned to v0.96.0 (HPACK non-indexing and never-indexed literal) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 — HPACK non-indexing and never-indexed literal

Status: planned

#### Goal

Deliver **HPACK non-indexing and never-indexed literal** as the sole primary capability in this stop. It builds
on v0.95.0 (HPACK incremental-indexing literal) and must be independently trustworthy before v0.97.0 (Sensitive-field indexing policy) begins.

#### Deliverables

- Acceptance contract: Decode 0000 without-indexing and 0001 never-indexed forms with four-bit name indices or literal names, never mutate the dynamic table, preserve the never-indexed directive through intermediary APIs, and reject invalid indices/strings as COMPRESSION_ERROR before any field becomes visible.
- Preserve the exact WithoutIndexing/NeverIndexed provenance beside the independently owned decoded field boundary through the unpublished section handoff; no later semantic stage may reconstruct it from encoded bytes or mutable compression state.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK non-indexing and never-indexed literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.95.0 (HPACK incremental-indexing literal) still passes; no behavior assigned to v0.97.0 (Sensitive-field indexing policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.96.0 implementation stop reached. Run pentest for this exact commit.`

### v0.97.0 — Sensitive-field indexing policy

Status: planned

#### Goal

Deliver **Sensitive-field indexing policy** as the sole primary capability in this stop. It builds
on v0.96.0 (HPACK non-indexing and never-indexed literal) and must be independently trustworthy before v0.98.0 (HPACK encoder output commit and indexing policy) begins.

#### Deliverables

- Acceptance contract: Represent typed Index, WithoutIndexing, and NeverIndexed directives plus a caller-supplied generation-safe CompressionPrincipal provenance token; keep provenance as encoder-only sidecar metadata that never changes HPACK entry size, insertion order, eviction, or index numbering, so skipped cross-principal entries still occupy their normal indices; tag each insertion immutably as principal-owned or explicitly public, remove its provenance atomically on eviction/reset, and never relabel a private entry public because another principal produces equal bytes; prohibit encoder lookup across principals and default unknown provenance to WithoutIndexing or NeverIndexed; default credentials, Authorization, Proxy-Authorization, Proxy-Authenticate, Proxy-Authentication-Info, cookies, and caller-marked secrets to enforced NeverIndexed/redacted handling; never let an intermediary downgrade a received never-indexed representation to indexed; prohibit indexing decisions based on secret-value comparisons with attacker-controlled values; redact sensitive values from diagnostics; and reject caller overrides that weaken the active security profile.
- Bind decoded sensitivity/redaction and received never-indexed provenance immutably to each ordered decoded-field boundary. That metadata follows the field bytes through semantic validation and abort/failure cleanup without exposing raw sensitive names/values; caller-owned sensitive storage remains subject to the existing caller-scrub contract after its lease ends.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every directive/default/override combination, every origin/proxy
  credential/challenge/info field, intermediary forwarding of never-indexed
  fields, diagnostic redaction, and decision traces proving that
  attacker-controlled equality does not influence secret indexing.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sensitive-field indexing policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.96.0 (HPACK non-indexing and never-indexed literal) still passes; no behavior assigned to v0.98.0 (HPACK encoder output commit and indexing policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 — HPACK encoder output commit and indexing policy

Status: planned

#### Goal

Deliver **HPACK encoder output commit and indexing policy** as the sole primary capability in this stop. It builds
on v0.97.0 (Sensitive-field indexing policy) and must be independently trustworthy before v0.99.0 (Independent HPACK decode limits) begins.

#### Deliverables

- Acceptance contract: Encode each field block under one bounded provisional `HpackEncoderTransaction`; table-size updates start the block, lookup/indexing/sensitive overrides are deterministic, and complete block-size/storage preflight occurs before output. Maintain a separate linear `EncoderTableUpdateDebt { smallest_since_last_exposed_block: u32, final_value: u32 }` for every selected-capacity change not yet transferred to exposed wire output; raw `peer_received_ceiling` or `peer_wire_acknowledged_ceiling` changes never enter debt unless they actually clamp selection. Initialize debt when selected capacity starts below the protocol default 4096, and let local policy reductions/increases merge without requiring a SETTINGS frame after v0.92.0 validates their bounds. A new selected change retains the minimum of every selected value since the last exposed field block and the most recent selected final value. Private encoding obtains one non-Copy/non-Clone `EncoderTableUpdateDebtLease`, writes its exact one-update or smallest-then-final prefix, and does not clear connection history; rollback/capacity/cancellation restores the identical lease before any newer selected change merges. A later framing owner clears connection debt only by atomically transferring the lease at first non-empty block exposure to output guaranteed to finish, never at encoding or acknowledgement of an unrelated control frame. Here `HpackCommitted` means publication of the whole transaction after its owner confirms complete field-block acknowledgement, not the later HTTP/2 `FramingCommitted` state created by first frame exposure. No later field block encodes against provisional mutations, NeedOutput/retry cannot double-insert, and connection abandonment discards the transaction with its compression context. v0.137.0 binds debt transfer to first initial-frame exposure and owner confirmation to full acknowledgement of the frame carrying END_HEADERS.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Prove rollback/capacity/cancellation restores the identical lease before any newer change merges.
- Prove no published table mutation before whole-block `HpackCommitted`, no double insert after NeedOutput, exact Private debt lease/rollback, minimum/final preservation for selected 0→4096 and 4096→0→4096 before exposure, initial-below-4096 debt, local-policy debt without SETTINGS, zero debt for ceiling-only increases, serialized ownership, no debt clearing at private encoding, correct cancellation/partial-output/abandonment state, legal ordering, bounded preflight, and bounded indexing cost.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK encoder output commit and indexing policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.97.0 (Sensitive-field indexing policy) still passes; no behavior assigned to v0.99.0 (Independent HPACK decode limits) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 — Independent HPACK decode limits

Status: planned

#### Goal

Deliver **Independent HPACK decode limits** as the sole primary capability in this stop. It builds
on v0.98.0 (HPACK encoder output commit and indexing policy) and must be independently trustworthy before v0.100.0 (HPACK synchronization, publication barrier, and error scope) begins.

#### Deliverables

- Acceptance contract: Enforce independent ceilings for encoded header-block bytes, decoded bytes, field count, individual name/value length, Huffman decode work, dynamic-table memory, compression ratio, compression workspace, and immutable semantic field-section storage; classify peer compression violations separately from caller-capacity exhaustion and publish no partial field section when any limit wins. Preflight semantic-section capacity independently from encoded-fragment/Huffman/integer scratch and the dynamic table. A one-byte shortage cannot truncate, partially validate, or publish; after any committed decoder-table mutation, continue bounded synchronization in discard mode and take typed bounded connection shutdown rather than handing semantics an incomplete section.
- Define the eventual v0.123.0 storage split now: `CompressionWorkspace` owns encoded fragments, integer/Huffman scratch, and CONTINUATION assembly state; `TerminalFieldSection` owns immutable decoded name/value bytes, ordered boundaries, pseudo/ordinary classification, sensitivity/never-index provenance, and generation/stream binding. Fixed caller-provided storage must remain exclusively leased until terminal disposition; no caller buffer can be recycled while a semantic span refers to it.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Independent HPACK decode limits and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HPACK decode limits contract and all previously implemented relevant behavior have
reproducible evidence; v0.98.0 (HPACK encoder output commit and indexing policy) still passes; no behavior assigned to v0.100.0 (HPACK synchronization, publication barrier, and error scope) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 — HPACK synchronization, publication barrier, and error scope

Status: planned

#### Goal

Deliver **HPACK synchronization, publication barrier, and error scope** as the sole primary capability in this stop. It builds
on v0.99.0 (Independent HPACK decode limits) and must be independently trustworthy before v0.101.0 (HPACK conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Commit valid compression-table updates even when later semantic validation rejects a stream; withhold the complete independently owned decoded section until validation, make compression errors connection-fatal, never roll back connection compression state for stream errors, and close when limits prevent safe completion. No semantic consumer reparses encoded HPACK or reconstructs fields from mutable table/scratch state. Atomic completion yields either one exact ordered section with duplicates, empty values, sensitivity and never-index provenance intact, or no section plus the typed bounded shutdown/error path.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work. Decode fields wholly/partly from dynamic references, then immediately evict, overwrite, or reduce table size; vary exact and one-byte-short section storage, duplicate/empty fields, sensitive/never-indexed metadata, caller-buffer reuse attempts, and every input split. Prove exact independent output or no output, unchanged table semantics, redacted failures, and no stale alias.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK synchronization, publication barrier, and error scope contract and all previously implemented relevant behavior have
reproducible evidence; v0.99.0 (Independent HPACK decode limits) still passes; no behavior assigned to v0.101.0 (HPACK conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 — HPACK conformance audit and pentest

Status: planned

#### Goal

Deliver **HPACK conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.100.0 (HPACK synchronization, publication barrier, and error scope) and must be independently trustworthy before v0.102.0 (HTTP/2 client and server prefaces) begins.

#### Deliverables

- Acceptance contract: Run every RFC 7541 request/response example, integer/string/Huffman/table vector, all-byte-split case, table-size transition, malformed index/EOS/padding case, and at least two independent implementation transcripts under all resource profiles; require identical headers, table snapshots, error scope, and bounded work before the HPACK pentest exit.
- Include decoded-section ownership in the HPACK audit/pentest: dynamic/static/literal mixtures followed by immediate eviction/overwrite/size reduction, exact and one-byte-short independent section storage, duplicate/empty fields, sensitivity/never-index provenance, caller-buffer reuse attempts, and discard-mode synchronization after table mutation. Require exact immutable output or no output plus bounded shutdown, with no stale alias, partial section, metadata loss, or diagnostic exposure.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Prove no table mutation before committed representation bytes, no double insert after NeedOutput, correct cancellation/partial-output state, legal table-size-update ordering, bounded preflight, and bounded indexing cost.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.100.0 (HPACK synchronization, publication barrier, and error scope) still passes; no behavior assigned to v0.102.0 (HTTP/2 client and server prefaces) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 — HTTP/2 client and server prefaces

Status: planned

#### Goal

Deliver **HTTP/2 client and server prefaces** as the sole primary capability in this stop. It builds
on v0.101.0 (HPACK conformance audit and pentest) and must be independently trustworthy before v0.103.0 (HTTP/2 frame-header codec) begins.

#### Deliverables

- Acceptance contract: A server consumes exactly the 24-byte client connection preface before frames and treats mismatch as connection PROTOCOL_ERROR; both endpoints send SETTINGS as their first frame, a client validates the server's first frame as non-ACK SETTINGS, and partial preface/SETTINGS input publishes no stream or application event.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 client and server prefaces contract and all previously implemented relevant behavior have
reproducible evidence; v0.101.0 (HPACK conformance audit and pentest) still passes; no behavior assigned to v0.103.0 (HTTP/2 frame-header codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 — HTTP/2 frame-header codec

Status: planned

#### Goal

Deliver **HTTP/2 frame-header codec** as the sole primary capability in this stop. It builds
on v0.102.0 (HTTP/2 client and server prefaces) and must be independently trustworthy before v0.104.0 (DATA frame codec) begins.

#### Deliverables

- Acceptance contract: Decode the 24-bit payload length, type, flags, reserved stream bit, and 31-bit stream identifier incrementally; ignore the received reserved bit but never expose it as an identifier bit, emit reserved bits as zero, reject payload lengths above the local effective advertised receive limit (initially 16,384) as connection FRAME_SIZE_ERROR before payload publication, retain the absolute RFC ceiling of 16,777,215, and preserve unknown flags for frame-specific ignore rules.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 frame-header codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.102.0 (HTTP/2 client and server prefaces) still passes; no behavior assigned to v0.104.0 (DATA frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.103.0 implementation stop reached. Run pentest for this exact commit.`

### v0.104.0 — DATA frame codec

Status: planned

#### Goal

Deliver **DATA frame codec** as the sole primary capability in this stop. It builds
on v0.103.0 (HTTP/2 frame-header codec) and must be independently trustworthy before v0.105.0 (HEADERS frame codec) begins.

#### Deliverables

- Acceptance contract: Require a nonzero stream; recognize END_STREAM and PADDED while ignoring unknown flags; validate Pad Length before exposing a fragment, subtract Pad Length and padding without underflow, and require the remaining payload to contain application data of length zero or greater; count the entire payload, including Pad Length and padding, for flow control but only exposed data for Content-Length; emit reserved bits and generated padding bytes as zero; map stream zero or invalid padding to connection PROTOCOL_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The DATA frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.103.0 (HTTP/2 frame-header codec) still passes; no behavior assigned to v0.105.0 (HEADERS frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 — HEADERS frame codec

Status: planned

#### Goal

Deliver **HEADERS frame codec** as the sole primary capability in this stop. It builds
on v0.104.0 (DATA frame codec) and must be independently trustworthy before v0.106.0 (CONTINUATION frame codec) begins.

#### Deliverables

- Acceptance contract: Require a nonzero stream; recognize END_STREAM, END_HEADERS, PADDED, and PRIORITY while ignoring unknown flags; validate padding before exposing the header fragment, map padding length equal to or greater than the remaining payload to connection PROTOCOL_ERROR, require five bytes for PRIORITY fields after any Pad Length byte and map an undersized priority layout to connection FRAME_SIZE_ERROR, subtract every optional field without underflow, reject self-dependency as stream PROTOCOL_ERROR, emit reserved bits and generated padding bytes as zero, and map stream zero to connection PROTOCOL_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEADERS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.104.0 (DATA frame codec) still passes; no behavior assigned to v0.106.0 (CONTINUATION frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 — CONTINUATION frame codec

Status: planned

#### Goal

Deliver **CONTINUATION frame codec** as the sole primary capability in this stop. It builds
on v0.105.0 (HEADERS frame codec) and must be independently trustworthy before v0.107.0 (SETTINGS frame codec) begins.

#### Deliverables

- Acceptance contract: Require a nonzero stream, recognize only END_HEADERS while ignoring unknown flags, expose the full payload as a header fragment with no padding fields, emit reserved bits as zero, and map stream zero to connection PROTOCOL_ERROR; sequencing and wrong-stream continuation remain connection-fatal in the later legality milestone.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.105.0 (HEADERS frame codec) still passes; no behavior assigned to v0.107.0 (SETTINGS frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 — SETTINGS frame codec

Status: planned

#### Goal

Deliver **SETTINGS frame codec** as the sole primary capability in this stop. It builds
on v0.106.0 (CONTINUATION frame codec) and must be independently trustworthy before v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) begins.

#### Deliverables

- Acceptance contract: Require stream zero, payload length divisible by six, and zero payload length when ACK is set; recognize ACK while ignoring unknown flags, emit reserved bits as zero, and map a nonzero stream to connection PROTOCOL_ERROR and invalid length to connection FRAME_SIZE_ERROR before any setting is published.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.106.0 (CONTINUATION frame codec) still passes; no behavior assigned to v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 — SETTINGS syntax, role, directional values, and ACK rules

Status: planned

#### Goal

Deliver **SETTINGS syntax, role, directional values, and ACK rules** as the sole primary capability in this stop. It builds
on v0.107.0 (SETTINGS frame codec) and must be independently trustworthy before v0.109.0 (PING frame codec) begins.

#### Deliverables

- Acceptance contract: Validate SETTINGS syntax, role/direction, known values, unknown identifiers, duplicate ordering, empty ACK payloads, and pending versus acknowledged local values; store peer advertisements without touching stream, window, encoder, admission, or scheduler state that does not yet exist. Preserve every ordered HEADER_TABLE_SIZE value and the frame-final received-ceiling snapshot separately from any later selected-capacity delta; an increase is never evidence that local selection grew. Validate any locally emitted decoder HEADER_TABLE_SIZE against a predeclared safely representable decoder capacity and never advertise raw caller-slice length; HTTP/2 activation cannot claim a sub-4096 initial decoder capacity safe merely because a reduction is queued. For each complete non-ACK frame, first validate every ordered entry with zero component mutation, then atomically reserve exactly one connection-owned `InboundSettingsTransaction { frame_generation, ordered_entries: SettingsEntryLease, ack: ReservedSettingsAck, pending_participants: SettingsParticipantSet, disposition: SettingsDisposition }`. Define `SettingsDisposition::{WaitingParticipants, AckEligible, AckFrozen { acknowledged: 0..=8 }, AckCommitted, AbortedConnection}`; this stop establishes that participant effectiveness only reaches AckEligible, while later output milestones alone may freeze and commit the exact nine-byte ACK. The single ACK belongs to the complete frame regardless of entry count, duplicates, unknowns, or later participating subsystems. Process its entries in wire order without intervening frame dispatch; enabled components attach generation-bound participant obligations to the same transaction. Maintain transactions and ACK disposition in received-frame FIFO order and retain the owner until AckCommitted or AbortedConnection. A connection-fatal validation result creates no transaction or ACK and selects the exact connection error; a later participant failure selects AbortedConnection, cancels that transaction's unexposed ACK, prevents every component from emitting it independently, and commits the exact error/GOAWAY path. ACK-slot/transaction-capacity exhaustion before mutation selects typed bounded connection shutdown with no partial setting effect.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cross empty/single/multi/duplicate/unknown/invalid entries, HEADER_TABLE_SIZE 0/4096/`u32::MAX`, local advertised decoder capacity, ACK flag/payload errors, transaction/ACK capacity, generation reuse, and multiple received frames; prove complete prevalidation, exact per-frame received-ceiling snapshots without selected-capacity inference, safe decoder advertisement, one ACK owner per frame, wire-order/FIFO readiness, zero mutation on failure, and no inference that AckEligible means AckCommitted.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS syntax, role, directional values, and ACK rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.107.0 (SETTINGS frame codec) still passes; no behavior assigned to v0.109.0 (PING frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 — PING frame codec

Status: planned

#### Goal

Deliver **PING frame codec** as the sole primary capability in this stop. It builds
on v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) and must be independently trustworthy before v0.110.0 (GOAWAY frame codec) begins.

#### Deliverables

- Acceptance contract: Require stream zero and exactly eight payload bytes, recognize ACK while ignoring unknown flags, preserve the opaque bytes exactly, emit reserved bits as zero, and map a nonzero stream to connection PROTOCOL_ERROR or a non-eight-byte payload to connection FRAME_SIZE_ERROR. After syntax and capacity preflight, every non-ACK PING copies its payload into a distinct bounded FIFO `InboundPingTransaction` before caller input is released; ACK-bearing PINGs create no reply transaction. Identical payloads remain separate one-for-one RFC obligations and cannot be coalesced or deduplicated. Define the exact 17-byte ACK encoding and `PingAckOutput::{ReservedPrivate { transaction_generation, opaque: [u8; 8] }, Frozen { transaction_generation, frame: [u8; 17], acknowledged: 0..=16 }, Complete}` for later scheduler/reserved-output activation. At this codec stop, missing caller capacity returns typed `PingReplyCapacity` without accepting a transaction or retaining input; v0.150.0 maps that condition on an active connection to bounded shutdown, and v0.153.0 activates partial ACK output.
- Locally originated PINGs use bounded generation-checked
  `LocalPingCorrelation` live records plus bounded recent-completion tombstones.
  Encode a monotonic connection-local `u64` as the exact opaque wire key. A wire
  key is never reissued during the connection; exhaustion or wrap returns typed
  local backpressure. Exact live-key lookup completes one record regardless of
  ACK arrival order and classifies an in-order or reordered match. A tombstone
  classifies a recent duplicate/stale ACK; after eviction the unknown key is
  unsolicited. All nonmatches are state-neutral and never automatic RFC
  connection errors. Caller metadata remains out-of-band and cannot replace the
  wire key.
- A local correlation becomes ACK-matchable only after full acknowledgement of
  its exact outbound PING frame. ReservedPrivate/Frozen correlation state cannot
  complete from peer input. Reversed adapter delivery is rejected by the
  v0.20.0/v0.25.0 driver causality boundary; if an ACK nevertheless reaches the
  protocol layer without a committed live record, it is unsolicited and
  state-neutral, never implicit output commitment.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Overwrite caller input immediately after parsing and prove every non-ACK transaction retained its own exact bytes. Cover ACK-bearing no-reply, distinct/identical inbound PINGs, FIFO/correlation capacity, unique local keys, matching/unsolicited/duplicate/reordered/stale ACKs, generation wrap/reuse, and exact 17-byte encoding without claiming later partial-output scheduling. Inject a matching ACK while its local PING is Private/Frozen and at every output prefix; prove no correlation completion, input-derived commitment, or retained ACK, plus acknowledgement-first success through the combined driver call.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) still passes; no behavior assigned to v0.110.0 (GOAWAY frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 — GOAWAY frame codec

Status: planned

#### Goal

Deliver **GOAWAY frame codec** as the sole primary capability in this stop. It builds
on v0.109.0 (PING frame codec) and must be independently trustworthy before v0.111.0 (RST_STREAM frame codec) begins.

#### Deliverables

- Acceptance contract: Require stream zero and at least eight payload bytes, mask the reserved bit from the last-stream identifier, preserve the error code, cap retained debug data independently from frame acceptance, ignore unknown flags, emit reserved bits as zero, and map a nonzero stream to connection PROTOCOL_ERROR or a short payload to connection FRAME_SIZE_ERROR. Define checked exact output length `17 + debug_len`, guarantee the 17-byte minimum independently from optional debug capacity, and emit last-stream reserved bits as zero. Bound inbound retained debug and outbound generated debug separately. Drain every unretained inbound debug byte to preserve framing; copy any retained bytes into owned fixed storage before input reuse; redact debug contents by default. For outbound debug, copy the configured-cap prefix and record DebugTruncated when requested input exceeds that cap; if optional storage cannot hold the selected prefix, omit it entirely and record DebugOmittedCapacity. Absent, retained, truncated, and omitted are distinct, and no optional-debug outcome can prevent minimum shutdown.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cover exact 17-byte minimum, zero/maximum/over-limit debug, checked length arithmetic, independent inbound/outbound caps, input overwrite after retained copy, complete drain after retention cap, default redaction, reserved-bit zeroing, and successful minimum encoding when optional debug storage is absent.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.109.0 (PING frame codec) still passes; no behavior assigned to v0.111.0 (RST_STREAM frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 — RST_STREAM frame codec

Status: planned

#### Goal

Deliver **RST_STREAM frame codec** as the sole primary capability in this stop. It builds
on v0.110.0 (GOAWAY frame codec) and must be independently trustworthy before v0.112.0 (WINDOW_UPDATE codec and checked windows) begins.

#### Deliverables

- Acceptance contract: Require a nonzero stream and exactly four payload bytes, ignore unknown flags, preserve the error code, emit reserved bits as zero, and map stream zero to connection PROTOCOL_ERROR or any other payload length to connection FRAME_SIZE_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RST_STREAM frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.110.0 (GOAWAY frame codec) still passes; no behavior assigned to v0.112.0 (WINDOW_UPDATE codec and checked windows) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 — WINDOW_UPDATE codec and checked windows

Status: planned

#### Goal

Deliver **WINDOW_UPDATE codec and checked windows** as the sole primary capability in this stop. It builds
on v0.111.0 (RST_STREAM frame codec) and must be independently trustworthy before v0.113.0 (Legacy PRIORITY frame handling) begins.

#### Deliverables

- Acceptance contract: Require exactly four payload bytes and a nonzero reserved-bit-masked 31-bit increment, ignore unknown flags, and emit reserved bits as zero; map invalid length to connection FRAME_SIZE_ERROR, zero on stream zero to connection PROTOCOL_ERROR, and zero on a nonzero stream to stream PROTOCOL_ERROR before checked window mutation. Define the canonical exact 13-byte frame (nine-byte header plus four-byte increment), typed stream-or-connection target, and checked increment primitive reused by v0.133.0–v0.153.0; encoding never permits `advertised_remaining + increment > 2^31 - 1`.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WINDOW_UPDATE codec and checked windows and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cover stream zero/nonzero targets, reserved-bit masking/zeroing, increments zero/one/`2^31 - 1`, exact 13-byte encoding, and checked result overflow without mutation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE codec and checked windows contract and all previously implemented relevant behavior have
reproducible evidence; v0.111.0 (RST_STREAM frame codec) still passes; no behavior assigned to v0.113.0 (Legacy PRIORITY frame handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.112.0 implementation stop reached. Run pentest for this exact commit.`

### v0.113.0 — Legacy PRIORITY frame handling

Status: planned

#### Goal

Deliver **Legacy PRIORITY frame handling** as the sole primary capability in this stop. It builds
on v0.112.0 (WINDOW_UPDATE codec and checked windows) and must be independently trustworthy before v0.114.0 (PUSH_PROMISE frame handling) begins.

#### Deliverables

- Acceptance contract: Require a nonzero stream and exactly five payload bytes, decode exclusive dependency plus weight, reject self-dependency as stream PROTOCOL_ERROR, ignore unknown flags, and emit every reserved bit as zero; map stream zero to connection PROTOCOL_ERROR and invalid length to stream FRAME_SIZE_ERROR without treating priority as protocol correctness.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Legacy PRIORITY frame handling and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Legacy PRIORITY frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.112.0 (WINDOW_UPDATE codec and checked windows) still passes; no behavior assigned to v0.114.0 (PUSH_PROMISE frame handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 — PUSH_PROMISE frame handling

Status: planned

#### Goal

Deliver **PUSH_PROMISE frame handling** as the sole primary capability in this stop. It builds
on v0.113.0 (Legacy PRIORITY frame handling) and must be independently trustworthy before v0.115.0 (Unknown-frame extension policy) begins.

#### Deliverables

- Acceptance contract: Require a nonzero associated stream; recognize END_HEADERS and PADDED while ignoring unknown flags; validate Pad Length before exposing fragments and map padding length equal to or greater than the remaining payload to connection PROTOCOL_ERROR; require four bytes for the promised 31-bit stream identifier after any Pad Length byte and map an undersized promised-stream layout to connection FRAME_SIZE_ERROR; reject promised stream zero or any role/parity/state-illegal promised identifier with connection PROTOCOL_ERROR; subtract every optional field without underflow and emit reserved bits and generated padding bytes as zero.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PUSH_PROMISE frame handling and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PUSH_PROMISE frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.113.0 (Legacy PRIORITY frame handling) still passes; no behavior assigned to v0.115.0 (Unknown-frame extension policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 — Unknown-frame extension policy

Status: planned

#### Goal

Deliver **Unknown-frame extension policy** as the sole primary capability in this stop. It builds
on v0.114.0 (PUSH_PROMISE frame handling) and must be independently trustworthy before v0.116.0 (HTTP/2 stream-identifier rules) begins.

#### Deliverables

- Acceptance contract: Ignore an unknown frame unless an explicitly enabled extension owns its type; enforce the effective inbound frame-size limit, drain its payload incrementally without allocation from the declared length, emit no application event by default, and preserve nonzero progress under every payload fragmentation; an ignored frame cannot mutate stream, compression, priority, or flow-control state and cannot interrupt an active HEADERS/CONTINUATION sequence, where any intervening type remains connection PROTOCOL_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every unknown type, stream identifier, payload size, byte split,
  extension-disabled/enabled disposition, active field-block position, and
  before/after state snapshot with no allocation or application publication.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unknown-frame extension policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.114.0 (PUSH_PROMISE frame handling) still passes; no behavior assigned to v0.116.0 (HTTP/2 stream-identifier rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 — HTTP/2 stream-identifier rules

Status: planned

#### Goal

Deliver **HTTP/2 stream-identifier rules** as the sole primary capability in this stop. It builds
on v0.115.0 (Unknown-frame extension policy) and must be independently trustworthy before v0.117.0 (Generation-checked stream table and tombstones) begins.

#### Deliverables

- Acceptance contract: Use reserved-bit-masked 31-bit identifiers with client-initiated odd and server-push even parity, require monotonically increasing new IDs, keep stream zero only for connection frames, reject reused/lower illegal IDs with exact RFC scope, and on identifier exhaustion send bounded GOAWAY instead of wrapping.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 stream-identifier rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.115.0 (Unknown-frame extension policy) still passes; no behavior assigned to v0.117.0 (Generation-checked stream table and tombstones) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 — Generation-checked stream table and tombstones

Status: planned

#### Goal

Deliver **Generation-checked stream table and tombstones** as the sole primary capability in this stop. It builds
on v0.116.0 (HTTP/2 stream-identifier rules) and must be independently trustworthy before v0.118.0 (Exhaustive stream-state graph) begins.

#### Deliverables

- Acceptance contract: Store each live stream in a fixed slot with a generation token and retain bounded tombstones/cutoff metadata for closed IDs; reject stale commands and borrowed acknowledgements, never recycle before terminal events release, distinguish known-closed from idle IDs, and report local slot exhaustion without inventing a peer protocol error. Any live/reserved-to-rejected/closed transition must preflight tombstone and cutoff capacity before releasing its slot or convert that slot in place without a release/reacquire gap. Once an ID has been accepted as live or reserved, it is continuously represented as a generation-bound slot, tombstone, or connection-shutdown record and can never be reinterpreted as idle. Tombstones remain until terminal output commits and peer stream-ID/cutoff state can classify every later frame. If mandatory rejection/closure tracking cannot be represented, initiate typed bounded `StreamTrackingUnavailable` connection shutdown while retaining the current record through teardown; never silently forget the ID.
- Store policy disposition, current RFC wire state, generation-checked reset output/lease/acknowledged-prefix state, remote-closure cause, terminal-validation state/stage, compression-workspace ownership, immutable terminal-field-section lease, and active field-block ownership independently. Also retain an immutable first-wire-closure cause independently; policy rejection, closure, HPACK completion, reset exposure, or an intermediate stage alone never releases or implies another dimension. A policy-CANCEL reservation can become dormant only before output exposure. Once reset bytes are exposed, the exact frozen frame and owning stream/tombstone survive until every output token and acknowledged-prefix obligation resolves or connection-owned cleanup runs.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Generation-checked stream table and tombstones and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Exhaust tombstone/cutoff capacity at every live/reserved transition; interleave peer frames and local terminal-output backpressure; vary policy, wire state, reset-output progress, remote closure, and first-closure attribution independently; prove in-place conversion or typed bounded shutdown leaves no moment when an accepted ID is idle, no partial reset acknowledgement implies Closed, and every slot/tombstone releases exactly once only after its classification and active-field-block horizons.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Generation-checked stream table and tombstones contract and all previously implemented relevant behavior have
reproducible evidence; v0.116.0 (HTTP/2 stream-identifier rules) still passes; no behavior assigned to v0.118.0 (Exhaustive stream-state graph) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 — Exhaustive stream-state graph

Status: planned

#### Goal

Deliver **Exhaustive stream-state graph** as the sole primary capability in this stop. It builds
on v0.117.0 (Generation-checked stream table and tombstones) and must be independently trustworthy before v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) begins.

#### Deliverables

- Acceptance contract: Implement idle, reserved-local, reserved-remote, open, both half-closed states, and closed with exhaustive frame/role transition tables; validate before mutation, map every illegal transition through the exact error-scope milestone, preserve unrelated streams and connection windows on stream error, and recycle a slot only after terminal connection effects and borrowed events complete. Normalize END_STREAM separately from its carrying HEADERS or DATA event; CONTINUATION never changes wire state and active field-block ownership survives until END_HEADERS or connection failure. Track terminal work as `TerminalValidation::{NotTerminal, PendingFieldBlock(PendingBlockDisposition), PendingSemantics { stage: SemanticStage, fields: TerminalFieldSectionLease }, Valid, Malformed(StreamErrorCode), AbortedByPeerReset}` with `PendingBlockDisposition::{ValidateSemantics, AbortAfterHpackByPeerReset}`. Define sealed monotonic `SemanticStage::{PseudoFields, ConnectionFields, FieldAndContext, RequestMapping, ResponseMapping, ContentAndPhase, TrailerAndRoleRules}` ownership across v0.125.0–v0.131.0.
- Permit only sealed/private transition constructors. `PendingSemantics` always owns exactly one non-Copy/non-Clone generation/stream-bound immutable `TerminalFieldSectionLease`; every stage carries that same lease without reparse, reconstruction, truncation, or substitution. `NotTerminal` cannot coexist with a dormant reset or section lease; terminal results cannot retain semantic-stage/compression ownership. Each stage uses pre-reserved bounded work/storage; resumable pressure leaves the same stage, lease, and reservation intact, while inability to retain mandatory state transfers all cleanup exactly once to connection-owned shutdown.
- Model local reset and ordinary local END_STREAM completion as normalized transition events, distinct from command acceptance, output reservation, byte exposure, and partial acknowledgement. Track `FirstWireClosureCause::{LocalResetComplete, LocalEndStreamComplete, PeerReset, RemoteEndStream}` once, while retaining directional local/remote completion and peer-reset records independently. An acknowledged local END_STREAM moves Open to HalfClosedLocal without selecting a closure cause, but moves HalfClosedRemote to Closed with `LocalEndStreamComplete`; remote END_STREAM similarly selects `RemoteEndStream` only when it moves HalfClosedLocal to Closed. Only the first actual transition to Closed selects the cause; later closure evidence and output completion cannot overwrite it or repeat the transition.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Exhaustive stream-state graph and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross HEADERS/DATA frame events with END_STREAM present/absent, HEADERS with END_HEADERS present/absent, peer reset, and local reset/END_STREAM completion; prove directional half-close before final close, closed wire state with a still-active CONTINUATION obligation, immutable first-closure attribution, no duplicate close, and no wire-state transition from command acceptance, CONTINUATION, or partial output. Compile-fail or model-check every forbidden terminal-validation/field-block/reset/closure-cause combination and every non-monotonic or caller-forged transition.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Exhaustive stream-state graph contract and all previously implemented relevant behavior have
reproducible evidence; v0.117.0 (Generation-checked stream table and tombstones) still passes; no behavior assigned to v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 — HTTP/2 activation preface, first-SETTINGS, and deadline sequencing

Status: planned

#### Goal

Deliver **HTTP/2 activation preface, first-SETTINGS, and deadline sequencing** as the sole primary capability in this stop. It builds
on v0.118.0 (Exhaustive stream-state graph) and must be independently trustworthy before v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) begins.

#### Deliverables

- Acceptance contract: Validate the connection preface before frames, require SETTINGS as the first peer frame, apply bounded caller-driven preface/ACK deadlines, and reject frames before activation without publishing connection state. Before exposing byte zero of the client's 24-byte connection preface, atomically reserve its complete v0.139.0 initial `OutboundSettingsTransaction`, including exact frame/queue storage, future outstanding-ACK FIFO slot, timeout generation, and prevalidated local-effect snapshots; preface capacity failure returns local backpressure with zero exposure. After the complete client preface, that reserved SETTINGS is the sole eligible frame until its full commitment. A server performs the same reservation before exposing its first SETTINGS byte, which must be its first frame. Neither preface exposure nor command acceptance starts the SETTINGS ACK timeout; only full SETTINGS-frame acknowledgement does. Cancellation/failure cannot leave a successfully emitted client preface without a guaranteed SETTINGS transaction behind it.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Fragment the client preface at every byte and cross client/server initial SETTINGS reservation success, every one-slot-short frame/queue/future-ACK/timeout capacity, cancellation, stale generation, fatal intent, and transport failure. Prove zero preface exposure without the complete reservation, no intervening frame, and timeout start only at final SETTINGS acknowledgement.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 activation preface, first-SETTINGS, and deadline sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.118.0 (Exhaustive stream-state graph) still passes; no behavior assigned to v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.119.0 implementation stop reached. Run pentest for this exact commit.`

### v0.120.0 — HTTP/2 frame legality and fragmented-header-block sequencing

Status: planned

#### Goal

Deliver **HTTP/2 frame legality and fragmented-header-block sequencing** as the sole primary capability in this stop. It builds
on v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) and must be independently trustworthy before v0.121.0 (HTTP/2 error scope, typed deltas, and isolated stream mutation) begins.

#### Deliverables

- Acceptance contract: Apply the idle/reserved/open/half-closed/closed/unknown stream matrix, allow only one active fragmented header block per connection, reject illegal interleaving, and handle stream-ID exhaustion deterministically. Represent rejection policy and wire state separately from `ResetOutput::{Reserved { reason, disposition }, Frozen { stream: StreamToken, reason: ResetReason, frame: [u8; 13], offered: u8, acknowledged: u8, generation: OutputGeneration }, Complete, SupersededBeforeExposure}`, `ResetReason::{PolicyCancel, StreamError(StreamErrorCode)}`, `ReservedResetDisposition::{Active, PolicyDormantAfterEndStream}`, and `RemoteClosureCause::{Reset, EndStream}`. Normalize `HeadersStart { end_stream, end_headers }`, `Data { end_stream }`, `Continuation { end_headers }`, and `PeerReset` before lookup. A reserved reason may change or be superseded only before first non-empty exposure. Exposure atomically freezes the 9-byte RST_STREAM header plus 4-byte error code, stream token, reason, and generation; every field and all 13 bytes are thereafter immutable regardless of zero/short acknowledgement, peer reset, END_STREAM, semantic re-arm, or GOAWAY.
- `Frozen` has at most one generation-bound output token outstanding. Its `acknowledged` cursor advances only by a valid consumed token's exact reported delta and never beyond `offered`; after any positive prefix, emit only `frame[acknowledged..]`, never restart or regenerate. A zero acknowledgement consumes the token without changing the cursor. `ResetOutput::Reserved` and `Frozen { acknowledged: 0..=12 }` leave `WireStreamState` unchanged and every inbound frame uses that prior state's legality. `Complete` requires acknowledgement of all 13 bytes and atomically emits normalized `LocalResetComplete`: if the stream is not Closed, apply the local-reset wire transition exactly once and set `FirstWireClosureCause::LocalResetComplete`; if peer reset or remote END_STREAM already closed it, retain that first cause and record output completion without a second transition. Peer reset/valid completion can select `SupersededBeforeExposure` only from `Reserved` with no non-empty exposure; a zero-capacity NeedOutput poll is not exposure. Connection failure at prefix 0..=12 performs acknowledged-prefix cleanup without `Complete` or `LocalResetComplete`. Reserved(remote) DATA and non-idle promised-ID reuse remain connection PROTOCOL_ERROR until an actual transition makes the stream Closed.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cover policy/wire/closure/terminal/block state × every ResetOutput state/reason/generation/offered/acknowledged cursor × outstanding-token presence × normalized events. Inject every inbound frame at acknowledged offsets 0..=13. Prove only pre-exposure reservation changes reason; offsets 0..=12 preserve prior reserved/open/half-closed legality and never gain closed-stream DATA tolerance; byte 13 applies at most one local close; remote-first closure retains its cause; every frozen suffix is stable; invalid acknowledgement is state-neutral; closure never strands CONTINUATION or output ownership; and no slot/tombstone generation recycles early.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 frame legality and fragmented-header-block sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) still passes; no behavior assigned to v0.121.0 (HTTP/2 error scope, typed deltas, and isolated stream mutation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 — HTTP/2 error scope, typed deltas, and isolated stream mutation

Status: planned

#### Goal

Deliver **HTTP/2 error scope, typed deltas, and isolated stream mutation** as the sole primary capability in this stop. It builds
on v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) and must be independently trustworthy before v0.122.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) begins.

#### Deliverables

- Acceptance contract: Map every RFC 9113 frame/state violation to its exact error code and connection-versus-stream scope; represent stream errors as typed deltas restricted to that generation-checked stream; retain valid HPACK changes while making compression errors connection-fatal; enqueue exactly one RST_STREAM or GOAWAY through reserved mandatory-output capacity; prevent all further application publication after a connection-fatal decision; and keep the error action pending under serialization backpressure.
- Reserved(remote) DATA and reuse of a promised identifier that is no longer idle produce connection PROTOCOL_ERROR even when local policy already intends to reject that push. Malformed HPACK remains connection-fatal on synchronization-only and locally reset-associated-stream paths; neither rejection intent nor missing recycled application provenance may downgrade or upgrade RFC error scope.
- Define one deterministic error-action precedence: connection-fatal failure commits bounded shutdown; `StreamError(code)` may replace/re-arm `PolicyCancel` only while `ResetOutput::Reserved` has never exposed bytes; peer reset may supersede only that same pre-exposure reservation. `Frozen` frame identity and bytes always win over later reason changes—finish only its acknowledged-cursor suffix and emit no second reset. Reset intent, exposure, and acknowledgement through byte 12 never alter inbound error scope: reserved(remote) DATA remains connection PROTOCOL_ERROR and legal HEADERS can still transition it. Peer reset still aborts pending semantics after mandatory HPACK synchronization; full local-reset acknowledgement closes only if a remote transition has not already done so. Wire/HPACK transitions never roll back when the output action changes.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Property-test every error delta and reserved-output/backpressure state; after
  a stream error prove every unrelated stream, scheduler entry, flow window,
  generation, compression context, and queued event is byte-for-byte unchanged.
- Prove connection-fatal decisions publish no later application event and
  produce exactly one bounded GOAWAY attempt under every partial-output split.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 error scope, typed deltas, and isolated stream mutation contract and all previously implemented relevant behavior have
reproducible evidence; v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) still passes; no behavior assigned to v0.122.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 — HTTP/2 graceful GOAWAY and bounded shutdown sequencing

Status: planned

#### Goal

Deliver **HTTP/2 graceful GOAWAY and bounded shutdown sequencing** as the sole primary capability in this stop. It builds
on v0.121.0 (HTTP/2 error scope, typed deltas, and isolated stream mutation) and must be independently trustworthy before v0.123.0 (Atomic HPACK header-block integration) begins.

#### Deliverables

- Acceptance contract: Implement two-stage graceful GOAWAY, exact last-processed-stream classification, no new streams after cutoff, bounded mandatory-control output under backpressure, and deterministic cancellation/EOF shutdown completion. Keep local admission sealing, `ShutdownIntent`, `PublishedPeerStreamHighWater`, `GoawayOutput`, graceful timer generation, and `SentGoawayCutoff` as separate state. Advance the high-water only when data from a peer-initiated stream—including its first validated mapped head or body event—becomes application-visible, never when a frame parses, a slot allocates, or synchronization-only HPACK completes. Local admission sealing occurs at shutdown intent without claiming peer knowledge.
- Define `GoawayOutput::{None, ReservedPrivate { generation, stage,
  last_stream_id, error_code, debug }, Frozen { generation, stage,
  last_stream_id, error_code, slot, total_len, acknowledged }, Complete,
  AbandonedConnection}` with
  `stage::{GracefulInitial, GracefulFinal, Fatal}`. GracefulInitial uses
  `2^31 - 1` and NO_ERROR. Its RTT/grace timer is unarmed while requested,
  ReservedPrivate, or partially Frozen; only full frame acknowledgement arms a
  generation-checked deadline. Early, stale, duplicate, and wrong-generation
  timer events are state-neutral. GracefulFinal snapshots
  `PublishedPeerStreamHighWater` only at first non-empty exposure. From that
  boundary, higher peer streams may finish required HPACK synchronization and
  connection flow-control accounting but cannot publish any application event.
- Apply the foundational driver causality rule to every input whose
  classification depends on a committed local GOAWAY stage/cutoff/timer:
  combined calls acknowledge the GOAWAY prefix first, while reversed independent
  delivery returns `DriverCommitOrderViolation` without consuming input or
  advancing shutdown state.
- A fatal decision replaces an unexposed graceful record but never a Frozen
  frame. Fatal causes enter a closed `FatalCauseClass` order:
  CompressionSynchronization (COMPRESSION_ERROR), ProtocolState
  (PROTOCOL_ERROR, FLOW_CONTROL_ERROR, FRAME_SIZE_ERROR, CONNECT_ERROR, or a
  promoted STREAM_CLOSED), AuthenticatedSecurity (INADEQUATE_SECURITY or
  HTTP_1_1_REQUIRED), Timeout (SETTINGS_TIMEOUT), PeerResource
  (ENHANCE_YOUR_CALM), then LocalInvariant (INTERNAL_ERROR). REFUSED_STREAM and
  CANCEL remain stream-scoped and never enter this table. Within a class the
  earliest monotonic event ordinal wins and its exact typed RFC error code is
  retained. Preserve later
  causes as bounded redacted secondary diagnostics without another terminal
  frame. If fatal intent arrives during Frozen graceful output, finish those
  immutable bytes and then reserve at most one non-increasing fatal successor,
  or abandon the connection if output is unusable. Never widen a frozen or
  committed cutoff.
- Define the connection-owned terminal cleanup transaction and shared
  `ControlDisposition::{Private, Frozen, Complete,
  AbandonedByConnectionFatal { connection_generation }}`. A Frozen record or
  FramingCommitted field block finishes before fatal GOAWAY while output remains
  usable; unexposed controls may become Abandoned only through this typed
  terminal transition. Full fatal GOAWAY commitment atomically abandons every
  remaining Private SETTINGS ACK, PING ACK, RST_STREAM, WINDOW_UPDATE, and
  graceful GOAWAY record, exposes no later frame, invalidates their tokens, and
  releases each slot/transaction/tombstone/lease once. The cleanup runs no
  settings acknowledgement/HPACK-debt merge, advertised-credit restoration,
  local-reset completion, PING-response completion, or graceful-timer hook.
  Graceful GOAWAY never invokes it and existing-stream controls remain live.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cross admission seal, intent, publication high-water, every graceful/fatal state, timer request/reservation/partial/full-commit boundaries, early/stale/wrong-generation events, and every fatal class/arrival order. Publish immediately before/after final first exposure; prove the former advances the snapshot, the latter is suppressed while HPACK/connection credit still synchronize. Prove one fatal winner, bounded secondary causes, no Frozen rewrite, at most one non-increasing successor, and deterministic abandonment. Model every ControlDisposition transition and prove only typed fatal cleanup abandons Private records, every Frozen/FramingCommitted obligation finishes first, no semantic hook runs, all ownership releases once, stale tokens are neutral, and graceful shutdown performs no terminal cleanup.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 graceful GOAWAY and bounded shutdown sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.121.0 (HTTP/2 error scope, typed deltas, and isolated stream mutation) still passes; no behavior assigned to v0.123.0 (Atomic HPACK header-block integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 — Atomic HPACK header-block integration

Status: planned

#### Goal

Deliver **Atomic HPACK header-block integration** as the sole primary capability in this stop. It builds
on v0.122.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) and must be independently trustworthy before v0.124.0 (SETTINGS header-table encoder and header-list policy coupling) begins.

#### Deliverables

- Acceptance contract: Decode one complete HEADERS/PUSH_PROMISE plus CONTINUATION block through HPACK before field publication; once a block starts, immediate RST_STREAM, refusal, application cancellation, or later semantic stream error cannot cancel decoding or valid table changes, and a synchronization-only path completes the block with no decoded field exposed to the application; permit REFUSED_STREAM only when remaining HPACK/CONTINUATION work and storage can finish safely, otherwise perform bounded connection shutdown; make incomplete/invalid compression connection-fatal, publish an admitted field section atomically after capacity and semantic preflight, and preserve exact partial-input state.
- A normalized directional transition caused by HEADERS+END_STREAM, DATA+END_STREAM, or peer RST_STREAM cannot release an active field-block owner. The legacy statement "HEADERS with END_STREAM but without END_HEADERS records closed wire state immediately" is forbidden. After a valid HEADERS envelope with END_STREAM but without END_HEADERS is accepted, apply its directional transition—Open to HalfClosedRemote or HalfClosedLocal to Closed—yet decode every required CONTINUATION and commit valid HPACK mutations before releasing synchronization state; application publication remains independently forbidden where policy rejected the stream.
- HEADERS+END_STREAM without END_HEADERS sets `PendingFieldBlock(ValidateSemantics)` while separately reserving semantic-section capacity. On successful HPACK completion, atomically seal a non-Copy/non-Clone `TerminalFieldSectionLease` and transfer it to `PendingSemantics { stage: PseudoFields, fields }`, never directly to `Valid`. Only `CompressionWorkspace`—encoded fragments, integer/Huffman scratch, and CONTINUATION assembly—becomes releasable. The lease retains immutable decoded bytes, ordered boundaries, duplicates/empty values, pseudo classification, sensitivity/never-index provenance, and generation/stream binding through every stage; it never borrows dynamic-table entries, compression scratch, or recyclable caller input/output. Malformed HPACK or semantic-storage shortage after table mutation finishes bounded synchronization and transfers workspace, partial section storage, reset reservation, and cleanup exactly once to connection shutdown. Peer reset during fragmentation changes the disposition to abort-after-HPACK; completion releases both workspace and unpublished section storage, enters `AbortedByPeerReset`, and publishes nothing.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Atomic HPACK header-block integration and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Atomic HPACK header-block integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.122.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) still passes; no behavior assigned to v0.124.0 (SETTINGS header-table encoder and header-list policy coupling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 — SETTINGS header-table encoder and header-list policy coupling

Status: planned

#### Goal

Deliver **SETTINGS header-table encoder and header-list policy coupling** as the sole primary capability in this stop. It builds
on v0.123.0 (Atomic HPACK header-block integration) and must be independently trustworthy before v0.125.0 (Pseudo-field ordering and uniqueness) begins.

#### Deliverables

- Acceptance contract: Own `EncoderTableLimits { peer_received_ceiling: u32, peer_wire_acknowledged_ceiling: u32, selected_capacity: u32, physical_capacity: usize }` at the connection and arbitrate peer SETTINGS_HEADER_TABLE_SIZE through bounded `PendingEncoderTableSizeTransition::{None, AwaitingSafeApply { obligations: EncoderLimitAckObligationSet }, AppliedAwaitingAckCommit { obligations: EncoderLimitAckObligationSet }}`. Each ordered `EncoderLimitAckObligation { transaction_generation, peer_received_ceiling_after_frame, selected_update: Option<EncoderTableUpdateDebt> }` belongs to one v0.108.0 frame transaction but never owns its ACK. For every ordered value, immediately set peer_received_ceiling. If it is below selected capacity, atomically clamp selection, evict the committed/provisional future encoder state, and accumulate the smallest/final selected values in that frame's selected_update; if it is greater or equal, never enlarge selection and record no debt merely for the ceiling change. Maintain selected <= peer_received and checked selected <= profile/physical after every entry. With Private HPACK, first roll back provisional mutations and restore its exact debt lease before applying a reduction. With FramingCommitted, its encoded/transferred prefix remains immutable, but clamp its post-block encoder state immediately for all future lookup and retain the frame obligation while the guaranteed block drains. Report HPACK Effective only after each reduction's clamp/eviction/update obligation is atomically represented. At each owning ACK's FIFO byte-nine commitment, set peer_wire_acknowledged_ceiling to that obligation's frame snapshot and merge only its optional selected_update into existing debt, retaining the older debt minimum; a ceiling-only increase creates no debt. Local policy reductions atomically clamp/evict and merge selected debt without SETTINGS; local increases require the minimum of peer_received, peer_wire_acknowledged, profile, and checked physical capacity, then create selected debt. If another setting arrives while debt waits, preserve it; if it arrives during Private encoding, restore the lease first; after first exposure, transferred debt stays with FramingCommitted and later selected changes belong to the following block. A fatal result before ACK exposure cancels the transaction; partial ACK output, stale tokens, or transport failure abandons the connection without acknowledging the ceiling or exposing dependent output. No later HEADERS/PUSH_PROMISE block may encode or expose while AwaitingSafeApply or AppliedAwaitingAckCommit remains unresolved. Treat peer MAX_HEADER_LIST_SIZE as outbound guidance while preserving independent hard inbound decode limits.
- The pending transition and every encoder-limit obligation are participants only. It never owns, counts, queues, or serializes SETTINGS ACKs. ACK commitment never clears or replaces older debt.
- Prevalidate locally emitted MAX_HEADER_LIST_SIZE as bounded peer guidance and
  attach its exact snapshot to the v0.139.0 outbound commit plan. It becomes
  locally advertised committed only with the complete SETTINGS frame and never
  replaces independent hard inbound header-list limits or reapplies on peer
  ACK.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Cross physical/profile capacities below/equal/above 4096; peer ceilings 0, 4096, and `u32::MAX`; no-active, debt-waiting, Private debt lease, and every FramingCommitted boundary; duplicate/decrease/increase sequences; local policy reductions/increases without SETTINGS; initial selected below 4096; every ACK offset; backpressure; stale tokens; participant failure; reset; GOAWAY; and transport failure. Prove all four limit inequalities, immediate reduction clamp/eviction with selected update, zero automatic enlargement/debt for ceiling-only increase, local increase blocked until the relevant wire ACK, exact per-frame acknowledged snapshots, safe physical bounds, lease restoration, oldest selected minimum, first-exposure transfer, following-block debt, encoder/decoder equivalence, and no eviction without matching selected wire debt.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS header-table encoder and header-list policy coupling contract and all previously implemented relevant behavior have
reproducible evidence; v0.123.0 (Atomic HPACK header-block integration) still passes; no behavior assigned to v0.125.0 (Pseudo-field ordering and uniqueness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 — Pseudo-field ordering and uniqueness

Status: planned

#### Goal

Deliver **Pseudo-field ordering and uniqueness** as the sole primary capability in this stop. It builds
on v0.124.0 (SETTINGS header-table encoder and header-list policy coupling) and must be independently trustworthy before v0.126.0 (Connection-specific field and TE validation) begins.

#### Deliverables

- Acceptance contract: Require all pseudo-fields before regular fields, reject any duplicate or unknown pseudo-field, allow only request pseudo-fields in requests and :status in responses, forbid every pseudo-field in trailers, and complete these checks after HPACK synchronization but before mapped message publication.
- Own `SemanticStage::PseudoFields`: read the immutable ordered `TerminalFieldSectionLease` and carry the exact same lease on success to `PendingSemantics { stage: ConnectionFields, fields }`; never reparse HPACK, borrow compression/table state, or rebuild ordering/provenance. A forbidden/duplicate/unknown/misordered pseudo-field records terminal `Malformed(PROTOCOL_ERROR)` and consumes the retained mandatory reset reservation. It never becomes `Valid` merely because HPACK or peer END_STREAM completed first.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Pseudo-field ordering and uniqueness and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Pseudo-field ordering and uniqueness contract and all previously implemented relevant behavior have
reproducible evidence; v0.124.0 (SETTINGS header-table encoder and header-list policy coupling) still passes; no behavior assigned to v0.126.0 (Connection-specific field and TE validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 — Connection-specific field and TE validation

Status: planned

#### Goal

Deliver **Connection-specific field and TE validation** as the sole primary capability in this stop. It builds
on v0.125.0 (Pseudo-field ordering and uniqueness) and must be independently trustworthy before v0.127.0 (HTTP/2 malformed initial-field-block publication barrier) begins.

#### Deliverables

- Acceptance contract: Reject Connection, Proxy-Connection, Keep-Alive, Transfer-Encoding, and Upgrade in every HTTP/2 field section, including an Upgrade field received with status 426; accept TE only with the case-insensitive value trailers and no other list member, classify forbidden-field violations as malformed-message stream PROTOCOL_ERROR after full HPACK decode, and publish no invalid field section.
- Own `SemanticStage::ConnectionFields`: success carries the same lease only to `PendingSemantics { stage: FieldAndContext, fields }`; failure records `Malformed(PROTOCOL_ERROR)` without releasing the dormant reset reservation first. Peer-reset abort and connection-owned teardown remain available at the boundary before and after this stage.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Connection-specific field and TE validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-specific field and TE validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.125.0 (Pseudo-field ordering and uniqueness) still passes; no behavior assigned to v0.127.0 (HTTP/2 malformed initial-field-block publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 — HTTP/2 malformed initial-field-block publication barrier

Status: planned

#### Goal

Deliver **HTTP/2 malformed initial-field-block publication barrier** as the sole primary capability in this stop. It builds
on v0.126.0 (Connection-specific field and TE validation) and must be independently trustworthy before v0.128.0 (HTTP/2 request mapping) begins.

#### Deliverables

- Acceptance contract: Before any initial request or response becomes observable, reject uppercase names, NUL/CR/LF, forbidden whitespace, invalid checked Content-Length grammar or unequal duplicates, Host/:authority disagreement, missing or forbidden :scheme/:path/:authority for the exact request form, ordinary-versus-extended CONNECT pseudo-field matrix violations, non-three-digit :status, HTTP/2 status 101, and every pseudo-field in trailers; DATA-octet reconciliation remains later but an invalid initial declared length never reaches the application.
- Own `SemanticStage::FieldAndContext`: success carries the same lease only to `PendingSemantics { stage: RequestMapping, fields }`; if the block carried END_STREAM, every malformed-message result becomes terminal `Malformed(PROTOCOL_ERROR)` and re-arms the dormant reset slot as `StreamError(PROTOCOL_ERROR)` unless immutable reset bytes, peer-reset abort, or a connection-fatal decision already won. Remote completion is not a reason to suppress the required stream error.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 malformed initial-field-block publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.126.0 (Connection-specific field and TE validation) still passes; no behavior assigned to v0.128.0 (HTTP/2 request mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 — HTTP/2 request mapping

Status: planned

#### Goal

Deliver **HTTP/2 request mapping** as the sole primary capability in this stop. It builds
on v0.127.0 (HTTP/2 malformed initial-field-block publication barrier) and must be independently trustworthy before v0.129.0 (HTTP/2 response mapping) begins.

#### Deliverables

- Acceptance contract: Map validated :method/:scheme/:authority/:path into the exact ordinary, CONNECT, or extended-CONNECT request form; split :path on its first question mark into raw path and optional raw query, preserve absent versus empty query and percent-encoded octets exactly, require `/` for an empty HTTP(S) URI path except asterisk-form and CONNECT rules, reconcile Host and :authority, preserve ordered ordinary fields without pseudo-fields, and emit one request event only after the initial-field publication barrier and stream transition commit.
- Own `SemanticStage::RequestMapping`: request validation carries the lease only to `PendingSemantics { stage: ResponseMapping, fields }` after recording unpublished mapped evidence; response/trailer sections take the sealed checked-no-op transition. A terminal pipeline publishes neither that evidence nor an application event until its final applicable semantic owner commits `Valid`.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 request mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.127.0 (HTTP/2 malformed initial-field-block publication barrier) still passes; no behavior assigned to v0.129.0 (HTTP/2 response mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.128.0 implementation stop reached. Run pentest for this exact commit.`

### v0.129.0 — HTTP/2 response mapping

Status: planned

#### Goal

Deliver **HTTP/2 response mapping** as the sole primary capability in this stop. It builds
on v0.128.0 (HTTP/2 request mapping) and must be independently trustworthy before v0.130.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) begins.

#### Deliverables

- Acceptance contract: Require exactly one three-digit valid :status and no request pseudo-field, correlate informational and final responses to the initiating request, preserve ordered ordinary fields and Set-Cookie lines, reject 101 in HTTP/2, and publish only after complete HPACK, semantic, capacity, and stream-state validation; an HTTP/2 426 without Upgrade is framing-valid but produces a typed RFC 9110 received-semantic violation/recipient-policy disposition rather than PROTOCOL_ERROR or connection desynchronization, while any Upgrade field was already rejected by v0.126.0.
- Own `SemanticStage::ResponseMapping`: success, including the sealed checked-no-op for request sections, carries the lease only to `PendingSemantics { stage: ContentAndPhase, fields }`. Missing, duplicate, malformed, or context-invalid `:status` on terminal HEADERS records stream `Malformed(PROTOCOL_ERROR)` after HPACK synchronization and re-arms the retained mandatory reset reservation; no response or terminal-valid event is published.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 response mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.128.0 (HTTP/2 request mapping) still passes; no behavior assigned to v0.130.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.129.0 implementation stop reached. Run pentest for this exact commit.`

### v0.130.0 — HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation

Status: planned

#### Goal

Deliver **HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation** as the sole primary capability in this stop. It builds
on v0.129.0 (HTTP/2 response mapping) and must be independently trustworthy before v0.131.0 (Informational responses and trailers) begins.

#### Deliverables

- Acceptance contract: Reconcile Content-Length with DATA octets and enforce final-response, body-forbidden, trailer, DATA-after-trailer, and END_STREAM ordering for ordinary messages; classify every HTTP/2 CONNECT DATA octet after initial request HEADERS as tunnel data in fixed caller-capacity PendingConnect while the stream is AwaitingConnectOutcome, never as request content, with no peer-sized allocation, WINDOW_UPDATE, credit-release, DNS, dial, or socket claim at this milestone; if capacity is unavailable emit a typed local-capacity disposition plus RST_STREAM(CANCEL), not a peer protocol violation; consume one matching opaque AuthorizedConnectOutcome and forward nothing until it passes v0.19.0/v0.64.0 authority, endpoint, actual-peer, request, attempt, and policy checks; cancellation, reset, invalid outcome, policy change, non-2xx, or connection/tunnel commitment invalidates all remaining capabilities and makes duplicate/same-generation success InvalidState; discard/reset pending bytes without publication or unrelated-stream mutation; once connected allow only DATA and applicable stream-management frames, reject later HEADERS/trailers or other frames with stream PROTOCOL_ERROR, map caller-reported TCP failure/reset to RST_STREAM(CONNECT_ERROR), and expose HTTP/2 stream/connection failure as a typed caller action to reset upstream TCP; for inbound 205 use ordinary DATA/END_STREAM classification, emit a typed semantic violation and stream reset on nonzero DATA, and prevent valid-205 forwarding.
- Bind each PendingConnect range to ordinary-CONNECT request/stream generation
  provenance. A later bridge may wrap that existing linear owner as
  `PermittedOptimisticConnectInput`, but cannot rebind it to RFC 8441 WebSocket,
  duplicate its storage, or create a second discard/credit owner.
- Own `SemanticStage::ContentAndPhase`. Process each DATA payload's padding, flow-controlled length, semantic length, framing, Content-Length/body-forbidden/message-phase validation, and policy disposition before final reset arbitration for its normalized END_STREAM closure event. A valid terminal DATA for which this is the final applicable owner marks `TerminalValidation::Valid` and releases a dormant policy-reset slot only after credit; terminal HEADERS carry their lease to `PendingSemantics { stage: TrailerAndRoleRules, fields }` instead. Content-Length mismatch, body-forbidden DATA, DATA-after-trailers, or another terminal message violation marks `Malformed(PROTOCOL_ERROR)` and re-arms that slot. This ordered disposition lets v0.136.0 discard/credit a rejected half-closed(local) DATA+END_STREAM exactly once without losing terminal evidence.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PendingConnect at every DATA split and fixed-capacity boundary, ordinary-CONNECT versus mismatched extended-CONNECT provenance, CANCEL reset without peer blame, AwaitingConnectOutcome valid/stale/mismatched/alternate-peer and non-2xx transitions, absence of flow-credit/DNS/socket behavior, no early forwarding/content event, connected legal/illegal frame matrix, caller TCP-to-CONNECT_ERROR and HTTP/2-to-caller-TCP-reset actions, stream isolation, plus 205 zero/nonzero DATA and END_STREAM cases.
- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation contract and all previously implemented relevant behavior have
reproducible evidence; v0.129.0 (HTTP/2 response mapping) still passes; no behavior assigned to v0.131.0 (Informational responses and trailers) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 — Informational responses and trailers

Status: planned

#### Goal

Deliver **Informational responses and trailers** as the sole primary capability in this stop. It builds
on v0.130.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) and must be independently trustworthy before v0.132.0 (Cookie field combination and Set-Cookie preservation) begins.

#### Deliverables

- Acceptance contract: Allow ordered informational responses before one final response without prematurely completing the stream; accept trailers only after the body on trailing HEADERS with END_STREAM, forbid pseudo-fields and Content-Length, and apply the shared v0.52.0 `TrailerFieldPermission` policy while keeping local authentication-info generation unavailable until v0.157.2; received trailers carry no local capability, publish atomically into a separate ordered section, classify authentication-info as RequiresSchemeAuthorization and other forbidden fields with a typed semantic/policy disposition after stream synchronization rather than automatically as a framing error, cannot retroactively alter routing, framing, authentication, or representation decisions, and never merge into initial fields at this stop.
- Own the final HEADERS stage `SemanticStage::TrailerAndRoleRules`. Classify initial, informational, final, and trailer HEADERS independently from END_STREAM/END_HEADERS while reading the same immutable field-section lease. Any informational 1xx HEADERS carrying END_STREAM is terminal `Malformed(PROTOCOL_ERROR)` and requires stream RST_STREAM(PROTOCOL_ERROR); only successful completion of every prior stage may mark terminal `Valid`, atomically transfer the lease into the final unpublished/message-event lifecycle, and release the dormant reset slot. Malformed validation retains redaction and releases the lease exactly once through v0.138.0 cleanup. Trailer HEADERS require END_STREAM and close exactly once.
- When that final transaction makes the first event for a peer-initiated stream
  application-visible, atomically advance the v0.122.0
  `PublishedPeerStreamHighWater` with the same commit. Parsed, mapped,
  unpublished, policy-rejected, synchronization-only, reset, and capacity-failed
  streams never advance it. Once a final GOAWAY cutoff has Frozen, the
  publication gate rejects every higher stream before visibility while
  preserving required HPACK and connection flow-control work.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Informational responses and trailers and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Pause after every v0.125.0–v0.131.0 semantic stage and cross initial, informational, final, and trailer HEADERS with END_STREAM/END_HEADERS, peer reset, GOAWAY, connection failure, capacity exhaustion, valid/missing/malformed status, pseudo-fields, names, values, and HPACK success/failure. Prove no intermediate stage releases/reuses the dormant slot or publishes, 1xx+END_STREAM and malformed blocks re-arm once, peer reset aborts without publication after required HPACK drain, GOAWAY alone preserves the active pipeline, connection teardown owns cleanup, valid terminal blocks release only at the final owner, and exactly one terminal/error action commits. Cross peer/local initiation and publication immediately before/after final-cutoff exposure; prove atomic high-water advancement only with visibility and post-freeze synchronization without higher-stream publication.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational responses and trailers contract and all previously implemented relevant behavior have
reproducible evidence; v0.130.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) still passes; no behavior assigned to v0.132.0 (Cookie field combination and Set-Cookie preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.131.0 implementation stop reached. Run pentest for this exact commit.`

### v0.132.0 — Cookie field combination and Set-Cookie preservation

Status: planned

#### Goal

Deliver **Cookie field combination and Set-Cookie preservation** as the sole primary capability in this stop. It builds
on v0.131.0 (Informational responses and trailers) and must be independently trustworthy before v0.133.0 (Stream flow control) begins.

#### Deliverables

- Acceptance contract: When mapping HTTP/2 requests, concatenate multiple Cookie values in arrival order with exactly semicolon plus SP for the semantic cookie view while retaining source lines; never combine Set-Cookie response fields, preserve their order and bytes independently, and enforce field/output limits before producing either view.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cookie field combination and Set-Cookie preservation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cookie field combination and Set-Cookie preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.131.0 (Informational responses and trailers) still passes; no behavior assigned to v0.133.0 (Stream flow control) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 — Stream flow control

Status: planned

#### Goal

Deliver **Stream flow control** as the sole primary capability in this stop. It builds
on v0.132.0 (Cookie field combination and Set-Cookie preservation) and must be independently trustworthy before v0.134.0 (Connection flow control) begins.

#### Deliverables

- Acceptance contract: Maintain a checked signed send and nonnegative receive window per stream, charge the entire DATA payload before application publication or PendingConnect capacity disposition, including DATA received while AwaitingConnectOutcome, reject receive underflow with stream FLOW_CONTROL_ERROR, reject increment overflow with stream FLOW_CONTROL_ERROR, permit negative send windows after SETTINGS reduction, and mutate no connection window on a stream-only failure beyond required DATA accounting; capacity-triggered CANCEL does not restore stream credit before v0.136.0 owns discard/release.
- Establish the outbound stream-credit ledger used by v0.137.0: distinguish checked peer-window availability, generation-bound unexposed reservations, and irrevocable committed debits. Reservable stream credit is the nonnegative remainder after unexposed reservations; no queued frame can reserve from negative availability. This milestone provides the stream-local reservation/commit/release primitive but exposes no DATA frame before v0.134.0 adds the matching connection transaction and v0.137.0 owns frame output.
- Establish the inbound stream ledger as
  `ReceiveCredit { advertised_remaining: i32,
  reclaimed_unadvertised: u32, update_in_flight: u32 }`. Receiving DATA,
  including Pad Length and padding, immediately decrements
  `advertised_remaining` with stream FLOW_CONTROL_ERROR on underflow.
  Consumption is not restoration: application acknowledgement and every
  stream-level discard increase only `reclaimed_unadvertised`. No stream update
  increment can be selected unless checked addition keeps the resulting
  advertised window at or below `2^31 - 1`.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test ordinary, PendingConnect, AwaitingConnectOutcome, capacity-reset, padding, END_STREAM, and receive-underflow stream-window accounting. Test advertised/reclaimed/in-flight independence, padding-only DATA, every underflow prefix, checked update selection, stale generations, and state-neutral failure. Model available/reserved/committed outbound stream credit, negative windows, generation mismatch, exact reservation release, and no reservation from insufficient credit; create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stream flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.132.0 (Cookie field combination and Set-Cookie preservation) still passes; no behavior assigned to v0.134.0 (Connection flow control) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 — Connection flow control

Status: planned

#### Goal

Deliver **Connection flow control** as the sole primary capability in this stop. It builds
on v0.133.0 (Stream flow control) and must be independently trustworthy before v0.135.0 (SETTINGS initial-window active-stream integration and atomic rollback) begins.

#### Deliverables

- Acceptance contract: Maintain checked connection send/receive windows independently from every stream, charge every DATA payload including PendingConnect/AwaitingConnectOutcome bytes even when its stream is capacity-reset or later errors, reject connection-window underflow or increment overflow with connection FLOW_CONTROL_ERROR, apply WINDOW_UPDATE atomically, and expose backpressure without busy progress or hidden buffering; a stream-local CONNECT disposition never skips or double-restores connection accounting before v0.136.0 owns release.
- Extend the outbound ledger with connection available/reserved-unexposed/committed-debited credit. Reserve one exact DATA frame's flow-controlled length atomically against both its stream and the connection or mutate neither and return flow-control backpressure. Competing streams cannot observe or spend another frame's reservation. Stream or connection WINDOW_UPDATE changes checked availability without refunding committed debit; a blocked frame may reserve only in a later deterministic scheduling transaction.
- Add an independent connection `ReceiveCredit` ledger with the same three
  fields as each stream. Every DATA frame debits connection
  `advertised_remaining` even if stream validation, publication, reset, or
  closure later takes a different path. Reclamation updates the stream and
  connection ledgers independently: no stream update can consume, erase, or
  become connection credit, and connection-only post-closure reclamation never
  revives a stream ledger.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test ordinary and pending CONNECT DATA across connection-window boundaries, stream reset, non-2xx, and END_STREAM without skipped/double accounting. Cross every stream/connection advertised-window underflow prefix and prove the required error scope with no fabricated reclamation. Race multiple streams for the final connection octet and prove independent inbound ledgers, atomic outbound dual reservation, losing-stream backpressure, generation isolation, checked WINDOW_UPDATE, and exact paired release/commit; create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.133.0 (Stream flow control) still passes; no behavior assigned to v0.135.0 (SETTINGS initial-window active-stream integration and atomic rollback) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 — SETTINGS initial-window active-stream integration and atomic rollback

Status: planned

#### Goal

Deliver **SETTINGS initial-window active-stream integration and atomic rollback** as the sole primary capability in this stop. It builds
on v0.134.0 (Connection flow control) and must be independently trustworthy before v0.136.0 (HTTP/2 inbound DATA ownership, acknowledgement, and credit release) begins.

#### Deliverables

- Acceptance contract: Apply INITIAL_WINDOW_SIZE deltas to every active stream with checked signed arithmetic and all-or-nothing rollback on overflow; no stream may observe a partial settings transition. Attach one generation-bound window participant to the owning `InboundSettingsTransaction`, regardless of duplicates. Before committing any valid delta, atomically revoke every affected unexposed DATA reservation and release its paired connection reservation, apply entries in wire order, then leave queued frames blocked until they re-reserve under the new windows; report Effective only after all active windows/reservations commit. Frozen/exposed DATA retains its committed debit and exact suffix; a reduction can leave a stream window negative, in which case no later DATA frame becomes exposable until credit recovers. Overflow rolls back windows, reservation ownership, and queue eligibility together, reports connection-fatal failure to the shared transaction, and cannot independently emit its ACK.
- For a locally emitted INITIAL_WINDOW_SIZE, precompute the corresponding
  inbound stream receive-window delta and all-or-nothing rollback snapshot as a
  v0.139.0 outbound commit-plan participant before command acceptance. Apply it
  to every affected existing stream only at full SETTINGS-frame acknowledgement;
  prefixes and peer ACK apply no delta.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Apply increases, reductions, negative-window results, and overflow rollback between command acceptance, reservation, first exposure, partial acknowledgement, and completion; prove unexposed paired reservations revoke/re-reserve exactly, frozen debits never refund, and no stream observes mixed SETTINGS state.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS initial-window active-stream integration and atomic rollback contract and all previously implemented relevant behavior have
reproducible evidence; v0.134.0 (Connection flow control) still passes; no behavior assigned to v0.136.0 (HTTP/2 inbound DATA ownership, acknowledgement, and credit release) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 — HTTP/2 inbound DATA ownership, acknowledgement, and credit release

Status: planned

#### Goal

Deliver **HTTP/2 inbound DATA ownership, acknowledgement, and credit release** as the sole primary capability in this stop. It builds
on v0.135.0 (SETTINGS initial-window active-stream integration and atomic rollback) and must be independently trustworthy before v0.137.0 (HTTP/2 outbound per-stream message command lifecycle) begins.

#### Deliverables

- Acceptance contract: Treat each DATA delivery as a borrowed, generation-checked range; separately record flow-controlled payload length (including Pad Length and padding) and semantic DATA length (excluding both), route ordinary ranges to application Content-Length reconciliation but route CONNECT PendingConnect/AwaitingConnectOutcome/connected ranges only to stream-local bounded tunnel ownership with no application-content event; immediately add padding the application never sees to internal consumed-credit accounting for both stream and connection, permit partial acknowledgement while retaining the suffix, release credit only for acknowledged or policy-discarded octets, and coalesce WINDOW_UPDATE emission under independent threshold, rate, and amplification budgets; replace v0.130.0 capacity-reset-only handling with credit-aware backpressure where caller capacity exists, otherwise reset and release exactly once; keep acknowledgement, discard, cancellation, invalid outcome, non-2xx cleanup, generation, and credit local to that stream while preserving one terminal ordering across DATA, END_STREAM, reset, cancellation, and shutdown. “Release” here means moving exact octets into `reclaimed_unadvertised`, never increasing `advertised_remaining`: DATA already decremented both advertised ledgers before publication, and only the v0.153.0 full-frame output commitment makes an update peer-visible.
- For a policy-rejected promised stream, DATA in reserved(remote) takes the v0.121.0 connection-PROTOCOL_ERROR path before discard accounting, including while its reset is Frozen with only 0..=12 bytes acknowledged; DATA after legal response HEADERS moved the stream to half-closed(local) is discarded with ordinary stream and connection credit. DATA+END_STREAM first charges/discards its full payload and padding, releases each stream/connection credit exactly once, then records remote closure. Only DATA after `ResetOutput::Complete` caused local closure, or after an independent remote closed-state race, consumes/restores connection-level credit alone and must never emit stream WINDOW_UPDATE.
- Define `WindowUpdateOutput::{None, Private { target, generation,
  increment }, Frozen { target, generation, increment, frame: [u8; 13],
  acknowledged: 0..=12 }}`. Before exposure, same-target/same-generation
  reclaimed credit may coalesce with checked arithmetic. First exposure moves
  only the chosen increment from reclaimed to in-flight and freezes target,
  generation, increment, and bytes without restoring advertised credit.
  Reclamation during Frozen remains private for the next update. Stream closure
  may cancel Private stream output, but preserves the independent connection
  reclamation; Frozen finishes unchanged or the connection is abandoned.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Extend the HTTP/2 frame/state harness with every DATA split, partial
  acknowledgement, backpressure, trailers/END_STREAM, reset, cancellation,
  shutdown, stream-slot reuse, all-padding tiny-frame churn, threshold crossing,
  coalescing, amplification-budget, PendingConnect capacity/non-2xx cleanup,
  and ordinary-versus-tunnel publication permutation.
- Assert application acknowledgement, padding discard, and policy discard
  mutate only reclaimed-unadvertised credit. Cross coalescing before and after
  first exposure, reset/closure and connection-only post-reset reclamation,
  stale tokens, and arithmetic ceilings; this milestone does not claim
  advertised restoration before v0.153.0.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 inbound DATA ownership, acknowledgement, and credit release contract and all previously implemented relevant behavior have
reproducible evidence; v0.135.0 (SETTINGS initial-window active-stream integration and atomic rollback) still passes; no behavior assigned to v0.137.0 (HTTP/2 outbound per-stream message command lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 — HTTP/2 outbound per-stream message command lifecycle

Status: planned

#### Goal

Deliver **HTTP/2 outbound per-stream message command lifecycle** as the sole primary capability in this stop. It builds
on v0.136.0 (HTTP/2 inbound DATA ownership, acknowledgement, and credit release) and must be independently trustworthy before v0.138.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) begins.

#### Deliverables

- Acceptance contract: Define capacity-bounded HEADERS, DATA, trailers, and END_STREAM commands per generation-checked stream; reject illegal ordering, duplicate completion, ordinary body-forbidden data, locally generated Content-Length disagreement, local HTTP/2 status 426 as InvalidState, and trailers lacking v0.52.0 field permission, while authentication-info generation remains unavailable until v0.157.2; for 205 require initial response HEADERS with END_STREAM and optional Content-Length: 0, reject every DATA/trailer/nonzero-length command; for an established HTTP/2 CONNECT or RFC 8441 stream expose separate tunnel DATA/finish commands where DATA is not request/response content, forbid later HEADERS/trailers, and preserve directional END_STREAM; keep raw local response HEADERS construction crate-private until v0.182.1 requires the complete frozen `ValidatedResponse` rather than a raw head beside a permit. Apply the v0.25.0 boundary to every frame: private unexposed encoding may be discarded, but first non-empty exposure freezes the frame and an acknowledged prefix resumes only from its remaining suffix. Cancellation preserves compression and mandatory reset/shutdown actions.
- Accepting a command that carries END_STREAM irreversibly seals the application-facing local send direction, so later DATA/trailer/finish commands return `InvalidState`, but acceptance, private encoding, exposure, and partial acknowledgement do not alter `WireStreamState`. Only acknowledgement of the complete frame emits normalized `LocalEndStreamComplete`: Open becomes HalfClosedLocal; HalfClosedRemote becomes Closed and selects `FirstWireClosureCause::LocalEndStreamComplete`; a stream already Closed by peer RST_STREAM records outbound completion without changing state or its first cause. Connection failure before full acknowledgement records only the written prefix and never claims local half-close, closure, or END_STREAM completion.
- For HEADERS or trailers carrying END_STREAM, completion of that entire HEADERS frame—not command acceptance, the first exposed byte, or final CONTINUATION—emits the directional transition. If END_HEADERS is absent, the connection must still retain and finish the complete CONTINUATION/HPACK block under its existing owner after the stream becomes HalfClosedLocal or Closed. The same full-frame rule covers DATA, empty DATA, and initial/trailing HEADERS carrying END_STREAM.
- Represent each ordinary encoded frame as `OrdinaryFrameOutput::{AcceptedPrivate { slot: OutboundFrameSlot, completion, credit }, Frozen { slot: FrozenOutboundFrameSlot, offered, acknowledged, generation, completion, debit }, Complete, SupersededBeforeExposure}`. Peer RST_STREAM, completed local reset, or cancellation may select `SupersededBeforeExposure` only from AcceptedPrivate that is not owned by a FramingCommitted outbound field block, release any unexposed DATA reservation, serialize no byte, and emit no completion hook. First non-empty exposure—including a later zero acknowledgement—atomically freezes the exact slot bytes and converts DATA reservation to committed debit. Frozen output can no longer be superseded: finish its exact suffix before any same-connection RST_STREAM, and invoke its completion hook exactly once at full acknowledgement; if peer reset already closed the stream, record output completion without changing wire state or first-closure attribution. Connection failure owns frozen-prefix cleanup without refund or fabricated completion.
- Use one caller-provided fixed-capacity `OutboundFrameArena` with exclusive generation-checked byte slots and a separate bounded queue-entry table. Require `slot_capacity >= checked_add(9, ResourceProfile::max_outbound_frame_payload)` at configuration; overflow or shortage is typed local capacity failure. Copy each exact encoded DATA frame—nine-byte header, immutable payload, optional Pad Length, and zeroed padding—into one slot before it reaches AcceptedPrivate. The source payload may be released after the copy, but callers cannot access, mutate, or reuse the staged slot until SupersededBeforeExposure, full acknowledgement, or connection-owned cleanup releases it. `ResourceProfile::max_outbound_frame_payload` is checked, nonzero, independent of peer MAX_FRAME_SIZE, and no larger than representable arena/queue-byte capacity. Exhausted byte capacity returns typed local `OutboundFrameStorageCapacity` backpressure, never a peer protocol error; queue byte capacity and queue-entry capacity are measured and exhausted independently.
- Track `OutboundFieldBlock::{Private { stream, generation, hpack: HpackEncoderTransaction, table_update_debt: Option<EncoderTableUpdateDebtLease>, initial, continuations }, FramingCommitted { stream, generation, hpack: HpackEncoderTransaction, transmitted_table_update: Option<EncoderTableUpdateDebt>, remaining_continuations }, HpackCommitted, AbandonedWithConnection}` at connection scope. Define `field_fragment_cap = min(16_384, ResourceProfile::max_outbound_frame_payload, checked_sub(slot_capacity, 9))`; reject zero/overflow and require it to fit the enabled initial frame's mandatory payload prefix (four promised-stream-ID octets for PUSH_PROMISE and five priority octets only when that HEADERS form is enabled). Check `ResourceProfile::max_outbound_field_block_bytes` before encoding. Compute initial fragment capacity after its prefix, then compute `continuation_count = checked_ceil_div(remaining_encoded_block_bytes, field_fragment_cap)` and require it not exceed `ResourceProfile::max_outbound_continuations_per_block`. Before any initial HEADERS/PUSH_PROMISE exposure, linearly lease the exact connection `EncoderTableUpdateDebt`, fully encode its required one or smallest-then-final prefix plus the bounded block, and atomically reserve/materialize the exact initial slot, every CONTINUATION slot, total checked arena bytes, and `checked_add(1, continuation_count)` queue entries. This actual local cap is no larger than the minimum legal peer MAX_FRAME_SIZE, so a valid peer reduction cannot require resegmentation; shortage or oversized locally generated fields returns typed local `OutboundFieldBlockCapacity`/validation failure with zero exposure and restores the debt lease exactly. The whole Private block may be superseded, returning that lease before any newer setting merges and releasing all slots plus provisional HPACK mutations together. First non-empty initial-frame exposure atomically transfers the lease into FramingCommitted and clears only the connection-side debt; the pre-reserved block is then guaranteed to finish and every remaining CONTINUATION is non-supersedable. SETTINGS_HEADER_TABLE_SIZE received after that boundary cannot alter the transferred prefix and accrues debt for the following block after its own ACK commits. No later field block encodes against the provisional transaction or an unresolved transition. Full acknowledgement of the frame carrying END_HEADERS atomically publishes `HpackCommitted` and releases block resources in order. No RST_STREAM, GOAWAY, PING ACK, SETTINGS ACK, WINDOW_UPDATE, or other-stream output can interleave. Fatal transport failure may abandon transferred debt and the transaction/block only with the entire connection. An END_STREAM completion hook on initial HEADERS still runs when that frame is fully acknowledged, independently of final HPACK commit. v0.145.0 applies the same lifecycle to PUSH_PROMISE.
- Each `OutputToken` offered by HTTP/2 owns exactly one frame-slot suffix. Scalar and vectored adapters may expose that suffix but cannot combine it with another slot; a short acknowledgement advances only this slot, exact completion runs only this frame's hook, and an acknowledgement extending into the next frame is `InvalidState` without mutation.
- A response or dependent frame on a locally initiated stream cannot be consumed
  while its request `OutputToken` is outstanding. The combined driver call
  consumes that exact token first; input-only delivery with the live token
  returns `DriverCommitOrderViolation` without parsing, publishing, changing
  HPACK/stream state, or using the response as request commitment evidence.
  After a valid zero/short acknowledgement resolves the offer, ordinary
  protocol rules decide whether the resulting committed prefix permits the
  received frame.
- Before a DATA frame becomes exposable, use checked arithmetic for `payload = data + optional_pad_length_octet + padding`, require payload to fit the peer limit, local cap, both flow-control windows, remaining source, and `slot_capacity - 9` simultaneously, then atomically reserve that entire flow-controlled payload against both ledgers; the nine-byte frame header is not charged. Derive data length only after subtracting checked padding overhead. If requested padding alone cannot fit, follow the configured deterministic padding-reduction policy or return typed local capacity/backpressure; never truncate source data silently or overflow. First exposure atomically commits/debits the reservation before returning bytes. Insufficient/negative credit or stale generation leaves the frame unexposed. Zero-length DATA carrying END_STREAM reserves/debits zero credit but follows the ordinary output and completion lifecycle.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Extend the HTTP/2 frame/state harness with every command ordering, partial
  HPACK/frame write, declared-length boundary, cancellation point, mandatory
  reset path, 205 HEADERS-END_STREAM/Content-Length-zero/nonzero DATA rejection,
  CONNECT tunnel DATA/directional finish, and retry-after-NeedOutput permutation.
  Prove first non-empty initial-frame exposure atomically transfers the lease into FramingCommitted.
  For HEADERS, DATA, trailers, and empty DATA carrying END_STREAM, interleave
  command acceptance, zero/partial/full acknowledgement, remote END_STREAM,
  peer RST_STREAM, CONTINUATION, and connection failure. Prove send sealing at
  acceptance, no premature wire transition, exact full-frame directional
  transition, retained HPACK ownership, correct first cause, and no duplicate
  half-close/close or fabricated completion. Cross AcceptedPrivate,
  private-encoded, Frozen-with-zero-acknowledgement, every partial prefix, and
  Complete with peer reset, completed local reset, cancellation, and failure;
  prove pre-exposure supersession/release, frozen suffix priority, no reset
  interleaving, and one completion hook. Cross Frozen and Complete request
  HEADERS against response input before/with/after output acknowledgement; prove
  reversed input is wholly unconsumed local DriverCommitOrderViolation and the
  combined call commits request output before parsing/publishing the response.
  For DATA, vary payload/padding charge,
  zero-length END_STREAM, stream/connection last credit, concurrent contenders,
  stale generations, WINDOW_UPDATE, and SETTINGS reduction before exposure.
  Exhaust caller-provided frame bytes separately from queue entries; mutate and
  reuse source payload immediately after copy, then attempt staged-slot alias,
  mutation, and reuse before supersession/full acknowledgement/cleanup. Vary
  peer maximum through 16,777,215 while the local payload cap stays fixed.
  For multi-frame HEADERS, reset/cancel/fail before initial exposure, at every
  initial-frame prefix/completion, between CONTINUATION frames, within the final
  CONTINUATION, and after an initial END_STREAM hook; prove whole-block private
  rollback or committed contiguity through END_HEADERS. Exhaust each slot/entry
  needed by the smallest supported local field fragment cap before initial exposure and
  prove zero bytes/HPACK publication; after exposure, exhaust all unrelated
  capacity and reduce peer MAX_FRAME_SIZE while the pre-reserved block still
  completes. Prove provisional HPACK rollback, no later-block dependency,
  final-frame-only HpackCommitted publication, and connection-owned discard.
  Cross absent and pending 0→4096/4096→0→4096 update debt at Private encoding,
  preflight failure, supersession, first non-empty initial exposure, and every
  CONTINUATION boundary; prove exact lease restoration before exposure,
  irreversible transfer at exposure, following-block ownership afterward, and
  encoder/decoder table equivalence after completion.
  Cross zero/overflow, caps below/equal/above each enabled mandatory prefix,
  exact and one-over max field-block bytes, checked ceiling-division boundaries,
  zero/max/one-over continuation count, total arena-byte/entry overflow, and
  oversized generated fields; prove exact local failure before exposure.
  For DATA cross checked slot/header/payload/padding boundaries, padding-only
  overflow/reduction policy, and attempted token acknowledgement into the next
  slot; prove exact arithmetic, no truncation, and one slot/hook per token.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 outbound per-stream message command lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.136.0 (HTTP/2 inbound DATA ownership, acknowledgement, and credit release) still passes; no behavior assigned to v0.138.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 — HTTP/2 body cancellation, reset, and flow-credit lifecycle

Status: planned

#### Goal

Deliver **HTTP/2 body cancellation, reset, and flow-credit lifecycle** as the sole primary capability in this stop. It builds
on v0.137.0 (HTTP/2 outbound per-stream message command lifecycle) and must be independently trustworthy before v0.139.0 (SETTINGS outstanding-ACK accounting) begins.

#### Deliverables

- Acceptance contract: Emit at most one RST_STREAM and implement the exact v0.120.0 `ResetOutput` lifecycle. `Reserved` is mutable/suppressible with no non-empty exposure. On first exposure, construct and retain one generation-bound 13-byte `Frozen` record and token; `reason`, stream ID, length, type, flags, error code, and bytes never change even when acknowledgement is zero. Valid token acknowledgement consumes one offer and advances only its exact prefix; positive prefixes resume at the remaining suffix, while zero re-offers the same frozen bytes under a fresh generation token. Duplicate, oversized, stale, cross-stream/generation, or out-of-order acknowledgement returns `InvalidState` without mutation. `Complete` occurs only at acknowledged byte 13 and is the sole reset-output event permitted to request local wire closure.
- Track reset output, terminal stage/section lease, RFC wire state, remote closure, and first-closure cause independently. Peer RST_STREAM or valid remote completion supersedes only unexposed `Reserved`; malformed semantics re-arms PolicyCancel as StreamError only there. Once `Frozen`, later peer reset, malformed evidence, END_STREAM, or GOAWAY cannot replace/suppress it or create a second reset. `Reserved` and `Frozen` at acknowledged offsets 0..=12 leave the wire state unchanged: reserved(remote) DATA is still connection PROTOCOL_ERROR, legal HEADERS may move it to half-closed(local), and peer RST_STREAM/END_STREAM can close it. On byte 13, apply local-reset closure once only if still non-Closed; otherwise retain the remote first cause and record only outbound completion. Continue any frozen suffix after remote closure while the connection remains usable. Stream-slot/tombstone reuse waits for the frozen record and every output token/prefix obligation. Connection failure invalidates the lease via connection-owned cleanup and records only `acknowledged`, never `offered`, `Complete`, or a local wire transition. Caller-sensitive storage remains redacted and caller-scrubbed after lease termination.
- Adopt the v0.122.0 control disposition for reset output. A fatal intent waits
  behind an already Frozen reset suffix while output remains usable. Full fatal
  GOAWAY commitment moves every still-Private reset to
  `AbandonedByConnectionFatal`, emits no RST_STREAM, runs no
  `LocalResetComplete` hook or wire-state transition, releases its slot and
  tombstone hold exactly once, and makes every outstanding reset token stale.
- Arbitrate a newly required local reset against v0.137.0 ordinary output and `OutboundFieldBlock` before scheduling it. Supersede an unexposed Private field block or unrelated AcceptedPrivate frame in place, release its complete reserved slot/entry set, roll back provisional HPACK work, restore any exact `EncoderTableUpdateDebtLease` before a newer setting can merge, and release unexposed DATA reservations before queueing reset. Once the initial HEADERS/PUSH_PROMISE is exposed, its debt has transferred irreversibly and every remaining CONTINUATION is protected by the FramingCommitted block obligation even while AcceptedPrivate; complete the pre-reserved block through END_HEADERS before reset serialization, then publish HpackCommitted only on final-frame acknowledgement. Outside a framing-committed block, Frozen ordinary output—even with zero acknowledged—retains its slot/debit and finishes its exact frame before reset. Completed ordinary output runs its hook once; connection failure may abandon committed output/HPACK/transferred debt only by abandoning the connection and cannot inject GOAWAY or invent completion/refund.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. At every acknowledged offset 0..=13 inject every legal/illegal inbound frame, policy-to-error re-arm, peer reset, valid/malformed terminal evidence, END_STREAM/END_HEADERS, GOAWAY, connection failure, cancellation, and capacity. Inject stale, duplicate, oversized, cross-generation/out-of-order tokens, caller-buffer reuse, and stream-generation rollover. Prove exact reserved/half-closed/closed legality and credit at each offset, no premature DATA tolerance, immutable suffix continuation, one local close only at full acknowledgement, remote-first closure/cause preservation, state-neutral invalid acknowledgements, partial-failure cleanup without completion/closure, no duplicate reset, and no early record/slot/tombstone reuse. Cross fatal commitment with a Private reset and every Frozen offset; prove the Frozen suffix completes before fatal when usable, while Private abandonment produces no reset bytes, local-completion hook, wire transition, double release, or reusable token. Cross each reset with Private debt lease, initial HEADERS prefixes/completion, every CONTINUATION boundary, final-CONTINUATION prefixes, settings arrival, ordinary Frozen/Complete, and initial END_STREAM hook; prove only whole unexposed blocks restore debt/supersede/release, first exposure prevents restoration, post-exposure changes remain following-block debt, and every committed block reaches END_HEADERS contiguously before reset with encoder/decoder equivalence.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 body cancellation, reset, and flow-credit lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.137.0 (HTTP/2 outbound per-stream message command lifecycle) still passes; no behavior assigned to v0.139.0 (SETTINGS outstanding-ACK accounting) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 — SETTINGS outstanding-ACK accounting

Status: planned

#### Goal

Deliver **SETTINGS outstanding-ACK accounting** as the sole primary capability in this stop. It builds
on v0.138.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) and must be independently trustworthy before v0.140.0 (Bounded stream admission) begins.

#### Deliverables

- Acceptance contract: Represent every locally emitted non-ACK frame as
  `OutboundSettingsTransaction::{ReservedPrivate { generation,
  ordered_entries, frame_slot, future_ack_slot, commit_plan }, Frozen {
  generation, ordered_entries, frame_slot, future_ack_slot, commit_plan,
  total_len, acknowledged }, CommittedAwaitingAck { generation, ack_fifo_slot,
  committed_snapshot, deadline_generation }, PeerAcked,
  AbandonedBeforeExposure, AbandonedConnection}`. Before command acceptance,
  fully validate ordered entries and atomically reserve checked
  `9 + 6 * entry_count` bytes, one output queue entry, one future
  outstanding-ACK FIFO slot, timeout state, and every generation-bound
  local-effect snapshot. Insufficient capacity returns typed local backpressure
  before exposure. First exposure freezes entries and exact bytes; acknowledged
  prefixes below `total_len` change no locally advertised effect and start no
  timeout. Full-frame acknowledgement atomically applies the prevalidated commit
  plan, promotes the already reserved slot into the bounded outstanding FIFO in
  committed wire order, and starts its injected-monotonic generation-bound
  timeout. Peer ACK consumes the oldest CommittedAwaitingAck record exactly once
  without reapplying effects; multiple local frames preserve commitment order,
  and any ACK with no committed transaction is unsolicited connection
  PROTOCOL_ERROR even when a ReservedPrivate/Frozen transaction exists. Track `locally_requested`,
  `frozen_on_wire`, `locally_advertised_committed`, and `peer_acknowledged`
  separately.
- Never retain, defer, or later consume an ACK received without a
  CommittedAwaitingAck owner. It cannot cancel a timeout, set
  `peer_acknowledged`, enable an ACK-gated setting/extension, or act as evidence
  of output commitment. v0.20.0/v0.25.0 require the driver to report the complete
  SETTINGS output acknowledgement before feeding a causally possible ACK; a
  reversed independent call returns local `DriverCommitOrderViolation` before
  protocol parsing, while a peer ACK that legitimately reaches this protocol
  state with no committed owner selects connection PROTOCOL_ERROR. Fatal GOAWAY
  before exposure selects AbandonedBeforeExposure and applies nothing. Fatal
  intent while Frozen waits for its exact suffix and commitment before GOAWAY
  when output remains usable. Terminal shutdown after CommittedAwaitingAck
  releases timeout/FIFO ownership without rolling back possibly peer-visible
  effects.
- Committed records enter the bounded FIFO only after each complete frame's bytes commit;
  their capacity is nevertheless reserved before exposure and cannot fail at
  promotion.
- The commit plan is the sole wire-commit authority for every enabled locally
  advertised effect: decoder header-table capacity, stream initial receive
  windows, inbound MAX_FRAME_SIZE readiness, inbound concurrent-stream
  admission, header-list guidance, ENABLE_PUSH and
  ENABLE_CONNECT_PROTOCOL directionality, and enabled extension settings. Each
  owning milestone attaches a prevalidation/apply operation to this plan; no
  effect may activate at request, reservation, first exposure, a prefix, or peer
  ACK.
- Independently activate the v0.108.0 connection-wide `InboundSettingsTransaction` for received non-ACK frames: fully validate ordered entries; reserve its sole ACK before mutation; then attach HPACK, stream-window, MAX_FRAME_SIZE, admission/MAX_CONCURRENT_STREAMS, ENABLE_PUSH, known extension, and other enabled participant obligations to that frame generation. Apply entries in wire order without intervening frame processing. Every-participant Effective moves WaitingParticipants to AckEligible; first ACK exposure moves to AckFrozen, acknowledged offsets 0..=8 remain uncommitted, and only acknowledgement of all nine bytes moves to AckCommitted. Several eligible/frozen transactions retain receive order for both serialization and wire commitment; later transactions cannot overtake a partial earlier ACK. Retain each transaction and every dependent HPACK owner reference until AckCommitted. For an encoder-limit obligation, that exact event advances `peer_wire_acknowledged_ceiling` to the frame's stored received-ceiling snapshot and merges only its optional selected-capacity update into separate unsignaled debt; a raw ceiling increase neither selects capacity nor creates debt. Unknown settings attach no participant but remain covered by the same single ACK; duplicate entries never create another ACK. Any connection-fatal participant before exposure cancels pending transactions; stale/invalid output acknowledgement is state-neutral, while transport failure after partial ACK output atomically selects AbortedConnection for every uncommitted transaction and exposes no dependent field block. Rolled-back Private re-encoding is not a participant, begins only after the selected update merges, and cannot delay AckEligible or ACK output.
- Full fatal GOAWAY commitment moves every AckEligible but still-Private
  transaction to `AbandonedByConnectionFatal`, not AckCommitted: it emits no
  ACK, advances no peer-wire-acknowledged ceiling, merges no selected delta or
  HPACK debt, releases all participant/slot ownership exactly once, and makes
  transaction and output tokens stale. An AckFrozen suffix still finishes
  before fatal while output is usable.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Build combined SETTINGS frames spanning HEADER_TABLE_SIZE 0/4096/`u32::MAX`, INITIAL_WINDOW_SIZE, MAX_FRAME_SIZE, MAX_CONCURRENT_STREAMS, ENABLE_PUSH, duplicate and unknown entries. Cross every entry order, small physical arenas, selected policy, Private/FramingCommitted HPACK state, participant failure, ACK capacity/offsets, multiple queued transactions, cancellation, GOAWAY, stale tokens, transport failure, and generation reuse. Prove one frame ACK, FIFO snapshot commitment, acknowledged ceiling changes only at byte nine, selected-only debt, no automatic increase, retained owners through byte eight, no mutation before validation/reservation, and no dependent exposure after partial failure.
- For outbound transactions, exhaust frame/queue/future-ACK/timeout/commit-plan
  capacity independently, including one-slot-short outstanding FIFOs; cross
  empty/single/multiple/duplicate/unknown entries, every exact frame offset,
  several committed frames, ACK ordering, speculative ACK input, timeout generations,
  fatal shutdown at every lifecycle state, partial failure, stale tokens, and
  generation reuse. Prove zero exposure on reservation failure, immutable
  ordered bytes, final-byte-only effect activation/FIFO promotion/deadline,
  one oldest-record ACK with no effect reapplication, PROTOCOL_ERROR for every
  ReservedPrivate/Frozen offset and after full offer before acknowledgement,
  no timeout/peer-acknowledged/feature mutation, acknowledgement-first combined
  processing, state-neutral local driver-order failure, unknown visibility on
  partial failure, and no rollback after commitment.
- Cross fatal commitment with every transaction state and AckFrozen offset.
  Prove Frozen completion precedes fatal when usable and Private abandonment
  neither commits an ACK nor advances a ceiling/debt, releases every owner
  once, and cannot be revived by a stale or reused-generation token.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS outstanding-ACK accounting contract and all previously implemented relevant behavior have
reproducible evidence; v0.138.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) still passes; no behavior assigned to v0.140.0 (Bounded stream admission) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 — Bounded stream admission

Status: planned

#### Goal

Deliver **Bounded stream admission** as the sole primary capability in this stop. It builds
on v0.139.0 (SETTINGS outstanding-ACK accounting) and must be independently trustworthy before v0.141.0 (SETTINGS max-concurrent-streams admission integration) begins.

#### Deliverables

- Acceptance contract: Count open, half-closed-local, and half-closed-remote streams against concurrency while excluding reserved streams; reject a peer stream above the advertised inbound limit with stream PROTOCOL_ERROR or REFUSED_STREAM, using REFUSED_STREAM only while VEF can prove no application processing occurred; distinguish internal stream-table capacity exhaustion from peer misconduct when the peer remains within the advertised limit; and reserve/release each generation-checked slot exactly once across open, reset, close, GOAWAY, and cancellation races.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded stream admission contract and all previously implemented relevant behavior have
reproducible evidence; v0.139.0 (SETTINGS outstanding-ACK accounting) still passes; no behavior assigned to v0.141.0 (SETTINGS max-concurrent-streams admission integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 — SETTINGS max-concurrent-streams admission integration

Status: planned

#### Goal

Deliver **SETTINGS max-concurrent-streams admission integration** as the sole primary capability in this stop. It builds
on v0.140.0 (Bounded stream admission) and must be independently trustworthy before v0.142.0 (Bounded outbound scheduling) begins.

#### Deliverables

- Acceptance contract: Apply peer MAX_CONCURRENT_STREAMS to local outbound admission and VEF's advertised value to inbound policy; attach generation-bound admission participation to the owning `InboundSettingsTransaction` and report Effective only after the ordered limit change is visible. Count open and both half-closed states, exclude reserved streams, and do not terminate existing streams solely because a later setting reduces the limit; reject only new excess peer streams with stream PROTOCOL_ERROR or REFUSED_STREAM, permit REFUSED_STREAM only before any application processing, and report independent local stream-table exhaustion as capacity/policy rather than peer violation. Admission never owns/emits the frame ACK; fatal participant failure aborts the shared transaction.
- Prevalidate every locally advertised MAX_CONCURRENT_STREAMS value against
  fixed stream-table/admission capacity and attach its inbound-admission
  transition to the outbound SETTINGS commit plan. Full frame acknowledgement
  alone changes the locally advertised committed limit; reservation, prefixes,
  and peer ACK do not.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS max-concurrent-streams admission integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.140.0 (Bounded stream admission) still passes; no behavior assigned to v0.142.0 (Bounded outbound scheduling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.141.0 implementation stop reached. Run pentest for this exact commit.`

### v0.142.0 — Bounded outbound scheduling

Status: planned

#### Goal

Deliver **Bounded outbound scheduling** as the sole primary capability in this stop. It builds
on v0.141.0 (SETTINGS max-concurrent-streams admission integration) and must be independently trustworthy before v0.143.0 (SETTINGS max-frame-size outbound integration) begins.

#### Deliverables

- Acceptance contract: Once HEADERS or PUSH_PROMISE begins without END_HEADERS, emit only CONTINUATION frames for that same stream until the block commits; flow-controlled DATA cannot block mandatory control output or runnable unrelated streams; reserve application-independent capacity for RST_STREAM, SETTINGS ACK, PING ACK, WINDOW_UPDATE, and GOAWAY; cancellation cannot strand a partially emitted HPACK block; deterministic tie-breaking and bounded starvation hold under continuous higher-priority arrivals; and SETTINGS frame-segmentation changes affect only uncommitted frames. Use one connection-wide total order: (1) the outstanding Frozen frame suffix, (2) the next frame of an active FramingCommitted HEADERS/PUSH_PROMISE/CONTINUATION obligation, (3) fatal GOAWAY, (4) PING ACK, (5) SETTINGS ACK, (6) graceful GOAWAY, (7) RST_STREAM, (8) WINDOW_UPDATE, (9) outbound non-ACK SETTINGS, then (10) ordinary output. Graceful GOAWAY therefore precedes RST_STREAM, but unlike fatal GOAWAY leaves existing-stream controls operational. Before normal scheduling activates, the reserved initial SETTINGS is the sole eligible frame after the client preface or at server startup until full commitment.
- Scheduling a frozen mandatory-control record never regenerates it from live stream state. An outstanding token owns its offered range; after acknowledgement, schedule exactly the frozen unacknowledged suffix before record reclamation. Stream/tombstone generation changes cannot retarget a queued/frozen frame.
- Dispose both RFC urgency rules explicitly. Fatal GOAWAY is the terminal
  exception permitted ahead of PING ACK's priority SHOULD. PING ACK otherwise
  precedes not-yet-exposed SETTINGS ACK, while SETTINGS "immediately" means FIFO
  service at the first scheduler transaction allowed by committed framing,
  fatal state, and the finite bypass gates below. First PING exposure freezes
  its exact 17-byte frame; later identical PINGs, control demand, correlation
  events, cancellation, or priority changes cannot replace or deduplicate it.
- Preserve FIFO ordering within every class. Stamp each record with immutable
  enqueue ordinal, class, connection generation, and record generation; these
  fields deterministically break equivalent ties without caller clock input.
  Within its class, choose the oldest eligible PING.
  `ControlServiceProfile` provides positive `max_consecutive_ping_acks`,
  positive per-waiting-record `max_control_bypass`, and a positive
  `settings_ack_service_ticks`. Every completed higher nonfatal class increments
  an older Private mandatory record's bypass count. At its bound, gate all
  unexposed higher nonfatal classes until the oldest bound-reached record is
  exposed; Frozen/FramingCommitted/fatal output is never gated. A SETTINGS ACK
  deadline starts only at AckEligible. Injected monotonic expiry saturates its
  bypass count and closes the same gate at the next scheduler transaction; it
  cannot reorder a Frozen suffix, committed field block, or fatal GOAWAY, and a
  local missed deadline is never blamed on the peer. Thus absent fatal cleanup,
  each mandatory record is exposed after at most its configured number of
  higher-class completions once eligible, even under continuous admitted PINGs.
  An accepted later outbound SETTINGS transaction is a distinct class with the
  same positive per-record bypass guarantee; ordinary output cannot starve it.
- This milestone defines and model-checks the ordering hook over finite eligible
  records but does not activate live PING ACK output. v0.153.0 activates it only
  after v0.147.0/v0.150.0 install the pre-mutation rate/work ceilings needed to
  preserve the scheduler's bounded-starvation security contract under a
  continuous PING source.
- Schedule each `WindowUpdateOutput` as one exclusive protocol record.
  FramingCommitted field-block output blocks its serialization while credit may
  continue accumulating in the private ledger. Outside that obligation, first
  non-empty exposure freezes exactly one stream-or-connection target,
  generation, increment, and 13-byte frame. Later reclamation, stream closure,
  reset, generation reuse, priority change, and other update demand cannot
  replace its suffix or convert a stream update into a connection update.
- Schedule each `GoawayOutput` as one exclusive terminal record. Existing
  Frozen frame suffix and FramingCommitted CONTINUATION ownership finish first.
  Before exposure, a fatal winner may replace ReservedPrivate graceful output;
  first non-empty exposure freezes stage, cutoff, error, owned debug bytes,
  total length, slot, and generation. No later stream publication, fatal cause,
  timer, PING/control demand, or shutdown request can rewrite that suffix.
  After completion, a pending fatal successor occupies fatal-GOAWAY class ahead
  of every nonterminal class and must carry a non-increasing cutoff.
- Preserve each v0.137.0 END_STREAM frame's completion hook through scheduling and fragmentation: only acknowledgement of that frame's final byte can emit `LocalEndStreamComplete`. Priority changes, interleaved streams, CONTINUATION ownership, zero/short writes, cancellation, and connection failure cannot run the hook early or twice; command-level send sealing remains independent from wire-state transition.
- Treat each unexposed DATA reservation as a linear scheduler capability bound to one stream generation, connection generation, immutable frame layout, and queue entry. Arbitration may revoke/release it before exposure; first exposure consumes it into a non-refundable debit. A Frozen ordinary frame owns connection framing until its suffix completes, so mandatory RST_STREAM waits behind that frame but ahead of later ordinary work. WINDOW_UPDATE or SETTINGS changes wake/revoke eligible reservations without allowing two streams to spend the same connection credit.
- Make FramingCommitted `OutboundFieldBlock` the scheduler's highest framing obligation. Admission exposes its initial frame only after every worst-case-fragmented slot and queue entry through END_HEADERS is atomically reserved/materialized. From first initial-frame exposure through final-frame acknowledgement, select only its exact current suffix or next pre-reserved CONTINUATION; individual AcceptedPrivate disposition and later local capacity exhaustion cannot authorize supersession. All required control queues remain reserved but blocked behind that obligation. A connection-fatal protocol decision waits to emit GOAWAY until END_HEADERS if output remains usable; fatal transport failure abandons block, provisional HPACK transaction, and connection with no further bytes.
- Serialize encoder work, SETTINGS_HEADER_TABLE_SIZE obligations, and selected-capacity debt. No new field-block encoding is runnable while a Private/FramingCommitted transaction or `PendingEncoderTableSizeTransition` is unresolved. A peer reduction before Private exposure supersedes that block, restores its debt lease, clamps/evicts selected state, and records selected update; an increase changes received ceiling only. Behind FramingCommitted, its transferred prefix is immutable while the future encoder state clamps immediately and the per-frame obligation waits. Schedule the one all-effective ACK in FIFO order and retain its received-ceiling snapshot plus optional selected delta through offsets 0..=8. Final-byte AckCommitted advances only that snapshot and merges only that delta; local policy increases remain blocked by the acknowledged/profile/physical minimum. The next Private block may lease selected debt, and first exposure transfers it. Invalid/stale tokens change nothing, output backpressure preserves all ownership, and transport failure abandons the connection without dependent exposure.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Model-check field-block contiguity, mandatory-control preemption, cross-stream
  progress, cancellation at every partial-output boundary, deterministic ties,
  starvation ceilings, SETTINGS changes at every commit boundary, and exactly
  one END_STREAM completion hook only at its frame's full acknowledgement.
  Exhaust competing-stream reservations at the final connection credit and
  reset/cancel every AcceptedPrivate/Frozen boundary; prove paired credit and
  whole-frame-before-reset ordering.
- Cross SETTINGS ACK offsets 0..=9, multiple table-size-owning transactions,
  0→4096 and 4096→0→4096 collapse, debt waiting before a block, Private lease
  rollback, first exposure, every CONTINUATION boundary, exact suffix
  backpressure, stale tokens, and failure before byte nine; prove FIFO
  AckCommitted merge, oldest-minimum preservation, post-exposure following-block
  debt, and encoder/decoder table equivalence after rollback/completion.
  Start multi-frame HEADERS/PUSH_PROMISE blocks, then enqueue every mandatory
  control type and other-stream output at each initial/CONTINUATION prefix;
  prove no interleaving, no per-frame supersession, END_STREAM hook independence,
  and connection-abandonment-only escape. Exhaust capacity before preflight and
  after FramingCommitted; prove zero exposure in the first case and guaranteed
  completion from already owned slots/entries in the second.
- For stream and connection WINDOW_UPDATE records, cross FramingCommitted
  blocking, first exposure, every acknowledged offset 0..=13, new reclamation
  while Frozen, reset/closure/reuse, stale/cross-record tokens, zero/short
  writes, and transport failure. Prove immutable suffix scheduling and no
  advertised-credit mutation at offsets 0..=12.
- Enqueue distinct and identical PING transactions before, during, and after a
  frozen ordinary/control suffix and every fragmented field-block boundary.
  Prove the committed suffix and mandatory CONTINUATION sequence finish first,
  then every eligible PING ACK wins in FIFO order without coalescing; zero/short
  writes, stale/cross-record tokens, and transport failure never change bytes or
  reclaim a transaction early.
- Block ReservedPrivate GOAWAY behind every ordinary/control Frozen suffix and
  each initial/CONTINUATION prefix, then cross first exposure and every
  `17 + debug_len` split. Inject graceful timers, publication, and fatal causes
  at every boundary; prove no interleaving or rewrite, final-cutoff snapshot at
  exposure, and at most one eligible fatal successor after completion.
- Make every pair and all five mandatory control classes eligible together.
  Permute enqueue ordinals/generations, expire SETTINGS deadlines, and run
  continuous budget-admitted PINGs through each positive bypass boundary.
  Prove the exact total order, FIFO/tie stability, fatal-over-PING exception,
  SETTINGS deadline gating without committed-byte reordering, and finite
  service bounds for SETTINGS ACK, graceful GOAWAY, RST_STREAM, and
  WINDOW_UPDATE.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded outbound scheduling contract and all previously implemented relevant behavior have
reproducible evidence; v0.141.0 (SETTINGS max-concurrent-streams admission integration) still passes; no behavior assigned to v0.143.0 (SETTINGS max-frame-size outbound integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 — SETTINGS max-frame-size outbound integration

Status: planned

#### Goal

Deliver **SETTINGS max-frame-size outbound integration** as the sole primary capability in this stop. It builds
on v0.142.0 (Bounded outbound scheduling) and must be independently trustworthy before v0.144.0 (GOAWAY cutoff and retry classification) begins.

#### Deliverables

- Acceptance contract: Maintain three distinct checked values: the peer-advertised limit governing VEF outbound segmentation, VEF's effective locally advertised inbound limit governing received frames (initially 16,384), and the absolute RFC maximum 16,777,215; a larger local inbound limit becomes enforceable no later than commitment of the complete outbound SETTINGS frame that advertises it, while a reduction never retroactively invalidates an already accepted or partially received frame. Attach MAX_FRAME_SIZE handling to its owning `InboundSettingsTransaction`, apply ordered valid values/resegmentation atomically, and report Effective without owning the frame ACK; failure aborts the shared transaction. Segment ordinary queued frames against the peer limit effective when each frame's bytes commit, while every field block uses `field_fragment_cap = min(16_384, max_outbound_frame_payload, checked_sub(slot_capacity, 9))` and its checked mandatory-prefix/block-byte/continuation limits before initial exposure; never allocate directly from an advertised value. For DATA calculate `payload_budget = min(peer_max_frame_size, ResourceProfile::max_outbound_frame_payload, available_stream_credit, available_connection_credit, checked_sub(slot_capacity, 9))`, calculate `padding_overhead = optional_pad_length_octet + padding` with checked arithmetic, reject or deterministically reduce padding when overhead exceeds the budget, then select `data = min(remaining_source, checked_sub(payload_budget, padding_overhead))`. The exact payload is data plus overhead; never silently truncate beyond explicit source progress. The peer's possible 16,777,215-byte maximum is only an upper bound and never requires equivalent local storage. Replacing an unexposed ordinary segmentation releases its slot and paired reservation before reserving the replacement; Frozen layout/slot/debit never changes.
- Attach the checked locally advertised inbound MAX_FRAME_SIZE readiness
  transition to the v0.139.0 outbound commit plan. Only full SETTINGS
  acknowledgement activates the frozen value for subsequently received frame
  boundaries; a prefix, early peer ACK, or later peer ACK cannot activate or
  reapply it.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test increase/reduction activation at every outbound SETTINGS byte split,
  partially received inbound frames across a reduction, queued commands across
  peer-limit changes, DATA resegmentation with paired reservation release,
  frozen-layout stability, local payload caps below/equal peer limits, maximum
  peer value with small staging arenas, separate byte/entry exhaustion,
  field-block preflight at every supported local fragment cap followed by peer reduction, checked 9-byte
  slot addition/subtraction, zero/max padding overhead, padding-only shortage,
  deterministic padding reduction versus typed capacity, exact remaining-source
  progress, rollback, ACK ordering, and absolute-boundary values.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS max-frame-size outbound integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.142.0 (Bounded outbound scheduling) still passes; no behavior assigned to v0.144.0 (GOAWAY cutoff and retry classification) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 — GOAWAY cutoff and retry classification

Status: planned

#### Goal

Deliver **GOAWAY cutoff and retry classification** as the sole primary capability in this stop. It builds
on v0.143.0 (SETTINGS max-frame-size outbound integration) and must be independently trustworthy before v0.145.0 (Server-push lifecycle) begins.

#### Deliverables

- Acceptance contract: Record received and fully wire-committed sent GOAWAY cutoffs in separate ledgers, both monotonically non-increasing. Requested, ReservedPrivate, Frozen, and partially acknowledged local values do not mutate `SentGoawayCutoff`; only the exact completion event from v0.153.0 may do so. On partial transport failure record `PeerVisibleCutoff::UnknownAfterPartial` without inventing a sent cutoff. Classify locally initiated streams above the peer's received cutoff as possibly unprocessed and those at/below separately, reject new streams after the cutoff, and never equate cutoff classification with replay authorization or duplicate terminal events. A received cutoff above the prior value retains the prior lower cutoff and yields typed `ReceivedGoawayCutoffIncrease` connection PROTOCOL_ERROR rather than widening admission/retry state.
- Never use received GOAWAY or later peer input as evidence that a local GOAWAY
  prefix committed. When interpretation depends on the local committed cutoff,
  apply the v0.25.0 acknowledgement-first combined call or reject reversed
  driver delivery locally before cutoff/retry mutation.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cross requested/reserved/frozen/partial/complete/abandoned sent states, multiple decreasing received/sent cutoffs, equal cutoffs, illegally increasing received cutoffs, stale generations, stream classification, and transport failure. Prove monotonic ledgers, prior-cutoff retention on violation, unknown partial peer visibility, no early sent mutation, and no cutoff-derived replay permit.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY cutoff and retry classification contract and all previously implemented relevant behavior have
reproducible evidence; v0.143.0 (SETTINGS max-frame-size outbound integration) still passes; no behavior assigned to v0.145.0 (Server-push lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.144.0 implementation stop reached. Run pentest for this exact commit.`

### v0.145.0 — Server-push lifecycle

Status: planned

#### Goal

Deliver **Server-push lifecycle** as the sole primary capability in this stop. It builds
on v0.144.0 (GOAWAY cutoff and retry classification) and must be independently trustworthy before v0.146.0 (ALPN and cleartext prior-knowledge selection) begins.

#### Deliverables

- Acceptance contract: Integrate SETTINGS_ENABLE_PUSH directionally: clients reject server use that violates the effective setting, servers never advertise it, and receipt of PUSH_PROMISE from a client is connection PROTOCOL_ERROR; before publication validate the complete promised request field section, require a recognized method classified both safe and cacheable, prohibit content indication and trailers, and require connection-/generation-bound PushAuthorityEvidence carrying caller-certified authenticated TLS origin metadata, caller-certified cleartext endpoint authority, or explicitly configured proxy authority without depending on v0.190.0 coalescing; invalid promised semantics produce promised-stream PROTOCOL_ERROR without resetting or mutating the associated stream; for outbound servers require the associated stream open/half-closed(remote), while receiving clients observe the equivalent open/half-closed(local); atomically validate associated legality, promised server-ID availability, peer permission, GOAWAY cutoff, and a separate bounded reserved-push-slot/work budget before reservation; reserved streams do not count against SETTINGS_MAX_CONCURRENT_STREAMS and reservation remains legal at zero, but opening the promised response enforces the then-current concurrent-stream limit; cancellation/reset reclaims exactly once; pushed responses carry typed cacheability metadata and every non-cacheable response is marked forbidden for cache storage even though storage remains outside VEF. Keep the validated promised request, trusted authority/push-policy provenance, and reserved slot unpublished and rollback-capable until the admission transaction commits. The promised slot includes or pre-reserves its v0.117.0 in-place rejection-tombstone/cutoff representation, so accepting PUSH_PROMISE makes the promised ID continuously tracked through publication, rejection, or bounded connection shutdown. At v0.145.0 the transaction's participants are the promised-stream slot/work and rejection tracking; v0.181.0 adds assembly invalidation and independent pushed provenance at the same prepublication gate. No v0.145.0-only pushed response has partial-retention or cross-request assembly authority.
- A promised ID, reserved slot, validated request, or unpublished pushed response
  does not advance `PublishedPeerStreamHighWater`. Only the same atomic commit
  that makes the peer-initiated pushed stream's first validated response event
  application-visible advances it. If final GOAWAY cutoff exposure already
  froze a lower value, keep the promised stream tracked and finish HPACK/credit
  obligations but reject publication and assembly authority.
- ENABLE_PUSH processing attaches a generation-bound push participant to the owning `InboundSettingsTransaction`, applies duplicate values in wire order, and reports Effective only after directional validation/state mutation. It never owns the SETTINGS ACK; an invalid role/value reports connection-fatal failure to the shared transaction so no other participant can expose an ACK.
- A locally emitted ENABLE_PUSH value is prevalidated for role/direction and
  attached to the v0.139.0 outbound commit plan. The local advertised-committed
  policy changes only on full frame acknowledgement and is never reapplied by
  peer ACK.
- PUSH_PROMISE field blocks use the exact v0.137.0 debt lifecycle: Private encoding leases unsignaled table-size history, rollback returns it before any newer setting merges, first non-empty PUSH_PROMISE exposure transfers it irreversibly to the guaranteed CONTINUATION sequence, and later settings create debt only for the following HEADERS/PUSH_PROMISE block.
- Rejected promised streams use the v0.118.0 orthogonal model: policy, wire state, remote/first-closure cause, `ResetOutput`, output-token generation/cursor, compression workspace, immutable `TerminalFieldSectionLease`, terminal stage, and active block remain distinct. HPACK success moves the section lease into semantics. Final valid/malformed/peer-reset outcomes may change only an unexposed reserved reset; a frozen CANCEL remains the sole immutable frame and continues from its acknowledged suffix. Prefixes 0..=12 retain prior frame legality; completion at 13 applies one local close only when remote closure has not already won. Connection-fatal failure owns cleanup and records acknowledged bytes only.
- Define a total auditable `RejectedPushFrameDisposition` matrix keyed by policy/wire/remote-closure/first-closure state, every ResetOutput state/reason/generation/offered/acknowledged value and outstanding-token state, terminal stage, workspace/section lease state/capacity, normalized event/END flags, header phase, and active block, with no wildcard/default cell. Every cell declares protocol/error scope, wire transitions, output exposure/freeze/offer/ack/suffix action, HPACK/lease action, application visibility, credit, reset arbitration, peer-reset abort, redaction, and fatal cleanup owner. Wire transitions additionally distinguish local completion, remote-first no-op completion, and partial-prefix non-transition.
- Implement RFC 9113's in-flight PUSH_PROMISE exception for an associated stream with a locally initiated reset. Retain its generation-checked tombstone from reset intent through the closed-stream classification horizon and any active field block; accept and completely decode PUSH_PROMISE plus every CONTINUATION in either ordering around full reset acknowledgement and `LocalResetComplete`, preserving valid HPACK changes. Validate and continuously track the promised ID, publish no promised request, and recreate no application, authority, push-policy, invalidation, or assembly provenance. Missing recycled associated-request provenance selects safe promised-stream rejection through the same pending-CANCEL state machine, not connection PROTOCOL_ERROR merely because the associated stream completed local reset. Illegal promised IDs remain connection PROTOCOL_ERROR and malformed HPACK remains connection-fatal; capacity failure retains bounded tracking or commits the typed shutdown path.
- Outbound PUSH_PROMISE reuses the v0.137.0 connection-scoped `OutboundFieldBlock`: require `field_fragment_cap >= 4`, subtract the promised-stream-ID prefix before its initial HPACK fragment, checked-ceiling-divide the remainder, and atomically materialize/reserve every exact PUSH_PROMISE/CONTINUATION slot and queue entry plus its provisional HPACK transaction before exposure. Its whole Private block may roll back, but first exposure selects FramingCommitted and guarantees drain through END_HEADERS against reset, GOAWAY, control replies, other streams, application cancellation, peer MAX_FRAME_SIZE reduction, and later local exhaustion. Promised-/associated-stream policy changes cannot supersede an individual continuation; final-frame acknowledgement publishes HpackCommitted, while only whole-connection abandonment discards an exposed transaction.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test client-originated PUSH_PROMISE failure and all prior authority/admission cases. At reset acknowledgement offsets 0..=13 cross every inbound frame, terminal/section state, wire/closure cause, peer reset, END_STREAM/END_HEADERS, malformed re-arm, GOAWAY, failure, stale/duplicate/oversized/out-of-order token, caller-buffer reuse, and stream-generation rollover. Also retain the dynamic-reference/section-lease cases. Prove prior legality and credit through offset 12, no premature closed-stream DATA tolerance, one local close at 13, remote-first cause preservation, immutable suffixes, acknowledged-only diagnostics, and no block/stage/reset/output/section lease stranded, aliased, reused early, or completed twice. Cross promised reservation, response validation, publication immediately before/after final-cutoff exposure, rejection, and synchronization-only completion; prove only atomic visibility advances the processed high-water and post-freeze higher streams gain no application/assembly authority.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Server-push lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.144.0 (GOAWAY cutoff and retry classification) still passes; no behavior assigned to v0.146.0 (ALPN and cleartext prior-knowledge selection) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.145.0 implementation stop reached. Run pentest for this exact commit.`

### v0.146.0 — ALPN and cleartext prior-knowledge selection

Status: planned

#### Goal

Deliver **ALPN and cleartext prior-knowledge selection** as the sole primary capability in this stop. It builds
on v0.145.0 (Server-push lifecycle) and must be independently trustworthy before v0.147.0 (Independent HTTP/2 rate and work budgets) begins.

#### Deliverables

- Acceptance contract: Select encrypted HTTP/2 only from the exact authenticated post-handshake ALPN value h2; absent, unknown, unauthenticated, or pre-handshake ALPN fails closed and never selects HTTP/2; select cleartext prior knowledge only through explicit caller policy or a dedicated endpoint, with no sniffing or guessed HTTP/1 fallback; never reuse bytes consumed under a failed selection; and make the protocol choice immutable once preface processing begins.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test exact and near-match ALPN bytes, every authentication/handshake state,
  explicit/dedicated cleartext policy, failed-selection byte ownership, preface
  fragmentation, and every attempted post-preface protocol switch.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The ALPN and cleartext prior-knowledge selection contract and all previously implemented relevant behavior have
reproducible evidence; v0.145.0 (Server-push lifecycle) still passes; no behavior assigned to v0.147.0 (Independent HTTP/2 rate and work budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 — Independent HTTP/2 rate and work budgets

Status: planned

#### Goal

Deliver **Independent HTTP/2 rate and work budgets** as the sole primary capability in this stop. It builds
on v0.146.0 (ALPN and cleartext prior-knowledge selection) and must be independently trustworthy before v0.148.0 (Rapid-reset defenses) begins.

#### Deliverables

- Acceptance contract: Maintain independent saturating budgets for streams opened/reset, SETTINGS frames and entries, PINGs, CONTINUATION frames and bytes, WINDOW_UPDATE churn, unknown frames and bytes, HPACK work, and generated control output; charge before the governed parse/mutation/admission work, refill deterministically only from the injected monotonic clock, classify exhaustion as a local policy/resource disposition rather than automatic peer PROTOCOL_ERROR, and invoke an optional caller-supplied shared admission/budget hook before connection-local admission so deployments can enforce identity/address/principal limits across reconnects and concurrent connections. For PING, separately charge syntax handling, local-correlation lookup, inbound transaction/payload copy, reply creation, scheduler wake, and output before mutating the FIFO/table or releasing input. Failed lookup, ACK-bearing input, identical payloads, and later shutdown do not refund completed work. Activate v0.142.0 `ControlServiceProfile` with positive checked `max_consecutive_ping_acks`, per-record `max_control_bypass`, and `settings_ack_service_ticks`. Saturate bypass/age counters; a completed higher nonfatal control charges every older eligible lower mandatory record, including accepted later outbound SETTINGS, once, while Frozen, FramingCommitted, fatal, backpressured/no-progress, and abandoned records do not fabricate completions. SETTINGS deadline time comes only from injected monotonic input and closes eligibility gates without changing immutable class/enqueue/generation order. The outbound peer-ACK deadline is separate: it begins only when its complete SETTINGS frame commits and never changes scheduler order.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Exhaust each PING parse/lookup/copy/reply/output charge independently before mutation and prove deterministic refill, no partial FIFO/correlation insertion, no retained caller borrow, no refund, and policy/resource rather than fabricated protocol error. Test service-profile values one, typical, and maximum; saturate each bypass/deadline counter; inject early/equal/late/stale time; and prove finite completed-record bounds, no clock-based tie reorder, no count on backpressure/abandonment, and no peer blame for a local missed SETTINGS service deadline.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HTTP/2 rate and work budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.146.0 (ALPN and cleartext prior-knowledge selection) still passes; no behavior assigned to v0.148.0 (Rapid-reset defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 — Rapid-reset defenses

Status: planned

#### Goal

Deliver **Rapid-reset defenses** as the sole primary capability in this stop. It builds
on v0.147.0 (Independent HTTP/2 rate and work budgets) and must be independently trustworthy before v0.149.0 (SETTINGS amplification defenses) begins.

#### Deliverables

- Acceptance contract: Charge stream creation, initial HEADERS/HPACK work, admission lookup, and reset work before application admission; never refund those charges for immediate RST_STREAM, refusal, cancellation, or connection close; apply both connection-local opened/reset ceilings and the caller-injected shared admission hook before allocating a stream slot; REFUSED_STREAM remains available only before application processing and only when VEF can consume every CONTINUATION, finish the complete HPACK block, and commit its valid table changes without exposing decoded fields, while insufficient HPACK/CONTINUATION work budget or storage requires exactly one bounded connection shutdown action rather than abandonment or compression desynchronization; policy exhaustion never becomes peer PROTOCOL_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Rapid-reset defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Rapid-reset defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.147.0 (Independent HTTP/2 rate and work budgets) still passes; no behavior assigned to v0.149.0 (SETTINGS amplification defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 — SETTINGS amplification defenses

Status: planned

#### Goal

Deliver **SETTINGS amplification defenses** as the sole primary capability in this stop. It builds
on v0.148.0 (Rapid-reset defenses) and must be independently trustworthy before v0.150.0 (PING flood defenses) begins.

#### Deliverables

- Acceptance contract: Charge every SETTINGS frame, six-byte entry, complete prevalidation, shared-transaction reservation, participant mutation, single frame ACK, and emitted local SETTINGS before work/output reservation, with no refund after rollback or reset. Duplicate/mixed entries increase entry/participant work but never ACK count. Process valid entries in wire order without intervening dispatch; bound simultaneous `InboundSettingsTransaction`, ordered-entry leases, pending-participant references, and FIFO ACK slots. Never silently ignore a valid frame when transaction/ACK/output budget is exhausted: before component mutation, commit exactly one bounded shutdown action. Use saturating counters, injected-time refill, and distinct frame/entry/participant/work/output ceilings.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS amplification defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.148.0 (Rapid-reset defenses) still passes; no behavior assigned to v0.150.0 (PING flood defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 — PING flood defenses

Status: planned

#### Goal

Deliver **PING flood defenses** as the sole primary capability in this stop. It builds
on v0.149.0 (SETTINGS amplification defenses) and must be independently trustworthy before v0.151.0 (CONTINUATION bomb defenses) begins.

#### Deliverables

- Acceptance contract: Charge every inbound PING, local correlation lookup, opaque payload copy/comparison, transaction/ACK reservation, scheduler wake, and outbound PING before work, including ACK-bearing frames, with saturating counters and deterministic injected-time refill; a valid non-ACK PING cannot be ignored when ACK capacity is exhausted, so atomically reserve its distinct transaction and ACK or commit exactly one bounded shutdown action. Never coalesce or deduplicate replies, including identical payloads. ACK-bearing PING produces no reply. Queue/rate exhaustion cannot silently drop an obligation, mutate correlation, or pin caller input; classify exhaustion as policy/resource unless the frame itself violates RFC syntax. Reordered exact live-key ACKs complete their own record; unsolicited, duplicate, and stale correlations remain state-neutral and do not refund lookup work.
- Full fatal GOAWAY commitment moves every still-Private reply to
  `AbandonedByConnectionFatal`, records no response-sent/Complete outcome,
  releases its copied payload and slot exactly once, and invalidates its token;
  a Frozen reply completes before fatal while output remains usable. Typed
  terminal abandonment is the only admitted non-reply outcome and never queues
  another fatal action.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PING flood defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Flood distinct and identical non-ACK PINGs, ACK-bearing PINGs, and matching/unsolicited/duplicate/reordered/stale local ACKs through each queue/rate boundary. At every locally originated PING output prefix, cross speculative ACK input, reversed independent delivery, and combined acknowledgement-plus-input; prove no uncommitted match/retention, state-neutral local driver violation, and commitment-before-correlation. Cross fatal commitment with every Private record and Frozen offset; prove Frozen-first completion, typed Private abandonment, no response-sent hook, no duplicate fatal output, exact-once release, and stale-token neutrality. Prove one owned FIFO obligation per accepted non-ACK frame, zero replies for ACK-bearing frames, exact pre-mutation charges, bounded shutdown instead of loss/pinning, and no peer protocol error for correlation mismatch.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING flood defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.149.0 (SETTINGS amplification defenses) still passes; no behavior assigned to v0.151.0 (CONTINUATION bomb defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 — CONTINUATION bomb defenses

Status: planned

#### Goal

Deliver **CONTINUATION bomb defenses** as the sole primary capability in this stop. It builds
on v0.150.0 (PING flood defenses) and must be independently trustworthy before v0.152.0 (WINDOW_UPDATE churn defenses) begins.

#### Deliverables

- Acceptance contract: Charge every CONTINUATION frame, fragment byte, HPACK decode step, field byte, and one-byte-fragment transition before processing with independent saturating ceilings and no refund on semantic rejection; preserve mandatory field-block contiguity and compression synchronization, and on local budget exhaustion stop publication and perform one bounded connection shutdown without converting exhaustion itself into peer PROTOCOL_ERROR.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test CONTINUATION bomb defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION bomb defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.150.0 (PING flood defenses) still passes; no behavior assigned to v0.152.0 (WINDOW_UPDATE churn defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.151.0 implementation stop reached. Run pentest for this exact commit.`

### v0.152.0 — WINDOW_UPDATE churn defenses

Status: planned

#### Goal

Deliver **WINDOW_UPDATE churn defenses** as the sole primary capability in this stop. It builds
on v0.151.0 (CONTINUATION bomb defenses) and must be independently trustworthy before v0.153.0 (Reserved control-output queues) begins.

#### Deliverables

- Acceptance contract: Charge every WINDOW_UPDATE frame, checked increment, target lookup, scheduler wake, and coalesced emitted update before mutation; use saturating frame/work/output counters with deterministic injected-time refill, never refund churn because a stream closes, preserve valid zero/nonzero and overflow RFC dispositions, and treat budget exhaustion as local policy/resource followed by one bounded shutdown action rather than automatic peer PROTOCOL_ERROR. Outbound coalescing is permitted only while Private and only for the same target and generation. Select an increment with checked arithmetic satisfying `advertised_remaining + increment <= 2^31 - 1`; budget exhaustion may delay a private update but cannot merge targets, alter Frozen bytes, count reclaimed credit as advertised, or strand independent connection credit when a stream closes.
- Full fatal GOAWAY commitment moves every still-Private update to
  `AbandonedByConnectionFatal`, restores no advertised credit, releases its
  target/generation ownership exactly once, and invalidates its token; a Frozen
  update completes before fatal while output remains usable.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WINDOW_UPDATE churn defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Exercise tiny acknowledgements and padding-only DATA around threshold/rate/amplification limits, checked same-target coalescing before exposure, reclamation after exposure, maximum-window arithmetic, stream closure, and independent connection progress; Frozen target/increment/bytes never change. Cross fatal commitment with every Private stream/connection record and Frozen offset; prove Frozen-first completion, no advertised-credit restoration for abandonment, exact-once release, and stale-token neutrality.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE churn defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.151.0 (CONTINUATION bomb defenses) still passes; no behavior assigned to v0.153.0 (Reserved control-output queues) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 — Reserved control-output queues

Status: planned

#### Goal

Deliver **Reserved control-output queues** as the sole primary capability in this stop. It builds
on v0.152.0 (WINDOW_UPDATE churn defenses) and must be independently trustworthy before v0.154.0 (HTTP/2 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Reserve independent fixed capacity for required RST_STREAM, SETTINGS ACK, PING ACK, WINDOW_UPDATE, and GOAWAY commands plus their partially committed bytes; application output cannot consume it, cancellation cannot discard it, and valid required replies cannot be silently dropped; when the relevant reserved queue or generation-safe slot is exhausted, coalesce where RFC-safe and otherwise commit exactly one terminal bounded shutdown action with no duplicate control frame. Reserve exactly one nine-byte ACK slot inside each validated `InboundSettingsTransaction`, never inside HPACK/window/admission/push/frame-size participants; retain transaction FIFO order and make that slot eligible only after all participants are Effective. First exposure freezes its bytes and token-bound suffix as AckFrozen; acknowledged offsets 0..=8 retain the slot, transaction, participant outcome, FIFO position, and each encoder obligation's received-ceiling snapshot plus optional selected delta. Only exact final-byte acknowledgement releases the slot, advances the wire-acknowledged ceiling to that snapshot, merges only that selected delta into `EncoderTableUpdateDebt`, and produces AckCommitted; later ACKs cannot commit first. Never put raw peer ceilings into debt, automatically enlarge selection, clear older debt, or let an ACK bypass profile/physical bounds. Duplicate/mixed entries still share the slot. Participant failure cancels before exposure; invalid/stale acknowledgement is state-neutral; transport failure at any frozen prefix marks uncommitted transactions AbortedConnection and exposes no dependent block. FramingCommitted defers ACK serialization; Private rollback restores any debt lease before a selected delta can merge. No subsystem can race an ACK, forge an acknowledged ceiling, fabricate debt, or clear unsignaled history.
- Reserve independent fixed-capacity ownership for each outbound non-ACK
  SETTINGS transaction: checked exact frame bytes/queue entry, a future
  outstanding-ACK FIFO slot, timeout generation, commit-plan snapshots, and one
  immutable FIFO commitment plan are one atomic admission unit. The future slot is
  unavailable to later commands while ReservedPrivate/Frozen and is promoted
  in place at final-byte commitment; no allocator or fallible capacity step
  remains at that boundary. Initial activation reserves this unit before client
  preface/server frame exposure. Terminal cleanup releases an unexposed unit
  without effects, preserves Frozen-first completion, and releases a committed
  awaiting-ACK unit without rolling back its advertised snapshot.
- Reserve WINDOW_UPDATE storage and queue ownership for both stream and
  connection targets. Private owns a checked coalescible increment but no
  protocol-visible credit. First exposure atomically subtracts that increment
  from `reclaimed_unadvertised`, adds it to `update_in_flight`, and freezes the
  exact 13-byte record. Acknowledgements 0..=12 retain the slot and change
  neither `advertised_remaining` nor the frozen record. Acknowledgement of all
  13 bytes atomically adds exactly `update_in_flight` to
  `advertised_remaining`, clears that in-flight amount, reclaims the slot, and
  leaves later reclaimed credit for the next Private record. Invalid, stale,
  duplicate, cross-target, or overlong acknowledgement is state-neutral.
  Partial transport failure abandons the connection and never fabricates
  advertised credit. A Private stream record may be cancelled at closure
  without cancelling independent connection credit; Frozen completes exactly
  or is abandoned only with the connection.
- Reserve a bounded FIFO slot and exact 17-byte output record for every accepted
  non-ACK PING transaction. `ReservedPrivate` owns its copied `[u8; 8]` and is
  never coalesced, including with an identical neighbor. First exposure freezes
  header, ACK flag, opaque bytes, transaction generation, and token-bound
  suffix. Acknowledged offsets 0..=16 retain the transaction and slot; only
  acknowledgement of all 17 bytes produces Complete and releases them. Stale,
  duplicate, cross-record, out-of-order, or overlong acknowledgement is
  state-neutral. Queue exhaustion before acceptance selects one bounded
  connection shutdown, while transport failure at any Frozen prefix abandons
  connection-owned transactions without claiming Complete or retaining caller
  input.
- Reserve a generation-safe GOAWAY slot that always fits the 17-byte minimum;
  optional owned debug uses separate bounded capacity and is omitted/truncated
  under its recorded policy rather than blocking shutdown. ReservedPrivate may
  be replaced only by the selected fatal winner before exposure. First exposure
  freezes the exact stage, last-stream ID, error code, owned/redacted debug
  bytes, slot, generation, and checked `total_len = 17 + debug_len`.
  Acknowledged offsets below `total_len` retain the slot and change neither
  `SentGoawayCutoff` nor timer state. Only acknowledgement of all `total_len`
  bytes produces Complete, atomically lowers the sent-cutoff ledger, and arms
  the generation-checked grace timer when stage is GracefulInitial. Invalid,
  stale, duplicate, cross-record, out-of-order, or overlong acknowledgement is
  state-neutral. Transport failure at acknowledged zero moves to
  AbandonedConnection with `PeerVisibleCutoff::NotVisible`; failure after a
  positive incomplete prefix records `PeerVisibleCutoff::UnknownAfterPartial`.
  Neither arms a timer or commits a cutoff, and no further frame is emitted.
  Frozen graceful completion with pending
  fatal intent reserves exactly one non-increasing successor or abandons the
  connection; duplicate fatal causes never multiply queue entries.
- Activate the v0.142.0 connection scheduler over these reserved owners. Its
  eligible order is Frozen suffix, FramingCommitted field-block frame, fatal
  GOAWAY, PING ACK, SETTINGS ACK, graceful GOAWAY, RST_STREAM, WINDOW_UPDATE,
  then ordinary output; FIFO within a class uses immutable enqueue ordinal,
  connection generation, and record generation. Fatal GOAWAY is the explicit
  exception ahead of the PING priority SHOULD. Positive v0.147.0 bypass limits,
  the consecutive-PING bound, and AckEligible SETTINGS deadline close only
  nonfatal eligibility gates; they never reorder Frozen/FramingCommitted output
  or fatal GOAWAY.
- On full fatal GOAWAY commitment, atomically transition every remaining
  Private mandatory control to
  `AbandonedByConnectionFatal { connection_generation }` before another
  output offer can be made. This typed terminal outcome is the only exception
  to delivering an accepted valid required reply and is never a silent drop:
  SETTINGS performs no ACK commitment, ceiling advance, or HPACK-debt merge;
  WINDOW_UPDATE restores no advertised credit; RST_STREAM runs no local reset
  completion; PING records no response sent; and graceful GOAWAY arms no timer.
  Release every slot, copied payload, participant, target, tombstone hold, and
  queue entry exactly once; reject every outstanding token as stale. Graceful
  GOAWAY performs none of this cleanup and existing-stream controls remain
  schedulable.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Reserved control-output queues and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Queue each required control during every initial/CONTINUATION prefix; use mixed-entry SETTINGS frames and prove one inbound transaction-owned ACK slot each, exact participant completion, FIFO eligibility, and smallest/final HPACK collapse without ACK collapse. Exhaust outbound SETTINGS frame, queue, future-ACK FIFO, timeout, and commit-plan capacity independently at one slot short; prove atomic pre-exposure backpressure and no fallible final-byte step. Inject speculative SETTINGS ACK at every ReservedPrivate/Frozen offset, after full offer before acknowledgement, and among multiple committed/frozen records; prove no banking, timeout cancellation, peer-acknowledged mutation, or feature activation, strict committed FIFO matching, acknowledgement-first combined processing, and local driver-order failure before protocol parsing. Exercise every pair of scheduler classes, every same-class arrival/generation tie, all mandatory controls plus later outbound SETTINGS simultaneously, continuous admitted PING, SETTINGS deadlines, bypass values one/typical/maximum, and capacity-triggered shutdown with replies already queued; prove the exact total order, finite service bounds, and no clock-based committed-frame reorder. Prove capacity remains reserved, participant failure cancels before exposure, Private rollback permits ACK ahead of failing re-encode, FramingCommitted waits through final acknowledgement/HpackCommitted, and transport failure emits no interleaved control byte. For GOAWAY, overwrite caller debug after command acceptance and exhaust every acknowledged offset 0..=`17 + debug_len` for zero/maximum debug, graceful initial/final/fatal stages, early/stale/correct timers, fatal escalation at each Frozen prefix, minimum-slot-only exhaustion, duplicate causes, stale/cross-slot tokens, and transport failure. Enter fatal shutdown while each mandatory control and outbound SETTINGS is Private, Frozen, or committed-awaiting-ACK; prove committed framing/Frozen settings finish first, full fatal GOAWAY commitment atomically abandons only Private records, no later frame is offered, every owner releases once, all tokens become stale across generation reuse, peer-visible setting effects never roll back, and no ACK/debt, advertised-credit, reset-completion, PING-response, or graceful-timer hook is fabricated. Prove graceful shutdown performs no terminal cleanup. Prove byte-for-byte immutability, final-byte-only cutoff/timer commitment, zero-prefix NotVisible versus positive-prefix UnknownAfterPartial, non-increasing successor, and optional debug never blocking shutdown. For PING, overwrite input after parse and exhaust every output split/acknowledged offset 0..=17 across distinct/identical FIFO records, ACK-bearing no-reply, queue exhaustion, stale/duplicate/cross-slot/overlong tokens, and failure at every prefix; each accepted non-ACK PING emits its own exact ACK unless the typed fatal-abandonment terminal outcome wins before exposure and releases only at byte 17 otherwise. For WINDOW_UPDATE, exhaust offsets 0..=13 for stream and connection records, every underflow/overflow boundary, coalescing before/after exposure, new credit while Frozen, padding-only DATA, reset/closure and connection-only post-reset credit, stale/cross-record tokens, and failure at every prefix; advertised credit changes once and only at byte 13.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reserved control-output queues contract and all previously implemented relevant behavior have
reproducible evidence; v0.152.0 (WINDOW_UPDATE churn defenses) still passes; no behavior assigned to v0.154.0 (HTTP/2 conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 — HTTP/2 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/2 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.153.0 (Reserved control-output queues) and must be independently trustworthy before v0.155.0 (Protocol-neutral HTTP translation representation) begins.

#### Deliverables

- Acceptance contract: Replay every RFC 9113 frame, stream-state, continuation, flow-control, SETTINGS, GOAWAY, push, priority, HPACK, malformed-field, flood, and shutdown vector for both roles; require exact connection/stream error code, state delta, publication trace, control output, work charge, and interop transcript before the HTTP/2 pentest exit. Replay every inbound frame at local RST_STREAM acknowledgement offsets 0..=13 and require pre-completion legality, full-acknowledgement-only local closure, immutable first-closure attribution, remote-first completion behavior, and partial-failure non-completion evidence. For ordinary output, replay whole Private/FramingCommitted/HpackCommitted HEADERS and PUSH_PROMISE blocks plus every initial/CONTINUATION prefix against all SETTINGS_HEADER_TABLE_SIZE sequences, local fragment caps/mandatory prefixes/block-byte/continuation ceilings, resource exhaustion, peer MAX_FRAME_SIZE reduction, remote END_STREAM, peer/local reset, every control type, other streams, cancellation, GOAWAY, and transport failure; require exact debt merge after ACK commitment, Private lease and rollback-before-newer-merge, first-exposure transfer, immutable transmitted prefix through FramingCommitted, post-exposure following-block debt, exact FIFO ACK suffix commitment, no later stale encoding or dependent exposure through ACK byte eight, actual-cap slot/entry preflight, zero-exposure local oversized-field failure, final-frame-only table publication, independent initial END_STREAM hook, and connection-abandonment-only escape. Exhaust atomic stream+connection DATA reservations and caller-provided staging bytes across checked `9 + payload`, padding overhead/data selection, padding-only shortage/reduction policy, concurrent last-credit contenders, WINDOW_UPDATE, negative SETTINGS reductions, unexposed resegmentation/revocation, frozen debit, zero-length END_STREAM, peer maximum 16,777,215, local payload cap, and independent byte/entry exhaustion. Require every scalar/vectored `OutputToken` to own one slot suffix and reject cross-slot acknowledgement without mutation.
- Audit combined-entry `InboundSettingsTransaction` products spanning HEADER_TABLE_SIZE, INITIAL_WINDOW_SIZE, MAX_FRAME_SIZE, MAX_CONCURRENT_STREAMS, ENABLE_PUSH, duplicates, unknowns, and enabled extensions in every wire order. Require one frame-wide ACK; generation-bound participants; FIFO ACK states; separate peer-received/peer-wire-acknowledged/selected/physical limits; per-frame ceiling snapshots and optional selected deltas; immediate reduction clamp/eviction; no automatic increase; selected-only debt for peer clamps, local policy changes, and initial-below-4096; safe decoder advertisement/activation; exact 0→4096 and 4096→0→4096 debt history across Private/exposure/CONTINUATION boundaries; stale-token neutrality; failure cleanup; and encoder/decoder table equivalence with no physical eviction lacking matching wire debt.
- Audit `OutboundSettingsTransaction` across initial/later, client/server,
  empty/mixed/duplicate/unknown/extension entries, every byte offset, all
  independent reservation ceilings, multiple commitment/ACK orders, speculative ACK,
  injected deadlines, fatal shutdown, partial failure, stale tokens, and
  generation reuse. Require complete pre-reservation before preface/first frame
  or command acceptance, immutable bytes, final-byte-only commit-plan
  activation/FIFO promotion/deadline, oldest committed ACK without
  reapplication, no ACK banking at any uncommitted offset, exact unsolicited
  error versus local driver-order classification, no speculative timeout/feature
  effect, unknown partial visibility, and no rollback of committed local
  advertisements.
- Audit stream and connection `ReceiveCredit` independently across DATA
  validation, application acknowledgement, padding/policy discard, private
  coalescing, first exposure, every WINDOW_UPDATE offset 0..=13, new
  reclamation while Frozen, FramingCommitted blocking, reset/closure/reuse,
  connection-only post-reset handling, stale tokens, 31-bit ceilings, and
  transport failure. Require flow-control underflow at the exact offending
  prefix, no advertised restoration through byte 12, one exact restoration at
  byte 13, immutable target/increment/suffix, and no stream lifecycle loss or
  transfer of independent connection credit.
- Audit inbound PING transaction ownership from syntax/capacity preflight
  through copied payload, FIFO scheduling, first exposure, every offset 0..=17,
  completion/failure, and input reuse. Cross distinct/identical non-ACK PINGs,
  ACK-bearing no-reply, frozen suffixes, fragmented field blocks, budget/queue
  exhaustion, and stale/cross-slot acknowledgements. Audit bounded locally
  originated correlation across unique keys, in-order/reordered matching,
  unsolicited, duplicate, stale, wrap, and tombstone expiry; require exact
  live-key completion regardless of arrival order, exact one-for-one peer
  replies, byte-17-only release, explicit PING priority SHOULD disposition, and
  no RFC connection error for correlation mismatch.
- Audit GOAWAY across admission seal, shutdown intent, application-publication
  high-water, graceful initial/final and every fatal class, ReservedPrivate,
  every Frozen offset 0..=`17 + debug_len`, Complete/AbandonedConnection,
  committed sent and received cutoff ledgers, and timer generations. Cross
  caller debug reuse, zero/maximum debug, minimum-only capacity, final-cutoff
  publication races, higher-stream HPACK/credit synchronization, received
  decreasing/equal/increasing cutoffs, scheduler blocking, duplicate fatal
  causes, and transport failure at every prefix. Require full-frame-only
  cutoff/timer commitment, zero-prefix nonvisibility versus unknown positive
  partial visibility, deterministic fatal
  precedence, immutable Frozen bytes, no post-final higher-stream publication,
  one non-increasing successor at most, default redaction, and no replay
  authority from cutoff classification.
- Audit the connection-wide scheduler across every pair and simultaneous set of
  Frozen framing, fatal/graceful GOAWAY, PING ACK, SETTINGS ACK, RST_STREAM,
  WINDOW_UPDATE, and ordinary output. Require immutable FIFO/generation ties,
  finite configured bypass/deadline service, fatal-before-PING exception, and
  graceful-before-reset placement. At every Private state and Frozen byte
  offset, require fatal commitment to abandon only unexposed controls, expose
  nothing afterward, release ownership exactly once, reject stale tokens, and
  fabricate no SETTINGS/debt, credit, reset, PING, or timer completion; require
  graceful shutdown to preserve all existing-stream control obligations.
- Audit Sans-I/O causality for SETTINGS ACK, locally originated PING ACK,
  response HEADERS on locally initiated streams, locally advertised
  ENABLE_PUSH/ENABLE_CONNECT_PROTOCOL/extension-dependent frames, and GOAWAY
  state. At every output prefix, cross output-only, input-only, and combined
  calls; require acknowledgement-first combined processing, wholly unconsumed
  reversed input with local `DriverCommitOrderViolation`, strict protocol
  classification after commitment, and no input-derived completion, timeout
  cancellation, feature activation, stream publication, or cutoff mutation.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.153.0 (Reserved control-output queues) still passes; no behavior assigned to v0.155.0 (Protocol-neutral HTTP translation representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.154.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 4 — Proxy, client, server, and public APIs

Phase contract: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.

### v0.155.0 — Protocol-neutral HTTP translation representation

Status: planned

#### Goal

Deliver **Protocol-neutral HTTP translation representation** as the sole primary capability in this stop. It builds
on v0.154.0 (HTTP/2 conformance audit and pentest) and must be independently trustworthy before v0.156.0 (Effective URI and authority consistency) begins.

#### Deliverables

- Acceptance contract: Define an immutable representation IR for validated source semantics only; it emits no destination bytes and claims no effective-URI, hop-stripping, or framing translation before those prerequisites land.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Protocol-neutral HTTP translation representation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Protocol-neutral HTTP translation representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.154.0 (HTTP/2 conformance audit and pentest) still passes; no behavior assigned to v0.156.0 (Effective URI and authority consistency) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 — Effective URI and authority consistency

Status: planned

#### Goal

Deliver **Effective URI and authority consistency** as the sole primary capability in this stop. It builds
on v0.155.0 (Protocol-neutral HTTP translation representation) and must be independently trustworthy before v0.157.0 (Connection-field stripping and cache-metadata preservation) begins.

#### Deliverables

- Acceptance contract: Reuse the already validated v0.40.0 EffectiveTarget and its generation-bound TrustedRequestContext rather than introducing or changing scheme/authority policy during translation; carry trusted scheme, authority/port, raw path, optional raw query, request-target form, Host/:authority disposition, validated ConnectAuthority, and end-origin identity without normalization; preserve query/percent encoding, use absolute-form target authority rather than Host, accept an empty authority only from the earlier explicit default, and reject decision/context mismatch before translation IR publication with distinct syntax, policy, and caller-capacity failures.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test absolute-target authority versus conflicting Host, origin-server absolute-form, grammar-valid empty Host, explicit reject/default handling for empty effective authority, regenerated proxy Host, and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Effective URI and authority consistency contract and all previously implemented relevant behavior have
reproducible evidence; v0.155.0 (Protocol-neutral HTTP translation representation) still passes; no behavior assigned to v0.157.0 (Connection-field stripping and cache-metadata preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 — Connection-field stripping and cache-metadata preservation

Status: planned

#### Goal

Deliver **Connection-field stripping and cache-metadata preservation** as the sole primary capability in this stop. It builds
on v0.156.0 (Effective URI and authority consistency) and must be independently trustworthy before v0.157.1 (Via grammar, append, privacy, and loop policy) begins.

#### Deliverables

- Acceptance contract: Consume the exact ordered nominations in v0.56.0 `ValidatedConnectionOptions` for either HTTP/1.0 or HTTP/1.1; never parse or normalize `Connection` again. Preserve and validate the source version binding, reject stale, cross-message, cross-role, cross-version, or cross-connection evidence and forbidden nominations, remove every occurrence of each validated nominated field plus fixed hop-by-hop fields without deleting unrelated end-to-end fields, preserve remaining field order and RFC 9111 cache metadata exactly, and publish the stripped representation only after complete validation and destination-capacity preflight. In particular, strip received HTTP/1.0 `keep-alive` and its nominated fields as hop-local data; forwarding can never carry `ValidatedHttp10KeepAlive`, synthesize `CommittedHttp10KeepAliveHead`, or contribute either received signal to another hop's `Http10ReusePermit`. Each destination hop independently generates, commits, and validates its own v0.75.0 negotiation.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test nominated/fixed hop-field removal by replaying the v0.56.0 repeated-field/comma-list/case/OWS/empty-element/close-precedence/quoted-substring/Proxy-Connection/malformed corpus under both HTTP versions through the same sealed evidence. Require identical lexical nominations, version-specific semantic refinements, and correct stripping for either version. For HTTP/1.0 proxy translation, prove received keep-alive fields and all sealed evidence stop at the source hop, the destination creates a fresh local signal only through its own policy/head commitment, and no source signal can help mint a destination reuse permit. Test stale/cross-message/role/version/connection substitution, duplicate/forbidden nominations, end-to-end preservation, ordered cache metadata, zero destination output before complete validation, every capacity boundary, and all earlier positive/negative/truncation/cancellation/no-panic behavior. Require no second grammar or normalization decision.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-field stripping and cache-metadata preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.156.0 (Effective URI and authority consistency) still passes; no behavior assigned to v0.157.1 (Via grammar, append, privacy, and loop policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.157.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.1 — Via grammar, append, privacy, and loop policy

Status: planned

#### Goal

Deliver **Via grammar, append, privacy, and loop policy** as the sole primary capability in this stop. It builds
on v0.157.0 (Connection-field stripping and cache-metadata preservation) and must be independently trustworthy before v0.157.2 (Dependency-free generic authentication grammar and sensitive storage) begins.

#### Deliverables

- Acceptance contract: Parse the full ordered Via member grammar under explicit member/comment/value/work limits; preserve all existing members and append exactly one caller-configured received-protocol plus pseudonym entry without replacement or combination; record the inbound protocol/version rather than the outbound version; require every proxy on every forwarded message and every HTTP-to-HTTP gateway on inbound forwarded requests to append; default to a pseudonym at firewall/private boundaries so internal hosts/ports are not disclosed; preflight output capacity; and expose a bounded caller-configured self-pseudonym loop hook that never derives identity from peer bytes.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test complete Via grammar/order/comments/member limits, append/no-replace/no-combine, inbound-version recording across HTTP/1↔HTTP/2, proxy/gateway applicability, firewall pseudonym privacy, capacity preflight, self-loop policy, no input-derived identity, and all earlier behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Via grammar, append, privacy, and loop policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.0 (Connection-field stripping and cache-metadata preservation) still passes; no behavior assigned to v0.157.2 (Dependency-free generic authentication grammar and sensitive storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.157.1 implementation stop reached. Run pentest for this exact commit.`

### v0.157.2 — Dependency-free generic authentication grammar and sensitive storage

Status: planned

#### Goal

Deliver **Dependency-free generic authentication grammar and sensitive storage** as the sole primary capability in this stop. It builds
on v0.157.1 (Via grammar, append, privacy, and loop policy) and must be independently trustworthy before v0.157.3 (Proxy-authentication hop ownership and 407 lifecycle) begins.

#### Deliverables

- Acceptance contract: Add a separate dependency-free, no_std `vef-auth` crate with a bounded incremental scheme-neutral parser/serializer for challenge, credentials, token68, and auth-param including exact BWS, quoted-string/escape, token, and parameter-count/value/work limits; compare authentication scheme and parameter names case-insensitively while preserving raw scheme spelling, reject duplicate parameter names within one challenge, require generated realm values to use quoted-string, and reject any token68 data after terminal `=` padding; disambiguate comma-separated auth parameters from subsequent challenges without unsafe normalization, preserve multiple field-line and challenge boundaries, and support WWW-Authenticate, Authorization, Authentication-Info, Proxy-Authenticate, Proxy-Authorization, and Proxy-Authentication-Info without implementing Basic, Digest, or any authentication scheme; introduce caller-supplied scheme-specific `AuthenticationTrailerPermission`, bind it to the exact authentication-info field/message generation, and integrate the positive outbound authentication-trailer and explicitly safe-merge paths into both HTTP/1 and HTTP/2 without changing the v0.52.0/v0.131.0 received-trailer classification; sensitive values remain borrowed or in caller-owned storage, are never copied into diagnostics or HPACK indexing, and on logical invalidation VEF releases references and preserves redaction/non-indexing but does not promise optimizer-resistant physical zeroization—the caller must scrub its owned buffers when required.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including authentication, Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test raw-preserving case-insensitive scheme comparison, case-insensitive parameter names, duplicate rejection, quoted generated realm, every legal/illegal token68 padding suffix, token68-versus-parameter form, comma ambiguity, repeated/empty list members, BWS, quoted escape, malformed token/value, every limit/split/round trip, all six fields, valid/stale/cross-message authentication trailer permission, positive/denied HTTP/1 and HTTP/2 authentication-trailer generation, allowed/denied safe merge, unchanged received RequiresSchemeAuthorization classification, borrowed lifetime/redaction/non-indexing, logical invalidation/caller scrub, and unknown schemes without Basic/Digest behavior.
- Create a stateful authentication grammar fuzz target with adversarial comma/quote/escape corpora and retain every minimized regression.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The generic authentication grammar and sensitive-storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.1 (Via grammar, append, privacy, and loop policy) still passes; no behavior assigned to v0.157.3 (Proxy-authentication hop ownership and 407 lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.157.2 implementation stop reached. Run pentest for this exact commit.`

### v0.157.3 — Proxy-authentication hop ownership and 407 lifecycle

Status: planned

#### Goal

Deliver **Proxy-authentication hop ownership and 407 lifecycle** as the sole primary capability in this stop. It builds
on v0.157.2 (Dependency-free generic authentication grammar and sensitive storage) and must be independently trustworthy before v0.157.4 (Injected civil time and HTTP-date policy) begins.

#### Deliverables

- Acceptance contract: Consume one validated HopScopedProxyCredential at the first expecting proxy and remove Proxy-Authorization before origin forwarding; never treat it as Authorization or rebind it to another exchange even when connection/policy generations match; permit relay only through explicit generation-bound cooperative policy naming the next hop; scope Proxy-Authenticate and Proxy-Authentication-Info only to the next outbound client; require at least one v0.157.2-valid Proxy-Authenticate challenge on every generated 407; mark every proxy credential/challenge/info field sensitive, redacted, HPACK never-indexed, and TRACE-excluded; apply v0.65.0 mandatory close/fresh-connection behavior to HTTP/1 CONNECT 407; and logically invalidate credentials plus pending optimistic/tunnel bytes on consume, rejection, cancellation, policy change, non-2xx, or retry without claiming caller-buffer zeroization.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including authentication, Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test credential consume/remove versus Authorization preservation, denied/allowed named-next-hop relay, stale and same-generation cross-exchange rebind, duplicate consume, next-client response-field scoping, malformed/empty/valid generated 407 challenges, redaction/non-indexing/TRACE exclusion, HTTP/1 CONNECT close/fresh retry, logical invalidation with no surviving pending bytes/references, caller scrub ownership, and all earlier behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The proxy-authentication hop ownership and 407 lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.2 (Dependency-free generic authentication grammar and sensitive storage) still passes; no behavior assigned to v0.157.4 (Injected civil time and HTTP-date policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.157.3 implementation stop reached. Run pentest for this exact commit.`

### v0.157.4 — Injected civil time and HTTP-date policy

Status: planned

#### Goal

Deliver **Injected civil time and HTTP-date policy** as the sole primary capability in this stop. It builds
on v0.157.3 (Proxy-authentication hop ownership and 407 lifecycle) and must be independently trustworthy before v0.157.5 (Dependency-free media-type grammar) begins.

#### Deliverables

- Acceptance contract: Add checked no_std `UtcCivilTime` and generation-bound `CivilTimeEvidence::{Available, Unavailable}` to `vef-core`, separate from monotonic deadlines; let callers supply evidence directly and add an optional `vef-io::CivilClock` provider that returns it without giving protocol crates clock ownership. Represent generic civil years 0001..=9999 and checked calendar fields including HTTP leap-second 60, while keeping the narrower validated `HttpDate` type distinct and rejecting every HTTP date earlier than 1900 as required through RFC 9110's RFC 5322 date semantics. Implement the RFC 850 two-digit-year resolver using the complete supplied current `UtcCivilTime` instant—not only its year—and roll a candidate back by 100 years only when its complete timestamp is more than 50 years in the future; v0.180.1 must reuse it and reject a resolved pre-1900 result. Unavailable current-instant evidence yields a typed UnresolvedCivilTime disposition, never a guessed century.
- Define origin and intermediary Date policy before v0.160.0 translation: an origin with Available evidence must generate Date on 2xx/3xx/4xx and may on 1xx/5xx, an origin with Unavailable evidence must not generate Date, and a recipient with Available evidence appends receipt time when caching/forwarding a response without Date and may replace invalid Date while an unavailable recipient preserves absence/invalid evidence without invention. With a clock, clamp a future application Last-Modified to message-origination Date; without one, generate Last-Modified only when an external system explicitly assigned it. Every inserted/replaced/clamped field is included in the destination message generation and later selected-representation snapshot.
- Preserve no_std/platform neutrality: monotonic timeout providers cannot satisfy civil-time APIs, Aesynx without an RTC reports Unavailable, and no protocol decision reads an OS clock, timezone, locale, or global state.
- Update paragraph-addressable RFC 9110 HTTP-date, Date, Last-Modified, forwarding, conditional, and security requirements plus the inherited RFC 5322 Section 3.3 calendar/year rules, threat model, APIs, release notes, traceability, resource measurements, and conformance corpora.

#### Verification

- Test exactly 50 years versus 50 years plus one second, leap-day boundaries, end-of-year and century transitions, resolution near the representable maximum year, generic civil years 0001/1899/1900/9999 versus the HTTP-date year floor, leap years and second 60, invalid calendar fields, Available/Unavailable transitions, origin 1xx–5xx Date matrix, forwarding/cache insertion and invalid replacement, Last-Modified clamp/external assignment, stale/cross-generation evidence, monotonic/civil type separation, and a mock no-RTC caller under every split/capacity/cancellation path.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The injected civil-time and HTTP-date policy contract and all previously implemented relevant behavior have reproducible evidence; v0.157.3 (Proxy-authentication hop ownership and 407 lifecycle) still passes; no behavior assigned to v0.157.5 (Dependency-free media-type grammar) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.157.4 implementation stop reached. Run pentest for this exact commit.`

### v0.157.5 — Dependency-free media-type grammar

Status: planned

#### Goal

Deliver **Dependency-free media-type grammar** as the sole primary capability in this stop. It builds
on v0.157.4 (Injected civil time and HTTP-date policy) and must be independently trustworthy before v0.158.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) begins.

#### Deliverables

- Acceptance contract: Add a separate dependency-free, no_std `vef-media-type` crate depending only on `vef-core`; implement the RFC 9110 generic grammar as bounded incremental syntax parsing of media type, subtype, ordered parameter and empty-parameter-slot events, tokens, quoted strings, quoted-pair escapes, and OWS around semicolons with independent raw-byte, field-count, slot-count, parameter-count, decoded-byte, and work limits. Preserve ordered duplicate parameter names and every permitted empty slot, including a trailing semicolon; compare names case-insensitively without changing raw spelling. Reject whitespace on either side of `=`, missing values such as `name=`, invalid tokens/quotes/escapes, and lossy normalization, while accepting a distinct syntactically empty quoted value `name=""`. Return sealed `ParsedMediaType` syntax evidence bound to the exact field bytes and message generation plus non-authoritative borrowed views; generic syntax assigns no duplicate-name semantics, multipart meaning, or partial-response authority.
- Add a separate conservative local-generation policy that consumes current `ParsedMediaType` and the frozen field set to issue sealed `ValidatedGeneratedMediaType`. It rejects duplicate Content-Type field lines, duplicate parameter names, stale evidence, and same-generation field substitution before output, while media-type-specific validators remain free to define duplicate parameters as invalid, equivalent, or meaningful. v0.158.0 must consume this generated evidence for OPTIONS content, later validators must reuse the same parser, and missing/invalid evidence emits zero head/body bytes. Received generic extension media types remain syntax-valid despite duplicate parameters or empty slots and are not rejected merely by the local generation policy.
- Source-lock RFC 2046 alongside RFC 9110, record paragraph-addressable media-type and multipart boundary requirements, and distinguish generic parameter syntax from later v0.180.5 multipart/byteranges classification. Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update threat model, controls, APIs, release notes, traceability, resource measurements, and conformance corpora; define exact progress, capacity, cancellation, ownership, publication, commit/rollback, and typed error behavior.

#### Verification

- Exhaust type/subtype casing, `text/plain;`, consecutive and trailing empty slots, ordered duplicate names, OWS around semicolons, token/quoted parameter values, `name=""` versus invalid `name=`, forbidden `name =value`/`name= value`, quoted-pair escapes, field substitution, stale/cross-message evidence, every limit/split/truncation, round trips, arbitrary-input no-panic behavior, and no hidden allocation. Prove generic `ParsedMediaType` preserves valid duplicates/slots, generated policy rejects configured duplicates without redefining syntax, generated OPTIONS uses only exact current `ValidatedGeneratedMediaType`, and no second grammar exists in an engine or facade.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The dependency-free media-type grammar and generated-content validation contract and all previously implemented relevant behavior have reproducible evidence; v0.157.4 (Injected civil time and HTTP-date policy) still passes; no behavior assigned to v0.158.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.157.5 implementation stop reached. Run pentest for this exact commit.`

### v0.158.0 — Max-Forwards TRACE and OPTIONS intermediary semantics

Status: planned

#### Goal

Deliver **Max-Forwards TRACE and OPTIONS intermediary semantics** as the sole primary capability in this stop. It builds
on v0.157.5 (Dependency-free media-type grammar) and must be independently trustworthy before v0.159.0 (HTTP/1 TE request-field and trailers forwarding semantics) begins.

#### Deliverables

- Acceptance contract: Parse one valid Max-Forwards value, decrement only a received value on forwarded TRACE/OPTIONS, never synthesize it when absent, handle zero locally without forwarding, define malformed/duplicate disposition, and preserve or ignore it correctly for other methods; classify only absolute-form OPTIONS with empty path and absent query as ServerWideOptionsCandidate, preserve its absolute-form when forwarding to another forward proxy, and convert it to asterisk-form only at the final origin-facing hop, while present-but-empty query, `OPTIONS /`, and every resource path remain distinct and never convert; TRACE client builders reject content, Cookie, Authorization, Proxy-Authorization, Proxy-Authenticate, Proxy-Authentication-Info, and caller-marked sensitive fields, a final TRACE responder produces only a bounded sanitized reflection representation excluding all credential fields and sensitive values, OPTIONS client content requires exact current v0.157.5 `ValidatedGeneratedMediaType` evidence for its frozen Content-Type, and both response types are non-cacheable.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test absent Max-Forwards, decrement/zero-local/no-forward, malformed/duplicate values; absolute empty-path/no-query OPTIONS across intermediate and final proxy hops; present-empty query, `/`, and resource nonconversion; TRACE builder content/sensitive rejection, bounded reflection/no leakage, OPTIONS Content-Type with valid/stale/substituted/missing v0.157.5 evidence and zero prevalidation bytes, and non-cacheable metadata.
- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Max-Forwards TRACE and OPTIONS intermediary semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.5 (Dependency-free media-type grammar) still passes; no behavior assigned to v0.159.0 (HTTP/1 TE request-field and trailers forwarding semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 — HTTP/1 TE request-field and trailers forwarding semantics

Status: planned

#### Goal

Deliver **HTTP/1 TE request-field and trailers forwarding semantics** as the sole primary capability in this stop. It builds
on v0.158.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) and must be independently trustworthy before v0.160.0 (Normative HTTP/1 and HTTP/2 translation matrix) begins.

#### Deliverables

- Acceptance contract: Treat TE as a request field distinct from Transfer-Encoding, accept only trailers where required, enforce Connection: TE nomination in HTTP/1 forwarding, and map TE: trailers safely across HTTP versions.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 TE request-field and trailers forwarding semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.158.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) still passes; no behavior assigned to v0.160.0 (Normative HTTP/1 and HTTP/2 translation matrix) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 — Normative HTTP/1 and HTTP/2 translation matrix

Status: planned

#### Goal

Deliver **Normative HTTP/1 and HTTP/2 translation matrix** as the sole primary capability in this stop. It builds
on v0.159.0 (HTTP/1 TE request-field and trailers forwarding semantics) and must be independently trustworthy before v0.161.0 (CONNECT translation across HTTP versions) begins.

#### Deliverables

- Acceptance contract: Map target/Host to pseudo-fields and back while carrying raw path plus optional raw query exactly: construct :path as path followed by `?` plus query when present, preserve an empty query's trailing `?`, split inbound :path only on the first `?`, preserve percent-encoded octets byte-for-byte, and replace an empty HTTP URI path with `/` only where RFC 9112 requires; preserve absolute-form ServerWideOptionsCandidate when the next hop is another forward proxy, but at the final origin-facing hop map its empty-path/absent-query target to HTTP/1 `OPTIONS *` or HTTP/2 `:path: *`; never convert present-empty query or `OPTIONS /`; proxies never otherwise modify path/query; keep received trailers separate and capability-free, translate a field only after destination-side v0.52.0 field permission and, for authentication-info, v0.157.2 scheme permission authorize the new message generation, and never merge it into the destination head without distinct safe-merge permission; preserve received multipart/byteranges 206 content opaquely across versions without parsing boundaries or claiming part validation; HTTP/1 426 with valid Upgrade is untranslatable to HTTP/2 and yields zero-output typed failure unless the application explicitly selects and revalidates an alternative status, while HTTP/2 426 semantic violations never become a valid forwarded response; also map other status, framing, fields, informational/HEAD/body-forbidden responses including invalid 205 suppression, CONNECT/Upgrade, and close-delimited reframing before emitting bytes.
- Apply v0.157.4 civil-time policy identically across versions: forwarding/cache recipients with Available evidence append a missing Date or may replace an invalid Date using receipt time before destination validation, Unavailable evidence never invents one, and every resulting Date/Last-Modified value is bound to the translated message generation without changing protocol framing.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every matrix cell in both directions, including HTTP/1 426+Upgrade to HTTP/2 zero-output failure and explicit application alternative, received HTTP/2 426 semantic-violation nonforwarding, Available/Unavailable missing/invalid Date forwarding and Last-Modified binding, permitted/prohibited/authentication trailers, separate storage and denied/allowed safe merge, OPTIONS star conversions, present-empty query and `/`, invalid 205, query/percent identity, slash conversion, forbidden normalization, partial output, capacity, cancellation, and zero prevalidation bytes.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Normative HTTP/1 and HTTP/2 translation matrix contract and all previously implemented relevant behavior have
reproducible evidence; v0.159.0 (HTTP/1 TE request-field and trailers forwarding semantics) still passes; no behavior assigned to v0.161.0 (CONNECT translation across HTTP versions) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.160.0 implementation stop reached. Run pentest for this exact commit.`

### v0.161.0 — CONNECT translation across HTTP versions

Status: planned

#### Goal

Deliver **CONNECT translation across HTTP versions** as the sole primary capability in this stop. It builds
on v0.160.0 (Normative HTTP/1 and HTTP/2 translation matrix) and must be independently trustworthy before v0.162.0 (RFC 8441 extended CONNECT) begins.

#### Deliverables

- Acceptance contract: Translate only the shared validated ConnectAuthority between HTTP/1 authority-form and HTTP/2 :method CONNECT plus :authority with no :scheme/:path; preserve bracketed host and explicit 1..=65535 port, never use Host/default, and reuse the completed lexical authorization → ConnectAttemptToken → caller resolution/per-endpoint authorization → generation-matched AuthorizedConnectOutcome lifecycle in both directions before upstream output or tunnel publication; reject HTTP/1 request content/framing, but treat HTTP/2 DATA through v0.130.0 PendingConnect/AwaitingConnectOutcome and v0.133.0–v0.137.0 flow/ownership/command states only for ordinary CONNECT as sealed `PermittedOptimisticConnectInput`, never as HTTP content, forwarding none before validated outcome and linearly handing the same owner once on success or discarding/resetting it once on invalid outcome/non-2xx; forbid generated successful HTTP/1 length/transfer fields, mark responses non-cacheable, map non-2xx as ordinary HTTP, publish only after destination success, and hand bytes exactly once. Never apply ordinary-CONNECT optimistic authority to RFC 8441 WebSocket or HTTP/1 CONNECT-UDP.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test identical authority/token/resolved-endpoint/actual-peer/generation decisions in both directions, stale or alternate AuthorizedConnectOutcome, HTTP/1 content rejection versus staged ordinary HTTP/2 PendingConnect DATA, ordinary versus RFC 8441 request provenance, no pre-success forwarding, fixed-capacity reset then flow-aware backpressure ownership, invalid-outcome/non-2xx cleanup, one success transfer, port/bracket/Host conflicts, success fields, non-cacheability, failure mapping, exactly-once bytes, and all earlier behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT translation across HTTP versions contract and all previously implemented relevant behavior have
reproducible evidence; v0.160.0 (Normative HTTP/1 and HTTP/2 translation matrix) still passes; no behavior assigned to v0.162.0 (RFC 8441 extended CONNECT) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.161.0 implementation stop reached. Run pentest for this exact commit.`

### v0.162.0 — RFC 8441 extended CONNECT

Status: planned

#### Goal

Deliver **RFC 8441 extended CONNECT** as the sole primary capability in this stop. It builds
on v0.161.0 (CONNECT translation across HTTP versions) and must be independently trustworthy before v0.163.0 (Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge) begins.

#### Deliverables

- Acceptance contract: Accept only SETTINGS_ENABLE_CONNECT_PROTOCOL values 0 and 1 and track peer_enabled_outbound_connect separately from local_advertised_inbound_connect; only a client receiving peer value 1 may initiate outbound extended CONNECT, while receipt by a server has no effect; inbound extended CONNECT is accepted only after the local server's SETTINGS value 1 bytes commit, not when queued, otherwise return stream PROTOCOL_ERROR with no request publication; after either side sends value 1 it can never send 0 on that connection, mapping peer 0-after-1 to connection PROTOCOL_ERROR and a local attempt to InvalidState; a proxy/gateway advertises 1 only with an available native endpoint or fully configured bridge/entropy capability, and later transient endpoint, nonce, or capacity failure becomes a bounded HTTP failure without SETTINGS rollback; enforce :protocol plus extended :scheme/:path/:authority, distinguish ordinary CONNECT, reject 101 semantics, and publish no transition before final response and byte handoff succeed.
- Driver delivery of an inbound extended CONNECT while its enabling local
  SETTINGS remains unacknowledged is rejected at the v0.25.0 causality boundary
  without consuming the frame; peer input cannot commit the advertisement.
- Prevalidate the local ENABLE_CONNECT_PROTOCOL monotonicity/capability snapshot
  inside the v0.139.0 outbound commit plan. Full SETTINGS acknowledgement alone
  changes `local_advertised_inbound_connect`; Frozen prefixes and peer ACK do
  not, and terminal cleanup after commitment never rolls it back.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test values 0/1/other, client/server receipt direction, queued versus committed local advertisement, inbound-before-advertisement stream error and publication barrier, repeated 1, peer/local 0-after-1, transient failure after advertisement, disabled/missing bridge, missing entropy, native endpoint ownership, and ordinary versus extended CONNECT.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 8441 extended CONNECT contract and all previously implemented relevant behavior have
reproducible evidence; v0.161.0 (CONNECT translation across HTTP versions) still passes; no behavior assigned to v0.163.0 (Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.162.0 implementation stop reached. Run pentest for this exact commit.`

### v0.163.0 — Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge

Status: planned

#### Goal

Deliver **Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge** as the sole primary capability in this stop. It builds
on v0.162.0 (RFC 8441 extended CONNECT) and must be independently trustworthy before v0.164.0 (vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton) begins.

#### Deliverables

- Acceptance contract: For HTTP/1 downstream to HTTP/2 upstream, validate and retain the HTTP/1 Sec-WebSocket-Key, strip Connection, Upgrade, Host, Sec-WebSocket-Key, and any Sec-WebSocket-Accept from the HTTP/2 request/response, construct extended CONNECT with ws mapped to :scheme http and wss to https, lowercase every emitted HTTP/2 field name, and preserve/validate Origin, Sec-WebSocket-Version, Sec-WebSocket-Protocol, and Sec-WebSocket-Extensions plus ordinary end-to-end cookies/authorization through the normal matrix; validate selected protocol/extensions against the exact original absent/empty/duplicate offers without processing key/accept upstream, then after HTTP/2 2xx locally compute the HTTP/1 accept and commit 101; for HTTP/2 downstream to HTTP/1 upstream, ignore received HTTP/2 key/accept fields for key generation, obtain a fresh v0.69.0 nonce, generate the HTTP/1 key, validate upstream 101/accept and selected negotiation, then translate success to HTTP/2 2xx without copying HTTP/1 accept/Connection/Upgrade. Define four sealed, non-Copy/non-Clone phase-specific capabilities: `ValidatedDownstreamRequest`, `CommittedUpstreamRequest`, `ValidatedUpstreamSuccess`, and `CommittedDownstreamSuccess`. Each binds the bridge generation, connection and leg identity, client/server role, request/response kind, exchange or stream generation, and exact HTTP/1 or HTTP/2 head identity. `ValidatedDownstreamRequest` requires complete request semantic validation, CONNECT/extended-CONNECT form, advertisement/authorization/negotiation prerequisites, and legal inbound state. `CommittedUpstreamRequest` requires final HTTP/1 request-head acknowledgement or outbound HTTP/2 whole-field-block commitment. `ValidatedUpstreamSuccess` requires complete inbound head validation, and for HTTP/2 complete HEADERS/CONTINUATION compression synchronization, the sealed exact `TerminalFieldSectionLease`, every semantic stage, `TerminalValidation::Valid`, final 2xx, exact upstream-request/stream-generation correlation, negotiation agreement, and legal tunnel stream state; it never contains, requires, or fabricates outbound `HpackCommitted`. `CommittedDownstreamSuccess` requires final HTTP/1 success-head acknowledgement or outbound HTTP/2 whole-field-block commitment.
- Represent the asymmetric proxy flow as `BridgeTransaction::{Reserved, DownstreamRequestValidated, UpstreamRequestCommitted, UpstreamSuccessValidated, DownstreamSuccessFrozen, ActiveAfterDownstreamSuccessCommitted, FailedBeforeDownstreamSuccessExposure(BridgeFailurePhase), FailedAfterDownstreamSuccessExposure}` with one sealed generation. Its first three advancing transitions consume only `ValidatedDownstreamRequest`, `CommittedUpstreamRequest`, and `ValidatedUpstreamSuccess`; final downstream wire acknowledgement produces one non-Copy/non-Clone `CommittedDownstreamSuccess` as evidence of exact wire commitment, not activation authority. Minting the sealed `BridgeActivationPermit` is one atomic runtime transition that consumes the exact `CommittedDownstreamSuccess`, the pre-reserved permit slot, a clear `PrematureInputLatch` snapshot, and the matching `DownstreamSuccessFrozen` bridge generation. The matching `PrematureInputLatch` is clear at that transition or minting fails. Only the resulting permit enters `ActiveAfterDownstreamSuccessCommitted`; duplicate/stale acknowledgements, repeated completion hooks, cancellation races, and generation reuse cannot recreate any consumed input or mint a second permit/success publication/lease transfer. If cancellation wins before the atomic transition, it owns terminal cleanup and no permit exists; if permit minting wins, subsequent cancellation consumes the permit/Active owner through the one terminal path. No phase accepts another phase's capability even when connection, generation, or numeric stream identifiers coincide. Before exposing any upstream request byte, atomically reserve transaction/lease metadata, every required HTTP/1 over-read store, request/success output record, close/reset/abort action, suffix-completion owner, activation permit slot, premature-input latch, and terminal cleanup owner.
- Seal `TransitionInputProvenance::{SuccessFollowingTransitionInput, PermittedOptimisticConnectInput(OptimisticConnectPermit), UnpermittedOptimisticConnectInput { reason: MissingCommittedCloseProof }, ForbiddenOptimisticWebSocketInput, ForbiddenHttp1ConnectUdpInput}` with bridge, protocol, role, leg, request/stream, and exchange generations. `BridgeInputLease::{Http1(OverreadLease), Http2(PendingConnectLease)}` can be minted only from the first two variants. Success-following input is upstream HTTP/1 101 plus over-read WebSocket bytes or upstream HTTP/2 success HEADERS plus DATA. HTTP/1 ordinary-CONNECT permission consumes `OptimisticConnectCloseProof::{ReceivedValidatedCloseOption, LocallyCommittedCloseHead}`: the received variant proves a fully validated `Connection: close` option in that exact request head, while the local variant proves that exact serialized close-bearing request head reached v0.54.0 `HeadCommitted`; queued bytes or configured close intent alone grant no authority. Missing proof selects the strict unpermitted disposition: discard once, close, never HTTP-reparse, and never later promote even if CONNECT succeeds. HTTP/2 ordinary CONNECT remains permitted only through the existing v0.130.0 PendingConnect generation. Neither permit can be rebound to RFC 8441 WebSocket or HTTP/1 CONNECT-UDP; both forbidden classes terminate without lease creation.
- Apply the acknowledgement-first boundary without content classification. In `advance_io(output_ack, input)`, complete 101/2xx acknowledgement runs its success hook before input and permits post-handshake handling in that same call. Valid zero or short acknowledgement followed by WebSocket input leaves success uncommitted, classifies the input as premature, and selects the terminal violation; invalid acknowledgement remains state-neutral and leaves input wholly unconsumed.
- For legal HTTP/1 transition input or a terminal-only transition, create one `PendingHttp1Transition { overread: Option<OverreadLease>, terminal: Option<PreActiveTerminalCause>, bridge_generation, leg, exchange_generation, transport_generation }`. Optional over-read represents a valid 101/2xx followed by immediate termination with zero bytes, bytes without a terminal event, or combined bytes and termination. The sealed owner retains immutable first-terminal-cause attribution and distinguishes `PlainTcpEof`, `TlsCloseNotify`, `TlsTruncationEof`, `FatalTlsAlert`, `TransportReset`, `TransportFailure`, and `Cancellation`. It disposes optional bytes and terminal ownership exactly once. WebSocket EOF/failure before downstream success exposure fails the handshake; after any success exposure it closes/aborts both legs without a replacement HTTP response. Ordinary CONNECT follows an explicit drain/close policy. TLS close_notify never fabricates TCP half-close authority.
- Extend the existing HTTP/2 stream owner through `AwaitingConnectOutcome -> AwaitingBridgeActivation { bridge_generation } -> ActiveTunnel`. Validated upstream success enters `AwaitingBridgeActivation` rather than releasing or reclassifying PendingConnect. `PendingConnectLease` remains a linear reference to the existing v0.130.0/v0.136.0 PendingConnect ranges and creates no second byte store, copy, discard, or credit owner. This state retains all existing DATA ranges in exact order, semantic length versus padding charge, stream and connection receive-credit ownership, END_STREAM/remote-half-close state, and reset, EOF, TLS-alert, GOAWAY/connection-failure, and immutable first-terminal-cause attribution for the exact bridge generation. Success HEADERS followed in the same input buffer by DATA remains in this owner. Activation transfers ranges and any permitted pending directional FIN exactly once without copying or credit reclamation; failure uses the existing discard/reset/credit cleanup once. For WebSocket, upstream END_STREAM before downstream success exposure fails the handshake. For ordinary CONNECT, explicit policy either preserves it as a pending remote half-close published immediately after Active or rejects it before exposure. RST_STREAM or fatal failure before downstream success exposure remains an HTTP-framed downstream failure; after any success exposure it selects close-plus-abort and never another HTTP response.
- Premature downstream RFC 8441 WebSocket DATA first validates frame syntax and padding; any independent connection-fatal framing condition retains its normal scope. Otherwise charge the complete flow-controlled payload against both stream and connection windows, latch `PrematureExtendedConnectData`, discard semantic DATA only for that stream, and reclaim it only through the existing v0.136.0 `ReceiveCredit` ledger. Then arbitrate against the v0.137.0/v0.142.0 downstream-success output state. If the provisional 2xx remains `AcceptedPrivate` and no byte was exposed, supersede it and emit only reserved `RST_STREAM(PROTOCOL_ERROR)`—no HTTP response. If it is `Frozen` or `FramingCommitted`, including first exposure with zero acknowledged bytes, enter `FailedAfterDownstreamSuccessExposure`, finish the exact immutable HEADERS/CONTINUATION suffix contiguously through END_HEADERS, commit HPACK and framing normally, never activate or transfer tunnel input, and only then emit the reserved reset. If final END_HEADERS acknowledgement was processed before the DATA in the same combined call, its success hook may mint `BridgeActivationPermit` first and the DATA is legal Active input. A connection failure while the immutable suffix is finishing selects connection-owned cleanup without fabricating response completion, Active, permit, or reset completion. Later same-buffer SETTINGS, PING, HEADERS, and DATA for unrelated streams continue normally; never mutate/reset them, discard their bytes, or desynchronize HPACK.
- Never expose downstream 101/2xx before complete upstream inbound validation. First downstream success exposure freezes its exact bytes. `CommittedDownstreamSuccess` records full wire commitment only; it cannot override a latched premature-input failure or itself authorize Active. Only the engine-minted `BridgeActivationPermit` transfers each provenance-authorized input lease once without copying or releasing HTTP/2 credit. Success transfers success-following and permitted optimistic ordinary-CONNECT ownership once; non-2xx/failure and unpermitted/forbidden input dispose under their exact one-shot rules. Application acknowledgement or policy discard remains the sole reclamation path and WINDOW_UPDATE owner. Failure from any earlier phase normally remains an HTTP-framed downstream failure and invokes the HTTP/1 `PendingHttp1Transition` or existing HTTP/2 non-2xx/reset/PendingConnect cleanup once; premature RFC 8441 DATA uses the output-state arbitration above. Failure after any downstream success exposure closes downstream and aborts/resets the established upstream side without a replacement response or double discard. Over-read/PendingConnect bytes remain owned by their original leg and provenance until Active or cleanup.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test both directions with RFC 6455/RFC 8441 vectors: ws/wss scheme mapping, lowercase HTTP/2 names, Origin/version preservation, ordinary cookies/authorization, stripped/generated key/accept/Connection/Upgrade, hostile HTTP/2 key/accept noninfluence, fresh nonce, absent versus empty and duplicate offers, selected-but-unoffered protocol/extension, failure translation, and cancellation. Exhaust reservation one resource short before upstream exposure; cross every HTTP/1 head, outbound HTTP/2 field-block commitment, inbound HTTP/2 compression/terminal-semantic/correlation stage, ordered transaction phase, stale generation, lease kind, and failure phase. Compile-fail every cross-phase capability substitution, including equal numeric stream IDs with mismatched bridge/connection/leg/role/message/head generations. Prove inbound validation cannot be forged from outbound commitment, phase skipping/reordering is impossible, and downstream success never exposes before complete upstream success validation.
- Feed success HEADERS followed in the same input buffer by DATA, padded DATA, DATA plus END_STREAM, and RST_STREAM. Cross HTTP/1 ordinary CONNECT with both exact close-proof constructors, missing proof, configured intent alone, queued versus fully committed local close-bearing heads, every local head acknowledgement offset, stale/cross-head proof, early bytes, then 2xx/non-2xx; also cross HTTP/2 ordinary CONNECT DATA before 2xx versus RFC 8441 WebSocket DATA before 2xx, downstream HTTP/1 premature WebSocket bytes, zero/short/full/invalid success acknowledgement, legal upstream HTTP/1 101 plus data, and legal HTTP/2 success-following cases. Prove only success-following or permitted optimistic provenance creates a transferable lease, strict unpermitted input is discarded/closed once without reparse or later promotion, and forbidden input creates no Active/forwarding/lease or duplicate credit owner. At final commitment inject duplicate and stale acknowledgements, repeated completion-hook invocation, cancellation before/during/after the atomic mint, and bridge-generation teardown/reuse; require one consumption of `CommittedDownstreamSuccess` and the reserved slot, at most one permit and success event, no permit when cancellation wins first, and no duplicate Active publication or lease transfer.
- For premature RFC 8441 DATA, cross every valid/invalid padding and flow-window boundary; `AcceptedPrivate` with no exposure; first exposure with zero acknowledgement; every initial HEADERS acknowledgement offset; every CONTINUATION boundary and offset; final END_HEADERS acknowledgement in the same combined call before versus after DATA; and connection failure at every immutable suffix prefix. Require exact stream/connection charge, v0.136.0-only reclamation, private supersession followed only by reset, exposed suffix completion and normal HPACK/framing commitment before reset, no `BridgeActivationPermit`, Active, lease transfer, fabricated completion, or duplicate cleanup on the failure paths, and legal Active input only when the final acknowledgement hook wins first. Interleave SETTINGS, PING, HEADERS, and DATA for unrelated streams and require continued processing, no unrelated mutation/loss/reset, and no HPACK desynchronization.
- Include padding-only and mixed padded DATA, then cross every downstream-success output offset, stream/connection WINDOW_UPDATE threshold, GOAWAY, PendingConnect/bridge capacity boundary, and bridge cancellation. Test valid HTTP/1 success head plus terminal with zero over-read bytes in the same call and next call, over-read plus terminal, and optional over-read with `PlainTcpEof`, `TlsCloseNotify`, `TlsTruncationEof`, `FatalTlsAlert`, `TransportReset`, `TransportFailure`, or `Cancellation` at every bridge phase and immediately before/after first downstream success exposure. Test WebSocket pre-exposure handshake failure, ordinary CONNECT drain/close and preserve-versus-reject policies, pending FIN publication immediately after Active, and reset/fatal failure immediately before versus after first success exposure. Prove one existing owner per protocol and no duplicate copy/store, exact range order and padding/semantic accounting, no early/double credit or discard, immutable first terminal cause, exactly-once HTTP/1 optional-byte/terminal cleanup, no close_notify-derived TCP half-close, existing HTTP/2 cleanup once before Active, linear ranges/FIN transfer once at Active, generation teardown safety, partial downstream-success close/abort without a second response, and WebSocket bytes cross only after Active.
- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge contract and all previously implemented relevant behavior have
reproducible evidence; v0.162.0 (RFC 8441 extended CONNECT) still passes; no behavior assigned to v0.164.0 (vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.163.0 implementation stop reached. Run pentest for this exact commit.`

### v0.164.0 — vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton

Status: planned

#### Goal

Deliver **vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton** as the sole primary capability in this stop. It builds
on v0.163.0 (Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge) and must be independently trustworthy before v0.165.0 (Structured Fields integer and decimal ranges) begins.

#### Deliverables

- Acceptance contract: Introduce optional dependency-free no_std vef-structured-fields ownership, a checked incremental lexical cursor, and a non-publishing bare-item tag dispatcher skeleton; define consumed/blocked/error progress and caller-owned capacity now, but do not claim complete item parsing until every item grammar and the later complete dispatcher milestone exist.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton contract and all previously implemented relevant behavior have
reproducible evidence; v0.163.0 (Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge) still passes; no behavior assigned to v0.165.0 (Structured Fields integer and decimal ranges) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.164.0 implementation stop reached. Run pentest for this exact commit.`

### v0.165.0 — Structured Fields integer and decimal ranges

Status: planned

#### Goal

Deliver **Structured Fields integer and decimal ranges** as the sole primary capability in this stop. It builds
on v0.164.0 (vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton) and must be independently trustworthy before v0.166.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) begins.

#### Deliverables

- Acceptance contract: Enforce exact RFC 9651 integer/decimal digit, sign, scale, and numeric ranges with checked arithmetic, canonical internal values, and overflow distinguished from malformed syntax.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields integer and decimal ranges contract and all previously implemented relevant behavior have
reproducible evidence; v0.164.0 (vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton) still passes; no behavior assigned to v0.166.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.165.0 implementation stop reached. Run pentest for this exact commit.`

### v0.166.0 — Structured Fields strings, tokens, bytes, booleans, dates, and display strings

Status: planned

#### Goal

Deliver **Structured Fields strings, tokens, bytes, booleans, dates, and display strings** as the sole primary capability in this stop. It builds
on v0.165.0 (Structured Fields integer and decimal ranges) and must be independently trustworthy before v0.167.0 (Structured Fields complete bare-item dispatcher) begins.

#### Deliverables

- Acceptance contract: Implement each remaining bare-item grammar, escape/base64/date validation, display-string decoding policy, exact limits, and type-specific errors without automatic coercion.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields strings, tokens, bytes, booleans, dates, and display strings contract and all previously implemented relevant behavior have
reproducible evidence; v0.165.0 (Structured Fields integer and decimal ranges) still passes; no behavior assigned to v0.167.0 (Structured Fields complete bare-item dispatcher) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.166.0 implementation stop reached. Run pentest for this exact commit.`

### v0.167.0 — Structured Fields complete bare-item dispatcher

Status: planned

#### Goal

Deliver **Structured Fields complete bare-item dispatcher** as the sole primary capability in this stop. It builds
on v0.166.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) and must be independently trustworthy before v0.168.0 (Structured Fields parameters) begins.

#### Deliverables

- Acceptance contract: Complete the dependency-free vef-structured-fields bare-item dispatcher only after every RFC 9651 item grammar exists; dispatch without speculative publication, preserve exact consumed/blocked/error progress, enforce per-type ranges and caller-owned output capacity, and prove identical results for contiguous input and every fragmentation boundary.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC 9651 vectors, all-byte splits, malformed/capacity corpora,
  cross-type dispatcher cases, canonical round trips, and work-limit assertions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields complete bare-item dispatcher contract and all previously implemented relevant behavior have
reproducible evidence; v0.166.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) still passes; no behavior assigned to v0.168.0 (Structured Fields parameters) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.167.0 implementation stop reached. Run pentest for this exact commit.`

### v0.168.0 — Structured Fields parameters

Status: planned

#### Goal

Deliver **Structured Fields parameters** as the sole primary capability in this stop. It builds
on v0.167.0 (Structured Fields complete bare-item dispatcher) and must be independently trustworthy before v0.169.0 (Structured Fields inner lists and lists) begins.

#### Deliverables

- Acceptance contract: Parse parameters as an ordered map with index/key access and lowercase keys; when a duplicate key occurs, overwrite the existing value in place so all but the final value are ignored rather than rejected; support at least 256 parameters and 64-character keys in the RFC-conformant profile, preserve incremental publication/capacity atomicity, and return CapacityExceeded—not malformed syntax—when caller storage is insufficient.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields parameters contract and all previously implemented relevant behavior have
reproducible evidence; v0.167.0 (Structured Fields complete bare-item dispatcher) still passes; no behavior assigned to v0.169.0 (Structured Fields inner lists and lists) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.168.0 implementation stop reached. Run pentest for this exact commit.`

### v0.169.0 — Structured Fields inner lists and lists

Status: planned

#### Goal

Deliver **Structured Fields inner lists and lists** as the sole primary capability in this stop. It builds
on v0.168.0 (Structured Fields parameters) and must be independently trustworthy before v0.170.0 (Structured Fields dictionaries) begins.

#### Deliverables

- Acceptance contract: Parse bounded inner lists and top-level lists with whitespace rules, item/parameter ownership, nesting fixed by grammar, and independent member/work limits.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields inner lists and lists contract and all previously implemented relevant behavior have
reproducible evidence; v0.168.0 (Structured Fields parameters) still passes; no behavior assigned to v0.170.0 (Structured Fields dictionaries) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.169.0 implementation stop reached. Run pentest for this exact commit.`

### v0.170.0 — Structured Fields dictionaries

Status: planned

#### Goal

Deliver **Structured Fields dictionaries** as the sole primary capability in this stop. It builds
on v0.169.0 (Structured Fields inner lists and lists) and must be independently trustworthy before v0.171.0 (Structured Fields canonical serialization) begins.

#### Deliverables

- Acceptance contract: Parse dictionaries as ordered maps with index/key access, implicit true booleans, Items/Inner Lists, and parameters; when a duplicate key occurs, overwrite its existing value in place so all but the final value are ignored rather than rejected; support at least 1,024 members and 64-character keys in the RFC-conformant profile with independent work/storage limits and CapacityExceeded distinct from malformed syntax.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields dictionaries contract and all previously implemented relevant behavior have
reproducible evidence; v0.169.0 (Structured Fields inner lists and lists) still passes; no behavior assigned to v0.171.0 (Structured Fields canonical serialization) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.170.0 implementation stop reached. Run pentest for this exact commit.`

### v0.171.0 — Structured Fields canonical serialization

Status: planned

#### Goal

Deliver **Structured Fields canonical serialization** as the sole primary capability in this stop. It builds
on v0.170.0 (Structured Fields dictionaries) and must be independently trustworthy before v0.172.0 (Structured Fields incremental parsing and caller-owned storage) begins.

#### Deliverables

- Acceptance contract: Serialize every item/list/dictionary type in canonical RFC 9651 form under partial output, with size preflight and no state advancement before bytes commit.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields canonical serialization contract and all previously implemented relevant behavior have
reproducible evidence; v0.170.0 (Structured Fields dictionaries) still passes; no behavior assigned to v0.172.0 (Structured Fields incremental parsing and caller-owned storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.171.0 implementation stop reached. Run pentest for this exact commit.`

### v0.172.0 — Structured Fields incremental parsing and caller-owned storage

Status: planned

#### Goal

Deliver **Structured Fields incremental parsing and caller-owned storage** as the sole primary capability in this stop. It builds
on v0.171.0 (Structured Fields canonical serialization) and must be independently trustworthy before v0.173.0 (Structured Fields malformed-input and complexity limits) begins.

#### Deliverables

- Acceptance contract: Bind all parsers to borrowed input and caller-provided stores, preserve progress across every byte split, acknowledge published values before reuse, and expose NeedInput/NeedOutput/CapacityExceeded distinctly.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields incremental parsing and caller-owned storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.171.0 (Structured Fields canonical serialization) still passes; no behavior assigned to v0.173.0 (Structured Fields malformed-input and complexity limits) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.172.0 implementation stop reached. Run pentest for this exact commit.`

### v0.173.0 — Structured Fields malformed-input and complexity limits

Status: planned

#### Goal

Deliver **Structured Fields malformed-input and complexity limits** as the sole primary capability in this stop. It builds
on v0.172.0 (Structured Fields incremental parsing and caller-owned storage) and must be independently trustworthy before v0.174.0 (Priority field semantics) begins.

#### Deliverables

- Acceptance contract: Publish an RFC-conformant resource profile supporting at least 1,024 List and Dictionary members, 256 Inner List members, 256 parameters, 64-character keys, 1,024-character decoded Strings, 512-character Tokens, 16,384 decoded Byte Sequence octets, and every Date from year 1 through 9999 (-62,135,596,800 through 253,402,214,400 seconds); label every smaller bare-metal profile constrained rather than generally RFC 9651 conformant, return CapacityExceeded for insufficient caller storage, and cap duplicate overwrite, lookup, decoding, and one-byte fragmentation work non-quadratically.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields malformed-input and complexity limits contract and all previously implemented relevant behavior have
reproducible evidence; v0.172.0 (Structured Fields incremental parsing and caller-owned storage) still passes; no behavior assigned to v0.174.0 (Priority field semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.173.0 implementation stop reached. Run pentest for this exact commit.`

### v0.174.0 — Priority field semantics

Status: planned

#### Goal

Deliver **Priority field semantics** as the sole primary capability in this stop. It builds
on v0.173.0 (Structured Fields malformed-input and complexity limits) and must be independently trustworthy before v0.175.0 (SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration) begins.

#### Deliverables

- Acceptance contract: Map RFC 9218 urgency and incremental parameters through the Structured Fields API, apply defaults and invalid-field handling, and separate advisory priority from protocol correctness.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority field semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.173.0 (Structured Fields malformed-input and complexity limits) still passes; no behavior assigned to v0.175.0 (SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.174.0 implementation stop reached. Run pentest for this exact commit.`

### v0.175.0 — SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration

Status: planned

#### Goal

Deliver **SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration** as the sole primary capability in this stop. It builds
on v0.174.0 (Priority field semantics) and must be independently trustworthy before v0.176.0 (Priority scheduling hints and fairness) begins.

#### Deliverables

- Acceptance contract: Apply SETTINGS_NO_RFC7540_PRIORITIES only when it appears in the peer's initial SETTINGS frame, reject later or contradictory occurrences with the RFC-defined connection error, and bind the negotiated mode to generation-stable connection state; in legacy mode retain RFC 7540 dependency signals, while in no-legacy mode ignore prohibited legacy priority signals and use RFC 9218 Priority inputs without treating advisory priority as protocol correctness; define the admission rule for later PRIORITY_UPDATE support without claiming that frame capability here.
- Bind any locally emitted NO_RFC7540_PRIORITIES value and every later enabled
  extension setting to an engine-owned outbound SETTINGS commit-plan
  participant. Prevalidate initial-only/monotonic rules before acceptance and
  activate local advertised state only at full frame acknowledgement, never at
  reservation, prefix exposure, or peer ACK.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add initial-versus-later SETTINGS vectors, duplicate/contradictory values,
  legacy/no-legacy mode transitions, ignored legacy signals, and bounded
  priority-input stateful traces.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.174.0 (Priority field semantics) still passes; no behavior assigned to v0.176.0 (Priority scheduling hints and fairness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.175.0 implementation stop reached. Run pentest for this exact commit.`

### v0.176.0 — Priority scheduling hints and fairness

Status: planned

#### Goal

Deliver **Priority scheduling hints and fairness** as the sole primary capability in this stop. It builds
on v0.175.0 (SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration) and must be independently trustworthy before v0.177.0 (Priority intermediary behavior) begins.

#### Deliverables

- Acceptance contract: Feed validated priority hints into bounded scheduling with starvation prevention, deterministic tie-breaking, reprioritization cost limits, and no peer-controlled unbounded queue movement.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority scheduling hints and fairness contract and all previously implemented relevant behavior have
reproducible evidence; v0.175.0 (SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration) still passes; no behavior assigned to v0.177.0 (Priority intermediary behavior) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.176.0 implementation stop reached. Run pentest for this exact commit.`

### v0.177.0 — Priority intermediary behavior

Status: planned

#### Goal

Deliver **Priority intermediary behavior** as the sole primary capability in this stop. It builds
on v0.176.0 (Priority scheduling hints and fairness) and must be independently trustworthy before v0.178.0 (PRIORITY_UPDATE frame support) begins.

#### Deliverables

- Acceptance contract: Define when intermediaries consume, forward, regenerate, or ignore Priority fields and how local policy overrides are represented without misreporting upstream choices.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority intermediary behavior contract and all previously implemented relevant behavior have
reproducible evidence; v0.176.0 (Priority scheduling hints and fairness) still passes; no behavior assigned to v0.178.0 (PRIORITY_UPDATE frame support) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.177.0 implementation stop reached. Run pentest for this exact commit.`

### v0.178.0 — PRIORITY_UPDATE frame support

Status: planned

#### Goal

Deliver **PRIORITY_UPDATE frame support** as the sole primary capability in this stop. It builds
on v0.177.0 (Priority intermediary behavior) and must be independently trustworthy before v0.179.0 (Priority update flood budgeting) begins.

#### Deliverables

- Acceptance contract: Implement only HTTP/2 PRIORITY_UPDATE type 0x10 with every target state expressed from the receiving server's perspective, frame-header stream identifier zero, ignored unknown flags, and zero outbound reserved bits; require at least four payload bytes for a nonzero reserved-bit-masked 31-bit prioritized stream identifier or return connection FRAME_SIZE_ERROR/PROTOCOL_ERROR respectively; permit only client-to-server frames and return connection PROTOCOL_ERROR if a client receives one; for request streams apply/buffer the latest update in idle, open, or half-closed-remote and discard half-closed-local/closed targets; for push streams accept reserved-local or half-closed-remote, discard closed, and reject idle with connection PROTOCOL_ERROR; keep idle-prioritized plus active streams within SETTINGS_MAX_CONCURRENT_STREAMS or return connection PROTOCOL_ERROR; parse the remaining ASCII Priority Field Value and, by fixed policy, ignore a malformed update while retaining prior/default priority and charging its flood budget.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PRIORITY_UPDATE frame support and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PRIORITY_UPDATE frame support contract and all previously implemented relevant behavior have
reproducible evidence; v0.177.0 (Priority intermediary behavior) still passes; no behavior assigned to v0.179.0 (Priority update flood budgeting) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.178.0 implementation stop reached. Run pentest for this exact commit.`

### v0.179.0 — Priority update flood budgeting

Status: planned

#### Goal

Deliver **Priority update flood budgeting** as the sole primary capability in this stop. It builds
on v0.178.0 (PRIORITY_UPDATE frame support) and must be independently trustworthy before v0.180.0 (Client request builder and target forms) begins.

#### Deliverables

- Acceptance contract: Rate-limit parse work, queued updates, scheduler mutations, and response/control amplification independently while preserving connection progress for non-priority frames.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority update flood budgeting contract and all previously implemented relevant behavior have
reproducible evidence; v0.178.0 (PRIORITY_UPDATE frame support) still passes; no behavior assigned to v0.180.0 (Client request builder and target forms) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.179.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.0 — Client request builder and target forms

Status: planned

#### Goal

Deliver **Client request builder and target forms** as the sole primary capability in this stop. It builds
on v0.179.0 (Priority update flood budgeting) and must be independently trustworthy before v0.180.1 (Dependency-free conditional semantics crate and validators) begins.

#### Deliverables

- Acceptance contract: Build origin-, absolute-, authority-, and asterisk-form draft requests with method coherence, validated Host/authority, ordered fields, sensitive-indexing metadata, exact body framing, injection-proof internal serialization, and capacity failure before any request token or bytes are published; expose no public raw-head serialization token, because v0.180.4 must final-validate the exact frozen draft including known fields inserted through generic APIs.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Client request builder and target forms and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client request builder and target forms contract and all previously implemented relevant behavior have
reproducible evidence; v0.179.0 (Priority update flood budgeting) still passes; no behavior assigned to v0.180.1 (Dependency-free conditional semantics crate and validators) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.180.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.1 — Dependency-free conditional semantics crate and validators

Status: planned

#### Goal

Deliver **Dependency-free conditional semantics crate and validators** as the sole primary capability in this stop. It builds
on v0.180.0 (Client request builder and target forms) and must be independently trustworthy before v0.180.2 (Conditional request fields and ordered precondition evaluation) begins.

#### Deliverables

- Acceptance contract: Add a separate dependency-free, no_std `vef-conditions` crate depending only on `vef-core`; implement bounded incremental entity-tag parsing with exact weak-prefix/opaque-tag grammar, raw preservation, and distinct RFC strong/weak comparison; implement checked HTTP-date parsing for IMF-fixdate and the two required obsolete received forms, reject impossible calendar/time values and every direct or resolved year below 1900, use the complete v0.157.4 `CivilTimeEvidence::Available` instant for the exact RFC 850 more-than-50-year comparison, return UnresolvedCivilTime rather than guessing when current-instant evidence is unavailable, and emit only IMF-fixdate. Enforce explicit byte/digit/work/storage limits, preserve syntax versus capacity dispositions, and accept caller-supplied current ETag and last-modified evidence without inventing representation state.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable RFC 9110 conditional-request requirements and inherited RFC 5322 Section 3.3 HTTP-date semantics, role/applicability decisions, SHOULD dispositions, deviations, verified/held errata, threat model, controls, API docs, release notes, traceability, resource measurements, and conformance corpora.
- Define exact progress, capacity, cancellation, ownership, publication, commit/rollback, and typed error behavior for the new crate.

#### Verification

- Test every valid/invalid weak and strong entity tag, opaque-tag boundary, strong/weak comparison combination, all three received HTTP-date formats, RFC 850 exactly-50-years and plus-one-second, leap-day/end-of-year/century/maximum-year boundaries with Available evidence, unavailable-current-instant rejection, generic-civil acceptance versus pre-1900 HTTP-date rejection, canonical IMF generation, calendar/weekday and numeric boundaries, every-byte splits, truncation, capacity/work exhaustion, arbitrary-input no-panic behavior, and no hidden allocation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The dependency-free conditional validators and all previously implemented relevant behavior have reproducible evidence; v0.180.0 (Client request builder and target forms) still passes; no behavior assigned to v0.180.2 (Conditional request fields and ordered precondition evaluation) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.180.1 implementation stop reached. Run pentest for this exact commit.`

### v0.180.2 — Conditional request fields and ordered precondition evaluation

Status: planned

#### Goal

Deliver **Conditional request fields and ordered precondition evaluation** as the sole primary capability in this stop. It builds
on v0.180.1 (Dependency-free conditional semantics crate and validators) and must be independently trustworthy before v0.180.3 (Bounded byte ranges and single-range response planning) begins.

#### Deliverables

- Acceptance contract: In `vef-conditions`, parse bounded If-Match and If-None-Match as either the exclusive wildcard or an ordered entity-tag list; parse If-Modified-Since, If-Unmodified-Since, and If-Range with field-specific invalid-value dispositions. Define a read-only `PendingConditionalRequest` that exposes only the validated head and selection inputs; accept generation-bound application evidence but forbid body delivery, method execution, and reentrant engine commands while evaluation is pending. Evaluate preconditions only for an origin server or authorized cache, only when the otherwise selected response is 2xx or 412, and only for a method that selects or modifies a representation; non-evaluating intermediaries preserve them and CONNECT/OPTIONS/TRACE ignore them. Evaluate RFC 9110 preconditions in order—If-Match, If-Unmodified-Since only when If-Match is absent, If-None-Match, then If-Modified-Since only for GET/HEAD when If-None-Match is absent—before processing request content, method execution, or range selection.
- Separate admission evidence from response construction. A sealed generation-bound `CurrentRepresentationEvidence` contains only the pre-action representation identity/generation, existence, current ETag, and Last-Modified needed by conditional GET/HEAD and unsafe methods. A sealed retrieval-only `WouldBe200Snapshot` refines matching current evidence for GET/HEAD with encoded length, Content-Type/content-coding, Date evidence, and the exact ordered fields that the corresponding 200 would contain, including Cache-Control, Expires, Content-Location, Vary, and other representation metadata. `PreconditionOutcome` always references the exact current evidence and references the retrieval snapshot only where GET/HEAD 304 or later range/response construction needs it; unsafe PUT/POST/DELETE admission never requires hypothetical-200 metadata. Before admission, any relevant evidence, selection, role, method, or request change invalidates the outcome.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable RFC 9110 conditional-request requirements, role/applicability decisions, SHOULD dispositions, deviations, verified/held errata, threat model, controls, API docs, release notes, traceability, resource measurements, and conformance corpora.
- Define exact progress, capacity, cancellation, ownership, publication, commit/rollback, and typed error behavior for evaluation and evidence lifetimes.

#### Verification

- Exhaust wildcard/list syntax, duplicate and malformed field disposition, method/role/status applicability, absent representation, strong/weak comparisons, invalid/obsolete dates, every RFC precondition-order permutation, If-None-Match precedence over If-Modified-Since, If-Match precedence over If-Unmodified-Since, satisfied/304/412 results, stale/cross-request/cross-exchange evidence, PendingConditionalRequest read-only/reentrancy restrictions, unsafe admission with no hypothetical 200, current-evidence versus retrieval-snapshot identity, retrieval field presence/order and same-generation substitution, every pre-admission invalidating mutation, all splits/limits, and model-based comparison with the requirement table.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The conditional-field and ordered-evaluation contract and all previously implemented relevant behavior have reproducible evidence; v0.180.1 (Dependency-free conditional semantics crate and validators) still passes; no behavior assigned to v0.180.3 (Bounded byte ranges and single-range response planning) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.180.2 implementation stop reached. Run pentest for this exact commit.`

### v0.180.3 — Bounded byte ranges and single-range response planning

Status: planned

#### Goal

Deliver **Bounded byte ranges and single-range response planning** as the sole primary capability in this stop. It builds
on v0.180.2 (Conditional request fields and ordered precondition evaluation) and must be independently trustworthy before v0.180.4 (Outbound conditional and range request validation) begins.

#### Deliverables

- Acceptance contract: In `vef-conditions`, parse bounded Range byte-range, open-ended range, and suffix-range members plus satisfied and unsatisfied Content-Range forms with checked decimal accumulation; cap raw bytes, decimal digits, member count, normalization work, and output before arithmetic, reject overflow/reversed/impossible Content-Range, and distinguish malformed syntax/capacity from an unsupported request Range unit, which an origin ignores as a full-response disposition. Unknown received Content-Range units still undergo the generic `range-unit SP (range-resp / unsatisfied-range)` grammar exactly once: require one valid alternative, checked decimal parsing, first-pos <= last-pos, and a known complete length greater than last-pos. Preserve the bounded unit and raw value as `OpaqueUnknownContentRange` only after those unit-independent checks, without unit-specific arithmetic or recombination authority; malformed and unknown remain distinct. Ignore Range except on GET and apply If-Range only at the final RFC precondition step: entity tags use strong comparison, dates require caller-certified strong-validator status and exact equality with Last-Modified, and false conditions select the full response. Normalize against the exact v0.180.2 `WouldBe200Snapshot` with checked inclusive arithmetic; issue a sealed `SingleRangePlan` only for one normalized satisfiable range, a generation-bound unsatisfied context for 416, or a typed full-response/policy disposition, never multipart generation.
- Consume the matching PreconditionsSatisfied outcome and complete the gate with non-forgeable one-shot `RequestContentPermit` and `MethodExecutionPermit` bound to the request/exchange generation and exact `CurrentRepresentationEvidence`, plus `WouldBe200Snapshot` only for retrieval. Terminal 304/412 produces neither permit. No request content may be processed or published and no method side effect may occur before these permits. A pre-admission evidence, method, field, policy, or generation change requires full re-evaluation; once consumed, `MethodExecutionPermit` authorizes exactly one execution and remains valid through the representation mutation caused by that execution, after which response construction requires fresh post-action evidence/snapshots rather than retroactive invalidation.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable RFC 9110 range requirements and security considerations, role/applicability decisions, SHOULD dispositions, deviations, verified/held errata, threat model, controls, API docs, release notes, traceability, resource measurements, and conformance corpora.
- Define exact progress, capacity, cancellation, ownership, publication, commit/rollback, and typed error behavior for parsing, normalization, and range-plan lifetimes.

#### Verification

- Test closed/open/suffix boundaries, zero-length representations, clamping, satisfiable/unsatisfied results, all byte Content-Range forms, maximum and overflowing decimals, digit/member/work caps, many/overlapping/tiny-range policy, unsupported-request-unit ignore versus malformed syntax, and unknown-unit valid/invalid alternative count, reversed positions, impossible complete length, overflow, injection, and capacity. Exhaust If-Range outcomes, wrong/stale/cross-generation evidence and retrieval snapshots, every pre-admission mutation, a consumed unsafe execution permit surviving exactly its own mutation but not reuse, fresh post-action response evidence, missing/forged/duplicated/swapped permits, terminal 304/412 issuing none, exact single-range body agreement, multipart impossibility, every-byte splits, fuzz/model arithmetic, and no panic or hidden allocation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The bounded range and single-range planning contract and all previously implemented relevant behavior have reproducible evidence; v0.180.2 (Conditional request fields and ordered precondition evaluation) still passes; no behavior assigned to v0.180.4 (Outbound conditional and range request validation) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.180.3 implementation stop reached. Run pentest for this exact commit.`

### v0.180.4 — Outbound conditional and range request validation

Status: planned

#### Goal

Deliver **Outbound conditional and range request validation** as the sole primary capability in this stop. It builds
on v0.180.3 (Bounded byte ranges and single-range response planning) and must be independently trustworthy before v0.180.5 (Partial-response media-type classification integration) begins.

#### Deliverables

- Acceptance contract: Add one final `vef-conditions` validation pass over the exact frozen ordered client request before either HTTP engine serializes it; typed builders and known conditional/range fields inserted through a generic field API converge on the same sealed non-Copy/non-Clone `ValidatedConditionalRequest`, and neither HTTP/1 nor HTTP/2 accepts the raw request beside a token. Enforce bounded field grammar, duplicates, method applicability, byte-range arithmetic, one generated range only for the 1.0 single-range profile, and all conditional interactions before output.
- Reject local If-Range without Range, weak entity-tag If-Range, and date-based If-Range unless no ETag is available for that stored representation and caller evidence certifies the date as a strong validator; bind the validated request to its request generation, exact requested range, target/representation identity, available validator, and later v0.181.0 correlation token. Unsupported locally generated range units and multipart-dependent requests are InvalidState, while received unsupported units remain the v0.180.3 origin ignore disposition.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable RFC 9110 client conditional/range requirements, threat model, APIs, release notes, traceability, resource measurements, and conformance corpora.

#### Verification

- Test typed/generic-field equivalence; missing Range, weak If-Range, ETag-present date rejection, weak date evidence, valid strong entity-tag/date paths, single/multiple/unknown/malformed ranges, wrong methods, duplicate fields, frozen-field substitution and mutation, wrong protocol/generation, zero prevalidation bytes, HTTP/1 and lowercase HTTP/2 output, every split/capacity/cancellation case, and compile-fail attempts to forge or reuse validation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The outbound conditional/range request contract and all previously implemented relevant behavior have reproducible evidence; v0.180.3 (Bounded byte ranges and single-range response planning) still passes; no behavior assigned to v0.180.5 (Partial-response media-type classification integration) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.180.4 implementation stop reached. Run pentest for this exact commit.`

### v0.180.5 — Partial-response media-type classification integration

Status: planned

#### Goal

Deliver **Partial-response media-type classification integration** as the sole primary capability in this stop. It builds
on v0.180.4 (Outbound conditional and range request validation) and must be independently trustworthy before v0.181.0 (Client correlation, cancellation, and retry tokens) begins.

#### Deliverables

- Acceptance contract: Reuse only the v0.157.5 `vef-media-type` grammar and exact `ParsedMediaType` evidence; add partial-response-specific field-set validation and sealed `PartialContentTypeClassification::{Absent, NonMultipart, MultipartByteRanges}`. More than one Content-Type field, malformed/stale/substituted evidence, or any classification attempted before the entire ordered field set validates is a framing-synchronized received semantic violation and yields no classification capability. `NonMultipart` is the sole valid present non-multipart state; there is no ambiguous SinglePart versus Other distinction.
- Recognize `multipart/byteranges` only by exact case-insensitive type/subtype comparison regardless of parameter order or casing. Enforce the source-locked RFC 2046 boundary grammar: exactly one required nonempty boundary parameter, at most 70 characters, only permitted boundary characters, no trailing space, valid quoted-string decoding, and the generic v0.157.5 raw/decoded/work limits. Exact multipart/byteranges with an absent, empty, duplicate, overlong, or otherwise invalid boundary is a synchronized semantic violation with no partial capability and can never fall through to `Absent` or `NonMultipart`; misleading prefix/suffix names remain `NonMultipart`.
- Starting here `vef-conditions` depends on `vef-media-type` and accepts only its sealed classification in v0.181.1. `MultipartByteRanges` can never grant top-level Content-Range, stored-segment, or combination authority; `Absent`/`NonMultipart` can enter the single-part path only when every independent 206 and Content-Range check passes. Semantic violations remain synchronized under recipient policy but produce no validated partial head.
- Update paragraph-addressable RFC 2046 boundary grammar and RFC 9110 media-type, Content-Type, 206, multipart/byteranges, and security requirements plus threat model, API docs, release notes, traceability, resource measurements, and conformance corpora.

#### Verification

- Exhaust reuse of v0.157.5 evidence, exact type/subtype casing, boundary quoted/unquoted forms, permitted characters, lengths 0/1/70/71, trailing space, parameter order, missing/empty/duplicate boundary, duplicate Content-Type fields, stale/substituted evidence, malformed quotes/escapes, every misleading exact-match prefix/suffix, multipart with top-level Content-Range, all independent limits, and every split/truncation. Prove exact multipart with any invalid boundary produces a semantic violation rather than `NonMultipart`; only exact sealed `MultipartByteRanges` reaches `NeedsMultipartConsumer`; and no malformed/multipart input reaches single-range or combination paths.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The partial-response media-type classification integration contract and all previously implemented relevant behavior have reproducible evidence; v0.180.4 (Outbound conditional and range request validation) and v0.157.5 (Dependency-free media-type grammar) still pass; no behavior assigned to v0.181.0 (Client correlation, cancellation, and retry tokens) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.180.5 implementation stop reached. Run pentest for this exact commit.`

### v0.181.0 — Client correlation, cancellation, and retry tokens

Status: planned

#### Goal

Deliver **Client correlation, cancellation, and retry tokens** as the sole primary capability in this stop. It builds
on v0.180.5 (Partial-response media-type classification integration) and must be independently trustworthy before v0.181.1 (Streaming partial-response and retained-prefix validation) begins.

#### Deliverables

- Acceptance contract: Assign one generation-safe request token retaining the exact v0.180.4 `ValidatedConditionalRequest`, requested range, target/representation identity, and validator evidence; correlate informational/final responses, body/trailers, cancellation, reset, GOAWAY, and connection loss; classify possibly-unprocessed separately from replay safety, expose the correlation to v0.181.1 without caller rebinding, and publish no duplicate terminal event. For a locally initiated request when assembly is enabled, before serializing any request byte or creating its correlation, reserve one non-forgeable `AssemblyInvalidationHandle` containing at least effective target, opaque representation principal, privacy partition, and navigation namespace. This mandatory metadata comes from an engine-only fixed per-shard reserve that Vary fields, normalization, identity storage, another shard, and other optional peer-driven work cannot consume. Exhaustion returns typed local `AssemblyInvalidationCapacity`, emits zero request bytes, creates no correlation, never rotates or clears an existing arena, and applies ordinary Sans-I/O backpressure until capacity is released; it cannot continue as NoRecombine because a later full 200 still needs replacement invalidation. Each arena has a mandatory caller-supplied principal/tenant shard identity and cannot contain another shard. A caller that intentionally disables assembly for the entire shard generation must explicitly rotate/clear that shard before admitting any request without a handle.
- Extend the v0.145.0 receiving-client PUSH_PROMISE transaction only after complete HPACK and semantic validation of the immutable `TerminalFieldSectionLease`, but before promised-request publication. Atomically preflight the stream slot, assembly handle, pushed provenance, rejection tracking, compression workspace, and semantic-section capacity independently. Capacity failure keeps the tracked slot rejecting and publishes no request/correlation. Apply the exact v0.145.0 terminal/lease pipeline: END_STREAM leaves policy reset dormant and the sealed section leased through every stage; valid transfers it into the unpublished promised-message lifecycle, malformed re-arms and releases once, peer reset aborts after HPACK and releases once, and fatal failure transfers all cleanup to bounded shutdown. Dynamic-table mutation never invalidates the section. Every slot, handle, provenance lease, reset, terminal state/stage, compression workspace, field-section lease, tombstone, and shutdown record reaches exactly one terminal owner.
- Concretely, wait until after the complete promised field block and all CONTINUATION input have decoded. Atomically preflight/commit the existing promised-stream slot, matching `AssemblyInvalidationHandle`, independent pushed-provenance storage, and mandatory rejection-tombstone/cutoff tracking, plus an independent semantic-section lease. If any later admission resource is unavailable, retain the provisional slot, set only `PolicyDisposition::Rejecting`, leave its RFC wire state reserved(remote), queue `ResetReason::PolicyCancel`, and publish nothing; the ID is never momentarily untracked. Reserved(remote) DATA and duplicate promised ID remain connection PROTOCOL_ERROR. If mandatory tracking/lease state cannot be represented, retain the slot and initiate typed bounded `PushRejectionTrackingUnavailable` shutdown. Every provisional slot, handle, provenance lease, reset reservation/command, terminal state/stage, compression workspace, field-section lease, field-block owner, tombstone, and shutdown record releases or transfers exactly once.
- The inherited reset reservation also pre-reserves its frozen 13-byte record and output generation. Assembly/provenance failure may queue or re-arm policy/error reason only before exposure; once offered, every correlation/reset/GOAWAY/failure path retains the exact frame and token/cursor until completion or acknowledged-prefix cleanup, preventing promised-slot or tombstone reuse.
- At the same transaction, derive sealed non-Copy/non-Clone `PushedAssemblyProvenance` from the exact validated promised target plus the associated locally initiated request and caller push policy—never peer identity claims. Copy into engine-owned fixed storage or independently lease only the minimal immutable effective-target, principal, privacy-partition, tenant-shard, navigation-namespace, policy-generation, and assembly-arena/generation evidence required by the promised response; it must not borrow associated-stream application/request buffers. Bind the accepted pushed handle and correlation permanently to that provenance. Associated-stream completion/reset/terminal delivery and buffer recycling cannot release, mutate, or rebind it; later principal/navigation/policy changes cannot alter it. Provenance storage/lease exhaustion returns typed local `PushedAssemblyProvenanceCapacity` and rejects before publication through the tracked path above. Multiple promised streams from one associated request own independent provenance lifetimes and release exactly once with their own terminal correlations.
- Make `AssemblyInvalidationHandle` a linear non-Copy/non-Clone capability bound to exactly one ordinary or promised-request correlation and, for push, its independent `PushedAssemblyProvenance`. Reserve it once before local request output or promised-request publication; for accepted push hold both through reserved(remote), open response, informational response, body/trailers, reset, GOAWAY, connection failure, and terminal-event backpressure. Release each exactly once only after final completion and terminal delivery, cancellation, reset, connection failure, or a committed retry disposition. A retry cannot duplicate or rebind the old handle/provenance: the old correlation reaches its release disposition and the new correlation independently reserves before output. Fixed per-shard and per-connection assembly-admission limits bound stalled correlations and accepted pushes, and one shard's exhaustion cannot borrow or consume another shard's reserve.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Client correlation, cancellation, and retry tokens and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Exhaust handles with concurrent HTTP/2 requests, accepted pushes, and stalled streams at every per-shard/per-connection limit; prove local `AssemblyInvalidationCapacity` emits no request bytes, creates no tracked correlation, applies resumable backpressure, never rotates/clears an existing arena, and cannot consume another shard's reserve. For push floods independently exhaust all admission/tracking capacities; cross wire/reset/reason/validation/closure state, END_STREAM/END_HEADERS, message phase, valid/malformed status/fields/Content-Length/body rules, peer reset, duplicate promise, HPACK success/failure, payload/padding credit, every reset output boundary, GOAWAY, connection failure, and typed shutdown. Prove valid remote completion releases a dormant reserved policy reset; malformed terminal completion emits exactly one PROTOCOL_ERROR reset only when the reservation remains unexposed; an exposed CANCEL remains the sole frozen reset and resumes at its acknowledged suffix; an exposed protocol reset never downgrades or duplicates; fatal HPACK wins connection shutdown; and wire, credit, HPACK, token, and acknowledged-prefix state remain exact. For accepted pushes close/reset/terminally deliver the associated stream immediately, recycle and overwrite buffers, mutate principal/navigation/policy inputs, and complete multiple promised responses independently; prove immutable provenance/handles and every reset/validation record release once. Exercise pushed full 200/206 handoff, cancellation, retry, stale/rebound/Copy/Clone attempts, and whole-shard assembly disable ordering; prove distinct principal/tenant shards never share an arena.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client correlation, cancellation, and retry tokens contract and all previously implemented relevant behavior have
reproducible evidence; v0.180.5 (Partial-response media-type classification integration) still passes; no behavior assigned to v0.181.1 (Streaming partial-response and retained-prefix validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.181.0 implementation stop reached. Run pentest for this exact commit.`

### v0.181.1 — Streaming partial-response and retained-prefix validation

Status: planned

#### Goal

Deliver **Streaming partial-response and retained-prefix validation** as the sole primary capability in this stop. It builds
on v0.181.0 (Client correlation, cancellation, and retry tokens) and must be independently trustworthy before v0.181.2 (Cross-request partial assembly and header synthesis) begins.

#### Deliverables

- Acceptance contract: Add a non-forgeable `PartialResponseDisposition` bound permanently to the exact v0.180.4 validated locally initiated request or v0.181.0 validated promised request, its request/correlation generation, and its `AssemblyInvalidationHandle`; pushed disposition also requires the exact independent `PushedAssemblyProvenance`. Consume only v0.180.5 sealed Content-Type classification: `MultipartByteRanges` yields opaque `NeedsMultipartConsumer` and forbids top-level Content-Range/segment/combination authority; malformed/duplicate Content-Type or exact multipart with invalid boundary yields a synchronized semantic violation and no partial capability; only `Absent`/`NonMultipart` can continue through every independent single-part check. Publish `ValidatedPartialResponseHead` only after exactly one understood bytes Content-Range, requested-range correlation, head semantics, and limits pass; it starts generation-bound inclusive body accounting. A pushed 206 without the exact admitted promised-request correlation, handle, and provenance cannot stream into retention or assembly. Missing, weak, or mismatching validators do not invalidate standalone streaming and produce `StandaloneOnly`/`NoRecombine`.
- Before consuming body bytes accept a public freely constructible `PartialDeliveryPreference::{StreamOnly, RetainOnly, StreamAndRetain}` and have the correlation engine validate storage, response kind, capacity, and generation before issuing one sealed non-forgeable `SelectedPartialDelivery` permit with the same three modes. The permit, not the preference, authorizes body handling. `StreamOnly` publishes borrowed acknowledgement-capable `PartialBodyChunk<'a>` events without storage. `RetainOnly` writes/accounts bytes without application chunk publication. `StreamAndRetain` copies and accounts each chunk into retained storage before publishing its borrowed event, and acknowledgement cannot recycle transport input until that retention write commits. Issue `StandalonePartialComplete` only after exact length and the entire message, including permitted trailers, complete; malformed, out-of-request, unknown-unit, short, or long responses never produce completion proof.
- Retention is explicit and optional. Before a 206 body, preflight the known inclusive Content-Range length against an exclusive `&mut [u8]` or sealed fixed-arena slot before consuming any content; insufficiency is typed local `RetentionCapacity`, never a peer error. The safe API gives engine writes exclusive access and freezes the completed region as immutable `StoredRepresentationSlice<'a>` with exact `StorageLeaseGeneration`, interval, and `TransferDecodedContentEncoded` domain; only resulting `StoredPartialSegment` can refine for combination. No trust constructor/caller storage trait/alias exists, and DMA adapters fence first. In `RetainOnly`, unexpected storage failure cancels/discards under transport policy; in `StreamAndRetain`, a retained incomplete-200 buffer filling irrevocably transitions to `StreamOnly(NoRetainedPrefix)` and streaming continues, while already retained bytes receive no prefix authority. Cancellation yields a retained incomplete prefix only when every content octet received before cancellation was stored and existing framing/synchronization checks pass.
- Finalize `StoredPartialSegment` only after complete termination and validated trailers. A permitted trailer ETag can supply final strong-validator evidence when the head omitted it, retained with trailer provenance and never merged into the head/stored-header section; duplicate head/trailer ETag receives `DuplicateValidatorEvidence`, differing values receive `ConflictingValidatorEvidence`, and neither becomes combinable. Trailer processing cannot alter Content-Range, interval, content coding/byte domain, request correlation, or the original `ResponseHeadReceiptOrdinal`; standalone streaming can proceed before final validator eligibility is known.
- At atomic validated-head publication, the correlation engine parses bounded Vary field-name lists and derives sealed semantic `VariantSelectionIdentity` from the Vary names and corresponding exact original-request values, opaque caller representation principal, cache/privacy partition, and navigation identity. It separately mints non-forgeable `VariantSelectionEvidence` containing that identity plus the exact request, response, correlation, and selection provenance generations. Per-response generations never participate in identity equality. Deduplicate Vary names case-insensitively; `*` anywhere yields permanent `NoRecombine`; preserve absent versus present-empty request fields; combine multiple request field lines only for definitions explicitly marked combinable; apply only sealed field-specific semantic normalizers already implemented by VEF, otherwise retain a conservative ordered raw comparison. Callers supply opaque principal/partition/navigation inputs but cannot construct or replace the derived identity or evidence. Received trailer Vary deterministically yields `NoRecombine` and never changes selection, Content-Range, byte domain, identity, or head evidence.
- Before minting that identity, preflight every selected request field name, ordered field line/value or absence marker, and sealed-normalizer identifier into one explicit long-lived storage mode: immutable generation-bound `VariantFieldLease<'a>` values over original request storage, or engine-written caller-provided fixed-capacity `VariantIdentityStorage<'a>`. Copied storage can be created only from exclusive `&mut [u8]` or a sealed fixed-arena slot; the engine freezes it as an immutable generation-bound lease. No caller storage trait, unsafe/trust constructor, alias, mutation, recycle, or reissue path exists while either lease lives. DMA/device-backed request and identity buffers remain quiesced and fenced for the complete lease lifetime. Semantic invalidation rejects every dependent operation immediately but never ends a Rust lifetime or makes physically borrowed storage reclaimable; after all leases are dropped or acknowledged, the caller owns scrubbing copied sensitive bytes. Never truncate, omit, or use a digest/hash as equality authority; opaque replacement tokens are outside 1.0. `VariantIdentityCapacity` is local NoRecombine, never peer error, and release/recycle invalidates every dependent evidence/segment/context admission.
- Reuse field sensitivity metadata for identity storage and force Cookie, Authorization, Proxy-Authorization, and caller-marked secret fields sensitive even when nominated by Vary. Raw names/values from sensitive entries never enter Debug, diagnostics, traces, events, errors, or non-redacted equality failures; diagnostics expose only bounded type/count/length and opaque generation information. Principal/privacy/navigation equality never authorizes comparison across partitions, and no public API reveals retained sensitive bytes through the identity object.
- Execute every sealed field-specific semantic normalizer exactly once while constructing `VariantSelectionIdentity`. Before parsing any selected value, derive sealed `ActiveVariantNormalizationBudget` from the active resource profile; monotonically charge raw bytes, members, work, and canonical output with checked arithmetic. For a normalized field retain only its complete canonical equality bytes plus normalizer identity/provenance; for a field without a normalizer its exact raw bytes are the canonical representation. Never retain a second raw copy merely for identity equality, although an independently selected borrowed-request mode may keep the original request bytes alive. Temporary copied raw sensitive bytes are scrubbed before their storage is returned when feasible, without claiming guaranteed physical zeroization. Canonical storage is never a digest, and the normalizer's documented equality must match exactly the field definition's equivalence relation. Comparisons use stored canonical bytes and never parse or normalize again. Work/output/storage exhaustion returns local `VariantNormalizationWorkLimit` or `VariantNormalizationCapacity` and permanently downgrades that response to NoRecombine.
- When a GET receives a complete, semantically valid 200 head but content terminates prematurely, produce `ValidatedIncomplete200Prefix` only if optional retained storage yielded a stored-slice lease; otherwise report typed incomplete standalone termination with no combination input. The retained prefix binds original request/correlation, target/selection, coding, expected/received length, interval, metadata, and final available validator evidence. Eligible termination is premature HTTP/1 EOF before Content-Length, EOF before terminal chunk with otherwise valid syntax, or HTTP/2 RST_STREAM/connection failure/cancellation before END_STREAM after a validated head. Clean HTTP/2 END_STREAM length disagreement is malformed stream PROTOCOL_ERROR with no prefix; invalid fields/pseudo-fields, fatal HPACK/framing, ambiguous HTTP/1 framing, or malformed chunks likewise yield none. HTTP/1 becomes non-reusable; HTTP/2 preserves its connection only while synchronized.
- Classify only a successfully completed, framing- and semantics-valid correlated ordinary or pushed 200 as sealed `FullRepresentationFallback::{Keyed, Unkeyed}` through the same machinery; pushed evidence consumes only its immutable `PushedAssemblyProvenance`, never current/recycled associated-stream state. A truncated 200 follows only the incomplete-prefix/discard path. `Keyed` carries the exact `AssemblyReplacementKey`. When Vary `*`, identity capacity/work failure, normalization failure, released/stale identity storage, or other local policy prevents a key, `Unkeyed` consumes the correlation-bound handle into `ConservativeInvalidationScope::Reserved { handle: AssemblyInvalidationHandle, refinement: Option<ConservativeReplacementScope> }`. The optional refinement contains coding/byte-domain only; if it lacks capacity, all coding/domain children within the handle's mandatory effective-target/principal/privacy-partition/navigation namespace are selected. `ConservativeInvalidationScope::AssemblyArenaGeneration(ArenaRotationCause)` is permitted only with sealed `ArenaRotationCause::{DetectedSemanticCorruption, DetectedStorageCorruption, ExplicitCallerPolicy}`. The two corruption causes require an internal invariant breach or trusted-storage integrity failure; peer malformed input, semantic violations, conflicting partial bytes, and all capacity exhaustion—including invalidation-handle, Vary, identity, and normalization exhaustion—never construct an arena-rotation cause. Producing Unkeyed is a local capacity/policy outcome, never peer error, and v0.181.2 must invalidate conservatively before terminal publication so identity loss cannot leave old partial contexts usable. A proxy preserves a well-formed unknown range unit even though a VEF client returns UnsupportedRangeUnit/NoRecombine.
- Preserve exact response/body/trailer correlation, bounded byte accounting, cancellation/reset behavior, and no partial assembly publication before the terminal disposition.
- Update paragraph-addressable RFC 9110 206/combination/unknown-unit requirements, RFC 9111 incomplete-response storage constraints, and RFC 9112/RFC 9113 incomplete-message and transport dispositions plus threat model, APIs, release notes, traceability, resource measurements, and conformance corpora.

#### Verification

- Exhaust Content-Type classifications and prove multipart never reaches top-level Content-Range. Exhaust every delivery preference/permit, chunk split, mismatch, forged/stale permit, storage-before-publication order, acknowledgement/recycle attempt, backpressure, cancellation, and capacity boundary. Prove 206 retention preflight, local-not-peer capacity, RetainOnly cancellation, StreamAndRetain NoRetainedPrefix fallback, exact retained-prefix eligibility, zero-retention large ranges, terminal proof, safe leases, DMA fencing, and head/trailer validator finalization. For pushed 206 prove exact promised request/correlation/handle/provenance binding, trusted associated-request principal/partition/tenant/navigation inheritance, independent arena/generation lifetime after associated-stream completion/reset/buffer reuse and later policy changes, and rejection of unpublished/capacity-rejected/cross-associated or peer-claimed identity. Exhaust bounded Vary deduplication, `*`, exact request values, absent/empty and repeated-field semantics, sealed normalizers, trailer Vary, identity equality across ordinary and pushed responses, evidence freshness, and principal/privacy isolation.
- For identity storage add compile-fail alias/mutate/recycle/reissue and trust-trait/constructor attempts; exclusive slice/sealed-arena creation; DMA mutation throughout the lease; semantic invalidation without lifetime termination; no zeroization claim; caller scrub after release; sensitive canonical redaction; maximum values; exact capacity/one-byte shortage; and no truncation/digest/token substitution. For each sealed normalizer exhaust equivalent/non-equivalent raw spellings, canonical-output capacity, work exhaustion at every byte/member boundary, active-profile caps, temporary-raw scrubbing where feasible, absence of a redundant retained raw copy, and many candidate contexts while instrumenting exactly one normalization and zero comparison-time parsing. Exhaust Keyed and every Unkeyed reason with exact/short identity storage, Vary `*`, normalization exhaustion, released storage before terminal completion, missing coding/domain refinement, and authorized corruption/caller-policy arena-rotation causes; invalidation-handle exhaustion is rejected before local request output or promised-request publication at v0.181.0 and cannot reach this fallback. Prove malformed/semantic/conflicting peer input cannot mint a corruption cause. With multiple unrelated targets/principals prove malicious capacity, Vary, and normalization exhaustion cannot rotate the arena or evict outside the reserved namespace.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The streaming partial-response and retained-prefix validation contract and all previously implemented relevant behavior have reproducible evidence; v0.181.0 (Client correlation, cancellation, and retry tokens) still passes; no behavior assigned to v0.181.2 (Cross-request partial assembly and header synthesis) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.181.1 implementation stop reached. Run pentest for this exact commit.`

### v0.181.2 — Cross-request partial assembly and header synthesis

Status: planned

#### Goal

Deliver **Cross-request partial assembly and header synthesis** as the sole primary capability in this stop. It builds
on v0.181.1 (Streaming partial-response and retained-prefix validation) and must be independently trustworthy before v0.182.0 (Retry safety, idempotency, and body-replayability contract) begins.

#### Deliverables

- Acceptance contract: Add a caller-created but non-forgeable, generation-safe, fixed-capacity `PartialAssemblyContext` for one semantic `AssemblyReplacementKey`: effective target, the engine-derived v0.181.1 `VariantSelectionIdentity`, content coding, and representation-byte domain. Per-request/response/correlation generations exist only in each segment's `VariantSelectionEvidence` and never enter replacement-key equality. Admission first verifies every evidence token's provenance, freshness, and exact embedded identity, then compares only semantic identity across requests; callers cannot normalize, construct, or replace either value. Arena identity and `StorageLeaseGeneration` likewise remain physical validity evidence only inside stored-slice capabilities. `Vary: *` is never eligible for cross-request assembly. The old strong validator and complete length remain combination constraints, not replacement identity. Each `StoredPartialSegment` remains bound to its original request/correlation/storage generations; exact context matching refines stored inputs from different Range requests into `CombinablePartialSegment` or `CombinableIncomplete200Prefix`, while retries or caller input cannot rebind them.
- Add a non-forgeable fixed-capacity `PartialCombinationPlan` that consumes only admitted combinable values with immutable input leases. A caller may supply freely constructible `RequestedOverlapBudget`, but before sorting, output acquisition, or comparison the engine rejects any request above the active resource profile as local `WorkLimit` and mints sealed plan-bound `ActiveOverlapBudget` capped by that profile. Sorting and the interval sweep monotonically charge it with checked decrement plus saturating diagnostic counters; it cannot reset, clone, enlarge, or be replaced while the plan executes, and exhaustion is typed local `WorkLimit`, never a peer violation. Overlapping equal octets deduplicate; the first unequal octet returns `ConflictingPartialContent`, publishes no output, and never chooses receipt order as byte authority. Obtain output only by safe non-overlapping slice splitting from the exclusively owned arena or a separate sealed arena; no public unsafe/trust constructor or caller storage trait can assert non-aliasing. Preflight every lease, interval, copy schedule, and capacity; keep inputs immutable until commit/cancel; publish success atomically and invalidate partial output on failure.
- On `ConflictingPartialContent`, atomically quarantine the entire assembly context, its strong-validator association, segments, leases, and plans before returning the error. A quarantined context accepts no further partial input. It clears only when a complete validated 200 with the same `AssemblyReplacementKey` atomically replaces all old bytes, or when evidence proves a genuinely new representation with a different strong validator and representation generation, every old segment/context object is destroyed, and a new empty context is created. A 304, successful revalidation retaining the conflicting validator, unchanged-validator generation refresh, caller assertion, retry, receipt order, storage rotation, or another partial response cannot clear it. A new navigation or variant-selection identity creates a separate context and never unquarantines the old one. Quarantine and work-limit paths expose no synthesized headers or bytes.
- Add a caller-owned, generation-bound `ReceiptOrderSource` shared by correlations in one assembly scope across requests/connections. The correlation engine—not an arbitrary caller action—mints one checked monotonic local `ResponseHeadReceiptOrdinal` when the complete validated header section is atomically published and retains it through complete-body or incomplete-prefix classification. Neither value derives from Date or other peer input; a context accepts only its source generation, and exhaustion requires source/context rotation. Apply RFC header-source rules using this head ordinal, so body delay cannot make older headers newest: a latest incomplete 200 supplies combined headers; otherwise the locally most recent 200 supplies them when any stored response is 200; when all are 206, use the greatest head ordinal and replace corresponding fields from the newly admitted 206 except Content-Range. A full union yields complete 200 with corrected Content-Length; a prefix-only union yields incomplete 200; one continuous non-prefix union yields single 206 with corrected Content-Range and Content-Length; disjoint unions remain separate and VEF never synthesizes multipart/byteranges.
- Consume v0.181.1 ordinary and pushed full-200 terminal evidence atomically before publishing it. Pushed evidence derives its replacement namespace exclusively from immutable arena/generation-bound `PushedAssemblyProvenance`; associated-stream teardown, storage reuse, and later caller-policy changes are irrelevant. `Keyed` semantically invalidates every context, segment, identity/body lease, and plan with the exact semantic `AssemblyReplacementKey`, regardless of validator or arena generation. `Unkeyed` uses its reserved `AssemblyInvalidationHandle` to invalidate or quarantine every Vary/validator sibling within the effective-target, principal/privacy-partition, and navigation namespace; it narrows by coding/domain only when that refinement is retained, otherwise it selects every coding/domain child in the namespace. Whole-arena generation rotation requires a sealed detected-semantic-corruption, detected-storage-corruption, or explicit-caller-policy cause and is never selected by any capacity exhaustion, Vary `*`, or identity/normalization exhaustion. Handle/provenance capacity failure occurred before local request output or promised-request publication and therefore supplies no response correlation or terminal evidence to consume. Scope loss can reduce reuse but cannot preserve a potentially replaced context; these remain local outcomes. A truncated 200 never triggers replacement. Invalidation moves affected storage first to `SemanticallyInvalid`, so every stale capability rejects operations immediately, but neither exact invalidation nor namespace invalidation nor arena rotation ends a Rust lifetime, recycles a sealed slot with a live `&[u8]`, or permits a new mutable lease over storage still borrowed by body, identity, or output capabilities. Storage becomes `PhysicallyReclaimable` only after every such lease is dropped or explicitly acknowledged; allocation before then returns typed local `LeaseHeld`/capacity. Trailer-finalized combinability retains the original head ordinal, and no combined output becomes observable before every immutable byte, validator, output lease, and synthesized metadata check passes.
- Update paragraph-addressable RFC 9110 partial-combination/header-selection requirements and RFC 9111 metadata/content-domain integrity rules, threat model, APIs, release notes, traceability, resource measurements, and conformance corpora.

#### Verification

- Exhaust safe split/separate-arena output, compile-fail alias/mutation/recycle/decode, stale body/identity leases, copy schedules, output exhaustion, cancellation, and DMA fencing. Combine generations only after fresh storage/evidence admission and semantic equality; reject every stale/rebound/mismatched/standalone/multipart/unknown-unit/`Vary: *` input. Test requested budgets zero through maximum, pre-work profile rejection, forged/stale/cross-plan active budgets, every charge boundary, saturating telemetry, and reset/enlarge/replace attempts. Model equal/conflicting overlaps, quarantine clearance, head/trailer validators, head ordinals under delay/retry/Date manipulation, all union forms, corrected headers/lengths, backpressure, and no panic/allocation.
- For full 200 test Keyed exact invalidation and every Unkeyed reason across ordinary and pushed responses: identity capacity exact/one-byte-short, Vary `*`, normalization work/output exhaustion, identity lease release immediately before completion, missing coding/domain refinement, and every authorized corruption/caller-policy arena-rotation cause. Prove invalidation-handle/provenance capacity cannot produce a response/fallback or rotate an arena because v0.181.0 emitted no local request bytes or promised-request publication/correlation. Exercise pushed full 200 before/after reset scheduling and terminal backpressure; close/reset the associated stream, recycle/overwrite its buffers, mutate principal/navigation/policy inputs, then prove each promised response uses only its independent immutable provenance and releases it once. Populate multiple sibling Vary variants plus different targets/principals/partitions/navigation/codings/domains; prove the handle invalidates all and only its mandatory namespace, missing refinement selects every coding/domain child there, peer-controlled exhaustion cannot evict another target or principal, authorized arena rotation invalidates all generation members, invalidation precedes terminal publication, validators cannot prevent it, failures are local rather than peer errors, and every old capability is semantically unusable. Hold old body, identity, and output leases across keyed invalidation, namespace invalidation, and arena rotation; prove no slot reuse or new mutable alias until every lease drops/acknowledges, observe typed `LeaseHeld` while any remain, then prove reuse only under a fresh generation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy, audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The cross-request partial-assembly and header-synthesis contract and all previously implemented relevant behavior have reproducible evidence; v0.181.1 (Streaming partial-response and retained-prefix validation) still passes; no behavior assigned to v0.182.0 (Retry safety, idempotency, and body-replayability contract) is claimed; the active resource profile passes; and no critical/high finding is open.

`0.181.2 implementation stop reached. Run pentest for this exact commit.`

### v0.182.0 — Retry safety, idempotency, and body-replayability contract

Status: planned

#### Goal

Deliver **Retry safety, idempotency, and body-replayability contract** as the sole primary capability in this stop. It builds
on v0.181.2 (Cross-request partial assembly and header synthesis) and must be independently trustworthy before v0.182.1 (Role-aware outbound response semantic validator) begins.

#### Deliverables

- Acceptance contract: Classify method safety and idempotency independently from explicit caller retry authorization; require a generation-checked replayable-body handle and distinguish zero transmission, partial transmission, and possibly-unprocessed outcomes; never infer permission from GOAWAY, 421, reset, or connection loss and never automatically retry an unsafe request without explicit authorization and reproducible body bytes.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Retry safety, idempotency, and body-replayability contract and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Retry safety, idempotency, and body-replayability contract contract and all previously implemented relevant behavior have
reproducible evidence; v0.181.2 (Cross-request partial assembly and header synthesis) still passes; no behavior assigned to v0.182.1 (Role-aware outbound response semantic validator) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.182.0 implementation stop reached. Run pentest for this exact commit.`

### v0.182.1 — Role-aware outbound response semantic validator

Status: planned

#### Goal

Deliver **Role-aware outbound response semantic validator** as the sole primary capability in this stop. It builds
on v0.182.0 (Retry safety, idempotency, and body-replayability contract) and must be independently trustworthy before v0.183.0 (Origin-server role API) begins.

#### Deliverables

- Acceptance contract: Add a separate dependency-free, no_std `vef-semantics` crate depending only on `vef-core`, `vef-auth`, `vef-media-type`, and `vef-conditions`; it owns role-aware response validation and returns an opaque sealed protocol/role/message-generation-bound `ValidatedResponse<'a>` with private construction and no Copy/Clone. `ValidatedResponse` owns or immutably borrows the exact ordered response head, framing plan, sensitivity/indexing metadata, body plan, and trailer permissions that were validated; its internal `ResponseEmissionPermit` cannot be extracted or paired with caller-supplied data. `vef-http1` and `vef-http2` consume the complete object exactly once before response-head serialization; no API accepts `(raw_head, permit)`, raw response heads have no public serialization path, and any status, field, ordering, framing, metadata, body-plan, or trailer-permission change requires a new validation while DATA/body/trailer commands remain bound to that frozen response generation.
- Validate the complete role/method/status/field/content semantic matrix before issuing `ValidatedResponse`; the caller chooses application values but supplies typed v0.157.2 challenges, allowed-method sets, upgrade protocols, sealed v0.180.2 precondition outcomes, sealed v0.180.3 range plans, and their exact `CurrentRepresentationEvidence` plus retrieval-only `WouldBe200Snapshot` where applicable; mismatched evidence is InvalidState. Require every generated 401 in HTTP/1 or HTTP/2 to carry at least one valid WWW-Authenticate challenge, with normal lowercase HTTP/2 field serialization, require 405 to carry Allow, and require HTTP/1 426 to carry valid Upgrade; reject every locally generated HTTP/2 426 as InvalidState because Upgrade is forbidden and no compliant field set exists.
- For 1.0 permit generated 206 only from one matching `SingleRangePlan` with one Content-Range consistent with emitted content; if Date, Cache-Control, ETag, Expires, Content-Location, or Vary exists in its `WouldBe200Snapshot`, require it in 206; with If-Range suppress other representation fields by fixed SHOULD-NOT policy, otherwise require every representation field the 200 would contain. Reject generated multipart/byteranges but preserve received multipart bodies opaquely. Permit 304 only from the matching conditional GET/HEAD `PreconditionOutcome` and retrieval snapshot, require every snapshot 200 field among Content-Location, Date, ETag, Vary, Cache-Control, and Expires, prohibit content/trailers, and reject unrelated representation metadata unless explicitly useful for cache updates. Bind 416 to the matching unsatisfied range context and require an unsatisfied bytes Content-Range when complete length is known; all generated Date/Last-Modified values obey v0.157.4. Any pre-emission evidence, Date, metadata, content-selection, or generation change invalidates the outcome, plan, and response. A successful unsafe execution instead consumes its admission permit, then obtains new post-action evidence and a status-appropriate response plan; it is never retroactively unauthorized because the action changed the representation.
- Reserve engine-only semantic-validation slots and frozen-head storage for mandatory v0.25.0/v0.38.0 responses, optionally use minimal prevalidated templates whose dynamic fields are still checked, and prohibit application validation from consuming that reserve; if reserve validation or output cannot proceed, commit exactly one deterministic close/shutdown action with no partial response output.
- Invalid locally constructed responses return InvalidState with a typed semantic-construction cause, issue no permit, and serialize zero bytes; invalid received responses—including HTTP/2 426 without Upgrade—remain framing-synchronized and produce a typed SemanticViolation plus explicit recipient-policy action, never a framing error or automatic connection desynchronization; forwarded responses preserve end-to-end fields—including unmodified WWW-Authenticate and Authentication-Info—and apply only already-authorized intermediary transformations/cache rules; HTTP/1 426 cannot be translated to HTTP/2 by stripping Upgrade.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including authentication, status, conditional, and range semantics, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Exhaust the generated/received/forwarded × role/method/status/protocol matrix; test private/sealed non-Copy/non-Clone construction, wrong protocol/role/generation, duplicate consumption, same-generation head substitution, mutable-buffer aliasing, field replacement/reordering, framing/indexing/body/trailer-plan mutation requiring revalidation, cancellation during partial output, and absence of any `(raw_head, permit)` or raw-head serialization path in both engines; test missing/empty/malformed/multiple 401 challenges over HTTP/1 and HTTP/2, HTTP/2 lowercase output, HTTP/1 valid/invalid 426, local HTTP/2 426 InvalidState, received HTTP/2 Upgrade stream error versus 426-without-Upgrade semantic violation, HTTP/1→HTTP/2 nontranslation, and 405. Exhaust same/mismatched/mutated current evidence and retrieval-snapshot identity; every conditional 206 hypothetical-200 field with and without If-Range; exact 304 required/extra metadata; unsafe 201/202/204 without hypothetical-200 input and fresh post-action evidence; Date/Last-Modified policy; sealed single-range body agreement; generated multipart rejection plus opaque received preservation; sealed 304/416 contexts; every other response semantic; zero local bytes; received synchronization/policy; and field preservation.
- Exhaust ordinary response permits/storage, then trigger malformed requests, 400/414/431, pipeline errors, cancellation, and output backpressure; prove the mandatory semantic reserve remains available, application work cannot consume it, minimal templates still validate, and total reserve failure produces one close/shutdown action with zero partial response bytes. Create a stateful response-semantic model/fuzz harness that varies frozen data, typed evidence, status, method, field multiplicity, content commands, translation direction, capacity, and cancellation while asserting no invalid local serialization, substitution, aliasing, or framing misclassification.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The role-aware outbound response semantic validator contract and all previously implemented relevant behavior have
reproducible evidence; v0.182.0 (Retry safety, idempotency, and body-replayability contract) still passes; no behavior assigned to v0.183.0 (Origin-server role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.182.1 implementation stop reached. Run pentest for this exact commit.`

### v0.183.0 — Origin-server role API

Status: planned

#### Goal

Deliver **Origin-server role API** as the sole primary capability in this stop. It builds
on v0.182.1 (Role-aware outbound response semantic validator) and must be independently trustworthy before v0.184.0 (Forward-proxy role API) begins.

#### Deliverables

- Acceptance contract: After head/framing validation publish only a read-only v0.180.2 `PendingConditionalRequest` for representation selection, accept matching generation-bound `CurrentRepresentationEvidence` plus `WouldBe200Snapshot` only for GET/HEAD retrieval, and run v0.180.2/v0.180.3 evaluation before application content delivery or method side effects. Only matching non-forgeable `RequestContentPermit` and `MethodExecutionPermit` unlock body chunks and method dispatch; do not emit 100 Continue, consume/publish already-buffered body bytes, or allow reentrant engine commands while pending. A terminal 304/412 issues neither permit, emits only through the v0.182.1 frozen `ValidatedResponse` path, and follows a deterministic bounded reject/drain-or-close policy without application body delivery. Consuming the execution permit authorizes one action even when it creates a new representation generation; response construction then requires fresh post-action evidence. Pending-buffer exhaustion backpressures or closes without peer-sized allocation.
- Correlate exactly one response lifecycle, provide no facade/raw-head or `(raw_head, permit)` bypass, preserve the engine-only mandatory semantic/head reserve, reject stale/cross-request snapshots or swapped/reused permits, reserve mandatory error output, and complete or cancel all pending body/evidence/storage ownership before pipeline or connection reuse.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test unconditional and every conditional outcome; stale/cross-request/mutated evidence; forged/swapped/reused content/execution permits; application reentrancy; Expect with satisfied/304/412/error outcomes and no early 100; body bytes already buffered before the head event; partial input, pending-buffer exhaustion and backpressure; terminal reject/drain/close; cancellation at every gate; pipelined successor isolation/reuse; zero application body/method side effects before authorization; and every earlier positive/negative/boundary/no-panic case.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Origin-server role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.182.1 (Role-aware outbound response semantic validator) still passes; no behavior assigned to v0.184.0 (Forward-proxy role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.183.0 implementation stop reached. Run pentest for this exact commit.`

### v0.184.0 — Forward-proxy role API

Status: planned

#### Goal

Deliver **Forward-proxy role API** as the sole primary capability in this stop. It builds
on v0.183.0 (Origin-server role API) and must be independently trustworthy before v0.185.0 (Reverse-proxy and gateway role API) begins.

#### Deliverables

- Acceptance contract: Validate absolute-form/effective URI and Host, Max-Forwards, TE, exact append-only Via, hop stripping, cache preservation, CONNECT, translation, upstream capacity/error disposition, and replayability before forwarding; expose the one-shot staged ConnectAttemptToken/AuthorizedConnectOutcome API without DNS/socket access and reject duplicate/stale/alternate endpoint or peer evidence before head, 2xx, or tunnel bytes; consume one exchange-bound HopScopedProxyCredential locally, remove it before origin forwarding, distinguish Authorization, allow only named-next-hop cooperative relay, scope proxy authentication response fields to the downstream client, generate 407 only with a v0.157.2-valid challenge, apply v0.65.0 fresh-connection closure to HTTP/1 CONNECT 407, and logically invalidate/release pending tunnel bytes and credential references across retry while requiring caller-owned buffer scrubbing.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test forward-proxy endpoint-outcome bindings, no resolver/socket authority, Via append/privacy/loop behavior, local proxy-credential consumption, origin non-forwarding, cooperative next-hop allow/deny, Authorization separation, response-field hop scope, challenged 407, HTTP/1 CONNECT close/fresh retry with no surviving owned bytes or live credential references plus explicit caller scrub, and all prior positive/negative/boundary/cancellation/capacity/no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Forward-proxy role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.183.0 (Origin-server role API) still passes; no behavior assigned to v0.185.0 (Reverse-proxy and gateway role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.184.0 implementation stop reached. Run pentest for this exact commit.`

### v0.185.0 — Reverse-proxy and gateway role API

Status: planned

#### Goal

Deliver **Reverse-proxy and gateway role API** as the sole primary capability in this stop. It builds
on v0.184.0 (Forward-proxy role API) and must be independently trustworthy before v0.186.0 (Tunnel lifecycle and half-close semantics) begins.

#### Deliverables

- Acceptance contract: Separate downstream authority from configured upstream authority, validate and reserialize through the translation matrix, append the v0.157.0 inbound received-protocol/pseudonym Via entry for every HTTP-to-HTTP gateway-forwarded request with bounded loop/privacy policy, preserve response ordering/cache metadata, map upstream failure to typed gateway actions, and never leak partial upstream/downstream state across requests.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test reverse-proxy/gateway authority separation plus mandatory inbound-request Via append, inbound rather than outbound protocol/version, pseudonym privacy, loop disposition, capacity preflight, and all earlier positive/negative/boundary/truncation/invalid-state/cancellation/capacity/no-panic behavior.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reverse-proxy and gateway role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.184.0 (Forward-proxy role API) still passes; no behavior assigned to v0.186.0 (Tunnel lifecycle and half-close semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.185.0 implementation stop reached. Run pentest for this exact commit.`

### v0.186.0 — Tunnel lifecycle and half-close semantics

Status: planned

#### Goal

Deliver **Tunnel lifecycle and half-close semantics** as the sole primary capability in this stop. It builds
on v0.185.0 (Reverse-proxy and gateway role API) and must be independently trustworthy before v0.187.0 (Upgrade transformation boundary) begins.

#### Deliverables

- Acceptance contract: Use protocol-specific tunnel closure states with bounded buffers and one owner per direction: HTTP/1 CONNECT TCP EOF enters Http1DrainingAfterClose, accepts no new closed-side bytes, attempts only already-owned delivery under injected drain deadline/byte/work limits, then closes both connections and diagnoses discarded remainder. HTTP/2 CONNECT and applicable RFC 8441 END_STREAM enter genuine local/remote half-closed states under the v0.137.0 boundary: FIN command acceptance seals the local tunnel-send direction, but wire half-close occurs only after the final DATA/empty-DATA carrying frame is fully acknowledged. Forward preceding DATA before directional FIN, continue reverse DATA, map upstream TCP FIN to final DATA plus END_STREAM, and close normally only after both directions finish. RST_STREAM, TCP reset/error, fatal TLS alert, cancellation, or HTTP/2 connection failure abort both directions and map required TCP reset/CONNECT_ERROR actions; an injected idle/half-close timeout may abort a stuck tunnel. Partial FIN output/failure never fabricates wire half-close, END_STREAM alone never closes the opposite direction, and no tunnel returns to HTTP reuse.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HTTP/1 EOF flush-then-close separately from HTTP/2/RFC8441 directional END_STREAM; final DATA+FIN command sealing versus full-frame wire commit, zero/partial/full acknowledgement, reverse traffic after one committed FIN, both-FIN normal close, every abort/reset/alert/cancellation/connection error mapping, idle/half-close timeout, all buffered/partial-write boundaries, discard diagnostics, no reuse, stream isolation, and bounded termination.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Tunnel lifecycle and half-close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.185.0 (Reverse-proxy and gateway role API) still passes; no behavior assigned to v0.187.0 (Upgrade transformation boundary) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.186.0 implementation stop reached. Run pentest for this exact commit.`

### v0.187.0 — Upgrade transformation boundary

Status: planned

#### Goal

Deliver **Upgrade transformation boundary** as the sole primary capability in this stop. It builds
on v0.186.0 (Tunnel lifecycle and half-close semantics) and must be independently trustworthy before v0.188.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) begins.

#### Deliverables

- Acceptance contract: Transform only a fully validated Upgrade request/101 response pair, preserve selected protocol and negotiation metadata, and reuse the v0.163.0 ordered `BridgeTransaction`, its four phase-specific `ValidatedDownstreamRequest`/`CommittedUpstreamRequest`/`ValidatedUpstreamSuccess`/`CommittedDownstreamSuccess` capabilities, sealed five-way `TransitionInputProvenance`, optional-over-read `PendingHttp1Transition`, and protocol-specific `BridgeInputLease`. Reserve transaction/lease/output/failure resources plus HTTP/1 optional over-read/terminal storage before upstream request exposure; then require `Reserved -> DownstreamRequestValidated -> UpstreamRequestCommitted -> UpstreamSuccessValidated -> DownstreamSuccessFrozen -> ActiveAfterDownstreamSuccessCommitted`. Every capability retains its exact bridge/connection/leg/role/message/head-generation binding and is accepted only at its matching edge. Never use outbound HpackCommitted for a received success. HTTP/2 reuses existing PendingConnect/ReceiveCredit ownership through `AwaitingBridgeActivation { bridge_generation }` without a second store or early WINDOW_UPDATE, retaining ordered DATA, padding/semantic charge, pending FIN, and first terminal cause. Emit no downstream 101 before complete upstream success validation and no cross-leg/post-transition bytes before Active. Treat `CommittedDownstreamSuccess` as wire evidence only and require the matching engine-minted `BridgeActivationPermit` with a clear premature-input latch before Active. Missing HTTP/1 ordinary-CONNECT close proof retains the strict discard/close/no-reparse/no-promotion disposition. Premature RFC 8441 DATA reuses the v0.163.0 AcceptedPrivate-versus-Frozen/FramingCommitted suffix/reset arbitration; a failure after any exposure completes immutable framing when the connection remains usable, then resets/closes without a replacement response, activation, or double discard. Reject unsupported cross-version upgrades with an HTTP-framed close action.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Upgrade transformation boundary and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross resource reservation, each of the four phase-specific capabilities and every binding mismatch, each inbound HTTP/2 semantic stage, both input-lease kinds, same-buffer success-plus-DATA/END_STREAM/reset, padded/pending DATA and credit thresholds, every legal phase edge, every illegal phase skip/reorder, stale generations, reset/GOAWAY/cancellation, and partial transport failure; require upstream validation before downstream exposure, no evidence/byte/FIN/credit-owner confusion, Active before cross-leg publication, and phase-correct one-shot cleanup.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Upgrade transformation boundary contract and all previously implemented relevant behavior have
reproducible evidence; v0.186.0 (Tunnel lifecycle and half-close semantics) still passes; no behavior assigned to v0.188.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.187.0 implementation stop reached. Run pentest for this exact commit.`

### v0.188.0 — Exact CONNECT, Upgrade, and tunnel byte-handoff ownership

Status: planned

#### Goal

Deliver **Exact CONNECT, Upgrade, and tunnel byte-handoff ownership** as the sole primary capability in this stop. It builds
on v0.187.0 (Upgrade transformation boundary) and must be independently trustworthy before v0.189.0 (GOAWAY, 421, and retry coordination) begins.

#### Deliverables

- Acceptance contract: Stop at the precise committed transition boundary using the generation-bound ordered `BridgeTransaction` for CONNECT and Upgrade. Pre-reserve transaction/lease metadata, required HTTP/1 optional-over-read/`PendingHttp1Transition` storage, downstream suffix/reset ownership, activation permit state, and every output/failure owner before upstream exposure; consume `ValidatedDownstreamRequest`, `CommittedUpstreamRequest`, and `ValidatedUpstreamSuccess` only at their ordered edges. Each opaque capability binds bridge, connection/leg, role, request/response kind, exchange/stream generation, and exact head identity, so equal numeric stream identifiers provide no substitution authority. Inbound HTTP/2 success requires compression synchronization, `TerminalValidation::Valid`, final 2xx, exact correlation/negotiation/state; only committed outbound HTTP/2 capabilities use field-block HpackCommitted. Consume sealed five-way `TransitionInputProvenance`: success-following input and permitted optimistic ordinary CONNECT may mint `BridgeInputLease`; unpermitted ordinary CONNECT with `MissingCommittedCloseProof`, optimistic WebSocket, and HTTP/1 CONNECT-UDP never may. HTTP/1 permission requires `ReceivedValidatedCloseOption` in the exact received request or `LocallyCommittedCloseHead` for the exact serialized close-bearing head after `HeadCommitted`; configured intent, queued output, and stale/cross-head evidence fail closed through discard/close/no-reparse/no-later-promotion. HTTP/2 ordinary CONNECT reuses its exact PendingConnect generation.
- Audit premature RFC 8441 DATA against every downstream success output state. Validate padding, charge both windows, discard only that stream, and reclaim only through v0.136.0. `AcceptedPrivate` with no exposure is superseded and followed only by `RST_STREAM(PROTOCOL_ERROR)`. `Frozen` or `FramingCommitted`, including exposed with zero acknowledgement, enters `FailedAfterDownstreamSuccessExposure`, completes the exact immutable HEADERS/CONTINUATION suffix through END_HEADERS with normal HPACK/framing commitment, and only then emits the reset; it never mints `BridgeActivationPermit` or transfers a lease. A final acknowledgement processed before DATA may produce `CommittedDownstreamSuccess`; activation atomically consumes that exact evidence, the reserved permit slot, clear failure-latch snapshot, and matching frozen bridge generation. Connection failure during suffix completion uses connection-owned cleanup without fabricated response/reset completion or Active. Preserve unrelated same-buffer frames and HPACK unless independently connection-fatal. `CommittedDownstreamSuccess` is wire evidence only; only the one engine-minted permit authorizes Active, and duplicate/stale final acknowledgements, repeated hooks, cancellation races, or generation reuse cannot repeat success publication or lease transfer.
- Acknowledgement-first zero/short/full/invalid behavior otherwise remains exact. `PendingHttp1Transition` has optional over-read for terminal-only/bytes-only/combined transitions and binds immutable first plain-EOF/close_notify/TLS-truncation/fatal-alert/reset/transport-failure/cancellation cause to bridge, leg, exchange, and transport generations. `PendingConnectLease` linearly references existing padded-DATA/stream-generation/ReceiveCredit ownership through `AwaitingBridgeActivation { bridge_generation }`, retaining ordered ranges, pending FIN, and first terminal cause. Only Active transfers HTTP/1 bytes or HTTP/2 leases/allowed FIN exactly once. WebSocket terminal input before success exposure fails the handshake; ordinary CONNECT follows explicit drain/close and preserve-for-Active-or-reject policy. Failure before downstream exposure uses the protocol's exact HTTP/reset cleanup; failure after partial exposure closes downstream and aborts/resets upstream without another response or double cleanup. TLS close_notify never fabricates TCP half-close authority.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Exact CONNECT, Upgrade, and tunnel byte-handoff ownership and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross all five input provenance classes; both HTTP/1 close-proof constructors, missing proof, configured intent, every local head acknowledgement offset, stale/cross-head evidence, early bytes, and 2xx/non-2xx; HTTP/2 ordinary CONNECT DATA versus RFC 8441 DATA before 2xx; zero/short/full/invalid success acknowledgement; legal upstream 101-plus-data and success-HEADERS-plus-DATA; terminal-only valid success, next-call terminal, and over-read plus every HTTP/1 terminal cause at every phase; HTTP/2 padding/window/reclamation boundaries and unrelated same-buffer SETTINGS/PING/HEADERS/DATA; each legal/illegal bridge phase; stale generations; RST_STREAM/GOAWAY/connection failure; and terminal events immediately before/after first downstream exposure. For premature DATA cross private output, first exposure with zero acknowledgement, every HEADERS/CONTINUATION offset, final END_HEADERS acknowledgement ordering, and connection failure at every suffix prefix. At final commitment cross duplicate/stale acknowledgements, repeated hook calls, cancellation at every atomic-mint edge, and generation teardown/reuse. Prove permitted optimistic input transfers once on success and discards/closes once on failure; unpermitted/forbidden input has no lease/reparse/Active/forwarding; private output is superseded before reset; exposed output completes immutably before reset without activation; exact evidence/slot/latch/generation inputs are consumed together; only one clear-latch `BridgeActivationPermit` authorizes Active; at most one success event and lease transfer occur; terminal cause is immutable; close_notify grants no TCP half-close; no inbound HpackCommitted fabrication or duplicate owner/copy/credit/discard occurs; and failure selects exactly one terminal cleanup.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Exact CONNECT, Upgrade, and tunnel byte-handoff ownership contract and all previously implemented relevant behavior have
reproducible evidence; v0.187.0 (Upgrade transformation boundary) still passes; no behavior assigned to v0.189.0 (GOAWAY, 421, and retry coordination) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.188.0 implementation stop reached. Run pentest for this exact commit.`

### v0.189.0 — GOAWAY, 421, and retry coordination

Status: planned

#### Goal

Deliver **GOAWAY, 421, and retry coordination** as the sole primary capability in this stop. It builds
on v0.188.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) and must be independently trustworthy before v0.190.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) begins.

#### Deliverables

- Acceptance contract: Track GOAWAY last-stream protocol processing status separately from application replay permission; consume received or fully wire-committed sent cutoff evidence but never requested, partial, or unknown-after-failure output as proof of peer processing; correlate each affected request exactly once; treat 421 as an origin-authorization failure and permit its retry only when the retry contract authorizes it and a new non-coalesced connection is authenticated for that origin. Above-cutoff “possibly unprocessed” is classification only and never fabricates replay authority.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone. Cross received/committed/partial/unknown cutoff evidence with safe, unsafe, idempotent, non-idempotent, body-replayable, and non-replayable requests; prove classification never creates a retry permit and each separately authorized retry correlates exactly once.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY, 421, and retry coordination contract and all previously implemented relevant behavior have
reproducible evidence; v0.188.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) still passes; no behavior assigned to v0.190.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.189.0 implementation stop reached. Run pentest for this exact commit.`

### v0.190.0 — Authenticated origin authorization and HTTP/2 coalescing metadata

Status: planned

#### Goal

Deliver **Authenticated origin authorization and HTTP/2 coalescing metadata** as the sole primary capability in this stop. It builds
on v0.189.0 (GOAWAY, 421, and retry coordination) and must be independently trustworthy before v0.191.0 (Fixed-capacity caller-storage public API) begins.

#### Deliverables

- Acceptance contract: Bind coalescing authorization to authenticated SNI, certificate identity, scheme, port, remote endpoint, tunnel authority, end origin, validation generation, connection-specific policy inputs, and a caller-supplied CompressionPrincipal per request; invalidate authorization when any generation, authenticated input, or principal binding changes, prohibit shared encoder lookup across principals unless an entry is explicitly public, default missing/unknown provenance to non-indexing, and expose a typed non-coalesced route requirement after 421.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Authenticated origin authorization and HTTP/2 coalescing metadata contract and all previously implemented relevant behavior have
reproducible evidence; v0.189.0 (GOAWAY, 421, and retry coordination) still passes; no behavior assigned to v0.191.0 (Fixed-capacity caller-storage public API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.190.0 implementation stop reached. Run pentest for this exact commit.`

### v0.191.0 — Fixed-capacity caller-storage public API

Status: planned

#### Goal

Deliver **Fixed-capacity caller-storage public API** as the sole primary capability in this stop. It builds
on v0.190.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) and must be independently trustworthy before v0.192.0 (Optional alloc-backed convenience API) begins.

#### Deliverables

- HTTP/1.0 API extension: expose neither reserved common/cause interrupt binding, completion generation, resolution/interrupt constructors, revoked reuse identity, work kind/spec/units, private `AdmissionWorkPermit`, nor attempt progress cursors. `Http10TerminalDecision` exposes no stored or caller-settable planned state. Every cursor remains borrow-bound to one call and is destroyed before a reason-only result; no public type retains the command. Callers cannot carry progress into a corrected/mutated command, allocate/rebind a completion generation, pre-traverse iterators, select work quantity/cost, fabricate/reuse a work permit, use `AdmissionWorkReceipt` as authority, rewind progress, or request an uncharged rescan.
- Acceptance contract: Stabilize borrowed/fixed-capacity APIs first, including acknowledgements, lifetimes, explicit capacity errors, and proof that protocol correctness needs no allocator. Expose `OutboundFrameArena` only from exclusive caller storage, with generation-checked `OutboundFrameSlot`/`FrozenOutboundFrameSlot` ownership, independent queue-byte/entry sizing, nonzero `ResourceProfile::max_outbound_frame_payload`, and typed `OutboundFrameStorageCapacity`; no API sizes storage directly from peer MAX_FRAME_SIZE or permits caller access/reuse before supersession, full acknowledgement, or connection cleanup. `PartialDeliveryPreference`, `RequestedOverlapBudget`, `AssemblyInvalidationCapacity`, `PushedAssemblyProvenanceCapacity`, `StreamTrackingUnavailable`, `PushRejectionTrackingUnavailable`, `LeaseHeld`, and ordinary error values are freely constructible and confer no authority; caller-provided `VariantIdentityStorage` is constructible only from exclusive slices/sealed slots. Expose civil-time evidence, PendingConditionalRequest, CurrentRepresentationEvidence, WouldBe200Snapshot, request content/execution permits, ParsedMediaType, ValidatedGeneratedMediaType, ValidatedConditionalRequest, PartialContentTypeClassification, PartialResponseDisposition, ValidatedPartialResponseHead, SelectedPartialDelivery, PartialBodyChunk, StandalonePartialComplete, VariantFieldLease, VariantSelectionIdentity, VariantSelectionEvidence, ActiveVariantNormalizationBudget, FullRepresentationFallback, AssemblyInvalidationHandle, PushedAssemblyProvenance, ConservativeReplacementScope, ConservativeInvalidationScope, ArenaRotationCause, ActiveOverlapBudget, StorageLeaseGeneration, StoredRepresentationSlice, StoredPartialSegment, ValidatedIncomplete200Prefix, CombinablePartialSegment, CombinableIncomplete200Prefix, AssemblyReplacementKey, PartialAssemblyContext, ReceiptOrderSource, ResponseHeadReceiptOrdinal, CombinationOutputLease, and PartialCombinationPlan only with the sealed generation/lifetime constraints appropriate to authority-bearing evidence. The invalidation handle and pushed provenance remain non-Copy/non-Clone, exact promised-correlation-bound, independently leased from associated-stream storage, held through reserved push and terminal backpressure, and exactly-once released; no public operation duplicates, rebinds, substitutes peer identity, crosses associated requests, borrows recyclable associated-stream storage, or releases either early. Semantic invalidation is observable only as rejection and cannot shorten a lease or authorize physical reclamation. Expose generated responses only through fixed-capacity `vef-semantics` validation yielding a frozen `ValidatedResponse` consumed whole by the selected engine, preserve the mandatory reserve, and keep raw request/response serializers and separable capability/data pairings non-public.
- Stabilize `advance_io(output_ack, input)` so output acknowledgement is applied
  before any input borrow is consumed. With a live `OutputToken`, only a
  combined call consuming that exact token accepts nonempty input; input-only
  APIs return typed `DriverCommitOrderViolation` with the entire input borrow
  and all engine state unchanged. Invalid acknowledgement likewise leaves the
  input untouched; zero/short/full acknowledgement establishes the parse
  state, and later parse failure preserves its committed prefix. No
  convenience/alloc facade may add a dependency classifier, reorder the two
  phases, buffer rejected input, treat vectored/DMA queuing as transport
  consumption, or synthesize commitment from input.
- Expose early-final policy preference without exposing progress or reuse
  authority. Keep `EarlyFinalBodyDisposition`, exact request-body committed/
  unsent prefix, fixed/chunked delimiter/trailer obligation, exchange
  generation, successor gate, and close/reuse promotion engine-owned. Keep
  the legality matrix, reserved continuation budget/deadline, automatic
  AlreadyMessageCommitted selection, and `EarlyFinalTransportAction`
  engine-owned; caller preference cannot override framing, persistence,
  writability, source, or TLS/transport constraints. Keep `BridgeTransaction`,
  its phase/generation/reservation owners, all four phase-specific bridge
  capabilities, the sole sealed version-bound `ValidatedConnectionOptions`
  parser result and its HTTP/1.1 persistence/received-close/Upgrade, HTTP/1.0
  `Http10PersistenceDisposition` role/direction/newest-message owner,
  `ValidatedHttp10KeepAlive`, `CommittedHttp10KeepAliveHead`,
  `CorrelatedHttp10KeepAliveRequest`, connection/hop `Http10ReuseLedger`,
  lifecycle-bound exactly-once Completing state,
  `Http10ReuseResolutionRecord`, `Http10TerminalDecision`,
  `Http10ReusePermit` with sole deadline ownership, internal linear
  `Http10NextExchangeReservation` with deadline snapshot and pre-Active
  completion binding, fact-only terminal decision with exhaustive final-state
  method, command-borrow-bound attempt cursors, O(1) unit metadata, private
  single-use work permits and non-authoritative receipts, total
  reason-only-capacity `Http10SuccessorAdmissionOutcome`,
  `Http10LocalPersistenceMode`, generation-bound cleanup authority, the sole
  `Reusable -> ActiveExchange` successor transition, checked generation-
  exhaustion owner, exact future-admission allowance, role-feasible
  last-use-close builder obligation, reclaimable Active leases versus
  irreversible accounting, output-phase persistence-loss action, and
  either-version stripping refinements;
  `UnsupportedHttp10ConnectDisposition`, fixed 70-byte
  501 record, typed terminal action, later-input rejection, and mandatory close
  ownership;
  sealed five-way `TransitionInputProvenance`,
  `OptimisticConnectCloseProof`, `OptimisticConnectPermit`,
  one-shot `CommittedDownstreamSuccess`, reserved `BridgeActivationPermit` slot,
  clear-latch snapshot, matching frozen generation, and `BridgeInputLease` minting,
  optional-over-read `PendingHttp1Transition`, PendingConnect/ReceiveCredit/
  AwaitingBridgeActivation linkage, pending FIN/terminal-cause ownership,
  downstream-success exposure, Active promotion, and terminal action
  engine-owned. Callers cannot substitute request/response, leg, role, head, or
  generation evidence; construct/reparse/renormalize Connection evidence;
  substitute it across versions; forge, copy, or cross-bind either HTTP/1.0
  keep-alive signal, correlation owner, or reuse permit; consume a permit
  without a complete engine-owned reservation and atomic successor commit;
  construct, expose, extract, copy, or retain a partial reservation; reset,
  increment, refund, or decrement the ledger except once on admission; consult
  or modify the ActiveExchange snapshot as authorization; require a server
  response head to exist at request admission; drop/bypass/rebind
  `LastUseMustClose`; advertise keep-alive from an initial-zero or one-to-zero
  allowance; duplicate/move deadline ownership into the reservation or Active;
  reclaim accounting or leak committed leases; release a later generation with
  stale cleanup; conflate mint and admission failures; repeat mint after
  duplicate acknowledgement/hook/cancellation;
  classify a
  terminal preflight failure as peer misconduct; extract/return/borrow/consume
  input or permit on retryable capacity; numerically wrap
  a generation; admit overlapping generations; parse/accept/expose a successor
  before admission; treat head/record commitment short of bodyless/fixed
  `MessageCommitted` as the fast path; authorize HTTP/1.0 Transfer-Encoding,
  chunked, trailers, or close-delimited reuse; restore `Reusable` after
  admission; or turn
  `ValidatedHttp10KeepAlive` into
  received-close, optimistic-CONNECT, or Upgrade authority; bypass or rewrite
  a role-specific HTTP/1.0 persistence/CONNECT disposition; retain an older
  persistence permit after a newer message, refine proxy/gateway downstream
  request persistence, revoke the exact local request signal before response
  correlation, bind a response to a non-oldest request, forward received
  keep-alive authority, defer close to an illegal successor, mutate
  Frozen/HeadCommitted output, or enable HTTP/1.0
  pipelining; publish/resolve/forward before CONNECT rejection; mutate the fixed
  501, consume later input, change `Flush501ThenClose` on invalid
  acknowledgement, or fabricate complete 501 output after partial failure;
  forge committed close proof or optimistic permission; bind an HTTP/1.1 close
  proof to HTTP/1.0 default-close/keep-alive state;
  treat configured close intent as proof; promote unpermitted input after
  success; use wire-commit evidence as activation authority; mint an activation
  permit after premature input; repeat the completion hook or reuse consumed
  success/slot/latch/generation inputs; rebind ordinary CONNECT to WebSocket/CONNECT-UDP;
  turn unpermitted/forbidden input into a lease; copy/release/rebind
  pending bytes; publish a pending FIN; replace/collapse the first terminal
  cause; turn TLS close_notify into TCP half-close; escalate stream-local
  premature DATA; reset before an exposed immutable success block reaches
  END_HEADERS; skip/reorder phases; expose downstream success; cross bytes;
  retry an incomplete exchange; or mark a request/bridge reusable or active.
- Public constructors reject overflow in `checked_add(9, max_outbound_frame_payload)`, zero/undersized `field_fragment_cap`, enabled mandatory-prefix shortage, inconsistent block/continuation capacity, ambiguous padding, and HPACK layouts whose checked logical physical capacity exceeds exclusive caller storage. `EncoderTableLimits`, received/acknowledged ceiling transitions, selected-capacity mutation, decoder advertisement proof, `InboundSettingsTransaction`, `PendingEncoderTableSizeTransition`, `EncoderTableUpdateDebt`, leases, AckCommitted promotion, debt merge/restore/transfer, and HPACK promotion remain engine-owned and non-constructible. Callers provide storage and policy preferences but cannot forge a larger physical capacity, select outside limits, acknowledge a peer ceiling, advertise unsafe decoder capacity, or expose ACK/debt authority. Public output acknowledgement accepts only one token-bound suffix.
- Keep `OutboundSettingsTransaction`, ordered frozen entries, future-ACK FIFO
  reservation, commit plan/snapshot, timeout generation, strict committed FIFO,
  and every requested/frozen/committed/peer-ACK promotion engine-owned and
  non-constructible. Callers may request validated local settings and provide
  fixed storage/time, but cannot accept a command without its atomic reservation,
  mutate entries after exposure, apply advertised effects, promote the FIFO,
  start/cancel the deadline, bind an ACK, or roll back committed effects.
- Keep `ReceiveCredit`, `WindowUpdateOutput`, target/generation binding,
  private-to-in-flight transfer, and advertised-credit commitment engine-owned
  and non-constructible. Callers may acknowledge borrowed DATA and an exact
  offered output suffix, but cannot directly reclaim or advertise credit,
  choose/retarget an increment, acknowledge byte 13 without its token, merge
  stream and connection ledgers, or revive a closed generation.
- Keep `InboundPingTransaction`, `PingAckOutput`, copied opaque bytes, FIFO
  position, local correlation keys/generations/tombstones, and completion
  promotion engine-owned and non-constructible. Callers may request a local
  liveness probe and acknowledge one exact offered suffix, but cannot supply or
  reuse the wire correlation key, forge a peer reply obligation, access opaque
  peer bytes after parsing, coalesce transactions, match an ACK, or release a
  PING slot before byte 17.
- Keep `ShutdownIntent`, `PublishedPeerStreamHighWater`, `GoawayOutput`,
  `SentGoawayCutoff`, fatal-cause ranking, owned debug, and graceful timer
  evidence engine-owned and non-constructible. Callers may request graceful
  shutdown, supply optional debug input that is copied/redacted under policy,
  and acknowledge one offered suffix, but cannot choose the final processed
  cutoff, forge publication, arm/fire a timer, rank fatal causes, rewrite Frozen
  bytes, commit a prefix, claim peer visibility, or derive retry authority.
- Keep scheduler class, enqueue ordinal, bypass/deadline counters,
  `ControlServiceProfile`, `ControlDisposition`, and fatal-cleanup promotion
  engine-owned and non-constructible. Callers may supply checked positive
  service-policy values and monotonic time, but cannot rank or reorder records,
  close a service gate, forge age/deadline expiry, abandon a control, run a
  semantic completion hook, or revive ownership after fatal cleanup.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Fixed-capacity caller-storage public API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-capacity caller-storage public API contract and all previously implemented relevant behavior have
reproducible evidence; v0.190.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) still passes; no behavior assigned to v0.192.0 (Optional alloc-backed convenience API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.191.0 implementation stop reached. Run pentest for this exact commit.`

### v0.192.0 — Optional alloc-backed convenience API

Status: planned

#### Goal

Deliver **Optional alloc-backed convenience API** as the sole primary capability in this stop. It builds
on v0.191.0 (Fixed-capacity caller-storage public API) and must be independently trustworthy before v0.193.0 (Stable diagnostics and security events) begins.

#### Deliverables

- Acceptance contract: Build the owned layer only as a wrapper reducible to the stable borrowed API, with identical protocol decisions and no alloc-only correctness path; owned request builders cannot bypass final conditional/range validation or detach correlation evidence, and owned response builders must obtain and consume the same frozen `ValidatedResponse` object and cannot extract a permit, substitute another head, fabricate, clone, cache, reuse, mutate after validation, or bypass request/content/partial-response/semantic/trailer permissions and the mandatory reserve.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Optional alloc-backed convenience API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional alloc-backed convenience API contract and all previously implemented relevant behavior have
reproducible evidence; v0.191.0 (Fixed-capacity caller-storage public API) still passes; no behavior assigned to v0.193.0 (Stable diagnostics and security events) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.192.0 implementation stop reached. Run pentest for this exact commit.`

### v0.193.0 — Stable diagnostics and security events

Status: planned

#### Goal

Deliver **Stable diagnostics and security events** as the sole primary capability in this stop. It builds
on v0.192.0 (Optional alloc-backed convenience API) and must be independently trustworthy before v0.194.0 (Feature and dependency-policy surface) begins.

#### Deliverables

- HTTP/1.0 diagnostics extension: report whether the completion binding was reserved by initial/successor admission, common and cause-specific binding comparison, resolution record, optional first interrupt, exhaustively computed final state, attempt generation, work kind/charged units/processed units/base/per-unit/total, O(1) unit source, actual cursor progress, retry recharge, and typed error through `AdmissionWorkReceipt`. Diagnostics store neither a command borrow/cursor nor `AdmissionWorkPermit`; receipts, revoked reuse identity, and other diagnostics never grant authority.
- Acceptance contract: Assign stable non-secret diagnostic codes to syntax, protocol scope/code, policy, capacity, cancellation, timeout, transport, and peer/local role; include bounded offsets/counters and generation identifiers, redact field/credential/compression/section contents, and emit each event once. Distinguish local `AssemblyInvalidationCapacity`, `PushedAssemblyProvenanceCapacity`, `StreamTrackingUnavailable`, `PushRejectionTrackingUnavailable`, and `OutboundFrameStorageCapacity`. For reset and ordinary output, separately record AcceptedPrivate/Frozen/Complete/SupersededBeforeExposure disposition, Private/FramingCommitted/HpackCommitted/AbandonedWithConnection field-block disposition, stream/block/slot generation, remaining CONTINUATION count, command/local-send seal, exposure, offered/acknowledged counts, outstanding token, completion hook, directional transition, remote/reset records, and immutable first-wire-closure cause. For DATA, record bounded arena/queue bytes and entries, local payload cap, staged slot length, stream/connection available, reserved-unexposed, committed-debited charge, and reservation generation without payload contents. Never report released reservation as debit, freed arena capacity as still owned, refund frozen debit, offered-but-unacknowledged bytes as written, partial/failing output as half-closed/closed, RemoteEndStream as a closure cause when it only produced HalfClosedRemote, or later completion as replacing a peer-first close. Record terminal/section/workspace dispositions without raw contents and preserve redaction/caller-scrub rules.
- Record early-final request generation, framing kind, disposition, bounded
  committed/unsent counts, delimiter/trailer obligation, successor/reuse gate,
  legality inputs, reserved deadline/work, typed transport action, and
  close/abort reason without body contents. Record bridge generation, ordered
  phase, reserved capacities, one of the four phase/message-kind capability
  classes and its redacted leg/role/head-generation binding, inbound terminal/
  correlation stage, all five transition-input provenance classes, v0.56.0
  validated-option evidence generation, exact HTTP version, lexical result,
  and consumer/refinement kind; HTTP/1.0 role/direction persistence disposition,
  newest-message generation/revocation, received/local keep-alive signal
  generation, oldest-request correlation/transfer outcome, local-head
  commitment, pair/hop match, total reuse-resolution outcome/reason, reuse-ledger before/
  after count, future-admission allowance meaning, immutable snapshot,
  `Negotiable`/`LastUseMustClose` mode and builder application point,
  permit-exclusive deadline plus reservation snapshot and stale-expiry result,
  exactly-once completion/cancellation winner, next-exchange reservation component
  acquisition/release/commit, terminal lease/unused-parser-reserve reclamation,
  irreversible ledger/count/work accounting, cleanup generation/result,
  successor outcome/reason, permit/input ownership, exact bodyless/fixed
  message-completion boundary, next-generation checked-exhaustion result,
  output-phase persistence-loss action, and pipeline-disabled state;
  close-proof kind and exact received/locally-committed head binding;
  role-specific HTTP/1.0 CONNECT classification/precedence point,
  local-capacity/start-line-kind/414/431/400/501 outcome,
  application/resolve/forward suppression, original optimistic-byte discard,
  exact 70-byte mandatory 501 reserve/image/output offset, later-input
  unconsumed count, `Flush501ThenClose`/`CloseTransportNow`, invalid-
  acknowledgement neutrality, zero-partial close fallback, and terminal outcome;
  optimistic permit kind/binding,
  strict missing-proof disposition, transfer/discard outcome,
  and acknowledgement offset,
  HTTP/1
  PendingHttp1Transition/OverreadLease versus HTTP/2 PendingConnectLease and
  AwaitingConnectOutcome/AwaitingBridgeActivation/ActiveTunnel ownership,
  optional-over-read presence, padded/semantic DATA and private/advertised
  credit counts, distinct plain EOF/close_notify/TLS-truncation/fatal-alert/
  reset/transport-failure/cancellation cause, pending-FIN policy, immutable
  first terminal cause, lease-minted/terminal-discarded disposition, HTTP/2
  stream-versus-connection failure scope and reset code, downstream-success
  AcceptedPrivate/Frozen/FramingCommitted/Committed disposition, exposure and
  HEADERS/CONTINUATION acknowledgement offset, immutable suffix/reset order,
  premature-input latch, consumed/unconsumed wire-commit evidence, reserved/
  consumed permit slot, latch-snapshot and frozen-generation match, completion-
  hook outcome, activation-permit state, Active promotion, and exact pre-exposure HTTP
  failure or post-exposure close/reset/abort action without handshake/tunnel
  bytes or duplicate ownership.
- Report `DriverCommitOrderViolation` as a local adapter defect with redacted
  connection/output generation, acknowledged cursor, and dependent-input class;
  never consume/log input contents, attribute it to peer protocol misconduct,
  or emit a protocol transition/event for the rejected call.
- Distinguish Private/FramingCommitted/HpackCommitted/AbandonedWithConnection, transition/debt ownership, and SETTINGS disposition; separately report bounded peer-received ceiling, peer-wire-acknowledged ceiling, selected capacity, checked physical capacity, active profile cap, per-frame snapshot/selected-delta presence, ACK offset, debt smallest/final values, and decoder advertised/effective capacity without settings/header contents or raw storage addresses. Never conflate a ceiling with selection/debt, report an increase as selected, overstate physical storage, attribute ACK ownership to debt, report AckEligible/offset eight as committed, diagnose Private encoding as debt consumption, or hide eviction lacking a selected wire update.
- For outbound SETTINGS, separately report redacted transaction/generation,
  requested/Frozen/CommittedAwaitingAck/PeerAcked/abandoned disposition, entry
  count, total/acknowledged bytes, future/FIFO slot state, commit-plan effect
  classes, deadline generation/state, speculative-ACK/driver-order classification, and peer
  visibility. Never expose setting contents unnecessarily, report a prefix as
  locally advertised, report peer ACK as effect application, retain an
  uncommitted ACK for later, hide DriverCommitOrderViolation as peer fault, or
  diagnose terminal cleanup as rollback.
- For stream and connection receive flow control, separately report bounded
  advertised remaining, reclaimed-unadvertised, update-in-flight, update target
  kind/generation, Private/Frozen disposition, and acknowledged offset 0..=13.
  Never report reclaimed or in-flight credit as advertised, offset 12 as
  committed, a cancelled stream update as lost connection credit, a stale token
  as progress, or a transport-failed prefix as window restoration.
- For PING, report redacted inbound transaction generation, FIFO position,
  ReservedPrivate/Frozen/Complete disposition, acknowledged offset 0..=17,
  capacity/budget outcome, and local correlation
  in-order-match/reordered-match/unsolicited/duplicate/stale classification.
  Never expose
  opaque bytes, treat equal peer payloads as one transaction, report offset 16
  as complete, claim a failed prefix released its slot, or diagnose correlation
  mismatch as an RFC connection error.
- For GOAWAY, separately report admission-sealed, graceful/fatal intent and
  selected cause class/code, stage, output generation, ReservedPrivate/Frozen/
  Complete/AbandonedConnection disposition, total/acknowledged lengths,
  application-published high-water, requested/frozen/committed/received cutoff,
  timer generation/state, debug length/truncated-or-omitted disposition, and
  peer-visibility known/unknown. Never expose debug contents, report a prefix as
  sent, arm the timer early, treat parsed/allocated as processed, replace Frozen
  cause/bytes, widen an increasing received cutoff, or imply replay authority.
- For the connection scheduler, report redacted class, FIFO/enqueue ordinal,
  connection/record generation, bypass count, deadline state, and
  `ControlDisposition`, including fatal-abandonment generation. Never expose
  PING payload/debug contents, diagnose a service gate as wire commitment,
  report abandoned work as sent/ACKed/credited/reset-complete, or emit more
  than one terminal cleanup event for an owner.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Stable diagnostics and security events and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stable diagnostics and security events contract and all previously implemented relevant behavior have
reproducible evidence; v0.192.0 (Optional alloc-backed convenience API) still passes; no behavior assigned to v0.194.0 (Feature and dependency-policy surface) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.193.0 implementation stop reached. Run pentest for this exact commit.`

### v0.194.0 — Feature and dependency-policy surface

Status: planned

#### Goal

Deliver **Feature and dependency-policy surface** as the sole primary capability in this stop. It builds
on v0.193.0 (Stable diagnostics and security events) and must be independently trustworthy before v0.195.0 (Multi-implementation interoperability) begins.

#### Deliverables

- Acceptance contract: Keep default and all feature combinations no_std, safe, and free of third-party Cargo dependencies; `http1` includes `vef-core` + `vef-auth` + `vef-conditions` + `vef-semantics` + `vef-http1`, `http2` additionally includes `vef-hpack` + `vef-http2`, and no facade feature can disable conditional/range/response/trailer validation or the mandatory semantic reserve while retaining serialization; features only add separately owned APIs/crates, never weaken limits or validation, compile under Rust 1.90.0..=1.97.1, and fail policy checks on dependency, std, unsafe, or unintended facade-surface drift.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Feature and dependency-policy surface and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Feature and dependency-policy surface contract and all previously implemented relevant behavior have
reproducible evidence; v0.193.0 (Stable diagnostics and security events) still passes; no behavior assigned to v0.195.0 (Multi-implementation interoperability) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.194.0 implementation stop reached. Run pentest for this exact commit.`

### v0.195.0 — Multi-implementation interoperability

Status: planned

#### Goal

Deliver **Multi-implementation interoperability** as the sole primary capability in this stop. It builds
on v0.194.0 (Feature and dependency-policy surface) and must be independently trustworthy before v0.196.0 (Adversarial and stateful fuzz campaign) begins.

#### Deliverables

- Acceptance contract: Run fixed HTTP/1, HTTP/2, HPACK, Structured Fields, Upgrade, CONNECT, and proxy transcripts against at least two independent peers per applicable protocol; record versions and wire artifacts, require semantic and error-scope agreement, and resolve every divergence without adding permissive parser exceptions.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Multi-implementation interoperability and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Multi-implementation interoperability contract and all previously implemented relevant behavior have
reproducible evidence; v0.194.0 (Feature and dependency-policy surface) still passes; no behavior assigned to v0.196.0 (Adversarial and stateful fuzz campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.195.0 implementation stop reached. Run pentest for this exact commit.`

### v0.196.0 — Adversarial and stateful fuzz campaign

Status: planned

#### Goal

Deliver **Adversarial and stateful fuzz campaign** as the sole primary capability in this stop. It builds
on v0.195.0 (Multi-implementation interoperability) and must be independently trustworthy before v0.197.0 (Compile-fail state and lifetime tests) begins.

#### Deliverables

- HTTP/1.0 fuzz extension: cross initial/successor completion-generation exhaustion, abandonment, cancellation, reservation-slot reuse, exact/stale common bindings, and every cause generation in all phases and after publication/successor admission. Combine every resolution/interrupt pair through the non-stored final-state method; fuzz command mutation between reason-only retries, per-call cursor destruction, charged `n` versus actual `0..=n`, stale/cross-attempt/duplicated/reused work permits, receipt misuse, instrumented iterators, max fields/bytes, early malformed bytes, one-byte fragments, retries/rescans, and arithmetic errors. Assert full retry recharge, actual-progress movement, no residual authority, and no unpriced/quadratic work.
- Acceptance contract: Maintain stateful fuzz targets for HTTP/1, HPACK, HTTP/2, Structured Fields, and translation with deterministic minimized replay. The HTTP/2 oracle spans ResetOutput × ordinary AcceptedPrivate/Frozen/Complete/Superseded output × `OutboundFieldBlock` Private/FramingCommitted/HpackCommitted/AbandonedWithConnection × initial/CONTINUATION position × exposure/acknowledgement × completion hook × HEADERS/PUSH_PROMISE/DATA/trailers/empty-DATA layout × arena slot/byte/entry ownership × peer/local payload limits × stream/connection available-reserved-committed credit × padding × every control queue × WINDOW_UPDATE/SETTINGS/resegmentation × token generations × every inbound frame × wire/closure/terminal/section state × peer/local reset/GOAWAY/failure/reuse. It asserts whole-block-only private supersession, END_HEADERS contiguity after FramingCommitted and final-frame-only HpackCommitted publication, no continuation/control interleaving, independent initial END_STREAM completion, connection-only abandonment, staged-byte immutability/no early reuse, typed independent byte/entry backpressure, peer-maximum framing under a small local cap, paired refund, no frozen refund/mutation, exact suffix and hook once, atomic no-oversubscription credit, full payload but no header charge, zero-length zero charge, negative-window blocking, directional legality, HPACK ownership, stable first cause, partial-failure non-completion, and no stranded state.
- Add stateful transitions for every combined SETTINGS transaction plus `EncoderTableLimits`, transition obligations, and selected debt. Cross encoder/decoder caller arenas from unusable through 4096+, peer ceilings 0/4096/`u32::MAX`, profile boundaries, local policy changes without SETTINGS, increases before/after the relevant ACK byte nine, initial selected capacity below 4096, unsafe decoder advertisement/activation, every Private/exposure/CONTINUATION/debt boundary, rollback, backpressure, stale tokens, reset, GOAWAY, and failure. Assert all inequalities, immediate reduction/no automatic increase, exact per-frame acknowledged snapshots, selected-only debt, no eviction without matching update, correct first-block reduction, lease restoration/transfer, one ACK/fatal cancellation, and encoder/decoder table equivalence.
- Add stateful outbound SETTINGS transactions across client/server initial
  activation, later commands, exact `9 + 6 * entry_count` capacity, every frame
  offset, future-ACK/timeout/commit-plan reservation, all setting-effect owners,
  several committed frames, speculative/ordered/unsolicited ACK, deadline
  generations, fatal GOAWAY, partial failure, stale tokens, and connection reuse.
  Assert preface/first-frame coupling, zero-exposure capacity failure,
  immutable bytes, final-byte-only effect/FIFO/deadline commitment, no effect
  reapplication, oldest-committed ACK, no uncommitted ACK retention,
  acknowledgement-first combined calls, state-neutral driver-order failure,
  unknown partial visibility, and no committed-effect rollback.
- Add stateful `ReceiveCredit × WindowUpdateOutput` transitions for both target
  kinds. Generate DATA/padding/acknowledgement/discard, checked private
  coalescing, first exposure, all output offsets 0..=13, further reclamation,
  FramingCommitted blocking, stream reset/closure/reuse, connection-only
  post-reset paths, stale/cross-record tokens, flow-control underflow at every
  prefix, and partial transport failure. Assert ledger conservation, the
  31-bit ceiling, immutable Frozen bytes/target/increment, and final-byte-only
  advertised restoration.
- Add stateful `InboundPingTransaction × PingAckOutput ×
  LocalPingCorrelation` transitions. Overwrite receive storage immediately;
  generate distinct and identical non-ACK PINGs, ACK-bearing frames, bounded
  FIFO/table/tombstone exhaustion, unique-key wrap/reuse, every scheduling
  boundary, all output offsets 0..=17, stale/duplicate/cross-record/overlong
  tokens, transport failure, and matching/unsolicited/duplicate/reordered/stale
  ACKs. Assert owned-byte independence, exact one-for-one replies, no
  coalescing, byte-17-only release, priority after committed framing, bounded
  cleanup, and state-neutral nonmatching correlation.
- Add stateful `ShutdownIntent × PublishedPeerStreamHighWater × GoawayOutput ×
  SentGoawayCutoff × GraceTimer` transitions. Generate application publication
  immediately around final exposure, higher-stream HPACK/credit work, graceful
  initial/final, every ranked fatal arrival order, zero/maximum/reused debug,
  scheduler blocking, all offsets 0..=`17 + debug_len`, timer generations,
  received decreasing/equal/increasing cutoffs, queue exhaustion, duplicate
  causes, stale/cross-record tokens, and transport failure. Assert
  publication-derived snapshots, immutable Frozen bytes, final-byte-only
  cutoff/timer commitment, monotonic ledgers, unknown partial visibility,
  deterministic single fatal successor, owned/redacted debug, and no
  cutoff-derived replay permit.
- Add the global scheduler and fatal-cleanup product: generate every pair and
  simultaneous set of mandatory controls, same-class FIFO/generation ties,
  continuous PING bursts, bypass/deadline boundaries, capacity shutdown, fatal
  arrival in every Private state and Frozen byte offset, and stale tokens after
  generation reuse. Assert the exact total order, finite configured service,
  no caller-clock reorder of committed work, Frozen-first completion, atomic
  Private-only abandonment after fatal commitment, no later output, exact-once
  release, and no fabricated ACK/debt, credit, reset, response, or timer hook.
- Fuzz the v0.25.0 causal call product over offered bytes, invalid/stale/
  oversized and every valid zero/short/full acknowledgement, outstanding token
  generations, input-only/combined delivery, input parse failure, scalar/
  vectored/DMA progress, HTTP/1 request/response heads and transition barriers,
  inbound SETTINGS/PING ACK, locally initiated HTTP/2 response frames,
  extension-dependent frames, GOAWAY, failure, and retry. Assert the exact
  token is consumed before any parsing, invalid acknowledgement leaves input
  wholly unconsumed, zero parses unchanged state, committed prefixes survive
  parse failure, input-only with a live token returns only
  `DriverCommitOrderViolation`, and no peer input, classifier, or queued caller
  memory completes output.
- Fuzz HTTP/1 `AcceptedPrivate/Frozen/HeadCommitted/MessageCommitted/Abandoned`
  request generations, outstanding-response FIFO order, every fixed/chunked/
  zero-chunk/trailer output offset, 1xx/final/100 timing, all
  `EarlyFinalBodyDisposition` outcomes, persistence/default-close/
  close-delimited framing, transport writability, source availability,
  continuation-budget/deadline exhaustion, both typed transport actions,
  simultaneous response bodies, cancellation, 417 retry, and attempted
  successors. Assert correlation begins only at request HeadCommitted;
  zero/short/full body progress survives the combined call;
  AlreadyMessageCommitted is automatic; continuation is impossible unless
  every condition holds; suppression releases only certified-unsent bytes and
  never restores reuse; and retry generations cannot overlap incomplete
  originals.
- Fuzz CONNECT 2xx, Upgrade/WebSocket 101, and the v0.163.0/v0.187.0/v0.188.0
  `BridgeTransaction` at every one of the four capability kinds, HTTP/1 head,
  outbound HTTP/2 field-block, inbound HTTP/2 compression/semantic/correlation
  stage, binding mismatch, reservation shortage, legal phase edge, illegal
  phase skip/reorder, lease kind, stale generation, and pre/post-downstream-
  exposure failure. Replay the sole v0.56.0 `ValidatedConnectionOptions` corpus
  under both versions through HTTP/1.1 persistence/close-proof/Upgrade,
  HTTP/1.0 default-close/`ValidatedHttp10KeepAlive`/
  `CommittedHttp10KeepAliveHead`/`CorrelatedHttp10KeepAliveRequest`/
  `Http10ReusePermit`, and either-version intermediary-stripping consumers.
  Exhaust oldest-request correlation-before-revocation, ambiguous response
  closure, all two-signal orders and output commitment offsets, per-hop
  non-forwarding, separate total reuse resolution and `Reusable -> ActiveExchange`
  admission transitions for both role entry points; ledger maxima 0/1/N, every
  resolution/admission reason, initial-zero/one-to-zero mode across client request,
  delayed server response and existing-private-head builders, reason-only
  capacity retry with engine-retained permit/deadline, every
  `Http10NextExchangeReservation` component one short/exact and atomic
  storage/count/work/deadline-snapshot/generation/mode commit, exact deadline
  preservation on rollback and stale expiry after admission, duplicate final
  acknowledgement and completion-hook calls, cancellation immediately
  before/during/after completion resolution and same-call admission, exact
  deadline/add-overflow in its correct phase,
  generation maximum/exhaustion with stale tokens, and every combined
  response `MessageCommitted` plus successor-input order across positive
  bodyless/fixed and negative Transfer-Encoding/chunked/trailered/close-
  delimited output,
  every `AcceptedPrivate`/`Frozen`/`HeadCommitted`/`MessageCommitted`
  persistence-loss boundary, newest-message revocation, one-shot reuse, and
  no-pipelining rule. At every post-admission terminal point prove generation-
  bound exactly-once record/lease/unused-reserve reclamation while ledger/count/
  consumed-work/admission-work accounting stays charged. Require no false
  keep-alive advertisement, no server-response dependency at admission, no
  duplicate deadline owner, no partial reservation/debit/lease, no engine
  structural fallibility after Active publication, and at most one resolution,
  permit, decrement, reservation commit, cleanup, and successor.
  Require identical lexical decisions with distinct semantic authority and
  reject every cross-role/direction/version/connection/generation substitution.
  Generate all five provenance
  classes, both HTTP/1 ordinary-
  CONNECT close-proof constructors, missing proof, configured intent, every
  locally generated head acknowledgement offset, stale/cross-head proof, and
  early bytes through 2xx/non-2xx,
  downstream WebSocket data with zero/short/full/invalid success
  acknowledgement, legal upstream 101 plus data, ordinary HTTP/2 PendingConnect,
  and success HEADERS followed by DATA/padding/END_STREAM/RST_STREAM. Cross
  terminal-only, bytes-only, and combined HTTP/1 transitions with all seven
  causes at every phase. For premature RFC 8441 DATA, cross syntax/padding/
  stream-and-connection-window/reclamation boundaries and interleave unrelated
  SETTINGS/PING/HEADERS/DATA. Cross AcceptedPrivate, first exposure with zero
  acknowledgement, every HEADERS/CONTINUATION suffix offset, final-END_HEADERS
  acknowledgement ordering, connection failure at every suffix prefix, duplicate/
  stale final acknowledgements, repeated completion hooks, cancellation at each
  atomic completion-publication edge, and bridge-generation teardown/reuse.
  Assert exact provenance gates, strict missing-proof disposal, one transfer or
  discard, no ordinary-to-WebSocket rebinding, private supersession or exposed
  immutable completion before stream-local PROTOCOL_ERROR reset, no activation
  permit on a latched failure, exactly one evidence/slot/latch/generation
  consumption and at most one permit/success event/lease transfer, preserved
  unrelated frames/HPACK, no duplicate owner/credit, no close_notify-derived
  TCP half-close, and immutable first cause. Replay every role-specific
  `UnsupportedHttp10ConnectDisposition` through local capacity, aggregate
  start-line byte/work, method/version component, target-within-cap aggregate,
  target/work 414, field/work 431, syntax/framing/content 400, and valid CONNECT
  501 precedence at every boundary, request-plus-optimistic-bytes, all
  persistence matrix variants,
  the exact 70-byte image, every offset 0..=70, invalid/stale/cross/oversized
  acknowledgement neutrality, input-only driver-order failure, valid-
  acknowledgement-first input closure, mandatory-response capacity failure,
  EOF/cancellation/transport failure, and attempted
  publication/resolution/forwarding/successor/tunnel creation. Require
  zero-output local builder rejection or reserved 501-and-close/zero-partial
  fallback, one original discard, later input wholly unconsumed, no variable
  response/body, invalid-call state mutation, fabricated completion, indefinite
  backpressure, or HTTP/1.1 authority.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Adversarial and stateful fuzz campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Adversarial and stateful fuzz campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.195.0 (Multi-implementation interoperability) still passes; no behavior assigned to v0.197.0 (Compile-fail state and lifetime tests) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.196.0 implementation stop reached. Run pentest for this exact commit.`

### v0.197.0 — Compile-fail state and lifetime tests

Status: planned

#### Goal

Deliver **Compile-fail state and lifetime tests** as the sole primary capability in this stop. It builds
on v0.196.0 (Adversarial and stateful fuzz campaign) and must be independently trustworthy before v0.198.0 (Long-running soak and exhaustion campaign) begins.

#### Deliverables

- HTTP/1.0 compile-fail extension: reject common/cause binding creation/rebinding, post-publication completion-generation allocation, construction/caching of final-state authority, resolution/interrupt conflation, revoked reuse identity conversion to permit, attempt cursor escape beyond the command borrow/call, reason-only result retaining progress, work-kind/spec/unit/cursor construction, private permit fabrication/clone/copy/reuse/cross-attempt transfer, receipt-to-permit conversion, numeric charge entry, cursor rewind, iterator pre-traversal, and entry inspection without consuming a work permit.
- Acceptance contract: Provide compile-fail cases proving borrowed input/body/events cannot outlive storage, acknowledged chunks cannot be reused, stale stream/exchange generations cannot issue commands, role-specific builders cannot construct forbidden transitions, and fixed-capacity APIs cannot smuggle alloc/std ownership into core crates; additionally prove callers cannot construct/clone/copy/reuse/rebind civil-time evidence, `OutputToken`, `OutboundFrameSlot`, `FrozenOutboundFrameSlot`, CurrentRepresentationEvidence, WouldBe200Snapshot, RequestContentPermit, MethodExecutionPermit, ParsedMediaType, ValidatedGeneratedMediaType, ValidatedConditionalRequest, PartialContentTypeClassification, PartialResponseDisposition, ValidatedPartialResponseHead, SelectedPartialDelivery, PartialBodyChunk, StandalonePartialComplete, VariantFieldLease, VariantSelectionIdentity, VariantSelectionEvidence, ActiveVariantNormalizationBudget, FullRepresentationFallback, AssemblyInvalidationHandle, PushedAssemblyProvenance, ConservativeReplacementScope, ConservativeInvalidationScope, ArenaRotationCause, ActiveOverlapBudget, StorageLeaseGeneration, StoredRepresentationSlice, StoredPartialSegment, ValidatedIncomplete200Prefix, CombinablePartialSegment, CombinableIncomplete200Prefix, AssemblyReplacementKey, PartialAssemblyContext, ReceiptOrderSource, ResponseHeadReceiptOrdinal, CombinationOutputLease, PartialCombinationPlan, or `ResponseEmissionPermit`; prove callers can construct preferences/requested budgets/ordinary errors without authority and create `OutboundFrameArena`/VariantIdentityStorage only from exclusive slice/sealed-slot inputs; reject duplicate/stale/cross-generation output acknowledgement, access/mutation/reuse of staged arena bytes while AcceptedPrivate/Frozen/offered, slot duplication/rebinding, frozen-frame/reset substitution, early stream/tombstone reuse, invalidation-handle/provenance Copy/Clone/duplication/rebinding/early or double release/retry reuse, ordinary-to-pushed or cross-associated-request rebinding, peer-derived principal/partition/tenant/navigation substitution, associated-stream-borrowed provenance or reuse after associated-stream teardown, promised publication without atomic slot/handle/provenance/rejection-tracking reservation, tombstone release before cancellation/classification horizon, caller storage traits/trust constructors, alias/mutate/recycle/reissue while leased, semantic invalidation used to end a borrow or authorize slot reuse, unfenced DMA mutation, identity release then assembly admission, active-budget reset/enlargement/replacement, frozen-data substitution, wrong generation/domain/principal use, trailer decision changes, and fabricated outcomes.
- Reject APIs or call patterns that alias the same input/output storage across
  causal phases, forge output-commit evidence from input, reorder the combined
  operation, classify input to bypass a live token, acknowledge caller-queued
  vectored/DMA bytes, or let the engine retain rejected input. The caller
  regains wholly unconsumed input after invalid acknowledgement or input-only
  delivery with a live token and may resubmit it through a valid combined call.
- Reject caller construction, copying, rebinding, or direct mutation of
  `EarlyFinalBodyDisposition` progress/reuse evidence and `BridgeTransaction`
  phase/reservation/commitment/validation/lease/Active/terminal evidence.
  Reject caller-selected AlreadyMessageCommitted, continuation without every
  persistence/writability/source/budget condition, fabricated transport action
  or half-close, successor/417 overlap with an incomplete request, reuse after
  suppression/partial framing, release of transport-consumed body bytes, and
  delimiter/trailer omission. Reject every substitution among
  `ValidatedDownstreamRequest`, `CommittedUpstreamRequest`,
  `ValidatedUpstreamSuccess`, and `CommittedDownstreamSuccess`, including
  mismatched bridge/connection/leg/role/message/head generations with equal
  numeric stream IDs; reject inbound HpackCommitted fabrication,
  caller construction/rebinding of ValidatedConnectionOptions,
  Http10PersistenceDisposition, ValidatedHttp10KeepAlive,
  CommittedHttp10KeepAliveHead, CorrelatedHttp10KeepAliveRequest, or
  Http10ReusePermit,
  TransitionInputProvenance, OptimisticConnectCloseProof,
  OptimisticConnectPermit, CommittedDownstreamSuccess, or
  BridgeActivationPermit; raw Connection reparsing by later consumers;
  cross-role/direction/version option substitution; older persistence evidence
  retained after a newer message; proxy/gateway downstream request keep-alive;
  missing one side of negotiation; cross-hop or forwarded keep-alive authority;
  response correlation after signal revocation; non-oldest/missing/duplicate
  request correlation; reuse before both message lifecycles complete; permit
  construction/extraction/rebinding/duplication after retryable capacity;
  reservation construction/exposure/extraction/rebinding/duplication or
  consumption with any missing exchange/correlation/parser/event/output/count/
  work/deadline-snapshot/generation/mode component; deadline ownership in both
  permit and reservation/Active; retry losing the exact deadline; stale expiry
  closing Active; post-Active engine-structural initialization; requiring a
  server response head during admission; bypassing or dropping
  `LastUseMustClose` before later response construction;
  consumption without complete preflight; ledger reset/increment/refund or
  duplicate decrement; initial-zero keep-alive, one-to-zero keep-alive, a zero
  snapshot/mode minting `CommittedHttp10KeepAliveHead`; duplicate/stale cleanup,
  cross-generation release, failure to release reclaimable leases/unused parser
  reserve, refund of ledger/count/consumed-work/admission-work accounting;
  duplicate mint/hook/acknowledgement or cancellation recreating `Reusable`;
  zero/count/work/policy/deadline/correlation/generation
  failure assigned to the wrong mint/admission phase; omitted
  `PermitLedgerMismatch`; failure with wrong permit/input/state/error ownership;
  stale/expired permit
  admission; deadline equality accepted; unchecked deadline addition; numeric
  generation wrap or ABA; overlapping successor generation; client request
  acceptance/exposure or server input consumption before admission; capacity
  failure retaining a partial lease/debit/charge, consuming permit/input, or
  decrementing the ledger; no-refund interpreted as caller-storage leakage;
  snapshot modified or consulted as authorization;
  head/nonfinal-record acknowledgement treated
  as MessageCommitted; Transfer-Encoding/chunked/trailer/close-delimited reuse;
  fixed successor admitted before completion; cancellation refund; rollback from
  ActiveExchange to Reusable;
  close deferred to a successor;
  Frozen/HeadCommitted head mutation; HTTP/1.0 pipelining;
  HTTP/1.0 keep-alive/default-close rebound
  as HTTP/1.1 close proof, optimistic CONNECT, or Upgrade authority;
  construction/bypass/rebinding of UnsupportedHttp10ConnectDisposition;
  mutable/non-70-byte/HTTP/1.1/chunked/trailered/body-bearing 501 output;
  wrong local-capacity/start-line/414/431/400/501 precedence; any aggregate,
  method, or version limit falling through to 501; application-visible
  authority-form CONNECT; later-input consumption or retention after rejection;
  invalid acknowledgement changing the 501 cursor, action, token, or input;
  application publication/authority resolution/forwarding after HTTP/1.0
  CONNECT; successor/tunnel or fabricated 501 completion after partial failure;
  configured close intent accepted as proof;
  missing-proof input promoted after success; raw CommittedDownstreamSuccess
  accepted as activation authority; duplicate consumption of committed-success,
  permit-slot, latch-snapshot, or frozen-generation evidence; activation after a
  latched premature input;
  ordinary-CONNECT permission reused for WebSocket or CONNECT-UDP;
  unpermitted/forbidden-input BridgeInputLease minting; construction/copy/
  rebinding of PendingHttp1Transition, mandatory-overread-only APIs that cannot
  represent terminal-only state, mutation/replacement/collapse of
  PreActiveTerminalCause, close_notify-to-TCP-half-close conversion,
  premature RFC 8441 DATA escalated beyond its stream without an independent
  connection-fatal cause, reset scheduled before an exposed immutable
  HEADERS/CONTINUATION suffix reaches END_HEADERS,
  PendingConnectLease/AwaitingBridgeActivation range or FIN duplication/copy/
  rebinding/early credit/discard, bridge phase skip/reorder, downstream success
  exposure before upstream validation, byte/FIN crossing before Active, and a
  replacement HTTP response after partial downstream exposure.
- Reject construction/rebinding of `EncoderTableLimits`, peer-ceiling snapshots, acknowledged-ceiling evidence, selected-capacity transitions, decoder-advertisement proof, `HpackEncoderTransaction`, SETTINGS/ACK transactions, `EncoderTableUpdateDebt`, or its lease. Reject selected > received/profile/physical, increases > wire-acknowledged ceiling, raw peer ceiling inserted as debt, automatic selection increase, eviction without selected update, unsafe decoder advertisement, AckCommitted before byte nine, duplicate/cross-block debt lease, rollback without exact restoration, early clearing/transfer, caller HpackCommitted, bound bypass, and cross-record acknowledgement.
- Reject construction, cloning, copying, rebinding, or direct promotion of
  `OutboundSettingsTransaction`, future-ACK slot, commit plan/snapshot, timeout
  generation, and committed-FIFO evidence. Reject unreserved preface/SETTINGS
  exposure, checked-length overflow, entry mutation after exposure,
  locally-advertised promotion before full acknowledgement, caller FIFO/deadline
  promotion, peer-ACK effect reapplication, cross-generation ACK/timeout,
  committed-effect rollback, and slot reuse before terminal release.
- Reject construction, cloning, copying, rebinding, or direct mutation of
  `ReceiveCredit`, `WindowUpdateOutput`, update targets/generations, and
  private/in-flight credit. Reject caller-selected increments, cross-target or
  cross-generation acknowledgement, acknowledgement beyond the offered suffix,
  advertised restoration before byte 13, frozen retargeting/substitution,
  stream-to-connection conversion, and reuse after completion or abandonment.
- Reject construction, cloning, copying, rebinding, payload substitution,
  coalescing, or direct completion of `InboundPingTransaction`,
  `PingAckOutput`, and `LocalPingCorrelation`. Reject caller-chosen/reused
  correlation keys, cross-transaction/generation acknowledgement, completion
  before byte 17, access or recycling of frozen/copied storage while owned,
  duplicate slot release, FIFO bypass, stale tombstone revival, and forged
  match/unsolicited/duplicate/reordered/stale dispositions.
- Reject construction, cloning, copying, rebinding, or direct promotion of
  `ShutdownIntent`, `PublishedPeerStreamHighWater`, `GoawayOutput`,
  `SentGoawayCutoff`, `PeerVisibleCutoff`, fatal-cause rank/ordinal, and graceful
  timer evidence. Reject caller-selected final cutoff, parsed/allocated stream
  used as processed, borrowed debug retained after acceptance, cross-generation
  acknowledgement/timer events, completion before `17 + debug_len`, Frozen
  stage/cutoff/error/debug substitution, increasing-cutoff acceptance, duplicate
  terminal output, early timer arm, forged peer visibility, and cutoff converted
  into replay permission.
- Reject construction or mutation of `ControlServiceProfile` after validation,
  scheduler class/enqueue/generation keys, bypass/deadline state,
  `ControlDisposition`, and fatal-cleanup authority. Reject zero service bounds,
  caller-selected eligibility/ranking, caller time before AckEligible, direct
  Complete/Abandoned promotion, semantic hooks for abandoned records, duplicate
  release, stale-token revival, and any output offer after fatal commitment.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Compile-fail state and lifetime tests and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Compile-fail state and lifetime tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.196.0 (Adversarial and stateful fuzz campaign) still passes; no behavior assigned to v0.198.0 (Long-running soak and exhaustion campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.197.0 implementation stop reached. Run pentest for this exact commit.`

### v0.198.0 — Long-running soak and exhaustion campaign

Status: planned

#### Goal

Deliver **Long-running soak and exhaustion campaign** as the sole primary capability in this stop. It builds
on v0.197.0 (Compile-fail state and lifetime tests) and must be independently trustworthy before v0.199.0 (Role and API conformance audit and pentest) begins.

#### Deliverables

- HTTP/1.0 soak extension: cycle initial/successor completion-generation reservation, abandonment, slot reuse, stale interrupt replay, and every resolution/interrupt pair across saturation; repeatedly mutate commands between reason-only retries, destroy/recreate attempt cursors, and run every charged/processed split through maximum fragmented methods/targets/fields/output and early rejection until cumulative exhaustion. Require no cursor escape/skipped validation, permit/receipt confusion, stale/reused work authority, unused-unit reuse/refund, planned-progress advancement, free retry/rescan, quadratic growth, or accounting drift.
- Acceptance contract: Soak long-lived HTTP/1 and HTTP/2 connections through counter saturation, stream/table generation wrap boundaries, repeated cancellation, flow-control stalls, mandatory-control backpressure, flood refill, and caller-capacity exhaustion; memory/storage remains flat, work stays within profile, and shutdown completes within bounded steps.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Long-running soak and exhaustion campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Run repeated HTTP/1.0 admission/normal-success/cancellation/parse-failure/transport-failure/connection-close cycles through every reclaimable-capacity high-water mark; require exchange/correlation/parser/event/output leases and unused parser-work reserve to return exactly once to the original caller pools, while reuse-ledger decrements, request-count debits, consumed parser work, and admission-work charges never return. Inject duplicate and stale generation-bound cleanup plus stale permit-deadline expiry throughout; require no later-generation release/close, no capacity decay or growth, and no hidden storage leak under `LastUseMustClose` delayed server responses.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Long-running soak and exhaustion campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.197.0 (Compile-fail state and lifetime tests) still passes; no behavior assigned to v0.199.0 (Role and API conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.198.0 implementation stop reached. Run pentest for this exact commit.`

### v0.199.0 — Role and API conformance audit and pentest

Status: planned

#### Goal

Deliver **Role and API conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.198.0 (Long-running soak and exhaustion campaign) and must be independently trustworthy before v0.200.0 (Standard blocking-stream adapter) begins.

#### Deliverables

- HTTP/1.0 role extension: neither role may forge/reserve a completion binding, collapse resolution with interrupt, store a caller-controlled final state, retain attempt cursors/command borrows in reason-only outcomes, derive units by traversal, obtain work permits/turn receipts into authority, or control cursor progress. Pentest corrected/mutated commands after rejection/capacity, cursor escape, retry undercharging, permit duplication/staleness/cross-attempt use, receipt misuse, processed-over-charged input, unused-unit reuse, early-rejection refund, planned-progress movement, retry bypass, and fragmentation amplification.
- Acceptance contract: Audit client, origin, intermediary, proxy, gateway, tunnel, HTTP/0.9, HTTP/1, and HTTP/2 public APIs against their capability matrix; prove no role can construct an unauthorized target, field, retry, transition, push, coalescing, or close action. In particular, prove HTTP/1.0 client request and delayed origin response builders consume the same sealed `Http10LocalPersistenceMode`, no server response is required at request admission, no public API exposes/duplicates the permit deadline or cleanup authority, and terminal cleanup cannot refund accounting or retain caller storage. Then pentest the frozen role surface and close every critical/high finding.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Role and API conformance audit and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases. Cross `Negotiable` and `LastUseMustClose` through client, origin, proxy-upstream, and existing-private-head builder timing; attempt deadline, cleanup, reservation, and later-generation forgeries; require identical mandatory-close authority, exact role-feasible timing, exactly-once reclamation, and irreversible accounting.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role and API conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.198.0 (Long-running soak and exhaustion campaign) still passes; no behavior assigned to v0.200.0 (Standard blocking-stream adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.199.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence

Phase contract: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.

### v0.200.0 — Standard blocking-stream adapter

Status: planned

#### Goal

Deliver **Standard blocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.199.0 (Role and API conformance audit and pentest) and must be independently trustworthy before v0.201.0 (Standard nonblocking-stream adapter) begins.

#### Deliverables

- Acceptance contract: Map short reads/writes, interruption, clean/truncated EOF, scalar/vectored operation, cancellation, partial output, and mandatory-close actions without hidden buffering or protocol reinterpretation.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard blocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.199.0 (Role and API conformance audit and pentest) still passes; no behavior assigned to v0.201.0 (Standard nonblocking-stream adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.200.0 implementation stop reached. Run pentest for this exact commit.`

### v0.201.0 — Standard nonblocking-stream adapter

Status: planned

#### Goal

Deliver **Standard nonblocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.200.0 (Standard blocking-stream adapter) and must be independently trustworthy before v0.202.0 (Brynja TLS provider contract and admission review) begins.

#### Deliverables

- Acceptance contract: Map WouldBlock, spurious/edge/level readiness, wake coalescing, interest changes, partial I/O, cancellation, EOF, and optional vectored I/O with scalar fallback and no reentrant engine calls.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard nonblocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.200.0 (Standard blocking-stream adapter) still passes; no behavior assigned to v0.202.0 (Brynja TLS provider contract and admission review) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.201.0 implementation stop reached. Run pentest for this exact commit.`

### v0.202.0 — Brynja TLS provider contract and admission review

Status: planned

#### Goal

Deliver **Brynja TLS provider contract and admission review** as the sole primary capability in this stop. It builds
on v0.201.0 (Standard nonblocking-stream adapter) and must be independently trustworthy before v0.203.0 (Separate vef-brynja adapter crate) begins.

#### Deliverables

- Acceptance contract: Require Brynja to publish ALPN only after handshake success plus TLS version/cipher, compression/renegotiation status, certificate/SNI validation outcome, authenticated peer identity, resumption identity, early-data state, close_notify/fatal-alert/EOF state, and bounded nonblocking progress; missing metadata blocks admission.
- Require an explicit Brynja capability/result contract for
  `EarlyFinalTransportAction`: sealing future HTTP writes while continuing
  bounded response reads, initiating/sending `close_notify`, and immediate
  transport abort/close are distinct. Never model TLS as supporting TCP
  write-half-close, and no action can restore HTTP connection reuse.
- Verification contract: test both actions across write/read readiness,
  close_notify send/receive, fatal alert, EOF, cancellation, missing capability,
  and bounded-drain exhaustion; the provider must never claim TCP half-close or
  reuse.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Brynja TLS provider contract and admission review contract and all previously implemented relevant behavior have
reproducible evidence; v0.201.0 (Standard nonblocking-stream adapter) still passes; no behavior assigned to v0.203.0 (Separate vef-brynja adapter crate) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.202.0 implementation stop reached. Run pentest for this exact commit.`

### v0.203.0 — Separate vef-brynja adapter crate

Status: planned

#### Goal

Deliver **Separate vef-brynja adapter crate** as the sole primary capability in this stop. It builds
on v0.202.0 (Brynja TLS provider contract and admission review) and must be independently trustworthy before v0.204.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) begins.

#### Deliverables

- Acceptance contract: Map every admitted Brynja handshake/progress/alert/EOF metadata state into vef-io capabilities and typed TLS outcomes plus a generation/connection-bound TrustedRequestContext carrying authenticated transport-security state and any configured fixed/trusted-gateway scheme; reject missing, stale, or conflicting context and never infer security from socket/runtime types, hidden buffering, reentrancy, protocol fallback, or dependency leakage into protocol crates.
- Map `SealHttpOutputAndDrainResponse` to rejection of all later HTTP output
  while bounded TLS record processing may continue response input, followed by
  explicit TLS close; map `CloseTransportNow` to the provider's immediate
  abort/close path. Preserve the early-final request generation and permanent
  non-reuse across readiness, close_notify, fatal alert, EOF, and cancellation;
  never translate either action into a fabricated TCP half-close.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test the adapter mapping across every partial HTTP-output prefix, response
  input split, WouldBlock wake order, close_notify/fatal/EOF race, drain budget,
  cancellation, and generation reuse; prove no later HTTP output, fabricated
  half-close, successor, or restored reuse.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-brynja adapter crate contract and all previously implemented relevant behavior have
reproducible evidence; v0.202.0 (Brynja TLS provider contract and admission review) still passes; no behavior assigned to v0.204.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.203.0 implementation stop reached. Run pentest for this exact commit.`

### v0.204.0 — HTTP/2 TLS admission prerequisites and authenticated metadata

Status: planned

#### Goal

Deliver **HTTP/2 TLS admission prerequisites and authenticated metadata** as the sole primary capability in this stop. It builds
on v0.203.0 (Separate vef-brynja adapter crate) and must be independently trustworthy before v0.205.0 (TLS transport termination, resumption, alert, and EOF mapping) begins.

#### Deliverables

- Acceptance contract: Admit HTTP/2 only after handshake-success ALPN; require TLS 1.2+, reject prohibited TLS 1.2 suites, compression, and renegotiation; consume provider-supplied certificate/SNI validation, identity, session-resumption, and early-data state without inference.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 TLS admission prerequisites and authenticated metadata contract and all previously implemented relevant behavior have
reproducible evidence; v0.203.0 (Separate vef-brynja adapter crate) still passes; no behavior assigned to v0.205.0 (TLS transport termination, resumption, alert, and EOF mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.204.0 implementation stop reached. Run pentest for this exact commit.`

### v0.205.0 — TLS transport termination, resumption, alert, and EOF mapping

Status: planned

#### Goal

Deliver **TLS transport termination, resumption, alert, and EOF mapping** as the sole primary capability in this stop. It builds
on v0.204.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) and must be independently trustworthy before v0.206.0 (TLS 1.3 early-data prohibition and close semantics) begins.

#### Deliverables

- Acceptance contract: Map authenticated resumption identity, fatal alerts, close_notify, clean EOF, truncation, half-close, and transport failure into distinct typed outcomes; preserve early-data state separately even though 1.0 rejects its use. For a live HTTP/1 bridge transition, map them without collapse to `PreActiveTerminalCause::{PlainTcpEof, TlsCloseNotify, TlsTruncationEof, FatalTlsAlert, TransportReset, TransportFailure, Cancellation}`, retaining the immutable first cause and allowing terminal-only ownership when no over-read bytes exist.
- Integrate the v0.54.0 `EarlyFinalTransportAction` mapping: bounded
  seal-output-and-drain ends in an explicit TLS close_notify/close outcome,
  immediate close selects the provider abort/close outcome, and peer
  close_notify/EOF/fatal alert while draining terminates the action once.
  TLS half-close terminology cannot grant new HTTP output or reuse.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Cross both early-final transport actions with local/peer close_notify, fatal
  alert, clean EOF, truncation, cancellation, write closure, and bounded drain;
  require one typed terminal outcome and permanent rejection of HTTP output/
  reuse.
- Cross every TLS/transport outcome into a PendingHttp1Transition with no
  over-read, empty/absent over-read after a valid success, and nonempty
  over-read; prove clean EOF, close_notify, truncation EOF, fatal alert, reset,
  generic failure, and cancellation remain distinct, first-cause immutable,
  and close_notify never grants TCP half-close.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TLS transport termination, resumption, alert, and EOF mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.204.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) still passes; no behavior assigned to v0.206.0 (TLS 1.3 early-data prohibition and close semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.205.0 implementation stop reached. Run pentest for this exact commit.`

### v0.206.0 — TLS 1.3 early-data prohibition and close semantics

Status: planned

#### Goal

Deliver **TLS 1.3 early-data prohibition and close semantics** as the sole primary capability in this stop. It builds
on v0.205.0 (TLS transport termination, resumption, alert, and EOF mapping) and must be independently trustworthy before v0.207.0 (Aesynx fixed-memory capability profile) begins.

#### Deliverables

- Acceptance contract: Reject offered, accepted, or replayed TLS early data before an HTTP engine consumes request bytes; keep early-data state observable in diagnostics, require a fresh post-handshake request path, and map close_notify, fatal alert, truncation, cancellation, and EOF distinctly.
- Prove both early-final transport actions and every close_notify/EOF/fatal
  outcome permanently retain non-reuse and cannot revive the suppressed
  request, accept a successor, or carry a 417 retry on the closed generation.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Replay both early-final actions through every TLS terminal outcome and attempt
  suppressed-request revival, successor admission, same-generation 417 retry,
  and connection reuse; all attempts remain rejected.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TLS 1.3 early-data prohibition and close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.205.0 (TLS transport termination, resumption, alert, and EOF mapping) still passes; no behavior assigned to v0.207.0 (Aesynx fixed-memory capability profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.206.0 implementation stop reached. Run pentest for this exact commit.`

### v0.207.0 — Aesynx fixed-memory capability profile

Status: planned

#### Goal

Deliver **Aesynx fixed-memory capability profile** as the sole primary capability in this stop. It builds
on v0.206.0 (TLS 1.3 early-data prohibition and close semantics) and must be independently trustworthy before v0.208.0 (Aesynx transport and readiness adapter) begins.

#### Deliverables

- Acceptance contract: Publish aligned arena sizes, buffer ownership, maximum events/streams/control output, scalar and optional scatter-gather capabilities, cancellation slots, and failure behavior when static capacity is insufficient.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx fixed-memory capability profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.206.0 (TLS 1.3 early-data prohibition and close semantics) still passes; no behavior assigned to v0.208.0 (Aesynx transport and readiness adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.207.0 implementation stop reached. Run pentest for this exact commit.`

### v0.208.0 — Aesynx transport and readiness adapter

Status: planned

#### Goal

Deliver **Aesynx transport and readiness adapter** as the sole primary capability in this stop. It builds
on v0.207.0 (Aesynx fixed-memory capability profile) and must be independently trustworthy before v0.209.0 (Aesynx timer and deadline adapter) begins.

#### Deliverables

- Acceptance contract: Prove short I/O, WouldBlock, spurious edge/level readiness, wake coalescing, EOF/starvation distinction, alignment, cancellation, and scalar fallback against the fixed-memory profile; inject a generation/connection-bound TrustedRequestContext with explicit configured scheme/gateway and authenticated transport-security capability, reject stale/conflicting metadata, and never infer TLS from Aesynx handle or socket types; implement the optional v0.157.4 civil-time provider only when the platform exposes a trusted complete UTC instant from an RTC/time service, otherwise return `CivilTimeEvidence::Unavailable`, never derive civil time from monotonic ticks.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions; test trusted RTC evidence, absent/untrusted RTC Unavailable evidence, stale generation rejection, and strict civil-versus-monotonic separation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx transport and readiness adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.207.0 (Aesynx fixed-memory capability profile) still passes; no behavior assigned to v0.209.0 (Aesynx timer and deadline adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.208.0 implementation stop reached. Run pentest for this exact commit.`

### v0.209.0 — Aesynx timer and deadline adapter

Status: planned

#### Goal

Deliver **Aesynx timer and deadline adapter** as the sole primary capability in this stop. It builds
on v0.208.0 (Aesynx transport and readiness adapter) and must be independently trustworthy before v0.210.0 (Aesynx kernel integration tests) begins.

#### Deliverables

- Acceptance contract: Map monotonic ticks with checked wrap/deadline arithmetic, wake coalescing, cancellation races, expired-before-poll ordering, and no wall-clock dependency.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx timer and deadline adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.208.0 (Aesynx transport and readiness adapter) still passes; no behavior assigned to v0.210.0 (Aesynx kernel integration tests) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.209.0 implementation stop reached. Run pentest for this exact commit.`

### v0.210.0 — Aesynx kernel integration tests

Status: planned

#### Goal

Deliver **Aesynx kernel integration tests** as the sole primary capability in this stop. It builds
on v0.209.0 (Aesynx timer and deadline adapter) and must be independently trustworthy before v0.211.0 (Deterministic CPU, stack, code-size, and amplification budgets) begins.

#### Deliverables

- Acceptance contract: The Aesynx kernel integration tests outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx kernel integration tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.209.0 (Aesynx timer and deadline adapter) still passes; no behavior assigned to v0.211.0 (Deterministic CPU, stack, code-size, and amplification budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.210.0 implementation stop reached. Run pentest for this exact commit.`

### v0.211.0 — Deterministic CPU, stack, code-size, and amplification budgets

Status: planned

#### Goal

Deliver **Deterministic CPU, stack, code-size, and amplification budgets** as the sole primary capability in this stop. It builds
on v0.210.0 (Aesynx kernel integration tests) and must be independently trustworthy before v0.212.0 (32-bit target campaign) begins.

#### Deliverables

- HTTP/1.0 sizing extension: independently bound pre-Active common/cause binding reservation, completion-generation domain, resolution/interrupt records and exhaustive final-state computation, revoked identity, one command-borrow-bound attempt and its cursors, granular kinds/spec units/base/per-unit calculation, private work permit, diagnostic receipt, O(1) stored lengths/counts, actual-progress chunks, fragmentation, and retry rescans. No stored planned-state record or cross-call cursor exists; duplicate binding, identity, spec, cursor, work permit, receipt-as-authority, or reuse-permit ownership is forbidden.
- Acceptance contract: Measure maximum stack and minimal-feature code size, prohibit peer-controlled recursion, cap work per byte/frame and amplification, detect quadratic work, price one-byte fragmentation, verify scheduler fairness, and document Aesynx arena sizing. Replay `OutboundFrameArena` slot-byte and queue-entry exhaustion independently, every supported nonzero `max_outbound_frame_payload`, and peer MAX_FRAME_SIZE up to 16,777,215 while proving bounded local storage, typed local backpressure, no alias/reuse, and no loss of committed field-block progress.
- Size each profile for encoder and decoder caller arenas, checked logical `physical_capacity` after metadata/alignment/entry overhead, selected/profile bounds, initial 4096 decoder safety, and every dynamic-table entry/eviction case. Separately size `EncoderTableLimits`, per-frame ceiling snapshots/optional selected deltas, SETTINGS/ACK records, one connection debt, at most one Private lease or transferred debt, FIFO metadata, and cleanup; peer `u32::MAX` never requires equivalent storage, mixed entries cannot multiply records unboundedly, and backpressured prefixes retain bounded ownership. Prove all `u32`/`usize` conversions and `9 + payload` arithmetic at target boundaries.
- Independently size outbound SETTINGS ordered-entry storage, checked
  `9 + 6 * entry_count` frame slots, queue entries, ReservedPrivate/Frozen
  records, pre-reserved future-ACK FIFO slots, commit-plan snapshots, timeout
  generations, and strict committed FIFO metadata. Prove initial activation and
  the configured number of later transactions need no allocation at final-byte
  commitment, all multiplication/addition is checked on 32-/64-bit targets,
  and terminal cleanup releases each reserved/committed owner exactly once.
- Prove the causal combined operation requires no hidden input buffering:
  input-only delivery with a live token and combined invalid acknowledgement
  both leave input caller-owned and wholly unconsumed, so enforcing
  `DriverCommitOrderViolation` adds only fixed token/generation metadata within
  existing connection profiles and no peer-content classification storage.
- Independently size each configured early-final request's framing/progress/
  disposition record, legality inputs, continuation deadline/work budget,
  typed transport action, and held body/zero-chunk/trailer/successor ownership.
  Size the one bounded version-neutral `ValidatedConnectionOptions` ordered-
  token/nominated-field record and exact version/generation bindings once for
  HTTP/1.1 persistence/close-proof/Upgrade, HTTP/1.0 default-close/
  `Http10PersistenceDisposition`/`ValidatedHttp10KeepAlive`/
  `CommittedHttp10KeepAliveHead`/`CorrelatedHttp10KeepAliveRequest`/
  `Http10ReuseLedger`/`Http10ReuseResolutionRecord`/
  `Http10TerminalDecision`/`Http10ReusePermit`, newest-
  message revocation, per-hop signal pairing, response-correlation owner, sole
  mutable future-admission count, immutable ActiveExchange snapshot with
  pre-reserved completion binding, fact-only exhaustive final-state derivation,
  one-call command-borrow-bound cursors, O(1) unit metadata, private linear work
  permits, diagnostic receipts and actual-progress advancement,
  `Http10LocalPersistenceMode`, exactly-once resolution/completion state, permit-
  exclusive deadline owner, bounded `Http10NextExchangeReservation` with
  deadline snapshot, exchange/correlation/parser/event/output leases, count/
  work charges and parser-work reserve, generation-bound cleanup authority and
  terminal reclamation state, separate reclaimable/irreversible accounting,
  separate resolution and successor results/reasons/ownership, exact
  bodyless/fixed MessageCommitted gate plus negative framing state, checked
  next-generation exhaustion owner, output-phase persistence-loss action, and
  either-version intermediary stripping.
  Size the role-specific `UnsupportedHttp10ConnectDisposition`, original
  optimistic-byte discard owner, exact immutable 70-byte mandatory 501 record,
  acknowledgement cursor, `Flush501ThenClose`/`CloseTransportNow`, later-input-
  unconsumed state, and zero-partial close fallback. Size each
  bridge generation's transaction, four phase-capability records,
  five-way input provenance, exact close-proof and optimistic-permit records,
  premature-input latch, one-shot wire-commit evidence, reserved/consumed
  activation-permit slot, latch snapshot and frozen-generation binding,
  transfer/discard disposition, downstream output/suffix/reset reservation,
  and lease metadata; each HTTP/1 leg's one optional bounded over-read store
  plus PendingHttp1Transition bridge/leg/exchange/transport generations and
  first plain-EOF/close_notify/TLS-truncation/fatal-alert/reset/transport-
  failure/cancellation cause; and the existing HTTP/2 PendingConnect/
  AwaitingBridgeActivation store plus linear lease/range/generation/padding/
  ReceiveCredit/pending-FIN/first-terminal-cause metadata plus stream-local
  premature-DATA disposition separately—never two generic bridge stores.
  Include upstream/
  downstream output records, inbound terminal-validation evidence, HTTP/2
  outbound field blocks, terminal actions, and cleanup before upstream
  exposure. Exhaust each
  capacity one unit short and prove no unbounded retention, duplicate bytes/
  credit, downstream success exposure, phase promotion, retry/successor
  admission, or fallible Active/terminal cleanup step.
- Size one connection and the configured maximum stream `ReceiveCredit`
  ledgers, independent bounded private/frozen WINDOW_UPDATE records, their
  exact 13-byte storage, generations, counters, and reserved queue entries.
  Prove padding-only and one-octet reclamation cannot force unbounded output,
  frozen prefixes retain bounded ownership, and all coalescing, `i32`/`u32`,
  31-bit-window, and profile-count arithmetic is checked on 32- and 64-bit
  targets.
- Size the inbound PING FIFO, owned eight-byte payloads, frozen 17-byte ACK
  records, output slots/tokens, local correlation table, and bounded tombstone
  horizon independently for every resource profile. Prove identical payloads
  consume distinct bounded obligations, peer input storage is released after
  copy, correlation-key generation/wrap is checked, rate limits bound priority
  starvation/amplification, and every partial prefix retains only
  profile-bounded connection-owned state.
- Size the guaranteed 17-byte GOAWAY minimum slot independently from optional
  outbound debug, the inbound retained-debug cap/drain scratch, maximum Frozen
  record, shutdown/high-water/cutoff/timer ledgers, fatal primary plus bounded
  secondary causes, and one successor reservation. Prove checked
  `17 + debug_len` arithmetic, maximum-prefix ownership, optional-debug
  exhaustion fallback, constant-bounded precedence work, no duplicate terminal
  amplification, and profile-bounded cleanup on 32- and 64-bit targets.
- Size the global scheduler's fixed class heads, FIFO ordinals/generations,
  positive saturating consecutive-PING/bypass/deadline counters, and
  `ControlDisposition` cleanup metadata for every mandatory queue. Prove the
  configured service bound requires no peer-sized heap or timer structure,
  simultaneous fatal cleanup is linear in fixed admitted capacity, counters
  cannot wrap into priority changes, and every owner is released once within
  the existing profile-bound storage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic CPU, stack, code-size, and amplification budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.210.0 (Aesynx kernel integration tests) still passes; no behavior assigned to v0.212.0 (32-bit target campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.211.0 implementation stop reached. Run pentest for this exact commit.`

### v0.212.0 — 32-bit target campaign

Status: planned

#### Goal

Deliver **32-bit target campaign** as the sole primary capability in this stop. It builds
on v0.211.0 (Deterministic CPU, stack, code-size, and amplification budgets) and must be independently trustworthy before v0.213.0 (Big-endian target campaign) begins.

#### Deliverables

- Acceptance contract: The 32-bit target campaign outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test 32-bit target campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 32-bit target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.211.0 (Deterministic CPU, stack, code-size, and amplification budgets) still passes; no behavior assigned to v0.213.0 (Big-endian target campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.212.0 implementation stop reached. Run pentest for this exact commit.`

### v0.213.0 — Big-endian target campaign

Status: planned

#### Goal

Deliver **Big-endian target campaign** as the sole primary capability in this stop. It builds
on v0.212.0 (32-bit target campaign) and must be independently trustworthy before v0.214.0 (Cross-architecture campaign) begins.

#### Deliverables

- Acceptance contract: The Big-endian target campaign outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Big-endian target campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Big-endian target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.212.0 (32-bit target campaign) still passes; no behavior assigned to v0.214.0 (Cross-architecture campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.213.0 implementation stop reached. Run pentest for this exact commit.`

### v0.214.0 — Cross-architecture campaign

Status: planned

#### Goal

Deliver **Cross-architecture campaign** as the sole primary capability in this stop. It builds
on v0.213.0 (Big-endian target campaign) and must be independently trustworthy before v0.215.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) begins.

#### Deliverables

- Acceptance contract: The Cross-architecture campaign outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cross-architecture campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cross-architecture campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.213.0 (Big-endian target campaign) still passes; no behavior assigned to v0.215.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.214.0 implementation stop reached. Run pentest for this exact commit.`

### v0.215.0 — Linux, Windows, BSD, macOS, Android, and iOS matrix

Status: planned

#### Goal

Deliver **Linux, Windows, BSD, macOS, Android, and iOS matrix** as the sole primary capability in this stop. It builds
on v0.214.0 (Cross-architecture campaign) and must be independently trustworthy before v0.216.0 (Kani shared-core proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: The Linux, Windows, BSD, macOS, Android, and iOS matrix outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Linux, Windows, BSD, macOS, Android, and iOS matrix and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Linux, Windows, BSD, macOS, Android, and iOS matrix contract and all previously implemented relevant behavior have
reproducible evidence; v0.214.0 (Cross-architecture campaign) still passes; no behavior assigned to v0.216.0 (Kani shared-core proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.215.0 implementation stop reached. Run pentest for this exact commit.`

### v0.216.0 — Kani shared-core proof replay and expansion

Status: planned

#### Goal

Deliver **Kani shared-core proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.215.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) and must be independently trustworthy before v0.217.0 (Kani HTTP/1 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: The Kani shared-core proof replay and expansion outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Kani shared-core proof replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani shared-core proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.215.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) still passes; no behavior assigned to v0.217.0 (Kani HTTP/1 proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.216.0 implementation stop reached. Run pentest for this exact commit.`

### v0.217.0 — Kani HTTP/1 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/1 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.216.0 (Kani shared-core proof replay and expansion) and must be independently trustworthy before v0.218.0 (Kani HPACK proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: The Kani HTTP/1 proof replay and expansion outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/1 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.216.0 (Kani shared-core proof replay and expansion) still passes; no behavior assigned to v0.218.0 (Kani HPACK proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.217.0 implementation stop reached. Run pentest for this exact commit.`

### v0.218.0 — Kani HPACK proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HPACK proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.217.0 (Kani HTTP/1 proof replay and expansion) and must be independently trustworthy before v0.219.0 (Kani HTTP/2 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: The Kani HPACK proof replay and expansion outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Kani HPACK proof replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HPACK proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.217.0 (Kani HTTP/1 proof replay and expansion) still passes; no behavior assigned to v0.219.0 (Kani HTTP/2 proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.218.0 implementation stop reached. Run pentest for this exact commit.`

### v0.219.0 — Kani HTTP/2 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/2 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.218.0 (Kani HPACK proof replay and expansion) and must be independently trustworthy before v0.220.0 (Stateful cargo-fuzz replay and expansion) begins.

#### Deliverables

- Acceptance contract: The Kani HTTP/2 proof replay and expansion outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/2 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.218.0 (Kani HPACK proof replay and expansion) still passes; no behavior assigned to v0.220.0 (Stateful cargo-fuzz replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.219.0 implementation stop reached. Run pentest for this exact commit.`

### v0.220.0 — Stateful cargo-fuzz replay and expansion

Status: planned

#### Goal

Deliver **Stateful cargo-fuzz replay and expansion** as the sole primary capability in this stop. It builds
on v0.219.0 (Kani HTTP/2 proof replay and expansion) and must be independently trustworthy before v0.221.0 (Differential and interoperability campaign) begins.

#### Deliverables

- Acceptance contract: The Stateful cargo-fuzz replay and expansion outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Stateful cargo-fuzz replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stateful cargo-fuzz replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.219.0 (Kani HTTP/2 proof replay and expansion) still passes; no behavior assigned to v0.221.0 (Differential and interoperability campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.220.0 implementation stop reached. Run pentest for this exact commit.`

### v0.221.0 — Differential and interoperability campaign

Status: planned

#### Goal

Deliver **Differential and interoperability campaign** as the sole primary capability in this stop. It builds
on v0.220.0 (Stateful cargo-fuzz replay and expansion) and must be independently trustworthy before v0.222.0 (Whole-project conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: The Differential and interoperability campaign outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Differential and interoperability campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Differential and interoperability campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.220.0 (Stateful cargo-fuzz replay and expansion) still passes; no behavior assigned to v0.222.0 (Whole-project conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.221.0 implementation stop reached. Run pentest for this exact commit.`

### v0.222.0 — Whole-project conformance audit and pentest

Status: planned

#### Goal

Deliver **Whole-project conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.221.0 (Differential and interoperability campaign) and must be independently trustworthy before v0.223.0 (Independent security audit) begins.

#### Deliverables

- Acceptance contract: The Whole-project conformance audit and pentest outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Whole-project conformance audit and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Whole-project conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.221.0 (Differential and interoperability campaign) still passes; no behavior assigned to v0.223.0 (Independent security audit) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.222.0 implementation stop reached. Run pentest for this exact commit.`

### v0.223.0 — Independent security audit

Status: planned

#### Goal

Deliver **Independent security audit** as the sole primary capability in this stop. It builds
on v0.222.0 (Whole-project conformance audit and pentest) and must be independently trustworthy before v0.224.0 (Audit remediation and API freeze) begins.

#### Deliverables

- Acceptance contract: The Independent security audit outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Independent security audit and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent security audit contract and all previously implemented relevant behavior have
reproducible evidence; v0.222.0 (Whole-project conformance audit and pentest) still passes; no behavior assigned to v0.224.0 (Audit remediation and API freeze) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.223.0 implementation stop reached. Run pentest for this exact commit.`

### v0.224.0 — Audit remediation and API freeze

Status: planned

#### Goal

Deliver **Audit remediation and API freeze** as the sole primary capability in this stop. It builds
on v0.223.0 (Independent security audit) and must be independently trustworthy before v0.225.0 (Documentation, packaging, SBOM, provenance, and RC readiness) begins.

#### Deliverables

- Acceptance contract: The Audit remediation and API freeze outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Audit remediation and API freeze and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Audit remediation and API freeze contract and all previously implemented relevant behavior have
reproducible evidence; v0.223.0 (Independent security audit) still passes; no behavior assigned to v0.225.0 (Documentation, packaging, SBOM, provenance, and RC readiness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.224.0 implementation stop reached. Run pentest for this exact commit.`

### v0.225.0 — Documentation, packaging, SBOM, provenance, and RC readiness

Status: planned

#### Goal

Deliver **Documentation, packaging, SBOM, provenance, and RC readiness** as the sole primary capability in this stop. It builds
on v0.224.0 (Audit remediation and API freeze) and must be independently trustworthy before the 1.0 release-candidate sequence begins.

#### Deliverables

- Acceptance contract: The Documentation, packaging, SBOM, provenance, and RC readiness outcome must define reproducible target/tool inputs, deterministic pass/fail evidence, bounded resources and time, cancellation/failure handling, artifact provenance, and exact release-blocking criteria; it cannot weaken protocol invariants or claim unsupported targets, audits, or coverage.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Documentation, packaging, SBOM, provenance, and RC readiness contract and all previously implemented relevant behavior have
reproducible evidence; v0.224.0 (Audit remediation and API freeze) still passes; no behavior assigned to the 1.0 release-candidate sequence is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.225.0 implementation stop reached. Run pentest for this exact commit.`

## 1.0 release candidates

### v1.0.0-rc.1

Status: planned

Goal: freeze public APIs and expose the candidate to public interoperability,
security, usability, resource, and documentation review.

Deliverables: API freeze, migration guidance, package dry runs, RFC/errata
coverage, platform/resource matrices, limitations, SBOM, provenance, and
complete release evidence.

Verification: replay every fuzz/model/resource harness, repository gate,
independent multi-implementation interop, manual audit, and exact-commit
pentest.

Exit criteria: no new features and all evidence reproducible.
`1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0-rc.2

Status: planned

Goal: remediate RC1 findings without expanding scope.

Deliverables: fixes, regression tests, final source/RFC review, MSRV/target and
resource declarations, and refreshed evidence.

Verification: repeat every fuzz, model, pentest, conformance, interop,
portability, resource, package, SBOM, and provenance gate.

Exit criteria: no unresolved critical/high findings or unreviewed behavior.
`1.0.0-rc.2 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0

Status: planned

Goal: publish the first serious production-ready VEF HTTP crate.

Release only when applicable requirements are verified, capacity/error
dispositions are unambiguous, resource ceilings pass, fixed storage works
without allocation, HTTP/1 framing/body/transition ownership is deterministic,
HPACK output/input state is synchronized, HTTP/2 activation/publication/
SETTINGS/flow/cancellation/shutdown evidence is exhaustive, intermediary and
translation matrices pass, TLS admission/termination is explicit, every role
and platform claim is verified, independent-audit remediation is complete, and
HTTP/3 remains out of scope.
