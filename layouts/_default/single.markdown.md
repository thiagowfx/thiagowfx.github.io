---
title: {{ .Title | jsonify }}
{{- with .Description }}
description: {{ . | jsonify }}
{{- end }}
url: {{ .Permalink }}
last_updated: {{ .Lastmod.Format "2006-01-02" }}
---

{{ .RawContent }}
