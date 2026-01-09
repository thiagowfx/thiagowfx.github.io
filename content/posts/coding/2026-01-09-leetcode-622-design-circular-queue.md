---
title: "LeetCode #622: Design Circular Queue"
date: 2026-01-09T04:35:00-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #622: Design Circular Queue](https://leetcode.com/problems/design-circular-queue):

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k

        self.start = 0
        self.end = 0
        self.count = 0

    ## -- queue

    ## .   .  .
    ## se

    ## 1   .  .
    ## s      e

    ## 1   .  2
    ## s   e

    ## --  dequeue

    ## 1 . 2
    ## s e

    ## . . 2
    ##   e s

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.end] = value
        self.end = (self.end - 1) % self.k
        self.count += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.start = (self.start - 1) % self.k
        self.count -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.start]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[(self.end + 1) % self.k]


    def isEmpty(self) -> bool:
        return self.count == 0


    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
