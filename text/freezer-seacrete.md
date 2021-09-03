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
the sodium chloride, would greatly improve the situation.)  Making
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
molar).  Alternatively, magnesium hydroxide, brucite, Mohs 2.5–3,
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
units used by electroplating shops in the US, which is on the high end
of the current levels commonly used for electroplating, so it may be a
little high but it’s not outrageously so.  Nickel sulfamate baths for
nickel plating are operated as high as 15 A/dm² at the cathode.

At the other end of the spectrum, suppose we can accrete smithsonite,
ZnCO₃ (125.4 g/mol, 4.5 g/cc).  5.18 micromoles per coulomb here gives
us 0.650 mg of smithsonite per coulomb, or 6.5 mg/s at 10 A, or
23.4 g/hour, and over 100 cm² that’s... 0.52 mm/hour.  I was hoping
for a way more exciting number, but I guess the higher density of the
smithsonite mostly cancels out its higher molar mass.

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
hygroscopic phyllosilicates like mica and talc can fill their role.

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

Post-hoc carbonatation
----------------------

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
    |           |                           | (calamine)           |
    | beryllium | behoite (4)               | ??? soluble          |

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

The other polyprotic acids I’m familiar with are similarly unhelpful;
nobody knows what hydrogenchromates would look like, and hydrosulfide
(“bisulfide”) and hydrogenoxalate (“bioxalate”) are similar to
bisulfate, with soluble sodium, potassium, and ammonium compounds but
no polyvalent cations.  Potassium bioxalate is notable as “salt of
sorrel”; I'm not sure there’s a (di)potassium oxalate.

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
but with calcium and a different crystal structure).  Why chlorine is
always involved in these tektoborates is a mystery to me (well,
londonite and rhodizite lack it, but they're beryllium-based and may
lack boron entirely).  There’s a pure calcium borate called nobleite
(Mohs 3) which is a phylloborate.

It would be really interesting if you could solidify waterglass
electrolytically; maybe you could drive out those pesky alkali ions
that reduce its hardness and glass transition temperature so badly.
You’d be left with a silica gel rather than fused quartz, though.

There are about another 35 inorganic polyprotic [oxoacids][11] known
that might conceivably support the same kind of mineralization as
carbonic acid.

[11]: https://en.wikipedia.org/wiki/Oxyacid
