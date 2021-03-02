I spent some time trying to figure out what it would take to be able
to read, write, and interactively compute, without a connection to a
power grid, with maximal autonomy.  See also file `microlisp.md` for
thoughts on how to design a software environment.

Lead-acid batteries: 9–36 kJ/US$ at retail, mostly around 20 kJ/US$
-------------------------------------------------------------------

Lead-acid batteries are generally cheaper than the lithium-ion type,
even in 02021.  At the very low end joules per buck drops
dramatically; [a 1.3-amp-hour 12V HiStarX LA612 battery goes for
AR$900][0]; at AR$147/US$ that’s US$6.10 for 56 kJ, or 9.2 kJ/US$.  By
contrast, a [2-kg 7-amp-hour Risttone battery goes for AR$1220][1],
US$8.30, 300 kJ, 36 kJ/US$.  A [24-amp-hour deep-cycle golf-cart Press
PR12240D goes for AR$9000][2], US$61, which is getting low again: 17
kJ/US$; while car starter batteries are in theory much cheaper, like
[a Rosler 65-amp-hour starter goes for AR$4900][3], US$33, 84 kJ/US$,
but of course you can only use a fraction of that before you start
killing the battery.  Even with starter batteries, prices per joule go
way up at the low end: [a Yuasa 5.3-amp-hour 1.5kg 12N5-3B 12-volt
motorcycle starter battery][10] (230 kJ) is [sold for AR$2500][11]
(US$17, 13 kJ/US$).

[0]: https://articulo.mercadolibre.com.ar/MLA-904920119-bateria-de-gel-12v-13ah-recargable-luz-emergencia-ups-_JM
[1]: https://articulo.mercadolibre.com.ar/MLA-871599822-bateria-de-gel-12v-7a-amper-sistema-alarmas-cerco-electrico-_JM
[2]: https://articulo.mercadolibre.com.ar/MLA-671410956-bateria-12v-24ah-press-ciclo-profundo-moto-carros-golf-_JM
[3]: https://articulo.mercadolibre.com.ar/MLA-856727008-bateria-12x65-super-oferta-nueva-_JM
[10]: https://www.yuasa.es/batteries/moto-e-powersport/convencional-de-12-voltios/12n5-3b.html
[11]: https://articulo.mercadolibre.com.ar/MLA-853988819-bateria-moto-yuasa-12n5-3b-motomel-c-110-0518-_JM

Digging further suggests higher-capacity options like [the 2.8-kg
9-amp-hour Moura 12MVA-9][19] for AR$2500 (US$17, 390 kJ, 23 kJ/US$),
or, in the extreme, [the Ultracell UCG 100-12 100-amp-hour deep-cycle
gel cell][18] for AR$38400 (4.3 MJ, US$261, 17 kJ/US$).

[18]: https://articulo.mercadolibre.com.ar/MLA-852742149-bateria-ciclo-profundo-gel-12v-100ah-ultracell-ppanel-solar-_JM
[19]: https://articulo.mercadolibre.com.ar/MLA-867421155-bateria-moura-12v-9ah-gel-ups-alarmas-paneles-solares-_JM

Low-power lithium-ion batteries are more expensive at 3–16 kJ/US$
-----------------------------------------------------------------

Lithium-ion batteries are trickier to buy because of the profusion of
fakery, but [this Sanyo NCR20700b cell is specified at 4250mAh and
3.7V for AR$2500][4], which would be US$17 and 57 kJ, or only 3.3
kJ/US$.  (The seller falsely claims it’s an 18650.  It’s tested at
[3.7–4.2 amp hours at 0.2–15 amps of discharge rate][12] by what I
think is an independent tester, who weighed it at 61 g.)  But there
are a lot of fake lithium-ion batteries like this [UltroFite GH 18650
“6800 mAh” which sells for AR$427][5], which would be 91 kJ, US$2.90,
and 31 kJ/$, nearly an order of magnitude cheaper and up in the
lead-acid price range.  (Lithium-ion batteries are already immensely
cheaper per watt or amp rather than per joule, but so are capacitors.)
USB “power banks” are even less controlled, but much more convenient
to use; [this Tedge H555 claims 10 amp-hours for AR$1700][6],
US$11.50, 180 kJ, 16 kJ/$, and it probably has 18650s inside, which
could be replaced, while [this offbrand Libercam powerbank claims 20
amp-hours for AR$1500][9] and is too thin to contain 18650s.  I'm
guessing it’s fake.

My “10050 mAh” powerbank (180 kJ) can recharge my phone about four
times, which can keep it alive for about a week.

[4]: https://articulo.mercadolibre.com.ar/MLA-756391264-panasonic-sanyo-ncr20700b-4250mah-10a-20700-ion-litio-37v-_JM
[5]: https://articulo.mercadolibre.com.ar/MLA-816550268-pila-bateria-recargable-18650-6800mah-37v-para-linterna-_JM
[6]: https://articulo.mercadolibre.com.ar/MLA-795347543-cargador-bateria-portatil-powerbank-2-usb-10000-mah-tedge-_JM
[9]: https://articulo.mercadolibre.com.ar/MLA-856270207-power-bank-cargador-portatil-20000-mah-celular-micro-usb-_JM
[12]: https://lygte-info.dk/review/batteries2012/Sanyo%20NCR20700B%204000mAh%20%28Red%29%20UK.html

High-power lithium batteries are down around 1.4–1.6 kJ/US$ but 25 W/US$
------------------------------------------------------------------------

