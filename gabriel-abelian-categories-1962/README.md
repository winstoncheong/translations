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
theorems restart per chapter; lemmas restart per *section* while
corollaries start afresh after every *proposition* (Ch. V §6 prints
Corollaries 1--2 to Proposition 11, then 1--3 to Proposition 13, then
1--2 to Proposition 14, cited as "corollaire $N$ de la proposition
$M$"); and some corollaries are printed with no number at all (p. 360).
The preamble encodes this with separate counters plus a reset of the
corollary counter at each proposition, and those corollaries use the
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
| `ch1-03-functors.tex` | Functors | 330–333 |
| `ch1-04-additive-categories.tex` | Additive categories | 333–335 |
| `ch1-05-abelian-categories.tex` | Abelian categories | 335–336 |
| `ch1-06-generators-and-limits.tex` | Categories with generators and exact inductive limits | 336–338 |
| `ch1-07-adjoint-functors.tex` | Adjoint functors | 338–341 |
| `ch1-08-equivalences.tex` | Equivalences of categories | 341–342 |
| `ch1-09-enough-injectives.tex` | Abelian categories with enough injectives | 343–345 |
| `ch2-01-functor-categories.tex` | Functor categories | 345–348 |
| `ch2-02-left-exact-functors-abelian.tex` | Left exact functors with values in an abelian category | 348–354 |
| `ch2-03-left-exact-functors-groups.tex` | Left exact functors with values in abelian groups | 354–355 |
| `ch2-04-noetherian-categories.tex` | Noetherian categories | 355–358 |
| `ch2-05-injective-envelopes.tex` | Injective envelopes in abelian categories | 358–362 |
| `ch2-06-generators-and-limits.tex` | Categories with generators and exact inductive limits | 362–364 |
| `ch3-01-quotient-categories.tex` | Quotient categories | 365–369 |
| `ch3-02-section-functor.tex` | Properties of the section functor | 369–374 |
| `ch3-03-injective-envelopes.tex` | Categories with injective envelopes | 374–377 |
| `ch3-04-generators-and-limits.tex` | Categories with generators and exact inductive limits | 377–379 |
| `ch3-05-localizing-subcategories.tex` | A few examples of localising subcategories | 379–381 |
| `ch4-01-krull-dimension.tex` | The Krull dimension of an abelian category | 382–387 |
| `ch4-02-structure-of-injectives.tex` | The structure of injective objects in a locally noetherian category | 387–390 |
| `ch4-03-pseudocompact-modules.tex` | Pseudocompact modules | 390–395 |
| `ch4-04-duality.tex` | Duality between locally finite categories and pseudocompact modules | 395–402 |
| `ch5-01-module-categories.tex` | Module categories | 402–411 |
| `ch5-02-localisation.tex` | Localisation | 411–416 |
| `ch5-03-goldies-theorem.tex` | Goldie's theorem | 416–421 |
| `ch5-04-indecomposable-injectives.tex` | Indecomposable injectives and prime two-sided ideals | 421–426 |
| `ch5-05-stability-under-injective-envelopes.tex` | Stability under injective envelopes | 426–429 |
| `ch5-06-finite-extensions.tex` | Finite extensions of commutative noetherian rings | 429–436 |
| `ch5-07-krull-dimension-of-rings.tex` | The Krull dimension of some rings | 436–439 |
| `ch6-01-gluing-abelian-categories.tex` | Gluing of abelian categories | 439–441 |
| `ch6-02-properties-of-a-gluing.tex` | Properties of a gluing of abelian categories | 442–446 |
| `ch6-03-preschemes.tex` | Preschemes and abelian categories | 446–447 |
| `bibliography.tex` | Bibliography | 447–448 |

## Editorial decisions (running log)

Added as sections are translated. Recorded here because section files are not
allowed to touch this file.

### Mathematical mistakes in the original are emended, and the emendation is footnoted

Where Gabriel prints something that is wrong as mathematics — a transposed
index, a letter that must be another letter, an obviously vacuous
hypothesis — the translation **prints the corrected mathematics**, and an
editorial footnote records what the original said and what we print instead.
The `\ednote` macro in `preamble.tex` produces these, numbered per chapter
and prefixed "Translator's note" so they are distinguishable from the
original's own footnotes (of which there are none).

Emendations made so far:

| Place | Original prints | We print |
| --- | --- | --- |
| p. 345, Prop. 15 | $R'F$ onto $R^0F$ | $R'G$ onto $R^0G$ |
| p. 361, Corollaire | "$N'$ *of* $N$" | left as printed; footnoted |
| p. 354, Lemma 2 (§4) | italic *C* for the category | $\mathbf{C}$ |
| p. 350 | $\lim_{F\in\mathbf{S}_A} FS$ | $\lim_{S\in\mathbf{S}_A} FS$ |
| p. 358, Lemma 1 (§5) | "monomorphisme de source $Q$" | "morphisme"; footnoted |
| p. 361, complement | "$M\cap Q = 0$" | "$N\cap Q = 0$"; footnoted |
| p. 332 | $O_{M,N} = \eta_M\circ\varepsilon_N$ | $0_{M,N} = \eta_N\circ\varepsilon_M$; footnoted |
| p. 332 | $q'_M$ (second $M\Pi N$ projection) | $q'_N$; footnoted |
| p. 331 | $\operatorname{Hom}(\Cat,\Ab)$ for $X\mapsto\dot X$ | $\operatorname{Hom}(\Cat,\Ens)$; footnoted |
| p. 334 | $o_{N,M}$ neutral in $\operatorname{Hom}(M,N)$ | $0_{M,N}$; footnoted |
| p. 334 | $c(M)$ opposite in $\operatorname{Hom}(M,N)$ | $\operatorname{Hom}(M,M)$; footnoted |
| p. 336 | $M\cap N = \ker(M\to M/N\oplus M/P)$ | $N\cap P$; footnoted |
| p. 345 | $Gf_M$ ($f_M$ undefined) | $Gj_M$; footnoted |
| p. 409 | $R$-$A^c$-bimodule (enveloping algebra $A^e$ just defined) | $R$-$A^e$; footnoted |
| p. 410, Prop. 2(e) | $A/\mathfrak m A$ simple central ``over $A$'' | over $R/\mathfrak m$; footnoted |
| p. 411, $(e)\Rightarrow(d)$ | concludes ``assertion (c)'' | (d); footnoted |
| p. 415, Prop. 5 | ``si $a$ est nul'' (non-sequitur for $(\star\star)$) | ``si $s.a$ est nul''; footnoted |
| p. 415, Prop. 5 | target $A_F$ (notation $M_S$ just introduced) | $A_S$; footnoted |
| p. 427 | ``proposition 11'' reformulating Prop. 9(a) + Cor. 1 | Proposition 9; footnoted |
| p. 394, Cor. 3 | $h\circ g = \mathrm{id}_{\prod P_i}$ ($h\circ g\colon A\to A$) | $g\circ h$; footnoted |
| p. 435, Prop. 14 | $m'$ ``$A$-linear'' ($E$ has no $A$-structure) | $R$-linear; footnoted |
| p. 438, Cor. 1 | $\sigma^{-i}(\mathfrak a_i)=\sigma^{i-1}(\mathfrak a_{i+1})$ | $\sigma^{-i-1}(\mathfrak a_{i+1})$; footnoted |
| p. 440, Prop. 1 | $(FA,GA,\tau(A))$ ($F,G$ not defined on $\mathbf A$) | $(SA,TA,\tau(A))$; footnoted |
| p. 441 | $F\|U\cap V$ ($F$ not a sheaf) | $M\|U\cap V$ (resp.\ $N$); footnoted |

Two constraints on this, both stated in `AGENTS.md`:

- **Only emend what is unambiguously wrong.** Where two readings are possible,
  the choice is surfaced rather than made silently.
- **Stylistic quirks are left completely alone**, with no footnote. Archaic
  vocabulary, odd word order, "les sorties habituels" on p. 336, and
  inconsistent terminology are the author's voice, not errors.

The corollary on p. 361 is the worked example of the first constraint. Its
condition is vacuous as printed — both $M'$ and $N'$ are subobjects of $N$ —
but two emendations ("$N'$ de $M$" or "$M$ contient") are equivalent and the
text does not decide between them, so it is left as printed with a footnote
giving the likely intended reading.

### Some candidates were checked and are *not* errors

Recorded so that nobody "fixes" them later:

- **"$N + P$" (p. 336)** is correct as printed. The sentence contains both
  symbols side by side: $N + P$ is defined as the image of the morphism of
  $N \oplus P$ into $M$. The bare `+` is not a mis-typed `\oplus`.
- **Proposition 4's "$\sigma = \tau\circ\rho$" (p. 348)** is correct:
  $\sigma\colon F\to G$ is the morphism being factored through $R^0F$.
- **Lemma 1's "$S''\geq S$, $S''\geq S'$" (p. 349)** is correct as
  printed: $S''$ is a common upper bound of $S$ and $S'$ (right
  filtering), not a link in a chain. An earlier draft "corrected" this
  to a chain and was reverted.
- **The inductive-system morphism condition "$f_j\circ u_{ji} =
  v_{ji}\circ f_i$, $j > i$" (p. 337)** is correct as printed either:
  both sides go $M_i\to N_j$. An earlier draft transposed the indices
  (following the worked example that used to stand in `AGENTS.md`) and
  was reverted as ill-typed.

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