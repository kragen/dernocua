I watched a [GreatScott! video recently in which he designed and built
a direct-digital synthesis waveform generator][0] going up to a few
MHz, using a waveform-generator chip which mostly consists of a 28-bit
counter driving a sin() ROM attached to a DAC through a mux.  When you
want a sawtooth wave instead, the mux selects the counter instead of
the ROM output, and when you want a square wave, it just selects the
MSB.

(I haven’t tried any of what is described below, even in simulation,
so it wouldn’t be unsurprising if there are fatal flaws in my
calculations.)

GreatScott’s designs
--------------------

[0]: https://www.youtube.com/watch?v=Y1KE8eAC9Bk

In the video, he compares his €600 Siglent SDG 2082 X, which goes up
to 80 MHz and generates 1.2 gigasamples per second; his €70 Ascel
Æ20125, which goes up to 10 MHz but only up to ±5 V; the
above-mentioned cascade of three LM318N circuits, which only operates
over about 1.7 kHz to 40 kHz with the passives he chose, and of course
has a nasty temperature coefficient; a €6 kit built around the analog
XR-2206 monolithic function generator, which goes up to 1 MHz; and his
own €50 design built around the AD9833 DDS function generator IC
[(which IC goes for US$10.04 on Digi-Key in quantity 1][6]), which
goes from DC to a bit past 12 MHz.

[6]: https://www.digikey.com/en/products/detail/analog-devices-inc/AD9833BRMZ-REEL/993964

He points out the AD9833 gives better results than a popular
pure-analog three-opamp circuit which configures the first opamp as a
relaxation oscillator and the other two as integrators, in large part
because the relaxation oscillator output has shitty RC-decay edges.

The LM318N is pretty fast; [TI’s LM318N datasheet][1] claims 15MHz
“small-signal bandwidth” (typical, not minimum) and 50V/μs slew rate;
their plot of unity-gain bandwidth suggests 15MHz at ±5V and 25°
increasing to 19MHz at ±20V.  [Digi-Key lists them for US$1.13 in
quantity 10][2].  Its open-loop gain is claimed to drop off from 110dB
below 100 Hz at the usual 20dB per decade, so at GreatScott’s desired
10MHz it only has about 5dB left.  The circuit in question is maybe
not very demanding of the op-amp’s open-loop gain, since each opamp is
just amplifying its own output or the output of the previous stage.
The slew rate should also be okay.  It should be fine for a sine
wave — I think 10MHz is a radian per 16 μs, so at Scott’s desired
±12V, the maximum slew rate of a sine wave is 24V/16μs, or
1.5V/μs — and even a 10MHz square wave shouldn’t be too trapezoidal at
0.5 μs of rise or fall time followed by 50 μs of high or low time.  I
conclude the opamp is fine and the circuit design is at fault.
Probably a Schmitt trigger to clean up the square-wave transitions and
careful control of parasitics would yield totally acceptable results.

[1]: https://www.ti.com/lit/ds/symlink/lm318-n.pdf
[2]: https://www.digikey.com/en/products/detail/texas-instruments/LM318N-NOPB/6180

Microcontroller-based DDS
-------------------------

At lower frequencies, you might as well just use a microcontroller.  A
[108MHz GD32 can, in theory, happily spit out 54 megasamples per
second][3] of digital data on one of its 16-bit I/O ports, and if you
feed that to a simple R-2R DAC feeding an amplifier, you can easily
get 6 bits of precision, or 8 bits with careful trimming.  And, [on
the similar STM32F103C8 from ST, StackOverflow user SirSpunk was able
to achieve one output word per two clock cycles][4], which would give
the above 54 megasamples per second, though this required some
trickiness like keeping the samples in CPU registers.  (Chips like the
STM32F103 and the GD32F103 also include a 12-bit DAC with supposedly
about 10 bits of precision, but the DAC cannot run nearly this fast.)
A dedicated DAC chip could improve precision, but improving the sample
rate would require using a faster microcontroller.  Moreover, even
this data rate may not be achievable if the data samples need to come
from somewhere else, like an arithmetic operation or fetching from
RAM.  [ST’s appnote 4666][5] details achieving sustained data rates of
8 to 10 megasamples per second using DMA on some other STM32-family
microcontrollers, but I don’t think the STM32F103 or GD32F103 supports
DMA for GPIO.

