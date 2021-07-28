I’m reading through the ISO 32000-2008 PDF-1.7 spec, which is about
340,326 words, 60% of the size of War and Peace.  But for the time
being I’m not interested in all of it:

* §1 Scope (1 p.), yes.
* §2 Conformance (1 p.), yes.
* §3 Normative references (4 pp.), yes.
* §4 Terms and Definitions (4 pp.), yes.
* §5 Notation (1 p.), yes.
* §6 Version designations (1 p.), yes.
* §7 Syntax (100 pp.), yes.
* §8 Graphics (127 pp.), no.
* §9 Text (59 pp.), yes.
* §10 Rendering (24 pp.), no.
* §11 Transparency (42 pp.), no.
* §12 Interactive Features (124 pp.), no.
* §13 Multimedia Features (61 pp.), no.
* §14 Document Interchange (96 pp.), I don’t think so.

This works out to only about (+ 1 1 4 4 1 1 100 59) = 171 pages of
reading.  I don’t think I’m going to be able to make it through the
whole thing in the next couple of hours...

It’s interesting that on p. 251 in §9.4.3 it requires you to backslash
all of your special characters in the string, with no provision for
nesting parens:

> The strings shall conform to the syntax for string objects. When a
> string is written by enclosing the data in parentheses, bytes whose
> values are equal to those of the ASCII characters LEFT PARENTHESIS
> (28h), RIGHT PARENTHESIS (29h), and REVERSE SOLIDUS (5Ch)
> (backslash) shall be preceded by a REVERSE SOLIDUS) character. All
> other byte values between 0 and 255 may be used in a string
> object. These rules apply to each individual byte in a string
> object, whether the string is interpreted by the text-showing
> operators as single-byte or multiple-byte character codes.

I think this is an error because §7.3.4.2 on p. 23 says:

> Any characters may appear in a string except unbalanced parentheses
> (LEFT PARENHESIS [sic] (28h) and RIGHT PARENTHESIS (29h)) and the
> backslash (REVERSE SOLIDUS (5Ch)), which shall be treated specially
> as described in this sub-clause. Balanced pairs of parentheses
> within a string require no special treatment.

It’s surprising to see that “name objects” are apparently new in PDF
1.2:

> Beginning with PDF 1.2 a name object is an atomic symbol uniquely
> defined by a sequence of any characters (8-bit values) except null
> (character code 0).

But maybe that isn’t really what is meant; maybe they existed
previously but could include null or couldn’t include, say, DEL.

It’s a relief to see that names are interpreted as UTF-8.

Strings and character encodings
-------------------------------

The encoding of string contents is tricky.  §7.9.2.2 says they’re
PDFDocEncoded unless they begin with a BOM.  But that’s only for
“structural” strings, not for strings that are part of document
content.  Actual text strings on the page are decoded by the font:

> With a composite font (PDF 1.2), multiple-byte codes may be used to
> select glyphs.  In this instance, one or more consecutive bytes of
> the string shall be treated as a single character code.  The code
> lengths and the mappings from codes to glyph are defined in a data
> structure called a *CMap*, described in [§]9.7, “Composite Fonts”.

It isn't really described there.  §9.7.5.3 explains that CMaps are
*really* described in “[Adobe Technical Note #5014, Adobe CMap and
CIDFont Files Specification][0].”  Although it does give an example
CMap that implements Shift-JIS, which is evidently written in
PostScript, and there’s some further explanation in §9.7.6.2, but it
assumes you’re already familiar with the aforementioned TN5014.
§9.10.3 also suggests reading “Adobe Technical Note #5411, ToUnicode
Mapping File Tutorial.”

[0]: https://adobe-type-tools.github.io/font-tech-notes/pdfs/5014.CIDFont_Spec.pdf

TN#5014 explains further:

> Some CID-keyed font rendering software (such as ATM-J) takes
> advantage of a particular stylized use of the PostScript
> language. As a result, CID-keyed font files must also adhere to
> these PostScript language usage conventions. The syntax resulting
> from these conventions is considerably more restricted than that of
> the PostScript language; CID-keyed fonts can be read and executed by
> PostScript interpreters, but not all PostScript language usage is
> acceptable in CID-keyed fonts.

