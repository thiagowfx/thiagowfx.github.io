---
title: "Send emails straight to spam"
url: https://perrotta.dev/2022/03/send-emails-straight-to-spam/
last_updated: 2024-12-25
---


Just tested [straight to spam](https://straight2spam.xyz) today:

> Love emails but hate people? Don't want someone 🤡 at your party 🥳 but have to invite them 🤢 cause your mom 💁‍♀️ made you? Trust Straight 2 Spam to send your v important email 📧 straight to their spam 🗑
>
> Click the button below👇 to copy a nasty ❌ ooey ❌ gooey ❌ spam-keyword filled invisible message 🔤 for your email that you totally sent on time ⏰ but the 🐦 dodo-brain 🧠 won't see it because they didn't check their spam folder 📂 (Just make sure you're not in the recipient's address book 📇, or all bets are off 🙅‍♀️)

It works exactly as advertised:

- Send an email to someone whose address book contains your email address, and it will _not_ go to spam.
- Send an email to someone whose address book does _not_ contain your email address, and it goes straight to the spam folder.

The email body is indeed invisible, at least in the Gmail web UI. Even `Ctrl+A` won't reveal it. If you click "Show original" to inspect the full message body and headers though, you'll see some junk like the following:

```text
Hello#1 $$$ 100% Act now Action Additional income Affordable All
natural/new Amazed Apply now Avoid Be amazed/your own Bitcoin boss
Beneficiary Billing Billion Bonus Boss Buy Call!!!!!! free/now Cancel
Crypto Cash Casino
```

There's actually more, but I don't want to make this post too spammy for search engines.

The aforementioned text is wrapped in this HTML:

```html
<div dir=3D"ltr">Hello<span style=3D"color:rgb(255,255,255);font-family:&quot;Comic Sans MS&quot;;font-size:1px">
```

Which explains why it is 'invisible' (note the white color).

