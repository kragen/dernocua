I was thinking that seacrete (electrolytic mineral accretion) is a
really interesting possible digital fabrication process, but it’s
slow.  Seacrete deposition is claimed to be around 5 cm per year
normally, which is about 1.6 nm/s, so doubling the thickness of a
10-μm-thick aluminum-foil origami figure would take about an hour, and
getting to a thickness of 3 mm would take about 11 days.  So speeding
up the process would be very worthwhile.  Fortunately, there seem to
be several likely routes to increase the deposition rate by an order
of magnitude or more.

More concentrated electrolytes
------------------------------

First, maybe you could get better Faraday efficiency for depositing
seacrete by using a feedstock solution more concentrated than
seawater, and with less useless ions.  Seawater is only 0.13%
magnesium and 0.04% calcium, so the large majority of cations you’ll
attract to the cathode are sodium (it’s 1.1% sodium).  (Simply boiling
down seawater, or drying it out in ponds, to crystallize out most of
the sodium chloride leaving [bitterns][14],
would greatly improve the situation.)  Making
most of the cations something that can participate in the
mineralization reaction ought to boost the Faraday efficiency of the
process by a factor of 6 or so.

WP gives chalk’s solubility as .013 g/ℓ, or 1.3 mg/100mℓ, so maybe
that’s about how dilute a solution of bicarbonate and calcium ions
would need to be, though [it gives calcium bicarbonate’s solubility as
16.6 g/100 mℓ][4], so maybe you can go that high; WP says bicarbonate
ions are 0.14% of all dissolved ions in seawater, which is 3.5%
dissolved ions, so maybe that’s about 5 mg/100 mℓ already (depending
on whether those numbers are both by weight, or whether one of them is
molar).  Alternatively, magnesium hydroxide (brucite, Mohs 2.5–3),
might be a more practical primary electrolytic mineral accretion
material.  However, maybe enough dissolved choke-damp could enable
higher chalk deposition rates.

[4]: https://en.wikipedia.org/wiki/Calcium_bicarbonate

Supposedly [Epsom salt][0] dissolves 26.9 g/100 mℓ (anhydrous basis)
in water at 0°, and only 35.1 g/100 mℓ at 20°, so you could probably
dissolve at least 10 g/100 mℓ at -20°.  It’s 120.366 g/mol, while
magnesium is 24.305 g/mol, so it’s 20.193% magnesium by weight, so
this would be a solution of about 2% magnesium, 15 times as high as
seawater; so we might expect a deposition rate on the order of 15
times as high, even without the improved Faraday efficiency from
getting rid of the useless sodium.

[0]: https://en.wikipedia.org/wiki/Magnesium_sulfate

Upper bound estimations
-----------------------

100% Faraday efficiency with divalent cations would be 3.12 × 10¹⁸
ions per coulomb, which is 5.18 micromoles per coulomb, or 0.126 mg of
magnesium per coulomb.  At 58.3197 g/mol, that would be 0.302 mg of
brucite per coulomb.  So at 10 amperes you’d deposit 3 mg of brucite
per second, or 10.8 g per hour.  If this were distributed over
100 cm², with brucite’s density of 2.3446 g/cc, it would be
0.46 mm/hour, which is about 80× the reported rates for seacrete.
This is probably an achievable level of current with a tabletop (or
household freezer) setup, and depending on the voltage, it might be
10–50 watts, which is an acceptable power level; and you might be able
to reach 10–60% Faraday efficiency in real life.

These 10 A/dm² would be 93 “amps per square foot” in the medieval
units used by US electroplating shops, which is on the high end
of the current levels commonly used for electroplating, so it may be a
little high but it’s not outrageously so.  Nickel sulfamate baths for
nickel plating are operated as high as 15 A/dm² at the cathode.

At the other end of the spectrum, suppose we can accrete smithsonite,
ZnCO₃ (125.4 g/mol, 4.5 g/cc).  5.18 micromoles per coulomb here gives
us 0.650 mg of smithsonite per coulomb, or 6.5 mg/s at 10 A, or
23.4 g/hour, and over 100 cm² that’s... 0.52 mm/hour.  I was hoping
for a way more exciting number, but I guess the higher density of the
smithsonite mostly cancels out its higher molar mass.

In theory you can use higher current densities than that, but if you
keep increasing the current density eventually you will boil your
electrolyte; there’s also the risk of primary nucleation somewhere
other than your cathode, forming a particle which might be swept away
and consumed.  Somewhere in between, though, I suspect you might be
able to control the porosity with current density; higher or lower
porosities might be desirable in different situations.  In particular,
higher porosity will give you higher strength, hardness, and density,
while lower porosity will give you easier ionic conduction, faster
mineralization (at least volumetrically), higher filler fractions (if
you’re using fillers), and greater flexural rigidity per material
mass.

Temperature and pressure
------------------------

Doing the whole operation in the freezer would decrease the solubility
of the salts and products, but also of the product, which might be a
win on net.  It would also *increase* the solubility of choke-damp, as
would higher pressures.

I think lower temperature would also increase the resistance of the
electrolyte, which means lower thermodynamic efficiency.  In
combination with inert fillers, it might reduce ion mobility to an
undesirable degree.

So it might turn out that *high* temperatures rather than low
temperatures are most desirable.

Inert fillers
-------------

If you buried the cathode “form”, of origami aluminum foil or
whatever, in sand or silt, perhaps the brucite or calcite forming
around the form would concrete the sand together, forming a *real*
concrete rather than the ersatz limestone type; this could both
dramatically increase the strength of the resulting material multiply
the effective deposition rate by a factor of 2–5, since sharp sand and
surface soil typically has a void ratio around 0.4, and subsurface
soil is commonly around 0.2.  Void fractions as low as 0.1 (and thus
multipliers of 10×) might be practical with a combination of fillers,
though sufficiently low void fractions will impede ionic conduction.

This could boost maximum theoretical performance in the scenario
described above from 0.46 mm per hour of brucite deposited to as high
as 4.6 mm per hour of brucite-cemented sand.

Burying a pre-shaped cathode in sand may pose practical difficulties;
aluminum foil origami, bent thin wire, or a formed sheet of knitted
wire might bend under the weight of even a fairly small amount of sand
that settles on top of it.  Depending on the shape, you might be able
to manipulate the cathode into an existing sand bed so as to diminish
the problem; an origami crane, for example, can be inserted vertically
into the sand up to its wings, which can then be laid out horizontally
on top of the sand, while its head and tail might be able to stand up
to the falling sand.