Its §5 and §7 explain the CMap in more detail; TN#5014§5 gives what
looks like a slightly less abbreviated version of the Shift-JIS CMap
given as an example in the PDF spec.  The most crucial information is
on TN#5014 p. 51:

> the cidrange sections associate the beginning and ending of a range
> of acceptable character codes, expressed as hexadecimal strings,
> with the starting CID for that range. ...
> 
>     100 begincidrange
>        <20>     <7e>   1
>        <8140> <817e> 633
>        <8180> <81ac> 696
>     ...
>     endcidrange

Evidently this means that the byte sequence 0x20 maps to CID 1, 0x21
to CID 2, ... 0x7e to CID 95, then 0x81 0x40 to CID 633, 0x81 0x41 to
CID 634, etc.  Evidently 0x81 0x7f is an invalid sequence in
Shift-JIS, and [Wikipedia agrees that it is][1].

[1]: https://en.wikipedia.org/wiki/Shift_JIS#As_defined_in_JIS_X_0208:1997

Also there are some predefined CMap names, given as the "/Encoding" of
a Type0 font, including /Identity-H (which is UTF-16BE for horizontal
text) and some UTF-16BE and UCS-2 cases.

The /Type0 font can include, in addition to an /Encoding, a /ToUnicode
which points at another CMap which tells how to convert to Unicode
rather than indexes into some font.  The example given maps the ASCII
range, unpacks some ligatures with “basefont ranges”, and maps a
single character to a surrogate pair with a “basefont char”:

    2 beginbfrange
    <0000> <005E> <0020>
    <005F> <0061> [<00660066> <00660069> <00660066006C>]
    endbfrange
    1 beginbfchar
    <3A51> <D840DC3E>
    endbfchar

Nobody ever uses a predefined CMap for /ToUnicode.  And they always
compress their CMaps.  I extracted one of these content streams to a
file and read it with Python’s zlib.decompress; evidently it was set
up using a super dumb ASCII subsetting procedure:

    >>> print zlib.decompress(open('tmp.flate').read())
    /CIDInit /ProcSet findresource begin 12 dict begin begincmap /CIDSystemInfo <<
    /Registry (F3+0) /Ordering (T1UV) /Supplement 0 >> def
    /CMapName /F3+0 def
    /CMapType 2 def
    1 begincodespacerange <20> <78> endcodespacerange
    6 beginbfchar
    <20> <0020>
    <2a> <002A>
    <2e> <002E>
    <41> <0041>
    <59> <0059>
    <61> <0061>
    endbfchar
    7 beginbfrange
    <31> <35> <0031>
    <43> <49> <0043>
    <4b> <50> <004B>
    <52> <56> <0052>
    <63> <69> <0063>
    <6d> <6f> <006D>
    <72> <78> <0072>
    endbfrange
    endcmap CMapName currentdict /CMap defineresource pop end end

Here’s another case from another file that’s not quite so innocent:

    /CIDInit /ProcSet findresource begin 12 dict begin begincmap /CIDSystemInfo <<
    /Registry (NDBBAF+ArialMT+0) /Ordering (T42UV) /Supplement 0 >> def
    /CMapName /NDBBAF+ArialMT+0 def
    1 begincodespacerange <0114> <012a> endcodespacerange
    2 beginbfrange
    <0114> <0114> <0144>
    <012a> <012a> <017C>
    endbfrange
    endcmap CMapName currentdict /CMap defineresource pop end end

A nicer case is this one, from a third PDF file:

    /CIDInit /ProcSet findresource begin
    12 dict begin
    begincmap
    /CIDSystemInfo <<
    /Registry (Adobe)
    /Ordering (UCS)
    /Supplement 0
    >> def
    /CMapName /Adobe-Identity-UCS def
    /CMapType 2 def
    1 begincodespacerange
    <0000> <FFFF>
    endcodespacerange
    1 beginbfrange
    <0000> <FFFF> <0000>
    endbfrange
    endcmap
    CMapName currentdict /CMap defineresource pop
    end
    end

