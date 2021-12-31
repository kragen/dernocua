It occurred to me that a back-biased red or green LED or base-emitter
junction might make an interesting substitute for a spark gap in a
tiny Marx generator.  These often break down in avalanche mode with
minimal or no damage to the semiconductor, often at voltages under
10 volts.  So you could easily produce a pulse train at 100 volts or
more, perhaps from a 5-volt source using only tiny surface-mount
components.  This led me to dig a bit into the existing literature on
similar devices.

Possible characteristics of such semiconductor-switched Marx generators
-----------------------------------------------------------------------

The average achievable power of the device probably will not be large,
since especially base-emitter junctions are not optimized for power
dissipation, and, according to folklore, high-power LEDs generally do
not tolerate avalanche breakdown well.  Moreover, the properties the
device relies on here (avalanche energy tolerance, reverse breakdown
voltage) are not among the properties the manufacturer normally
specifies, except I guess on JFETs.  But JFETs are tiny high-precision
devices, so JFET gate junctions are probably even worse for this
application.

I suspect that, at least with silicon, you won’t get a good avalanche
effect until 7 volts or more; below that, the less abrupt Zener effect
will dominate.  Purpose-built “zener” avalanche diodes might also
work, but since they’re sold as voltage references, they might be
designed to spike as little as possible — the spikes we’re after here
are troublesome noise in voltage-reference applications.  At least
you’d have a well-characterized and optimized power rating.  And of
course diacs would definitely work and have been used in production
Marx generators in the past.  (Can you get MOS latchup out of power
MOSFETs?  Probably not.)

Looking at file `pick-and-place.md`, I see that 5% 1k resistors
occupying half an 0402-equivalent cost 0.385¢ soldered (and a few
other values are available); discrete 1% 0402s are 0.305¢ in a wide
variety of sizes; 0402 MLCCs are 0.4¢, while 1206 MLCCs are 1.3¢; NPN
S9013 transistors are 1.58¢ and MMBT3904 is 1.32¢; red 0805 LEDs are
1.54¢; zeners only come in 5.6V and 3.3V and cost 1.35¢; 5.8V TVSs
cost 2.91¢.  Each Marx stage requires an avalanche element, a cap, and
two resistors, so maybe an MMBT3904 (3 mm × 3 mm?), an 0402 cap (1 mm
× ½ mm), and two 0402 resistors, for a total of 2.33¢ and 10½ mm²,
probably 25 mm² in practice.

A particularly interesting question is how fast the device completes
its avalanche discharge and recovers (through recombination of the
freed-up charge carriers).  It wouldn’t surprise me to find a
transistor was capable of producing higher frequencies in this
avalanche-diode mode than when being used as a real transistor.  But
are we talking about potential pulse repetition rates of 10 kHz,
100 kHz, 1 MHz, 10 MHz, 100 MHz, 1 GHz, 10 GHz?  How high do the
harmonics go?  I’m guessing that they’re much faster than a
corona-stabilized spark gap (≈20 kHz repetition rate) but I don’t know
how much.  Even high-voltage SCRs typically manage 10 kHz.

Possible applications
---------------------

- Pulsed power for operating LEDs at higher power without time for
  thermal runaway through current hogging.  Probably very inefficient.
- Neuron-style spike-train computation, in which a stimulus pulse can
  produce a much larger (synchronized) response pulse if the “neuron”
  is currently charged up enough — so you get implicit addition of
  spikes that arrive nearby in time;
- Phase-locked spike-train computation (a [technique published in a
  blog comment by Pete Castagna in 02016 and probably long
  before][25]), in which a “clock” spike train defines 2–5 phases at
  which “slave” oscillators can run; depending on their charging rate,
  their phase can be advanced by feeding them one or more additional
  stimulus pulses at the right time.  Although the hardware is
  different, higher-level logic design out of such devices might be
  similar to the bistable elements described in file
  `snap-logic-ii.md` and in my Derctuo note about “majority DRAM
  logic”.
- There’s no need for all the slaves to have the same period; this
  would result in nonstop phase displacement among them.  Three slaves
  of periods 3, 4, and 5 produce a period-60 counter, spiking at the
  same time once every 60 clock spikes.
- Low-jitter pulse amplification for trigger pulses for larger devices.
- RF signal generation, either for UWB communication and ranging, or
  to produce a crude high-voltage VCO (CCO?) that can then be filtered
  to a band of interest.  Because the time-domain comb signal from an
  idealized free-running Marx includes equal amounts of all harmonics
  (dc, f, 2f, 3f, etc.) the actual frequency of interest may be far
  above the spike frequency.
- If you drive two divide-by-2 slave generators from the same master
  clock, then the *difference* between them will only contain the odd
  harmonics of the slave frequency: f, 3f, 5f, etc., notably excluding
  dc.
