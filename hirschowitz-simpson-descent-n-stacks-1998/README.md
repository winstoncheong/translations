# Hirschowitz–Simpson (1998; rev. 2001) — *Descent for n-Stacks* — English translation

Translation of **André Hirschowitz and Carlos Simpson, *Descente pour les
n-champs***, arXiv:math/9807049v3 (13 March 2001; first version 1998).

- Abstract page: <https://arxiv.org/abs/math/9807049v3>
- Source: <https://arxiv.org/e-print/math/9807049v3> (a single gzipped `.tex`,
  not a tarball)
- Modernized source used as the starting point:
  `../arxiv-fixes/math_9807049v3/`
- The original PDF has 250 pages; page references in this translation are to
  that PDF (1–250).

The paper develops the theory of Segal $n$-stacks by systematic use of closed
model categories, proves the descent theorem for left Quillen presheaves, and
applies it to $n$-stacks and to complexes of $\mathcal O$-modules.

## Source and method

The French source is a single LaTeX file. It was modernized in
`arxiv-fixes/math_9807049v3` (LaTeX 2.09 → LaTeX 2e, real section structure,
`hyperref`, `T1`/`lmodern`, a proofreading pass). That modernized file is the
base of this translation: the mathematics, notation, labels and result
numbering are carried over unchanged, and only the prose is translated.

The authors' own English **Abstract** is reproduced verbatim. The French
**Résumé** is not reprinted: it duplicates the abstract. The v2/v3 errata
headers in the source are the authors' text and are preserved in the
corresponding places.

## Status

**Translated in full** (250/250 pages of the original). The per-file
`%@ status` comments in `src/` are the single source of truth;
`python tools/translation_report.py .` from the repository root reads them.
The build produces 183 pages, because the English is set in 11pt Latin
Modern on A4 with narrower margins than the authors' 12pt layout and because
the translation is more compact than the French; the page range in
`%@ pages` always refers to the original PDF, not to this translation.

The numbering of results is the original's: one shared counter per section,
printed as `Lemma 2.1`, `Theorem 2.2`, `Proposition 2.3`, and so on. Every
result environment shares that counter. Do not insert `\setcounter` to make
numbers line up: if they look wrong, the transcription is wrong. Spot checks
against the authors' own v3 errata confirm the numbers: Theorem 12.1,
Theorem 19.4, Theorem 20.1 and Theorem 20.5 in this translation are the
results the errata calls 12.1, 19.4, 20.1 and 20.5.

## Editorial decisions

**`cmf` is translated `cmc`.** The French abbreviates *catégorie de modèles
fermée*; the authors' own English abstract writes *closed model category
(cmc)*. The abbreviation `cmc` is used throughout, including in prose where
the French says `cmf`.

