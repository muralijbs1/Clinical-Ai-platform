"""
Provider registry — the only place that reads config.yaml and instantiates backends.

Usage:
    from providers.registry import get_vector_store, get_embedder, get_document_store, get_cache

Returns a singleton per provider type for the lifetime of the process.
Swap backends by changing config.yaml — no code changes needed.
"""

import yaml
from functools import lru_cache
from pathlib import Path

from providers.base import (
    VectorStoreProvider,
    EmbeddingProvider,
    DocumentStoreProvider,
    CacheProvider,
)


def _load_config() -> dict:
    path = Path(__file__).parent.parent / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


@lru_cache(maxsize=1)
def get_vector_store() -> VectorStoreProvider:
    config = _load_config()
    provider = config["vector_store"]["provider"]

    if provider == "memory":
        from providers.local.memory_vector_store import MemoryVectorStore
        return MemoryVectorStore()
    if provider == "chroma":
        from providers.local.chroma_vector_store import ChromaVectorStore
        return ChromaVectorStore(config["vector_store"])
    if provider == "pinecone":
        from providers.cloud.pinecone_vector_store import PineconeVectorStore
        return PineconeVectorStore(config["vector_store"])

    raise ValueError(f"Unknown vector_store provider: {provider!r}")


@lru_cache(maxsize=1)
def get_embedder() -> EmbeddingProvider:
    config = _load_config()
    provider = config["embeddings"]["provider"]

    if provider == "tfidf":
        from providers.local.tfidf_embedder import TfidfEmbedder
        return TfidfEmbedder()
    if provider == "sentence_transformers":
        from providers.local.sentence_transformer_embedder import SentenceTransformerEmbedder
        return SentenceTransformerEmbedder(config["embeddings"])
    if provider == "openai":
        from providers.cloud.openai_embedder import OpenAIEmbedder
        return OpenAIEmbedder(config["embeddings"])

    raise ValueError(f"Unknown embeddings provider: {provider!r}")


@lru_cache(maxsize=1)
def get_document_store() -> DocumentStoreProvider:
    config = _load_config()
    provider = config.get("document_store", {}).get("provider", "filesystem")

    if provider == "filesystem":
        from providers.local.filesystem_document_store import FilesystemDocumentStore
        return FilesystemDocumentStore(config.get("document_store", {}))
    if provider == "s3":
        from providers.cloud.s3_document_store import S3DocumentStore
        return S3DocumentStore(config["document_store"])

    raise ValueError(f"Unknown document_store provider: {provider!r}")


@lru_cache(maxsize=1)
def get_cache() -> CacheProvider:
    config = _load_config()
    provider = config.get("state_store", {}).get("provider", "memory")

    if provider == "memory":
        from providers.local.memory_cache import MemoryCache
        return MemoryCache()
    if provider == "redis":
        from providers.cloud.redis_cache import RedisCache
        return RedisCache(config["state_store"])

    raise ValueError(f"Unknown cache provider: {provider!r}")
