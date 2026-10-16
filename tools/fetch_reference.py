#!/usr/bin/env python3
"""Fetch a document's reference material: the original scan and its OCR text.

Neither is kept in the repository -- the scan is large and the OCR text is
derivable from it -- so a fresh clone has to fetch them before translating.
This does both in one step, from the URL recorded in ``meta.json``.

    python tools/fetch_reference.py gabriel-abelian-categories-1962

Equivalent to, but tidier than:

    curl -L -o <doc>/reference/source.pdf <meta.json:source>
    python tools/extract_ocr.py <doc>/reference/source.pdf \\
        <doc>/reference/ocr --first-page <meta.json:first_page - 1>

Requires PyMuPDF for the OCR step: ``pip install pymupdf``.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.request

UA = "math-translations/1.0 (+https://github.com/; reference fetcher)"


def download(url: str, dest: pathlib.Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        print(f"  scan already present ({dest.stat().st_size / 1e6:.1f} MB); "
              "delete it to refetch")
        return
    print(f"  fetching {url}")
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=300) as response:
        if response.headers.get("Content-Type", "").startswith("text/html"):
            sys.exit(
                f"  {url} returned HTML, not a PDF. Check meta.json:source."
            )
        data = response.read()
    dest.write_bytes(data)
    print(f"  wrote {dest} ({len(data) / 1e6:.1f} MB)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("document", type=pathlib.Path,
                    help="document directory, e.g. gabriel-abelian-categories-1962")
    ap.add_argument("--force", action="store_true",
                    help="refetch the scan even if it is already present")
    args = ap.parse_args()

    doc_dir: pathlib.Path = args.document
    meta_path = doc_dir / "meta.json"
    if not meta_path.is_file():
        sys.exit(f"no meta.json in {doc_dir}")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    source = meta.get("source")
    if not source:
        sys.exit(f"{meta_path} has no \"source\" URL")
    first_page = meta.get("first_page", 1)

    print(f"{doc_dir.name}: {meta.get('title', '?')}")
    pdf_path = doc_dir / "reference" / "source.pdf"
    if args.force and pdf_path.exists():
        pdf_path.unlink()
    download(source, pdf_path)

    try:
        from extract_ocr import extract
    except ImportError:
        sys.exit("PyMuPDF is required for the OCR step: pip install pymupdf")
    except Exception as exc:  # pragma: no cover
        sys.exit(f"cannot import extract_ocr: {exc}")

    print("  extracting the OCR text layer")
    pages = extract(pdf_path, doc_dir / "reference" / "ocr", first_page - 1)
    last = first_page + pages - 1
    print(f"  wrote {pages} pages to reference/ocr "
          f"(printed pages {first_page}..{last})")
    print("Done. Note the OCR text mangles mathematics: always check the "
          "page image in reference/source.pdf.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())