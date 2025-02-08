---
title: "MLC Chat: off-line LLMs in your iPhone"
date: 2025-02-08T16:26:04+01:00
tags:
  - dev
  - privacy
  - selfhosted
---

[MLC Chat](https://apps.apple.com/us/app/mlc-chat/id6448482937):

> Large language models locally in phone
>
> MLC Chat lets users chat with open language models locally on ipads and
> iphones. After a model is downloaded to the app, everything runs locally
> without server support, and it works without internet connections do not
> record any information.
>
> Because the models run locally, it only works for the devices with sufficient
> VRAM depending on the models being used.
>
> MLC Chat is part of open source project MLC LLM, with allows any language
> model to be deployed natively on a diverse set of hardware backends and native
> applications. MLC Chat is a runtime that runs different open model
> architectures on your phone. The app is intended for non-commercial purposes.
> It allows you to run open-language models downloaded from the internet. Each
> model can be subject to its respective licenses.

I originally heard about it last year via [Simon
Willison](https://simonwillison.net/).

I used the `LLAMA-3.2-3B-Instruct` model on my iPhone 14 Pro, and it worked
quite well[^1]. The performance was quite acceptable for what I would expect of a
local LLM on my phone in 2024-25. It takes a few seconds to initialize / warm up
at startup.

A noticeable side effect: my phone heats up _significantly_ when using it for a
couple of minutes. Battery drain is also perceivable.

The app is super simple. There's no chat history, it's a single conversation.

[^1]: One minor annoyance: that model is quite verbose and somewhat overly
    enthusiastic. Did someone give it the personality from Microsoft Word
    Clippy?
