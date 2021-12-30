2-D cutting fabrication techniques like laser cutting, plasma torch
table cutting, waterjet cutting, and CNC milling are often immensely
faster than 3-D printing.  But they typically require more assembly
steps and more difficult design.

Cutting sheet metal in particular is promising because you can bend it
after cutting, both hardening it and getting a 3-D shape.  Given some
sort of press, you can bend it by pressing it between dies cut from
the same sheet metal, either many of them stacked up or a smaller
number in a crisscross pattern (ideally not quite at 90°).  With
something like a beading roller, you can use a fairly small die to
make a fairly large part.  Metal has a lot of other advantages.

Another potentially interesting process for getting a solid 3-D
surface from a 2-D contour is to roll up or accordion-fold a strip,
using some minimal number of alignment slots to get the successive
layers properly aligned.

Laminated sheet metal is actually better than solid metal for
electromagnetic purposes, although random mild steel will perform an
order of magnitude worse than genuine electrical steel.  Permanent
magnets are not needed for variable reluctance motors.

Matter bandwidth
----------------

Ultimately I think the figure of merit that matters most for digital
fabrication processes is the "matter bandwidth", which (being rusty on
my Shannon) I roughly define as the number of bits exceeding the noise
floor you can impress into a physical object per second.  If you can
produce a surface with 100-micron precision, then the height of a
point on that surface anywhere in a 3.2-mm range counts as 5 bits.
But if you have 10-micron precision, that's a little over 8 bits.  The
reason is that if you can make things more precise, you can make them
smaller, while if you suffer less precision, they have to be bigger.

And smaller is actually faster.  After having a system that works at
all, speed is my most important goal: being able to iterate quickly
will enable me to overcome almost any obstacle at all, from fragility
(because I can make a stock of spare parts in time) to debugging
(because I can try many things) to political opposition (because it
arises too slowly to be relevant).  This is an enormous reversal from
coal-age industrial processes in which mass production and mass
processing was of paramount importance.

Very roughly, I think that for a production time of one month (2.6
megaseconds) and a production complexity of a million "voxels", one
voxel per 2.6 seconds is adequate.  But an order of magnitude better
than that would get us out of marginal territory.  Given that existing
machinery (e.g., laser and inkjet printers) is seven orders of
magnitude faster than this, and even RepRap FDM printers are about 10
voxels per second, it seems likely to be achievable, but of course
that's drawing on billions of dollars of industrial infrastructure in
the form of semiconductor fabs.

(Actually, if we figure 90 mm/s is a normal print speed, 500 microns
is a normal trace width, and the resolution is 100 microns, that's
4500 voxels per second.)

Looking at [the Maker's Muse product shill infomercial for the US$2900
Phrozen Sonic Mega 8K][0] LCD stereolithography printer, I see it
prints layers of 7680×4320 43-micron pixels.  The salesman in the
video says it he set the first (50-micron) layer to cure for 50
seconds to get it to work reliably in his cold winter, but that this
is a really long cure time.  I think 20 seconds is a more normal layer
time for these UV-cured resin printers, but if we suppose it's 30
seconds, that's still 1.1 megavoxels per second.  Later on, he showed
that he got 10 hours 11 minutes for a build plate full of 35-mm-tall
miniatures, which I think works out to 52.4 seconds per 50-micron
layer, mostly due to peel time, since the cure time per layer was only
4 seconds.  (The company claims 70 mm/hour print speed, which would be
either 2.6 seconds per layer or, more likely, much thicker layers.)
He compared to the much smaller Photon Mono X with cure times of 1.5-2
seconds and 60 mm/hour maximum print speed with, I assume, a similar
layer height.

[0]: https://www.youtube.com/watch?v=p6wljI-6EzI

If we compare to laser printers, they are typically 600 dpi (23.6kp/m
or 558Mp/m²), and the A4-sized ones (0.06237 m², thus 34.8 million
pixels) typically print between 5 and 22 pages per minute, which works
out to 2.9 million to 12.8 million pixels per second.  They're not in
very precise places, but the imprecision with respect to the other
pixels is predictable and consistent.  Unfortunately, it's difficult
to convert laser-printed pages into almost anything else; if you print
on transparency film such as cellulose acetate, you may be able to
take a mold of the printout, but it's hard to stack that up.
