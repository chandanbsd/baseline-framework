# The Baseline Standard: revision 2 of design 1

**Revision** · 2026-11-18 · status: **decisions approved by the Software Engineer on 2026-11-18; the calls in section 4 are the writer's**

This revision records the Software Engineer's answers to the items that [revision 1](2026-11-18-baseline-standard-revision-1-design.md) left open in its section 5. After revision 1 was committed, each of them was put to the Software Engineer again as a numbered decision, with a recommendation first and its other options. There were six decisions in that message, and their answer was "All recommendations approved". Two of the six, starting the docs agent and deleting the sandbox repository, change no file in this repository. The other four are recorded here. [Design 1, the standard](2026-11-14-baseline-standard-design.md), [its decision trail](2026-11-14-baseline-decision-trail.md) and revision 1 stay exactly as they were written, because a revision of a spec gets its own thinking PR (design 1, section 6.3, rule 8) and the spec itself is committed untouched (rule 1). Where this revision and revision 1 differ, this revision wins, and section 2 says where.

## 1. Intent and the why

Revision 1 left four things open on purpose: the two reasons that the Software Engineer had not given, two gaps for which the hand-off report stated no option, and who records an ADR's rejection. Until they were answered, the standard and the playbooks said "No reason is stated for this call." in two rows, and said nothing about the PR kind of three paths or about which record of `standards_enabled` wins. A guess about how work is done is a call that belongs to the Software Engineer (design 1, section 13.1), so each of the four was put to them. This revision records their answers, so that the standard, the playbooks and the docs agent follow one reading.

**Goals.** Record each answer with the options that were put, the pick and the reason, and say what it changes and in which files.

**Non-goals.** It changes none of design 1's goals, constraints or Appendix A decisions, and none of the decisions of revision 1 except where section 2 says so. It settles no gap that was not put as a decision, and section 4 lists what stays open.

**Anti-goal.** A reason that the Software Engineer did not give is never written as if they had given it. Where the Software Engineer adopted a proposed line, the record says that it was proposed.

## 2. The decisions

Each decision has the situation, the options that were put, the pick, the reason and what it changes.

### D6, closed: the two reason lines

**Situation.** Revision 1's D6 left two rows of the Software Engineer's decision list, anything that changes how work is done and anything that persists or ships and cannot be undone, saying "No reason is stated for this call." until the Software Engineer gave a line for each.

**Options.** (a) The Software Engineer adopts as their own the two lines that were proposed to them. (b) They give their own words.

**Pick.** (a). **Why.** The lines were put with the recommendation and no further reason, and the Software Engineer approved them. They were proposed by the agent that put the decision, and they are the Software Engineer's reasons from 2026-11-18.

**Changes.** The row for anything that changes how work is done now says "The baseline cannot know what suits a project's kind and goals." The row for anything that persists or ships and cannot be undone now says "A wrong call cannot be taken back, and its cost falls outside the repository." The two sentences of the standard that said that only some rows of the table have a reason now say that every row has one. Files: `docs/agents/working-with-the-engineer.md` and `standard/20-working-rules.md`.

### D11, closed: the PR kinds of `baseline.yml` and of a stack folder's `README.md` and `AGENTS.md`

**Situation.** Design 1 gives no PR kind for a change to `baseline.yml` or to a stack folder's own `README.md` or `AGENTS.md`. The kind of a PR is inferred from the paths it touches, and `stack_folders` lists the folders whose changes are code. By that rule alone a stack folder's `README.md` would be code, although the standard counts it among the descriptive documents, which only the docs agent writes, and counts a stack folder's `AGENTS.md` among the prescriptive documents. Revision 1 (D8) put the move of `baseline_version` in the update's code group, which gave one change to `baseline.yml` a kind.

**Options.** (a) `baseline.yml` is code. A stack folder's own `README.md` is a description path and its own `AGENTS.md` is a thinking path. Every other path in a stack folder is code. (b) Leave the kinds to the checker's defaults, which are for the tooling's design to settle.

