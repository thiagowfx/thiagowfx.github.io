
[LeetCode #346: Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream):

Use a `deque`:

```python
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.coll = deque()

    def next(self, val: int) -> float:
        if len(self.coll) == self.size:
            self.coll.popleft()

        self.coll.append(val)

        return sum(self.coll) / len(self.coll)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

Or avoiding computing the `sum` all the time:

```python
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.mysum = 0
        self.coll = deque()

    def next(self, val: int) -> float:
        if len(self.coll) == self.size:
            self.mysum -= self.coll.popleft()

        self.mysum += val
        self.coll.append(val)

        return self.mysum / len(self.coll)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

