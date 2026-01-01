# Plan: Convert Coding to Category

## Problem
`/categories/` page exists but is empty. Need to make it meaningful by treating "coding" as a proper category.

## Solution: Restructure Posts by Category

### 1. Convert "coding" from tag to category
- Move all posts tagged with "coding" to a separate directory
- Use Hugo's directory-based category structure

### 2. Reorganize content structure

#### English posts
- Keep general posts under `content/posts/`
- Move coding posts to `content/posts/coding/`

#### Portuguese posts
- Keep general posts under `content/pt/posts/`
- Move coding posts to `content/pt/posts/coding/`

### 3. Update Hugo config
```yaml
taxonomies:
  tag: tags
  category: categories
```

### 4. Remove "coding" tag
- Remove "coding" from all post frontmatter
- Use categories (via directory structure) for coding posts instead
- Reserve tags for actual topics: dev, meta, privacy, serenity, etc.

## Benefits
- `/categories/` page becomes meaningful (shows "Coding" category)
- `/tags/` shows only topic-based tags
- Cleaner organizational separation
- Proper Hugo taxonomy usage