- Pulse density modulation, in which the device is either triggered or
  not triggered every microsecond or so.  This is appealing not only
  because of power gain (which it might or might not provide) but also
  because of the potential for driving high-impedance analog loads
  like piezoelectrics.
- RF demodulation: by keeping the Marx generator charged to the
  instantaneous voltage of a poorly filtered radio signal, then
  reliably triggering it with a “sampling-comb” pulse train at some
  harmonic of the desired frequency (say, 2×, 3×, or 4×), you will
  selectively amplify the subharmonics of the pulse-train frequency,
  effectively multiplying it by a sampling comb in the time domain,
  and therefore convolving it with a comb in the frequency domain,
  converting every subharmonic of the sampling frequency to baseband.
  For this application, the Marx generator itself is a somewhat
  suboptimal many-pole RC low-pass filter, which should mitigate the
  aliasing problem.  This requires avalanche times an order of
  magnitude or more above the frequency of interest.  Honestly a
  regular S&H is probably a lot better for this unless you can’t get a
  fast enough transistor.
- Polyphase analog filtering: by running multiple slave oscillators at
  the same period and different phase shifts, you can generate spike
  trains to multiple different analog samplers.
- Similarly for CDMA-type time-domain communication applications,
  where instead of “sampling” at regular intervals, you sample at
  times pooped out by an LFSR or something.  If you have two such
  sampling devices, each powering an integrator (or one charging an
  integrating cap and one discharging it), you ought to be able to
  decode your signal of interest from the difference.  This of course
  requires extreme temporal synchronization, but that might be doable
  in a simple PLLish way, letting the sequence generator run free at a
  slightly wrong speed until it detects a signal, and then running two
  detectors off it at a slight delay to get the phase error to drive
  the PLL.
- Powering a Cockcroft–Walton generator, for example, to fire a xenon
  strobe lamp on a camera.
- RF switching: if the capacitors in the Marx are reverse-biased
  diodes, their capacitance goes down and their impedance goes up as
  they charge up.  Every time you erect the Marx, they will discharge
  and briefly be low impedance to RF signals, before charging up
  again.  This potentially allows you to sample more than just a point
  on a signal.  It probably requires inductors on the avalanche
  elements in order to slow the edge and remove interference it would
  otherwise create in the band of interest, plus of course bias tees
  to couple the RF signal in and out.
- Generating magnetic pulses for magnetoforming, for example, aluminum
  foil.

[25]: http://dangerousprototypes.com/blog/2013/07/20/avalanche-pulse-generator-and-some-scope-porn/#comment-5451593

One particularly amusing hackish thought: the avalanche elements can
be back-biased diodes, the capacitors can be beefier back-biased
diodes, and the charging speed limiters could also maybe be tiny
diodes instead of resistors, though that’s a trickier proposition;
this would enable you to do digital logic entirely out of diodes!  If
it’s possible, and fast, this seems like it would have been a killer
advantage in the 01950s and early 01960s, when transistors were
expensive and hard to get, and vacuum tubes more so; some Russian
electronics were “ferrite/diode” systems in which the diodes took care
of the combinational logic and (square-loop?) ferrite transformers
handled memory and inversion.

When I was 9, I proposed solid-state switching elements for
computation that worked on the neon-lamp-like principle of avalanche
breakdown in ionic solids.  Those are not practical, because the
device would require very high voltages, and its crystal structure
would rapidly lose integrity (almost certainly, anyway).  But
avalanche discharge in solid-state semiconductors is commonplace; it’s
the way diacs, triacs, and other thyristors and SCRs work.

Notes on other people’s work
----------------------------

### Kerry Wong’s minimal 2N3904 pulse generator ###

[Kerry Wong built a 2N3904-based pulse generator][1], running it off
120V (!!) and back-biasing the *collector*—base junction, which he
says consistently avalanches around 100V, saying:

> Avalanche transistors can be used to generate fast rise time
> pulses. Their usage in the hobby world was made popular following an
> application note ([Linear] AN72 [2] [now at Analog[9]]) by Jim
> Williams and was further publicized via [this EEVBlog video][3]. ...
> 
> R2, C1 along with the NPN transistor form a relaxation oscillator.
> The capacitor gets charged via R2 and then rapidly discharges when
> the collector-emitter voltage reaches the avalanche voltage.  The
> discharge current flows through R1 during the avalanche and forms a
> fast-rise pulse between ground and the emitter.  The choice of R2
> and C1 is pretty liberal.  In general, C1 can range from a few pF’s
> to tens of pF’s and R2 can range from 100K to 1M.  The larger the
> value of C1, the wider the avalanche pulses due to increased
> discharging RC (R1C1) constant.  But C1 cannot be too large as the
> energy released during the short avalanche period could cause the PN
> junction to fail.  The RC constant (R2C1) determines the operation
> frequency.  For the values given [220kΩ and 22pF], the pulsing
> frequency is at roughly 30 kHz.  R1 is chosen to match the
> characteristic impedance of the load. ...
> 
> During my build process, I sampled a large batch of 2N3904’s, and
> found that most can avalanche pretty consistently at around 100V. ...
> 
> ...The following picture shows the same pulse observed on a
> Tektronix 2445 (150MHz bandwidth) with matching input impedance. The
> measured rise time is around 1.5 ns which corresponds to a bandwidth
> of approximately 230 Mhz [0.35/Tᵣ].

