# Baseline Skills Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the smallest working path of the thin baseline: a four-skill Agent Skills package that installs into a repo, initialises it, updates it through migration scripts, and runs the desired-state step.

**Architecture:** `skills/` holds four skills (two real, two stubs). `baseline-init` carries the kit and two stdlib-only Python scripts (`init.py`, `update.py`) that share one module (`kit.py`). Everything deterministic is tested with `unittest` through the scripts' command lines, the way an agent runs them. The install and agent-behaviour claims are proved by hand in a throwaway repo (Tasks 6 and 7).

**Tech Stack:** Markdown skills (Agent Skills format), Python 3.9+ standard library only, `unittest`, the `skills` npm CLI (install proof only).

**Spec:** `docs/superpowers/specs/2026-11-25-baseline-thin-skills-design.md` (sections 5, 6, 9)

## Global Constraints

- Scripts: Python 3.9+, standard library only, non-interactive, `--help`, and `--dry-run` wherever files change. Use `from __future__ import annotations` and `typing.Optional`; no `X | Y` at runtime.
- SKILL.md: under 500 lines; `name` 1–64 chars, lowercase letters, digits and single hyphens, no leading or trailing hyphen, equal to its folder name; `description` 1–1,024 chars on one line; `references/` one level deep.
- The four skill names, exactly: `baseline-desired-state`, `baseline-documentation`, `baseline-refactor`, `baseline-init`.
- All four carry `metadata.version: "0.2.0"`.
- Skills share nothing: no file in one skill's folder reads another skill's folder (no `../` literal, no `skills/baseline-` path).
- Do not touch this repo's `standard/`, `docs/agents/`, `docs/adr/`, `AGENTS.md`, `CLAUDE.md` or `baseline.yml` (that is the last project, not this plan).
- Commit messages carry no co-author trailer and no "generated with" line (`AGENTS.md` rule 5). Nothing is pushed, merged or published.
- Run all tests with: `python3 -m unittest discover -s tests -p '*_test.py' -v`

## Review Focus

1. `init.py` on a repo whose `AGENTS.md` already holds other content: that content stays byte-for-byte (Task 3).
2. `init.py` on an already-initialised repo: refuses, changes nothing (Task 3).
3. A repo whose `baseline_version` is newer than the installed skills: `update.py` refuses (Task 4).
4. A migration that fails midway: the version does not advance (Task 4).
5. A local edit inside the `AGENTS.md` block: `finish` refuses to overwrite it without `--discard-edits` (Task 4).

## Decisions this plan makes where the spec was silent

- `baseline-documentation` and `baseline-refactor` are stubs, so the four-skill install is real. The intake, the check script and the CI workflow are not in the skeleton.
- The spec says `baseline_version` moves last. Here it moves after each applied migration, so a declined migration leaves the repo at the last applied version, and `finish` moves it to the installed version.
- Local-edit detection: the block's begin marker records the SHA-256 of its body.
- `update.py` takes `--installed-version` and `--migrations-dir` so tests can use fixtures.
- Desired-state files go in `docs/desired-state/<YYYY-MM-DD>-<topic>.md`.
- The skeleton's `finish` refreshes the `AGENTS.md` block only; the two templates are created by init and not refreshed yet.
- "Keep a local edit as an override" is not built: `finish` either replaces the block (`--discard-edits`) or refuses. If the engineer wants to keep an edit, `finish` is not run. Overrides are designed with the content phase.

---

### Task 1: Package skeleton and spec-lint test

**Files:**
- Create: `skills/baseline-init/SKILL.md`, `skills/baseline-desired-state/SKILL.md`, `skills/baseline-documentation/SKILL.md`, `skills/baseline-refactor/SKILL.md`
- Create: `tests/helpers.py`, `tests/skill_spec_test.py`

**Interfaces:**
- Produces (`tests/helpers.py`):
  - `ROOT: Path` (repo root), `skill_dir(name: str) -> Path`
  - `read_skill(name: str) -> Skill`, where `Skill` is a dataclass with `name, description, compatibility, version: str`, `body: str`, `dir: Path`. The parser reads the frontmatter between the first two `---` lines: `key: value` lines (quotes stripped) and one indented `metadata:` map.
  - `run(script: Path, *args: str, cwd: Optional[Path] = None) -> subprocess.CompletedProcess` (runs `sys.executable`, captures text output, never raises)
  - `snapshot(root: Path) -> Dict[str, bytes]` (every file under `root`, keyed by relative path, for before/after comparisons)

