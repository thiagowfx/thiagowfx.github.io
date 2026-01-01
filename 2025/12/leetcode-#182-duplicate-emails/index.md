
[LeetCode #182: Duplicate Emails](https://leetcode.com/problems/duplicate-emails):

```sql
SELECT EMAIL FROM (
    SELECT EMAIL, COUNT(EMAIL) AS NUM FROM PERSON GROUP BY EMAIL
) AS _T WHERE NUM > 1;
```

