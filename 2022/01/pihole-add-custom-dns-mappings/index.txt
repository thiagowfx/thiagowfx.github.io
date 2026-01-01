
This post covers how to add DNS entries / mappings to a local network managed
with [pihole][pihole].

There are several ways to do so:

## 1. The CLI way: `/etc/pihole/`

Edit `/etc/pihole/custom.list`, set one mapping per line, just as you would for
`/etc/hosts`:

```shell
$ cat /etc/pihole/custom.list
127.0.0.1     localhost.corp.google.com
192.168.1.75  myhostname.home.arpa
```

This works because `/etc/dnsmasq.d/01-pihole.conf` contains
`addn-hosts=/etc/pihole/custom.list` by default.

From [Gentoo Wiki][gentoo-wiki]:

> It is possible to refer to an (additional) hosts file to use as source for
> DNS queries. To do so, add the -H /path/to/hostsfile
> (--addn-hosts=/path/to/hostsfile) command line option. It is also possible to
> pass a directory; in that case, all files inside that directory will be
> treated as additional hosts files.

## 2. The CLI way: `/etc/dnsmasq.d/`

```shell
$ cat /etc/dnsmasq.d/03-pihole-custom-dns.conf
address=/localhost.corp.google.com/127.0.0.1
address=/myhostname.home.arpa/192.168.1.75
```

From [ArchWiki][arch-wiki]:

> In some cases, such as when operating a captive portal, it can be useful
> to resolve specific domains names to a hard-coded set of addresses.
> This is done with the address config.

## 3. The Web way

Navigate to http://pi.hole/admin/dns_records.php and set your DNS records
there. From pihole docs:

> The order of locally defined DNS records is:
>
> 1. The device's host name (`/etc/hostname`) and `pi.hole`
> 1. Configured in a config file in `/etc/dnsmasq.d/`
> 1. Read from `/etc/hosts`
> 1. Read from the "Local (custom) DNS" list (stored in `/etc/pihole/custom.list`) (the aforementioned ways)
>
> Only the first record will trigger an address-to-name association.

## Wrapping up

Then restart pihole to apply changes:

```shell
$ pihole restartdns
```

[arch-wiki]: https://wiki.archlinux.org/title/Dnsmasq#Override_addresses
[gentoo-wiki]: https://wiki.gentoo.org/wiki/Dnsmasq#Additional_hosts_file
[pihole]: https://pi-hole.net/

