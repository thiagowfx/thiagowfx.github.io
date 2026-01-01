
What does `[1, 4]` mean?

If you're thinking in **Mathematics** terms: it's a closed interval from 1 to 4
(=both inclusive).

If you're thinking in **Programming** terms (Python): it's a list containing two
elements: 1 and 4.

This is ambiguous, eh?

In prose I propose to use
`{1, 4}` to represent the list (or set),
and `1..4` to represent the closed interval.

Refer to it as "for 1..4" instead of "from 1..4".
If you want to use "from", then state "from 1 to 4" fully.

Or, alternatively, make it explicit which convention you're using, perhaps by
making the context prominent.

Likewise beware of `(1, 4)`: it could be an open interval from 1 to 4 (=both
exclusive) or a tuple containing the elements 1 and 4.

