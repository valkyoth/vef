# GitHub Security Settings

Status: operator checklist

GitHub CodeQL default setup is required. Do not add an advanced CodeQL
workflow while default setup is active.

Before a release:

1. Confirm default setup is active for the default branch.
2. Confirm the latest analysis passed on the implementation and report commits.
3. Require pull-request review for `rfc/`, `spec/`, `security/`, and workflows.
4. Confirm secret scanning, push protection, Dependabot alerts, and private
   vulnerability reporting are enabled where available.
5. Record the settings check in the permanent pentest report.
