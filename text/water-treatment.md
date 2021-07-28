Posted at <https://news.ycombinator.com/item?id=27763602>

(I should preface this by saying that, unlike you, I have no real water disinfection expertise, so I may be overlooking significant fundamentals in what follows.)

Those costs sound reasonable for niche uses (though I do think they would prevent it from "revolutionizing water disinfection technologies" as they claim in the Conclusions), and being able to operate in practical terms at a very small scale seems to me like an advantage rather than a disadvantage.  It clearly is more expensive than conventional water treatment and would have difficulty scaling to replace it for reasons of material availability.  Other alternative very-small-scale disinfection approaches are probably cheaper than their process in its current form; they mention ozonation, UV irradiation with germicidal lamps, photocatalytic disinfection, and the Fenton process in the paper and supplement.

I don't see how the square-cube law plays into it; the reason they're supporting the catalyst on rutile (anatase?) instead of just using solid bars of metal alloy is precisely to ensure neat linear scaling, and the reason it's 1% metal instead of 0.1% or 0.001% is that the rutile is in the form of 1–100 nm particles.  (See p. 8/12 in the article and Fig. 4 on p. 7/12).  The only square-cube thing that occurs to me is that a large ice bath requires much less ice input than a small ice bath, but that favors scaling the process up, not down.

A couple of other points:

⓪ Your calculations seem to be correct.

① People's drinking water needs are lower than you suggest by a factor of about 65, although conventional surface-water treatment plants cannot take advantage of this.

② You're not taking into account the supply-chain issues that plague smaller-scale treatment facilities.

③ The cost of consumables that this process would eliminate would still be lower than the cost of the catalyst.

④ There are plausible ways the process might be improved that could make it economic.

Thanks to mkr-hn I found the paper at https://www.researchgate.net/publication/352882305_A_residue-free_approach_to_water_disinfection_using_catalytic_in_situ_generation_of_reactive_oxygen_species; the canonical paper link (unforgivably missing from the original press release) is https://www.nature.com/articles/s41929-021-00642-w, and the supplementary material is at https://static-content.springer.com/esm/art%3A10.1038%2Fs41929-021-00642-w/MediaObjects/41929_2021_642_MOESM1_ESM.pdf.

— ⁂ —

⓪ Scaling calculations.

Here are the calculations in more detail, since I misread yours badly at least twice.

You say 0.5 MGD is 6.5 million times higher than the 0.2 mℓ/min (3.3 μℓ/s) in the experiment.  0.5 MGD is 21.9 ℓ/s, which is 6.6 million times higher than 3.3 μℓ/s.

I think you are reading it correctly; they do say their catalyst is 0.5% Au and 0.5% Pd on a TiO₂ support: 0.6 mg of gold and 0.6 mg of palladium to process 0.2 mℓ/min of water.  The supplementary material has a plot of different catalyst mixes they tried (Sup. Fig. 14, p. 12, 13/32).

If we normalize that amount of catalyst metal to SI units, that's 180 gram seconds per liter (g·s/ℓ) each of gold and palladium.  Your 0.5 MGD (22 ℓ/s) for 5000 people is 4.4 mℓ/s per person, which works out to 790 mg per person each of gold and palladium.  Palladium at US$2800 per troy ounce (https://www.kitco.com/charts/livepalladium.html — that *is* per troy ounce, isn't it?) is US$90/g.  Gold at US$1800 per troy ounce is US$58/g.  Multiplying it out, that's US$71 of palladium per person and US$46 of gold per person, for a total of US$117 of catalyst metals per person.  This seems likely to be the dominant cost of the whole shebang at anything larger than laboratory scale; the actual preparation of the catalyst with these metals by the process they reported in the paper might be even more expensive, but presumably cheaper methods are possible.

The 5000-person 0.5 mgd plant you cite as an example would need 3.9 kg of gold (US$230k) and of palladium (US$350k) for its catalysts, a total of US$580k, which is the number you gave for "our small plant".

