Ooh, broken disks are [AR$1200 (US$8) for a ten-pack][1].  $120 (80¢)
(or [US$1 in the EU in 02013][0]) [gets you][7] a voice-coil actuator
built around two pyrophoric [neodymium magnets plated in nickel
mounted on permalloy or mu-metal brackets][16], a 5400rpm long-life
bearing, and a BLDC motor with a controller, plus some extremely flat
([Ra 120 pm][4]) first-surface glass-ceramic mirrors with [80%
reflectivity][2] and a low thermal coefficient of expansion ([7.4
ppm/° for TS-10][3]) and high modulus (100 GPa), [about 400g of
castable aluminum][0] between possible platters and the case (maybe
[A380 or ADC12][5] or [6061 or 5052][6]) some Torx screws, a SATA
power connector, some machined 6061-T6 aluminum spacers, and some
jumper blocks.  Oh and maybe [an accelerometer and temperature and
pressure sensors][8].  As scrap metal this totals about [US$1.66][0],
mostly from copper and gold from the PCB, but obviously you can’t get
voice-coil actuators or bearings that cheap.

[0]: http://www.resourcefever.com/publications/reports/Bo2W_HDD_Dismantling_Nov2015_final.pdf "Recycling of Hard Disk Drives, Manhart et al., 02015"
[1]: https://articulo.mercadolibre.com.ar/MLA-691736404-discos-rigidos-a-revisar-reparar-lote-de-10-surtidos-_JM?searchVariation=46220774514
[2]: http://imajeenyus.com/optical/20140813_hdd_mirrors/index.shtml
[3]: http://www.oharacorp.com/pdf/TS-10.pdf
[4]: https://www.fujielectric.com/company/tech/pdf/57-02/FER-57-2-062-2011.pdf "Aluminum Substrate for 3.5-inch 1 TB Magnetic Recording Media, Kainuma et al. 02011"
[5]: https://www.quora.com/What-aluminum-alloy-is-used-to-cast-computer-hard-drive-shells
[6]: https://www.scrapmetalforum.com/computer-recycling/25497-hard-drive-shells-heatsinks-alloy-separation.html
[7]: https://hackaday.com/2016/02/03/hard-drive-disassembly-is-easy-and-rewarding/
[8]: https://www.st.com/en/applications/data-center/hard-disk-drive-hdd.html
[16]: https://www.scrapmetaljunkie.com/269/how-to-scrap-hard-drives-2

Oh, and [an ARM core accessible over JTAG, using external RAM and
Flash][9].  And it talks to the controller that controls the spindle
and head over SPI.  [The Flash format has been largely reversed][10],
but [the chipmakers don’t publish datasheets][11].

[9]: https://spritesmods.com/?art=hddhack&page=3
[10]: https://web.archive.org/web/20130228021446/http://nazyura.hardw.net/Part02.htm
[11]: https://www.overclockers.com/forums/showthread.php/568740-Microcontrollers-on-Hard-drives

The whole precisely balanced platter assembly with the platters,
motor, and bearings is nowadays almost invariably 5400rpm or 7200rpm;
10krpm disks are exotic rarities, and 3600rpm disks are antique.  A
7200-rpm 3.5" desktop drive has a rim speed of 5.3 m/s, while a
5400-rpm 2.5" laptop drive is 2.9 m/s.  Either of these is a fairly
respectable speed on its own for things like fine grinding, but also
you can also [overclock them quite a bit][12].  They’re normally only
operated at about 3 watts, so you probably can’t get more than 30
watts out of them no matter how much cooling you add.

[12]: http://imajeenyus.com/electronics/20140125_brushless_motor_driver/index.shtml

The motor might be suitable as a hand pullstring generator.

Desktop disks still use aluminum platters, typically [635 μm][13]
thick.  These are also 6061.

[13]: https://ceramics.org/ceramic-tech-today/glass-could-replace-aluminum-in-hard-disk-drives-that-store-20-tb-of-data

For small machinery the cobalt alloy used for the magnetic medium
might be worth extracting and refining.  I’m guessing it’s on the
order of 10 mg per disk, assuming 25 nm thickness, 3 platters, and
3.5", and ignoring the center hole; [there are also two layers on top
of it and three underneath][4].

[Reputedly the head arm bearing is also very high precision][14].
[Micah Elizabeth Scott built a 4kpps laser projector in 02008][15]
using two voice-coil actuators from hard disks.

[14]: https://hackaday.com/2018/01/07/scrap-a-hard-drive-build-a-rotary-encoder/#comment-4301966
[15]: https://scanlime.org/2008/07/hard-disk-laser-scanner-at-ilda-4k/

Not sure how to use the actual GMR sensors themselves; presumably they
can detect small magnetic fields reliably.
