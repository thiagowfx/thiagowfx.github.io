---
title: "LeetCode #692: Top K Frequent Words"
date: 2026-01-11T10:26:15-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words):

```python
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ## return [word for (word, freq) in Counter(words).most_common()][:k]

        by_freq = defaultdict(list)

        for (word, freq) in Counter(words).most_common():
            by_freq[freq].append(word)

        ans = []

        for (freq, words) in sorted(by_freq.items(), reverse=True):
            ans.extend(sorted(words))
            if len(ans) >= k:
                break

        return ans[:k]
```
