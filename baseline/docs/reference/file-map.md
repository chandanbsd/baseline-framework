# File map
covers: what each folder of the repository holds and which document explains it

## Folders

| Path | What it holds | Explained in |
|---|---|---|
| `/` | `AGENTS.md` (instructions for agents here), `CLAUDE.md` (imports it), `README.md`, and `baseline.yml` of the first design | `AGENTS.md` repo map |
| `.github/workflows/` | `baseline.yml`: runs the check on pull requests and on pushes to `main` and `master` | [course 3](../course/03-check-the-baseline-folder.md) |
| `baseline/` | This repository's own baseline: `baseline.md` (the baseline's instructions), `baseline.yml` (version and skipped families), `check.py` | [architecture](../architecture/README.md) |
| `baseline/adr/` | `TEMPLATE.md` for decision records; no ADR is written yet | [decisions and standards](../features/decisions-and-standards.md) |
| `baseline/standards/` | `TEMPLATE.md` for coding standards; no standard is written yet | [decisions and standards](../features/decisions-and-standards.md) |
| `baseline/desired-state/` | The accepted desired-state files, named `NNNNN-name.md` | [course 4](../course/04-agree-the-end-state-before-code.md) |
| `baseline/docs/` | These documents: `README.md`, `architecture/`, `course/`, `features/` and `reference/`; no `deploy/` because the family is skipped | [course 5](../course/05-document-the-accepted-code.md) |
| `baseline/flags/` | What the documentation agent could not settle, one file per flag | [documentation from the code](../features/documentation-from-the-code.md) |
| `skills/` | The four Agent Skills, one folder each | [architecture](../architecture/README.md) |
| `skills/baseline-init/` | `SKILL.md` for setting up and updating a repository | [course 1](../course/01-set-up-a-repository.md), [course 2](../course/02-update-a-repository.md) |
| `skills/baseline-init/scripts/` | `init.py`, `update.py` and `kit.py`, which they share | [course 1](../course/01-set-up-a-repository.md), [course 2](../course/02-update-a-repository.md) |
| `skills/baseline-init/assets/kit/` | The bodies `init.py` copies: `baseline/baseline.md`, `baseline/check.py`, the two templates, `github-workflow/baseline.yml`, `AGENTS.pointer.md` | [course 1](../course/01-set-up-a-repository.md) |
| `skills/baseline-init/migrations/` | A `README.md` with the migration contract; no migration ships | [course 2](../course/02-update-a-repository.md) |
| `skills/baseline-brainstorm/` | `SKILL.md` for the questions protocol, with `scripts/next_number.py`, `assets/desired-state-template.md` and two guides in `references/` | [course 4](../course/04-agree-the-end-state-before-code.md) |
| `skills/baseline-documentation/` | `SKILL.md` for writing the documents, `scripts/covers.py`, and in `references/` one guide per family plus one for flags | [course 5](../course/05-document-the-accepted-code.md) |
| `skills/baseline-refactor/` | A `SKILL.md` that says the skill is not implemented | [architecture](../architecture/README.md) |
| `tests/` | The `unittest` suites for the scripts and the skill rules, with `helpers.py` | [architecture](../architecture/README.md) |
| `tools/` | `bump_version.py`, which sets one version across the four skills | [course 2](../course/02-update-a-repository.md) |
| `docs/agents/` | Playbooks for agents working in this repository | `AGENTS.md` |
| `docs/adr/`, `docs/architecture/`, `docs/course/`, `docs/deploy/`, `docs/features/`, `docs/standards/`, `docs/reader-profile.md` and `standard/` | The first design's documents, kept as an archive. No script reads them | `AGENTS.md` repo map |