[3]: https://www.gigadevice.com/datasheet/gd32f103xxxx-datasheet/
[4]: https://stackoverflow.com/a/59905461
[5]: https://www.st.com/resource/en/application_note/dm00169730-parallel-synchronous-transmission-using-gpio-and-dma-stmicroelectronics.pdf

Up to 1 MHz, 54 megasamples per second is a buttload of samples,
technically speaking.  The tenth harmonic would be 10 MHz, and its
Nyquist frequency 20 MHz, so you should be able to get nice sharp
edges on your 1 MHz square and sawtooth waveforms.  At 10 MHz, they’ll
start to look pretty darn fuzzy, though: you only have 5.4 samples per
cycle, so you’re going to have slow transitions, a lot of ringing, or
most likely both, depending on how you set up the analog output
filtering.

Adjusting the clock speed is a potential approach to avoiding
computation in the inner loop of slamming the samples out; for
example, if you can store 8 samples in 8 CPU registers, you can
produce those 8 samples in a tight loop, getting a 6.75MHz arbitrary
waveform at 54Msps; and by producing them once forward and once in
reverse, you can get a 3.375MHz arbitrary symmetrical waveform.  But
producing an arbitrary *6MHz* waveform would be much easier to do if
you can lower the CPU clock to 96MHz.

The great advantage of using a microcontroller is that you can
potentially output a very flexible set of waveforms: not just square,
sawtooth, triangle, and sine, but also for example AM, FM, QPSK, white
noise, and filtered weighted sums of any of the previous ones.  But
what good is that if your waveform comes out shoddy?

For square waves in particular you may be able to use a separate
analog data path with different filtering (sharpening edges with a
Schmitt trigger and relying on clamping to the power-supply rails,
say), but that doesn’t help with other waveforms containing sharp
edges.

Non-microcontroller logic
-------------------------

### Parallel SRAM ###

Well, what if you hook up a DAC (R-2R or IC) to the output of a RAM
chip?  [Digi-Key sells the obsolete CY62256NLL-70ZRXIT for
US$0.58][7], which is a 28-pin 70ns SRAM chip with 8-bit-wide output
and 15 address lines; if you gang up two of these mothers you get
16-bit-wide output.  As long as they’re in read mode, every time you
change the value on the address bus, you get your data out 70ns later
(or [55ns later in some other grades of the chip, according to
Cypress’s datasheet][8]).  They used to even sell them in DIP and SOIC
forms.  Too bad it hit end-of-life in 02017.  I don’t know how glitchy
the output is, so you might need external tristate buffering, and also
it uses TTL thresholds, so you may need level shifters.  (Also, since
you need to load the data on the same data bus you’re using for the
DAC, you might want external tristate buffering to disable the DAC
while you’re loading that data.)

[7]: https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY62256NLL-70ZRXIT/1205300
[8]: https://www.cypress.com/file/43841/download

70ns isn’t fast enough, though; if you didn’t need any extra time to
switch addresses you would only get 14.3Msps that way, and so a
maximum sine-wave speed of 7.1MHz, and a maximum square-wave speed
somewhere in the neighborhood of 1 MHz.

A much more modern, but still obsolete, part is [the 80¢ Cypress
CY7C1021BN-12ZXC][9], which has 16 address lines, 16 data lines, 44
pins, and a 12-ns access time.  [The CY7C1021BN datasheet, which is
for the 15-ns version,][10] claims that it’s basically otherwise
identical to the older chip, except that it has separate
byte-high-enable and byte-low-enable inputs so you can use it with an
8-bit bus if you want.

[9]: https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY7C1021BN-12ZXC/1205573
[10]: https://www.cypress.com/file/38791/download

So this is starting to sound decent; you should be able to get 60
megasamples per second out of such a chip once you’ve loaded the
waveform into it.  And you can load up to 65536 samples into it, or
131072 if you just use 8 bits of data and use the /BHE and /BLE lines
as an additional address bit; or you could tie some address lines to
ground in order to save I/O pins.

