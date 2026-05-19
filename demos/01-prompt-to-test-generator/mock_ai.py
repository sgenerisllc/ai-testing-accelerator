"""
Deterministic offline test generator.

Uses keyword pattern matching to produce realistic Playwright test
skeletons without any network or API call. The output is intentionally
high-quality so the demo is impressive on its own.
"""

from __future__ import annotations

import re
from templates import (
    CHECKOUT_TEMPLATE,
    GENERIC_TEMPLATE,
    LOGIN_TEMPLATE,
    PASSWORD_RESET_TEMPLATE,
    SEARCH_TEMPLATE,
    SIGNUP_TEMPLATE,
)

# Pattern matching: (keywords, template)
PATTERNS = [
    (["login", "log in", "sign in", "signin"], LOGIN_TEMPLATE),
    (["signup", "sign up", "register", "registration", "create account"], SIGNUP_TEMPLATE),
    (["checkout", "payment", "purchase", "buy", "cart"], CHECKOUT_TEMPLATE),
    (["search", "filter", "find"], SEARCH_TEMPLATE),
    (["password reset", "forgot password", "reset password"], PASSWORD_RESET_TEMPLATE),
]


def _slugify(scenario: str) -> str:
    """Convert a scenario string into a valid Python function name."""
    slug = re.sub(r"[^a-zA-Z0-9_\s]", "", scenario.lower())
    slug = re.sub(r"\s+", "_", slug.strip())
    return slug[:80]


def _match_template(scenario: str) -> str:
    """Pick the most relevant template based on keywords in the scenario."""
    lower = scenario.lower()
    for keywords, template in PATTERNS:
        if any(kw in lower for kw in keywords):
            return template
    return GENERIC_TEMPLATE


def generate_test_skeleton(scenario: str) -> str:
    """Produce a Playwright test skeleton for the given scenario."""
    template = _match_template(scenario)
    func_name = _slugify(scenario) or "generated_test"
    return template.format(scenario=scenario, func_name=func_name)
