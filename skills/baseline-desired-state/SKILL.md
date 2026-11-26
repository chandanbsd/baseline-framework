---
name: baseline-desired-state
description: Summarise the conversation as a short desired-state document with diagrams before any code is written, then record the ADRs and coding standards the conversation settled. Use at the end of the questions, when you would otherwise wait for the engineer's approval to start coding, and whenever a decision or repeatable rule comes up later.
metadata:
  version: "0.2.0"
---

# baseline-desired-state

Paths are relative to this skill's folder.

## When

The questions are done and you would now wait for the engineer's approval to start coding. Do this first, then wait.

## 1. Write the desired state

Write `docs/desired-state/<YYYY-MM-DD>-<topic>.md` in the repo from `assets/desired-state-template.md`.

- Condensed: diagrams and snippets first, little prose. The engineer reads it in two minutes.
- It is engineer-only. It replaces nothing a skill already wrote (a spec, a plan), and it is never maintained: it may go stale.
- Under "Decisions to record", list each ADR or standard this conversation already settled. Use `references/deciding-adrs-and-standards.md` to decide. Write `None` when there are none.

## 2. Open it for review

Put the file on its own branch and open a PR if the repo has a GitHub remote and `gh` works. Otherwise commit it on a branch and say so. Tell the engineer to read it, then wait for their approval. If they ask for changes, change the file and wait again.

## 3. After approval: the decisions PR

Write each ADR and standard you listed yourself, in this session, from the `TEMPLATE.md` in `docs/adr/` or `docs/standards/`. Put them in the next PR above the desired-state PR: the decisions PR. The engineer reviews it. Then implement.

## 4. Implement

Nothing else from the baseline applies. Stack the code however reads best: when to open PRs, how to cut slices, frontend before backend before database. The ADRs and standards are context, and the code must meet them.

## 5. Later decisions

A decision or repeatable rule that comes up during or after coding goes into the decisions PR. Add or amend the file there, rebase the code PRs above it, and tell the engineer what changed.
