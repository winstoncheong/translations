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
| Corollary | after each **proposition** (fresh 1, 2, … run per proposition) | Ch. V §6 prints Cors. 1--2 to Prop. 11, then 1--3 to Prop. 13, then 1--2 to Prop. 14, cited as "corollaire $N$ de la proposition $M$" |
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

## Mistakes and typos in the original

Gabriel prints a fair number of slips. When you meet one — a transposed
index, a letter that must be another letter, an obviously vacuous
hypothesis — do all three of these:

1. **Print the corrected mathematics in the translation.** The reader wants
   the right statement, not a faithful copy of a wrong one.
2. **Add an editorial footnote at that point** recording what the original
   actually printed and that it has been corrected. Use the `\ednote` macro:
   ```latex
   maximal for the equality $N\cap Q = 0$\ednote{The original prints
   $M\cap Q = 0$; since $Q$ is a subobject of $M$ this would force $Q$
   itself to be zero. We print $N\cap Q = 0$, the only reading under
   which the complements below make sense.}
   ```
   (An earlier version of these instructions used a p.~337 index
   "transposition" as its example; the scan shows the original is
   type-correct there and the "correction" was the error. Examples in
   this file must themselves be checked against the page image.)
3. **Note it in the file header comment** as well, so the next agent sees it.

The footnote is a record of an emendation, not an apology: it must say what
was printed and what we print instead. `\ednote` prints "Translator's note."
so emendations are distinguishable from Gabriel's own footnotes (there are
none). Footnote numbers restart with each chapter.

Two rules of judgement:

- **Only emend what is unambiguously wrong.** If you are confident the
  intended reading is unique, correct it. If two readings are possible, do
  not pick one silently — either leave the print and note the difficulty, or
  ask.
- **Stylistic quirks are not mistakes.** Odd phrasing, unusual word order,
  inconsistent terminology and archaic vocabulary are the author's voice.
  Leave them completely alone, with no note. Reserve `\ednote` for things
  that are wrong as mathematics.

## Diagrams

Use `tikz-cd` (already loaded in the preamble), not `xy`/`picture`. Match the
original's arrow labels and direction.

**Two tikz-cd gotchas in this TeX Live**, both of which have already cost time:

- The braces-only label form does **not** work: `\arrow[r, {a,b}]` is passed
  straight to `pgfkeys` and fails with "I do not know the key `/tikz/abc`".
  Use the quoted form: `\arrow[r, "a,b"]`.
- With the quoted form, any comma *inside* the label must be braced, because
  `pgfkeys` splits the options on top-level commas before the quotes library
  sees them:
  ```latex
  \arrow[r, "\operatorname{Hom}(\dot X{,}f)"]   % works
  \arrow[r, "\operatorname{Hom}(\dot X,f)"]    % fails
  ```
  A braced comma is visually identical, so this costs nothing typographically.
  Leave a short `%` comment at any diagram where you had to do this.

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

## PDF conventions

- **Bibliographical back-references are wanted.** Load `hyperref` with
  `pagebackref`, e.g. `\usepackage[pagebackref]{hyperref}`, so each
  bibliography entry ends with the pages on which it is cited. This is the
  preference for new and touched documents; do not convert an existing
  document solely to add it.
- Keep `hyperref` colour links on (`colorlinks`), as in the existing
  preambles.
- `pagebackref` writes a `.brf` file. It is a build artefact: never commit
  it. The repository `.gitignore` covers `*.brf`.

## Commit discipline

- One logical unit per commit: one section, or one infrastructure change.
- Say what was translated and from which pages, e.g.
  `Translate Ch. I §3 (Functors), original pp. 330-332`.
- Never commit `build/` output or the source PDFs; `.gitignore` covers both.
- **Pushing is authorised once a translation is complete and committed.**
  Finish the job first: all sections translated, the full build green
  (exit 0, no `^!` errors, no undefined references), the report at 100%,
  and `git status` clean apart from intended files. Then commit and
  `git push origin <branch>`. Do not push a half-translated or broken
  tree, and re-fetch/rebase before pushing if the remote has moved.
- CI builds only the documents whose directory changed. A push that touches
  only this file, `tools/`, or the root `README.md` rebuilds nothing; touch a
  document directory to rebuild that document. A `.github/` change is the
  exception: it builds every document so the workflow itself is exercised.
  Manual dispatch always builds everything.