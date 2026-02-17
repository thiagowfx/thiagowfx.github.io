---
title: "Matlab debootstrapping #1"
date: 2014-11-18T21:45:00-03:00
tags:
  - dev
  - legacy
---

Alternative title: "Matlab, second impressions". I am trying to learn Matlab
super fast for prototyping purposes. Fast learning isn't my preferred style for
approaching a new programming language. However, this is necessary at the
moment.

**Disclaimer**: This is not a tutorial. Just annotations and notes. Information
is not necessarily correct, so consume it at your own risk.

## Matlab Paradise

- Everything is optimized for matrices and vectors. Matlab means "matrix laboratory".
- A number is treated as a 1x1 matrix. This is really interesting and has nice implications and syntactic sugar.
- **Matrix manipulation**: `A = [1,2,3]` is a row vector; `B = [1;2;3]` is a column vector; `C = [1,2;3,4]` mixes them together.
- **Slicing**: Python style, but with different syntax. `1:10` means `range(1,10)` and `1:2:5` means `range(1,5,2)` but Matlab is inclusive (5 is present).
- **Indexing vectors**: `A(1,2)`, `A(2,1)`. Beware: indexes begin from 1, not zero.
- **Performance**: slow, slow, slow. See benchmarks on Julia's homepage.
- `matlab -nodesktop` for command-line prompt. Self-contained, and you can still browse help with `doc lu` or `help lu`.
- **Introspection #1**: `whos`. Know everything about your variables.
- **Workspace view**: Really nice. Save variables with `save out.mat`. Load them with `load out.mat`.
- Some Unix goodness is available: `ls`, `cd`, `pwd`, `ls -l`.
- However, `mkdir` and `rmdir` work differently.
- **Hello, world!**: `fprintf('string here')` or `display('hello, world!')`.
- Strings are enclosed with single quotes, not double. Why?
- **Functions**: C/C++/Java style. `f(a,b,c,d,e)`.
- Some functions have more than one return value: `ret1, ret2 = f(a,b,c)`.
- Clear screen: `C-l` or `clc`.
- **Beware!** `clear` deletes your variables. `clear var` is more specific. `clear all` is even more destructive.
- Auto-completion with TAB. No `C-Space`.
- Need help? `lu(` then F1. Hints? `C-F1`.
- Matlab hotkeys seem optimized for emacs users. See `C-y` (yank/paste), `C-k` (kill/copy), `C-a` and `C-e` (navigation), `C-s` (search), `C-_` (undo).
- `open file.m` to open files without the fancy GUI.
- `delete file.m`. Not `rm`.
- Comments with percent sign (%). Why not hashes?
- Run a Matlab script: `cd` into its directory then type `file<CR>` in the prompt.
- `version`! R2014a == 8.3.0.x
- `C-c` for long computations.
- `rand(2,2)` if you ran out of creativity for numbers.
- `v = [1 2]` equals `v = [1,2]`. Who needs commas?
- Element-wise operators are preceded with a dot. Example: `.*`.
- Love intelligent prompts: `C-p`, `M-p`, `C-n`, `M-n`, `<UP>`, `<DOWN>`.
- Miss your shell? `system('echo Hello world!')`.
- File handling: `fid = fopen('file.txt','w'); fprintf(fid,'...'); fclose(fid);`

## Introspection

- `which lu.m`, `which lu`
- `edit lu.m`, `edit lu`
- `help <command>` spits output
- `doc <command>` opens help browser
- `whos` shows your variables and symbols and functions
- `type <command>`. Like Unix's `cat`.
- Try double-clicking on a variable in your workspace
- `path`

## Internals: Functions, variables, types, control flow

- `sum(a), min(a), max(a), median(a), var(a), prod(a), mean(a), size(a), mode(a), std(a)`
- `false` is 0. `true` is 1. Case sensitive!
- `isvector(a), isempty(a)`
- Not is a tilde `~`, not `!` (C-style)
- **Matrix indexing**: Column 2: `a(:,2)`; Line 2: `a(2,:)`.
- `inv(a)` for inverse
- `find (a < 3)` filter
- `2^3 == 8`
- Quick matrix generation: `zeros, ones, eye, magic, rand`
- Math: `cos(pi), sin(pi), tan(pi), tanh(pi)`
- More math: `rad2deg(pi) == 180, deg2rad`
- `det(m), rank(m), trace(m), a,b = lu(m)`
- `if, elseif, else, end`. No parenthesis required.
- `for k=1:10; display('hey'); end`
- `while`
- `switch b; case 1; display('one'); end`. No colon after cases.

## Symbolic math library/toolbox

- `syms x y z` shorthand for `x = sym('x')`
- `x = sym('x', [2 1])` for a symbolic column vector
- `f = x + y^2` symbolic function
- `subs(f, [x y], [1 2])` evaluates the function
- `gradient(f), hessian(f), ccode(f)` magic functions!

## Fancy stuff

- `diary on`, `diary off`, `help diary` to record terminal sessions
