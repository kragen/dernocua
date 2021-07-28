(This note has several calculations I’ve noted errors in that need
redoing.)

It’s often stated that one of the advantages of the Chinese windlass
mechanism is that it’s self-locking, or not back-drivable.  Another
advantage is that, being a differential mechanism, its mechanical
advantage can be arbitrarily large.  A third advantage, rarely
remarked upon perhaps because of its obviousness, is that since most
of the mechanism is purely in tension, it can extend over a great
distance while containing very little mass; it is practical to
construct a Chinese windlass that applies substantial forces between
points a hundred meters distant, weighing only 200 grams, half of
which is 1-mm UHMWPE cord.  A fourth is that most of the contact in
the mechanism is not sliding contact and thus does not cause abrasive
wear or frictional losses; only the bearing of the windlass drum has
sliding contact, and possibly the bearing of the pulley.

In a sense the third advantage above is the opposite extreme from
Reuleaux’s definition of a machine as something that imposes motion in
desired degrees of freedom but prevents it in all others — that is,
has effectively infinite rigidity in all other degrees of freedom.
The differential pulley in the windlass mechanism is imposes motion in
one desired degree of freedom, employing motion in a second degree of
freedom (usually attached to a bearing so this can be ignored); it is
somewhat restrained in a third degree of freedom, though not very
rigidly; and has effectively infinite *compliance* in the remaining
four degrees of freedom.  In a well, that is, the bucket can swing
back and forth and twist around while receiving only very small
restoring elastic forces from the rope’s minuscule rigidity.

One disadvantage of the mechanism is that the differential mechanical
advantage can be somewhat imprecise; as layers of rope build up on the
drums, they change the drums’ effective radius and potentially their
difference in radius.  Grooved drums can prevent this from happening,
but only if the drums are long enough.

The M.A. of the mechanism is the ratio between the crank arm and the
*difference* in drum radii.  This implies that the absolute drum radii
can be as large or small as desired without changing the M.A.
However, if the difference in radii is, say, 1mm, you only get 6.28mm
of elongation per revolution, regardless of whether that revolution is
running 100 mm of cord through the differential pulley or 100 m of it.
So, this allows you to increase the rigidity of the drum, which might
allow you to increase its length, thus permitting more unlayered cord,
but not to use less layers of cord in the same length.

The wrapping of the cable on the drum can be protected from
side-loadings by running the cable through a grommet in between the
drum and the differential pulley.  That way the angle at which the
cable rolls onto the drum only depends on where the cable is on the
drum and the tension on the cable, not on any other side-loadings.  If
the grommet is sort of hyperboloid-of-one-sheet-shaped, it will avoid
kinking the cable there and avoid any concentrations of force at one
point on the grommet, and if it is made of a hard material such as
sintered sapphire, like sparkplugs, it will not suffer much from
abrasion.

The self-locking nature of the mechanism is an advantage for some
uses, but being able to use an arbitrarily large mechanical advantage
in reverse would be useful in some situations.  The reason it is
usually self-locking is that the frictional torque is the side loading
on the bearing, multiplied by the bearing’s radius, multiplied by the
bearing’s coefficient of friction μ; and the frictional force
resisting the differential pulley is that torque divided by the
effective moment arm, which is the difference in radii.  Typical
coefficients of friction for dry journals are 0.2–1.6; for example,
[bronze on cast iron is 0.22][0], wood on dry wood is typically
0.25–0.5, steel on steel is 0.5–0.8, and copper on copper is 1.6.
Usually the side loading on the bearing *is* the force on the
differential pulley.  So, if μ = 0.22, then 100 N of pull on the
differential pulley will generate 22 N of friction at the bearing.

Suppose, for example, that the journal is 20 mm radius (40 mm
diameter), and the radius difference is 10 mm (say, the drums are of
radii 50 mm and 60 mm).  So the torque on the shaft from the
differential pulley is 100 N · 60 mm - 100 N · 50 mm = 100 N · (60 mm
- 50 mm) = 100 N · 10 mm = 1 N m.  And the torque from the friction is
22 N · 20 mm = 0.44 N m.  So in this case the mechanism will not be
self-locking.  (It will be somewhat efficient: 1.44 N m from the crank
will be converted to 1 N m at the drum and thus 100 N, for 69%
efficiency.)

