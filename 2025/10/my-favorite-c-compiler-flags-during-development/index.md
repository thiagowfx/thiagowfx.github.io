
Chris Wellons, [My favorite C compiler flags during development](https://nullprogram.com/blog/2023/04/29/):

> The major compilers have an enormous number of knobs. Most are highly
> specialized, but others are generally useful even if uncommon. For warnings,
> the venerable `-Wall -Wextra` is a good start, but circumstances
> improve by tweaking this warning set. This article covers high-hitting
> development-time options in GCC, Clang, and MSVC that ought to get more
> consideration.
>
> [...]
>
> **Summary**:
>
> ```
> $ cc -g3 -Wall -Wextra -Wconversion -Wdouble-promotion
>    -Wno-unused-parameter -Wno-unused-function -Wno-sign-conversion
>    -fsanitize=undefined -fsanitize-trap ...
> ```

Such a great post!

Today I learned:

> Another common mistake in tutorials is using plain old -g instead of -g3
> (read: "debug level 3"). That's like using -O instead of -O3. It adds a lot
> more debug information to the output, particularly enums and macros. The extra
> information is useful and you're better off having it!
>
> All the major build systems — CMake, Autotools, Meson, etc. — get this wrong
> in their standard debug configurations. Producing a fully-featured debug build
> from these systems is a constant battle for me. Often it's easier to ignore
> the build system entirely and cc -g3 **/*.c (plus sanitizers, etc.).

