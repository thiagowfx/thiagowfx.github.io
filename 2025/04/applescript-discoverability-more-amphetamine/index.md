
Previously: [Amphetamine: Keep awake]({{< ref "2025-03-28-amphetamine-keep-awake" >}}).

The previous setup would turn my external monitor off upon:

```applescript
tell application "Amphetamine" to start new session
```

I needed to modify it to issue that command only when the session is not yet
active.

Via [Apple Stack
Exchange](https://apple.stackexchange.com/questions/46521/how-do-i-find-out-the-applescript-commands-available-for-a-particular-app)
I noticed I could open the `Script Editor.app`, then `File > Open
Dictionary...`, then select `Amphetamine.app`.

This would open a new window with a list of all available AppleScript commands
to my disposal.

I quickly spotted one called `session is active`:

> Returns boolean — true or false — indicating whether there is an active session

...that's exactly what I needed!

Now I just needed to combine `if` + `session is active` + `start a new session`.

I don't know AppleScript, and I didn't intend to specialize on it now. In the
old days, I would have used a search engine and/or consulted a Stack Exchange
website to figure out what is the `if` syntax. Or maybe even have introspected
the AppleScript documentation / manual.

But we're in 2025.

I write `llm applescript if "session is active" tell application to start new
session` in Chrome. `llm` is aliased to
`https://chatgpt.com/?hints=search&ref=ext&q=%s`. ChatGPT Search happily tells
me what the correct syntax is:

```applescript
tell application "Amphetamine"
    if not (session is active) then
        start new session
    end if
end tell
```

I follow up with `inline in osascript`, which results in:

```shell
osascript -e 'tell application "Amphetamine" to if not (session is active) then start new session'
```

Exactly what I was looking for.

Moments later there's a new commit in my corp dotfiles:

```
% git show b306e31597b63007bb8c3aadb56340cdb6f52703
commit b306e31597b63007bb8c3aadb56340cdb6f52703
Author: Thiago Perrotta <{email redacted}>
Date:   Tue Apr 1 13:31:33 2025 +0200

    better amphetamine

diff --git profile/.profile.d/functions_corp.sh profile/.profile.d/functions_corp.sh
index e58333a..365c176 100644
--- profile/.profile.d/functions_corp.sh
+++ profile/.profile.d/functions_corp.sh
@@ -19,7 +19,7 @@ redacted_login() {
 # Run at the start of the work day
 prodaccess() {
        echo "--> Amphetamine"
-       osascript -e 'tell application "Amphetamine" to start new session'
+       osascript -e 'tell application "Amphetamine" to if not (session is active) then start new session'
```

