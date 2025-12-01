#!/usr/bin/env python3
"""Verify that LeetCode and ByteByteGo post titles follow the expected format."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEETCODE_PATTERN = re.compile(r"^LeetCode #\d+: .+$")
BYTEBYTEGO_PATTERN = re.compile(r"^ByteByteGo: .+$")
AOC_PATTERN = re.compile(r"^(?:AoC|Advent of Code) \d{4} Day \d{1,2}: .+$")


def extract_title(path: Path) -> str | None:
    """Return the title value from the front matter, if present."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:  # pragma: no cover - surfaced to the caller
        raise RuntimeError(f"{path}: unable to read file ({exc})") from exc

    if not lines or lines[0].strip() != "---":
        return None

    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if stripped.startswith("title:"):
            _, value = stripped.split(":", 1)
            return _strip_quotes(value.strip())

    return None


def _strip_quotes(value: str) -> str:
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def check_file(path: Path) -> str | None:
    """Return an error message if the file fails validation."""
    stem = path.stem.lower()
    if "leetcode" in stem:
        pattern = LEETCODE_PATTERN
        expected = "'LeetCode #NN: Title'"
    elif "bytebytego" in stem:
        pattern = BYTEBYTEGO_PATTERN
        expected = "'ByteByteGo: Title'"
    elif "aoc" in stem or "advent" in stem:
        pattern = AOC_PATTERN
        expected = "'AoC YYYY Day N: Title' or 'Advent of Code YYYY Day N: Title'"
    else:
        return None

    try:
        title = extract_title(path)
    except RuntimeError as exc:
        return str(exc)

    if not title:
        return f"{path}: missing title front matter"

    if not pattern.fullmatch(title):
        return f"{path}: title must match {expected} (found: {title!r})"

    return None


def main(argv: list[str]) -> int:
    errors = []

    for filename in argv:
        path = Path(filename)
        if path.suffix.lower() != ".md":
            continue

        error = check_file(path)
        if error:
            errors.append(error)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
