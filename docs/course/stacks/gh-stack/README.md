# gh stack and stacked PRs: what else it offers

The course teaches the parts of stacked PRs and `gh stack` that this repository uses, from the first command. This page shows the boundary: every command that `gh stack` 0.3.0 lists in its help, whether the baseline uses it, and why not when it does not. It is a map, not a course; each row sends you to the official documentation.

The lessons:

1. [A stack of pull requests](01-a-stack-of-pull-requests.md)
2. [gh stack link and the stack on GitHub](02-gh-stack-on-github.md)

| Topic | Feature | In one line | Used here | Official docs |
|---|---|---|---|---|
| Plain git | `git branch` pointers and the chain check | The stack's branches, made and checked without `gh stack`. | Used: [A stack of pull requests](01-a-stack-of-pull-requests.md) | [git branch](https://git-scm.com/docs/git-branch) |
| Remote operations | `gh stack link` | Create or update a stack on GitHub from branch names, with no local tracking. | Used: [gh stack link and the stack on GitHub](02-gh-stack-on-github.md) | [gh stack](https://github.com/github/gh-stack) |
| Remote operations | `gh stack merge` | Merge a stack in one all-or-nothing operation. | Not used: nothing merges unless the Software Engineer asks, and the baseline never runs it on its own | [gh stack](https://github.com/github/gh-stack) |
| Remote operations | `gh stack submit`, `push`, `sync`, `rebase` | Push, create PRs, sync and rebase a locally tracked stack. | Not used: they work from local tracking, and the baseline makes its branches with plain git and links them ([docs/agents/stacks.md](../../../agents/stacks.md)) | [gh stack](https://github.com/github/gh-stack) |
| Stack management | `gh stack view` | Show the current stack's branches and PR status. | Used, as an extra look only: [gh stack link and the stack on GitHub](02-gh-stack-on-github.md) | [gh stack](https://github.com/github/gh-stack) |
| Stack management | `gh stack checkout` | Check out a stack by number, PR or branch, importing it into local tracking. | Used only to import a linked stack before `gh stack view`: [gh stack link and the stack on GitHub](02-gh-stack-on-github.md) | [gh stack](https://github.com/github/gh-stack) |
| Stack management | `gh stack unstack` | Remove a stack locally and on GitHub; `--local` removes only the local tracking. | Used only as `--local`, after an extra look; removing a stack on GitHub is not part of the normal flow | [gh stack](https://github.com/github/gh-stack) |
| Stack management | `gh stack init`, `add`, `modify` | Start a locally tracked stack, add a branch to it, restructure it. | Not used: the baseline cuts its stacks as pointers with plain git ([docs/agents/stacks.md](../../../agents/stacks.md)) | [gh stack](https://github.com/github/gh-stack) |
| Navigation | `gh stack up`, `down`, `top`, `bottom`, `trunk`, `switch` | Move between the branches of a locally tracked stack. | Not used: they need local tracking, which a linked stack does not have | [gh stack](https://github.com/github/gh-stack) |
| Utilities | `gh stack alias`, `feedback` | Make a shell alias; send feedback. | Not used: no document here needs them; the reason is not recorded | [gh stack](https://github.com/github/gh-stack) |
| Ecosystem | GitHub's stacked pull requests | GitHub's own feature for stacks, in public preview. | Used: every stack of this repository is a GitHub stack; its documented rules are not yet confirmed against its behaviour | [Stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/stacked-pull-requests) |
| Tooling | `gh extension install` | Install a `gh` extension. | Used, to install `gh stack`: [README](../../../../README.md), "Prerequisites" | [gh extension install](https://cli.github.com/manual/gh_extension_install) |
