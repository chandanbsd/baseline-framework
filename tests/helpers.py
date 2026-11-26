"""Shared helpers for the baseline package tests (standard library only)."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Skill:
    name: str
    description: str
    compatibility: str
    version: str
    body: str
    dir: Path


def skill_dir(name: str) -> Path:
    return ROOT / "skills" / name


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def read_skill(name: str) -> Skill:
    """Parse skills/<name>/SKILL.md: simple `key: value` lines plus one indented `metadata:` map."""
    directory = skill_dir(name)
    lines = (directory / "SKILL.md").read_text(encoding="utf-8").splitlines()
    assert lines and lines[0] == "---", "SKILL.md must start with a --- line"
    end = lines.index("---", 1)
    fields: Dict[str, str] = {}
    metadata: Dict[str, str] = {}
    in_metadata = False
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line[0] in " \t":
            if in_metadata:
                key, _, value = line.strip().partition(":")
                metadata[key.strip()] = _unquote(value)
            continue
        key, _, value = line.partition(":")
        in_metadata = key.strip() == "metadata" and not value.strip()
        if not in_metadata:
            fields[key.strip()] = _unquote(value)
    return Skill(
        name=fields.get("name", ""),
        description=fields.get("description", ""),
        compatibility=fields.get("compatibility", ""),
        version=metadata.get("version", ""),
        body="\n".join(lines[end + 1:]),
        dir=directory,
    )


def run(script: Path, *args: str, cwd: Optional[Path] = None) -> subprocess.CompletedProcess:
    """Run a script the way an agent would: a command line, captured text output, never raises."""
    return subprocess.run(
        [sys.executable, str(script), *[str(a) for a in args]],
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )


def snapshot(root: Path) -> Dict[str, bytes]:
    """Every file under root, keyed by relative path, for before/after comparisons."""
    return {str(p.relative_to(root)): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class TempRepoCase(unittest.TestCase):
    """A test case whose self.t is a fresh empty directory, removed afterwards."""

    def setUp(self):
        self.t = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.t)
