# The Baseline Standard: revision 1 of design 1

**Revision** · 2026-11-18 · status: **decisions approved by the Software Engineer on 2026-11-18; the calls in section 5 are the writer's**

This revision records the decisions that the Software Engineer took on 2026-11-18, after the first stack of the baseline was built. The hand-off report of that build, which is kept outside the repository, put eleven decisions to them, each with a recommendation and its other options. Their answer was "Accept recommendations on all above". [Design 1, the standard](2026-11-14-baseline-standard-design.md) and [its decision trail](2026-11-14-baseline-decision-trail.md) stay exactly as they were written, because a revision of a spec gets its own thinking PR (design 1, section 6.3, rule 8) and the spec itself is committed untouched (rule 1). Where this revision and design 1 differ, this revision wins, and section 2 says where. Three of the decisions settle what design 1 and the standard had left open: when the PRs are published (D3), how the docs agent receives the lists (D1) and who records an ADR's acceptance (D5).

## 1. Intent and the why

Building the standard from design 1 meant guessing in some places: design 1 disagreed with itself, said nothing, or stated something that does not hold when it is tried. A guess about how work is done is a call that belongs to the Software Engineer (design 1, section 13.1), so each one was put to them as a numbered decision, with the recommendation first. This revision records their answers, so that the standard, the playbooks and the docs agent follow one reading and none of them has to guess.

**Goals.** Record each decision with the options that were put, the pick and the reason, and say what it changes and in which files.

**Non-goals.** It changes none of design 1's goals or constraints and none of the decisions in its Appendix A; where it differs from a rule in design 1's text, section 2 says so. It settles no gap that the hand-off report did not put as a decision, and section 5 lists what stays open.

**Anti-goal.** A reason that the Software Engineer did not give is never written as if they had given it. Where a rule has no stated reason, the standard says so.

## 2. The decisions

Each decision has the situation, the options that were put, the pick, the reason and what it changes.

### D1. How the docs agent receives the "Rulings I made" lists and the stack table

**Situation.** Design 1, section 10, has the docs agent read the "Rulings I made" lists and the stack table in the PR descriptions. PRs 3 and up are not open when the docs agent starts, so those descriptions do not exist.

**Options.** (a) Hand the docs agent the two as files, by path, in the instruction that starts it. (b) Open all the PRs with their descriptions before it starts, which needs the Software Engineer's yes and the descriptions written first. (c) Give it nothing and let it report what it lacked.

**Pick.** (a). **Why.** The PR descriptions do not exist yet, and the list is the exhaustive input that the deviations part of the docs section is built from.

