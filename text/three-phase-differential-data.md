Single-ended data transmission, as used in RS-232, is limited in noise
immunity, so higher-speed data is commonly transmitted with
differential signaling.  Unfortunately, this requires twice as much
wire.

AC power transmission faces a similar problem: unless you’re willing
to use the planet as your current return path (commonplace in parts of
Brazil and for submarine cables) you need to carry the current from
the power plant to the load — and then back again.  In AC power
transmission, this problem (as well as the problem of starting large
AC motors) is solved with three-phase power transmission: three wires
carry alternating voltages 120° out of phase with one another.  The
sum of the three phasors is zero: always approximately, and for
balanced loads like a three-phase motor, exactly.  This permits
carrying thrice as much power over only 50% more wires than the
single-phase approach used in household outlets.

If you replace your twisted-pair data transmission lines with twisted
triads, for 50% more wires you can’t get *thrice* the data rate, but
you *can* get *twice* the data rate, with roughly the same
noise-immunity benefit you get from twisted-pair differential
signaling.  The third wire carries a balancing voltage and current
which maintains the triad’s net voltage and current at 0; the mutual
inductances and capacitances of the three wires remain constant along
their lengths, just like in a twisted pair, and because these mutual
inductances and capacitances are are all equal, crosstalk can be
accurately canceled.  At low speeds this balancing voltage can be
arranged straightforwardly by driving the third wire with an opamp
that maintains a constant reference voltage at a summing Y junction;
higher speeds might require more elaborate drivers that multiplex the
third wire among, in the bilevel case, four compensation voltages.

Attempts to extend this approach to differential quads, quintuplets,
and so on will suffer from the fact that the balancing wire and signal
wires cannot all be equidistant, at least in three-dimensional space.
The result is that either data edges on one signal wire that couple
equally to two other signal wires cannot be perfectly canceled on both
of them by a single balancing wire, or data edges on one signal wire
that couple *unequally* to two other signal wires cannot be perfectly
canceled on both of them by a single balancing wire.  Also, if the
voltage levels on the three or more signal wires were uncorrelated,
the balancing wire would be subject to much larger voltage swings.
Still, MIMO approaches could yield fruit with *n* wires while
retaining net zero voltage and current on the wire bundle; in theory
it’s just a question of solving a well-conditioned, very nearly linear
system of *n* equations in *n* unknowns, one of which is the
common-mode noise.

The problem of unequal voltage swings and complex analog line drivers
can be solved, at the cost of reduced data rates, with a
constant-weight *m*-of-*n* code like the 2-of-5 code.  In a sense the
1-of-3 encoding SETUN used for its three-way flip-flop(-flap?)s was a
constant-weight encoding providing 1.58 bits over three “differential”
wires.  Decoding such a constant-weight code could be considerably
simpler than a more sophisticated MIMO approach, merely amounting to
comparing each wire to a threshold from a summing junction; a balanced
code on 8 wires would provide 6.1 bits of data per clock (70 valid
codes), and a 9-of-19 code on 19 wires would provide 15.9 bits per
clock (8314020 valid codes).

More generally, if you can statically estimate (linear, memoryless)
crosstalk coefficients between particular wires, you can build a
summing junction that computes the “predicted” crosstalk for each
wire, to be used as the comparison threshold for that wire, thus
mostly canceling that crosstalk.
