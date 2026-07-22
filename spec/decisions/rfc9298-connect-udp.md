# RFC 9298 HTTP/1.1 CONNECT-UDP Applicability

Status: reviewed 1.0 scope decision

RFC 9298 is not applicable to VEF 1.0 because the declared profiles do not
implement HTTP/1.1 CONNECT-UDP. Generic CONNECT, RFC 9931 transition security,
and RFC 8441 extended CONNECT remain independently applicable as recorded in
the requirement manifest.

This decision must be reopened before any HTTP/1.1 CONNECT-UDP API, parser
profile, forwarding behavior, or interoperability claim is added. Reopening
requires a release-plan milestone, requirement extraction, security review,
and tests for capsule/proxy transition boundaries before implementation.
