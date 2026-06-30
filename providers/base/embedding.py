"""
Abstract base class for embedding backends.

Turns text into vectors. Local = TF-IDF / sentence-transformers.
Cloud = OpenAI / hosted models. Swap via config.yaml.
"""

from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """Embed a single string and return its vector."""
        ...

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of strings. More efficient than calling embed() in a loop."""
        ...

    @abstractmethod
    def dimension(self) -> int:
        """Return the length of the vectors this provider produces."""
        ...
