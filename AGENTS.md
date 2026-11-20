# Instructions for working in baseline-framework

This is the primary instruction for working in this repository. Each rule in it gives its reason and points to a playbook, a longer guide in `docs/agents/` that explains the rule in full.

## Who and what

`baseline-framework` is the baseline: a standard for documenting and delivering a software project of any kind, in any technology. It fixes which documents a project has and who writes them, how work is delivered through pull requests (PRs), and how a project's approved preferences become the standards that drive code. This repository follows its own standard and is also a resource the team learns the approach from.

The Software Engineer is Chandan. They decide in this repository, and the baseline is built for them: an engineer working toward Distinguished Engineer by taking on the responsibilities of a Lead Engineer, a Principal Engineer and a Solutions Architect, with agents writing most of the code. [working-with-the-engineer.md](docs/agents/working-with-the-engineer.md) lists what they decide and what you decide yourself.

If the Software Engineer says something different in the conversation, the conversation wins for that task. Because: they are the one who decides, and this file and the playbooks guide the work without limiting what they can ask for.

[docs/reader-profile.md](docs/reader-profile.md) records who the documents are written for. Read it before you write or change a document. Because: it sets which basics a document explains, and it shapes documents only, never the code or the scope.

## The core rules

Each rule is followed by its reason and by the playbook that explains it. A rule whose reason is gone is removed: if you meet one whose reason no longer holds, say so in your report and let the Software Engineer decide. Because: a rule without a living reason is an unexplained constraint on every later task, and changing how work is done is the Software Engineer's call.

1. **Work as stacks, and keep each PR to one kind.** A **stack** is an ordered series of PRs, each based on the one below it and merged from the bottom up: the spec, the plan, small PRs of decision records, the code in slices (logical groups of code, one code PR each), and the docs last. A **thinking PR** holds the documents that say what will be built or how work is done (the spec, the plan, architecture decision records called ADRs, standards, the reader profile and the playbooks), a **code PR** holds code and tests, and a **description PR** holds the documents that say what was built.

   Because: each kind is easier to review on its own. A PR that mixes kinds is not wrong, only harder to review, so the baseline asks that the kinds be separated when PRs are opened.

   Playbook: [stacks.md](docs/agents/stacks.md).

2. **Keep one repository per project, with no exceptions.** Anything that must be published separately, an SDK for example, is a folder in the repository that CI publishes as a package.

   Because: a stack cannot span repositories, and in one repository an agent sees the whole product.

   Playbook: [stacks.md](docs/agents/stacks.md).

3. **Skills run as written and write where they write, and you never edit a skill's documents to fit the baseline.** The baseline does not tell a skill where to write. It reads the paths a skill writes to, recorded in `baseline.yml`, and arranges the PRs around them. If a skill revises its own spec or plan later, that revision gets its own thinking PR, at the point in the stack where it happened.

   Because: the baseline sits beside the skills and changes nothing about how they work, so a document a skill produced stays as the skill produced it.

   Playbook: [stacks.md](docs/agents/stacks.md).

4. **Nothing merges, deploys or publishes unless the Software Engineer asks.** Opening the PRs of a stack is publishing, so it waits for their yes too, the first two PRs included, and the rest of the stack waits until its docs section is in.

   Because: merging, deploying and publishing are the Software Engineer's calls, and the merge of a stack is also the acceptance of its ADRs. The rest of the stack waits for its docs section because the stack is complete only with the docs section on top (`stacks.md` has the rules of a stack).

   Playbooks: [working-with-the-engineer.md](docs/agents/working-with-the-engineer.md) and [stacks.md](docs/agents/stacks.md).

5. **Add no attribution lines to commits or PR descriptions:** no co-author trailer and no "generated with" line.

   Because: the Software Engineer does not want them, and Claude Code adds such lines by default, so the rule has to be stated explicitly.

   Playbook: [stacks.md](docs/agents/stacks.md).

6. **Descriptive documents are written only by the fresh docs agent, from the finished tip.** The **tip** is the last commit of the stack, and it is finished once the building is done. Descriptive documents say only what exists at that tip: the README, the architecture reference, the feature docs, the course, the deployment docs and the reference pages. The **docs agent** is an agent started fresh at that tip, and its documents go in the description PRs on top of the stack. Any other agent writes none of them.

   Because: the agent that built the code tends to document what it meant, and cannot tell when the code does not say it.

   Playbook: [docs-agent.md](docs/agents/docs-agent.md).

7. **Agents propose standards and never write them silently.** When you notice a preference in a conversation or a review comment, propose the rule in the chat, with its reason in the Software Engineer's words and its scope, and write it only after the Software Engineer approves.

   Because: a standard steers every later generation of code, so a rule that nobody approved would steer it wrongly and no one would notice.

   Playbook: [standards.md](docs/agents/standards.md).

