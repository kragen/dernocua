On Earth we make our photovoltaic panels out of semiconductors,
separating the positive and negative charge collection nets with the
depletion region of a reverse-biased pn semiconductor junction, but in
space we could use photoemission across a vacuum gap; this will
probably give less power per unit area but more power per unit mass
than silicon solar cells, but will be thoroughly dominated by
thin-film cells.

I got this idea from a discussion with Luke Parrish, who suggested
that for space-based PV panels you could just use vacuum, and
contributed several other key ideas to what follows.

Basic design
------------

We were discussing [aerographite][0], which has recently been mooted
as a possible solar sail material with 1 kPa UTS and 180 g/m³.  As it
happens, aerographite is fairly conductive (0.2 S/m at that density).

[0]: https://en.wikipedia.org/wiki/Aerographite

You could make a large [photoemissive][8] solar panel, like old
vacuum-tube electric eyes but [backward-biased][2].  [WP claims][1]
that cesium on a silver oxide support gives photoemissivity down into
the infrared, so you could plate such a mixture on the sunward side of
the aerographite support to make a photoemissive cathode, potentially
a gigantic one; [photon energy][3] beyond what is needed to overcome
the work function becomes electron kinetic energy, which can push the
electron uphill against a potential difference to an electron
collector grid anode, which needs to be porous, to let light through,
and spaced far enough away from the cathode with insulating supports
to prevent field emission from stealing the electrons back to the
cathode.  The spacing can be any distance that is small relative to
the mean free path in the vacuum medium.

[1]: https://en.wikipedia.org/wiki/Phototube
[2]: https://en.wikipedia.org/wiki/Work_function#Work_function_of_cold_electron_collector
[3]: https://en.wikipedia.org/wiki/Photon_energy
[8]: https://en.wikipedia.org/wiki/Photoelectric_effect

### The anode grid ###

The spaces in the electron collector grid through which light comes
will also permit the loss of some photoelectrons, perhaps the
majority.  Assuming no charge transfer to the solar wind, the lost
electrons will eventually fall back to the positively-charged PV
panel, some striking the cathode and others the anode.  If it’s
desired to maximize efficiency per area rather than efficiency per
mass, you can extend the grid sunward into a honeycomb which lets
almost all of the light through, while capturing all of the electrons,
except for those emitted at a very small angle to the incoming light.
However, extending the grid “vertically” in this way runs into
diminishing returns very quickly; to maximize the electrons captured
per unit mass of panel, the thickness should be only a little thicker
than the width of the “wires” in the grid in the “horizontal”
direction.

This means that the mesh of the grid should be as fine as possible,
but its holes still need to be large relative to the wavelength of
light and relative to the thickness of its “wires”.  I suspect that
hole diameter on the order of 1–10 μm will be optimal, with “wires” on
the order of 0.1–1 μm “horizontally” and 0.1–3 μm “vertically”.  An
omnitriangulated mesh would be optimal for rigidity; a hexagonal mesh
would be optimal for compliance and wire-to-hole ratio; a square mesh
is in between these extremes.

This works out to be on the order of 1 g/m² for the mesh if it is made
of something like aluminum (2 · 0.3 μm · 1 μm · 3 μm / (3 μm)² · (3
g/cc) = 0.6 g/m²), corresponding to the areal density of a uniform
sheet of about 100 nm.  These dimensions are too small to make use of
the lower density of aerographite itself, because those result from
heterogeneity at larger scales than that.

### The cathode structure ###

If the cathode has 50 nm of low-work-function photoemissive material
plated onto the front of it, which I think is realistic, backed by the
low-density aerographite mentioned above with an areal density of
½ g/m², it would be about 2.8 mm in average thickness.  You would of
course want to give both this cathode and the anode thicker and
thinner parts, like the veins of a dicotyledon leaf or the threads of
ripstop nylon, to reduce their electrical resistance and mechanical
compliance.

It may be important to keep the electrodes cool to avoid loss of the
electrodes from the anode mesh.  Using a high-work-function surface
for the anode and the non-sunward side of the cathode may be helpful
to reduce such losses.  Also, if you’re using volatile metals like
cesium, you need to keep the electrode cool or it will evaporate off
into space.

Areal density: 2 g/m²
---------------------

This adds up to an areal density for our orbiting solar panels on the
order of 2 g/m² or 2 tonnes per km², roughly a hundred times lighter
than conventional silicon solar panels at 100 μm thickness; typically
in space multijunction cells [with efficiency around 30%][4] are used.

Calculating efficiency
----------------------

