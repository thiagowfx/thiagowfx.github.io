<!-- markdownlint-disable -->
{{/* Semantic sitemap in markdown for AI agent discovery. */}}

# Sitemap — {{ .Site.Title }}

> {{ .Site.Params.description }}

## Pages

{{ range where .Site.Pages "Kind" "page" }}{{ if eq .Section "" }}
- [{{ .Title }}]({{ .Permalink }}){{ with .Description }}: {{ . }}{{ end }}
{{- end }}{{ end }}

## Blog Posts

{{ range where .Site.RegularPages "Section" "posts" }}
- [{{ .Title }}]({{ .Permalink }}) ({{ .Date.Format "2006-01-02" }}){{ with .Description }}: {{ . }}{{ end }}
{{- end }}

## Tags

{{ range .Site.Taxonomies.tags }}
- [{{ .Page.Title }}]({{ .Page.Permalink }}) ({{ .Count }} posts)
{{- end }}
