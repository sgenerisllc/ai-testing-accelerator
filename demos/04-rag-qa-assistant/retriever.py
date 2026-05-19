"""
Minimal TF-IDF retriever — zero external dependencies.

Splits markdown documents into chunks (paragraph-sized), computes
TF-IDF vectors for each chunk and the query, and ranks by cosine
similarity. Designed for demo-scale knowledge bases (< 1,000 docs).

For production scale, replace with Chroma, Qdrant, or a hosted
vector DB. The Retriever class API is intentionally compatible
with a drop-in vector retriever.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "have", "i", "in", "is", "it", "its", "of", "on", "or",
    "that", "the", "this", "to", "was", "were", "will", "with",
    "you", "your", "we", "our", "do", "how", "what", "when", "where",
    "which", "who", "why", "can", "if", "so", "but",
}

TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_-]+")


def tokenize(text: str) -> list[str]:
    return [
        t.lower()
        for t in TOKEN_RE.findall(text)
        if t.lower() not in STOPWORDS and len(t) > 1
    ]


@dataclass
class Chunk:
    source: str  # file path
    text: str
    tokens: list[str]


def chunk_markdown(text: str, source: str, max_chars: int = 600) -> list[Chunk]:
    """Split markdown into paragraph-ish chunks, respecting headers."""
    chunks: list[Chunk] = []
    current: list[str] = []
    current_len = 0
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > max_chars and current:
            joined = "\n\n".join(current)
            chunks.append(Chunk(source=source, text=joined, tokens=tokenize(joined)))
            current = [para]
            current_len = len(para)
        else:
            current.append(para)
            current_len += len(para)
    if current:
        joined = "\n\n".join(current)
        chunks.append(Chunk(source=source, text=joined, tokens=tokenize(joined)))
    return chunks


class Retriever:
    """TF-IDF retriever with cosine similarity ranking."""

    def __init__(self, knowledge_base_dir: Path) -> None:
        self.kb_dir = knowledge_base_dir
        self.chunks: list[Chunk] = []
        self.doc_freq: Counter[str] = Counter()
        self.idf: dict[str, float] = {}
        self._build_index()

    def _build_index(self) -> None:
        for md_file in sorted(self.kb_dir.glob("*.md")):
            text = md_file.read_text()
            self.chunks.extend(chunk_markdown(text, source=md_file.name))

        # Document frequency
        for chunk in self.chunks:
            for term in set(chunk.tokens):
                self.doc_freq[term] += 1

        # IDF
        n = max(len(self.chunks), 1)
        self.idf = {
            term: math.log((n + 1) / (df + 1)) + 1.0
            for term, df in self.doc_freq.items()
        }

    def _vectorize(self, tokens: list[str]) -> dict[str, float]:
        tf = Counter(tokens)
        if not tf:
            return {}
        max_tf = max(tf.values())
        return {
            term: (count / max_tf) * self.idf.get(term, 1.0)
            for term, count in tf.items()
        }

    @staticmethod
    def _cosine(v1: dict[str, float], v2: dict[str, float]) -> float:
        common = set(v1) & set(v2)
        if not common:
            return 0.0
        dot = sum(v1[t] * v2[t] for t in common)
        norm1 = math.sqrt(sum(v * v for v in v1.values()))
        norm2 = math.sqrt(sum(v * v for v in v2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    def search(self, query: str, top_k: int = 3) -> list[tuple[Chunk, float]]:
        query_tokens = tokenize(query)
        query_vec = self._vectorize(query_tokens)
        scored = [
            (chunk, self._cosine(query_vec, self._vectorize(chunk.tokens)))
            for chunk in self.chunks
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [(c, s) for c, s in scored[:top_k] if s > 0.0]

    def list_sources(self) -> list[str]:
        return sorted({c.source for c in self.chunks})
