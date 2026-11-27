"""baseline-init's update.py: what an agent runs to bring a repository to the installed version."""
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from helpers import TempRepoCase, run, skill_dir, snapshot

INIT = skill_dir("baseline-init") / "scripts" / "init.py"
UPDATE = skill_dir("baseline-init") / "scripts" / "update.py"

MIGRATE = '''import sys
from pathlib import Path
repo, mode = Path(sys.argv[1]), sys.argv[2]
if mode == "--dry-run":
    if %(needs)r and not (repo / %(needs)r).exists():
        print("missing " + %(needs)r, file=sys.stderr)
        sys.exit(1)
    print("move docs/old -> docs/new")
elif mode == "--confirm":
    if %(fail)s:
        print("boom", file=sys.stderr)
        sys.exit(1)
    if %(raw)s:
        sys.stdout.buffer.write(b"caf\\xe9\\n")
    (repo / "docs" / "old").rename(repo / "docs" / "new")
'''


class UpdateTest(TempRepoCase):
    def setUp(self):
        super().setUp()
        self.mig = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.mig)

    def make_migration(self, frm, to, fail=False, needs="", raw=False, instructions=False, script=True):
        d = self.mig / ("%s-to-%s" % (frm, to))
        d.mkdir()
        if script:
            (d / "migrate.py").write_text(MIGRATE % {"fail": fail, "needs": needs, "raw": raw})
        if instructions:
            (d / "MIGRATION.md").write_text("Rename the folder by hand.\n")

    def make_repo(self, version):
        self.assertEqual(run(INIT, self.t).returncode, 0)
        self.config.write_text("baseline_version: %s\ndocuments_skipped: []\n" % version)
        (self.t / "docs" / "old").mkdir(parents=True)
        (self.t / "docs" / "old" / "note.txt").write_text("x")
        # the owned files that init wrote carry the installed version; age them to the repo's version
        self.age_owned(version)

    OWNED = ("baseline/baseline.md", "baseline/check.py", ".github/workflows/baseline.yml")

    def age_owned(self, version):
        for rel in self.OWNED:
            path = self.t / rel
            path.write_text(re.sub(r"version=\S+", "version=%s" % version, path.read_text(), count=1))

    @property
    def config(self):
        return self.t / "baseline" / "baseline.yml"

    def upd(self, command, *args, installed):
        return run(UPDATE, command, self.t, *args, "--installed-version", installed, "--migrations-dir", self.mig)

    def version(self):
        return self.config.read_text().splitlines()[0]

    def header_version(self):
        return re.search(r"version=(\S+)", (self.t / "baseline" / "baseline.md").read_text()).group(1)

    def test_plan_up_to_date(self):
        self.make_repo("0.2.0")
        r = self.upd("plan", installed="0.2.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("baseline.md: unchanged", r.stdout)
        self.assertIn("AGENTS.md pointer: present", r.stdout)
        self.assertIn("up to date", r.stdout)

    def test_plan_shows_the_dry_run_and_changes_nothing(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        before = snapshot(self.t)
        r = self.upd("plan", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("migration 0.2.0-to-0.3.0", r.stdout)
        self.assertIn("  move docs/old -> docs/new", r.stdout)
        self.assertIn("baseline.md: outdated", r.stdout)
        self.assertEqual(snapshot(self.t), before)

    def test_plan_without_baseline_yml_exits_2(self):
        r = self.upd("plan", installed="0.2.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline/baseline.yml", r.stderr)

    def test_apply_runs_the_migration_and_moves_the_version(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((self.t / "docs" / "new" / "note.txt").exists())
        self.assertFalse((self.t / "docs" / "old").exists())
        self.assertEqual(self.version(), "baseline_version: 0.3.0")

    def test_a_failed_migration_does_not_advance_the_version(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0", fail=True)
        r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
        self.assertEqual(r.returncode, 1)
        self.assertIn("boom", r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.0")

    def test_a_repo_newer_than_the_installed_skills_is_refused(self):
        self.make_repo("0.4.0")
        self.make_migration("0.2.0", "0.3.0")
        before = snapshot(self.t)
        self.assertEqual(self.upd("plan", installed="0.3.0").returncode, 3)
        self.assertEqual(self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0").returncode, 3)
        self.assertEqual(self.upd("finish", installed="0.3.0").returncode, 3)
        self.assertEqual(snapshot(self.t), before)

    def test_apply_out_of_order_is_refused(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        self.make_migration("0.3.0", "0.4.0")
        r = self.upd("apply", "0.3.0-to-0.4.0", installed="0.4.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("0.2.0-to-0.3.0", r.stderr)  # the error names the migration that is next
        self.assertEqual(self.version(), "baseline_version: 0.2.0")

    def test_finish_refuses_while_migrations_are_pending(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        r = self.upd("finish", installed="0.3.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("0.2.0-to-0.3.0", r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.0")

    def test_finish_replaces_baseline_md_and_sets_the_version(self):
        self.make_repo("0.2.0")
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.1")
        self.assertEqual(self.header_version(), "0.2.1")
        self.assertIn("baseline.md: unchanged", self.upd("plan", installed="0.2.1").stdout)

    def test_an_edited_baseline_md_is_reported_and_protected(self):
        self.make_repo("0.2.0")
        path = self.t / "baseline" / "baseline.md"
        edited = path.read_text().replace("Read both", "Skim both")
        self.assertIn("Skim both", edited)  # the edit really happened
        path.write_text(edited)
        self.assertIn("baseline.md: edited", self.upd("plan", installed="0.2.1").stdout)
        before = snapshot(self.t)
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 4)
        self.assertEqual(snapshot(self.t), before)
        r = self.upd("finish", "--discard-edits", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        text = path.read_text()
        self.assertIn("Read both", text)
        self.assertNotIn("Skim both", text)

    def test_a_baseline_md_replaced_by_the_teams_own_text_counts_as_edited(self):
        self.make_repo("0.2.0")
        path = self.t / "baseline" / "baseline.md"
        path.write_text("# Our own notes\n")
        self.assertIn("baseline.md: edited", self.upd("plan", installed="0.2.1").stdout)
        self.assertEqual(self.upd("finish", installed="0.2.1").returncode, 4)
        self.assertEqual(path.read_text(), "# Our own notes\n")

    def test_a_missing_baseline_md_is_reported_and_recreated_by_finish(self):
        self.make_repo("0.2.0")
        (self.t / "baseline" / "baseline.md").unlink()
        self.assertIn("baseline.md: missing", self.upd("plan", installed="0.2.1").stdout)
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.header_version(), "0.2.1")

    def test_finish_keeps_a_crlf_baseline_md_crlf(self):
        self.make_repo("0.2.0")
        path = self.t / "baseline" / "baseline.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertIn("baseline.md: unchanged", self.upd("plan", installed="0.2.0").stdout)
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = path.read_bytes()
        self.assertIsNone(re.search(rb"(?<!\r)\n", data))
        self.assertEqual(self.header_version(), "0.2.1")

    def test_update_never_writes_agents_md_and_reports_a_missing_pointer(self):
        self.make_repo("0.2.0")
        agents = self.t / "AGENTS.md"
        agents.write_text("# Ours, with no pointer\n")
        r = self.upd("plan", installed="0.2.1")
        self.assertIn("AGENTS.md pointer: missing", r.stdout)
        self.assertNotIn("up to date", r.stdout)
        self.assertEqual(self.upd("finish", installed="0.2.1").returncode, 0)
        self.assertEqual(agents.read_text(), "# Ours, with no pointer\n")

    def test_plan_reports_the_check_and_the_workflow(self):
        self.make_repo("0.2.0")
        r = self.upd("plan", installed="0.2.1")
        self.assertIn("baseline.md: outdated", r.stdout)
        self.assertIn("check.py: outdated", r.stdout)
        self.assertIn("workflow: outdated", r.stdout)
        r = self.upd("plan", installed="0.2.0")
        self.assertIn("check.py: unchanged", r.stdout)
        self.assertIn("workflow: unchanged", r.stdout)
        self.assertIn("up to date", r.stdout)

    def test_finish_overwrites_the_check_and_the_workflow(self):
        self.make_repo("0.2.0")
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        for rel in self.OWNED:
            with self.subTest(file=rel):
                self.assertIn("version=0.2.1 ", (self.t / rel).read_text().splitlines()[0] + " ")
        self.assertNotIn("outdated", self.upd("plan", installed="0.2.1").stdout)

    def test_an_edited_check_or_workflow_is_reported_protected_and_named(self):
        for rel, label in (("baseline/check.py", "check.py"), (".github/workflows/baseline.yml", "workflow")):
            with self.subTest(file=rel):
                self.t = Path(tempfile.mkdtemp())
                self.addCleanup(shutil.rmtree, self.t)
                self.make_repo("0.2.0")
                path = self.t / rel
                path.write_text(path.read_text() + "# our own line\n")
                self.assertIn("%s: edited" % label, self.upd("plan", installed="0.2.1").stdout)
                before = snapshot(self.t)
                r = self.upd("finish", installed="0.2.1")
                self.assertEqual(r.returncode, 4)
                self.assertIn(label, r.stderr)
                self.assertEqual(snapshot(self.t), before)
                r = self.upd("finish", "--discard-edits", installed="0.2.1")
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertNotIn("our own line", path.read_text())

    def test_a_deleted_check_or_workflow_is_not_recreated_but_baseline_md_is(self):
        self.make_repo("0.2.0")
        for rel in self.OWNED:
            (self.t / rel).unlink()
        plan = self.upd("plan", installed="0.2.1").stdout
        for label in ("baseline.md", "check.py", "workflow"):
            self.assertIn("%s: missing" % label, plan)
        self.assertEqual(self.upd("finish", installed="0.2.1").returncode, 0)
        self.assertTrue((self.t / "baseline" / "baseline.md").exists())
        self.assertFalse((self.t / "baseline" / "check.py").exists())
        self.assertFalse((self.t / ".github" / "workflows" / "baseline.yml").exists())

    def test_plan_dry_runs_only_the_next_migration(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        self.make_migration("0.3.0", "0.4.0", needs="docs/new")  # its dry run is only valid after the first is applied
        r = self.upd("plan", installed="0.4.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("migration 0.2.0-to-0.3.0", r.stdout)
        self.assertIn("then migration 0.3.0-to-0.4.0", r.stdout)
        self.assertNotIn("dry run failed", r.stdout)
        self.assertEqual(r.stdout.count("  move docs/old -> docs/new"), 1)
        self.assertEqual(self.upd("apply", "0.2.0-to-0.3.0", installed="0.4.0").returncode, 0)
        r = self.upd("plan", installed="0.4.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("  move docs/old -> docs/new", r.stdout)

    def test_non_utf8_migration_output_does_not_crash_after_the_change(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0", raw=True)
        r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.3.0")

    def test_baseline_version_is_read_and_written_in_common_yaml_forms_and_the_rest_survives(self):
        self.make_migration("0.2.0", "0.3.0")
        forms = [
            ('baseline_version: "0.2.0"', 'baseline_version: "0.3.0"', "\n"),
            ("baseline_version: 0.2.0  # pinned", "baseline_version: 0.3.0  # pinned", "\n"),
            ("baseline_version: 0.2.0", "baseline_version: 0.3.0", "\r\n"),
        ]
        for before, after, eol in forms:
            with self.subTest(form=before, eol=repr(eol)):
                self.t = Path(tempfile.mkdtemp())
                self.addCleanup(shutil.rmtree, self.t)
                self.make_repo("0.2.0")
                rest = "documents_skipped: [deployment]" + eol
                self.config.write_bytes((before + eol + rest).encode())
                r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(self.config.read_bytes(), (after + eol + rest).encode())

    def test_an_unreadable_baseline_version_is_refused_cleanly(self):
        self.make_repo("0.2.0")
        self.config.write_text("baseline_version: latest\n")
        r = self.upd("plan", installed="0.3.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline_version", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_apply_and_finish_have_a_dry_run_that_changes_nothing(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        before = snapshot(self.t)
        r = self.upd("apply", "0.2.0-to-0.3.0", "--dry-run", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("  move docs/old -> docs/new", r.stdout)
        r2 = self.upd("finish", "--dry-run", installed="0.2.1")  # the 0.3.0 migration is not pending for 0.2.1
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertIn("would", r2.stdout)
        self.assertEqual(snapshot(self.t), before)

    def test_plan_names_instructions_and_warns_about_a_folder_without_a_script(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0", instructions=True)
        self.make_migration("0.3.0", "0.4.0", script=False, instructions=True)
        r = self.upd("plan", installed="0.4.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0.2.0-to-0.3.0/MIGRATION.md", r.stdout)
        self.assertIn("ignored 0.3.0-to-0.4.0: no migrate.py", r.stdout)

    def test_the_shipped_migrations_folder_has_nothing_pending(self):
        self.make_repo("0.2.0")
        r = run(UPDATE, "plan", self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("up to date", r.stdout)


if __name__ == "__main__":
    unittest.main()