A km² of sunlight is about 4200 megawatts at Earth’s orbital distance, or
much more if you’re closer to the sun, but how much of that can we
really gather?

[4]: https://commons.wikimedia.org/wiki/File:CellPVeff%28rev210104%29.png

This depends on the [quantum efficiency][7] of photoemission from the
cathode (what fraction of photons eject an electron) and the reverse
bias voltage we demand the electrons fight against.  Photons whose
energy is precisely the work function plus the bias voltage are
converted with 100% efficiency; photons at any lower energy are
entirely wasted; any excess photon energy over that minimum is wasted.
(We could imagine multiple cleverly shaped anodes whose electric
fields guide most electrons to the highest-energy anode they’d be able
to reach, but let’s assume we don’t do that.)

[7]: https://en.wikipedia.org/wiki/Photocathode#Quantum_Efficiency_%28QE%29

### Bias voltage limits spectral efficiency to 33% ###

So, too high a bias voltage will produce zero current, but lowering
the bias voltage will eventually produce insufficient additional
current to make up for the energy loss per electron; there’s some
voltage at which we see the maximum power.  (This closely corresponds
to spectrum losses in conventional PV panels.)  This MPPT bias voltage
will be a little lower than the energy of the average photon, which is
[probably about 700 nm][5]; *h c*/700 nm = 1.2398 eV/0.7 ≈ 1.8 eV, so
probably the right bias voltage is on the order of 1.8 V, which is a
conveniently tractable voltage; the [Shockley-Queisser limit][6] is an
efficiency of 33% at a semiconductor bandgap of 1.34 eV, which I think
corresponds to a bias voltage of 1.34 V in this photoemissive panel.

[5]: https://en.wikipedia.org/wiki/Sunlight#Spectral_composition_of_sunlight_at_Earth%27s_surface
[6]: https://en.wikipedia.org/wiki/Shockley%E2%80%93Queisser_limit

(Note: the above is incorrect, and energy efficiency calculations
hereafter erroneously assume that the bias voltage between the
electrodes is 1.8 V, which is wrong.  1.34 V or 1.8 V is the amount of
energy per electron lost in overcoming the work function of the
photocathode material; the energy remaining to be harvested at the
anode is whatever the photon energy is, *minus* that work function.
So the right bias voltage might be 0.5 V or 1 V or something.  I
should fix this but I don’t have time this year.  It means that the
main efficiency conclusions below are too high by some unknown factor
probably between 1 and 4.)

I think the recombination losses found in semiconductor PV cells do
not have much of an analogue in this device; the space charge is
entirely negative, and the only way electrons can “recombine” after
leaving the cathode is to fall back onto it, either because they
lacked the energy to reach the anode or because they went through
holes in the anode twice.  Presumably there is at least some
probability that they will be “emitted” into the cathode material,
though, where they will immediately “recombine”.

### Quantum efficiency can be around 15% ###

So, what about the quantum efficiency?  Evidently in silicon PV it’s
around 0.8, but these photoemissive panels might be much worse.  If
their quantum efficiency were, say, 10⁻⁶, they would produce less
electrical energy per mass than conventional silicon cells, rendering
them useless.  Wikipedia says that phototubes typically produce
microamperes, and they typically have a cathode area around 10 cm² and
are typically illuminated by an infrared beam that can’t be much more
than 10 W/m² (or we’d feel it on our skin and possibly damage our
eyes), which puts a lower bound on their QE of about 10 cm² · 10 W/m²
/ 1.7 eV / (μA/e) ≈ 1/6000.  At this QE we would expect 33% ·
1400 W/m² / 6000 ≈ 77 mW/m², which is high enough to be useful but not
high enough to compete with conventional solar cells; dividing by the
estimate above of 2 g/m², we get 39 mW/g, which is much lower than the
areal efficiency of conventional multijunction silicon solar cells,
30% · 1400 W / m² / (230 g/m²) ≈ 1800 mW/g, 46 times higher.

So this approach can be mass-competitive with multijunction silicon
solar cells if the photoemissive cathode quantum efficiency is more
than about 1/130, i.e., 0.8%.