I thought maybe the motorcycle starter batteries were about to get
murdered by lithium, since lithium is so great at rapid discharge, but
it’s not so clear.  The Yuasa 12N5-3B above is only 35 or 39 cold
cranking amps, depending on who you believe, which is only like 450
watts (26 W/US$).  At 3.7 volts and 15 amps the Sanyo cell, which is
the same US$17 price, delivers only 56 watts; you’d need 9 of them (9
times the price!)  to deliver the same starter power as the lead-acid
beast, though admittedly the resulting 0.550 kg of lithium battery is
noticeably lighter the 1.5 kg of the Yuasa battery.

However, 4 amp hours and 15 amps is a discharge rate of only “3.75C”,
and [lithium-ion batteries for drones][13] come in “C ratings” of
“15C”, “20C”, “25C”, “30C”, and even “50C”, though at a substantial
penalty in joules per buck.  Does this make them competitive for
starting motorcycles?  Well, a [Blomiky SDL-853562 7.4V 1600mAh 25C
radio-controlled car battery][14], for example, is listed for AR$6900
(US$47) and hypothetically ought to hold only 43 kJ (0.91 kJ/US$) but
be able to deliver 40 amps.  But that’s still only 300 watts, and it
costs more than twice as much as the lead-acid battery.  Cheaper drone
batteries like [this Kitch Tech 30C 7.5-V 1200-mAh YZ-803063 for
AR$3500][15] come closer — if real, that’s 32 kJ for US$24 (1.4
kJ/US$), 36 amps, and 270 watts, but lead-acid still beats it by a
substantial factor.  [This Zippy 25C 2200mAh 11.1V drone battery][16]
can purportedly deliver 610 watts (or 850 watts, 35C, in bursts) and
is listed at only AR$4700 (US$32, 2.7 kJ/US$).  850 W / US$32 is
27 W/US$, within a stone’s throw of the Yuasa price — but far from
dramatically undercutting it.

Moreover, [advertised C ratings are often fake, even outside
Argentina][17].

[13]: https://electronica.mercadolibre.com.ar/drones-accesorios-repuestos-baterias/
[14]: https://articulo.mercadolibre.com.ar/MLA-843144652-bateria-lipo-74v-1600mah-25c-t-connector-blomiky-_JM
[15]: https://articulo.mercadolibre.com.ar/MLA-873577542-bateria-pila-lipo-yz-803063-1200mah-75v-30c-drone-drones-_JM
[16]: https://articulo.mercadolibre.com.ar/MLA-741554734-bateria-lipo-zippy-compact-2200mah-3s-25c-111v-xt60-_JM
[17]: https://oscarliang.com/lipo-battery-c-rating/

Laptops need tens of watts and often run off old 18650s
-------------------------------------------------------

My “new” HP laptop’s `/sys/class/power_supply/BAT0/power_now` produces
numbers ranging from about 11 million to about 32 million, with CPU
usage seeming to be the biggest determinant.  (I’m guessing these are
microwatts.)  Its battery (four 18650 cells, I think) is so shot that
it only runs for about an hour and a half on it, which suggests a
capacity in the 60–180 kJ range, probably close to 100 kJ.  The (HP
V104) notebook battery is *labeled as* “14.8 V” and “41Wh” (though the
broken off-brand spare says “2200mAh/33Wh”), and
`/sys/class/power_supply/BAT0/energy_full_design` says 23206000, and
bizarrely so does `energy_full`, and `energy_now` approaches that
level (20364000 at the moment).  `cycle_count` reports 208, but then
after popping the battery out and back in, only 200.  [The docs
say][7] that energy is reported in μWh; `power_now` is not documented
there but [SuperUser says it’s in μW][8], and indeed 23 watt-hours
divided by 15 watts is about an hour and a half.  I suspect the
battery is worn out down to 57% capacity and just doesn’t report its
design capacity.  23 Wh at 14.8 V is 1600 mAh, which is in a
reasonable range for the half-worn-out 18650s it presumably contains.

[7]: https://www.kernel.org/doc/Documentation/power/power_supply_class.txt
[8]: https://superuser.com/questions/808397/understanding-the-output-of-sys-class-power-supply-bat0-uevent

It can do something like 10 or 15 billion instructions per second, so
this is something like 2000–3000 pJ per instruction, including the
monitor.

Prospects for energy-independent computing
------------------------------------------

So I was thinking it might be worthwhile to buy a 12-volt gel cell
like those mentioned above and rig up some power supplies for offline
computation.  The AR$1200 7-amp-hour Risttone battery mentioned above
ought to be able to run this laptop at 15 watts for 6 hours (given
appropriate boost conversion), or recharge this cellphone about 6
times, and there might be better deals out there too.  Two or three
such batteries, or a single larger battery, could perhaps power the
laptop, or a fan, through a long night.

Standard photovoltaic solar panel modules are 990 mm × 1650 mm or
thereabouts, deliver 200–400 Wp, and, at retail in Argentina, cost
[AR$12000][20]–[AR$24000][21] (US$80–160), on the order of 30¢–40¢/Wp.
Smaller panels like [this AR$3200 20-Wp jobbie][22] do exist but cost
more per watt (US$22, US$1.09/Wp in this case).