**Changes.** No file (a writer's call, section 5). `docs/agents/docs-agent.md` and `standard/18-docs-agent.md` already say that how a fresh docs agent is started in practice, and where the lists and the table are when the PRs are not open, is not yet confirmed. The first docs run, started this way, is the check of design 1's claim V5 (section 17.2), so those sentences stay until that run has been recorded.

### D2. The folded history

**Situation.** The fixes of the build's final review were folded into the slices that introduced each file, by an autosquash rebase. The final tree is the same as before the fold.

**Options.** (a) Keep the folded history. (b) Rebuild the fixes as PRs on top of the stack, which is the baseline's convention for a cross-cutting fix.

**Pick.** (a). **Why.** The lower PRs then read as final text, so the Software Engineer does not review text that is known to be wrong.

**Changes.** No file.

### D3. When the PRs are published

**Situation.** Design 1 disagrees with itself. The picture in section 10 has the thinking and code PRs published before the docs agent starts, while the finish-menu seam in section 14 keeps the branch until the docs section is in and then publishes it. Section 6.3, rule 3, opens PRs 1 and 2 immediately, and rule 10 says that nothing publishes unless the Software Engineer asks.

**Options.** (a) Hold PRs 3 and up until the docs section is in, then publish the whole stack with the Software Engineer's yes. (b) Publish them before the docs agent starts.

**Pick.** (a). **Why.** The playbooks and the plan already work that way, and rule 10 says that nothing publishes unless the Software Engineer asks.

**Changes.** The seam in section 14 stands and the picture in section 10 does not. Rule 3, which opens PRs 1 and 2 immediately, is qualified: where the project's `AGENTS.md` or the conversation asks for the Software Engineer's yes before anything is opened, they are opened once the Software Engineer has said yes. In this repository `AGENTS.md`, rule 4, now says that opening a stack's PRs is publishing, so it waits for the Software Engineer's yes, PRs 1 and 2 included. The qualification is written in `docs/agents/stacks.md` (rule 3 and the paragraph that opens PRs 1 and 2), in `docs/agents/docs-agent.md` and in `standard/03-stack-model.md` (rule 3), so that `AGENTS.md`, the playbooks and the standard agree. The calls in this paragraph are the writer's (section 5).

### D4. The gated steps, and their order

**Situation.** Three steps of the plan wait for the Software Engineer's yes: a sandbox in which to try the stack flow (Task 5), opening PRs 1 and 2 (Task 6) and publishing the whole stack (Task 25).

**Options.** (a) The sandbox first, then push `main` and open PRs 1 and 2, so that the Software Engineer can read the spec and the plan while the docs agent works, and publish the whole stack only after the docs section is in. (b) Skip the sandbox and publish directly, leaving the behaviour that the sandbox would show unconfirmed.

**Pick.** (a). **Why.** The standard and the playbooks stated two points as not yet confirmed, that branches cut as pointers link with `gh stack link` and how the pending-on-lower-PRs gate behaves, and the sandbox was to prove them before the stack relies on them.

**Done.** The sandbox, the push of `main` and PRs 1 and 2 were done on 2026-11-18, and section 3 gives what they showed. The sandbox proved that pointer branches link. It also showed what `gh stack view` displays, which the playbooks had likewise left unconfirmed. It did not prove the pending-on-lower-PRs gate (section 3). Publishing the whole stack waits for the docs section and for a fresh yes (D3).

**Changes.** The sentences that called pointer linking and `gh stack view` not yet confirmed now say what was checked: `docs/agents/stacks.md`, `docs/agents/docs-agent.md`, `standard/03-stack-model.md`, `standard/21-skills-seams.md` and `standard/22-tooling-requirements.md`. What was not checked stays unconfirmed (section 3).

### D5. Who records an ADR's acceptance

**Situation.** The Software Engineer's merge of the stack is the acceptance of its ADRs (design 1, section 11.2). The status in the file is text, though, and design 1 names no one who changes it from Proposed to Accepted after the merge, while the "valid status" check of section 15.3 needs someone to make that edit.

**Options.** (a) The Software Engineer, or an agent at their ask, right after the merge. (b) The next docs agent run records it. (c) The tooling does.

**Pick.** (a). **Why.** Acceptance is the Software Engineer's call, and design 1 names no one else.

**Changes.** `docs/agents/adrs.md` and `standard/11-adrs.md` say it, for the status Accepted. Section 5 lists what they leave open.

### D6. The reasons that design 1 does not give

**Situation.** Design 1 states no reason for these rules: two rows of the Software Engineer's decision list (anything that changes how work is done; anything that persists or ships and cannot be undone), the numbered decision form, the exact command or click path, why a report opens with what the Software Engineer has to do, the date and source of a rule and the opt-in to standards, two of the diagram quality rules (the caption and the glossary labels), most parts of the code-PR description (Why, What changes, How to review, Risks and rollout, Ideas introduced, Out of scope and follow-ups) and the checkable outcome of a lab. The standard states these rules without a reason instead of inventing one.

**Options.** (a) The Software Engineer gives their own one line for each of the two rows of their decision list, and every other rule stays as stated. (b) All stay as stated.

**Pick.** (a). **Why.** The two rows are the most visible of the rules that have no reason.

**Status.** Open: the two lines are not given yet. Until they are, the two rows say "No reason is stated for this call."

**Changes.** None yet.

### D7. The generated indexes

**Situation.** Design 1, section 9.6, rule 9, names "the course index, the file map, the glossaries and the ADR index" as generated and never hand-edited. It never defines the course index, and its tree shows none. The rule also leaves out the index of the architecture reference, which the tree marks as generated.

**Options.** (a) Define the course index as the index of the guided course, and add the architecture reference's index to the rule, so that the files agree. (b) Leave the standard as it is.

**Pick.** (a). **Why.** So that the files agree.

**Changes.** The rule names five indexes: the course index, the architecture reference's index, the file map, the glossaries and the ADR index. The course index is the generated `README.md` of `docs/course/`, the same place as the indexes of `docs/architecture/` and `docs/adr/`. The standard sets no shape for it beyond that it is generated, because the generators are for design 3 to specify. Where no generator exists yet, the docs agent writes the architecture reference's index in the reference PR, with the architecture reference. These three points are the writer's calls (section 5). Files: `docs/agents/docs-agent.md`, `docs/agents/working-with-the-engineer.md`, `standard/05-project-layout.md`, `standard/10-course-reference-pages.md`, `standard/17-evidence-and-truth.md` and `standard/20-working-rules.md`.

### D8. Updates and project-owned files

**Situation.** Design 1 says that an update never touches project-owned files (section 15.2), and it lists the reader profile, the standards, the ADRs and all the documents as project-owned. It does not list `baseline.yml` as baseline-owned, and the standard counts it among the project-owned files, as the project's own configuration. Design 1 also says that the update opens a stack whose third PR onwards are description PRs, for existing documents that the new standard makes non-compliant (section 15.5). It does not say who moves `baseline_version`.

**Options.** (a) The update's code group moves `baseline_version`, and the description PRs are the docs agent's own change to the project's documents, reviewed like any other. (b) Leave it open until the tooling is designed.

**Pick.** (a). **Why.** It keeps "never touches" true of the update itself: what the update replaces is only baseline-owned, and the project's own files change only in PRs that the Software Engineer reviews like any other.

**Changes.** `standard/05-project-layout.md` and `standard/22-tooling-requirements.md` say it. The group that holds the workflow and the checker pins also holds the new `baseline_version`.

### D9. Mind maps and the palette

**Situation.** Design 1, section 9.1, lists mind maps among the diagram types that Mermaid covers. A reviewer of the build found that Mermaid's mind maps were not legible in both themes with the pinned renderer, mermaid-cli 12.2.0, so the capability map of the standard had to be a flowchart. The approved palette's tinted rows measure 3.6 to 4.4:1 contrast in dark, below the 4.5:1 that WCAG AA asks of normal text, though they read well.

**Options.** (a) Drop mind maps from the list, and let the tooling confirm the palette's final values, as design 1 already says (section 17.1). (b) Keep both as they are.

**Pick.** (a). **Why.** A reviewer measured Mermaid's mind maps as not legible in both themes with the pinned renderer, and the palette's final values were always the tooling's to confirm, as design 1 already says.

**Changes.** `standard/16-diagrams.md` no longer lists mind maps. The palette stays as approved.

### D10. The process rule in the reader profile

**Situation.** `docs/reader-profile.md`, in the bootstrap commit on `main`, says to "update the reading of it in 'What this file is' in the same PR". The rule is in neither design 1 nor the brief that produced the bootstrap.

**Options.** (a) Drop it in a later thinking PR, and do not rewrite `main`. (b) Keep it.

**Pick.** (a). **Why.** It is harmless until then, and `main` is not rewritten for it.

**Changes.** The thinking PR of this revision removes the clause from `docs/reader-profile.md`.

### D11. The smaller gaps

**Situation.** The hand-off report named four smaller gaps and said that the Software Engineer could accept the option that it would take.

**Pick.** This revision settles the two for which the report stated an option or the standard already holds one, and leaves the other two open, because the report stated no option for them (section 5).

- **Fenced ASCII (settled).** Design 1, section 9.1, has the source and the re-render rule for the other text-based tools. Fenced ASCII is text already, so it has no separate source and no rendered image, and the re-render and the two-variant rules do not apply to it. `standard/16-diagrams.md` says so.
- **"A real file, module or class", or "any real path" (settled, no change).** This follows from the standard's text, not from an option in the report: the standard's diagram check already names both, so it covers a file, a module and a class as well as a path (`standard/22-tooling-requirements.md`).
- **The PR kind of a change to `baseline.yml`, or to a stack folder's own `README.md` or `AGENTS.md` (open).** Design 1 gives none.
- **`standards_enabled` (open).** It is recorded in `baseline.yml` and in the header of the reader profile, and design 1 does not say which wins.

## 3. Facts checked after the build

Checked on 2026-11-18 with `gh` 2.103.3 and the `gh stack` extension 0.3.0. `gh stack link` creates a stack on GitHub from branch names, and `gh stack view` shows a stack.

| Fact | How it was checked |
|---|---|
| `gh stack link` links branches cut as pointers into one linear history. | In a throwaway private repository, three commits on one branch and one `git branch` pointer at each commit: `gh stack link` with the three pointers and `--open` pushed them in one atomic push, created three PRs whose bases were `main` and the two pointers below, and created one GitHub stack. No PR was a draft, and each was clean and mergeable. The same command then did the same for PRs 1 and 2 of this repository. |
| What `gh stack view` shows for a stack made with `gh stack link`. | Right after the link, run on the branch that the commits were made on, which is not one of the stack's branches, it said that the branch is not part of a stack. After `gh stack checkout <the stack's number>` imported the stack, it listed the three branches with their PRs, the top first, and its JSON output gave each branch's head, its base (the head of the branch below) and `needsRebase` as false. After `gh stack unstack --local` removed the local tracking of the stack, and the PRs stayed open, it said that the current branch is not part of a stack on each of the stack's own branches too. The check of `gh stack view` was made in the throwaway repository only. |

**Not checked.** GitHub's behaviour for required checks on every PR of a stack, for the pending-on-lower-PRs gate and for merging bottom-up (design 1, section 17.2, V1). Checking them needs the stack gate of design 3 or a merge, and nothing was merged. The help of `gh stack merge` says that it merges the stack up to the chosen PR in one all-or-nothing operation, and that GitHub evaluates branch protection and repository rules when the merge runs. The sandbox repository was left in place, and its deletion waits for the Software Engineer's yes.

## 4. What changes in the repository

The decisions land in two PRs on top of the first stack's code, as the rules of the stack ask for a cross-cutting change: a thinking PR with the revision, the playbooks, `AGENTS.md` and `docs/reader-profile.md`, and a code PR with the standard's text, so that each kind is reviewed on its own.

| Decision | Thinking PR | Code PR |
|---|---|---|
| D3 | `AGENTS.md`, `docs/agents/stacks.md`, `docs/agents/docs-agent.md` | `standard/03-stack-model.md` |
| D4 | `docs/agents/stacks.md`, `docs/agents/docs-agent.md` | `standard/03-stack-model.md`, `21-skills-seams.md`, `22-tooling-requirements.md` |
| D5 | `docs/agents/adrs.md` | `standard/11-adrs.md` |
| D7 | `docs/agents/docs-agent.md`, `docs/agents/working-with-the-engineer.md` | `standard/05-project-layout.md`, `10-course-reference-pages.md`, `17-evidence-and-truth.md`, `20-working-rules.md` |
| D8 | none | `standard/05-project-layout.md`, `22-tooling-requirements.md` |
| D9 | none | `standard/16-diagrams.md` |
| D10 | `docs/reader-profile.md` | none |
| D11 | none | `standard/16-diagrams.md` |
| D1, D2, D6 | none | none |

## 5. Left open, and the writer's calls to confirm

**Left open.**

- The two lines of D6, one for each of the two rows of the decision list.
- The PR kind of a change to `baseline.yml` or to a stack folder's own `README.md` or `AGENTS.md`, and which of the two records of `standards_enabled` wins (D11). The hand-off report named these as gaps without an option, so each is put to the Software Engineer again with an option. D8 puts the move of `baseline_version` in the update's code group, which gives one change to `baseline.yml` a PR kind, and the open question takes that into account.
- Who records the status Rejected after a send-back, and which PR or commit carries the status edit after the merge. D5 answered only who records Accepted.
- Every other gap that the hand-off report listed as a gap and not as a decision.

**The writer's calls, which the Software Engineer has not seen in this exact form.**

1. That this revision wins where it differs from design 1.
2. D1: that no file changes, so that the hedges in `docs/agents/docs-agent.md` and `standard/18-docs-agent.md` stay until the first docs run has been recorded.
3. D3: that `AGENTS.md` makes PRs 1 and 2 wait for the Software Engineer's yes as well, which the plan already did, and the sentences that qualify rule 3 in `docs/agents/stacks.md`, `docs/agents/docs-agent.md` and `standard/03-stack-model.md`.
4. D7: the path of the course index, `docs/course/README.md`; that the standard sets no shape for it beyond "generated"; and that the docs agent writes the architecture reference's index in the reference PR, which follows from the PR order in `docs/agents/docs-agent.md`.
5. D8: the wording that reconciles "never touches" with the update's stack. The update itself never touches a project-owned file, and its stack carries two changes to project-owned things, each in a PR that the Software Engineer reviews.
6. The wording of the facts in section 3 where the playbooks and the standard now state them.
7. D11: that "a real file, module or class" against "any real path" needs no change, because the standard's diagram check already names both.
