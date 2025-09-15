---
title: "{{ getenv "HUGO_TITLE" }}"
date: {{ .Date }}
tags:
  - coding
---

{{- $leetcode_slug := getenv "HUGO_LEETCODE_SLUG" }}
{{- $url := cond (ne $leetcode_slug "") (printf "https://leetcode.com/problems/%s/" $leetcode_slug) "#" }}

[{{ getenv "HUGO_TITLE" }}]({{ $url }}):

```python
```
