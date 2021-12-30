What if your system call interface was usable as a shell?

That is, you might plug a user process into an outlet that lets it ask
the kernel to do things and get back responses, but the language that
it’s speaking to the kernel is a language that a person can also
reasonably speak.  Or, maybe not a person, but at least a text
terminal, if it’s plugged into that same outlet.  Maybe you can open a
file and read some data from it by typing a couple of lines of text
into the kernel, and those are the same lines of text a program would
send to do the same operation.

In a sense, this isn’t such a profound idea: on a modern computer,
instead of the shell interpreting user interface events (received
through system calls) and translating them into system calls, the
terminal emulator would interpret user interface events received
through system calls and translate them into system calls.  The actual
interface between the terminal emulator and the kernel wouldn’t have
to look like an ASR-33 byte stream punctuated by CRLFs; it could take
any convenient form.  The key difference from current shells is that
the form of the interface is something that could just as well be used
to talk to programs other than the kernel, and often is.

