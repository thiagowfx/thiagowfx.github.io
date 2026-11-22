---
title: "FAQFlow #4: OpenMPI: notes"
date: 2015-04-20T22:23:18-03:00
tags:
  - dev
  - legacy
---

**Note**: this is just for future reference. Sometimes [^1] [^2] I create posts
of this nature to serve as summaries of broad topics I might need later on.
Because, in a few {months,years}, the future Thiago won't remember what the
current one was thinking...and, of course, I take those opportunities to share
knowledge as well.

## OpenMPI (and some OpenMP)

- OpenMPI is like OpenMP in the sense that they both are standards: sponsored,
  endorsed and maintained by a bunch of important corporations.
- OpenMP has something to do with parallelization, and doesn't necessarily
  involve multiple machines. In particular, MP stands for *multiprocessing*[^3].
  It is like an add-on to the compiler, to take advantage of multiple
  processing cores available on several machines nowadays. Keyword: **shared
  memory**.
- OpenMPI, in the other hand, is more like an API (a particular case of MPI),
  and is something that has been created for the purpose of having a common
  interface to pass messages between different computers (computing cores, for
  that matter). Keyword: **distributed memory**. You write a single program,
  which is run by all nodes(computers); however, each computer is uniquely
  assigned a number, so you can orchestrate the processing logic{,power} through
  them all.
- Both support C, C++ and FORTRAN.
- OpenMPI uses mainly the "mpi.h" header, and it usually uses a wrapper compiler
  (e.g. mpic++) which calls an underlying compiler (for example: `g++`, `clang++`,
  or the Intel compiler) which does the actual compilation. Why this wrapper? To
  encapsulate libraries and directories – the developer has no need to worry
  about `-L`, `-I`, or `-l` flags. The CXX environment variable can be used to define
  the underlying compiler, but this is not usually necessary.
- OpenMP is hooked to the compiler: you don't have to care about anything
  besides adding a few compile directives (`#pragma`) to your code. Keyword:
  **thread parallelism**. Because of this, data racing is common.

Still confused?[^4] might help.

## OpenMPI, innocuous example

```cpp
/* hello.cpp */
#include
int main() {
  std::cout << "Hello, world!" << std::endl;
  return 0;
}
```

Now, you would normally run this program with:

```shell
g++ hello.cpp -o hello && ./hello
```

What would you do with OpenMPI? Nothing fancy, really:

```shell
mpic++ hello.cpp -o hellompi && ./hellompi
```

This will call `g++` under the hood (supposing there are no other recognized C++
compilers on the system), but adding a few command-line flags to make it
understand the MPI world. Of course, this example doesn't contain anything which
actually uses MPI. But, in fact, you can inspect they produce different
executables:

```shell
sdiff <(strings hello) <(strings hellompi)
# or, alternatively, use `diff -uN`
# you'll see a few additional strings in the hellompi executable specific to OpenMPI
```

## OpenMPI, real example

Credits for the source: on[^3].

```cpp
/* example.cpp */
#include
#include
int main(int argc, char *argv[]) {
    int rank; // id
    int size; // number of processors

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    std::cout << "Hello from " << rank << std::endl;
    MPI_Finalize();
}
```

Let's proceed...

```shell
mpic++ example.cpp -o example
# note: if you try to compile this example with g++...well, then you're screwed, as it won't work out-of-the-box -- you would have to add the required compile flags manually
```

Then run it:

```shell
# naive: this will do nothing special
$ ./example
Hello from 0

# this is where the magic happens
# no need to specify it as "./example"; just use the executable name
$ mpirun -np 4 example
Hello from 0
Hello from 1
Hello from 2
Hello from 3
```

I ran it a few times and the order in which the lines were printed occasionally
became different. You can use "400" instead of "4"...no problem. My load average
became "100"...whoa!!! Okay, a more lightweight example is "10":

```shell
$ mpirun -np 10 example
Hello from 5
Hello from 3
Hello from 4
Hello from 0
Hello from 8
Hello from 7
Hello from 9
Hello from 2
Hello from 6
Hello from 1
```

You don't have to have the number of cores of the argument you pass to the -np
flag. This just specifies the number of processes you'll spawn. When I just run
"mpirun example", without the -np argument, only two lines are printed. My
ultrabook has two physical cores and two threads per core (2 x 2 = 4 virtual
processors), so I believe mpirun picked the number of physical cores from my
computer.

## Conclusion

OpenMPI distributes work **across** nodes (between different nodes) and OpenMP
distributes work within nodes (within a given node). In OpenMPI, each process is
isolated from each other and can't see variables or the memory from each other;
in OpenMP, the several threads spawned by a process **do** share memory and can
see variables from the other ones. **The End**.

## Bonus

- How many virtual processors do you have? Run `nproc`.
- More info about processors? Run `lscpu` or inspect /proc/cpuinfo.
- Slides on [^5]
- Run `ompi_info`.
- `man MPI_Send` and `man MPI_Recv` (they're both blocking calls)
- `mpic++ --showme` (want to see the the compile flags of your friendly wrapper compiler?)
- Difference between *mpiexec* and *mpirun*? It looks like the former is more standardized; however, the last one seems to be more common – at least on the sources I accessed.

[^1]: [FAQFlow #2: Android Upgrading/Rooting Notes]({{< ref "2015-03-11-faqflow-2-android-upgrading-rooting-notes" >}})

[^2]: [Scilab Notes (HOWTO)]({{< ref path="2014-03-07-scilab-notes-howto" lang="pt" >}})

[^3]: http://pawangh.blogspot.com.br/2014/05/mpi-vs-openmp.html

[^4]: http://darmawan-salihun.blogspot.com.br/2009/11/openmp-vs-openmpi.html

[^5]: https://www.open-mpi.org/papers/sc-2009/jjhursey-iu-booth.pdf
