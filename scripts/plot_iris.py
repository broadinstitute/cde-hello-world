#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "matplotlib>=3.8",
#   "pandas>=2.0",
# ]
# ///
"""Run with ``uv run`` to save an Iris sepal scatter under ~/experiments."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DEFAULT_CSV = Path("/home/user/mnt/cde-hello-world/iris.csv")
DEFAULT_OUT = Path.home() / "experiments" / "iris_sepal_scatter.png"


def main() -> None:
    """Create a sepal-length vs sepal-width scatter colored by species.

    Inputs: optional ``--csv`` and ``--out`` paths.
    Output: none; writes a PNG and prints the output path.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    frame = pd.read_csv(args.csv)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    fig, axis = plt.subplots(figsize=(6, 4))
    for species, group in frame.groupby("species"):
        axis.scatter(
            group["sepal_length"],
            group["sepal_width"],
            label=species,
            alpha=0.8,
        )
    axis.set_xlabel("sepal_length (cm)")
    axis.set_ylabel("sepal_width (cm)")
    axis.set_title("Iris sepal length vs width")
    axis.legend()
    fig.tight_layout()
    fig.savefig(args.out, dpi=120)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()