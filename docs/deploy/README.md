# Deployment docs

This folder says how the baseline runs in the real world. The baseline runs nothing: it is a repository of text, hosted on GitHub and read there, and nothing is deployed. The repository itself is the artifact, and merging a stack into its `main` branch on GitHub is how finished work reaches its readers.

The folder has one file for each of the eleven areas that [standard/12-deployment-docs.md](../../standard/12-deployment-docs.md) sets. An area that does not apply is one line that says why.

| # | Area | What it says here |
|---|---|---|
| 1 | [Topology](01-topology.md) | The repository on GitHub and the local repository where the agents work. |
| 2 | [Environments](02-environments.md) | The local repository and GitHub; there is no CI, staging or production. |
| 3 | [Infrastructure as code](03-infrastructure-as-code.md) | Not applicable. |
| 4 | [Configuration and secrets](04-configuration-and-secrets.md) | The keys of `baseline.yml` and of the reader profile's header; no secrets. |
| 5 | [Build and release pipeline](05-build-and-release-pipeline.md) | No build and no release: a stack merged into `main` is what readers read. |
| 6 | [Deploying](06-deploying.md) | Publishing the stack on GitHub and merging it, the Software Engineer's steps. |
| 7 | [Rollback and recovery](07-rollback-and-recovery.md) | Not applicable. |
| 8 | [Operations](08-operations.md) | Not applicable. |
| 9 | [Security and hardening](09-security-and-hardening.md) | A private repository; who has access was not checked. |
| 10 | [Cost](10-cost.md) | No running cost; the GitHub plan was not checked. |
| 11 | [Troubleshooting](11-troubleshooting.md) | What a reader or an agent may meet while the stack is half published. |

Of the five diagrams that the standard asks of these documents, three are here: the topology, the pipeline and the deploy sequence. The rollback flow and the backup and restore flow belong to area 7, which does not apply, so they are not drawn: an area that stays as one line has no diagram ([standard/12-deployment-docs.md](../../standard/12-deployment-docs.md)).

Every command whose output is shown was run in the local repository on 2026-11-18, and run again on 2026-11-19, after the docs section was rebased onto revision 3. Publishing and merging were not run, because both are the Software Engineer's to do, so the steps that do them are marked "not verified".
