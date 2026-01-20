---
title: "LeetCode #2166: Design Bitset"
date: 2026-01-20T22:20:59+01:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2166: Design Bitset](https://leetcode.com/problems/design-bitset):

Time limit exceeded:

```python
class Bitset:

    def __init__(self, size: int):
        self.bits = [False] * size


    def fix(self, idx: int) -> None:
        self.bits[idx] = 1


    def unfix(self, idx: int) -> None:
        self.bits[idx] = 0


    def flip(self) -> None:
        self.bits = [not bit for bit in self.bits]


    def all(self) -> bool:
        return all(self.bits)


    def one(self) -> bool:
        return any(self.bits)


    def count(self) -> int:
        return len([bit for bit in self.bits if bit])


    def toString(self) -> str:
        return ''.join('1' if bit else '0' for bit in self.bits)



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
```

Optimized:

```python
class Bitset:

    def __init__(self, size: int):
        self.bits = [False] * size
        self.ones = 0
        self.flipped = False


    def fix(self, idx: int) -> None:
        if self.flipped:
            # When flipped, fixing means setting underlying bit to 0
            if self.bits[idx]:
                self.bits[idx] = False
                self.ones -= 1
        else:
            # Normal case: set to 1
            if not self.bits[idx]:
                self.bits[idx] = True
                self.ones += 1


    def unfix(self, idx: int) -> None:
        if self.flipped:
            # When flipped, unfixing means setting underlying bit to 1
            if not self.bits[idx]:
                self.bits[idx] = True
                self.ones += 1
        else:
            # Normal case: set to 0
            if self.bits[idx]:
                self.bits[idx] = False
                self.ones -= 1


    def flip(self) -> None:
        self.flipped = not self.flipped


    def all(self) -> bool:
        if self.flipped:
            return self.ones == 0
        else:
            return self.ones == len(self.bits)


    def one(self) -> bool:
        if self.flipped:
            # When flipped, we need at least one 0 in underlying array (which becomes 1)
            return self.ones < len(self.bits)
        else:
            return self.ones > 0


    def count(self) -> int:
        if self.flipped:
            return len(self.bits) - self.ones
        else:
            return self.ones


    def toString(self) -> str:
        if self.flipped:
            return ''.join('0' if bit else '1' for bit in self.bits)
        else:
            return ''.join('1' if bit else '0' for bit in self.bits)
```