The problem diminishes when the water becomes denser, adding buoyancy
to the sand, and when the sand is low-density, like quartz, rather
than high-density, like sapphire or forsterite.  Using aluminum-wire
screening rather than aluminum foil is one attack on the problem;
another is to initially pour deflocculated silt over the form, so that
it flows around the form on all sides while being barely denser than
water, then flocculate it by adding flocculants.

More generally, colloidal fillers, such as deflocculated clay,
deflocculated silt, or especially deflocculated micron-sized barytes,
might reduce the problem significantly; unlike sand and similar
particles, they can flow around the aluminum, and you can adjust them
to have density that is very close to that of aluminum to make it
closer to neutrally buoyant.

Additional fillers like ground mica, talc, mullite, glass fiber,
basalt fiber, chopped rock wool, carbon fiber, and cellulose fiber
should help to improve the mechanical properties of the result, as
well as decreasing porosity and thus increasing effective deposition
rate.  Low concentrations of metal fibers or graphite might be
sufficient to increase the strength of the result without being
present in high enough concentrations to form a conductive network;
they might also work to increase the effective surface area of the
cathode, thus enabling the use of higher currents and therefore higher
deposition rates.  If they formed a continuous conductive network, the
mineralization would occur at the surface of the sand bed rather than
surrounding the cathode within it.

Clays are commonly used as functional fillers in plastics, but I
suspect that they might be counterproductive in this application,
since even kaolin contracts significantly when dried.  Less
hygroscopic phyllosilicates like mica and talc can fill their role;
so, too, could platy nanocrystals of non-phyllosilicate minerals.

Normally in electrodeposition dendrites are to be avoided, since they
screw up the geometry.  But in this case it might be worthwhile to
start with an initial stage of dendrite-forming electrodeposition to
increase the surface area of the cathode, safely ensconced within its
powder bed, before switching electrolytes for mineralization.

Powder-bed 3-D printing of cathodes
-----------------------------------

By powder-bed 3-D printing the sand bed with conductive fillers in it
(for example, carbon black, powdered aluminum, powdered silver,
powdered gold, or powdered copper) you could produce an anode with an
elaborate form; it will not mineralize consistently, since parts of
the cathode that are shielded from the ionic current will not
electrodeposit, but this is likely acceptable for many uses.

An alternative to printing conductive fillers is printing materials
that break down to conductive coatings; for example, silver oxalate
readily decomposes to silver and gases on gentle heating.  [Copper
formate][9] similarly decomposes to copper and gases, and has the
additional advantage of being water-soluble and thus suitable for
inkjet printing; selectively coating sand grains with conductive
copper might also allow the use of smaller amounts of copper.

[9]: https://www.youtube.com/watch?v=auyCK8-DMP0

More anions, more and better cations
------------------------------------

Other useful abundant mineral-forming cations might include ferrous,
cupric, aluminum, ferric, nickel, cobalt, and zinc; less abundant but
still useful might be manganese, trivalent chromium, beryllium, tin,
vanadium, and titanium.  In most cases the sulfate salts would be
nearly the most soluble, but using a variety of anions (not just
bicarbonate and sulfate but bromate, perchlorate, chloride, chlorate,
nitrate, nitrite, acetate, formate, fluorosilicate, bromide, iodate,
iodide, etc.) would permit a higher total number of cations than the
use of any single anion type.  The ordering by solubility (g/100 mℓ at
20°) might be something like the following:

* Calcium: bromate (230), chlorate (209), perchlorate (188), bromide
  (143), nitrate (129), nitrite (84.5), chloride (74.5), iodide (66),
  acetate (34.7), bicarbonate (16.6), formate (16.6), fluorosilicate
  (0.518)
* Magnesium: chlorate (135), iodide (140), bromide (101), nitrate
  (69.5), chloride (54.6), acetate (53.4), perchlorate (49.6), sulfate
  (35.1), fluorosilicate (30.8), bromate (<58), formate (14.4), iodate
  (8.6), [bicarbonate][5] (0.077)
* Ferrous: perchlorate (299), bromide (117), nitrate (87.525, unstable
  at room temperature), acetate (“highly soluble”), chloride (62.5),
  sulfate (28.8)
* Cupric: chlorate (242), bromide (126), nitrate (125), fluorosilicate
  (81.6), chloride (73), sulfate (32), formate (12.5), iodate (0.109)
* Aluminum: perchlorate (133), nitrate (73.9), chloride (45.8),
  sulfate (36.4)
* Ferric: perchlorate (368), nitrate (138), chloride (91.8), sulfate
  (25.6), iodate (0.36)
* Nickel: iodide (148), chlorate (133), bromide (131), perchlorate
  (110), acetate (“easily soluble”), nitrate (94.2), chloride (66.8),
  sulfate (44.4), bromate (28), formate (3.25)
* Cobalt: iodide (203), chlorate (180), fluorosilicate (118), bromide
  (112), perchlorate (104), nitrate (97.4), chloride (52.9), bromate
  (45.5), sulfate (36.1), iodate (1.02), nitrite (0.4)
* Zinc: bromide (446), iodide (432), chloride (395), chlorate (200),
  nitrate (between 98 and 138), sulfate (53.8), acetate (30), formate
  (5.2)
* Beryllium: perchlorate (147), nitrate (108), chloride (42), sulfate
  (39.1)

[5]: https://en.wikipedia.org/wiki/Magnesium_bicarbonate

Where an anion is missing from the list, it is sometimes because the
salt is insoluble and sometimes because I don’t know.

So you could, for example, use a mix of calcium, magnesium, and
ferrous cations, with nitrate, chloride, and acetate ions; I think the
lowest solubility of the six is calcium acetate, 34.7 g/100 mℓ, so you
could probably get an electrolyte with over 100 g/100 mℓ of solutes.
Because of the low solubility of magnesium bicarbonate, you probably
can’t get a lot of calcium bicarbonate into solution if you also have
magnesium.  (I suspect that most other cations would simply
precipitate the bicarbonate as an insoluble carbonate.)  Similarly,
you can’t use sulfate as part of the mix if you’re trying to
mineralize with calcium ions.

It might be worthwhile to pick anions that won’t corrode your anode,
which is another thing that’s less of a problem at lower temperatures.
If you have the luxury of using a gold, platinum, or pyrolytic
graphite anode, this is straightforward, but if you’re making do with
baser metals, you may have to be choosy.  See below, however, about
anode protection.