[1]: http://www.kerrywong.com/2013/05/18/avalanche-pulse-generator-build-using-2n3904/
[2]: http://cds.linear.com/docs/en/application-note/an72f.pdf "A Seven Nanosecond Comparator for Single Supply Operation (broken link)"
[3]: http://www.eevblog.com/2012/07/06/eevblog-306-jim-williams-pulse-generator/ "EEVBlog #306"
[9]: https://www.analog.com/media/en/technical-documentation/application-notes/an72f.pdf "A Seven Nanosecond Comparator for Single Supply Operation, by Jim Williams, 01998, 44 pp."

His pulses look like only 50 volts, though, suggesting that they might
actually be much faster than 1.5 ns, and being limited by the
oscilloscope’s 150MHz input bandwidth.  Oddly, log(120V/100V)/(220kΩ
22pF) works out to about 16 kHz, not 30 kHz.

Using the huge collector-base junction instead of the teensy
emitter-base junction probably means you can handle a lot more power,
and it is at least a somewhat controlled process parameter, since
people actually do often require that their transistors resist a back
bias on the base-collector junction; [ST’s 2N3904 datasheet][5]
specifies a minimum of 60 V for the base-collector reverse breakdown
and, surprisingly, provides a minimum value for the base-emitter
reverse breakdown voltage as well: 6 V.  Interestingly, its delay time
and rise time (for normal transistor operation) are specced as 35 ns,
with 200 ns for storage time and 50 ns for fall time, and a 270 MHz
transition frequency.

This means that the pulse’s rise time is more than 20 times faster
than the pulse you’d get using the transistor *as* a transistor
*switch*, but maybe no faster or even a bit slower than if you were
using it in its linear region.  But probably the transistor is not the
limiting feature here.

[5]: https://www.sparkfun.com/datasheets/Components/2N3904.pdf

He also cites [a 01997 paper by Kilpelä and Kostamovaara][4] and [a
pulse generator project by Andrew Holme][6].

[4]: http://icecube.wisc.edu/~kitamura/NK/Flasher_Board/Useful/research/RSI02253.pdf "Laser pulser for a time-of-flight laser radar, by Ari Kilpelä and Juha Kostamovaara, Rev. Sci. Instrum. 68 (6), June 01997, p. 2253"

### Holme’s 2N3904 pulse generator ###

Holme used a 2N3904 and an open coax transmission line rather than a
22-pF cap to get a rectangular pulse with about a 400-ps rise time,
which he says is limited by his oscilloscope.  Astonishingly, he did
this with through-hole components.

The coax transmission line suggests how to get arbitrarily high gain
from such a circuit, considered as an amplifier: an arbitrarily short
input pulse can produce an arbitrarily long output pulse, as long as
the current is high enough to maintain the avalanche but not high
enough to overheat the transistor.  (I think you can do this with a
capacitor too — it’s just messier.)

Holme mentions that you can trigger the circuit by applying short
pulses to the base, which is a thing I hadn’t thought of; both Wong
and Holme are taking their main signal from the emitter and just tying
the base to ground through a big resistor.  I suppose that you’d pull
the base *negative* to trigger it in that case, thus increasing
|V<sub>CB</sub>| enough to cause an avalanche — just treating the
transistor as a pair of back-to-back diodes?  (This is wrong; see
below.)

Holme also cites Jim Williams’s Linear AN72 and [AN94][7].  I guess
when Analog bought Linear they broke the link, but [I found it
anyway][10].

[6]: http://www.aholme.co.uk/Avalanche/Avalanche.htm
[7]: http://www.linear.com/pc/downloadDocument.do?navId=H0,C1,C1154,D4183 "Linear AN94 Slew Rate Verification for Wideband Amplifiers - The Taming of the Slew. (broken link)"
[10]: https://www.analog.com/media/en/technical-documentation/application-notes/an94f.pdf "Linear Technology AN94 Slew Rate Verification for Wideband Amplifiers: The Taming of the Slew, by Jim Williams, May 02003"

### AN94: The Taming of the Slew ###

