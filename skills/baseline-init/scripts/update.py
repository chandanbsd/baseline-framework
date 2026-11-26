#!/usr/bin/env python3
"""Bring a repository from its baseline_version to the installed version of the skills.

Usage:
  update.py plan   <repo>                              the next pending migration with its dry run, the later ones by name,
                                                       and the state of the owned AGENTS.md block
  update.py apply  <repo> <migration-id> [--dry-run]   apply the next pending migration, then move baseline_version
  update.py finish <repo> [--discard-edits] [--dry-run]  replace the owned AGENTS.md block, then move baseline_version
Options on every command: --installed-version V and --migrations-dir DIR (both exist for tests).

Exit codes: 0 ok; 1 a migration failed; 2 refused (not initialised, out of order, migrations pending, unreadable
baseline_version, AGENTS.md markers that do not form exactly one block); 3 the repo is newer than the installed
skills; 4 the owned block was edited and --discard-edits was not given.
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
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
# baseline_version: 0.2.0   also "0.2.0", '0.2.0', a trailing # comment, and CRLF line endings.
CURRENT_RE = re.compile(r"^(baseline_version:[ \t]*[\"']?)(\S+?)([\"']?)([ \t]*(?:#[^\r\n]*)?)(\r?)$", re.M)


@dataclass
class Migration:
    id: str
    frm: str
    to: str
    dir: Path

    @property
    def script(self) -> Path:
        return self.dir / "migrate.py"


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
    m = CURRENT_RE.search(kit.read_text(path))
    if not m:
        raise Stop("baseline.yml has no baseline_version line", 2)
    if not SEMVER_RE.match(m.group(2)):
        raise Stop("baseline_version must look like 1.2.3 (found %r)" % m.group(2), 2)
    return m.group(2)


def write_current(repo: Path, version: str) -> None:
    path = repo / "baseline.yml"
    text = CURRENT_RE.sub(lambda m: m.group(1) + version + m.group(3) + m.group(4) + m.group(5), kit.read_text(path), count=1)
    kit.write_text(path, text)


def check_not_newer(current: str, installed: str) -> None:
    if vtuple(current) > vtuple(installed):
        raise Stop("the repo is at %s, newer than the installed skills (%s); update the skills first" % (current, installed), 3)


def scan(current: str, installed: str, migrations_dir: Path) -> Tuple[List[Migration], List[str]]:
    """Pending migrations in order, and the names of in-range folders that have no migrate.py."""
    found, ignored = [], []
    if migrations_dir.is_dir():
        for d in sorted(migrations_dir.iterdir()):
            m = MIGRATION_NAME_RE.match(d.name)
            if not (d.is_dir() and m):
                continue
            frm, to = m.groups()
            if not (vtuple(frm) >= vtuple(current) and vtuple(to) <= vtuple(installed)):
                continue
            if (d / "migrate.py").is_file():
                found.append(Migration(d.name, frm, to, d))
            else:
                ignored.append(d.name)
    return sorted(found, key=lambda mig: vtuple(mig.frm)), ignored


def read_block(repo: Path) -> Optional[kit.Block]:
    path = repo / "AGENTS.md"
    if not path.exists():
        return None
    try:
        return kit.find_block(kit.read_text(path))
    except kit.BlockError as error:
        raise Stop("AGENTS.md: %s" % error, 2)


def block_status(repo: Path, installed: str) -> str:
    block = read_block(repo)
    if block is None:
        return "missing"
    if kit.block_is_edited(block):
        return "edited"
    return "unchanged" if block.version == installed else "outdated"


def run_migration(migration: Migration, repo: Path, mode: str) -> Tuple[int, str, str]:
    r = subprocess.run([sys.executable, str(migration.script), str(repo), mode], capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace"), r.stderr.decode("utf-8", errors="replace")


def print_indented(text: str) -> None:
    for line in text.splitlines():
        print("  " + line)


def cmd_plan(repo: Path, installed: str, migrations_dir: Path) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    print("current %s" % current)
    print("installed %s" % installed)
    pending, ignored = scan(current, installed, migrations_dir)
    failed = False
    for index, migration in enumerate(pending):
        print("%smigration %s" % ("" if index == 0 else "then ", migration.id))
        if (migration.dir / "MIGRATION.md").is_file():
            print("  instructions: %s/MIGRATION.md" % migration.id)
        if index == 0:  # later migrations are dry-run after the earlier ones are applied
            code, out, err = run_migration(migration, repo, "--dry-run")
            print_indented(out)
            if code != 0:
                failed = True
                print("  dry run failed:")
                print_indented(err)
    for name in ignored:
        print("ignored %s: no migrate.py" % name)
    status = block_status(repo, installed)
    print("owned AGENTS.md block: %s" % status)
    if failed:
        return 1
    if not pending and current == installed and status == "unchanged":
        print("up to date")
    return 0


def cmd_apply(repo: Path, migration_id: str, installed: str, migrations_dir: Path, dry_run: bool) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    pending, _ = scan(current, installed, migrations_dir)
    if not pending or pending[0].id != migration_id:
        raise Stop("%s is not the next pending migration (next: %s)" % (migration_id, pending[0].id if pending else "none"), 2)
    migration = pending[0]
    if dry_run:
        print("would apply %s" % migration.id)
        code, out, err = run_migration(migration, repo, "--dry-run")
        print_indented(out)
        if code != 0:
            print_indented(err)
        return 0 if code == 0 else 1
    code, out, err = run_migration(migration, repo, "--confirm")
    sys.stdout.write(out)
    if code != 0:
        sys.stderr.write(err)
        raise Stop("migration %s failed (exit %d); baseline_version stays %s" % (migration.id, code, current), 1)
    write_current(repo, migration.to)
    print("applied %s; baseline_version is now %s" % (migration.id, migration.to))
    return 0


def cmd_finish(repo: Path, installed: str, migrations_dir: Path, discard_edits: bool, dry_run: bool) -> int:
    current = read_current(repo)
    check_not_newer(current, installed)
    pending, _ = scan(current, installed, migrations_dir)
    if pending:
        raise Stop("migrations pending: %s" % ", ".join(m.id for m in pending), 2)
    block = read_block(repo)
    if block and kit.block_is_edited(block) and not discard_edits:
        raise Stop("the AGENTS.md block was edited; run again with --discard-edits to replace it, or leave it as it is", 4)
    if dry_run:
        print("would replace the AGENTS.md block and set baseline_version to %s" % installed)
        return 0
    path = repo / "AGENTS.md"
    text = kit.read_text(path) if path.exists() else ""
    kit.write_text(path, kit.with_block(text, installed))
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
    apply_.add_argument("--dry-run", action="store_true", help="show the migration's dry run and change nothing")
    finish = sub.add_parser("finish", parents=[common], help="replace the owned block and move the version")
    finish.add_argument("repo", type=Path)
    finish.add_argument("--discard-edits", action="store_true", help="replace the AGENTS.md block even if it was edited")
    finish.add_argument("--dry-run", action="store_true", help="say what would happen and change nothing")
    args = parser.parse_args(argv)

    installed = args.installed_version or kit.installed_version()
    migrations_dir = args.migrations_dir or (kit.SKILL_DIR / "migrations")
    try:
        if args.command == "plan":
            return cmd_plan(args.repo, installed, migrations_dir)
        if args.command == "apply":
            return cmd_apply(args.repo, args.migration_id, installed, migrations_dir, args.dry_run)
        return cmd_finish(args.repo, installed, migrations_dir, args.discard_edits, args.dry_run)
    except Stop as stop:
        print("error: %s" % stop, file=sys.stderr)
        return stop.code


if __name__ == "__main__":
    sys.exit(main())
