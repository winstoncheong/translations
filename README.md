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
| `report` | translation progress, plus detection of untranslated French text and TODO markers; **fails** if a section file has no `%@` metadata |
| `build` | compiles every document in the TeX Live container and uploads the PDF as an artifact |
| `site` | assembles the PDFs and an index page (on the default branch) |
| `deploy` | publishes that site to GitHub Pages |

To enable the site: **Settings → Pages → Source: GitHub Actions**. Every
push to the default branch then rebuilds the PDFs and redeploys them.

The `report` job's French-leftover check is a safety net against passages that
were copied over instead of translated. It is a warning by default (a word list
cannot be perfect); run the workflow manually with the `strict` input to make
it fail the build.

## Tools

| Tool | Purpose |
| --- | --- |
| `tools/extract_ocr.py` | splits a scanned PDF's OCR text layer into one file per printed page |
| `tools/translation_report.py` | progress, leftover detection, metadata validation |
| `tools/make_site.py` | builds the GitHub Pages landing page from the compiled PDFs |

All three are dependency-free Python 3 (`extract_ocr.py` needs PyMuPDF).

## Working on a translation

Read [`AGENTS.md`](AGENTS.md) first. The short version: translate from the
page image, not the OCR text; keep one section per file; never invent
content; leave stubs in place rather than guessing.

## Licence and attribution

Translations here are derivative works. Each `meta.json` records the original's
copyright holder and licence (Gabriel 1962: © Bulletin de la Société
Mathématique de France, digitised by Numdam under CC BY-SA 4.0). Keep the
attribution notice in the front matter of each document.