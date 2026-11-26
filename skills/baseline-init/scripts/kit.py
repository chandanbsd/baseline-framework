"""Shared by init.py and update.py: the kit files and the baseline-owned block of AGENTS.md."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
KIT_DIR = SKILL_DIR / "assets" / "kit"
BEGIN_TOKEN = "<!-- baseline:begin"
END_TOKEN = "<!-- baseline:end -->"
BLOCK_RE = re.compile(
    r"<!-- baseline:begin version=(\S+) sha256=([0-9a-f]{64}) -->\r?\n(.*?)<!-- baseline:end -->(?:\r?\n)?", re.S
)
VERSION_RE = re.compile(r'^[ \t]+version:[ \t]*"?([^"\n]+?)"?[ \t]*$', re.M)


class BlockError(Exception):
    """The baseline markers in a file do not form exactly one complete block."""


@dataclass
class Block:
    start: int
    end: int
    version: str
    sha256: str
    body: str  # line endings normalised to LF, so the hash does not depend on the file's endings


def read_text(path: Path) -> str:
    """Read a file keeping its line endings exactly as they are."""
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def write_text(path: Path, text: str) -> None:
    """Write text without translating line endings."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def installed_version() -> str:
    """The version this skill was installed at: metadata.version in its own SKILL.md."""
    return VERSION_RE.search(read_text(SKILL_DIR / "SKILL.md")).group(1)


def _lf(text: str) -> str:
    return text.replace("\r\n", "\n")


def _newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def _digest(body: str) -> str:
    return hashlib.sha256(_lf(body).encode("utf-8")).hexdigest()


def find_block(text: str) -> Optional[Block]:
    """The one baseline block in text, or None when there is none. Raises BlockError for anything else."""
    begins, ends = text.count(BEGIN_TOKEN), text.count(END_TOKEN)
    if begins == 0 and ends == 0:
        return None
    m = BLOCK_RE.search(text)
    if begins != 1 or ends != 1 or not m:
        raise BlockError(
            "expected exactly one complete baseline block, found %d begin and %d end markers; "
            "fix the markers by hand and run again" % (begins, ends)
        )
    return Block(m.start(), m.end(), m.group(1), m.group(2), _lf(m.group(3)))


def block_is_edited(block: Block) -> bool:
    """True when the body no longer matches the hash recorded in the begin marker."""
    return _digest(block.body) != block.sha256


def render_block(version: str, newline: str = "\n") -> str:
    body = _lf(read_text(KIT_DIR / "AGENTS.block.md"))
    if not body.endswith("\n"):
        body += "\n"
    block = "<!-- baseline:begin version=%s sha256=%s -->\n%s%s\n" % (version, _digest(body), body, END_TOKEN)
    return block if newline == "\n" else block.replace("\n", newline)


def with_block(text: str, version: str) -> str:
    """Replace the block in text, or append it after a blank line when there is none; keeps the file's line endings."""
    newline = _newline(text)
    block = render_block(version, newline)
    found = find_block(text)
    if found:
        return text[: found.start] + block + text[found.end:]
    if text and not text.endswith("\n"):
        text += newline
    return text + (newline if text else "") + block


def kit_files(version: str) -> Dict[str, str]:
    """Relative path -> content for every kit file except AGENTS.md (which holds the block)."""
    files = {"baseline.yml": "baseline_version: %s\n" % version, "CLAUDE.md": "@AGENTS.md\n"}
    for rel in ("docs/adr/TEMPLATE.md", "docs/standards/TEMPLATE.md"):
        files[rel] = read_text(KIT_DIR / rel)
    return files
