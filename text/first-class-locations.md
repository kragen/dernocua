As mentioned in file `layout-typescript.md` one of the deficiencies of
the Lisp object-graph memory model is that *places* aren’t
first-class: object slots (instance variables or record fields), local
variables, global variables, array elements, and so on, can’t be
referred to in the language except indirectly.  In that note, I was
pondering the implications for LispM-style “presentations” in a
typescript, which I’d like to make interactively explorable by
default, but I’ve also written about a related question in terms of
IMGUI libraries.

In an IMGUI library, it’s very convenient to be able to say something
like (from [Dear ImGui]):

    ImGui::SliderFloat("this field is called f", &f, 0.0f, 1.0f);

[1]: https://github.com/ocornut/imgui

This works in C because we can pass a pointer to the global variable
`f` to the slider; similarly we can pass pointers to record (struct)
fields.  Golang and C++ are similarly empowered.  But this is
potentially unsafe, in the sense that we can also pass pointers to
local variables, the callee can save the pointer somewhere, and those
local variables can then go out of scope, leaving a dangling pointer
ready to cause mischief.

In languages like Pascal, a safe version of this facility is available
as “var parameters”: a parameter which, rather than being a local
variable with a copy of the passed-in value, is an alias to a location
provided by the caller.  This preserves the freedom for the compiler
to manage activation records with a stack discipline, while also
providing the ability for SliderFloat or whatever to get the reference
it wants.  The callee can pass this reference to other subroutines but
cannot reseat the reference or save it elsewhere.  C++’s reference
type works similarly.

On a modern machine, we could imagine saving activation records on the
heap and capturing references to them inside of, for example, textual
or graphical output, enabling a debugger to go back and trace the
“why” of a given value — as in [Bret Victor’s tree demo from
_Inventing on Principle_][0], for example.  In an IMGUI context we
can fake it by recreating the XXX

[0]: https://youtu.be/8QiPFmIMxFc?t=483 "8'3": ‘This has to work the other way too: that if I see part of the picture, I need to know what code was responsible for drawing it.  So I do the same thing: I hold down the Option key, and now as I move over each pixel of the picture, you’ll see on the right it’s jumping to the line of code that drew that pixel.’ http://vimeo.com/36579366"