I just read the 100 most popular words from the British National
Corpus out loud, one at a time, with pauses in between:

> the of and to a in it is was that i for on you he be with by at have
> are this not but had his they from as she which or we an there her
> were do been all their has would will what if one can so no who said
> more about them some could him into its then up two time my out like
> did only me your now other may just these new also people any know
> first see well very should than how get most over back way our much
> think between years go er

This took 114 seconds, or 1.14 seconds per word, so probably the first
1000 words would take me about 20 minutes, and the first 10000 words
about three or four hours.

These 100 words comprise 50.56% of the words in the BNC (“the” being
about 6.87%, and “er” being about 0.1%), or at any rate the part of it
that is represented in my frequency table, so if you had recordings of
them (as LPC-10 or whatever) you could only synthesize about half of
the words in typical text.  Here’s an overview of how that number
changes:

<table>
<tr><th>Word     <th>Rank <th>Cumulative %<th>Self % <th>Time to record<br />this many <th>To miss one <br />word in
<tr><td>much     <td>95   <td>50.05%   <td>0.10%     <td>2 minutes                     <td>2
<tr><td>er       <td>100  <td>50.56%   <td>0.10%     <td>2 minutes                     <td>2
<tr><td>married  <td>1261 <td>75.005%  <td>0.0083%   <td>24 minutes                    <td>4
<tr><td>colonel  <td>4407 <td>87.5004% <td>0.0020%   <td>1½ hours                      <td>8
<tr><td>cdna‽    <td>10445<td>93.7500% <td>0.0006%   <td>3½ hours                      <td>16
<tr><td>capitals <td>10446<td>93.7506% <td>0.0006%   <td>3½ hours                      <td>16
<tr><td>stabilise<td>20104<td>96.87494%<td>0.00019%  <td>6½ hours                      <td>32
<tr><td>pasha    <td>33275<td>98.43748%<td>0.00007%  <td>11 hours                      <td>64
<tr><td>lessens  <td>43350<td>99%      <td>0.00004%  <td>14 hours                      <td>100
<tr><td>pizzicato<td>60386<td>99.5%    <td>0.00002%  <td>19 hours                      <td>200
<tr><td>superfields<td>76770<td>99.75% <td>0.000011% <td>24 hours                      <td>400
</table>

After the first 8000 words or so, the ordering starts to be somewhat
dubious, as reverse alphabetization sets in due to small corpus size.

Brute-force recording the whole English lexicon seems like a
surprisingly approachable, if boring, project, from this point of
view.  In a few days of work you could compile enough recordings that
your computer could read most text understandably, if not naturally.

I analyzed (an earlier version of) this note using these frequencies.
It contained two known words less common than #65536: “BNC” and
“superfields”; four words less common than #32768: “synthesize”,
“pasha”, “lessens”, and “pizzicato”; three words less common
than #16384: “pauses”, “stabilise”, and “approachable”, plus some HTML
tags; and 8 words less common than #8192: “corpus”, “comprise”,
“cumulative”, “cdna”, “capitals”, “brute”, “lexicon”, and “compile”.

Here’s the full analysis:

    unknown
        100 114 1 14 1000 20 10000 100 50 56 6 87 0 1 LPC 10 95 50 05 0 10 2 2 100
        50 56 0 10 2 2 1261 75 005 0 0083 24 4 4407 87 5004 0 0020 1 8 10445 93 7500
        0 0006 3 16 10446 93 7506 0 0006 3 16 20104 96 87494 0 00019 6 32 33275 98
        43748 0 00007 11 64 43350 99 0 00004 14 100 60386 99 5 0 00002 19 200 76770
        99 75 0 000011 24 400
    1
        the the the the the the the the the the the
    2
        of and and of and of of of of of of
    4
        a in to a in it in it in in to To in a In a
    8
        I is was that i for on you he that is you you that you that
    16
        from at with be with by at have are this not but had his they from as she
        which This at had as this from this
    32
        one or we an there her were do been all their has would will what if one can
        so no who said more about them some could him into its then up two or so
        would about about or about about or so if them or could about an one if
        could
    64
        just most out time between time my out like did only me your now other may
        just these new also people any know first see well very should than how get
        most over back way our much think between years go er first take me first
        three These being er being any my only Here how Time many much er like work
    128
        British National took four part number point days
    256
        read words word probably words minutes words hours words words rate table
        half words table Word word minutes minutes minutes hours hours hours hours
        hours hours hours hours table whole English seems view few enough
    512
        popular per whatever s changes record miss force project
    1024
        typical text married
    2048
        seconds seconds represented frequency th th th th Self th th recording
        surprisingly
    4096
        loud recordings overview Rank br br colonel boring recordings
    8192
        Corpus comprise Cumulative cdna capitals Brute lexicon compile
    16384
        pauses tr tr td td td td td td tr td td td td td td tr td td td td td td tr
        td td td td td td tr td td td td td td tr td td td td td td tr td stabilise
        td td td td td tr td td td td td td tr td td td td td td tr td td td td td
        td tr td td td td td td approachable
    32768
        synthesize pasha lessens pizzicato
    65536
        BNC superfields

So, with 16384 words, which could be recorded in a day or two, plus
numbers and initialisms, only “pauses” and “approachable” would have
been missed in a text-to-speech of a note like this one, if we leave
out the words deliberately chosen to be uncommon.  Even with only a
512-word vocabulary, the note would be comprehensible.

Other notes in Dernocua are not so fortunate.  [The 7500-word note on
energy-autonomous computing](energy-autonomous-computing.md), for
example, includes 1790 words not in the BNC at all; about half of
these are real English words such as Github, Kobo, joule,
touchscreens, ebook, and 80Mbps, plus many Spanish words and
initialisms.  The most common 512 words would have covered a bit over
3000 of its 7500 words.
