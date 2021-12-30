STMs and AFM can achieve deep subatomic resolution (10 pm is common),
but STMs are limited to conductive materials, and in air they are
limited to those that don’t form a nonconductive oxide: mostly gold
and graphite.  Anything else requires not just vacuum but
pain-in-the-ass UHV, worse even than an STM.  And, as I understand it,
their failure mode is to crash the probe if there’s insulating crud on
the surface, potentially destroying it.

Optical microscopes are normally limited to about 200’000 pm (a
nominal wavelength of 600 nm divided by twice an oil-immersion NA of
1.5), four orders of magnitude worse.  If you can see something at all
in a visible-light optical microscope, it’s probably at least 400
atoms across, which means it contains 64’000’000 atoms: seven orders
of magnitude coarser than the atoms you can see with an STM.
Ultraviolet microscopy can get partway into that region, but at a
wavelength below 124’000 pm you run into the wall of vacuum
ultraviolet, to which all gases and all liquids are opaque, so you’re
stuck around 40’000 pm, about 80 atoms across, 512’000 atoms or so per
particle.

Can’t we do anything to get into this region?  Well, scanning
near-field optical microscopy can help us with going under this limit;
it can reach 20 nm (20’000 pm) with evanescent-wave illumination
bringing it to life, but that’s still more than three orders of
magnitude away from STM/AFM resolution, 64’000 atoms or so.  And it’s
limited to fluorescent samples, for which there are a number of other
techniques available.

Here’s a possible alternative for conductive samples, which includes
anything we can sputter metals onto.  If we have a *convex* conductive
sample, we can immerse it in a fluid of high permittivity, such as
water, glycerol, or propylene glycol, and set up an alternating
low-voltage electrical field between the sample and some “reference
electrode” in contact with the same liquid some distance away.  The
contour surfaces of constant voltage that form in the fluid can then
be measured with a needle probe that is heavily isolated with a
low-permittivity dielectric such as teflon, polyethylene, or beeswax,
except at the tip.  Assuming the resistivity of the sample is much
lower than that of the fluid, one of these contour surfaces will be
the surface of the sample itself, and others will be nearby; this
should permit scanning the probe over the surface while maintaining a
fixed distance, without crashing it, and without especial concern
around the formation of insulating oxide films on the surface, etc.

The reason for the relative permittivities of the fluid and the probe
insulation is that the potential gradient through the fluid (the
electric field) should be fairly weak, while the potential gradient
through the insulating sheath should be very strong indeed, so that
the voltage we measure on the other end of the probe, somewhere
outside the liquid, which is the same as the voltage at the probe tip,
is the same as the voltage that would be present if the probe were
absent.  This requires minimizing the capacitive coupling between the
shaft of the probe and the liquid it passes through.

An electrolyte liquid, such as saline water, can be used instead of a
pure dielectric, if its conductivity isn’t too high and the voltage is
low enough to avoid destructively large amounts of electrolysis or
other reactions at the surface.

If we stick the probe inside a cavity in the sample surface, though,
the potential gradient should entirely disappear.  To correct this
problem, we can use a second scanning probe as the reference
electrode, so that we can insert it into the cavity at the same time.
By shortening the distance, this method also greatly increases the
potential gradient (which is to say, the electric field strength) we
can apply, so that our microscopy resolution is limited not by the
electrode potentials of potential electrolysis reagents but by the
avalanche breakdown of the high-permittivity fluid.

Water’s dielectric strength is sometimes cited as being around 70
MV/m, but such numbers strongly depend on the timescale; it can be
enormously higher over short (subsecond) timescales, or much lower
over long (multi-hour) timescales.  Also, I think the Paschen minimum
happens with avalanche breakdown in things that aren’t gases as well,
so the effective dielectric strength at submicron distances might be
smaller.  70 MV/m is 70 mV/nm, and 70 mV is not a terribly challenging
voltage to amplify (my stereo is faithfully amplifying submillivolt
signals as I write this), so subnanometer resolution is probably
attainable with this method.

At high frequencies high permittivity shades into conductivity;
capacitors pass high frequencies, and if the dielectric is lossy
enough, the current comes into phase with the voltage.  The
conventional value for the resistivity of deionized water is 18.2
megohm cm, which would give you about 200 teraohms (2e14) over a 1-nm
channel with a square nanometer of cross-sectional area.  Using a
relative permittivity of 80, we get a capacitance of 7e-19 F for the
same dimensions (C = εA/d = 80 × 1 nm² × 8.85e-12 F/m / 1 nm) and a
reactance (X = 1/2πfC) which becomes smaller than the resistance at
about 1 kHz and gets down to 200 megohms a bit above 1 GHz.

So on one hand the intuition that the water will polarize in such a
way that it acts mostly capacitively is correct, but on the other hand
detecting the current through such a tiny capacitance would be very
challenging, if possible at all.  Even at 1μm² of tip area positioned
1μm away from the workpiece we only get 0.0007 pF.

However, I’m confident that if we load up the solution with enough
ions, we’ll be able to detect the voltage from the ionic current.
Maybe a porous tip, or a dendritic tip, or one with lots of
micro-slots cut into it, would enable a larger contact area with the
ion-rich liquid.  And you might have to use a lowish frequency to give
the ions time to move around.  The final distribution of ions will
probably give a very nonlinear voltage distribution, but that should
be okay if we’re running the tip along a voltage contour.
