MOSFET body diodes are PIN diodes, according to [Characterization of
body diodes in the-state-of-the-art SiC FETs -Are they good enough as
freewheeling
diodes?](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2585927/EPE2018v10.pdf?sequence=1).
The paper is about carborundum FETs, but presumably this is true of
silicon FETs too.  I suspect this means that they would make usable
ionizing particle detectors, perhaps even in reverse-biased avalanche
mode; power MOSFETs are commonly very robustly constructed with very
low capacitance between the source and drain, increasing the chance
that they could survive such treatment.

Silicon MOSFETs would probably be better for this than GaN HEMTs or
carborundum FETs, because carborundum’s higher critical breakdown
field strength is [7x higher than
silicon’s](https://www.mouser.com/pdfDocs/infineon-CoolSiC-MOSFET-Revolution.pdf),
permitting the carborundum device to be much smaller for a given
maximum voltage rating.  This, in turn, means a smaller area over
which to capture particles.

This may be an appealing alternative to purpose-built PIN diodes for
detecting ionizing particles, especially in places or times with
supply-chain weaknesses and breakdowns, because power MOSFETs are very
widely available, both as discrete parts easily salvaged from broken
equipment (with sufficiently powerful soldering irons) and, because
they are often the first part of the equipment to fail, as replacement
parts.
