# Phase 1: Checklist and reference triage

Purpose: decide in advance what this review must look at and which references it must read, so that scrutiny is systematic and not driven by first impressions.

## Part A: Checklist

Build a numbered list, P-1, P-2, …, of things to check, from three sources.

1. Every core card. They apply to any empirical paper.
2. Every technique or field card whose `applies_when` line matches something in the methods summary. Say which cards you selected, and which techniques used in the paper have no card.
3. Every user concern from intake, as the question you restated it into, tagged `user`.

For a technique that matters to the paper's headline and has no card, write up to five items from that field's standard practice, tagged `ad hoc`. Each must name a benchmark source, which goes through verification in Phase 7 like any other citation. An item whose benchmark cannot be verified stays on the list, marked as unverified judgement.

Give each item: the question, its source (card id, `user` or `ad hoc`), and where in the paper it applies. Drop card items that plainly do not apply to this paper, and say which you dropped.

The items are questions for Phase 3 and Phase 5 to answer. A paper that does not address an item has not thereby failed; whether the gap matters is decided claim by claim.

## Part B: Reference triage

For every reference in the paper's list, record:

- **Role.** What the paper uses it for: sole support for a claim; one of several supports; source of a number; basis of a method; theoretical basis; comparison or benchmark; background.
- **Where cited.**
- **Record check.** Whether the bibliographic record exists as cited: `matches`, `mismatch` (say which fields differ), `not found`, or `not checked` if you have no way to look it up.
- **Notices.** Any correction, expression of concern or retraction attached to the record you found.
- **Priority** for a deep-dive in Phase 4:
  - high: a headline or tier-3 claim leans on it as its sole or main support; or it supplies a key number or the theoretical basis of the argument; or it carries a retraction or expression of concern and any claim leans on it;
  - medium: it supports a tier-2 claim or justifies a method choice;
  - low: background.

Priority depends only on how much the paper's argument leans on the reference and on the state of its record. Who wrote it plays no part.

Then list:

- Incomplete or placeholder citations in the text, such as "[ref]" or a citation with no entry in the list.
- Relevant work the paper does not cite, only where you can name a specific source and say why a reader would expect it. Such a source goes through verification like any other.

Write both parts to `01_checklist_and_references.md`.
