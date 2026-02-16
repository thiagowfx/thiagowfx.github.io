
[Kagi](https://kagi.com/), a paid search engine, allows adding [custom](https://duckduckgo.com/bangs) [bangs](https://help.kagi.com/kagi/features/bangs.html).

Today we'll add a custom bang for [LeetCode](https://leetcode.com/).

1. Navigate to https://kagi.com/settings/custom_bangs
2. Click 'Add Bang'
3. Input:
    — Bang name: LeetCode
    — Bang shortcut: leetcode
    — URL template: https://leetcode.com/search/?q=%s
    — [x] Shortcut Menu ("Show this custom bang in the More search menu")
    — [x] Open Base Path ("When using this bang without a query, navigate to the
      base path of the URL instead")
4. Save

To trigger the bang, search for e.g. `!leetcode Remove Duplicates from Sorted Array`.

You could also add this URL to your [browser search engine
settings](https://support.google.com/chrome/answer/95426?hl=en&co=GENIE.Platform%3DDesktop), just set the shortcut starting with an exclamation mark / bang (`!`).

When to choose which?
Kagi settings will work seamlessly on mobile.

