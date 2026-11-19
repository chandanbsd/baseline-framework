<!-- Generated: the technical glossary, assembled from the terms that the lessons and chapters declare in their headers. No generator exists yet, so the docs agent writes it as the single writer of its stack (standard/17-evidence-and-truth.md, rule 11). Do not edit it by hand. -->

# Technical glossary

Each entry is a term that a lesson or a chapter of the course declares in its header, with its plain definition and a link to where it is taught. The plain-language glossary of the feature docs is [docs/features/glossary.md](../../features/glossary.md).

Terms: 60.

**ADR.** An architecture decision record: one file for one decision, with the options that were explored and the evidence for each. Taught in [A decision becomes an ADR](../system/03-decision-to-adr.md).

**alt block.** The part of a sequence diagram between alt and end that draws two or more alternative branches, separated by else. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**ancestor.** A commit that another commit was built on, directly or through others; git merge-base --is-ancestor tells whether one commit is an ancestor of another. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**approved palette.** The one set of colours a diagram of the baseline may hard-code: a translucent green, red or amber tint with a solid border of the same colour, and no text colour. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**atomic push.** A push of several branches in which all of them update or none does. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**backfilled rationale.** Reasoning written after a decision to justify it, which a decision record exists to prevent; anti-goal A4. Taught in [A decision becomes an ADR](../system/03-decision-to-adr.md).

**backtick string.** A Mermaid label written as a quote and a backtick at each end, whose text Mermaid formats as Markdown; the baseline uses it to name a real file in backticks. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**base.** The branch a pull request is compared against and merged into; in a stack, the branch of the pull request below. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**bootstrap commit.** The very first commit of a new repository, the one commit that goes straight to main, since there is nothing yet to branch from. Taught in [A project starts with the intake](../system/06-a-project-starts-with-the-intake.md).

**build branch.** The one branch on which the work of a stack is committed, task by task, before the stack is cut. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**caption.** The one-line italic sentence under every diagram that says what it shows and the one thing to notice. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**cardinality.** How many rows on one side of a relationship go with a row on the other side, drawn in Mermaid with marks such as || and o{. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**change marker.** The text +, ~ or - written in a diagram to say that a column or relationship was added, changed or removed, because Mermaid colours only whole tables. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**classDef.** A Mermaid statement that defines a named set of colours, which nodes or entities can then share through a class statement. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**code PR.** A pull request that holds code and tests; in this repository, the files of the standard. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).

**decision of impact.** A decision that meets one of six criteria: a new technology or dependency, a data model or public interface, a security or trust boundary, the deployment topology, a contract between technology stacks, or anything hard to reverse. Taught in [A decision becomes an ADR](../system/03-decision-to-adr.md).

**description PR.** A pull request that holds descriptive documents, the ones that say only what exists at the tip, written by the docs agent. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).

**deviations list.** The part of a description PR that lists where the built work departs from the plan, taken only from the Rulings I made lists. Taught in [The docs agent writes the docs section](../system/04-docs-agent-writes-the-docs-section.md).

**docs agent.** A fresh agent, started from the finished tip of a stack, that writes every descriptive document and never changes code. Taught in [The docs agent writes the docs section](../system/04-docs-agent-writes-the-docs-section.md).

**docs section.** The group of description PRs at the top of a stack, in reading order: reference, language lessons, stack lessons, system chapters. Taught in [The docs agent writes the docs section](../system/04-docs-agent-writes-the-docs-section.md).

**draft.** A pull request marked as not yet ready for review; gh stack link with --open marks every PR of the stack ready. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**edge label.** Text written on an arrow between two nodes. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**entity-relationship diagram.** A Mermaid diagram of a database's tables, called entities, with their columns and the relationships between them. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**evidence rules.** The eleven rules that keep what a descriptive document says true, from saying only what exists at the tip to writing the indexes as their single writer where no generator exists. Taught in [How documents stay true](../system/07-how-documents-stay-true.md).

**finish menu.** The choice an execution skill offers straight after its final review; for stack work the pick is to keep the branch as it is until the docs are in. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).

**finished tip.** The last commit of a stack once the building is done, from which the docs agent starts. Taught in [The docs agent writes the docs section](../system/04-docs-agent-writes-the-docs-section.md).

**flagged code.** A place where the code was unclear to a fresh reader, named in a description PR with the code PR its fix belongs in. Taught in [The docs agent writes the docs section](../system/04-docs-agent-writes-the-docs-section.md).

**flowchart.** A Mermaid diagram of nodes joined by arrows, laid out in one main direction. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**front matter.** A block of YAML between two lines of three dashes at the very start of a Markdown file, which keeps data a program can read in the file a person reads. Taught in [A project starts with the intake](../system/06-a-project-starts-with-the-intake.md).

**generated index.** An index that no one edits by hand: the course index, the architecture reference's index, the file map, the glossaries and the ADR index. Taught in [How documents stay true](../system/07-how-documents-stay-true.md).

