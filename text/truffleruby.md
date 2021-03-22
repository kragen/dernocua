I recently learned about Chris Seaton’s dissertation on TruffleRuby,
an efficient implementation of Ruby he wrote — 90% of the performance
of C in some cases.  It’s built on top of Graal, which is now free
software, and I thought taking some notes would be worthwhile.

Really great stuff
------------------

The dissertation itself is not a great pleasure to read, but it has a
lot of really first-class information in it.

He mentions “value profiling” where TruffleRuby observes that a
particular edge in the dataflow graph is usually a constant value and
so partially evaluates the rest of the graph with respect to it.  And
he has a generalized “inline cache” mechanism (“dispatch chains”,
introduced p. 101, ch. 5) that caches the results of expensive
reflection mechanisms, such as calling a method determined by a
selector argument, and checks to see if they are still valid.  Both of
these seem highly relevant to Bicicleta.

He mentions SubstrateVM, a feature of Graal which I hadn’t heard of,
but which aims at ahead-of-time compilation for, mostly, JVM
applications.

On p. 90 he mentions the `ExactMath` class from Graal, which throws an
exception on arithmetic overflow of integers, allowing the TruffleRuby
implementation to transparently fall back to bignums upon overflow.
This seems like an interesting technique; in a COMFY-style 

If we suppose that the diagram of “a conventional PIC” on p. 104 is
literally correct, it may explain why Ur-Scheme got such (relatively
speaking) reasonable performance with such simple techniques: the PIC
diagrammed here doesn’t inline Fixnum#div or Double#div, but instead
invokes them through a conventional call-return mechanism!  (Though he
does say “or possibly inlined” beneath it.)

The PSD.rb he mentions in his blogpost was also one of his early
evaluation benchmarks (p. 108).

His name for “specialization” seems to be “splitting”, or perhaps
splitting is a certain kind of specialization.

Rails support
-------------

On p. 93 of the dissertation, he says TruffleRuby doesn’t run
Rails yet, even though a lot of his motivating examples about what
makes Ruby difficult to implement efficiently come from Rails.
But <https://github.com/oracle/truffleruby> says TruffleRuby *does*
run Rails now:

> TruffleRuby can run Rails and is compatible with many gems,
> including C extensions. However, TruffleRuby is not 100% compatible
> with MRI 2.7 yet. Please report any compatibility issues you might
> find. TruffleRuby passes around 97% of ruby/spec, more than any
> other alternative Ruby implementation.
> 
> TruffleRuby might not be fast yet on Rails applications and large
> programs. Notably, large programs currently take a long time to
> warmup on TruffleRuby and this is something the TruffleRuby team is
> currently working on. Large programs often involve more
> performance-critical code so there is a higher chance of hitting an
> area of TruffleRuby which has not been optimized yet.

Apparently he got [hired by Shopify, which uses Rails, but not to make
this happen][37].  There he confesses:

> Baseline memory is often pretty high, and it takes memory to run our
> optimisations, but TruffleRuby when it’s running then has
> optimisations to reduce memory used for each request, such as
> removing object allocations, zero-copy strings, and so
> on. Realistically TruffleRuby is designed for larger deployments
> serving many users, and probably isn’t suite for a 500 MB $5
> instance, this is true.

[37]: https://discuss.rubyonrails.org/t/plans-for-truffleruby-support/75381

Disappointments
---------------

He kind of begs off evaluation of warmup time, startup performance,
and memory usage, saying that he doesn’t know how to evaluate them,
that they aren’t important for his purposes, and anyway he wants to
trade them off for higher peak performance.  It would seem to me that
in order to trade something off you would need to know how much of it
you have and how much of it you’re paying in order to know if it’s a
good tradeoff.  Overall I think this is sort of a problem with the JVM
in general.

A disappointing thing about the dissertation is that it scales all the
reported performance results by an opaque fudge factor, so none of
them are individually falsifiable, are comparable to other published
results, and none provide even an order-of-magnitude estimate of
performance that could be used for other purposes.  For example,
perhaps an alpha-blending algorithm is reported, and in TruffleRuby it
can alpha-blend 2.7 times as many pixels per second as in MRI and 2.3
times as many as in Rubinius.  Does that mean it is alpha-blending
2700 pixels per second, 2.7 million, or 2.7 billion?  This information
is nowhere to be found, not in Figure 5.4 or anywhere else in the
dissertation.