I think this doesn’t comply with the explanation of `beginbfrange`
from the PDF spec:

> EXAMPLE 2 in this sub-clause illustrates several extensions to the
> way destination values may be defined. To support mappings from a
> source code to a string of destination codes, this extension has
> been made to the ranges defined after a beginbfchar operator:
> 
>      n beginbfchar
>      srcCode dstString
>      endbfchar
> 
> where dstString may be a string of up to 512 bytes. Likewise,
> mappings after the beginbfrange operator may be defined as:
> 
>      n beginbfrange
>      srcCode1 srcCode2 dstString
>      endbfrange
> 
> In this case, the last byte of the string shall be incremented for
> each consecutive code in the source code range.
> 
> When defining ranges of this type, the value of the last byte in the
> string shall be less than or equal to 255 - (srcCode2 -
> srcCode1). This ensures that the last byte of the string shall not
> be incremented past 255; otherwise, the result of mapping is
> undefined.

But evidently in this case the intent is to increment both of the
bytes of dstString, not just the last one.

But /Adobe-Identity-UCS isn’t always so nice.  Here’s another one,
from another file:

    /CIDInit /ProcSet findresource begin
    12 dict begin
    begincmap
    /CIDSystemInfo
    <<  /Registry (Adobe)
    /Ordering (UCS)
    /Supplement 0
    >> def
    /CMapName /Adobe-Identity-UCS def
    /CMapType 2 def
    1 begincodespacerange
    <0001> <046D>
    endcodespacerange
    10 beginbfchar
    <005F> <007C>
    <0061> <007E>
    <0070> <00E9>
    <0085> <00A3>
    <0087> <2022>
    <00A9> <00AB>
    <00AA> <00BB>
    <00AB> <2026>
    <00C2> <2219>
    <013C> <2033>
    endbfchar
    7 beginbfrange
    <0003> <0004> <0020>
    <0006> <003E> <0023>
    <0040> <0042> <005D>
    <0044> <005D> <0061>
    <00B1> <00B2> <2013>
    <00B3> <00B4> <201C>
    <00B5> <00B6> <2018>
    endbfrange
    endcmap
    CMapName currentdict /CMap defineresource pop
    end
    end

Strangely enough nobody seems to include the DSC comments in their
embedded CMaps.

U+2022 is a bullet, U+2026 is horizontal ellipsis, U+2219 is BULLET
OPERATOR, and U+2033 is DOUBLE PRIME.  So I think this is specifying a
transcoding from some Adobe encoding into Unicode.  The font in
question unfortunately uses /Identity-H as its /Encoding:

    344 0 obj
    <</Type /Font
    /Subtype /Type0
    /BaseFont /Georgia
    /Encoding /Identity-H
    /DescendantFonts [350 0 R]
    /ToUnicode 351 0 R
    >>
    endobj

So apparently in the font we will find DOUBLE PRIME at CID 013C, 316
decimal.

Georgia is not one of the PDF base fonts; it’s also embedded in the
file:

    356 0 obj
    <</Type /FontDescriptor
    /FontName /Georgia
    /Flags 6
    /Ascent 916.9922
    /Descent 219.2383
    /StemV 133.7891
    /CapHeight 692.8711
    /ItalicAngle 0
    /FontBBox [-490.2344 -303.2227 1796.3867 1074.707]
    /FontFile2 357 0 R
    >>
    endobj
    357 0 obj
    <</Length1 49484
    /Filter /FlateDecode
    /Length 29751
    >> stream

`ttfdump` on the extracted font file actually agrees with my inference
above about the encoding; the corresponding feature in TrueType is
actually also called `cmap`:

    'cmap' Table - Character to Glyph Index Mapping Table
    -----------------------------------------------------
    ...
                     Seg   107 : St = 2032, En = 2033, D =  57609, RO =      0, gId# = N/A
    ...
    Segment 107:
                    Char 0x2032 -> Index 315
                    Char 0x2033 -> Index 316

