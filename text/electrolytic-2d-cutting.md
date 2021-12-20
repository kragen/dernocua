As I’ve written about at some length previously, some of the most
promising computational fabrication technologies at macroscopic scale
are 2-D cutting processes like laser cutting, waterjet cutting, and
CNC plasma table cutting.  See file `layers-plus-electroforming.md`
for notes on the scaling laws.  [Cooper Zurad][0] has prototyped an
electrolytic 2-D cutting process using a needle-shaped cathode, but
his process is very slow and imprecise because he’s cutting at a
single point, and because he’s not doing the usual ECM things:
closed-loop control of the process gap, using pulsed current, or
vibrating the electrodes to reduce the tradeoff between flushing and
cutting speed.  [Traumflug did similar experiments in 02011][1].

[0]: https://hackaday.com/2021/12/17/simple-mods-turn-3d-printer-into-electrochemical-metal-cutter/
[1]: https://reprap.org/wiki/Electrochemical_Machining#A_Study_on_Suitability_for_PCB_Manufacturing

However, even without gap control, pulsing, and vibration, if you’re
cutting over a large area rather than just a point, you should be able
to get a proportionally higher material removal rate.  And if you’re
cutting a thin sheet of material, even a low material removal rate
might be adequate.

Unlike other ways of cutting a thin sheet of material, this sort of
electrolytic cutting leaves no burrs and does not produce
heat-affected zones or mechanical stresses in the material being
cut — though for very thin sheets the surface tension of the
electrolyte may be big enough to plastically deform the workpiece,
possibly requiring supercritical drying if the workpiece is ever to be
removed from water.

Cathode patterns
----------------

One way to do this is, as I wrote in Dercuano in 02016, to have an
array of separate cathodes close to the anode workpiece, controlling
the voltage or current of each cathode to either dissolve the
workpiece near it, or not.  A different way is to prepare the pattern
of the cuts in a material form, for example as a printed circuit
board, a network of wires on an insulating plate, or a pattern of
apertures in an dielectric mask placed over a continuous-sheet
cathode, and make this pattern the cathode.  Then you can “print” this
cut pattern on a series of sheets of metal.

One particularly interesting cathode-patterning possibility is to
produce the insulating “mask” by laser-printing on paper, ideally
paper that will not fall apart when soaked with the electrolyte.  If
the laser printing is sufficiently solid to be used for other
toner-transfer methods, it should also work for this electrolytic
sheet cutting approach; unlike the other toner-transfer methods, it
might be possible to get more than one metal copy from a single paper
pattern.

Thermal wax printers may or may not produce a better dielectric
pattern.

Separators between the cathode and anode
----------------------------------------

In either case, the cathode is placed very close to the anode
workpiece; the most practical way of doing this is probably to
separate them with either some sort of fabric, such as a paper towel
or other nonwoven cloth or a woven cloth, or with a thin porous
membrane full of holes, for example a thin porous layer of
polyethylene.  (In the case of laser printing on paper, the paper
itself provides the separator.)  Once the current is turned on, the
cuts are all made simultaneously, though some may take longer to
finish than others.  Voltammetry should be adequate to determine when
the process completes.

With this approach, the porous separator, plus any space it produces
around the cathode, need to be able to absorb the metal salts produced
by the cutting, since vibration or indeed flushing at all would be
very difficult.

Containment: inner and outer cut contours
-----------------------------------------

In cases where the cut pattern contains some cuts that are completely
surrounded by others, for example holes “drilled” in a part to be cut
out, there is a potential problem.  If we feed the anode current in
from the edge of the anode workpiece, it may not be able to reach the
inner cuts if the outer cuts happen to complete first.  There are
several possible ways to solve this problem:

1. We can do the cutting in two phases, first cutting out the inner
   contours and then later the outer contours.  This is a common
   tactic in single-point 2-D cutting processes like those I mentioned
   above, because it prevents the outer piece from falling out of
   plane before you’ve cut the holes in it.  This would result in
   slower cutting but prevents the problem.  It requires setting up
   the cathode pattern in two or more electrically separate parts.

2. We can feed in the current to the anode with an inert conductive
   backing anode, thus coupling in current to the workpiece over its
   entire back surface rather than only at the edge.  This will reduce
   the efficiency of the process and perhaps eliminate the usefulness
   of voltammetry for measuring its completion.

3. We can try to leave “tabs” around the outside of each cut, so that
   when the process is finished all the desired parts are still all
   connected together and must be removed from their support in a
   separate step.  This is commonly done in casting, molding, and,
   especially in the case of thin materials, 2-D cutting by means such
   as lasers.  It might be possible to calibrate the process with
   enough precision that the tabs are barely thick enough to maintain
   electrical continuity until the inner contours are all cut out, but
   continuing the process a little longer severs the tabs.

