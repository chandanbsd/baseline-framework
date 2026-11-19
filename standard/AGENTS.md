# Standard: instructions for working in this folder

This file holds the instructions for working in `standard/`, the folder that holds the baseline's standard as plain Markdown: its commands and its layout. The `AGENTS.md` at the root of the repository is the primary instruction for working here, and if the Software Engineer says something different in the conversation, the conversation wins for that task.

## Commands

None. The folder holds text only, so nothing in it is built, run or tested. The checks that the standard requires of a project's tooling are listed in `22-tooling-requirements.md`, and the baseline's own tooling does not exist yet.

## Layout

- `01-why-and-scope.md` to `22-tooling-requirements.md` are the 22 files of the standard, numbered in reading order. Each opens with a paragraph that says what the file covers.
- `README.md` is the index of the standard. It is a description path, so the docs agent checks it against the tip and does not rewrite it, and a change to it goes in a description PR (`AGENTS.md` at the root gives the reason).
- `AGENTS.md` is this file. A stack folder's own `AGENTS.md` is a thinking path, so a change to it goes in a thinking PR (`AGENTS.md` at the root gives the reason).

## Links

**Let a numbered file link only to files with a lower number, and name a higher-numbered file in backticks.** Because: every PR of a stack has to leave the repository working, and a link to a higher-numbered file would point at a file that only a later PR adds.