[20]: https://articulo.mercadolibre.com.ar/MLA-882723840-panel-solar-solamerica-260w-tipo-250w-270w-280w-12v24v-_JM
[21]: https://articulo.mercadolibre.com.ar/MLA-898045941-panel-solar-jinko-solar-mono-perc-405w-media-celda-_JM
[22]: https://articulo.mercadolibre.com.ar/MLA-718610857-panel-pantalla-solar-20w-watts-policristalino-111-amper-amp-_JM

Suppose the solar capacity factor for residential solar panels here is
15%, so 100 Wp delivers 15 watts average.  (It’s fairly sunny here in
Buenos Aires, but we get more clouds than California and Arizona
deserts with their 29% and 25% capacity factors, and also residential
panels may have to deal with shadows and suboptimal angling.)  And
suppose we want 24 hours of “autonomy”, meaning, we can keep computing
even when it’s super cloudy; so a watt of average usage requires 24
watt-hours (86 kJ) of battery.

So each watt of usage requires 86 kJ of battery, which at 20 kJ/US$
costs US$4.30, plus 7 Wp of solar panel, about US$2.30 at retail, for
a total of US$6.60, plus some amount of power electronics.  So running
the laptop all the time at 15 watts would cost a bit over US$100 of
equipment; at 32 watts we’re talking US$210.  I paid AR$50k (at the
time, about US$320) for the laptop a couple months ago.  So powering
it autonomously nearly doubles its cost!  Also, 32 watts average at a
15% capacity factor means 213 watts of solar panel, which is a whole
square-meter panel.  It would occupy a significant fraction of the
balcony and might attract unwanted attention.

Lower-power computing
---------------------

Ordinary microcontrollers (without a monitor) are comparable to the
laptop’s 2000–3000 pJ/intruction power usage, or a bit lower, or much
worse for floating-point or SIMDable computations, but low-power
microcontrollers like the STM32L0 or the Atmel SAMD picoPower ARM
chips are in the 150–250 pJ/insn range, and the MSP430 just a little
higher (though only 16-bit).

Recent reports are that [the new RISC-V-based microcontroller line
“GD32V”][23] are better by another factor of 3 or so.  [The datasheet
for the GD32VF103][24] doesn’t yet provide a lot of detail on lowest
possible power consumption, but the numbers they do give say that it
uses about 2.1 mW/MHz at 2 MHz, which drops to 0.7 mW/MHz at 36–48 MHz
and 0.6 mW/MHz at 72–108 MHz, at 3.3 V, executing from Flash, with all
peripherals off.  You can probably improve this by running at 2.6 V,
which is still kind of sad because the RISC-V core itself is running
at 1.2 V.  (The datasheet and user manual claim it’s a Harvard
architecture, so you probably can’t execute from RAM, and executing
from RAM does improve power consumption on ARM microcontrollers.)  If
we assume that’s about one instruction per clock cycle, 0.6 mW/MHz is
also 0.6 mW/MIPS (not Dhrystone MIPS!), which works out to 600 pJ per
instruction.  This is a little better than the STM32F0 (which I think
is 12 mA at 3.6 V and 48 MHz: 900 pJ/instruction) but a lot worse than
the STM32L0.

[23]: http://www.gd32mcu.com/en/product/risc
[24]: https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/

### Estimating the necessary performance for basic interactive computation: 0.1 DMIPS ###