In fact the [cesium-antimony photocathodes][9] used in the first
commercially successful photomultiplier tubes have a quantum
efficiency of 12% at 400 nm, though the quantum efficiency of earlier
silver-oxide-cesium photocathodes peaked at 0.4% at 800 nm.  This
information seems to come from p. 4 of the [Photomultiplier
Handbook][10]; on p. 11 it says, “on the best sensitized commercial
photosurfaces, the maximum yield reported is as high as one electron
for three light quanta,” which would work out to 33% QE.  This would
give an overall solar cell efficiency of 33% · 33% = 11%, but that’s
probably for a single wavelength; a few of the QEs of different
materials plotted on p. 15 are above 10% at 555 nm, and some, like
Na₂KSb, are above 20% at 450 nm, so maybe 33% · 15% ≈ 5% is more
realistic.  In Table I on p. 16, Na₂KSb’s responsivity to tungsten
light at 2856 K is given as 43 μA/lumen, while K₂CsSb (nominally 33%
QE) is given as 90 μA/lumen.  Nominally lower QE materials with
longer-wavelength peaks are even higher: GaAs:Cs-O is said to have
720 μA/lumen despite only a 12% QE due to an 800-nm response peak, and
semitransparent Na₂KSb:Cs on a reflecting substrate is 300 μA/lumen
with 16% QE with a 530-nm response peak, which matches sunlight better
than it does a tungsten lightbulb.  Presumably these are all in a
forward-biased condition, as they are used in PMTs, not back-biased,
but hopefully the correction is small.

Rechecking the calculation from a different angle, 1000 W/m² is about
128000 lux, so the above-the-atmosphere 1400 W/m² should be about
180 klux = 180 klm/m², which at 300 μA/lm would be 54 A/m²; at 1.8 V
that would be 97 W/m², which is 6.9% efficiency, close to the 6% I
estimated above.

So it seems likely that, using new ultralight electrode materials like
aerographite, coated with modern (semiconducting?) multialkali
photocathode materials, this photoemissive generator can probably beat
silicon PV in power per unit mass by a factor of, say, 20 or so
(50 W/g instead of 1.8 W/g), but it will be five times worse in power
per unit area (6% efficiency rather than 30%).

[9]: https://en.wikipedia.org/wiki/Photomultiplier_tube#Improved_photocathodes
[10]: https://psec.uchicago.edu/links/Photomultiplier_Handbook.pdf "Burle Industries, Ⓒ 1980, 10-89, supersedes PMT-62, 8-80, TP-136"

Thin-film semiconductor PV cells like CIGS can probably beat it in
power per unit mass, too.

Moreover, the Photomultiplier Handbook says, “Semiconductors,
therefore, are superior to metals in all three steps of the
photoemissive process: they absorb a much higher fraction of the
incident light, photoelectrons can escape from a greater distance from
the vacuum interface, and the threshold wavelengths can be made longer
than those of a metal.  Thus, it is not surprising that all
photoemitters of practical importance are semiconducting materials.”
So in a sense this gadget *is* a semiconductor thin film solar cell.

10.1088/1361-648X/aa79bd “Super low work function of
alkali-metal-adsorbed transition metal dichalcogenides” claims work
functions as low as 0.7 V with a potassium film on a strained tungsten
telluride backing.

Interestingly, the “semitransparent” photocathode materials are
“deposited on a transparent medium,” with typical film thicknesses
around 30 nm, so as to emit electrons in the opposite direction from
the incident light.  That suggests the possibility of reversing the
positions of the cathode and anode and making the anode opaque, so
there is no question of electrons escaping through holes in it.
Conceivably supporting the photocathode thin film in a vacuum on a
sparse grid like the anode grid described earlier, covering what would
be holes in the grid, would get photoelectrons coming out both sides,
so that by placing anodes on both sides you could increase the quantum
efficiency, perhaps doubling it.  That might boost you to 14%
efficiency or so, but still not enough to compete with existing CIGS
and similar solid-state thin-film PV cells.

Cathode meshes
--------------

Most of the mass of the cathode in the above setup comes from the
thin-film cathode (and then I just calculated on the assumption that
the anode mesh would have comparable mass).  An interesting way to
reduce the mass further is to use a photocathode *mesh* or foam rather
than a solid layer.  A mesh with holes significantly smaller than the
wavelength of light can be essentially opaque to the light if it’s
sufficiently conductive, so you could use a photocathode mesh with
100-nm-wide pores separated by 1-nm-wide “wires”, thus reducing the
necessary areal density of the cathode by 98%.

Existing systems
----------------

Parrish commented that existing systems are about an order of
magnitude heavier than the number I was using above as a
silicon-solar-cell comparison:

> [The ISS uses 8 solar array wings][11] massing about 1 ton each that
> get 84–120kW average or up to 240 in direct sunlight.  So about
> 30W/kg in direct sunlight.  We’re talking 3 orders of magnitude
> improvement.

[11]: https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station

Apparently [photoelectric solar power is a thing][12], and I should
read about how well it works, but I don’t have time this year.

[12]: https://www.sciencedirect.com/science/article/pii/S2542435117301782 "Photoelectric Solar Power Revisited"