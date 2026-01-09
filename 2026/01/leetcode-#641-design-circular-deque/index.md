
[LeetCode #641: Design Circular Deque](https://leetcode.com/problems/design-circular-deque):

```python
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k

        self.start = 0
        self.end = 0
        self.count = 0

        ##  .  . . .
        ## se

        ## . 1 . .
        ## s   e

        ## . 2 3 .
        ## s     e

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.q[self.start] = value
            self.start = (self.start - 1) % self.k
            self.end = (self.end + 1) % self.k
            self.count += 1
            return True

        if self.isFull():
            return False

        self.q[self.start] = value
        self.start = (self.start - 1) % self.k
        self.count += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.q[self.end] = value
            self.start = (self.start - 1) % self.k
            self.end = (self.end + 1) % self.k
            self.count += 1
            return True

        if self.isFull():
            return False

        self.q[self.end] = value
        self.end = (self.end + 1) % self.k
        self.count += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.start = (self.start + 1) % self.k
        self.count -= 1
        ## self.q[self.start] = None

        if self.count == 0:
            self.end = self.start

        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.end = (self.end - 1) % self.k
        self.count -= 1
        ## self.q[self.end] = None

        if self.count == 0:
            self.start = self.end

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.start + 1) % self.k]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.end - 1 % self.k]


    def isEmpty(self) -> bool:
        return self.count == 0


    def isFull(self) -> bool:
        return self.count == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