My previous estimate in Dercuano was that basic interactive
computation like word processing takes about 7500 32-bit instructions
per keystroke.  At one point, I said, “WordStar on a 2MHz (≈0.5MIPS)
8-bit CPU would sometimes fall behind your typing a bit,” but then
later calculated that a Commodore 64 (now [AR$12000][28] = US$80) or
Apple ][ would only do about 200 000 8-bit instructions per second and
were usable for word processing, and a 32-bit instruction is roughly
equivalent to two 8-bit instructions, so you need about 0.1 32-bit
MIPS, and you might be typing like 160 wpm (13.3 keystrokes per
second), which works out to about 7500 instructions per keystroke.

Also in Dercuano, I estimated that painting text in a framebuffer fast
enough that it doesn’t slow down reading at 350wpm might take about 50
bytes of I/O per glyph and 100 instructions / glyph × 350 wpm × 6
glyphs / word × 1 minute / 60 seconds = 3500 instructions/second.  But
that’s orders of magnitude lower than the computations I discussed
above.  Indeed, old computers like the Sinclair ZX-81 with its
3.25-MHz Z-80, lacking an external framebuffer, would use the CPU to
repaint the screen 50 times a second.

#### Modern microcontrollers run at around 1 Dhrystone MIPS per MHz ####

How fast are modern microcontrollers?  [dannyf compiled Dhrystone 2.1
with a modern compiler][48] and got 921 repetitions per second per MHz
on an STM32F1 with what I guess is the vendor compiler, or 736 with
GCC; to [convert that into Dhrystone MIPS I think we divide by
1757][58], so that’s 0.52 and 0.42 DMIPS/MHz.  However, other
commenters say the ARM Cortex-M0+ used in the STM32F1 is 0.93 DMIPS
per MHz, and the STM32F103x8/STM32F103xB datasheet says it's actually
“1.25 DMIPS/MHz (Dhrystone 2.1)”.  And apparently [a CoreMark is about
half a DMIP][49].

[58]: https://en.wikipedia.org/wiki/Dhrystone#Results
[48]: https://www.eevblog.com/forum/microcontrollers/dhrystone-2-1-on-mcus/
[49]: http://linuxgizmos.com/hifive-unmatched-sbc-showcases-new-fu740-risc-v-soc/
[50]: http://www.homebrewcpu.com/new_stuff.htm

#### Historical computer performance: a 1-MHz 6502 was a bit less than 0.1 DMIPS ####

A Commodore 64 or Apple ][ were also capable of running the VisiCalc
spreadsheet, the Berkeley Softworks GEOS GUI and geoPaint and whatnot,
and Contiki, though not, say, the GEM desktop.  The 5MHz and sub-MIPS
Apple Lisa was capable of running a non-janky GUI, but even on the
Macintosh (7.8 some MHz, 16-bit ALU, [0.40–0.52][25] Dhrystone MIPS
even though [some 68000 machines were faster][26]) it was slow enough
that you could see the order in which the lines of dropdown menus got
painted, top to bottom.  [With GEOS on the Commodore 64, though, you
can see that it paints each line of the dropdown menu left to right,
even with a memory expander cartridge,][47] and in geoWrite, typing
onto the end of a short line of centered text makes it flicker quite
noticeably as it gets erased and repainted left to right in the new
position.

[25]: http://performance.netlib.org/performance/html/dhrystone.data.col0.html
[26]: https://en.wikipedia.org/wiki/Instructions_per_second
[28]: https://articulo.mercadolibre.com.ar/MLA-896239873-computadora-commodore-64-c-funciona-liquido-dream-_JM
[47]: https://youtu.be/gnFavusEwVE?t=1146 "10MARC Presents: GEOS Adventures Part 1"

The [Magic-1 4-MHz homebrew microcoded TTL minicomputer gets 506
Dhrystone repetitions per second][50], while the same page says the
Mac 512 gets 625. I guess those work out to ` (mapcar (lambda (x) (/ x
1757.0)) '(506 625)) ` 0.29 and 0.36 respectively.  0.36 is a little
lower than the 0.40–0.52 range in the netlib page cited above, but
it's pretty close.  The same page reports that a 2.5-MHz Z-80 did 91
Dhrystones per second, which is 36.4 Dhrystones per second per MHz,
and that an Apple IIe only squoze 37 Dhrystones per second out of its
1.02 MHz 65C02, which by the same calculation is ` (/ 37 1757.0)
` = 0.021 DMIPS, and thus 0.021 DMIPS/MHz.  And so that seems to be
close to the minimum CPU power to run a usable GUI.

So the STM32F1 does about 50 (!) times as much Dhrystone work per
clock cycle, and about 4–5 times as many instructions per clock cycle,
so it’s doing about 10–12 times as much Dhrystone work per
*instruction*.  This is substantially larger than the factor of 2 I
had guesstimated for the 8-bit vs. 32-bit difference, and I suspect
it’s unrealistically large — an artifact of trying to benchmark the
C-unfriendly 6502 with a C program, and perhaps using a lousy compiler
to boot.

#### [SRI’s oN-Line System][52] ran on an SDS 940 system at around 0.1 DMIPS ####

[52]: https://en.wikipedia.org/wiki/NLS_%28computer_system%29

The Mother of All Demos, demonstrating the mouse, windowing, networked
hypertext, multimedia computerized documents including images, and
IDEs, was done in 01968 on an SDS 940 (one of some 60 ever built, over
a third of which were sold to Tymshare) which supported 6 concurrent
users, using specialized analog hardware for video compositing.  The
system’s interactive response slowed notably when more than one person
was using it actively.  The SDS 940 had a 24-bit CPU and up to 64
kibiwords of 24-bit memory.  [An integer add instruction on its
predecessor the 930 took 3.5 μs][53], and the memory’s cycle time was
1.75 μs, so we can estimate it roughly at 200,000 instructions per
second, about the same as the 1-MHz 6502 in the Commodore 64; but they
were 24-bit instructions instead of 8-bit instructions, so it might
have been perhaps twice as fast as the C64.

The 940 they were running NLS on [was exactly the same in those
respects][54]: 0.7-μs memory access time, 1.75-μs cycle time, 3.5-μs
“typical execution time” for integer addition “(including memory
access and indexing)”, and 7.0 μs for integer multiply.

The manual/brochure for the machine, which was built for the Berkeley
Timesharing System under which NLS ran, says:

> System response times are a function of the number of active users.
> Typical times are:
> 
> 6 active users . . . . . 1 second  
> 20 active users . . . . . 2 seconds  
> 32 active users . . . . . 3 seconds  

[53]: https://en.wikipedia.org/wiki/SDS_9_Series#SDS_930
[54]: http://archive.computerhistory.org/resources/access/text/2010/06/102687219-05-08-acc.pdf "SDS 940 Time-Sharing Computer System, 18 pp."

It's very unlikely that anybody ever ran Dhrystone on the SDS 940; its
successor the SDS 945 was announced in 01968, and that was the last of
the whole SDS 9 line; SDS continued to introduce upgrades to the
32-bit [SDS Sigma series][55] until 01974 (though that series began
earlier, in 01966), until Xerox sold them to Honeywell in 01975.  I
think the last operational SDS 940 probably got decommissioned in the
mid-1970s.  (These things weren't cheap to run; the SDS 940 manual
cited above says it used 3 “Kva”, which is roughly kilowatts.)  But
[Dhrystone][57] wasn’t written until 01984.

[55]: https://en.wikipedia.org/wiki/SDS_Sigma_series
[57]: https://en.wikipedia.org/wiki/Dhrystone

Amusingly, some [former SDS employees refounded the company in
01979][56].  Guess what CPU their new computer used?

A 6502A.

[56]: https://en.wikipedia.org/wiki/Scientific_Data_Systems#A_new_start

The vague handwaving argument above that the 1-MHz 6502’s 0.02-DMIPS
number is a little lower than would be realistic, along with the
estimate that the SDS 940 was probably about twice as fast, combine to
form a vaguer, even more handwaving argument that the SDS 940 was
about 0.1 DMIPS, which was barely able to support 6 concurrent users
with specialized analog display hardware.

This reinforces the above argument that 0.1 Dhrystone MIPS is close to
the minimum practical for an interactive computing system.

### This probably means an interactive computer terminal needs a few milliwatts ###

0.1 MIPS at 1000 pJ/insn works out to 0.1 milliwatts, but at those
power levels other parts of the system consume the majority of the
power.  For example, unless the UI is purely audio, you need a
display.

My estimate from Dercuano was that updating an e-paper display takes
about 25 μJ per glyph; at 350 wpm and thus 35 glyphs per second, this
works out to 875 μW, which is several times more than the 0.1 MIPS.
My friend Eric Volpe tells me that he’s gotten old Nokia SPI screens
(like the 84×48 Nokia 3310 screen, about 25 words of text) to maintain
their display on less than 1 mA at 3.3 volts (though [others say it
needs 6–7 mA][25], and he reports that it consumes more when you’re
updating it, too).  They’re readable without backlight in direct
illumination, but if you use it, he says the backlight also uses
nearly a milliamp.

[25]: https://duino4projects.com/using-nokia-3310-84x48-lcd-arduino/

So you might need 10 milliwatts or more to get a really good
responsive interactive computation environment.

### Batch processing can wait until the sun is shining ###

For batch processing, it might make sense to wait until the daytime:
an average watt of batch-processing power might be 7 watts during the
15% of the time that the sun is shining full force, and 7 Wp of solar
panels only costs US$2.30, which is a lot less than US$6.60.  Also you
don’t need a high-power battery charge controller.

### Lower power opens up alternative power sources and stores, like supercaps ###

As I pointed out in Dercuano, a pullstring can yield 500 mm of pull at
50 N, which is 25 J, which (if harnessed with a dynamo) would run the
laptop for a second or two, but that’s enough to run a 10-milliwatt
computer for 40 minutes, or a 100-milliwatt Swindle for 4 minutes.
For that you don’t need a battery; a capacitor will do.

You might think to go with ceramics, but that’s still impractical for
a pocket computer or laptop.  Although you can get a [25V 4.7μF X5R
0805 Samsung cap for 2.2¢][59] or a [25V 10μF X5R 0805 Taiyo Yuden cap
for 4.1¢][60], either in quantity 1000, ½CV² at the rated voltage
works out to 1.5 mJ and 3.1 mJ respectively, so you’d need thousands
of caps.

Getting to 25 J at under 50 V requires 10000 uF, and for that you need
electrolytics or supercaps.  You can get [22000-μF TDK electrolytics
for a buck fifty][61], but those caps are only 16V, so you’d need five
of them (or 18 of them to have a comfortable 2× margin on the voltage
rating), and they’re a bit bulky: 30 mm diameter, 32 mm tall.

[59]: https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL21A475KAQNNNE/3886902
[60]: https://www.digikey.com/en/products/detail/taiyo-yuden/TMK212BBJ106KG-T/2714163
[61]: https://www.digikey.com/en/products/detail/epcos-tdk-electronics/B41231C4229M000/3493609

Electrolytics are really optimized for charge/discharge frequencies of
60Hz up to a few kHz, though.  This application has frequencies closer
to a millihertz, albeit kind of sawtoothy.  So a supercap like the
[US$4 5.5V 5F Illinois Capacitor DGH505Q5R5][62], the [US$5 5V 1.5F
Maxwell BMOD0001 P005 B02][63], or the [US$2.50 5.5V 1.5F Illinois
Capacitor DGH155Q5R5][64] would probably work; these are rated at 75
J, 18 J, and 22 J, respectively, and they’re pretty small, in the last
case 12 mm × 17 mm × 8.5 mm.

Supercaps are notorious for leakage, but that’s in different contexts;
the Maxwell supercap, for instance, is rated for 5 μA, which is a loss
of 12 mV per hour, so it will lose its charge in a matter of weeks.

Another reason to use two or more is to allow faster charging — the
Maxwell cap is only rated for 3.1 A of one-second surge current, and
the DGH155Q5R5 for 2.8 A, so your pull-cord charge would need to take
a few seconds.  The DGH505Q5R5 is rated for 8.4 A, though.  Smaller
supercaps might include [the US$1 1F 2.7V Eaton HV0810-2R7105-R][65],
which is rated to hold 3.6 J, but rated for 1.1 amps of pulse current,
8 mm in diameter, 13.5 mm long, and 1.2 grams.  You’d need to use
about 8–16 of these, giving you 8.8–17.6 amps of pulse current at up
to 2.7 V, which would probably be enough for the pull cord.

Me, I’d be tempted to vastly oversize the capacitor bank, but that
could be dangerous.

[62]: https://www.digikey.com/en/products/detail/illinois-capacitor/DGH505Q5R5/7387525
[63]: https://www.digikey.com/en/products/detail/maxwell-technologies-korea-co-ltd/BMOD0001-P005-B02/946807
[64]: https://www.digikey.com/en/products/detail/illinois-capacitor/DGH155Q5R5/7387513
[65]: https://www.digikey.com/en/products/detail/eaton-electronics-division/HV0810-2R7105-R/3878078

To charge the capacitor from the pull cord you need not just a dynamo
but also something like a MPPT buck converter that regulates its
output voltage to just above the present voltage of the capacitor bank
(any voltage drop from the capacitor bank’s ESR is, after all, wasted,
and produces heat), then varies it a bit to do MPPT on the pull-cord
dynamo.  At some point, if overloaded as I did with the regenerative
braking on Trevor Blackwell’s scooter, it might need to just
open-circuit the dynamo or connect it to a power resistor instead, but
smoothly feathering into that by easing off of the maximum power point
would be better than suddenly releasing all mechanical resistance.
(That is what the scooter did, falling out from under me, but I think
the mechanism was that I blew a fuse.)

### Ereaders use on the order of 200 mW; maybe reprogram one? ###

The [Amazon Swindle 2][29] uses a 3.7V-1530 mAh battery (20 kJ), which
reportedly lasts [7 days after Amazon tweaked the firmware][30], which
I think is based on some nominal usage level per day — [Amazon shill
sites claim it’s only 15 hours of active use][31], and people say they
[normally charge their e-readers around once a week][32] or [every
32–64 hours of use or so][33], with 6–8 weeks of standby time.  So
this is about 100–300 mW during active use.  Other e-ink-based
“ereaders” have similar battery lives.  All of them have much higher
display resolution than a Nokia cellphone display (typically 300 dpi
instead of like 20 dpi), but evidently they also use two orders of
magnitude more power, a problem which may not be entirely fixable in
software.

[29]: https://en.wikipedia.org/wiki/Amazon_Kindle#Kindle_2
[30]: https://ceklog.kindel.com/2009/11/24/longer-battery-life-for-the-kindle-2/
[31]: https://www.pickmyreader.com/long-will-kindle-battery-last/
[32]: https://www.goodreads.com/topic/show/19252863-battery-draining-quickly
[33]: https://archive.fo/bg5vd "https://www.quora.com/How-long-is-the-battery-life-for-a-Kindle-Paperwhite"

Reprogramming and possibly rewiring an ereader (Amazon or otherwise)
might be a reasonable approach.  Since the [Swindle Touch][34] in
02011, most of them have touchscreens, and since the Paperwhite in
02012, most have backlights or frontlights, which can be turned off.
New, these cost on the order of US$150 here, but older models are
available used and supposedly working for [AR$7000–10000][35]
(US$50–70), 86% Amazon-branded (344 out of 398 current listings).
Older devices tend to have more I/O options, while newer ones tend to
be waterproof.  An [already-jailbroken Swindle is currently for sale
for AR$17000][36] (US$115; Paperwhite 3, 1072×1448, 300dpi, LED
frontlit, 1GHz CPU, 0.5 GiB RAM, “4/3” GB Flash, touchscreen).
Non-Amazon ereaders like the [Noblex ER6A15][37] (AR$12500, US$85)
tend to run Android and have SD card slots, which have been removed
from more recent models of the Swindle — though that one in particular
has no data radios.

[34]: https://en.wikipedia.org/wiki/Amazon_Kindle#Kindle_Touch
[35]: https://computacion.mercadolibre.com.ar/tablets-accesorios/e-readers/usado/_PriceRange_0-10000
[36]: https://articulo.mercadolibre.com.ar/MLA-902119551-kindle-paperwhite-3ra-generacion-como-nuevofundajailbreak-_JM
[37]: https://articulo.mercadolibre.com.ar/MLA-869689729-noblex-er6a15-e-reader-6-memoria-4gb-luz-micro-sd-funda-_JM

Some Swindles have LCDs instead of e-ink displays, and these have
larger batteries; the [Swindle Fire HD 7’s is reportedly 4440 mAh,
bringing its weight to 345 g][38], for example.

[38]: https://www.devicespecifications.com/en/model-battery/e1a32e23

The Kobo seems to have the best reputation for hackability and can run
the [portable open-source ereader firmware “KOReader”][41] (though
there aren’t many for sale; Forma 8 and Clara HD seem to be the
options, but [one Aura N514 remains, at AR$16000][39]), and at least
some models of the Barnes & Noble Nook pair a small, fast LCD with a
large e-ink display, enabling you to have both rapid feedback and low
power use, but [none of them on sale now have this][46].

[46]: https://computacion.mercadolibre.com.ar/tablets-accesorios/e-readers/barnes-noble/

[Report on rooting the Aura][40]:

> I had read that some newer models had the NAND flash soldered onto
> the board, but mine is a Sandisk sdcard in a slot. So I pulled the
> card out, dd copied it, and I can restore if I do anything really
> bad that makes it stop booting.
> 
> There is a well-marked ttl level serial port on the back. uboot is
> accessible and allows for interrupting boot. You can log into a root
> shell onto the running system without a password. It's basically
> open for business.

[The Kobo company does have some despicable practices you have to
protect yourself from][42].

[39]: https://articulo.mercadolibre.com.ar/MLA-904536370-ereader-_JM
[40]: https://www.mobileread.com/forums/showthread.php?t=281817
[41]: https://github.com/koreader/koreader
[42]: https://www.mobileread.com/forums/showthread.php?t=223155

The Kobo Clara is reputedly [pretty easy to program without needing to
jailbreak.][44] It uses the same [.kobo/KoboRoot.tgz firmware upgrade
process earlier Kobos did.][45]

[44]: https://www.mobileread.com/forums/showthread.php?t=314032
[45]: https://yingtongli.me/blog/2018/07/30/kobo-telnet.html

Jailbreaking the Swindle is [quite a pain by contrast][43], because
Amazon keeps causing trouble.

[43]: https://blog.the-ebook-reader.com/2018/03/17/list-of-hacks-mods-and-add-ons-for-kobo-ereaders/

### Memory ###

SD cards are very cheap nowadays, but also you can get surprisingly
cheap and fast SPI flash, as outlined in file `ghz-dds.md`: [the 30¢
GD25D10C][66] contains half a mebibit of NOR flash and can read it at
160 megabits per second, and of course eMMC and SD cards are even
cheaper per byte, though a bit slower.  Flash does not use energy to
maintain data the way DRAM does, though the GD part uses about 0.1 μA
(0.33 μW) in standby — you’d have to cut its power line with a MOSFET
or something if you want to avoid that.  Actively reading from it at
this 160Mbps speed is supposed to cost 2.5 mA (8.25 mW), and *writing*
costs *20* mA (**66 mW**) and is also slow as dogshit.  After a
snowstorm!  Doing the math, reading a byte (of a long stream of them)
at that speed costs about 400 pJ, plus whatever the processor spends
on frobbing the SPI lines.

(How slow is writing?  100 000 000 ns (a suspiciously round number!)
to erase a 4KiB sector (thus 24 000 ns to erase each byte), 30 000 ns
to program the first byte, and 2500 ns to program each subsequent
byte.  This staggering total of 10 300 000 ns to write an erased
sector brings the total time to 110 000 000 ns to erase and rewrite
it, or 27 000 ns per byte, and the *energy* to write the byte to some
1800 nJ, on the order of executing 3000 instructions.)

CMOS SRAM uses a little energy, but much less than DRAM; for example,
[the Cypress CY62136EV30LL-45ZSXIT][67] is a 2-mebibit (256-kibibyte)
45-ns asynchronous parallel SRAM chip for US$1.11 that claims it
typically uses 1 μA at 2.2–3.6 V to retain its data when in standby
mode.  The big problem with SRAM is that fast SRAM is all
parallel-interface, so you need at least to spend at least 26 pins to
talk to this chip, though this is less of a problem if you spend a
27th pin to pull its /CE line high — you can share the pins with other
signals as long as they go to other things that also have some kind of
/CE-like mechanism.

[66]: https://www.gigadevice.com/datasheet/gd25d10c/
[67]: https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/CY62136EV30LL-45ZSXIT/1543737

Still, spending 3 μW to get an extra quarter-mebibyte of 45ns SRAM
seems pretty cheap.  But that goes up to 6000 μW/MHz when you’re
actively frobbing it.  That’s, I guess, 6000 pJ per off-chip SRAM
access, which is kind of high when we recall that we’re only paying on
the order of 500 pJ per instruction and 400 pJ per byte read from SPI
NOR Flash.  Accessing the SRAM *once* costs as much as running *12*
instructions.  You can write a byte of SRAM in 45 ns instead of the
Flash’s average 27 000 ns, and spending 6000 pJ instead of the Flash's
1 800 000 pJ, and it really is random access both for reading and
writing, which the Flash very much is not.

The CY7C1020D-10VXI also mentioned therein is a smaller parallel CMOS
SRAM with 10-ns access time and fifteen times higher cost per byte.
But it’s enormously more power-hungry, too: 3 mA rather than 1 μA in
standby, according to the datasheet, and *80 mA* when being accessed
at 100 MHz, which (at 5 V) is *400 mW*.  That’s still less energy per
access when going full tilt — 4000 pJ per byte instead of
6000 pJ — but the 3000-times-higher high quiescent draw means this
chip has no place in milliwatt computing.

SD cards have NAND flash on them and can normally write with higher
bandwidth than that, and I think they *must* use a bit less energy
(1800 nJ per byte would mean 10 megabytes per second would be 18
watts), but I don’t know if they have lower latency.  And I don’t
think the energy usage is orders of magnitude lower, just a little
lower.

Four promising bare NAND chips are the [US$3 104MHz quad SPI
128-mebibyte Winbond W25N01GVZEIG TR][70], the [US$2.50 120MHz
quad-SPI 128-mebibyte GigaDevice GD5F1GQ4RF9IGR][71], the [US$1
45-ns/25000-ns 48-pin parallel 128-mebibyte Cypress
S34MS01G200TFI900][72] (whose datasheet has been memory-holed from
Cypress’s site but [a datasheet for a clone of which I found on Mouser
via Yandex][73] after filling out a captcha in Cyrillic), and the
[US$2.30 50MHz quad-SPI 128-mebibyte Micron MT29F1G01ABBFDWB-IT:F
TR][74] whose [datasheet I found the same way][75].

[70]: https://www.digikey.com/en/products/detail/winbond-electronics/W25N01GVZEIG-TR/5803931
[71]: https://www.digikey.com/en/products/detail/gigadevice-semiconductor-hk-limited/GD5F1GQ4RF9IGR/9484745
[72]: https://www.digikey.com/en/products/detail/cypress-semiconductor-corp/S34MS01G200TFI900/4833856
[73]: https://ru.mouser.com/datasheet/2/980/002-03238-1669830.pdf
[74]: https://www.digikey.com/en/products/detail/micron-technology-inc/MT29F1G01ABBFDWB-IT-F-TR/6135561
[75]: https://datasheet.octopart.com/MT29F1G01AAADDH4-IT:D-Micron-datasheet-11572380.pdf

The SkyHigh Memory datasheet for the S34MS01G2 claims SLC, 25 μs (max)
for random access, but 45 ns (min) for sequential access, and there
are versions with 8-bit and 16-bit I/O buses (this is the 8-bit
version); for writing, it takes 300 μs to program a 2048+64-byte page
and 3 ms to erase a 64-page block.  It uses the same 8-bit or 16-bit
bus for address and data bits, so I have no idea why it has 48 pins;
only 23 are used in the 8-bit version, and 31 in the 16-bit version,
and 8 of those are power pins!  So you only need 15 GPIO pins to talk
to it.

To access the memory, first you clock in 1–4 command bytes, and then
you feed in the address on the bus in four successive clock cycles
while signaling the desired operation with some other control lines.
A read command copies a page from the Flash into a buffer (in
25000 ns, apparently), signaled by the “ready/busy” pin going high,
and then you can read out a word (8 bits on this chip, but 16 bits on
16-bit parts) every 45 ns, as you choose to toggle the read-enable
pin.

*Writing* the memory may fail and need to be retried — at a different
page address, probably.  Also typically NAND chips have about 2% bad
bits.

It supports prefetching pages so you can overlap the 25000-ns
copying-into-buffer with your reading of the previous page, and
similarly you can send it data you’re planning to write to another
page while it’s still burning in the data you sent before.

So it looks like kind of a pain to talk to, but still easier than
you’d think from the 48-pin package; but how much *power* does it use?

It runs on 1.8 volts, and it claims to use 15 mA typical, 30 mA max,
for all of read, program, and erase!  That can’t possibly be correct.
(Can it?)  And 10 μA typical standby current (“(CMOS)”, whatever that
means).

But if that *were* correct, it would work out to 27 mW for 22 million
bytes *read* per second, assuming the 25000-ns overlap thing works
out.  So that’s 1.2 nJ per byte, three times the cost of reading from
NOR.  *Writing* 131072 bytes (not counting the 64) supposedly requires
21.2 ms at the same 27 mW, plus 5.9 ms to clock them into the device,
potentially overlapping, which would be only 4.4 nJ per byte.
[Avinash Aravindan of Cypress explains that this two orders of
magnitude faster erasure, using much lower power, is characteristic of
NAND][76], and [Edouard Haas has an insightful article on the same
subject][77], where he points out among other things that NOR permits
single-byte write operations, and in [his QSPI NAND article][78] he
points out that NOR uses 100 times more energy for erase+write than
NAND.

[76]: https://www.embedded.com/flash-101-nand-flash-vs-nor-flash/
[77]: https://www.jblopen.com/nor-vs-nand-so-you-think-you-know-the-music/
[78]: https://www.jblopen.com/qspi-nand-intro/

The “obsolete” GD5F1GQ4RF9IGR is another 1.8 V 128-mebibyte NAND
Flash, but this time SPI/dual-SPI/QSPI, with broadly similar
performance: 400 μs (700 μs max) to program a (2048+128)-byte page,
3000 μs to erase a 64-page block, 80 μs to read a page, using 40 mA
maximum active current (again, for all of read, program, and erase, so
I guess that *can* be real) and 90 μA standby current.  It has
internal ECC, so you don’t have to worry about bad bits.  It actually
looks like *higher* bandwidth than the 8-bit parallel chip — 120 MHz
and quad-SPI gives you 60 megabytes a second instead of 22 — but its
internal slowness more than compensates.  It doesn’t seem to have the
pipelining feature the Cypress part has to overlap fetches with reads,
or burns with loads.  The Digi-Key page linked above is the 8×6mm
8-VLGA package.

This works out to 72 mW and 80+34 μs = 114 μs to read a page, so 56 ns
and 4 nJ to read each byte (again, disregarding the “extra data”);
writing a 131072-byte block takes 3 ms to erase, 25.6 ms to program
(plus 34 μs per page to clock in the data, which might add another
2.2 ms) for 28.6 ms: 220 ns per byte, which means 16 nJ per byte.

I’m going to assume the other two gibibit NAND chips are similar.

Another option is SPI SRAM chips like the [US$1.20 Microchip
23K256][68], which has 32 kibibytes of SRAM, a 20MHz SPI interface,
and runs on 3.3V; it uses 10 mA (33 mW) reading at 20 MHz (20Mbps) and
idles at 1 μA (typical).  The datasheet doesn’t specify the write
power usage; if we assume it’s the same as the read power usage, then
they’re both around 1700 pJ per bit, or 13 000 pJ per (sequential)
byte.  (Random access costs four times as much.)

[68]: https://www.digikey.com/en/products/detail/microchip-technology/23K256-I-P/2001112

“Quad SPI” chips like the [US$2.10 Microchip 23LC1024][69], with 128
KiB, are generally faster.  It runs at 2.5–5 V and up to 20 MHz,
purporting to use only 3 mA (10 mW at 3.3 V) reading at 20 MHz.
Moreover, it can transfer data at 80Mbps instead of 20Mbps, so this
ends up being 120 pJ/bit or 1000 pJ/byte, nearly as low as reading the
GD SPI NOR Flash above.  Typical standby current is higher at 4 μA, but
not so high as to matter here.

[69]: https://www.digikey.com/en/products/detail/microchip-technology/23LC1024-I-SN/3543084