"""In-memory record store with JSON persistence."""

from __future__ import annotations

import json
from pathlib import Path


class Store:
    def __init__(self) -> None:
        self._records: list[dict] = []

    def add(self, record_id: int, name: str, amount: float) -> dict:
        record = {"id": record_id, "name": name, "amount": amount}
        self._records.append(record)
        return record

    def all(self) -> list[dict]:
        return list(self._records)

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self._records, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Store":
        store = cls()
        store._records = json.loads(path.read_text(encoding="utf-8"))
        return store
