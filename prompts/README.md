# Generic prompts

These prompts carry the OpenPaperReviewer method to any LLM. They are generated from the same files the skill uses, so they say the same thing. Do not edit them by hand; change the files under `plugin/skills/open-paper-reviewer/references/` and run `python3 scripts/build_prompts.py`.

| File | Use it when |
|---|---|
| `full-review-prompt.md` | Your model can take the whole method at once. It includes the core checklist cards and an index of the other cards by folder, with links. |
| `phase-prompts/`, in `open-paper-reviewer-phase-prompts-<version>.zip` on each [release](https://github.com/sinkomr/OpenPaperReviewer/releases/latest) | Your model's context is small, or you want to run and inspect one phase at a time. |

## Running a full review

1. Start a new conversation and paste the prompt.
2. Fill in the "Details of this run" block. The model identifier and the reasoning-effort setting must come from you: read them from the tool's model picker or settings. A model's own guess at what it is does not count.
3. Attach the paper, or paste its text, with any supplementary material. If the paper uses a technique or makes a kind of claim that has a card in the index at the end of the prompt, paste that card in too; the model will also ask for the ones it needs.
4. The model asks whether you have specific concerns about the paper or want a standard review. Answer it.
5. The model works one phase at a time and stops after each. Save each document under its file name and reply "continue".
6. At the end, save `run.json`, `prompt.md`, `claims.json` and `citations.json`.

If your tool has no web access, the review still runs. Every outside source is marked unverified and the synthesis says so. Open and check those sources yourself before relying on any statement that rests on one.

## Running phase by phase

Each file in `phase-prompts/` is a complete prompt for one phase, with only the parts of the rubric that phase uses, and lists what to paste in with it. Run them in order, 00 to 07, each in a new conversation, saving the output of each as the files it names.

## Checking the result

With Python 3 installed, check the saved folder:

```bash
python3 plugin/skills/open-paper-reviewer/scripts/validate_review.py path/to/review-folder
```

The validator reports anything missing or outside the rubric. To post the review, see [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## If you changed the prompt

Set `method.modified` to `true` in `run.json` and put the full changed text in `prompt.md`, so that readers know the review was not made with the published method.
