As I was washing some dried pancake batter off a bowl, I realized that
there was a phase transition between the part of the batter that had
congealed into masses (stuck to the surface) and the part that hadn’t
and could simply be washed away with water.  I think this is the
percolation-threshold behavior that also governs the sol-gel phase
transition: once the particles of flour are close enough together on
average, instead of forming small agglomerations of particles, they
form a continuous network of particles.  The same thing happens in
paints at the critical pigment volume concentration (CPVC), and
similarly with latex paints when they’re diluted: if the drops in
latex or pigment particles in paint fail to form a continuous network,
they fall apart.

Naturally my mind ran to how this could be used for digital
fabrication.  This critical threshold is a point where a very small
change in composition provokes a phase change between a sol and a gel,
provoked, in the case of the pancake batter, by water evaporation.  If
you can provoke this change in the places you want to solidify, while
keeping the rest of a solution as a sol, you can then just rinse away
the sol to extract a green gel object, which can provide geometry for
further processing.  Until this point, the sol supports the gel
weightlessly, since they have essentially the same density.

The new insight here is that the gelation stimulus can be made
arbitrarily small to within the precision with which you can control
the state of the near-critical sol.

A wide variety of gelation stimuli can be used.

The conventional approach with stereolithography 3-D printing is to
use ultraviolet lasers or spatially modulated ultraviolet illumination
through an LCD to produce free radicals, which locally initiate
polymerization.  Two-photon polymerization, where the number of free
radicals produced is proportional to the square of the light intensity
rather than directly to the light intensity because two photons are
needed to initiate the reaction, is becoming popular.  Any of these
approaches can be used; the benefit of the near-critical sol is
primarily in reducing the needed amount of light.

The spatially controlled addition of small amounts of material is
another possibility, either a catalyst or a limiting reagent; this can
be done either at the surface of a sol bath, similar to powder-bed
printing, or throughout its volume with one or more movable nozzles,
similar to FDM printing, though this poses the risk of the gelated
material sticking to the nozzle instead of the workpiece.
Electrolysis is one appealing way to locally deposit some ions, and
electrolysis can also be used to initiate other reactions.

Worth special mention here is the possibility of using inkjet nozzles
or gas jets scanned over the surface of a bath in order to precisely
deposit the reagent.

Related to electrolysis, but different, is the possibility of plasma
activation, where corona discharge around sharp points is used to
stimulate some points on the surface of the sol but not others.

Another possibility is locally altering the temperature, either down
(with a gas jet) or up (with a gas jet, flame, plasma, or laser or
other light).  Almost any resin system that can will polymerize on its
own in enough time, such as commercial casting polyesters and epoxies,
can also be convinced to polymerize much more rapidly with some heat,
while a wide variety of bistable soluble gelling materials such as
agar-agar will gelate upon cooling to a critical gelation temperature,
but remain gelled up to a higher melting temperature.

If the sol has an extremely low vapor pressure, or an e-beam window
can be moved very close to it, local gelation with an electron beam is
also a possibility.  This potentially provides finer spatial
resolution than visible light.

In an upside-down printing vat like those used for LCD UV
stereolithography resin polymerization printers, another possibility
is to electrostimulate the bottom of the resin capacitively, for
example by pushbroom-scanning a line of electrodes across the bottom
of the vat, outside the protective membrane, while modulating an RF
signal onto the electrodes.  This would at least locally heat it up,
which is enough to have the desired effect, but maybe even resistive
heating through the membrane would be enough.

By substituting a cathode-ray tube for the vat-bottom membrane, it’s
possible to stimulate the sol with light, X-rays, heat, or electron
beams that pass through the glass.  Ion beams can be substituted for
electron beams, with the usual tradeoffs.  Ideally the gel would
polymerize a slight distance away from the glass to avoid mechanical
forces on the glass; this would be least infeasible with the
electron-beam approach.

The sol can be formulated with a wide variety of functional fillers
which, among other things, reduce the amount of material that needs to
be gelled to form a continuous network.

The above gelation stimuli can also be used without the sol, of
course, as they are in conventional stereolithography.
