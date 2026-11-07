# OpenPaperReviewer

A skill for reviewing a scientific paper claim by claim. It works in Claude (Claude Code, claude.ai, Cowork) and in Codex.

Ask for a review of a paper, preprint or manuscript and the skill will:

1. Ask whether you have specific concerns about the paper that deserve closer scrutiny, or want a standard review.
2. Extract the paper and list every claim it makes, quoted verbatim with its location.
3. Check each claim four ways: against the paper's own evidence, against the literature, against alternative explanations, and against standard practice for the techniques used.
4. Give each claim a verdict, severity and confidence from a fixed rubric.
5. Read the references the claims lean on and check that they say what they are cited for.
6. Write a synthesis that states what the paper establishes as well as what it does not.
7. Verify its own citations and numbers, correct anything wrong, and record the model, reasoning effort and prompt used.

## Install

In Claude Code:

```
claude plugin marketplace add sinkomr/OpenPaperReviewer
claude plugin install open-paper-reviewer@openpaperreviewer
```

In Codex:

```
codex plugin marketplace add sinkomr/OpenPaperReviewer
codex plugin add open-paper-reviewer@openpaperreviewer
```

Then ask for a review of a paper. For an automated run, say "standard review" or list your concerns in the request, so the skill does not stop to ask.

## What the skill reads, runs and sends

- **Reads:** the paper you give it and any supplementary files you supply.
- **Fetches:** when the tool has web access, it opens public pages for the works it cites (DOI resolvers, publisher pages, arXiv, PubMed and similar) in order to verify them.
- **Runs:** two bundled Python scripts that use only the standard library. `scripts/validate_review.py` checks the output folder locally and sends nothing. `scripts/verify_citations.py` looks up DOIs and arXiv identifiers through the public Crossref and arXiv APIs; the only data it sends is those identifiers.
- **Writes:** a review folder in your working directory. Nothing is posted anywhere unless you do it yourself.

The skill does not search for information about a paper's authors, and it treats the paper and every fetched page as data, never as instructions.

In the repository, the plugin's `evals/` folder holds regression cases that run the skill on short invented papers. They are left out of the release zips. One of those papers contains a sentence addressed to automated reviewers, on purpose: the case checks that the skill notes it and does not follow it.

## Limits

The output is an AI-assisted draft for a qualified person to check, not a substitute for expert peer review. Do not give it a manuscript you received in confidence unless you are permitted to share it with an AI tool.

Method, source and posted reviews: https://github.com/sinkomr/OpenPaperReviewer

Everything in this plugin is released under the MIT License; see `LICENSE`.