Example setups
--------------

1. As one example, as I wrote in “Dead bugging” in Derctuo, it’s easy
   enough to find 100-μm-thick copper conductors (a) in stranded
   copper wire.  You could paste these in the desired pattern (b) onto
   a high-impact polystyrene surface (c) with PVA glue (d), bridging
   disconnected parts of the cut pattern with fine varnish-insulated
   magnet wire (e).  After allowing the PVA glue to dry, you make it
   water-insoluble by treating with a borax solution.  You lay a paper
   towel (f) onto the pattern and soak it with sodium nitrate (g).
   You lay a sheet of 10-μm-thick household aluminum foil (h) onto the
   paper towel and press the whole assembly together, then apply a low
   voltage power supply for long enough to dissolve more than 10 μm of
   aluminum.  The results should be, for example, if your current
   density is enough to cut 100 μm/s, that the cut is completed in
   100 ms.  Applying electricity for less time will result in etching
   the surface rather than cutting through.

2. You can heat up example 1 to make the cutting go faster, using a
   heated press such as are commonly used in dye sublimation, laundry
   pressing, and vinyl transfer onto cloth.

3. For the foil (h) in examples 1 or 2 you can substitute heavy-duty
   aluminum foil, commonly available in thicknesses such as 50 μm;
   aluminum flashing; aluminum sheet from aluminum cans (typically
   100 μm) after cleaning nonconductive contaminants off of one of its
   two sides; aluminum sheet as is commonly available from metal
   vendors like Metals Depot, commonly in thicknesses as low as .032"
   (81 μm) or any other source of sheet aluminum.  Thicker sheets will
   take proportionally longer to cut, produce less precise cuts, and,
   above a certain thickness, will also require a thicker separator
   (f).  Cutting multiple stacked layers of metal (h) in a single run
   is a possibility that may increase the efficiency of the process in
   several ways, such as amortizing the setup time over multiple
   produced pieces, but will reduce the precision achieved.

4. For the sodium nitrate (g) in examples 1, 2, or 3 you can
   substitute any other soluble salt whose anion forms a soluble
   aluminum salt or aluminate, such as sodium chloride, azanium
   acetate, iron sulfate, or potassium hydroxide, among dozens of
   other possibilities; particularly appealing are the chloride,
   acetate, sulfate, and hydroxide salts of azanium and the alkali
   metals, due to their high solubility and low toxicity; the
   corresponding salts of iron and zinc are also relatively safe and,
   except for the hydroxides, soluble.  More toxic options include
   sodium perchlorate.  In cases such as potassium hydroxide which are
   capable of corroding the aluminum rapidly without electricity, it
   will be necessary to stop the reaction, for example by washing the
   pieces thus produced with water, a buffer solution, or an acid that
   will not attack the aluminum.  Salts which produce a passivating
   “anodized” layer on the aluminum at lower voltages may be
   preferable, because although they reduce efficiency, they will
   restrict the electrolytic etching to areas at sufficiently high
   voltages, improving the precision of the process.  It is probably
   also useful to include additives such as metal borates, metal EDTA,
   metal tetrasodiumglutamatediacetates (GLDA) to prevent the
   formation of aluminum hydroxide, metal cyanides, SPS (CAS
   27206-35-5), MPS (CAS 17636-10-1), ZPS (CAS 49625-94-7),
   polyethylene glycol, polyvinyl alcohol, polyvinyl acetate,
   glycerine, propylene glycol, dipropylene glycol, DPS (CAS
   18880-36-9), surfactants (such as SLS, alkali stearates, EN 16-80
   (CAS 26468-86-0), or EA 15-90(CAS 154906-10-2)), UPS (CAS
   21668-81-5), PPS (CAS 15471-17-7), NAPE 14-90 (CAS 120478-49-1),
   sodium benzoate, saccharin, coumarin, metal tartrates, metal
   citrates, metal sulfonates not otherwise mentioned, metal urates,
   thiazole, benzaldehyde, thiourea, quaternary azanium salts,
   phthalimide, metal methanesulfonates, metal ethylene sulfonates,
   depolarizers (such as manganese dioxide, metal sulfates, silver
   oxide, or metal chromates and dichromates, among many other
   possibilities), the acid forms of the anions mentioned here, or
   these anions’ salts with organic cations or azanium, as well as
   other additives used in electrodeposition and ECM.  Also, the
   solvent in which the salt is dissolved can be replaced with any
   other solvent suitable for the salts employed, such as DMSO,
   ammonia, ethyl acetate, THF, DCM, acetone, acetonitrile, DMF,
   formamide, acetic or formic acid, alcohols (such as methanol,
   ethanol, and isopropanol, among many others), organic carbonates
   (such as propylene carbonate, ethylene carbonate, diethyl
   carbonate, or dimethyl carbonate, among many others), glycerol,
   nitromethane, molten methylsulfonylmethane, deep eutectic systems,
   or other ionic solvents, among hundreds of others, or mixtures of
   these, with or without water; such substitution can permit the use
   of higher temperatures or electrolyte salts that either react
   undesirably in water or will not dissolve in it, and may be able to
   reduce the surface tension to less mechanically damaging levels.
   Generally the more important solubility consideration will be the
   solubility of the salts produced at the anode workpiece, since you
   cannot choose their cations, rather than the electrolytic etchant
   (g).