A CPLD or something could be configured as a counter to generate the
addresses at a higher clock speed than the microcontroller can manage.
In the case where the carry chain is becoming too slow, you can use an
LFSR instead of a normal binary counter, with the XOR gates interposed
between successive register bits, thus getting your critical path
delay down to a single XOR’s propagation delay.

Non-obsolete parallel memory parts that could be used similarly
include the following:

<table>
<tr><th>Part number  <th>Price, qty 1  <th>Access time  <th>Maximum clock speed  <th>Address lines  <th>Data lines  <th>Package  <th>Voltage
<tr><th><a href="https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY62136EV30LL-45ZSXIT/1543737">CY62136EV30LL-45ZSXIT</a>
                      <td>US$1.11      <td>45ns         <td>(async)              <td>17             <td>16          <td>44TSOP II<td>2.2–3.6V
<tr><th><a href="https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY7C1020D-10VXI/1543809">CY7C1020D-10VXI</a>
                      <td>US$3.94      <td>10ns         <td>(async)              <td>15             <td>16          <td>44-BSOJ  <td>4.5–5.5V
<tr><th><a href="https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY7C1329H-133AXC/1839383">CY7C1329H-133AXC</a>
                      <td>US$2.30      <td>(N/A)        <td>133MHz               <td>16             <td>32          <td>100-TQFP <td>3.15–3.6V
<tr><th><a href="https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY7C1360C-166BZC/1839408">CY7C1360C-166BZC</a>
                      <td>US$4.56      <td>(N/A)        <td>166MHz               <td>18             <td>36          <td>165-FBGA <td>3.135–3.6V
<tr><th><a href="https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY7C1360C-200AJXC/1205794">CY7C1360C-200AJXC</a>
                      <td>US$4.18      <td>(N/A)        <td>200MHz               <td>16             <td>36          <td>100-TQFP <td>3.135–3.6V
</table>

The other 5-volt part also shares the annoying TTL thresholds.

The CY7C1329H and CY7C1360C “include[] a two-bit internal counter for
burst operation” when you hold the /ADV line low, which suggests that
you could feed it an externally-generated address every *four*
samples, which means you could even use a cheap microcontroller to do
the address generation, since you need no more than 50 million
addresses per second.  Amusingly, it even has an “interleaved” mode
(selected by tying the MODE pin to V<sub>DD</sub>) in which it can
count either 0123, 3210, 1032, or 2301 rather than the usual 0123,
1230, 2301, and 3012 alternatives; this would be useful for
time-reversing a part of a waveform.

These parts, being synchronous, of course produce output data starting
in the following clock cycle rather than as soon as possible.

For such synchronous memories, you might need some external glue logic
to gate off the memory control lines faster than the microcontroller
can do it on its own.

You’d think that someone would have sub-nanosecond SRAM by now, and
[Cypress used to make a line of what purported to be sub-nanosecond
SRAM][32], but no longer, and anyway it was synchronous at speeds of
200MHz or less.  If you want “subnanosecond” RAM today you have to go
with DRAM, and none of it can support random write accesses in less
than 15ns.  Digi-Key has [42 Winbond W971GG6SB-18 chips][33] in stock
for US$4 each; these are a gibibit organized 16 bits wide with a
533MHz DDR2-1066 clock.  Its CAS latency is 6 clocks (11.3 ns), its
write recovery time is 15 ns, and if I understand correctly, there are
various other latencies related to random accesses that bring its
random access latency up near 100 ns.  But if you just want to spew
out a sequential stream of data, it can totally give you 16 fresh bits
every 940 picoseconds for a good long while.

[32]: https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CYDD09S36V18-167BBXC/1206282
[33]: https://www.digikey.com/en/products/detail/winbond-electronics/W971GG6SB-18/5125231

The async parts would still need some kind of external counter logic
to drive their address lines faster than the microcontroller can
manage.  You could do this with a two- to four-bit counter on the
low-order address lines or by wiring up the whole address bus to the
thing.

#### CPLDs and PLDs as counters ####

