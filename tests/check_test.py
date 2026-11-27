"""The check that init copies to baseline/check.py: what CI runs over baseline/ and nothing else."""
import shutil
import stat
import tempfile
import unittest
from pathlib import Path

from helpers import TempRepoCase, run, skill_dir, snapshot

CHECK = skill_dir("baseline-init") / "assets" / "kit" / "baseline" / "check.py"
FAMILIES = ("readme", "architecture", "course", "features", "deployment", "reference")

# A valid document for each place, built from the required headings of the family's reference.
DOCS = {
    "README.md": ["## What this is", "## Prerequisites", "## Get it running", "## Repo map", "## Configuration", "## Troubleshooting"],
    "architecture/README.md": ["## What the system is", "## Big picture", "## Components", "## Key flows"],
    "course/README.md": ["## Chapters"],
    "course/01-order.md": ["## The flow", "## Walkthrough", "## Alternatives and why this one", "## Pitfalls and failure modes", "## Practice"],
    "features/README.md": ["## Features"],
    "features/refunds.md": ["## What it is and why", "## Who can use it", "## What a person can do", "## When things go wrong"],
    "deploy/README.md": ["## Topology", "## Environments", "## Configuration and secrets", "## Pipeline", "## Deploying and rolling back", "## Troubleshooting"],
    "reference/glossary.md": ["## Terms"],
    "reference/file-map.md": ["## Folders"],
}
FLOW = "```mermaid\nflowchart LR\n    A --> B\n```\n"
# Shell built-ins only, because the test gives the check a PATH that holds nothing but this file.
FAKE_MMDC = """#!/bin/sh
while [ $# -gt 0 ]; do
  if [ "$1" = "-i" ]; then input="$2"; fi
  shift
done
while IFS= read -r line; do
  case "$line" in *BROKEN*) echo "Parse error on line 2" >&2; exit 1;; esac
done < "$input"
exit 0
"""


