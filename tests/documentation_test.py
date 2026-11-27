"""baseline-documentation: its covers.py helper, and its references matching the families init asks about."""
import re
import sys
import unittest

from helpers import TempRepoCase, run, skill_dir, snapshot

sys.path.insert(0, str(skill_dir("baseline-init") / "scripts"))
import kit  # noqa: E402

DOC = skill_dir("baseline-documentation")
COVERS = DOC / "scripts" / "covers.py"
REQUIRED_RE = re.compile(r"^## Required sections\n\n((?:- `#{1,3} [^`]+`[^\n]*\n)+)", re.M)


class ReferencesTest(unittest.TestCase):
    def test_each_family_init_asks_about_has_a_reference_file(self):
        for family in kit.FAMILIES:
            with self.subTest(family=family):
                self.assertTrue((DOC / "references" / ("%s.md" % family)).is_file())

    def test_each_reference_lists_its_required_sections_as_exact_headings(self):
        for family in kit.FAMILIES:
            path = DOC / "references" / ("%s.md" % family)
            with self.subTest(family=family):
                self.assertTrue(path.is_file())
                match = REQUIRED_RE.search(path.read_text(encoding="utf-8"))
                self.assertIsNotNone(match, "no '## Required sections' list of backticked headings")
                headings = re.findall(r"^- `(#{1,3} [^`]+)`", match.group(1), re.M)
                self.assertGreaterEqual(len(headings), 1)

    def test_the_flags_reference_names_every_kind_the_skill_can_write(self):
        text = (DOC / "references" / "flags.md").read_text(encoding="utf-8")
        for kind in ("empty-family", "stale-doc", "breaks-rule", "inferred-reason",
                     "overlap", "command-failed", "not-backed", "link-readme"):
            with self.subTest(kind=kind):
                self.assertIn("`%s`" % kind, text)


class CoversTest(TempRepoCase):
    def docs(self):
        d = self.t / "baseline" / "docs"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def listing(self):
        r = run(COVERS, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.splitlines()

    def test_lists_each_documents_covers_line_in_path_order(self):
        d = self.docs()
        (d / "README.md").write_text("# Title\ncovers: the whole repository\n\n## What this is\n")
        (d / "course").mkdir()
        (d / "course" / "01-order.md").write_text("# Order\ncovers: order creation, from POST /orders to the email\n")
        self.assertEqual(
            self.listing(),
            [
                "baseline/docs/README.md\tthe whole repository",
                "baseline/docs/course/01-order.md\torder creation, from POST /orders to the email",
            ],
        )

    def test_a_document_without_a_covers_line_is_listed_as_missing(self):
        (self.docs() / "a.md").write_text("# A\n\nNo covers line here.\n")
        self.assertEqual(self.listing(), ["baseline/docs/a.md\t(no covers line)"])

    def test_an_empty_covers_line_counts_as_missing(self):
        (self.docs() / "a.md").write_text("# A\ncovers:   \n")
        self.assertEqual(self.listing(), ["baseline/docs/a.md\t(no covers line)"])

    def test_only_the_first_ten_lines_count(self):
        (self.docs() / "a.md").write_text("# A\n" + "\n" * 10 + "covers: too far down\n")
        self.assertEqual(self.listing(), ["baseline/docs/a.md\t(no covers line)"])

    def test_crlf_files_are_read(self):
        (self.docs() / "a.md").write_bytes(b"# A\r\ncovers: crlf text\r\n")
        self.assertEqual(self.listing(), ["baseline/docs/a.md\tcrlf text"])

    def test_an_unreadable_file_is_listed_not_crashed_on(self):
        (self.docs() / "a.md").write_bytes(b"# A\ncovers: caf\xe9\n")
        self.assertEqual(self.listing(), ["baseline/docs/a.md\t(unreadable)"])

    def test_only_markdown_under_baseline_docs_counts(self):
        d = self.docs()
        (d / "notes.txt").write_text("covers: not markdown\n")
        (self.t / "docs").mkdir()
        (self.t / "docs" / "other.md").write_text("# Other\ncovers: not ours\n")
        self.assertEqual(self.listing(), [])

    def test_no_docs_folder_prints_nothing_and_succeeds(self):
        self.assertEqual(self.listing(), [])

    def test_it_writes_nothing(self):
        (self.docs() / "a.md").write_text("# A\ncovers: x\n")
        before = snapshot(self.t)
        self.listing()
        self.assertEqual(snapshot(self.t), before)

    def test_a_missing_repo_exits_2(self):
        r = run(COVERS, self.t / "nope")
        self.assertEqual(r.returncode, 2)
        self.assertIn("nope", r.stderr)


if __name__ == "__main__":
    unittest.main()
