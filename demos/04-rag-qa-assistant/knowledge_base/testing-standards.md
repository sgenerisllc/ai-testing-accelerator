# Testing Standards

## Quality Bar

Every test must meet these standards before being merged:

- Independent and idempotent (no shared state between tests)
- Deterministic — no `sleep()` calls; use explicit waits
- Self-contained — generates its own data, cleans up after itself
- Fast — under 30 seconds per test where possible
- Readable — a new engineer should understand intent in 30 seconds

## Flaky Test Policy

A test is considered flaky if it fails more than 2% of CI runs in a rolling 7-day window.

When a flaky test is detected:

1. **Hour 1:** Test is auto-quarantined (moved to `tests/quarantine/`) and the CI pipeline continues.
2. **Day 1:** A Jira ticket is opened automatically and assigned to the test owner (per `CODEOWNERS`).
3. **Day 7:** If unfixed, the test is deleted and a follow-up task is created to redesign coverage.

The flaky test policy is non-negotiable. Quarantined tests that linger past 7 days erode CI trust.

## Disabling a Test

You can disable a test temporarily using `test.skip('reason and Jira ticket')`. The skip reason must include:

- Why the test is disabled
- A Jira ticket tracking re-enablement
- Owner name

Tests skipped without a ticket are deleted by the test-hygiene bot weekly.

## Code Review Checklist

Before approving a test PR:

- [ ] Test has a clear, descriptive name
- [ ] Locators use accessibility-first patterns (`getByRole`, `getByLabel`)
- [ ] No hardcoded sleeps
- [ ] Test cleans up its own data
- [ ] Failure messages are actionable

## Coverage Targets

- Smoke suite: 100% of P0 user journeys
- Regression suite: 80% of P0+P1 user journeys
- Unit tests: 70% line coverage for shared utilities

These are minimums. Critical paths (payment, authentication) require 100% coverage.
