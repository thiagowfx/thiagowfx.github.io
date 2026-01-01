
When I created this blog, I pondered a lot about which typography to use. I
kept experimenting with several fonts available in [Google
Fonts](https://fonts.google.com/), and settled on a few favorites for websites:

- Header fonts (sans-serif): Inter, Fira Sans, Lato

- Body fonts (serif): Crimson Pro, Vollkorn, Alegreya

- Code fonts (mono): Fira Code, PT Mono, IBM Plex Mono

Ultimately though, none of them mattered. I was motivated and
influenced by Kev Quirk's [Trying To Go Green With Local
Fonts](https://kevq.uk/how-local-fonts-can-save-the-environment/)
and Steve's [This website is killing the
planet](https://visitmy.website/2020/07/13/this-website-is-killing-the-planet/),
which basically boils down to the same spirit of
https://motherfuckingwebsite.com/: The web is too bloated
nowadays, most websites have a ton of unnecessary CSS and
JavaScript junk to fetch over and over again.

This is not a big deal if you have access to fast internet and
powerful computers, but that's not the case for many people in
the planet.

With the intent of not unnecessarily fetching fonts from the web, that's why my
current font stack just uses the existing fonts in your system, with a few
opinionated bits in case you have some of my favorite fonts already installed:

```css
body {
    font-family: Crimson Pro, Vollkorn, Alegreya, Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Noto Serif, Droid Serif, Times, Source Serif Pro, serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
}

h1, h2, h3, h4, h5, h6, footer, nav, .toc, .post-meta {
    font-family: Inter, Fira Sans, Lato, system-ui, -apple-system, BlinkMacSystemFont, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Cantarell, Arial, sans-serif;
}

code, pre {
    font-family: Fira Code, PT Mono, IBM Plex Mono, Menlo, Consolas, Monaco, Liberation Mono, Ubuntu Mono, Lucida Console, monospace;
}
```

The system font stack reference comes from https://systemfontstack.com/ and [CSS Tricks](https://css-tricks.com/snippets/css/system-font-stack/).