One approach here would be to use a generic programmable-logic chip
like the [US$0.94 Altera MAX V 5M40ZE64C5N 40-(one-bit)-logic-element
7.5-ns CPLD][11], which [can run its output buffers at up to 3.6 volts
and run a 16-bit counter at up to 118.3 MHz][12]; the [US$1.44 Lattice
“ispMACH” 4000ZE-series LC4032ZE-7TN48C 32-macrocell 7.5-ns CPLD][13],
which [can also do 3.3-volt output][14] and I think is similar in
speed or perhaps could manage up to 260MHz; the [US$1.80 Atmel
ATF1502ASV-15AU44 32-macrocell 15-ns CPLD][15], which runs at 3.3
volts natively and I think can reach 77 MHz; or maybe [an
old-fashioned PLD][18] like the [US$2.06 22V10, which comes in a 10-ns
grade][16] and astoundingly [even a US$2.14 5-ns grade][17] these
days, and of course run on 5 volts and have annoying TTL thresholds,
but in theory can run at up to 166MHz.  Since even a two-bit counter
would be enough to lower the burden on the microcontroller by a factor
of four, we could even consider smaller PLDs like a 16R4 or 16V4, but
they are all obsolete.

[11]: https://www.digikey.com/en/products/detail/intel/5M40ZE64C5N/2499440
[12]: https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max-v/mv51003.pdf
[13]: https://www.digikey.com/en/products/detail/lattice-semiconductor-corporation/LC4032ZE-7TN48C/2751416
[14]: http://www.latticesemi.com/~/media/LatticeSemi/Documents/Solutions/Packaging%20Solutions/ispMACH4000ZE%20Family%20Data%20Sheet1022.pdf
[15]: https://media.digikey.com/pdf/Data%20Sheets/Atmel%20PDFs/ATF1502ASV.pdf
[16]: https://www.digikey.com/en/products/detail/microchip-technology/ATF22V10C-10JU/1008554
[17]: https://www.digikey.com/en/products/detail/microchip-technology/ATF22V10C-5JX/1027056
[18]: http://www.pldworld.com/html/technote/Tour_of_PLDs.htm

Amusingly, the Altera chip also contains an 8192-bit block of Flash
with auto-increment addressing, so if your waveform data is smaller
than that and never changes, you don’t need an external RAM chip!

And *obviously* with [an FPGA like a Lattice UltraPlus ICE40UP5K][28]
([US$6][29], 5280 4-LUTs, 120 kibibits of block RAM, 1 mebibyte of
SPRAM, eight 16-bit multipliers, capable of running a 16-bit counter
at 100 MHz, fully supported by IceStorm) or [a Lattice
LFE5UM5G-45F-8BG381C][30] ([US$31][31], 85k 4-LUTs, 72 18-bit
multipliers, four 5Gbps SERDES channels, running some functions at up
to 400 MHz) you can do all the DDS you want entirely inside the chip,
as long as it’s not above a couple hundred megahertz.

[28]: https://github.com/tinyvision-ai-inc/UPduino-v3.0
[29]: https://www.digikey.com/en/products/detail/lattice-semiconductor-corporation/ICE40UP5K-SG48I/7785190
[30]: https://github.com/oskirby/logicbone
[31]: https://www.digikey.com/en/products/detail/lattice-semiconductor-corporation/LFE5UM5G-45F-8BG381C/6173744?s=N4IgTCBcDaIDIDECiBWAqgWRQcQLQBYUFcAOAIWwGYSBGAYRAF0BfIA

#### Dedicated counter ICs ####

There are various popular counters like the [72¢ 4-bit 90MHz
74AC161][19], the [54¢ 14-bit 65MHz 74HC4060][20], the [38¢ dual-4-bit
107MHz 74HC393][21], and the [50¢ 4-bit 167MHz 74HC161][23]; all of
these can use a wide variety of supply voltages.  Ripple counters like
the [42¢ 12-bit 210MHz 74VHC4040][22] would not work for this.

[19]: https://www.digikey.com/en/products/detail/texas-instruments/CD74AC161M96/1691776
[20]: https://www.digikey.com/en/products/detail/stmicroelectronics/M74HC4060RM13TR/591945
[21]: https://www.digikey.com/en/products/detail/nexperia-usa-inc/74HC393PW118/1230333
[23]: https://www.digikey.com/en/products/detail/on-semiconductor/MC74HC161ADG/2305548

But what about memories with built-in counters?

Serial memories
---------------

