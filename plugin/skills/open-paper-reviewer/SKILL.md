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
2. Read `references/rubric.json`. Every verdict, severity, confidence, access level and status comes from it, in its exact words. Its `limits` set the quote lengths and word budgets, and its `rules` are part of the method.
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

Checklist cards for Phase 1 are in `references/checklists/`: every card in `core/`, plus any card in the other folders whose `applies_when` line matches the paper. Read only the cards you select.

After Phase 2, tell the user in a few lines what you found: how many claims in which groups, which cards were selected, which references are on the reading list, and any supplementary material that is missing. Then carry on without waiting for a reply.

## The intake question

Phase 0 opens by asking the user whether they have specific concerns about the paper or want a standard review. Ask it in the words the phase file gives, then stop and wait for the answer before doing anything else.

- Skip the question only if the request already says "standard review" or already lists concerns.
- Go ahead without an answer only if you have been told that the run is automated or that you must not ask questions. Then run a standard review and record the intake as `not_interactive`.
- If you are unsure whether anyone can answer, ask and stop. The user can reply in the next message.

## Recording the model, effort and tool

Record the model identifier and reasoning-effort setting that your tool reports to you. If the request itself states them, use those and record them as supplied by the user. If neither gives you a value, ask the user. If you cannot ask, write `unknown`: the validator will then report the run record as incomplete, and the person running the review must fill it in before the review can be posted.

Record the tool's name and version the same way. Some tools do not show their version to the model, and a command that would print it may need approval you cannot get. Then ask the user if you can; if you cannot, write `unknown`. An unknown tool version does not stop a review from being posted: the validator only warns about it.

## Sub-agents

The whole method works in a single agent from start to finish. Where your tool can run sub-agents, three phases split well:

- Phase 3: one sub-agent per claim group, up to about six at a time.
- Phase 4: one sub-agent for every one or two references.
- Phase 7: a fresh sub-agent that has not seen the reasoning behind the review.

In a run nobody is watching (headless, scheduled or scripted), run each sub-agent in the foreground and wait for its result. If your tool can only run them in the background, do not end your turn while any of them is still working: an unattended session can stop when your turn ends, and the unfinished work is lost. This matters most for Phase 7, the last thing a run does.

Give each sub-agent `references/rules.md`, `references/rubric.json`, the phase file, the templates that phase names, and the earlier outputs it needs: `00_extraction.md`, the checklist and the registry for Phases 3 and 4, and every file for Phase 7. Read what each sub-agent wrote before moving on, and correct any value that is not in the rubric. If a sub-agent ran on a different model or effort from yours, add it to `models` in `run.json` with the phases it ran.

## Scripts

Both scripts need only Python 3 and its standard library.

- `scripts/validate_review.py <output folder>` checks the finished folder against the method's rules. Run it at the end of Phase 7 and fix everything it reports. Add `--posting` to apply the extra rules for a review that will be posted publicly.
- `scripts/verify_citations.py <output folder>/citations.json` looks up each DOI and arXiv identifier and reports records that do not match the reference text. It needs network access and sends only the identifiers. It checks records, not content: whether a source supports a statement still has to be judged by reading it.

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

If the user wants to post the review to the public OpenPaperReviewer repository, the paper must be publicly available and `run.json` needs their GitHub handle, a statement of what a person checked, and a conflict-of-interest statement. The steps are in `CONTRIBUTING.md` at https://github.com/sinkomr/OpenPaperReviewer.
