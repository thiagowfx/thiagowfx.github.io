---
title: "deque"
url: https://perrotta.dev/2026/01/deque/
last_updated: 2026-01-11
---


```python
from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
assert d == deque([2, 1])
assert list(d) == [2, 1]

d.popleft()
assert d == deque([1])

d = deque(range(4))
d.rotate(1)
assert d == deque([3, 0, 1, 2])

d = deque(range(4))
d.rotate(-1)
assert d == deque([1, 2, 3, 0])

d = deque(maxlen=3)
d.extend(range(4))
assert d == deque([1, 2, 3])
```

