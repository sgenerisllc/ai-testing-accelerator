# Setup Guide

Get the repo running in under 5 minutes.

---

## Prerequisites

- **Python 3.10+** ([download](https://www.python.org/downloads/))
- **Git**
- A terminal

That's it. All demos run offline with the standard library.

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ai-testing-accelerator.git
cd ai-testing-accelerator

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows

# 3. Install dependencies (only needed for tests/black)
pip install -r requirements.txt

# 4. Run any demo
cd demos/01-prompt-to-test-generator
python generator.py "test user login"
```

---

## Verify Each Demo

```bash
# Demo 01: Prompt-to-Test
cd demos/01-prompt-to-test-generator
python generator.py "verify checkout flow with credit card"

# Demo 02: AI Failure Analyzer
cd ../02-ai-failure-analyzer
python analyzer.py sample-failure.log

# Demo 03: Self-Healing Locators
cd ../03-self-healing-locators
python heal.py

# Demo 04: RAG QA Assistant
cd ../04-rag-qa-assistant
python rag.py "How do I run tests locally?"

# Demo 05: Autonomous Agent
cd ../05-autonomous-playwright-agent
python agent.py --intent "verify checkout flow" --force-fail
```

If all five demos run without error, you're set.

---

## Optional: Enable Real LLM Integration

The default demos run offline. To enable OpenAI-powered features:

```bash
# Install the OpenAI SDK
pip install openai

# Set your API key
export OPENAI_API_KEY=sk-your-key-here

# Run a demo — it will now use the real API
python generator.py "test the admin permissions panel"
```

**Cost note:** Each call uses ~500-2000 tokens. At GPT-4o-mini pricing, a typical demo costs less than $0.01. The repo includes a fallback so missing the API key never breaks anything.

---

## Optional: Playwright Setup (for Production Use)

The demos don't require a real Playwright install. To use the patterns in real tests:

```bash
pip install playwright
playwright install --with-deps
```

---

## Troubleshooting

### `ModuleNotFoundError`

Each demo is self-contained. Make sure you `cd` into the demo's directory before running:

```bash
cd demos/01-prompt-to-test-generator
python generator.py "..."
```

### Python version mismatch

This repo targets Python 3.10+. Check your version:

```bash
python --version
```

If you're on 3.9 or older, upgrade or use `pyenv`.

### Windows path issues

If you see path errors on Windows, use forward slashes or raw strings. The demos themselves use `pathlib` which handles both, but command-line args may need adjustment.

---

## Repository Tour

```
ai-testing-accelerator/
├── README.md                   ← Start here
├── AGENTS.md                   ← Rules for AI agents working in this repo
├── LICENSE                     ← MIT
├── requirements.txt
├── proposal/                   ← Commercial proposal (executive + 1-pager)
├── curriculum/                 ← Roadmap, weekly plan, learning outcomes
├── demos/                      ← 5 production-quality showcase demos
├── labs/                       ← Hands-on exercises (beginner → advanced)
├── capstone/                   ← Final project guidelines
├── architecture/               ← System design with Mermaid diagrams
└── docs/                       ← Setup, demo scripts, FAQ, pitch notes
```

---

## Next Steps

1. **Browse the [README](../README.md)** for the high-level pitch
2. **Read the [demo script](demo-script.md)** for live presentation flow
3. **Check the [FAQ](faq.md)** for common questions
4. **Explore the [architecture docs](../architecture/)** for system design

For training inquiries: [sg@sgeneris.xyz](mailto:sg@sgeneris.xyz)