The actual text painted on the page using this font happens to be in a
ridiculously inefficient form:

    BT
    /F1 11 Tf
    1 0 0 -1 31.375 118 Tm
    <0031> Tj
    1 0 0 -1 39.813 118 Tm
    <0032> Tj
    1 0 0 -1 47.9985 118 Tm
    <0039> Tj
    1 0 0 -1 55.3301 118 Tm
    <0028> Tj
    1 0 0 -1 62.5166 118 Tm
    <0030> Tj
    1 0 0 -1 72.7163 118 Tm
    <0025> Tj
    1 0 0 -1 79.9082 118 Tm
    <0028> Tj
    1 0 0 -1 87.0947 118 Tm
    <0035> Tj

According to the above CMap, this encodes the text “NOVEMBER”.  In 283
bytes.  I guess it’s less, deflated; the content stream for that page
is 84551 bytes uncompressed, 16920 bytes deflated, so that's only
about 57 deflated bytes.

Annotations and actions
-----------------------

The whole string thing is super confused.  Line breaks are permitted
inside strings and are 0x0a LF, but paragraph separators in markup
annotation text are 0x0d CR (§12.5.6.2, p. 391, 399/756).

The whole annotation spec is a nightmare, and unfortunately a
necessary one for including hypertext links (§12.5.6.5).  Annotations
can have intents, titles, subjects, reply-tos, modification dates, and
author-specific states (marked, unmarked, accepted, completed).  It
even includes a separate richtext format that isn’t PDF (§12.7.3.4,
“Rich Text Strings”).  They can embed arbitrary file attachments
(§12.5.6.15), sounds (§12.5.6.16), and videos (§12.5.6.17).  Link
annotations can either go to “destinations” (§12.3.2) or take
“actions” (§12.6), “such as launching an application, playing a sound,
changing an annotation's appearance state.”

The action spec is 16 pages long and includes halfhearted warnings
against infinitely recursive and self-modifying code; in theory you
should only be able to program a sequence of actions, but triggers
include mouseovers, clicks, and page opening and closing.  And the
form spec lets you write actions in JS, including dependency-directed
recalculation of form fields!  And there's a SubmitForm action
(§12.7.5.2) that lets you submit a data form to a URL!  And ImportData
(§12.7.5.4) to load data from a local file!  Plus also GoTo actions to
navigate around the document (§12.6.4.2, though you can also link
within the document without using an action) and URI actions
(§12.6.4.7, with an IsMap parameter).  And you can hide or show
annotations (Hide, §12.6.4.10), which can be of a variety of drawable
types, as well as do a display transition (§12.6.4.14, transitions
listed in §12.4.4.1 like Wipe, Dissolve, etc., with a duration), make
“optional content groups” visible or hidden (§12.6.4.12), or reorient
a 3-D view (§12.6.4.15).

It doesn’t look like you can do arbitrary drawing from these actions,
though, though maybe you could get pretty far with custom fonts.  Or
modify the document tree, so I’m not sure what's up with the
prohibition on self-modifying code.

The JS stuff is specified in a totally separate document, “Adobe
JavaScript for Acrobat API Reference”.

Streams
-------

A curious thing is that this is, I think, an indirect dictionary
object:

    31820 0 obj
    << /Length 10 >>
    endobj

While this is not a dictionary object:

    31820 0 obj
    << /Length 10 >>
    stream
    helloworld
    endstream
    endobj

That’s a stream object.  Stream objects must be indirect objects
(§7.3.8.1) and cannot be nested within object streams like most other
indirect objects (§7.5.7).  So when you are parsing either of these,
you don’t know if you’re parsing a stream object or a dictionary
object until you reach the `endobj` or `stream` keyword.  But you are
guaranteed to hit one or the other.

The easiest way to think about this is as a sequence of stack
operations: `stream` is an operation that consumes the dictionary on
the stack and uses it to parse the following data before returning
control of the input stream to the normal PDF parser.
