One of the problems I ran into with flux-deposition particle-bed 3-D
printing was depositing small consistent amounts of flux particles.
Fine particles clump and stick, which means dry particles don’t
deposit uniformly.

I learned today of a device called a “trickler” used for depositing
small amounts of particulate (milligrams, not micrograms, at a rate of
a few milligrams per second).  It’s a near-horizontal cylindrical tube
that can rotate around its axis with some particles in it.  As it
rotates, the particles roll around in it, which helps break up clumps,
and some fall out the end of the tube; some versions have a screw
thread on the inside of the tube to push the particles along.  There’s
a constant feed of new particles into the other end of the tube,
achieved for example by immersing it in a bin of particles and having
one or more holes in its side.  If you stop rotating the tube, the
particles stop falling out, because of friction with the floor of the
tube.

It seems to me that this approach is likely to work well for solid
particle flux deposition, although the resolution may be a bit coarse.
If we’re shooting for 100-micron “pixels”, well, that’s about two
micrograms, and the idea is that only about 5% of the total particle
bed is flux, so 10 nanograms per “pixel”, and we’d like that 10 ng to
be about 10 particles to reduce the random variation.  (Weighing or
filming the particulate bed during the operation may enable the
counting of individual flux particles.)

1 ng is about 500 cubic microns; your particle diameter then needs to
be on the order of 10 microns, which is about four or five linear
orders of magnitude smaller than what the “tricklers” normally manage.
Such fine particles tend to clump pretty aggressively.

Liquids
-------

Of course, the standard solution to particulate-bed printing is to
deposit “binder” via jets of liquid “ink” using a standard inkjet
printer mechanism.  I’d been thinking that this probably wasn’t a
viable option for flux deposition, because the fluxes usually aren’t
water-soluble, but now I think it’s possible in many cases to use
water-soluble forms of fluxes.

For fluxing quartz, for example, the highly water-soluble hydroxides,
bicarbonates, acetates, or formates of sodium (soluble to 109, 9.6,
46.4, and 81.2 g/100ml of water at 20°) or potassium (112, 33.7, 256,
and 337) would probably work; heating any of these will eventually
leave only the oxide.  Soluble salts of calcium such as the chloride
(74.5), formate (16.6), acetate (34.7), or nitrate (121.2) may be
helpful in addition, as they further lower the melting point of the
quartz while reducing the water-solubility of the final product.

Things that decompose into lead oxide might be superior to the above
for fluxing quartz.  Lead nitrate (54.3) is suitable; its acetate
(44.3), formate (16), chlorate (144), and perchlorate (440) might be,
too.

Boric acid is reasonably water-soluble (4.7 g/100ml) and liquefies at
only 170.9°, at which point it can dissolve or react with a fair
number of other things, most especially including quartz and other
silicates.  The whole sequence is somewhat complex: at 170.9° it
becomes metaboric acid, which melts at 176° and converts to B2O3 at
around 300°, which can crystallize into forms that melt at 450° or
510° but is more commonly amorphous.

Many other metals have highly soluble chlorates and perchlorates,
although potassium’s are only mildly soluble.  These could be
especially useful in contexts where mixing with potassium salts is not
necessary, but oxidation is either harmless or desired.  These
decompose to produce oxygen and chloride when heated above 400°.  This
kind of phenomenon may be useful for providing heat for firing the
printed part.

There are a number of highly water-soluble phosphate salts (TSP is
12.1 g/100ml, MSP is 59.9, DSP is 11.8, STPP 14.5, STMP 22, K3PO4 90,
MKP (KH2PO4) 22.6, MAP 36, DAP a bit over 57.5, TAP 58) which can
contribute phosphate ions; in particular the ammonium phosphates
decompose to phosphoric acid and ammonia gas at moderate temperatures
around 200°.  Phosphate ions can react with polyvalent cations to form
extremely stable materials like calcium phosphate (apatite, brushite,
whitlockite, bone, hilgenstockite), aluminum phosphate (berlinite,
augelite, variscite), and zinc phosphate (hopeite, parahopeite,
tarbuttite, and dental cement).  So you could imagine selectively
stabilizing some calcium-bearing or zinc-bearing material by squirting
phosphate salts on it, heating them to cause a reaction (which might
bind particles together), then removing the untreated particles.

Alumina is attacked by hydrochloric acid to become aluminum chloride,
which is not only highly soluble in water but also sublimes at 180°.
Generalized chlorates (including perchlorates, chlorites, and
hypochlorites such as that of calcium) may be suitable donors of
chlorine for such a reaction, but even ordinary chlorides like those
of sodium or calcium might work at a high enough temperature.

### Soluble fluxes for 3-D printing metal alloys ###

