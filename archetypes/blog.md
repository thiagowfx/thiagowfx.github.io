---
{{- $today := now.Format "2006-01-02"}}
title: "{{ replace .Name $today "" | humanize }}"
date: {{ .Date }}
categories:
{{- range $plural, $terms := .Site.Taxonomies }}
{{- if eq $plural "categories" }}
{{- range $term, $val := $terms }}
  - {{ printf "%s" $term }}
{{- end }}
{{- end }}
{{- end }}
tags:
{{- range $plural, $terms := .Site.Taxonomies }}
{{- if eq $plural "tags" }}
{{- range $term, $val := $terms }}
  - {{ printf "%s" $term }}
{{- end }}
{{- end }}
{{- end }}
---
