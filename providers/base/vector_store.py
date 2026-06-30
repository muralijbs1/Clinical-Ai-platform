"""
Abstract base class for vector store backends.

Agents never import a specific backend (Chroma, Pinecone, etc.).
They import this interface. Swapping backends = changing config.yaml only.
"""

from abc import ABC, abstractmethod
from schemas import Document


class VectorStoreProvider(ABC):

    @abstractmethod
    def add_documents(self, documents: list[Document]) -> None:
        """Embed and store a list of documents."""
        ...

    @abstractmethod
    def search(self, query_vector: list[float], top_k: int = 5) -> list[Document]:
        """Return the top_k most similar documents to the query vector."""
        ...

    @abstractmethod
    def delete(self, doc_id: str) -> None:
        """Remove a document by ID."""
        ...

    @abstractmethod
    def count(self) -> int:
        """Return total number of documents stored."""
        ...