There’s the possibility of [electrolytic iron plating][4], but it
seems that getting an iron metal deposit is actually somewhat
difficult, involving extreme pH and temperature conditions (like [pH
0.5–1.5 and 87°-99°][6]) and often chelating ligands like tartrate or
[cyanide or TEA and EDTA][8].  So I suspect that under normal
conditions you’ll get iron oxides and oxyhydroxides.

[4]: https://www.finishing.com/259/82.shtml
[6]: https://www.pfonline.com/articles/iron-plating%282%29
[8]: https://patents.google.com/patent/US2714089

Nickel, cobalt, and copper plating out as metals might be a more
difficult problem to solve.

Carbonatation
-------------

If only a metal hydroxide forms, it is likely possible to convert it
to a carbonate afterwards by exposing it wet to air or choke-damp, at
the cost of some volume expansion.  For example, the very rare
[theophrastite][1], Mohs 3.5, might form from nickel salts in the
absence of carbonate, but I think should carbonate to [nickel
carbonate (gaspéite)][2], Mohs 4.5.  Aluminum is the exception, since
it does not generally form a carbonate, so electrolyzed by itself it
would probably produce only gibbsite.

[1]: https://www.mindat.org/min-3936.html
[2]: https://en.wikipedia.org/wiki/Gasp%C3%A9ite
[3]: https://en.wikipedia.org/wiki/Gibbsite

    | cation    | hydroxide                 | carbonate            |
    |-----------+---------------------------+----------------------|
    | calcium   | soluble portlandite (2)   | chalk (3)            |
    | magnesium | brucite (2.5–3)           | magnesite (3.5–4.5)  |
    |           |                           | hydromagnesite (3.5) |
    | ferrous   | ???                       | siderite (3.75–4.25) |
    | cupric    | spertiniite (soft)        | malachite (3.5–4),   |
    |           |                           | azurite (3.5–4)      |
    | aluminum  | gibbsite (2.5–3)          | μ                    |
    | ferric    | goethite, sorta (5–5.5)   | ???                  |
    | cuprous   | ???                       | ???                  |
    | nickel    | theophrastite (3.5)       | gaspéite (4.5)       |
    | cobalt    | (rather unstable)         | spherocobaltite (4)  |
    | zinc      | soluble rare sweetite (3) | smithsonite (4.5)    |
    |           |                           | (a type of calamine) |
    | beryllium | behoite (4)               | ??? soluble          |

I think you could probably directly precipitate the carbonates by
keeping enough choke-damp dissolved in the water under pressure and
low temperature, which in most cases would produce a stronger result.

Goethite (FeOOH) is particularly interesting as the hardest mineral in
this table; limpets use goethite *fibers* (whiskers) to harden their
radula teeth, achieving [tensile strengths of 3.0–6.5 GPa][20],
several times higher than Kevlar, any steel, or even spider silk,
which is how limpets can literally eat rocks; the elastic modulus
measured 120 GPa.  Probably electrolytic deposition is not a useful
way to grow whiskers, much less protein/whisker nanocomposite
metamaterials, but it’s useful to have this approximation to
goethite’s mechanical properties.

Goethite is formed naturally through, among other processes, the
oxidation of siderite (FeCO₃), a process I suppose must swallow water
and throw off choke-damp and hydrogen.  Ferrous ions tend to oxidize
to ferric in the atmosphere, and there seems to be no ferric
carbonate.

[20]: https://royalsocietypublishing.org/doi/full/10.1098/rsif.2014.1326 "Extreme strength observed in limpet teeth, by Asa H. Barber, Dun Lu, and Nicola M. Pugno, 02015-04-06, J. R. Soc. Interface 12: 20141326, 10.1098/rsif.2014.1326, CC-BY"

Firing the result
-----------------

If you heat the resulting accreted mineral, you may be able to
transform it into something more useful, but generally this will
involve the expulsion of some material (water, choke-damp, perhaps
hydrogen) and a reduction in volume, which can cause the shape to
crumble.  Fillers as suggested above may be useful in keeping the
resulting stresses below cracking limits.

Brucite (2.3446 g/cc, 58.3197 g/mol) decomposes to magnesia at 350°
(periclase, Mohs 6, 3.6 g/cc, 40.304 g/mol) by the loss of a water
and, apparently, about 55% of its volume.  Magnesia is not very strong
but is notable for not melting until 2852°, far exceeding wüstite
(1377°), sapphire (2072°) and even quicklime (2613°).

Similar to brucite, aluminum hydroxide ([gibbsite][3], 2.42 g/cc,
78.00 g/mol, Mohs 2.5–3) decomposes at 300° into poorly structured
alumina, which converts to α-alumina (sapphire, 3.987 g/cc,
101.960 g/mol) upon further heating, apparently losing 60.33% of the
original hydroxide’s volume.  If it’s cementing together grains of
silica, you would expect the formation of aluminum silicates like
mullite at the sapphire-silica grain boundaries, and the silica might
be able to prevent the overall structure from crumbling from this
dramatic volume decrease, perhaps instead developing internal
porosity.  (Silica has its own dunting problems, but they are much
less severe than the volume loss from dehydrating gibbsite.)

Alternative fillers that might have less cracking problems include
sapphire, forsterite, mullite, larnite, phosphates such as those of
calcium and aluminum, and of course zirconia and other well-known
refractory materials.

Anode protection and solution replenishment by digestion
--------------------------------------------------------
    
Perhaps you could put the anode (which ought to be something inert,
maybe lead or carbon) in a block of chalk or slaked lime, so that the
acid formed at the anode harmlessly converts to calcium sulfate rather
than being released into the solution to attack the workpiece being
formed.  (This is another advantage of the sulfate anion, aside from
its high solubility with most candidate cations.)  However, carbonic
acid would attack the chalk and be neutralized by it.  Other anions
like the chloride should instead liberate calcium ions from the chalk
to renew the solution, allowing the use of a smaller amount of
solution and lower solute concentrations, since the great mineral
reservoir is in the block of chalk.  This process would also prevent
the anions from reaching the anode itself, where they could be
oxidized into undesired byproducts and erode the anode.

Insoluble hydroxides and carbonates of other cations would also work
for this purpose.  Of course, so would a sacrificial metal anode; but
perhaps smithsonite, magnesite, and siderite are cheaper than their
corresponding metals, and you can’t put calcium in water.