[Jim Williams’s AN94][10] is about measuring an amplifier slew rate at
2.8 GV/s, for which he had to build a 360ps-rise-time 15–20V pulse
generator for this purpose, because his fancy 1-ns rise-time pulse
generator was too slow for the amplifier he was measuring, but
subnanosecond-rise-time pulse generators cost US$10k–30k.  So he used
a 2N2501 (or maybe a 2N2369) as an avalanche transistor, biasing its
collector to 70 volts above ground.  Interestingly, my understanding
of triggering with a base pulse is incorrect, at least for this
circuit: he uses a *positive-going* trigger pulse into the base of the
avalanche transistor to trigger the avalanche, which I’d’ve thought
would be counterproductive.  He AC-couples the trigger pulse with a
5pF cap and protects the avalanche transistor’s base with a Schottky
up from ground.

The 2N2501 looks like a perfectly ordinary (but old) small-signal NPN
transistor: 350 MHz, β≈50 (or >3.5 for small signals), 40V minimum
V<sub>(BR)CBO</sub>, 1.2 W, 100 mA; the 2N2369 is pretty similar, but
maybe 500 MHz and 200 mA.  The datasheets show them in a 01960s-style
TO-18 metal can rather than a modern TO-220 or similar epoxy package;
[an advertisement for the 2N2501 appeared in the May 4, 01964 issue of
*Electronics*][11], though with only 20V “BV<sub>CBO</sub>”, and both
transistors appear in the [1965 Motorola Semiconductor Data
Manual][12], with ratings more like the 40V I mentioned earlier.
Neither is billed as an avalanche transistor or has a datasheet with
avalanche characteristics, and there’s nothing to suggest that they
can in any way be used to generate 400-picosecond edges.

I wonder if Williams used them even in 02003 instead of more modern
parts because the modern parts were “much improved” — in the sense of
having an inconveniently higher base-collector breakdown voltage.
(Does that also imply a larger junction capacitance?)  Williams
comments that not every transistor of this model was suitable:

> Q5 requires selection for optimal avalanche behavior. Such behavior,
> while characteristic of the device specified, is not guaranteed by
> the manufacturer. A sample of 30 2N2501s, spread over a 17-year date
> code span, yielded 90%. All "good" devices switched in less than
> 475ps with some below 300ps.⁶ In practice, Q5 should be selected for
> “in-circuit” rise time under 400 picoseconds.
>
> ***
>
> Note 6: 2N2501s are available from Semelab plc. Sales@semelab.co.uk;
> Tel. 44-0-1455-556565 A more common transistor, the 2N2369, may also
> be used but switching times are rarely less than 450ps. See also
> Footnotes 10 and 11.

[11]: https://www.rfcafe.com/references/electronics-mag/motorola-transistors-electronics-mag-may-4-1964.htm
[12]: https://archive.org/details/1965MotorolaSemiconductorDataManual "1965 Motorola Semiconductor Data Manual, p. 8-104 (448/916) and p. 8-112 (456/916)"

### AN72: A Seven-Nanosecond Comparator ###

Previously Williams wrote [AN72][9], which also covers the technique,
but at less length; most of AN72 is a primer on the basics of working
with VHF and faster circuits, or explanations of what you might want
to use Linear’s new high-speed LT1394 comparator for.  But in
pp. 32–34 and in appendix B, he gives a couple of simplified versions
of the AN94 design using a 2N2369, with a 2pF capacitor instead of a
transmission line.  Here he also explains the measures necessary to
prevent the 250-ps-rise-time avalanche pulse from overwhelming the
output of the comparator providing the trigger pulse: 100Ω and six
ferrite beads!  There must be a reason a diode wasn’t enough but I
don’t know what it is.

This suggests that after writing AN72 he found that the 2N2501 gave
better results than the 2N2369, which implies that probably most
transistors will be significantly worse.

He describes the transistor a couple of times as “a 40V breakdown
device”.

> The avalanche pulse measures 8V [4.8V where text is duplicated in
> appendix for slightly different circuit] high with a 1.2ns
> base. Rise time is 250ps [216ps in appendix], with fall time
> indicating 200ps [232ps in appendix]. The times are probably
> slightly faster, as the oscilloscope’s 90ps rise time influences the
> measurement.
> 
> Q5 may require selection to get avalanche behavior. Such behavior,
> while characteristic of the device specified, is not guaranteed by
> the manufacturer. A sample of 50 Motorola 2N2369s, spread over a
> 12-year date code span, yielded 82%. All “good” devices switched in
> less than 600ps [650ps in appendix].  C1 is selected for a 10V
> amplitude output. Value spread is typically 2pF to 4pF. Ground plane
> type construction with high speed layout, connection and termination
> techniques is essential for good results from this circuit.

Note that 8V is a lot less than the 70V or 90V to which the 2pF
capacitor is charged via a 1MΩ resistor; he says that 90V gives about
a 200kHz free-running frequency.

