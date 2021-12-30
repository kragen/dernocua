As explained in file `material-observations.md`, Elmer’s Glitter Glue
changes in an interesting way when it dries: as deposited, the glitter
flakes are dispersed almost isotropically, without any preferred
orientation, but drying makes the glitter flakes mostly parallel to
the surface.

Basic high-laminar-filler composites
------------------------------------

This suggests that by this means we can fabricate composite materials
with high loadings of fibrous or especially laminar reinforcing filler
(e.g., talc, clays, carbon fibers, carborundum whiskers, graphene,
MXenes; see file `electrolytic-2d-cutting.md` for some fuller lists)
without having to assemble them layer by layer.  Specifically, you
bulk up the polymer with a lot of solvent, mix in your functional
filler, deposit it in an X–Y sheet of uniform thickness on some
substrate, evaporate off the solvent resulting in a great loss of
volume, and then break the sheet free from the substrate.

Adherence to the substrate prevents the sheet from shrinking in the
X–Y plane as it dries, forcing all of the volume loss to be in the Z
direction; this reorients the filler particles nearly parallel to the
X–Y plane, allowing them to pack much more tightly than laminar
reinforcing particles normally could, potentially resulting in a final
product that consists almost entirely of the filler, bound together
with a small amount of matrix.  If the solution is sufficiently
viscous or dense, or if surface charges maintain the filler particles
deflocculated, the filler will not settle out or float out before
being held in place during the drying process.  Thus the filler will
be evenly dispersed through the resulting matrix.

Laminar reinforcing fillers are extremely desirable as reinforcement
because, while each particle of a fibrous filler adds strength in one
dimension, laminar fillers can add the same strength in two
dimensions.  So, in theory, where most of the composite’s strength
comes from the filler and not the matrix, laminar reinforcement should
be able to make materials that are twice as strong.  Normally, though,
they can only be added as very low percentages, because they either
run into one another at weird angles so that more filler can’t enter,
or they clump up in stacks, so their large surface area doesn’t touch
the surrounding matrix, so their strength doesn’t get transferred.

Sheets, whiskers, and other fibers below a critical dimension are
“flaw-insensitive”: they’re small enough that most of their length or
width lacks crystalline defects, so there is no flaw at which to
concentrate stress.  This commonly increases their strength by an
order of magnitude or more.  This effect does not come into play with
craft glitter.

Waterglass-matrix composites
----------------------------

Waterglass is another interesting possible candidate here, since it
forms a soluble mostly-silica xerogel when it dries, although it may
be brittle enough at room temperature that it won’t achieve super
strength.  Mixing waterglass with clay to repair things has a long
tradition in pottery, and [it deflocculates the clay due to its
alkali-metal ions][1].

[1]: https://digitalfire.com/material/sodium+silicate

(It is possible to further harden waterglass after it dries by
exchanging its alkali ions with polyvalent cations, as is done in KEIM
paint.)

Non-evaporated composites
-------------------------

Alternatively, rather than evaporating the solvent, you could try
removing it by some other means.  For example, you could press the
mass against a semiporous membrane so as to reverse-osmotically force
the solvent through the membrane, but not the dissolved matrix or the
filler, similar to using frit compression to produce buckypaper (which
typically has no binding matrix) or slipcasting pottery.  I’m pretty
sure this will work in a closely analogous way; the situation is very
closely analogous to the solvent case.

Maybe it would even work to squeeze a molten matrix material through a
porous material (such as a sintered frit, unglazed fired clay, or
dirt) in this way, leaving only the oriented filler and a small
remnant of binder, which would remain when the material was cooled; in
some cases, as with slipcasting, the capillary action in the porous
material would itself be enough to suck away the excess binder.

The things I’m not sure about is ① whether the currents of molten
binder will tumble the filler particles as they pass (I think not; I
think they’ll just press the filler particles up against the porous
wall, and at any rate you can do the squeezing more slowly to get
slower currents) and ② whether you can separate the composite from the
frit afterwards (but in the worst case you can cut it off parallel to
the frit surface while it’s still almost molten).

