# Checklist cards

A card is a short list of questions to ask of any claim that rests on a given technique or kind of evidence. Phase 1 builds a review's checklist from them: every card in `core/`, plus any card in another folder whose `applies_when` line matches the paper.

Cards exist so that a review asks the questions an experienced referee in that area would ask, whoever or whatever is doing the reviewing.

## Format

```markdown
---
id: T-EXAMPLE
name: Name of the technique or kind of evidence
type: technique
field: physics
applies_when: the paper does X, measures Y, or bases a claim on Z
version: "0.1"
---

# Name of the technique or kind of evidence

One or two sentences on what the technique is used to claim.

## 1. Short label

**Question.** A question that can be answered from the paper.

**Why it matters.** What can go wrong, in general terms, in one to three sentences.

**Resolved by.** What a paper shows when this is handled well.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Authors, Title, Venue volume, pages (year) | doi:10.xxxx/xxxxx | full text | Section and a one-line paraphrase of the supporting point |
```

- `id` starts with `C-` for a core card and `T-` for a technique card. `type` is `core` or `technique`.
- `field` is `any` for a core card; otherwise it matches the folder the card is in.
- `Access` is `full text` or `abstract`: the level the card's author actually reached when checking the source.

## Rules for cards

1. **Questions, not accusations.** Each item asks something a paper can answer well or badly. A paper that answers it well has earned the claim.
2. **General.** An item describes a recurring issue with the technique. It does not describe, or point at, any particular paper.
3. **Every benchmark was opened.** A source is listed only if the card's author opened it and found the supporting point there. The Sources table says where. A technique-card item with no source that could be opened is left out. A core-card item that is a matter of logic, not of field practice, may say "None needed" and give the reason.
4. **Benchmarks are sources a reader can find.** Prefer review articles, standards and recommendations from standards bodies, and well-known methods papers, open access where possible.
5. **Paraphrase.** Quote at most a phrase of under 15 words from any source.
6. **Short.** Five to eight items for a technique card, two to four for a core card.

## Adding a card

Put it in a folder named for its field (`physics/`, `chemistry/`, `biomedicine/`, …) and open a pull request. `CONTRIBUTING.md` in the repository describes the review a new card goes through.
