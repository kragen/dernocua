Bernstein’s [netstrings][0] are a sort of TLV encoding with
arbitrary-precision L and without the T: `foo` is encoded as `3:foo,`
and `3:foo,3:bar,` is encoded as `12:3:foo,3:bar,,`.  The intent is to
make protocols easy to parse reliably without making them non-textual.
(One assumes that he considered and rejected Fortran’s
`12H3Hfoo.3Hbar..`.)

[0]: https://cr.yp.to/proto/netstrings.txt

Though they’re self-delimiting, they’re not fully self-describing; you
need some external schema information to distinguish a netstring
containing more netstrings from a netstring containing just a blob.
So you could, for example, precede each netstring with a type byte:
`d12:s3:foo,s3:bar,,` might represent JSON’s `{"foo":"bar"}`.  Unlike
JSON, netstrings permit skipping over the contents in constant time,
without parsing them.

However, because the length field is variable-length, and minimal
encoding is mandatory (leading zeroes are prohibited), the length of
the length field depends on the length of the content.  Because the
content is *after* the length field, the offset at which the content
begins also depends on the content’s length.  So, when outputting a
netstring sequentially, it is not possible to output any of the
content before knowing the length of the whole content.  So a large
netstring in general cannot be emitted in a one-pass fashion.

A higher-level protocol can of course provide a facility analogous to
HTTP’s “Content-Encoding: Chunked”, for example permitting `foo` to be
encoded as `s3:foo,`, `s1:f,+2:oo,`, etc.  This has drawbacks, though:
it eliminates the ability to skip an item in constant time, it adds
back in the opportunities for bugs that netstrings were designed to
avoid, and without further restrictions it eliminates the bijective
nature of the netstrings encoding.

In many contexts, some kind of out-of-band framing indicates the end
of data — for example, the file size in a Unix or MS-DOS filesystem,
framing bytes in SLIP or PPP packets, the Frame Check Sequence in
HDLC, or a fixed-length count field in a program’s memory.  In these
contexts, we can place the length field at the *end* of the
representation instead of the beginning, encoding `foo` as, for
example, `(foo)3` and `(foo)3(bar)3` as `((foo)3(bar)3)12`, or
`\t\tfoo\tbar\n3\n12`.  This permits single-pass *output* of an
arbitrarily large tree of these strings, requiring memory proportional
only to the tree depth, and then constant-time navigation operations
on the resulting serialization as long as it is stored in
random-access memory.  However, unlike bytestuffing or quoting
approaches, it does not permit reliable partial parsing of any
truncated serialization.  For example, `(())2)3(()8)3)12` is also
valid, representing the 12-byte string `())2)3(()8)3`, which is the
concatenation of the representation of the 3-byte string `))2` and the
representation of the 3-byte string `()8`.  But its prefixes
`(())2)3(()8` and `(())2` are also valid.

Rather than “netstrings” we might call this representation
“diskstrings”.

If we concatenate diskstrings with type bytes (prefixed or suffixed)
we can represent JSON-like data in a random-access-friendly
ASCII-clean way; for example, `(37)2s` might represent the 2-byte
binary string `37`, while `(37)2n` represents the number 37₁₀,
`((37)2s(37)2n)12a` represents a sequence or array of them both
(Python `[b"37": 37]`), `((37)2s(37)2n)12d` represents a dictionary
mapping the first to the second (Python `{b"37": 37}`), `?` represents
a nil value, `t` represents Boolean true, and `f` represents Boolean
false.  If canonicalization or rapid searching is important, as in
bencode, we can require that dictionary keys be lexicographically
ordered (by their representations, to permit comparisons between
values of different types).

Prefix type bytes might have more desirable lexicographical ordering
properties or be more human-readable: `s(37)2`, `n(37)2`,
`a(s(37)2n(37)2)12`.  In that case punctuation type bytes would
probably improve readability further by breaking up the visual unity
of “2n”: `,("(37)2+(37)2)12` or something.

If compactness were more important than the extra error-detection, the
type bytes could be further merged with the trailing delimiter, and
the leading delimiter eliminated, thus `37H237#2@8`.  But it’s hard to
see when this would be a good tradeoff.
