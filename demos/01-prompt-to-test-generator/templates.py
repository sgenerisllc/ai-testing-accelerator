"""Playwright test templates keyed by scenario archetype."""

LOGIN_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
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
'''

SIGNUP_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
    page.goto("https://example.com/signup")

    page.get_by_label("First name").fill("Alex")
    page.get_by_label("Last name").fill("Tester")
    page.get_by_label("Email").fill("alex.tester@example.com")
    page.get_by_label("Password", exact=True).fill("Str0ng!Pass")
    page.get_by_label("Confirm password").fill("Str0ng!Pass")

    page.get_by_role("checkbox", name="I agree to the terms").check()
    page.get_by_role("button", name="Create account").click()

    expect(page.get_by_text("Verify your email")).to_be_visible()
'''

CHECKOUT_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
    page.goto("https://example.com/cart")

    # Step 1: Verify cart contents
    expect(page.get_by_test_id("cart-line-item")).to_have_count(1)

    # Step 2: Proceed to checkout
    page.get_by_role("button", name="Proceed to checkout").click()

    # Step 3: Fill shipping details
    page.get_by_label("Full name").fill("Alex Tester")
    page.get_by_label("Address").fill("123 Test St")
    page.get_by_label("City").fill("Testville")
    page.get_by_label("ZIP").fill("12345")

    # Step 4: Enter payment details
    page.get_by_label("Card number").fill("4242 4242 4242 4242")
    page.get_by_label("Expiry").fill("12/30")
    page.get_by_label("CVC").fill("123")

    # Step 5: Place the order
    page.get_by_role("button", name="Place order").click()

    # Step 6: Confirm success
    expect(page.get_by_role("heading", name="Order confirmed")).to_be_visible()
    expect(page.get_by_test_id("order-id")).to_be_visible()
'''

SEARCH_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
    page.goto("https://example.com")

    page.get_by_role("searchbox", name="Search").fill("playwright")
    page.get_by_role("searchbox", name="Search").press("Enter")

    results = page.get_by_test_id("search-result")
    expect(results.first).to_be_visible()
    expect(results).to_have_count(10)
'''

PASSWORD_RESET_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
    page.goto("https://example.com/login")

    page.get_by_role("link", name="Forgot password?").click()

    page.get_by_label("Email").fill("user@example.com")
    page.get_by_role("button", name="Send reset link").click()

    expect(page.get_by_text("Check your inbox")).to_be_visible()
'''

GENERIC_TEMPLATE = '''"""
Generated Playwright test: {scenario}
"""
from playwright.sync_api import Page, expect


def test_{func_name}(page: Page) -> None:
    # TODO: Replace with the real entry point for this flow
    page.goto("https://example.com")

    # Step 1: Trigger the primary action
    page.get_by_role("button", name="Start").click()

    # Step 2: Interact with the relevant inputs
    # page.get_by_label("Field name").fill("value")

    # Step 3: Verify the expected outcome
    expect(page.get_by_role("heading")).to_be_visible()
'''
