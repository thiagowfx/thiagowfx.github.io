
**Problem statement**: given a command run with a ton of output, how can you
take a glance at both (i) its first few lines and (ii) its last few lines?

Let's hypothetically call it `lorem`.

This is what we want to achieve:

```shell
lorem | head
```

```shell
lorem | tail
```

...ideally though we would like to run `lorem` _only once_.

How about this?

```shell
lorem | tee out.log
head out.log
tail out.log
rm out.log
```

It works, but can we do it without creating an intermediate `out.log` file?

[TIL](https://alexwlchan.net/notes/2026/truncate-middle-output/?ref=rss) via
Alex Chan:

> How to truncate the middle of long command output
>
> Use a command group { head -n 3; echo '[…]'; tail -n 5; } to snip print the
> first few and last few lines.
>
> If I'm running a command with lots of output, I can use head(1) to get the
> first few lines, or tail(1) to get the last few lines. What if I want to get
> some lines from the beginning and from the end, but truncate the middle?

```shell
lorem | { head; echo '[...]'; tail; }
```

Docs: [bash command
grouping](https://www.gnu.org/software/bash/manual/html_node/Command-Grouping.html):

> `{ list; }`
>
> Placing a list of commands between curly braces causes the list to be executed
> in the current shell environment. No subshell is created. The semicolon (or
> newline) following list is required.
>
> [...] The braces are reserved words, so they must be separated from the list
> by blanks or other shell metacharacters. [...]
>
> The exit status [...] is the exit status of list.