- [ ] **Step 1: Write the failing tests** in `tests/skill_spec_test.py` (class `SkillSpecTest`):

```python
NAMES = {"baseline-desired-state", "baseline-documentation", "baseline-refactor", "baseline-init"}

def test_exactly_four_skills(self):
    self.assertEqual({p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}, NAMES)

def test_name_and_description_rules(self):   # for each skill
    self.assertRegex(s.name, r"^[a-z0-9]+(-[a-z0-9]+)*$"); self.assertLessEqual(len(s.name), 64)
    self.assertEqual(s.name, s.dir.name); self.assertTrue(1 <= len(s.description) <= 1024)

def test_body_under_500_lines(self):         self.assertLess(len(s.body.splitlines()), 500)
def test_one_version_everywhere(self):       self.assertEqual({s.version for s in all}, {"0.2.0"})
def test_scripts_declare_python(self):       # skills with a scripts/ folder
    self.assertIn("Python 3.9", s.compatibility)
def test_referenced_paths_exist(self):       # every backticked scripts/ assets/ references/ migrations/ path in the body, skipping any path containing "<"
    self.assertTrue((s.dir / path).exists())
def test_references_one_level_deep(self):    self.assertEqual([d for d in (s.dir / "references").glob("*") if d.is_dir()], [])
def test_skills_share_nothing(self):         # every text file under each skill
    self.assertNotIn("../", text); self.assertNotIn("skills/baseline-", text)
```

- [ ] **Step 2: Run to verify failure.** Run the test command. Expected: FAIL (`test_exactly_four_skills`: no `skills/` folder).
- [ ] **Step 3: Create the four `SKILL.md` files** with frontmatter `name`, `description`, `compatibility` (init only: `Python 3.9+ (standard library only), git`), `metadata:` → `version: "0.2.0"`, and these descriptions:
  - init: "Set up a repository for the baseline (ADRs and coding standards that steer agents) or update a repository that already uses it. Use when the engineer asks to initialise, install, set up, adopt or update the baseline in a repo."
  - desired-state: "Summarise the conversation as a short desired-state document with diagrams before any code is written, then record the ADRs and coding standards the conversation settled. Use at the end of the questions, when you would otherwise wait for the engineer's approval to start coding, and whenever a decision or repeatable rule comes up later."
  - documentation: "Skeleton stub, not implemented yet. Will write the repository's documentation from the finished code after the engineer says all coding is done."
  - refactor: "Skeleton stub, not implemented yet. Will review a branch against the ADRs and coding standards and rewrite it. Use only when the engineer explicitly asks."
  Bodies for init and desired-state: one line ("Filled in by a later task."). Bodies for the two stubs: "This skill is a placeholder in version 0.2.0. If it is invoked, tell the engineer it is not implemented yet and stop."
- [ ] **Step 4: Run to verify pass.** Expected: all `SkillSpecTest` tests PASS.
- [ ] **Step 5: Commit**

```bash
git add skills tests
git commit -m "feat: four-skill package skeleton with spec-lint test"
```

---

### Task 2: One-command version bump

**Files:**
- Create: `tools/bump_version.py`
- Test: `tests/bump_version_test.py`

**Interfaces:**
- Consumes: `helpers.run`, `helpers.ROOT`
- Produces: CLI `bump_version.py <new_version> [--root PATH]`. It rewrites `metadata.version` in every `<root>/skills/*/SKILL.md`, printing `updated <relpath>` for each file changed. Exit 0; exit 2 and no change when `<new_version>` does not match `^\d+\.\d+\.\d+$`.

- [ ] **Step 1: Write the failing tests** (copy `ROOT/skills` into a temp dir and pass it as `--root`):

```python
def test_bumps_all_four(self):
    r = run(TOOL, "0.3.1", "--root", str(tmp)); self.assertEqual(r.returncode, 0)
    self.assertEqual({read_version(tmp, n) for n in NAMES}, {"0.3.1"})
def test_rejects_bad_version_and_changes_nothing(self):
    r = run(TOOL, "v1", "--root", str(tmp)); self.assertEqual(r.returncode, 2)
    self.assertEqual({read_version(tmp, n) for n in NAMES}, {"0.2.0"})
def test_second_run_is_a_no_op(self):  # run twice with 0.3.1; second prints no "updated" lines
```

