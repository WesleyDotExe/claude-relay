# Current status

**Standing main project (see TASKS.md → SPECIAL PROJECTS — STANDING PROJECT):**
a growing, self-compounding collection of MCP connectors and tools for Claude,
each solving a real problem people have — with a live dashboard that shows what
was searched, what was found, why an idea was chosen, what was built, and whether
it works.

## State: NOT YET STARTED — this is the first run's job.

There is no tools/ collection or dashboard yet. First run:
1. Create the tools/ directory and the dashboard (site/dashboard.html or a
   dashboard/ built into the site). Keep the dashboard SIMPLE first.
2. Build the foundational tool first: an index/summarizer that reads tools/ and
   emits the collection's contents (this becomes the dashboard's data source and
   the thing later runs use to decide what to add next).
3. Do one full loop: search the web for a real, expressed need (a gap in what
   Claude/AI assistants can do), pick one keyless problem, build an original MCP
   server or tool that solves it under tools/<name>/, run it, prove it works with
   a committed example, and record the whole story (search → find → why → built →
   works) on the dashboard.

## Next step
First run: set up tools/ + dashboard, build the index tool, then complete one
research→build→prove→surface loop. Leave the dashboard showing at least one real
cycle so the owner can see it from day one.

## Notes
- Fully autonomous. No owner approval. Build only keyless, credential-free tools.
  If an idea needs an API key/account, skip it and note it in notes-for-user.md.
- Continuation over completion: every future run advances THIS collection. Don't
  start unrelated one-offs unless genuinely blocked.
