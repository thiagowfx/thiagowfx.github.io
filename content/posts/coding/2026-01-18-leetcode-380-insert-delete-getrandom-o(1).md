---
title: "LeetCode #380: Insert Delete GetRandom O(1)"
date: 2026-01-18T02:54:25-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #380: Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o(1)):

Initial solution:

```python
import random

class RandomizedSet:

    def __init__(self):
        self.l = []

        self.d = {}
        ## self.d = dict()

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True

        return False


    def remove(self, val: int) -> bool:
        if val in self.d:
            del self.d[val]
            ## self.l: do not touch. Removal is O(n)
            return True

        return False


    def getRandom(self) -> int:
        return random.choice(list(self.d.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

However, `getRandom()` is `O(n)`.

Better solution:

```python
import random

class RandomizedSet:

    def __init__(self):
        self.l = []

        self.d = {}
        ## self.d = dict()

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True

        return False


    def remove(self, val: int) -> bool:
        if val in self.d:
            i = self.d[val]
            del self.d[val]

            del self.l[i]
            return True

        return False


    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

But it's still `O(n)` because of the list deletion.

Even better:

```python
import random

class RandomizedSet:

    def __init__(self):
        self.l = []

        self.d = {}
        ## self.d = dict()

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True

        return False


    def remove(self, val: int) -> bool:
        if val in self.d:
            i = self.d[val]
            del self.d[val]

            # swap with the last element
            self.l[i], self.l[len(self.l) - 1] = self.l[len(self.l) - 1], self.l[i]
            self.l = self.l[:-1]
            ## self.l.pop()

            swapped_val = self.l[i]
            self.d[swapped_val] = i

            return True

        return False


    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
