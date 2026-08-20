#!/usr/bin/env python3
"""Remove UTM tracking parameters from HTTP and HTTPS URLs."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote_plus, urlsplit, urlunsplit


HTTP_URL_RE = re.compile(r"https?://[^\s<>\"'`\]}]+", re.IGNORECASE)
UTM_KEY_RE = re.compile(r'\butm_[a-z0-9_]+\b', re.IGNORECASE)
TRAILING_PUNCTUATION = '.,;:!?*_~'


def strip_utm_parameters(url):
    """Remove UTM query parameters while preserving other URL components."""
    try:
        parts = urlsplit(url)
    except ValueError:
        return url

    if not parts.query:
        return url

    separator = '&amp;' if '&amp;' in parts.query.lower() else '&'
    parameters = re.split(r'&(?:amp;)?', parts.query, flags=re.IGNORECASE)
    kept = []

    for parameter in parameters:
        key = unquote_plus(parameter.partition('=')[0]).lower()
        if not key.startswith('utm_'):
            kept.append(parameter)

    if len(kept) == len(parameters):
        return url

    query = separator.join(parameter for parameter in kept if parameter)
    return urlunsplit(parts._replace(query=query))


def split_trailing_punctuation(url):
    """Separate Markdown punctuation that is not part of a URL."""
    suffix = ''

    while url and url[-1] in TRAILING_PUNCTUATION:
        suffix = url[-1] + suffix
        url = url[:-1]

    while url.endswith(')') and url.count(')') > url.count('('):
        suffix = ')' + suffix
        url = url[:-1]

    return url, suffix


def remove_utm_parameters(content):
    """Remove UTM parameters from all HTTP and HTTPS URLs in content."""

    def remove(match):
        url, suffix = split_trailing_punctuation(match.group(0))
        return strip_utm_parameters(url) + suffix

    return HTTP_URL_RE.sub(remove, content)


def fix_file(filename):
    """Fix one file and return its changed state and unresolved line numbers."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = remove_utm_parameters(content)
    changed = modified != content

    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)

    unresolved = [
        line_number
        for line_number, line in enumerate(modified.splitlines(), 1)
        if UTM_KEY_RE.search(line)
    ]
    return changed, unresolved


def main(argv=None):
    argv = argv or sys.argv[1:]

    if not argv:
        markdown_files = list(Path('.').glob('**/*.md'))
        if not markdown_files:
            return 0
        argv = [str(f) for f in markdown_files]

    ret = 0
    for filename in argv:
        changed, unresolved = fix_file(filename)
        if changed:
            print(f"Fixed: {filename}")
            ret = 1
        for line_number in unresolved:
            print(f"{filename}:{line_number}: UTM token could not be removed automatically")
            ret = 1

    return ret


if __name__ == '__main__':
    sys.exit(main())
