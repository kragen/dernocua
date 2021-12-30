(Posted originally on the orange website.)

I wonder what value you could add to this [service for building
websites by writing on paper] with a digitally referenced notebook?
By printing an unobtrusive sort of barcode on each page, you could
determine which part of which page of which notebook each scanned
pixel came from, and what lighting conditions it was photographed
under.  What could you do with that?

Well, the simplest and most greyface application is forms; you can
define particular areas of each page as being particular form fields.
If you’re blogging, you might have a field for a “slug” that appears
in the URL, for example, or a field for tags, or checkboxes for some
tags (plus a special page to declare the meanings of the checkboxes).
Or, if you’re tracking expenses, you could have a checkbox for each
expense category and columns for the date and the amount.

For me, the special feature of paper notebooks that cellphones and
other computers suck at is drawing.  If I want to draw a diagram or
illustration, it just works much better on paper: my pencil point
occludes much less drawing area than my finger does, there’s no
tracking error where the ink appears 2 mm to the side of the point, it
has much lower latency, and I can draw finer lines.  But scanning
those drawings into a computer is a pain, because I have to illuminate
them evenly and hold them flat while I photograph them, which still
probably involves some perspective distortion.  Barcodes on the paper,
together with reference lines and reference color swatches, could
solve that problem, as well as providing information about which parts
of the paper are occluded, if any.

For a few special applications like numismatics and entomology, the
paper could provide a precise physical measurement reference for
specimens.

Combining drawing with filling out forms, you can make a font from
your handwriting; this is enormously easier if you can correct the
various distortions.  In <http://canonical.org/~kragen/oilpencil/> I
spent about 24 hours fiddling with various graphics programs, but
there was a website I found somewhere where you can print out a form,
draw the font on it, upload the scan, and download your TrueType font.
This kind of thing might help with training OCR, too, especially if
you don’t have access to GPT-3.  (Or if OpenAI decides to peremptorily
destroy everything you’ve built because one of your users uses your
service to write about their dead fiancee:
<https://towardsdatascience.com/openai-opens-gpt-3-for-everyone-fb7fed309f6>)

Other ways to combine drawing and filling out forms include sketching
orthographic projections to build 3-D models; coloring a coloring
book; drawing maps for Minetest and similar grid-cell games
(especially 2-D ones); drawing heightfields; and sketching different
keyframes of an animation to automatically morph between.  You could
even draw a 2-D continuum of keyframes, thus providing an animation
character that’s continuously variable along two different axes; you
might put time on the theta axis and some sort of emotion along the
radius axis.

(You can also apply these ideas with drawings that are input via other
media, such as touchscreens, Wacom tablets, and mice, not only
scanning paper.  When you’re scanning paper it’s hard to get feedback
as you’re drawing, although you could maybe glance at your cellphone
screen periodically, or use a projector like DynamicLand, or have a
continuously updated monitor using a webcam feed.  It could even use
the occlusion information from the barcode to patch in remembered
images wherever your hands were occluding the paper.)

What should the barcodes look like?

In 02001 Anoto announced their “Digital Paper” approach:
<https://www.wired.com/2001/04/anoto/>.  As explained in
<https://en.wikipedia.org/wiki/Digital_paper> this uses an unobtrusive
2-D barcode scanned by a camera in a “digital pen” (later called the
“Fly Pen”, 02005) to locate the pen in an enormous global “virtual
desktop”; I think the NeoLAB “Neo smartpen” works the same way.  This
was all before cameraphones went mainstream and high resolution.  They
got 300 patents but fortunately everything they filed in 02001 expires
this year.  Anoto’s barcodes use a grid of slightly displaced grid
dots.

The Fly Pen provided a sort of graphical user interface on the paper,
using audio for output.  It was sort of aimed at kids doing schoolwork
and playing games.  It failed in 02009.  The founder started a new
company called Livescribe focusing on notetaking; the Livescribe
smartpen allows you to spatially organize and annotate a continuous
audio recording.  It has been more commercially successful:
<https://en.wikipedia.org/wiki/Livescribe>

Tiny unobtrusive dots might not reproduce reliably on a cellphone
camera, though having been published in WIRED in 02001 means the
technique is in the public domain (or will be next year).  A better
idea might be to use thin horizontal and vertical grid lines whose
thickness varies slightly, perhaps in a pastel subtractive primary
like cyan, magenta, or yellow; then you can optionally remove them in
software after scanning.  Scanning a whole page at a time, instead of
a tiny area around a pen point like the “digital pens” described
above, gives you a great deal more space for redundant page ID data in
the barcode; probably 48 bits or so is sufficient.