If we increase μ past 0.5, though, (the reciprocal of the M.A.), the
frictional torque rises past 1 N m, the mechanism becomes
self-locking, and its efficiency falls below 50% (assuming static and
dynamic friction are equal), because the frictional force has exceeded
the force from the slow/strong end of the mechanism, the differential
pulley.  The same thing happens if we leave μ at 0.22 and increase the
M.A. past 4.55, for example by increasing the journal radius from
20 mm to 46 mm or by decreasing the difference in radii from 10 mm to
4.3 mm.

[0]: https://www.engineeringtoolbox.com/friction-coefficients-d_778.html

This is a case of a general phenomenon where mechanisms with
efficiency above 50% are backdrivable, and those with lower
efficiencies are instead self-locking, under certain simplifying
assumptions.

But a M.A. of up to 5 is a far cry from an arbitarily large (inverse)
M.A.  What can we do if we want to use this mechanism to make things
go fast instead of slow?  Like, what if we want to pull a string to
spin something at 15000 rpm by hand to generate electricity?  Maybe
something only 120mm in diameter, so it can be comfortably handheld?

First, consider the parameters of the problem: a person can pull about
200 N at about 3 m/s for about 1 m.  (Think of someone trying to start
a lawnmower or chainsaw with a pullcord.)  The edge of the disc, which
will be generating the alternating magnetic field that generates
electricity, will be moving at about 94 m/s.  So we need a M.A. of
more than 62, probably at least 200 to be safe.  We’re missing a
factor of 40.

With modern UHMWPE fiber and its 3-GPa tensile strength, 200 N
requires a 290-μm-diameter cord; better say 500 μm to be safe, which
should be good to 580 N.  This means that a single layer of wrapping
on a 20-mm-long barrel holds 40 revolutions, and each layer adds
500 μm to the radius.  An 8-mm-diameter barrel with its 25-mm
circumference would hold about 1 m of cord per wrapping layer.

We can make some progress on the problem by using better bearing
materials.  Steel on polyethylene has μ ≈ 0.2, on graphite, μ ≈ 0.1;
on teflon, 0.05–0.2; and on tungsten carbide, 0.4–0.6.  Tungsten
carbide on tungsten carbide is listed as 0.2–0.25.  Materials with
lower μ might be worse if they require a larger journal radius to
compensate for lower compressive strength; WC’s 3+ GPa compressive
strength would theoretically allow it to bear 200 N on a 250-μm-long
250-μm-diameter shaft, if it doesn’t bend too much, for example.  

XXX I’ve confused circumferences and radii so there’s a missing factor
of τ from some of the below

Or a 500-μm-long 125-μm-diameter WC shaft, maybe somewhat tapered to
reduce the risk of breakage.  That would give you a 62-μm bearing
radius, so each 100 N of side load produces, say, 25 N of friction,
but only 1.55 millinewtonmeter of friction torque.  So if your
difference in radii is, say, 30 μm, say because one drum is 8.00 mm in
diameter and the other is 8.06, the 100 N will produce 3
millinewtonmeters of torque, which is twice as much as the friction,
so it will be able to backdrive the mechanism.  The M.A. to the magnet
disc, then, will be 60 mm / 30 μm, or 2000.  Our 3 m/s human pullcord
would be able to spin the rim of the magnet disc at 6000 m/s, or Mach
18, spinning at 955000 rpm.  Also, the ⅓ of the 200 J lost to
friction, or 60 J, would be deposited in the tungsten carbide
bearings, which are some 0.1 mm³ or about 1.6 mg of WC; with its
room-temperature specific heat of 200–480 J/kg/K its temperature would
rise to between 78000° and 188000°.