5. For the paper towel (f) in examples 1, 2, 3, or 4 you can
   substitute any other porous material that will not be attacked too
   rapidly by the salts and is not too electrically conductive except
   ionically; for example, asbestos, fiberglass, carbon fibers,
   carborundum fibers, rock wool, basalt fiber, ordinary paper,
   buckypaper, nonwoven polypropylene, nonwoven polyester, nonwoven
   cotton, nonwoven rayon, onion-skin paper, other thin papers such as
   crepe paper and those used for tracing drawings and rolling
   cigarettes, perforated polyethylene film, perforated PET film,
   perforated polypropylene film, hydrogels (such as gelatin, agar,
   borated polyvinyl alcohol, or silica gel), woven textiles of the
   above-mentioned fibers, and porous ceramics such as glass frits or
   unglazed fired clays, among dozens or hundreds of other
   possibilities.  Woven textiles will tend to add their weave pattern
   to the etched pattern, which may be considered a form of error in
   some applications.  You can stack more than one such layer; for
   example, a layer of perforated polyethylene film can be used to
   separate a layer of borated PVA hydrogel from the cathode,
   preventing adhesion.  Perforated boPET or polyethylene films can
   easily be made under 10 μm in thickness, a feature which might
   enable reproducing details not much larger than that.

6. For the varnish-insulated magnet wire (e) in examples 1, 2, 3, 4,
   and 5, you can substitute wire insulated by other means such as
   thin layers of dielectric polymers, or you can pierce holes in the
   dielectric backing (c) to pass through conductors from a region
   devoid of electrolyte or at least separated from the workpiece by a
   dielectric or by distance.

7. For the borate-crosslinked PVA glue (d) in examples 1, 2, 3, 4, 5,
   and 6, you can substitute any other material that will hold the
   pattern conductors in place while permitting electrolytic access to
   them; for example, agar, gelatin, cross-linked starch, hydrogels
   used for contact lenses (such as silicone hydrogels, hydroxyethyl
   methacrylate), sodium polyacrylate as used in maxi pads,
   polyethylene glycol (perhaps treated to crosslink it into an
   insoluble gel as is commonly done for cell encapsulation), and
   porous ceramics such as glass frits or those made by unglazed fired
   clay.  Alternatively, the separator material (f) can simply be
   bonded permanently to the cathode, which would require the
   electrolyte to be washed out between runs rather than merely
   replacing the separator as you would normally do.  Alternatively,
   instead of holding the cathode pattern in place with any kind of
   continuous material, you can hold it in place with occasional thin
   fibers of dielectric material either bonded to the dielectric
   separator (c) or passing through it, as is done in embroidery or
   furniture decoration to hold certain kinds of thread or piping on
   the surface of the material.

8. For the dielectric backing material (c) in examples 1, 2, 3, 4, 5,
   6, and 7, you can substitute any other dielectric material that
   will not be too readily attacked by the electrolyte and in
   particular the alkaline solution that will tend to form in contact
   with the cathode, such as glass, polyethylene terephthalate,
   polyethylene, polypropylene, epoxy resins, teflon, fluorinated
   ethylene propylene, other polyester resins, aluminum oxide, or
   other metal oxides, among many others.  A stack of such layers may
   be useful.  Extremely inert backing materials such as teflon
   introduce the problem that firmly adhering the cathode to them with
   the PVA glue (d) or its alternative may be more difficult; stacking
   a readily adherable material such as HIPS on top of a more inert
   material such as polyethylene is one possible solution, and welding
   the backing (c) to the glue (d) will also improve adhesion in
   difficult cases.

