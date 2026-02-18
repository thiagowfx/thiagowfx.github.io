
## Background

Sometimes we might need to store some sensible information as plain text. By
plain text I mean using no fancy stuff or third-party programs: the information
should be easily retrievable via a terminal or a text editor. So, what we can do
in this scenario? One such option is to create a `my_secret_file.txt` then
populate it with your important data. Of course, you'll be saving it in your
Desktop folder, where everyone with access to your computer/account will be able
to read it, right? **No!** I have to confess I once did it (with the exception
of the Desktop part…of course, a folder such as `Documents/passwords` doesn't
help either). Nothing too much important, but it was a password, damn. So, as we
value more our data, we find a KISS way to complete the same task.

## Show me the code…er, the way

In this post I'm documenting how to use Emacs + GNU PG + Org-mode to encrypt
your sensible information. **Warning**: I do not recommend to store your
passwords this way, because it is annoying to keep retrieving frequent used
information from a text editor; this method should be used only when you need to
store passwords you won't be retrieving too much. Does it looks reasonable?
Okay, so let's proceed. Here are the requirements list:

- Emacs 23+
- Org-mode (should be shipped by default with a recent emacs, if not, access
  orgmode.org)
- GNU PG — I'm also assuming you already have a gpg key. If not, see my previous
  posts (1), (2), for example.

All of those are easily obtained in a Linux or \*BSD machine. If you are on
Windows, Emacs can be easily installed with chocolatey, but I'm not sure about
GPG, you should try this yourself. Now, you should add something like this to
your `.emacs` file:

```lisp
(require 'org-crypt)
(org-crypt-use-before-save-magic)
(setq org-tags-exclude-from-inheritance '("crypt"))
(setq org-crypt-key "A905373C")
```

The only line you should change is the last one: you should reference your GPG
Key instead of mine. If you don't know what this means, you should read more
about OpenPGP. Now, I'm showing you the results via a mini screencast:
https://asciinema.org/a/11355 Notice this encrypted information could be shared
on the web; but nobody would be able to decrypt it without your private PGP key.
Just use the :crypt: tag for the entries you want to have encrypted; that's it.

