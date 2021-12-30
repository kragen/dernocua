Reading Bhattacharyya’s 02015 book on electrochemical micromachining.
Seems like the guy invented a significant part of the field.

By chapter
----------

This section of my notes is organized more or less in parallel with
the book, which is to say, it’s not organized.  The idea is to add a
later synthesis section below (or above).

Things I’m hoping to see but might not:

1. Flexures.
2. Recursion.
3. Control loop characteristics.
4. Machining speeds.
5. “Speeds and feeds” (coolant speed, current, voltage, vibration
   speed and amplitude, current waveforms, electrolyte choice).
6. Alternating ECM with selective electrodeposition.

### Preface ###

I’m surprised to see that you can electrochemically machine
semiconductors (p. xviii), since they aren’t held together by metallic
bonds.  I look forward to learning more.

“EMM”, “EMST” (“electrochemical microsystem technology”), and “ENT”
(“electrochemical nanotechnology”) are new terms to me.  “SECM” is
mentioned next to “STM” and “AFM”, and might mean “scanning
electrochemical microscopy”.

The English of the preface is lamentably somewhat broken, but I guess
Bhattacharyya earned his merit by building things, not writing English
poetry, and he chose to publish his book through Elsevier instead of a
publisher who actually has editors.  But it means the next couple
hundred pages will be a bit of a slog.

At the end of the preface there’s this tantalizing note:

> To assure that the reader is exposed to wider coverage of EMM, the
> book includes EMST and ENT for updating further applicability of
> anodic dissolution or deposition which promises significant advances
> not only in micromachining but also for nanofabrication as well as
> nanotechnology applications.

### 1. Introduction ###

The English gets worse:

> In prehistoric age, fragments stone, bone and wood were first used
> as tool by human beings for shaping the material to fulfill their
> urgent needs of day-to-day life.  Progress in machining technology
> started from those early days.  It was in about 4000 BC that use of
> drilling and cutting tools started in ancient Egypt...

Clearly there’s some imprecision being introduced here due to the poor
editing, because that would imply that ancient Egypt lacked cutting
tools such as hand axes for the previous two million years.

Ugh, and on p. 3 he misspells the title of Drexler’s book as “*Engine
of Creation*”.

It’s astounding to see him equate (also p. 3) top-down nanotechnology
with nanometer-scale subtractive manufacturing.  (He repeats the error
in his Figure 18 diagram on p. 22, where his “bottom up approach”
category includes “Rapid prototyping (RP)”, by which I assume he means
3-D printing, CVD, PVD, electroforming, and “electron beam direct
writing”.)

On p. 6 he’s careless about scale, suggesting that the universe is on
the order of 10<sup>15</sup> meters in scale, when actually that’s
only about 0.1 light years, so it’s too small by 11 orders of
magnitude.

Page after page of this carelessness is making me wish I was reading
*Nanosystems*, which has the unfortunate drawback that none of the
systems it describes have been built.

This is a boner too (p. 7):

> When the size of the microcomponent becomes smaller to atomic scale,
> it is not possible to utilize the top-down approach.  However,
> developments are taking place to improve some of the techniques such
> that machining and fabrication can be successfully made at the
> molecular level and may be extended even to subatomic scale.

Oh *really*.

On p. 8 we have a taxonomy of micromachining processes: TBM, USMM,
AJMM, AWJMM, WJMM (mechanical micromachining); EBMM, LBMM, EDMM, EDMM
again, IBMM (“thermal beam based micromachining”); PCMM and EMM
(chemical and electrochemical micromachining); and ECSMM, ECG, EDG,
and ELID (hybrid micromachining).  No expansions are given for any
acronym.

On p. 9 we have the first useful assertion: that the cutting-edge
radius on micro-scale conventional tools can be “up to 10 micron”,
with a diagram showing the removal of a chip that’s much thinner than
the tooltip radius.  “The main drawbacks of this process are high tool
wear, rigidity requirement of the machine tool, and heat generation at
the tool-work interface.”  I’d’ve thought the surface finish would be
a bigger drawback!

I think AJMM, AWJMM, and WJMM are supposed to be abrasive jet
micromachining, abrasive waterjet micromachining, and waterjet
micromachining.  However, he seems to have forgotten to cover AWJMM
and WJMM, and TBM is not mentioned but maybe means micro-scale
conventional cutting tools.

Micro-USM (p. 10) ultrasonic machining might be the meaning of the
enigmatic “USMM” on p. 8.  P. 10 also has a nice (though badly
pixelated) diagram of abrasive-jet machining at 0.2-0.8 MPa with
500-1000 nm abrasive particles and a photoresist film to abrade
selectively, none of which is mentioned in the text.

On p. 11 he says boron carbide is “often chosen as the abrasive [for
ultrasonic machining] for almost all materials except diamond due to
its cost effectiveness and ease of use.”  I wonder if maybe it’s
actually boron nitride, which he hasn’t mentioned.

