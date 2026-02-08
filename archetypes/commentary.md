---
{{- $today := now.Format "2006-01-02"}}
{{- $envTitle := getenv "HUGO_TITLE" }}
title: "{{ if $envTitle }}{{ $envTitle }}{{ else }}Reply to: {{ replace .Name $today "" | humanize }}{{ end }}"
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