Metal evaporation
-----------------

As I understand it, the drying process normally works by first gelling
the viscous solution into a hydrogel, then contracting it into a
xerogel under the influence of surface tension in the nanopores of the
gel.  Thus, carrying out the above process with metals using mercury
as a solvent may or may not work, because solid amalgams are not gels,
and the shrinking process may be different from xerogel collapse.  It
may work anyway, though; mercury can dissolve all of zinc, copper,
tin, lead, silver, and gold to an appreciable extent, and at least in
the case of gold it is commonplace to recover fully dense solid gold
by heating, which is how mercury gilding works.

The IUPAC solubility series volume 25 (_Metals in Mercury_) has the
following solubilities for some selected metals in mercury at a couple
of temperatures:

<table>
<tr><th>Metal         <th>Room temperature      <th>300°
<tr><th>Magnesium     <td>2.52%                 <td>26%
<tr><th>Aluminum      <td>0.014%                <td>5.6%
<tr><th>Tin           <td>1.05%                 <td>&gt;84% (tin melts at 231°; miscible?)
<tr><th>Lead          <td>1.47%                 <td>93% (lead melts at 327°)
<tr><th>Titanium      <td>0.000017%             <td>0.0035%
<tr><th>Chromium      <td>????                  <td>too low to measure
<tr><th>Iron          <td>????                  <td>&lt;0.00004%
<tr><th>Cobalt        <td>????                  <td>&lt;0.00007%
<tr><th>Nickel        <td>????                  <td>0.007%
<tr><th>Copper        <td>0.0092%               <td>0.6%
<tr><th>Silver        <td>0.065%                <td>5.1%
<tr><th>Gold          <td>0.13%                 <td>14%
<tr><th>Zinc          <td>6.32%                 <td>70%
</table>

Magnesium is the most tempting entry here, but I’m guessing that if
you were going to dissolve magnesium in mercury and then evaporate off
the mercury, you’d have to do it in a way well protected from oxygen.
Aluminum amalgams aggressively extrude fibers of aluminum oxide over
the course of hours when in contact with air.

Aluminum, zinc, and tin are also soluble to a useful extent; you could
dissolve a significant amount of zamak 3 (96% zinc, 4% aluminum) in
hot mercury.

Rather than using unfashionable and costly mercury, it might be better
to try to dissolve other metals in affordable and nontoxic magnesium
or zinc, and then use an elevated temperature to vaporize the
magnesium (boiling point: 1091°) or zinc (boiling point: 907°) from
the alloy.

