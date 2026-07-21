# VEF Conformance Engineering

Status: foundation contract

VEF does not claim vague “full RFC compliance.” The 1.0 claim is:

> Every identified and applicable MUST and MUST NOT requirement for a declared
> role in the effective specification set is linked to implementation and at
> least one passing conformance test. Every applicable SHOULD and SHOULD NOT is
> implemented or has a reviewed engineering decision.

## Requirement record

Each record under `spec/requirements/` carries:

- stable VEF requirement ID;
- RFC number, section, and paragraph locator;
- requirement level and exact source checksum;
- applicable protocol version and participant roles;
- applicability and security categories;
- implementation paths and symbols;
- positive, negative, fragmentation, adversarial, and interoperability tests;
- status: `unreviewed`, `planned`, `implemented`, `verified`, `not-applicable`,
  or `deviation`;
- reviewed rationale for SHOULD decisions and exclusions;
- applicable verified and unresolved errata.

`implemented` alone never supports a release claim. `verified` requires the
named code and named tests to exist and the release gate to execute them.

## Effective specifications

Documents that update another document are evaluated together. In particular,
RFC 9112 plus RFC 9931 form VEF's effective HTTP/1.1 security baseline.
Obsoleted historical documents remain evidence only for explicitly named
compatibility profiles.

## Generated release evidence

Each release generates role-specific coverage, unimplemented MUST/MUST NOT,
undecided SHOULD/SHOULD NOT, requirement-to-code, requirement-to-test, known
deviation, errata, and security-control reports. Reports bind to the RFC source
checksums and implementation commit.

## Source separation

Immutable RFC copies live under `rfc/`. VEF-authored requirements, decisions,
and generated evidence live under `spec/`. Mutable or redistribution-restricted
references live under ignored `references/private/` or `references/cache/`.
