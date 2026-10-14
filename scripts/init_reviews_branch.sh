#!/bin/sh
# Create the `reviews` branch: a separate history holding posted reviews.
#
# Run once from a checkout of main. It builds the branch in a temporary
# worktree, so the main working tree is not touched, and it does not push.
# Review the result, then push with:  git push origin reviews

set -eu

root=$(git rev-parse --show-toplevel)
cd "$root"

if git show-ref --verify --quiet refs/heads/reviews; then
  echo "A local branch named reviews already exists. Nothing done." >&2
  exit 1
fi

work=$(mktemp -d)
trap 'git worktree remove --force "$work" >/dev/null 2>&1 || true' EXIT

git worktree add --detach "$work" >/dev/null
cd "$work"
git checkout --orphan reviews >/dev/null 2>&1
git rm -rf --quiet . >/dev/null 2>&1 || true

mkdir -p .github/workflows
cp "$root/scripts/reviews-branch/.github/workflows/validate-review.yml" .github/workflows/
cp "$root/scripts/reviews-branch/.github/workflows/build-index.yml" .github/workflows/

# Any reviews staged for launch are copied in as they are.
if [ -d "$root/runs/launch-reviews" ]; then
  cp -R "$root/runs/launch-reviews/." .
fi

python3 "$root/scripts/build_index.py" .

git add -A
git commit --quiet -m "Start the reviews branch"
echo "Created local branch reviews at $(git rev-parse --short HEAD)."
echo "Inspect it with: git log reviews --stat"
