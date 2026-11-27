<!-- baseline version=0.2.0 sha256=bfdbf388ab9b216f8c31e83e4b449830d07700b2a570a6b61a07b0341d64f77b -->
# Baseline

This repository follows the baseline. This file is replaced whole when the baseline is updated, so do not edit it. `baseline/baseline.yml` is the project's.

- **Steering.** ADRs in `baseline/adr/` and coding standards in `baseline/standards/` steer agent-written code. Read both before you generate code.
- **New work.** When the engineer describes new work and you have questions, run the `baseline-brainstorm` skill.
- **Decisions.** When a decision or a repeatable rule comes up, write it yourself: an ADR or a standard, from the `TEMPLATE.md` in its folder, in the decisions PR.
- **The contract.** An accepted file in `baseline/desired-state/` is the contract for the work. Re-read it after a compaction.
- **Documentation.** The engineer accepts the code first. Then run the `baseline-documentation` skill in a fresh session or subagent.
- **Refactor.** Run the `baseline-refactor` skill only when the engineer asks.
- **The check.** CI runs `python3 baseline/check.py` through `.github/workflows/baseline.yml`. Run it yourself before a PR that touches `baseline/`. It renders Mermaid when `mmdc` is installed.
