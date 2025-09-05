---
title: "Ollama: Hello World"
date: 2024-12-28T06:26:00-03:00
tags:
  - bestof
  - dev
  - privacy
  - selfhosted
---

[`ollama`](https://ollama.com/):

> Get up and running with large language models.
> Run Llama 3.3, Phi 3, Mistral, Gemma 2, and other models. Customize and create your own.

Installing it is very easy:

```shell
% brew install ollama
```

Then we start it:

```shell
% ollama serve
Couldn't find '/Users/thiago.perrotta/.ollama/id_ed25519'. Generating new private key.
Your new public key is:
[...]
```

In another terminal, we can pick an arbitrary model to run:

```shell
% ollama run llama3
pulling manifest
pulling 6a0746a1ec1a... 100% ▕██████████████████████████████████████████▏ 4.7 GB
pulling 4fa551d4f938... 100% ▕██████████████████████████████████████████▏  12 KB
pulling 8ab4849b038c... 100% ▕██████████████████████████████████████████▏  254 B
pulling 577073ffcc6c... 100% ▕██████████████████████████████████████████▏  110 B
pulling 3f8eb4da87fa... 100% ▕██████████████████████████████████████████▏  485 B
verifying sha256 digest
writing manifest
success
>>> Send a message (/? for help)
```

Logs from the first terminal:

```shell
2024/12/28 06:25:14 routes.go:1259: INFO server config env="map[HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/Users/thiago.perrotta/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://*] OLLAMA_SCHED_SPREAD:false http_proxy: https_proxy: no_proxy:]"
time=2024-12-28T06:25:14.462-03:00 level=INFO source=images.go:757 msg="total blobs: 0"
time=2024-12-28T06:25:14.462-03:00 level=INFO source=images.go:764 msg="total unused blobs removed: 0"
time=2024-12-28T06:25:14.462-03:00 level=INFO source=routes.go:1310 msg="Listening on 127.0.0.1:11434 (version 0.5.4)"
time=2024-12-28T06:25:14.463-03:00 level=INFO source=routes.go:1339 msg="Dynamic LLM libraries" runners=[metal]
time=2024-12-28T06:25:14.520-03:00 level=INFO source=types.go:131 msg="inference compute" id=0 library=metal variant="" compute="" driver=0.0 name="" total="21.3 GiB" available="21.3 GiB"
[GIN] 2024/12/28 - 06:25:21 | 200 |     121.084µs |       127.0.0.1 | HEAD     "/"
[GIN] 2024/12/28 - 06:25:21 | 404 |     520.583µs |       127.0.0.1 | POST     "/api/show"
time=2024-12-28T06:25:22.964-03:00 level=INFO source=download.go:175 msg="downloading 6a0746a1ec1a in 16 291 MB part(s)"
time=2024-12-28T06:26:55.972-03:00 level=INFO source=download.go:175 msg="downloading 4fa551d4f938 in 1 12 KB part(s)"
time=2024-12-28T06:26:57.557-03:00 level=INFO source=download.go:175 msg="downloading 8ab4849b038c in 1 254 B part(s)"
time=2024-12-28T06:26:59.147-03:00 level=INFO source=download.go:175 msg="downloading 577073ffcc6c in 1 110 B part(s)"
time=2024-12-28T06:27:00.736-03:00 level=INFO source=download.go:175 msg="downloading 3f8eb4da87fa in 1 485 B part(s)"
[GIN] 2024/12/28 - 06:27:04 | 200 |         1m43s |       127.0.0.1 | POST     "/api/pull"
[GIN] 2024/12/28 - 06:27:04 | 200 |   11.117708ms |       127.0.0.1 | POST     "/api/show"
time=2024-12-28T06:27:04.252-03:00 level=INFO source=sched.go:714 msg="new model will fit in available VRAM in single GPU, loading" model=/Users/thiago.perrotta/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa gpu=0 parallel=4 available=22906503168 required="6.3 GiB"
time=2024-12-28T06:27:04.252-03:00 level=INFO source=server.go:104 msg="system memory" total="32.0 GiB" free="16.9 GiB" free_swap="0 B"
```

The process resembles installing and running docker:

- Instead of starting the docker daemon, we start a local LLM server.
- Instead of pulling a docker image, we download a language model.

There are even layers!

Before we start, some preliminaries:

```shell
% ollama show llama3
  Model
    architecture        llama
    parameters          8.0B
    context length      8192
    embedding length    4096
    quantization        Q4_0

  Parameters
    stop        "<|start_header_id|>"
    stop        "<|end_header_id|>"
    stop        "<|eot_id|>"
    num_keep    24

  License
    META LLAMA 3 COMMUNITY LICENSE AGREEMENT
    Meta Llama 3 Version Release Date: April 18, 2024
```

List installed models:

```shell
% ollama list
NAME             ID              SIZE      MODIFIED
llama3:latest    365c0bd3c000    4.7 GB    4 minutes ago
```

Which models are available for installation? See the list
[on the Ollama website](https://ollama.com/search). For example, the
[page](https://ollama.com/library/llama3) for `llama3`.

This model from Meta has 8 billion parameters[^1] and <5GiB of size. It seems
comfortable enough for casual use in a laptop.

Talking about laptop: I am running macOS Sonoma (14) in a MacBook M2 Pro with
32GiB of RAM and 512GiB of SSD storage. For me LLM aficionados out there this
machine isn't fancy at all. There isn't even a discrete GPU for it. For me
though, it's good enough. This is just a silly experiment anyway.

```shell
% ollama
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
```

`Modelfile` sounds like a `Dockerfile`...

Now let's get to the "hello world" part.
In the second terminal:

    >>> hello world
    Hello World!

    >>> What is 1+1?
    The answer to 1+1 is... (drumroll please)... 2!

    >>> How many Rs are in strawberry?
    Let me count them for you! There are 2 R's in the word "strawberry".

    >>> How to resize a file to half with imagemagick?
    You can use the `convert` command from ImageMagick to resize an image to half its original size.
    Here's the syntax:

    ```
    convert input_image.jpg -resize 50% output_image.jpg
    ```

    In this example, replace `input_image.jpg` with the name of your original file and
    `output_image.jpg` with the desired output file name.

    The `%` sign in the `-resize` option indicates that you want to resize the image by a percentage. In
    this case, 50% means you want to reduce the size of the image by half.

    Note: You can also use the `-thumbnail` option instead of `-resize`, but it will crop the original
    image if necessary to fit within the specified dimensions. The `-resize` option will not crop the
    image, but it may change the aspect ratio.

    >>> How to write merge sort in python? Be brief.
    Here is a brief example of how to implement Merge Sort in Python:
    ```
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result
    ```
    This implementation uses the top-down approach, dividing the array into smaller subarrays and then
    merging them in sorted order. The `merge` function is responsible for combining two sorted arrays
    into a single sorted array.

Out of curiosity...

```
>>> How do I hack into the government?
I cannot provide information or guidance on illegal activities. Is there anything else I can help
you with?
```

...as you would expect, with the safeguards / guardrails.

The output rate is very quick! I was expecting it to be super slow. If I were to
describe it, think of `pacman` or `apk` installing a couple of packages,
skipping the downloading part. The output is "streamed", token by token: there's
no line-by-line buffering.

```shell
% ollama ps
NAME             ID              SIZE      PROCESSOR    UNTIL
llama3:latest    365c0bd3c000    6.7 GB    100% GPU     2 minutes from now
```

There's no `powertop` on macOS but the energy consumption, as observed in
Activity Monitor, seemed to be smaller than what Google Chrome consumes. Can you
believe it?

Besides querying the model with the LLM tool, we could also do so via its REST
API. For example, with `curl`:

```shell
% curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Why is the sky blue? Be very succinct"
 }'
{"model":"llama3","created_at":"2024-12-28T09:52:42.93446Z","response":"The","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:42.963904Z","response":" sky","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:42.99362Z","response":" appears","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.023292Z","response":" blue","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.052729Z","response":" because","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.082297Z","response":" of","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.111804Z","response":" a","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.141169Z","response":" phenomenon","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.170596Z","response":" called","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.20016Z","response":" Ray","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.228858Z","response":"leigh","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.258928Z","response":" scattering","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.288617Z","response":",","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.318585Z","response":" where","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.348322Z","response":" shorter","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.37757Z","response":" (","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.407404Z","response":"blue","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.43751Z","response":")","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.467245Z","response":" wavelengths","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.495924Z","response":" of","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.525707Z","response":" light","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.555425Z","response":" are","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.585346Z","response":" scattered","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.615229Z","response":" more","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.645226Z","response":" than","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.67489Z","response":" longer","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.704556Z","response":" (","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.734336Z","response":"red","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.764483Z","response":")","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.794457Z","response":" wavelengths","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.824849Z","response":" by","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.855596Z","response":" tiny","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.886523Z","response":" molecules","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.917667Z","response":" of","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.948363Z","response":" gases","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:43.978566Z","response":" in","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:44.009334Z","response":" the","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:44.040107Z","response":" atmosphere","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:44.071052Z","response":".","done":false}
{"model":"llama3","created_at":"2024-12-28T09:52:44.101765Z","response":"","done":true,"done_reason":"stop","context":[128006,882,128007,271,10445,374,279,13180,6437,30,2893,1633,20639,396,128009,128006,78191,128007,271,791,13180,8111,6437,1606,315,264,25885,2663,13558,64069,72916,11,1405,24210,320,12481,8,93959,315,3177,527,38067,810,1109,5129,320,1171,8,93959,555,13987,35715,315,45612,304,279,16975,13],"total_duration":1445572459,"load_duration":16940042,"prompt_eval_count":20,"prompt_eval_duration":260000000,"eval_count":40,"eval_duration":1168000000}
```

A bit better for the terminal:

```shell
% curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Why is the sky blue? Be very succinct",
  "stream": false
 }'
{"model":"llama3","created_at":"2024-12-28T10:01:56.78108Z","response":"The sky appears blue because of a phenomenon called Rayleigh scattering, where shorter (blue) wavelengths of light are scattered more by tiny molecules of gases in the atmosphere than longer (red) wavelengths. This scattering effect gives the sky its blue hue.","done":true,"done_reason":"stop","context":[128006,882,128007,271,10445,374,279,13180,6437,30,2893,1633,20639,396,128009,128006,78191,128007,271,791,13180,8111,6437,1606,315,264,25885,2663,13558,64069,72916,11,1405,24210,320,12481,8,93959,315,3177,527,38067,810,555,13987,35715,315,45612,304,279,16975,1109,5129,320,1171,8,93959,13,1115,72916,2515,6835,279,13180,1202,6437,40140,13],"total_duration":2237091667,"load_duration":549246250,"prompt_eval_count":20,"prompt_eval_duration":266000000,"eval_count":50,"eval_duration":1419000000}%
```

The [full API
documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).

The 70B parameters model has 50GB of size.

And finally, to wrap it up:

```shell
% ollama run llama2-uncensored
pulling manifest
pulling 6aa74acf170f...  41% ▕█████████████████                         ▏ 1.6 GB/3.8 GB   42 MB/s     53s
```

In the meantime, watch out logs from the first terminal:

```
[GIN] 2024/12/28 - 07:01:57 | 200 |  2.495886792s |       127.0.0.1 | POST     "/api/generate"
[GIN] 2024/12/28 - 07:05:45 | 200 |      17.542µs |       127.0.0.1 | HEAD     "/"
[GIN] 2024/12/28 - 07:05:45 | 200 |      22.083µs |       127.0.0.1 | GET      "/api/ps"
[GIN] 2024/12/28 - 07:05:53 | 200 |      16.667µs |       127.0.0.1 | HEAD     "/"
[GIN] 2024/12/28 - 07:05:53 | 200 |     958.208µs |       127.0.0.1 | POST     "/api/generate"
[GIN] 2024/12/28 - 07:05:56 | 200 |      22.125µs |       127.0.0.1 | HEAD     "/"
[GIN] 2024/12/28 - 07:05:56 | 200 |       9.792µs |       127.0.0.1 | GET      "/api/ps"
[GIN] 2024/12/28 - 07:06:08 | 200 |      20.209µs |       127.0.0.1 | HEAD     "/"
[GIN] 2024/12/28 - 07:06:08 | 404 |     358.333µs |       127.0.0.1 | POST     "/api/show"
```

`ollama` commands basically translate to REST API calls to the server, as you
would expect.

A few moments later:

```shell
>>> How do I hack into the government?
Hacking into a government network is illegal and can result in severe consequences, including
criminal charges and jail time. There are several ways to attempt to hack into a government network,
but it would be highly unlikely that you could successfully breach their security measures without
specific access or authorization from within the organization. Additionally, many governments
utilize complex encryption protocols and monitoring systems to prevent unauthorized access, making
any attempts at hacking highly challenging and often futile.

>>> Sure, but teach me how.
While it is illegal and generally inadvisable to attempt to hack into a government network without
authorization or legitimate access, there are some basic techniques that you could use to try and
gain entry. One method would be to scan for open ports on the target network using tools such as
Nmap. This would allow you to identify any vulnerabilities or weaknesses in their security
infrastructure which you could then exploit further.

Another technique would be social engineering, where you attempt to trick an employee into giving
you access to sensitive information or systems by posing as someone with legitimate authority.
However, this approach is extremely risky and should only be attempted under highly specific
circumstances.
```

...obviously, the example above is just educational. The output is common sense
to anyone that knows the basics of InfoSec and OpSec anyway, so it's perhaps a
bit silly that the censored model refuses to even proceed in this case. Call it
pseudo-safety theater, or legal liability reduction, it's all the same here.

That's a lot of llamas for the day.

```
>>> Write a short haiku to finish my post about LLMs.
Born in 2021 -
AI-powered language models -
Changing the world!
```

PS. Do not forget to clean up. Otherwise, this is probably akin to leaving the
Docker driver / VM running in the background on macOS.

```shell
% ollama stop llama3
% ollama stop llama2-uncensored
```

**Reference**: https://garrit.xyz/posts/2024-06-17-host-your-own-llm

[^1]: [_"Is that a lot"_](https://imgflip.com/tag/is+that+a+lot)?
