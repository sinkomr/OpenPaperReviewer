---
type: regex
target: { source: file, path: out/run.json }
pattern: '"effort"\s*:\s*"default"[\s\S]{0,200}"effort_source"\s*:\s*"supplied_by_user"|"effort_source"\s*:\s*"supplied_by_user"[\s\S]{0,200}"effort"\s*:\s*"default"'
---