Water’s vapor pressure at 25° is about 3.2 kPa, 24 mmHg, at which rate
it evaporates fast enough to be useful.  Zinc melts at 419.5°, and its
vapor pressure is well approximated by log₁₀*P*ₘₘ = -7198/*T*+9.664
(McKinley & Vance 01954), where *T* is in K, so it reaches that
pressure at 869 K = 596°.  As metal-fabrication processes go, that’s a
pretty moderate temperature, which is why zinc fumes pose such a risk
of metal fume fever.  You might want to evaporate off the zinc in
vacuum or under argon or nitrogen.  ([At 600° you have to use ammonia
to get zinc nitride, so just nitrogen is adequately inert for
this.][4])

[4]: https://en.wikipedia.org/wiki/Zinc_nitride

Unfortunately, there’s no IUPAC solubility series volume on the
solubility of various metals in molten zinc, but [there are lots of
phase diagrams for zinc alloys][2].  In particular, molten zinc can
dissolve about 10% Cu at 596°, and [eutectics and near-eutectics used
in soldering include][3] Sn₉₁Zn₉ (KappAloy9) 199°, Zn₉₅Al₅ 382°, and
Cd₈₂.₅Zn₁₇.₅ 265°, so molten zinc is evidently capable of dissolving
substantial amounts of aluminum even at much lower temperatures.
[Below 596° no other structurally useful metals melt][5], but metals
that melt at lower temperatures than copper include gold, silver, and
of course lead, tin, and magnesium.  So we might reasonably guess
that, like copper, substantial amounts of those metals can dissolve in
molten zinc at 596°; [a paper suggests it can handle 20 mol% of
silver][7].  And in particular you ought to be able to dissolve
*bronze* in zinc at that temperature, then evaporate off the zinc, or
most of it.

[2]: https://www.tf.uni-kiel.de/matwis/amat/iss/kap_6/illustr/i6_2_1.html
[3]: https://en.wikipedia.org/wiki/Solder_alloys
[5]: https://chemistry.fandom.com/wiki/List_of_elements_by_melting_point
[7]: https://www.researchgate.net/figure/Aluminium-zinc-and-silver-zinc-binary-phase-diagrams-20_fig2_275032898

More excitingly, [a calculated phase diagram suggests][6] that zinc
should be able to dissolve about 3 mol% nickel at 600° and about 25
mol% at 873°, and [another suggests 2 mol% iron at 600°][7].

[6]: https://www.researchgate.net/figure/Calculated-Ni-Zn-binary-phase-diagram-using-thermodynamic-parameters-from-Vassilev-et-al_fig2_248129880
[7]: https://www.researchgate.net/figure/Fe-Zn-phase-diagram-for-stable-equilibrium-18-some-parameters-used-in-the-current_fig4_284812804

Nanolaminating to get flaw-insensitive laminar fillers
------------------------------------------------------

Typically the critical dimension for flaw-insensitivity is a few tens
of nanometers, which is an entirely practical thickness at which to
electroplate.  It occurs to me that if you want a lot of
high-aspect-ratio sheets, you could make them out of a metal in the
following way.  You start by plating a nanolaminate consisting of
alternating layers of your desired metal and some other metal or
material that is easily etched later, using an etchant that will spare
your desired metal; you might deposit, for example, 20 nm of each
metal.  Then you pulverize the nanolaminate (perhaps easiest if you
initially plated it onto a metal where it had terrible adhesion, or
onto a layer of graphite), for example by ball milling, into particles
of, say, 1 μm.  Then you etch these particles with the etchant and
separate the resulting metal sheets, which are 1 μm × 1 μm × 20 nm in
the example I’ve given.

If the adhesion between the layers of the nanolaminate were
sufficiently poor, maybe you wouldn’t even need the etching step.

These high-aspect-ratio flaw-insensitive metal particles are suitable
for use as a functional filler to make an ultrastrong composite
material, whether the binder is an organic polymer, a geopolymer,
waterglass, another metal, or something else.

Some pairs of metals cannot be plated from the same bath; in that case
you have to move the forming nanolaminate back and forth between two
baths, rinsing it in between.  In other cases, you can make a bath
which will plate only one metal at one voltage and a mixture of two
metals at a different voltage.  In other cases (chromium and titanium
being notable here) you can grow an anodic oxide layer by reversing
the voltage; this may be sufficiently thick to etch later but
sufficiently thin to permit plating metal on top of it.

An alternative to moving back and forth between baths is to consume
all the platable metal in one bath, leaving only, say, alkali metals;
then you can inject the new metal directly into the bath.  Indeed, you
may be able to “inject” the new metal simply by turning off the inert
cathode and switching to a cathode that will dissolve, or increasing
the voltage on the cathode.  By using a thin electrolyte (say, 1 mm)
and cathodes even more closely intercalated (say, 0.1 mm, perhaps
foils of two metals stacked alternatingly with dielectric sheets
between them, like a multilayer capacitor) you may be able to switch
back and forth more rapidly between metals than with a rinse tank.

Another possible alternative separator is to deposit not an anodic
oxide film but the insoluble hydroxide of a metal in solution, such as
magnesium, which will deposit on the cathode, just as metals do (see
file `freezer-seacrete.md`).  Magnesium hydroxide in particular is
easy to remove with many acids.
