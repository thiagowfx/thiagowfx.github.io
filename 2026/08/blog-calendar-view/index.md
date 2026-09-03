---
title: "blog: calendar view"
url: https://perrotta.dev/2026/08/blog-calendar-view/
last_updated: 2026-09-03
---


**Problem statement**: my blog archive was useful, but did not show its posting
pattern over time.

I liked [Jim Nielsen's calendar view](https://blog.jim-nielsen.com/2026/blog-calendar-view/),
so I added one too. [List](/posts/) remains better for finding a post. The new
[calendar](/calendar/) is for seeing when I published.

The calendar and list use one filter. Coding, recipes, and RSS-only posts stay
out of both:

```go-html-template {filename="layouts/partials/archive-pages.html"}
{{- $pages := where .pages "Site.Language.Lang" .lang -}}
{{- $pages = where $pages "Kind" "page" -}}
{{- $pages = where $pages "Params.rss_only" "!=" true -}}
{{- $excludeCategories := slice "coding" "recipes" -}}
{{- $pages = where $pages "Params.categories" "intersect" $excludeCategories | symdiff $pages -}}
{{- return $pages -}}
```

I group posts by ISO date. A day gets a blue dot. A day with a `bestof` post
gets a yellow star. Clicking it shows every post from that date:

```go-html-template {filename="layouts/_default/calendar.html"}
{{- $postsByDate := newScratch }}
{{- range $pages }}
  {{- $key := .Date.Format "2006-01-02" }}
  {{- $dayPages := $postsByDate.Get $key | default (slice) }}
  {{- $postsByDate.Set $key ($dayPages | append .) }}
{{- end }}

<details class="calendar-day calendar-day--has-post">
  <summary>
    <span class="calendar-day--post{{ if $featured }} calendar-day--featured{{ end }}">
      {{ if $featured }}<span class="calendar-day--featured-icon">★</span>{{ end }}
    </span>
  </summary>
  <div class="calendar-popover">
    {{- range $dayPages }}
    <a href="{{ .Permalink }}">
      <span>{{ if in .Params.tags "bestof" }}★ {{ end }}{{ .Title }}</span>
    </a>
    {{- end }}
  </div>
</details>
```

It has English, Portuguese, and Italian month labels. The marker target is 24
pixels tall, and mobile uses two month columns:

```css {filename="layouts/_default/calendar.html"}
.calendar-day--has-post summary {
  width: 100%;
  min-height: 24px;
}

@media (max-width: 600px) {
  .calendar-months {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

```shell
% git show --stat --oneline 9c1db78581
9c1db78581 calendar
11 files changed, 388 insertions(+), 33 deletions(-)

% hugo --environment production
                   │  EN  │ PT  │ IT
───────────────────┼──────┼─────┼────
 Pages             │ 2968 │ 225 │ 21
Total in 8080 ms
```

