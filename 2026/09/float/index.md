---
title: "float"
url: https://perrotta.dev/2026/09/float/
last_updated: 2026-09-07
---


```python
from math import floor, ceil

assert floor(3.5) == 3
assert ceil(3.5) == 4

assert floor(3) == 3
assert ceil(3) == 3

assert float(3.4).__round__() == 3
assert round(3.4) == 3
assert round(3.7) == 4
```

