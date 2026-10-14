#!/bin/bash
# Seeds the workspace with a review that stopped after Phase 2.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p out
cp "$here"/partial/* out/
