# The Baseline Standard: the decision trail

**Companion to** [design 1, the standard](2026-11-14-baseline-standard-design.md) · 2026-11-14

This file is the record of the brainstorm behind every decision in Appendix A of design 1. It exists so that the 31 ADRs can be written from a source, not reconstructed from memory: each entry gives the context, the drivers, the options as they were put to the Software Engineer, the pick and the reason, the evidence that was gathered, the consequences, and when to revisit.

**How to use it.** The regular agent that builds design 1 writes each ADR as a **draft** from its entry here; the docs agent then reviews the drafts within the guard rail (design 1, section 11.3). Where an entry says **not recorded**, nothing was discussed or measured and the ADR must say so; it must not invent a pro, a con or a number. Quotations are the Software Engineer's words from the brainstorm.

| Mark | Meaning |
|---|---|
| **Software Engineer** | The Software Engineer chose or approved it. |
| **Writer** | The writer proposed it and the Software Engineer approved the proposal. |

---

## 0001. Record decisions as ADRs with the options explored

- **Context.** The Software Engineer's first request names "architectural decision records documenting the technical decisions that were taken, options explored". The reference projects' records are thin: the-way's template is Context, Decision, Consequences (its ADR 0003 is 15 lines); my-quote keeps nine decisions in one file with Decision, Why, Consequences.
- **Drivers.** Options and evidence must be visible; records must be durable and reviewable by architects in the monthly read.
- **Options.** (a) the-way's three-part template: short, but no alternatives. (b) my-quote's one-file Decision/Why: better on the why, still no alternatives. (c) a full skeleton: context, ranked drivers, options with how-it-works diagram, pros, cons and evidence, comparison, decision, consequences, revisit signals, links.
- **Pick.** (c). **Software Engineer** bar: "options explored".
- **Evidence.** Reading `docs/adr/0003-sqlite-as-the-database.md` and `docs/deployment/ARCHITECTURE_DECISIONS.md`.
- **Consequences.** Heavier records; the guard rail and decision-time drafting are needed to keep the reasoning honest.
- **Revisit when.** The skeleton proves too heavy for small decisions, which would move them to rulings.

## 0002. Baseline scope

- **Context.** After the writer had added overlays per kind of project, security enforcement and verification tiers, the Software Engineer said the baseline is "more so the documentation structure that any project should follow", plus coding standards, "which are also nothing but documentation". Vulnerability checks, secrets handling and the like are "per project decisions" and often cannot be enforced.
- **Drivers.** Avoid rigidity ("we can't be overly rigid without knowing the project type, kind and goal"); keep the baseline the same for every kind.
- **Options.** (a) documentation structure, stack workflow and standards mechanism. (b) (a) plus per-kind overlays and per-stack slicing recipes. (c) (a) plus enforced security, dependency, verification and release policy.
- **Pick.** (a). **Software Engineer.** The Software Engineer's test: "Whether I build an AI application or a web application, how is the baseline going to change?" The answer is that it does not; what differs is what the docs say.
- **Evidence.** None beyond the Software Engineer's reasoning.
- **Consequences.** A smaller baseline; per-project preferences accumulate in `docs/standards/`; far fewer mechanical checks.
- **Revisit when.** A rule recurs in most projects, which would promote it into the baseline through a baseline ADR.

## 0003. Delivery of the baseline

- **Context.** The Software Engineer wants the baseline to be reusable for every new project, with a prompt at project start.
- **Drivers.** Reusable; no lock-in to one tool; updates must propagate; the intake needs something that asks questions.
- **Options.** (a) a copy-in kit only: simple and agent-neutral, but copies drift. (b) a Claude Code plugin only: one source of truth, but tied to one tool and invisible to a human reading a repo. (c) a Markdown standard, a starter kit and thin skills that apply them.
- **Pick.** (c). **Writer**; the Software Engineer proceeded on it after "this should be a prompt when starting a project".
- **Evidence.** Not recorded.
- **Consequences.** More parts; the standard works without the skills.
- **Revisit when.** The skills become the only consumers, which would justify collapsing the kit into them.

## 0004. The reader profile is the target team

