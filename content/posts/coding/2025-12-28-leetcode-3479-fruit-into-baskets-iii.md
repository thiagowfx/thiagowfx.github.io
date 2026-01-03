---
title: "LeetCode #3479: Fruit Into Baskets III"
date: 2025-12-28T04:56:30-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #3479: Fruit Into Baskets III](https://leetcode.com/problems/fruit-into-baskets-iii):

```python
import math

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        def chunk_list(l, size):
            return [l[i:i + size] for i in range(0, len(l), size)]

        chunk_size = int(math.sqrt(len(baskets)))
        chunks = chunk_list(baskets, chunk_size)

        max_chunks = []
        for chunk in chunks:
            max_chunks.append(max(chunk))

        unplaced = 0

        for i in range(len(fruits)):
            not_found = 1

            for j, max_chunk in enumerate(max_chunks):
                if max_chunk < fruits[i]:
                    continue

                for k, b in enumerate(chunks[j]):
                    if b >= fruits[i]:
                        chunks[j][k] = 0
                        not_found = 0
                        max_chunks[j] = max(chunks[j])
                        break

                if not_found == 0:
                    break

                # 6
                # [[4, 5, 6 -> 0, 7], ...]
                # [7, ...]

            unplaced += not_found

        return unplaced
```

A handy pattern to split a list into chunks of size `size`:

```python
def chunk_list(l, size):
    return [l[i:i + size] for i in range(0, len(l), size)]
```

For example:

```python
assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
```

A bit optimized, avoid the inner `max` chunk extra subarray pass:

```python
import math

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        def chunk_list(l, size):
            return [l[i:i + size] for i in range(0, len(l), size)]

        chunk_size = int(math.sqrt(len(baskets)))
        chunks = chunk_list(baskets, chunk_size)

        max_chunks = []
        for chunk in chunks:
            max_chunks.append(max(chunk))

        unplaced = 0

        for i in range(len(fruits)):
            not_found = 1

            for j, max_chunk in enumerate(max_chunks):
                if max_chunk < fruits[i]:
                    continue

                max_c = float('-inf')
                for k, b in enumerate(chunks[j]):
                    if b >= fruits[i] and not_found:
                        chunks[j][k] = 0
                        not_found = 0
                        continue

                    max_c = max(max_c, b)

                max_chunks[j] = max_c

                if not_found == 0:
                    break

                # 6
                # [[4, 5, 6 -> 0, 7], ...]
                # [7, ...]

            unplaced += not_found

        return unplaced
```
