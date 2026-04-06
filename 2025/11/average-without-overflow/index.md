---
title: "average without overflow"
url: https://perrotta.dev/2025/11/average-without-overflow/
last_updated: 2026-01-03
---


With potential overflow:

```python
mid = (left + right) // 2
```

With no overflow:

```python
mid = left + (right - left) // 2
```

