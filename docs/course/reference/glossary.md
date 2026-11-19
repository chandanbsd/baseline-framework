<!-- Generated: the technical glossary, assembled from the terms that the lessons and chapters declare in their headers. No generator exists yet, so the docs agent writes it as the single writer of its stack (standard/17-evidence-and-truth.md, rule 11). Do not edit it by hand. -->

# Technical glossary

Each entry is a term that a lesson or a chapter of the course declares in its header, with its plain definition and a link to where it is taught. The plain-language glossary of the feature docs is [docs/features/glossary.md](../../features/glossary.md).

Terms: 27.

**alt block.** The part of a sequence diagram between alt and end that draws two or more alternative branches, separated by else. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**ancestor.** A commit that another commit was built on, directly or through others; git merge-base --is-ancestor tells whether one commit is an ancestor of another. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**approved palette.** The one set of colours a diagram of the baseline may hard-code: a translucent green, red or amber tint with a solid border of the same colour, and no text colour. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**atomic push.** A push of several branches in which all of them update or none does. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**backtick string.** A Mermaid label written as a quote and a backtick at each end, whose text Mermaid formats as Markdown; the baseline uses it to name a real file in backticks. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**base.** The branch a pull request is compared against and merged into; in a stack, the branch of the pull request below. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**build branch.** The one branch on which the work of a stack is committed, task by task, before the stack is cut. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**caption.** The one-line italic sentence under every diagram that says what it shows and the one thing to notice. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**cardinality.** How many rows on one side of a relationship go with a row on the other side, drawn in Mermaid with marks such as || and o{. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**change marker.** The text +, ~ or - written in a diagram to say that a column or relationship was added, changed or removed, because Mermaid colours only whole tables. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**classDef.** A Mermaid statement that defines a named set of colours, which nodes or entities can then share through a class statement. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**draft.** A pull request marked as not yet ready for review; gh stack link with --open marks every PR of the stack ready. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**edge label.** Text written on an arrow between two nodes. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**entity-relationship diagram.** A Mermaid diagram of a database's tables, called entities, with their columns and the relationships between them. Taught in [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md).

**flowchart.** A Mermaid diagram of nodes joined by arrows, laid out in one main direction. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**gh stack.** The GitHub CLI extension for stacked pull requests, run as a subcommand of gh. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**gh stack link.** The gh stack command that pushes branch names given bottom to top, opens a PR for each that has none on the branch below it, and creates or extends the stack on GitHub, keeping no local record. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**linear history.** A line of commits with no merges and no side branches, each commit the child of the one before. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**local tracking.** The record of a stack that gh stack keeps on one machine for its other commands; gh stack link keeps none. Taught in [gh stack link and the stack on GitHub](../stacks/gh-stack/02-gh-stack-on-github.md).

**node shape.** The outline Mermaid draws around a node, chosen by the brackets around its label: a box, a rounded box, a diamond or a cylinder. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).

**participant.** One column of a sequence diagram: a person, an agent or a system, declared with a short id and a name. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**pointer.** A branch name that points at one commit of a linear history, made with git branch and holding no commit of its own. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**sequence diagram.** A Mermaid diagram of participants side by side, with the messages between them drawn top to bottom in the order they happen. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**stack of pull requests.** An ordered series of pull requests, each based on the one below it, so that each shows only its own change, merged from the bottom up. Taught in [A stack of pull requests](../stacks/gh-stack/01-a-stack-of-pull-requests.md).

**start and end state.** The point written [*] in a state diagram: the start when an arrow leaves it, the end when an arrow enters it. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**state diagram.** A Mermaid diagram of states and the transitions between them, each transition labelled with what causes it. Taught in [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md).

**subgraph.** A named box drawn around a group of nodes in a flowchart, which may have its own direction. Taught in [Flowcharts](../languages/mermaid/01-flowcharts.md).