9. For the fine copper conductors (a) in examples 1, 2, 3, 4, 5, 6, 7,
   and 8, you can substitute nearly any other conductive material at
   all as long as it’s sufficiently cathodically protected; for
   example, copper, aluminum, gold, silver, platinum, palladium,
   rhodium, tantalum, niobium, vanadium, molybdenum, graphite, glassy
   carbon, non-glassy amorphous carbon, nickel, stainless steel,
   chromium, lithium metal, sodium metal, or ordinary steel, or
   mixtures of these, among hundreds of other possibilities, in the
   form of fine wire, foil, thin film, or plating.  Some of these
   possibilities rule out the use of certain electrolytes; for
   example, sodium metal probably cannot be used in contact with water
   regardless of how well it’s cathodically protected.  The use of
   nobler metals such as tantalum and gold does not affect the anodic
   dissolution process and permits the use of more aggressive
   electrolytes.  Thinner metals such as gold leaf, especially
   together with thinner separator layers and thinner workpieces,
   permit finer patterning of the workpiece.  Additionally, you can
   provide the pattern instead by using a continuous layer or mesh of
   any of these materials as the cathode, superposed on a selectively
   nonporous mask of some dielectric material, such as the
   laser-printer toner mentioned earlier or materials such as those
   listed in example 9 above.

10. In examples 1, 2, 3, 4, 5, 6, 7, and 8, as an alternative to a
    pattern (a) supported on a dielectric backing (c) as described
    above, you can use a conductive plate (i) made out of any
    conductive material such as those mentioned in example 9 above
    with a selectively patterned impermeable dielectric mask (j) on
    it, so that electrolysis can only proceed where the mask is absent
    or at least porous.  For example, you can use sheet steel or any
    other sheet metal with nail polish selectively painted onto it; or
    a dielectric photoresist deposited on it and optically patterned
    in the way that is common for fabricating integrated circuits or
    printed circuit boards; or laser printer toner transferred onto
    it; or a dielectric coating selectively deposited by inkjet
    printing, perhaps then baked to improve the coating; or
    “permanent” marker ink; or “dry erase” marker ink; shellac (an
    idea due to Mina); cellophane tape; paraffin; powder coat paint,
    as commonly used for painting industrial machinery; glass, as in
    cloisonné; dried soluble silicates, if heated between uses to
    drive out excess water; a layer of a passivating compound formed
    from the surface of the conductive plate (i) itself, for example
    by heating or anodizing; or any other dielectric that is
    sufficiently resistant to the electrolyte.  Many of these
    dielectrics can be applied in a continuous layer and then
    selectively removed by laser ablation, for example with a
    low-wattage laser cutting and engraving machine like those
    commonly used for cutting MDF, or by some other method such as
    stamping, grinding, abrasive jet blasting, or scraping.  The mask
    (j) can be a separate removable layer rather than firmly adhered
    to the conductive plate, as in the earlier example of
    laser-printed paper; the screens used in silkscreening or the
    waxed fabric in batik would work well for this.  A nonwoven
    thermoplastic cloth can combine the functions of the mask (j) and
    the electrolyte bearer (f) by being melted in the regions to be
    “masked”, rendering it nonporous, as is commonly done to join
    nonwoven thermoplastic cloths.

11. In example 10, instead of protecting parts of the pattern
    electrode surface (i) with a solid dielectric, you can protect
    parts of the pattern surface by recessing them far enough that
    when the conductive pattern plate is brought into contact with the
    electrolyte-soaked porous material (f), the recessed parts are
    separated from it by an air gap.

12. In example 10, instead of protecting parts of the pattern
    electrode surface (i) with a solid dielectric, you can cut spaces
    in the electrolyte-soaked porous material (f), or otherwise
    pattern it to fill only a part of the space between the two
    electrodes.  For example, a thin stranded string of fiber can be
    shaped into the desired pattern, moistened with electrolyte, and
    squished between the two plates before applying the power.

13. In examples 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10, if you use an
    electrolyte that can dissolve the aluminum workpiece at zero
    voltage, such as alkali-metal hydroxides or hydrochloric acid, you
    can reverse the voltage to cathodically protect the *workpiece*
    rather than the pattern.  This will result in dissolution of the
    workpiece in a *positive* pattern (leaving workpiece where the
    pattern is present rather than where it is absent) rather than a
    negative one.  In this case it may be convenient to first subject
    the whole workpiece to cathodic reduction (using it as a cathode
    with an unpatterned anode, possibly with a different electrolyte)
    to eliminate possible passivating oxide films, before reversing
    the polarity.  This approach can also result in the dissolution of
    the pattern, possibly in an uneven fashion resulting from parts of
    it remaining connected longer, as with the tabs mentioned earlier.
    (A similar consideration applies to ensuring the electrical
    continuity of the protected part of the workpiece until the end of
    the process.)  This can be prevented by using a nobler material
    for the pattern than for the workpiece and operating at a moderate
    enough voltage to prevent the pattern from being attacked.
    Stainless steel wire or graphite is probably the most convenient
    pattern material in cases where copper is insufficiently noble.
    As an alternative to preventing this electrolytic pattern erosion,
    if the pattern is thick enough, you can alternate between
    patterning a workpiece cathode in this way, and electrodepositing
    new metal on the pattern to replace the lost metal.

