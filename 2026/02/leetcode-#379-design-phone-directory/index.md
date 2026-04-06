---
title: "LeetCode #379: Design Phone Directory"
url: https://perrotta.dev/2026/02/leetcode-%23379-design-phone-directory/
last_updated: 2026-02-23
---


[LeetCode #379: Design Phone Directory](https://leetcode.com/problems/design-phone-directory):

```python
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1

        return self.available.pop()


    def check(self, number: int) -> bool:
        return number in self.available


    def release(self, number: int) -> None:
        self.available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
```

