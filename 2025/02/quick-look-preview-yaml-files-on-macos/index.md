
You may be familiar with [Quick
Look](https://support.apple.com/en-gb/guide/mac-help/mh14119/mac) on macOS.

On Finder, select a file, then press the space bar. A preview pop-up appears,
wherein you can take a quick glance at the file contents.

Out-of-the-box many file formats are supported, even for images.

For developers, two popular formats are not supported:

- markdown
- yaml

I've been using [qlmarkdown](https://github.com/sbarex/QLMarkdown) for markdown,
and it works well. There's a homebrew package for it: `brew install --cask
qlmarkdown`.

Lately I wanted to add YAML as well. I found
[PreviewYaml](https://github.com/smittytone/PreviewYaml). It's MIT-Licensed and
open source, but there's no pre-built package for it, and it is not on homebrew
either. The author provides an app in the macOS App Store, but it's not free.

Upon digging deeper, I found
https://github.com/sbarex/SourceCodeSyntaxHighlight. It supports pretty much
every popular extension you'll need as a developer (including `.yaml`!). There's
a package for it:

```shell
% brew install --no-quarantine syntax-highlight
```

It is simple and works as advertised.

Should I uninstall `qlmarkdown` then? Not really:

> Markdown files (.md, .rmd): please use QLMarkdown which allows you to choose
> whether to display formatted output or the highlighted source code.

> Markdown files are not supported
>
> This is a deliberate choice. Most users want to see the formatted output and
> not the source code of their markdown files. If you need to view the markdown
> files (also with the possibility of choosing whether to show the formatting or
> the source code) I have developed QLMarkdown.

How nice! It turns out both extensions were developed by the same author. Thank
you, @sbarex!

