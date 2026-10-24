# OpenPaperReviewer

An open method for reviewing a scientific paper claim by claim, with a skill that runs it in Claude and Codex, a prompt that runs it in any other LLM, and a place to post the results.

A review made this way lists every claim the paper makes, quoted verbatim, and gives each one a verdict from a fixed rubric after the same four checks. The review verifies its own citations before it is finished, and records the model, reasoning effort and prompt that produced it. The result can be audited one claim at a time, and compared with someone else's review of the same paper.

## What a review contains

- A registry of the paper's claims, each quoted with its location.
- For each claim: what in the paper supports it, whether the cited literature agrees, which ordinary explanations were not excluded, how it compares with standard practice, and a verdict, severity and confidence.
- A close reading of the references the argument leans on, checking that they say what they are cited for.
- A synthesis that states what the paper establishes as well as what it does not, and what would settle the open questions.
- A verification log: every source the review cites, whether it was opened, and what was corrected.
- A run record: model, effort, tool, prompt, and what a person checked.

[`METHODOLOGY.md`](METHODOLOGY.md) explains the method and the reasoning behind it.

## Running a review

Before any analysis, the reviewer asks whether you have specific concerns about the paper that deserve closer scrutiny, or want a standard review. For an automated run, say "standard review" or list your concerns in the request.

### In Claude

Claude Code:

```bash
claude plugin marketplace add sinkomr/OpenPaperReviewer
```

```bash
claude plugin install open-paper-reviewer@openpaperreviewer
```

In claude.ai or Cowork, add this repository under Customize > Plugins, or upload `open-paper-reviewer-plugin-<version>.zip` from the latest release as a plugin. To add only the skill, upload `open-paper-reviewer-skill-<version>.zip` as a skill.

Then ask for a review of a paper: "Review this paper" with the file attached or its path given.

### In Codex

```bash
codex plugin marketplace add sinkomr/OpenPaperReviewer
```

```bash
codex plugin add open-paper-reviewer@openpaperreviewer
```

Then ask for a review, or invoke the skill directly with `$open-paper-reviewer`.

### In any other LLM

Paste [`prompts/full-review-prompt.md`](prompts/full-review-prompt.md) into a new conversation and follow [`prompts/README.md`](prompts/README.md). There is a version with the physics checklist cards, and a set of single-phase prompts for models with a small context.

## Posted reviews

Reviews of publicly available papers are collected on the [`reviews` branch](https://github.com/sinkomr/OpenPaperReviewer/tree/reviews) of this repository. Each one states the model, effort and prompt used and what a person checked.

To post one, see [`CONTRIBUTING.md`](CONTRIBUTING.md). Authors of a reviewed paper can respond or ask for a correction by opening an issue.

## Limits

- A review made with this method is an AI-assisted draft for a qualified person to check. It is not peer review.
- The method is not yet calibrated on sound papers: how often it downgrades a claim that deserves to stand has not been measured. [`METHODOLOGY.md`](METHODOLOGY.md) records what is known.
- A model's own citations are a known source of error. The method makes checking them a required phase, and every review reports which of its sources were confirmed and which were not. A review run without web access marks every source unverified.
- Do not give a manuscript you received in confidence to an AI tool unless you are permitted to.
- The method reviews papers, not people. It does not look up authors.

## What is in this repository

| Path | Contents |
|---|---|
| [`METHODOLOGY.md`](METHODOLOGY.md) | The method, explained |
| [`plugin/`](plugin/) | The plugin that installs in Claude and Codex |
| [`plugin/skills/open-paper-reviewer/`](plugin/skills/open-paper-reviewer/) | The skill: rules, rubric, phase instructions, templates, checklist cards and two scripts |
| [`prompts/`](prompts/) | The same method as prompts for any LLM, generated from the skill |
| [`scripts/`](scripts/) | Tools for maintaining the repository |
| [`tests/`](tests/) | Tests for the validator and the checklist cards, with a small fictional review as the fixture |
| `reviews` branch | Posted reviews |

The checklist cards cover experimental physics so far. Cards for other fields are welcome; the format is in [`checklists/README.md`](plugin/skills/open-paper-reviewer/references/checklists/README.md).

## Licence

Everything in this repository, including the method, templates, checklist cards, prompts, scripts and posted reviews, is released under the [MIT License](LICENSE).

To cite the method: OpenPaperReviewer, version 0.1.0, https://github.com/sinkomr/OpenPaperReviewer.