In AN94 he reported that he was having a hard time getting down to
300 ps, so maybe that 250-ps transistor was just a super good one, or
maybe he decided it wasn’t really 250 ps.

You might think that it would be hard to get less than 2pF parasitic
capacitance between PCB traces and stuff, but in the photo it seems he
just constructed that part of the circuit soldered to the backside of
a BNC connector.

This circuit also reconfirms that, contrary to my previous
expectations, he was triggering the avalanche by forward-biasing the
base-emitter junction, just like you normally would to operate a
transistor.

For more information about avalanche transistors for pulse generation
Williams refers us to these references:

17: Williams, J. “High Speed Amplifier Techniques,” Linear Technology
Corporation, Application Note 47 (August 1991)

20: Tektronix, Inc., Type 111 Pretrigger Pulse Generator Operating
and Service Manual, Tektronix, Inc. (1960) (Williams says his method
“borrows heavily from” this device.)

22: Williams, J., “Practical Circuitry for Measurement and Control
Problems,” Linear Technology Corporation, Application Note 61 (August
1994)

27: Haas, Isy, “Millimicrosecond Avalanche Switching Circuits
Utilizing Double-Diffused Silicon Transistors,” Fairchild
Semiconductor, Application Note 8/2 (December 1961)

28: Beeson, R. H., Haas, I., Grinich, V. H., “Thermal Response of
Transistors in the Avalanche Mode,” Fairchild Semiconductor, Technical
Paper 6 (October 1959)

### Tektronix Type 111 Pretrigger Pulse Generator ###

This could be used with the Tektronix Type N Sampling Plug-In Unit,
back when Tektronix was an oscilloscope company; in 01960 the Type N
claimed an 0.6-ns rise time on its front panel; it was used to trigger
an oscilloscope to repeatedly sample an otherwise-too-fast signal in
the analog domain:

> The sampling system thus formed permits the display of repetitive
> signals with fractional nanosecond (10⁻⁹ second or nsec)
> risetimes. By taking successive samples at a slightly later time at
> each recurrence of the pulse under observation, the Type N
> reconstructs the pulse on a relatively long time base. ...  The
> sampling system formed by the combination of the N Unit and a
> conventional oscilloscope is quite different in operation from
> normal oscilloscope systems. A conventional oscilloscope system
> traces out a virtually continuous picture of waveforms applied to
> the oscilloscope input; a complete display is formed for each input
> waveform. The sampling system, however, samples the input waveform
> at successively later points in relative time on a large number of
> input pulses. From this sampling process, a series of signal samples
> is obtained. The amplitude of each signal sample is proportional to
> the amplitude of the input signal during the short time the sample
> is made. Input waveforms are then reconstructed on the screen of the
> oscilloscope, as a series of dots, from these signal samples. The
> oscilloscope bandpass required to pass the “time stretched” signal
> samples is much less than the bandpass which would be required to
> pass the original input signal.

The Type 111 pulse generator was used to transmit the timing
information to the type-N sampler:

> As described previously, to trigger the Type N Unit you must first
> connect a triggering signal to either the TRIGGER INPUT or
> REGENERATED TRIGGER INPUT connector. When triggering signals are
> applied to the TRIGGER INPUT connector of the N Unit you must adjust
> the TRIGGER SENSITIVITY control for stable triggered operation.
> 
> ...
> 
> When the Type 111 Pretrigger Pulse Generator is used, no triggering
> adjustments are necessary except to turn the TRIGGER SENSITIVITY
> control of the N Unit fully counterclockwise. The N Unit is started
> automatically each time a pulse from the 111 is applied to the
> REGENERATED TRIGGER INPUT connector of the N Unit.

I haven’t been able to find the “Type 111 Operating and Service
Manual”, just the “Instruction Manual” from 01965 (59 pp.)  This
explains that it runs at up to 100 kHz (“kc”) and has a risetime of
500 ps at at least 10 volts, which is *astounding* for 01960:
“Determined from observed system risetime of 615 psec using a
Tektronix sampling oscilloscope with a risetime of 350 psec.  See
Calibration section.”

It evidently used an external coax “charge line” to produce a
rectangular pulse, so you could hook up different lengths of cable
there to produce pulses of different lengths, but only up to 142 ns
for serial numbers below 800: “Exceeding these limits may damage the
avalanche transistor, Q84.”  Higher serial numbers could use pulse
widths up to 1500 ns, so I guess they beefed up Q84.

You could also couple the pulse generator’s output pulse into the
device under test, I guess so that what you were viewing on the
oscilloscope was its pulse response.

The circuit is explained (p. 3–2, 22/59):

