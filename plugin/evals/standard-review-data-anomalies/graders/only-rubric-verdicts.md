---
type: regex
target: { source: file, path: out/claims.json }
pattern: '"verdict"\s*:\s*"(?!(?:Supported|Partially Supported|Unsupported|Contradicted|Cannot Evaluate)")'
match: not_contains
---