**Pick.** (a). **Why.** For `baseline.yml`, the update's code group moves its `baseline_version`. For the two files of a stack folder, the recommendation gave no reason, and the files give the one that is already in the standard: a stack folder's `README.md` is a descriptive document and its `AGENTS.md` is a prescriptive one (the writer's call, section 4).

**Changes.** The three kinds are stated in `docs/agents/stacks.md`, in `standard/03-stack-model.md` (a rule and the diagram of "How the kind is decided") and in `standard/05-project-layout.md` (the `stack_folders` row, the sentence about `baseline.yml` and the comment above `stack_folders` in the example). The comment above `stack_folders` in this repository's own `baseline.yml` carries the same wording as the example. The repo map of `AGENTS.md` says that `standard/README.md` is the one path of `standard/` that is not code, and that it keeps its form as the standard's index.

### D11, closed: which record of `standards_enabled` wins

**Situation.** `standards_enabled` is recorded in `baseline.yml` and in the header of the reader profile, and design 1 does not say which wins.

**Options.** (a) Neither wins: both record the one answer of the intake, and how a difference between them is reported is for the tooling's design to settle. (b) The header of the reader profile wins. (c) `baseline.yml` wins.

**Pick.** (a). **Why.** Both records are the intake's one answer.

**Changes.** The standard says that neither record wins, with the reason that both record the intake's one answer, and that how a difference is reported is for the tooling's design, in `standard/04-reader-profile.md`, `standard/05-project-layout.md` and `standard/19-standards-mechanism.md`. The playbook `docs/agents/standards.md` says that neither record wins, with the same reason.

### D5, extended: who records Rejected, and which PR carries a status edit

**Situation.** Revision 1's D5 answered only who records Accepted after the merge. It left open who records Rejected after a send-back, and which PR or commit carries the status edit.

**Options.** (a) The same people as for Accepted, the Software Engineer or an agent at their ask, and the edit goes in a small PR, like any other change. (b) The same people, and the edit is a direct commit.

**Pick.** (a). **Why.** The people are those who accept an ADR, because accepting and rejecting are both the Software Engineer's call, and a status edit is a change like any other.

**Changes.** `docs/agents/adrs.md` and `standard/11-adrs.md` say it for both statuses, in the rule that D5 added. Section 4 lists what they leave open.

## 3. What changes in the repository

The decisions land in two more PRs on top of revision 1's, as the rules of the stack ask for a cross-cutting change: a thinking PR with this revision, `AGENTS.md` and the playbooks, and a code PR with the standard's text and `baseline.yml`, which is code under the PR-kind decision above.

| Decision | Thinking PR | Code PR |
|---|---|---|
| D6, closed | `docs/agents/working-with-the-engineer.md` | `standard/20-working-rules.md` |
| D11, the PR kinds | `AGENTS.md`, `docs/agents/stacks.md` | `standard/03-stack-model.md`, `05-project-layout.md`, `baseline.yml` |
| D11, `standards_enabled` | `docs/agents/standards.md` | `standard/04-reader-profile.md`, `05-project-layout.md`, `19-standards-mechanism.md` |
| D5, extended | `docs/agents/adrs.md` | `standard/11-adrs.md` |

## 4. Left open, and the writer's calls to confirm

**Left open.**

- Where the small PR that records an ADR's rejection sits. An ADR that was sent back is still in a stack that has not merged, and the answer says only that the edit goes in a small PR like any other change, so the standard states no timing and no base for that PR.
- Every other gap that the hand-off report listed as a gap and not as a decision.

Nothing else that section 5 of revision 1 listed as open stays open.

**The writer's calls, which the Software Engineer has not seen in this exact form.**

1. That this revision wins where it differs from revision 1.
2. D11, the PR kinds: the reason written beside the two files of a stack folder, which comes from the standard's own lists of descriptive and prescriptive documents and not from the Software Engineer.
3. D11, the PR kinds: that the rule applies to this repository's own stack folder, `standard/`, as to any other. `standard/README.md`, the standard's index, was committed in a code PR before the rule existed, and it stays as committed. A change to it from now on goes in a description PR. The standard gives a stack folder's README the run, test and build structure of the root README (`standard/13-project-readme.md`), which the standard's index does not have, so the index keeps its form as the standard's index, and the docs agent only checks it against the tip instead of writing it again. `AGENTS.md` says both.
4. D11, the PR kinds: that the comment above `stack_folders`, in the standard's example and in `baseline.yml`, now names the two exceptions.
5. D11, `standards_enabled`: that the standard adds no check for a difference between the two records to its list of mechanical checks, because how a difference is reported is for the tooling's design to settle.
6. D5: that the files put the Rejected edit after the send-back, and not after a merge, and say nothing of where its PR sits (left open, above); and that they do not state the kind of the PR that carries a status edit. Its kind follows its paths like any other, and an ADR is a prescriptive document, so it is a thinking PR.
7. D6: that the two sentences of the standard that spoke of the rows "that have a reason" were rewritten to say that every row has one, because after this revision every row does.
