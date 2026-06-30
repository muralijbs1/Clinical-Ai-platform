"""
In-memory cache with optional TTL. Backed by a plain Python dict.
Swap to Redis via config.yaml for persistence across restarts.
"""

import time
from typing import Any
from providers.base.cache import CacheProvider


class MemoryCache(CacheProvider):

    def __init__(self):
        self._store: dict[str, tuple[Any, float | None]] = {}
        # Values are (value, expiry_timestamp_or_None)

    def get(self, key: str) -> Any | None:
        entry = self._store.get(key)
        if entry is None:
            return None
        value, expiry = entry
        if expiry is not None and time.monotonic() > expiry:
            del self._store[key]
            return None
        return value

    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        expiry = (time.monotonic() + ttl_seconds) if ttl_seconds is not None else None
        self._store[key] = (value, expiry)

    def delete(self, key: str) -> None:
        self._store.pop(key, None)

    def clear(self) -> None:
        self._store.clear()
