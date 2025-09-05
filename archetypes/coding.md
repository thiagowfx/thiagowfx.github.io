---
{{- $today := now.Format "2006-01-02"}}
title: "{{ replace .Name $today "" | humanize }}"
date: {{ .Date }}
tags:
  - coding
---

[{{ replace .Name $today "" | humanize }}](#):

```python
```
