
Obviously I'm biased to say this but I have just
[filed](https://github.com/gruntwork-io/pre-commit/issues/130) a high-quality
feature request for a software project I am interested to adopt. What makes it
great™:

- describe **concisely** and **precisely** **what** you're looking for
  - being concise is essential: we live in a fast-paced world. If no one looks
    at your FR, then it won't move forward. Period.
  - being precise (unambiguous) is important to avoid back-and-forth and
    potential bikeshedding
  - I prefer to write it using my own words. Using an LLM risks making your FR
    robotic and unappealing for anyone to consider. YMMV.

- describe **why**
  - what is the _raison d'être_ of the feature? What is the rationale behind it?
    How does it make the project better? How does it improve the developer
    experience?

- (_optional_, but **highly recommended**) suggest **how** and offer to address it
  - Everyone wants everything, but few people want to put in the effort to see
    changes take place. Your FR has a much higher chance of becoming reality if
    you volunteer your time, effort and expertise to implement the feature
    yourself, rather than [demanding](https://xkcd.com/2347/) someone (likely an
    unpaid volunteer) to do so for you.

In my experience it's better to file an issue / ticket / FR first, **prior to**
sending a pull request. You _cannot_ know in advance whether the FR is welcome
by the project or its maintainers. Sending in a PR just to see its underlying
_raison d'être_ be rejected is a waste of time, besides being a frustrating
experience.

Furthermore, the ticket doubles-down as documentation for the PR description /
commit message in the future, should the FR be accepted. The small overhead of
time to file a ticket is a reasonable trade-off.

Now, even if your FR is great and very reasonable[^1], there's absolutely no
guarantee:

- you will even get a reply in the first place[^2]
- back-and-forth chatter will be quick and responsive
- the maintainers / developers will agree with your sense of 'usefulness'
- the maintainers / developers will agree with _how_ you believe it should be
  tackled or implemented
- your follow-up PR will even be reviewed and, let alone, merged
- your merged PR will make it into a new point release

_Life is hard_. Nonetheless, do not give up! Open source software is beautiful
and serendipitous. :)

[^1]: It's a subjective matter.

[^2]: Sometimes it takes [more than 3
    years](https://github.com/funtoo/keychain/issues/119).

