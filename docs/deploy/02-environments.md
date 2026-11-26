---
scope: "The two places the repository lives, what each is for, how it was created, how they differ, what lives there and who has access; and the absence of CI, staging and production."
verified_against: { commit: bd7b1ce, versions: { git: "2.54.0", gh: "2.103.3", gh-stack: "0.3.0" } }
reading_time_min: 2
---

# Environments

The baseline has two environments, and neither runs anything.

| Environment | Purpose | How it was created | What lives there | Who has access |
|---|---|---|---|---|
| The local repository | Where the agents commit, cut the stack's branches and write the documents. | The bootstrap commit on `main`, `47615da`, on 2026-11-14, with `origin` set to the GitHub repository. | Every branch of the stack, and git-ignored scratch such as `.DS_Store` and `__pycache__/`. | Whoever uses the Software Engineer's machine. |
| GitHub | Where work is published, reviewed and merged, and where readers read it. | The private repository `chandanbsd/baseline-framework`; `main` and PRs 1 and 2 were pushed on 2026-11-18, and the rest of the stack on 2026-11-19. | `main`, with the first stack merged into it on 2026-11-20, the stack's 24 branches and its 24 merged PRs, #1, #2 and #4 to #25. | The repository's collaborators on GitHub. Who they are was not checked: not verified. |

There is no CI environment: the repository has no `.github/` folder and no workflow. There is no staging and no production, because nothing is deployed.

```mermaid
flowchart LR
    subgraph L["Local"]
        L1["Every branch of the stack"]
        L2["Git-ignored scratch"]
    end
    subgraph G["GitHub"]
        G1["main"]
        G2["The published branches<br/>and their PRs"]
    end
    L1 -->|"published with the Software Engineer's yes"| G2
    L2 -. "never pushed" .-> G
```

*The two environments hold what has been published, and the one thing to notice is the dotted line from the scratch files: they are git-ignored, so they never leave the local repository.*