There are some useful figures on USM on p. 11: abrasive grain size
from 200 to 20000 nm, 100 to 20000 nm vibration amplitude, 0.1 to 1 N
force, and 20-40 kHz (p. 10).  This information is very valuable, but
I wonder if it’s as unreliable as the other information presented
previously.

“EDG” is “electrodischarge grinding” (p. 12).

“LBM” is “laser beam machining” (p. 12), so maybe LBMM is “laser beam
micromachining”.

“PAM” is “plasma arc machining” (p. 13), which wasn’t mentioned in the
taxonomy diagram; maybe “PCMM” is intended to mean it.  The diagram is
just a more pixelated version of a standard plasma cutting torch.

“IBM” is “ion beam machining” (p. 14) but the diagram is actually a
diagram of e-beam machining (the next section) because it contains no
ion source.  I’m guessing “IBMM” is “ion beam micromachining”,
although, really, ion-beam machining pretty much has to be “micro” in
order to be useful at all.

“EBM” is “electron beam machining” (p. 14), so maybe “EBMM” is that
too.

On p. 15 he talks about “micro-CM” or “chemical micromachining (CMM)”
which he describes as the way “microdevices like semiconductor
devices, ICs, etc.,” are made.  I don’t think I’ve ever heard chip
fabrication called “CMM” before.

Aha!  On p. 18 there’s a chart of speed-and-feed stuff explaining what
sets EMM apart from regular ECM.  It answers immediately one of the
things that’s been puzzling me about ECM, namely, why people haven’t
been using it to make ridged mirrors: accuracy of ±0.02-0.1 mm, down
to 0.01 mm for EMM, which is two orders of magnitude worse than what
you need for optics.

### 2. Electrochemical machining: macro to micro ###

On p. 26 he gives a historical overview, which I’m hoping is actually
accurate: 

> In 1929, the Russian researcher W. Gusseff first developed a process
> to machine metal anodically through electrolytic process. In 1959,
> Anocut Engineering Company of Chicago established the anodic metal
> machining techniques as a commercially suitable technique.  After 1
> year, Steel Improvement and Forge Company followed with a commercial
> application of this technique, based upon research by the Battelle
> Memorial Institute. The technique was applied mainly for machining
> of large components made of advanced and difficult-to-cut metals in
> the 1960s and the 1970s, particularly in the gas turbine industry.
> Electrical discharge machining at that time was a more accurate
> technique and was preferred over ECM, because ECM was less accurate
> and its waste is hazardous to the environment. But ECM was able to
> achieve much higher machining speed.

It would be nice to get some specific information about the
environmental hazards so we can mitigate them.  If this was a major
industrial consideration in the 01960s they must have been *amazing*
environmental hazards; that was the period when they were
investigating open-cycle nuclear-powered jet engines, chlorine
trifluoride rocket fuel, and borate zip fuel, and the EPA and
Superfund didn’t exist yet.

On p. 26 his account of the effects of changing the process gap
implicitly assume a constant-voltage source.

On p. 27 his diagram suggests that the standard way to separate the
sludge is with a centrifuge.

On p. 28 there is a list of four major recent improvements: vibrating
axes permit maintaining a 100-micron process gap (because the
electrolyte can flush out during the other part of the vibration
cycle); pulsed current rather than constant direct current;
microfiltration for electrolyte regeneration; and CAD for cathode tool
profiles.  After having waded through 40 pages of tiresome sales
pitches for ECM I sure hope the book explains how to do these things
at some point.

On p. 29 there is a fundamental error:

>  During electrical conduction through electrolyte ... Distribution
>  [sic] of anion and cation remains uniform; hence the electrical
>  potential at all points in the electrolyte is also uniform.
>  Application of an external electric field causes migration of one
>  ion species with respect to other. [sic]

When the electric potential at all points in the electrolyte is the
same, no current flows.  I hope this is just a careless error and not
something he really believes.  (In Fig. 2.11 on p. 42 he gives a
correct, if only qualitative, diagram of how the electrical potential
differs at different points in the electrolyte.)

On p. 30 he gives Faraday’s constant as “96.485 C mol<sup>-1</sup>”,
which is correct if we read the “.” as a thousands separator.

I’m not sure about his description of electrolysis on pp. 30-33.  I
need to come back and reread it.  But at least it’s real information
instead of the sales pitch.

On p. 33 the concept of chemical equilibrium is incorrectly contrasted
with a description of chemical equilibrium:

> When no current is flowing, the electrochemical changes occurring at
> an electrode are in steady state, i.e., atoms leave the electrode
> and become ions and the ions move to the electrode and becomes [sic]
> atoms. The process continuous [sic] till [sic] equilibrium is
> reached.  A potential difference exists between
> electrode-electrolyte interfaces [sic], which is known as “electrode
> potential.”

On p. 34 there is a description of different anodic dissolution
regimes (pitting, polishing, both) that I need to reread.