## The playbooks

The playbooks are in `docs/agents/`. Each gives the rules of its subject in full, with the reason beside every rule. Read the one that fits when its subject comes up.

1. [working-with-the-engineer.md](docs/agents/working-with-the-engineer.md) covers who decides what, how a decision is put to the Software Engineer, what to do while they are busy, how to report, and how to record a ruling, which is a decision you take on their behalf.

   Read it at the start of every task, and again when you reach a choice and are not sure whose it is, before you put a question to the Software Engineer, before you hand them steps while they are busy, and before you write a report.

2. [stacks.md](docs/agents/stacks.md) covers the three kinds of PR, the rules and conventions of a stack, what `gh stack` is and how this baseline uses it, how to cut a stack from linear history and open it, small changes, and the seams with the skills.

   Read it before you commit work that will become a PR, when you cut, open or grow a stack, when a skill has produced a spec, a plan or any other document, when you are unsure which PR a change belongs in, and when you are asked for a small change.

3. [pr-descriptions.md](docs/agents/pr-descriptions.md) covers the header every PR description starts with, the form of the description for each kind of PR, and how to keep the stack tables current.

   Read it when you open a PR, when you write or change a description, and again every time the stack changes, because every description carries a table of the whole stack.

4. [docs-agent.md](docs/agents/docs-agent.md) is the brief of the docs agent: what it reads, what it never reads, what it writes, and when it stops and asks.

   If you are the docs agent, read it in full before you write anything. If you are the agent that builds, read it to know what the docs agent will read from your work.

5. [adrs.md](docs/agents/adrs.md) covers when a decision needs an ADR draft, how to write one, how an ADR moves from draft to accepted, how far the docs agent may go in reviewing a draft, and the check that a changed dependency manifest, schema or interface file is covered by an ADR or a ruling.

   Read it when you make or adopt a decision and have to tell whether it needs a draft, when you write a draft, when you review drafts as the docs agent, when you change a dependency manifest, a schema or an interface file, and when you are asked what state an ADR is in.

6. [standards.md](docs/agents/standards.md) covers what belongs in `docs/standards/`, how a preference becomes a standard, what to do when generated code is wrong, and what each rule records.

   Read it when you notice a preference in a conversation or a review comment, before you generate code, when generated code is wrong, when you are asked to add, change or remove a rule, and, if you are the docs agent, when you write a lesson that shows code a standard shaped.

## The repo map

This is the repository as its first stack leaves it. Folders for the baseline's later designs, the worked example (`examples/`) and the tooling (`kit/`, `checkers/` and `skills/`), appear when those designs are built, and this map then lists them.

- `standard/` is the standard itself, as plain Markdown. Its instructions are in `standard/AGENTS.md`, and `standard/README.md` is its index.
- `docs/` holds the documents:
  - [docs/reader-profile.md](docs/reader-profile.md) records who the documents are written for.
  - `docs/standards/` holds the standards, the preferences the Software Engineer has approved, each with its reason, scope, date and source. Read it before you generate code, when the folder exists. Because: the standards and the ADRs are the only documents that drive code, and the skills run untouched, so this pointer is how the standards reach you. The docs agent cites them in the lessons it writes. [docs/standards/README.md](docs/standards/README.md) explains how the folder fills.
  - `docs/adr/` holds the ADRs, one file for each decision, with the options that were explored. A draft is written when the decision is made, and the docs agent reviews and numbers it.
  - `docs/agents/` holds the playbooks listed above. A playbook holds no Markdown link and names another file in backticks. Because: the playbooks are replaced on update in every project, and a project does not hold some of the files they name, the baseline's own standard, so a link would break there while a name in backticks cannot.
  - `docs/superpowers/` holds the specs and plans that the superpowers skills produced, kept as the skills produced them (rule 3).
- [baseline.yml](baseline.yml) is the baseline's configuration for this repository. Its `artifact_map` records where skills write their documents and never tells them where to write, and its `stack_folders` lists the folders whose changes count as code. `standard/` is one of them, so a change to the standard is a code PR. Because: the standard is the product that this repository builds, so it is the code of this repository's own stack. Two files are the exception, as in any stack folder: `standard/README.md`, the standard's index, is a description path, so a change to it goes in a description PR, and `standard/AGENTS.md` is a thinking path, so a change to it goes in a thinking PR ([stacks.md](docs/agents/stacks.md)). The index keeps its form as the standard's index, so it does not take the run, test and build parts that `standard/13-project-readme.md` gives a stack folder's README, and the docs agent only checks it against the tip.

The README and the other descriptive documents are written by the docs agent after the build (rule 6). Only `standard/` has an `AGENTS.md` of its own so far. A folder that holds the code of one technology gets a short one, with its commands and layout, when that technology is introduced.
