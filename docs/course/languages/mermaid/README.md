# Mermaid: what else it offers

The course teaches the parts of Mermaid that this repository uses, to full depth. This page shows the boundary: what else Mermaid offers, whether this repository uses it, and why not when it does not. It is a map, not a course; each row sends you to the official documentation.

The lessons:

1. [Flowcharts](01-flowcharts.md)
2. [Sequence and state diagrams](02-sequence-and-state-diagrams.md)
3. [Entity-relationship diagrams and the palette](03-entity-relationship-diagrams-and-the-palette.md)

| Topic | Feature | In one line | Used here | Official docs |
|---|---|---|---|---|
| Diagram types | Flowcharts | Nodes and edges in one main direction. | Used: [Flowcharts](01-flowcharts.md) | [Flowcharts](https://mermaid.js.org/syntax/flowchart.html) |
| Diagram types | Sequence diagrams | Participants and the order of their messages. | Used: [Sequence and state diagrams](02-sequence-and-state-diagrams.md) | [Sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) |
| Diagram types | State diagrams | States and what moves between them. | Used: [Sequence and state diagrams](02-sequence-and-state-diagrams.md) | [State diagrams](https://mermaid.js.org/syntax/stateDiagram.html) |
| Diagram types | Entity-relationship diagrams | Tables, columns and relationships. | Used: [Entity-relationship diagrams and the palette](03-entity-relationship-diagrams-and-the-palette.md) | [Entity-relationship diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) |
| Diagram types | Mind maps | A central idea with branches. | Not used: dropped from the standard's list of diagram types because a reviewer measured them as not legible in both themes with the pinned renderer ([revision 1, D9](../../../superpowers/specs/2026-11-18-baseline-standard-revision-1-design.md)) | [Mind maps](https://mermaid.js.org/syntax/mindmap.html) |
| Diagram types | Timelines | Events along a time line. | Not used: the standard lists them among the types Mermaid covers, and no document here needed one | [Timelines](https://mermaid.js.org/syntax/timeline.html) |
| Diagram types | User journeys | A journey's steps with a score for each. | Not used: the standard lists them, and the feature docs draw journeys as flowcharts; the reason for that choice is not recorded | [User journeys](https://mermaid.js.org/syntax/userJourney.html) |
| Diagram types | Packet diagrams | The layout of the bytes of a message. | Not used: the standard lists them for byte layouts, and this repository has none | [Packet diagrams](https://mermaid.js.org/syntax/packet.html) |
| Diagram types | Gantt charts | Tasks along a schedule. | Not used: the standard does not list them, and its documents hold no schedules, because plans live in the spec and the plan | [Gantt charts](https://mermaid.js.org/syntax/gantt.html) |
| Diagram types | Class diagrams | Classes, their members and their relations. | Not used: the repository has no classes; the standard does not list them | [Class diagrams](https://mermaid.js.org/syntax/classDiagram.html) |
| Diagram types | Git graphs | Commits, branches and merges. | Not used: the standard draws stacks and pointers as flowcharts; the reason is not recorded | [Git graphs](https://mermaid.js.org/syntax/gitgraph.html) |
| Styling | Themes and theme overrides | Change the colours of one diagram or of all. | Not used: the theme rules forbid any theme override, so every diagram follows the reader's theme ([ADR 0020](../../../adr/0020-diagram-tooling-and-theme.md)) | [Theming](https://mermaid.js.org/config/theming.html) |
| Styling | `style` and `linkStyle` | Colour one node or one edge. | Not used: forbidden by the theme rules ([ADR 0020](../../../adr/0020-diagram-tooling-and-theme.md)) | [Flowcharts: styling](https://mermaid.js.org/syntax/flowchart.html) |
| Styling | `classDef` and `class` | Named colours that nodes share. | Used, for the approved palette only: [Entity-relationship diagrams and the palette](03-entity-relationship-diagrams-and-the-palette.md) | [Flowcharts: classes](https://mermaid.js.org/syntax/flowchart.html) |
| Text | Quoted labels and `<br/>` | Text read as a label, broken over lines. | Used: [Flowcharts](01-flowcharts.md) | [Flowcharts](https://mermaid.js.org/syntax/flowchart.html) |
| Text | Markdown strings | A label written in backticks, formatted as Markdown. | Used, to name a real file in a node: [Flowcharts](01-flowcharts.md) | [Flowcharts: Markdown strings](https://mermaid.js.org/syntax/flowchart.html) |
| Layout | Direction and subgraphs | The main axis, and boxes around groups. | Used: [Flowcharts](01-flowcharts.md) | [Flowcharts](https://mermaid.js.org/syntax/flowchart.html) |
| Interaction | Clicks and links on nodes | A node that opens a link. | Not used: no document here has one; the reason is not recorded | [Flowcharts: interaction](https://mermaid.js.org/syntax/flowchart.html) |
| Tooling | mermaid-cli | Render a diagram to an image from the command line. | Not used in the repository: the build rendered the standard with it outside the repository, the docs agent rendered every diagram of the repository with version 12.2.0 in dark and light outside it, and the checker that is to render every diagram does not exist ([ADR 0026](../../../adr/0026-checker-language.md)) | [mermaid-cli](https://github.com/mermaid-js/mermaid-cli) |
| Ecosystem | GitHub's rendering of Mermaid | GitHub draws a `mermaid` block in a Markdown file. | Used: it is how every diagram here is read ([ADR 0022](../../../adr/0022-reading-venue.md)) | [Creating diagrams on GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) |
