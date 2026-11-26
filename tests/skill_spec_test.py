"""The four baseline skills must follow the Agent Skills rules the design pins."""
import re
import unittest

from helpers import ROOT, read_skill

NAMES = {"baseline-desired-state", "baseline-documentation", "baseline-refactor", "baseline-init"}
PATH_RE = re.compile(r"`((?:scripts|assets|references|migrations)/[^`<>\s]*)`")


def all_skills():
    return [read_skill(n) for n in sorted(NAMES)]


class SkillSpecTest(unittest.TestCase):
    def test_exactly_four_skills(self):
        found = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
        self.assertEqual(found, NAMES)

    def test_name_and_description_rules(self):
        for s in all_skills():
            with self.subTest(skill=s.name):
                self.assertRegex(s.name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
                self.assertLessEqual(len(s.name), 64)
                self.assertEqual(s.name, s.dir.name)
                self.assertTrue(1 <= len(s.description) <= 1024)

    def test_description_is_safe_plain_yaml(self):
        # A strict YAML parser rejects ": " or " #" inside a plain scalar and the skill would not load.
        for s in all_skills():
            with self.subTest(skill=s.name):
                self.assertNotIn(": ", s.description)
                self.assertNotIn(" #", s.description)

    def test_body_under_500_lines(self):
        for s in all_skills():
            with self.subTest(skill=s.name):
                self.assertLess(len(s.body.splitlines()), 500)

    def test_one_version_everywhere(self):
        self.assertEqual({s.version for s in all_skills()}, {"0.2.0"})

    def test_scripts_declare_python(self):
        for s in all_skills():
            if (s.dir / "scripts").is_dir():
                with self.subTest(skill=s.name):
                    self.assertIn("Python 3.9", s.compatibility)

    def test_referenced_paths_exist(self):
        for s in all_skills():
            for path in PATH_RE.findall(s.body):
                with self.subTest(skill=s.name, path=path):
                    self.assertTrue((s.dir / path).exists())

    def test_references_one_level_deep(self):
        for s in all_skills():
            nested = [d for d in (s.dir / "references").glob("*") if d.is_dir()]
            with self.subTest(skill=s.name):
                self.assertEqual(nested, [])

    def test_skills_share_nothing(self):
        for s in all_skills():
            for f in sorted(p for p in s.dir.rglob("*") if p.is_file()):
                text = f.read_text(encoding="utf-8")
                with self.subTest(file=str(f.relative_to(ROOT))):
                    self.assertNotIn("../", text)
                    self.assertNotIn("skills/baseline-", text)


if __name__ == "__main__":
    unittest.main()