- **Context.** The Software Engineer first asked for a prompt about proficiency "with the tech stack", then clarified: "the answers I give will be the basis on how I will select the team to execute the project long term", and "the skill level answered here is purely for building the docs, not to reduce the scope of the technical implementation itself."
- **Drivers.** Teams vary; the profile doubles as a hiring bar; implementation quality must never depend on it.
- **Options.** (a) one level per project. (b) the Software Engineer's own level. (c) the target team's level, per technology and per knowledge area.
- **Pick.** (c). **Software Engineer.** The writer's earlier idea of tying code style to the reader's level (my-quote's "plain over clever" rule) was reversed.
- **Evidence.** my-quote's `AGENTS.md` section 1 ties code style to the Software Engineer's early-career level.
- **Consequences.** The profile is an input only the Software Engineer can give; a technology with no entry stops the docs agent.
- **Revisit when.** The team grows and areas get their own deciders.

## 0005. Detail is always maximum

- **Context.** The Software Engineer: detail "should be maximum regardless"; for an average reader "a for loop need not be explained but the architecture of the code still need to be specified regardless".
- **Options.** (a) scale detail to the level. (b) fix the detail and scale only the basics.
- **Pick.** (b). **Software Engineer.**
- **Evidence.** Not recorded.
- **Consequences.** The architecture, data flow, decisions and deployment are always fully documented; levels only change which basics are explained.
- **Revisit when.** Not recorded.

## 0006. Comparisons with a known stack

- **Context.** my-quote teaches Go and React through Angular and C# comparisons; the-way says "Never compare with other stacks".
- **Drivers.** The code must stay idiomatic to the stack; comparisons must never replace the stack-native explanation.
- **Options.** (a) never compare. (b) always compare with a known stack. (c) a per-technology choice at intake: compare with a named stack, or treat the technology as brand new; comparisons only in marked asides that say where the analogy breaks.
- **Pick.** (c). **Software Engineer**, who asked for exactly this prompt: "whenever to compare and contrast with a known stack (the code should still be idiomatic to the stack regardless) this is just about the docs".
- **Evidence.** The two reference repos' opposite rules.
- **Consequences.** A comparison setting per technology in the profile; asides are skippable and deletable.
- **Revisit when.** Not recorded.

## 0007. Descriptive documents at the top of the stack

- **Context.** The writer first proposed docs in each slice's PR. The Software Engineer objected: "docs should capture what was built and not what is supposed to be built".
- **Drivers.** Documents must describe the final built state; PRs must stay readable.
- **Options.** (a) docs in each slice's PR (the-way). (b) one docs PR last (my-quote). (c) a docs section of several PRs on top, split by family.
- **Pick.** (c). **Software Engineer** chose the top of the stack; the writer proposed splitting it by family.
- **Evidence.** A real lesson is 1,195 to 1,558 lines of Markdown (`learn-rust` lessons 01 and 02) against a code slice of about 400 lines, so a per-slice lesson is three to four times the size of the code; my-quote's rebase conflicts were all on shared index and number lines.
- **Consequences.** Taller stacks; a stack gate is needed because required checks apply to every PR in a stack.
- **Revisit when.** The stack gate cannot be made to work on GitHub's stacked-PR feature (design 1, V1).

## 0008. Who writes the descriptive documents

- **Context.** Following 0007, the writer asked who writes the docs section.
- **Options.** (a) the agent that built the code: cheaper, full context, but tends to document what it meant and cannot tell when the code does not say it. (b) a fresh agent working from the finished tip, reading the code, ADRs and spec but not the plan or the build conversation.
- **Pick.** (b). **Software Engineer**: "the documents need to be written by a fresh agent."
- **Evidence.** The execution skills already dispatch fresh subagents with crafted context.
- **Consequences.** More agent runs; intent that never reached an ADR shows up as a gap to fix.
- **Revisit when.** Not recorded.

## 0009. One kind per PR, for easier review

- **Context.** The Software Engineer wants every skill's artifact "to go out as separate PRs. That way it's easier to review for the reviewer who is a person to look at it, understand, make sense of it, and then go to the code in the stack." Later the Software Engineer corrected an overstated version of this in the design: a PR that holds both thinking and code is not wrong. The kinds are separated because that is easier to review, and a skill that revises its spec or plan in a later loop is free to; the point is that when PRs are opened, the revision is separated out into its own PR.
- **Options.** (a) mixed PRs. (b) three kinds, kept apart when PRs are opened: thinking, code, description.
- **Pick.** (b). **Software Engineer.** Kinds are inferred from paths. The writer's earlier drafts listed mixed PRs as an anti-goal and had a check fail them; both were withdrawn.
- **Evidence.** Not recorded.
- **Consequences.** A mixed PR gets a non-blocking notice that lists its files by kind (the writer's call). A spec or plan revision made mid-build becomes its own thinking PR instead of riding in a code PR. Small changes that touch documents become a two-PR stack.
- **Revisit when.** Not recorded.

## 0010. Skill-produced artifacts

- **Context.** The Software Engineer: "We do not want to touch documents generated by those skills." The writer's earlier steering (a stack layout in the plan, telling the planner to omit doc tasks, ADRs in the spec and plan PRs) was withdrawn. Later the Software Engineer pointed out that an earlier draft of the design said the baseline "decides where their output lands", which was misleading: superpowers can put its specs and plans wherever it wants, and the baseline only lists the additional documents that need to be built and how the PRs are arranged. The statement was corrected.
- **Options.** (a) steer where skills write and what they produce through `AGENTS.md`. (b) leave the skills alone: they write where they write, and the baseline arranges their output into one PR each and adds the description docs on top; `AGENTS.md` covers only that arrangement and the execution seams.
- **Pick.** (b). **Software Engineer.**
- **Evidence.** The superpowers 7.0.2 skill files: the spec and plan locations are overridable by user preference; `writing-plans` folds documentation steps into tasks (the one friction, handled by an execution rule); the execution skills log rulings and print "Rulings I made"; superpowers ranks `AGENTS.md` above its skills.
- **Consequences.** The seams table of design 1 section 14. The artifact map only records where a skill wrote; it never tells a skill where to write.
- **Revisit when.** A skill changes where or how it writes its artifacts.

## 0011. ADR authorship and approval

- **Context.** The writer first proposed a gate (a Proposed ADR before code, accepted by the Software Engineer). The Software Engineer: "The ADR being a gate seems like it's causing more problems than it's worth it."
- **Drivers.** The execution skills run continuously and settle conflicts as rulings; decision-time content must not be backfilled.
- **Options.** (a) an approval gate before code. (b) a record written afterwards by the docs agent. (c) the regular agent drafts at decision time and the docs agent reviews within a guard rail; the Software Engineer's merge of the stack is the acceptance.
- **Pick.** (c). **Software Engineer** proposed it; the **writer** added the guard rail, the draft numbering and the lifecycle.
- **Evidence.** Brainstorming already requires the approaches and the Software Engineer's pick; the execution skills stop only for irreversible or destructive actions, security-sensitive actions, outside side effects and a hopelessly broken plan.
- **Consequences.** A surprise decision gets the Software Engineer's eyes at stack review, so rework is possible, the same trade the skills already make.
- **Revisit when.** Mid-build decisions of impact prove frequent and costly.

## 0012. ADR placement in the stack

- **Context.** After 0011, where do drafts go?
- **Options.** (a) in the code PR that first depends on them. (b) at the end with the docs. (c) as small PRs of their own directly beneath the first slice that depends on them.
- **Pick.** (c). **Software Engineer**: the same reasoning as 0009, the reviewer reads the thinking first.
- **Evidence.** Not recorded.
- **Consequences.** A few more small PRs; each PR stays one kind, which is easier to review.
- **Revisit when.** Not recorded.

## 0013. One repository per project

- **Context.** GitHub's stacked-PR rules need all PRs of a stack in one repository, and the Software Engineer wants front-end and back-end PRs in one stack.
- **Options.** (a) one repo per stack. (b) a monorepo with a documented exception. (c) a monorepo with no exceptions.
- **Pick.** (c). **Software Engineer**: "There will only be one repo per project, and this is an intentional pattern and rule that we will not break apart from." An SDK that must be published separately becomes a folder published by CI as a package.
- **Evidence.** GitHub's rules as recorded in the Software Engineer's `learn-rust` design (same repository, bottom-up merge, linear history, required checks per PR); my-quote is already a monorepo with `api/`, `app/` and `desktop/`.
- **Consequences.** CI needs per-stack path filters; docs and the system course sit next to the code; one agent session sees the whole product.
- **Revisit when.** Not recorded.

## 0014. Scope of the courses

- **Context.** The Software Engineer wants a guided course for the language and the stack, "zero to advanced", and that "lives and grows along with the project codebase".
- **Options.** (a) codebase-scoped at full depth plus a short "what else it offers" map. (b) a whole-language curriculum regardless of the code.
- **Pick.** (a). **Software Engineer**: "They will be code-based scoped." Whole-language courses (like `learn-rust`, 74 lessons) stay a separate product; lessons seed the next project in that language.
- **Evidence.** `learn-rust` is already a standalone curriculum.
- **Consequences.** A reader can follow every line of this system but does not finish having seen features the code does not use; the map shows the boundary.
- **Revisit when.** Not recorded.

## 0015. Course tiers

- **Options.** (a) one course. (b) language and stack. (c) language, stack and system.
- **Pick.** (c). **Software Engineer**: one for the stack, the language as well, "then finally, all together combined, interactions between them will be a guided course."
- **Evidence.** Not recorded.
- **Consequences.** The system course is always specific to its project and is written last.
- **Revisit when.** Not recorded.

## 0016. The practice standard

- **Context.** The Software Engineer: the courses are "about getting the regular person to think critically as an engineer and a systems thinker", relevant to the code base "but also very systems critical thinking like".
- **Options.** (a) a recap with "check yourself" questions (my-quote). (b) `learn-rust`'s 10 theory and 10 programming questions with worked answers, tilted toward systems thinking, with labs for the system course and solutions stored as patches that CI re-applies.
- **Pick.** (b). **Software Engineer**, who approved the mix: 3 predict, 3 diagnose, 2 design trade-offs, 2 systems reasoning.
- **Evidence.** `learn-rust` lesson template; my-quote's exercises chapter notes its solutions needed re-running when code changed, which the patch approach automates.
- **Consequences.** What "tested" means is the project's call per technology.
- **Revisit when.** Not recorded.

## 0017. Form of the architecture reference

- **Options.** (a) one file (the-way's `architecture.md`, 277 lines for a small system). (b) a folder with one file per area and a generated index.
- **Pick.** (b). **Software Engineer** approved the proposal. A line-by-line read and a PR review stay manageable; the sections are minimums and the docs agent adds what the system needs.
- **Evidence.** The-way's single file already mixes product information (the capability matrix, the page list) with technical content.
- **Consequences.** More files; the index is generated.
- **Revisit when.** Not recorded.

## 0018. Feature documents

- **Context.** The Software Engineer added the missing document: "the feature document is one that explains the system from the interactions point of view, something that is a non-technical document that explains what our application is capable of", then asked for roles, user types and claims.
- **Options.** (a) fold it into the architecture reference. (b) a separate non-technical document with a Users and access page and a per-feature "who can use it" table; the technical half in the architecture reference.
- **Pick.** (b). **Software Engineer.** The matrix lives only in the feature docs.
- **Evidence.** The-way keeps its capability matrix inside `architecture.md`.
- **Consequences.** Two views of access that must not drift; the architecture links to the matrix and maps each row to its enforcement and test.
- **Revisit when.** Not recorded.

## 0019. Generated indexes

- **Options.** (a) hand-edited indexes. (b) generated indexes (course index, file map, glossaries, ADR index).
- **Pick.** (b). **Writer**, approved by the Software Engineer.
- **Evidence.** my-quote's cascading rebases conflicted on number lines in shared files; `learn-rust` avoided it by never editing a shared index.
- **Consequences.** Generators are needed (design 3); until they exist the baseline's own indexes are written by the docs agent under a bootstrap exception.
- **Revisit when.** Not recorded.

## 0020. Diagram tooling and theme

- **Context.** The Software Engineer wants extensive diagrams in every document, that work in dark and light theme, and always reviews in dark.
- **Options.** (a) Mermaid only. (b) Mermaid as default with text-source fallbacks (WaveDrom, Graphviz, fenced ASCII) and never a sourceless image. For colour: no hard-coded colours at all, or an approved palette tested in both themes.
- **Pick.** (b) with an approved translucent-tint palette. **Software Engineer** approved.
- **Evidence.** A test render with Mermaid 12.3.0 (the version `learn-rust` pins): a first palette of solid fills with white text looked fine in dark and failed in light (white text on white rows); a translucent tint with a solid coloured border and no text colour worked in both.
- **Consequences.** CI renders every diagram in both themes and checks the palette.
- **Revisit when.** GitHub's bundled Mermaid proves not to render the styling (design 1, V2).

## 0021. Database diagrams

- **Context.** The Software Engineer asked whether the docs would show the current database state in Mermaid and wants PRs that change the database to show a colour-coded diagram of the current state and the changes.
- **Options.** (a) hand-drawn diagrams. (b) a current-state ER diagram generated from the real schema with a drift check, plus a CI-maintained colour-coded diff block in the PR description.
- **Pick.** (b). **Software Engineer.**
- **Evidence.** The same test render: Mermaid colours whole tables only, so column and relationship changes are marked with `+`, `~` and `-` in text.
- **Consequences.** The generator is a project decision because it depends on the database.
- **Revisit when.** As 0020.

## 0022. Reading venue

- **Options.** (a) GitHub. (b) a generated docs site. (c) a PDF or EPUB bundle.
- **Pick.** (a). **Software Engineer**: GitHub only for now, a site possible later.
- **Evidence.** Not recorded.
- **Consequences.** Documents stay GitHub-flavoured Markdown plus Mermaid so a site can be built later without a rewrite.
- **Revisit when.** The Software Engineer wants a site.

## 0023. Enforcement

- **Options.** (a) advisory only. (b) gated only. (c) mixed: mechanical checks for what a machine can check, an agent rule and a docs-owed list for judgement.
- **Pick.** (c). **Software Engineer**: "Mixed is fine. We do want this to be living, breathing docs." Later scoped to what the baseline owns (documents and its standards).
- **Evidence.** The-way's docs stay honest by convention only; my-quote's checkers catch drift.
- **Consequences.** A stack gate over the whole change, pending on lower PRs.
- **Revisit when.** The gate cannot be made to work (design 1, V1).

## 0024. The standards folder

- **Context.** The Software Engineer: put fundamental baselines, then "create an empty coding standards folder where at the initialization of the project as well as over time the user's preferences are utilized (from agent conversations) to build a coding standards document if the user approves". Also: standards and ADRs "are the only kind that drive code"; when generated code is wrong, they are updated and the code regenerated "in a fresh context".
- **Options.** (a) rigid baseline rules. (b) an opt-in folder filled from approved preferences.
- **Pick.** (b). **Software Engineer.** The writer chose the name `docs/standards/` because it also holds verification, dependency and security preferences.
- **Evidence.** my-quote's `docs/agents/` guides hold lessons with the reason beside each rule.
- **Consequences.** Nothing is inferred silently; every rule needs the Software Engineer's approval.
- **Revisit when.** Not recorded.

## 0025. The update mechanism

- **Context.** The Software Engineer asked how updates to the baseline reach a target repository.
- **Options.** (a) a git submodule or subtree: drags the whole baseline into every repo and conflicts on edited files. (b) Copier's `update`, the closest off-the-shelf tool: a three-way merge, but unnecessary given an ownership split and unable to produce a stack of one-kind PRs. (c) manual copying: drifts. (d) an ownership split (baseline-owned and project-owned files) with a versioned `/baseline:update` that opens a normal stack and runs tested migrations.
- **Pick.** (d). **Software Engineer.**
- **Evidence.** Not recorded.
- **Consequences.** Each release ships migrations and tests them against the worked example.
- **Revisit when.** Not recorded.

## 0026. The checker language

- **Options.** (a) Python, with Node only for rendering Mermaid. (b) Go or Rust: a single binary but more effort. (c) Node.
- **Pick.** (a). **Writer**, accepted by the Software Engineer. Strong at text processing, fast to change, easy to test, and my-quote's checkers (`check_tutorial.py`, `tutorial_numbers.py`) are already Python.
- **Evidence.** The existing checkers and their tests.
- **Consequences.** The team will read this code, so the choice is recorded.
- **Revisit when.** A single-binary distribution becomes necessary.

## 0027. The worked example

- **Options.** (a) a Rust notes service with a CLI client. (b) a Go API with a TypeScript client (two language courses, about double the cost). (c) a miniature replicated key-value store with a TLA+ spec (closest to the Software Engineer's work, much heavier). (d) two examples.
- **Pick.** (a). **Software Engineer.** It is small enough to finish and rich enough to show every document type, and its Rust lessons seed upcoming Rust projects. It is a reference, a test fixture and an end-to-end eval: delete its docs, regenerate them with the docs agent, run the checkers.
- **Evidence.** Not recorded.
- **Consequences.** Needs a real codebase because the docs quote it and the exercises run against it.
- **Revisit when.** A second example is wanted.

## 0028. Build order of the baseline

- **Options.** (a) standard first, proven by the example, then tooling. (b) tooling first. (c) a pilot on a copy of an existing repo.
- **Pick.** (a). **Software Engineer.**
- **Evidence.** Not recorded.
- **Consequences.** Three design documents, each approved before its build.
- **Revisit when.** Not recorded.

## 0029. Conventions

- **Context.** my-quote's `AGENTS.md` fixes branch names, commit prefixes, the PR size guide and "Never add attribution lines". Claude Code adds attribution lines by default.
- **Options.** (a) none. (b) adopt the conventions, with the no-attribution rule stated explicitly.
- **Pick.** (b). **Software Engineer** approved.
- **Evidence.** my-quote's `AGENTS.md`.
- **Consequences.** `AGENTS.md` must state the rule.
- **Revisit when.** Not recorded.

## 0030. Shape of `AGENTS.md`

- **Options.** (a) one long file. (b) a short file with playbooks that give the reason beside each rule, plus adapters for generated instruction files. (c) a generated file.
- **Pick.** (b). **Software Engineer** approved.
- **Evidence.** my-quote's `AGENTS.md` is 90 lines with a two-line `CLAUDE.md` and nine guides; the-way's `AGENTS.md` is 182 lines identical to its `CLAUDE.md` and appears generated by Laravel Boost (unconfirmed).
- **Consequences.** In generated-file projects the baseline content goes into the generator's source.
- **Revisit when.** The Boost behaviour is confirmed (design 1, V3).

## 0031. The Software Engineer and the ladder as the baseline's why

- **Context.** The writer had called the person who decides "the owner". The Software Engineer asked what that meant and said they would prefer something more technical (lead engineer, principal engineer, an architect, or "C", as typed), though "owner also doesn't matter". They then set the frame: the goal is to behave as a Distinguished Engineer, taking on the responsibilities of the Principal Engineer and the Solutions Architect, along the ladder Software Engineer, Lead Engineer, Principal Engineer, Solutions Architect, Distinguished Engineer. "We can classify the owner as 'Software Engineer' and use the above flow as the central foundation. That is the WHY for the docs to be honest."
- **Options.** (a) keep "owner". (b) Lead Engineer. (c) Principal Engineer or architect. (d) the Software Engineer on a ladder toward Distinguished Engineer, with the ladder stated as the why of the baseline.
- **Pick.** (d). **Software Engineer.** The mapping of each rung to the baseline's parts (design 1, section 1.1, the table's two right-hand columns) is the writer's call.
- **Evidence.** Not recorded.
- **Consequences.** "Owner" is replaced throughout. The playbook becomes `working-with-the-engineer` and the reader-profile field becomes `software_engineer` (writer's calls). The baseline's README and course open with the why.
- **Revisit when.** Not recorded.