**`n-champ` / `préchamp` / `champ` are `n-stack` / `prestack` / `stack`.**
These are the authors' terms and the standard English ones. `champ de
modules` is `moduli stack`; `recollement` is `gluing`.

**`topologie grossière` is `coarse topology`**, not "gross topology".

**`compatible aux changements de base (ccb)` is `compatible with base change
(cbc)`**, and the abbreviation `cbc` is used in §11. The original's labels
`ccb1` and `cestccb` are left unchanged, since labels are not prose.

**`donnée de descente généralisée (dddg)` is `generalised descent data
(gdd)`.** The abbreviation is introduced in the introduction and used later.

**`n-précat` is `n-precategory`, not `n-prestack`.** The authors abbreviate
*n-précatégorie de Segal* as *n-précat de Segal*. This is a different notion
from *n-préchamp de Segal* (prestack): `nSePC` is the category of Segal
n-precategories, and a Segal n-prestack is a presheaf with values in
`nSePC`. The translation keeps the two apart: `n-precategory` for `n-précat`,
`prestack` for `n-préchamp`. Confusing them is easy because the words differ
by one letter, and a first pass did so in several sections; the files were
corrected against the French.

**`section équilibrée` / `eq-section` is `balanced section` / `eq-section`.**
This is the authors' own term, used once in the Introduction and defined in
§16 (an eq-section is a section σ for which the maps σ^r(f) are
equivalences). The abbreviation `eq` stands for French *équilibrée*
("balanced"); it is not "equi-free" or "equivariant". There is no established
English term, so the Introduction prints "balanced sections (or eq-sections)"
with a translator's note, and later sections keep the authors' abbreviation
`eq-section`.

**`Fl(A)` and `Fl^i(A)(x,y)` are kept.** They denote the Segal category of
1-morphisms and its iterated versions; the notation is the authors'.

**`section équilibrée (eq-section)` is `balanced section (eq-section)`**,
with the authors' parenthetical kept.

**`nSeCAT`, `nSeCHAMP`, `nCHAMP`, `Cpx_O`, `qis` are kept unchanged.** They
are notation, not prose.

**Bibliographic titles are left in the language in which they were printed.**
Only the authors' annotations in the reference list (URLs, "available at",
"to appear", "in preparation") are translated. A translated title would not
be searchable, and inventing one would be a silent editorial intervention.
As a consequence the French-leftover detector of
`tools/translation_report.py` reports words such as *des* and *et* inside
bibliographic titles; this is expected and is not an untranslated passage.

**The translation does not silently correct the mathematics.** Where a
formula looks wrong, it is translated as printed and the point is recorded
in `meta.json` (`warnings`) or in the file header. The only emendations are
delimiter repairs and obvious slips, each noted with `\ednote` or a `%`
comment. The authors' v3 errata already record the main mathematical error
(Proposition 6.1/Lemma 6.2 and its consequences for 10.11, 12.1, 14.4, 15.8,
19.4, 21.1); that text is preserved rather than independently re-checked.

**British spelling**, as elsewhere in this repository: *generalise*,
*localisation*, *fibre*, *characterisation*.

## Structure

One file per numbered section of the original, in the original's order. The
21 sections are numbered; the subsection headings are unnumbered
(`\subnumero`), exactly as in the original.

| File | Section | Original pages |
| --- | --- | --- |
| `frontmatter.tex` | Title, abstract, translator's note, contents | 1–3 |
| `ch01-introduction.tex` | Introduction | 4–16 |
| `ch02-segal-n-categories.tex` | Segal $n$-categories | 17–35 |
| `ch03-segal-n-prestacks.tex` | Segal $n$-prestacks | 36–49 |
| `ch04-functorialities.tex` | The functorialities $p^*$, $p_*$, $p_!$ | 50–53 |
| `ch05-bousfield-kan-structure.tex` | The Bousfield–Kan-type structure after Hirschhorn | 54–60 |
| `ch06-localisation-viewpoint.tex` | The localisation viewpoint | 61–67 |
| `ch07-segal-and-simplicial-categories.tex` | Segal categories and simplicial categories | 68–72 |
| `ch08-dwyer-kan-localisation.tex` | Dwyer–Kan localisation | 73–86 |
| `ch09-first-definition-of-stack.tex` | A first definition of stack | 87–93 |
| `ch10-criteria-for-stacks.tex` | Criteria for a prestack to be a stack | 94–107 |
| `ch11-internal-model-categories.tex` | Internal model categories | 108–124 |
| `ch12-universal-family.tex` | The universal family | 125–135 |
| `ch13-associated-stack.tex` | The stack associated to a prestack | 136–143 |
| `ch14-limits.tex` | Limits | 144–146 |
| `ch15-more-on-descent.tex` | A little more on the descent condition | 147–153 |
| `ch16-grothendieck-construction.tex` | The Grothendieck construction | 154–171 |
| `ch17-quillen-presheaves.tex` | Quillen presheaves | 172–184 |
| `ch18-strictification.tex` | Strictification | 185–208 |
| `ch19-descent-for-left-quillen-presheaves.tex` | Descent for left Quillen presheaves | 209–222 |
| `ch20-example-descent-for-n-stacks.tex` | Example: descent for $n$-stacks | 223–232 |
| `ch21-example-descent-for-complexes.tex` | Example: descent for complexes | 233–241 |
| `bibliography.tex` | References | 242–250 |

## Working on this document

Read `../../AGENTS.md` first. The short version:

- One file per section; do not merge or split sections.
- Keep `%@ pages` and `%@ status` current; change `todo` → `translated` only
  when the section is genuinely complete.
- Translate sentences, not paragraphs. Keep definitions in their
  data-then-axioms shape so they can be checked against the French clause by
  clause.
- Keep every formula, index, superscript and label. Confirm against the
  source; do not "improve" notation.
- Use `\ednote{...}` only for an unambiguous mathematical error, and say what
  the original printed and what is printed instead.
- Build with `make` (or `latexmk -pdf -outdir=build src/main.tex`). The
  repository CI builds each document in a TeX Live container.

## Known differences and open issues

- The printed layout is modern (standard LaTeX headings, `hyperref` links)
  rather than the authors' manual `\numero` layout. Section and result
  numbering are unchanged.
- Pagination differs from the arXiv PDF because the translation is in
  English and uses Latin Modern; `%@ pages` always refers to the original
  PDF, not to this translation.
- The v3 errata is preserved, not independently verified. In particular the
  paper's own correction says that 6.1/6.2 hold only for $n$-truncated
  prestacks and that 10.11, 14.4(c) and 15.8(c) apply only to $n$-prestacks;
  Theorem 19.4 gains hypothesis (5); Corollary 21.1 remains valid for
  complexes bounded below. See the comment header of the source.
- Delimiter repairs and other emendations are recorded in the individual
  file headers.
