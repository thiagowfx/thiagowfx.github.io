---
title: "{{ getenv "HUGO_TITLE" }}"
date: {{ .Date }}
tags:
  - coding
---

{{ $title := getenv "HUGO_TITLE" }}
{{ $url := "#" }}
{{ if strings.HasPrefix (lower $title) "leetcode" }}
  {{ $problem := $title | split ":" | index 1 | strings.TrimLeft " " }}
  {{ $slug := $problem | lower | replace " " "-" }}
  {{ $url = printf "https://leetcode.com/problems/%s/" $slug }}
{{ end }}

[{{ $title }}]({{ $url }}):

```python
```
