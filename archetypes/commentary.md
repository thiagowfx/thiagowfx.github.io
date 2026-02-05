---
{{- $today := now.Format "2006-01-02"}}
title: "Reply to: {{ replace .Name $today "" | humanize }}"
date: {{ .Date }}
categories:
  - commentary
tags:
{{- range $plural, $terms := .Site.Taxonomies }}
{{- if eq $plural "tags" }}
{{- range $term, $val := $terms }}
  - {{ printf "%s" $term }}
{{- end }}
{{- end }}
{{- end }}
external_link: "{{ getenv "HUGO_EXTERNAL_LINK" }}"
---
