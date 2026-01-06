
[LeetCode #2336: Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set):

```python
class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()

    def popSmallest(self) -> int:
        if not self.removed:
            self.removed.add(1)
            return 1

        n = len(self.removed)
        t = set(range(1, n + 2))
        m = min(t - self.removed)

        self.removed.add(m)
        return m

        ## t - self.removed
        ##
        ## {1, 2, 3, 4} - {1, 2, 3}
        ##
        ## or
        ##
        ## {1, 2, 3} - {2, 4}


    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

