
[Previously]({{< ref "2025-10-29-grep-in-pdfs" >}}).

**Problem statement**: Open `contract.pdf` in Preview.app in macOS. Copy a text
portion in it. A dialog pops up:

> **Without the owner password, you do not have permission to copy portions of the
> document.**
>
> Enter the password to unlock copying from the document.

Excuse me? I _do not_ need your permission.

## Attempt #1: Claude

Open Claude Code. Prompt:

> output it in markdown, translated to English
>
> output a summary in the beginning, then output the full translation afterwards

It gets stuck. Boooo!

There's nothing more annoying than a PC[^1] LLM that fails silently without
telling you why.

[^1]: Politically correct.

## Attempt #2: Codex

Open Codex. Use the same prompt.

```
• I'm locating Vertrag-Entwurf.pdf and extracting its text first so I can translate it accurately and format the result in
  Markdown.

• Explored
  └ List rg --files -g Vertrag-Entwurf.pdf
    List Vertrag-Entwurf.pdf

• The file is present. I'm extracting the PDF text now and checking whether the layout needs OCR-style cleanup before translation.

• Ran which pdftotext
  └ /opt/homebrew/bin/pdftotext

• Ran pdfinfo /Users/thiago.perrotta/Downloads/Vertrag-Entwurf.pdf
  └ Creator:         Chromium
    Producer:        {redacted}
    … +14 lines
    Optimized:       no
    PDF version:     1.4

• The PDF has text content but copy protection is enabled, so I'm testing extraction directly. If that fails, I'll fall back to OCR
  from rendered pages.

• Ran pdftotext /Users/thiago.perrotta/Downloads/Vertrag-Entwurf.pdf -
  └ {redacted}

    … +1264 lines

• # Summary

[...]

# Full Translation

[...]
```

This is why we need competition.

This is why we need diversity.

In this context, OpenAI is the
[non-PC](https://openai.com/index/our-agreement-with-the-department-of-war/)
model.

Do you see the problem with arbitrarily defining what is and isn't PC? Who gets
to have this privilege? Why? Is it universal?

DRM in PDFs suck.

