"""baseline-init's init.py and kit.py: what an agent gets when it sets up a repository."""
import hashlib
import re
import sys
import unittest

from helpers import TempRepoCase, run, skill_dir, snapshot

sys.path.insert(0, str(skill_dir("baseline-init") / "scripts"))
import kit  # noqa: E402

INIT = skill_dir("baseline-init") / "scripts" / "init.py"
KIT = skill_dir("baseline-init") / "assets" / "kit"
LAYOUT = {
    "AGENTS.md",
    "CLAUDE.md",
    "baseline/baseline.md",
    "baseline/baseline.yml",
    "baseline/check.py",
    "baseline/adr/TEMPLATE.md",
    "baseline/standards/TEMPLATE.md",
    ".github/workflows/baseline.yml",
}
HASH_HEADER_RE = re.compile(r"^# baseline version=(\S+) sha256=([0-9a-f]{64})$")


class InitTest(TempRepoCase):
    def test_init_creates_the_layout_and_nothing_else_in_an_empty_repo(self):
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(set(snapshot(self.t)), LAYOUT)
        self.assertEqual(
            (self.t / "baseline" / "baseline.yml").read_text(),
            "baseline_version: 0.2.0\ndocuments_skipped: []\n",
        )
        self.assertEqual((self.t / "CLAUDE.md").read_text(), "@AGENTS.md\n")

    def test_baseline_md_is_the_shipped_body_with_its_version_and_hash(self):
        run(INIT, self.t)
        first, _, body = (self.t / "baseline" / "baseline.md").read_text().partition("\n")
        shipped = (KIT / "baseline" / "baseline.md").read_text()
        self.assertEqual(body, shipped)
        self.assertEqual(first, "<!-- baseline version=0.2.0 sha256=%s -->" % hashlib.sha256(shipped.encode("utf-8")).hexdigest())

    def test_check_and_workflow_are_the_shipped_assets_with_a_hashed_header(self):
        run(INIT, self.t)
        for rel, asset in (
            ("baseline/check.py", KIT / "baseline" / "check.py"),
            (".github/workflows/baseline.yml", KIT / "github-workflow" / "baseline.yml"),
        ):
            with self.subTest(file=rel):
                first, _, body = (self.t / rel).read_text().partition("\n")
                shipped = asset.read_text()
                self.assertEqual(body, shipped)
                match = HASH_HEADER_RE.match(first)
                self.assertIsNotNone(match, first)
                self.assertEqual(match.group(1), "0.2.0")
                self.assertEqual(match.group(2), hashlib.sha256(shipped.encode("utf-8")).hexdigest())

    def test_a_fresh_init_passes_its_own_check(self):
        run(INIT, self.t)
        r = run(self.t / "baseline" / "check.py", env={"PATH": str(self.t)})  # no renderer on the PATH
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("not yet documented", r.stdout)

    def test_an_existing_workflow_is_kept(self):
        workflow = self.t / ".github" / "workflows" / "baseline.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text("name: ours\n")
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(workflow.read_text(), "name: ours\n")
        self.assertIn("keep .github/workflows/baseline.yml", r.stdout)

    def test_agents_md_gets_the_pointer_and_no_markers(self):
        run(INIT, self.t)
        text = (self.t / "AGENTS.md").read_text()
        self.assertIn((KIT / "AGENTS.pointer.md").read_text(), text)
        self.assertNotIn("baseline:begin", text)

    def test_existing_agents_md_is_kept_byte_for_byte_and_the_pointer_appended(self):
        original = "# My project\n\nRules that were here first.\n"
        (self.t / "AGENTS.md").write_text(original)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        text = (self.t / "AGENTS.md").read_text()
        self.assertTrue(text.startswith(original))
        self.assertIn("baseline/baseline.md", text[len(original):])
        self.assertIn("append AGENTS.md", r.stdout)

    def test_the_pointer_is_not_added_twice(self):
        original = "# Mine\n\n" + (KIT / "AGENTS.pointer.md").read_text()
        (self.t / "AGENTS.md").write_text(original)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.t / "AGENTS.md").read_text(), original)
        self.assertIn("keep AGENTS.md", r.stdout)

    def test_crlf_agents_md_is_kept_byte_for_byte(self):
        original = b"# Mine\r\n\r\nline two\r\n"
        (self.t / "AGENTS.md").write_bytes(original)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        data = (self.t / "AGENTS.md").read_bytes()
        self.assertTrue(data.startswith(original))
        self.assertIn(b"baseline/baseline.md", data[len(original):])
        self.assertIsNone(re.search(rb"(?<!\r)\n", data))  # no bare LF anywhere in a CRLF file

    def test_an_existing_claude_md_is_kept_and_a_missing_import_is_noted(self):
        (self.t / "CLAUDE.md").write_text("mine\n")
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.t / "CLAUDE.md").read_text(), "mine\n")
        self.assertIn("keep CLAUDE.md", r.stdout)
        self.assertIn("note: CLAUDE.md does not import AGENTS.md", r.stdout)

    def test_no_note_when_claude_md_already_imports_agents_md(self):
        (self.t / "CLAUDE.md").write_text("Intro\n@AGENTS.md\n")
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("note:", r.stdout)

    def test_refuses_when_already_initialised_and_changes_nothing(self):
        self.assertEqual(run(INIT, self.t).returncode, 0)
        before = snapshot(self.t)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 2)
        self.assertIn("already initialised", r.stderr)
        self.assertEqual(snapshot(self.t), before)

    def test_a_root_baseline_yml_of_an_older_layout_is_left_alone(self):
        (self.t / "baseline.yml").write_text("baseline_version: 0.1.0\n")
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.t / "baseline.yml").read_text(), "baseline_version: 0.1.0\n")
        self.assertTrue((self.t / "baseline" / "baseline.yml").exists())

    def test_dry_run_writes_nothing(self):
        r = run(INIT, self.t, "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("create baseline/baseline.yml", r.stdout)
        self.assertIn("dry run: nothing written", r.stdout)
        self.assertEqual(snapshot(self.t), {})

    def test_missing_target_exits_2(self):
        r = run(INIT, self.t / "nope")
        self.assertEqual(r.returncode, 2)
        self.assertIn("nope", r.stderr)

    def test_skip_is_written_to_documents_skipped_in_family_order_without_duplicates(self):
        r = run(INIT, self.t, "--skip", "reference, deployment,deployment")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(
            (self.t / "baseline" / "baseline.yml").read_text(),
            "baseline_version: 0.2.0\ndocuments_skipped: [deployment, reference]\n",
        )

    def test_an_unknown_family_is_refused_and_nothing_changes(self):
        r = run(INIT, self.t, "--skip", "deploy")
        self.assertEqual(r.returncode, 2)
        self.assertIn("'deploy'", r.stderr)
        self.assertIn("readme, architecture, course, features, deployment, reference", r.stderr)
        self.assertEqual(snapshot(self.t), {})

    def test_a_non_utf8_agents_md_is_refused_and_nothing_changes(self):
        (self.t / "AGENTS.md").write_bytes(b"caf\xe9\n")
        before = snapshot(self.t)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 2)
        self.assertIn("AGENTS.md", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(snapshot(self.t), before)

    def test_a_file_named_baseline_is_refused_and_nothing_changes(self):
        (self.t / "baseline").write_text("not a folder\n")
        before = snapshot(self.t)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(snapshot(self.t), before)

    def test_templates_do_not_claim_baseline_ownership(self):
        # A file written from a template becomes the project's own; it must not carry a baseline-owned marker.
        run(INIT, self.t)
        for rel in ("baseline/adr/TEMPLATE.md", "baseline/standards/TEMPLATE.md"):
            self.assertNotIn("baseline-owned", (self.t / rel).read_text())


class OwnedFileTest(unittest.TestCase):
    def test_a_rendered_file_parses_and_is_not_edited(self):
        owned = kit.parse_owned(kit.render_baseline_md("0.2.0"))
        self.assertEqual(owned.version, "0.2.0")
        self.assertFalse(kit.owned_is_edited(owned))

    def test_a_hash_style_header_round_trips_for_the_other_owned_files(self):
        for rel in ("baseline/check.py", ".github/workflows/baseline.yml"):
            with self.subTest(file=rel):
                text = kit.render_owned(rel, "0.2.0")
                self.assertTrue(text.startswith("# baseline version=0.2.0 sha256="))
                owned = kit.parse_owned(text)
                self.assertEqual(owned.version, "0.2.0")
                self.assertFalse(kit.owned_is_edited(owned))
                self.assertTrue(kit.owned_is_edited(kit.parse_owned(text + "# an edit\n")))

    def test_a_changed_body_counts_as_edited(self):
        text = kit.render_baseline_md("0.2.0").replace("Read both", "Skim both")
        self.assertIn("Skim both", text)  # the edit really happened
        self.assertTrue(kit.owned_is_edited(kit.parse_owned(text)))

    def test_a_wrong_hash_counts_as_edited(self):
        text = "<!-- baseline version=0.2.0 sha256=%s -->\nbody\n" % ("0" * 64)
        self.assertTrue(kit.owned_is_edited(kit.parse_owned(text)))

    def test_a_file_without_the_header_counts_as_edited(self):
        owned = kit.parse_owned("# My own notes\n")
        self.assertIsNone(owned.version)
        self.assertTrue(kit.owned_is_edited(owned))

    def test_a_crlf_conversion_is_not_an_edit(self):
        text = kit.render_baseline_md("0.2.0").replace("\n", "\r\n")
        self.assertFalse(kit.owned_is_edited(kit.parse_owned(text)))

    def test_render_keeps_a_requested_line_ending(self):
        out = kit.render_baseline_md("0.2.0", "\r\n")
        self.assertIsNone(re.search(r"(?<!\r)\n", out))
        self.assertFalse(kit.owned_is_edited(kit.parse_owned(out)))

    def test_with_pointer_appends_once_and_keeps_crlf(self):
        out = kit.with_pointer("# Mine\r\n")
        self.assertTrue(out.startswith("# Mine\r\n\r\n## Baseline"))
        self.assertIsNone(re.search(r"(?<!\r)\n", out))
        self.assertEqual(kit.with_pointer(out), out)

    def test_with_pointer_adds_the_missing_final_newline(self):
        self.assertTrue(kit.with_pointer("# Mine").startswith("# Mine\n\n## Baseline"))


if __name__ == "__main__":
    unittest.main()
