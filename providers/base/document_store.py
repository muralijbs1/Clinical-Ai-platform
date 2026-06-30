"""
Abstract base class for document store backends.

Stores and retrieves raw Document objects by ID.
Local = filesystem. Cloud = S3 / MinIO. Swap via config.yaml.
"""

from abc import ABC, abstractmethod
from schemas import Document


class DocumentStoreProvider(ABC):

    @abstractmethod
    def save(self, document: Document) -> str:
        """Persist a document. Returns the document ID."""
        ...

    @abstractmethod
    def load(self, doc_id: str) -> Document:
        """Retrieve a document by ID. Raises KeyError if not found."""
        ...

    @abstractmethod
    def exists(self, doc_id: str) -> bool:
        """Return True if a document with this ID exists."""
        ...

    @abstractmethod
    def delete(self, doc_id: str) -> None:
        """Remove a document by ID. No-op if not found."""
        ...
