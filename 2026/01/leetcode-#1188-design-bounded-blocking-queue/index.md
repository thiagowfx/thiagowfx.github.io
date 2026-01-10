
[LeetCode #1188: Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue):

```python
from collections import deque
from threading import Lock, Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = deque()
        self.capacity = capacity
        self.lock = Lock()
        self.not_full = Condition(self.lock)
        self.not_empty = Condition(self.lock)


    def enqueue(self, element: int) -> None:
        self.not_full.acquire()

        while self.size() == self.capacity:
            self.not_full.wait()

        self.q.append(element)
        self.not_empty.notify()
        self.not_full.release()

    def dequeue(self) -> int:
        self.not_empty.acquire()

        while self.size() == 0:
            self.not_empty.wait()

        element = self.q.popleft()
        self.not_full.notify()
        self.not_empty.release()

        return element


    def size(self) -> int:
        return len(self.q)
```

