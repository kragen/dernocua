In Dercuano I listed a bunch of “jellybean” FETs in 02017, coming up
with this table:

    | PN           | Vds |    A |  ohms | Qg (nC) |   ¢ |   W | type       |
    |--------------+-----+------+-------+---------+-----+-----+------------|
    | 2N7000       |  60 |   .2 |   1.9 |       2 |  36 |  .4 |            |
    | 2N7002       |  60 | .115 |     7 |       2 |  38 |     |            |
    | IRF630       | 200 |    9 |    .4 |      45 |  86 |  75 |            |
    | IRF9630      | 200 |  6.5 |    .7 |      29 | 151 |  74 | P-chan     |
    | IRLI630G     | 200 |  6.2 |  .400 |      40 | 229 |  35 |            |
    | IRLML6344    |  30 |    5 |  .029 |     6.8 |  36 | 1.3 |            |
    | IRLML6402    |  20 |  3.7 |  .065 |      12 |  40 | 1.3 | P-chan     |
    | EPC2036      | 100 |    1 |  .065 |    .910 |  97 |     | GaN        |
    | SI3483CDV    |  30 |    8 |  .034 |    11.5 |  89 | 4.2 | P-chan     |
    | FQP27P06     |  60 |   27 |  .070 |      43 | 134 | 120 | P-chan     |
    | NTD4906N     |  30 |   54 | .0055 |      24 |     | 2.6 | obsolete   |
    | IRF7307      |  20 |  4.3 |  .140 |         |  83 |     | dual (P&N) |
    | BSS138       |  50 | .200 |   3.5 |         |  24 |     |            |
    | CPC3703CTR   |     |      |       |         |  70 |     | depletion  |
    | 2N5457       |  25 |  .01 |       |         | 230 |     | JFET       |
    | 2N5458       |  25 |  .01 |       |         | 230 |     | JFET       |
    | SiS410DN     |  20 |   35 | .0048 |      41 |  94 |  52 |            |
    | PSMN4R0-40YS |  40 |  100 | .0056 |      38 |  88 | 106 | holy shit  |
    | IRF540N      | 100 |   33 |  .044 |      71 | 145 | 130 | fuck       |
    | IRF9540N     | 100 |   23 |  .117 |     110 | 189 | 110 | P-chan     |
    | IRF9530      | 100 |   12 |  .300 |      38 | 138 |  88 | P-chan SyC |

One heinous Python expression later and we have them ranked by watts
per cent:

    >>> csv.writer(sys.stdout).writerows(sorted(
        ((float(v[1]) * float(v[2]) / float(v[5]), v[0], v[1], v[2], v[5])
        for v in [line.split('|')[1:] for line in t.strip().split('\n')]
        if v[1].strip() and v[5].strip()), reverse=True))
    45.45454545454545, PSMN4R0-40YS ,  40 ,  100 ,  88 
    22.75862068965517, IRF540N      , 100 ,   33 , 145 
    20.930232558139537, IRF630       , 200 ,    9 ,  86 
    12.16931216931217, IRF9540N     , 100 ,   23 , 189 
    12.08955223880597, FQP27P06     ,  60 ,   27 , 134 
    8.695652173913043, IRF9530      , 100 ,   12 , 138 
    8.609271523178808, IRF9630      , 200 ,  6.5 , 151 
    7.446808510638298, SiS410DN     ,  20 ,   35 ,  94 
    5.414847161572053, IRLI630G     , 200 ,  6.2 , 229 
    4.166666666666667, IRLML6344    ,  30 ,    5 ,  36 
    2.696629213483146, SI3483CDV    ,  30 ,    8 ,  89 
    1.85, IRLML6402    ,  20 ,  3.7 ,  40 
    1.036144578313253, IRF7307      ,  20 ,  4.3 ,  83 
    1.0309278350515463, EPC2036      , 100 ,    1 ,  97 
    0.4166666666666667, BSS138       ,  50 , .200 ,  24 
    0.3333333333333333, 2N7000       ,  60 ,   .2 ,  36 
    0.18157894736842106, 2N7002       ,  60 , .115 ,  38 
    0.0010869565217391304, 2N5458       ,  25 ,  .01 , 230 
    0.0010869565217391304, 2N5457       ,  25 ,  .01 , 230 

That is, in theory, the PSMN4R0-40YS (unavailable in Argentina) is
capable of switching 4000 watts on and off for just under 90¢, so it
can control 45 watts per cent, while the IRF540N and IRF630
(available, even listed on MercadoLibre for 80¢ and 65¢) are almost
half as good, switching respectively up to 3300 watts or 145¢ (02017
price!) and 1800 watts for 86¢.  I probably should have also listed
the popular IRFZ44N (55V, 49A, thus 2700W, 76¢ locally) or IRLZ44N
(55V, 47A, 87¢, thus 2600W, logic-level threshold).

