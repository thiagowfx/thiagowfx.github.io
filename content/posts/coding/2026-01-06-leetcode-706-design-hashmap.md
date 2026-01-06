---
title: "LeetCode #706: Design HashMap"
date: 2026-01-06T16:41:59-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #706: Design HashMap](https://leetcode.com/problems/design-hashmap):

Shortcut:

```python
class MyHashMap:

    def __init__(self):
        self.m = {}

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.m:
            del self.m[key]
```

Proper:

```python
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.s = [[] for _ in range(self.size)]

    def hash(self, key):
        assert isinstance(key, int)
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.s[self.hash(key)]

        for (i, (k, v)) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.s[self.hash(key)]

        for (k, v) in bucket:
            if k == key:
                return v

        return -1


    def remove(self, key: int) -> None:
        bucket = self.s[self.hash(key)]

        for (i, (k, v)) in enumerate(bucket):
            if k == key:
                del bucket[i]
                break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.s = [[] for _ in range(self.size)]

    def hash(self, key):
        assert isinstance(key, int)
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.s[self.hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.s[self.hash(key)]
        if key in bucket:
            del bucket[bucket.index(key)]

    def contains(self, key: int) -> bool:
        bucket = self.s[self.hash(key)]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```
