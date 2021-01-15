Reading some hackers talking about Packrat parsers, it occurred to me
that perhaps you could get a huge speedup in Packrat by a different
memoizing approach.

Normally in Packrat a parsing grammar node (or perhaps a nonterminal)
is invoked at a given position of a given stream and returns a result,
either a parse tree and a new position, or a failure, and in either
case the result is memoized with the (position, grammar node) pair as
the memo table key, or (if the memo table is global or associated with
the grammar rather than the input stream) the (input stream, position,
grammar node) triple.  The memo table ensures that we only ever invoke
each parse at most once for each input position.

To facilitate incremental parsing, the parsers in [Darius Bacon’s
parsing sketch][0] additionally return a “far” value: how far ahead
they read in the input stream.  This makes it possible to invalidate
memo table entries that depend on changed parts of the text.

[0]: https://gist.github.com/darius/27acf96e3579b22d17a25c21d74c2b4b

It occurred to me, though, that a much more powerful approach is
possible: instead of using the (position, grammar node) pair as the
key, we can use the *actual text examined* by the parsing process.
Then, if we try to parse the same text again later in the input stream
with the same production, we can reuse the same memo-table result.
So, for example, when parsing a Python program, every time you find an
argument list in a function declaration that looks like `(self):`, you
can simply return the same argument list after a memo-table lookup.
Every identifier in a program would only be parsed for real only once
for each character following it; all other attempts to parse them
would find hits in the memo table.  So, for example, all the
occurrences of `weight(`, would have a single memo-table entry, but
`weight ` and `weight\n` would get their own entries.  Every
occurrence of `stack.pop()\n` or `for word in words:\n` or `if tree is
None:\n` or `i+1]` would share the same memo-table entry.

This might sound like an unreasonable thing to do that would result in
a huge and slow memo table, and it might be, but also it might not be.
The memo table itself can be stored as a trie rather than a hash
table, for example with Patricia, enabling it to be traversed
relatively quickly and use a relatively manageable amount of space.
And the great advantage it would have over the usual memo-table
approach is that the majority of memo-table entries would be shared
among several different locations in the source text.

It might also be possible to use this approach to automatically get
incremental reparsing by using the same memo table for more than one
parse.  To the extent that the second parse shares text with the first
parse, even in a different order, the old AST nodes will just flop
ready-made out of the memo table.

The big drawback of this approach is that it loses Packrat’s
linear-time guarantee, because now the process of testing for a memo
table hit potentially involves examining all the subsequent characters
in the input stream.  That means the overall parse potentially takes
quadratic time rather than linear time.
