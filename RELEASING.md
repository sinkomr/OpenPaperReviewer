# Releasing

Steps for a maintainer. Nothing here happens automatically.

## Before any release

1. Run the checks:

   ```bash
   python3 -m unittest discover -s tests
   ```

   ```bash
   python3 scripts/build_prompts.py --check
   ```

   ```bash
   python3 scripts/check_card_sources.py
   ```

   ```bash
   claude plugin validate --strict ./plugin
   ```

   ```bash
   claude plugin validate --strict .
   ```

2. Run the regression cases and read the report:

   ```bash
   claude plugin eval ./plugin --ablation none --scaffold --allow-tools Write Edit "Bash(python3 *)"
   ```

3. If the rubric, the phases or the rules changed, raise the version in `plugin/.claude-plugin/plugin.json`, in `plugin/.codex-plugin/plugin.json` and in the frontmatter of `plugin/skills/open-paper-reviewer/SKILL.md`. A test fails if the three differ.
4. Build the upload files. This writes two zips to `dist/`: `open-paper-reviewer-plugin-<version>.zip` for plugin uploads, and `open-paper-reviewer-skill-<version>.zip` for skill uploads (one top-level folder with `SKILL.md` inside it, no plugin manifest):

   ```bash
   python3 scripts/make_release_zip.py
   ```

## First publication

1. Make the repository public.
2. Push `main`.
3. Create the reviews branch and push it:

   ```bash
   sh scripts/init_reviews_branch.sh
   ```

   ```bash
   git push origin reviews
   ```

4. On GitHub, protect both branches: require the CI check on `main` and the review validation check on `reviews`, and require a maintainer's approval for pull requests.
5. Create a release tagged with the version and attach both zips from `dist/`.
6. Check that installation works from the public repository in Claude Code and in Codex, using the commands in `README.md`.

## Anthropic's directory

Reaches claude.ai, Cowork and Claude Code. Submitting needs a paid claude.ai plan.

- [ ] `claude plugin validate --strict ./plugin` passes.
- [ ] The plugin folder has a README of at least 40 words and a `LICENSE`.
- [ ] No file in the plugin folder is over 256 KiB, there are fewer than 512 files, and all are text or images.
- [ ] `plugin/README.md` describes everything the skill reads, runs, fetches and sends.
- [ ] Open the developer portal at https://claude.ai/directory/manage, choose Submit new, then Plugin bundle.
- [ ] Enter the repository and the plugin path `plugin`, select Validate, and fix every finding marked Blocking.
- [ ] Submit. A name made of generic words may be held for a reviewer; that is not a rejection.

The checks the portal runs are listed at https://claude.com/docs/plugins/pre-submission-checklist.

## OpenAI's plugin directory

Reaches ChatGPT and Codex. Submitting needs an organization owner (or a member with the Apps Management Write permission) and completed identity verification.

- [ ] `plugin/.codex-plugin/plugin.json` has `name`, `version`, `description`, `author.name` and the `interface` block: `displayName`, `shortDescription` (30 characters or fewer), `longDescription`, `developerName`, `category`, `capabilities`, `logo` and `composerIcon`.
- [ ] The icon is square and at least 48 by 48 pixels.
- [ ] The plugin contains only skills: no MCP server, no hooks, no app references.
- [ ] Open https://platform.openai.com/plugins, choose Upload new or existing plugin, and upload the plugin zip.
- [ ] Resolve the automated findings and complete the policy attestations.

The submission guide is at https://developers.openai.com/plugins/deploy/submission.

## After a release

- New versions reach Claude Code users of the marketplace when the version number changes.
- Posted reviews record the method version they were made with, so old reviews stay interpretable.
