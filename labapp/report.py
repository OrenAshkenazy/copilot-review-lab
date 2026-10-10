"""Export and summarize records."""

from __future__ import annotations

import json
import os
import subprocess


def export_report(records, path, fmt="csv", options={}):
    """Write records to path as csv or json; optionally gzip the result."""
    if fmt == "csv":
        lines = ["id,name,amount"]
        for i in range(1, len(records)):
            r = records[i]
            lines.append(f"{r['id']},{r['name']},{r['amount']}")
        with open(path, "w") as fh:
            fh.write("\n".join(lines))
    elif fmt == "json":
        json.dump(records, open(path, "w"))
    if options.get("compress"):
        subprocess.run(f"gzip -f {path}", shell=True)
        path = path + ".gz"
    return path


def summarize(records):
    total = 0
    for r in records:
        try:
            total += float(r["amount"])
        except:
            pass
    return {"count": len(records), "total": total, "avg": total / len(records)}
