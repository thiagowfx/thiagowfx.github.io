---
title: "Update DNS NS servers from Porkbun to Cloudflare"
date: 2024-12-27T22:45:45-03:00
tags:
  - bestof
  - dev
  - privacy
  - security
---

[Porkbun](porkbun.com) is my registrar of choice. It is quite decent but alas it
[does
not](https://kb.porkbun.com/article/10-how-to-set-up-email-forwarding-service)
support wildcard or catch-all emails, as per their own docs.

Cloudflare, on the other hand,
[does](https://community.cloudflare.com/t/creating-an-email-catchall/646357).

**Problem statement**: How to migrate from Porkbun to Cloudflare?

To be more precise: I'd still like to keep Porkbun as my registrar. They are
quite solid and I am very content with them. Cloudflare is also very solid but,
for now, I do not intend to switch my registrar to it.

Therefore the only transfer that should happen is the DNS management (DNS
server), via the authoritative nameservers (NS) setting.

It turns out both providers have excellent documentation on this process:

- **Porkbun**: https://kb.porkbun.com/article/22-how-to-change-your-nameservers
- **Cloudflare**: https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/

Upon creating an account on Cloudflare, I imported my site and its existing DNS
records by using their [records quick scan
tool](https://developers.cloudflare.com/dns/zone-setups/reference/dns-quick-scan/):

> Since the DNS records quick scan is based on this predefined list of commonly
> used record types and names, and is not tailored to the specific zone you are
> adding to Cloudflare, there can be cases where not all records are picked up.

Three DNS records were not automatically detected (two A records and one TXT
record)[^2]. I just added them manually. I chose to keep the records in Porkbun
intact in case I decide to revert back to them in the future.

For starters, I chose to [disable
proxying](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/)
via Cloudflare. It's quite interesting though, and it's a setting I would
consider to enable at some point.

From Porkbun, I had to update my [NS
entries](https://kb.porkbun.com/article/63-how-to-switch-to-porkbuns-nameservers)[^1] from:

```
curitiba.ns.porkbun.com
fortaleza.ns.porkbun.com
maceio.ns.porkbun.com
salvador.ns.porkbun.com
```

[To](https://blog.cloudflare.com/whats-the-story-behind-the-names-of-cloudflares-name-servers/):

```
anirban.ns.cloudflare.com
celine.ns.cloudflare.com
```

During the transfer, it's
[important](https://developers.cloudflare.com/dns/dnssec/) to delete
[DNSSEC](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#before-you-begin)
records at Porkbun:

> If you are onboarding an existing domain to Cloudflare, make sure DNSSEC is
> disabled at your registrar (where you purchased your domain name). Otherwise,
> your domain will experience connectivity errors when you change your
> nameservers.

Then I can keep an eye on
[WhatsMyDNS](https://www.whatsmydns.net/#NS/perrotta.dev) to monitor the NS
propagation. It may take up to 48 hours to be fully rolled out.

Or via CLI:

```shell
% dig perrotta.dev +trace @1.1.1.1 | grep perrotta.dev
; <<>> DiG 9.10.6 <<>> perrotta.dev +trace @1.1.1.1
perrotta.dev.		10800	IN	NS	anirban.ns.cloudflare.com.
perrotta.dev.		10800	IN	NS	celine.ns.cloudflare.com.
perrotta.dev.		300	IN	A	185.199.110.153
perrotta.dev.		300	IN	A	185.199.111.153
perrotta.dev.		300	IN	A	185.199.108.153
perrotta.dev.		300	IN	A	185.199.109.153
```

Just a few minutes after the update I could already see some nameservers picking
up the changes:

```
Paris, France
France Telecom
id 22228
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
perrotta.dev. IN NS
;ANSWER
perrotta.dev. 10800 IN NS anirban.ns.cloudflare.com.
perrotta.dev. 10800 IN NS celine.ns.cloudflare.com.
;AUTHORITY
;ADDITIONAL
```

```
Seoul, South Korea
KT
id 14115
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
perrotta.dev. IN NS
;ANSWER
perrotta.dev. 10800 IN NS anirban.ns.cloudflare.com.
perrotta.dev. 10800 IN NS celine.ns.cloudflare.com.
;AUTHORITY
;ADDITIONAL
anirban.ns.cloudflare.com. 50728 IN A 108.162.193.64
anirban.ns.cloudflare.com. 50728 IN A 172.64.33.64
anirban.ns.cloudflare.com. 50728 IN A 173.245.59.64
anirban.ns.cloudflare.com. 50728 IN AAAA 2606:4700:58::adf5:3b40
anirban.ns.cloudflare.com. 50728 IN AAAA 2803:f800:50::6ca2:c140
anirban.ns.cloudflare.com. 50728 IN AAAA 2a06:98c1:50::ac40:2140
celine.ns.cloudflare.com. 137333 IN A 108.162.194.98
celine.ns.cloudflare.com. 137333 IN A 162.159.38.98
celine.ns.cloudflare.com. 137333 IN A 172.64.34.98
celine.ns.cloudflare.com. 702 IN AAAA 2606:4700:50::a29f:2662
celine.ns.cloudflare.com. 702 IN AAAA 2803:f800:50::6ca2:c262
celine.ns.cloudflare.com. 702 IN AAAA 2a06:98c1:50::ac40:2262
```

Once the transfer is done, go to your Cloudflare dashboard. You should see the
following message:

> Great news! Cloudflare is now protecting your site

I also got an email from Cloudflare confirming it:

> perrotta.dev is now active on a Cloudflare Free plan

Now it's time to [re-enable
DNSSEC](https://developers.cloudflare.com/dns/dnssec/). Porkbun instructions are
in [the Porkbun DNSSEC
guide](https://kb.porkbun.com/article/93-how-to-install-dnssec): do not fill out
**keyData**. It's possible to verify it was properly configured via [DNSSEC
Analyzer](https://dnssec-analyzer.verisignlabs.com/perrotta.dev) by VeriSign
Labs, wherein all checkboxes should be green. Furthermore, from Cloudflare,
verify that `DNS > Settings > DNSSEC` is properly configured.

If you choose to [proxy your traffic through
Cloudflare](https://developers.cloudflare.com/cloudflare-one/policies/gateway/proxy/),
you can verify whether it's hiding your origin IP address with https://ping.eu.
Or, alternatively, `ping <hostname>` from the terminal. Beware of DNS caching.
It seems a no-brainer and sensible idea to enable it for your VPS instances[^3]. I
would not enable it for [Github
Pages](https://community.cloudflare.com/t/github-pages-require-disabling-cfs-http-proxy/147401/21)
though.

Up to this point everything was a no-op in terms of feature parity. The optional
Cloudflare goodies (e.g. proxying, blocking AI bots, caching, etc.) are just
cherries on top.

The most exciting part comes now: configuring email and MX records to use
Cloudflare's, with the final goal of supporting catch-all / wildcard emails.

## Email

Follow the steps at
https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/
to configure MX, SPF and DMARC. It's mostly a point-and-click process.
Cloudflare makes it easy and boring™.

Once the MX record is configured, verify it's working via [WhatsMyDNS](https://www.whatsmydns.net/#MX/perrotta.dev).

Verify DMARC is working via [MX
Toolbox](https://mxtoolbox.com/SuperTool.aspx?action=dmarc%3aperrotta.dev&run=toolpage).

Then [create custom routing
rules](https://blog.cloudflare.com/introducing-email-routing/#cloudflare-email-routing).
If desired, add a catch-all rule.

Once it is working test it by sending an email to yourself. And we're done!

More references on DKIM and DMARC:

- **Porkbun**: https://kb.porkbun.com/article/179-how-to-turn-on-dkim-dmarc (for
  comparison only)
- **Cloudflare**: https://www.cloudflare.com/en-ca/learning/email-security/dmarc-dkim-spf/

## References

- https://developers.cloudflare.com/learning-paths/get-started-free/

[^1]: [Fun
    fact](https://www.reddit.com/r/PorkBun/comments/170d6ve/unimportant_nameserver_naming_question/):
    The nameservers are named after Brazilian cities: "our CTO is a big fan of
    Brazil". Huh.

[^2]: The A records were subdomains of my domain, and the TXT record was the
    github pages site / domain verification.

[^3]: However it didn't work for my instances out-of-the-box. That's a problem
    for another day: `ERR_TOO_MANY_REDIRECTS`.
