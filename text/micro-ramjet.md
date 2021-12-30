Most of the fuel of a rocket is its oxidizer.  For the air, ramjets
are an appealing alternative: just carry the reducer, squirt it into a
combustion chamber, and let the hot compressed incoming air maintain
the combustion!

The autoignition temperature of heptane is 223°, and it’s nearly as
energy-dense as diesel or regular jet fuel: [gasoline is 34 MJ/l
versus diesel’s 39 or kerosene’s 35][0].  So if the incoming air can
get over 250° or so, a bit less than doubling its input temperature,
we’re golden; from there it’s just a matter of adding the heptane or
whatever gradually enough to avoid cooling the air below ignition
temperature.

[0]: https://en.wikipedia.org/wiki/Energy_density#In_chemical_reactions_(oxidation)

How much compression does that need?  For an ideal gas, *PV* = *nRT*;
in an isothermal process, where *nRT* is constant, *PV* = some
constant *C*.  So the short answer is that we need to double *PV*.
But when we increase *P*, *V* decreases.  By how much?

Well, in [adiabiatic heating and cooling][1], *PV<sup>n</sup>* = *C*,
where *n* is the adiabatic index, 7/5 for diatomic gases.  So, I
guess, if the volume is cut in half, then the pressure needs to
increase by a compensating factor of 2<sup>7/5</sup> = 2.64, which
means that the product *PV* and therefore the temperature increased by
32% (2<sup>2/5</sup> = 1.32).  So to double the temperature we need to
decrease the volume by 2<sup>5/2</sup> = 5.66, which will increase the
pressure by 5.66<sup>7/5</sup> = 11.314, and 11.314/5.66 = 1.999.

(I had to write 24 lines of Python to figure that out.)

[1]: https://en.wikipedia.org/wiki/Adiabatic_heating#Adiabatic_heating_and_cooling

So we need about 11 atmospheres of pressure on the front of the ram in
order to run the jet.  How fast is that?

As I understand it, in [isentropic compressible flow, the stagnation
pressure][2] is (1 + ½(*n*-1)*M*²)<sup>(*n*/(*n*-1))</sup> times the
static pressure of the surrounding air, at Mach *M*.  Here *n* is 7/5,
*n*-1 is 2/5, *n*/(*n*-1) is thus 7/2, so this simplifies to (1 +
*M*²/5)<sup>7/2</sup>.  So, to get 11 times higher stagnation
pressure:

> 11 = (1 + *M*²/5)<sup>7/2</sup>  
> 11<sup>2/7</sup> = 1 + *M*²/5  
> 5(11<sup>2/7</sup> - 1) = *M*²  
> *M* = (5(11<sup>2/7</sup> - 1))<sup>½</sup>  

This works out to be about Mach 2.22, about 760 m/s at sea level, if
I’ve calculated everything correctly.  But I suspect that it isn’t
correct because Wikipedia talks about [subsonic ramjets][3], and they
surely aren’t using fuel that ignites at a much lower temperature than
heptane, right?  Indeed, WP says that they’ve been run as low as 45
m/s, but need to run at at least Mach 0.5 to be self-sustaining.

[2]: https://en.wikipedia.org/wiki/Stagnation_pressure#Compressible_flow
[3]: https://en.wikipedia.org/wiki/Ramjet

A crucial thing here is that the stagnation pressure and thus the
stagnation temperature doesn’t depend on the scale or shape of the
ramjet in any way; it’s the same for a millimeter-wide ramjet or a
kilometer-wide ramjet.  I’m not sure if that’s part of my error,
though.  The ideal-gas assumptions break down in the transonic region,
as I understand it, but I don’t think that’s my problem.
