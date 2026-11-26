"""Shared by init.py and update.py: the kit files and the baseline-owned block of AGENTS.md."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
KIT_DIR = SKILL_DIR / "assets" / "kit"
BLOCK_RE = re.compile(
    r"<!-- baseline:begin version=(\S+) sha256=([0-9a-f]{64}) -->\n(.*?)<!-- baseline:end -->\n?", re.S
)
VERSION_RE = re.compile(r'^[ \t]+version:[ \t]*"?([^"\n]+?)"?[ \t]*$', re.M)


@dataclass
class Block:
    start: int
    end: int
    version: str
    sha256: str
    body: str


def installed_version() -> str:
    """The version this skill was installed at: metadata.version in its own SKILL.md."""
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    return VERSION_RE.search(text).group(1)


def _digest(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def find_block(text: str) -> Optional[Block]:
    m = BLOCK_RE.search(text)
    if not m:
        return None
    return Block(m.start(), m.end(), m.group(1), m.group(2), m.group(3))


def block_is_edited(block: Block) -> bool:
    """True when the body no longer matches the hash recorded in the begin marker."""
    return _digest(block.body) != block.sha256


def render_block(version: str) -> str:
    body = (KIT_DIR / "AGENTS.block.md").read_text(encoding="utf-8")
    if not body.endswith("\n"):
        body += "\n"
    return "<!-- baseline:begin version=%s sha256=%s -->\n%s<!-- baseline:end -->\n" % (version, _digest(body), body)


def with_block(text: str, version: str) -> str:
    """Replace the block in text, or append it after a blank line when there is none."""
    block = render_block(version)
    found = find_block(text)
    if found:
        return text[: found.start] + block + text[found.end:]
    if text and not text.endswith("\n"):
        text += "\n"
    return text + ("\n" if text else "") + block


def kit_files(version: str) -> Dict[str, str]:
    """Relative path -> content for every kit file except AGENTS.md (which holds the block)."""
    files = {"baseline.yml": "baseline_version: %s\n" % version, "CLAUDE.md": "@AGENTS.md\n"}
    for rel in ("docs/adr/TEMPLATE.md", "docs/standards/TEMPLATE.md"):
        text = (KIT_DIR / rel).read_text(encoding="utf-8")
        files[rel] = text.replace("{{VERSION}}", version)
    return files
