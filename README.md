# Mathematics translations

English translations of mathematical papers, typeset with LaTeX and published
as PDFs by GitHub Actions.

The point is not to paraphrase old papers but to make them *usable*: modern
English, modern notation where it has stabilised, the original's definitions
kept intact, and enough editorial apparatus that a reader can check any claim
against the French original page by page.

---

## Documents

| Document | Original | Progress |
| --- | --- | --- |
| [Abelian Categories](gabriel-abelian-categories-1962/) | P. Gabriel, *Des catégories abéliennes*, Bull. Soc. Math. France **90** (1962), 323–448 | 11/126 pp. |
| [Descent for n-Stacks](hirschowitz-simpson-descent-n-stacks-1998/) | A. Hirschowitz, C. Simpson, *Descente pour les n-champs*, arXiv:math/9807049v3 (2001) | 250/250 pp. |

Run `python tools/translation_report.py .` for current figures.

## How a document is laid out

```
<author>-<title>-<year>/
  meta.json        bibliographic metadata (drives the website)
  README.md        source, status, and the editorial decisions taken
  Makefile         local build — same commands CI runs
  reference/
    source.pdf     the original scan (git-ignored; re-fetch from meta.json)
    ocr/           one .txt per printed page, from the PDF's text layer
  src/
    main.tex       driver: inputs every section in order
    preamble.tex   document class, packages, theorem environments, macros
    terminology.tex the translation's terminology table
    <section>.tex  ONE FILE PER SECTION of the original
```

Each section file carries its own status in comments:

```latex
%@ pages 330-332
%@ status translated
```

`python tools/translation_report.py .` turns those comments into the progress
numbers, the website progress bars and the CI job summary. Nothing else needs
updating when a section is finished.

## Getting started

The reference material is **not** in the repository. The scanned original is
large and the per-page OCR text is derived from it, so both are fetched on
demand from the URL recorded in each document's `meta.json`:

```bash
pip install pymupdf
python tools/fetch_reference.py gabriel-abelian-categories-1962
```

That downloads `reference/source.pdf` and splits its OCR text layer into
`reference/ocr/page-NNNN.txt`, one file per printed page. The script is
idempotent — it skips the download if the scan is already there, and
`--force` refetches.

Then build:

```bash
cd gabriel-abelian-categories-1962 && make     # -> build/main.pdf
```

## Building

Locally, with any current TeX Live (2023 or later is fine):

```bash
cd gabriel-abelian-categories-1962
make            # -> build/main.pdf
```

CI uses the `texlive/texlive:latest` container image so that the build is
reproducible and independent of the runner. Pin the image in
`.github/workflows/ci.yml` if a TeX Live update ever breaks a build.

## Continuous integration

`.github/workflows/ci.yml` runs on every push and pull request:

| Job | What it does |
| --- | --- |
| `discover` | finds every directory containing `src/main.tex` |
| `changes` | maps changed paths to document directories; manual runs and `.github/` changes build everything, a push that only touches `AGENTS.md` or `tools/` builds nothing |
| `report` | translation progress, plus detection of untranslated French text and TODO markers; **fails** if a section file has no `%@` metadata |
| `build` | compiles the **changed** documents in the TeX Live container and uploads each PDF as an artifact |
| `site` | assembles fresh PDFs plus previously deployed ones (fetched from the live site) and an index page, on the default branch |
| `deploy` | publishes that site to GitHub Pages |

To enable the site: **Settings → Pages → Source: GitHub Actions**. A push
that changes a document rebuilds that document and redeploys the site;
unchanged PDFs are reused from the current deployment rather than rebuilt.

Build artifacts are kept for 7 days (`retention-days: 7`); they only need to
survive the site job of the same run. The published PDFs on Pages are
independent of that retention.

The `report` job's French-leftover check is a safety net against passages that
were copied over instead of translated. It is a warning by default (a word list
cannot be perfect); run the workflow manually with the `strict` input to make
it fail the build.

## Tools

| Tool | Purpose |
| --- | --- |
| `tools/fetch_reference.py` | downloads a document's scan and extracts its OCR text (one command, from `meta.json`) |
| `tools/extract_ocr.py` | splits a scanned PDF's OCR text layer into one file per printed page |
| `tools/translation_report.py` | progress, leftover detection, metadata validation |
| `tools/make_site.py` | builds the GitHub Pages landing page from the compiled PDFs |

The first needs PyMuPDF (`pip install pymupdf`); the others are
dependency-free Python 3.

## Working on a translation

Read [`AGENTS.md`](AGENTS.md) first. The short version: translate from the
page image, not the OCR text; keep one section per file; never invent
content; leave stubs in place rather than guessing.

## Licence and attribution

Translations here are derivative works. Each `meta.json` records the original's
copyright holder and licence (Gabriel 1962: © Bulletin de la Société
Mathématique de France, digitised by Numdam under CC BY-SA 4.0). Keep the
attribution notice in the front matter of each document.