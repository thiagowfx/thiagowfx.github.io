---
title: "WebAssembly: hello world"
date: 2025-05-24T10:39:13+02:00
tags:
  - dev
  - linux
---

Today I am attending a WebAssembly workshop.

[WebAssembly](https://webassembly.org/):

> WebAssembly (abbreviated _Wasm_) is a binary instruction format for a
> stack-based virtual machine. Wasm is designed as a portable compilation target
> for programming languages, enabling deployment on the web for client and
> server applications.

Given `add.wat`:

```
(module
  ;; stack/forth syntax
  ;; looks like vanilla assembly
  (func $add (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.add
  )

  ;; nested/lisp syntax
  ;; functional, parentheses hell
  (func $add-alt (param $a i32) (param $b i32) (result i32)
    (i32.add
      (local.get $a)
      (local.get $b))
  )

  (export "add" (func $add))
  (export "addAlt" (func $add-alt))
)
```

...it adds two integers.
There are two implementations, they are equivalent.

Install dependencies:

```shell
% brew install wabt wasm-tools
```

We can compile `.wat` to `.wasm` with one of:

```shell
% wat2wasm add.wat
% wasm-tools parse add.wat -o add.wasm
```

Now how do we consume it? Create a `test.js` file:

```js
import test from "node:test";
import assert from "node:assert";
import fs from "node:fs/promises";

test("Instantiate add.wasm and call exported functions", async () => {
  const bytes = await fs.readFile("add.wasm");

  const {instance} = await WebAssembly.instantiate(bytes);

  const {add, addAlt} = instance.exports;

  assert.equal(add(1, 4), 5);
  assert.equal(addAlt(10, 40), 50);
});
```

Execute it with `node` (`brew install node`):

```shell
% node ex0.js
✔ Instantiate add.wasm and call exported functions (4.1875ms)
ℹ tests 1
ℹ suites 0
ℹ pass 1
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 7.125625
```

Explanation:

- `bytes` reads the `.wasm` file, nothing special
- [`WebAssembly.instantiate`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/instantiate_static):
  compile and instantiate WebAssembly code
- access its
  [`exports`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module/exports_static)
  field

## References

- [WebAssembly from the Ground up](https://wasmgroundup.com/) by Mariano Guerra
  & Patrick Dubroy
  - [Workshop](https://wasmgroundup.com/workshop/)
- [WebAssembly Core
  Specification](https://www.w3.org/TR/2019/REC-wasm-core-1-20191205/)
