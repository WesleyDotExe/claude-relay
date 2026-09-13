# tools/

A growing collection of MCP connectors and tools for Claude, each solving a
real, expressed need — no external credentials or paid accounts required.
See `TASKS.md` -> Task 2 -> "SPECIAL PROJECTS — STANDING PROJECT" for the
loop every run follows: search for a genuine need, choose one that's
buildable keyless, build and run it under `tools/<name>/`, then record the
cycle in `special-projects/cycles.json` so `site/dashboard.html` can show
the story.

## Adding a tool

Each tool lives in its own `tools/<name>/` directory and needs at least:

- `manifest.json` — see `tools/collection-index/README.md` for the schema.
  `collection-index` reads this to build the dashboard, so a tool without
  one (or with one missing required fields) won't show up there.
- `README.md` — what it solves, how to run it, what it doesn't do.
- Tests, and a captured proof of a real run (a `proof/` file, a report
  under the tool's own directory, etc.) — a tool that's committed but
  never run is scaffolding, not finished work.

## What's here so far

- `collection-index/` — reads this directory and reports its contents.
  The foundational tool; the dashboard is built on top of it.
- `time-arithmetic/` — an MCP server for deterministic date/time/timezone
  math (DST, month rollover, cross-timezone elapsed time), because models
  are unreliable at exactly this kind of arithmetic.

Run `python3 tools/collection-index/index.py` for a live listing, or see
the dashboard at `site/dashboard.html` (built by `scripts/build_site.py`).
