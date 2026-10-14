# Template: run-record

Two files record how the review was produced: `run.json` and `prompt.md`. Start both in Phase 0 and complete them in Phase 7. A review that does not state the model, the reasoning effort and the prompt cannot be posted, because nobody could compare or reproduce it.

## run.json

```json
{
  "schema_version": "0.1",
  "method": {
    "name": "OpenPaperReviewer",
    "version": "0.1.0",
    "commit": null,
    "entry": "skill",
    "modified": false
  },
  "paper": {
    "title": "Title of the paper",
    "identifier": "arXiv:0000.00000",
    "version": "v2",
    "public": true,
    "supplementary_provided": true
  },
  "review": {
    "started": "2026-01-15",
    "finished": "2026-01-15",
    "mode": "standard",
    "intake": "asked",
    "concerns": [],
    "status": "active",
    "citation_verification": "all"
  },
  "tool": {
    "name": "Name of the tool the review ran in",
    "version": "1.2.3"
  },
  "models": [
    {
      "name": "Model name",
      "id": "exact-model-identifier",
      "id_source": "reported_by_tool",
      "effort": "high",
      "effort_source": "reported_by_tool",
      "phases": ["0", "1", "2", "3", "4", "5", "6", "7"]
    }
  ],
  "prompt_file": "prompt.md",
  "web_access": true,
  "reviewer": "github-handle",
  "human_check": "What a person checked, or none",
  "conflicts_of_interest": "none"
}
```

Field notes:

- **method.entry** is `skill` or `prompt`. **method.modified** is true if the instructions were changed in any way; `prompt.md` must then contain the full changed text. **method.commit** is the repository commit if known, otherwise null.
- **paper.identifier** is `doi:…`, `arXiv:…` or a URL. **paper.version** is the version reviewed: an arXiv version, "published version", or the date on a draft. **paper.public** says whether anyone can obtain the paper.
- **review.mode** is `standard` or `focused`. **review.concerns** holds the concerns as given, verbatim; it is empty for a standard review. **review.intake** is `asked`, `stated_in_request` or `not_interactive`.
- **review.citation_verification** is `all`, `partial` or `none`, set in Phase 7 from the citations table.
- **tool.version** is the version the tool reports, or the one the person running the review gives. If neither is available, write `unknown`. The validator warns about an unknown tool version but accepts it.
- **models** has one entry for each model that did any of the work, and together they must cover phases 0 to 7.
  - `id` is the exact identifier. `effort` is the reasoning-effort or thinking setting as the tool shows it. If the tool has no such setting, write `none exposed`.
  - `id_source` and `effort_source` are `reported_by_tool` when the tool showed the value to the model, and `supplied_by_user` when the person running the review gave it.
  - Never fill these in from the model's own impression of what it is. If the tool does not show a value, ask the person running the review.
- **reviewer**, **human_check** and **conflicts_of_interest** are needed to post a review. `human_check` says what a person actually checked. "none" is an acceptable answer; an invented one is not.

## prompt.md

```markdown
# Prompt record

## Request

The message or messages that started the review, verbatim.

## Intake

Question asked: the question verbatim, or "not asked: stated in the request", or "not asked: the run was not interactive".
Answer: verbatim.

## Method

One of:
- OpenPaperReviewer skill <version>, unmodified.
- Generic prompt `<file name>` from OpenPaperReviewer <version>, unmodified.
- Modified instructions: the full text follows.

## Later instructions

Any later message that changed the scope or direction of the review, verbatim, with the phase it arrived in. "None" if there were none.
```
