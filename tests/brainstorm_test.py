"""baseline-brainstorm's next_number.py: the five-digit number a new desired-state file gets."""
import unittest

from helpers import TempRepoCase, run, skill_dir, snapshot

NEXT = skill_dir("baseline-brainstorm") / "scripts" / "next_number.py"


class NextNumberTest(TempRepoCase):
    def folder(self):
        d = self.t / "baseline" / "desired-state"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def number(self):
        r = run(NEXT, self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def test_the_first_file_is_00001_even_without_a_baseline_folder(self):
        self.assertEqual(self.number(), "00001")

    def test_it_is_the_highest_number_plus_one_whatever_the_gaps(self):
        d = self.folder()
        for name in ("00001-a.md", "00007-b.md", "00003-c.md"):
            (d / name).write_text("x")
        self.assertEqual(self.number(), "00008")

    def test_names_that_do_not_start_with_five_digits_and_a_dash_are_ignored(self):
        d = self.folder()
        for name in ("notes.md", "1-short.md", "0000a-x.md", "000009-six.md"):
            (d / name).write_text("x")
        self.assertEqual(self.number(), "00001")

    def test_a_folder_with_a_number_counts_so_a_number_is_never_reused(self):
        (self.folder() / "00009-old-layout").mkdir()
        self.assertEqual(self.number(), "00010")

    def test_it_writes_nothing(self):
        (self.folder() / "00002-a.md").write_text("x")
        before = snapshot(self.t)
        self.number()
        self.assertEqual(snapshot(self.t), before)

    def test_a_missing_repo_exits_2(self):
        r = run(NEXT, self.t / "nope")
        self.assertEqual(r.returncode, 2)
        self.assertIn("nope", r.stderr)


if __name__ == "__main__":
    unittest.main()