It’s profoundly disappointing to find this statement on p. 94:

> Another advantage is that [microbenchmarks] are typically very well
> understood by researchers which allows new implementations to be
> quickly tuned to run them well, but they are highly unrepresentative
> of real Ruby code. For example, nobody is making money by running a
> web service in Ruby to provide solutions to n-body problems.

This implicit equation of “real Ruby code” with “making money” perhaps
explains some of the previous disappointments: he seems to consider
code to solve physics problems to be ‘fake code’ because what he
values is making money, not whatever else you might be able to achieve
by solving physics problems, such as understanding things more deeply.
And I guess nobody was paying him to polish this dissertation... but I
wouldn’t say that made it a “fake dissertation”.  But maybe that’s why
it says things like this (pp. 75–76):

> This means that adding additional cores will not reduce the response
> time for a single customer. [sic] Increasing the memory capacity of
> a server is more easy as the limit [sic] on the quantity of memory
> that can be attached to a server is very high and a single
> sequential process [sic] can take advantage of all memory attached
> to a system.

### Memory usage and performance ###

Overall the statistical performance evaluation that is the centerpiece
of the dissertation’s presented results is sort of disappointing.  Not
only does he give up on reporting any absolute performance numbers
that would be comparable to other publications, but also he throws up
his hands at statistical significance testing, taking independent
sample measurements, and in general on quantifying the sources of
error in his measurements.  (“However, there are also natural reasons
why there may be a visual pattern [in a Kalibera–Jones lag
plot] — some benchmarks just appear to be cyclic in nature, no[]
matter how long they are given to warm up.”  (p. 87), though he seems
not to have actually included any lag plots of his own data in the
dissertation; the plots on this page are from the Kalibera and Jones
paper.)

This gives me more appreciation for why he didn’t post any details of
allocation cost in the HN thread at the level of detail I was looking
at: he’s considering systems that are so complex and poorly understood
that it would be misleading to say, “this is the code the compiler
generates in this case,” because that is very dependent on an immense
and delicate web of circumstances.  Moreover, he was mostly chasing
large and obvious speedups, not small and subtle ones, so even a very
vague idea of what was going on would be sufficient.

He says it’s “easier to scale memory than processor power”, which is
true in a sense — if your *request latency* is limited by memory
usage, in 02021 or even in 02014 when he wrote the dissertation, it’s
much easier to get a machine you can jam twice as much RAM into as to
get a machine running at twice the clock speed.

But “scaling” generally isn’t about latency but about throughput: for
a network service, cutting your latency from 100 ms to 10 ms is
excellent, from 10 ms to 1 ms is useful, from 1 ms to 100 μs is
sometimes good, from 100 μs to 10 μs is pointless, and from 10 μs to
1 μs is probably unobservable.  *Scalability* of latency is a
non-goal.  (Seaton seems to be aiming lower than this, though: in one
case (p. 86) he compares a hypothetical 1-second latency to a
hypothetical 100-second latency, which is a dispiriting order of
magnitude to be considering.)

By contrast, *throughput* is eminently scalable.  If your Ruby web
service serves 10 requests per second on one EC2 m5.xlarge instance,
it will probably serve 1000 requests per second on 100 of them, and if
you set up some readslaves (or let Amazon do it) you can probably get
100,000 requests per second on 10,000 m5.xlarge instances, and maybe
you can scale to a million or ten million requests per second.  There
are some network services that do more, though usually not that
inefficiently.  In general, you can often usefully scale by several
orders of magnitude more than you can scale latency.

So it makes sense to ask what the limiting resource is for scaling the
throughput of a given application: CPU?  Memory?  Memory *bandwidth*?
L1 cache?  Disk bandwidth?  Network bandwidth?  Disk latency, or
rather its reciprocal?  There is *almost surely* one limiting resource
at any given time, and increasing the other resources — or,
equivalently, using them more efficiently — will not increase
throughput.  Seaton implicitly points this out when he says (p. 80):

> ...the application may create caches that are only cleared when
> there is memory pressure. This makes us consider whether optimising
> for low memory usage is even a desirable goal. If we have memory
> available in the system, why not use it?