For fluxing iron particles, carbohydrates like sugar would probably
work well; they can dehydrate, leaving only carbon, long before the
iron starts to absorb hydrogen, although oxidation of the iron with
the resulting water molecules may be a concern.  Paraffins contain no
oxygen and aren’t water-soluble, but other solvents may work to make
paraffin inkjets, and they too will carbonize around 300°, long before
the iron takes up their hydrogen; but anything but very-long-chain
paraffins (polyethylene) will boil off pretty easily.  So perhaps
something like linseed oil, which is largely a triglyceride made of
α-linolenic acid and linoleic acid, would work better, with nonzero
oxygen content but much lower thermal stability.  Turpentine is its
traditional solvent.

Among low-melting metal alloys, my attention is drawn by 5% tin or
aluminum added to zinc depressing its melting point from 419.53° to
382°; 2.5% silver added to lead depressing its melting point from
327.46° to 304°; 9% zinc added to tin (KappAloy9) depressing its
melting point from 231.93° to 199°; 3% silver added to indium
depressing its melting point from 156.5985° to 143°; and 5.5% zinc,
4.5% indium, and 3.5% bismuth added to tin depressing its solidus from
231.93° to 174°.  Also, in general the tin-lead alloys have a solidus
of 183°, the melting point of the eutectic.

Popular higher-melting metal alloys include brass, bronze, aluminum
bronze, and arsenical bronze.  Zinc-copper brass doesn’t really have a
eutectic; its lowest-melting version is 100% zinc (419.53°) and at low
zinc content there’s a relatively slow drop of the melting point from
copper’s 1084.62°.  The copper-tin system (ordinary bronze) is broadly
similar but somewhat luckier, with the solidus depressing to about
900° with 10% tin (if I’m reading this phase diagram right).  Aluminum
bronze has a real eutectic at 548.2° and about 32% copper, with a
fairly steep drop in aluminum’s solidus from 660.32° down to that
temperature with only about 6% copper, as well as a eutectoid on the
other side around 92% copper and about 1050°.  So you could imagine
using something near 6% copper as a “sintering aid” for aluminum
particles.  The arsenic-copper system is similar, with an apparent
eutectic at 685° and 20.8% As, but already depressing the solidus to
that temperature at only 7.96% As.  (Wait, that doesn’t make sense,
that’s higher than aluminum’s melting point.)

However, you probably can’t get tin or aluminum to alloy with metal
particles by adding water-soluble salts of tin or aluminum to it and
then heating the mix.  If you heat salts like aluminum nitrate it’s
going to be hard to get the metal out of them; instead you’ll just get
the oxide.  (I’m not sure what stannous chloride decomposes to, but I
imagine reducing it to tin is hard.)  You can eventually reduce just
about any metal oxide by heating it enough with hydrogen or ammonia,
but that may complicate the situation further here.  Such metals could
maybe be handled by including some magnesium particles in the bed to
steal their oxygens.

Copper and silver salts are more promising here.  Silver doesn’t
really mind being reduced at all, and even copper is only mildly
inerested in oxygen.  In particular, if copper oxide has a chance to
react with aluminum, it does so violently.  So you could imagine that
nitrates or acetates of copper could be inkjet-squirted into aluminum
particles (making, say, about 20% Cu(NO3)2), heated to decompose them
to oxide (say, about 8.4% CuO, which is 80% copper, so the mix was
1.7% oxygen), then reacted with the aluminum to produce an alloy (in
the example case, 6.7% copper and about 3.6% sapphire, with the
remainder being aluminum.)  Some chlorides (of copper, say) might help
to initiate the reaction with the aluminum by breaking down the
aluminum oxide layer.

Lin, Han, and Li (2012) report that copper acetate dehydrates at 168°
and decomposes to copper oxides at 302°.  Naktiyok and Özer (2019)
report similar results, though they report that the decomposition
starts happening below that temperature.

Silver should be even easier than copper to reduce; the
silver-aluminum eutectic, though, is something like 28% aluminum and
566°, with 15% silver needed to drop aluminum’s solidus below 600°.

(Although silicon is commonly used to reduce the melting points of
metals, I’ve omitted it entirely here on the theory that very few
metals are able to reduce silicates, which are the only water-soluble
silicon-bearers that occur to me.)

Indium, bismuth, and gallium might also be effective at reducing
metals’ melting points, but often the resulting alloys don’t have
desirable properties.  Also, bismuth doesn’t seem to have any
water-soluble salts, while indium and gallium salts are mostly soluble
but don’t decompose on heating.

Ammonium dihydrogen arsenate (48.7 g/l) might be a useful source of
arsenic for fluxing copper.

Alternative solvents might include carbon tetrachloride, ethanol,
carbon disulfide, chloroform, supercritical carbon dioxide,
dichloromethane, and ammonia.  Carbon disulfide in particular can
dissolve sulfur, which forms low-melting sulfides with a huge number
of metals; these can then be reduced back to the metal by roasting.

Other ways to get fine particles to not stick together
------------------------------------------------------

Flowability has been a major concern for pillmaking for a long time,
along with rules of thumb, like a 31-35° angle of repose and under 16%
compressibility for good flowability, and 56-65° angle of repose and
over 32% compressibility for very poor flowability.

