Veskeno needs to be able to fluently (and, above all,
deterministically) express the ingredients of software.  But what are
those ingredients?  What are the things we want to be able to express?

What does normal code consist of?
---------------------------------

> According to our data, a typical procedure consists of 8 or 9
> assignment statements, 4 calls to other procedures, 3 IF statements,
> 1 loop, and 1 escape (RETURN or EXITLOOP).  Two of the assignment
> statements simply assign a constant to a scalar variable, one
> assigns one scalar variable to another, and 3 or 4 more involve only
> one operand on the right hand size.  The entire procedure probably
> contains only 2 arithmetic operators.  Two of the three conditions
> in the IF statements involve only a single relational operator,
> probably = or ≠.

(Tanenbaum, 01978, “Implications of Structured Programming for Machine
Architecture”; note how no records, arrays, or other data structures
are mentioned)

I thought I’d go and look at a variety of random code in different
languages to get an idea of what random code looks like.  After all,
maybe my own personal preferences and practices aren’t typical!  Maybe
I tend to focus on some small niche area of the wide world of
programming.  After all, I do write code mostly in Python nowadays.
For better or worse, I’m focusing on languages I do know pretty well.
I looked at random bits of code in 12 languages.

[Modulecounts][0] says npm (JS) is growing at 940 modules a day, Maven
Central (Java) 234, PyPI 217, nuget (.NET) 181, Packagist (PHP) 102,
crates.io (Rust) 58, and RubyGems 19.  Everything else is below 10 new
modules per day.  I sampled the top three of these, plus another 9
that aren’t hip.  [TIOBE][1] gives C, Java, Python, C++, C# (.NET),
Visual Basic (.NET), JS, PHP, SQL, and assembly as its top 10; I
included five of these including the top four; [GitHub][2] ranks JS,
Python, Java, TypeScript, C#, PHP, C++, C, shell, and Ruby, and I
included six of these, including the top three.  (PHP and C# are the
big omissions.)  [Stack Overflow lists][9] JS, Python, Java, bash, C#,
PHP, TypeScript, C++, C, and Golang.

So, hopefully I’m getting a pretty broad range of programming styles,
although all these languages except m4 are pretty similar.

[0]: http://www.modulecounts.com/
[1]: https://www.tiobe.com/tiobe-index/
[2]: https://octoverse.github.com/
[9]: https://insights.stackoverflow.com/survey/2020

### Scheme ###

