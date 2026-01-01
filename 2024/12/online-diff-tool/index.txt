
Sometimes I have two snippets of text in my clipboard[^1] that I need to diff.

The quickest way to do so is roughly like this:

```shell
% cdtmp
% $EDITOR a  # then paste
% $EDITOR b  # then paste the other one
% diff -uN a b
```

[`cdtmp`]({{< ref "2024-10-07-cdtmp" >}}) was previously covered, it `cd`s to a
temporary directory.

The `diff` tool in the CLI is not very important, you could pick any one between
`diff -uN`, `colordiff -uN` or [`icdiff`]({{< ref
"2024-07-09-icdiff-side-by-side-diff" >}}).

However the terminal has its limitations.
Sometimes it's much better to diff with a graphical application.

For macOS I've heard that [Kaleidoscope](https://kaleidoscope.app/) is great,
but I don't use it. For Linux there's KDiff3 and Meld.

It's much easier to use a web tool though, as it's operating system agnostic.

Julia Evans has recently recommended
[diffdiff](https://jvns.ca/til/diffdiff--a-great-diff-tool/): https://diffdiff.net/. I like it!

At Google we had an internally hosted one at `http://diff/` (or was it `go/diff`?).

[^1]: If you're only able to hold one at a time, you should definitely upgrade
    your workflow to using a clipboard manager, you're missing out. For macOS,
    see my [previous post]({{< ref "2023-12-02-maccy-macos-clipboard-manager"
    >}}).