**gh stack.** The GitHub CLI extension for stacked pull requests, run as a subcommand of gh. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**gh stack link.** The gh stack command that pushes branch names given bottom to top, opens a PR for each that has none on the branch below it, and creates or extends the stack on GitHub, keeping no local record. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**guard rail.** The limit on the docs agent's review of an ADR draft: it may clean up, add, review, number and flag, and may not rewrite the decision, the drivers, the options or the rationale. Taught in [A decision becomes an ADR](../system/03-decision-to-adr.md).

**intake.** The set of questions asked when a project starts, whose answers make the reader profile and decide whether the project keeps standards. Taught in [A project starts with the intake](../system/06-a-project-starts-with-the-intake.md).

**level.** Beginner, average or advanced: how much basic material a document explains to its reader about a technology or a knowledge area. Taught in [A project starts with the intake](../system/06-a-project-starts-with-the-intake.md).

**linear history.** A line of commits with no merges and no side branches, each commit the child of the one before. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**local tracking.** The record of a stack that gh stack keeps on one machine for its other commands; gh stack link keeps none. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**node shape.** The outline Mermaid draws around a node, chosen by the brackets around its label: a box, a rounded box, a diamond or a cylinder. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**not verified note.** The note that marks a statement nobody ran or measured, so that a reader does not take it as checked. Taught in [How documents stay true](../system/07-how-documents-stay-true.md).

**participant.** One column of a sequence diagram: a person, an agent or a system, declared with a short id and a name. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**pointer.** A branch name that points at one commit of a linear history, made with git branch and holding no commit of its own. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**presence check.** The check that a changed dependency manifest, schema or interface file is covered by an ADR or a ruling; it looks for a record, not for whether the decision was right. Taught in [How documents stay true](../system/07-how-documents-stay-true.md).

**reader profile.** The project's record of who its documents are written for: a level for each technology and each knowledge area, also the bar the Software Engineer hires against. Taught in [A project starts with the intake](../system/06-a-project-starts-with-the-intake.md).

**regenerate.** To have an agent write code again, in a fresh context, from corrected standards or ADRs, instead of patching the code. Taught in [A preference becomes a standard](../system/05-preference-to-standard.md).

**rule record.** The four things recorded beside every standard: its reason in the Software Engineer's words, its scope, its date and its source. Taught in [A preference becomes a standard](../system/05-preference-to-standard.md).

**ruling.** A decision an agent takes on the Software Engineer's behalf without stopping to ask, recorded as Ruling: what, why, cost if wrong. Taught in [A decision becomes an ADR](../system/03-decision-to-adr.md).

**rung.** One step of the ladder: a responsibility, and what the baseline gives the Software Engineer to carry it. Taught in [Why this exists](../system/01-why-this-exists.md).

**seam.** A point where what a skill does meets what the baseline does; the baseline keeps each seam small and never changes the skill. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).

**sequence diagram.** A Mermaid diagram of participants side by side, with the messages between them drawn top to bottom in the order they happen. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**slice.** A logical group of code that becomes one code PR, chosen by the agent and recorded as a ruling. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).

**stack gate.** The check the standard requires over the whole change of a stack, from main to the tip, which keeps the lower PRs pending until the tip passes. Taught in [How documents stay true](../system/07-how-documents-stay-true.md).

**stack of pull requests.** An ordered series of pull requests, each based on the one below it, so that each shows only its own change, merged from the bottom up. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**standard.** Written in lower case: an approved preference of the Software Engineer, recorded as a rule in docs/standards/, which drives code with the ADRs. Taught in [A preference becomes a standard](../system/05-preference-to-standard.md).

**start and end state.** The point written [*] in a state diagram: the start when an arrow leaves it, the end when an arrow enters it. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**state diagram.** A Mermaid diagram of states and the transitions between them, each transition labelled with what causes it. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**subgraph.** A named box drawn around a group of nodes in a flowchart, which may have its own direction. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**the ladder.** The rungs the Software Engineer climbs toward behaving as a Distinguished Engineer: Lead Engineer, Principal Engineer and Solutions Architect, each a responsibility taken on and kept. Taught in [Why this exists](../system/01-why-this-exists.md).

**the principle that outranks all others.** The rule that the reader's level shapes the documents only, and never the scope, scale, architecture or quality of what is built. Taught in [Why this exists](../system/01-why-this-exists.md).

**the standard.** The text of the baseline, in the files of standard/, as opposed to a project's standards. Taught in [A preference becomes a standard](../system/05-preference-to-standard.md).

**thinking PR.** A pull request that holds prescriptive documents, the ones that say what will be built or how work is done: the spec, the plan, ADRs, standards, the reader profile and the playbooks. Taught in [A feature goes from brainstorm to merged stack](../system/02-brainstorm-to-merged-stack.md).
