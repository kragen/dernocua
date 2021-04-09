I think you ought to be able to take a weeks-long EKG
(Elektrokardiogramm) from a person with an easy-to-fabricate
electronic device that could retail under US$25.

Specifically, you should be able to hook up some low-noise analog
amplifiers to a couple of electrodes on your skin to amplify the
millivolt-level EKG signals by 60dB, digitize the resulting signals of
a volt or two with any old ADC (as long as it doesn’t produce too much
noise) at about 1 ksps and 8–12 bits deep, and record the results in
NAND Flash.  You want to pot the whole thing so it doesn’t get eaten
by your sweat, then tape it to your chest for a week or a month.  When
your cellphone is nearby, you can copy over the resulting data
wirelessly for offline analysis.

I think the overall BOM can probably be kept under US$2.50, auguring a
total retail cost under US$25.  The total energy budget is about 1 mW.

This outline is almost feasible:

    |---------------------+--------------------+----------------------------|
    | Item                | BOM cost (qty 100) | Average power dissipation  |
    |---------------------+--------------------+----------------------------|
    | [CR2032 cell][25]   | 37¢                | 1 μW (internal resistance) |
    | ATTiny1614 μC       | 65¢                |                            |
    | (sampling)          |                    | 240 μW                     |
    | (communicating)     |                    | 320 μW                     |
    | MCP6401 opamp       | 27¢                | 120 μW                     |
    | S34MS01G2 Flash     | 104¢               | 35 μW                      |
    | 4×1μF bypass caps   | 6.1¢               | 0.03 μW                    |
    | 4×0.1μF bypass caps | 2.2¢               | (probably less)            |
    |---------------------+--------------------+----------------------------|
    | Total               | 241¢               | 716 μW                     |
    |---------------------+--------------------+----------------------------|

[25]: https://www.digikey.com/en/products/detail/energizer-battery-company/CR2032VP/704858

(It’s suffering from the fact that the microcontroller doesn’t have
enough pins to operate the Flash, it may be entirely too weak, the
resistors for the opamp feedback aren’t included, the opamp may need
to be an inamp, and you probably need another 0.01-μF cap or something
for the antialiasing filter.  Maybe it would be best to build a
prototype with more generously specified parts first before trying to
cost-optimize it.)

BOM outline
-----------

You need a battery, some kind of communication, a microcontroller, an
ADC, an amplifier or two, maybe some Flash, maybe a voltage reference,
maybe a linear regulator or two, maybe a crystal, and maybe a few
passives.  It might be possible to shrink this down to a battery, a
mixed-signal microcontroller with an onboard oscillator, a NAND Flash
chip, and a couple of bypass caps, plus a loop of wire for bit-banged
NFC or BLE communications to your phone.

My thought with the Flash is that 1 ksps for a month is 2.6 billion
samples, and 2.6 gigabytes of Flash uses a lot less power and costs a
lot less than 2.6 gigabytes of SRAM, and costs less and uses
enormously less power than 2.6 gigabytes of DRAM.  And maybe you can
get by with less Flash than that if you can send data to your phone
more often.

I don’t know much about mixed-signal microcontrollers, so I don’t know
which ones to use.

Skin electrodes
---------------

ENIG, a common PCB finish, deposits an 0.1-μm layer of gold (or [a bit
less][0]) on top of a 6-μm layer of nickel on top of exposed PCB
copper.  Gold is safe for skin contact; nickel is safe for 80% of the
population.  You can fab a 2-layer PCB with exposed ENIG pads as
skin-contact electrodes a few centimeters apart.  Certain lead-free
solders might be a more robust nontoxic alternative: tin, silver,
zinc, indium, and (for most people) bismuth and copper are acceptable
ingredients, but antimony, nickel, cobalt, cadmium, and lead are
toxic, and a small number of people are allergic to copper, and a few
more to bismuth.  So, for example, [SAC305 should be fine][1], being
96.5% tin, 3% silver, and 0.5% copper; the eutectic is 95.6:3.5:0.9.
ASTM96TS eliminates the copper, and KappAloy9 is instead the eutectic
of 91% tin, 9% zinc.