Microcontrollers are commonly used with memories with bit-serial
interfaces, either SPI, I²C, dual SPI, or quad-SPI.  Typically you can
write these memories in true bit-serial mode and read them in
quasi-parallel mode, but even when not, it would be practical to gang
up several of them (4, 5, 8, or 10 chips, say), write to several of
them one at a time, then read from them all at once; typically they
permit reading an entire sector with a single command.  Almost
invariably these are Flash — serial SPI SRAM like the 23K256 exists
but only up to 45MHz.  Some of these SPI Flash memories are too slow
to be useful for this kind of application, but others are plenty fast.
Specimens of this genre include the [US$2.07 166MHz quad-SPI Winbond
W25N512GVEIG][24], the [30¢ 100MHz dual-SPI GigaDevice
GD25D05CTIGR][25], and the [31¢ 85MHz quad-SPI Adesto
AT25SF041B-SSHB-B][26].

[24]: https://www.digikey.com/en/products/detail/winbond-electronics/W25N512GVEIG/12143334
[25]: https://www.digikey.com/en/products/detail/gigadevice-semiconductor-hk-limited/GD25D05CTIGR/9484665
[26]: https://www.digikey.com/en/products/detail/adesto-technologies/AT25SF041B-SSHB-B/12808415

Taking the GigaDevice device as typical, [we find in its
datasheet][27] that it not only permits bit-serial writing, it
requires it.  Puzzlingly it claims to permit reads at 160Mbps but a
100MHz clock (see below).  It holds half a gibibit of data, divided
into 16-page sectors of 256-byte pages.  The data-rate doubling is
implemented by making its serial input pin bidirectional.

A single READ command (0x03, or 0x0B for fast read, followed in either
case by three address bytes) will eventually read the whole memory if
CS# is held low for enough clock cycles.  There are no dummy bits,
start bits, stop bits, or command bits in the timing diagram once the
data stream starts.

[27]: https://www.gigadevice.com/datasheet/gd25d10c/

The “AC characteristics” table clarifies the clock speed mystery:
“fast read” 0x0b can happen at 100MHz, but regular read (0x03, which
appears to be otherwise identical) and dual-output read (0x3b) can
only happen at 80MHz.

Because it’s Flash, programming a new waveform into the chip is slow
(700 μs per page, about 300 times slower than reading), and can only
be done some 100k times before risking burning the chip out.  This
seems like an acceptable tradeoff.

