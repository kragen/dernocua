Consider the family of hardware designs explored in file
`microlisp.md`.  Could you use these for centuries-long data
retention?

Flash chips are typically specified for 10-year data retention.  That
means the 4.4 or 16 nJ cited in that note to write each byte aren’t
forever; that’s per byte per decade.  If we want to keep 128 mebibytes
refreshed indefinitely, as discussed in “Egg of the Phoenix”, we need
0.6–2 J per decade, which is 2–7 nW, or about 40 nW per gibibyte.  So
the STM32L011 mentioned in file `microlisp.md`, with its microwatt of
stop-mode power, uses about as much power as keeping 25 gibibytes.

If you coupled that chip with 64–256 GiB of NAND Flash, all you’d need
is a power source that reliably provides 3–10 μW for decades or
centuries.  No conventional battery can do this; alternatives include
an Atmos-clock-style air-pressure energy harvesting system, as I
suggested in Dercuano (where I calculated that the daily barometric
variation of a few hundred pascals amounts to a theoretical maximum of
a few μW per liter, though Atmos clocks are reported to only use about
250 nW), or perhaps something like the Clarendon Dry Pile.  This is
much less than the 160 μW for 100 GB I estimated in Dercuano.
