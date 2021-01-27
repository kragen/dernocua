Occurred to me that if you have a loop in machine code:

    loop: add r0, r1, r2
          mul r3, r2, r4
          sd r3, foo(r0)
          subi r0, 1
          beq r0, zero, loop

you can reasonably build the loop body into a dataflow graph, then
perhaps run it in a pipelined fashion at maybe as little as one loop
iteration per clock cycle.

What conditions are necessary for this to work?  You don’t necessarily
need a lot of ILP but you do need instructions that aren’t inside the
core critical path from one iteration of the loop to the next.  If it
requires a chain of five RTL operations to get the next state of the
loop variables from the current state, you aren’t going to be able to
run the loop at less than five clock cycles per iteration.

The idea here is that you do a sort of “place & route” either upon
entry to the loop or after figuring out that you’re going to be in the
loop for long enough to justify it.  Each value you produce as you go
through the loop gets assigned to a hardware register with a given ALU
function attached to it, with the inputs routed from the inputs to the
operation.  All branches of a conditional are computed, though some
care is needed here to prevent Spectre and also faults; the correct
results are selected out with a mux.

What if the loop body doesn’t fit in the hardware resources?  What
about non-innermost loops?
