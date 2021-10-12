I was watching the CHM David Liddle interview, and I was surprised by
[his description of the “spark pen”][2], a 01970s pointing device
using a glass panel and microphones, using the audio transit time of
the sound of a spark to measure the position you were pointing at.

[2]: https://youtu.be/k79rIfcNDfg "Oral history of David Liddle, interviewed by Hansen Hsu and Marc Weber, 02020-02-04, at 36 minutes 11 seconds"

You can get several MHz of acoustic bandwidth through a glass panel,
and a spark gap has submicrosecond rise time, so you can get
submicrosecond positioning precision — maybe a millimeter or so.  Two
things occurred to me about this:

1. A very low-tech way to get the spark is by mechanically opening a
   switch with the pen point, pushing two pieces of metal apart, while
   running current through those pieces of metal in series with an
   inductor, ideally with regulated current.  This is maybe easiest if
   the pen point doing the pushing is a glass rod, but metal would
   work too.

2. If you instead have a spark gap that can be induced to spark
   frequently by opening a high-voltage MOSFET in parallel with it,
   you can send a pseudorandom sequence of sparks that sounds like
   white noise, allowing you to track the pen’s position continuously
   instead of only on command.
