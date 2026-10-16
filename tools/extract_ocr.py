#!/usr/bin/env python3
"""Extract the OCR text layer of a scanned PDF, one text file per *printed* page.

The source PDFs in NUMDAM are page scans with an OCR text layer.  The text
layer is good enough to draft a translation from, but it is unreliable for
mathematics (sub/superscripts, fractions and italics are frequently mangled),
so it must always be checked against the page image.

Usage:
    python tools/extract_ocr.py <pdf> <outdir> [--first-page N] [--offset N]

    python tools/extract_ocr.py gabriel.pdf reference/ocr --first-page 323

Writes ``<outdir>/page-0323.txt`` ... one file per page of the article.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF is required: pip install pymupdf")


def extract(pdf: pathlib.Path, outdir: pathlib.Path, first_page: int = 1) -> int:
    """Write one .txt per page of ``pdf`` into ``outdir``; return the count."""
    doc = fitz.open(pdf)
    outdir.mkdir(parents=True, exist_ok=True)
    for index in range(doc.page_count):
        printed = first_page + index
        text = doc[index].get_text("text")
        # Normalise the whitespace that OCR leaves between words/symbols but
        # keep the line structure: it carries the display-math layout.
        lines = [line.rstrip() for line in text.splitlines()]
        body = "\n".join(lines).strip() + "\n"
        (outdir / f"page-{printed:04d}.txt").write_text(body, encoding="utf-8")
    pages = doc.page_count
    doc.close()
    return pages


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=pathlib.Path)
    ap.add_argument("outdir", type=pathlib.Path)
    ap.add_argument(
        "--first-page",
        type=int,
        default=1,
        help="printed page number of the first PDF page (default: 1)",
    )
    args = ap.parse_args()

    if not args.pdf.is_file():
        sys.exit(f"no such file: {args.pdf}")

    pages = extract(args.pdf, args.outdir, args.first_page)
    last = args.first_page + pages - 1
    print(f"wrote {pages} pages to {args.outdir} "
          f"(pages {args.first_page}..{last})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())