Although the bearings could withstand the mechanical pressure at room
temperature, they would vaporize and the disc would explode.  Also,
any practical mass of disk would make the pullcord too hard to pull.
And extending the pulley pull handle by 1 m at 30 μm of difference per
revolution and 25 mm of cord per revolution would require 33000
revolutions, unwinding some 800 m of cord from one drum and winding it
up on the other.  Clearly this is taking things too far!

Let’s try backing off to our planned M.A. of 200: a difference of
radii of 300 μm.  And let’s consider ordinary cast iron on bronze: μ =
0.22.  Cast iron can withstand 500+ MPa of compression, but UNS C93200
(SAE 660) bearing bronze only some 300 MPa, with a fatigue strength of
only 110 MPa.  Also, consider that there are two bearings, one at each
end, so each can bear half the 200 N load.  100 N ÷ 110 MPa gives
950 μm diameter × 950 μm length, say, or 450 μm diameter × 2 mm
length, giving 225 μm radius (probably, again, an average over a
slight taper).  200 N · 0.22 · 225 μm = 9.9 millinewtonmeters of
friction, and 200 N · 300 μm = 60 millinewtonmeters of applied
differential torque.  The leftover 50 mN m manifests as an 0.8 N
resistance at the 60-mm-radius generator ring, which should be quite
straightforward to produce by, for example, generating electricity
through pancake coils.

This is an improvement, but we still face the dismaying prospect of
3000 revolutions of the main spindle unrolling 75 m of UHMWPE thread
from one drum and rolling it onto the other.  That’s a lot of
revolutions!  And the 17% power loss in the main journal bearings is
worrisome not only because it’s wasteful but also because of the heat
problem.

By adding an additional idler pulley behind one of the differential
drums, so that the side loadings from the two strings are in opposite
directions, you can reduce the side loadings on the drums’ bearings.
The idler adds some friction, requiring a journal similar in stoutness
to that of the main wheel, but it can be quite narrow (<1 mm) and
large in diameter (40 mm, say).  So the string running around the
idler has a lever arm of 20 mm with which to counteract the 0.225-mm
lever arm of the journal’s friction, an M.A. of 89, which when divided
by μ = 0.22 gives us a factor of some 400.  So the idler will consume
about ¼% of the energy; and it ought to be able to reduce the friction
in the bearings of the main differential wheel considerably, perhaps
by a factor of 2, which matters a great deal more, because their
friction has a great deal more M.A.

Instead of just having one idler pulley, one differential pulley on
the pull handle, and one spindle, we can improve the situation
further: by adding three more idlers in the body and three more in the
pull handle, with an additional 1.5% efficiency loss, we can run the
cable back and forth between the main body and the pull handle eight
times instead of twice.  This enables us to use a much smaller M.A. in
the differential windlass mechanism itself — 50 instead of 200,
realized by paying out 1.2 mm of differential cable per revolution of
the drums rather than 0.3 mm.  By pulling the two parts of the
mechanism apart by 1 m, 8 m of cable is demanded of the differential
windlass itself, which is still (!?) 6700 revolutions.  But now each
cable only bears 25 N (XXX, I was overspeccing it above by a factor of
2) and so can be hair-thin: 150 μm diameter at 3 GPa should withstand
50 N.  And the side-loading imposed by these threads on the spindle,
and the frictional losses in the journals, are correspondingly lower.

It’s important to design the handle so the pulleys can pivot to
equalize tension among these threads; otherwise you will accidentally
put all the tension on one thread while yanking the handle and break
it.

Suppose our windlass barrels are 30 mm long and 7 mm in diameter.
Each layer of this thread on the barrel is 200 revolutions, 22 mm in
circumference, and thus holds 4.4 meters of thread.  If this
circumference remained unchanged, there would be 33 layers, totaling
4.95 mm in thickness, on a fully charged barrel.  This is clearly a
practical volume of thread.

I’m still concerned, though, about the thread thickness changing the
barrel radius and thus the M.A.  1.2 mm of circumference difference is
only 190 μm of radius difference: barely more than a single layer of
thread.

It’s worth mentioning that in such a mechanism the electronics could
be entirely sealed away from the rotor and pulleys, communicating
exclusively through magnetic fields.
