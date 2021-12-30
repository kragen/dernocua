As a kid I was always confused by the requirement to “show your work”
on math tests, which is to say, demonstrate how you derived your
answer.  Why did it matter how I got the answer?  What mattered was
whether the answer was right or wrong, wasn’t it?

This comes out of the street-fighting approach to math commonly taught
in elementary schools, in which math is treated as a skill used to
come up with answers to potentially difficult puzzles --- or, worse,
merely a means to pass math tests.  (And surely one motivation for
demanding the “showing of work” is to reduce cheating on tests.)  One
alternative approach is to see math as a medium of creative
expression, as explained in Lockhart’s Lament, in which the tools and
materials are abstract ideas rather than clay or paintbrushes.  But
another alternative is to see math as a form of argument, whose
quality is to be judged by its convincingness and fallibility.

That is, although I could tell you that 48303 / 27 = 1789, even if you
trust me, it may not be immediately obvious to you whether I am
mistaken or not.  If you are going to rely on this fact for some
purpose, such that you will put yourself in a position to be harmed if
it turns out to be false, you might want some sort of stronger
assurance than merely my fallible assertion.  And this is the
objective of “showing your work” if you write down the partial sums:

       1789
       × 27
      -----
      12523
    + 3578
    -------
      48303

This is an abbreviated notation for a syllogistic argument for the
truth of my original assertion, which we could partly unpack as
follows: 1789 × 7 = 12523; 1789 × 20 = 35780; 12523 + 35780 = 48303;
therefore 48303 / 27 = 1789.  (There are several other implicit
premises as well, such as the distributive law of multiplication.)

Although it happens to be correct, this is not a very good argument,
because each of the three premises I stated explicitly above is less
than obvious.  If I had written 1789 × 20 = 35870, for example, it
might take you a while to spot the error.  I claim that a principal
objective of math is to *state arguments in such a way as to make any
errors obvious*.  Such an argument can be far more convincing: if it
contains no obvious errors, then it contains no errors at all.  Then,
if its premises are correct, so is its conclusion, even if its author
is untrustworthy.

I think this is a better argument for the same proposition: 1789 +
1789 = 3578; 3578 + 1789 = 5367; 53670 - 5367 = 48303; therefore 48303
/ 27 = 1789.  These calculations are simpler and so if there is an
error in them it should be easier to spot, although perhaps the
reasoning requires a little more explaining (30 - 3 = 27, so 30 × 1789
- 3 × 1789 = 1789 × 27).

In practice, though, I checked these calculations mostly by doing them
with computer programs that I believe are unlikely to produce wrong
answers, and it’s common nowadays for people to use spreadsheets, cash
registers, or pocket calculators for this purpose.  Arguably,
repeating a calculation a few times with different calculators is more
trustworthy than mental checking.  But there’s still a great deal of
potential for error in the process of invoking the calculator, as well
as from hardware and software bugs.

This mathematical form of argument is the central ratchet that has
allowed human knowledge to advance rather than falling backward over
the last few centuries, because, just as money permits us to gain
safety and sustenance by the efforts of not only honest hardworking
folk but even treasonous cutpurses and greedy misers, math allows us
to gain true and trustworthy knowledge of the universe from the
reasoning of half-mad alchemists and deluded fools, because we can
sift the occasional flake of gold from the mountains of superstitious
dross they produced; by mathematical argument we can recognize a truth
even when beset on all sides by nonsense, and often we can perfect a
near-truth into a truth, and just as easily we can spot a flaw even in
the sweetest honey of theory, dripping from the mouth of the finest of
philosophers.

Unfortunately, at present we cannot do the analogous operation for
results produced from a computer program rather than a mathematical
formula.  Often not enough information is published to even allow us
to reproduce the published results by re-executing the program used by
the original researcher; when such reproduction is possible, often the
results diverge, and the error is quite frequently a different
environment on the computer of the researcher attempting the
reproduction, a situation more closely resembling chemistry than
mathematics.  Even if the results reproduce the original results
correctly, they may well be due to a bug present in software installed
on both computers.
