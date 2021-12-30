Electrolytic machining of glass may be feasible, using a sort of
micro-scale variant of the chlor-alkali process in which the
alkali-producing anode directs a stream of dilute near-boiling aqueous
alkali against the glass, locally corroding its surface into soluble
sodium silicate which is immediately washed away, carrying the ionic
current toward the anode.  This would be a very slow process, but may
be useful for precisely shaping amorphous silicates.

As I understand it, the usual overall reaction of electrolysis of, for
example, sodium bicarbonate works like this.  The current is carried
by Na+ ions migrating from the anode to the cathode (in industrial
practice, through a cation-exchange membrane), while the HCO3- ions
left behind at the anode give up their electrons to the anode and
produce CO2, O2, and water: 4HCO3- -> 4CO2 + 4OH-; 4OH- -> O2 + 2H2O +
4e-.  At the cathode, meanwhile, the Na+ ions aren’t actually taking
the electrodes from it; instead, they’re taking hydroxyls from it,
which the cathode is producing as 4H2O + 4e- -> 2H2 + 4OH-.  So the
overall reaction is apparently 4NaHCO3 + 2H2O -> 4NaOH + 4CO2 + O2 +
2H2.  This contradicts [Simon et al.][0], which says it’s 2NaHCO3 +
2H2O -> 2NaOH + 2CO2 + O2 + 2H2, splitting twice as much water, but I
guess you could totally have some arbitrary number of hydroxyl anions
additionally traveling in the opposite direction through the
cation-exchange membrane and thus totally split twice as much water,
or ten times as much.  Or maybe I miscalculated something above?

[0]: https://core.ac.uk/download/pdf/36998552.pdf "Sodium hydroxide production from sodium carbonate and bicarbonate solutions using membrane electrolysis: A feasibility study solutions using membrane electrolysis: A feasibility study, 02014, https://ro.uow.edu.au/eispapers/2129"

Anyway, so for glass ECM in this context you would have a tiny little
“chlor-alkali” sodium bicarbonate cell whose cathode is a metal tube,
like a hypodermic, nearly pressed up against the glass.  Hot water is
being pumped through the tube through a membrane, behind which you
have a tiny pressure chamber, made of an insulator, full of
ridiculously positively charged water.  The water is pumped into it
from where it’s bubbling out oxygen and carbon dioxide after the anode
destroys bicarbonate ions and gives the water that strong positive
charge.  The cathode neutralizes this positive charge and produces
hydroxyl ions and hydrogen gas, which then come out its tip tens of
microns away from the glass.  After the alkaline water impinges on the
glass it spreads out into a rapid current of some kind of buffer or
acid, which neutralizes it and keeps it from corroding the rest of the
glass.  Maybe the acid is also produced by a similar kind of
electrolytic cell, from sodium sulfate or something, so you don’t need
an acid reservoir.  Maybe even the same electrolytic cell.

Now, how plausible is this?  I was originally thinking it would
require a totally implausible degree of macroscopic charge separation,
with unrealistically large coulombic forces from the highly charged
water on nearby objects.  But of course the reason water is a good
solvent for things like sodium ions is precisely that it solvates them
with its high permittivity, screening all but a tiny amount of their
electric field.  And nickel, at least, can withstand contact with hot
caustic solutions.  You might need to supplement the needle cathode
with a high-surface-area reticulated non-graphitizable carbon
electrode, and build the anode in the same way, to get high enough
current.  You might need to use a high overvoltage and thus get poor
current efficiency.  But it seems clearly feasible.

What if you ditch all the complicated plumbing and just immerse the
glass in the hot sodium bicarbonate solution or whatever, and for your
cathode use a solid metal needle insulated except for the tip?  What
happens if you pump a pulse of electrons into the cathode?  Won’t they
produce hydroxyls that attract more Na+ to the area and enable it to
etch the glass there?  Won’t they repel HCO3- ions from the area?

Well, I don’t know.  Maybe?  It seems like it ought to work.

We might be talking about microscopic effects, though; [some
researchers ran some experiments on glass recycling in 02010][1] and
it took them about 15 days to dissolve 25% of their glass samples,
pulverized to 250-800 microns, in 1-molar NaOH at 70°.  KOH was
somewhat less effective, 5-M NaOH was slightly more effective, using a
solution at only 50° was much less effective, and smaller particles
sizes were significantly more effective, but overall we’re talking
about rates in the ballpark of 30 microns a day or 400 picometers per
second.

[1]: https://www.ceramics-silikaty.cz/2010/pdf/2010_03_235.pdf "Dissolution of Waste Glasses in High Alkaline Solutions, Kouassi, Andji, Bonnet, Rossignol, 02010"

Yet I’ve seen [demonstrations of dissolving silica gel in 30% aqueous
NaOH][2] that converted amorphous silica gel to sodium silicate in a
few hours.  The silica gel in question didn’t have any alkaline earth
elements in it, I suppose, which Kouassi et al. mentioned as a factor
that slowed dissolution for them.  And the demonstrations I’ve seen
where lye dissolved glass in seconds or minutes were with molten
anhydrous lye, not aqueous lye, which would be something like “25
molar” and is also at something like 350° instead of 70° or 100°.

[2]: https://www.youtube.com/watch?v=U1ZWJCuJAYA
