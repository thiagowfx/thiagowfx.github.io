---
title: "LeetCode #347: Top K Frequent Elements"
date: 2026-01-10T02:09:59-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements):

With `Counter`:

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for (k, v) in Counter(nums).most_common()[:k]]
```

With `defaultdict(int)`:

```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for num in nums:
            c[num] += 1

        return [k for (k, v) in (sorted(c.items(), key=lambda item: item[1], reverse=True))[:k]]
```

With max heap:

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c = defaultdict(int)
        # for num in nums:
        #     c[num] += 1

        # return [k for (k, v) in (sorted(c.items(), key=lambda item: item[1], reverse=True))[:k]]

        counter = Counter(nums)

        class Pair:
            def __init__(self, num, freq):
                self.num = num
                self.freq = freq

            def __lt__(self, other):
                if not isinstance(other, Pair):
                    raise ValueError
                # note: > instead of < because we want the TOP elements – max heap
                return self.freq > other.freq

        pq = []

        for (num, freq) in counter.items():
            pq.append(Pair(num, freq))

        heapq.heapify(pq)

        ans = []

        for _ in range(k):
            pair = heapq.heappop(pq)
            ans.append(pair.num)

        return ans
```
