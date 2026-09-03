---
title: "markdown: nested code fences"
date: 2026-08-17T01:27:47+02:00
tags:
  - bloggify
  - coding
  - dev
  - meta
---

**Problem statement**: a code block that quotes a markdown file swallows the
first closing fence it meets, which is the *inner* one.

The [ADRs and LLMs]({{< ref "2026-01-11-adrs-and-llms" >}}) post quotes a
`README.md` that itself contains a fenced template. Written naively:

````markdown
```markdown
# README

Use this template:

```markdown
# ADR-NNNN: Title
```

That was the template.
```
````

The [CommonMark spec](https://spec.commonmark.org/0.31.2/#fenced-code-blocks)
says who wins:

> The content of the code block consists of all subsequent lines, until a
> closing code fence of the same type as the code block began with (backticks
> or tildes), and with at least as many backticks or tildes as the opening code
> fence.

Three backticks close three backticks, so the template's closing fence
terminates the *outer* block. Everything after it leaks into the page:

```html
<div class="codeblock" data-lang="markdown">
  <!-- header -->
<p>That was the template.</p>
<div class="codeblock">
   <div class="highlight"><pre tabindex="0" class="chroma"><code class="language-plaintext" data-lang="plaintext"></code></pre></div>
</div>
```

Two code blocks and a stray paragraph, where one code block was meant.

The fix is a longer outer fence — four backticks, or more:

`````markdown
````markdown
# README

Use this template:

```markdown
# ADR-NNNN: Title
```

That was the template.
````
`````

Two details make this worth writing down.

The damage is quiet. On the real file the outer fence was `shell`, so Hugo
rendered a plausible block that had merely lost its last line. Comparing the
rendered code block before and after the fix:

````diff
-lang: shell
+lang: markdown
 …What becomes easier or more difficult to do because of this change?
+```
````

And `markdownlint` was happy the whole time:

```shell
% prek run markdownlint --files content/posts/2026-01-11-adrs-and-llms.md
markdownlint-cli2........................................................Passed
```

Rule of thumb: count the backticks of the innermost block, then add one for
every level above it.
