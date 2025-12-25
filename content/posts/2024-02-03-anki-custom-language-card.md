---
title: "Anki: custom language card"
date: 2024-02-03T13:02:21-03:00
tags:
  - bestof
  - dev
---

The more time you spent playing with [Anki](https://apps.ankiweb.net/), the
more opinionated you become.

Upon reading [Fluent Forever](https://fluent-forever.com/index.html) by Gabriel
Wyner, I got an itch to create my own Anki note template for learning
languages.

## The template

There's no point explaining how to create a new template; the excellent [Anki
documentation](https://docs.ankiweb.net/templates/intro.html) already does so.
Instead, I'll just list and explain the template I created.

The template is called "Deutsch Language Card 🇩🇪". It has four fields:

1. Front
1. Front Example
1. Back
1. Striked

Front and Back come from the built-in template. There's nothing special about
them. I use "Front" for the canonical term in the foreign language I'm
learning, and "Back" for the explanation in the base / native language I'm
mostly familiar with[^1].

Here's an example:

```
Front: das Buch
Back: book 📚
```

Whenever possible I include one or more emojis 😃 in the "Back" field.

The **canonicalization** of the "Front" field is important, and one of the best
(key, even!) features of Anki. It will smartly detect (and prevent!) duplicates
from being created. It is case sensitive, therefore it's important to create
one convention and stick to it.

"Front Example" is used to complement the "Front" field. It consists of one or
both of the following:

- A phrase or sentence containing the Front term.
- A picture representing the Front term.

To increase overall retention, it's always best to add cues familiar to your
context.

Add phrases that resonate with you or that you find in textbooks or
blog posts that resonate with you. In my experience, adding random phrases is
not effective.

Add images that represent well that you're describing and that
resonate with you. Photos that you take yourself are also fair game!

"Striked" is to disambiguate synonyms or false cognates. For example:

```
Front: der Sturm
Back: storm ⛈️
Striked: das Gewitter, das Unwetter
```

When I am reviewing the Back card, I want to cue myself not to think about the
striked terms.

## The source code

### The Front card

```text
{{Front}} {{tts de_DE:Front}}

{{#Front Example}}
<br>
<i>{{Front Example}}</i> {{tts de_DE:Front Example}}
{{/Front Example}}
```

The front card includes a text-to-speech sample that is generated on-the-fly.
It works very well on macOS and iOS. In fact, that's main reason why the
template is called "Deutsch Language Card" instead of just "Language Card". The
text-to-speech engine is customized to have an accent in the given language.
For (High) German, that is `de_DE`.

### The Back card

```text
{{Back}}

{{#Striked}}
<br><br>
<s>{{Striked}}</s>
{{/Striked}}
```

The striked terms are ~~striked~~, as you would expect.

[^1]: Interestingly I prefer to use English most of the time, even though it is
    not my mother tongue.