Alternative solvents
--------------------

Water has many nice features for electrolysis, particularly for this
purpose: it’s highly polar, relatively nontoxic, relatively stable at
commonplace temperatures and pressures, it provides hydroxyl ions to
the minerals being formed, and it will dissolve any water-soluble
products, which is desirable if you want the final product to
withstand contact with water.  Still, many other polar solvents are
known, and one of them might be better for this purpose; polar
solvents include anhydrous ammonia, dimethyl sulfoxide, molten
phosphoric acid, acetonitrile, ethanol, ethyl acetate, sulfur dioxide,
tetrahydrofuran, nitromethane, dichloromethane, anhydrous formic acid,
propylene carbonate, acetone, hydrogen fluoride, anhydrous nitric
acid, anhydrous sulfuric acid, glacial acetic acid, formamide, molten
salt systems including low-temperature ionic liquids, deep eutectic
systems, and dinitrogen tetroxide, but there are many others.

Some of these can contribute their own radicals to the substances
being formed through electrolysis; ammonia, for example, could
contribute amide and ammonium ions rather than hydroxyl ions, say to
precipitate struvite or metal amides like sodamide.  I suspect that
molten phosphoric acid can dissolve many phosphates; for example,
perhaps you could dissolve magnesium ions or even frank (tri)magnesium
(di)phosphate in molten phosphoric acid, then electrophoretically
accumulate the magnesium anions at the cathode, without reducing them
to metallic magnesium?  Phosphoric acid has been used for 40 years as
an electrolyte in phosphoric-acid fuel cells, operating between 170°
and 220°, but in that case it only has to carry hydrogen, of which it
is of course eminently capable.  I don’t know how to find out what
else it can solvate.

[Propylene carbonate][10] is another particularly promising solvent;
it’s commonly used as an electrolyte in primary lithium batteries, has
a stronger dipole moment and a wider liquid range than water (-48° to
242°), and, like phosphoric acid, is nontoxic and not inflammable.

[10]: https://en.wikipedia.org/wiki/Propylene_carbonate

Oh dude, what about aqueous phosphates?
---------------------------------------

Phosphate has multiple protonation states very similar to carbonate,
with a similar effect on solubility.

Acid (mono)calcium (dihydrogen) (di)phosphate dissolves 2 g/100 mℓ in
water and melts at only 109°.  By contrast, “dicalcium” (hydrogen)
(mono)phosphate, the mineral brushite (Mohs 2.5), is 100× less
water-soluble, 0.02 g/100 mℓ, and tricalcium (di)phosphate, the
dehydrated version of hydroxyapatite, is less water-soluble still, at
0.00012 g/100 mℓ.  Hydroxyapatite itself (Mohs 5) is perfectly
insoluble in water.  So, if you have a saturated solution of
monocalcium phosphate, you ought to be able to get precipitation of
the more basic calcium phosphates around a cathode, where there’s less
phosphate and more calcium, as long as the region doesn’t get
phosphate-depleted by a factor of 100×.  Perhaps more exciting, you
ought to be able to do this in molten monocalcium phosphate at very
accessible temperatures.

5.18 micromoles per coulomb of dicalcium phosphate (136.06 g/mol) is
0.705 mg per coulomb, and the density is only 2.929 g/cc, so under the
conditions considered earlier (10 A over 100 cm²) we’d get
0.866 mm/hour at 100% Faraday efficiency, about twice the growth rate
of brucite.  For brushite.  Except probably you’d end up converting
most of it to TCP or hydroxyapatite, which cuts the growth rate in
half again.

(Mono)magnesium (dihydrogen) (di)phosphate is not as friendly to
water, since it hydrolyzes into phosphoric acid and the insoluble
dimagnesium form, and I’m not sure about the aluminum salts.

Other polyprotic anions
-----------------------

I don’t think there are corresponding opportunities with the analogous
ammonium/ammonia/amide and sulfate/bisulfate/sulfuric-acid systems, at
least not in water solution.  The sulfates of calcium, lead,
strontium, and barium are reasonably water-insoluble, but even calcium
bisulfate doesn’t seem to exist at all, except in homework-cheating
websites and the catalogs of fraudulent chemical merchants.

The other polyprotic acids I’m familiar with are mostly similarly
unhelpful; nobody knows what hydrogenchromates would look like, and
hydrosulfide (“bisulfide”) and hydrogenoxalate (“bioxalate”) are
similar to bisulfate, with soluble sodium, potassium, and ammonium
compounds but no polyvalent cations.  Potassium bioxalate is notable
as “salt of sorrel”; I’m not sure there’s a (di)potassium oxalate.

I’m not sure about citrate, which is triprotic.  The magnesium/citrate
system does at least have known trimagnesium and (highly soluble)
monomagnesium forms, but different sources vary on whether the
trimagnesium form is highly soluble or, like tricalcium citrate,
sparingly soluble.  I also don’t know about monocalcium and dicalcium
citrate.

Boric acid is triprotic but it’s hard to get it to react with things
other than itself and to form insoluble compounds; however, as with
silicates, there are nesoborates, soroborates (hypothetically),
cycloborates (hypothetically), inoborates, phylloborates, and
tektoborates.  Boracite (Mohs 7–7.5, “very slowly soluble in water”)
is a tektoborate Mg₃B₇O₁₃Cl, which I guess is sort of like
trimagnesium heptaborate.  The other known tektoborates are
chambersite (same thing but with manganese) and hilgardite (same thing
but with calcium (2½ borons per calcium) and a different crystal
structure).  Why chlorine is always involved in these tektoborates is
a mystery to me (well, londonite and rhodizite lack it, but they’re
beryllium-based and may lack boron entirely).  There’s a pure calcium
borate called nobleite (Mohs 3, 6 borons per calcium) which is a
phylloborate, and another called colemanite (Mohs 4.5, 3 borons per
calcium) which is an inoborate.

I suspect the calcium borates might work for this: if the overall
electrolyte is mostly dilute boric acid with some anions to help keep
calcium dissolved (chloride or acetate, say) maybe the calcium
concentration around the cathode would get high enough to precipitate
insoluble calcium borates.  But I’m just speculating, lacking any real
evidence that you could maintain an adequately soluble calcium/borate
electrolyte at any pH.  Magnesium borates are maybe more promising
given their natural occurrence.

