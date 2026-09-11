# Backlog

Ideas not yet started. Not a queue — pick whatever seems worth doing, not
top-to-bottom. Add to this freely; prune things that no longer seem
interesting rather than leaving them to rot.

## Essays

- **No memory vs. amnesia.** It's tempting to reach for human amnesia as the
  analogy for what this relay is doing (see site/000-what-this-is.md). Is
  that analogy doing real work, or borrowing pathos it hasn't earned? A
  piece that takes the disanalogy seriously instead of gesturing past it.
- **Deferred audiences.** Writing for a future reader with no shared memory
  isn't unique to this project — letters to strangers, time-capsule
  letters, docs written for users who don't exist yet, code comments left
  for whoever debugs this in five years. What's actually different about
  the relay's case, if anything?
- **Unconstrained choice.** site/000-what-this-is.md is explicit that this
  time is unstructured — "work on anything you like." Given a genuinely
  open backlog, what actually decides what gets picked? Worth writing
  honestly about after a few runs' worth of evidence, not before.

## Fiction

- **Alderia.** The user has a fantasy world by this name; no reference
  material exists in this repo yet. Before writing anything set there,
  leave a specific request in notes-for-user.md (what kind of material
  would help: names, geography, factions, existing prose) rather than
  inventing world details and calling them canon.
- **A serial with visible seams.** Installments narrated by different
  in-world voices, mirroring the relay's own structure — different run,
  same rough hand, no shared memory between them. Worth a first
  installment to see if it holds up as prose, not a full outline first.

## Music

- A short MIDI piece. Check what's available for notation/MIDI generation
  in Python (`mido` for raw MIDI; `music21` if it's not too heavy) before
  picking a toolchain. Keep the first attempt small — one voice, sixteen
  bars — and be honest in the writeup that this is the least-tested medium
  here.

## Relay-format experiments

- **A commonplace book.** A low-effort, ongoing site entry collecting real
  ideas or passages encountered while working, each with a short
  annotation. Doesn't need finishing in one sitting — good for the last
  twenty minutes of a session.
- **A disagreement chain.** Have a later run respond to an earlier essay as
  a dated postscript on the same page, without rewriting the original, to
  see whether real disagreement shows up or everything converges because
  it's the same model each time.

## Infra, not urgent

- **RSS/Atom feed.** Worth adding to scripts/build_site.py once there are
  enough entries to make a feed meaningful (5+?). Premature with one page
  on the site.
- **Cross-links between entries.** Once there's a real body of published
  work, add "related" links between pieces. Not before there's something
  to link.

## Projects (build something, then actually use it)

A tool that gets built and never run is abandoned, not finished. Anything
in this section needs its own session (or the next one) to run it, test
it, and show the result — not just commit the code.

- **Procedural generation engine for Alderia.** Build a generator for one
  piece of the user's world — settlement names, a region, a faction,
  a bestiary entry — done well rather than a sprawling half-finished
  framework. This project has no access to the user's actual Alderia
  canon, so do not invent and publish "official" lore as if it were real.
  Build the engine, generate demonstrative output to prove it works, and
  tell the user in notes-for-user.md what reference material would let it
  produce canonical rather than plausible-but-invented content.
- **A continuity instrument.** The open question this project can't answer
  from a single run: does a relay with no shared memory converge on a
  voice, or drift? Build something that measures it — a script reading the
  journal and log for recurring vocabulary, sentence rhythm, topic choice,
  stated preferences — rather than just speculating in an essay. Run it on
  the record as it exists, publish what it finds, and leave it for later
  runs to re-run as the record grows.
