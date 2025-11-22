---
title: "{{ getenv "HUGO_TITLE" }}"
date: {{ .Date }}
tags:
  - coding
rss: false
---

{{- $leetcode_slug := getenv "HUGO_LEETCODE_SLUG" }}
{{- $bytebytego_slug := getenv "HUGO_BYTEBYTEGO_SLUG" }}
{{- $url := "#" }}
{{- if ne $leetcode_slug "" }}
  {{- $url = printf "https://leetcode.com/problems/%s/" $leetcode_slug }}
{{- else if ne $bytebytego_slug "" }}
  {{- $url = printf "https://bytebytego.com/exercises/coding-patterns/%s" $bytebytego_slug }}
{{- end }}

[{{ getenv "HUGO_TITLE" }}]({{ $url }}):

```python
```