13. In examples 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, and 13, as explained
    earlier, rather than using a dielectric backing (c) with a
    patterned electrode (a) on it, you could use an array (k) of
    independently controlled electrode pixels insulated from one
    another.

14. In examples 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12, rather than
    *dissolving* the workpiece, you can deposit oxides or other
    insoluble metal salts on its surface by a suitable choice of
    electrolyte (g), known as “anodizing”.  This can be used, among
    other things, to selectively passivate it for future use as a
    pattern electrode (as mentioned in example 10), to selectively
    passivate it to selectively resist some other etching process or
    reaction, to selectively harden the surface, to color it with
    opaque compounds, or to color it with iridescence by controlling
    the layer thickness, a process which is less effective for
    aluminum than it would be with some other metals.  It may be
    possible to modulate the current density over time to spatially
    modulate the density of the oxide layer to form a rugate filter.

15. In examples 1, 2, 3, 4, 5, 6, 7, 8, 9, and 14, instead of a
    dielectric backing (c) with a patterned cathode, you can use one
    or more movable cathodes (m) that electro-etches the anode
    workpiece (h) where it touches the porous material (f) and not
    elsewhere.  Some useful forms of patterned cathode for this
    purpose might include one or more a narrow rollers like pizza
    cutters, which cut along a line rather than at a single point
    while exerting minimal friction on the porous material (f); one or
    more needles which are touched to the surface of the porous
    material (f) at different points at different times; a metal ball
    like that used in ballpoint pens and ball bearings, which can roll
    like the pizza cutters; outlines of various forms, such as circles
    and semicircles of different diameters, the edges of razor blades,
    the whole shapes of parts, logos, letters, cartoon characters, and
    halftone patterns, which can be placed at different points on the
    material at different times and etched to varying depths.  These
    “stamps” can be made in many different ways, including engraving
    or etching a solid metal or graphite surface, and bending wire.  A
    soft wire brush is another candidate cathode.  The roller approach
    and the seal approach can be combined in a rolling seal.  A wire
    or metal tape can be used to etch a straight line of variable
    length all at once, either by hand or under the control of a
    machine similar to an old automatic wire-wrap machine.

16. In example 15, the porous material (f) can be attached to the
    movable cathode or cathodes (m) rather than to the workpiece (h),
    and the pattern can be in the porous material rather than the
    cathode, as in example 12.

17. In examples 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, or 16,
    the aluminum sheet (h) can be replaced by a sheet of almost any
    other metal or conductive ceramic with a corresponding change of
    electrolyte (g), though platinum and a few related substances are
    considered impossible to dissolve anodically.  This opens up more
    interesting anodizing possibilities, such as bluing steel, or
    depositing iridescent layers on metals with transparent oxides
    with high refractive indices such as titanium.  This cutting
    process is particularly appealing for very hard metals, ceramics,
    and cermets.

Patterning the “paper”
----------------------

In the cases where the porous material (f) is held fixed relative to
the workpiece (h), the result of the process includes not only the
etching of the anode (h) but also metal ions impregnated into parts of
the porous material (f).  In some cases this directly produces a
visible pattern on the paper or similar material, but whether it does
or not, onchrome or afterchrome dyeing can be used to produce a
permanent, colorfast pattern.  Mordants commonly used for dyeing
include salts of copper, tin, iron, aluminum, chromium, and tungsten,
so electro-etching anode metals containing these metals can be used to
selectively mordant a textile in this way — either one that is dyed
afterwards (“onchrome”) or one that is pre-impregnated with the dye
(“afterchrome”) and then merely washed to reveal the pattern.  For
this it is necessary to use a dye that cannot be effectively mordanted
with whatever cations are present in the electrolyte before
electro-etching; I think azanium ions are safe for all dyes.

