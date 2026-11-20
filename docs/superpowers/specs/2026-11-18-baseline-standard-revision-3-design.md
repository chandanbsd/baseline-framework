# The Baseline Standard: revision 3 of design 1

**Revision** · 2026-11-18 and 2026-11-19 · status: **decisions approved by the Software Engineer on 2026-11-18 and 2026-11-19; the calls in section 4 are the writer's**

This revision records the Software Engineer's answers to the decisions that the docs agent put to them after it wrote the docs section of the first stack. The docs agent's report numbered nine decisions, each with a recommendation first and its other option. The answer, given in the docs agent's session on 2026-11-18, was "Approved on all recommendations." The same message approved read-only `gh` calls and `git ls-remote`, which change no file. The report's decision 1, to publish the whole stack, changes no file either: it waits until these changes are built, the docs section is rebased and re-checked on top of them, every PR has a description and the Software Engineer has read the docs section. The other eight are recorded here as D1 to D8, which are the report's decisions 2 to 9. [Design 1, the standard](2026-11-14-baseline-standard-design.md), [its decision trail](2026-11-14-baseline-decision-trail.md), [revision 1](2026-11-18-baseline-standard-revision-1-design.md) and [revision 2](2026-11-18-baseline-standard-revision-2-design.md) stay exactly as they were written, because a revision of a spec gets its own thinking PR (design 1, section 6.3, rule 8) and the spec itself is committed untouched (rule 1). A second round followed on 2026-11-19: the first version of this revision was reviewed, and four more decisions were put to the Software Engineer, the two reason lines of D8, whether to record the first docs run (D9) and how the product glossary is produced (D5). Their answer was "All recommendations approved."

## 1. Intent and the why

The docs agent wrote the docs section from the finished tip of revision 2, reading the standard line by line against the code. It found places where the standard, the ADRs and the playbooks disagree with one another, and places where a call was never written down. A guess about how work is done is a call that belongs to the Software Engineer (design 1, section 13.1), so the docs agent put each one to them as a numbered decision. This revision records their answers, so that the standard, the playbooks, the ADRs and the docs agent follow one reading.

**Goals.** Record each decision with the options that were put, the pick and the reason, and say what it changes and in which files.

**Non-goals.** It changes none of design 1's goals, constraints or Appendix A decisions, and none of the decisions of revisions 1 and 2. It settles no gap that was not put as a decision, and section 4 lists what stays open.

**Anti-goal.** A reason that the Software Engineer did not give is never written as if they had given it. Where a reason is the agent's own proposal, the record says so.

## 2. The decisions

Each decision has the situation, the options that were put, the pick, the reason and what it changes.

### D1. ADR 0019 and the five indexes

**Situation.** ADR 0019 decides on four generated indexes. Revision 1 (D7) made the standard name five.

**Options.** (a) The regular agent writes a new ADR draft that records D7. (b) Treat revision 1 as the record.