It would be really interesting if you could solidify waterglass
electrolytically; maybe you could drive out those pesky alkali ions
that reduce its hardness and glass transition temperature so badly.
You’d be left with a silica gel rather than fused quartz, though.
(See below about Veeraraghavan et al., who seem to have had success.)

There are about another 35 inorganic polyprotic [oxoacids][11] known
that might conceivably support the same kind of mineralization as
carbonic acid, but I mostly don’t know anything about them.

[11]: https://en.wikipedia.org/wiki/Oxyacid

3-D printing stone by directing electric fields
-----------------------------------------------

The mineralization reaction, like any electrodeposition reaction, can
be limited by ion concentrations or by electric field strength.  By
using a pointed anode, especially one that’s insulated except for the
tip, you can concentrate the electric field in a particular area and
thus accelerate the electrodeposition there.  By varying the current
through several such anodes, you can vary the electric field
spatially, and possibly also the ion concentration; so by moving them
around you can perhaps deposit stone where you like.  In the more
immediate vicinity of the anodes, however, you form acid, which will
*erode* hydroxide and carbonate minerals.

Demolding
---------

Suppose you electrolytically mineralize a thick sheet of hydroxide or
carbonate stone onto one surface of a metal sheet cathode which has
been bent into some sort of desirable shape.  If you now reverse the
polarity of the electrolysis, acid should form at the surface of the
old cathode and attack the part of the stone that’s in direct contact
with it; in most cases, this will dissolve it, although there are
exceptions such as sulfate attacking calcium compounds or phosphate
attacking most things.  Then you can remove the stone from the old
cathode easily.  This could enable the use of such a metal sheet as a
reusable mold in a process similar to pottery slipcasting, making many
stone copies of the same metal form.

The anodic dissolution process will tend to attack the form, but it’s
probably possible to get a long form life anyway with metals that are
fairly resistant to that kind of attack, like lead, chromium, gold, or
platinum.  And it may not be a very serious problem, since the stone
will quickly neutralize the acid thus generated.

Previous work
-------------

Sometimes a month in the lab can save you an hour in the library.
What does the library have to say about this stuff?

### Deng et al. ###

[Deng et al.][15] report Faraday efficiencies of 50% to 76.5% in
electrolytic precipitation of 99.6% pure magnesium hydroxide with a
100cm² graphite anode 4 cm from a stainless cathode of the same size,
with a room-temperature electrolyte of 100 g of magnesium chloride
hexahydrate dissolved in 2 ℓ of deionized water and <1% Na⁺, running
40 mA/cm² (thus 4 A) for 4 h.  They report the best efficiency at
0.5mol/ℓ Mg⁺⁺.  This paper tells me exactly what I wanted to know on
the first page (the reproducible setup for their experiment and their
major results); the only missing information is the voltage.

The paper then goes on to explain what factors they found affect
Faraday efficiency: low magnesium concentrations lower Faraday
efficiency; current densities below 40 mA/cm² also lower Faraday
efficiency (above which it’s basically constant, though they only
tried up to 70 mA/cm², i.e., 7 A/dm² or 700 A/m²), which is the
opposite of what I expected; so do interelectrode distances under 4 cm
because they allow the MgCl₂ to recombine; so do Na⁺ concentrations
under 1% (because they increase electrolyte resistance) or of 3% or
over (for obvious reasons), dropping Faraday efficiency from 70.5% at
1% Na⁺ down to 65% at 10% Na⁺.  They don’t say whether that’s weight
percentage or mole percentage, or whether the denominator is the salt,
the cations, or the solution.

The brucite precipitated was in the form of 40–200 nm nanoparticles,
so it must have been a royal pain in the ass to filter out.

My only complaint is that I would have liked to see some numbers from
particular runs, though, including the actual measured mass of the
dried magnesium hydroxide rather than the calculated Coulomb
efficiency.

At 76.5% faradaic efficiency they’d be getting 36.9 kilocoulombs per
mole of brucite (2.3446 g/cc, 58.3197 g/mol), thus 1.58 mg/C and
0.674 μℓ/C, or the other way around, 1.48 MC/ℓ or 633 kC/kg.  If we
suppose that they were using 3 V, which has to be in the ballpark,
then that’s 4–5 MJ/ℓ or about 2 MJ/kg.  At a nominal price of 4¢/kWh
(11 nanodollars per joule, typical for wholesale power, though solar
has brought this down by a factor of 4 for new projects in much of the
world) this is about 2¢/kg, which is cheaper than construction sand
and enormously cheaper than portland cement.  Of course that doesn’t
include the cost of getting hold of bittern, much less purified
magnesium salts.

[15]: https://www.atlantis-press.com/article/25837650.pdf "Current efficiency of synthesis magnesium hydroxide nanoparticles via electrodeposition, by XinZhong Deng, YaoWu Wang, JianPing Peng, YueZhong Di, 3rd International Conference on Material, Mechanical and Manufacturing Engineering (IC3ME 2015)"

### Sano, Hao, and Kuwahara ###

[Sano, Hao, and Kuwahara report][12] efficient electrolytic extraction
of magnesium from seawater as 99% pure magnesium hydroxide by using a
cation exchange membrane and “deaerating” the seawater first (either
by boiling or by acidifying) in order to remove the choke-damp and
thus avoid precipitating chalk.  Their objective seems to have been to
get magnesium as a structural metal or battery electrode.  They ran a
solution of 5% sal mirabilis through their “anode channel” (they
didn’t want to use a chloride salt to avoid chlorine production) and
used platinum-plated titanium electrodes.

If they bothered to say anything about the material properties of the
brucite thus formed, or the currents, voltages, current densities, or
electrode spacings they used, I must have missed it.

[12]: https://www.sciencedirect.com/science/article/pii/S2405844018320735 "Development of an electrolysis based system to continuously recover magnesium from seawater, by Yoshihiko Sano, YiJia Hao, and Fujio Kuwahara, Heliyon 4 (2018) e00923, 10.1016/j.heliyon.2018.e00923, CC-BY"

### Johra et al. ###

[Johra et al.][16] tested some seacrete; they produced some at
0.8 cm/year with 2.5 V in 25°–31° seawater off Thailand, and tested
some more that was accidentally produced by parasitic currents around
the Italy–Greece 400 kV submarine power transmission cable, which had
more magnesium and was consequently software.  They report that
brucite deposits from seawater when the pH locally reaches 9.2, and
confirm my inference above that brucite is weaker than calcite.  The
paper contains the following text apparently plagiarized from
<http://www.globalcoral.org/faq/> (identical matching text
*italicized*):

