---
title: "TV Shows"
url: https://perrotta.dev/2026/08/tv-shows/
last_updated: 2026-08-31
---


[Previously]({{< ref "2026-08-24-books" >}}).

I added a [TV shows](/tv-shows/) page with a sample of my favorites, inspired
by [Michael Harley's watching page](https://michaelharley.net/watching/) and
[Michael Stapelberg's series page](https://michael.stapelberg.ch/series/).

The list lives in YAML. Trakt keeps my full watch history; this file stays
small, alphabetical, and intentionally incomplete:

```yaml {filename="data/tv-shows.yaml"}
shows:
  # keep-sorted start case=no by_regex=title:\s+"?([^"]+)
  - title: 13 Reasons Why
    years: 2017–2020
    seasons: 4
    url: https://www.themoviedb.org/tv/66788-13-reasons-why
    cover: https://media.themoviedb.org/t/p/w500/nel144y4dIOdFFid6twN5mAX9Yd.jpg
  - title: 3%
    years: 2016–2020
    seasons: 4
    url: https://www.themoviedb.org/tv/68467-3
    cover: https://media.themoviedb.org/t/p/w500/uLBJSLuAQ8UqLIKZVWG3uNEXwjt.jpg
  # keep-sorted end
```

A custom Hugo layout turns each record into a poster card. Show details and
posters come from [The Movie Database](https://www.themoviedb.org/):

```go-html-template {filename="layouts/_default/tv-shows.html"}
<div class="tv-shows-grid">
  {{- range $data.shows }}
  <div class="tv-shows-item">
    <a href="{{ .url }}" title="{{ .title }} ({{ .years }})">
      <img class="tv-shows-cover" src="{{ .cover }}" alt="Poster for {{ .title }}" loading="lazy" decoding="async" referrerpolicy="no-referrer">
      <div class="tv-shows-item-title">{{ .title }}</div>
    </a>
    <div class="tv-shows-item-meta">
      {{ .years }} &middot; {{ .seasons }} {{ cond (eq .seasons 1) "season" "seasons" }}
    </div>
  </div>
  {{- end }}
</div>
```

The data has a JSON schema, and the page now sits next to Books in the More
menu:

```shell
% git show --stat --oneline 97dc4bde16
97dc4bde16 add TV shows page
6 files changed, 305 insertions(+), 3 deletions(-)
```

TV show recommendations are almost always welcome.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

