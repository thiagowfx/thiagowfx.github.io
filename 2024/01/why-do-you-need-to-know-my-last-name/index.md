
Some (annoying) websites and/or mobile apps will refuse to let you proceed past
their registration / login screen unless you provide a last name. Isn't my
first name enough[^1]?

There are a couple of ways to work around this:

- Provide a fake last name
- Provide a gibberish last name (aklsjslkja)
- Provide only the first or second letter of your real last name (e.g. "Thiago
  P")
- Provide some non-latin-alphabetic character (e.g. "1", ".", "Э̇")

Recently it occurred to me there's an even cleverer idea: provide an empty
(whitespace) character.

Some services have validation in place to prevent you from inserting a mere
ASCII whitespace (' ').

However, most will not bother to check "invisible" unicode whitespace:

```
​
```

There's a single whitespace character above you can easily copy. `vim` displays
it as `<200b>` – [zero-width space](https://unicode-explorer.com/c/200B).

Another one (`<200e>` – [left-to-right mark](https://unicode-explorer.com/c/200E)):

```
‎
```

**References**:

- https://emptycharacter.com/
- https://unicode-explorer.com/c/200B
- https://unicode-explorer.com/c/200E

[^1]: Actually, why do you even need to know my first name in the first place?
    I am just some random database primary key ID.

