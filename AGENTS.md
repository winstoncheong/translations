# AGENTS.md

Operating instructions for coding agents (and people) working in this
repository. Read this before touching any `.tex` file.

## What this repository is

Translations of mathematical papers **into English**, typeset with LaTeX.
Each translated document is a top-level directory:

```
<author>-<short-title>-<year>/
  meta.json        bibliographic metadata; drives the website
  README.md        per-document notes: source, status, terminology decisions
  Makefile         local build, mirroring CI
  reference/       the original scan + its OCR text layer
  src/             the LaTeX sources  <-- the translation lives here
```

## Golden rules

1. **Never invent content.** If a passage is not translated, leave the stub
   and its `%@ status todo`. A missing translation is honest; a plausible
   invention is a serious defect.
2. **Check the page image, always.** `reference/ocr/*.txt` is OCR output and
   is wrong in predictable ways: subscripts and superscripts collapse,
   `0`/`o` and `1`/`l` are confused, ligatures (`œ`, `ﬁ`) are dropped, page
   numbers are misread (`327` → `827`, `374` → `3^4`, `447` → `44^`), and
   small capitals lose their case. Every formula, index and page number must
   be confirmed against the image in `reference/source.pdf`.
3. **Translate, don't paraphrase.** Keep Gabriel's sentences. Where he gives a
   definition as *data + axioms*, keep that shape so the translation can be
   checked against the original clause by clause.
4. **One section per file.** Do not merge sections into one file and do not
   split a section across files. This is what makes progress trackable.

## The `%@` metadata contract

Every content file under `src/` starts with:

```latex
%@ pages 328-330
%@ status translated
```

- `pages` are the pages of the **original** article, not of this translation.
- `status` is one of `translated`, `partial`, `todo`.

`main.tex`, `preamble.tex` and `terminology.tex` are exempt (they have no
pages). Everything else must declare both, or CI fails.

When you finish a section, change `todo` → `translated`. Nothing else in the
repository needs to be touched for progress to update: the report reads these
comments.

## Terminology

The authoritative table is `src/terminology.tex`. Policy:

- Use standard modern English where it exists, so results are findable in the
  current literature.
- Keep the French at first occurrence for coinages that are part of the
  history, then use the English.
- Keep established notation: bold upright for categories (`\mathbf{C}`), Fraktur
  for universes (`\Univ`), and Gabriel's `\dot\varphi` for natural
  transformations.
- New shared macros go in `src/preamble.tex`; document each in a comment.
- Record any decision you are unsure about in the document's `README.md`.

## Numbering of results — check the original, do not assume

Gabriel does **not** number his results with one counter. This is verified
against the scan, and getting it wrong makes every reference in the
translation wrong:

| Result | Restarts | Evidence |
| --- | --- | --- |
| Proposition | each **chapter**, continuous across its sections | Ch. I ends at Prop. 15 (p. 345); Ch. II opens at Prop. 1 (p. 346); §2 continues at Prop. 4 (p. 348) |
| Theorem | each **chapter** | "Théorème 1" on p. 338 and again on p. 356 |
| Lemma | each **section** | §1 of Ch. II runs to "Lemme 4" (p. 348), §2 opens with "Lemme 1" (p. 349) |
| Corollary | each **section** | p. 332, 344, 355, 358 each open a run at "Corollaire 1" |
| Definition / Remark | each **section** | — |

The environments in `preamble.tex` already do this: `theorem`, `proposition`,
`lemma`, `corollary`, `definition`, `remark`. Use them and never write a
literal number.

**Some corollaries carry no number.** The original prints a bare "Corollaire."
with a full stop and no figure (p. 360, between Proposition 9 and
Proposition 10). For those use the `unnumberedcorollary` environment. Check
the page: if the printed header has a number, it is numbered; if it reads
just "Corollaire.", it is not.

Never insert a `\setcounter` to make numbers line up. If the numbering looks
wrong, the transcription is wrong, not the counter.

## Diagrams

Use `tikz-cd` (already loaded in the preamble), not `xy`/`picture`. Match the
original's arrow labels and direction. Example:

```latex
\begin{tikzcd}
FM \arrow[r, "\dot\varphi^{(M)}"] \arrow[d, "Ff"'] & GM \arrow[d, "Gf"] \\
FN \arrow[r, "\dot\varphi^{(N)}"'] & GN
\end{tikzcd}
```

## Verifying your work

Other agents may be editing other sections of the same document at the same
time, so **do not run the shared build** — you will collide on the output
directory and you may be blamed for someone else's error. Verify your own
file in isolation instead:

```bash
cd <repo>/gabriel-abelian-categories-1962/src
mkdir -p /tmp/chk
cp preamble.tex terminology.tex /tmp/chk/
printf '\\input{preamble}\n\\begin{document}\n\\mainmatter\n\\input{YOURFILE}\n\\end{document}\n' > /tmp/chk/main.tex
cd /tmp/chk && pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Use a unique scratch directory if you are running several checks at once.
This catches every LaTeX error except those that depend on cross-references.

## Style

- British or American spelling: be consistent within a file. Existing files
  use **British** ("generalise", "recognise", "normalised").
- Date format, ranges: `1958--1959`, `pp.~323--448`.
- Use `~` for non-breaking spaces before references: `Chapter~VI`, `\S1`.
- Accents: UTF-8 directly (`géométrie`), not `\'e` — the escapes are error-prone.
- Do not reformat code you are not otherwise touching; keep diffs reviewable.

## Commit discipline

- One logical unit per commit: one section, or one infrastructure change.
- Say what was translated and from which pages, e.g.
  `Translate Ch. I §3 (Functors), original pp. 330-332`.
- Never commit `build/` output or the source PDFs; `.gitignore` covers both.