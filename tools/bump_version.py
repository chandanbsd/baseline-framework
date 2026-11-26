#!/usr/bin/env python3
"""Set metadata.version in every skills/*/SKILL.md, so the four skills always share one version.

Usage: bump_version.py <new_version> [--root PATH]
Prints "updated <path>" for each file it changed. Exits 2, changing nothing, on a bad version.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional

VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
VERSION_LINE_RE = re.compile(r'^([ \t]+version:[ \t]*)"?[^"\n]+"?[ \t]*$', re.M)


def bump_text(text: str, version: str) -> str:
    """Rewrite the indented version line inside the frontmatter only; the body is never touched."""
    lines = text.split("\n")
    end = lines.index("---", 1)
    head = "\n".join(lines[: end + 1])
    new_head = VERSION_LINE_RE.sub(lambda m: '%s"%s"' % (m.group(1), version), head, count=1)
    return "\n".join([new_head] + lines[end + 1:])


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Set one version across all four baseline skills.")
    parser.add_argument("version", help="the new version, for example 0.3.1")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root that holds skills/ (default: this repository)")
    args = parser.parse_args(argv)
    if not VERSION_RE.match(args.version):
        parser.error("%r is not a version like 1.2.3" % args.version)
    for path in sorted((args.root / "skills").glob("*/SKILL.md")):
        old = path.read_text(encoding="utf-8")
        new = bump_text(old, args.version)
        if new != old:
            path.write_text(new, encoding="utf-8")
            print("updated %s" % path.relative_to(args.root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
