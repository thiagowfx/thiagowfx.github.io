---
title: "LeetCode #359: Logger Rate Limiter"
date: 2026-01-06T23:45:02-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #359: Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter):

```python
class Logger:

    def __init__(self):
        self.log = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log:
            self.log[message] = timestamp
            return True

        if timestamp - self.log[message] <= 10:
            return False

        self.log[message] = timestamp
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
```
