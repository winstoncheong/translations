# Gabriel (1962) — *Abelian Categories* — English translation

Translation of **Pierre Gabriel, *Des catégories abéliennes***, Bulletin de la
Société Mathématique de France **90** (1962), 323–448.

- Original (Numdam): <https://www.numdam.org/item/10.24033/bsmf.1583/>
- Scan used: `reference/source.pdf` (git-ignored; re-fetch from the URL above)
- OCR text layer: `reference/ocr/page-NNNN.txt`, one file per printed page
- DOI: [10.24033/bsmf.1583](https://doi.org/10.24033/bsmf.1583)

This is also Gabriel's doctoral thesis (Thèse Sc. math., Paris, 1961).

## Why this paper is worth translating

It is the paper that fixes the meaning of *abelian category*, and the first
systematic treatment of injectivity, localising subcategories, noetherian
categories and localisation in general. Most of the vocabulary in use today was
coined or given its final sense here, and several notions that later became
central — the exactness conditions on functors, Krull dimension of a category,
pseudocompact modules — appear here for the first time. The Introduction alone
is a compact statement of the whole programme.

## Status

126 pages. Page numbering in the translation is aligned with the original, so
translation page 328 = original page 328 (the alignment drifts slowly, since
English prose runs longer than French; section and theorem numbering do not
drift at all).

`python tools/translation_report.py .` from the repository root gives the
current figure.

## Editorial decisions

These are the choices a reader is most likely to query. The full table lives in
`src/terminology.tex`.

**"Foncteur" is translated "functor", not Gabriel's coinage.** Some digitised
tables of contents and secondary sources render this as *fondeur*; that is an
artefact. Gabriel writes *foncteur* for what Grothendieck would later call a
*covariant functor*, reserving *contravariant* for the opposite variance — the
distinction he insists on throughout §3. Reading "fondeur" as a separate
notion is a transcription error, and the OCR text layer of this very scan
contains it.

**"Morphisme functoriel" becomes "natural transformation".** Gabriel also
glosses it as "functorial morphism"; the modern name is used, with the French
at first occurrence.

**"Catégorie avec générateurs et limites inductives exactes" is left
untranslated** as "a category with generators and exact inductive limits",
rather than rendered "Grothendieck category". The modern name postdates this
paper by several years, and the section title is one of Gabriel's own.

**"Préschéma" is "prescheme"**, not "scheme"; Gabriel is careful about the
distinction throughout Chapter VI.

**"Recollement" is "gluing"** in Chapter VI, with the French retained where
useful.

**Definitions keep their original shape** — a list of data followed by a list
of axioms — so that the translation can be checked against the French clause by
clause. This is why Chapter I §2 reads as verbosely as it does.

**Result numbering follows the original's irregular scheme, not a single
running counter.** Gabriel numbers propositions continuously across the
sections of a chapter and restarts them at each chapter (Chapter I ends at
Proposition 15 on p. 345; Chapter II opens at Proposition 1 on p. 346);
theorems restart per chapter; lemmas and corollaries restart per *section*;
and some corollaries are printed with no number at all (p. 360). The preamble
encodes this with four separate counters, and those corollaries use the
`unnumberedcorollary` environment. This was established by reading the page
images — the obvious assumption (one counter throughout) is wrong.

**Bibliography titles are given in English** with the printed title in
parentheses. Front matter carries the copyright notice of the Société
Mathématique de France and states that the French original is authoritative.

## Structure

One file per section of the original, in `src/`, in the original's order:

| File | Section | Original pages |
| --- | --- | --- |
| `frontmatter.tex` | Title, preface, contents, terminology table | 322–324 |
| `introduction.tex` | Introduction | 324–327 |
| `ch1-01-univers.tex` | Grothendieck universes | 328 |
| `ch1-02-categories.tex` | Definition of categories | 328–330 |
| `ch1-03-functors.tex` | Functors | 330–332 |
| `ch1-04-additive-categories.tex` | Additive categories | 333–334 |
| `ch1-05-abelian-categories.tex` | Abelian categories | 335 |
| `ch1-06-generators-and-limits.tex` | Categories with generators and exact inductive limits | 336–337 |
| `ch1-07-adjoint-functors.tex` | Adjoint functors | 338–340 |
| `ch1-08-equivalences.tex` | Equivalences of categories | 341–342 |
| `ch1-09-enough-injectives.tex` | Abelian categories with enough injectives | 343–344 |
| `ch2-01-functor-categories.tex` | Functor categories | 345–347 |
| `ch2-02-left-exact-functors-abelian.tex` | Left exact functors with values in an abelian category | 348–353 |
| `ch2-03-left-exact-functors-groups.tex` | Left exact functors with values in abelian groups | 354 |
| `ch2-04-noetherian-categories.tex` | Noetherian categories | 355–357 |
| `ch2-05-injective-envelopes.tex` | Injective envelopes in abelian categories | 358–361 |
| `ch2-06-generators-and-limits.tex` | Categories with generators and exact inductive limits | 362–364 |
| `ch3-01-quotient-categories.tex` | Quotient categories | 365–368 |
| `ch3-02-section-functor.tex` | Properties of the section functor | 369–373 |
| `ch3-03-injective-envelopes.tex` | Categories with injective envelopes | 374–376 |
| `ch3-04-generators-and-limits.tex` | Categories with generators and exact inductive limits | 377–378 |
| `ch3-05-localizing-subcategories.tex` | A few examples of localising subcategories | 379–381 |
| `ch4-01-krull-dimension.tex` | The Krull dimension of an abelian category | 382–386 |
| `ch4-02-structure-of-injectives.tex` | The structure of injective objects in a locally noetherian category | 387–389 |
| `ch4-03-pseudocompact-modules.tex` | Pseudocompact modules | 390–394 |
| `ch4-04-duality.tex` | Duality between locally finite categories and pseudocompact modules | 395–401 |
| `ch5-01-module-categories.tex` | Module categories | 402–410 |
| `ch5-02-localisation.tex` | Localisation | 411–415 |
| `ch5-03-goldies-theorem.tex` | Goldie's theorem | 416–420 |
| `ch5-04-indecomposable-injectives.tex` | Indecomposable injectives and two-sided ideals | 421–425 |
| `ch5-05-stability-under-injective-envelopes.tex` | Stability under injective envelopes | 426–428 |
| `ch5-06-finite-extensions.tex` | Finite extensions of commutative noetherian rings | 429–435 |
| `ch5-07-krull-dimension-of-rings.tex` | The Krull dimension of some rings | 436–438 |
| `ch6-01-gluing-abelian-categories.tex` | Gluing of abelian categories | 439–441 |
| `ch6-02-properties-of-a-gluing.tex` | Properties of a gluing of abelian categories | 442–445 |
| `ch6-03-preschemes.tex` | Preschemes and abelian categories | 446 |
| `bibliography.tex` | Bibliography | 447–448 |

## Editorial decisions (running log)

Added as sections are translated. Recorded here because section files are not
allowed to touch this file.

### Typos and slips in the original are reproduced, not corrected

Where Gabriel prints something that is plainly a slip, the translation
follows the print and the file header records it. Known cases so far:

| Place | What's printed | Handling |
| --- | --- | --- |
| p. 345, Prop. 15 | "$F$" where the context demands "$G$" | reproduced |
| p. 361, Corollaire | "$N'$ *of* $N$" where "$M$" is meant | reproduced |
| p. 354, Lemma 2 (§4) | "*C*" in italics where **C** is meant | reproduced |
| p. 337 | $f_j\circ u_{ji} = v_{ji}\circ f_i$, indices transposed | reproduced |

Each is noted in the comment header of its own file. Nothing has been silently
corrected; if a reader prefers emendations, they belong in footnotes.

### Notation decided here

- **Zero object**: Gabriel prints it inconsistently (`O` on p. 336, italic
  `o` elsewhere). The translation uses `0` throughout, which is the modern
  convention and unambiguous in context.
- **Hook arrow** `X \longmapsto F` for Gabriel's wavy arrow.
- **`somme fibrée` / `produit fibré`** are rendered "coproduct" / "product",
  per the terminology policy.
- **Fraktur where Gabriel uses it**: the Coim→Im morphism is `\mathfrak{S}`,
  the set of isomorphism classes `\mathfrak{E}`; the semisimple subcategory
  is `\mathbf{S}`, consistent with `\Cat` = `\mathbf{C}`.
- **Bold upright** for categories and object/morphism sets throughout, as in
  the original.

### Page ranges do not align with section boundaries

Sections run on past the page on which the next one starts: §9 of Ch. I ends
on p. 345, §1 of Ch. II ends on p. 348, §5 ends on p. 336 and §6 on p. 338, §3
of Ch. II ends on p. 355 and §4 on p. 358. Pages are therefore *shared* between
adjacent files. The `%@ pages` range of each file is the true extent of that
section, and `tools/translation_report.py` counts a union of ranges, so nothing
is double-counted. Ranges that are still provisional are noted in the
respective file headers.

## Working on this document

Read `../../AGENTS.md` first. In particular:

- Draft from `reference/ocr/`, but **confirm every formula against the page
  image**. The OCR layer of this scan is unreliable in ways that matter here:
  it renders `\operatorname{Hom}` as `Hom^`, loses subscripts, and misreads
  page numbers in the table of contents (`369` → `366`, `447` → `44^`,
  `374` → `3^4`). The page ranges in the table above were corrected against
  the images.
- Keep `%@ status todo` until the section is genuinely complete.
- British spelling, `~` before references, UTF-8 accents.