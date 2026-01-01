
[dedoimedo](https://www.dedoimedo.com/computers/iphone-lockdown-mode.html) makes
me realize that the iOS lockdown mode is actually quite usable, even for us
normies:

> For a while now, I've been hearing about this tool. Mostly in regard to
> high-profile zero-day, zero-click, hands-free, security vulnerabilities in
> iPhones and subsequent hacking of said devices by nation-state actors. Sounds
> blockbustery, which piqued my interest. I am usually rather disdainful of
> mainstream media reporting of tech affairs, but that does not mean there isn't
> something genuinely cool behind flashy, scary headlines. And so I decided to
> test the Lockdown Mode.

What are its effects?

> Specifically, most attachments are blocked in Messages, websites that use
> JavaScript engines that run Just-in-Time (JIT) compilers or use remote fonts
> will not render their pages correctly, various app invitations and calls are
> blocked from people you haven't approved beforehand, location information for
> shared photos is excluded, Wi-Fi connectivity to insecure networks is limited,
> and so on.

Aren't these all sensible defaults anyway?

> Pretty much everything in the list above makes absolute sense. None of the
> "restricted" features are actually important or desired. Think about it. Calls
> from people you don't know? Check! Photo location blocking? Check! Web pages
> with pointless remote fonts? Double check! Sounds like an Internet reset,
> going back to 2010, when the computing world was nicer, saner, cleaner!

Enabling it is trivial, the prompts are perhaps a bit scarier than necessary
though:

> You get a whole bunch of explanations and warnings. Confirm. Reboot. The
> iPhone will load without any visible signs that it's actually running in a
> "restricted" mode. Now. Launch Safari, and you will see a notification
> displayed below the address bar. This is the first indication that the phone
> is using the Lockdown Mode. But that does not mean you will be affected. Far
> from it. I spent quite some time browsing, and I didn't notice any website not
> working correctly. Then again, the sites I go to are normal, sane sites, with
> no sensory overload.

Initially Logseq and Obsidian would not properly work: they didn't seem to be
able to read files from iCloud. I had to explicitly whitelist them in lockdown
mode settings. All other apps worked just fine.

When web browsing with Safari I didn't find any issue (so far) in the websites I
normally surf. The only noticeable UI difference is that, as web fonts are
blocked, the visual identity of websites are gone[^1].

This is not necessarily a negative point: blocking web fonts has the positive
side effect of loading less remote data / reducing bandwidth.

Furthermore, by making websites look more generic, perhaps that doubles-down as
a feature to make them less appealing / interesting, akin to using a
software filter to make your phone display everything in black-and-white; we're
all spending a lot of screen time after all.

I am curious how long it will take until I run into some limitation and/or
strong annoyance from using lockdown mode. If that doesn't ever happen though,
perhaps it's a good idea to stick to it.

[^1]: Ironically, not mine, as I [don't]({{< ref
    "2022-02-26-website-fonts-just-use-the-system-font-stack">}}) use any custom
    fonts in this blog.

