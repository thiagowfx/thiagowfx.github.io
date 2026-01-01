
Let's say the files you want to copy are in `~/Downloads`.

Start a local HTTP server on your laptop:

```
$ cd ~/Downloads
$ python3 -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

Find the IP address of your laptop within your LAN:

```
$ ifconfig  # macOS
$ ip addr   # linux
```

Now go to your Steam Deck, access `http://<ip>:8000` via the installed web
browser, and download your files.

Alternatively, run `wget` / `curl` in a terminal.

