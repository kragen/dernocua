The PDF standard (since PDF 1.1) has the amusing terminology of
“beads” on a “thread” of “articles”.  I think “bead” might be better
than “line” or “card” or “page” for my card-based hypertext thing
(suggesting perhaps its intellectual descent from wampum).

And indeed the meaning in PDF is closely related:

> Some types of documents may contain sequences of content items that
> are logically connected but not physically sequential.
> 
> EXAMPLE 1: A news story may begin on the first page of a newsletter
> and run over onto one or more nonconsecutive interior pages.
> 
> To represent such sequences of physically discontiguous but
> logically related items, a PDF document may define one or more
> articles (PDF 1.1). The sequential flow of an article shall be
> defined by an article thread; the individual content items that make
> up the article are called beads on the thread. Conforming readers
> may provide navigation facilities to allow the user to follow a
> thread from one bead to the next.

The beads are “chained” with “N (next) and V (previous) [attributes]”,
while they link to their actual contents with “P” for the page object
and “R” for the rectangle on the page.

*My* intent, of course, is to eliminate or ephemeralize the physical
sequence entirely, rather than to simply superimpose a secondary
sequence on it.
