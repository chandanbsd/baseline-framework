#!/usr/bin/env python3
"""Set up a repository for the baseline.

Usage: init.py <target> [--dry-run]
Prints one line per action: create <path>, append AGENTS.md, update AGENTS.md or keep <path>.
Never overwrites a file. Exits 2 when the target is not a directory or already holds baseline.yml.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

import kit

NEW_AGENTS_MD = "# Instructions for working in this repository\n"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Set up a repository for the baseline.")
    parser.add_argument("target", type=Path, help="the repository to set up")
    parser.add_argument("--dry-run", action="store_true", help="print what would happen and write nothing")
    args = parser.parse_args(argv)
    target = args.target
    if not target.is_dir():
        print("error: %s is not a directory" % target, file=sys.stderr)
        return 2
    if (target / "baseline.yml").exists():
        print("error: %s is already initialised (baseline.yml exists); use the update mode" % target, file=sys.stderr)
        return 2

    version = kit.installed_version()
    writes = []  # (relative path, content)

    agents = target / "AGENTS.md"
    if agents.exists():
        current = agents.read_text(encoding="utf-8")
        verb = "update" if kit.find_block(current) else "append"
    else:
        current, verb = NEW_AGENTS_MD, "create"
    print("%s AGENTS.md" % verb)
    writes.append(("AGENTS.md", kit.with_block(current, version)))

    for rel, content in kit.kit_files(version).items():
        if (target / rel).exists():
            print("keep %s" % rel)
        else:
            print("create %s" % rel)
            writes.append((rel, content))

    if args.dry_run:
        print("dry run: nothing written")
        return 0
    for rel, content in writes:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