> Regarding the CO₂ budget of the calcium carbonate precipitation, one
> could intuitively think *that since limestone deposition is removing
> dissolved inorganic carbon from the ocean, this should be
> compensated by absorption of atmospheric CO₂* into *the ocean.*
> However, the opposite phenomenon occurs. This can be explained by
> the fact *that there is* actually *much more dissolved inorganic
> carbon in the ocean (in the form of bicarbonate ion* HCO₃̄) *than
> there is CO₂ in the atmosphere*. Consequently, *the predominant
> reaction* for the precipitation o [sic] calcium carbonate is as
> follows:
> 
> > Ca⁺⁺ + 2HCO₃ = CaCO₃ + H₂O + CO₂
> 
> Therefore, for every two molecules *of bicarbonate precipitated as
> limestone in the ocean, one molecule* of CO₂ is released into the
> atmosphere. On the *geological time scale, this is the major source
> of atmospheric CO₂ along with volcanic* activity [9]. More
> information about Seacrete and materials formed by electrodeposition
> of minerals in seawater can be found in the publications of Goreau
> [9,10].

The corresponding text on the Global Coral Reef Alliance site says
(again, with identical matching text italicized):

> It seems intuitively obvious that *since limestone deposition is
> removing dissolved inorganic carbon from the ocean, that this should
> be compensated by one molecule of atmospheric CO2 [sic] dissolving*
> in *the ocean*, but in fact the opposite happens.
> 
> The reason is *that there is much more dissolved inorganic carbon in
> the ocean, in the form of bicarbonate ion, than there is CO2 [sic]
> in the atmosphere*, and the ocean is a pH buffered system due to
> dissolution of limestone sediments and also acid base reactions
> [sic] involving weathering of oceanic basalts to clay minerals. So
> *the predominant reaction* is:
> 
> Ca++ + 2HCO3- = CaCO3 + H2O + CO2 [sic]
> 
> That is to say, in order to preserve pH and charge balance, for each
> molecule *of bicarbonate precipitated as limestone in the ocean, one
> molecule* is released as CO2 [sic] to the atmosphere. On a
> geological time scale, this is the major source of atmospheric CO2
> [sic] along with volcanic* gases.

Note that the text that isn’t copied verbatim is only a slight
paraphrase.

This text has been on the Global Coral Reef Alliance website since at
least [02014-05-05][17], so it’s clear they didn’t plagiarize it from
this 02021 paper, though it’s possible that the authors of the paper
*are* the Global Coral Reef Alliance, in which case no plagiarism
would be involved; or that both plagiarized the text from some third
source, such as the Goreau papers cited.

However, the paper is not listed in
<http://www.globalcoral.org/gcra-papers/>, and the authors of those
papers are Thomas Goreau ([husband of Dra. Nora Isabel Arango de
Urriola y Goreau, who died in 02016][18]), Verena Vogler, Raymond
Hayes, Ernest Williams, Charles Mazel, Paul Andre DeGeorges,
R. Grantham, H. Faure, T. Greenland, N.A. Morner,
J. Pernetta, B. Salvat, V.R. Potter, Paulus Prong, Munandar, Mahendra,
Muhammad Rizal, Chair Rani, Ahmad Faizal, and herrzoox, who Johra et
al. fail to list as co-authors.  Of these I think Thomas Goreau,
herrzoox, and maybe Paul Andre DeGeorges are actually part of GCRA,
and Wolf Hilbertz and Dra. Arango de Urriola were also involved.
Goreau seems to have predeceased his wife, but they had a son also
named Tom, and there seem to be new papers by “Thomas Goreau” from
02020, so there may be two Thomas Goreaus publishing on this topic.

[17]: https://web.archive.org/web/20140712191745/http://www.globalcoral.org/faq/#sink
[18]: http://www.globalcoral.org/memoriam-dr-nora-goreau-april-25-1921-december-18-2016/

[One of the Goreau papers is open access under CC-BY][19], and doesn’t
contain this text, being mostly a catalog of ways people have screwed
up their seacrete experiments, up to and including connecting the
cables backwards!

[19]: https://www.scirp.org/journal/paperinformation.aspx?paperid=48444 "Electrical Stimulation Greatly Increases Settlement, Growth, Survival, and Stress Resistance of Marine Organisms, by Thomas J. Goreau, Global Coral Reef Alliance, Cambridge, USA; in Natural Resources, Vol. 5 No. 10, July 2014 10.4236/nr.2014.510048 CC-BY"

Their apparent plagiarism aside, Johra et al. report that their
low-voltage seacrete was 80.8% aragonite, 18.9% brucite, and 0.3%
calcite, while the high-voltage seacrete was 52.3% brucite.  They also
detected significant amounts of silicon, aluminum, strontium, iron,
chlorine, and sulfur in the seacrete samples.  They report
2499.2 kg/m³ (σ=9.1 kg/m³) for the low-voltage seacrete and 1771 kg/m³
(σ=17.4 kg/m³) for the high-voltage seacrete due to higher porosity.
Disappointingly, they measured the compressive strength of only the
high-voltage seacrete (16.8 MPa), though they did some imprecise
improvised tests that suggest that the low-voltage seacrete should be
in the neighborhood of 25 MPa.

[16]: https://www.sciencedirect.com/science/article/pii/S0950061820330294 "Thermal, moisture and mechanical properties of Seacrete: A sustainable sea-grown building material, by Hicham Johra, Lucia Margheritini, Yovko Ivanov Antonov, Kirstine Meyer Frandsen, Morten Enggrob Simonsen, Per Møldrup, and Rasmus Lund Jensen, Construction and Building Materials, Volume 266, Part A, 10 January 2021, 121025, 10.1016/j.conbuildmat.2020.121025"

### Alamdari et al. ###

[Alamdari et al.][13] report that magnesium goes from 1272 ppm in
seawater to 30,000 ppm in the “end [bitterns][14] of NaCl production
units from seawater”, and they precipitated brucite from that bittern
using lye.

[13]: https://www.researchgate.net/publication/244400927_Kinetics_of_magnesium_hydroxide_precipitation_from_sea_bittern "Kinetics of magnesium hydroxide precipitation from sea bittern, by A. Alamdari, M. R. Rahimpour, Nadia Esfandiari, Ehsan Nourafkan, February 2008, Chemical Engineering and Processing 47(2):215-221, 10.1016/j.cep.2007.02.012"
[14]: https://en.wikipedia.org/wiki/Bittern_%28salt%29

