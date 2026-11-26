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

Filled in by the next task.