Ferrous (Fe²⁺) ions from the photodecomposition of organic ferric
(Fe³⁺) complexes (ferrioxalate, ferricitrate, ferric oxalate, ferric
tartrate) are commonly used in this way to tone siderotypes with
various kinds of vegetable pigments, as explained in Mike Ware’s
*Cyanomicon* §3.5 (p. 77).  It also explains the possibility of using
the ferrous ions to “reduce the compounds of a ‘noble’ metal, such as
platinum, palladium, silver or gold, to the metallic state”, which
also leaves an indelible mark in the paper.  Below about pH 9, the
[Pourbaix diagram for iron][3] says there’s a wide stability range for
ferrous ions; unfortunately this range extends below 0 V, to about
-0.6 V, so if we look only at the equilibrium, this range can only be
used directly in the examples above in the “positive” process, where
the workpiece is a cathode that is dissolved *except* where it is
cathodically protected.  However, I think that in practice the
spontaneous reaction rates may be low enough to permit the use of the
“negative” process where the iron electrode is anodically dissolved,
particularly if there’s a little bit of postprocessing to cathodically
draw some of the dissolved iron out of solution.

[3]: https://en.wikipedia.org/wiki/Iron%28III%29#Chemistry_of_iron%28III%29

It would be exciting to be able to do the same trick with an ion that
could be further oxidized to reduce something a little less noble (and
expensive) like copper.  But I can’t think of anything.

Imaging is not the only way of using this selective ion impregnation.
The polyvalent cations thus obtained can selectively catalyze other
reactions if the porous material is supplied with the reagents, and
they can (noncatalytically) harden soluble silicate and phosphate
solutions, which can thus selectively stiffen the porous material,
thus forming a ceramic/fiber composite object with flexible blades of
fibrous material joining stiff blades of fiber-reinforced ceramic.

Ware’s book also reports (§4.2 “Pellet’s process”, p. 89):

> The new feature that Pellet introduced to solve the problem of
> fixing the positive-working process was based on earlier
> observations by Alphonse Poitevin in 1863, that ferric salts cause
> gum and similar colloids to harden and become insoluble in water,
> whereas ferrous salts do not.

In §4.10 on p. 113 he explains the gel lithography process:

> Gel lithography was also variously known in its hey-day by several
> proprietory [sic] names: Lithoprint, Ferro-gelatine, Fotol,
> Ordoverax, Velograph or Fulgur printing. The method took an
> over-exposed, but unprocessed negative blueprint image as its
> source, which was lightly squeegeed into contact with a matrix of
> moist gelatine, known as a “graph”, containing a ferrous
> salt. Diffusion of excess potassium ferricyanide out of the
> lightly-exposed and unexposed regions of the cyanotype (the image
> shadows) formed Prussian blue in the gelatin matrix, with the effect
> of hardening it locally (see §4.1.1), where it became receptive to a
> greasy lithographers’ ink, which was still repelled by the moisture
> in the unhardened regions of the gelatin. After a minute or so, the
> cyanotype was peeled off and the jelly surface inked with a
> roller. About 25 positive copies of the original image could be
> ‘pulled’, using little pressure, from the jelly, which was re-inked
> between each.

I’m not sure whether the effect of hardening the gelatin was due to
the complexed ferric ions in the ferricyanide (but Ware asserts that
it is, and we can probably trust him) or some other effect of forming
the Prussian blue.

Faraday efficiency and energy usage
-----------------------------------

Aluminum has only one common oxidation state (3+), so the Faraday
efficiency of the setup should be near perfect with aluminum.  It’s
27.0 g/mol.  At 96485.34 coulombs per mole, times three, we have 10.7
megacoulombs per kilogram:

You have: avogadro 3 e / (aluminum g/mol)
You want: MC/kg
	* 10.727928
	/ 0.093214641

At an ordinary electroplating current density of 10 A/dm² and 2.70
g/cc this is almost a year per meter:

    You have: avogadro 3 e / (aluminum g/mol) / (10 A/dm^2) * 2.70 g/cc
    You want: days/m
            * 335.24776
            / 0.0029828685

This works out to only 35 nm/s, which would take 300 seconds to cut
through a 10 μm household aluminum foil.  We ought to be able to use a
much higher current density for electrochemical machining because we
don’t have to worry about forming dendrites, but the 1000 A/dm² we’d
need to do the cut in three seconds sounds pretty extreme.  Is it?

Considering the 100-μm-diameter copper wires I was talking about at
the beginning, how much current are we talking about?  Suppose one
such wire is 100 mm long; it then covers an area roughly 100 μm by
100 mm on the porous medium (f), 10 mm².  Then 1000 A/dm² would be
just 1 amp.  Suppose we’re feeding it from both ends.  At a nominal
copper conductivity value of 58 siemens m / mm² (from
definitions.units) this works out to 2.20 Ω/m and thus 0.11 Ω in the
50 mm; if all the current came out in the middle it would be 500 mA in
each side through that 0.11 Ω, with a resulting voltage drop of about
55 mV, which is probably bearable.  But actually the current is
hopefully coming out evenly along the length of the wire, so the
situation is a little better, with that 500 mA though 2.20 mΩ/mm
initially dropping 1.1 mV/mm, but linearly dropping to 0 mA and thus
constant voltage in the middle of the wire.  Without actually doing
the algebra, I think this works out to a voltage drop of 27 mV.

