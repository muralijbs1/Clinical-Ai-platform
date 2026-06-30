"""
In-memory vector store. Stores vectors in a Python list.
Uses brute-force cosine similarity (dot product on L2-normalised vectors).

Fast enough for thousands of documents. For larger corpora, swap to
Chroma or Pinecone via config.yaml — zero agent code changes needed.
"""

import math
from dataclasses import dataclass, field
from providers.base.vector_store import VectorStoreProvider
from schemas import Document


@dataclass
class _Entry:
    document: Document
    vector: list[float]


class MemoryVectorStore(VectorStoreProvider):

    def __init__(self):
        self._entries: list[_Entry] = []

    # ── VectorStoreProvider interface ──────────────────────────────────────────

    def add_documents(self, documents: list[Document]) -> None:
        raise NotImplementedError(
            "MemoryVectorStore.add_documents() requires pre-computed vectors. "
            "Use add_with_vectors() directly, or use the RAG pipeline which handles embedding."
        )

    def add_with_vectors(self, documents: list[Document], vectors: list[list[float]]) -> None:
        """Add documents alongside their pre-computed embedding vectors."""
        if len(documents) != len(vectors):
            raise ValueError("documents and vectors must have the same length.")
        for doc, vec in zip(documents, vectors):
            # Remove any existing entry with the same ID first
            self._entries = [e for e in self._entries if e.document.id != doc.id]
            self._entries.append(_Entry(document=doc, vector=vec))

    def search(self, query_vector: list[float], top_k: int = 5) -> list[Document]:
        if not self._entries:
            return []
        scored = [
            (_cosine(query_vector, e.vector), e.document)
            for e in self._entries
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:top_k]]

    def delete(self, doc_id: str) -> None:
        self._entries = [e for e in self._entries if e.document.id != doc_id]

    def count(self) -> int:
        return len(self._entries)


def _cosine(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a)) or 1.0
    norm_b = math.sqrt(sum(y * y for y in b)) or 1.0
    return dot / (norm_a * norm_b)
