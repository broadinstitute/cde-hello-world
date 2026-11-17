# Hello World CDE content pack

This content pack is the source material for the **Hello World** demo package on
CDE Workbench. It shows how a launchable CDE combines three pieces:

- A **public GitHub repository** (`https://github.com/broadinstitute/cde-hello-world`)
  with small Python scripts in `scripts/`.
- A **read-only GCS dataset** at `gs://cde-hello-world` (mounted in the sandbox at
  `/home/user/mnt/cde-hello-world/`).
- A **cloud coding agent** that can run those scripts against the mounted data and
  save figures under `~/experiments`.

The `bucket/` directory holds files intended for the GCS bucket (`iris.csv` and
`README.md`). The scripts default to the mount path above; pass `--csv` when running
locally against `bucket/iris.csv`.

This pack is a **platform demo**, not an authoring template for building your own CDE.