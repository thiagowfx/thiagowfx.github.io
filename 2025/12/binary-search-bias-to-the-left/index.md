---
title: "binary search, bias to the left"
url: https://perrotta.dev/2025/12/binary-search-bias-to-the-left/
last_updated: 2026-01-03
---


Prefer:

```python
mid = left + (right - left) // 2
```

Instead of:

```python
mid = (left + right) // 2
```

...to avoid a potential integer overflow.

Not a real concern in Python, but still a best, defensive practice.

