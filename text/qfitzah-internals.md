Qfitzah represents terms as cons lists in the conventional Lisp way,
exploiting the isomorphism between ordered trees and binary trees.  A
term may be a constant, a variable, or a list; a list is represented
as a pair of the first item in the list, which may be any term, and
the rest of the list, which is either a pair or nil.  Additionally,
variables and constants are symbols.  I’m planning to add a new kind
of constant that is an unboxed small integer and not a symbol.

Each of the values in a pair is represented by a 32-bit word, and the
pair is represented by two adjacent 32-bit words in memory; its three
low-order bits represent the type tag of the object pointed to.  A
pair is represented by a pointer to the beginning of that pair, and
its low-order bits are ?00, 000 I think.

Variables (represented in the concrete syntax as symbols beginning
with an uncapitalized letter or their ilk) are represented by words
whose low-order bits are 010, and constants are represented by words
whose low-order bits are 001.  I’m planning to make numerical
constants be represented by words whose low-order bits are 101.  Nil
is represented by -1, so its low-order bits are 111, so if you were
expecting a term and got nil, it would look like both a variable and a
constant.  XXX this is a bug!  There are bugs where empty lists are
concerned.  Shit.  They match things they shouldn’t, for example:

    $ ./qfitzah
    ↪ () (W)
    ↪ (F)
    Violación de segmento (`core’ generado)

If you mask off the two low-order bits of the word that represents a
symbol, you get the address of a 32-bit word containing a pointer to
the characters of the symbol’s name; the following 32-bit word is the
length of the symbol’s name.  These records are allocated sequentially
in the atom table, which is initially filled with zeroes.

My thought is that if you shift an unboxed integer by 3 bits you get
the integer value.
