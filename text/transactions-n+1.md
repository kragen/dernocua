Reading [a note on Rust for web
APIs](https://macwright.com/2021/01/15/rust.html) I ran across the
“n+1” problem, familiar to anyone who’s done database-backed web
sites: 

> The n+1 problem is something that everyone building web applications
> should understand. The gist is: you have a page of photos (1
> query). You want to show the author of each photo. How many queries
> do you end up with: 1, combining the photos & authors, or a query
> per photo to get the author after retrieving the photos? Or 2
> queries, with the second having something like `user.id IN ids` to
> fetch all authors in a single pass and then reconnect them to their
> photos.

Now, the most straightforward kind of ORM to write will kind of push
you to having the n+1 problem, but there are a variety of design
approaches to writing an ORM (or other database layer) that make it
possible to avoid it.  In Django’s ORM, for example, you'd say
`photo.author_id.name` to get the field `name` from the related row in
the authors table, but whether or not this results in an n+1 problem
depends on how `photo` was fetched.  If you did something like `for
photo in Photo.objects.all()` then by default you have an n+1 problem,
but [you can specify][0] `for photo in
Photo.objects.all().select_related('author')` to do just a single
query joining both tables.  And Django has a janky special-purpose
`author__publisher__country` syntax that allows following multiple
levels here, and a `prefetch_related` that handles one-to-many
relationships in one query per table.  Other systems such as Rails
have analogous facilities.

[0]: https://docs.djangoproject.com/en/dev/ref/models/querysets/#prefetch-related

The trouble with this is that to some extent it violates DRY.  You
have to specify *twice* that you are going to access the photos’
authors: once when you construct the query, and again later when you
use it.  If you don’t so specify, your code will still run and produce
the same results, but it may run two orders of magnitude slower (or
more, if your database is fucked up enough!), which may be better or
worse than just crashing, depending on your situation.  When you
modify the set of attributes used from each photo, you must also
remember to modify the query accordingly, which is likely in a
different file from the HTML template where the attributes are used.

One approach is to build up the `prefetch_related` set lazily: when an
`author` object is fetched via one of the `photo` objects, we can
notify the original query that the `photo` came from that it was
inadequate, and it needs to add a `.prefetch_related('author')`
and execute it forthwith.

Also, though, I’ve been enthusiastic about transactions.  How can
transactions help?

Maybe we can rerun the query
----------------------------

Closely related to the “build up `prefetch_related` lazily” approach
is “abort the transaction whenever it tries to read data that isn’t
yet loaded, and retry it when the data arrives”.

Maybe we can use type inference
-------------------------------

Here’s a wild non-transaction approach.

If we statically infer the set of attributes required on an argument
passed in to the template, we can use that to build up a query (or
finite number of queries) whose results have the right type.  The
“type” in this case is something like a solution to a set of
equations describing a sort of graph:

    photo = {url: str, author: α, ..}
    α = {name: str, publisher: β, ..}
    β = {country: str, ..}

Here `str` is a concrete type (an atomic constant of the universe of
types) and the `{..}` syntax specifies a minimal set of fields
(outgoing graph edge labels) that must be present at the specified
node.  In this case the equations are acyclic and so could be directly
solved by substitution:

    photo = {url: str, author: {name: str, publisher: {country: str, ..}, ..}, ..}

If we additionally have a `.` operator on field labels (analogous to
Django’s `__` mentioned above) perhaps we can use a distributive law
to expand this:

    photo = {url: str, author.name: str, author.publisher.country: str, ..}

This sort of distributivity suggests that perhaps we are looking at a
semiring.  You could however reasonably argue that the two statements
above are not equivalent: in the second case, the photo might have two
or more authors, one which has a string name and another of which has
a publisher with a string country.  But for the moment I will explore
this possibly unsound path of reasoning to see if there’s some way to
chop off its feet to fit it into the semiring bed.

If we make the additional simplification of replacing “the concrete
type str” (a node in the universe of types) with “a node with the
field str” then really what we have here is

    photo = url str + author α
    α = name str + publisher β
    β = country str

    photo = url str + author (name str + publisher (country str))

    photo = url str + author name str + author publisher country str

I’m not quite sure how to interpret the semantics here: are these
really structural types, in the sense of the OCaml lower-type-bound
syntax I’m aping?  (Presumably `photo` here is a different sort of
name than `url`, `author`, and `str`.)  Are they relations, with
multiplication/concatenation being interpreted as composition and
addition being interpreted as relational product (and, if so, does it
make sense to bring in Kleene closure, and do we get a Kleene algebra,
and what about the inverse relation)?  (Binary relations are matrices
indexed by the relation’s domain and range over the Boolean semiring,
and their matrix multiplication does correspond to composition, but
their matrix addition is of course just simple union, not relational
product; relational product is more closely allied to intersection.)
Does this expression represent a query that could be evaluated,
perhaps over a directed graph or a SQL database, and return a table
with three columns?  Is this just Binate again with different syntax?

Nevertheless, in some cases the solution is not quite so simple:

    x = Guy.objects.get(id=id)
    while x.manager_id is not None:
        x = x.manager_id
    return x.name

Type inference here gives us something like:

    guy = {manager: guy, name: α ..}

Which is to say:

    guy = manager guy + name α

Does allowing the nose of Kleene closure into the tent allow us to
solve this equation, with something like the following?

    guy = manager* (name α)

See also file `parson-rpn.md`.

Maybe we can have stuff in RAM already
--------------------------------------

One of the claims I was making is that pervasive transactionality
ought to make cache invalidation more straightforward and performant.
So maybe if our database is more like an OODBMS like ObjectStore or
Gemstone, the n+1 query problem stops being a problem at all: each
traversal of an `author` link from a `photo` is just a read of a
transactional variable, so it’s not an outrageous cost and doesn’t
necessarily involve a context switch or network round trip.

Maybe we can pipeline
---------------------

If all of the *n* individual fetches of the author of a photo can run
concurrently, with their small queries being pipelined to the database
server and back, then you still have n+1 queries, but only two round
trips, and that might be acceptable.
