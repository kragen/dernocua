Looking at PDF, whose syntax derives from PostScript, I’m struck by
the fact that a lot of its constructs are most easily parsed right to
left.  An object reference like `16 0 R` starts with an integer
object, and so you end up having to backtrack if you’re using a PEG
parser.

If instead you parse it right to left, you don’t have this problem as
much; the R announces that you are looking at an object reference, and
it contains the following two integers.  Similarly, in a content
stream, you may encounter a text object like Example 1 from §9.2.2 of
the PDF 1.7 spec, ISO 32000-1:2008:

    BT
       /F13 12 Tf
       288 720 Td
       (ABC) Tj
    ET

As an S-expression, this is `(text (font 'F13 12) (pos 288 720) (paint
"ABC"))`; `Tf` is the operator that sets the font, `Td` is the
operator that sets the position, and `Tj` is an operator that draws
text.  Reading this backwards, it’s trivial to predict what you’re
going to have to parse; reading it forwards, you either need to
maintain a stack of pending values like 288 and 720, or do a lot of
backtracking.

However, individual tokens in here are more easily read forwards;
`/F13` looks like an integer if you look at its last 0, 1, or 2
characters, and perhaps like an operator if you only look at its last
3.

Is there a way to get PEG-like memoization for an asymptotic
performance guarantee and flexibility, while maintaining a LALR-like
stack of bottom-up items that can tell us what parses to even attempt?
Is that even a meaningful question?