- [ ] **Step 2: Run to verify failure.** Expected: FAIL (script missing).
- [ ] **Step 3: Implement `main(argv: List[str]) -> int` in `tools/bump_version.py`.** Replace only inside the frontmatter block, with a regex on the indented `version:` line, preserving the quotes.
- [ ] **Step 4: Run to verify pass.**
- [ ] **Step 5: Commit** — `git add tools tests && git commit -m "feat: one-command version bump across the four skills"`

---

### Task 3: Init — kit, `AGENTS.md` block, templates

**Files:**
- Create: `skills/baseline-init/scripts/kit.py`, `skills/baseline-init/scripts/init.py`
- Create: `skills/baseline-init/assets/kit/AGENTS.block.md`, `skills/baseline-init/assets/kit/docs/adr/TEMPLATE.md`, `skills/baseline-init/assets/kit/docs/standards/TEMPLATE.md`
- Modify: `skills/baseline-init/SKILL.md` (init mode)
- Test: `tests/init_test.py`

**Interfaces:**
- Produces (`kit.py`):
  - `installed_version() -> str` (reads `metadata.version` from this skill's own `SKILL.md`, located from `__file__`)
  - `@dataclass Block(start: int, end: int, version: str, sha256: str, body: str)`; `find_block(text: str) -> Optional[Block]`; `block_is_edited(b: Block) -> bool`
  - `render_block(version: str) -> str`: `<!-- baseline:begin version=<v> sha256=<hex of body> -->\n` + body of `assets/kit/AGENTS.block.md` + `<!-- baseline:end -->\n`
  - `with_block(text: str, version: str) -> str`: replaces the block if present, otherwise appends a blank line and the block
  - `kit_files(version: str) -> Dict[str, str]`: relative path → content, for `baseline.yml` (`baseline_version: <v>\n`), `CLAUDE.md` (`@AGENTS.md\n`), `docs/adr/TEMPLATE.md`, `docs/standards/TEMPLATE.md` (each starts with `<!-- baseline-owned version=<v> -->`)
- Produces (`init.py`): CLI `init.py <target> [--dry-run]`. Prints one line per action: `create <path>`, `append AGENTS.md`, `keep <path>` (file exists, left alone). A dry run prints the same lines plus `dry run: nothing written`. Exit 0; exit 2 if `<target>` is not a directory or already holds `baseline.yml`.

- [ ] **Step 1: Write the failing tests** (`InitTest`, each in a fresh temp dir; import `kit` by inserting `skill_dir("baseline-init") / "scripts"` into `sys.path`):

```python
def test_init_creates_files_in_empty_repo(self):
    r = run(INIT, str(t)); self.assertEqual(r.returncode, 0)
    self.assertEqual((t/"baseline.yml").read_text(), "baseline_version: 0.2.0\n")
    self.assertEqual((t/"CLAUDE.md").read_text(), "@AGENTS.md\n")
    self.assertTrue((t/"docs/adr/TEMPLATE.md").read_text().startswith("<!-- baseline-owned version=0.2.0 -->"))
    b = kit.find_block((t/"AGENTS.md").read_text()); self.assertFalse(kit.block_is_edited(b))
def test_block_routes_the_agent(self):   # text of the block body
    for s in ("baseline-desired-state", "docs/adr/", "docs/standards/", "baseline-documentation"): self.assertIn(s, body)
    self.assertIn("only when the engineer asks", body)
def test_templates_have_required_headings(self):
    adr: "## Decision", "## Why", "## Diagram or snippet" in order
    standard: "## End result", "## Snippets", "## Exceptions" in order
def test_existing_agents_md_kept_byte_for_byte(self):   # Review Focus 1
    (t/"AGENTS.md").write_text(orig); run(INIT, str(t)); self.assertTrue((t/"AGENTS.md").read_text().startswith(orig))
def test_existing_claude_md_is_kept(self):               # output contains "keep CLAUDE.md"
def test_refuses_when_already_initialised(self):         # Review Focus 2
    run(INIT, str(t)); before = snapshot(t); r = run(INIT, str(t))
    self.assertEqual(r.returncode, 2); self.assertEqual(snapshot(t), before)
def test_dry_run_writes_nothing(self):  # stdout has "create baseline.yml" and "dry run: nothing written"; snapshot unchanged
def test_missing_target_exits_2(self):
```

- [ ] **Step 2: Run to verify failure.** Expected: FAIL (scripts missing).
- [ ] **Step 3: Write the kit assets.** Block body (about 10 lines, tight), under `## Baseline`:
  - The baseline steers code through ADRs in `docs/adr/` and coding standards in `docs/standards/` only; read both before generating code.
  - Before coding: when the questions are done and you would wait for approval to start, run `baseline-desired-state` first and wait for the engineer's approval.
  - When a decision or repeatable rule comes up, write it as an ADR or standard from the template in that folder, in the decisions PR; never leave it for another agent.
  - When the engineer says the work is finished, run `baseline-documentation` in a fresh session or subagent.
  - Run `baseline-refactor` only when the engineer asks.
  - Do not edit this block; `baseline-init` replaces it on update.

  ADR template headings: `# <Title>`, `## Decision`, `## Why`, `## Diagram or snippet` (each with one-line guidance in comments). Standard template headings: `# <The rule in one line>`, `## End result`, `## Snippets`, `## Exceptions` (default text: "None.").
- [ ] **Step 4: Implement `kit.py` and `init.py`** to the signatures above. A missing `AGENTS.md` starts from the line `# Instructions for working in this repository` and then `with_block`.
- [ ] **Step 5: Write the init-mode body of `skills/baseline-init/SKILL.md`** (short): run `scripts/init.py <repo> --dry-run`, show the engineer the lines, run it for real after their yes, then say which files appeared and that nothing is committed. Paths are relative to this skill's folder. Mention `assets/kit/`.
- [ ] **Step 6: Run to verify pass** (the whole suite).
- [ ] **Step 7: Commit** — `git add skills tests && git commit -m "feat: baseline-init kit, AGENTS.md block and init script"`

---

### Task 4: Update runner with migrations

**Files:**
- Create: `skills/baseline-init/scripts/update.py`, `skills/baseline-init/migrations/README.md`
- Modify: `skills/baseline-init/SKILL.md` (update mode)
- Test: `tests/update_test.py`

**Interfaces:**
- Consumes: `kit.installed_version()`, `kit.find_block`, `kit.block_is_edited`, `kit.with_block`
- Produces (`update.py`, all take `--installed-version V` and `--migrations-dir DIR`, both optional):
  - `plan <repo>`: prints `current <v>`, `installed <v>`, then per pending migration `migration <from>-to-<to>` followed by that migration's `--dry-run` output indented two spaces, then `owned AGENTS.md block: <unchanged|outdated|edited|missing>` and, when nothing is pending, the versions match and the block is `unchanged`, `up to date`. Exit 0; exit 2 if the repo has no `baseline.yml`; exit 3 if `current` is newer than `installed`.
  - `apply <repo> <migration-id>`: the id must be the first pending migration (else exit 2). Runs its `migrate.py <repo> --confirm`; on exit 0 sets `baseline_version` to the migration's `to`; on failure exits 1 and leaves the version alone.
  - `finish <repo> [--discard-edits]`: exit 2 if migrations are pending; exit 4 (changing nothing) if the block is `edited` and `--discard-edits` is absent; otherwise `with_block(…, installed)` and `baseline_version = installed`.
- Migration contract (written in `migrations/README.md`): folder `<from>-to-<to>/migrate.py`; `migrate.py <repo> --dry-run` prints the planned changes and changes nothing; `migrate.py <repo> --confirm` applies them and exits non-zero on failure. Pending = `from >= current` and `to <= installed`, ordered by `from`. Optional `MIGRATION.md` holds instructions for changes a script cannot make.

- [ ] **Step 1: Write the failing tests** (`UpdateTest`; helper `make_migration(dir, frm, to, fail=False)` writes a `migrate.py` that prints `move docs/old -> docs/new` on `--dry-run` and renames `docs/old` to `docs/new` on `--confirm`, or exits 1 when `fail`; helper `make_repo(version)` runs the real `init.py` and then rewrites `baseline_version`):

```python
def test_plan_up_to_date(self):              # repo 0.2.0, installed 0.2.0 -> exit 0, "up to date" in stdout
def test_plan_shows_dry_run_and_changes_nothing(self):
    out has "migration 0.2.0-to-0.3.0" and "  move docs/old -> docs/new"; (t/"docs/old").exists(); version still 0.2.0
def test_apply_runs_migration_and_moves_version(self):
    apply -> exit 0; (t/"docs/new").exists(); version == "0.3.0"
def test_failed_migration_does_not_advance(self):        # Review Focus 4
    apply -> exit 1; version still 0.2.0
def test_repo_newer_than_installed(self):                # Review Focus 3
    repo 0.4.0, installed 0.3.0 -> plan exits 3; apply exits non-zero
def test_apply_out_of_order_refused(self):               # two migrations; apply the second first -> exit 2
def test_finish_refuses_while_pending(self):             # exit 2
def test_finish_replaces_block_and_sets_version(self):
    repo 0.2.0, --installed-version 0.2.1 -> exit 0; block version == "0.2.1"; baseline.yml == "baseline_version: 0.2.1\n"
def test_edited_block_is_reported_and_protected(self):   # Review Focus 5
    edit one line inside the block; plan prints "owned AGENTS.md block: edited"
    finish -> exit 4, AGENTS.md unchanged; finish --discard-edits -> exit 0, block unedited
```

- [ ] **Step 2: Run to verify failure.**
- [ ] **Step 3: Implement `update.py`** to the interface above. Versions compare as tuples of ints; the version line in `baseline.yml` is rewritten with a regex, leaving the rest of the file alone.
- [ ] **Step 4: Write `migrations/README.md`** (the contract above, with one made-up example folder name) and an `.gitkeep`-free layout: no migration ships in 0.2.0.
- [ ] **Step 5: Write the update-mode body of `SKILL.md`** (short): `plan` → show the engineer the output → for each migration ask for approval (one numbered decision each, recommendation first) → `apply` → `finish` (ask about edits first) → leave committing to the repo's own conventions. Rules, stated plainly: a migration may change project-owned files only after the engineer has seen its dry run and approved; a declined migration stops the update, so tell the engineer the repo stays at that version and why; never skip a migration.
- [ ] **Step 6: Run to verify pass** (whole suite).
- [ ] **Step 7: Commit** — `git add skills tests && git commit -m "feat: baseline-init update runner with migrations"`

---

### Task 5: `baseline-desired-state` content

**Files:**
- Modify: `skills/baseline-desired-state/SKILL.md`
- Create: `skills/baseline-desired-state/assets/desired-state-template.md`, `skills/baseline-desired-state/references/deciding-adrs-and-standards.md`
- Test: `tests/desired_state_test.py`

**Interfaces:**
- Consumes: the ADR and standard templates in a repo's `docs/adr/` and `docs/standards/` (Task 3)
- Produces: the desired-state file convention `docs/desired-state/<YYYY-MM-DD>-<topic>.md`

- [ ] **Step 1: Write the failing tests** (`DesiredStateTest`):

```python
def test_template_headings_in_order(self):
    # "# Desired state:", "## End state", "## Diagram", "## Decisions to record", "## Not in scope"
def test_template_has_one_mermaid_block(self):  self.assertEqual(text.count("```mermaid"), 1)
def test_template_is_short(self):               self.assertLess(len(text.splitlines()), 40)
def test_skill_points_at_its_files(self):       # body mentions both asset/reference paths and "docs/desired-state/"
def test_skill_covers_the_flow(self):           # body contains: "approval", "decisions PR", "same session", "never maintain"
```

- [ ] **Step 2: Run to verify failure.**
- [ ] **Step 3: Write the template**: `## End state` (3–6 bullets), `## Diagram` (one Mermaid block), `## Decisions to record` (lines starting `ADR:` or `Standard:`, or `None`), `## Not in scope`. Tight, with one-line guidance comments.
- [ ] **Step 4: Write `references/deciding-adrs-and-standards.md`** (under 60 lines): a standard is a blanket rule with very limited exceptions, stated as the end result plus mnemonic snippets (worked example: "C# payloads and contracts are records, not classes"); an ADR is for a decision of impact (new technology or dependency, data model or public interface, security or trust boundary, deployment topology, anything hard to reverse); a conversation can settle both, one, or neither.
- [ ] **Step 5: Write the `SKILL.md` body** (under 120 lines), in this order:
  1. When: the questions are done and you would wait for approval to code.
  2. Write `docs/desired-state/<date>-<topic>.md` from the template: condensed, diagrams and snippets first. It is engineer-only, replaces nothing a skill already wrote, and is never maintained.
  3. Put it on its own branch and open a PR if the repo has a GitHub remote and `gh` works; otherwise commit it and say so.
  4. Tell the engineer to read and approve; wait.
  5. After approval: write the ADRs and standards listed under "Decisions to record" yourself, in this session, from the repo's templates, as the next PR above the desired-state PR (the decisions PR); the engineer reviews them; then implement. Stack the code however reads best.
  6. A later decision goes into the decisions PR; rebase the code PRs above and tell the engineer what changed.
- [ ] **Step 6: Run to verify pass** (whole suite).
- [ ] **Step 7: Commit** — `git add skills tests && git commit -m "feat: baseline-desired-state skill, template and decision guide"`

---

### Task 6: Install proof (by hand, throwaway repo)

**Files:** none changed unless a fix is needed. Results go in the final report.

**Interfaces:** Consumes the whole package. Produces a written result for each check below, marked verified or not verified.

- [ ] **Step 1: Pin the installer.** Run `npm view skills version`, note it as `<V>`, and use `DISABLE_TELEMETRY=1 npx skills@<V> ...` for every command below (the CLI sends telemetry otherwise).
- [ ] **Step 2: List from a local path.** `DISABLE_TELEMETRY=1 npx skills@<V> add <repo-root> --list`. Expected: the four skill names. Record the output.
- [ ] **Step 3: Install into a throwaway repo.** `PROOF=$(mktemp -d); cd $PROOF && git init -q`, then `DISABLE_TELEMETRY=1 npx skills@<V> add <repo-root> -a claude-code --skill '*' -y`. Expected: four skills under the agent's skills folder and a `skills-lock.json`. Record the exact folders used and whether they are symlinks or copies.
- [ ] **Step 4: Check nothing was lost.** `diff -r <repo-root>/skills/baseline-init <installed-baseline-init>`. Expected: no difference, so `scripts/`, `assets/` and `migrations/` came through intact.
- [ ] **Step 5: Run init from the installed copy.** `python3 <installed-baseline-init>/scripts/init.py $PROOF`. Expected: the five `create`/`append` lines and the files from Task 3. Then `update.py plan $PROOF`: expected `up to date`.
- [ ] **Step 6: Other routes.** Run `gh skill --help`. If installing from a local path or the repo is supported, try it in a second throwaway repo and record the result. Record Copilot's skills folder as the CLI reports it, against GitHub's documented `.github/skills/`.
- [ ] **Step 7: Codex (engineer-run).** Codex is not installed here. Repeat Steps 3–5 with `-a codex`, then start Codex in the repo and list its skills. Record the folder used and whether all four appear. If it cannot be run, report it as not verified.

---

### Task 7: Behaviour proof in an agent (by hand)

**Files:** none changed unless a fix is needed.

**Interfaces:** Consumes the throwaway repo from Task 6 (initialised, skills installed, `app.py` containing a tiny command-line script, everything committed).

- [ ] **Step 1: Start Claude Code in the throwaway repo** and say exactly: "I want to add a `--json` flag to app.py. Brainstorm it with me, one question at a time. Also, from now on every payload type in this repo should be a dataclass, never a dict." Answer its questions briefly until it has none left.
- [ ] **Step 2: Check each expectation** and record pass or fail:
  1. It reads the `AGENTS.md` block and runs `baseline-desired-state` without being told the skill's name.
  2. `docs/desired-state/<date>-<topic>.md` exists with the template's headings and one Mermaid block.
  3. "Decisions to record" lists a standard about dataclasses.
  4. It stops and waits for approval before writing code.
- [ ] **Step 3: Say "approved."** Expected: it writes `docs/standards/<slug>.md` from the template (headings `End result`, `Snippets`, `Exceptions`), puts it in a separate PR or branch above the desired-state one, and waits for review before implementing. Record whether it opened PRs or reported that there was no remote.
- [ ] **Step 4: Repeat Steps 1–3 in Codex** (engineer-run). If it cannot be run, report it as not verified.
- [ ] **Step 5: Write the report**: what was installed where, what each agent did against the expectations, and everything not verified. Do not commit anything from the throwaway repo.
