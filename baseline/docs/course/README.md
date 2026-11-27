# Course
covers: the course index, one chapter per outcome the baseline delivers

Each chapter follows one outcome from the command or request that starts it to the result, and deepens a flow in [the architecture overview](../architecture/README.md#key-flows). Run the practice commands from the repository root.

## Chapters

1. [Set up a repository](01-set-up-a-repository.md): `init.py` writes the `baseline/` folder, the workflow and the pointer, after a dry run the engineer approves.
2. [Update a repository](02-update-a-repository.md): `update.py` moves a project to the installed version through migrations, then replaces the files the baseline owns; `bump_version.py` sets that version.
3. [Check the baseline folder](03-check-the-baseline-folder.md): `check.py` and the workflow that runs it on every pull request.
4. [Agree the end state before code](04-agree-the-end-state-before-code.md): the questions protocol and `next_number.py` that end in an accepted desired-state file.
5. [Document the accepted code](05-document-the-accepted-code.md): a fresh agent writes `baseline/docs/` and `baseline/flags/` from the code.
