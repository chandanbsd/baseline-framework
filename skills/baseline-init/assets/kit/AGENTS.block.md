## Baseline

This repository follows the baseline. Two documents steer agent-written code: ADRs in `docs/adr/` and coding standards in `docs/standards/`. Read both before you generate code.

- **Before coding.** When the questions are done and you would wait for the engineer's approval to start, run the `baseline-desired-state` skill first, then wait for approval.
- **Decisions.** When a decision or a repeatable rule comes up, write it yourself, in the same session: an ADR or a standard, from the `TEMPLATE.md` in its folder, in the decisions PR.
- **Documentation.** When the engineer says the work is finished, run `baseline-documentation` in a fresh session or subagent.
- **Refactor.** Run `baseline-refactor` only when the engineer asks.
- Do not edit this block. `baseline-init` replaces it on update.