What can we do to get even flow, other than trickler-style rotating
tubes?

- Ultrasonic vibration, as I’ve suggested previously.  Even
  non-ultrasonic vibration is commonly used in pillmaking, with
  accelerations in the tens of gees; above five or ten gees even
  relatively stubborn particulates may flow, though if the angle of
  repose is higher than 65° or the compressibility over 37% even that
  may not be enough.  Particulates with “good flowability” as
  described above do not need vibration.

- Dilute them with coarser inert carrier particles, or grow coarser
  particles on them.  If each 10-micron-diameter particle of binder is
  attached to a 200-micron-diameter round particle of ammonium
  chloride, it will flow easily; mild heating of the particle bed will
  “sublimate” the ammonium chloride.  Many other possible alternatives
  exist for ammonium chloride: sulfur, dry ice, paraffin wax, other
  polyolefins, and so on.  Other possible ways of removing the inert
  carrier include reacting it with a gas to form another gas or
  dissolving it in a solvent, which might permit the use of even table
  salt.  The crucial fact is just that the carrier particles must
  somehow be made to disappear without disturbing the binder.
  (Solvent removal ought to use low-surface-tension solvents.)  In dry
  inhalers, lactose is the typical carrier.

- Premix them with some other particles that they don’t stick to, but
  which form part of the final result.  In the case of fluxing an iron
  particle bed with 3% carbon, you could mix each part of the carbon
  particles with 3 parts of additional iron particles, so you’d have
  to add 12% instead of 3%.  In systems where a little graphite
  inclusion would be harmless, you might be able to mix inert graphite
  particles with the flux particles to keep them flowing freely.
  Taken to the extreme, this approach amounts to depositing the
  particle bed like a stack of sand paintings, depositing different
  mixes in different parts of a layer to form a layer of constant
  thickness.

- Coat the particle surfaces with something that sticks together
  poorly; in the case of waterglass particles used to flux quartz, for
  example, treating the surface with the sorts of silanes used to
  enhance adhesion of glass fillers to nonpolar polymers might work
  well, so that when the flux particles touch one another, they
  encounter only alkane moieties and very little adhesion.  Magnesium
  stearate is commonly used for this purpose in pillmaking, simply by
  dry-tumbling it with, for example, a microcrystalline cellulose
  excipient, for a few minutes.  It might work even better to coat
  *some* flux particles with an alkane moiety like the tail of
  stearate and *others* with a fluorocarbon moiety, so that they will
  tend to have even less affinity for the foreign half of their
  neighbors.  Other stearates commonly used are that of calcium and of
  zinc.

- As an alternative to *adding* a low-surface-energy coating it may be
  possible to *transmute the surface into* one in some cases.
  Fluorinating the surface of a polymer or metal is one example,
  although this shades into the sort of silane surface treatment
  suggested above, and fluorinating some things will *increase* their
  surface energy rather than decreasing it.
  
- Keeping them very dry will help in many cases.  Materials commonly
  added to table salt for this purpose include calcium silicate,
  sodium aluminosilicate (a zeolite), sodium ferrocyanide, and
  potassium ferrocyanide; other common anticaking food additives that
  work by similar absorption include bentonite and tricalcium
  phosphate.

- Presumably there’s a temperature effect, but whether being cold or
  being hot is better, I don’t know.

- An ion emitter (or the foil used on those antistatic phonorecord
  brushes) may help to reduce electrostatic forces that tend to cause
  clumping.  Maybe also using conductive particles or a conductive
  coating.

- If you run the whole apparatus inside a centrifuge, so that the
  small flux particles have proportionally more mass relative to their
  surface forces, that should help.

- Generating the flux particles as smoke generates them out of contact
  with one another, so they cannot stick to one another.  The smoke
  can be generated in a stream of plasma or gas, which is then sucked
  the gas through the particulate bed so the flux can deposit.  Or it
  can be generated simply by heating and deposited on the particulate
  by diffusion.

- Of course to the extent that the fine particles can be spherical
  rather than irregular, acicular, or platy, they will tend to clump
  less.  The lower the aspect ratio, the better.

- And to the extent that the particles are nonuniform in size, I think
  the smaller particles will provide more adhesion among the larger
  ones.

- On the contrary, though, a small quantity of very fine irregular
  particles should help to keep a much larger quantity of much larger
  particles apart; “glidants” in pills commonly work in this way,
  including silica gel, fumed silica, talc, magnesia, and even
  cornstarch.  Magnesia was what made Morton Salt pour when it rained.

- Porous and soft particles will adhere to one another at lower
  pressures than hard ones.

It occurs to me that if a particulate is gently tumbled in a closed
drum that has pinholes in its walls, clumps that fall down and impact
a pinhole may not fit through, but may be able to eject some particles
through the hole.  If this can be observed it may be a solution to the
problem of depositing ten or fewer particles in a given position.
