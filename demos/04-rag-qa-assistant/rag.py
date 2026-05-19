"""
RAG QA Assistant CLI.

Retrieves grounded answers from a markdown knowledge base.
Runs fully offline. Optional LLM synthesis if OPENAI_API_KEY is set.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from retriever import Chunk, Retriever

KB_DIR = Path(__file__).parent / "knowledge_base"


def extractive_answer(chunks: list[tuple[Chunk, float]], question: str) -> str:
    """Return the best-matching paragraph as the answer.

    Strategy: score every non-header paragraph across all retrieved
    chunks by query-keyword overlap, weighted by chunk relevance.
    Return the highest-scoring paragraph.
    """
    if not chunks:
        return "I don't have an answer in the knowledge base for that question."

    from retriever import tokenize

    query_tokens = set(tokenize(question))
    best_para = ""
    best_score = -1.0

    for chunk, chunk_score in chunks:
        for para in chunk.text.split("\n\n"):
            para = para.strip()
            if not para or para.startswith("#"):
                continue
            para_tokens = set(tokenize(para))
            overlap = len(query_tokens & para_tokens)
            if overlap == 0:
                continue
            # Weight overlap by chunk relevance; prefer concise paragraphs
            length_penalty = 1.0 / (1.0 + len(para) / 400)
            score = overlap * (1.0 + chunk_score) * length_penalty
            if score > best_score:
                best_score = score
                best_para = para

    if best_para:
        return best_para

    # Fallback: first non-header paragraph of top chunk
    top_chunk, _ = chunks[0]
    for para in top_chunk.text.split("\n\n"):
        if para.strip() and not para.startswith("#"):
            return para.strip()
    return top_chunk.text


def llm_answer(chunks: list[tuple[Chunk, float]], question: str, api_key: str) -> str:
    """Optional LLM-synthesized answer. Falls back to extractive if SDK missing."""
    try:
        from openai import OpenAI  # type: ignore
    except ImportError:
        return extractive_answer(chunks, question)

    context = "\n\n---\n\n".join(
        f"[Source: {c.source}]\n{c.text}" for c, _ in chunks
    )
    prompt = (
        "You are a QA documentation assistant. Answer the question using ONLY "
        "the context below. Cite sources by filename. If the answer is not in "
        f"the context, say so.\n\nContext:\n{context}\n\nQuestion: {question}"
    )
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return response.choices[0].message.content or extractive_answer(chunks, question)


def render_report(question: str, chunks: list[tuple[Chunk, float]], answer: str) -> str:
    lines: list[str] = []
    lines.append("🧠 RAG QA Assistant")
    lines.append("═" * 60)
    lines.append(f"Question: {question}")
    lines.append("")

    if not chunks:
        lines.append("📚 No relevant documents found.")
        lines.append("")
        lines.append("💡 Answer:")
        lines.append(f"   {answer}")
        return "\n".join(lines)

    lines.append(f"📚 Retrieved {len(chunks)} relevant document(s):")
    for idx, (chunk, score) in enumerate(chunks, start=1):
        lines.append(f"   {idx}. {chunk.source:<28} (relevance: {score:.2f})")
    lines.append("")
    lines.append("💡 Answer:")
    for line in answer.split("\n"):
        lines.append(f"   {line}")
    lines.append("")
    lines.append("🔖 Sources:")
    seen = set()
    for chunk, _ in chunks:
        if chunk.source not in seen:
            seen.add(chunk.source)
            lines.append(f"   • knowledge_base/{chunk.source}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="RAG QA Assistant for testing docs.")
    parser.add_argument("question", nargs="?", help="The question to ask")
    parser.add_argument("--list-sources", action="store_true", help="List indexed documents")
    parser.add_argument("--top-k", type=int, default=2, help="Number of chunks to retrieve")
    args = parser.parse_args()

    retriever = Retriever(KB_DIR)

    if args.list_sources:
        print("📚 Knowledge Base Sources:")
        for source in retriever.list_sources():
            print(f"   • {source}")
        return 0

    if not args.question:
        parser.error("Provide a question or use --list-sources")

    chunks = retriever.search(args.question, top_k=args.top_k)

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("🤖 Using OpenAI for answer synthesis", file=sys.stderr)
        answer = llm_answer(chunks, args.question, api_key)
    else:
        answer = extractive_answer(chunks, args.question)

    print(render_report(args.question, chunks, answer))
    return 0


if __name__ == "__main__":
    sys.exit(main())