This is a very reasonable voltage drop.  I think it also works out to
about 7 mW, which normally would be a large enough power to worry
about in a tiny wire like this, but maybe not when it’s immersed in
water.

The [standard electrode potential][10] of reducing 2H₂O to H₂ and 2OH⁻
is -0.8277 V (per electron), and that for oxidizing Al to Al³⁺ + 3e⁻
is -1.662 V (per electron).  If I understand this stuff right, which I
might not be, that means you need at least 834 mV between the
electrodes before you start electro-etching the aluminum.  This is a
very easy voltage to supply and implies that the overall power needed
to do these cuts is only about 800 mW, plus whatever gets wasted on
Joule heating of the electrolyte and the cathode (about 3.4% in the
electrode in the above example).  If you have something in the
electrolyte that’s more likely to deposit on the cathode than sodium
or aluminum — copper, say — then you might not have to pay even that
much; but then your cathode becomes less precise.

[10]: https://en.wikipedia.org/wiki/Standard_electrode_potential_%28data_page%29

If we use the [conductivity of seawater, 50 mS/cm](11) and an
electrolyte path of 100 μm, we get 2 Ω:

    You have: 100 um / (50 mS/cm * 100 um 100 mm)
    You want: ohms
            * 2
            / 0.5

[11]: https://en.wikipedia.org/wiki/Conductivity_%28electrolytic%29

At 1 A this would be a joule-heating voltage drop of 2 V, giving a
total of 2.859 V: 2.000 V in the electrolyte, 0.832 V in the
electrolytic interfaces, and 0.027 V in the wire.  The conductivity is
proportional to the ion mobility, the ion concentration, the ion
charge, and the temperature (≈2%/°); with more concentrated solutions,
and concentrations with highly mobile ions (hydronium beats sodium
7×), we ought to be able to get it down to 0.2 Ω and thus 0.2 V, so
that even at 1000 A/dm² (100 mA/mm²) we spend 80% of the energy on
electrolysis.  And of course at lower currents the ohmic losses become
insignificant.

At significantly higher currents the voltage drop along the wire would
become sufficient to provoke different electrolytic reactions in
different places, which is not the desired effect.  This would also
produce different current densities in different places, and thus
reaction speeds, cutting speeds, and potentially cut widths; a
higher-resistivity electrolyte will tend to avoid this problem, at the
expense of wasting more energy as heat.

A power supply that can produce 3 V at 1 A is straightforward to
cobble together from common components; in the most primitive form,
two resistors and a power-transistor emitter follower can produce this
from many USB chargers, though it would produce a lot of heat.  A more
efficient switcher design is also not very demanding and would be a
lot safer.

So in fact cutting through hand-sized aluminum foil in a few seconds
with submillimeter precision is eminently attainable, and should be
reasonably efficient, using minimally 8 mJ per millimeter and
realistically 30 mJ/mm.  If you could manage a thinner kerf, it could
be even more efficient.  Scaling the cutting up to higher speeds,
larger workpieces, or very complex cuts might start to be a challenge,
though.

Workpiece materials
-------------------

Different metals require somewhat different amounts of current, but
the density of the electron gas you’re sucking out of the metal
doesn’t vary nearly as much as other properties of metals such as
hardness, toughness, mass density, and electronegativity; here are my
calculations for the common metals:

