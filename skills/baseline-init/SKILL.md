---
name: baseline-init
description: Set up a repository for the baseline (ADRs and coding standards that steer agents) or update a repository that already uses it. Use when the engineer asks to initialise, install, set up, adopt or update the baseline in a repo.
compatibility: Python 3.9+ (standard library only), git
metadata:
  version: "0.2.0"
---

# baseline-init

Paths are relative to this skill's folder. Run the scripts with `python3`.

## Init: set up a repository

1. Run `python3 scripts/init.py <repo> --dry-run` and show the engineer the lines it prints.
2. After their yes, run `python3 scripts/init.py <repo>`.
3. Tell the engineer what was created or appended, and that nothing is committed.

The script is `scripts/init.py`. It never overwrites a file, and it refuses a repo that already has `baseline.yml` (use update mode there). The files it copies come from `assets/kit/`.

## Update: bring a repository to the installed version

The skills are updated by the package manager first. Then, in the repo:

1. Run `python3 scripts/update.py plan <repo>` and show the engineer its output: the versions, each pending migration with its dry run, and the state of the owned `AGENTS.md` block.
2. For each pending migration, in order, put one decision to the engineer: the recommendation first, with one reason. Only after their yes, run `python3 scripts/update.py apply <repo> <migration-id>`.
3. When none is pending, run `python3 scripts/update.py finish <repo>`. If it exits 4 the block was edited: show the engineer the edit and let them decide; `--discard-edits` replaces it.
4. Leave committing and PRs to the repo's own conventions.

Rules:
- A migration may change project-owned files (standards, `baseline.yml`, ADRs, project docs) only after the engineer has seen its dry run and approved.
- A declined migration stops the update. Say that the repo stays at its current version, and why. Never skip a migration and never record an override.
- The script is `scripts/update.py`; the migration contract is in `migrations/README.md`.
