# tools/translation_report.py
"""Repository checks for the translation pipeline.

Three jobs, all dependency-free so they can run anywhere Python 3 runs:

1. ``progress``   -- how much of each document is actually translated, as a
   table for the CI job summary.
2. ``leftovers``  -- French text that survived into the English sources, i.e.
   forgotten passages that were never translated.
3. ``markers``    -- explicit TODO/untranslated markers.

Each document lives in a top-level directory containing ``src/main.tex``, e.g.::

    gabriel-abelian-categories-1962/src/

Each ``.tex`` file may declare its metadata in leading comments::

    %@ pages 324-327
    %@ status translated

Statuses: ``translated``, ``partial``, ``todo``.  Missing metadata is reported
rather than silently treated as finished.

Usage:
    python tools/translation_report.py [root] [--strict]
                                      [--format text|json|markdown]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

META_PAGE = re.compile(r"^%@\s*pages\s+(\S+)", re.MULTILINE)
META_STATUS = re.compile(r"^%@\s*status\s+(\S+)", re.MULTILINE)
KNOWN_STATUS = ("translated", "partial", "todo")

# ---------------------------------------------------------------------------
# Strip LaTeX so that leftover detection only looks at prose
# ---------------------------------------------------------------------------

MATH_ENVS = (
    "equation",
    "equation*",
    "align",
    "align*",
    "alignat",
    "alignat*",
    "gather",
    "gather*",
    "multline",
    "multline*",
    "eqnarray",
    "eqnarray*",
    "displaymath",
    "math",
    "array",
    "matrix",
    "pmatrix",
    "bmatrix",
    "cases",
    "split",
    "CD",
    "tikzcd",
)

_MATH_ENV_RE = re.compile(
    r"\\begin\{(" + "|".join(env for env in MATH_ENVS) + r")\}.*?\\end\{\1\}",
    re.DOTALL,
)
_MATH_RE = re.compile(r"\$\$.*?\$\$|\$.*?\$|\\\(.+?\\\)|\\\[.*?\\\]", re.DOTALL)
_COMMENT_RE = re.compile(r"(?<!\\)%.*?$", re.MULTILINE)
_VERBATIM_RE = re.compile(
    r"\\begin\{(verbatim|lstlisting|minted|thebibliography|filecontents)\}.*?\\end\{\1\}",
    re.DOTALL,
)
_CMD_RE = re.compile(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])*")
_ARG_RE = re.compile(r"\{([^{}]*)\}")
_WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+")

# Files that define the document's machinery rather than its content, and so
# have no pages of their own.  Everything else must declare %@ pages/%@ status.
SUPPORT_FILES = frozenset({"main.tex", "preamble.tex", "terminology.tex"})


def is_support_file(tex: pathlib.Path) -> bool:
    return tex.name in SUPPORT_FILES or tex.name.startswith("_")


def prose_only(text: str) -> str:
    """Reduce a LaTeX file to running prose, as far as is cheaply possible."""
    text = _VERBATIM_RE.sub(" ", text)
    text = _MATH_ENV_RE.sub(" ", text)
    text = _MATH_RE.sub(" ", text)
    text = _COMMENT_RE.sub(" ", text)
    text = PROPER_TITLES_RE.sub(" ", text)
    # Drop font/formatting commands but keep their text arguments.
    for _ in range(4):
        stripped = _CMD_RE.sub("", text)
        if stripped == text:
            break
        text = stripped
    # Drop the remaining brace groups (macro arguments, mostly labels).
    text = _ARG_RE.sub(" ", text)
    return text


# ---------------------------------------------------------------------------
# French leftover detection
# ---------------------------------------------------------------------------

# Function words that carry no meaning in an English sentence.  Words that are
# also valid English ("on", "certain", "me", "son", "te", "ta") are deliberately
# omitted: a false positive on every page is worse than missing a few.
FRENCH_STOPWORDS = frozenset(
    """
    alors ainsi afin ait apres après aupres auprès auquel aussi autre autres
    avaient avais avait avant avec ayant bien car ce ceci cela celle celles
    celui cependant certaines certains ces cet cette ceux chaque
    chez comme comment dans de dedans dehors deja depuis des deux doit donc
    dont du duquel elle elles en encore entre es est et etaient etait etant
    ete été etre être eu eux fait faire fois font hors ici il ils jamais
    jusqu laquelle le lequel les lesquelles lesquels leur leurs lors lorsque
    lui mais malgré moins ne ni nos notre nous nul ont ou oui par parce parmi
    pas pendant peu peut peuvent plusieurs pour pourquoi près puis quand que
    quel quelle quelles quels qui quoi sa sans se selon sera si sien sienne
    siens soi soit sommes sont sous soyez suis sur tandis tant tes toi ton
    toujours tous tout toute toutes tres très trop un une vers voici voila
    voilà vos votre vous y
    """.split()
)

# Names and titles that legitimately remain in French inside an English
# translation.  Matched case-insensitively as whole words.
ALLOWED = frozenset(
    """
    abelienne abeliennes abelien abeliens Gabriel Grothendieck Buchsbaum
    Cartan Eilenberg Serre Dieudonne Bourbaki numdam Numdam mathématique
    semantique préschéma
    """.split()
)

# Whole titles that must survive untranslated: journals, seminar series and
# book titles.  These are masked out before the prose is tokenised, otherwise
# every citation of the Bulletin reads as untranslated French.
PROPER_TITLES_RE = re.compile(
    r"(?:Bulletin\s+de\s+la\s+Soci[ée]t[ée]\s+Math[ée]matique\s+de\s+France)"
    r"|(?:S[ée]minaire\s+Bourbaki)"
    r"|(?:S[ée]minaire\s+Dubreil--Pisot)"
    r"|(?:S[ée]minaire\s+Cartan)"
    r"|(?:S[ée]minaire\s+J\.-P\.\s+Serre)",
    re.IGNORECASE,
)

MARKER_RE = re.compile(
    r"\\(?:todo|TODO|untranslated|toTranslate)\b|\bFIXME\b|\bXXX\b|\[\[\s*", re.IGNORECASE
)


def leftovers(text: str) -> list[tuple[str, str]]:
    """Return (word, context) pairs of French function words in the prose."""
    hits: list[tuple[str, str]] = []
    for lineno, line in enumerate(prose_only(text).splitlines(), start=1):
        for match in _WORD_RE.finditer(line):
            word = match.group(0)
            low = word.lower()
            if low in FRENCH_STOPWORDS and low not in ALLOWED:
                start = max(0, match.start() - 45)
                end = min(len(line), match.end() + 45)
                hits.append((word, line[start:end].strip()))
    return hits


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def parse_page_range(spec: str) -> tuple[int, int]:
    spec = spec.replace("--", "-").replace("\u2013", "-").replace("\u2014", "-")
    parts = spec.split("-")
    try:
        first = int(parts[0])
        last = int(parts[-1])
    except ValueError:
        return (0, 0)
    return (min(first, last), max(first, last))


def scan_document(doc_dir: pathlib.Path) -> dict:
    src = doc_dir / "src"
    files: list[dict] = []
    if not src.is_dir():
        return {"name": doc_dir.name, "files": [], "done": 0, "total": 0,
                "leftovers": [], "markers": [], "missing_meta": []}

    for tex in sorted(src.rglob("*.tex")):
        text = tex.read_text(encoding="utf-8")
        if is_support_file(tex):
            continue
        page_spec = META_PAGE.search(text)
        status_match = META_STATUS.search(text)
        rel = tex.relative_to(src.parent).as_posix()
        entry = {
            "file": rel,
            "status": status_match.group(1) if status_match else None,
            "pages": page_spec.group(1) if page_spec else None,
        }
        if not page_spec or not status_match:
            entry["missing_meta"] = True
            files.append(entry)
            continue
        if entry["status"] not in KNOWN_STATUS:
            entry["missing_meta"] = True
        lo, hi = parse_page_range(entry["pages"])
        entry["first"], entry["last"] = lo, hi
        files.append(entry)
        hits = leftovers(text)
        if hits:
            entry["leftovers"] = hits
        for m in MARKER_RE.finditer(text):
            entry.setdefault("markers", []).append(m.group(0))

    # Sections can share a page (a heading often lands at the foot of the
    # preceding page), so progress is measured as a union of pages rather
    # than a sum of ranges.
    covered: set[int] = set()
    translated: set[int] = set()
    declared: set[int] = set()
    for f in files:
        if f.get("missing_meta"):
            continue
        pages = set(range(f["first"], f["last"] + 1))
        declared |= pages
        if f["status"] == "translated":
            translated |= pages
        covered |= pages

    # meta.json, when present, gives the authoritative extent of the article.
    meta_path = doc_dir / "meta.json"
    total = len(declared)
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if meta.get("first_page") and meta.get("last_page"):
                total = meta["last_page"] - meta["first_page"] + 1
        except json.JSONDecodeError:
            pass

    return {"name": doc_dir.name, "files": files, "done": len(translated),
            "total": total, "covered": len(covered)}


def collect(root: pathlib.Path) -> list[dict]:
    """Find every document directory (any dir containing ``src/main.tex``)."""
    docs = []
    for main in sorted(root.rglob("main.tex")):
        src = main.parent
        if src.name != "src":
            continue
        # Skip anything inside a build directory.
        if any(part in {"build", "_build", "output"} for part in src.parts):
            continue
        docs.append(scan_document(src.parent))
    return docs


def render(doc: dict) -> str:
    pct = (100.0 * doc["done"] / doc["total"]) if doc["total"] else 0.0
    lines = [f"### {doc['name']}", "", "| file | pages | status |", "| --- | --- | --- |"]
    for f in doc["files"]:
        status = f["status"] or "**missing metadata**"
        lines.append(f"| `{f['file']}` | {f.get('pages') or '--'} | {status} |")
    lines += ["", f"**Translated: {doc['done']} / {doc['total']} pages ({pct:.1f}%)**"]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "root",
        type=pathlib.Path,
        nargs="?",
        default=pathlib.Path("."),
        help="directory to scan for documents (default: the repository root)",
    )
    ap.add_argument("--format", choices=("text", "json", "markdown"), default="text")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero when French leftovers or markers are found",
    )
    args = ap.parse_args()

    if not args.root.is_dir():
        sys.exit(f"no such directory: {args.root}")

    docs = collect(args.root)
    leftover_total = sum(len(f.get("leftovers", [])) for d in docs for f in d["files"])
    marker_total = sum(len(f.get("markers", [])) for d in docs for f in d["files"])
    meta_total = sum(1 for d in docs for f in d["files"] if f.get("missing_meta"))

    if args.format == "json":
        print(json.dumps(
            {"documents": docs,
             "leftovers": leftover_total,
             "markers": marker_total,
             "missing_metadata": meta_total},
            indent=2, ensure_ascii=False))
    elif args.format == "markdown":
        print("\n\n".join(render(d) for d in docs))
    else:
        for doc in docs:
            pct = (100.0 * doc["done"] / doc["total"]) if doc["total"] else 0.0
            print(f"{doc['name']}: {doc['done']}/{doc['total']} pages ({pct:.1f}%)")
            for f in doc["files"]:
                flag = " <-- missing metadata" if f.get("missing_meta") else ""
                print(f"    {f['status'] or '?':<12} {f.get('pages') or '?':<10} {f['file']}{flag}")
                for word, ctx in f.get("leftovers", [])[:8]:
                    print(f"        French? {word!r}: ...{ctx}...")
                if f.get("markers"):
                    print(f"        markers: {sorted(set(f['markers']))}")
        print()
        print(f"French leftovers: {leftover_total}")
        print(f"TODO markers:     {marker_total}")
        print(f"Missing metadata: {meta_total}")

    if args.strict and (leftover_total or marker_total):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())