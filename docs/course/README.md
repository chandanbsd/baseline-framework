<!-- Generated index of docs/course/. No generator exists yet, so the docs agent writes it, in this form, as the single writer of its stack (standard/17-evidence-and-truth.md, rule 11). Do not edit it by hand. -->

# The guided course

The course teaches this repository to the people who join it. Its shape is set in [standard/08-course-lessons.md](../../standard/08-course-lessons.md), [standard/09-course-system-chapters.md](../../standard/09-course-system-chapters.md) and [standard/10-course-reference-pages.md](../../standard/10-course-reference-pages.md).

## Language lessons

### Mermaid

The diagram language of every document. [What else it offers](languages/mermaid/README.md).

| Lesson | What you will learn | Reading time |
|---|---|---|
| [Flowcharts](languages/mermaid/01-flowcharts.md) | How the standard's flowcharts are built, from direction and node shapes to edge labels, dotted edges and subgraphs, and the rules that keep every one readable in both themes. | 27 min |
| [Sequence and state diagrams](languages/mermaid/02-sequence-and-state-diagrams.md) | How the standard draws who does what in what order with sequence diagrams, and what can happen from each status with state diagrams, including notes, alternatives, start and end states and states with plain-language names. | 25 min |
| [Entity-relationship diagrams and the palette](languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md) | How the standard draws a database schema as an entity-relationship diagram, how it marks what a PR adds, changes and removes, and why the approved palette is the one colour a diagram may set. | 20 min |

## Stack lessons

### gh stack and stacked PRs

How work reaches GitHub as a stack of pull requests. [What else it offers](stacks/gh-stack/README.md).

| Lesson | What you will learn | Reading time |
|---|---|---|
| [A stack of pull requests](stacks/gh-stack/01-a-stack-of-pull-requests.md) | What a stack of pull requests is, and how this repository makes one by hand with plain git: bases, one linear history, pointer branches, the kind of each commit read from its paths, and the check that the branches form one chain. | 25 min |
| [gh stack link and the stack on GitHub](stacks/gh-stack/02-gh-stack-on-github.md) | How a stack cut with plain git becomes a stack on GitHub with gh stack link, how to check that every PR has the right base and is ready, what gh stack view shows for such a stack, and which commands of gh stack the baseline never uses. | 21 min |

## System chapters

### How we build

The course on the baseline itself: why it exists, then one chapter for each flow of the framework.

| Chapter | What you will learn | Reading time |
|---|---|---|
| [Why this exists](system/01-why-this-exists.md) | Why the baseline exists, the ladder from Software Engineer to Distinguished Engineer, and which documents and workflows carry each rung, so that every later chapter can be read as serving one of them. | 16 min |
| [A feature goes from brainstorm to merged stack](system/02-brainstorm-to-merged-stack.md) | How one piece of work travels from a brainstorm to a merged stack: the spec and the plan as the first two PRs, the build that the baseline leaves untouched, the cut, the docs section on top, the publish and the merge, and where each step can go wrong. | 21 min |
| [A decision becomes an ADR](system/03-decision-to-adr.md) | How a decision becomes an ADR: the test that tells a decision of impact from a ruling, the draft written at decision time, the docs agent's review within its guard rail, the number and the move to Proposed, and acceptance at the merge. | 18 min |
| [The docs agent writes the docs section](system/04-docs-agent-writes-the-docs-section.md) | How a fresh docs agent turns a finished tip into the docs section: how it is started, what it reads and never reads, the four groups it writes in reading order, how it checks each claim, and how it hands over. | 22 min |
| [A preference becomes a standard](system/05-preference-to-standard.md) | How a preference the Software Engineer states becomes a standard that drives code: the proposal in the chat, the yes that alone writes it, the four records beside the rule, the thinking PR where it lands, and how agents read it and the docs agent cites it. | 16 min |
| [A project starts with the intake](system/06-a-project-starts-with-the-intake.md) | How a project starts on the baseline: the intake's four groups of questions, the reader profile and the standards folder they produce, baseline.yml, the one commit that goes straight to main, and what adopting the baseline in an existing repository is to do. | 15 min |
| [How documents stay true](system/07-how-documents-stay-true.md) | How the baseline keeps its documents true: the eleven evidence rules a claim passes through, the indexes with a single writer until generators exist, the checks and the stack gate that the standard requires of its tooling, and what can be checked by hand today. | 18 min |

## Reference pages

| Page | What it holds |
|---|---|
| [The file map](reference/file-map.md) | Every tracked file, with one line on what it does and the lesson or chapter that explains it. |
| [The technical glossary](reference/glossary.md) | The terms the lessons and chapters declare, each with a plain definition and a link to where it is taught. |
