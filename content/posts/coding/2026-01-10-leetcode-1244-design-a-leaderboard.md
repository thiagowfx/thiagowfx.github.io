---
title: "LeetCode #1244: Design A Leaderboard"
date: 2026-01-10T00:12:45-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1244: Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard):

With Counter:

```python
from collections import Counter

class Leaderboard:

    def __init__(self):
        self.counter = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.counter[playerId] += score

    def top(self, K: int) -> int:
        return sum(v for (k, v) in self.counter.most_common()[:K])

    def reset(self, playerId: int) -> None:
        del self.counter[playerId]
        ## self.counter[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```

With priority queue (heap):

```python
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.d = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.d[playerId] += score

    def top(self, K: int) -> int:
        pq = []

        for score in self.d.values():
            heapq.heappush(pq, score)
            if len(pq) > K:
                heapq.heappop(pq)

        return sum(pq)

    def reset(self, playerId: int) -> None:
        del self.d[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```
