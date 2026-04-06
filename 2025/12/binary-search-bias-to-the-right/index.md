---
title: "binary search, bias to the right"
url: https://perrotta.dev/2025/12/binary-search-bias-to-the-right/
last_updated: 2026-01-03
---


Prefer:

```python
mid = left + (right - left + 1) // 2
```

Prefer:

```python
mid = (left + right + 1) // 2
```

Instead of:

```python
mid = ((left + right) // 2) + 1
```

