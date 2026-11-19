<!-- Generated: the file map, every tracked file. No generator exists yet, so the docs agent writes it as the single writer of its stack (standard/17-evidence-and-truth.md, rule 11). Do not edit it by hand. -->

# File map

Every tracked file of the repository, with one line on what it does and the lesson or chapter of the course that explains it, taken from the `files` in each one's header. A Markdown file's opening paragraph serves as its line ([standard/10-course-reference-pages.md](../../../standard/10-course-reference-pages.md)), and the standard leaves to the tooling how the line is cut from it. No tool does that yet, so the docs agent wrote each line from the file, and for an ADR the line is its number and title. The two files that are not Markdown, `.gitignore` and `baseline.yml`, carry no one-line header comment, so their lines too were written from the file.

Files: 122.

| Path | What it does | The lesson that explains it |
|---|---|---|
| [`.gitignore`](../../../.gitignore) | Keeps the build's scratch folder, `.superpowers/`, and `.DS_Store` out of git. | None |
| [`AGENTS.md`](../../../AGENTS.md) | The primary instruction for agents: who decides, the seven core rules with their reasons, the playbooks and the repo map. | None |
| [`CLAUDE.md`](../../../CLAUDE.md) | A two-line pointer to `AGENTS.md`. | None |
| [`README.md`](../../../README.md) | The front door: why the baseline exists, what it is, how to apply it by hand and how to contribute. | None |
| [`baseline.yml`](../../../baseline.yml) | The baseline's configuration for this repository: version, artifact map, stack folders and standards. | None |
| [`docs/adr/0001-adrs-with-options-explored.md`](../../../docs/adr/0001-adrs-with-options-explored.md) | ADR 0001: Record decisions as ADRs with the options explored. | None |
| [`docs/adr/0002-baseline-scope.md`](../../../docs/adr/0002-baseline-scope.md) | ADR 0002: Baseline scope. | None |
| [`docs/adr/0003-delivery-standard-kit-skills.md`](../../../docs/adr/0003-delivery-standard-kit-skills.md) | ADR 0003: Delivery. | None |
| [`docs/adr/0004-reader-profile-is-the-target-team.md`](../../../docs/adr/0004-reader-profile-is-the-target-team.md) | ADR 0004: The reader profile is the target team. | None |
| [`docs/adr/0005-detail-always-maximum.md`](../../../docs/adr/0005-detail-always-maximum.md) | ADR 0005: Detail is always maximum. | None |
| [`docs/adr/0006-comparisons-in-marked-asides.md`](../../../docs/adr/0006-comparisons-in-marked-asides.md) | ADR 0006: Comparisons with a known stack. | None |
| [`docs/adr/0007-docs-at-top-of-stack.md`](../../../docs/adr/0007-docs-at-top-of-stack.md) | ADR 0007: Descriptive docs at the top of the stack. | None |
| [`docs/adr/0008-fresh-docs-agent.md`](../../../docs/adr/0008-fresh-docs-agent.md) | ADR 0008: The docs author. | None |
| [`docs/adr/0009-one-kind-per-pr.md`](../../../docs/adr/0009-one-kind-per-pr.md) | ADR 0009: One kind per PR, for easier review. | None |
| [`docs/adr/0010-skill-artifacts.md`](../../../docs/adr/0010-skill-artifacts.md) | ADR 0010: Skill-produced artifacts. | None |
| [`docs/adr/0011-adr-authorship-and-approval.md`](../../../docs/adr/0011-adr-authorship-and-approval.md) | ADR 0011: ADR authorship and approval. | None |
| [`docs/adr/0012-adr-placement-in-stack.md`](../../../docs/adr/0012-adr-placement-in-stack.md) | ADR 0012: ADR placement in the stack. | None |
| [`docs/adr/0013-one-repo-per-project.md`](../../../docs/adr/0013-one-repo-per-project.md) | ADR 0013: One repo per project. | None |
| [`docs/adr/0014-course-scope.md`](../../../docs/adr/0014-course-scope.md) | ADR 0014: Course scope. | None |
| [`docs/adr/0015-course-tiers.md`](../../../docs/adr/0015-course-tiers.md) | ADR 0015: Course tiers. | None |
| [`docs/adr/0016-practice-standard.md`](../../../docs/adr/0016-practice-standard.md) | ADR 0016: Practice standard. | None |
| [`docs/adr/0017-architecture-reference-form.md`](../../../docs/adr/0017-architecture-reference-form.md) | ADR 0017: Architecture reference form. | None |
| [`docs/adr/0018-feature-docs.md`](../../../docs/adr/0018-feature-docs.md) | ADR 0018: Feature docs. | None |
| [`docs/adr/0019-generated-indexes.md`](../../../docs/adr/0019-generated-indexes.md) | ADR 0019: Indexes. | None |
| [`docs/adr/0020-diagram-tooling-and-theme.md`](../../../docs/adr/0020-diagram-tooling-and-theme.md) | ADR 0020: Diagram tooling and theme. | None |
| [`docs/adr/0021-database-diagrams.md`](../../../docs/adr/0021-database-diagrams.md) | ADR 0021: Database diagrams. | None |
| [`docs/adr/0022-reading-venue.md`](../../../docs/adr/0022-reading-venue.md) | ADR 0022: Reading venue. | None |
| [`docs/adr/0023-enforcement.md`](../../../docs/adr/0023-enforcement.md) | ADR 0023: Enforcement. | None |
| [`docs/adr/0024-standards-folder.md`](../../../docs/adr/0024-standards-folder.md) | ADR 0024: Standards folder. | None |
| [`docs/adr/0025-update-mechanism.md`](../../../docs/adr/0025-update-mechanism.md) | ADR 0025: The update mechanism. | None |
| [`docs/adr/0026-checker-language.md`](../../../docs/adr/0026-checker-language.md) | ADR 0026: Checker language. | None |
| [`docs/adr/0027-worked-example.md`](../../../docs/adr/0027-worked-example.md) | ADR 0027: The worked example. | None |
| [`docs/adr/0028-build-order.md`](../../../docs/adr/0028-build-order.md) | ADR 0028: Build order. | None |
| [`docs/adr/0029-conventions.md`](../../../docs/adr/0029-conventions.md) | ADR 0029: Conventions. | None |
| [`docs/adr/0030-agents-md-shape.md`](../../../docs/adr/0030-agents-md-shape.md) | ADR 0030: Shape of AGENTS.md. | None |
| [`docs/adr/0031-software-engineer-and-the-ladder.md`](../../../docs/adr/0031-software-engineer-and-the-ladder.md) | ADR 0031: The Software Engineer and the ladder as the baseline's why. | None |
| [`docs/adr/0032-five-generated-indexes.md`](../../../docs/adr/0032-five-generated-indexes.md) | ADR 0032: Five generated indexes. | None |
| [`docs/adr/0033-adr-status-recording.md`](../../../docs/adr/0033-adr-status-recording.md) | ADR 0033: Who records an ADR's acceptance and rejection. | None |
| [`docs/adr/0034-update-moves-baseline-version.md`](../../../docs/adr/0034-update-moves-baseline-version.md) | ADR 0034: The update's code group moves baseline_version. | None |
| [`docs/adr/0035-pr-kinds-of-baseline-yml-and-folder-files.md`](../../../docs/adr/0035-pr-kinds-of-baseline-yml-and-folder-files.md) | ADR 0035: The PR kinds of baseline.yml and of a stack folder's README.md and AGENTS.md. | None |
| [`docs/adr/README.md`](../../../docs/adr/README.md) | The generated index of the ADRs, by area and by number. | None |
| [`docs/agents/adrs.md`](../../../docs/agents/adrs.md) | The playbook on ADR drafts, their lifecycle, the docs agent's guard rail and the presence check. | None |
| [`docs/agents/docs-agent.md`](../../../docs/agents/docs-agent.md) | The brief of the docs agent: what it reads, never reads and produces, and when it stops and asks. | None |
| [`docs/agents/pr-descriptions.md`](../../../docs/agents/pr-descriptions.md) | The playbook on PR descriptions: the header, the three forms and keeping stack tables current. | None |
| [`docs/agents/stacks.md`](../../../docs/agents/stacks.md) | The playbook on stacks: the three kinds, the rules, `gh stack`, cutting and opening a stack, and the seams. | None |
| [`docs/agents/standards.md`](../../../docs/agents/standards.md) | The playbook on a project's standards: what belongs, how a preference becomes a rule, and wrong code. | None |
| [`docs/agents/working-with-the-engineer.md`](../../../docs/agents/working-with-the-engineer.md) | The playbook on who decides what, numbered decisions, hand-overs, reports and rulings. | None |
| [`docs/architecture/01-overview.md`](../../../docs/architecture/01-overview.md) | Architecture: what the baseline is, its technology choices, quality goals and big picture. | None |
| [`docs/architecture/02-the-standard.md`](../../../docs/architecture/02-the-standard.md) | Architecture: the components, the files of the standard and the playbooks, and their dependency direction. | None |
| [`docs/architecture/03-the-stack-model.md`](../../../docs/architecture/03-the-stack-model.md) | Architecture: the flow from brainstorm to merged stack, a PR's life and the stack's contracts. | None |
| [`docs/architecture/04-the-docs-agent.md`](../../../docs/architecture/04-the-docs-agent.md) | Architecture: the docs agent as a procedure, its states and its inputs and outputs. | None |
| [`docs/architecture/05-decisions-and-adrs.md`](../../../docs/architecture/05-decisions-and-adrs.md) | Architecture: how a decision becomes an ADR, the ADR lifecycle and the ADR's contract. | None |
| [`docs/architecture/06-standards-and-the-reader-profile.md`](../../../docs/architecture/06-standards-and-the-reader-profile.md) | Architecture: the intake, the standards mechanism and the formats of their files. | None |
| [`docs/architecture/07-evidence-and-checks.md`](../../../docs/architecture/07-evidence-and-checks.md) | Architecture: how documents stay true, the required checks and the quality section. | None |
| [`docs/architecture/08-cross-cutting.md`](../../../docs/architecture/08-cross-cutting.md) | Architecture: data, concurrency, security and trust, operations, known limits and where decisions live. | None |
| [`docs/architecture/README.md`](../../../docs/architecture/README.md) | The generated index of the architecture reference, with where each minimum section is. | None |
| [`docs/course/README.md`](../../../docs/course/README.md) | The generated index of the guided course. | None |
| [`docs/course/languages/mermaid/01-flowcharts.md`](../../../docs/course/languages/mermaid/01-flowcharts.md) | Lesson: flowcharts, the diagram the standard draws most. | None |
| [`docs/course/languages/mermaid/02-sequence-and-state-diagrams.md`](../../../docs/course/languages/mermaid/02-sequence-and-state-diagrams.md) | Lesson: sequence diagrams and state diagrams. | None |
| [`docs/course/languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md`](../../../docs/course/languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md) | Lesson: entity-relationship diagrams, the change markers and the approved palette. | None |
| [`docs/course/languages/mermaid/README.md`](../../../docs/course/languages/mermaid/README.md) | The Mermaid map: what else Mermaid offers, and whether this repository uses it. | None |
| [`docs/course/reference/file-map.md`](../../../docs/course/reference/file-map.md) | This file map: every tracked file, what it does and where it is taught. | None |
| [`docs/course/reference/file-map.md`](../../../docs/course/reference/file-map.md) | This file map: every tracked file, what it does and where it is taught. | None |
| [`docs/course/reference/file-map.md`](../../../docs/course/reference/file-map.md) | This file map: every tracked file, what it does and where it is taught. | None |
| [`docs/course/reference/glossary.md`](../../../docs/course/reference/glossary.md) | The technical glossary, assembled from the terms that the lessons and chapters declare. | None |
| [`docs/deploy/01-topology.md`](../../../docs/deploy/01-topology.md) | Deployment: the local repository and the private repository on GitHub, and how work reaches readers. | None |
| [`docs/deploy/02-environments.md`](../../../docs/deploy/02-environments.md) | Deployment: the two environments, and the absence of CI, staging and production. | None |
| [`docs/deploy/03-infrastructure-as-code.md`](../../../docs/deploy/03-infrastructure-as-code.md) | Deployment: infrastructure as code, not applicable. | None |
| [`docs/deploy/04-configuration-and-secrets.md`](../../../docs/deploy/04-configuration-and-secrets.md) | Deployment: every setting of `baseline.yml` and of the reader profile's header, and no secrets. | None |
| [`docs/deploy/05-build-and-release-pipeline.md`](../../../docs/deploy/05-build-and-release-pipeline.md) | Deployment: no build or release; a merged stack is what readers read. | None |
| [`docs/deploy/06-deploying.md`](../../../docs/deploy/06-deploying.md) | Deployment: the runbook for publishing and merging the stack. | None |
| [`docs/deploy/07-rollback-and-recovery.md`](../../../docs/deploy/07-rollback-and-recovery.md) | Deployment: rollback and recovery, not applicable. | None |
| [`docs/deploy/08-operations.md`](../../../docs/deploy/08-operations.md) | Deployment: operations, not applicable. | None |
| [`docs/deploy/09-security-and-hardening.md`](../../../docs/deploy/09-security-and-hardening.md) | Deployment: the repository's access model and what was checked about it. | None |
| [`docs/deploy/10-cost.md`](../../../docs/deploy/10-cost.md) | Deployment: cost, with the GitHub plan not checked. | None |
| [`docs/deploy/11-troubleshooting.md`](../../../docs/deploy/11-troubleshooting.md) | Deployment: symptoms while the stack is half published, with checks and fixes. | None |
| [`docs/deploy/README.md`](../../../docs/deploy/README.md) | The front of the deployment docs: the eleven areas and what each says here. | None |
| [`docs/features/README.md`](../../../docs/features/README.md) | Feature docs: what the baseline gives a project, its capability map and its features. | None |
| [`docs/features/access.md`](../../../docs/features/access.md) | Feature docs: the kinds of user, the roles, the conditions and the who-can-do-what matrix. | None |
| [`docs/features/decision-records.md`](../../../docs/features/decision-records.md) | Feature page: decisions recorded with their options. | None |
| [`docs/features/delivery-as-a-stack.md`](../../../docs/features/delivery-as-a-stack.md) | Feature page: work delivered as a stack of reviews. | None |
| [`docs/features/document-set.md`](../../../docs/features/document-set.md) | Feature page: the complete set of documents a project keeps. | None |
| [`docs/features/documents-from-what-was-built.md`](../../../docs/features/documents-from-what-was-built.md) | Feature page: documents written by a fresh agent from what was built. | None |
| [`docs/features/documents-pitched-for-the-team.md`](../../../docs/features/documents-pitched-for-the-team.md) | Feature page: the reader profile and documents pitched for the team. | None |
| [`docs/features/documents-that-stay-true.md`](../../../docs/features/documents-that-stay-true.md) | Feature page: the evidence rules and diagrams that keep documents true. | None |
| [`docs/features/glossary.md`](../../../docs/features/glossary.md) | The product glossary, in plain language. | None |
| [`docs/features/standards.md`](../../../docs/features/standards.md) | Feature page: rules from the Software Engineer's approved preferences. | None |
| [`docs/features/working-with-the-software-engineer.md`](../../../docs/features/working-with-the-software-engineer.md) | Feature page: who decides what, numbered decisions and reports. | None |
| [`docs/reader-profile.md`](../../../docs/reader-profile.md) | Who the documents are written for: the header of levels, and the sections generated from it. | None |
| [`docs/reader-profile.md`](../../../docs/reader-profile.md) | Who the documents are written for: the header of levels, and the sections generated from it. | None |
| [`docs/reader-profile.md`](../../../docs/reader-profile.md) | Who the documents are written for: the header of levels, and the sections generated from it. | None |
| [`docs/standards/README.md`](../../../docs/standards/README.md) | How the standards folder fills; it holds no approved rule yet. | None |
| [`docs/superpowers/plans/2026-11-14-baseline-standard.md`](../../../docs/superpowers/plans/2026-11-14-baseline-standard.md) | The plan of design 1's build, as `writing-plans` produced it. | None |
| [`docs/superpowers/specs/2026-11-14-baseline-decision-trail.md`](../../../docs/superpowers/specs/2026-11-14-baseline-decision-trail.md) | The decision trail: the context, options and reasons behind design 1's 31 decisions. | None |
| [`docs/superpowers/specs/2026-11-14-baseline-standard-design.md`](../../../docs/superpowers/specs/2026-11-14-baseline-standard-design.md) | Design 1, the standard: the spec of this repository, as brainstorming produced it. | None |
| [`docs/superpowers/specs/2026-11-18-baseline-standard-revision-1-design.md`](../../../docs/superpowers/specs/2026-11-18-baseline-standard-revision-1-design.md) | Revision 1 of design 1: the Software Engineer's decisions after the first build. | None |
| [`docs/superpowers/specs/2026-11-18-baseline-standard-revision-2-design.md`](../../../docs/superpowers/specs/2026-11-18-baseline-standard-revision-2-design.md) | Revision 2 of design 1: the answers to what revision 1 left open. | None |
| [`docs/superpowers/specs/2026-11-18-baseline-standard-revision-3-design.md`](../../../docs/superpowers/specs/2026-11-18-baseline-standard-revision-3-design.md) | Revision 3 of design 1: the answers to the decisions in the first docs run's report. | None |
| [`standard/01-why-and-scope.md`](../../../standard/01-why-and-scope.md) | The standard: who the baseline is for, the ladder, and the goals, non-goals, anti-goals and constraints. | None |
| [`standard/02-vocabulary.md`](../../../standard/02-vocabulary.md) | The standard: the three roles and every term. | None |
| [`standard/03-stack-model.md`](../../../standard/03-stack-model.md) | The standard: the stack of PRs, the three kinds, the thirteen rules and the conventions. | [Flowcharts](../languages/mermaid/01-flowcharts.md) |
| [`standard/04-reader-profile.md`](../../../standard/04-reader-profile.md) | The standard: the reader profile, the intake and the sections generated from it. | None |
| [`standard/05-project-layout.md`](../../../standard/05-project-layout.md) | The standard: where every document lives, `baseline.yml`, ownership and the artifact map. | [Flowcharts](../languages/mermaid/01-flowcharts.md) |
| [`standard/06-feature-docs.md`](../../../standard/06-feature-docs.md) | The standard: the feature docs. | [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md) |
| [`standard/07-architecture-reference.md`](../../../standard/07-architecture-reference.md) | The standard: the architecture reference and its thirteen minimum sections. | None |
| [`standard/08-course-lessons.md`](../../../standard/08-course-lessons.md) | The standard: the course's tiers, the lesson anatomy, the lesson header and the practice standard. | None |
| [`standard/09-course-system-chapters.md`](../../../standard/09-course-system-chapters.md) | The standard: the system chapters, their labs and their practice. | None |
| [`standard/10-course-reference-pages.md`](../../../standard/10-course-reference-pages.md) | The standard: the file map, the glossaries, the what-else maps and the generated indexes. | None |
| [`standard/11-adrs.md`](../../../standard/11-adrs.md) | The standard: the ADR template, decisions of impact, the lifecycle, the guard rail and the presence check. | [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md) |
| [`standard/12-deployment-docs.md`](../../../standard/12-deployment-docs.md) | The standard: the deployment docs, their eleven areas and the honesty rule. | None |
| [`standard/13-project-readme.md`](../../../standard/13-project-readme.md) | The standard: the README's ten parts and the stack folders' READMEs. | [Flowcharts](../languages/mermaid/01-flowcharts.md) |
| [`standard/14-pr-descriptions.md`](../../../standard/14-pr-descriptions.md) | The standard: the PR description header and the three forms. | [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md) |
| [`standard/15-agents-md-and-playbooks.md`](../../../standard/15-agents-md-and-playbooks.md) | The standard: `AGENTS.md`, `CLAUDE.md` and the six playbooks. | None |
| [`standard/16-diagrams.md`](../../../standard/16-diagrams.md) | The standard: diagrams, their minimums, quality and theme rules, and the approved palette. | [Flowcharts](../languages/mermaid/01-flowcharts.md), [Entity-relationship diagrams and the palette](../languages/mermaid/03-entity-relationship-diagrams-and-the-palette.md) |
| [`standard/17-evidence-and-truth.md`](../../../standard/17-evidence-and-truth.md) | The standard: the eleven evidence rules and the bootstrap exception for indexes. | [Sequence and state diagrams](../languages/mermaid/02-sequence-and-state-diagrams.md) |
| [`standard/18-docs-agent.md`](../../../standard/18-docs-agent.md) | The standard: the docs agent and its six rules. | None |
| [`standard/19-standards-mechanism.md`](../../../standard/19-standards-mechanism.md) | The standard: how approved preferences become a project's standards. | None |
| [`standard/20-working-rules.md`](../../../standard/20-working-rules.md) | The standard: who decides what, decisions, hand-overs and reports. | None |
| [`standard/21-skills-seams.md`](../../../standard/21-skills-seams.md) | The standard: the nine seams with the skills. | None |
| [`standard/22-tooling-requirements.md`](../../../standard/22-tooling-requirements.md) | The standard: what the kit, the checkers and the skills must do. | None |
| [`standard/AGENTS.md`](../../../standard/AGENTS.md) | The instructions for working in `standard/`: no commands, its layout and the rule for links between its numbered files. | None |
| [`standard/README.md`](../../../standard/README.md) | The standard's index: what it is, the why, how to read it and its contents. | [Flowcharts](../languages/mermaid/01-flowcharts.md) |
