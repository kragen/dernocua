I think the usual way to make a SERDES is with a shift register.
Let’s consider the deserialization case, where we want to, say,
convert a 2Gbps serial connection into a 31.25 MHz 64-bit parallel
interface.  We use a shift register with 64 bits in it clocked at
2GHz, toggling on average 32 bits per cycle and thus 64 gigatoggles
per second.  Every 64 cycles, we latch its current state into a 64-bit
output register, also toggling 32 bits on average, but this only
pushes us from 64 to 65 gigatoggles per second.

A different way to do this is with a logarithmically slowing series of
stages, like a DSP polyphase filter.  Initially we have a 2-bit shift
register which is clocked at 2GHz as usual.  Every 2 cycles, its
output gets shifted into the low bits of two more 2-bit shift
registers, which are thus clocked at 1GHz.  Every two shifts, their 4
bits of output are shifted into the low bits of four 2-bit shift
registers, which are clocked at 500MHz.  And similarly for 16 bits
clocked at 250MHz, 32 bits clocked at 125MHz, 64 bits clocked at
62.5MHz, and finally a 64-bit output latch register clocked at
31.25MHz.  This gives us 2 × 1 gigatoggles + 4 × 500 megatoggles + 8 ×
250 megatoggles + 16 × 125 megatoggles + 32 × 62.5 megatoggles + 16 ×
31.25 megatoggles × 2 = 10 gigatoggles per second, 6.5 times lower
power consumption than the straightforward shift register approach.
Moreover, it’s possible that the stages after the first 2 or 4 bits
can be driven at lower voltage or built in a simpler fashion, because
they don’t need to run nearly as fast.

Instead of 128 latches, now we need 190, but that’s less than 50%
overhead.  It’s probably useful to stagger the phases of the 7
different clocks to smooth out the load current and thus keep the
voltage rails more constant.

(You can of course just time-reverse this to get a serializer instead
of a deserializer.)

A slightly different way to design the device is as a binary tree of
127 flip-flops.  The flip-flop at the root of the tree is clocked at
2GHz, fed directly from the incoming data stream.  Each of its
children is clocked at 1GHz, but on alternate 2GHz clock cycles,
latching in the root's output.  Each 2GHz clock cycle, one of the four
latches at the next level of the tree is clocked, and so on.  So on
each 2GHz clock cycle, the bits shift along some 7-bit path from the
root of the tree down to one leaf, but which leaf changes every cycle.
This way the number of flip-flops clocked per cycle is constant at 7,
and there are on average 3½ toggles per cycle.

However, this is sort of cheating, because an output bit still changes
every 500 ps.  If you want to read it at 31.25MHz, that probably isn’t
okay, so you probably need another 64 bits to latch the output,
bringing this design back up to 191 latches, and clocking all the
output latches once every 64 cycles.

A different approach is to distribute the input signal using pass
transistors or write-enable bits or something instead of flip-flops.
This approach is exactly like the binary-tree approach, except without
all the intermediate tree levels: the input signal is buffered and
possibly latched at 2GHz and driven onto the inputs of 64 leaf
flip-flops, but only one of those flip-flops is clocked each cycle.
In a sense this requires 64-way fanout, which requires a fairly beefy
buffer for it to be fast.