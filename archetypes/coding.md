---
{{- $today := now.Format "2006-01-02" -}}
{{- $slug := replace .Name (printf "%s-" $today) "" | replace ".md" "" -}}
{{- $title := "" -}}
{{- $url := "#" -}}
{{- if hasPrefix $slug "leetcode-" -}}
  {{- $parts := split $slug "-" -}}
  {{- $problemSlug := after 2 $parts | delimit "-" -}}
  {{- $url = printf "https://leetcode.com/problems/%s/" $problemSlug -}}
  {{- $rest := $problemSlug | replace "-" " " | title -}}
  {{- $title = printf "LeetCode #%s: %s" (index $parts 1) $rest -}}
{{- else -}}
  {{- $title = $slug | humanize -}}
{{- end -}}
title: "{{ $title }}"
date: {{ .Date }}
tags:
  - coding
---

[{{ $title }}]({{ $url }}):

```python
```
