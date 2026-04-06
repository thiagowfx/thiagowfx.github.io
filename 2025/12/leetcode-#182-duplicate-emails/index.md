---
title: "LeetCode #182: Duplicate Emails"
url: https://perrotta.dev/2025/12/leetcode-%23182-duplicate-emails/
last_updated: 2026-01-03
---


[LeetCode #182: Duplicate Emails](https://leetcode.com/problems/duplicate-emails):

```sql
SELECT EMAIL FROM (
    SELECT EMAIL, COUNT(EMAIL) AS NUM FROM PERSON GROUP BY EMAIL
) AS _T WHERE NUM > 1;
```

