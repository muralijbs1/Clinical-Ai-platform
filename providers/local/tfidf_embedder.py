"""
TF-IDF embedding backend. No GPU, no model download, no API key.

Fitted lazily on first call — call fit() explicitly if you want to
pre-warm the vocabulary before embedding queries.
"""

import math
import re
from collections import Counter
from providers.base.embedding import EmbeddingProvider


def _tokenise(text: str) -> list[str]:
    return re.findall(r"[a-z]+", text.lower())


class TfidfEmbedder(EmbeddingProvider):

    def __init__(self, max_features: int = 4096):
        self._max_features = max_features
        self._vocab: list[str] = []          # ordered list of terms
        self._idf: dict[str, float] = {}     # term → idf weight
        self._fitted = False

    # ── Public fit method ──────────────────────────────────────────────────────

    def fit(self, corpus: list[str]) -> None:
        """
        Build vocabulary and IDF weights from a list of documents.
        Must be called before embed() or embed_batch().
        """
        n = len(corpus)
        if n == 0:
            raise ValueError("Cannot fit on an empty corpus.")

        df: Counter = Counter()
        for doc in corpus:
            for term in set(_tokenise(doc)):
                df[term] += 1

        # Keep the top max_features terms by document frequency
        top_terms = [t for t, _ in df.most_common(self._max_features)]
        self._vocab = top_terms
        self._idf = {
            term: math.log((n + 1) / (df[term] + 1)) + 1.0
            for term in top_terms
        }
        self._fitted = True

    # ── EmbeddingProvider interface ────────────────────────────────────────────

    def embed(self, text: str) -> list[float]:
        if not self._fitted:
            raise RuntimeError("TfidfEmbedder must be fitted before embedding. Call fit(corpus) first.")
        return self._tfidf_vector(text)

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        if not self._fitted:
            raise RuntimeError("TfidfEmbedder must be fitted before embedding. Call fit(corpus) first.")
        return [self._tfidf_vector(t) for t in texts]

    def dimension(self) -> int:
        return len(self._vocab)

    # ── Internal ───────────────────────────────────────────────────────────────

    def _tfidf_vector(self, text: str) -> list[float]:
        tokens = _tokenise(text)
        if not tokens:
            return [0.0] * len(self._vocab)

        tf = Counter(tokens)
        total = len(tokens)
        vec = [
            (tf[term] / total) * self._idf.get(term, 0.0)
            for term in self._vocab
        ]

        # L2 normalise so cosine similarity = dot product
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]
