"""
Self-Healing Locator demo.

Walks through a layered fallback strategy against a static HTML fixture.
Uses only the Python standard library (html.parser) so the demo runs
anywhere with zero external dependencies.

Fallback hierarchy:
    1. Primary CSS selector (id/class)
    2. data-testid attribute
    3. ARIA role + accessible name
    4. Visible text match
    5. AI vision/semantic fallback (stub — show where LLM plugs in)
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


@dataclass
class Element:
    tag: str
    attrs: dict[str, str]
    text: str = ""

    def __str__(self) -> str:
        attr_str = " ".join(f'{k}="{v}"' for k, v in self.attrs.items())
        return f"<{self.tag} {attr_str}>{self.text}</{self.tag}>".strip()


class _SimpleDOM(HTMLParser):
    """Minimal DOM extractor — produces a flat list of interactive elements."""

    INTERACTIVE_TAGS = {"button", "a", "input", "select", "textarea"}

    def __init__(self) -> None:
        super().__init__()
        self.elements: list[Element] = []
        self._current: Element | None = None
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.INTERACTIVE_TAGS:
            self._current = Element(tag=tag, attrs={k: (v or "") for k, v in attrs})
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._current is not None:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._current is not None and tag == self._current.tag:
            self._current.text = "".join(self._buffer).strip()
            self.elements.append(self._current)
            self._current = None
            self._buffer = []


def parse(html: str) -> list[Element]:
    dom = _SimpleDOM()
    dom.feed(html)
    return dom.elements


# ---------- Fallback strategies ---------- #

def try_primary(elements: list[Element], selector: str) -> Element | None:
    """Match #id or .class selectors."""
    if selector.startswith("#"):
        target_id = selector[1:]
        return next((e for e in elements if e.attrs.get("id") == target_id), None)
    if selector.startswith("."):
        target_class = selector[1:]
        return next(
            (e for e in elements if target_class in e.attrs.get("class", "").split()),
            None,
        )
    return None


def try_test_id(elements: list[Element], test_id: str) -> Element | None:
    return next(
        (e for e in elements if e.attrs.get("data-testid") == test_id),
        None,
    )


def try_role_name(elements: list[Element], role: str, name: str) -> Element | None:
    name_lower = name.lower()
    for e in elements:
        # role can be implicit (button tag) or explicit (role attr)
        implicit_role = "button" if e.tag == "button" else "link" if e.tag == "a" else None
        actual_role = e.attrs.get("role") or implicit_role
        if actual_role != role:
            continue
        accessible_name = e.attrs.get("aria-label") or e.text
        if accessible_name.lower() == name_lower:
            return e
    return None


def try_text(elements: list[Element], text: str) -> Element | None:
    text_lower = text.lower()
    return next((e for e in elements if text_lower in e.text.lower()), None)


def ai_fallback(elements: list[Element], description: str) -> Element | None:
    """Stub: where an LLM/vision model would plug in. Offline returns None."""
    # In production: send screenshot + DOM to a vision-capable model and ask which element matches.
    return None


# ---------- Self-healing orchestrator ---------- #

STRATEGIES = [
    ("PRIMARY_CSS", "#old-buy-button", try_primary),
    ("TEST_ID", "buy-now", try_test_id),
    ("ROLE_NAME", ("button", "Buy now"), try_role_name),
    ("TEXT_MATCH", "Buy now", try_text),
    ("AI_VISION", "the primary purchase button", ai_fallback),
]


def heal_and_act(html: str, target_action: str = "click 'Buy now' button") -> None:
    elements = parse(html)
    start = time.perf_counter()

    print("🩹 Self-Healing Locator Demo")
    print("═" * 60)
    print(f"Target action: {target_action}")
    print()

    for idx, (name, arg, fn) in enumerate(STRATEGIES, start=1):
        label = f"[{idx}/{len(STRATEGIES)}] Trying {name.lower().replace('_', ' '):<25}"
        if isinstance(arg, tuple):
            result = fn(elements, *arg)
            arg_display = f"role={arg[0]}, name={arg[1]!r}"
        else:
            result = fn(elements, arg)
            arg_display = repr(arg)
        print(f"{label} {arg_display}")
        if result is not None:
            elapsed = (time.perf_counter() - start) * 1000
            print(f"      ✅ SUCCESS — resolved to {result}")
            print()
            print(f"✨ Healed in {idx} step(s). Suggested test update:")
            print("   - page.locator('#old-buy-button')")
            print("   + page.get_by_role('button', name='Buy now')")
            print()
            print("📊 Heal stats:")
            print(f"   Strategies tried:     {idx}")
            print(f"   Final strategy:       {name}")
            print(f"   Time to heal:         {elapsed:.1f}ms")
            return
        print("      ❌ FAILED")

    print("\n💥 All strategies exhausted. Manual intervention required.")


if __name__ == "__main__":
    html = Path(__file__).parent.joinpath("fixture.html").read_text()
    heal_and_act(html)
