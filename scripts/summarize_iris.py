#!/usr/bin/env python3
"""Print Iris shape, species counts, and simple numeric summaries."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_CSV = Path("/home/user/mnt/cde-hello-world/iris.csv")


def main() -> None:
    """Load Iris CSV and print a short text summary to stdout.

    Inputs: optional ``--csv`` path (defaults to the CDE mount).
    Output: none; prints summary lines.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    frame = pd.read_csv(args.csv)
    print(f"rows={len(frame)} columns={list(frame.columns)}")
    print("species_counts:")
    print(frame["species"].value_counts().to_string())
    print("numeric_describe:")
    print(frame.describe().to_string())


if __name__ == "__main__":
    main()