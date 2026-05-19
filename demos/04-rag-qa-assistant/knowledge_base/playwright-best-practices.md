# Playwright Best Practices

## Locator Strategy (in priority order)

1. **`getByRole('button', { name: 'Submit' })`** — accessibility-first, semantic, resilient
2. **`getByLabel('Email')`** — best for form fields
3. **`getByTestId('submit-button')`** — explicit contract with developers
4. **`getByText('Sign in')`** — last resort, breaks on copy changes

Avoid:
- CSS selectors with implementation details (`.MuiButton-root-xyz`)
- XPath
- nth-child positional selectors

## Fixtures

Use Playwright fixtures for shared setup. Common fixtures live in `tests/fixtures/`:

- `authenticatedPage` — page with a logged-in user
- `seededDatabase` — fresh database snapshot
- `mockedAPI` — backend responses stubbed

Fixtures should be composable. Prefer multiple small fixtures over one mega-fixture.

## Waiting

Never use `await page.waitForTimeout(ms)`. Instead:

- `await expect(locator).toBeVisible()` — wait for visibility
- `await expect(locator).toBeEnabled()` — wait for interactivity
- `await page.waitForResponse(...)` — wait for API completion
- `await page.waitForURL(...)` — wait for navigation

## Parallelization

Tests within a file run serially. Tests across files run in parallel. To enable in-file parallelism, use `test.describe.configure({ mode: 'parallel' })`.

Each parallel worker gets its own browser context — no state bleed.

## Network Mocking

For deterministic tests, mock backend calls:

```typescript
await page.route('**/api/users', route =>
  route.fulfill({ json: { users: [...] } })
);
```

Use mocking sparingly in E2E tests. Prefer real backends for true integration coverage.

## Screenshots & Traces

Configure `playwright.config.ts`:

```typescript
use: {
  trace: 'retain-on-failure',
  screenshot: 'only-on-failure',
  video: 'retain-on-failure',
}
```

Traces are invaluable for debugging — view with `npx playwright show-trace trace.zip`.

## Test Organization

```
tests/
├── auth/          # Authentication flows
├── checkout/      # Purchase flows
├── admin/         # Admin panel
├── fixtures/      # Shared fixtures
└── helpers/       # Pure utility functions
```

One spec file per feature. Group related scenarios with `test.describe`.
