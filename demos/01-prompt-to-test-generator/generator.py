"""
Prompt-to-Test Generator CLI.

Converts plain English test scenarios into Playwright test skeletons.
Runs offline by default. Optionally uses OpenAI when OPENAI_API_KEY is set.

Usage:
    python generator.py "test user login with valid credentials"
    python generator.py "verify checkout flow" --out test_checkout.py
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from mock_ai import generate_test_skeleton


def _call_openai(scenario: str, api_key: str) -> str:
    """Optional path: real LLM call. Imported lazily so offline runs need no extras."""
    try:
        from openai import OpenAI  # type: ignore
    except ImportError:
        print("⚠️  openai package not installed. Falling back to offline mode.", file=sys.stderr)
        return generate_test_skeleton(scenario)

    client = OpenAI(api_key=api_key)
    prompt = (
        "Generate a Playwright Python test for the following scenario. "
        "Use sync_api, type hints, and accessibility-first locators "
        "(get_by_role, get_by_label, get_by_test_id). Return only Python code.\n\n"
        f"Scenario: {scenario}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content or generate_test_skeleton(scenario)


def generate(scenario: str) -> str:
    """Generate a Playwright test from a plain English scenario."""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("🤖 Using OpenAI API (set OPENAI_API_KEY to disable)", file=sys.stderr)
        return _call_openai(scenario, api_key)
    print("🔧 Using offline mock generator (set OPENAI_API_KEY for live AI)", file=sys.stderr)
    return generate_test_skeleton(scenario)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Playwright test skeletons from plain English."
    )
    parser.add_argument("scenario", help="Plain English test scenario")
    parser.add_argument(
        "--out",
        type=Path,
        help="Output file path (defaults to stdout)",
    )
    args = parser.parse_args()

    test_code = generate(args.scenario)

    if args.out:
        args.out.write_text(test_code)
        print(f"✅ Generated test written to {args.out}", file=sys.stderr)
    else:
        print(test_code)

    return 0


if __name__ == "__main__":
    sys.exit(main())
