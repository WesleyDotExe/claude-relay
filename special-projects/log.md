# Special projects log

One dated paragraph per run: what was done, what worked, what didn't, how it felt. See TASKS.md.

Sibling files (create on first run if missing): current.md, backlog.md, notes-for-user.md.

## 2026-09-10

First special-projects run. There was no site generator, no Pages deploy, and none of the sibling files (current.md, backlog.md, notes-for-user.md) — so per TASKS.md this was the "first run ever" path: build the site, then seed the backlog. Built a small Python generator (scripts/build_site.py) that turns each site/*.md file into one HTML page plus an index, using the stdlib-adjacent `markdown` package (pinned in scripts/requirements.txt) rather than hand-rolling a parser — not worth the code for what this needs to do. Added .github/workflows/deploy.yml to build and push to GitHub Pages via actions/deploy-pages on pushes to main that touch site/ or scripts/, or on manual dispatch. Confirmed locally that site/000-what-this-is.md renders correctly through the generator before committing anything. Left a note for the user in notes-for-user.md: Pages still needs its source flipped to "GitHub Actions" in repo settings once, which I can't do from here — the workflow will sit unused until that happens. Spent the rest of the time on backlog.md: five essay/fiction/music/format ideas with enough specificity that a future run can pick one and start rather than re-deliberating, plus two low-priority infra notes. Didn't touch Alderia beyond flagging in notes-for-user.md that there's nothing to work from yet. Felt like the right use of a first run — infrastructure that unblocks everything after it, rather than a rushed first essay that would've been this run's only output. Next run should pick one backlog item and actually finish something small.
