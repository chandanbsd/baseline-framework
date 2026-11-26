#!/usr/bin/env python3
"""Bring a repository from its baseline_version to the installed version of the skills.

Usage:
  update.py plan   <repo>                    show the pending migrations (each with its dry run) and the owned block's state
  update.py apply  <repo> <migration-id>     apply the next pending migration, then move baseline_version
  update.py finish <repo> [--discard-edits]  replace the owned AGENTS.md block, then move baseline_version to the installed version
Options on every command: --installed-version V and --migrations-dir DIR (both exist for tests).

Exit codes: 0 ok; 1 a migration failed; 2 refused (not initialised, out of order, migrations pending);
3 the repo is newer than the installed skills; 4 the owned block was edited and --discard-edits was not given.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

import kit

MIGRATION_NAME_RE = re.compile(r"^(\d+\.\d+\.\d+)-to-(\d+\.\d+\.\d+)$")
CURRENT_RE = re.compile(r"^baseline_version:[ \t]*(\S+)[ \t]*$", re.M)


@dataclass
class Migration:
    id: str
    frm: str
    to: str
    script: Path


class Stop(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code


def vtuple(version: str) -> Tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def read_current(repo: Path) -> str:
    path = repo / "baseline.yml"
    if not path.exists():
        raise Stop("%s has no baseline.yml; run init first" % repo, 2)
    m = CURRENT_RE.search(path.read_text(encoding="utf-8"))
    if not m:
        raise Stop("baseline.yml has no baseline_version line", 2)
    return m.group(1)


def write_current(repo: Path, version: str) -> None:
    path = repo / "baseline.yml"
    path.write_text(CURRENT_RE.sub("baseline_version: %s" % version, path.read_text(encoding="utf-8"), count=1), encoding="utf-8")


def check_not_newer(current: str, installed: str) -> None:
    if vtuple(current) > vtuple(installed):
        raise Stop("the repo is at %s, newer than the installed skills (%s); update the skills first" % (current, installed), 3)


def list_pending(current: str, installed: str, migrations_dir: Path) -> List[Migration]:
    found = []
    if migrations_dir.is_dir():
        for d in migrations_dir.iterdir():
            m = MIGRATION_NAME_RE.match(d.name)
            if d.is_dir() and m and (d / "migrate.py").is_file():
                frm, to = m.groups()
                if vtuple(frm) >= vtuple(current) and vtuple(to) <= vtuple(installed):
                    found.append(Migration(d.name, frm, to, d / "migrate.py"))
    return sorted(found, key=lambda mig: vtuple(mig.frm))


def block_status(repo: Path, installed: str) -> str:
    path = repo / "AGENTS.md"
    block = kit.find_block(path.read_text(encoding="utf-8")) if path.exists() else None
    if block is None:
        return "missing"
    if kit.block_is_edited(block):
        return "edited"
    return "unchanged" if block.version == installed else "outdated"


def run_migration(migration: Migration, repo: Path, mode: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(migration.script), str(repo), mode], capture_output=True, text=True)


def cmd_plan(repo: Path, installed: str, migrations_dir: Path) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    print("current %s" % current)
    print("installed %s" % installed)
    pending = list_pending(current, installed, migrations_dir)
    failed = False
    for migration in pending:
        print("migration %s" % migration.id)
        r = run_migration(migration, repo, "--dry-run")
        for line in r.stdout.splitlines():
            print("  " + line)
        if r.returncode != 0:
            failed = True
            print("  dry run failed:")
            for line in r.stderr.splitlines():
                print("  " + line)
    status = block_status(repo, installed)
    print("owned AGENTS.md block: %s" % status)
    if failed:
        return 1
    if not pending and current == installed and status == "unchanged":
        print("up to date")
    return 0


def cmd_apply(repo: Path, migration_id: str, installed: str, migrations_dir: Path) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    pending = list_pending(current, installed, migrations_dir)
    if not pending or pending[0].id != migration_id:
        raise Stop("%s is not the next pending migration (next: %s)" % (migration_id, pending[0].id if pending else "none"), 2)
    migration = pending[0]
    r = run_migration(migration, repo, "--confirm")
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise Stop("migration %s failed (exit %d); baseline_version stays %s" % (migration.id, r.returncode, current), 1)
    write_current(repo, migration.to)
    print("applied %s; baseline_version is now %s" % (migration.id, migration.to))
    return 0


def cmd_finish(repo: Path, installed: str, migrations_dir: Path, discard_edits: bool) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    pending = list_pending(current, installed, migrations_dir)
    if pending:
        raise Stop("migrations pending: %s" % ", ".join(m.id for m in pending), 2)
    path = repo / "AGENTS.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    block = kit.find_block(text)
    if block and kit.block_is_edited(block) and not discard_edits:
        raise Stop("the AGENTS.md block was edited; run again with --discard-edits to replace it, or leave it as it is", 4)
    path.write_text(kit.with_block(text, installed), encoding="utf-8")
    write_current(repo, installed)
    print("replaced the AGENTS.md block; baseline_version is now %s" % installed)
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--installed-version", default=None, help="override the installed version (for tests)")
    common.add_argument("--migrations-dir", type=Path, default=None, help="override the migrations folder (for tests)")
    parser = argparse.ArgumentParser(description="Bring a repository to the installed baseline version.")
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan", parents=[common], help="show what an update would do")
    plan.add_argument("repo", type=Path)
    apply_ = sub.add_parser("apply", parents=[common], help="apply the next pending migration")
    apply_.add_argument("repo", type=Path)
    apply_.add_argument("migration_id")
    finish = sub.add_parser("finish", parents=[common], help="replace the owned block and move the version")
    finish.add_argument("repo", type=Path)
    finish.add_argument("--discard-edits", action="store_true", help="replace the AGENTS.md block even if it was edited")
    args = parser.parse_args(argv)

    installed = args.installed_version or kit.installed_version()
    migrations_dir = args.migrations_dir or (kit.SKILL_DIR / "migrations")
    try:
        if args.command == "plan":
            return cmd_plan(args.repo, installed, migrations_dir)
        if args.command == "apply":
            return cmd_apply(args.repo, args.migration_id, installed, migrations_dir)
        return cmd_finish(args.repo, installed, migrations_dir, args.discard_edits)
    except Stop as stop:
        print("error: %s" % stop, file=sys.stderr)
        return stop.code


if __name__ == "__main__":
    sys.exit(main())
