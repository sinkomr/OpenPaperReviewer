# Checklist cards

A card is a short list of questions an experienced referee would ask. Phase 1 builds a review's checklist from them: every card in `core/`, plus every other card whose `applies_when` line matches the paper. The index of cards has two levels, so that a review reads only what it needs: `INDEX.md` lists the core cards and every folder of other cards with the names of the cards in it, and each folder's own `INDEX.md` gives the `applies_when` line of every card in that folder. A review reads the top-level index, then the index of each folder that could apply, and opens only the cards that match.

Cards exist so that a review asks the questions an experienced referee in that area would ask, whoever or whatever is doing the reviewing.

## Three kinds of card

- **Core** cards (`core/`) apply to any empirical paper: evidence, controls, statistics, uncertainty, processing, consistency, citations, availability.
- **Technique** cards apply to claims that rest on a measurement, synthesis or analysis technique, such as neutron scattering or Thomson scattering.
- **Claim** cards apply to a kind of claim, whatever technique supports it, such as a claim of superconductivity or of quantum advantage. They ask what evidence a careful demonstration of that kind of claim needs, and which ordinary explanations it must exclude.

## Format

```markdown
---
id: T-EXAMPLE
name: Name of the technique or kind of claim
type: technique
field: physics/condensed-matter
applies_when: the paper does X, measures Y, or bases a claim on Z
version: "0.1"
---

# Name of the technique or kind of claim

One or two sentences on what the technique is used to claim, or what the kind of claim asserts.

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

- `type` is `core`, `technique` or `claim`. The `id` is upper case and starts with `C-` for a core card, `T-` for a technique card and `CL-` for a claim card.
- `field` is `any` for a core card. For any other card it is the folder the card is in, for example `physics/condensed-matter`.
- `name` is plain: no parentheses. Put abbreviations in the opening sentence.
- `applies_when` is at most 45 words. It goes into the folder's `INDEX.md`, which every review of a paper in that area reads.
- `Access` is `full text` or `abstract`: the level the card's author actually reached when checking the source.

## Rules for cards

1. **Questions, not accusations.** Each item asks something a paper can answer well or badly. A paper that answers it well has earned the claim.
2. **General.** An item describes a recurring issue with the technique or the kind of claim. It does not describe, or point at, any particular paper, group or controversy.
3. **Every benchmark was opened.** A source is listed only if the card's author opened it and found the supporting point there. The Sources table says where. A technique or claim item with no source that could be opened is left out. A core-card item that is a matter of logic, not of field practice, may say "None needed" and give the reason.
4. **Benchmarks are sources a reader can find.** Prefer review articles, standards and recommendations from standards bodies, and well-known methods papers, open access where possible.
5. **Paraphrase.** Quote at most a phrase of under 15 words from any source.
6. **Short.** Two to four items for a core card; five to eight for a technique or claim card.
7. **No repeats of the core cards.** A technique or claim card asks what is specific to its technique or kind of claim. General questions about statistics, controls or data availability belong to the core cards.

`python3 scripts/check_card.py <card>` checks the format of a card. `python3 scripts/check_card_sources.py <card>` checks that each source's record exists and matches. Neither checks that a source supports its item: that needs someone to open it.

## Folders

Cards live in a folder for their field and, for large fields, a subfolder for the subfield: `physics/condensed-matter/`, `physics/particle/` and so on. Each folder has a `README.md` whose heading is the folder's title in the index. The `INDEX.md` files, the top-level one and one per folder, are generated from the cards by `scripts/build_prompts.py`; do not edit them by hand.

Physics is the only field so far, so the top-level index lists its subfields directly. Once other fields are added, the index may need a third level to keep the top level short: fields, then subfields, then cards.

## Adding a card

Put it in the folder for its field and subfield, run `python3 scripts/build_prompts.py` to update the indexes, and open a pull request. A new folder also needs a `README.md` with its title as the heading. `CONTRIBUTING.md` in the repository describes the review a new card goes through.
