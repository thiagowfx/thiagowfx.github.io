---
{{- $today := now.Format "2006-01-02"}}
title: "{{ replace .Name $today "" | humanize }}"
date: {{ .Date }}
tags:
{{- range $plural, $terms := .Site.Taxonomies }}
{{- range $term, $val := $terms }}
  - {{ printf "%s" $term }}
{{- end }}
{{- end }}
---

<!--more-->