> **Output Pulse Generator (S/N 800-Up)**
> 
> The positive output pulse from the Comparator blocking oscillator is
> applied to the Output Pulse Generator (avalanche stage) through C75
> and D80.  Since the collector voltage of Q84 is set just short of
> the point where the transistor will avalanche, when the voltage
> pulse from T60 turns on D80, a fast current pulse is applied to the
> base of Q84, causing the transistor to avalanche.  This allows the
> internal charge line (and the external charge line, if any) to begin
> to discharge.  The resulting positive voltage step at the emitter of
> Q84 produces the start of the output pulse.
> 
> ...
> 
> **Output Pulse Generator (S/N 101-799 only)**
> 
> The positive output pulse from the Comparator blocking oscillator is
> applied to the Output Pulse Generator (avalanche stage) through two
> paths.
> 
> One path is through C75 and R75 to the collector of Q84.  The pulse
> which takes this path is a current pulse and is most effective when
> short time duration charge lines are used.  The collector voltage of
> Q84 is set just short of the point where the transistor will
> avalanche.  Consequently, when the positive pulse from Q60 is
> applied to the collector of Q84, the signal is sufficient to cause
> Q84 to avalanche.
> 
> The second path, from T60 through C76 to the outer conductor of the
> internal charge line and to R77 and R78, couples a positive voltage
> pulse to the collector of Q84.  This pulse is more effective than
> the current pulse at getting Q84 to avalanche when long charge lines
> are used.  The internal charge line is passed through a ferrite
> toroid core (T78) to prevent the voltage pulse from being shorted to
> ground.  The toroid core effectively isolates one end of the
> internal charge line.

So, fascinatingly, they redesigned the circuit to trigger through the
base instead of by adding more voltage to the collector, starting with
serial number 800!  I guess they didn’t realize they could do that in
01960 and only figured it out around 01965.

There’s a parts list in the manual starting on p. 49 and absolutely
beautiful schematics on pp.54–55/59 (initialed TR 964 and TR 366),
annotated with expected oscilloscope traces in callouts and dc voltage
levels as well.  There are only three transistors in the whole
instrument!

The all-important Q84 avalanche transistor was originally “Selected
from 2N636”, but switched at serial number 800 to “Silicon Avalanche,
checked”, with Tektronix part numbers.  In the pre-800 schematic I
think its V<sub>BC</sub> is given as 37 volts, and its base is pulled
down to a (germanium) diode drop below ground.

C75 is a 47 pF ceramic up to S/N 799, 10 pF in 800 and up, 500 V.  The
resistors are [carbon?] composition; R75 is 1kΩ, ±10% ½W up to 799,
±5% 1W in 800 and up.  R77 and R78 are ½-W 10-Ω jobbies, deleted in
800 and up.  T60, cleverly arranged so that the
trigger-pulse-generating transistor Q60 that triggers Q84 turns itself
off, is a TD20 toroidal transformer up to 799, a 4T bifilar
transformer in 800 and up (actually trifilar on the schematic).

D80 is exotic: for serial numbers X241–799 it’s a Tektronix germanium
diode, and for 800 and up it’s a Tektronix gallium arsenide diode.
(To be fair, most of the 16 diodes were germanium; only 2–4 were
silicon, plus five more in a typewritten erratum stuck in the back of
the manual.)

This probably explains why Williams didn’t use a diode to block the
current pulse surging back through the base of his avalanche
transistor: his diodes were too slow!  He probably didn’t have a
superfast GaAs diode handy, so he opted for ferrites.

The General Electric 2N636 was a 15MHz germanium NPN transistor
specified for 20 volts of “BV<sub>cb</sub>”, 200 mA, and β=35,
[according to one 01962 compendium][15], or 300 mA and β=70, according
to [one from 01973][14].  It appears in GE’s 01958 Transistor Manual,
categorized as “computer” rather than “audio”, “amplifier & computer”,
“unijunction”, “tetrode”, or “IF”, and rated for 300 mA, β=35, and
only a 15-volt “punch through voltage” (p. 145, 143/167).

[15]: http://bitsavers.org/components/derivationAndTabulationAssociates/1962_DATA_Transistor_Characteristics_Tabulation.pdf
[14]: http://www.bitsavers.org/components/sams/Transistor_Specifications_Manual_6th_Edition_1973.pdf

### Fullwood 01960 ###

Fullwood says:

> The pnp transistor types 2N501, 2N502, 2N504, 2N588, as well as the
> npn types 2N635, 2N636, 2N697, 2N706, and 2N1168 have all been found
> to avalanche with the same order of rise time [which he states in
> the abstract and later to be about 1 ns].  However, the decay time
> that is observed varies greatly with type, being related to the
> transistor’s normal performance as a switch. ...  One hundred and
> twenty 2N504 were tested as to whether or not they would avalanche
> at all in the circuit of Fig. 1. About 80% were found to operate
> satisfactorily with the zero bias arrangement as shown and without
> oscillating at this steady current.

