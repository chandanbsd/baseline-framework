---
scope: "How finished work reaches readers: there is no build, no artifact and no release workflow; a stack merged into main on GitHub is what readers read. Versioning and the gates that exist."
verified_against: { commit: 9d4518e, versions: { git: "2.54.0", gh: "2.103.3", gh-stack: "0.3.0" } }
reading_time_min: 2
---

# Build and release pipeline

The repository has no CI workflow, no build and no release workflow: there is no `.github/` folder, and `git tag` lists no tags. Nothing is built, because the product is the text itself. A stack that the Software Engineer merges into `main` on GitHub is, from then on, what a reader of `main` reads.

```mermaid
flowchart LR
    A["The stack's branches<br/>in the local repository"] --> B{"Does the Software Engineer<br/>say yes to publish?"}
    B -->|"no"| W["The branches wait locally"]
    B -->|"yes"| C["gh stack link with --open:<br/>the PRs are open on GitHub"]
    C --> D["The Software Engineer reviews<br/>the whole stack"]
    D --> E{"Does the Software Engineer<br/>ask for the merge?"}
    E -->|"no"| C
    E -->|"yes"| F["Merged bottom-up into main"]
    F --> G["Readers read main on GitHub"]
```

*The only gates between the stack and its readers are two decisions of the Software Engineer, and the one thing to notice is that there is no build or check between them: the stack gate and the checks that the standard requires do not exist yet.*

## Versioning and promotion

The baseline's versions follow semver: a patch version for fixes, a minor version for optional additions and a major version for new required structure, with an upgrade guide ([standard/README.md](../../standard/README.md)). This repository's `baseline.yml` pins `baseline_version: 0.1.0`. No version has been released or tagged. There is no promotion, because there is only one place that readers read, `main` on GitHub.

## Approvals

Two approvals are the Software Engineer's: the yes to publish, because in this repository opening a stack's PRs is publishing (`AGENTS.md`, rule 4), and the merge, because nothing merges unless the Software Engineer asks. The standard requires a stack gate that keeps the lower PRs pending until the tip passes; it does not exist ([standard/22-tooling-requirements.md](../../standard/22-tooling-requirements.md)).
