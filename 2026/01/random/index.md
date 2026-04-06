---
title: "Random"
url: https://perrotta.dev/2026/01/random/
last_updated: 2026-01-16
---


I love to add little random features to this blog.

→ https://perrotta.dev/random

I am trying to keep the navigation bar lean...therefore, a link to `/random` was
added under the "Explore" item.

The initial implementation was very simple:

```js
<script>
  const posts = [
    {{- range $index, $page := where .Site.RegularPages "Section" "posts" }}
    {{- if $index }},{{ end }}
    "{{ $page.RelPermalink }}"
    {{- end }}
  ];
  if (posts.length > 0) {
    const randomPost = posts[Math.floor(Math.random() * posts.length)];
    window.location.replace(randomPost);
  }
</script>
```

...later on it was updated to exclude "coding" posts.

Randomness is often a great source of serendipity!

