---
title: "★ Keychron K2 on macOS: fix Home and End keys"
date: 2022-04-22T19:04:17-04:00
tags:
  - macos
  - bestof★
---

**Issue**: For whatever reason, the `Home` and `End` keys on my [Keychron K2]({{< ref "2022-01-12-keychron-k2-review" >}}) do not work as intended on macOS.

<!--more-->

## Expectations vs Reality

For example, when using a text editor such as TextMate or a web browser like Chrome, I'd expect:

- `Home` to position the text cursor in the beginning of the line (à la `C-a` in emacs)
- `End` to position the text cursor in the end of the line (à la `C-e` in emacs)

The only way to provoke these effects _out-of-the-box_ is by pressing, respectively, the `Cmd + Left` and `Cmd + Right` shortcuts, as you would normally do in a Macbook laptop native keyboard.

This is very annoying because it only happens in macOS[^1]: the `Home` and `End` keys work just fine in both Linux and Windows. [A reddit user](https://www.reddit.com/r/Keychron/comments/ooice5/home_and_end_keys_not_working_on_monterrey/) reported the same issue in `/r/keychron`, but the existing thread has no proposed solutions.

## Enter Karabiner Elements

I've always heard good things about [Karabiner Elements](http://karabiner-elements.pqrs.org) as a praised one-size-fits-all application for keyboards and macros in macOS, thus decided to give it a try. **Bonus points**: it is [open source](https://github.com/pqrs-org/Karabiner-Elements), released into the public domain.

Upon installing it with [Homebrew Cask](https://formulae.brew.sh/cask/karabiner-elements) (`brew install karabiner-elements`), I executed it. Then I needed to give a bunch of permissions to the application via `macOS Settings > Security & Privacy > Privacy > Input Monitoring`. The following apps were whitelisted accordingly:

- `karabiner_grabber`
- `karabiner_observer`
- `Karabiner-EventViewer.app`: this one is optional, but useful for debugging

The app is straightforward to use. It allows you to do all sorts of reactions to key codes input events.

I had a simple idea: I wanted to map `Home` to `Cmd + Left`, and `End` to `Cmd + Right`.

Unfortunately these are considered "Complex modifications" because they map one origin key to two destination keys. "Simple modifications" are _one-to-one_ key mappings. Why is it unfortunate? Because it doesn't seem to be possible to do such mappings via the app UI. Apparently one needs to express those mappings in a `.json` file instead.

## Ah, communities

Sure, no problem, I was about to do it but then I realized there's an [official website](https://ke-complex-modifications.pqrs.org) for community-maintained mappings. The website is well organized and curated. Why create something fully from scratch when I could just reuse an existing one?

I found a "Keychron K2" category which made me instantly happy but it turned out not to be useful, as there were only two defined mappings therein:

> - Change Keychron K2 keyboard layout to more closely resemble an Apple keyboard
> - Remap some Keychrom K2(US) keys to make it less painful to switch from Macbook(RU) keyboard

None of these mattered to me. Then I searched for `home to cmd` which led me to [this entry](https://ke-complex-modifications.pqrs.org/#HomeEnd), which had exactly the mappings I wanted:

> Home and End
>
> - Home to Command Left
> - End to Command Right

[Its resulting JSON](https://ke-complex-modifications.pqrs.org/json/HomeEnd.json) looks roughly like this (irrelevant bits stripped for the sake of brevity):

```json
{
  "title": "Home and End",
  "rules": [
    {
      "description": "Home to Command Left",
      "manipulators": [
        {
          "type": "basic",
          "from": {
              "key_code": "home"
            },
          "to": [
            {
            "key_code": "left_arrow",
            "modifiers": "command"
            }
          ]
        }
      ]
    },
    {
      "description": "End to Command Right",
      "manipulators": [
        {
          "type": "basic",
          "from": {
              "key_code": "end"
            },
          "to": [
            {
            "key_code": "right_arrow",
            "modifiers": "command"
            }
          ]
        }
      ]
    }
  ]
}
```

There's conveniently an **Import** button in the website though, which automatically opens the mappings in Karabiner Elements, so I didn't even need to copy and paste the JSON.

## Verdict

**End Result**: It worked flawlessly! The only caveat is that from now on I need to keep the Karabiner Elements application running as a daemon, but it is well justified. Plus, if I ever need[^2] to map additional keys in the future, now I already have a workflow in place to do so.

Karabiner is like having [QMK](https://qmk.fm) purely at the software layer, which works for any keyboard whatsoever.


[^1]: As of this writing: macOS Monterey: 12.3.1.
[^2]: https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it...
