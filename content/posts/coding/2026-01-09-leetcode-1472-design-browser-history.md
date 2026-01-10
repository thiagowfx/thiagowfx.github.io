---
title: "LeetCode #1472: Design Browser History"
date: 2026-01-09T22:07:44-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1472: Design Browser History](https://leetcode.com/problems/design-browser-history):

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

        # example.com <-
        #   example.org
        #     foo.example.com <=


    def visit(self, url: str) -> None:
        if self.pos == (len(self.history) - 1):
            self.history.append(url)
            self.pos += 1
        else:
            self.pos += 1
            self.history[self.pos] = url
            self.history = self.history[:self.pos + 1]


    def back(self, steps: int) -> str:
        steps = min(steps, self.pos)
        self.pos -= steps
        return self.history[self.pos]


    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.history) - 1 - self.pos)
        self.pos += steps
        return self.history[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```
