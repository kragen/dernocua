Originally posted at <https://news.ycombinator.com/reply?id=26441466&goto=threads%3Fid%3Dkragen%2326441466>

I guess you aren’t trolling; you’re just confusing the part of
programming that you know about with the whole field.  But there are more things in heaven and earth, Horatio, than are dreamt of in your
philosophy…

You said, “If you allocate a a few bytes at a time, it will top out in the ballpark of 10 million per second per core.”  In my link above, I demonstrated a one-line program which, allocating a few bytes at a time, tops out at 150 million allocations per second per core; if the memory stays in use long enough to survive a minor GC, that drops to 100 million allocations per second per core.  It’s using the same allocator SBCL uses for everything (except large blocks), and these performance numbers include the time for deallocation.  It takes into account all of the things that make memory allocation problematic for performance.†  But it does an order of magnitude more allocations per second than you’re saying is possible.  Even LuaJIT 2.0.5 on this same laptop manages 42 ns per allocation, 23 million per second:

    function nlist(n)
        local rv = nil
        for i = 1, n do
            rv = {i, rv}
        end
        return rv
    end

    function mnlist(m, n)
        print('m='..m..' n='..n)
        for i = 1, m do nlist(n) end
    end

    mnlist(500000, 2000)

It’s true, as you say, that the way it works is similar to “adding [small numbers] to the size of a C++ vector with a large capacity on each iteration of a loop.”  (It’s not “adding 1” because allocations of all sizes are served from the same nursery; interspersing different open-coded allocation sizes affects performance only a little.)  But just doing that doesn’t save you from writing a garbage collector and implementing write barriers, or alternatively doing MLKit-style static reasoning about lifetimes the way you do to allocate things on a per-frame heap in C++.

It’s *also* true that, as you say, “memory allocation is often huge low hanging fruit for optimization.”  You aren’t going to get this kind of performance out of HotSpot or a malloc implementation, not even mimalloc.  So if you’re using one of those systems, memory allocation is an order of magnitude more expensive.  And, if you’re concerned about *worst-case* performance—latency, rather than throughput, as HFT people and AAA game programmers are—probably *no* kind of garbage collection is a good idea, and you may even need to avoid allocation altogether, although recent versions of HotSpot make some remarkable claims about worst-case latency, claims which may be true for all I know.

Of course, even when it comes to throughput, there is no free lunch.  An allocator design so heavily optimized for fast allocation necessarily makes mutation more expensive—SBCL notoriously uses segfaults for its write barrier so that writes into the nursery are as fast as possible, a cost that would be intolerable for more mutation-oriented languages like Java or C++; and heavy mutation is generally a necessary evil if latency is important.  (Also, I think there are algorithms, especially in numerical computation, where the best known mutation-based algorithms have a logarithmic speedup over the best known pure functional algorithms.)

You can find a more detailed discussion of some of the issues in <https://archive.fo/itW87> (Martin Cracauer’s comparison of implementing memory allocation in LLVM and SBCL, including years of experience running SBCL in production and extensive discussion of the latency–throughput tradeoff I touch on above) and the mimalloc technical report, <https://www.microsoft.com/en-us/research/publication/mimalloc-free-list-sharding-in-action/>.  The mimalloc report, among other things explains how they found that, for mimalloc, BBN-LISP-style per-page free-lists (Bobrow & Murphy 1966, AD647601, AFCRL-66-774) were faster than pointer-bumping allocation!

______

† This build of SBCL does have multithreading enabled, and the allocation benchmark takes the same amount of time running in a separate thread, but on my machine it doesn’t get a very good speedup if run in multiple threads, presumably due to some kind of allocator contention.
