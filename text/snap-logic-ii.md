In Derctuo I wrote a note about “majority DRAM logic” about logic
elements consisting of two CMOS inverters in a latch, shorted by a
pass transistor, as a sort of differential ampifier.  It occurred to
me today, though, that if for some reason you had to build digital
logic out of discrete components, a simpler version involving two
transistors rather than five might be more useful: an RTL latch.

The NPN version of this is rather simple: Vcc-(100k-b-NPN[Q1,
C=a]||82k-a-NPN[Q2, C=b])-GND, where a and b are two points to which
the collectors of the opposing resistors connect.  In [Falstad’s
circuit simulator][0]:

[0]: https://tinyurl.com/y2dsytfc

    $ 1 0.000005 10.20027730826997 66 5 43
    R 192 96 192 32 0 0 40 5 0 0 0.5
    r 192 96 192 192 0 100000
    t 304 304 384 304 0 1 -0.519462912774937 0.02791600975110754 100
    r 384 96 384 192 0 82000
    t 288 304 192 304 0 1 0.519462912774937 0.5473789225260445 100
    w 192 192 192 288 0
    w 384 192 384 288 0
    w 288 304 384 192 0
    w 304 304 192 192 0
    g 192 320 192 352 0 0
    g 384 320 384 352 0 0
    R 384 96 384 32 0 0 40 5 0 0 0.5
    s 384 192 464 192 0 1 true
    g 464 192 464 352 0 0
    s 112 192 192 192 0 1 true
    g 112 192 112 352 0 0
    o 6 64 0 4097 1.25 0.000390625 0 4 6 3 5 0 5 3

This simple simulation, just two resistors and two transistors, had a
metastability problem where both transistors were on in forward-active
mode.  If either ever gets into saturation, for example because you
press the other transistor’s switch, it pulls the base voltage of the
other down into cutoff, which supplies further base current to the
already-saturated transistor.  But it doesn’t find its way there if
it's ever in this initial balanced DC operating point.

(This is somewhat worrisome, because I’d like to ensure that this
equilibrium, which must of course exist, is an unstable one: the
positive feedback coefficient around the operating point ought to be
more than 1.  But I suspect that is not the case, and my attempts to
solve it by aimlessly adding resistors have failed.  It is of course
possible to solve the problem with more transistors, but I feel that
it should be possible to fix it with resistors...)

This basic flip-flop element has fairly strong current-sinking
capability (as an output) and fairly weak current-sourcing capability,
differing by a factor of β.  5 volts over 100kΩ gives us 44 μA of
pullup current, which the presumed β=100 of the transistors amplifies
to 4.4 mA.  These can be equalized somewhat with emitter resistors,
and flip-flops of various strengths can be made; in the case where
driving a strong one from a weak one is desired, an inverting buffer
of the same nature (NPN[C=1k-Vcc], or even a Darlington) can be
interposed.

The LGP-30 approach mentioned in the earlier note, in which flip-flop
Set and Reset inputs are driven by separate signals, is likewise
applicable.

One interesting clocked-logic approach from the 1960s is [Autonetics’s
four-phase logic, recently explained by Ken Shirriff in his
explorations of the 1969 Sharp EL-8 pocket calculator][12], which was
pretty interesting.  In PMOS a clocked four-phase-logic inverter was
three transistors, one of which was just used as a diode, and the
clock signals were the only power connections to the gates.

[12]: http://www.righto.com/2020/12/reverse-engineering-early-calculator.html