[0]: https://www.eurocircuits.com/che-niau-or-enig-electro-less-nickel-immersion-gold/
[1]: https://en.wikipedia.org/wiki/Solder_alloys

It should be possible to connect the skin-contact pads to printed
traces that are covered with solder mask, and which run to
plated-through vias a safe distance away from the exposed pads
themselves to connect them to the other side of the board.

Power, storage, and communication
---------------------------------

A CR2032 lithium coin cell contains about 2.2 kJ of energy ([233 mAh
at 2.7 V][10] is 2.3 kJ).  If we’re aiming for a useful life of a
month, that gives us a power budget of about 840 μW; 1 mW gives us 25
days.  If we want to collect data continuously, we can’t turn the
amplifiers on and off, so they need to be low power enough to use only
a fraction of that.

[10]: https://www.embedded.com/how-much-energy-can-you-really-get-from-a-coin-cell/

Probably the right NAND strategy is to buffer up on the order of
2048–65536 samples in the microcontroller’s onboard SRAM before
applying some kind of lossless data compression to them, powering up
the Flash, and writing a sector or ten to the Flash.

As a ballpark on processing cost, the STM32L0 uses about 230 pJ per
instruction, so if it were using the whole 1 mW power budget it would
be averaging 4.3 MIPS continuously.  The popular STM32F chips use more
like 1500 pJ/insn, which would be more like 0.67 MIPS.  It’s probably
best to shoot for something like 0.07 MIPS, 105 μW.  The devices also
use about 1 μW in stop-with-RTC mode, which takes 5 μs to wake up, and
can thus usefully do a 100-instruction quantum of work before going
back to sleep; so waking up 500 times a second would work, and even
1000 times a second isn’t out of the question.

Writing to NAND costs on the order of 10 nJ/byte, but can usually only
be done a 2048-byte sector at a time.  If we assume that our
compression takes us from 12 bits per sample down to 3, and we’re
taking 1000 samples per second, the average NAND power would be about
4 μW.

More detailed design options
----------------------------

So, we have a 2.7-volt coin cell driving a low-power microcontroller
with an onboard ADC, fed from a low-power differential amp connected
to the person through some 100kΩ resistors or something, storing data
in some NAND Flash at around 1 Hz, and occasionally talking to a phone
with BLE or NFC.  Maybe there’s an antialiasing RC filter in between
the opamp and the ADC, and each of the three chips has a couple of
bypass caps.  The microcontroller has additional bypassing on its Vdda
to reduce the power-supply noise introduced by digital electronics.

So what chips should we use?

Hopefully no discrete voltage regulators at all are necessary with the
appropriate choice of parts.

### Microcontroller: STM32? ###

The STM32F103 seems to be the default microcontroller these days,
though it’s probably too expensive (US$3+).  I’m looking at the short
version of its 117-page datasheet, DocID 13587 revision 17.

The most common one, the STM32F103C8, runs at up to 72 MHz, has dual
1Msps 12-bit ADCs, 64 or 128 KiB of Flash, and 20 KiB of SRAM, with a
single-cycle 32-bit multiplier, and runs on 2.0–3.6 V.  It has an
internal voltage reference rated to be between 1.16 V and 1.24 V
(±3.4%) at -40°–85° with a 100-ppm/° tempco.  I’m thinking that this
is really quite excessive accuracy for our purposes since sticking the
device in a slightly different place would probably attenuate its
voltage more than that.

The power consumption part of the datasheet is extensive.  At an
externally-clocked 72 MHz, where it’s most efficient, it draws 32.8 mA
at 85° with all peripherals disabled; at 2.7 V that’s 89 mW or 1200 pJ
per cycle, which is pretty close to 1200 pJ per instruction.  At
36 MHz, half the clock speed, it uses 19.8 mA, 53 mW, 1500 pJ per
cycle, which would be a lot easier on a coin cell.  You might get a 5%
improvement by dropping the temperature to 25°.  In Stop mode, with
the regulator in Run mode, it claims to use more like 24 μA (65 uW),
though that’s without the oscillators.  Using the internal RC
oscillator instead, at 36 MHz it’s 14.1 mA.

