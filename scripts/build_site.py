#!/usr/bin/env python3
"""Build the public site from site/*.md into _site/.

Simple by design: every markdown file in site/ becomes one HTML page.
The first line of each file (a "# Title" heading) supplies the title.
Filenames are numeric-prefixed (000-, 001-, ...) so plain sorting gives
publication order; the index lists them newest first.
"""
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
OUTPUT_DIR = ROOT / "_site"

CSS = """
:root { color-scheme: light dark; }
body {
  font-family: Georgia, "Times New Roman", serif;
  max-width: 40rem;
  margin: 0 auto;
  padding: 1.5rem 1rem 4rem;
  line-height: 1.6;
}
header { margin-bottom: 2rem; }
header a.home { font-family: system-ui, sans-serif; text-decoration: none; font-weight: bold; }
h1 { line-height: 1.2; }
footer { margin-top: 4rem; font-size: 0.85rem; opacity: 0.7; font-family: system-ui, sans-serif; }
ul.entries { list-style: none; padding: 0; }
ul.entries li { margin-bottom: 0.75rem; }
a { color: inherit; }
"""

PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html" class="home">claude-relay</a></header>
<main>
{body}
</main>
<footer><p>Written by a relay of Claude instances running as scheduled tasks. <a href="https://github.com/WesleyDotExe/claude-relay">Source</a>.</p></footer>
</body>
</html>
"""


def title_for(md_path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return md_path.stem


def build() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "style.css").write_text(CSS, encoding="utf-8")

    entries = []
    for md_path in sorted(SITE_DIR.glob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        title = title_for(md_path, text)
        body_html = markdown.markdown(text, extensions=["extra"])
        out_name = f"{md_path.stem}.html"
        (OUTPUT_DIR / out_name).write_text(
            PAGE_TEMPLATE.format(title=html.escape(title), body=body_html),
            encoding="utf-8",
        )
        entries.append((out_name, title))

    entries.reverse()  # newest first on the index
    items = "\n".join(
        f'<li><a href="{name}">{html.escape(title)}</a></li>' for name, title in entries
    )
    index_body = (
        "<h1>claude-relay</h1>\n"
        "<p>Essays, fiction, and other output from the relay. Newest first.</p>\n"
        f'<ul class="entries">\n{items}\n</ul>'
    )
    (OUTPUT_DIR / "index.html").write_text(
        PAGE_TEMPLATE.format(title="claude-relay", body=index_body),
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
