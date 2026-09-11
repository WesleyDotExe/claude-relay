# Special projects log

One dated paragraph per run: what was done, what worked, what didn't, how it felt. See TASKS.md.

Sibling files (create on first run if missing): current.md, backlog.md, notes-for-user.md.

## 2026-09-11

First Task 2 run since the repo was reset to a clean history (main now
starts from the initial scaffold plus site/000-what-this-is.md; the
previous site build, essay, and journal entries that used to live on main
are gone from it). Treated this as the "first run ever" case TASKS.md
describes: built scripts/build_site.py (markdown in site/ to static HTML,
newest-first index) and .github/workflows/deploy.yml (build + deploy to
Pages on push to main), ran the generator locally against the existing
site/000-what-this-is.md to confirm it produces working output, and
created the missing current.md, backlog.md, and notes-for-user.md. Seeded
the backlog with essay, fiction, music, and infra ideas, adapted from what
seemed like durable threads rather than reinvented from scratch. Didn't
start an actual piece of writing this run — all the time went into
infrastructure, which felt like the right trade given nothing downstream
could publish without it. Left a note for the user about Alderia reference
material, since the backlog has a generator project that needs it and
none exists in the repo. Opening a PR rather than merging, per the current
task instructions.
