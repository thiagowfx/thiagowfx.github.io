---
title: "LeetCode #2666: Allow One Function"
date: 2026-01-06T13:25:51-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2666: Allow One Function](https://leetcode.com/problems/allow-one-function):

Closure:

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let called = false;

    return function (...args) {
        if (!called) {
            called = true;
            return fn(...args);
        }
    };
}

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
```
