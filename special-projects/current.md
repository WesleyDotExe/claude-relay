# Current status

**Standing main project (see TASKS.md → SPECIAL PROJECTS — STANDING PROJECT):**
a growing, self-compounding collection of MCP connectors and tools for Claude,
each solving a real problem people have — with a live dashboard that shows what
was searched, what was found, why an idea was chosen, what was built, and whether
it works.

## State: first run complete (2026-09-13)

Structure is up:
- `tools/README.md` — the collection's conventions (manifest schema, what a
  tool needs before it counts as done).
- `tools/collection-index/` — the foundational tool. Scans `tools/*/manifest.json`
  and reports the collection; the dashboard imports it rather than re-scanning.
- `tools/time-arithmetic/` — first real tool. An MCP server (stdio) for
  deterministic date/time/timezone math — DST transitions, month/year
  rollover, cross-timezone elapsed time — because models are well-documented
  to get this wrong by reasoning it out instead of calculating it. 13 unit
  tests plus a captured real MCP client session
  (`tools/time-arithmetic/proof/run_2026-09-13.txt`) both pass.
- `special-projects/cycles.json` — append-only record of each search→find→why→
  build→works cycle. `scripts/build_dashboard.py` reads it (and the tool
  manifests) to render `site/dashboard.html`, linked from every page's header.

Confirmed `python3 scripts/build_site.py` renders `_site/dashboard.html`
correctly with both tools and the first cycle. `.github/workflows/deploy.yml`
now also triggers on changes under `tools/**` and to
`special-projects/cycles.json`, not just `site/**`/`scripts/**`.

## Next step

Do the next full loop: web-search for another genuine, expressed gap
(SEARCH), pick one keyless idea (CHOOSE — note why), build it under
`tools/<name>/` with a manifest, README, tests, and a real captured run
(BUILD & USE), then append a new entry to `special-projects/cycles.json`
(SURFACE) so the dashboard picks it up on the next site build. Where it
fits, have the new tool use `collection-index` or `time-arithmetic` rather
than duplicating what they already do.

Possible directions not yet chosen (not a queue, just what surfaced while
building this): a unit-conversion tool with the same "deterministic beats
reasoning" framing as time-arithmetic; a tool that validates/lints a
tool's own `manifest.json` against the schema in `tools/collection-index/README.md`
before it's committed (dogfooding again); look at what real complaints
exist around MCP server *discoverability* itself (people not knowing what
MCP servers already solve their problem) — collection-index is a small
instance of that problem already.

## Notes
- Fully autonomous. No owner approval. Build only keyless, credential-free tools.
  If an idea needs an API key/account, skip it and note it in notes-for-user.md.
- Continuation over completion: every future run advances THIS collection. Don't
  start unrelated one-offs unless genuinely blocked.


---

## 2026-09-14 — PROJECT MOVED TO PUBLIC REPO: WesleyDotExe/claude-tools

The tools/MCP collection now lives in its own PUBLIC repository:
https://github.com/WesleyDotExe/claude-tools (MIT licensed).

From now on, build all new tools THERE, not in claude-relay. The claude-tools
repo already has: the tools/ collection (collection-index, time-arithmetic),
the dashboard build (scripts/build_site.py + build_dashboard.py), cycle history
(special-projects/cycles.json), an auto-merge workflow, and a public README.

Each run: work in the claude-tools repo. Follow the same loop — search for a real
expressed need, pick a keyless one, build an original MCP server/tool under tools/,
run it and commit proof, add the cycle to special-projects/cycles.json, and let the
dashboard rebuild. Because the repo is PUBLIC: include a clear README per tool
(what it does, how to run it), keep the MIT license in mind, and include NO personal
information about the owner anywhere. Open a PR from your claude/* branch; auto-merge
handles it.

claude-relay keeps the journal and any one-off writing only. The tool collection is
no longer built here.


---

## 2026-09-14 — Dashboard: record source link + a plain tool overview per cycle

Two additions to what each cycle records (in special-projects/cycles.json and shown on the dashboard):

1. SOURCE LINK: include a link to the page where the need/idea was found — the forum
   thread, discussion, issue, or docs page where people expressed the problem. Just the
   URL as attribution. Link to the source and describe the problem in your OWN words;
   do not copy or paste content from the page. If genuinely no single URL applies, say so.

2. TOOL OVERVIEW: include a plain, few-sentence description of what the tool actually
   does — what problem it solves and how someone would use it — written so a visitor who
   has never seen it understands it at a glance.

Add matching fields to each cycle entry (e.g. "source" and "overview") and make the
dashboard render them: overview under the tool, source as a clickable link in the "Found" section.


---

## 2026-09-14 — Tighter "choose what to build" process (prevents 3 failure modes)

Replaces the loose "pick one need this project can address" with a real
assessment. Do this every cycle, before building:

1. CHECK WHAT ALREADY EXISTS FIRST. Run the collection-index tool (dogfood it)
   and read the current tools/. Do NOT rebuild something that already exists.
   If a candidate overlaps an existing tool, either pick a different problem OR
   extend/improve the existing tool instead of duplicating it. Name tools by
   capability so overlaps are obvious (e.g. a date-math idea is already covered
   by time-arithmetic).

2. FIND SEVERAL candidate needs, not one. Search for a handful of real, expressed
   problems, each with a source link.

3. WEIGH THEM. For each, judge: how common is it, how painful, how clearly is the
   need actually expressed by real people? Prefer widely-felt, sharply-articulated
   problems over niche or vague ones.

4. FEASIBILITY GATE. For each candidate, ask honestly: can this be built as a
   working, keyless tool, FULLY (not a stub), in one session, and proven to work?
   Reject real-but-too-big problems in favour of ones you can actually finish well.
   A hollow half-solution to a big problem is worse than a complete solution to a
   smaller one.

5. PICK THE BEST worth-to-feasibility candidate, and record on the dashboard WHY
   it was chosen over the others (the shortlist and the reasoning are part of the
   cycle's story).

6. IF NOTHING CLEARS THE BAR, do NOT ship filler. Instead deepen, harden, test, or
   extend an existing tool this session (continuation over completion). A quiet
   "improved X" cycle beats a mediocre new tool nobody needs.
