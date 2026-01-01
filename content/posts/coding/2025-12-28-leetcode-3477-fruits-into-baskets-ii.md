---
title: "LeetCode #3477: Fruits Into Baskets II"
date: 2025-12-28T03:55:14-03:00
categories:
  - coding
---

[LeetCode #3477: Fruits Into Baskets II](https://leetcode.com/problems/fruits-into-baskets-ii):

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        assert len(fruits) == len(baskets)

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    fruits[i] = baskets[j] = 0
                    break

        return sum(1 for fruit in fruits if fruit > 0)
```

Optimized:

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        assert len(fruits) == len(baskets)

        unplaced = 0

        for i in range(len(fruits)):
            not_found = True
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    fruits[i] = baskets[j] = 0
                    not_found = False
                    break
            unplaced += int(not_found)

        return unplaced
```