The ADCs, which are connected to the second APB, use 17.5 and
16.07 μA/MHz.  The APB2 bridge uses another 3.75 μA/MHz (p. 51, table
19).  If these are clocked at 2 MHz then ADC2 would use 32 μA or 87 μW
at 2.7 V and the APB would use 8 μA = 20 μW more for a total of
107 μW.

The reference manual RM0008 (Rev 20, 1134 pp.) goes into more detail.
It explains (p. 215) that the ADC is successive-approximation and
can’t be clocked (ADCCLK) over 14 MHz, so I’m guessing it needs 14
clocks per sample.  It’s rated only down to 2.4 V even though the rest
of the device works down to 2.0 V.

The cheapest in-stock STM32 on Digi-Key (other than the STM32G031J6M6)
is the [STM32L011F3P6][11] at US$1.40 in quantity 100.  It runs at
32 MHz.  Its reference manual (RM0377, DocID 025942 rev. 8) explains
that it has a 12-bit successive-approximation ADC with up to 256×
hardware oversampling that can run at up to 1.14 Msps at 12 bits, and
it can run down to 1.65 V.  Its clock can run at a lower speed than
the APB clock (figure 33, p. 278) using a prescaler (1×-256×) from an
independent clock source, or by dividing the APB clock by 1, 2, or 4.
It supports DMA (§13.2, p. 272; §13.5.2, p. 290; §13.5.5, “Managing
converted data using the DMA”, p. 291).

[11]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32L011F3P6/6166957

Oh, but maybe I made an error above: in STM32 Stop mode the clocks are
stopped, so I’m not sure the ADC can run.  To leave the ADC running,
maybe you need to use sleep or low-power sleep mode (p. 144).  But
maybe not; the HSI16 16MHz oscillator can still run in Stop mode
(§6.3.9, p. 151) and you can run the ADC from it (§7.2, p. 166; also
Table 57 in §13.3.5 on p. 279) and it looks like you can run the AHB
PRESC off the HSI16 oscillator and the APB{1,2} PRESC off the AHB
PRESC (Figure 17, clock tree, p. 168), so maybe you *can* use the ADC
in Stop mode.  Not sure about whether the DMA controller works in Stop
mode.

HSI16 is factory calibrated to ±1% which may be too loosey-goosey for
communications.

Looking at the 119-page datasheet (DocID 027973 rev. 5) the
STM32L011x3/4 runs at up to 32MHz, uses 0.29 μA in Stop mode (0.8 μW
at 2.7 V) and “down to” 76 μA/MHz in Run mode (200 μW/MHz, 200
pJ/cycle).  It only has 2KiB SRAM, limiting the possibilities for
pre-storage compression, and 16 KiB Flash.  In sleep mode at 16 MHz,
the device uses 1000 μA (2700 μW), which clearly isn’t acceptable
(§3.1, p. 14) but maybe if you can clock it at 4MHz or 2MHz with a
clock prescaler it would be okay.  The wakeup time from Stop mode is
3.5 μs, which is fine (56 clock cycles at 16MHz).

[This StackOverflow question implies that running the ADC in Stop mode
is impossible on an STM32L4][12].

[12]: https://stackoverflow.com/questions/53173447/optimize-power-consumption-with-stm32l4-adc

### Microcontroller: STM32G? ###

The [STM32G031J6M6][14] mentioned above seems to be new as of 02019.
It’s very interesting: 64MHz, 8 KiB RAM, 32 KiB Flash, 2.5Msps 12-bit
ADC, which can run up to 4.38Msps at 6-bit precision.  The US$1.30
package is an 8-pin SOIC, but it comes in other packages with up to 32
pins ([STM32G031K][15], US$2.78) or even 48 ([STM32G031C][16],
US$2.98).  It seems like an evolution of the STM32F chips: slightly
tighter tolerances on Vrefint (±2.5%), lower Vrefint tempco (30 ppm/°)
and Vddcoeff of 250 ppm/V.  Energy consumption is similar to the
STM32L line: 5.2 mA at 64 MHz and 25° running from Flash, which at
2.7 V is 220 pJ per cycle and probably per instruction.  Low-power run
mode at 2 MHz running from SRAM is 146 μA, 197 pJ per cycle.

