---
title: "LeetCode #904: Fruit Into Baskets"
date: 2025-12-28T04:22:09-03:00
categories:
  - coding
---

[LeetCode #904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets):

The problem statement is a bit confusing.

Once understood, it's a DP problem.

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from functools import cache

        n = len(fruits)

        @cache
        def solve(i, choices):
            if i < 0:
                return 0

            # take if possible
            a = None
            if len(choices) < 2 or fruits[i] in choices:
                a = 1 + solve(i - 1, tuple(set(choices + (fruits[i],))))

            # do not take
            # this is only a valid choice in the beginning
            b = None
            if len(choices) == 0:
                b = 0 + solve(i - 1, choices)

            return max(el for el in (a, b, 0) if el is not None)

        return solve(n - 1, tuple())
```

For memoization we need a tuple. We cannot use a list or a set.

This is a handy pattern to extract the `max` of a tuple/list when certain of its
elements can be `None`:

```python
max(el for el in (a, b, 0) if el is not None)
```
