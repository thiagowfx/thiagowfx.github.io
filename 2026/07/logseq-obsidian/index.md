---
title: "logseq → obsidian"
url: https://perrotta.dev/2026/07/logseq-obsidian/
last_updated: 2026-07-21
---


[Previously]({{< ref "2026-07-18-brew-pin" >}}).

**Problem statement**: LogSeq v2 is moving its graph format from markdown files
to a sqlite database:

- [What's New with Logseq DB — May 16th 2026](https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020)
- [Big update: Logseq is splitting into two versions](https://logseq.io/p/e3YDyX5AYr)

This is _not OK_ for my workflow.

The whole point of adopting LogSeq was, just like
[Obsidian](https://obsidian.md/), the promise of
managing my notes in plain markdown files.

Even though this migration is supposed to improve the performance of the app, it
ends up breaking a fundamental reason why I decided to use it in the first
place.

Furthermore, the Second Brain app of my choice is supposed to be boring. It is
a big deal to wake up one day and find that I can no longer open my notes
graph with the new version of the app. This is a no-go.

Well, classic LogSeq (dubbed "Logseq OG") will be [kept
around](https://github.com/logseq/og), but I can only assume that from this
point on it will become poorly maintained — it will never get the same amount of
resources and attention as the new version.

Also, even if I really wanted to use the new version, it turns out it does not
work on mobile (iOS), which is a dealbreaker, therefore I would be forced to
stay stuck with OG for a while. Heck, the iOS app hasn't been updated in 2y
anyway, and it shows.

There will be no hard feelings, this is a peaceful breakup; I enjoyed LogSeq,
it's simpler and more streamlined than Obsidian; as such, I will keep
recommending it to most people.

That said, I've always been pondering whether to switch back to Obsidian.
There's no doubt that Obsidian is more actively maintained and better suited for
Gen AI / LLM workflows these days (see [Obsidian CLI](https://obsidian.md/cli)
for starters).

Why did I switch to LogSeq from Obsidian in the first place? Because Obsidian
was too much for me. It was more complicated (in terms of its feature set) than
warranted for my purposes. It offered more than I needed. That's not necessarily
a bad thing. It's like saying (hypothetically) "I prefer `nano` instead of
`vim`", or that I prefer to live in a studio apartment than in a 3-bedroom
house.

Obsidian won't let me down in terms of changing its file format: [file over
app](https://stephango.com/file-over-app) is one of their core
[promises](https://stephango.com/self-guarantee):

> File over app is a philosophy: if you want to create digital artifacts that
> last, they must be files you can control, in formats that are easy to retrieve
> and read. Use tools that give you this freedom.
>
> File over app is an appeal to tool makers: accept that all software is
> ephemeral, and give people ownership over their data.

This is very important. My Second Brain app must not lock me in. LogSeq, upon
the switch to a sqlite database, breaks this invariant. I want — I need — boring
markdown files. Do not break the beauty and simplicity of this setup.

## Migration

LogSeq and Obsidian are similar but not identical.

In order to bridge the gap, a small python script (drafted by Claude Fable 5,
reviewed by me) walked the existing LogSeq Graph and wrote to a fresh Obsidian
Vault, leaving the source untouched, should I decide to roll back.

These are some mappings (LogSeq → Obsidian):

```text
journals/2024_03_04.md         ->  journals/2024-03-04.md
pages/Foo___Bar.md             ->  Foo/Bar.md          (namespaces)
- TODO buy milk                ->  - [ ] buy milk
- DOING ...                    ->  - [/] ...
- DONE ...                     ->  - [x] ...
[[Feb 9th, 2026]]              ->  [[2026-02-09]]
((67ea7dba-3200-...))          ->  [[2025-03-31#^67ea7dba]]
{{embed ((67ea7dba-3200-...))}} -> ![[2025-03-31#^67ea7dba]]
{{video https://...}}          ->  plain URL
id:: 67ea7dba-3200-...         ->  ^67ea7dba block anchor (when referenced)
collapsed:: true, :LOGBOOK:    ->  dropped
```

Plus one line of config so that the LogSeq journals become Obsidian daily notes:

```json {filename=".obsidian/daily-notes.json"}
{
    "folder": "journals",
    "format": "YYYY-MM-DD"
}
```

...and then I spent some time trying to dumb down Obsidian, disabling core
plug-ins I do not need at this time. There's no need for community plug-ins for
now (if ever).

So far, I only migrated my corp (work) notes. I'll need to migrate my personal
PKM as well, but I am happy to simply pilot this migration at work first, so
that I don't get to regret twice.

The migration script:

```python {filename="migrate.py"}
#!/usr/bin/env python3
"""Migrate LogSeq graph -> Obsidian vault. Source is never modified."""
import re
import shutil
from pathlib import Path

SRC = Path("/Users/thiago.perrotta/Library/Mobile Documents/iCloud~com~logseq~logseq/{redacted}")
DST = Path("/Users/thiago.perrotta/Library/Mobile Documents/iCloud~md~obsidian/{redacted}")

UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

MARKER_MAP = {
    "TODO": "[ ]", "LATER": "[ ]", "WAITING": "[ ]",
    "DOING": "[/]", "NOW": "[/]", "IN-PROGRESS": "[/]",
    "DONE": "[x]",
    "CANCELED": "[-]", "CANCELLED": "[-]",
}


def journal_name(stem: str) -> str:
    return stem.replace("_", "-")


def dest_rel(src_file: Path) -> Path:
    """Map a source md file to its vault-relative destination path."""
    if src_file.parent.name == "journals":
        return Path("journals") / (journal_name(src_file.stem) + ".md")
    # namespace pages: A___B.md -> A/B.md; everything else under pages/
    parts = src_file.stem.split("___")
    return Path(*parts[:-1]) / (parts[-1] + ".md") if len(parts) > 1 else Path("pages") / src_file.name


def page_ref(src_file: Path) -> str:
    """Wiki-link target for a source file (what goes inside [[...]])."""
    if src_file.parent.name == "journals":
        return journal_name(src_file.stem)
    return "/".join(src_file.stem.split("___"))


def collect_ids():
    """uuid -> (link target, anchor) for every id:: definition; also which uuids are referenced."""
    defined, referenced = {}, set()
    for f in sorted(SRC.glob("pages/*.md")) + sorted(SRC.glob("journals/*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(rf"^\s*id:: ({UUID})\s*$", text, re.M):
            defined[m.group(1)] = (page_ref(f), m.group(1)[:8])
        for m in re.finditer(rf"\(\(({UUID})\)\)", text):
            referenced.add(m.group(1))
    return defined, referenced


def convert(text: str, defined, referenced) -> str:
    lines = text.split("\n")
    out = []
    in_fence = False
    in_logbook = False

    def resolve_ref(m):
        uuid = m.group(1)
        if uuid in defined:
            target, anchor = defined[uuid]
            return f"[[{target}#^{anchor}]]"
        return m.group(0)

    def resolve_embed(m):
        uuid = m.group(1)
        if uuid in defined:
            target, anchor = defined[uuid]
            return f"![[{target}#^{anchor}]]"
        return m.group(0)

    def date_link(m):
        mon, day, year = m.group(1), int(m.group(2)), int(m.group(4))
        return f"[[{year:04d}-{MONTHS[mon]:02d}-{day:02d}]]"

    pending_merge_indent = None  # indent of an empty bullet awaiting its continuation line

    for line in lines:
        stripped = line.strip()

        # merge continuation text into a bullet whose first line was a property
        if pending_merge_indent is not None:
            m = re.match(rf"^{re.escape(pending_merge_indent)}\s\s?(\S.*)$", line)
            pending_merge_indent = None
            if m and out:
                out[-1] = out[-1] + m.group(1)
                continue

        # LogSeq opens fences on bullet lines ("- ```lang"), closes with bare "```"
        if re.match(r"^\s*(?:[-*+]\s+)?```", line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        # LOGBOOK drawers
        if stripped == ":LOGBOOK:":
            in_logbook = True
            continue
        if in_logbook:
            if stripped == ":END:":
                in_logbook = False
            continue

        # bullet-form property lines: block whose first line is the property itself
        # ("- collapsed:: true" with real content on the continuation line below)
        m = re.match(rf"^(\s*)- (collapsed:: (?:true|false)|logseq\.order-list-type:: number|id:: ({UUID}))\s*$", line)
        if m:
            indent = m.group(1)
            uuid = m.group(3)
            if uuid and uuid in referenced:
                out.append(f"{indent}- ^{uuid[:8]}")
            else:
                out.append(f"{indent}- ")
                pending_merge_indent = indent
            continue

        # property lines
        m = re.match(rf"^\s*id:: ({UUID})\s*$", line)
        if m:
            uuid = m.group(1)
            if uuid in referenced and out:
                # anchor goes at end of the block's first line
                for i in range(len(out) - 1, -1, -1):
                    if out[i].strip():
                        out[i] = out[i].rstrip() + f" ^{uuid[:8]}"
                        break
            continue
        if re.match(r"^\s*collapsed:: (true|false)\s*$", line):
            continue
        if re.match(r"^\s*logseq\.order-list-type:: number\s*$", line):
            # convert the previous bullet line to a numbered item; number it by
            # walking back past deeper lines to the previous same-indent sibling
            for i in range(len(out) - 1, -1, -1):
                bm = re.match(r"^(\s*)- (.*)$", out[i])
                if bm:
                    indent = bm.group(1)
                    n = 1
                    for j in range(i - 1, -1, -1):
                        if not out[j].strip():
                            continue
                        lead = out[j][: len(out[j]) - len(out[j].lstrip())]
                        if len(lead) > len(indent):
                            continue  # child or continuation line
                        if lead == indent:
                            nm = re.match(rf"^{re.escape(indent)}(\d+)\. ", out[j])
                            n = int(nm.group(1)) + 1 if nm else 1
                        break
                    out[i] = f"{indent}{n}. {bm.group(2)}"
                    break
            continue

        # task markers on bullet lines (not headings)
        line = re.sub(
            r"^(\s*)- (TODO|LATER|WAITING|DOING|NOW|IN-PROGRESS|DONE|CANCELED|CANCELLED)\s+",
            lambda m: f"{m.group(1)}- {MARKER_MAP[m.group(2)]} ",
            line,
        )

        # drop LogSeq priority markers
        line = re.sub(r"\[#[A-C]\]\s*", "", line)

        # embeds and block refs
        line = re.sub(rf"\{{\{{embed \(\(({UUID})\)\)\}}\}}", resolve_embed, line)
        line = re.sub(r"\{\{embed \[\[([^]]+)\]\]\}\}", r"![[\1]]", line)
        line = re.sub(rf"\(\(({UUID})\)\)", resolve_ref, line)
        line = re.sub(r"\{\{video ([^}]+)\}\}", r"\1", line)

        # date links: [[Feb 9th, 2026]] -> [[2026-02-09]]
        line = re.sub(
            r"\[\[(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2})(st|nd|rd|th), (\d{4})\]\]",
            date_link, line)

        # asset paths
        line = line.replace("](../assets/", "](assets/")

        out.append(line)

    result = "\n".join(out)
    if result.strip() == "-":  # LogSeq empty-page placeholder
        result = ""
    return result


def main():
    defined, referenced = collect_ids()
    orphans = referenced - set(defined)
    if orphans:
        print(f"WARNING: refs without target: {orphans}")

    written = 0
    for f in sorted(SRC.glob("pages/*.md")) + sorted(SRC.glob("journals/*.md")):
        rel = dest_rel(f)
        dst = DST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(convert(f.read_text(encoding="utf-8"), defined, referenced),
                       encoding="utf-8")
        written += 1

    assets_dst = DST / "assets"
    assets_dst.mkdir(exist_ok=True)
    copied = 0
    for a in SRC.glob("assets/*"):
        if a.name == ".DS_Store":
            continue
        shutil.copy2(a, assets_dst / a.name)
        copied += 1

    print(f"wrote {written} notes, copied {copied} assets")


if __name__ == "__main__":
    main()
```

