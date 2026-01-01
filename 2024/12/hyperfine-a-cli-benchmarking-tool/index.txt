
This week I accidentally stumbled upon [`hyperfine`](https://github.com/sharkdp/hyperfine).

It's a CLI benchmarking tool, with the most sensible user interface I could ever
conceive:

```shell
% hyperfine --warmup 3 'find -iname "*.ts" | wc' 'fd -e ts | wc'
Benchmark 1: find -iname "*.ts" | wc
  Time (mean ± σ):       2.5 ms ±   2.7 ms    [User: 0.7 ms, System: 1.9 ms]
  Range (min … max):     0.0 ms …   8.4 ms    260 runs

  Warning: Command took less than 5 ms to complete. Note that the results might be inaccurate because hyperfine can not calibrate the shell startup time much more precise than this limit. You can try to use the `-N`/`--shell=none` option to disable the shell completely.

Benchmark 2: fd -e ts | wc
  Time (mean ± σ):     103.9 ms ±   5.8 ms    [User: 238.4 ms, System: 688.8 ms]
  Range (min … max):    94.3 ms … 114.4 ms    28 runs

Summary
  find -iname "*.ts" | wc ran
   41.43 ± 44.04 times faster than fd -e ts | wc
hyperfine --warmup 3 'find -iname "*.ts" | wc' 'fd -e ts | wc'  7.84s user 23.35s system 443% cpu 7.034 total
```

Give it two (or more) commands, fine-tune it as much as you need (see `hyperfine
--help`), and then profit[^1]. Definitely adding it to my toolbox.

The author (`@sharkdp`) has also written `fd` and `bat`.

[^1]: Interestingly the result in my experimentation is counter-intuitive, as
    `fd` is supposed to be faster than `find`, it's probably an edge case with
    the repository I used.

["Do one thing and do it well"](https://en.wikipedia.org/wiki/Unix_philosophy), hands-down.

