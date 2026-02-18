
Wikimedia is the most full-featured wiki software out there and powers
Wikipedia. Let me talk about what you may not know yet.

I tried to deploy it on Debian. While Debian tries to set everything up for you,
pulling dependencies like Apache and MySQL, this doesn't necessarily reflect
what you want.

First, Apache creates a new process for every connection, which doesn't scale
(see the c10k problem). While probably the most used web server nowadays, I
prefer something more lightweight. Two good options are nginx and lighttpd.

Second, PostgreSQL is better than MySQL. This is not something I can fully argue
about, but most people I know agree on that.

Conclusion: if you use Debian, either you'll struggle to get the packages and
software you want working together, or a sub-optimal solution will be deployed.
I prefer a KISS operating system. For familiarity, I chose Arch Linux.

**Note**: Be aware that some people discuss using Arch as a server, mainly for
stability reasons. The point is: choose an OS that doesn't get in your way.

## Installation

- Get php: `pacman -S php`
- Get a CGI program for php. I like fastcgi: `pacman -S fcgi` (alternative:
  php-fpm)
- Get a database server. PostgreSQL: `pacman -S postgresql`
- Get a web server. Lighttpd: `pacman -S lighttpd`
- Get wikimedia and optional dependencies: `pacman -S wikimedia php-gd php-intl
  php-pgsql imagemagick`

Now it's a matter of configuration. I advocate using "/srv/http" instead of
"/var/www" for storing web files. However, wikimedia gets installed to
"/usr/share/webapps/wikimedia", so you have to either create a symlink or use
lighttpd's mod_alias to create an alias to this path. I prefer the last option
so wikimedia gets placed in a specific directory—for example, "/wiki".

Consult the Arch Wiki or lighttpd doc pages for configuration details. After
configuring lighttpd with fastcgi and wikimedia, configure php (enable
extensions and fix cgi path info to 1) and PostgreSQL.

After everything is properly configured, start the services. Arch uses systemd:

```shell
% systemctl enable lighttpd
% systemctl enable postgresql
```

That's it.

## Footnotes

- c10k problem: http://www.kegel.com/c10k.html
- Arch Wiki — Server: https://wiki.archlinux.org/index.php/Server
- Arch Linux forum discussion: https://bbs.archlinux.org/viewtopic.php?id=162434
- Reddit discussion:
  https://www.reddit.com/r/archlinux/comments/1wqpdw/do_you_use_arch_for_production_servers/

