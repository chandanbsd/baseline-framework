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
    print("move docs/old -> docs/new")
elif mode == "--confirm":
    if %(fail)s:
        print("boom", file=sys.stderr)
        sys.exit(1)
    (repo / "docs" / "old").rename(repo / "docs" / "new")
'''


class UpdateTest(TempRepoCase):
    def setUp(self):
        super().setUp()
        self.mig = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.mig)

    def make_migration(self, frm, to, fail=False):
        d = self.mig / ("%s-to-%s" % (frm, to))
        d.mkdir()
        (d / "migrate.py").write_text(MIGRATE % {"fail": fail})

    def make_repo(self, version):
        self.assertEqual(run(INIT, self.t).returncode, 0)
        (self.t / "baseline.yml").write_text("baseline_version: %s\n" % version)
        (self.t / "docs" / "old").mkdir(parents=True)
        (self.t / "docs" / "old" / "note.txt").write_text("x")

    def upd(self, command, *args, installed):
        return run(UPDATE, command, self.t, *args, "--installed-version", installed, "--migrations-dir", self.mig)

    def version(self):
        return (self.t / "baseline.yml").read_text()

    def test_plan_up_to_date(self):
        self.make_repo("0.2.0")
        r = self.upd("plan", installed="0.2.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("up to date", r.stdout)

    def test_plan_shows_the_dry_run_and_changes_nothing(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        before = snapshot(self.t)
        r = self.upd("plan", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("migration 0.2.0-to-0.3.0", r.stdout)
        self.assertIn("  move docs/old -> docs/new", r.stdout)
        self.assertIn("owned AGENTS.md block: outdated", r.stdout)
        self.assertEqual(snapshot(self.t), before)

    def test_plan_without_baseline_yml_exits_2(self):
        r = self.upd("plan", installed="0.2.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline.yml", r.stderr)

    def test_apply_runs_the_migration_and_moves_the_version(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((self.t / "docs" / "new" / "note.txt").exists())
        self.assertFalse((self.t / "docs" / "old").exists())
        self.assertEqual(self.version(), "baseline_version: 0.3.0\n")

    def test_a_failed_migration_does_not_advance_the_version(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0", fail=True)
        r = self.upd("apply", "0.2.0-to-0.3.0", installed="0.3.0")
        self.assertEqual(r.returncode, 1)
        self.assertIn("boom", r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.0\n")

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
        self.assertEqual(self.version(), "baseline_version: 0.2.0\n")

    def test_finish_refuses_while_migrations_are_pending(self):
        self.make_repo("0.2.0")
        self.make_migration("0.2.0", "0.3.0")
        r = self.upd("finish", installed="0.3.0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("0.2.0-to-0.3.0", r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.0\n")

    def test_finish_replaces_the_block_and_sets_the_version(self):
        self.make_repo("0.2.0")
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.version(), "baseline_version: 0.2.1\n")
        agents = (self.t / "AGENTS.md").read_text()
        self.assertEqual(re.findall(r"<!-- baseline:begin version=(\S+) ", agents), ["0.2.1"])

    def test_an_edited_block_is_reported_and_protected(self):
        self.make_repo("0.2.0")
        path = self.t / "AGENTS.md"
        path.write_text(path.read_text().replace("Do not edit this block.", "Edit as you like."))
        self.assertIn("owned AGENTS.md block: edited", self.upd("plan", installed="0.2.1").stdout)
        before = snapshot(self.t)
        r = self.upd("finish", installed="0.2.1")
        self.assertEqual(r.returncode, 4)
        self.assertEqual(snapshot(self.t), before)
        r = self.upd("finish", "--discard-edits", installed="0.2.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        text = path.read_text()
        self.assertIn("Do not edit this block.", text)
        self.assertNotIn("Edit as you like.", text)

    def test_the_shipped_migrations_folder_has_nothing_pending(self):
        self.make_repo("0.2.0")
        r = run(UPDATE, "plan", self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("up to date", r.stdout)


if __name__ == "__main__":
    unittest.main()
