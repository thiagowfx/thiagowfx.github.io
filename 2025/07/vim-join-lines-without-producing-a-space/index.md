
Here's a common issue I have when blogging, when inserting a markdown link with
`vim`. The edit progression is as follows, wherein `|` represents the cursor:

First, blank:

```md
|
```

Then, type out the hyperlink label and prepare to insert the link:

```md
[example](|
)
```

Now go to another buffer (window) and copy the link (with `y` + motion).

Go back to the original buffer and paste it with `p`:

```md
[example](
|https://example.com/
)
```

Press `kJ`:

```md
[example](| https://example.com/
)
```

Press `J` again:

```md
[example](| https://example.com/)
```

`J` is for "join lines" (`:help J`).

Do you see the issue above? The first `J` inserts a space, the second one does
not. This inconsistency is frustrating.

This [vi stack
exchange](https://vi.stackexchange.com/questions/439/how-to-join-lines-without-producing-a-space)
question seeks to address it:

> The standard J command for joining lines replaces the newline character(s)
> with a space. It's useful when editing 'literature' but can be troublesome if
> I, say, edit a hex dump by hand if I forget to remove the superfluous space.
>
> Is there a quick & easy method to join two lines without producing a space
between them?

The standard recommendation is to use `gJ` to do so. From `:help gJ`:

> Join [count] lines, with a minimum of two lines. Don't insert or remove any
> spaces.

But it's harder to memorize than simply `J`. Plus, it's an extra keystroke. I'd
rather unconditionally use `J`.

It turns out it's possible to do so with a simple config setting, added to
`~/.vimrc`:

```vim
nnoremap J gJ
```

When repeating the original link insertion sequence, it yields the following
result, as desired (no spaces anywhere!):

```md
[example](|https://example.com/)
```

