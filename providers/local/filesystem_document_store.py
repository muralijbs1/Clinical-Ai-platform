"""
Filesystem-backed document store. Saves each Document as a JSON file.
Survives process restarts. Swap to S3/MinIO via config.yaml for cloud.
"""

import json
from pathlib import Path
from providers.base.document_store import DocumentStoreProvider
from schemas import Document


_DEFAULT_STORE_DIR = Path(__file__).parent.parent.parent / "data" / "document_store"


class FilesystemDocumentStore(DocumentStoreProvider):

    def __init__(self, config: dict | None = None):
        store_dir = (config or {}).get("path", str(_DEFAULT_STORE_DIR))
        self._root = Path(store_dir)
        self._root.mkdir(parents=True, exist_ok=True)

    def save(self, document: Document) -> str:
        path = self._path(document.id)
        path.write_text(document.model_dump_json(indent=2), encoding="utf-8")
        return document.id

    def load(self, doc_id: str) -> Document:
        path = self._path(doc_id)
        if not path.exists():
            raise KeyError(f"Document not found: {doc_id!r}")
        return Document.model_validate_json(path.read_text(encoding="utf-8"))

    def exists(self, doc_id: str) -> bool:
        return self._path(doc_id).exists()

    def delete(self, doc_id: str) -> None:
        path = self._path(doc_id)
        if path.exists():
            path.unlink()

    def _path(self, doc_id: str) -> Path:
        safe_id = doc_id.replace("/", "_").replace("\\", "_")
        return self._root / f"{safe_id}.json"
