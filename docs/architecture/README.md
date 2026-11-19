<!-- Generated index of docs/architecture/. No generator exists yet, so the docs agent writes it, in this form, as the single writer of its stack (standard/17-evidence-and-truth.md, rule 11). Do not edit it by hand. -->

# Architecture reference

How the baseline is built, as it is at commit `cb4fb22`. The shape of this folder is set in [standard/07-architecture-reference.md](../../standard/07-architecture-reference.md).

| File | Scope | Reading time |
|---|---|---|
| [01-overview.md](01-overview.md) | What the baseline is at this tip, the technology choices with the ADR that records each, the quality goals that drive the design, and the big picture: who and what the repository works with, and the parts it is made of. | 8 min |
| [02-the-standard.md](02-the-standard.md) | The components of the baseline: the 22 files of the standard and its index, grouped as the index groups them, the six playbooks and the two instruction files that carry the rules to agents, what each is responsible for, and the direction in which they depend on each other. | 8 min |
| [03-the-stack-model.md](03-the-stack-model.md) | How work is delivered as one stack of PRs: the flow from brainstorm to merged stack, the workflow a PR of the stack goes through, and the contracts that make a stack: branch names, how a PR's kind is read from its paths, the PR description and gh stack link. | 8 min |
| [04-the-docs-agent.md](04-the-docs-agent.md) | The docs agent as a procedure: the flow by which it writes the docs section, the states it goes through, and its contract: what it reads, what it never reads and what it produces. | 7 min |
| [05-decisions-and-adrs.md](05-decisions-and-adrs.md) | The ADR model: the flow by which a decision becomes an ADR, the lifecycle of an ADR's status, and the ADR's contract: its template, its file name, its number and the guard rail on the docs agent's review. | 7 min |
| [06-standards-and-the-reader-profile.md](06-standards-and-the-reader-profile.md) | The two inputs that a project gives the baseline: the reader profile, made by the intake, and the standards, made from approved preferences. The flows by which each is made, the states a standard and a profile entry go through, and their formats, with baseline.yml. | 7 min |
| [07-evidence-and-checks.md](07-evidence-and-checks.md) | How the documents are kept true: the flow from a claim to a sentence, the eleven evidence rules, the checks and the stack gate that the standard requires of the tooling, and the quality section: performance and the testing strategy at this tip. | 7 min |
| [08-cross-cutting.md](08-cross-cutting.md) | The minimum sections that cut across the whole baseline: data, the concurrency and failure model of stacks in flight, security and trust, the operations summary, the known limits found while documenting it, and where the decisions live. | 12 min |

## The thirteen minimum sections

| # | Section | Where it is |
|---|---|---|
| 1 | What the system is | [01-overview.md](01-overview.md) |
| 2 | The big picture | [01-overview.md](01-overview.md) |
| 3 | Components | [02-the-standard.md](02-the-standard.md) |
| 4 | Key flows | [03-the-stack-model.md](03-the-stack-model.md), [04-the-docs-agent.md](04-the-docs-agent.md), [05-decisions-and-adrs.md](05-decisions-and-adrs.md), [06-standards-and-the-reader-profile.md](06-standards-and-the-reader-profile.md), [07-evidence-and-checks.md](07-evidence-and-checks.md) |
| 5 | Data | [08-cross-cutting.md](08-cross-cutting.md): not applicable |
| 6 | State machines | [03-the-stack-model.md](03-the-stack-model.md), [04-the-docs-agent.md](04-the-docs-agent.md), [05-decisions-and-adrs.md](05-decisions-and-adrs.md), [06-standards-and-the-reader-profile.md](06-standards-and-the-reader-profile.md) |
| 7 | Interfaces and contracts | [03-the-stack-model.md](03-the-stack-model.md), [04-the-docs-agent.md](04-the-docs-agent.md), [05-decisions-and-adrs.md](05-decisions-and-adrs.md), [06-standards-and-the-reader-profile.md](06-standards-and-the-reader-profile.md) |
| 8 | Concurrency and failure model | [08-cross-cutting.md](08-cross-cutting.md) |
| 9 | Security and trust | [08-cross-cutting.md](08-cross-cutting.md) |
| 10 | Operations summary | [08-cross-cutting.md](08-cross-cutting.md): not applicable |
| 11 | Quality | [07-evidence-and-checks.md](07-evidence-and-checks.md) |
| 12 | Known limits | [08-cross-cutting.md](08-cross-cutting.md) |
| 13 | Where decisions live | [08-cross-cutting.md](08-cross-cutting.md), generated |