Six of these monster transistors, plus the appropriate drive circuitry
to control them, give you a three-way H-bridge to control a
multi-horsepower “brushless” motor.  One may be sufficient for a
multi-kilowatt switchmode power supply, though maybe running off
Argentine 240VAC you’d want two or three in series.

And, for electrolysis they can potentially drive material removal or
deposition with jitter under 10 ns and pulse times of 100 ns or so.
(This is inferred from the IRF630 datasheet, which has apparently
renamed “HexFET” to “STripFET”: “typ.” 118.5 ns reverse recovery time,
5.6 ns turn-on delay time, 2.6 ns rise time, measured with 4.7 ohm
gate resistance and 10 V; oddly they don’t state t[d](off) so it must
be something terrible.)  For pulses, all of these MOSFETs support even
higher powers; the IRF630 is rated for only 9 A continuous, but 36 A
pulsed.

Of course you’d have to run the electrolysis through a step-down
transformer or SMPS if you wanted to deliver that kind of power in a
useful way; 3600 A at 2 V would be a lot more useful than 36 A at 200
V, which would mostly just heat up the water.  Such a transformer with
10MHz bandwidth might be hard to find.

The gate charge is “typ.” 12 nC, so delivering it in 10 ns would
require driving the MOSFET gate with 1200 mA, which is I guess why
MOSFET gate driver ICs and pulse transformers are so popular.  Getting
a 10-ns-rise-time edge through the rest of your circuit is also
doable, but nontrivial.

Suppose we *could* deliver 3600 A at 2 V for 100 ns.  That’s 0.72
millijoules of energy, a perfectly manageable amount for ordinary
circuits, and correspondingly 0.36 millicoulombs, or 2.2e15 electrons,
or 1.12e15 divalent cations, about 1.87 nanomoles; for copper that
works out to be 119 nanograms, and for iron 104 nanograms, assuming
perfect Faraday efficiency.  That’s about a 30-micron-diameter sphere
of either of these metals: visible, but barely.  (It would punch right
through aluminum foil, though.)

(In practice such high current densities would be prevented by the
formation of an insulating salt film on the surface.  Also 0.72
millijoules in 100 nanograms is 7200 kJ/kg, which is still plenty to
vaporize the metal.)

If an electrolytic cathode is flying over a flat metal substrate at 25
m/s, like in a laptop hard disk (but full of water), 100 ns is about
2.5 microns.  The 10-ns jitter guessed at above amounts to 250 nm of
imprecision.  If you were using this to record information, you might
encode 4 bits into the delay before each new pulse, with an average of
180 ns per pulse and rest, giving a data rate of 22 megabits per
second.

If you wanted to archive a 10 GiB ZIM file of English Wikipedia on
nickel foil this way, it might take an hour or so.  You might want to
reduce the current so you wouldn’t be gouging huge 20-micron-deep
craters in the surface of the metal that would be hard to tell apart;
130 mA for 100 ns would suffice to give you a hemispherical
1-micron-radius pit.  Spacing tracks 2.5 microns apart would give you
400 tracks per millimeter, and 4.5-micron-long pulse-and-rest cycles
would give you 889 bits per millimeter, so 2200 bits or 278 bytes per
square millimeter, so, all in all, you’d need 39 square meters of
nickel.

Consider instead the average material removal rate (or deposition
rate), supposing we can step down an average of 9 A at 200 V to 900 A
at 2 V; that’s about 4.7 millimoles per second, about 300 mg/s of
copper or 260 mg/s of iron, supposing divalent ions and 100% Faraday
efficiency in each case.  That’s about 1 kg per hour.

However, 10-ns precision at 300 mg/s means 3-nanogram precision in how
much material you remove.  If that’s spread over a square millimeter
at 9 g/cc, that’s an etching or electrodeposition precision of 0.3
nanometers, roughly one atom.  If we step down to the kind of
precision we need for optical systems of about 40 nm, that works out
to about a 90 micron by 90 micron area.

So if you were using such a transistor to control the low-precision
hogging-out phase of cutting a first-surface mirror, your kg/hour
hogging-out process would hit its limit at 40-nm Z precision per
90-micron-square area.  Of course, that assumes you’re using laser
interferometry or something for positional feedback of the electrode.

Then, by turning down the current for a finishing pass, you could
overcome that resolution limitation and get the mirror surface more
precise, still at the same bandwidth of a few tens of megabits per
second.

One of the more interesting devices that can be usefully controlled at
10 MHz or more is a piezoelectric actuator.  These don’t require a lot
of current but they do need relatively high voltages.
