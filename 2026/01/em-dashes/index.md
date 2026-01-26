
I use em dashes extensively (–).

And, apparently, [so](https://folkertstijnman.com/blog/why-em-dashes-are-common-in-llm-outputs/) [do](https://medium.com/@raj-srivastava/how-llms-turned-the-em-dash-into-a-villain-technical-nuances-b564857adc3b) [LLMs](https://www.seangoedecke.com/em-dashes/).

These days I feel that I need to put in some _additional_ effort to make my sentences sound more natural / human, otherwise some people could erroneously assume that they're LLM-generated.

_C'est la vie_.

On macOS, press `Option + -` to insert an em-dash (–).

Alternatively,
[instruct](https://vi.stackexchange.com/questions/2199/what-is-the-easiest-way-to-insert-en-dash-in-vim)
`nvim` to insert an em-dash when typing the sequence `--<space>` (=two dashes
followed by a space) in markdown files by changing
`~/.config/nvim/after/ftplugin/markdown.lua`:

```lua
-- Convert -- followed by space to em-dash
vim.keymap.set('i', '--<Space>', '—', { buffer = 0, desc = 'Em-dash' })
```

Or in `vim` (`~/.vim/after/ftplugin/markdown.vim`):

```vimscript
inoremap <buffer> -- —
```

