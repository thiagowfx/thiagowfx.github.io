
The list of my default apps for this year.

In the past I would maintain an ["uses"](https://uses.tech/) page in my blog, but I no longer believe in it.
User needs change all the time, and it's a chore to keep them up-to-date.
People shouldn't be defined by the software they use.

That said, having a clean snapshot of the software I use at a fixed point in time isn't a bad proposition.
It doesn't need to be maintained.
I will probably look back at it within 5 years and laugh at myself for how many things changed.
And also for how many didn't.

- Browser: Google Chrome on macOS, Chromium on Linux, Safari on iOS.
- Search: A combination of Google and DuckDuckGo (mostly for their [!bangs](https://duckduckgo.com/bangs)).
- Writing: A combination of VSCode, `vim` and [MarkEdit](https://github.com/MarkEdit-app/MarkEdit) (macOS markdown editor app). I never got around to long-form writing in Obsidian or Logseq, however it's something I strive to.
- Cloud File Storage: There's no need to share this. Basic OpSec. Why would people share it?
- Chat: WhatsApp remains king in terms of popularity, despite Telegram being superior from an architectural and usability perspective for power users. Facebook Messenger is officially dead at this point. And I'm too much of a millennial for all other apps (Discord, Matrix, etc). Disappearing messages exist in all of these, except Instagram.
- Scheduling: There's no real choice here. You use the platform your employer uses. Otherwise, Google Calendar is the most sensible choice other than self-hosting.
- Video Calls: Ditto. I am way too used to Google Meet to justify switching to an alternative at this point.
- Music: Spotify, hands down. YouTube Music is a good fallback. There's no need to pay for YouTube Premium for music, do your research.
- Podcasts: Overcast on iOS.
- Password Management: Once again, why would you share this?
- Code Editor: VScode and `vim`. Maybe I'll switch to `neovim` at some point. I refrain from using IDEs in general but, when I need to, JetBrains is the answer. I tried [`zed`](https://zed.dev/) this year but wasn't convinced, and their core team is quite small. The flurry of "AI"[^1] editors should be ignored, as none of them are likely to stick long-term. Instead, it's better to invest in "AI" tooling that is editor agnostic; for example, Simon Willison's [`llm`](https://github.com/simonw/llm), or GitHub Copilot.
- Terminal: iTerm2 on macOS. I haven't used desktop linux in a while (:sad:), but I'd probably still stick to Tilix and/or Alacritty there. I no longer use hterm (ChromeOS).
- VPN: Unless you're rolling your own, it doesn't matter too much. Avoid the big players if you can afford to.
- Bookmarks: None. [Absolutely none](https://www.goodreads.com/book/show/25614984-spark-joy). When I need to store _transient_ link lists, I use my Second Brain app to do so.
- Read It Later: Ditto as above. Otherwise: starring articles on Miniflux, or keeping Safari tabs open until I get to them, or parking a handful of items in an "inbox" browser bookmarks folder.
- Mail Client: The official clients of my email providers. No agnostic app at this time. It's especially inconvenient to do so on iOS.
- Mail Server: N/A.
- Launcher: `Cmd-Space` on macOS a.k.a. Spotlight. I keep Raycast around but I rarely use it. On Linux `i3-dmenu-desktop` is still my favorite.
- Screenshots: `Cmd-Shift-4` on macOS, or `scrot` on Linux.
- Menu Bar: [Hidden Bar](https://github.com/dwarvesf/hidden). It's free, and available as a cask on homebrew.
- Containers: Rancher Desktop.
- Automation: None. I tried Hammerspoon this year but found no use for it.
- Second Brain: A mixture of Obsidian and Logseq. Which I'd really like to end, it would be easier to have a single app to rule them all, as they both support multiple vaults / graphs anyway (e.g. to partition personal vs work notes).
- Operating System: [Alpine Linux](https://alpinelinux.org/) is my current favorite for servers, and I'm biased anyway because I maintain a couple of aports (packages) there. For desktop, it's awfully hard to use anything other than macOS ever since M1 processors got released. I miss Linux desktop from time to time but realistically it's no longer an intrinsic goal of mine; that said, I'd likely go back to my beloved Arch Linux should that ever reoccur.
- Shell: `zsh` + [`grml-zsh-config`](https://grml.org/zsh/), no change here. Sometimes I think of migrating to `fish`, but the POSIX incompability always discourages me to do so.
- Terminal Multiplexer: `tmux`, but only for remote sessions (`ssh`). Locally I tend to just open new terminal tabs on VSCode and/or iTerm2. Alas, `tmux` + `VSCode` do not play well together anyway (citation needed, for another day).

This post was inspired by https://micro.webology.dev/2024/12/19/default-apps.html.

[^1]: For the correct way to refer to them, pick one of: LLMs, Gen AI, or "AI". _Never_ drop the quotes when using the plain term! Otherwise you fall into the same trap for using the term "crypto" to distinguish between cryptography and cryptocurrency.