[14]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32G031J6M6/10300265
[15]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32G031K8T6/10300267
[16]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32G031C6T6/10300268

The STM32G031J seems like it would probably be a superior choice to
the STM32F or STM32L011 chips for this device, at least if software
support is adequate.

### Microcontroller: CKS32F? ###

CKS makes a line of STM32 replacement chips such as the
[CKS32F051C8T6][17] (US$1.08 in quantity 100 from LCSC).  This is a
drop-in compatible replacement for the STM32F051C8T6, which would cost
more than twice as much at Digi-Key except that it’s out of stock.
(Digi-Key does have a 36-WLCSP version, the [STM32F051T8Y6TR][18], for
US$2.43 in quantity 100.)

Section 5.3.5 of the CKS datasheet, which is entirely in Chinese
except for some plots they probably copied from the ST datasheet, is
power consumption; table 24 on p. 42 says that running from Flash on
the HSI oscillator at 32 MHz and 25° it uses 15.5 mA, which at 2.7 V
would be 1300 pJ per cycle, quite comparable from the STM32F figures.

[17]: https://lcsc.com/product-detail/Other-Processors-and-Microcontrollers-MCUs_CKS-CKS32F051C8T6_C556574.html
[18]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32F051T8Y6TR/5806782

I feel like this kind of thing would probably be about the same as
using an STM32F, but neither CKS nor GD seem to have an STM32L or
STM32G equivalent.

### Microcontrollers: AVRs?  The ATTiny1614 can maybe do 240 μW for 65¢ ###

There are some very cheap AVRs out there that don’t use a lot of
energy, but for example the [30¢ ATTiny25V-15MT][19] only has 128
bytes of RAM, and in general AVRs are too power-hungry for this
application.

The [ATTiny1614][21], which seems to be new since 02018, is 65¢ in
quantity 100 and has 2KiB of SRAM and an ADC.  I think you can get it
to work if you don’t try to run the ADC continuously, but it will suck
up a quarter of the whole power budget.

According to its 598-page datasheet (DS40002204A), it runs at 20MHz
(though only 5 MHz at 2.7 V or less), runs anywhere from 1.8V to 5.5V,
and has dual 10-bit 115-ksps ADCs and 12 GPIOs.  It belongs to the
“tinyAVR 1-series”.  It has a couple of FPGA-style 3-LUTs on the chip
with it (“configurable custom logic”), and an analog comparator, but
no opamps or differential ADCs.

Active power consumption at 5MHz and 3V is given as 3.2mA (table 36-4,
§36.4, p. 508), which works out to a lamentable 1900 pJ per
cycle — particularly lamentable considering these are 8-bit
instructions.  “Standby” power consumption at 3V is given as about
0.7 μA with a 32kHz oscillator running (internal or external);
“power-down” consumption, with all peripherals stopped, is given as
0.1 μA (table 36-5).  These numbers are quite adequate.  But “idle”
power consumption would be 0.6 mA at 5 MHz and 3V, which is far too
much.

[21]: https://www.digikey.com/en/products/detail/microchip-technology/ATTINY1614-SSNR/7354616

However, no figures are given for “standby” with a high-speed
oscillator running!

So, if we can stay in “standby” or “power-down” most of the time, this
chip might be a cheaper but less efficient alternative to the STM32.
The question is, can it wake up 1000 times a second to take a sample,
or leave the ADC running while in “standby”?

§10.3.4.1.1 says the internal OSC20M 16/20MHz oscillator starts up in
“the analog start-up time plus four oscillator cycles”.  There’s also
a 32.768 kHz internal oscillator (OSCULP32K, §10.3.4.1.2) which can be
used as a clock source (CLKSEL[1:0] = 0x1, §10.5.1; see also the block
diagram in Figure 10-1, §0.2.1, p. 75); I suspect that might be fast
enough for the ADC.

