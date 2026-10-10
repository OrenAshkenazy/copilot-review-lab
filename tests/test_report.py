from pathlib import Path

from labapp.report import export_report, summarize


RECORDS = [
    {"id": 1, "name": "alpha", "amount": 10.5},
    {"id": 2, "name": "beta", "amount": 4.0},
    {"id": 3, "name": "gamma", "amount": "n/a"},
]


def test_summarize_counts_and_totals() -> None:
    result = summarize(RECORDS)
    assert result["count"] == 3
    assert result["total"] == 14.5


def test_export_csv_writes_header(tmp_path: Path) -> None:
    out = export_report(RECORDS, str(tmp_path / "r.csv"))
    assert Path(out).read_text().splitlines()[0] == "id,name,amount"
