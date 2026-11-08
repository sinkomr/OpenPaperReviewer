---
name: open-paper-reviewer
description: Review a scientific paper claim by claim. Use when the user asks to review, referee, critique, fact-check or audit a research paper, preprint or manuscript, or asks whether a paper's claims are supported by its evidence and citations. Extracts every claim verbatim, checks each against the paper's own evidence, the literature, alternative explanations and standard practice, assigns a verdict from a fixed rubric, verifies the review's own citations, and records the model, effort and prompt used.
license: MIT
metadata:
  short-description: Claim-by-claim review of a scientific paper
  version: "0.1.0"
---

# OpenPaperReviewer

Review a scientific paper claim by claim. Every claim is quoted, checked four ways and given a verdict from a fixed rubric, and the review's own citations are verified before anything is delivered.

The method lives in this skill's `references/` folder. Paths below are relative to the folder that holds this file.

## Before you start

1. Read `references/rules.md`. Those rules hold in every phase.
2. Read `references/rubric.json`: every value, limit and rule the method uses.
3. Locate the paper: a PDF, a text or LaTeX file, or a URL or identifier you can fetch. Many claims rest on what a figure shows, so view the pages or images where your tool can, and do not rely on extracted text alone. Check that the paper actually reached you: a read of a very large PDF can come back empty without an error. If you received no text, or no page images, get a readable copy first (read it in page ranges, render the pages to images, or ask for a smaller file). Never review from the title, the abstract or memory.
4. Choose the output folder: `opr-review-<short-paper-name>/` in the working directory, unless the user names one. If it already holds phase files, this is a resumed run. Continue from the first phase whose output is missing and do not redo finished phases.

## Phases

Run the phases in order. Read each phase file when you reach it, and read a template when a phase names it (`references/templates/<name>.md`).

| Phase | Instructions | Output |
|---|---|---|
| 0 Intake and extraction | `references/phases/00-intake-and-extraction.md` | `run.json`, `prompt.md`, `00_extraction.md` |
| 1 Checklist and reference triage | `references/phases/01-checklist-and-references.md` | `01_checklist_and_references.md` |
| 2 Claims registry | `references/phases/02-claims-registry.md` | `02_claims_registry.md` |
| 3 Per-claim scrutiny | `references/phases/03-per-claim-scrutiny.md` | `03_scrutiny/group_<letter>.md` |
| 4 Reference deep-dives | `references/phases/04-reference-deep-dives.md` | `04_references/ref_<number>.md` |
| 5 Methods deep-dive | `references/phases/05-methods-deep-dive.md` | `05_methods.md` |
| 6 Synthesis | `references/phases/06-synthesis.md` | `06_synthesis.md` |
| 7 Verification | `references/phases/07-verification.md` | `07_verification.md`, `claims.json`, `citations.json` |

Checklist cards for Phase 1 are in `references/checklists/`. Start at its `INDEX.md`, which says how to choose them.

After Phase 2, tell the user in a few lines what you found: how many claims in which groups, which cards were selected, which references are on the reading list, and any supplementary material that is missing. Then carry on without waiting for a reply.

## The intake question

Phase 0 opens with the intake question. Ask it in the phase file's words, then stop and wait for the answer before doing anything else, unless the phase file says not to ask.

## Sub-agents

The whole method works in a single agent from start to finish. Where your tool can run sub-agents, these phases can go to them; it is worth doing for a long paper, and seldom for a short one:

- Phase 1, Part A: one sub-agent selects the cards and writes the checklist, with the path of each card it selected, into `01_checklist_and_references.md`, so the indexes and cards stay out of your context for the rest of the run. Give it the concerns as restated at intake. Then read the checklist and write Part B yourself. If a later phase needs the detail of a card, open that card.
- Phase 3: one sub-agent per claim group, up to about six at a time.
- Phase 4: one sub-agent for every one or two references.
- Phase 7: a fresh sub-agent that has not seen the reasoning behind the review.

Give each sub-agent `references/rules.md`, `references/rubric.json`, the phase file, the templates that phase names, and the earlier outputs it needs: `00_extraction.md` for Phase 1; the paper, `00_extraction.md`, the checklist and the registry for Phases 3 and 4; the paper and every file for Phase 7. In a run nobody is watching, run sub-agents in the foreground, or do not end your turn until all of them have finished: the session can stop when your turn ends, and their work is lost. This matters most for Phase 7, the last thing a run does. Read what each sub-agent wrote, and correct any value that is not in the rubric. Add a sub-agent that ran on a different model or effort to `models` in `run.json`, with its phases.

## Scripts

Both scripts need only Python 3 and its standard library.

- `scripts/validate_review.py <output folder>` checks the finished folder against the method's rules. Run it at the end of Phase 7 and fix everything it reports. Add `--posting` for a review that will be posted publicly.
- `scripts/verify_citations.py <file>` looks up DOIs and arXiv identifiers and reports records that do not match the reference text, and any correction or retraction on them. It needs network access and sends only the identifiers. In Phase 1, run it once on a JSON list of the paper's references that have an identifier, `[{"id": "12", "reference": "Authors, Title, Venue (year)", "identifier": "doi:…"}]`, instead of looking up each record. In Phase 7, run it on `citations.json`. It checks records, not content: whether a source supports a statement still has to be judged by reading it.

If you cannot run scripts, check the same things by hand against `references/templates/claims-and-citations.md`.

## Without web access

Run every phase. Mark every outside source as unverified, set the citation-verification line to `none`, and say in the first lines of the synthesis that no citation was checked. Verdicts of Contradicted and severities of Critical then need a basis in the paper itself.

## When you finish

Tell the user:

- where the review folder is;
- the assessment of each headline claim, and how many claims received each verdict;
- the citation-verification status and any source left unverified;
- what could not be evaluated, and why;
- that this is an AI-assisted draft for a qualified person to check.

To post the review publicly, the paper must be publicly available, and `run.json` needs the reviewer's GitHub handle, what a person checked and a conflict-of-interest statement. The steps are in `CONTRIBUTING.md` at https://github.com/sinkomr/OpenPaperReviewer.
