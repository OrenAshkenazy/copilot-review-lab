from pathlib import Path

from labapp.store import Store


def test_round_trip(tmp_path: Path) -> None:
    store = Store()
    store.add(1, "alpha", 10.5)
    store.add(2, "beta", 4.0)
    store.save(tmp_path / "s.json")

    loaded = Store.load(tmp_path / "s.json")

    assert loaded.all() == store.all()
