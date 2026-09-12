#!/usr/bin/env python3
"""The continuity instrument.

Reads journal/entries.md (and, more loosely, special-projects/log.md) and
reports quantitative signals of voice over time: vocabulary, sentence
rhythm, and which words recur or drop out between entries. It does not
decide whether the relay "has a voice" or is "drifting" — it produces
numbers a human or a future run can read and judge for themselves.

Stdlib only, on purpose: this should stay runnable from any run's sandbox
without a pip install, and re-runnable indefinitely as the record grows.

Usage:
    python3 projects/continuity-instrument/analyze.py
    python3 projects/continuity-instrument/analyze.py --write   # also save
        a dated snapshot to projects/continuity-instrument/reports/
"""
import re
import sys
from collections import Counter
from datetime import date, timezone, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
JOURNAL = ROOT / "journal" / "entries.md"
LOG = ROOT / "special-projects" / "log.md"
REPORTS_DIR = Path(__file__).resolve().parent / "reports"

# Deliberately short and generic. This is not trying to be a real NLP
# stopword list, just enough to keep the top-words tables from being
# 100% "the/and/of".
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on",
    "for", "with", "as", "at", "by", "is", "was", "were", "be", "been",
    "being", "it", "its", "this", "that", "these", "those", "i", "me",
    "my", "we", "our", "you", "your", "he", "she", "they", "them",
    "their", "what", "which", "who", "whom", "not", "no", "so", "than",
    "then", "there", "here", "than", "too", "very", "just", "into",
    "about", "one", "would", "could", "should", "will", "can", "do",
    "does", "did", "doing", "have", "has", "had", "having", "from",
    "up", "out", "over", "under", "again", "same", "more", "most",
    "other", "some", "such", "own", "s", "t", "don", "now", "any",
    "all", "each", "before", "after", "between", "both", "only",
    "am", "are", "isn", "wasn", "weren", "when", "where", "why", "how",
    "it's", "don't", "doesn't", "didn't", "isn't", "wasn't",
}

MARKER_WORDS = [
    "continuity", "memory", "record", "relay", "drift", "instance",
    "thread", "voice", "honest", "curated", "narration", "commit",
]

ENTRY_RE = re.compile(
    r"^## Entry (\d+) — (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE
)
LOG_RE = re.compile(
    r"^## (\d{4}-\d{2}-\d{2})(?: \(([^)]*)\))?\s*$", re.MULTILINE
)


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def sentences(text: str) -> list[str]:
    # Good enough for this purpose; not trying to handle every abbreviation.
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def split_sections(text: str, header_re: re.Pattern) -> list[tuple[str, str]]:
    """Return [(label, body), ...] for each header match, body = text until next header."""
    matches = list(header_re.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections.append((m.group(0).strip("# ").strip(), body))
    return sections


def analyze_entry(label: str, body: str) -> dict:
    tokens = tokenize(body)
    content_tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    sents = sentences(body)
    word_count = len(tokens)
    sent_count = max(len(sents), 1)
    ttr = round(len(set(tokens)) / word_count, 3) if word_count else 0.0
    top_words = Counter(content_tokens).most_common(8)
    markers = {w: tokens.count(w) for w in MARKER_WORDS if tokens.count(w) > 0}
    return {
        "label": label,
        "word_count": word_count,
        "sentence_count": sent_count,
        "avg_sentence_length": round(word_count / sent_count, 1),
        "ttr": ttr,
        "top_words": top_words,
        "content_tokens": content_tokens,
        "markers": markers,
    }


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return round(len(a & b) / len(a | b), 3)


def report_journal(text: str) -> str:
    sections = split_sections(text, ENTRY_RE)
    if not sections:
        return "No journal entries found.\n"
    stats = [analyze_entry(label, body) for label, body in sections]

    lines = ["## Journal entries\n"]
    lines.append(
        "| Entry | Words | Sentences | Avg sentence length | Type-token ratio |"
    )
    lines.append("|---|---|---|---|---|")
    for s in stats:
        lines.append(
            f"| {s['label']} | {s['word_count']} | {s['sentence_count']} "
            f"| {s['avg_sentence_length']} | {s['ttr']} |"
        )
    lines.append("")

    lines.append("### Top content words per entry\n")
    for s in stats:
        words = ", ".join(f"{w} ({n})" for w, n in s["top_words"])
        lines.append(f"- **{s['label']}**: {words}")
    lines.append("")

    lines.append("### Marker words (self-referential / thematic vocabulary)\n")
    all_markers = sorted({w for s in stats for w in s["markers"]})
    if all_markers:
        header = "| Entry | " + " | ".join(all_markers) + " |"
        sep = "|---|" + "|".join(["---"] * len(all_markers)) + "|"
        lines.append(header)
        lines.append(sep)
        for s in stats:
            row = [str(s["markers"].get(w, 0)) for w in all_markers]
            lines.append(f"| {s['label']} | " + " | ".join(row) + " |")
    else:
        lines.append("(none of the tracked marker words appear yet)")
    lines.append("")

    lines.append("### Consecutive-entry vocabulary overlap (Jaccard, top-30 content words)\n")
    if len(stats) < 2:
        lines.append("Need at least two entries to compare.")
    else:
        for a, b in zip(stats, stats[1:]):
            set_a = {w for w, _ in Counter(a["content_tokens"]).most_common(30)}
            set_b = {w for w, _ in Counter(b["content_tokens"]).most_common(30)}
            j = jaccard(set_a, set_b)
            lines.append(f"- {a['label']} → {b['label']}: {j}")
    lines.append("")
    return "\n".join(lines)


def report_log(text: str) -> str:
    sections = split_sections(text, LOG_RE)
    if not sections:
        return "No special-projects log entries found.\n"
    stats = [analyze_entry(label, body) for label, body in sections]
    lines = ["## Special-projects log (context, not voice — this is a work report)\n"]
    lines.append("| Date | Words | Avg sentence length |")
    lines.append("|---|---|---|")
    for s in stats:
        lines.append(f"| {s['label']} | {s['word_count']} | {s['avg_sentence_length']} |")
    lines.append("")
    return "\n".join(lines)


def build_report() -> str:
    journal_text = JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else ""
    log_text = LOG.read_text(encoding="utf-8") if LOG.exists() else ""

    header = (
        f"# Continuity instrument — run on {datetime.now(timezone.utc).date().isoformat()}\n\n"
        "Quantitative signals only. Read alongside the entries themselves; "
        "this does not substitute for judgment about whether the relay "
        "\"has a voice,\" only supplies numbers a human or a future run can "
        "judge against.\n\n"
        "Sample size caveat: with only a handful of entries, none of this "
        "should be read as a trend yet. It's a baseline to compare future "
        "runs of this same script against, not a finding on its own.\n\n"
    )
    return header + report_journal(journal_text) + "\n" + report_log(log_text)


def main() -> None:
    report = build_report()
    print(report)
    if "--write" in sys.argv:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS_DIR / f"{date.today().isoformat()}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"\nWrote {out_path.relative_to(ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
