Suppose you want to reflect light of a given wavelength (say, 555 nm)
coming from a given direction into given directions from all points of
a surface.  It is sufficient to be able to determine the phase delay
at all points of the surface; the gradient of that phase delay with
respect to the u-v coordinates on the surface then determines the
output beam direction.

If you can only control the phase delay up to some limit, then
occasionally you will have a discontinuity, like in a Fresnel lens.
This is minimally disruptive if the discontinuity jumps an integer
number of wavelengths, such as 1.  So it’s sufficient to be able to
control the phase delay over a single cycle, for example by etching
the surface selectively to depths of up to half a wavelength, since a
half-wavelength-deep pit will induce a whole wavelength of phase delay
for normal light.  Less depth is needed if the light is at an oblique
angle.

277 nm is a pretty shallow etching depth, and the average depth is
only half of that, 139 nm.  If you want to achieve it purely via
electropolishing, you’re removing 139 picoliters per square
millimeter.  But if you can use a combination of electrodeposition and
electropolishing, the average amount of material moved is only half of
*that*, 69 nm or 69 pl/mm².  If the material is copper, which weighs
8.89 g/cc, that’s 610 nanograms per square millimeter.  Copper is
63.546 g/mol, so that’s 9.7 nanomol per square millimeter, which works
out to 5.8 × 10<sup>15</sup> atoms per square millimeter added and removed.

Electropolishing copper involves removing two electrons per atom, and
electrodepositing it involves adding them, and the electron charge is
about 1.6 × 10<sup>-19</sup> coulombs, so that’s about 1.9
millicoulombs per square millimeter.

So, if your feedback and control systems were up to the task, with 100
mA you could electroform/electropolish 54 mm² per second; that’s
probably about half a watt.  For 22 A4 pages per minute, you’d need
about 43 amps, which is a lot better than a regular laser printer.

If you were anodizing aluminum in water instead of electropolishing
copper, you’d need to do the whole 139 nm depth since you can’t
electrodeposit aluminum in water, and you’d need to remove three
electrons per atom instead of two.  Aluminum is only 2.70 g/cc, while
its atomic weight is only 26.9815384(3), so a mole of aluminum is 10
cc to copper’s 7.14.  So you actually need roughly the same amount of
current per volume of aluminum as you do for copper.

Actually though the anodization layer you’re depositing has a high
refractive index; according to a couple of different papers, ranging
from 2.1 at 2 volts or 10 mA/cm² down to 1.6 at 10 volts or 100
mA/cm².  Either way the index gets even higher for blue light.  This
means your wavelength is 1.6 to 2.5 times shorter than the vacuum
wavelength, so you actually need about the same amount of current per
area despite the inability to electrodeposit aluminum.

(This variation in ior with applied current suggests that fabrication
of rugate filters in nanoporous aluminum oxide by applying a
time-varying current may be feasible.)

Actually, it’s even better than that; the above is calculated assuming
the etched space is filled with this ior-1.8-or-whatever coating, but
in fact typically the anodized coating on aluminum is twice as thick
as the aluminum thus consumed.  So each 10 nm of aluminum you anodize
into oxide produces 20 nm of oxide, which the light will strike 10 nm
earlier than for the untouched surface and leave 10 nm later.  So the
total phase delay is, say, 1.8 × (20 nm + 20 nm) - 20 nm, which ends
up being 52 nm of phase delay.

At 30 mA/cm² our 2 mC/mm² or so would take a few seconds.  Like, 7
seconds.  So this seems like an eminently feasible process to carry
out at a physical level; the only question is how to do the process
control, using viscosity, positional control, current pulses, and
perhaps optical feedback.

Even a 10-micron-thick layer of aluminum foil would be more than
sufficient to electro-etch 80 nm deep into.  You could imagine doing
10 or 100 wavelengths or more of phase delay instead of just one, thus
allowing your mirror to function across a wide range of wavelengths
and reducing the number of discontinuities and their associated
stray-light losses.  (Ordinary non-selective hard anodization coatings
on aluminum do already indeed reach 50 microns routinely and 100
microns occasionally.)  This will enable rapid computational
production of white-light holograms, diffraction gratings, imaging
mirrors, and solar concentrators.

Despite the inevitable micro-cracks, the shapes of anodizing coating
thus thrust up from the aluminum surface may also be usable for
non-optical, mechanical purposes such as stamping, or as mechanically
mating surfaces that slide past one another.

Anodizing titanium rather than aluminum offers the possibility of
stronger refraction and and thus thinner films and faster production,
as well as of course the direct use of the stronger iridescence that
comes from rutile’s higher ior.

I think electropolishing of aluminum in chloride electrolytes such as
sodium chloride produces water-soluble aluminum chloride rather than
insoluble aluminum hydroxide, although some production of the gel is
also reported; [one experimenter reports 3.6 mm per minute
drilling][0] (60 microns/second) with 5-14% sodium chloride and a
0.1-0.4 mm interelectrode gap.  By comparison, EMAG’s “PECM”
die-sinking ECM machines’ oscillating process gap typically goes down
below 50 microns; they imply it oscillates at 50 Hz and goes higher
than 750 microns to improve sludge clearance, flushing at 10-50 m/s.

[0]: https://youtu.be/x4m1RWWJElM
