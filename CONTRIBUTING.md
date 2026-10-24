# Contributing

There are three ways to contribute: post a review, add or improve a checklist card, or propose a change to the method.

## Posting a review

Posted reviews live on the `reviews` branch, one folder per review.

### What can be posted

- **Publicly available papers only**: published articles and public preprints. Never a manuscript you received in confidence, such as one sent to you to referee.
- **Reviews made with this method**, with the run record complete: model, reasoning effort, tool, prompt, and whether the review was standard or focused.
- **Reviews a person has looked at.** `run.json` says what you checked. "none" is an acceptable answer; an invented one is not.
- **Claims and evidence, not people.** A review makes no statement about anyone's competence, motives or conduct.
- **Your conflicts of interest**, declared in `run.json`: a relationship with the authors, a competing result, a financial interest. "none" if there are none.

### What is never posted

- The paper itself, its figures, or long passages from it. Claims are quoted in a sentence or two; the validator enforces a limit.
- `00_extraction.md`, which reproduces the paper's abstract and reference list.

### Steps

1. Run the review. Fill in `reviewer` (your GitHub handle), `human_check` and `conflicts_of_interest` in `run.json`.
2. Check it:

   ```bash
   python3 plugin/skills/open-paper-reviewer/scripts/validate_review.py path/to/review --posting
   ```

3. Fork the repository and create a branch from `reviews`.
4. Put the review at `<paper-id>/<paper-version>/<your-handle>-<date>/`, where the names follow from `run.json`. The validator prints the expected path if you add `--check-path`. For example: `arxiv-0000.00000/v2/your-handle-2026-01-15/`.
5. Open a pull request against the `reviews` branch. The pull request may add or change files only inside your own review folder.

A check runs the validator on every pull request. A maintainer then reads the review for the rules above. Maintainers do not vouch for the correctness of posted reviews.

### Correcting or withdrawing a review

Open a pull request that changes your own folder. Set `review.status` in `run.json` to `corrected` or `withdrawn`, and for a correction describe the change in `07_verification.md`. Reviews are not deleted, so that the record stays intact.

### If your paper was reviewed

Open an issue with the "Author response" template. You can point out an error, supply material the review did not have, or ask for a correction. Responses are linked from the review.

## Checklist cards

Cards live in `plugin/skills/open-paper-reviewer/references/checklists/`. The format and rules are in the [README there](plugin/skills/open-paper-reviewer/references/checklists/README.md). In short:

- A card is a technique card (claims that rest on a technique) or a claim card (a kind of claim, whatever supports it). Core cards cover what applies to every paper.
- Each item is a question a paper can answer well or badly, written in general terms. It does not describe or point at any particular paper.
- Every benchmark source was opened by you, and the Sources table says where in the source the support is and what access you had.
- Cards go in a folder for their field and subfield, such as `physics/condensed-matter/`. New fields get a new folder beside `physics/`, and every new folder gets a `README.md` whose heading is its title.
- The index of cards has two levels: a top-level list of folders with the names of their cards, then one index per folder with each card's `applies_when` line. Physics is the only field so far. Once other fields are added, the index may need a third level: fields, then subfields, then cards.

Before opening a pull request:

```bash
python3 scripts/check_card.py path/to/your-card.md
```

```bash
python3 scripts/check_card_sources.py path/to/your-card.md
```

```bash
python3 scripts/build_prompts.py
```

The first checks the format. The second looks up each DOI and compares the record with your reference text. The third adds your card to its folder's index and to the top-level list the skill reads. None of them can tell whether a source supports an item, so a reviewer will open a sample of your sources.

## Changing the method

The method is the set of files under `plugin/skills/open-paper-reviewer/references/`: the rules, the rubric, the phase instructions and the templates. The prompts in `prompts/` and parts of `METHODOLOGY.md` are generated from them.

1. Open an issue first for anything beyond a wording fix, saying what problem the change solves.
2. Edit the files under `references/`. Keep phase files free of instructions specific to one tool; those belong in `SKILL.md`.
3. Regenerate and test:

   ```bash
   python3 scripts/build_prompts.py
   ```

   ```bash
   python3 -m unittest discover -s tests
   ```

4. If you changed the rubric, the phases or the rules, raise the version in both `plugin/.claude-plugin/plugin.json` and `plugin/.codex-plugin/plugin.json`, and in the skill's frontmatter. Reviews record the version they were made with.
5. If you have Claude Code, run the regression cases:

   ```bash
   claude plugin eval ./plugin --ablation none --scaffold --allow-tools Write Edit "Bash(python3 *)"
   ```

## Licence of contributions

By contributing you agree that what you contribute, whether text, cards, reviews or code, is released under the MIT License, like the rest of the repository.
