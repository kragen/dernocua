What would you do if you wanted to dump a capacitor holding 100 joules
at 1000 amps in a millisecond, briefly dissipating 100 kilowatts?

Most IGBTs are not equipped to deal with pulse currents like this, and
I don’t think you can parallel them the way you can MOSFETs, due to
current hogging by the hottest device; the [IXGX320N60B3][2] costs
US$22 and is rated to dissipate 1700 watts itself, and IXYS doesn’t
publish a datasheet for it.  [Similarly for triacs.][4]

[4]: https://electronics.stackexchange.com/a/365478

MOSFETs like the [SIHB33N60E-GE3][3] are maybe more promising: for
US$6 you can switch 600 V and pulses of 88 A with 0.1Ω with a
150-nanosecond turn-on delay plus rise time, and you can safely
parallel them.  (88 A is almost three times their maximum continuous
current of 33 A.)  So if you [put a dozen of them in parallel][5]
(US$70) the datasheet claims you can get them to control a kiloamp
pulse.  (Probably a good idea to add enough series inductance to keep
the pulse current from going higher than that.)  The [Infineon
IPA60R099C6XKSA1][4] is US$8 in quantity 1 and rated for 112-amp
pulses, so you’d still spend US$70.

[2]: https://www.digikey.com/en/products/detail/ixys/IXGX320N60B3/3586374
[3]: https://www.digikey.com/en/products/detail/vishay-siliconix/SIHB33N60E-GE3/3900194
[4]: https://www.digikey.com/en/products/detail/infineon-technologies/IPA60R099C6XKSA1/2338038
[5]: http://www.irf.com/technical-info/appnotes/an-941.pdf "Paralleling Power MOSFETs, anonymous"

I wonder if a simple mercury-wetted reed relay would be a better
choice.