Here’s [a working-in-simulation bipolar-logic version of the
four-phase inverter Shirriff explains][1], along with a four-phase
clock generator:

    $ 1 0.000005 2.5790339917193066 65 5 43
    R -112 144 -144 144 0 4 40 2.5 2.5 0 0.5
    a -32 400 64 400 9 5 0 1000000 0 1.7540000000326756 100000
    w -112 144 -32 144 0
    w -112 144 -112 224 0
    w -112 224 -112 304 0
    w -112 304 -112 384 0
    w -112 384 -32 384 0
    w -112 304 -32 304 0
    w -112 224 -32 224 0
    R -64 112 -64 80 0 0 40 5 0 0 0.5
    r -64 112 -64 176 0 100000
    r -64 176 -64 256 0 100000
    r -64 256 -64 336 0 100000
    r -64 336 -64 416 0 100000
    w -64 416 -32 416 0
    g -64 416 -64 432 0 0
    w -64 336 -32 336 0
    w -64 256 -32 256 0
    w -64 176 -32 176 0
    a -32 320 64 320 9 5 0 1000000 1.2500000000148503 1.7540000000326756 100000
    a -32 240 64 240 9 5 0 1000000 2.500000000006107 1.7540000000326756 100000
    a -32 160 64 160 9 5 0 1000000 3.7500000000030536 1.7540000000326756 100000
    I 64 320 160 320 0 0.5 5
    150 160 336 272 336 0 2 0 5
    w 64 400 160 400 0
    w 160 400 160 352 0
    I 64 240 160 240 0 0.5 5
    150 160 256 272 256 0 2 5 5
    w 160 272 160 352 0
    w 64 240 64 192 0
    150 160 176 272 176 0 2 0 5
    w 64 192 64 112 0
    w 64 112 272 112 0
    I 64 160 160 160 0 0.5 5
    w 64 192 160 192 0
    207 272 336 272 368 4 φ1
    207 272 256 272 288 4 φ2
    207 272 176 272 208 4 φ3
    207 272 112 272 144 4 φ4
    d 368 112 464 112 2 default
    w 464 112 528 112 0
    c 528 112 528 176 0 1e-8 7.368162603581507 0.001
    g 528 176 528 208 0 0
    t 432 272 464 272 0 1 -7.368162450073534 -0.022391121926448803 100
    R 368 208 368 176 0 0 40 5 0 0 0.5
    s 368 208 368 272 0 1 false
    r 368 272 368 368 0 100000
    g 368 368 368 384 0 0
    207 368 112 368 144 4 φ1
    w 464 288 464 336 0
    t 448 352 464 352 0 1 0.5146280159592591 0.5325562677671504 100
    207 400 352 400 384 4 φ2
    207 464 416 464 448 4 φ1
    r 464 368 464 416 0 100
    207 528 112 576 112 4 /Q
    r 368 272 432 272 0 1000000
    r 400 352 448 352 0 100000
    d 464 112 464 256 2 default
    207 368 272 336 272 4 Q\sinput
    o 35 64 0 4098 5 0.05 0 2 35 3
    o 36 64 0 4098 10 0.05 0 2 36 3
    o 37 64 0 4098 5 0.00009765625 0 2 37 3
    o 38 64 0 4098 5 0.00009765625 0 2 38 3
    o 54 64 0 4099 10 0.00009765625 1 2 54 3

[1]: https://tinyurl.com/yxeeksny

This inverter is powered from phases φ1 and φ2; the φ1 pulse charges
its output capacitor, and then φ2 discharges it if the input is high.
The circuit is φ1->-/Q-(10nF-GND||>-x), Q-1M-NPN[Q1, C=x]-y,
φ2-100k-NPN[Q2, C=y]-100-GND.  So φ1 charges up the /Q output through
a diode when φ1 is high; a capacitor to ground then holds the output
high when φ1 goes low, unless point x pulls the capacitor down through
a second diode (unnecessary in the PMOS version, but necessary to
prevent the base-collector junction on the input transistor from going
into forward conduction.)  Point x is pulled to ground via the input
NPN transistor Q1, which sees the input through a 1MΩ base resistor,
and whose emitter goes to the collector of Q2.  Q2's base is connected
to φ2 via a 100kΩ resistor, and its emitter is connected to φ1 via a
100Ω resistor, so Q2 only pulls Q1's emitter to ground when φ2 is high
and φ1 is low.  Then the circuit’s output is valid during φ3 and φ4.
Whew!

As it happens φ2 (the “sample phase”) is never low when φ1 (the
“precharge phase”) is high, so the diode nature of Q2’s base-emitter
junction is not relevant here; a relay winding between the two phases
would also work.  Similarly Q1 would work just as well being a relay,
but of course wouldn't be able to run at 60kHz like in the original
calculator.

Series-parallel combinations of input transistors can provide
arbitrary monotonic logic functions before the inversion, at a cost of
one extra transistor (and perhaps base resistor) per input, and of
course you can use diodes too.

φ3 and φ4 work in exactly the same way as φ1/φ2, and you can
additionally use the same design with φ1/φ3 and φ3/φ1, although in
that case it *does* matter that Q2 stays off when the sample phase
goes low, reverse-biasing its base-emitter junction.  Otherwise the
circuit is exactly the same.

