# Glossary
covers: the terms the baseline documents use, product and technical

## Terms

| Term | Meaning | Where it appears |
|---|---|---|
| adopt run | A documentation run in a repository that has no `baseline/docs/` yet: it documents the whole repository and raises an `overlap` flag for each existing document that covers the same ground. | [course 5](../course/05-document-the-accepted-code.md) |
| ADR | Architecture decision record: one file in `baseline/adr/` that states a decision of impact as the desired output, with a line or two of why. | [decisions and standards](../features/decisions-and-standards.md) |
| Agent Skill | A folder with a `SKILL.md` (name, description, instructions) and optional `scripts/`, `assets/`, `references/`, which an agent loads when the task fits. The baseline is four of them. | [architecture](../architecture/README.md) |
| apply | `update.py apply REPO ID`: runs the next pending migration for real and moves `baseline_version` to its target. | [course 2](../course/02-update-a-repository.md) |
| arrival decision | One decision in a desired-state file: the decision, why, and each option not taken with a line on why it lost. | [course 4](../course/04-agree-the-end-state-before-code.md) |
| `baseline/` folder | `baseline/` in a project: everything the baseline writes, apart from the `AGENTS.md` pointer, `CLAUDE.md` and the workflow. | [set up a repository](../features/set-up-a-repository.md) |
| `baseline_version` | The key in `baseline/baseline.yml` that records which version of the skills the project is at. | [course 2](../course/02-update-a-repository.md) |
| check | `baseline/check.py`, run by CI on every pull request: it looks only inside `baseline/`. | [course 3](../course/03-check-the-baseline-folder.md), [pull request check](../features/pull-request-check.md) |
| coding standard | A file in `baseline/standards/` that states a blanket rule about how code is written, with its end result, snippets and exceptions. | [decisions and standards](../features/decisions-and-standards.md) |
| compaction | An agent's context being shortened during a long task. `baseline.md` tells the agent to re-read the accepted desired-state file after one. | [course 4](../course/04-agree-the-end-state-before-code.md) |
| `covers:` line | Line 2 of every baseline document: the behaviour it describes. `covers.py` lists them. | [course 5](../course/05-document-the-accepted-code.md) |
| decisions PR | The pull request above the desired-state PR that holds the new ADRs and standards, for the engineer to review before any code. | [decisions and standards](../features/decisions-and-standards.md) |
| desired-state file | `baseline/desired-state/NNNNN-name.md`: the end state, the arrival decisions and what they settle, accepted by the engineer before any code. | [questions before code](../features/questions-before-code.md) |
| document family | One of the six kinds of document: `readme`, `architecture`, `course`, `features`, `deployment`, `reference`. | [course 5](../course/05-document-the-accepted-code.md) |
| `documents_skipped` | The key in `baseline/baseline.yml` that lists the families that do not apply to the project. | [course 3](../course/03-check-the-baseline-folder.md), [course 5](../course/05-document-the-accepted-code.md) |
| dry run | A run that prints what it would do and changes nothing (`--dry-run`). | [course 1](../course/01-set-up-a-repository.md), [architecture](../architecture/README.md) |
| edited | The status of an owned file whose body no longer matches the hash in its header, or that has no header. | [architecture](../architecture/README.md), [course 2](../course/02-update-a-repository.md) |
| `empty-family` flag | The file `baseline/flags/empty-family-<family>.md` with `about: <family>`. The check fails until the family is skipped or written. | [course 3](../course/03-check-the-baseline-folder.md) |
| finish | `update.py finish REPO`: replaces the owned files and sets `baseline_version` once no migration is pending. | [course 2](../course/02-update-a-repository.md) |
| flag | A file in `baseline/flags/` where the documentation agent records something the engineer should decide. | [documentation from the code](../features/documentation-from-the-code.md) |
| `inferred` | The label on a reason in a course chapter that is the writer's guess, not stated in the code or its instructions. | [course 1](../course/01-set-up-a-repository.md) |
| kit | `skills/baseline-init/assets/kit/`: the file bodies that `init.py` copies into a project. | [architecture](../architecture/README.md) |
| Mermaid | A text format for diagrams that GitHub draws; every diagram in the baseline documents uses it. | [course 3](../course/03-check-the-baseline-folder.md) |
| migration | A folder `migrations/FROM-to-TO/` with a `migrate.py` that moves project-owned files from one version to the next. None ships at 0.2.0. | [course 2](../course/02-update-a-repository.md) |
| `mmdc` | The Mermaid command-line renderer. The check renders diagrams with it when it is on the `PATH`. | [course 3](../course/03-check-the-baseline-folder.md) |
| notice | A line the check prints that never fails it, for example `not yet documented: course`. | [pull request check](../features/pull-request-check.md) |
| owned file | A file the baseline writes whole and replaces on update: `baseline/baseline.md`, `baseline/check.py` and the workflow. Its first line is a header with a version and a hash. | [architecture](../architecture/README.md) |
| plan | `update.py plan REPO`: shows versions, the next migration and the state of the owned files. | [course 2](../course/02-update-a-repository.md) |
| pointer | The short block `init.py` adds to `AGENTS.md` that sends agents to `baseline/baseline.md`. | [course 1](../course/01-set-up-a-repository.md) |
| revise run | A documentation run after the engineer comments on the documentation pull requests. | [course 5](../course/05-document-the-accepted-code.md) |
| stub | A skill that is only a placeholder: `baseline-refactor` says it is not implemented and stops. | [architecture](../architecture/README.md) |
| tip | The last commit of the branch being documented. The documentation agent describes what exists there. | [course 5](../course/05-document-the-accepted-code.md) |
| update run | The normal documentation run: it takes the diff of the stack and rewrites the documents whose behaviour the diff changes. | [course 5](../course/05-document-the-accepted-code.md) |