This is a sensible question if the limiting resource is something
other than memory, such as CPU time, or if your evaluation objective
is latency rather than throughput.  But a very common case in everyday
web services is for memory rather than the other possibilities above
to be the limiting resource.  httpdito can handle some 25’000 HTTP
requests per second on my laptop in part because it only uses one 4KiB
page of memory per concurrent request.  AWS Lambda usage is presently
billed at seventeen nanodollars per gibibyte millisecond, starting at
128 MiB; a “lambda function” that uses one gibibyte costs eight times
as much to run per millisecond as one that uses 128 mebibytes.
(Though AWS does claim they scale CPU availability proportionally.)

A typical sort of situation is a frontend host dynamically generating
a web page using a few dozen SQL queries sent to a remote database
server, perhaps spending 64 ms in all waiting on SQL replies.  During
these 64 ms, the frontend host can spend its CPU time serving other
concurrent web page requests, but it cannot spend its RAM on those
other requests — the RAM is tied up until it gets the response back.
Perhaps each request only take 2 ms of computation, so if it is
CPU-bound, each core can do the computation for 32 other web pages
while it’s waiting for the SQL responses.  If it has 4 cores, its
response times will remain consistent until it’s processing 128
concurrent requests, about 1900 requests per second.

But, if processing each of those requests is using 256 mebibytes of
RAM, it needs 32 gibibytes of RAM to reach this level of concurrency.
The m5.xlarge instance type has 4 (virtual) 3.1GHz Xeon Platinum 8175M
cores but only 16 gibibytes of RAM, so at this performance level, its
CPU couldn’t be more than 50% utilized in this scenario.  If the
amount of time spent waiting on I/O is higher, even smaller memory
usage becomes a problem; by contrast, faster I/O, like SSDs, reduces
memory demands proportionally.  Typically SSDs are around 128 times
lower latency than spinning rust — [typical NAND Flash chips take
16–128 μs to read a 2048-byte page rather than the 8192 μs typical of
spinning rust](energy-autonomous-computing.md), so there is the
opportunity to redesign the system architecture for higher throughput
by getting better CPU efficiency at the expense of RAM efficiency.

Actually, this shift seems like maybe a big opportunity for things
like TruffleRuby.

### Conflating metaprogramming with reflection ###

Frequently the dissertation says “metaprogramming” when it means
“reflection” or even specifically “reflection” or even more
specifically “dynamic method invocation”; though, in places (§5.2,
p. 102) it acknowledges that macro expansion and runtime code
generation are also metaprogramming, in others it contradicts this:

> However metaprogramming has not received the same research attention
> and is often not optimised, even in mature language implementations.
> ...  In Ruby, probably more so than in other languages,
> metaprogramming should not be viewed by implementers as a
> side-channel that does not need to be optimised, but instead as just
> another form of dispatch. (p. 101)

> This is a good example of *metaprogramming* being used to make the
> program simpler (from the perspective of the Ruby community) but
> *the dynamism* not actually being needed in practice.  (p. 108,
> emphasis mine)

### Dispatch chains ###

Chapter 5 outlined how dispatch chains in TruffleRuby work, and
presented measurements showing that in some cases they produce good
performance, but it sort of handwaves about how this happens; all the
magic remains behind Graal’s curtain:

> Our second contribution in this chapter is to observe that the
> structures we have described above are trees, and so can be
> implemented using the same nodes as we use to implement the Ruby
> AST. Each condition in the chain is implemented as a node with a
> child node for the cache-miss case, and a child node for the
> cache-hit case, in the case of first level of caching, or a
> reference to the method to be called in the case of the second level
> of caching. ... we rely entirely on the partial evaluation in
> Truffle’s Graal backend to remove the degree of freedom in the
> method name if we are not using it. ... we have confidence in the
> partial evaluation phase of Truffle’s Graal backend to propagate
> that constant and entirely constant fold and remove the logic in the
> dispatch chain that handles varying method names. (pp. 106–7).

It would be useful to see the output of the partial evaluation phase
of Truffle’s Graal backend, or of the entire backend, in order to
understand whether this confidence is justified, and if so, under what
circumstances.  Instead all we get are execution-time boxplots from
which the absolute units of time have been carefully erased.
