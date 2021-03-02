Reading [“A Command Structure for Complex Information Processing” from
01958][3], and it’s pretty astonishing.

[3]: http://bitsavers.org/pdf/rand/ipl/P-1277_A_Command_Structure_For_Complex_Information_Processing_Aug58.pdf "Shaw, Newell, Simon, and Ellis"

It talks about a memory made of dotted pairs in the same year as LISP,
and a CPU without arithmetic decades before Steele’s Scheme chip.

They hadn’t invented garbage collection yet, so they tried to use a
“responsibility bit” to distinguish the “owning” pointer to a
substructure, with the intent of giving their system a purely
hierarchical structure like a hard-link-free Unix filesystem.  They
didn’t know about symlinks, though, and they only associated this bit
with `car`, not `cdr` (pp. 17–18 (19–20/54)):

> The single bit, *e*, is an essential piece of auxiliary information.
> The address, *d*, in a symbol [“symbol” here means what LISP calls
> `car`] may be the address of another list structure.  The
> responsibility code in a symbol occurrence [`car`] indicates whether
> this occurrence is “responsible” for the structure designated by
> *d*.  If the same address, *d*, occurs in more than one word, only
> one of these will indicate responsibility for *d*. ...The need for a
> definite assignment of responsibility can be seen by considering the
> process of erasing a list. ...although a system that will handle
> merging lists also requires a responsibility bit on the link [`cdr`]
> *f*.

Their design is a two-stack machine significantly before Forth; the
operand stack is “L<sub>0</sub>, *Communication List*” and the return
stack is “L<sub>2</sub>, *List of Current Instruction Addresses
(CIA)*” (p. 14).

They had the idea of a generator coroutine or OO or thunking or lazy
evaluation or duck typing too.  p. 7:

> Without breakout devices [this is difficult to gloss], this format
> would ... permit the operand [argument] of a process [subroutine] to
> be specified only by giving its address.  ...these limitations are
> removed... by allowing the address for an operand to refer either to
> the operand itself or to any process that will determine the
> operand.

Note that this was *before* thunking was invented for ALGOL-60 call by
name!  On p. 8 we see duck typing, coroutines, and laziness:

> *Identity of Data with Programs*
>
> In current computers, the data are considered “inert.”  They are
> symbols to be operated upon by the program.  All “structure” of the
> data is ... encoded implicitly into the programs that work with the
> data.  The structure is embodied in the conventions that determine
> what bits the processes will decode, and so on.
> 
> An alternative approach is to make the data “active.”  All words in
> the computer will have the instruction format; there will be “data”
> programs, and the data will be obtained by executing these
> programs. ... a list of data, for example, may be specified by a
> list of processes that determine the data.  Since data are only
> desired “on command” by the processing programs, this approach leads
> to a computer that, although still serial in its control, contains
> at any given moment a large number of parallel active programs,
> frozen in the midst of operation and waiting until called upon to
> produce the next operation or piece of data.  This identity of data
> with program can be attained only if the processing programs require
> for their operation no information about the structure of the data
> programs — only information about how to receive the data from them.
