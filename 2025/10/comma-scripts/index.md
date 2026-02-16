
Ricardo Ander-Egg
[suggests](https://ricardoanderegg.com/posts/executable-bin-scripts-instead-of-shell-aliases/)
to use executable scripts instead of shell aliases:

> I stopped using shell aliases and moved everything into executable scripts.

I've been slowly doing the same. From his post, adapted:

**Main Benefits**:

- No need to source your shell rc after adding new scripts
  — Use immediately without reloading your shell
- No need to edit your shell rc, just drop executable files in `$HOME/.bin` (already in my `$PATH`)
  — Faster iteration (edit script, re-run command, repeat)
- Can be used out-of-the-box with `fd` / `find` / `xargs` and friends

Another recommendation:

Brandon Rhodes: [Start all of your commands with a comma](https://rhodesmill.org/brandon/2009/commands-with-comma/):

> A quick experiment revealed in a flash that the comma was exactly the
> character that I had been looking for! Every tool and shell that lay in arm's
> reach treated the comma as a perfectly normal and unobjectionable character in
> a filename. By simply prefixing each of my custom commands with a comma, they
> became completely distinct from system commands and thus free from any chance
> of a collision.

> And, best of all, thanks to the magic of tab-completion, it became very easy
> to browse my entire collection of commands. When trying to remember which of
> my commands are available in my ~/bin/ directory on a given system, or when
> simply trying to remember what some of my commands are called, I simply type a
> comma followed by tab and my list of commands appears:

> I heartily recommend this technique to anyone with their own ~/bin/ directory
> who wants their command names kept clean, tidy, and completely orthogonal to
> any commands that the future might bring to your system.

I used to do this with prefixes (`t-` because of my first name initial, and then
[`sd-`](https://ianthehenry.com/posts/sd-my-script-directory/)), but a
non-alphabetic character is more compelling.