Normal SPI uses three pins on your master chip plus one per slave: SCK
(“SCLK”), MOSI (“SI”), MISO (“SO”), and one /CS (“CS#”) per slave.
(This chip additionally has a “WP#” pin which must be high for writes,
which I suppose is intended to prevent accidental erasure due to EMI
or software bugs, but it would probably be acceptable to tie it low.)
But if we’re going to use various memory chips’ SO pins to directly
drive a DAC, they can’t all be tied to each other as they normally
would be.

Ganging up 8 GD25D05Cs in this way could be achieved most simply by
just *not routing the MISO pins back to the master* — that is,
configuring the memory chip as write-only memory, with their output
pins connected only to the DAC.  This would prevent the program from
reading the status register, or reading back waveforms to verify them,
but that’s not necessary for the waveform generator to work.  Then all
that remains is to drive the SCK inputs of the slaves from a
free-running 100MHz clock on command from the slower master, so you
need a 100-MHz 2-mux on the clock line; SCK, MOSI, and mux-select pins
on the master for all slaves; and eight /CS pins on the master, one
per slave.  When issuing a “fast read” command, the master would
broadcast it to all slaves at once.

And that way you get 100Msps of waveform-generation output.

The Adesto chip seems to be very similar, down to using the same
opcode bytes and the same pins for dual-output reads, but also
supports four-bit-per-clock output by co-opting the /WP pin and a
/HOLD pin the GD25D05C lacks; also its multi-bit reads run at full
speed, and it has the option of clocking in the address bits on
multiple pins as well, and clocking in the data bits on multiple pins
when writing the chip.

Augmenting the circuit to support reading from the memory chips
without using more pins on the microcontroller is relatively simple: a
pullup resistor per memory chip, plus an 8-input AND, NAND, or parity
chip; or alternatively pulldowns and an OR, NOR, or parity.  Another
way to implement this is with diode logic: one diode down from the
shared microcontroller pin to each memory chip’s MISO pin, and a
pullup resistor on the master side, which can be internal on most
popular microcontrollers.  Or you can just use a separate
microcontroller pin for each MISO line, bringing the total to 19 GPIOs
for 8 memory chips.

Augmenting these circuits to support the use of multi-bit outputs is
potentially more difficult if you don’t have all those GPIOs: the MOSI
line becomes bidirectional, and you want the master to be able to send
bits to any of the slaves, but you don’t want the slaves’ drivers to
be able to fight each other.  This is similar to the problem of a
bidirectional level shifter, which is in fact a thing you might want
in this case anyway.

If not, though, one approach is a pullup on each slave MOSI pin, a
diode from each slave MOSI pin to the shared master MOSI pin, and a
pull*down* on the master MOSI pin.  When all the involved pins are
tristated, a weak current will flow through the diodes, maintaining
all the relevant pins in an indeterminate state which probably wastes
a lot of power.  If the master pulls its pin low and the slaves are
tristated, this will bring all the slaves’ pins to a diode drop above
ground, which hopefully is low enough to count as “low”; if it pulls
its pins high, this will overwhelm its pulldown and allow the slaves’
pullups to pull their inputs high.  If the master tristates its pin
and some slave pulls its pin high (because MOSI has become part of a
multi-bit bus that the slave is writing to), the master’s pin will
rise to a diode drop below V<sub>CC</sub>, which is safely HIGH at
most voltages; if the slave pulls its pin low, overwhelming its
pullup, then the master’s pullup will pull its pin all the way to
ground.  And in no case can two slaves’ outputs fight each other.

(Incidentally, this kind of thing would also be useful for spewing out
canned bitstreams at higher rates than your microcontroller can
manage, too: generate the bitstream at your leisure in the serial
memory, then spew out bits at high speed, possibly repeatedly and into
a SERDES.)

Toward a gigahertz
------------------

Unfortunately, none of the above approaches get us close to being able
to synthesize gigahertz signals.  In fact, most of them top out (with
easily available hardware, anyway) around 100Msps, where the top sine
frequency you could manage would be around 50 MHz, and the top
frequency with reasonably sharp edges would be in the neighborhood of
5 or 10 MHz.  So I guess that’s why “GreatScott” picked that US$10
Analog Devices chip; you *can* do better, but it’s not easy.

To manage hundreds of megahertz with an arbitrary waveform, let alone
a gigahertz, we’d need a different approach.  I think it’s feasible
without reaching for exotica like indium phosphide, though.  AD and TI
both have analog-switch ICs reaching from DC up to 1 GHz or more;
ADG902-EP (4.5GHz, US$3.39 from Digi-Key, 17-ns on+off switching
time), ADG919 (4GHz, US$3.34, 19.5-ns on+off switching time) TMUX1072
(1.2GHz, US$1.18, 260000-ns on+off switching time), and TMUX136 (6GHz,
US$0.98, 600-ns on+off switching time) are representative examples.
These are MOSFET switches; the more common PIN-diode type typically
takes over a microsecond.

MOSFETs have an intermediate “ohmic mode” of conduction, in between
“saturated” fully on and “subthreshold” fully off; as can be seen from
the above figures, they have much higher bandwidth through the channel
than they do for turning the gate on and off.  By precisely
controlling the gate voltage, you can control the impedance a signal
sees going through the channel, and thus its attenuation.  This
phenomenon is not extremely linear in the gate voltage (especially if
you don’t subtract the threshold voltage, but even then), and the
current isn’t even all *that* linear in the drain-to-source voltage
V<sub>DS</sub>.  But it’s a reasonably good approximation when
V<sub>DS</sub> isn’t too high and V<sub>GS</sub> isn’t too low.  And,
as we will see, in this application we can correct for the
nonlinearity in gate voltage in software.

With two such pseudo-variable-resistors, you can make a voltage
divider from an output signal terminal, through a MOSFET channel, to
an input signal terminal, through a second MOSFET channel to ground,
such that the total input impedance seen by the input signal terminal
is some constant impedance such as 500Ω.  If a short pulse arrives on
the input terminal, some attenuated version of the pulse will be seen
at the output terminal.  If the upper MOSFET is nearly saturated at
10Ω, the lower MOSFET to ground ought to be nearly off, at about
24500Ω, for the input to see 500Ω.  If the upper MOSFET is at 250Ω,
then the lower MOSFET should be at 500Ω, and the signal will be
attenuated by half (6 dB).  If the upper MOSFET is at 400Ω, then the
lower MOSFET should be at 125Ω, and the signal will be attenuated by ⅘
(14 dB).

The key point here is that this configuration allows you to
selectively attenuate a pulse train.  Moreover, a similar
voltage-divider arrangement allows you to selectively steer them with
reasonably low insertion loss!  If the input signal is to be divided
evenly between two 500Ω outputs without losing impedance matching,
then a MOSFET to each of them operating in the ohmic region with a
250Ω resistance will do the job, wasting only four ninths of the
signal energy (3.6 dB), and this is the worst case; by reconfiguring
the gate voltages to pass more of the signal to one side, this loss is
reduced.

For example, if the MOSFET channel resistance to the left output is
50Ω, then the MOSFET channel resistance to the right input should be
5kΩ.  The voltage on the left channel will be 500/550 of the input
voltage, or 91%, and the power 83% of the original, a loss of about
0.8 dB.  The voltage on the right channel is 500/5500 of the original,
or 9.1%, and the power 0.83% (21 dB attenuated).

(The pulse passing through to the MOSFET source will, if positive,
reduce V<sub>GS</sub> temporarily, creating distortion; adding
capacitance across those terminals should push that problem out to a
long enough timescale that this nonlinearity doesn’t provoke harmonic
distortion and reflections.)

Multi-way splits with impedance matching are higher-loss than two-way
splits; for example, if we split the signal into four equal parts with
500Ω each, we need 1500Ω of series resistance on each branch, thus
losing ¾ of the voltage and burning 15/16 of the power in the
resistors, a 12 dB loss.  (XXX is that right?  That can’t be right.)

Such attenuated pulse trains can be passed over microstrip (or
stripline if necessary) and summed with a resistor network (at the
cost of further attenuation), following variable delays imposed by
variable lengths of microstrip.  Configuring the set of attenuations
for each delay, by way of setting the gate voltage on the various
MOSFETs, amounts to configuring a convolution kernel in the time
domain, which is to say, a single iteration of a waveform; a pulse
train at the desired fundamental frequency is then all that is needed
to synthesize the desired waveform.  If the delays are regularly
spaced, thus forming a regular sampling, a spurline filter can notch
out the sampling frequency and its harmonics.

So then the problem of gigahertz DDS reduces to the problem of setting
the gate voltages on all these MOSFETs and producing a pulse train at
the desired fundamental frequency.

How much microstrip are we talking about?  Crudely speaking, about
150 mm per nanosecond, so perhaps on the order of a meter for signals
with a fundamental frequency down to a few hundred megahertz.

How should we distribute the delays to the customizable attenuators?
If we distribute them evenly over the maximum possible interval — for
example, 20 attenuators distributed every 250 ps out to 5 ns — then we
will have effectively many fewer data points at even fractions of that
interval.  That is, if we emit a pulse every 190 ps, we’re pretty
okay — the first attenuator provides a pulse image at 60 ps from the
beginning of a pulse interval, the second at 120 ps, then 180 ps, 50,
110, 170, 40, 100, 160, 30, 90, 150, 20, 80, 140, 10, 70, 130, 0, and
finally 60 again, so we have a nice 10-ps effective sampling interval,
just scrambled.  But if we increase the pulse interval to 200 ps, we
suddenly have only four samples per cycle: 50, 100, 150, and 0.

Distributing them at random is of course one possibility, which would
be about as good or bad at all frequencies.

If we have room to make our microstrip 20 ns long, which is only about
a meter and a half serpentined onto a PCB, we might have time to
reconfigure the transistors between one pulse and the next, perhaps
using one of the parallel-memory approaches described above, so at
this magic point we have no lower frequency limit.  AD’s existing
chips claim to achieve turning their pass transistors fully on and off
within 20 ns, so this is apparently physically feasible.