§11 describes the sleep controller.  §11.3.2.1 says, “SleepWalking is
available for the ADC module,” but doesn’t explain further, but Table
11-1 says the ADCs *can* be enabled in idle or standby mode, but not
power-down mode; the RTC, PTC (“peripheral touch controller”), TCBn
(“timer/counter type B #n”), BOD, and WDT can too.  Moreover the
ADC/PTC interrupts can wake the CPU.  Wakeup time is 6 main clock
cycles, which is totally insignificant, plus possibly time to restart
the clock, which could probably be avoided here, although table 36-6
in §36.5 on p. 509 says 10 μs.  That’s still fine though.

§30.1 says the ADC has “accumulation of up to 64 samples per
conversion,” which I think means oversampling (giving 13 bits of
precision), and “interrupt available on conversion complete”, which
would wake up the CPU.  I don’t think there’s any DMA, but with
6-clock-cycle wakeup I don’t think we need it.

§30.3.2.2 (p. 431) shows the ADC clock prescaler dividing `CLK_PER` by
anything from 2 to 256 to get `CLK_ADC`.  So if `CLK_PER` were 5 MHz
(maybe from dividing OSC20M by 4) we could run `CLK_ADC` at anywhere
from 19.5 kHz to 2.5 MHz, both of which are outside the 50 kHz–1.5 MHz
range demanded on that page “for maximum resolution”.  A normal
conversion takes 13 `CLK_ADC` cycles (§30.3.2.3, p. 432) so if we want
1ksps with 64× oversampling then we want `CLK_ADC` to be about
832 kHz; probably the best compromise is setting `CLK_ADC` to
`CLK_PER`/8 = 625 kHz (by setting the PRESC field in CTRLC to 0x2,
§30.5.3, p. 440) and using 32× oversampling for 1.502 ksps (by setting
the SAMPNUM field in CTRLB to 0x5, §30.5.2, p. 439).

So then I guess every 666 μs we get an ADC interrupt, wake up another
microsecond later, store the conversion result in RAM, and then go
back to standby?  Probably setting the ADC to “free-running mode”
would be best so the clock doesn’t ever get turned off — but see below
for why this isn’t viable.

If we were stuck with a 32.768-kHz oscillator for `CLK_PER` then
`CLK_ADC` would be, at best, 16.384 kHz, which the datasheet says is
too slow for full accuracy; but then we’d get 1.260 ksps without any
oversampling.

Table 36-7 in §36.6 (p. 510) says the ADC itself uses 325 μA at 50ksps
or 340 μA at 100ksps.  That is, by itself, 0.92 mW at 2.7 V, which is
probably enough to blow our 1-mW power budget.  Also, OSC20M uses
125 μA.  So, free-running mode is far too power-hungry.

A more exotic “compressed sensing” approach might be viable.  Instead
of sampling the signal every 1000 μs, sample it at a random time
within each 1000-μs interval, awoken by TCB0.  You need 10 μs to come
out of standby mode, 8 μs to start up OSC20M (table 36-12, §36.9,
p. 512), running with `CLK_PER` at 5 MHz because we’re at 2.7V, and
with `CLK_ADC` configured as 5 MHz/4 = 1.25MHz, another 10.4 μs to
take the sample.  This works out to 28.4 μs or a 2.84% duty cycle, so
the 8.4 mW when active averages out to 240 μW: suboptimal but possibly
acceptable.

Actually if you do the antialiasing filter on the analog side, like
with a simple passive RC filter, you can just sample every 1000 μs
using that same approach.  So, 240 μW it is.

There are also things like the [AVR32DA28T][20] with 4 KiB of RAM and
running on 4.7 mA at 24 MHz, anywhere from 1.8V to 5.5V, with
different power-down modes ranging from 650 nA to 2.3 mA.  Despite the
name, it’s an 8-bit AVR, but it costs US$1.20 in quantity 100 anyway!

[19]: https://www.digikey.com/en/products/detail/microchip-technology/ATTINY25V-15MT/1914688
[20]: https://www.digikey.com/en/products/detail/microchip-technology/AVR32DA28T-I-SO/12663969

### Discrete amplifiers ###

We don’t care much about signals above about 500 Hz or below about
0.1 Hz, so the amp or amps don’t need to be fast, low-offset,
chopper-stabilized, or any of that good stuff.  But we do need a lot
of gain and pretty low power.  We can bias the signal to be halfway
between our rails, so we don’t need rail-to-rail inputs or outputs.
And we only need one differential amp if we only have two electrodes.
The input impedance is the skin contact resistance; without gel this
is standardly modeled as 1.5 kΩ but can easily be up to 1 MΩ or so, so
our input bias current needs to be about 1 nA or less.

500 Hz bandwidth and a closed-loop gain of 1000 means we need at least
half a MHz of gain-bandwidth product.

My first thought was that this needs to be high precision, so an
instrumentation amp is in order.

The [MCP6N11][2] is Digi-Key’s cheapest in-stock INA.  But it costs
US$1.42 in quantity 1, just about blowing out our hopes for a US$2 BOM
in a single shot.  It’s 35 MHz GBW (about two orders of magnitude more
than we need), 10 pA input bias, rail-to-rail output, and uses 800μA,
which would also just about blow out our power budget.

[2]: https://www.digikey.com/en/products/detail/microchip-technology/MCP6N11-100E-SN/2802058

Also, though, the excellent properties of INAs are useless here.
Input impedance matching?  Don’t need it, no RF here.  Low drift?
Irrelevant.  Low noise?  Well, our input signal isn’t actually all
that tiny.  High CMRR?  The whole circuit is floating so this doesn’t
matter at all.

Digi-Key’s cheapest in-stock opamp in quantity 1 is the
[MCP6001RT-I/OT][3], which costs US$0.24 in quantity 1 or US$0.18 in
quantity 100.  It’s a teensy little SOT23-5 with 1 MHz GBW, 1 pA input
bias, 4.5 mV input offset voltage, drawing 100 μA of power at down to
1.8 V, so it seems like it might be adequate.  [The 50-page MCP6001
datasheet][4] has lots of data, including an 86dB PSRR, 88dB open-loop
gain, 6 mA output short-circuit current even at 1.8 V, 50–170 μA
quiescent current, and 6.1-μV input noise voltage.  Though it claims
28 nV/√Hz, which would be only 0.6 μV in the 500-Hz bandwidth of
interest, the 1/f knee in figure 2-12 on p.8 (“Input noise voltage
density vs. frequency”) is around 1 kHz, so almost all this noise is
actually in range.

[3]: https://www.digikey.com/en/products/detail/microchip-technology/MCP6001RT-I-OT/562449
[4]: https://ww1.microchip.com/downloads/en/DeviceDoc/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf

However, in quantity 100, Digi-Key also has in stock (at the moment)
the Diodes Inc. [AZ4558CMTR-G1][5] *dual* op-amp for only 16.7¢, or
11¢ in quantity 500.  But in quantity 1, they’ll charge you 40¢ for
the damn thing.  *It* has *5.5* MHz GBW and lower input noise of
10 nV/√Hz, but because it’s bipolar, it uses *2500* μA of supply
current (typical!  The max is 4500!), making it far too power-hungry
for this application—it works up to ±20 V supply and 60 mA output.

[5]: https://www.digikey.com/en/products/detail/diodes-incorporated/AZ4558CMTR-G1/5306054

A TI [LM358LVIDDFR][6] dual op-amp is just as cheap (19¢ in quantity
100, 10.1¢ in quantity 1000, 41¢ in quantity 1) and uses even less
power (90 μA per channel), and also has 1 MHz of GBW.  It has a lower
input offset voltage, which we don’t care about (1 mV) and a higher
15 pA input bias current, which still isn’t high enough to cause
problems.  It has about the same noise (5.1 μV peak-to-peak,
40 nV/√Hz) which is probably plenty low.  One drawback is that it's
only specced to run down to 2.7 V instead of the Microchip’s 1.8 V.
The [LM321 single-device package of the same opamp][7] might be a
better fit—half the quiescent current—but costs slightly *more*, 20¢
in quantity 100.

[6]: https://www.digikey.com/en/products/detail/texas-instruments/LM358LVIDDFR/10715375
[7]: https://www.digikey.com/en/products/detail/texas-instruments/LM321LVIDBVR/9685426

There are *much* lower-power opamps than that, though.  TI’s
[OPA379][8] claims 2.9 μA, but isn't suitable—it only has 90 kHz GBW
and costs US$1.24 in quantity 1, 86¢ in quantity 100, or 59¢ in
quantity 1000.  This astonishingly low power usage is the very first
thing in the datasheet title: “1.8V, 2.9μA, 90kHz Rail-to-Rail I/O
OPERATIONAL AMPLIFIERS”.

[8]: https://www.digikey.com/en/products/detail/texas-instruments/OPA379AIDCKR/1572627

Another possible option, though, is Microchip’s [MCP6401][9] at 27¢
(37¢ in quantity 1), which runs on 1.8–6 V and 45 μA (70 μA max),
delivering 1 MHz GBW and 3.6 μV p-p input noise.  Its open-loop gain
at 500 Hz is supposedly still about 65 dB.

[9]: https://www.digikey.com/en/products/detail/microchip-technology/MCP6401UT-E-OT/2332835

### NAND Flash ###

We need to be able to buffer up some EKG data during times when the
user’s phone is out of communication range.  If we’re recording 1000
samples per second and can manage to use 8 bits per sample, that’s
1000 bytes per second; 2048 bytes of RAM only buffers up 2 seconds’
worth.  24 hours’ worth would be 86.4 megabytes of data.  The only
practical way to buffer up so much data at under a milliwatt is
nonvolatile memory, of which NAND Flash is the cheapest and also takes
the least power to write.

Something like the “obsolete” [GigaDevice GD5F1GQ4RF9IGR][71] might be
a good start.  It’s 128 mebibytes of NAND Flash in an 8-LGA with an
SPI/dual-SPI/quad-SPI interface that can run at 100MHz.  In quantity
100, it costs a dismaying US$2.21, instantly torpedoing any hopes of
the US$2 BOM cost mentioned above.  Its top voltage is 2V, so it would
need an external linear regulator.  Parallel-interface NAND Flash
chips like the S34MS01G2 (also 128 MiB) are cheaper but require lots
of I/O lines.  Like 15.  It uses 10 μA at idle.

[71]: https://www.digikey.com/en/products/detail/gigadevice-semiconductor-hk-limited/GD5F1GQ4RF9IGR/9484745

2-gibibit Flash seems to start at US$2.60 in quantity 100 with things
like the Micron MT29F2G08, with no datasheet available, or US$2.79
with the [Kioxia TC58BVG1S3HTA00][13], which runs on 2.7–3.6 V, uses
30 mA in operation and 50 μA in standby, and has a serial interface.
Programming a 2048+64-byte page takes 330 μs, erasing a 64-page block
takes 2.5 ms, and despite its 48 pins it looks like you can run it on
15 GPIOs or less.  Doing the math, erasing takes 19 ns per byte,
writing takes 161 ns per byte, and the total 180 ns at 30 mA and 2.7 V
takes 15 nJ per byte.  This is a bit higher than the 4.4 nJ number I
computed for the S34MS01G2, but not ridiculous.  1000 bytes per second
at 15 nJ is 15 μW, which is adequately small.  (NOR Flash takes about
100× as much power to write, which would blow our power budget.)

The Kioxia part seems to be specced for 40MHz, but probably 8MHz is a
more realistic speed for driving it from a cheap microcontroller.
This adds another 256 μs or so of time to write each page, which might
or might not double its power usage, but either way it’s fine.

[13]: https://www.digikey.com/en/products/detail/kioxia-america-inc/TC58BVG1S3HTA00/5226306

Although Kioxia’s pricing suggests that maybe 1-gibibit NAND is
already at or above the linear pricing region, Digi-Key only stocks
one 512-mebibit NAND chip, the Winbond W25N512GVEIG, which is actually
*more* expensive than the gibibit chips.

### Bypass caps ###

We probably can’t get by without bypassing, and to get down below
1 mW, we need at least 10kΩ leakage resistance in all the bypass caps
put together.  This is a sufficiently undemanding spec that I think
random ceramics will be fine; we don’t need to go for 30V or 100V
caps, which would be a way to cut down bypass losses further.

Sufficiently beefy bypass caps might make a coin-cell battery last
longer by preventing current draw at the battery from spiking to 30 mA
or more during normal use.

The 0.55¢ Samsung X5R [CL05A104KA5NNNC][25] seems like a reasonable
0.1μF bypass cap, though the datasheet doesn’t specify leakage, and,
e.g., the Yageo X5R 0201 [1.52¢ Yageo CC0201MRX5R5BB105][26] is
probably adequate for a 1-μF bypass cap.  Its datasheet suggests
insulation resistance of 10 GΩ “or Rins × Cr ≥ 50Ω.F, whichever is
less,” which works out to just 1 GΩ.  So it exceeds requirements by
four orders of magnitude in this case.

[25]: https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05A104KA5NNNC/3886701
[26]: https://www.digikey.com/en/products/detail/yageo/CC0201MRX5R5BB105/5195022

### Bluetooth Low Energy ###

[Wikipedia say][22] BLE give 0.27–1.37 Mbps of “application
throughput” for 0.01–0.50 W and under 15 mA.  Suppose this means we
can get 1 Mbps for 40 mW (15 mA at 2.7 V), which seems plausible.
Well, that’s 40 nJ per bit, or 320 nJ/byte.  It’s about an 0.8% duty
cycle if we’re producing 1000 bytes per second of sample data, as
suggested above, but that still works out to 320 μW, which is not
impossible but is a major part of our energy budget.

[22]: https://en.wikipedia.org/wiki/Bluetooth_LE

Transmitting a full 128-MiB Flash chip load of EKG data would take
almost 20 minutes at 1 Mbps, which is annoyingly slow but not
infeasible.

It may be feasible to [bitbang BLE on an ATTiny24 and an nRF24L01+, at
least for transmitting][23] but this is probably not really viable
without using BLE hardware.

[23]: https://dmitry.gr/?r=05.Projects&proj=11.%20Bluetooth%20LE%20fakery

### Near-field communication ###

Lots of cellphones and other hand computers now support [ISO/IEC
18000-3 13.56 MHz NFC][24], at 106–424 kbps, and also under 15 mA;
because the data rate is five times slower, the cost per bit is
probably about five times higher, or 1.5 mW.

[24]: https://en.wikipedia.org/wiki/Near-field_communication

Wikipedia claims NFC communication can be added for 10¢, but I don’t
know how to do that.  [It seems to be popular][25].  One popular NFC
chip is the [NXP PN532][26], which I guess is an 8051 with NFC
hardware, but [it seems to cost more like 700¢][27]; even a cheaper
alternative like the [NXP 512][28] is still almost US$4.  Nobody seems
to be bitbanging it successfully either.  ST sells a US$1.33 8-SOIC
called the [M24LR64E-RMN6T/2][29], which is a pretty complete
energy-harvesting RFID tag that also supports I²C, but it seems like
that’s only to read and write its memory, not to use it as a
transceiver.

[25]: https://hackaday.com/tag/nfc/
[26]: https://www.makerfabs.com/pn532-nfc-module-v3.html
[27]: https://www.digikey.com/en/products/detail/nxp-usa-inc/PN5321A3HN-C106-55/2296486
[28]: https://www.digikey.com/en/products/detail/nxp-usa-inc/PN5120A0HN-C1-518/11515556
[29]: https://www.digikey.com/en/products/detail/stmicroelectronics/M24LR64E-RMN6T-2/4156627