class CheckTest(TempRepoCase):
    def setUp(self):
        super().setUp()
        self.empty_bin = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.empty_bin)
        self.env = {"PATH": str(self.empty_bin)}  # no renderer on the PATH unless a test puts one there

    def baseline_yml(self, skipped=""):
        path = self.t / "baseline" / "baseline.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("baseline_version: 0.2.0\ndocuments_skipped: [%s]\n" % skipped)

    def doc(self, rel, headings, extra=""):
        path = self.t / "baseline" / "docs" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Title\ncovers: x\n\n" + "".join("%s\ntext\n\n" % h for h in headings) + extra)

    def all_docs(self):
        for rel, headings in DOCS.items():
            self.doc(rel, headings)

    def check(self, *args, env=None):
        return run(CHECK, self.t, *args, env=self.env if env is None else env)

    def with_fake_renderer(self):
        bin_dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, bin_dir)
        mmdc = bin_dir / "mmdc"
        mmdc.write_text(FAKE_MMDC)
        mmdc.chmod(mmdc.stat().st_mode | stat.S_IEXEC)
        return {"PATH": str(bin_dir)}

    def test_there_is_nothing_to_check_without_baseline_yml(self):
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("nothing to check", r.stdout)

    def test_a_fresh_repo_passes_with_a_notice_for_each_needed_family(self):
        self.baseline_yml()
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for family in FAMILIES:
            self.assertIn("not yet documented: %s" % family, r.stdout)

    def test_a_skipped_family_gets_no_notice(self):
        self.baseline_yml("deployment, reference")
        r = self.check()
        self.assertNotIn("not yet documented: deployment", r.stdout)
        self.assertNotIn("not yet documented: reference", r.stdout)
        self.assertIn("not yet documented: readme", r.stdout)

    def test_a_complete_set_passes_clean(self):
        self.baseline_yml()
        self.all_docs()
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("not yet documented", r.stdout)
        self.assertIn("0 errors", r.stdout)

    def test_a_missing_required_section_fails_and_names_it(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"][:-1])
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("baseline/docs/README.md", r.stdout)
        self.assertIn('"## Troubleshooting"', r.stdout)

    def test_a_heading_inside_a_code_fence_does_not_count(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"][:-1], extra="```\n## Troubleshooting\n```\n")
        self.assertEqual(self.check().returncode, 1)

    def test_a_course_index_and_a_chapter_have_their_own_required_sections(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("course/README.md", [])
        self.doc("course/01-order.md", DOCS["course/01-order.md"][:-1])
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("baseline/docs/course/README.md", r.stdout)
        self.assertIn('"## Chapters"', r.stdout)
        self.assertIn("baseline/docs/course/01-order.md", r.stdout)
        self.assertIn('"## Practice"', r.stdout)

    def test_a_feature_page_is_checked_but_users_and_access_is_not(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("features/users-and-access.md", ["## Users and access"])
        self.assertEqual(self.check().returncode, 0)
        self.doc("features/refunds.md", ["## What it is and why"])
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn('"## Who can use it"', r.stdout)

    def test_an_empty_family_flag_fails_until_the_family_is_skipped_or_written(self):
        self.baseline_yml()
        flags = self.t / "baseline" / "flags"
        flags.mkdir()
        (flags / "empty-family-deployment.md").write_text("# Nothing deploys\nkind: empty-family\nabout: deployment\n\nText.\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("empty-family", r.stdout)
        self.assertIn("deployment", r.stdout)
        self.baseline_yml("deployment")
        self.assertEqual(self.check().returncode, 0)
        self.baseline_yml()
        self.doc("deploy/README.md", DOCS["deploy/README.md"])
        self.assertEqual(self.check().returncode, 0)

    def test_a_flag_of_another_kind_does_not_fail(self):
        self.baseline_yml()
        flags = self.t / "baseline" / "flags"
        flags.mkdir()
        (flags / "stale-doc-readme.md").write_text("# Old\nkind: stale-doc\nabout: baseline/docs/README.md\n")
        self.assertEqual(self.check().returncode, 0)

    def test_an_unknown_name_in_documents_skipped_fails(self):
        self.baseline_yml("deploy")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("'deploy'", r.stdout)

    def test_documents_skipped_may_be_a_block_list(self):
        (self.t / "baseline").mkdir()
        (self.t / "baseline" / "baseline.yml").write_text("baseline_version: 0.2.0\ndocuments_skipped:\n  - deployment\n")
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("not yet documented: deployment", r.stdout)

    def test_a_broken_link_between_baseline_documents_fails(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="[x](architecture/missing.md)\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("architecture/missing.md", r.stdout)

    def test_good_links_pass_including_a_fragment_and_a_folder(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="[a](architecture/README.md#big-picture) [b](course/) ![c](../baseline.yml)\n")
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_links_to_code_urls_anchors_and_mail_are_not_checked(self):
        self.baseline_yml()
        self.all_docs()
        extra = "[c](../../src/gone.py) [u](https://example.com/x) [a](#top) [m](mailto:a@b.c) [r](/src/gone.py)\n"
        self.doc("README.md", DOCS["README.md"], extra=extra)
        self.assertEqual(self.check().returncode, 0)

    def test_links_inside_code_are_ignored(self):
        self.baseline_yml()
        self.all_docs()
        extra = "`[x](nope.md)`\n\n```\n[y](nope.md)\n```\n"
        self.doc("README.md", DOCS["README.md"], extra=extra)
        self.assertEqual(self.check().returncode, 0)

    def test_a_missing_folder_link_fails(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="[f](nope/)\n")
        self.assertEqual(self.check().returncode, 1)

    def test_well_formed_mermaid_blocks_pass(self):
        self.baseline_yml()
        self.all_docs()
        blocks = "".join(
            "```mermaid\n%s\n```\n\n" % body
            for body in (
                "flowchart LR\n    A --> B",
                "graph TD\n    A --> B",
                "sequenceDiagram\n    A->>B: hi",
                "erDiagram\n    A ||--o{ B : has",
                "stateDiagram-v2\n    [*] --> A",
                "%%{init: {'theme': 'dark'}}%%\nflowchart LR\n    A --> B",
                "---\ntitle: T\n---\nflowchart LR\n    A --> B",
            )
        )
        self.doc("README.md", DOCS["README.md"], extra=blocks)
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_an_empty_mermaid_block_fails(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="```mermaid\n```\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("empty", r.stdout)

    def test_an_unknown_diagram_type_fails(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="```mermaid\nnot a diagram\n```\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("baseline/docs/README.md", r.stdout)
        self.assertIn("not a diagram", r.stdout)

    def test_an_unclosed_fence_fails(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="```mermaid\nflowchart LR\n    A --> B\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("unclosed", r.stdout)

    def test_mermaid_is_checked_in_every_baseline_document_not_only_docs(self):
        self.baseline_yml()
        folder = self.t / "baseline" / "desired-state"
        folder.mkdir()
        (folder / "00001-x.md").write_text("# X\n\n```mermaid\nnot a diagram\n```\n")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("baseline/desired-state/00001-x.md", r.stdout)

    def test_without_a_renderer_a_notice_says_the_blocks_were_not_rendered(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra=FLOW)
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("not rendered", r.stdout)

    def test_no_notice_when_there_are_no_mermaid_blocks(self):
        self.baseline_yml()
        self.all_docs()
        self.assertNotIn("not rendered", self.check().stdout)

    def test_a_renderer_that_accepts_the_blocks_passes_and_says_how_many_it_rendered(self):
        # A passing CI log must show that rendering happened, not only that nothing failed.
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra=FLOW + "\n" + FLOW)
        r = self.check(env=self.with_fake_renderer())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("not rendered", r.stdout)
        self.assertIn("rendered 2 block(s) with mmdc", r.stdout)

    def test_the_count_leaves_out_the_blocks_that_failed_to_render(self):
        self.baseline_yml()
        self.all_docs()
        extra = FLOW + "\n```mermaid\nflowchart LR\n    BROKEN\n```\n"
        self.doc("README.md", DOCS["README.md"], extra=extra)
        r = self.check(env=self.with_fake_renderer())
        self.assertEqual(r.returncode, 1)
        self.assertIn("rendered 1 block(s) with mmdc", r.stdout)
        self.assertIn("Parse error", r.stdout)

    def test_a_renderer_error_fails_and_names_the_file(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="```mermaid\nflowchart LR\n    BROKEN\n```\n")
        r = self.check(env=self.with_fake_renderer())
        self.assertEqual(r.returncode, 1)
        self.assertIn("baseline/docs/README.md", r.stdout)
        self.assertIn("Parse error", r.stdout)

    def test_no_render_skips_the_renderer_even_when_it_is_present(self):
        self.baseline_yml()
        self.all_docs()
        self.doc("README.md", DOCS["README.md"], extra="```mermaid\nflowchart LR\n    BROKEN\n```\n")
        r = self.check("--no-render", env=self.with_fake_renderer())
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_documents_outside_baseline_are_never_read(self):
        self.baseline_yml()
        (self.t / "docs").mkdir()
        (self.t / "docs" / "other.md").write_text("# Other\n[x](nope.md)\n```mermaid\nnot a diagram\n```\n")
        (self.t / "README.md").write_text("# Root\n[x](nope.md)\n```\nunclosed\n")
        self.assertEqual(self.check().returncode, 0)

    def test_it_writes_nothing(self):
        self.baseline_yml()
        self.all_docs()
        before = snapshot(self.t)
        self.check()
        self.assertEqual(snapshot(self.t), before)

    def test_a_missing_repo_exits_2(self):
        r = run(CHECK, self.t / "nope", env=self.env)
        self.assertEqual(r.returncode, 2)
        self.assertIn("nope", r.stderr)

    def test_the_repo_defaults_to_the_parent_of_the_folder_that_holds_the_script(self):
        self.baseline_yml()
        self.all_docs()
        copy = self.t / "baseline" / "check.py"
        shutil.copy(CHECK, copy)
        self.assertEqual(run(copy, env=self.env).returncode, 0)
        self.doc("README.md", DOCS["README.md"][:-1])
        self.assertEqual(run(copy, env=self.env).returncode, 1)


if __name__ == "__main__":
    unittest.main()
