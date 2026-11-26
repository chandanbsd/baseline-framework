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

The script is `scripts/init.py`. It never overwrites an existing file: it appends its block to `AGENTS.md` and leaves the rest of your file as it is, line endings included. It refuses a repo that already has `baseline.yml` (use update mode there) and an `AGENTS.md` whose baseline markers do not form exactly one block. The files it copies come from `assets/kit/`.

## Update: bring a repository to the installed version

The skills are updated by the package manager first. Then, in the repo:

1. Run `python3 scripts/update.py plan <repo>`. It prints the versions, the next pending migration with its dry run, the later ones by name, and the state of the owned `AGENTS.md` block.
   - Exit 3: the repo is newer than the installed skills. Stop and tell the engineer to update the skills first.
   - Exit 2: it refuses (for example, the `AGENTS.md` markers do not form exactly one block). Show the engineer the message and do not edit around it.
2. Put one decision to the engineer for that migration: the recommendation first, with one reason. Only after their yes: if the plan names instructions for it, read and follow them, then run `python3 scripts/update.py apply <repo> <migration-id>`. Run `plan` again for the next migration.
   - Exit 1 means a migration failed. The version stays and nothing is rolled back, so tell the engineer to check `git status`.
3. When none is pending, run `python3 scripts/update.py finish <repo>`. Exit 4 means the block was edited: show the engineer the edit and let them decide; `--discard-edits` replaces it. If they want to keep the edit, stop there and say that the repo is not fully at the installed version (`plan` keeps reporting the block as edited), because recording an override is not built yet.
4. Leave committing and PRs to the repo's own conventions.

`apply` and `finish` take `--dry-run` to show what they would do and change nothing.

Rules:
- A migration may change project-owned files (standards, `baseline.yml`, ADRs, project docs) only after the engineer has seen its dry run and approved.
- A declined migration stops the update. Say that the repo stays at its current version, and why. Never skip a migration and never record an override.
- The script is `scripts/update.py`; the migration contract is in `migrations/README.md`.
