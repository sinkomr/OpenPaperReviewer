<!-- Keep the section that applies and delete the other. -->

## Posting a review (target branch: `reviews`)

- Paper (title and identifier):
- [ ] The paper is publicly available. It is not a manuscript I received in confidence.
- [ ] `validate_review.py <folder> --posting --check-path` passes.
- [ ] `run.json` states the model, reasoning effort and prompt, what a person checked, and my conflicts of interest.
- [ ] The review criticizes claims and evidence, and says nothing about the authors as people.
- [ ] The folder contains no copy of the paper, its figures or `00_extraction.md`.
- [ ] This pull request changes files only inside my review folder.

## Changing the method, a card or the tooling (target branch: `main`)

- What problem does this solve?
- [ ] `python3 -m unittest discover -s tests` passes.
- [ ] `python3 scripts/build_prompts.py` was run and its output is included.
- [ ] For a card: I opened every source listed and recorded in `card-sources/` where each supports the card, and `scripts/check_card_sources.py` reports no mismatch.
- [ ] For a change to the rubric, phases or rules: the version is raised in both plugin manifests and in the skill.
