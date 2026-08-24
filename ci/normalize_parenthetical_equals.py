#!/usr/bin/env python3
"""Remove space between '(' and '=' in Markdown prose."""

import re
import sys
from pathlib import Path


FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+).*?\1")
PARENTHETICAL_EQUALS_RE = re.compile(r"\([ \t]+=[ \t]*")


def normalize_prose_line(line):
    """Normalize prose outside inline code spans."""
    result = []
    position = 0

    for match in INLINE_CODE_RE.finditer(line):
        result.append(PARENTHETICAL_EQUALS_RE.sub("(=", line[position : match.start()]))
        result.append(match.group(0))
        position = match.end()

    result.append(PARENTHETICAL_EQUALS_RE.sub("(=", line[position:]))
    return "".join(result)


def normalize_parenthetical_equals(content):
    """Normalize parenthetical equals in prose, outside frontmatter and fenced code."""
    lines = content.split("\n")
    result = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    fence = None

    for index, line in enumerate(lines):
        if in_frontmatter:
            result.append(line)
            if index > 0 and line.strip() == "---":
                in_frontmatter = False
            continue

        fence_match = FENCE_RE.match(line)
        if fence is not None:
            result.append(line)
            if re.fullmatch(rf"[ \t]{{0,3}}{re.escape(fence[0])}{{{fence[1]},}}[ \t]*", line):
                fence = None
            continue

        if fence_match:
            marker = fence_match.group(1)
            fence = (marker[0], len(marker))
            result.append(line)
            continue

        result.append(normalize_prose_line(line))

    return "\n".join(result)


def fix_file(filename):
    """Fix one file. Return True when content changed."""
    path = Path(filename)
    content = path.read_text(encoding="utf-8")
    modified = normalize_parenthetical_equals(content)

    if modified == content:
        return False

    path.write_text(modified, encoding="utf-8")
    return True


def main(argv=None):
    argv = argv or sys.argv[1:]

    if not argv:
        argv = [str(path) for path in Path("content").glob("**/posts/**/*.md")]

    for filename in argv:
        fix_file(filename)

    return 0


if __name__ == "__main__":
    sys.exit(main())
