"""baseline-init's init.py and kit.py: what an agent gets when it sets up a repository."""
import hashlib
import re
import sys
import unittest

from helpers import TempRepoCase, run, skill_dir, snapshot

sys.path.insert(0, str(skill_dir("baseline-init") / "scripts"))
import kit  # noqa: E402

INIT = skill_dir("baseline-init") / "scripts" / "init.py"
BLOCK_ASSET = skill_dir("baseline-init") / "assets" / "kit" / "AGENTS.block.md"


class InitTest(TempRepoCase):
    def test_init_creates_the_kit_in_an_empty_repo(self):
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.t / "baseline.yml").read_text(), "baseline_version: 0.2.0\n")
        self.assertEqual((self.t / "CLAUDE.md").read_text(), "@AGENTS.md\n")
        for rel in ("docs/adr/TEMPLATE.md", "docs/standards/TEMPLATE.md"):
            self.assertTrue((self.t / rel).exists())

    def test_agents_md_block_carries_the_shipped_body_and_its_hash(self):
        run(INIT, self.t)
        text = (self.t / "AGENTS.md").read_text()
        m = re.search(r"<!-- baseline:begin version=0\.2\.0 sha256=([0-9a-f]{64}) -->\n(.*?)<!-- baseline:end -->\n", text, re.S)
        self.assertIsNotNone(m)
        shipped = BLOCK_ASSET.read_text()
        self.assertEqual(m.group(2), shipped)
        self.assertEqual(m.group(1), hashlib.sha256(shipped.encode("utf-8")).hexdigest())

    def test_existing_agents_md_is_kept_byte_for_byte(self):
        original = "# My project\n\nRules that were here first.\n"
        (self.t / "AGENTS.md").write_text(original)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        text = (self.t / "AGENTS.md").read_text()
        self.assertTrue(text.startswith(original))
        self.assertIn("<!-- baseline:begin version=0.2.0", text)
        self.assertIn("append AGENTS.md", r.stdout)

    def test_existing_claude_md_is_kept(self):
        (self.t / "CLAUDE.md").write_text("mine\n")
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.t / "CLAUDE.md").read_text(), "mine\n")
        self.assertIn("keep CLAUDE.md", r.stdout)

    def test_refuses_when_already_initialised_and_changes_nothing(self):
        self.assertEqual(run(INIT, self.t).returncode, 0)
        self.assertTrue((self.t / "baseline.yml").exists())
        before = snapshot(self.t)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 2)
        self.assertIn("already initialised", r.stderr)
        self.assertEqual(snapshot(self.t), before)

    def test_dry_run_writes_nothing(self):
        r = run(INIT, self.t, "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("create baseline.yml", r.stdout)
        self.assertIn("dry run: nothing written", r.stdout)
        self.assertEqual(snapshot(self.t), {})

    def test_missing_target_exits_2(self):
        r = run(INIT, self.t / "nope")
        self.assertEqual(r.returncode, 2)
        self.assertIn("nope", r.stderr)


    def test_templates_do_not_claim_baseline_ownership(self):
        # A file written from a template becomes the project's own; it must not carry a baseline-owned marker.
        run(INIT, self.t)
        for rel in ("docs/adr/TEMPLATE.md", "docs/standards/TEMPLATE.md"):
            self.assertNotIn("baseline-owned", (self.t / rel).read_text())

    def test_crlf_agents_md_is_kept_byte_for_byte(self):
        original = b"# Mine\r\n\r\nline two\r\n"
        (self.t / "AGENTS.md").write_bytes(original)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        data = (self.t / "AGENTS.md").read_bytes()
        self.assertTrue(data.startswith(original))
        self.assertIn(b"<!-- baseline:begin version=0.2.0", data)
        self.assertIsNone(re.search(rb"(?<!\r)\n", data))  # no bare LF anywhere in a CRLF file
        block = kit.find_block(kit.read_text(self.t / "AGENTS.md"))
        self.assertFalse(kit.block_is_edited(block))

    def test_an_unpaired_marker_is_refused_and_nothing_changes(self):
        broken = "# Mine\n\n<!-- baseline:begin version=0.2.0 sha256=" + "0" * 64 + " -->\nold\n\n## My later section\nkeep me\n"
        (self.t / "AGENTS.md").write_text(broken)
        before = snapshot(self.t)
        r = run(INIT, self.t)
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline block", r.stderr)
        self.assertEqual(snapshot(self.t), before)


class BlockTest(unittest.TestCase):
    BODY = "line one\nline two\n"

    def wrap(self, body, sha=None):
        sha = sha or hashlib.sha256(body.encode("utf-8")).hexdigest()
        return "before\n<!-- baseline:begin version=0.2.0 sha256=%s -->\n%s<!-- baseline:end -->\nafter\n" % (sha, body)

    def test_find_block_reads_version_and_body_and_sees_no_edit(self):
        b = kit.find_block(self.wrap(self.BODY))
        self.assertEqual((b.version, b.body), ("0.2.0", self.BODY))
        self.assertFalse(kit.block_is_edited(b))

    def test_a_changed_body_counts_as_edited(self):
        original_hash = hashlib.sha256(self.BODY.encode("utf-8")).hexdigest()
        b = kit.find_block(self.wrap("line one\nline 2\n", sha=original_hash))
        self.assertTrue(kit.block_is_edited(b))

    def test_find_block_returns_none_without_markers(self):
        self.assertIsNone(kit.find_block("# Title\n\nNo block here.\n"))

    def test_find_block_refuses_unpaired_or_repeated_markers(self):
        good = self.wrap(self.BODY)
        cases = {
            "no end marker": good.replace("<!-- baseline:end -->\n", ""),
            "no begin marker": re.sub(r"<!-- baseline:begin[^\n]*\n", "", good),
            "two blocks": good + good,
        }
        for name, text in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(kit.BlockError):
                    kit.find_block(text)

    def test_a_crlf_block_is_not_seen_as_edited(self):
        b = kit.find_block(self.wrap(self.BODY).replace("\n", "\r\n"))
        self.assertFalse(kit.block_is_edited(b))

    def test_with_block_replaces_in_place_and_keeps_the_rest(self):
        text = "head\n\n" + kit.render_block("0.1.0") + "tail\n"
        out = kit.with_block(text, "0.2.0")
        self.assertTrue(out.startswith("head\n\n"))
        self.assertTrue(out.endswith("tail\n"))
        self.assertEqual(kit.find_block(out).version, "0.2.0")
        self.assertEqual(out.count("baseline:begin"), 1)


if __name__ == "__main__":
    unittest.main()
