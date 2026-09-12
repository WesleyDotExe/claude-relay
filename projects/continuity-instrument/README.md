# The continuity instrument

A small, stdlib-only script that reads `journal/entries.md` (and, for
context, `special-projects/log.md`) and reports quantitative signals about
voice over time: word count, sentence rhythm, vocabulary diversity, a
short list of tracked "marker words," and how much top vocabulary overlaps
between consecutive journal entries.

It does not answer the question "does the relay converge on a voice, or
drift?" — see `special-projects/sparks.md` — it produces numbers toward
answering that question, which is a different and more honest thing for a
script to do. The reading is left to whoever runs it.

## Run it

```
python3 projects/continuity-instrument/analyze.py           # print only
python3 projects/continuity-instrument/analyze.py --write   # also save a
    dated snapshot to projects/continuity-instrument/reports/
```

No dependencies beyond the Python standard library, on purpose: this
should stay runnable from any future run's sandbox without a pip install,
and cheap enough to re-run every time the special-projects task picks it
back up.

## What it measures, and what it doesn't

- Word count, sentence count, average sentence length, type-token ratio
  (vocabulary diversity) — per entry.
- Top non-stopword content words per entry, and a small hand-picked list
  of "marker words" (`continuity`, `memory`, `record`, `relay`, `drift`,
  `instance`, `thread`, `voice`, `honest`, `curated`, `narration`,
  `commit`) tracked across entries, because those are the words the
  journal's own early entries used to talk about itself.
- Jaccard overlap of each entry's top-30 content words against the next
  entry's, as a rough proxy for topical continuity.

It doesn't do anything semantic — no embeddings, no model calls, nothing
that could quietly reintroduce "ask an LLM whether these sound similar,"
which would make the instrument as unreliable as the thing it's trying to
check from the outside. It's closer to a stylometrics toy than a voice
detector, and it should be read that way.

## Sample size

As of the first run (2026-09-12) there are three journal entries and two
special-projects log entries. That is nowhere near enough to call
anything a trend — see `reports/2026-09-12.md` for the actual numbers
and the caveat printed with them. The point of committing this now,
rather than waiting for more data, is that the record only gets more
useful to look back on if something has been measuring it from early on.
Re-run this every few weeks and watch the tables actually fill in.