### Veeraraghavan, Haran, Slavkov, et al. ###

[These researchers succeeded at electrodepositing sodium silicate on
galvanized steel for corrosion resistance in 02003][29], and they
mention that Speers and Cahoon had success with “anodic deposition at
high voltages” (E. A. Speers and J. R. Cahoon, J. Electrochem. Soc.,
145, 1812 (1998)):

> Speers and Cahoon report the deposition of Si from alkaline silicate
> electrolytes by anodizing Al at 350 V.  However, this process is
> limited to Al or similar metals which have stable anodic oxide films
> and also involves application of large potentials.  Recently,
> Chigane et al. reported formation of silica thin films on copper
> substrates through cathodic electrolysis of pH 3.3 ammonium
> hexafluorosilicate solution.  In acid solutions, fluoride ions help
> keep the silica stable in solution.  In the absence of fluoride
> ions, the bath becomes unstable and precipitates as Si(OH)₄.
> However, high pH and presence of fluoride ions limits the process
> developed by Chigane et al. to metals capable of withstanding
> corrosive environments.  Further, the deposits obtained by them were
> highly porous and hence not suitable as a protective coating.

[29]: https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1170&context=eche_facpub "Development of a Novel Electrochemical Method to Deposit High Corrosion Resistant Silicate Layers on Metal Substrates, by Basker Veeraraghavan, Bala Haran, Dragan Slavkov, Swaminatha Prabhu, Branko Popov, and Bob Heimann, Electrochemical and Solid-State Letters, 6 2 B4-B8 2003, 10.1149/1.1537092, https://scholarcommons.sc.edu/eche_facpub/171"

I’m not sure that what precipitates is orthosilicic acid rather than
frank silica, but whatever.

Veeraraghavan et al. were using a 3.22 SiO₂:Na₂O mole ratio solution
for their electrodeposition, which I think is similar to the bottle I
have here, and platinum-niobium anodes, and apparently they
electrodeposited zinc onto their workpieces themselves before
beginning the silicate deposition.  Initially they diluted the
waterglass to 5.6 wt% sodium silicate, pH 10.5, and electrodeposited
with a potentiostat† at 12 V for 15' at 75°, and I guess they finally
got a 1μm-thick silicate layer of zinc silicate followed by silica and
pyrosilicate (Si₂O₇).  They report that at room temperature no
silicate formed, but further heating to 85° gave highly porous
deposits but no faster deposition.

(For my purposes, the higher porosity would be desirable, but their
objective was to replace chromate conversion coatings for metal
protection, not grow rocks in a tank, and by that measure they
achieved an order of magnitude better performance, for which the
porosity was undesirable.)

They were definitely depositing on the cathodes, not the anodes; they
say, “The silicate deposition was carried out in a two-electrode
plating cell made of glass with Pt-niobium anodes.  Zinc-plated steel
panels (EZG-60G) of surface area 116 cm² each side, as-received from
ACT labs[,] were used as the cathodes.”  They contrast their process
with the anodic deposition process of Speers and Cahoon:

> Under an applied potential, before Si anions can be
> electrochemically reduced on the surface of Zn, all the solvent
> water will be electrolyzed.  The soluble silicate is a complex
> mixture of silicate anions.  Hence it can be expected that under
> large applied electric fields, the negatively charged silicate
> species migrate to the anode and are deposited.  Speers and Cahoon
> report that the thickness of the silicate layer formed using such
> method is limited only by the time of anodic deposition. They report
> thickness up to 100 μm for 20 min of deposition. ... Note that the
> silicate layer is not more than 1 μm thick.  Unlike anodic silicate
> deposition, the deposits are very thin 1–3 μm.  The maximum
> thickness seems to be limited to 3 μm.  These results indicate that
> the mechanism of cathodic Si deposition in our case is more complex
> than was previously reported.

They report that drying the layer at 100° instead of room temperature
made it 0.69—2 orders of magnitude more resistive, presumably by
affecting the structure of the silica layer, and they show that drying
at 175° or 200° made the layer much less full of cracks, and it
retained corrosion resistance better afterwards.

They explain the electrodeposition through an increase in hydroxyls
and thus pH around the cathode, which increases the polymerization of
the silicate and thus decreases its solubility.  Weird thing about
that, waterglass usually precipitates with *decreasing* pH, but maybe
that’s because normally you’re adding Na⁺ or K⁺ ions to the solution
to increase the pH, and in this case they’re adding Zn⁺⁺ ions, or
rather bizincate ZnO(OH)⁻ ions.

If I had to criticize something about this paper, it would be that
they don’t mention anything about stirring, turbulence, anode size,
electrode distances, or the nature of the surface of their anode,
which could be important considerations to reproducing their results.
Also, they only analyzed the surface film with EDAX, which can show
the concentration of Zn, Si, Fe, and other such heavy elements, but is
useless for light elements like Na and O (their EDAX results for these
oxide coatings include an obviously spurious “0.00 wt%” oxygen entry,
and don’t mention sodium at all).  But, from my point of view, the
sodium content of these protective films is one of the most important
questions, even for their declared objective of corrosion resistance:
the lower it is, the better the films will resist years-long immersion
in water.  Presumably a Keim-like treatment with alkaline-earth
cations would help, but whether it’s necessary is clearly an important
question for the wide deployment of their process.

______  
† A “potentiostat” is usually the chemist’s name for a voltage
regulator.  The main difference is that they cost US$3000.  There are
also three-electrode potentiostats that use a third reference
electrode to keep the working electrode (the cathode in this case) at
a fixed voltage relative to the electrolyte, but Veeraraghavan et
al. don’t mention such a reference electrode and specifically say
their “plating cell” was “two-electrode”, so I think they were just
using a 12-volt voltage regulator.

### Harman 01924 ###

[R.W. Harman wrote an article in 01924][30] about reducing the
alkalinity of sodium silicate solutions by a method quite similar to
the chlor-alkali process, but starting from sodium metasilicate rather
than salt.  They comment that silica precipitation on the anode was a
problem at high current densities:

> The second method[,] of increasing the C.D. considerably hastens the
> removal of the alkali and gave good results; but it has its
> limitations in the fact that, above a certain limit, increase of
> C.D. causes separation of solid silica on the platinum anode.  This
> limiting C.D., above which silica separates on the anode, varies not
> only with the dilution but also markedly with the ratio.  The more
> concentrated the silicate solution and the greater the proportion of
> silica in the ratio, the lower must be the limiting C.D.