790 mg of gold per person, times 7.7 billion people, would be about 6100 tonnes, about 3% of all the 200 000 tonnes of gold that has been mined so far.  However, the corresponding 6100 tonnes of palladium would vastly exceed the above-ground stocks of palladium, estimated at 4.5 "moz", which I think means "million troy ounces", or 140 tonnes.

However, they also tried 1% gold without any palladium, and although this produced lower H₂O₂ concentrations, they were still high enough to be somewhat effective (≈80 ppm rather than 220 ppm, resulting in a 1.6 log₁₀ reduction rather than the 8.1 they were so satisfied with).  So in the face of resource limits you could trade off a larger amount of gold and a longer residence time against scarce palladium.

① Potable water needs are 5.7 ℓ/day/person, not 380.

Your figure of 4.4 mℓ/s/person is 380 liters per day per person (100 gallons per day per person), but Burning Man recommends *1.5* gallons per day per person (5.7 liters/day/person, 0.066 mℓ/s/person), which includes water for showers, for cooking, and for drinking in a very dry environment with extensive physical exertion, though not for bidets.  My experience at Burning Man is that you can get by on less.

That's 67 times less water than your figure.

Maybe your waterworks is supplying not only drinking water but also toilet-flushing water and lawn-irrigating water?  Those don't normally need antibacterial treatment.  Even the 0.2 mℓ/min benchtop catalyst they used in the paper (containing 5.4¢ of palladium and 3.5¢ of gold) would supply 0.29 liters per day; it would only need to be scaled up by a factor of 20 (to 12 mg gold (US$0.69) 12 mg palladium (US$1.10), 2.4 g rutile) to supply the requisite 5.7 liters per day per person.

② Supply-chain issues with consumables.

This is mentioned in the Conclusions section of the paper.

Conventional surface-water treatment facilities involve treatment with hypochlorite, permanganate, chloramine, and whatnot.  These pose some safety concerns (especially at small scales) and in many places are subject to legal reporting requirements.  Occasionally there are industrial accidents because a truck driver pumped ammonia into the hypochlorite tank or vice versa; when people try to use the same materials at the household scale, sometimes you get medical problems because somebody put 1000 ppm of hypochlorite into their drinking water instead of 3 ppm.  And, especially for individual households in middle-income and poor countries, there are often supply-chain issues with these materials; sometimes shipments don't arrive, or the household doesn't have enough money to buy a new bottle of bleach when they run out, or the products are falsely labeled, or have degraded before delivery—a particular problem with sodium hypochlorite.

For example, the cleaning-products store down the street from me here in Argentina advertises that they sell "100% chlorine", which I found pretty alarming until I saw that they are unpressurized bottles of liquid, not pressurized gas cylinders.  Probably it's mostly aqueous sodium hypochlorite, but who the hell knows what the concentration is, and what else they put in it?  The supermarket has jugs of sodium hypochlorite solution stabilized with sodium hydroxide, and the label tells you the nominal concentration (usually 66 g Cl/ℓ) but of course the bottles aren't hermetically sealed, may be exposed to sunlight, and may not have been properly quality-controlled at the factory in the first place.

If you're running an 0.5 mgd water treatment plant, you can presumably just *measure* the concentration in your hypochlorite tank, and have someone assigned to do this.  And since they replaced the water main last year, we finally do have a reliable water supply 24/7, instead of only at night when the neighbors aren't pumping so much water.  Still, the water from the mains has to be pumped up to the rooftop tank, where the chlorine concentration falls before we use it; maybe the water plant is putting way too much chlorine in the water to compensate for that, because it smells pretty strongly of bleach when it comes out of the tap.

If, by contrast, you have a durable catalyst that fulfills the same microbicidal function without needing constant reliable shipments of bleach, all of these concerns go away.  It's like the difference between photovoltaic panels and the electric grid: even if a reliable electric grid might give you energy at a lower cost than having your own solar panels, that doesn't help if you don't have a reliable electric grid.  It might be worth spending US$10-US$200 per person for an autonomous germicidal appliance; it might be cheaper than a refrigerator or washing machine.