An interesting thing about this is that he *was* triggering the
avalanches with a pulse on the base, unlike the 01960 version of the
Tektronix device.  Because the 2N504 was pnp, it was a negative-going
pulse, and the circuit was driven from a -300 V power supply.  Trigger
pulses were supplied from a “mercury pulser”.

DOI 10.1063/1.1716847, “On the Use of 2N504 Transistors in the
Avalanche Mode for Nuclear Instrumentation", by Ralph Fullwood (under
Walter Selove) at U Penn (later at RPI), *Review of Scientific
Instruments*, Volume 31, Number 11, November, 01960, interestingly the
same journal that published Kilpelä and Kostamovaara 37 years later
(see below).

He cites:

1. D. J. Hamilton, J. F. Gibbons, and W. Shockley, Proc. IRE 47, 1102
   (1959).
2. I. A. D. Lewis and F. H. Wells, Millimicrosecond Pulse Technique
   (Pergamon Press, New York, 1959), 2nd ed.

This paper is interesting because it has a number of very simple
circuits that do interesting things, like amplify the tiny pulses from
a photomultiplier tube.

### AN122: Never has so much trouble been had by so many with so few terminals ###

After Holme’s project, [Williams and David Beebe revisited pulse
generators in Linear AN122 in 02009][17].  In Appendix B,
“Subnanosecond Rise Time Pulse Generators for the Rich and Poor”, on
p. 11/20, they explain:

> The Tektronix type 111 has edge times of 500ps, with fully variable
> repetition rate and external trigger capabilities.  Pulse width is
> set by external charge line length.  Price is usually about [US]$25.
> ... Residents of Silicon Valley tend towards inbred
> techno-provincialism.  Citizens of other locales cannot simply go to
> a flea market, junk store or garage sale and buy a sub-nanosecond
> pulse generator.

Then they again present the circuit from AN94, unmodified as far as I
can tell, but this time its performance has been derated again, to a
400ps rise time.  And in Appendix F, they explain, “The Tektronix type
109 mercury wetted reed relay based pulse generator will put a 50V
pulse into 50Ω (1A) in 250ps.”  Perhaps this is the “mercury pulser”
Fullwood was talking about.

[17]: https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/26/an122f.pdf

### Wong’s Reverse Avalanche ###

[Kerry Wong revisited the theme in 02014][18] using the lower-voltage
emitter-base junction as I suggested above, producing the following
table of emitter reverse breakdown voltages with a 1000μF (!!!) cap:

<table>
<tr><td>2N4401 	<td>~12.5V
<tr><td>SS9014 	<td>~12.5V
<tr><td>2N4124 	<td>~12V
<tr><td>2N3904 	<td>~12V
<tr><td>BD137 	<td>~11V
<tr><td>BD139 	<td>~11V
<tr><td>BC337 	<td>~9V
<tr><td>SS9018 	<td>~8.2V
</table>

[18]: http://www.kerrywong.com/2014/03/19/bjt-in-reverse-avalanche-mode/

He found some important limitations:

> Also, while I could get most NPN transistors to oscillate in their
> reverse breakdown regions I could only get a couple of BD138 PNP
> transistors to oscillate using the same circuit above (power
> polarity is reversed). And the oscillation only occurred at a very
> tight voltage interval (e.g. ±0.05V).
> 
> One of the useful features of a standard avalanche pulser (like this
> one [linking to his other project]) is its extremely fast rise time
> (subnanosecond), so can we use negistors to build similar pulsers?
> 
> Well, the short answer is no. After some experiments it appeared
> that the rise time of a negistor pulser is magnitudes higher
> (e.g. ~100ns) than a typical avalanche pulser.
> 
> ...the capacitance cannot be arbitrarily small. In my case, 100nF
> seems to be near the lower limit.

Importantly, he says in the comments:

> Just the e-b junction won’t work, it would just act like a Zener
> diode.

analogspiceman posted the following SPICE model in the comments:

    * UpsideDown.asc – a single transistor relaxation oscillator model for LTspice
    V1 1 0 10
    R1 1 2 1k5
    C1 2 0 1µ Rser=8m
    XQ1 0 NC_01 2 2N2222r
    *
    .subckt 2N2222r e b c ; this subckt just turns the NPN upside down
    Q1 c b e 2N2222r
    .model 2N2222r npn Is=10f Xtb=1.5 Rb=10 ; nondirectional parameters
    + Br=200 Ikr=0.3 Var=100 tr=400p ; reverse (forward) parameters
    + Bf=7 Ikf=0.5 Vaf=10 tf=100n Itf=1 Vtf=2 Xtf=3 Ptf=180 ; fwd (rev) params
    + Re=.3 Cje=8p Ise=5p ; emitter (collector) parameters
    + Rc=.2 Cjc=25p Isc=1p BVcbo=7 ; collector (emitter) parameters
    .ends 2N2222r
    *
    .opt plotwinsize=0
    .tran 0 10m 0 1u uic

