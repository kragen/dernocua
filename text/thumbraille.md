Braille Unicode characters fit 8 square pixels per character cell.  We
can make a thumbnail view of a text file (such as a C program) by
mapping its character cells to these pixels; if we reduce 8× linearly,
then each Braille character cell represents 8 columns of 8 lines with
its 2×4 pixels.  This maps 4 columns of 2 lines to each pixel.  Some
kind of threshold for how much text needs to be in this area to light
up the pixel ought to work reasonably well to give a thumbnail view;
if you can fit 40 lines of text on the screen then you can fit
thumbnails of 320 lines of text, which is a lot; 410 out of the 443
"source files" (`*.c *.cc *.h *.ml *.java *.py *.lisp *.html`) in
~/dev3 are shorter than this.  Also the thumbnail will only take up 10
columns at a standard 80-column width, so maybe you can do multiple
columns of thumbnail.

Alternatively you could scroll horizontally by pages/columns, and put
the thumbnailed pages at the top or bottom of the screen.  This would
take up 5 lines out of the 40.