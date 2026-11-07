---
title: "Using cmake with the ninja generator"
date: 2015-04-19T17:37:03-03:00
tags:
  - dev
  - legacy
---

Suppose you have a [cmake](http://www.cmake.org/) `CMakeLists.txt` file, which is
pretty common for a medium-sized C/C++ project. You probably use the `make`
generator to build the project associated with this file, right?

A typical parallelized build is done as follows:

```shell
mkdir build; cd build
cmake ..
make -j$(nproc) -l$(nproc)
```

But you can also use the [ninja](https://martine.github.io/ninja/) generator
(just make sure to install it first):

```shell
mkdir build; cd build
cmake -G Ninja ..
```

This will create a couple of files in your current build directory, one of them
is a `build.ninja` – a `rules.ninja` might be created too. This is like a
`Makefile` (which is read by `make`); if you run the `ninja` program now, your
project will (probably) be built.

So, why would you use this generator if you can simply use make? This is left as
an exercise to the reader...

OK, not really. I won't advocate anything because I'm not sure of ninja is super
useful or better than make; however, you can conclude that by yourself. Here are
a couple of resources to start from:

- https://martine.github.io/ninja/manual.html
- http://jpospisil.com/2014/03/16/replacing-make-with-ninja.html
- http://www.aosabook.org/en/posa/ninja.html
- http://www.slideshare.net/cwdoh/ninja-build-simple-guide-for-beginners

Some things would work as you expect:

- `ninja clean`
- `ninja install`
- `ninja <target name>`

The project is built in a parallel fashion by default – no need to specify `-j`
flags, though you can if you want. Additionally, there are a couple of elegant
features for its final user (a.k.a. the developer). For example, you can
generate graphs of dependencies (`ninja -t graph <target name>`), which can be
processed/visualized with `graphviz`. There is also a web server which provides
interactive pages with some information about targets and its dependencies.

## Conclusion

Ninja claims to be faster than make – actually, this was the motivation behind
its creation. If you have a big project with potentially high compile times,
maybe you should experiment with it a little bit.
