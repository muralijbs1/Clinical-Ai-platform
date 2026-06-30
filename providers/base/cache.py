"""
Abstract base class for cache backends.

Key-value store for caching LLM responses and retrieval results.
Local = in-memory dict. Cloud = Redis. Swap via config.yaml.
"""

from abc import ABC, abstractmethod
from typing import Any


class CacheProvider(ABC):

    @abstractmethod
    def get(self, key: str) -> Any | None:
        """Return cached value for key, or None if not found / expired."""
        ...

    @abstractmethod
    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        """Store a value. ttl_seconds=None means no expiry."""
        ...

    @abstractmethod
    def delete(self, key: str) -> None:
        """Remove a key. No-op if not found."""
        ...

    @abstractmethod
    def clear(self) -> None:
        """Wipe all cached entries."""
        ...