First consider this chunk of code from Ur-Scheme:

    (define interned-symbol-list '())
    (define (intern symbol)
      (interning symbol interned-symbol-list))
    (define (interning symbol symlist)
      (cond ((null? symlist) 
             ;; XXX isn't this kind of duplicative with the global variables stuff?
             (set! interned-symbol-list 
                   (cons (list symbol (new-label)) interned-symbol-list))
             (car interned-symbol-list))
            ((eq? symbol (caar symlist)) (car symlist))
            (else (interning symbol (cdr symlist)))))
    (define (symbol-value symbol) (cadr (intern symbol)))

I think this is more or less normal code.  It has some definitions, an
assignment, a loop, a mutable variable, some immutable arguments, some
comparisons, some conditionals, some invocations of some primitive
functionality (mostly to access container objects), and some calls to
high-level functions.  It contains an unusually small amount of
mutation (one assignment), an unusually small number of constants
(just one, nil), and an unusually small amount of sequencing (just 
the sequence of two consequents of `null? symlist` and the top-level
sequence of definitions).  You can’t tell from looking, but it invokes
two macros: both `define` and `cond` are defined as macros in
Ur-Scheme.

### Python ###

Here’s some more code that is also pretty normal, from bzrlib.plugins.gtk:

    class LockDialog(Gtk.Dialog):

        def __init__(self, branch):
            super(LockDialog, self).__init__()

            self.branch = branch

            self.set_title('Lock Not Held')

            self.get_content_area().add(
                Gtk.Label(label=(
                    'This operation cannot be completed as '
                    'another application has locked the branch.')))

            self.add_button('Break Lock', RESPONSE_BREAK)
            self.add_button(Gtk.STOCK_CANCEL, RESPONSE_CANCEL)

            self.get_content_area().show_all()

This has a class definition with inheritance and a constructor, a
superclass constructor invocation, some arguments, some references to
free variables (imported from other modules in this case), some
constant strings, a sequence of method calls, and even an object
instantiation and a named argument.  The only primitives used, other
than those mentioned above, are attribute access.

### C ###

Here’s some slightly less normal code, from gpsd/json.c:

    json_debug_trace((1, "JSON parse of '%s' begins.\n", cp));

    /* parse input JSON */
    for (; *cp != '\0'; cp++) {
	json_debug_trace((2, "State %-14s, looking at '%c' (%p)\n",
			  statenames[state], *cp, cp));
	switch (state) {
	case init:
	    if (isspace(*cp))
		continue;
	    else if (*cp == '{')
		state = await_attr;
	    else {
		json_debug_trace((1,
				  "Non-WS when expecting object start.\n"));
		return JSON_ERR_OBSTART;
	    }
	    break;
	case await_attr:
	    if (isspace(*cp))
		continue;

I would have included the whole function, but it’s 454 lines long.
This includes three calls to a C macro, which invokes a variadic
function called `json_trace`; a couple of character constants; a loop;
a couple of integer constants; three string constants; an assignment;
a passel of sequencing; pointer arithmetic, including mutation by
postincrement; indexing into an array by the enum; a switch statement
on an enum; some early exits; lots of primitive operations; and a
couple of invocations of `isspace`, from the standard library, which
could be a subroutine but is probably a macro.

### JS ###

Here’s some more fairly normal code, this time from a JS version of
Python’s `bisect` binary search library, included in a package called
“crossfilter”.  I’ve removed the comments but they already didn’t say
who the author was:

    function bisect_by(f) {
      function bisectLeft(a, x, lo, hi) {
        while (lo < hi) {
          var mid = lo + hi >>> 1;
          if (f(a[mid]) < x) lo = mid + 1;
          else hi = mid;
        }
        return lo;
      }

      function bisectRight(a, x, lo, hi) {
        while (lo < hi) {
          var mid = lo + hi >>> 1;
          if (x < f(a[mid])) hi = mid;
          else lo = mid + 1;
        }
        return lo;
      }

      bisectRight.right = bisectRight;
      bisectRight.left = bisectLeft;
      return bisectRight;
    }

This has some functions with parameters; conditionals; a couple of
loops; comparisons; a few assignments; a little bit of arithmetic
(unlike the others!), including a bit shift; a higher-order function
taking a functional argument and returning closures; some assignments
to attributes; and indexing into arrays.

### Java ###

Here’s some more code that isn’t very normal at all, from Mako, “a
simple stack-based virtual game console, designed to be as simple as
possible to implement”, but mostly another copy of Forth:

	public void tick() {
		int o = m[m[PC]++];
		int a, b;

		switch(o) {
			case OP_CONST  :  push(m[m[PC]++]);                       break;
			case OP_CALL   : rpush(m[PC]+1); m[PC] = m[m[PC]];        break;
			case OP_JUMP   :                 m[PC] = m[m[PC]];        break;
			case OP_JUMPZ  : m[PC] = pop()==0 ? m[m[PC]] : m[PC]+1;   break;
			case OP_JUMPIF : m[PC] = pop()!=0 ? m[m[PC]] : m[PC]+1;   break;
			case OP_LOAD   : push(load(pop()));                       break;
			case OP_STOR   : stor(pop(),pop());                       break;
			case OP_RETURN : m[PC] = rpop();                          break;
			case OP_DROP   : pop();                                   break;
			case OP_SWAP   : a = pop(); b = pop(); push(a); push(b);  break;
			case OP_DUP    : push(m[m[DP]-1]);                        break;
			case OP_OVER   : push(m[m[DP]-2]);                        break;
			case OP_STR    : rpush(pop());                            break;
			case OP_RTS    : push(rpop());                            break;
			case OP_ADD    : a = pop(); b = pop(); push(b+a);         break;
			case OP_SUB    : a = pop(); b = pop(); push(b-a);         break;
			case OP_MUL    : a = pop(); b = pop(); push(b*a);         break;
			case OP_DIV    : a = pop(); b = pop(); push(b/a);         break;
			case OP_MOD    : a = pop(); b = pop(); push(mod(b,a));    break;
			case OP_AND    : a = pop(); b = pop(); push(b&a);         break;
			case OP_OR     : a = pop(); b = pop(); push(b|a);         break;
			case OP_XOR    : a = pop(); b = pop(); push(b^a);         break;
			case OP_NOT    : push(~pop());                            break;
			case OP_SGT    : a = pop(); b = pop(); push(b>a ? -1:0);  break;
			case OP_SLT    : a = pop(); b = pop(); push(b<a ? -1:0);  break;
			case OP_NEXT   : m[PC] = --m[m[RP]-1]<0?m[PC]+1:m[m[PC]]; break;
		}
	}

This has a method definition; a switch statement; some constants; a
bunch of method calls; a bunch of arithmetic primitives (including
bitwise operators, which we haven't seen before); indexing into
arrays; conditionals; lots of assignment and other mutation; and a
number of numeric constants.

Here's some more normal code, also in Java, reformatted from the
OpenJDK; this code is compilation output from some kind of macro
processing, and it implements a FIFO of double-precision
floating-point numbers:

    public DoubleBuffer asReadOnlyBuffer() {
        return new HeapDoubleBufferR(hb, this.markValue(), this.position(),
                                     this.limit(), this.capacity(), offset);
    }

    protected int ix(int i) { return i + offset; }
    public double get() { return hb[ix(nextGetIndex())]; }
    public double get(int i) { return hb[ix(checkIndex(i))]; }

    public DoubleBuffer get(double[] dst, int offset, int length) {
        checkBounds(offset, length, dst.length);
        if (length > remaining())
            throw new BufferUnderflowException();
        System.arraycopy(hb, ix(position()), dst, offset, length);
        position(position() + length);
        return this;
    }

This contains a number of method calls with varying protection, lots
of type declarations (including methods overridden by type signature),
lots of method calls, a little attribute access, some implicit
self-instance-variable access, object instantiation, array indexing, a
little bit of arithmetic (two additions and a comparison), a
conditional, some mutation, and an exception.

### Perl ###

Here’s some more pretty normal code, this time in Perl, from
Net::DBus::Binding::Message::Error:

    =item my $error = Net::DBus::Binding::Message::Error->new(
          replyto => $method_call, name => $name, description => $description);

    Creates a new message, representing an error which occurred during
    the handling of the method call object passed in as the C<replyto>
    parameter. The C<name> parameter is the formal name of the error
    condition, while the C<description> is a short piece of text giving
    more specific information on the error.

    =cut

    sub new {
        my $proto = shift;
        my $class = ref($proto) || $proto;
        my %params = @_;

        my $replyto = exists $params{replyto} ? $params{replyto} : die "replyto parameter is required";

        my $msg = exists $params{message} ? $params{message} :
            Net::DBus::Binding::Message::Error::_create
            (
             $replyto->{message},
             ($params{name} ? $params{name} : die "name parameter is required"),
             ($params{description} ? $params{description} : die "description parameter is required"));

        my $self = $class->SUPER::new(message => $msg);

        bless $self, $class;

        return $self;
    }

This is a method definition including properly marked-up
documentation.  It contains five conditionals, six local variables, no
mutation, three exceptions, a bunch of hash table lookups by string
(like Python, Perl uses string-indexed hash tables instead of record
types), a method call (on the superclass), deeply nested namespaces,
and lots and lots of invocations of primitives, including `shift`,
`ref`, `exists`, `@_`, and `bless`.  It has a lot of string literals
if we count the parameter/attribute names and the package names, but
otherwise the only constants are some string literals for error
messages.

### Elisp ###

Here’s some more pretty normal Lisp code, this time in Elisp, from
Eric Ludlam’s Speedbar package:

    (defun speedbar-add-supported-extension (extension)
      "Add EXTENSION as a new supported extension for speedbar tagging.
    This should start with a `.' if it is not a complete file name, and
    the dot should NOT be quoted in with \\.  Other regular expression
    matchers are allowed however.  EXTENSION may be a single string or a
    list of strings."
      (interactive "sExtension: ")
      (if (not (listp extension)) (setq extension (list extension)))
      (while extension
        (if (member (car extension) speedbar-supported-extension-expressions)
            nil
          (setq speedbar-supported-extension-expressions
                (cons (car extension) speedbar-supported-extension-expressions)))
        (setq extension (cdr extension)))
      (setq speedbar-file-regexp (speedbar-extension-list-to-regex
                                  speedbar-supported-extension-expressions)))

This function contains two conditionals, four assignments, a loop,
properly formatted documentation, one to three constants (nil and two
strings) depending on how you count, lots of calls to primitives, and
a call to another function in the same package.

### Lua ###

Here’s some more pretty normal code, this time in Lua from NMap,
slightly reformatted.  This is from Patrik Karlsson’s interface to get
packets from WinPcap:

      -- Holds the two supported authentication mechanisms PWD and NULL
      Authentication = {
        PWD = {
          new = function(self, username, password)
            local o = { 
              type = 1,
              username = username,
              password = password,
            }
            setmetatable(o, self)
            self.__index = self
            return o
          end,

          __tostring = function(self)
            local DUMMY = 0
            return bin.pack(">SSSSAA", self.type, DUMMY, #self.username,
                            #self.password, self.username, self.password)
          end,
        },

Her we have three levels of nesting of Lua tables (dictionaries),
`...Authentication.PWD.new`.  There are a couple of functions (which
are methods on a metatable object; one is a constructor), a couple of
local variable declarations, an assignment to the `__index` attribute,
a few accesses to attributes, invocation of the `#` length primitive,
a call to a function from another module, and the construction of a
new table `o`.  There are three constants, one of which is a string in
a binary serialization little language.  There is a sequence of four
statements in `new`.

### C++ ###

Here’s some more much less normal code, this time in C++, from
OpenSCAD’s ColorModule (slightly reformatted):

    #include "colormap.h"
    AbstractNode *ColorModule::instantiate(const Context *ctx,
       const ModuleInstantiation *inst,
       const EvalContext *evalctx)
    const
    {
       ColorNode *node = new ColorNode(inst);

       node->color[0] = node->color[1] = node->color[2] = -1.0;
       node->color[3] = 1.0;

       AssignmentList args;

       args += Assignment("c", NULL), Assignment("alpha", NULL);

       Context c(ctx);
       c.setVariables(args, evalctx);

       Value v = c.lookup_variable("c");
       if (v.type() == Value::VECTOR) {
          for (size_t i = 0; i < 4; i++) {
             node->color[i] = i < v.toVector().size()
                ? v.toVector()[i].toDouble()
                : 1.0;
             if (node->color[i] > 1)
                PRINTB_NOCACHE("WARNING: color() expects numbers between"
                               " 0.0 and 1.0. Value of %.1f is too large.",
                                node->color[i]);
          }
       } else if (v.type() == Value::STRING) {
          std::string colorname = v.toString();

Here we see an `#include`, (the beginning of) a method definition,
lots of parameters and other local variables, lots of type
declarations, some object instantiations, lots of accesses to
attributes (“instance variables” or “fields”), constness, lots of
constants (numeric, string, and enum), arithmetic (using postincrement
mutation) to step through an array and check numeric ranges, a loop,
four conditionals, pseudo-RAII (`Context`’s constructors and
destructors maintain a context stack for `lookup_variable` — it isn’t
so much that they acquire resources so much as that they automatically
release them), operator overloading, lots of method calls, array
indexing, macros, and floating point.

### Bourne shell ###

Here’s a shell script from eglibc’s test suite:

    common_objpfx=$1
    run_program_prefix=$2
    objpfx=$3

    LC_ALL=C
    export LC_ALL

    # Create the domain directories.
    mkdir -p ${objpfx}domaindir/de_DE/LC_MESSAGES
    mkdir -p ${objpfx}domaindir/fr_FR/LC_MESSAGES
    # Populate them.
    msgfmt -o ${objpfx}domaindir/de_DE/LC_MESSAGES/multithread.mo tst-gettext4-de.po
    msgfmt -o ${objpfx}domaindir/fr_FR/LC_MESSAGES/multithread.mo tst-gettext4-fr.po

    GCONV_PATH=${common_objpfx}iconvdata
    export GCONV_PATH
    LOCPATH=${common_objpfx}localedata
    export LOCPATH

    ${run_program_prefix} ${objpfx}tst-gettext4 > ${objpfx}tst-gettext4.out

    exit $?

This has very little in common with the other examples, although we
can identify parameters (`$1`, `$2`), variables, sequencing, string
constants, primitives (`export`, `exit`), invocation of library
functionality analogous to library functions (`mkdir`, `msgfmt`),
containers of data (directories), and nested namespaces.

It’s not entirely coincidental that this shell script lacks
conditionals, loops, and subroutines (other than the whole script).
It’s pretty common for shell scripts to be just straight sequences
like that: just a sequence of mutations, slightly parameterized.

### Tcl ###

Here’s some fairly normal Tcl code from the ArsDigita Community System,
somewhat reformatted:

    # calendar-defs.tcl
    # by philg@mit.edu late 1998
    # for the /calendar system documented at /doc/calendar.html 

    proc calendar_system_owner {} {
        return [ad_parameter SystemOwner calendar [ad_system_owner]]
    }

    proc calendar_footer {} {
        return [ad_footer [calendar_system_owner]]
    }

    ns_share ad_user_contributions_summary_proc_list

    if { ![info exists ad_user_contributions_summary_proc_list]
       || [util_search_list_of_lists $ad_user_contributions_summary_proc_list "/calendar postings" 0] 
          == -1 } {
        lappend ad_user_contributions_summary_proc_list \
            [list "/calendar postings" calendar_user_contributions 0]
    }

Again we see invocations of “primitives” (`if`, `lappend`, `list`);
two subroutine definitions (which could have had parameters but
don’t); variables; invocations of non-primitive functionality like
`util_search_list_of_lists` and `ad_parameter`; string constants (all
over the place), some of which are also integer constants; sequencing;
and a couple of conditionals.

Tcl is kind of close to shell scripts in a lot of ways — its only data
type is ostensibly strings — though it’s imported some aspects of
Lisp.  The ACS codebase is probably less shell-scripty than most Tcl
codebases.  I think of this script from the OpenTitan project as being
more typical of Tcl:

    # Copyright lowRISC contributors.
    # Licensed under the Apache License, Version 2.0, see LICENSE for details.
    # SPDX-License-Identifier: Apache-2.0

    source ./tcl/sta_common.tcl

    set overall_rpt_file "${lr_synth_rpt_out}/timing/overall"
    timing_report $lr_synth_clk_input $overall_rpt_file $lr_synth_sta_overall_paths

    set lr_synth_path_group_list [list]

    setup_path_groups $lr_synth_inputs $lr_synth_outputs lr_synth_path_group_list

    foreach path_group $lr_synth_path_group_list {
      puts $path_group
      set path_group_rpt_file "${lr_synth_rpt_out}/timing/$path_group"
      timing_report $path_group $path_group_rpt_file $lr_synth_sta_paths_per_group
    }

    exit

Here we have variables (which are in some sense parameters, since they
occur free), a loop, and sequencing, but no conditionals.  There’s
technically an assignment in the loop but the mutation to that
variable is kind of nonessential.  However, since it’s almost purely a
sequence, mutation is the only way for it to do anything useful.

Tcl and shell are both very easy to get started with, like keyboard
macros, but very bug-prone and kind of hard to understand.  Part of
the problem is that much of their semantics is based on string
interpolation.

### m4 ###

Speaking of which, what does typical m4 look like?  Dennis Ritchie’s
m4 is a Turing-complete macro language, in which (unlike in bash and
Tcl, like in Make) the results of macro substitution are subject to
further macro substitution, which allows you to write a loop by
writing a macro that conditionally expands to invoke itself.  For
example, although it has a built-in `len` operation that gives the
length of a string, we can also define a new one recursively in terms
of its built-in `ifelse`, `incr`, and `substr` operations:

    define(`length',`ifelse(,$1,0,`incr(length(substr($1,1)))')')

I adapted this from this example found on [the Softpanorama page about
m4][7]:

    define(len,`ifelse($1,,0,`eval(1+len(substr($1,2)))')')

[7]: http://www.softpanorama.org/Tools/m4.shtml

This definition, however, has a bug in it: the `2` should be `1`, a
bug introduced in an earlier version of this example in Kernighan and
Plauger’s _Software Tools_ in 01976 (p. 280).  It took me quite a
while to debug it because the definition line doesn’t quote `len`, so
my attempts to redefine it were (apparently) silently ignored; I was
instead defining a macro named `0`:

    $ m4
    define(len,`ifelse($1,,0,`eval(1+len(substr($1,2)))')')len(wotcha)
    3
    len(half)
    2
    define(len,`ifelse($1,,0,`eval(1+len(substr($1,1)))')')len(wotcha)
    3
    len(huh)
    2
    len(why does nothing make sense)
    13
    define(`len',`ifelse($1,,0,`eval(1+len(substr($1,1)))')')len(wotcha)
    6

The built-in `len` macro, by contrast, doesn’t get substituted unless
you offer it arguments (though this behavior is a GNU extension),
which permitted the first definition to succeed.

This accidentally-defined macro `0` can't be invoked by normal means
because its name isn’t “a word”, but it does exist:

    0(wibbling)
    0(wibbling)
    indir(0,wibbling)
    5

The output can build up macro names through concatenation, either
intentionally or unintentionally, which means that both the input† and
the output of the macro are subject to macro expansion.  I think that
is actually sufficient to construct conditionals without the `ifelse`
builtin, but I haven’t figured out how.

    define(foo,l$1)foo(en)(something)
    9
    foo(e)n(something)
    9

In _Software Tools_ (p. 281) Kernighan and Plauger warn:

> As you can see this is not the most transparent programming language
> in the world.  ...you get the hang of it.  But beware of becoming
> too clever with macros.  In principle, `macro` [the early version of
> m4 presented in the book] is capable of performing any computing
> task, but it is all too easy to write unreadable macros that cause
> more trouble than they save work.

Hopefully this gives some flavor of both m4’s capabilities and its
nightmarish bug-proneness.

Most current use of m4 is by way of autoconf.  Here’s part of the
autoconf script for an old version of libart:

    dnl AM_PATH_LIBART([MINIMUM-VERSION, [ACTION-IF-FOUND [, ACTION-IF-NOT-FOUND]]])
    dnl Test for LIBART, and define LIBART_CFLAGS and LIBART_LIBS
    dnl
    AC_DEFUN([AM_PATH_LIBART],
    [dnl 
    dnl Get the cflags and libraries from the libart-config script
    dnl
    AC_ARG_WITH(libart-prefix,[  --with-libart-prefix=PFX   Prefix where LIBART is installed (optional)],
                libart_prefix="$withval", libart_prefix="")
    AC_ARG_WITH(libart-exec-prefix,[  --with-libart-exec-prefix=PFX Exec prefix where LIBART is installed (optional)],
                libart_exec_prefix="$withval", libart_exec_prefix="")
    AC_ARG_ENABLE(libarttest, [  --disable-libarttest       Do not try to compile and run a test LIBART program],
                        , enable_libarttest=yes)

m4 is a templating language with dangerous delusions of grandeur,
capable of not only Turing-complete computation but higher-order
programming; but, as you can see, autoconf has managed to build its
own castle on that swamp, turning m4 into an entirely separate
programming language.  Unfortunately I don’t know enough about
autoconf to know what those ugly names mean and how they work
together.

Here’s an excerpt from [what claims to be a typical 02005 use of m4
for configuring Sendmail][6], which is a lot closer to vanilla m4.
You’ll note that it has a lot of `dnl` invocations; these are to
prevent spurious newlines from being emitted, but they are completely
unnecessary in this case because of the leading `divert(-1)`; it’s
just cargo-cult code:

    divert(-1)
    include(`/usr/share/sendmail-cf/m4/cf.m4')
    VERSIONID(`linux setup for my Linux dist')dnl
    OSTYPE(`linux')
    define(`confDEF_USER_ID',``8:12'')dnl
    undefine(`UUCP_RELAY')dnl
    undefine(`BITNET_RELAY')dnl
    define(`PROCMAIL_MAILER_PATH',`/usr/bin/procmail')dnl
    define(`ALIAS_FILE', `/etc/aliases')dnl
    define(`UUCP_MAILER_MAX', `2000000')dnl

[6]: https://www.ibm.com/developerworks/library/l-metaprog1/index.html

D. Robert Adams gives [this motivating example][8] in his introduction
to m4, sometime prior to 02006:

    define(`PAGE_HEADER',
    `<table border="0" background="steel.jpg" width="100%">
      <tr>
        <td align="left">$1</td> 
        <td align="right">$2</td>
      </tr>                                
    </table>
    <div align=right>
      Last Modified: esyscmd(`date')
    </div>
    ')

[8]: https://web.archive.org/web/20060907073945/www.csis.gvsu.edu/~adams/Blosxom/Scholarship/Papers/m4.asc

I probably *should* have included PHP, another templating language with
dangerous delusions of grandeur, but I don’t have anything that I
think is “typical PHP” code handy.

† Macro argument are macro-expanded by default, but you can quote
them.  Kernighan and Plauger make this change in the middle of their
chapter in _Software Tools_ about m4, saying, “for common uses like
replacing symbolic parameters, the two methods produce the same
result,” and it contributes considerably to m4’s already impressive
bug-proneness.

### Forth ###

Unfortunately I don't have a lot of confidence that this represents
“typical” Forth, but it’s one of the few Forth programs I’ve actually
used and didn’t write:

    \ tt.pfe        Tetris for terminals, redone in ANSI-Forth.
    \               Written 05Apr94 by Dirk Uwe Zoller,
    \                       e-mail duz@roxi.rz.fht-mannheim.de.
    \               Look&feel stolen from Mike Taylor's "TETRIS FOR TERMINALS"
    \
    \               Please copy and share this program, modify it for your system
    \               and improve it as you like. But don't remove this notice.
    \ ...

    : draw-pit      \ --- ; draw the contents of the pit
                    deep 0 do  i draw-line  loop ;

    : show-key      \ char --- ; visualization of that character
                    dup bl <
                    if  [char] @ or  [char] ^ emit  emit  space
                    else  [char] ` emit  emit  [char] ' emit
                    then ;

    : show-help     \ --- ; display some explanations
                    30  1 at-xy ." ***** T E T R I S *****"
                    30  2 at-xy ." ======================="
                    30  4 at-xy ." Use keys:"
                    32  5 at-xy left-key    show-key ."  Move left"
    \ ...
                    ;

    : update-score  \ --- ; display current score
                    38 16 at-xy score @ 3 .r
                    38 17 at-xy pieces @ 3 .r
                    38 18 at-xy levels @ 3 .r ;


Here we have three subroutines, one of which takes a parameter; they
contain a conditional and a loop; they invoke primitives like `@`,
`or`, `[char]`, and `emit`.  This excerpt barely uses variables,
`score`, `pieces`, and `levels`; `i` is not really a variable, though
it’s variable-like.  The parameter to `show-key` is not a variable.
`deep` and `left-key` are constants.  There’s a little arithmetic (on
ASCII codes for keys).  There are lots of places where one subroutine
invokes another; `draw-line` and `show-key` are parts of the Tetris
game.  `at-xy` comes with PFE.

I think this program uses less variables and longer subroutines than
is typical for Forth, but it shows how you can use high-level Forth
words to script at whatever level is comfortable for your application.

What do these things look like compiled?
----------------------------------------

The execution model for all of the above, except m4, are actually
fairly similar.  They’re eager imperative languages, equipped with
closed subroutines and primitive facilities for arithmetic and
constructing and accessing composite data structures.  They’re all
equipped with textual namespaces to use for describing dataflow
connections by connascence of name.  Though not all the control flow
shown above is single-entry single-exit, it *is* all “structured” in
the truer sense.  None of them have pattern matching or strong static
type checking, much less dependent types.  None of them (except m4)
have an outlandish execution model like Prolog, Erlang, Haskell,
Miranda, SNOBOL, or Icon, although Python and Lua do have one or
another kind of coroutine, and most of them can use threads.

There are some major practical differences.  Python lists don’t
support efficient FP-persistent incremental construction like my
initial example from Ur-Scheme used, and we lack garbage collection
entirely in C, C++, and Forth.  JS supports higher-order functions
with closures, a feature pioneered in Scheme but missing from C, C++,
Forth, and Elisp, and much less used in the other languages than in JS
and perhaps Lua.  Elisp, C, C++, Forth, Java, and Scheme don’t support
the effortless digraph-of-dictionaries-referencing-each-other memory
structure that characterizes Python, Perl, Lua, and JS, so I had to
write `(caar symlist)` instead of the more transparent `sym.name`.
Tcl, m4, and the Bourne shell don’t support references at all, except
by name.

Their scoping differs — Elisp has a single global namespace where it
temporarily binds local variables; Scheme has a single global
namespace and then lexically-nested block scopes within it; C has
three nested kinds of namespace (extern, file-static, and block scope,
which nests arbitrarily); Forth word scopes extend from declarations
forward until something hides the declaration, such as a change of
wordlist; and there are nested hierarchical namespaces in JS, Lua,
Java, Perl, and Python.  (I forget how scoping works in Tcl and m4.)
But for the most part these scoping differences disappear before
execution time.

Elisp, Forth, Scheme, Tcl, the Bourne shell, m4, and C don’t have a
concept of “object scope”, “class scope”, or “methods”, while Java,
Python, C++, JS, Lua, and Perl all have varying concepts.  All of
these languages have some way to invoke a function whose identity is
not known until runtime, although in Tcl and the Bourne shell this is
done with a string referencing a function in the global namespace, and
in C you have to do extra work to invoke a *closure*.  Java and C++
mostly treat objects as primary and methods as mere details of
objects, leading to things like the `Callable` interface, while
functions are first-class objects in Elisp, Scheme, Python, JS, Lua,
and Perl.

But most of these differences are sort of details.

### The Elisp implementation in more depth ###

Consider that initial example:

    (define interned-symbol-list '())
    (define (intern symbol)
      (interning symbol interned-symbol-list))
    (define (interning symbol symlist)
      (cond ((null? symlist) 
             ;; XXX isn't this kind of duplicative with the global variables stuff?
             (set! interned-symbol-list 
                   (cons (list symbol (new-label)) interned-symbol-list))
             (car interned-symbol-list))
            ((eq? symbol (caar symlist)) (car symlist))
            (else (interning symbol (cdr symlist)))))
    (define (symbol-value symbol) (cadr (intern symbol)))

We can translate this into Elisp as follows:

    (defvar interned-symbol-list '())

    (defun ur-intern (symbol)
      (interning symbol interned-symbol-list))

    (defun new-label ()
      (gensym))

    (defun interning (symbol symlist)
      (cond ((null symlist) 
             (setq interned-symbol-list 
                   (cons (list symbol (new-label)) interned-symbol-list))
             (car interned-symbol-list))
            ((eq symbol (caar symlist))
             (car symlist))
            (t
             (interning symbol (cdr symlist)))))

    (defun ur-symbol-value (symbol)
      (cadr (ur-intern symbol)))

This byte-compiles as follows, with the unprintable bytes removed:

    (defalias 'ur-intern #[(symbol) "(redacted)"
                           [symbol interned-symbol-list interning] 3])
    (defalias 'new-label #[nil "(redacted)" [gensym] 1])
    (defalias 'interning
      #[(symbol symlist) "(redacted)"
        [symlist symbol interned-symbol-list x new-label interning]
        4])
    (defalias 'ur-symbol-value #[(symbol) "(redacted)"
                                 [symbol x ur-intern] 3])

The redacted bytecodes disassemble as follows:

    byte code for ur-intern:
      args: (symbol)
    0       constant  interning
    1       varref    symbol
    2       varref    interned-symbol-list
    3       call      2
    4       return    

    byte code for new-label:
      args: nil
    0       constant  gensym
    1       call      0
    2       return    

Those two are very simple, just some eager nested expressions.
But `interning` contains conditionals, and a recursive loop,
although its tail-call nature is not visible in the bytecode:

    byte code for interning:
      args: (symbol symlist)
    0       varref    symlist
    1       goto-if-not-nil 1                 ; forward jump past the first cond case; note the double negation
    4       varref    symbol
    5       constant  new-label
    6       call      0
    7       list2                             ; build a 2-item list
    8       varref    interned-symbol-list
    9       cons      
    10      dup                               ; one reference for the variable, the other for return value
    11      varset    interned-symbol-list
    12      car       
    13      return    
    14:1    varref    symbol                  ; second case:
    15      varref    symlist
    16      dup       
    17      varbind   x                       ; note, not varset; this creates a local binding
    18      car                               ; `caar` compiles into two successive `car` bytecodes
    19      car       
    20      unbind    1                       ; discard useless x binding
    21      eq        
    22      goto-if-nil 2                     ; jump to the else
    25      varref    symlist
    26      car       
    27      return    
    28:2    constant  interning               ; set up the recursive call
    29      varref    symbol
    30      varref    symlist
    31      cdr                               ; reduce toward the base case
    32      call      2
    33      return    

`max-lisp-eval-depth` defaults to 500, and it does kill functions
like this in my version of Emacs when they tail-recurse too
deeply, whether byte-compiled or not.  That is, Elisp doesn’t
have tail-call elimination as Ur-Scheme does.

If you want a loop in Elisp, you need to use an explicit looping
construct, such as `while`, which gets compiled to
`goto-if-not-nil` bytecodes like the ones above, just backwards
instead of forwards.

    byte code for ur-symbol-value:
      args: (symbol)
    0       constant  ur-intern
    1       varref    symbol
    2       call      1
    3       dup       
    4       varbind   x
    5       cdr       
    6       car       
    7       unbind    1
    8       return    

Except for the special forms `define`, `cond`, and `setq`, the Lisp
source makes no distinction between primitive operations like `cdr`
and `null`, one one hand, and invocations of ordinary functions like
`interning` and `new-label`, on the other.  But the bytecode compiler
certainly does, as an efficiency hack; it has special bytecodes for
the basic Lisp functions (in this case, `list`, `cons`, `car`, `eq`,
`null` (merged with the `cond`), and `cdr`), as well as lots of
Emacs-specific operations like `save-excursion`, `forward-char`,
`insert`, and `forward-word`, which don’t occur here.  This makes the
bytecode very compact, though it still carries around a “constant
vector” for opcodes like `constant` and `varref` to index into.  It
just doesn’t have to indirect through the constant vector and look up
a function binding every time you invoke `car`, so it runs,
reportedly, about four times faster.

(In the case of `interning`, the constant vector is 6 items, so
presumably 56 more bytes including a count field; there's also a
“bytecode object” that ties the bytecode to the arguments, constant
vector, etc.  It doesn’t seem to have been designed for minimum memory
usage, despite the admirable compactness of the bytecode itself.)

The `exec_byte_code` function in the Emacs source code that executes a
bytecode-compiled function like the above is about 1500 lines of C.

The `interning` bytecode above is pretty short, 34 bytes.  Here’s the
implementation of the `Bvarref` bytecode that begins the
`interning` function, as well as its cousins:

	CASE (Bvarref7):
	  op = FETCH2;
	  goto varref;

	CASE (Bvarref):
	CASE (Bvarref1):
	CASE (Bvarref2):
	CASE (Bvarref3):
	CASE (Bvarref4):
	CASE (Bvarref5):
	  op = op - Bvarref;
	  goto varref;

	/* This seems to be the most frequently executed byte-code
	   among the Bvarref's, so avoid a goto here.  */
	CASE (Bvarref6):
	  op = FETCH;
	varref:
	  {
	    Lisp_Object v1, v2;

	    v1 = vectorp[op];
	    if (SYMBOLP (v1))
	      {
		if (XSYMBOL (v1)->redirect != SYMBOL_PLAINVAL
		    || (v2 = SYMBOL_VAL (XSYMBOL (v1)),
			EQ (v2, Qunbound)))
		  {
		    BEFORE_POTENTIAL_GC ();
		    v2 = Fsymbol_value (v1);
		    AFTER_POTENTIAL_GC ();
		  }
	      }
	    else
	      {
		BEFORE_POTENTIAL_GC ();
		v2 = Fsymbol_value (v1);
		AFTER_POTENTIAL_GC ();
	      }
	    PUSH (v2);
	    NEXT;
	  }

I guess this means that the Elisp definition of “the binding of a
variable” is sort of complicated.

FETCH isn’t a constant; it’s defined as `*stack.pc++`, and FETCH2 is
similar but fetches two bytes.  But in this case none of that comes
into play.

There are several other such groups of 8 opcodes: 6 with the operand
packed into the low three bits of the byte, and two “breakouts” that
consume one or two immediate bytes to get the real operand.
`stack-ref`, `varref`, `varset`, `varbind`, `call`, and `unbind` all
work this way; there are also four fixed-arity versions of the `list`
function plus a variable-arity version, three fixed-arity versions of
the `concat` function plus a variable-arity version, and some others.
There are 173 bytecodes defined in all, so it’s about 9 lines of code
per bytecode, but 48 of the bytecodes are these groups of 8.

### In SBCL ###

The same Elisp code is valid as Common Lisp code, and SBCL (1.0.57.x)
compiles `interning` as follows for amd64.  You will note that it is
noticeably more than 34+56 = 90 bytes, more like 439 bytes; our sweet
innocent 9-line Lisp function has exploded into 131 assembly
instructions:

    * (compile 'interning)

    INTERNING
    NIL
    NIL
    * (disassemble 'interning)

    ; disassembly for INTERNING
    ; 02A2FBF7:       4881FE17001020   CMP RSI, 537919511         ; no-arg-parsing entry point
    ;      BFE:       744B             JEQ L2
    ;      C00:       8BC6             MOV EAX, ESI
    ;      C02:       240F             AND AL, 15
    ;      C04:       3C07             CMP AL, 7
    ;      C06:       0F8559010000     JNE L11
    ;      C0C:       488BC6           MOV RAX, RSI
    ;      C0F:       488B48F9         MOV RCX, [RAX-7]
    ;      C13:       8BC1             MOV EAX, ECX
    ;      C15:       240F             AND AL, 15
    ;      C17:       3C07             CMP AL, 7
    ;      C19:       0F854D010000     JNE L12
    ;      C1F:       488B49F9         MOV RCX, [RCX-7]
    ;      C23:       4939C8           CMP R8, RCX
    ;      C26:       750A             JNE L1
    ;      C28:       488B56F9         MOV RDX, [RSI-7]
    ;      C2C: L0:   488BE5           MOV RSP, RBP
    ;      C2F:       F8               CLC
    ;      C30:       5D               POP RBP
    ;      C31:       C3               RET
    ;      C32: L1:   488B7E01         MOV RDI, [RSI+1]
    ;      C36:       498BD0           MOV RDX, R8
    ;      C39:       488B0540FFFFFF   MOV RAX, [RIP-192]         ; #<FDEFINITION object for INTERNING>
    ;      C40:       B904000000       MOV ECX, 4
    ;      C45:       FF7508           PUSH QWORD PTR [RBP+8]
    ;      C48:       FF6009           JMP QWORD PTR [RAX+9]
    ;      C4B: L2:   488D5424F0       LEA RDX, [RSP-16]
    ;      C50:       4883EC18         SUB RSP, 24
    ;      C54:       488B052DFFFFFF   MOV RAX, [RIP-211]         ; #<FDEFINITION object for NEW-LABEL>
    ;      C5B:       31C9             XOR ECX, ECX
    ;      C5D:       48892A           MOV [RDX], RBP
    ;      C60:       488BEA           MOV RBP, RDX
    ;      C63:       FF5009           CALL QWORD PTR [RAX+9]
    ;      C66:       480F42E3         CMOVB RSP, RBX
    ;      C6A:       488B75F0         MOV RSI, [RBP-16]
    ;      C6E:       4C8B45F8         MOV R8, [RBP-8]
    ;      C72:       488BFA           MOV RDI, RDX
    ;      C75:       498BD0           MOV RDX, R8
    ;      C78:       49896C2440       MOV [R12+64], RBP
    ;      C7D:       4D8B5C2418       MOV R11, [R12+24]
    ;      C82:       498D5B20         LEA RBX, [R11+32]
    ;      C86:       49395C2420       CMP [R12+32], RBX
    ;      C8B:       0F86E0000000     JBE L13
    ;      C91:       49895C2418       MOV [R12+24], RBX
    ;      C96:       498D5B07         LEA RBX, [R11+7]
    ;      C9A: L3:   488BC3           MOV RAX, RBX
    ;      C9D:       488950F9         MOV [RAX-7], RDX
    ;      CA1:       4883C010         ADD RAX, 16
    ;      CA5:       488940F1         MOV [RAX-15], RAX
    ;      CA9:       488978F9         MOV [RAX-7], RDI
    ;      CAD:       48C7400117001020 MOV QWORD PTR [RAX+1], 537919511
    ;      CB5:       49316C2440       XOR [R12+64], RBP
    ;      CBA:       7402             JEQ L4
    ;      CBC:       CC09             BREAK 9                    ; pending interrupt trap
    ;      CBE: L4:   488B05CBFEFFFF   MOV RAX, [RIP-309]         ; 'INTERNED-SYMBOL-LIST
    ;      CC5:       488B5021         MOV RDX, [RAX+33]
    ;      CC9:       498B1414         MOV RDX, [R12+RDX]
    ;      CCD:       4883FA61         CMP RDX, 97
    ;      CD1:       7504             JNE L5
    ;      CD3:       488B50F9         MOV RDX, [RAX-7]
    ;      CD7: L5:   4883FA51         CMP RDX, 81
    ;      CDB:       0F84A7000000     JEQ L14
    ;      CE1:       49896C2440       MOV [R12+64], RBP
    ;      CE6:       4D8B5C2418       MOV R11, [R12+24]
    ;      CEB:       498D4B10         LEA RCX, [R11+16]
    ;      CEF:       49394C2420       CMP [R12+32], RCX
    ;      CF4:       0F8693000000     JBE L15
    ;      CFA:       49894C2418       MOV [R12+24], RCX
    ;      CFF:       498D4B07         LEA RCX, [R11+7]
    ;      D03: L6:   49316C2440       XOR [R12+64], RBP
    ;      D08:       7402             JEQ L7
    ;      D0A:       CC09             BREAK 9                    ; pending interrupt trap
    ;      D0C: L7:   488959F9         MOV [RCX-7], RBX
    ;      D10:       48895101         MOV [RCX+1], RDX
    ;      D14:       488B1575FEFFFF   MOV RDX, [RIP-395]         ; 'INTERNED-SYMBOL-LIST
    ;      D1B:       488B4221         MOV RAX, [RDX+33]
    ;      D1F:       49833C0461       CMP QWORD PTR [R12+RAX], 97
    ;      D24:       7406             JEQ L8
    ;      D26:       49890C04         MOV [R12+RAX], RCX
    ;      D2A:       EB04             JMP L9
    ;      D2C: L8:   48894AF9         MOV [RDX-7], RCX
    ;      D30: L9:   488B0559FEFFFF   MOV RAX, [RIP-423]         ; 'INTERNED-SYMBOL-LIST
    ;      D37:       488B4821         MOV RCX, [RAX+33]
    ;      D3B:       498B0C0C         MOV RCX, [R12+RCX]
    ;      D3F:       4883F961         CMP RCX, 97
    ;      D43:       7504             JNE L10
    ;      D45:       488B48F9         MOV RCX, [RAX-7]
    ;      D49: L10:  4883F951         CMP RCX, 81
    ;      D4D:       7455             JEQ L16
    ;      D4F:       8BC1             MOV EAX, ECX
    ;      D51:       240F             AND AL, 15
    ;      D53:       3C07             CMP AL, 7
    ;      D55:       7552             JNE L17
    ;      D57:       488B51F9         MOV RDX, [RCX-7]
    ;      D5B:       E9CCFEFFFF       JMP L0
    ;      D60:       CC0A             BREAK 10                   ; error trap
    ;      D62:       02               BYTE #X02
    ;      D63:       18               BYTE #X18                  ; INVALID-ARG-COUNT-ERROR
    ;      D64:       54               BYTE #X54                  ; RCX
    ;      D65: L11:  CC0A             BREAK 10                   ; error trap
    ;      D67:       04               BYTE #X04
    ;      D68:       02               BYTE #X02                  ; OBJECT-NOT-LIST-ERROR
    ;      D69:       FE9501           BYTE #XFE, #X95, #X01      ; RSI
    ;      D6C: L12:  CC0A             BREAK 10                   ; error trap
    ;      D6E:       02               BYTE #X02
    ;      D6F:       02               BYTE #X02                  ; OBJECT-NOT-LIST-ERROR
    ;      D70:       55               BYTE #X55                  ; RCX
    ;      D71: L13:  6A20             PUSH 32
    ;      D73:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      D7B:       41FFD3           CALL R11
    ;      D7E:       5B               POP RBX
    ;      D7F:       488D5B07         LEA RBX, [RBX+7]
    ;      D83:       E912FFFFFF       JMP L3
    ;      D88: L14:  CC0A             BREAK 10                   ; error trap
    ;      D8A:       02               BYTE #X02
    ;      D8B:       1A               BYTE #X1A                  ; UNBOUND-SYMBOL-ERROR
    ;      D8C:       15               BYTE #X15                  ; RAX
    ;      D8D: L15:  6A10             PUSH 16
    ;      D8F:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      D97:       41FFD3           CALL R11
    ;      D9A:       59               POP RCX
    ;      D9B:       488D4907         LEA RCX, [RCX+7]
    ;      D9F:       E95FFFFFFF       JMP L6
    ;      DA4: L16:  CC0A             BREAK 10                   ; error trap
    ;      DA6:       02               BYTE #X02
    ;      DA7:       1A               BYTE #X1A                  ; UNBOUND-SYMBOL-ERROR
    ;      DA8:       15               BYTE #X15                  ; RAX
    ;      DA9: L17:  CC0A             BREAK 10                   ; error trap
    ;      DAB:       02               BYTE #X02
    ;      DAC:       02               BYTE #X02                  ; OBJECT-NOT-LIST-ERROR
    ;      DAD:       55               BYTE #X55                  ; RCX

(See file `open-coded-primitives.md` for a more complete dissection of
some SBCL output.)

I’m not quite sure where to start with this.  This looks like a type
test, with the type tag 7 in the low four bits of a pointer, and the
place it’s jumping to claims to signal an “OBJECT-NOT-LIST-ERROR”:

    ;      C00:       8BC6             MOV EAX, ESI
    ;      C02:       240F             AND AL, 15
    ;      C04:       3C07             CMP AL, 7
    ;      C06:       0F8559010000     JNE L11

So I guess SBCL is hoisting a type test from the various conditional
branches, all of which demand that the symlist be either null or a
cons, up to the top of the function.  Actually the null test may be
the thing above, so this might just be a pair test:

    ; 02A2FBF7:       4881FE17001020   CMP RSI, 537919511         ; no-arg-parsing entry point
    ;      BFE:       744B             JEQ L2

Maybe 537919511 (0x20100017) is SBCL’s representation of NIL, and RSI
is the second argument.  If so, it looks like it would pass that LISTP
test too, ending in a 7 as it does.  The consequent of that test is
this horrendous basic block, which looks like it’s doing the right
thing as it starts by allocating some stack space and loading in
NEW-LABEL in RAX.  Why SBCL opted to put this down near the end of the
function I’m not sure; maybe it decided that `symlist` (RSI) was
almost never going to be `NIL`.

    ;      C4B: L2:   488D5424F0       LEA RDX, [RSP-16]
    ;      C50:       4883EC18         SUB RSP, 24
    ;      C54:       488B052DFFFFFF   MOV RAX, [RIP-211]         ; #<FDEFINITION object for NEW-LABEL>
    ;      C5B:       31C9             XOR ECX, ECX

I guess that means ECX (not RCX!) has the argument count (0) we’re
going to pass to NEW-LABEL?  I did something similar in Ur-Scheme, but
it’s nice to not have to pass and check argument counts at run time.
(Notice that `interning` doesn’t in fact check its argument count!)

    ;      C5D:       48892A           MOV [RDX], RBP

That’s *storing* RBP into the stack; this is Intel operand order.

    ;      C60:       488BEA           MOV RBP, RDX

That way it can overwrite it with the new frame pointer.  Why it’s
allocating a new frame in the middle of a function I don’t know.

    ;      C63:       FF5009           CALL QWORD PTR [RAX+9]

Presumably this is loading the pointer to `NEW-LABEL`'s code from 9
bytes past the beginning of its FDEFINITION object, not actually
jumping there.

    ;      C66:       480F42E3         CMOVB RSP, RBX

Now, I’m not sure what’s going on *here*.  We expect `NEW-LABEL` to
have passed us back some kind of return status in the flags?  So that
we can decide whether or not to ... clobber the stack pointer with
RBX‽ Maybe this is how SBCL handles errors?  Anyway, then we set up
some registers from things stored in the stack frame, one of which is
presumably `NEW-LABEL`’s return value:

    ;      C6A:       488B75F0         MOV RSI, [RBP-16]
    ;      C6E:       4C8B45F8         MOV R8, [RBP-8]
    ;      C72:       488BFA           MOV RDI, RDX
    ;      C75:       498BD0           MOV RDX, R8
    ;      C78:       49896C2440       MOV [R12+64], RBP

Okay, now we’re saving our frame pointer at an offset from... R12‽

    ;      C7D:       4D8B5C2418       MOV R11, [R12+24]
    ;      C82:       498D5B20         LEA RBX, [R11+32]
    ;      C86:       49395C2420       CMP [R12+32], RBX
    ;      C8B:       0F86E0000000     JBE L13

Okay, at this point I have no idea what’s going on.

    ;      D71: L13:  6A20             PUSH 32
    ;      D73:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      D7B:       41FFD3           CALL R11
    ;      D7E:       5B               POP RBX
    ;      D7F:       488D5B07         LEA RBX, [RBX+7]
    ;      D83:       E912FFFFFF       JMP L3

Ohhh, it was checking to see if the nursery was full.  I guess R11 is
the allocation limit, and R12 is the allocation pointer.  Maybe 32 is
how many bytes we’re going to allocate.  So if we ran out of space in
the nursery we invoke a minor GC before continuing:

    ;      C8B:       0F86E0000000     JBE L13                    ; (duplicated context instruction above)
    ;      C91:       49895C2418       MOV [R12+24], RBX
    ;      C96:       498D5B07         LEA RBX, [R11+7]

So maybe it’s actually RBX that’s the allocation pointer?  I don't
know.  But I think we’re in the middle of an open-coded implementation
of two-argument LIST.

    ;      C9A: L3:   488BC3           MOV RAX, RBX
    ;      C9D:       488950F9         MOV [RAX-7], RDX

So now our newly allocated cons pointer is in RAX.  16 sounds like the
size of a dotted pair on a 64-bit machine.  So we stored... RDX into
it?  That originally came from `[RBP-8]`, so maybe it was new-label’s
return value.

    ;      CA1:       4883C010         ADD RAX, 16
    ;      CA5:       488940F1         MOV [RAX-15], RAX
    ;      CA9:       488978F9         MOV [RAX-7], RDI

Okay, so we’re creating a second cons, and poking its address into the
CDR of the previously allocated one, and now poking RDI (maybe our
first argument, `symbol`?) into the car.

    ;      CAD:       48C7400117001020 MOV QWORD PTR [RAX+1], 537919511

And this is our magic number again that might mean NIL, and we’re
poking it into what looks like the CDR of our second cons.  One
problem with the above hypotheses: the putative `symbol` and putative
new label are in the wrong order in the list.

    ;      CB5:       49316C2440       XOR [R12+64], RBP
    ;      CBA:       7402             JEQ L4
    ;      CBC:       CC09             BREAK 9                    ; pending interrupt trap

Aha, this is some runtime safety code to verify that RBP still (or
again) has the same value it had when we saved it earlier ... because
if it doesn’t, we have a pending interrupt‽ Anwyay, normally we’ll
jump over that `BREAK` and into the code that sets up to call `CONS`:

    ;      CBE: L4:   488B05CBFEFFFF   MOV RAX, [RIP-309]         ; 'INTERNED-SYMBOL-LIST
    ;      CC5:       488B5021         MOV RDX, [RAX+33]
    ;      CC9:       498B1414         MOV RDX, [R12+RDX]
    ;      CCD:       4883FA61         CMP RDX, 97
    ;      CD1:       7504             JNE L5

So we’re using PC-relative addressing to get to the value cell of this
global variable, and then we ... follow a couple of pointers in ways I
don’t understand, and expect to get 97.  What is that?  The ASCII code
for `` ` ``?  If that's not what we got, we jump to L5.  L5?

    ;      CD1:       7504             JNE L5
    ;      CD3:       488B50F9         MOV RDX, [RAX-7]
    ;      CD7: L5:   4883FA51         CMP RDX, 81
    ;      CDB:       0F84A7000000     JEQ L14

Well apparently if it wasn't 97, now we look someplace else to see if
we have an 81 (ASCII `Q`)?  I’m not sure what all this has to do with
consing the new list onto `interned-symbol-list` and sticking it in
`interned-symbol-list`?

    ;      D88: L14:  CC0A             BREAK 10                   ; error trap
    ;      D8A:       02               BYTE #X02
    ;      D8B:       1A               BYTE #X1A                  ; UNBOUND-SYMBOL-ERROR
    ;      D8C:       15               BYTE #X15                  ; RAX

Oh, apparently the value 81 in the word before a symbol’s value cell
signifies that the signal is unbound?  Because that is a possibility,
after all.  And the next thing we need to do is get the actual value
of the symbol to pass it to cons.  Still, I’m not sure why it makes
sense to jump from finding that RDX is 97 to checking to see whether
it’s 81.  So, what does the happy path look like?

    ;      CDB:       0F84A7000000     JEQ L14
    ;      CE1:       49896C2440       MOV [R12+64], RBP
    ;      CE6:       4D8B5C2418       MOV R11, [R12+24]
    ;      CEB:       498D4B10         LEA RCX, [R11+16]
    ;      CEF:       49394C2420       CMP [R12+32], RCX
    ;      CF4:       0F8693000000     JBE L15

This looks like another open-coded allocation with R11 and R12, and
saving off a copy of RBP again to check later if it’s been scroggled.
But now we’re using RCX, so evidently the allocation pointers aren’t
kept persistently in registers; they live at these weird offsets from
R11 and R12.  Actually maybe just from R12, since that's where we
loaded R11 from.  (R12 remains sacrosanct throughout.)

    ;      D8D: L15:  6A10             PUSH 16
    ;      D8F:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      D97:       41FFD3           CALL R11
    ;      D9A:       59               POP RCX
    ;      D9B:       488D4907         LEA RCX, [RCX+7]
    ;      D9F:       E95FFFFFFF       JMP L6

That seems right, although it seems kind of goofy to have all this
duplicated machine code hanging around, differing only in the
registers used and the address we jump back to.  So, what if
allocation succeeded?

    ;      CF4:       0F8693000000     JBE L15
    ;      CFA:       49894C2418       MOV [R12+24], RCX
    ;      CFF:       498D4B07         LEA RCX, [R11+7]
    ;      D03: L6:   49316C2440       XOR [R12+64], RBP
    ;      D08:       7402             JEQ L7
    ;      D0A:       CC09             BREAK 9                    ; pending interrupt trap

In the happy path we’ve stored `[R12+24]+16` back into `[R12+24]`,
thus allocating an additional cons cell.  We’re gonna open-code
`CONS`!  And now we overwrite RCX with, I guess, an address somewhere
in the middle of the cons.  And check again to see if our base pointer
has gotten cabbaged.

(I think the weird +7 stuff is because 7 is the type tag for dotted
pairs and NIL (and maybe value cells for global variables too?), so
SBCL just uses immediate offsets of +1 and -7 to access the `CDR` and
`CAR` respectively.)

I’m guessing that what comes next is that we’re going to store
`interned-symbol-list`’s value into the `CDR` of our new cell, and the
`LIST` we constructed earlier (or maybe its reversal?) into the `CAR`?

    ;      D0C: L7:   488959F9         MOV [RCX-7], RBX
    ;      D10:       48895101         MOV [RCX+1], RDX
    ;      D14:       488B1575FEFFFF   MOV RDX, [RIP-395]         ; 'INTERNED-SYMBOL-LIST
    ;      D1B:       488B4221         MOV RAX, [RDX+33]
    ;      D1F:       49833C0461       CMP QWORD PTR [R12+RAX], 97
    ;      D24:       7406             JEQ L8

Bingo!  RBX, remember, was set to `R11+7` when we were allocating the
list.  And RDX was the thing we fetched from `INTERNED-SYMBOL-LIST`
previously, which we were concerned might be 81 or 97.  (It wasn’t
81.)  Now we’re checking again to see if something or other related to
`interned-symbol-list` is 97 for some reason.  Why?  We already have
its value!  It’s already in the `CDR`!

    ;      D26:       49890C04         MOV [R12+RAX], RCX
    ;      D2A:       EB04             JMP L9
    ;      D2C: L8:   48894AF9         MOV [RDX-7], RCX
    ;      D30: L9:   488B0559FEFFFF   MOV RAX, [RIP-423]         ; 'INTERNED-SYMBOL-LIST
    ;      D37:       488B4821         MOV RCX, [RAX+33]
    ;      D3B:       498B0C0C         MOV RCX, [R12+RCX]
    ;      D3F:       4883F961         CMP RCX, 97
    ;      D43:       7504             JNE L10

Well, I guess if `[R12+RAX]` wasn’t 97, we’re going to store our new
CONS pointer there.  But if it was, we’re going to store the new list
pointer back at `interned-symbol-list`.

Hmm, maybe this 97 thing is some sort of garbage collector write
barrier?

Anyway, then we *again* check to see if something indexed off RCX
related to `interned-symbol-list` is 97.

    ;      D43:       7504             JNE L10
    ;      D45:       488B48F9         MOV RCX, [RAX-7]
    ;      D49: L10:  4883F951         CMP RCX, 81
    ;      D4D:       7455             JEQ L16

I feel like I’m in a loop.  This is Groundhog Day.  Time has no
meaning.  Now we’re loading the value of `interned-symbol-list`
*again* to see if it’s 81, *again*.  Even though we just set it.  To
an address that probably ends in a 7.

    ;      DA4: L16:  CC0A             BREAK 10                   ; error trap
    ;      DA6:       02               BYTE #X02
    ;      DA7:       1A               BYTE #X1A                  ; UNBOUND-SYMBOL-ERROR
    ;      DA8:       15               BYTE #X15                  ; RAX

And if it was 81, we again have an `UNBOUND-SYMBOL-ERROR`.  But how
does that make any sense?  Ohhh, now we’re past the mutation!  Now
we’re in the next line of code, where we return its `CAR`!

Well, if so, we should fetch from `[RCX-7]` next, then return.

    ;      D4F:       8BC1             MOV EAX, ECX
    ;      D51:       240F             AND AL, 15
    ;      D53:       3C07             CMP AL, 7
    ;      D55:       7552             JNE L17
    ;      D57:       488B51F9         MOV RDX, [RCX-7]
    ;      D5B:       E9CCFEFFFF       JMP L0

Yes!  We fetched the `CAR`!  And we put it in `RDX`!  After checking
the type tag to make sure it was a list.  That is what we were
checking, right?

    ;      DA9: L17:  CC0A             BREAK 10                   ; error trap
    ;      DAB:       02               BYTE #X02
    ;      DAC:       02               BYTE #X02                  ; OBJECT-NOT-LIST-ERROR
    ;      DAD:       55               BYTE #X55                  ; RCX

Yup.  Okay, what’s L0?  Are we going to clean up our stack frame and
return?

    ;      C2C: L0:   488BE5           MOV RSP, RBP
    ;      C2F:       F8               CLC
    ;      C30:       5D               POP RBP
    ;      C31:       C3               RET

Yup, exactly.  Also we carefully clear the carry flag first, in case
our caller is going to pull the same kind of `CMOVB` trick we did when
we called `NEW-LABEL`.  Apparently leaving the carry flag set means
some kind of exceptional condition or something in SBCL’s calling
convention.  So that was the compilation of these four lines of code:

            ((null symlist) 
             (setq interned-symbol-list 
                   (cons (list symbol (new-label)) interned-symbol-list))
             (car interned-symbol-list))

So, how about if it *wasn’t* nil?  Back to the top:

    ; 02A2FBF7:       4881FE17001020   CMP RSI, 537919511         ; no-arg-parsing entry point
    ;      BFE:       744B             JEQ L2
    ;      C00:       8BC6             MOV EAX, ESI
    ;      C02:       240F             AND AL, 15
    ;      C04:       3C07             CMP AL, 7
    ;      C06:       0F8559010000     JNE L11

So, once we get past the `JNE L11` guardian of the bridge, we know RSI
is a list, or at any rate NIL or a dotted pair.  Our next case is the
name-match case:

            ((eq symbol (caar symlist))
             (car symlist))

I suppose now we’re going to fetch `[RSI-7]` (the `CAR`), do the same
type-test on it, and then return its `CAR`?

    ;      C0C:       488BC6           MOV RAX, RSI
    ;      C0F:       488B48F9         MOV RCX, [RAX-7]
    ;      C13:       8BC1             MOV EAX, ECX
    ;      C15:       240F             AND AL, 15
    ;      C17:       3C07             CMP AL, 7
    ;      C19:       0F854D010000     JNE L12
    ;      C1F:       488B49F9         MOV RCX, [RCX-7]
    ;      C23:       4939C8           CMP R8, RCX
    ;      C26:       750A             JNE L1

Looks like it, although there’s an extra apparently useless register
move in there.  (`L12` is indeed another `OBJECT-NOT-LIST-ERROR`
trap).  And now we’re using an open-coded `eq` to check that `caar`
against... R8?  Could it be that `symbol`, our first argument, gets
passed in R8?  But in the other branch we overwrote R8 without
checking, and used the value in RDX... hmm, well, what happens next if
they *are* equal?

    ;      C28:       488B56F9         MOV RDX, [RSI-7]
    ;      C2C: L0:   488BE5           MOV RSP, RBP
    ;      C2F:       F8               CLC
    ;      C30:       5D               POP RBP
    ;      C31:       C3               RET

We load the `CAR` from `RSI` (`symlist`), which we’ve already verified
was a list so we don’t need to check again, and fall into the return
path, returning `RDX` as before.

So that’s what SBCL has decided is the “happy path” for the function;
it’s only 20 instructions.  Unfortunately SBCL is wrong about this;
this is just the second of the two base cases for the recursion
(search failure, then search success).  The inner recursive loop is
the part we haven’t seen yet:

            (t
             (interning symbol (cdr symlist)))))

Starting from L1:

    ;      C32: L1:   488B7E01         MOV RDI, [RSI+1]
    ;      C36:       498BD0           MOV RDX, R8
    ;      C39:       488B0540FFFFFF   MOV RAX, [RIP-192]         ; #<FDEFINITION object for INTERNING>
    ;      C40:       B904000000       MOV ECX, 4
    ;      C45:       FF7508           PUSH QWORD PTR [RBP+8]
    ;      C48:       FF6009           JMP QWORD PTR [RAX+9]

...that’s... it?  We load an argument count of 4 (‽ Maybe it’s
doubled?) into `ECX`, set up the function object in `RAX` in case the
function is a closure, set `RDI` to be the `CDR` of `RSI`, set `RDX`
to be `R8` (which apparently is somehow `symbol`, our first argument).
Then we push something on the stack (‽) and do a tail call by making a
jump.  So apparently whatever lurks at that address is expecting its
arguments in (`RDX`, `RDI`), not (`RSI`, `R8`) as we received them.
But this whole tail call is only 6 instructions.

So the inner recursive loop is 21 instructions, and the likely initial
misprediction due to SBCL getting the cases in the wrong order
probably only costs a single branch prediction error per program
restart, before the CPU learns to guess the branch correctly.

Of the total of 131 assembly instructions, in fact, only 92 are on any
of the three control paths that are present in the source; the other
39 instructions and pseudo-instructions are exception handlers tagged
onto the end of the function in case of type errors or running out of
memory.

Wait!  That’s not all!  It also included this bit of dead code in case
the arg count is wrong.  (Maybe some code somewhere else jumps to it.)

    ;      D60:       CC0A             BREAK 10                   ; error trap
    ;      D62:       02               BYTE #X02
    ;      D63:       18               BYTE #X18                  ; INVALID-ARG-COUNT-ERROR
    ;      D64:       54               BYTE #X54                  ; RCX

Upon reading on the web, it seems that SBCL doesn’t have user-level
write barriers, so I’m not sure what this 97 stuff is.  [The SBCL
Internals Manual has a Calling Convention section][3] which probably
answers some of the questions I had above; in particular [Full
Calls][4] explains the calling convention:

> Basically, we use caller-allocated frames, pass an fdefinition,
> function, or closure in `EAX`, argcount in `ECX`, and first three
> args in `EDX`, `EDI`, and `ESI`. `EBP` points to just past the start
> of the frame (the first frame slot is at `[EBP-4]`, not the
> traditional `[EBP]`, due in part to how the frame allocation
> works). The caller stores the link for the old frame at `[EBP-4]`
> and reserved space for a return address at `[EBP-8]`. `[EBP-12]`
> appears to be an empty slot that conveniently makes just enough
> space for the first three multiple return values (returned in the
> argument passing registers) to be written over the beginning of the
> frame by the receiver. The first stack argument is at
> `[EBP-16]`. The callee then reallocates the frame to include
> sufficient space for its local variables, after possibly converting
> any `&rest` arguments to a proper list. ... The above scheme was
> changed in 1.0.27 on x86 and x86-64 by swapping the old frame
> pointer with the return address and making `EBP` point two words
> later:

[3]: http://115.28.130.42/sbcl/sbcl-internals/Calling-Convention.html#Calling-Convention
[4]: http://115.28.130.42/sbcl/sbcl-internals/Full-Calls.html#Full-Calls

No idea what’s going on with R8 still.

Also, “[Unknown-Values Returns][5]” explains the carry-flag thing:

> For a single-value return, we load the return value in the first
> argument-passing register (A0, or EDI), reload the old frame
> pointer, burn the stack frame, and return. The old convention was to
> increment the return address by two before returning, typically via
> a JMP, which was guaranteed to screw up branch- prediction
> hardware. The new convention is to return with the carry flag clear.
> 
> For a multiple-value return, we pass the first three values in the
> argument-passing registers, and the remainder on the stack. ECX
> contains the total number of values as a fixnum, EBX points to where
> the callee frame was, EBP has been restored to point to the caller
> frame, and the first of the values on the stack (the fourth overall)
> is at `[EBP-16]`. The old convention was just to jump to the return
> address at this point. The newer one has us setting the carry flag
> first.
> 
> The code at the call site for accepting some number of unknown-
> values is fairly well boilerplated. If we are expecting zero or one
> values, then we need to reset the stack pointer if we are in a
> multiple-value return. In the old convention we just encoded a `MOV
> ESP, EBX` instruction, which neatly fit in the two byte gap that was
> skipped by a single-value return. In the new convention we have to
> explicitly check the carry flag with a conditional jump around the
> `MOV ESP, EBX` instruction.

But I suppose the CMOVB is a better alternative.

[5]: http://www.sbcl.org/sbcl-internals/Unknown_002dValues-Returns.html#Unknown_002dValues-Returns

Since `interned-symbol-list` is essentially a private variable for
`interning`, I added a declaration to tell SBCL to not worry so much
about type checking, although maybe `truly-the` is the real ticket:

    (defvar interned-symbol-list '())

    (defun new-label ()
      (gensym))

    (defun interning (symbol symlist)
      (declare (optimize (safety 0)))
      (cond ((null symlist) 
             (setq interned-symbol-list 
                   (cons (list symbol (new-label)) interned-symbol-list))
             (car interned-symbol-list))
            ((eq symbol (caar symlist))
             (car symlist))
            (t
             (interning symbol (cdr symlist)))))

Now the whole function is only 90 instructions, and the short path
(success) is down to 11 instructions, and the inner loop (the
recursive path) 12 instructions:

    ; disassembly for INTERNING
    ; 029F972D:       4881FE17001020   CMP RSI, 537919511         ; no-arg-parsing entry point
    ;      734:       7430             JEQ L2

    ;      736:       488B46F9         MOV RAX, [RSI-7]
    ;      73A:       488B48F9         MOV RCX, [RAX-7]
    ;      73E:       4939C8           CMP R8, RCX
    ;      741:       750A             JNE L1

    ;      743:       488B56F9         MOV RDX, [RSI-7]

    ;      747: L0:   488BE5           MOV RSP, RBP
    ;      74A:       F8               CLC
    ;      74B:       5D               POP RBP
    ;      74C:       C3               RET

    ;      74D: L1:   488B7E01         MOV RDI, [RSI+1]
    ;      751:       498BD0           MOV RDX, R8
    ;      754:       488B0565FFFFFF   MOV RAX, [RIP-155]         ; #<FDEFINITION object for INTERNING>
    ;      75B:       B904000000       MOV ECX, 4
    ;      760:       FF7508           PUSH QWORD PTR [RBP+8]
    ;      763:       FF6009           JMP QWORD PTR [RAX+9]

    ;      766: L2:   488D5424F0       LEA RDX, [RSP-16]
    ;      76B:       4883EC18         SUB RSP, 24
    ;      76F:       488B0552FFFFFF   MOV RAX, [RIP-174]         ; #<FDEFINITION object for NEW-LABEL>
    ;      776:       31C9             XOR ECX, ECX
    ;      778:       48892A           MOV [RDX], RBP
    ;      77B:       488BEA           MOV RBP, RDX
    ;      77E:       FF5009           CALL QWORD PTR [RAX+9]

    ;      781:       480F42E3         CMOVB RSP, RBX
    ;      785:       488B75F0         MOV RSI, [RBP-16]
    ;      789:       4C8B45F8         MOV R8, [RBP-8]
    ;      78D:       488BFA           MOV RDI, RDX
    ;      790:       498BD0           MOV RDX, R8
    ;      793:       49896C2440       MOV [R12+64], RBP
    ;      798:       4D8B5C2418       MOV R11, [R12+24]
    ;      79D:       498D5B20         LEA RBX, [R11+32]
    ;      7A1:       49395C2420       CMP [R12+32], RBX
    ;      7A6:       0F86B3000000     JBE L11

    ;      7AC:       49895C2418       MOV [R12+24], RBX
    ;      7B1:       498D5B07         LEA RBX, [R11+7]

    ;      7B5: L3:   488BC3           MOV RAX, RBX
    ;      7B8:       488950F9         MOV [RAX-7], RDX
    ;      7BC:       4883C010         ADD RAX, 16
    ;      7C0:       488940F1         MOV [RAX-15], RAX
    ;      7C4:       488978F9         MOV [RAX-7], RDI
    ;      7C8:       48C7400117001020 MOV QWORD PTR [RAX+1], 537919511
    ;      7D0:       49316C2440       XOR [R12+64], RBP
    ;      7D5:       7402             JEQ L4

    ;      7D7:       CC09             BREAK 9                    ; pending interrupt trap

    ;      7D9: L4:   488B05F0FEFFFF   MOV RAX, [RIP-272]         ; 'INTERNED-SYMBOL-LIST
    ;      7E0:       488B5021         MOV RDX, [RAX+33]
    ;      7E4:       498B1414         MOV RDX, [R12+RDX]
    ;      7E8:       4883FA61         CMP RDX, 97
    ;      7EC:       7504             JNE L5

    ;      7EE:       488B50F9         MOV RDX, [RAX-7]

    ;      7F2: L5:   49896C2440       MOV [R12+64], RBP
    ;      7F7:       4D8B5C2418       MOV R11, [R12+24]
    ;      7FC:       498D4B10         LEA RCX, [R11+16]
    ;      800:       49394C2420       CMP [R12+32], RCX
    ;      805:       766F             JBE L12
    ;      807:       49894C2418       MOV [R12+24], RCX
    ;      80C:       498D4B07         LEA RCX, [R11+7]

    ;      810: L6:   49316C2440       XOR [R12+64], RBP
    ;      815:       7402             JEQ L7

    ;      817:       CC09             BREAK 9                    ; pending interrupt trap

    ;      819: L7:   488959F9         MOV [RCX-7], RBX
    ;      81D:       48895101         MOV [RCX+1], RDX
    ;      821:       488B15A8FEFFFF   MOV RDX, [RIP-344]         ; 'INTERNED-SYMBOL-LIST
    ;      828:       488B4221         MOV RAX, [RDX+33]
    ;      82C:       49833C0461       CMP QWORD PTR [R12+RAX], 97
    ;      831:       7406             JEQ L8

    ;      833:       49890C04         MOV [R12+RAX], RCX
    ;      837:       EB04             JMP L9

    ;      839: L8:   48894AF9         MOV [RDX-7], RCX

    ;      83D: L9:   488B0D8CFEFFFF   MOV RCX, [RIP-372]         ; 'INTERNED-SYMBOL-LIST
    ;      844:       488B4121         MOV RAX, [RCX+33]
    ;      848:       498B0404         MOV RAX, [R12+RAX]
    ;      84C:       4883F861         CMP RAX, 97
    ;      850:       7504             JNE L10

    ;      852:       488B41F9         MOV RAX, [RCX-7]

    ;      856: L10:  488B50F9         MOV RDX, [RAX-7]
    ;      85A:       E9E8FEFFFF       JMP L0

    ;      85F: L11:  6A20             PUSH 32
    ;      861:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      869:       41FFD3           CALL R11

    ;      86C:       5B               POP RBX
    ;      86D:       488D5B07         LEA RBX, [RBX+7]
    ;      871:       E93FFFFFFF       JMP L3

    ;      876: L12:  6A10             PUSH 16
    ;      878:       4C8D1C2570724200 LEA R11, [#x427270]        ; alloc_tramp
    ;      880:       41FFD3           CALL R11

    ;      883:       59               POP RCX
    ;      884:       488D4907         LEA RCX, [RCX+7]
    ;      888:       EB86             JMP L6

I think this is mostly the same except for all the elided type checks.