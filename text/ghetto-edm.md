In theory you could cut any shape into steel, tungsten carbide, or
diamond by electroerosion with nothing more than the tip of a copper
wire or graphite point, a cup of diesel fuel, a capacitor or inductor
sufficient to power an arc, and some way to supply power to it
(originally, in 01943, a resistor).  All you have to do is touch the
wire to the steel (or other workpiece) wherever you don’t want steel,
and stir the dielectric around to sweep away the swarf.  The trouble
is just knowing where the cutting tip is, where steel is, and also
that it’s a slow process.

Nowadays you should be able to use the cutting tip itself to probe
where the steel is, at least relative to the tip; a secondary tip
operated at lower voltage and therefore not suffering from sparking
can be used for touch-off to correct for tip wear.  This should enable
you to get an accurate picture of where the workpiece is and what
remains to be cut, as well as the cutting rate of the spark
parameters.

This kind of feedback should permit much higher material removal rates
than are typical for wire EDM or die-sink EDM, because the feedback
system compensates for the tool-electrode wear, permitting the use of
much more aggressive sparks like those used in tap-burning EDM
equipment.

To the extent that you can use a hollow needle electrode with
dielectric squirting through it, you should be able to get higher
cutting rates due to better swarf clearance.

Diesel fuel is cheaper than kerosene, lamp oil, vegetable oil,
transformer oil, or laxative mineral oil, although any of these would
also work, and these oils are much easier to keep in a dielectric
state than water, which is very sensitive to slight amounts of ionic
contamination.  The oils only need to be circulated and have
particulates strained out of them.  Machines using water, even plain
tap water, seem to have higher MRRs in practice, but I don’t know why.

One inventor creating unorthodox devices in his shed [reported success
with die-sink EDM with an RC circuit](https://youtu.be/MZm-mvxa2qo)
with a 60V supply and a 400V electrolytic 100μF capacitor switched at
5kHz and a 10% duty cycle with an IRF IRG4PC40S IGBT.  For his
resistor he used a cartridge heater of “a few ohms”.  He used a water
dielectric and got an MRR on aluminum of 18 mm³/minute (a 3-mm hole
through a 1-mm aluminum sheet in 23 seconds) or 310 nl/s, and his
brass tool electrode had visible pitting after even this brief use.
This works out to a maximum of about 400 mJ per spark and
theoretically up to about 1800 watts, but I suspect that in practice
the power was much lower because he was getting more like 50 sparks
per second than 5000.

Later he added an aquarium pump to recirculate the water through a
paper coffee filter, switched to a lower-ESR 300V 160μF electrolytic,
and added a servomechanism which simply feeds the electrode down when
the current spikes of the sparks didn’t reach a preset set point.  At
times, his aquarium-pump setup squirts water *onto* the cut rather
than immersing the whole apparatus in water.  With an additional patch
to lift the electrode periodically to improve flushing, he was able to
cut steel.

[Another machinist](https://youtu.be/kRc1NFO8uwo) reported similar
success on aluminum, but used a tubular brass “die” tool electrode to
cut his round hole.  [A third amateur](https://youtu.be/6Jt08F1HOiU)
used diesel fuel as his dielectric and reported very slow cutting on
steel, limiting his current with the series resistance of a
quartz-halogen worklight at 120VDC.

[A much simpler approach](https://youtu.be/fRPmSgfIJqY) uses the
traditional solenoid buzzer circuit, with the sparking contacts being
the workpiece and tool and the solenoid itself holding the energy of
the spark, powered from merely 24VDC 1.8A.  Thus the servo,
energy-storage, and feed mechanisms are all provided by a single
simple mechanism.  He reported extremely slow cutting and applied a
light oil dielectric occasionally by hand; I think it was slow because
his cut was getting filled up with swarf.

[A review of a Luoyang Xincheng SFX-4000B tap
remover](https://www.youtube.com/watch?v=_u2JJ-Mx6_Y) reported burning
through a 50-mm-long broken tap in 8 minutes with about 10 amps at
about 40 volts (average, not peak), using a brass electrode in tap
water.  My best guess is that it was making a 2 mm cut through a 4 mm
wide tap flute, so about 400 mm³, or 50 mm³/minute.  The wear on the
brass tool electrode was visually about 15% of the wear on the
hardened steel workpiece.
