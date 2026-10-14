# Template: claims-and-citations

Two tables carry the review's results in a form that can be checked by a program and compared across reviews. Both are written in Phase 7. Every value comes from the rubric, in its exact words.

## claims.json

One entry per claim in the registry.

```json
{
  "schema_version": "0.1",
  "claims": [
    {
      "id": "A-01",
      "group": "A",
      "text": "The claim, verbatim from the paper.",
      "location": "Abstract; Sec. 3, Fig. 2a",
      "type": "observation",
      "tier": 1,
      "headline": false,
      "verdict": "Supported",
      "severity": null,
      "confidence": "High",
      "blocked_by": [],
      "basis": ["paper: Fig. 2a"],
      "summary": "One line on why."
    },
    {
      "id": "B-02",
      "group": "B",
      "text": "Another claim, verbatim.",
      "location": "Sec. 4",
      "type": "interpretation",
      "tier": 3,
      "headline": true,
      "verdict": "Unsupported",
      "severity": "Critical",
      "confidence": "Medium",
      "blocked_by": [],
      "basis": ["paper: Sec. 4, no control shown", "C-002"],
      "summary": "One line on why."
    }
  ]
}
```

Rules:

- `text` is verbatim and within the rubric's quote limit; `summary` is within its summary limit.
- `severity` is null exactly when the verdict is Supported.
- `blocked_by` lists claim ids. A blocked claim is never Supported.
- `basis` entries are either `paper: <location>` or a citation id. A Contradicted verdict or a Critical severity needs at least one basis that can be checked: a location in the paper, or a citation whose status is confirmed or corrected.

## citations.json

One entry for every outside source the review cites anywhere, including sources that were later dropped.

```json
{
  "schema_version": "0.1",
  "citations": [
    {
      "id": "C-001",
      "reference": "Authors, Title, Venue volume, pages (year)",
      "identifier": "doi:10.0000/example",
      "url": "https://example.org/where-it-was-read",
      "used_for": ["B-02", "methods"],
      "access": "full_text",
      "status": "confirmed",
      "error": null,
      "quote": "A short supporting quotation from the source.",
      "note": ""
    }
  ]
}
```

Rules:

- `used_for` lists claim ids and any of the labels `checklist`, `references`, `methods`, `synthesis`.
- `access` is the level actually reached in this run: `full_text`, `abstract`, `metadata` or `none`.
- `status` is `confirmed`, `corrected`, `removed` or `unverified`. Confirmed and corrected both require access of `full_text` or `abstract`, a `quote` within the rubric's limit, and an identifier or URL.
- `error` is null for a confirmed source. For a corrected one it says what was wrong: `misattributed`, `unsupported`, `nonexistent` or `other`. The note says what was changed.
- A source that was cited and then dropped keeps its entry with status `removed`, so the record shows what the review got wrong along the way.
