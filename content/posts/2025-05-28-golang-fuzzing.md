---
title: "Golang fuzzing"
date: 2025-05-28T17:37:06+02:00
tags:
  - dev
---

Given `go.mod`:

```shell
% cat go.mod
module testfuzzing

go 1.24.3
```

Given `fuzz_test.go`:

```shell
% cat fuzz_test.go
package testfuzzing

import (
        "encoding/json"
        "testing"
)

func FuzzJsonIsValid(f *testing.F) {
        f.Fuzz(func(t *testing.T, data []byte) {
                json.Valid(data)
        })
}
```

Run:

```shell
% go test -fuzz=FuzzJsonIsValid
fuzz: elapsed: 0s, gathering baseline coverage: 0/325 completed
fuzz: elapsed: 0s, gathering baseline coverage: 325/325 completed, now fuzzing with 12 workers
fuzz: elapsed: 3s, execs: 1193906 (397950/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 6s, execs: 2450910 (419012/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 9s, execs: 3720167 (423002/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 12s, execs: 4994906 (424923/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 15s, execs: 6159087 (388000/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 18s, execs: 7364384 (401883/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 21s, execs: 8588030 (407881/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 24s, execs: 9826978 (412996/sec), new interesting: 2 (total: 327)
fuzz: elapsed: 27s, execs: 11093873 (422306/sec), new interesting: 3 (total: 328)
fuzz: elapsed: 30s, execs: 12359227 (421773/sec), new interesting: 3 (total: 328)
^Cfuzz: elapsed: 31s, execs: 12650530 (403107/sec), new interesting: 3 (total: 328)
PASS
ok      testfuzzing     31.154s
go test -fuzz=FuzzJsonIsValid  286.93s user 61.51s system 1105% cpu 31.505 total
```

It's very cool (and convenient!) that golang supports fuzzing natively, and
integrated with its test framework. [Docs](https://go.dev/doc/security/fuzz/).