<table>
<tr><th>metal    <th>molar mass   <th>density    <th>valence <th>current required
<td><th>Silver   <td>107.868 g/mol<td>10.49 g/cc <td>1       <td>9.38 A/mm²/(mm/s)
<td><th>Gold     <td>196.967 g/mol<td>19.30 g/cc <td>1?      <td>9.45 A/mm²/(mm/s)
<td><th>Lead     <td>207.2 g/mol  <td>11.34 g/cc <td>2       <td>10.6 A/mm²/(mm/s)
<td><th>Tin      <td>118.710 g/mol<td>7.265 g/cc <td>2?      <td>11.8 A/mm²/(mm/s)
<td><th>Zirconium<td>91.224 g/mol <td>6.52 g/cc  <td>4       <td>13.8 A/mm²/(mm/s)
<td><th>Magnesium<td>24.305 g/mol <td>1.738 g/cc <td>2!      <td>13.8 A/mm²/(mm/s)
<td><th>Titanium <td>47.867 g/mol <td>4.506 g/cc <td>4?      <td>18.2 A/mm²/(mm/s)
<td><th>Zinc     <td>65.38 g/mol  <td>7.14 g/cc  <td>2       <td>21.1 A/mm²/(mm/s)
<td><th>Iron     <td>55.845 g/mol <td>7.874 g/cc <td>2?      <td>27.2 A/mm²/(mm/s)
<td><th>Copper   <td>64.546 g/mol <td>8.96 g/cc  <td>2?      <td>27.2 A/mm²/(mm/s)
<td><th>Aluminum <td>26.98 g/mol  <td>2.70 g/cc  <td>3       <td>29.0 A/mm²/(mm/s)
<td><th>Cobalt   <td>58.9332 g/mol<td>8.90 g/cc  <td>2?      <td>29.1 A/mm²/(mm/s)
<td><th>Nickel   <td>58.693 g/mol <td>8.908 g/cc <td>2?      <td>29.3 A/mm²/(mm/s)
<td><th>Chromium <td>51.9961 g/mol<td>7.19 g/cc  <td>3       <td>40.0 A/mm²/(mm/s)
<td><th>Tungsten <td>183.84 g/mol <td>19.3 g/cc  <td>6?      <td>60.8 A/mm²/(mm/s)
</table>

(The unit A/mm²/(mm/s) is equivalently A·s/mm³, GA·s/m³, or GC/m³, but
I find these units less intuitive.)

This ordering more closely aligns with those of malleability,
ductility, and hardness than with any other property I can think of:
gold is the most malleable metal, very nearly the fastest cutting, and
soft enough to dent with your teeth (as are lead and magnesium), while
tungsten is the brittlest and nearly the hardest, and chromium is
actually the hardest and also quite brittle.

If you wanted to design a material to be more rapidly cut by ECM,
you’d probably want a composite of two or more phases, such that most
of the volume of the material was in a discontinuous phase cemented
together by a metallic continuous phase, and you could
electrolytically cut the continuous phase without having to cut the
discontinuous phase.  The discontinuous phase might be a liquid or
gas, making the material a gel or foam; it might be some other
conductive substance, such as a metal with a more positive electrode
potential, in which case it would need to be physically removed from
the cut for it to proceed; or it might be an insulator.  In any case
the grain size of the discontinuous phase would need to be smaller
than the desired cuts.

Suitable nonconductive reinforcing discontinuous phases, ideally in
the form of submicron particles and especially submicron-length
whiskers or laminae, might include carborundum, carbon nanotubes,
carbon fibers, halloysite nanotubes, other clays, boron nitride
nanotubes, basalt fiber, goethite, sapphire, talc, cubic boron
nitride, boron carbide, silicon nitride, topaz, diamond, silica,
rutile, chrysoberyl, beryl, mica, aluminum magnesium boride, boron,
iron tetraboride, titanium nitride, and zirconium nitride (?). XXX

Zirconium is particularly appealing here; though it is not as abundant
as iron, aluminum, magnesium, or titanium, it is more abundant (in
Earth’s crust) than copper, zinc, nickel, chromium, tin, lead,
molybdenum, or tungsten, on par with carbon or vanadium, it is about
as strong as iron while being substantially less dense, having a
higher melting point, and being biocompatible, and it should
electrolyze twice as fast as iron, copper, nickel, or
cobalt — assuming you can sufficiently disrupt its protective oxide
layer during electrolysis, a problem which also arises with titanium.
You could imagine a zirconium-cemented composite consisting
principally of submicron grains of yttrium-stabilized
zirconia — assuming cubic zirconia adheres as well to zirconium as the
protective oxide layer does — that can be cut electrolytically five
times as fast as steel.  Zirconium also potentially supports the
formation of hardening carbide grains like those in steel, though I’m
not sure if there’s a way to form a pearlite-like structure in
zirconium.  (See file `exotic-steels.md` for more thoughts on this
theme.)

(Zirconia is notable for its electrical properties, but at room
temperature it is an insulator, because its conductance is mediated by
the mobility of oxygen ions.)

Metallic magnesium is also appealing here because it has not only a
high electrolysis rate but also a very low standard electrode
potential (-2.372 V) and many conveniently soluble compounds.  [It has
alloys with reasonable srength][11]: yield strength “typically
75–200 MPa, tensile strength 135–285 MPa … Young’s modulus is 42 GPa.”
ASTM A36 steel, for reference, has yield strength 250 MPa, UTS 400–500
MPa, Young’s modulus 200 GPa, so these alloys have a substantial
fraction of steel’s strength and (to a lesser degree) stiffness.
Stiffness can be improved with discontinuous reinforcing fillers to a
much greater extent than strength.

[11]: https://en.wikipedia.org/wiki/Magnesium_alloy