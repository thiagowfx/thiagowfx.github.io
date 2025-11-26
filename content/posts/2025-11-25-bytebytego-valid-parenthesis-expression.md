---
title: "ByteByteGo: Valid Parenthesis Expression"
date: 2025-11-25T21:39:15-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Valid Parenthesis Expression](https://bytebytego.com/exercises/coding-patterns/stacks/valid-parenthesis-expression):

```python
def valid_parenthesis_expression(s: str) -> bool:
    stack = []

    for c in s:
        if c in '([{':
            stack.append(c)

        if len(stack) == 0:
            return False

        if c == ')':
            if stack.pop() != '(':
                return False

        if c == ']':
            if stack.pop() != '[':
                return False

        if c == '}':
            if stack.pop() != '{':
                return False

    return len(stack) == 0
```

Refinement:

```python
def valid_parenthesis_expression(s: str) -> bool:
    stack = []

    ass = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for c in s:
        if c in '([{':
            stack.append(c)

        if len(stack) == 0:
            return False

        if c in ')]}':
            if stack.pop() != ass[c]:
                return False

    return len(stack) == 0
```