**Pick.** (a). **Why.** A changed decision is a new draft (the stack's rule 8, `docs/agents/stacks.md`).

**Changes.** A new ADR draft, `docs/adr/draft-five-generated-indexes.md`. ADR 0019 is not edited.

### D2. Revision decisions that extend ADRs

**Situation.** Revision 1's D5 and D8 and revision 2's D11 extend ADRs 0011 (who records acceptance), 0025 (the update's code group moves `baseline_version`) and 0009 (the PR kinds of `baseline.yml` and of a stack folder's own `README.md` and `AGENTS.md`), and no draft records any of them. Revision 2's D5, extended, adds who records rejection and the small PR to the decision of ADR 0011, and the draft for ADR 0011 records it too (section 4).

**Options.** (a) A draft for each, for the same reason as D1. (b) Let the revisions stand as the record.

**Pick.** (a). **Why.** The same as D1: a change to a decision is a new draft.

**Changes.** Three new ADR drafts: `docs/adr/draft-adr-status-recording.md` (revision 1's D5 and revision 2's D5 extended), `docs/adr/draft-update-moves-baseline-version.md` (revision 1's D8) and `docs/adr/draft-pr-kinds-of-baseline-yml-and-folder-files.md` (revision 2's D11 on the PR kinds). Each records the options as its revision recorded them, and says "Not recorded" where the revision records nothing. Revision 2's other D11 answer, that neither `standards_enabled` record wins, gets no draft (section 4).

### D3. The file map's one line for a Markdown file

**Situation.** `standard/10-course-reference-pages.md` says that the file map takes the one line on each file from a one-line header comment in the file. No file of the standard has one, so the docs agent wrote each line of the file map by hand.

**Options.** (a) Amend `standard/10` so that a Markdown file's opening paragraph serves as its line, since every file already opens with one. (b) Add the comments in PRs 5 to 13.

**Pick.** (a). **Why.** Every file of the standard already opens with a paragraph that says what the file is for.

**Changes.** `standard/10-course-reference-pages.md`: a Markdown file needs no header comment and no sidecar entry, because its opening paragraph serves as its line. The standard leaves to the tooling how the line is cut from the paragraph, as it leaves the form of a sidecar entry (section 4).

### D4. An area that does not apply has no diagram

**Situation.** `standard/12-deployment-docs.md` requires five diagrams, and it also lets an area stay as one line, `Not applicable: why`. `standard/16-diagrams.md` already says that a section of an architecture file that stays as one line has no diagram.

**Options.** (a) Say in `standard/12` that an area which does not apply has no diagram. (b) Draw diagrams for areas that do not apply.

**Pick.** (a). **Why.** As `standard/16` already says of an architecture section.

**Changes.** `standard/12-deployment-docs.md` says that the diagram of an area that stays as one line is not drawn, and `standard/16-diagrams.md` says the same of an area of the deployment docs in the note under its table of minimums.

### D5. The product glossary

**Situation.** A lesson's header cannot mark a term as a product term or a technical one, so the standard's statement that both glossaries are assembled from the terms that lessons declare does not hold for the product glossary.

**Options.** (a) Keep what the docs agent did, a product glossary built from the terms that the feature pages use, each linked to the lesson or chapter that teaches it, and write it into the standard. (b) Add a key to the lesson header that marks the kind of a term.

**Pick.** (a). **Why.** The report gave no reason beyond the situation: nothing in a lesson's header tells a product term from a technical one.

**Settled on 2026-11-19.** The review of the first version of this revision found that the standard calls a glossary generated and never edited by hand, while the feature pages declare no terms or definitions, so no generator can find the product glossary's terms. The Software Engineer was asked how the product glossary is produced. (a) The docs agent writes it as a page. (b) The standard says how the tooling finds the terms and where the definitions come from. They picked (a) ("All recommendations approved."). **Why.** The feature pages declare no terms or definitions, so there is nothing for a generator to read.

**Changes.** `standard/10-course-reference-pages.md` says that the docs agent writes the product glossary from the terms that the feature pages use, and that the technical glossary is assembled from the lessons' terms. `standard/08-course-lessons.md` says that the lessons' `terms` feed the technical glossary only, where three sentences said that they feed the glossaries. `standard/06-feature-docs.md`, `standard/17-evidence-and-truth.md`, `standard/22-tooling-requirements.md`, `docs/agents/docs-agent.md` and `docs/agents/working-with-the-engineer.md` no longer count the product glossary among the generated indexes: their lists name the technical glossary.

### D6. An AGENTS.md for the standard's folder

**Situation.** `standard/` is a stack folder, and the standard says that each stack folder gets a short `AGENTS.md` (`standard/15-agents-md-and-playbooks.md`), but `standard/` has none.

**Options.** (a) Add a short one, in a thinking PR. (b) Exempt `standard/`.

**Pick.** (a). **Why.** The report gave no reason. The record notes that the standard itself says each stack folder gets a short `AGENTS.md` (the writer's call, section 4).

**Changes.** A new file, `standard/AGENTS.md`, with the commands and the layout of the folder, and the repo map of `AGENTS.md`, which said that no folder has an `AGENTS.md` yet.

### D7. The grouping of the code PRs

**Situation.** Six of the nine code PRs of the first stack, PRs 7 to 10, 12 and 13, are larger than the size guide of about 400 changed lines. Measured with `git diff --shortstat` between neighbouring branches, the nine slices of the standard's text are 398, 399, 599, 762, 737, 551, 309, 580 and 488 lines. No ruling records why the code was grouped that way.

**Options.** (a) Keep the grouping and record it as a ruling when the stack is published. (b) Re-cut the slices.

**Pick.** (a). **Why.** The report gave no reason for the recommendation.

**Changes.** No file of the repository. The ruling goes in the descriptions of the code PRs, which are written as files and applied when the stack is published. The plan (PR 2) laid out the grouping: it groups the standard's text into nine slices "of about 400 lines each". `docs/agents/stacks.md`, rule 6, expects the opposite, that the plan carries no layout and that the grouping is a ruling of the agent, so this build departs from the playbook, because its plan carried a layout. The ruling in the descriptions words the grouping as the agent's, following the plan's layout, says that it departs from rule 6, and records the Software Engineer's decision to keep it.

### D8. Two link conventions

**Situation.** Two conventions hold at the tip, and nothing writes them down or gives a reason. A file of the standard links only to files with a lower number and names the higher-numbered ones in backticks. The playbooks hold no Markdown link and name other files in backticks. Both come from the plan (PR 2), which states them as constraints of the build: "a file links only to files that already exist at its own commit, so links point backward in the stack; later files are named in backticks without a link", and of the playbooks that they "contain no links (files are named in backticks)". The plan gives no reason for the playbooks beyond "Playbooks are operational".

**Options.** (a) Write each as a rule with its reason. (b) Leave them unwritten.

**Pick.** (a). **Why.** The report recommended it on the condition that the Software Engineer wants the conventions kept, and their approval says that they do.

**Settled on 2026-11-19.** A standard is written only with the Software Engineer's approval (`AGENTS.md`, rule 7), and revision 2's D6 is the precedent for a reason line that the Software Engineer adopts after it is proposed to them. Both lines were proposed by the agent, with the recommendation first, and the Software Engineer approved them ("All recommendations approved."). Rule A: "Because every PR of a stack has to leave the repository working, and a link to a higher-numbered file would point at a file that only a later PR adds." Rule B: "Because the playbooks are replaced on update in every project, and a project does not hold some of the files they name, the baseline's own standard, so a link would break there while a name in backticks cannot." The plan gives no reason for rule B beyond "Playbooks are operational", so its reason is the agent's proposal, adopted by the Software Engineer.

**Changes.** Rule A is written in `standard/AGENTS.md`. Rule B is written in `standard/15-agents-md-and-playbooks.md`, among the rules for the files themselves, and in the repo map of `AGENTS.md`.

### D9. The first docs run

**Situation.** `docs/agents/docs-agent.md`, `standard/18-docs-agent.md` and `standard/22-tooling-requirements.md` say that how a fresh docs agent is started in practice, and where the "Rulings I made" list and the stack table are when the PRs are not open, is not yet confirmed. Revision 1 (D1) kept those sentences until the first docs run had been recorded. The run took place on 2026-11-18, and its report lists nine things that neither the playbook nor the two input files told the docs agent.

**Options.** (a) Replace the sentences, in this revision, with what the first run showed. (b) Do it later, after the stack is published.

**Pick.** (a). **Why.** The docs agent re-checks everything after this revision anyway, so the change costs one pass and not two. The Software Engineer approved it on 2026-11-19 ("All recommendations approved.").

**Changes.** `docs/agents/docs-agent.md` records the first run in "How you are started", in the sentence about the PR descriptions and in the report rule. `standard/18-docs-agent.md` says that the start text handed the docs agent the two files by path. `standard/22-tooling-requirements.md` says that the point was tried once.

## 3. What changes in the repository

The decisions land in three PRs on top of revision 2's, in the order that the rules of the stack ask for: a thinking PR with this revision, `standard/AGENTS.md`, `AGENTS.md` and two playbooks; a thinking PR with the four ADR drafts, directly beneath the code PR of this revision (call 2 in section 4 says why they are not lower); and a code PR with the standard's text.

| Decision | Thinking PR with the revision | Thinking PR with the ADR drafts | Code PR |
|---|---|---|---|
| D1 | none | `docs/adr/draft-five-generated-indexes.md` | none |
| D2 | none | `docs/adr/draft-adr-status-recording.md`, `docs/adr/draft-update-moves-baseline-version.md`, `docs/adr/draft-pr-kinds-of-baseline-yml-and-folder-files.md` | none |
| D3 | none | none | `standard/10-course-reference-pages.md` |
| D4 | none | none | `standard/12-deployment-docs.md`, `standard/16-diagrams.md` |
| D5 | `docs/agents/docs-agent.md`, `docs/agents/working-with-the-engineer.md` | none | `standard/10-course-reference-pages.md`, `standard/08-course-lessons.md`, `standard/06-feature-docs.md`, `standard/17-evidence-and-truth.md`, `standard/22-tooling-requirements.md` |
| D6 | `standard/AGENTS.md`, `AGENTS.md` | none | none |
| D7 | none | none | none |
| D8 | `standard/AGENTS.md` (rule A), `AGENTS.md` (rule B) | none | `standard/15-agents-md-and-playbooks.md` (rule B) |
| D9 | `docs/agents/docs-agent.md` | none | `standard/18-docs-agent.md`, `standard/22-tooling-requirements.md` |

## 4. Left open, and the writer's calls to confirm

**Confirmed since revision 2.** Revision 2's call 3, that `standard/README.md` stays as committed, keeps its form as the standard's index and is only checked by the docs agent, was put to the Software Engineer again in the closing message that followed revision 2. They answered "3. Yes commendation approved" on 2026-11-18, which this record reads as "yes, the recommendation is approved".

**Left open.**

- What an entry of the product glossary links to when no lesson or system chapter teaches the term (D5).
- Whether the reason of `docs/agents/stacks.md`, rule 6, that the plan carries no layout, should change, because the plan of this build carried one (D7).
- Where the small PR that records an ADR's rejection sits (revision 2).
- Whether revision 2's other D11 answer, that neither `standards_enabled` record wins, needs an ADR draft. D2 names the three drafts that the decision called for, and the answer extends no ADR that the decision named.
- Every other gap that the docs agent's report listed as a gap and not as a decision.

**The writer's calls, which the Software Engineer has not seen in this exact form.**

1. D1 and D2: that each draft records its options as its revision recorded them. Three of the four drafts have one real option and "do nothing", because that is all the revisions put, and each says so.
2. D1 and D2: that the drafts sit in their own thinking PR, directly beneath the code PR of this revision, although the decisions that three of them record were written into the standard by PRs 15 and 17, which are lower. Moving the drafts beneath those PRs would rewrite them.
3. D3: that the standard leaves to the tooling how the line is cut from the opening paragraph, because it leaves the form of a sidecar entry to the tooling in the same way. Also that the rule is stated for a Markdown file in general, although the approved reason is about the files of the standard, and that the standard leaves to the tooling what serves as the line of a file that does not open with a paragraph, such as a lesson, which opens with its header block, or an ADR, which opens with its status lines.
4. D4: that the deployment docs' diagram of an area that stays as one line is not drawn, whichever of the five it is, and that `standard/16` carries the same sentence in the note under its table.
5. D5: that `standard/08-course-lessons.md` changes too, because it states the same rule that `standard/10` states, and that `standard/06`, `standard/17`, `standard/22` and two playbooks change with it, because each counted the product glossary among the generated indexes. The reason written beside the product glossary rule is the situation plus the reason that the Software Engineer approved on 2026-11-19.
6. D6: what the file holds, and that the reason given for it is the standard's own sentence that each stack folder gets one. Its commands say that nothing in the folder is built or run, and its layout names the numbered files and the index.
7. D7: that the ruling words the grouping as the agent's, following the plan's layout, and says that this departs from `docs/agents/stacks.md`, rule 6, because the plan of this build carried a layout, which the docs agent could not confirm because it does not read the plan.
8. D2: that the draft for ADR 0011 also records revision 2's D5, extended (who records rejection, and the small PR), which the approved D2 did not name.
9. D8: that rule A is written in `standard/AGENTS.md`, as part of the folder's own instructions, as the approved recommendation said, although `standard/15` puts coding preferences in `docs/standards/`; and that rule B is written in `standard/15` and in the repo map of `AGENTS.md`. Rule A says "a numbered file", because the index and the `AGENTS.md` of the folder have no number and the index links all 22 files.
10. D9: that the record in `docs/agents/docs-agent.md` lists the first run's gaps in one compact sentence and marks the two that the standard now answers, and that the start text it names is the first run's as it was hardened to name the folder and the branch.
11. The numbering: the report's decisions 2 to 9 are D1 to D8 here, and the docs agent's four description PRs, now 18 to 21, are renumbered above this revision's PRs.
