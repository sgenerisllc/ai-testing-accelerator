"""
Generated Playwright test: test user login with valid credentials
"""
from playwright.sync_api import Page, expect


def test_test_user_login_with_valid_credentials(page: Page) -> None:
    # Step 1: Navigate to the application
    page.goto("https://example.com")

    # Step 2: Locate login elements
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_label("Password").fill("secure-password")

    # Step 3: Perform the login action
    page.get_by_role("button", name="Login").click()

    # Step 4: Verify successful outcome
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
    expect(page).to_have_url("https://example.com/dashboard")
