---
title: "LeetCode #182: Duplicate Emails"
date: 2025-12-24T16:59:41-03:00
tags:
  - coding
rss: false
---

[LeetCode #182: Duplicate Emails](https://leetcode.com/problems/duplicate-emails):

```sql
SELECT EMAIL FROM (
    SELECT EMAIL, COUNT(EMAIL) AS NUM FROM PERSON GROUP BY EMAIL
) AS _T WHERE NUM > 1;
```
