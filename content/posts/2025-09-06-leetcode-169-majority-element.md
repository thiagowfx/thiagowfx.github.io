---
title: "LeetCode #169: Majority Element"
date: 2025-09-06T01:37:01+02:00
tags:
  - coding
---

[LeetCode #169: Majority Element](https://leetcode.com/problems/majority-element/):

## Quickly via sorting

It must appear in the middle (`(n - 1) / 2`):

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      return sorted(nums)[(len(nums) - 1) // 2]

    #     1      (n - 1) / 2
    #   a b c d
    #
    #     1
    #   a b c    (n - 1) / 2
```

Because we're sorting the list, this is `O(n * log n)`.

## Counter

Use a `Counter` to keep track of the most common element.

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      counter = Counter()
      for n in nums:
        counter[n] += 1

      ans = None
      ans_freq = float('-inf')

      for el, freq in counter.items():
        if freq > ans_freq:
          ans_freq = freq
          ans = el

      return ans
 ```

 You don't need to know about counters. A `defaultdict(int)` would suffice.

 If you can leverage built-in methods from `Counter`, then it's even simpler:

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
```

Which also makes me realize you can construct a counter straight off a list,
instead of doing it element by element.
