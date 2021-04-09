Watching the “Clickspring” series of videos on hobby clockwork, I came
across the section about the “stopwork”, which stops the mainspring
from being wound by more than, say, five turns.

The way this is done is very simple.  A pair of defective gearwheels
mesh; one is held in place only by light friction applied by a spring,
and has five teeth, with the rest of the gear solid out to the tip of
the teeth (the addendum circle), so if it were to be meshed with
another, non-defective wheel, it would only be able to rotate a
fraction of a rotation before locking, as the teeth of the other wheel
crash into the edge of the solid disc where no teeth have been cut.

However, it is instead meshed with a gearwheel that has been filed
down to just the base circle, except for a single tooth that remains
protruding.  So, for most of each rotation, this single-toothed wheel
doesn’t contact the counter wheel at all, but when it does, it
advances the counter wheel by a single tooth — unless the counter
wheel has already rotated all five teeth, in which case the single
tooth crashes into the solid disc much as the teeth of an ordinary
gearwheel would have done.

Thus an up/down counter is provided, one which blocks further motion
upon reaching the end of its count.  Its memory is retained in an
entirely analog fashion by friction, although the count being
remembered is essentially digital.

It occurred to me that a different approach to solving this problem is
to use a “Geneva drive” mechanism (aka “Maltese cross”, “Geneva stop”,
or sometimes “Geneva wheel”) which is similarly defective, with one of
the slots for the drive pin being blocked, so the drive wheel can only
spin three, or four, or six rotations, or whatever.

[This is apparently the original use of the Geneva drive!][0]

[0]: http://emweb.unl.edu/Mechanics-Pages/em373honors-S2001/em373/geneva/geneva.htm

The Geneva drive does not depend on friction and thus is invulnerable
to vibrations, and moreover is susceptible to being *chained* in a way
that ordinary gear wheels are not, which requires further explanation.

The defective gear wheels in the stopwork mechanism demonstrated by
Clickspring have the property that the “mechanical advantage” is
fairly accurately 1 during the moment when they are engaged, since
they happen to have the same pitch diameter, 0 when they are not
engaged, and then ∞ when they are locked.  This contrasts with the
simplest straightforward stopwork mechanism in which a drive pinion
spins a larger wheel which encounters a stop at some point in its
rotation; if the drive pinion is to be allowed to turn 8 times, for
example, we might drive a 73-tooth wheel with an 8-tooth pinion,
occupying 9/73 of its rotation with a stop.  But this stop needs to
resist 8 times the torque applied to the drive pinion.  The
defective-wheel mechanism does not have this problem.

But the Geneva drive permits carrying this further: not only can we
arrange for its mechanical advantage to average 1 during the driving
part of the cycle, but we can use one such wheel to drive another,
which drives another.  (Hmm, maybe that’s not such a big difference
after all; the one-tooth driver can do the same if it’s driving an
ordinary gearwheel, after all.)

A single Geneva wheel can be made with arbitrarily many slots, at the
cost of pushing the duty cycle up toward 50% with a single drive pin.
In the limit of 50% you have an intermittent-motion version of a rack
and pinion, with the possibility of endstops.

In the Geneva wheel’s original use as a stopwork, it was in fact a
limit on *differential* rotation: it limited not the absolute rotation
of the inner shaft of the mainspring or its outer barrel but their
*relative* rotation.

By rotating one or more disc sectors in a plane parallel to the
Maltese cross, it is possible to obstruct the entry of the drive pin
into the slot.  But perhaps a more interesting possibility for logic
is axial displacement; in the usual construction, the drive wheel has
a ward in the form of a partial circle that nestles into the Maltese
cross to keep it from turning when the drive pin is not engaged, with
a cutout in the circular ward around the drive pin to allow the
Maltese cross to rotate when the drive pin *is* engaged.  But the
circular ward could be made from part of a solid round shaft, along
which the Maltese cross can be slid; if the cutout does not extend
along its entire length, then sliding the cross up it by the thickness
of the cutout and enough to clear the pin, the cross can be exempted
from being incremented or decremented by the next passage of the pin.

This potentially gives us a clocked-logic system similar to Drexler’s
rod logic or Merkle’s buckling-spring logic, though probably less
suitable for miniaturization than the latter, since it relies heavily
on not only contact but sliding contact.