[30]: https://pubs.acs.org/doi/10.1021/j150255a014 "Aqueous Solutions of Sodium Silicates, I, by R.W. Harman, 01924. The Journal of Physical Chemistry, 29(9), 1155–1168.  10.1021/j150255a014"

They give the sodium/silicon ratios as “gram-equivalent” ratios of
sodia and silica, and concentrations as “weight normality” numbers
N<sub>w</sub> which I think are sodium ion molarities:

> Throughout the whole of this work, the different silicates and
> mixtures will be designated by the ratio Na₂O:SiO₂ in equivalent
> proportions, this being the simplest and most convenient system of
> nomenclature and one already finding general and serviceable use in
> industry.  Thus a ratio of 1:2 contains one equivalent of Na₂O in
> grams to two equivalents of SiO₂.
> 
> All concentrations, except where otherwise stated, are expressed in
> weight normality (N<sub>w</sub>) with regard to their sodium
> content, i.e. in gram-equivalents of sodium per 1000 grams of
> water. Thus, a 1 N<sub>w</sub> solution of ratio 1:4 contains
> ½(Na₂O·4SiO₂) expressed in grams, in 1000 grams of water.

[WP explains][31]:

> By this definition, the number of equivalents of a given ion in a
> solution is equal to the number of moles of that ion multiplied by
> its valence. If 1 mol of NaCl and 1 mol of CaCl₂ dissolve in a
> solution, there is 1 equiv Na, 2 equiv Ca, and 3 equiv Cl in that
> solution. (The valency of calcium is 2, so for that ion 1 mole is 2
> equivalents.)

[31]: https://en.wikipedia.org/wiki/Equivalent_%28chemistry%29

Given the above definition, I’m not totally sure but I guess a mole of
SiO₂ would be “two equivalents”.  The problem is that SiO₂ isn’t an
ion!  But we see that Harman considers Na₂O·4SiO₂ to be “1:4”.

So, given all that, we have Harman’s account of what circumstances
were necessary for rapid mineralization on his rotating-platinum-disc
anode:

> With a 2N<sub>w</sub> [2 mol/ℓ Na⁺] solution of ratio 1:1
> [Na₂O·SiO₂] or 1:2 [Na₂O·2SiO₂] a C.D. of 0.044 amps per
> sq. cm. scarcely diminishes the alkalinity of the solution; a
> C.D. of 0.15 amps per sq. cm. diminishes the alkalinity quite
> rapidly but yet does [not?] cause separation of solid silica.

The “not” here is missing from the published paper, but the sentence
structure (as well as a paragraph I will quote later) seems to
strongly suggest that it should be there, and the numerous
typographical inconsistencies and errors also suggest that such an
error is eminently possible, which unfortunately completely changes
its meaning.

Harman continues:

> With ratio 1:4 [Na₂O·4SiO₂] a 3N<sub>w</sub> solution gave a very
> thick deposit of silica with a C.D. of 0.11 amps per sq.cm.  A
> 2N<sub>w</sub> solution with a C.D. of 0.11 also gave a thick
> deposit[,] but with a C.D. of 0.044 amps per sq.cm., although silica
> was deposited on the anode, at the end of 4 hours the solution on
> analysis was found to be 0.8N<sub>w</sub> and its ratio was 1:5.2
> [Na₂O·5.2SiO₂].  This solution was very opalescent and after two
> days set to a gel and later on exhibited synaeresis.  A
> 0.5 N<sub>w</sub> solution of ratio 1:4 with a C.D. of 0.13 amps per
> sq. cm. also deposited silica, but at the end of 10 hours, during
> which time the C.D. gradually fell [I guess they weren’t using a
> galvanostat], the resulting solution was found to be 0.08
> N<sub>w</sub>, with a ratio of 1:40 [Na₂O·40SiO₂!!]. This dilute
> solution showed no signs of gel formation.
>
> Thus with ratio 1:1 a 2N<sub>w</sub>, solution may be electrolysed
> with a C.D. of 0.15 amps per sq. cm. but with ratio 1:4 a
> 1N<sub>w</sub> solution gives a deposit with as low a C.D. as 0.044.
> It has been found possible by this means to prepare 2 N<sub>w</sub>
> solutions of ratios 1:2, 1N<sub>w</sub> 1:3, and 1:4.  Higher ratios
> than these set to a gel, viz., 1:5 above 0.1N<sub>w</sub>, but in
> very dilute solutions the removal of alkali can proceed until the
> solution is practically one of pure silicic acid.

It seems that they consider anodic deposition something to be avoided
(perhaps since the silica deposit robs the solution of silica, while
the objective of the procedure is to increase the silica-to-sodium
ratio), but they considered the 1:1 2N<sub>w</sub> 0.15A/cm² result to
be acceptable.  This reinforces my inference that the “not” I inserted
above should be there.

Unfortunately the deposits are only ever described in qualitative
terms, as “thick” or “very thick”.  I’d really like to know whether
“thick” means 10μm and electrically insulating, 100 μm, 1 mm, or
10 mm.  WHAT DID YOU SEE, HARMAN?

But Harman’s main concern here was measuring the conductivity of the
solutions, not electrolyzing them.

Weird metals
------------

[Aerographite][32] can be 180 g/m³ (180 μg/cc, six times lighter than
air) and 1 kPa UTS, soaring in strength to 160 kPa at 8500 μg/cc.  The
fabrication process involves CVD of graphite at 760° onto a template
of ZnO (m.p. 1974°), which is then etched away with H₂, since zinc
boils at only 907°.

Zinc is very similar to magnesium (b.p. 1091°) in many ways, but
electrodepositing zinc in aqueous solution is feasible, while for
magnesium you need to use molten salt.  After selectively
electrodepositing zinc microwires, you could change chemistry to
electrodeposit zinc hydroxide (3.053 g/cc, 99.424 g/mol, amphoteric,
soluble in aqueous ammonia) in the same way described above for
brucite, then calcine it to ZnO at 125° with a loss of more than half
its volume (5.606 g/cc, 81.406 g/mol, and thus 69 mol/ℓ to the
hydroxide’s 30.7).  Then, you can use it as a template for CVD or PVD
(of carbon or anything else that can withstand 907°) and hydrogen-etch
away the ZnO.

[32]: https://en.wikipedia.org/wiki/Aerographite