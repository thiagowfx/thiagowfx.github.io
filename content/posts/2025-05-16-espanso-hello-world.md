---
title: "Espanso: hello world"
date: 2025-05-16T17:40:26+02:00
tags:
  - dev
  - macos
---

[Previously]({{< ref "2025-03-24-maccy-pin-items" >}}):

> Sometimes it's useful to have certain code snippets be easily accessible from
> the clipboard manager.
>
> [...]
>
> This workflow is decent for temporary entries. For semi-permanent ones, I
> should look into [Espanso](https://espanso.org/) at some point. For now,
> [Raycast Snippets]({{< ref "2025-01-29-raycast-snippets" >}}) fills in this
> role.

Today is the day!

[Espanso](https://espanso.org/):

> Supercharge your typing| experience.
>
> Tired of typing the same sentences over and over? Discover the incredible
> power of a full-blown text expander.

So?

> How it works
>
> Espanso detects when you type a keyword
>
> Today is :date
>
> (becomes) Today is 05/16/2025
>
> and replaces it while you're typing.

It's just like [Text Expander](https://www.raycast.com/core-features/snippets)
from Raycast snippets.

It's available on all major OSes (Windows, Linux, macOS). I am testing it on
macOS. Installation:

```shell
% brew install espanso
```

After installing it and opening it, give it all sorts of System Accessibility
permissions so that it can perform its magic.

This is just a "hello world" post, therefore I am not going to list every single
capability it has. Let's just keep it simple and get our feet wet.

I have to type `helm ls -A --max 9999 | grep -i {release}` [all the time]({{<
ref "2024-08-26-helm-list-all-installed-charts-in-the-cluster" >}}), and I'm fed
up with it.

I want to create a `:helm:ls` expansion that will trigger that command
expansion.

Run `espanso edit`. It opens a stock `base.yml` file:

```yaml
# espanso match file

# For a complete introduction, visit the official docs at: https://espanso.org/docs/

# You can use this file to define the base matches (aka snippets)
# that will be available in every application when using espanso.

# Matches are substitution rules: when you type the "trigger" string
# it gets replaced by the "replace" string.
matches:
  # Simple text replacement
  - trigger: ":espanso"
    replace: "Hi there!"

  # NOTE: espanso uses YAML to define matches, so pay attention to the indentation!

  # But matches can also be dynamic:

  # Print the current date
  - trigger: ":date"
    replace: "{{mydate}}"
    vars:
      - name: mydate
        type: date
        params:
          format: "%m/%d/%Y"

  # Print the output of a shell command
  - trigger: ":shell"
    replace: "{{output}}"
    vars:
      - name: output
        type: shell
        params:
          cmd: "echo 'Hello from your shell'"
  # And much more! For more information, visit the docs: https://espanso.org/docs/
```

The file is self-contained and well-documented enough that I do not need to look
up any docs nor use AI to add the desired entry:

```yaml
# [...]
matches:
  # [...]
  - trigger: ":helm:ls"
    replace: "helm ls --max 9999 -A | grep -i"
```

Once the file is saved, it's magic ✨, and it takes effect immediately.

Example usage[^1]:

```shell
:helm:ls redis
```

...becomes:

```shell
helm ls --max 9999 -A | grep -i redis
```

For reference, this is the full path to the file:

```shell
% espanso edit
Editing file: /Users/thiago.perrotta/Library/Application Support/espanso/match/base.yml
```

I am particularly excited it's YAML and it's accessible in a stable location: it
should be quite easy to integrate it with my dotfiles later on.

Its out-of-the-box usability (for developers who prefer text files) and
perceived speed are better than Raycast snippets.

There are so many possibilities to explore: command ~~espansions~~ expansions, LLM prompts,
email greetings, canned responses, and so on.

For Raycast snippets I was using `@@` as a prefix. Espanso seems to recommend
`:`. Let's see which one I will stick to.

Also, I'd like to thank Farzad for the recommendation via email. It wasn't the
first time I had heard about Espanso, but it has reinforced my desire to try it
out.

[^1]: In order to type a plain `:helm:ls` without expansion (e.g. for this blog
    post), type the following: `:helm:l{left arrow}{right arrow}s`.
