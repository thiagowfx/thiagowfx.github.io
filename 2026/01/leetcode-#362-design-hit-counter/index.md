
[LeetCode #362: Design Hit Counter](https://leetcode.com/problems/design-hit-counter):

With `Counter`:

```python
import bisect
from collections import Counter

class HitCounter:

    def __init__(self):
        self.hits = Counter()
        ## timestamp -> hits

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        ## 3 * 60 -> 2
        ## 4 * 60 -> 1
        ## getHits(8 * 60) -> 3

        ## (exclusive, inclusive)
        ## (self.hits[timestamp - 300], self.hits[timestamp])

        items = list(sorted(self.hits.items()))
        ## (timestamp, counter)

        ## inclusive
        ts_left = bisect.bisect_right(items, timestamp - 300, key=lambda item: item[0])
        ts_right = bisect.bisect_left(items, timestamp, key=lambda item: item[0])

        ans = 0

        for (timestamp, hits) in items[ts_left:]:
            ans += hits

        return ans


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

Alternatively, maintain our own sorted list of tuple:

```python
import bisect

class HitCounter:

    def __init__(self):
        self.hits = []
        ## (timestamp, hits)

    def hit(self, timestamp: int) -> None:
        i = bisect.bisect_left(self.hits, timestamp, key=lambda item: item[0])
        if i < len(self.hits) and self.hits[i][0] == timestamp:
            self.hits[i] = (timestamp, self.hits[i][1] + 1)
        else:
            self.hits.insert(i, (timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        ## 3 * 60 -> 2
        ## 4 * 60 -> 1
        ## getHits(8 * 60) -> 3

        ## (exclusive, inclusive)
        ## (self.hits[timestamp - 300], self.hits[timestamp])

        ## (timestamp, counter)

        ## inclusive
        ts_left = bisect.bisect_right(self.hits, timestamp - 300, key=lambda item: item[0])
        ts_right = bisect.bisect_left(self.hits, timestamp, key=lambda item: item[0])

        ans = 0

        for (timestamp, hits) in self.hits[ts_left:]:
            ans += hits

        return ans


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

