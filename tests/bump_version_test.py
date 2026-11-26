"""tools/bump_version.py moves all four skills to one version and touches nothing else."""
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT, run, snapshot

TOOL = ROOT / "tools" / "bump_version.py"
NAMES = ["baseline-desired-state", "baseline-documentation", "baseline-refactor", "baseline-init"]


def read_version(root: Path, name: str) -> str:
    text = (root / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    return re.search(r'^  version: "([^"]+)"$', text, re.M).group(1)


class BumpVersionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        shutil.copytree(ROOT / "skills", self.tmp / "skills")

    def versions(self):
        return {read_version(self.tmp, n) for n in NAMES}

    def test_bumps_all_four_and_changes_only_the_version_line(self):
        before = {n: (self.tmp / "skills" / n / "SKILL.md").read_text(encoding="utf-8") for n in NAMES}
        r = run(TOOL, "0.3.1", "--root", self.tmp)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.versions(), {"0.3.1"})
        self.assertEqual(r.stdout.count("updated "), 4)
        for n in NAMES:
            after = (self.tmp / "skills" / n / "SKILL.md").read_text(encoding="utf-8")
            self.assertEqual(after, before[n].replace('version: "0.2.0"', 'version: "0.3.1"'))

    def test_rejects_a_bad_version_and_changes_nothing(self):
        before = snapshot(self.tmp)
        for bad in ["v1", "1.2", "1.2.3.4", "1.2.x"]:
            with self.subTest(version=bad):
                r = run(TOOL, bad, "--root", self.tmp)
                self.assertEqual(r.returncode, 2)
                self.assertIn(bad, r.stderr)  # the error names the bad input
                self.assertEqual(snapshot(self.tmp), before)

    def test_second_run_is_a_no_op(self):
        run(TOOL, "0.3.1", "--root", self.tmp)
        r = run(TOOL, "0.3.1", "--root", self.tmp)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("updated", r.stdout)

    def test_a_version_looking_line_in_the_body_is_left_alone(self):
        path = self.tmp / "skills" / "baseline-init" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + '\n  version: "0.2.0"\n', encoding="utf-8")
        r = run(TOOL, "0.3.1", "--root", self.tmp)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(read_version(self.tmp, "baseline-init"), "0.3.1")
        self.assertTrue(path.read_text(encoding="utf-8").endswith('\n  version: "0.2.0"\n'))


if __name__ == "__main__":
    unittest.main()