Wong mentions [the term “negistor” Richard Phares used in Popular
Electronics in 01975][24] for this configuration (an avalanche
discharge has negative differential resistance, so “negative
resistance transistor”).  Phares notes that germanium transistors and
pnp transistors will not work, recommending the MPS-5172, the 2N2218
(7.7V), the 2N2222, or the 2N697.  Unfortunately, the term “negistor”
seems to have been largely co-opted by Keelynet crackpots lacking even
the most basic knowledge of physics and electronics.  [However, Alan
Yates, for example, built some oscillators using the term][20].
Prolific electronics hacker [sv3ora reports, “The 2N4124 gave the
lowest oscillation voltage, around 6.8V,”][21] and confirms that
grounding the base kills the oscillation.  [Jean-Louis Naudin reports
oscillation at 16.4 volts on a 2N2222A][22] and also characterizes its
available stable avalanche currents ranging from 5.47 V at 10 mA up to
6.54 V at 2 mA.

[20]: http://www.vk2zay.net/article/157
[21]: http://www.qrp.gr/negistor/index.html
[22]: http://jlnlabs.online.fr/cnr/negosc.htm
[24]: https://web.archive.org/web/20120329231651/http://www.schematicsforfree.com/files/Components/Circuits/Negistor%20Explained%20-%20The%20Mysterious%20Negistor.pdf?action=download

### Kilpelä and Kostamovaara’s 01997 laser ###

[These folks][4] wanted to make 5–10-ns semiconductor laser pulses for
LiDAR, but at tens of amps.  They said a transistor in avalanche mode
is faster than a thyristor or MOSFET, though GaAs thyristors were
reported to have reached the 500-ps-level most of the above discussion
has centered on.  They tried an MJE200, a 2N5190, two 2N5192s, and a
Zetex ZTX415 SOT-23 avalanche transistor; the MJE200 started breaking
down below 100V but was consistently only about 15A no matter how high
the voltage, while the others all required 250V to break down,
reaching 70 A at 400 V.  These all got rise times in the 2.5–4 ns
range; this extreme slowness (ha!) is probably because parasitic
inductances matter more at 70 amps than at 1 amp.

Their circuit is very different from all the others I’ve seen, full of
inductors, and I don’t understand it yet.  The paper has lots of good
explanation about how avalanche transistors work, though.

70 A at 400 V for 10 ns is 28 kW, but only about 0.28 mJ.

### Alex McCown’s ###

[Alex McCown (onebiozz) built a pulse generator to test his
oscilloscope][27] around a 2N3904, getting a 1.56-ns rise time (which
he thinks is the scope’s limit, not the circuit’s) but wished he’d
used a BFR505:

> I have to say this was a fun $0 project, but if i were to spend some
> cash what would i have done differently knowing what i do now?  Well
> for one i would not use an 2N3904, the BFR505 appears to be a better
> solution at a simple 30v avalanche of ~200-300pS.

[27]: https://dodgyengineering.com/2016/08/10/junk-box-2n3904-avalanche-pulse-generator/

### M. Gallant’s speed-of-light measurement ###

[Michel I. Gallant put 20ns pulses through an infrared LED][28] using
a 2N2369a avalanche transistor to measure the speed of light to within
about 1% in his living room, but the 25 MHz Vishay TSFF5210 LED he
chose slowed their rise time to 10ns.  Very simple perfboard circuit.
As a detector he used a 200 MHz Vishay BPV10 PIN photodiode amplified
by an AD8001 configured for 35× gain and 50MHz, but they also built
the circuit on a solderless breadboard, so it might have suffered some
signal integrity problems from that and from the long leads on their
components too.

Also interesting for fast-circuit purposes, he [measured the response
of different common LEDs up to 10MHz][29]: the TSFF5210 had drooped
less than 1dB at 10MHz, a red 08LCHR5 AlInGaP drooped 3dB, and a white
08LCHW3 InGaN drooped 3dB at 2MHz and 6dB at 3MHz.  Presumably that’s
a composite of fast blue and slow yellow, but the pulse response he
shows doesn’t show much fast blue.

[28]: https://www.jensign.com/sol/index.html
[29]: https://www.jensign.com/Discovery/LEDFrequencyResponse/index.html

### Michael Covington’s notes ###

[Covington notes that the avalanche effect of the emitter-base
junction makes a good white noise source][30], and also a good
low-leakage low-capacitance “zener diode”, citing EEVBlog #1157.

[30]: http://www.covingtoninnovations.com/michael/blog/1909/index.html#x190920