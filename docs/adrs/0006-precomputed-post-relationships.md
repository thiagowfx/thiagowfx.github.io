# ADR-0006: Pre-computed Post Relationships

## Status

Accepted

## Date

2026-01-18

## Context

Hugo build times were slow (~18 seconds) due to O(n²) template computations:

| Partial              | Cumulative Time | Avg/Call | Calls |
| -------------------- | --------------- | -------- | ----- |
| `related-posts.html` | 64s             | 62ms     | 1020  |
| `backlinks.html`     | 16s             | 15ms     | 1020  |
| `previously.html`    | 8s              | 8ms      | 1020  |

Each partial performed regex operations across all ~1000 posts to find relationships:

- **Backlinks**: Scan all posts for `ref` shortcodes linking to current post
- **Related posts**: Score all posts by title words, tags, categories, bidirectional links
- **Previously**: Find older posts with shared tags (jwz-style)
- **Graph visualization**: Build nodes/edges for D3.js force-directed graph

With 1000+ posts, this resulted in ~1 million regex operations per build.

## Decision

Pre-compute all post relationships in a Python script, output to `data/links.json`,
and have Hugo templates perform O(1) lookups instead of O(n²) computations.

### Implementation

**1. Python script (`ci/precompute_links.py`)**

Runs in ~4 seconds and outputs:

```json
{
  "posts": {
    "2024-01-01-post-slug": {
      "hugo_path": "/posts/2024-01-01-post-slug",
      "backlinks": ["other-post-1", "other-post-2"],
      "related": ["related-post-1", "related-post-2"],
      "previously": ["prev-1", "prev-2", "prev-3", "prev-4", "prev-5"]
    }
  },
  "paths": {
    "2024-01-01-post-slug": "/posts/2024-01-01-post-slug"
  },
  "graph": {
    "nodes": [{"id": "...", "hugo_path": "...", "title": "...", "date": "..."}],
    "edges": [{"source": "...", "target": "..."}]
  }
}
```

**2. Updated Hugo templates**

Partials now read from `$.Site.Data.links`:

```go-html-template
{{- $linkData := index $.Site.Data.links.posts $currentFilename -}}
{{- $backlinkIds := $linkData.backlinks | default slice -}}
{{- $paths := $.Site.Data.links.paths -}}
{{- range $backlinkIds -}}
  {{- $page := $.Site.GetPage (index $paths .) -}}
  ...
{{- end -}}
```

**3. Build integration**

`just build` now runs `precompute` before Hugo:

```just
precompute:
    python3 ci/precompute_links.py

build: precompute
    hugo --environment production --gc
```

### Alternatives Considered

1. **Hugo's `partialCached`**: Only caches within a single build, doesn't help with O(n²)
2. **Lazy-load via JavaScript**: Implemented for graph page, but partials need server-side data
3. **Skip in development**: Implemented initially, but pre-compute approach is fast enough

## Consequences

### Performance Results

| Metric             | Before | After  | Improvement |
| ------------------ | ------ | ------ | ----------- |
| `just build` total | ~18s   | ~8s    | 2.2x faster |
| Hugo only          | ~18s   | ~2.7s  | 6.7x faster |
| `just watch`       | ~10s   | ~2.6s  | 3.8x faster |

| Partial              | Before    | After       | Speedup |
| -------------------- | --------- | ----------- | ------- |
| `related-posts.html` | 62ms/call | 0.2ms/call  | 310x    |
| `backlinks.html`     | 15ms/call | 0.02ms/call | 750x    |
| `previously.html`    | 8ms/call  | 0.1ms/call  | 80x     |

### Easier

- Faster development iteration with `just watch`
- Production builds complete in ~8 seconds
- Graph visualization works with all 1000+ posts
- Centralized relationship logic in one Python script

### Harder

- New posts require running `just precompute` or `just build` to update relationships
- Data can become stale if `data/links.json` isn't regenerated
- Two-step build process (Python + Hugo)

### Current Limitations

Adding a new post still requires full recomputation (~4 seconds) because:

- Related posts: O(n²) to score each post against all others
- Previously: O(n²) to check tag overlap with older posts
- Backlinks: O(n) to rebuild reverse index

## Future Improvements

### 1. Incremental Updates

Detect changed files via `git diff` and only recompute affected relationships:

```python
changed_files = get_git_diff()
for post_id in changed_files:
    update_outlinks(post_id)
    update_backlinks_for_targets(post_id)
    update_related_for_affected(post_id)
```

**Estimated complexity**: O(changed × n) instead of O(n²)

### 2. Indexed Tag/Category Lookups

Pre-build inverted indexes for faster related/previously computation:

```python
tag_index = {"python": ["post-1", "post-2"], "hugo": ["post-3"]}
category_index = {"coding": ["post-1"], "meta": ["post-2"]}
```

**Benefit**: O(1) lookup for posts sharing tags instead of O(n) scan

### 3. Approximate Related Posts

Use locality-sensitive hashing or pre-computed embeddings for semantic similarity
instead of exact title word matching.

**Trade-off**: Less accurate but O(1) per post

### 4. Watch Mode Integration

Run incremental pre-compute when files change during `just watch`:

```just
watch:
    hugo server --watch &
    fswatch content/posts | xargs -I {} python3 ci/precompute_links.py --incremental {}
```

### 5. Parallel Computation

Use Python multiprocessing for related/previously calculations:

```python
with Pool() as p:
    results = p.map(compute_related, posts)
```

**Estimated speedup**: 2-4x on multi-core machines
