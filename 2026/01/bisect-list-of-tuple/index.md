
```python
a = [(1, 3), (1, 4), (2, 5), (3, 6), (3, 7), (5, 8)]
b = [1, 1, 2, 3, 3, 5]
c = [x for (x, _) in a]
assert b == c

import bisect
assert bisect.bisect_right(b, 1) == 2
assert bisect.bisect_right(b, 3) == 5
assert bisect.bisect_right(b, 6) == len(b)

## use:
## i = bisect.bisect_right(b, 3)
## return a[i - 1][1]
```