③ Consumables costs.

That brings us to the question of consumables costs.  Obviously enough, I've never operated a waterworks, but for example Callie Sue Rogers's 02008 B.S. thesis on conventional surface-water treatment plants https://core.ac.uk/download/pdf/4276743.pdf has a table surveying a number of Texas "conventional surface-water treatment facilities", concluding that they spend between US$20.21 and US$286.14 per million gallons on "chemical costs", depending on the condition of the water they're starting with; I infer "chemical costs" means things like the oxidants mentioned above, flocculants, and precipitants; this works out to 5.3 to 76 microdollars per liter.  She estimates that the total production cost ranges from US$0.31/1000 gallons for small 5 mgd plants down to US$0.13/1000 gallons for larger 130 mgd plants (respectively 81 and 34 microdollars per liter).

The US$120/person figure (US$120 per 100 gallons per day) would be 10400 microdollars per liter if the catalyst only lasted a month, 870 microdollars per liter if it lasts a year, 170 microdollars per liter if it lasts 5 years, or 43 microdollars per liter if it lasts 20 years.  It seems almost certain to exceed the cost of buying the necessary oxidants on the open market, particularly on a time-discounted basis.

How long would the catalyst last in practice? The catalyst materials in question are pretty darn inert, so you could probably clean them (with acids and/or alkali) if they get poisoned by some kind of inorganic contaminants in your incoming water.  Organic fouling won't be a concern, and organic catalyst poisons would just get chewed up by the H₂O₂.  You have to use cleaning agents that aren't so aggressive that they can corrode the porous rutile support, but I think that requires something like hot concentrated sulfuric acid.

Of course, such cleaning might cut into the supply-chain-autonomy advantage a bit.  But it might not be necessary at all; this isn't a car catalytic converter, after all, and it's constantly washed with fresh water.

What about the energy cost?  Maintaining a 2° ice bath is pretty cheap, but 10 bars (1 MPa, 145 psi) of pressure doesn't come for free.  It costs 1kJ/ℓ (a simple unit conversion).  Your 380 liters a day per person would be 4.4 watts.  At US$20/MWh this is US$0.77 per year of energy per person, probably in practical terms more like US$3 per year once you take into account the inefficiencies of electric motors and pumps.  This is small but not insignificant compared to the cost of the catalyst.  But it's still a low enough energy cost that you could hand-crank the pump.

④ Process improvements.

So this is an economically feasible way to provide the 5.7 liters per day of potable water a person needs, even if existing alternative processes are cheaper.  What are the prospects for improving the process further?

The key findings of this paper, as I read it, are that this catalytic process is resilient to common solutes, and that the witches' brew of reactive oxygen species produced in this process is more effective than commercially purchased H₂O₂—they say by a factor of 10⁷, but in Supplementary Table 2 (p. 18, 19/32) I see log₁₀ reduction of CFU/mℓ going from 0.44 to 0.98 (3.5×), from 0.64 to 1.25 (4×), from 0.96 to 1.18 (1.7×), and from 0.84 to 1.48 (4.4×), so I have no idea where 10⁷ comes from.

Process intensification is one possibility for making it economic; it's quite plausible that the use of higher pressures or additional alloying elements in the catalyst could increase reaction rates by an order of magnitude or more, and it's possible that heating the water after catalytic ROS production (by running it through a countercurrent heat exchanger into a hot tank) would enable even lower concentrations of ROS to disinfect effectively.  (Normally you'd also consider heating the catalyst, too, but presumably the ice bath is necessary to push the equilibrium toward high concentrations of H₂O₂ and other ROS.)  Applying light or a voltage to the catalyst are other possible routes to increased free radical production.

Another possibility is lowering the cost of the catalyst; metal-oxide, metal-(other-)chalcogenide, intermetallic, and even transition-metal catalyst systems might work adequately through the same route, and could be much cheaper even if the catalyst leaches at an appreciable rate.

After all, what use is a newborn baby?
