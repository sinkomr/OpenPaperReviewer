---
type: regex
target: { source: file, path: out/run.json }
pattern: '"id"\s*:\s*"(?!unknown")[^"]{3,}"'
---
