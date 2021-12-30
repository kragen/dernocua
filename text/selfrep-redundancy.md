A complex self-replicating system such as a hen contains a large
number of somewhat unreliable subsystems, such as an intestine.  If
the intestine ruptures, the chicken will die without being able to
produce another chicken; if the ovary dies, the hen will survive but
will produce no further eggs.  (Hens normally have only one
functioning ovary.)  As the number of such SPOFs grows, the chances
that one of them will fail prior to self-replication also grows; for
the total fertility rate to remain above the replacement threshold,
the reliability of each of these systems must also increase.

The replication rate of hens is somewhat complicated to calculate:
they [start laying at 18–24 weeks of age][0], up to 250 eggs per year,
maybe 75% fertile, requiring 21 days of incubation time.  Commercial
broiler operations kill their hens at one year of age, because
fertility declines below 50% at a year, and egg operations at one or
two years but otherwise chickens will typically live 3–7 years,
[laying less eggs each year][1]: maybe 250, 200, 175, 150, 125, 110,
90.  Half the eggs will be roosters.  [A hen can incubate 12–15 eggs
at a time][3], and normally only does this (“goes broody”) once a
year, and never more than three times a year, so the figures below
will assume artificial incubation.

[0]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2775730/ "Inheritance of fertility in broiler chickens, by Anna Wolc, Ian MS White, Victor E Olori, and William G Hill, Genet Sel Evol. 2009; 41(1): 47, PMCID: PMC2775730, PMID: 19874616, 10.1186/1297-9686-41-47"
[1]: https://www.purinamills.com/chicken-feed/education/detail/how-long-do-chickens-lay-eggs-goals-for-laying-hens
[3]: https://silkie.org/how-many-chicks-can-a-chicken-look-after.html

A simple simulation (with a slightly simplified version of that model)
reveals that this works out to something like a rate of increase of
3.3% per day, a doubling time of about 21 days.  Naïvely, this would
suggest that, disregarding infant mortality, as long as the hens’ MTBF
is more than 21 days, they would still produce replacements, but I
don’t think that’s actually true; only 1 in 101 would live to 20
weeks, and on average would produce less than 21 offspring.  I think
the actual crossover point (without calculating it) is an MTBF of just
over 32 days, at which point more than 1 in 21 hens survive to
reproductive age.

If hens have a single SPOF, then, such as an ovary, it needs to have
an MTBF of over 32 days to reach replacement fertility.  If they have
two SPOFs, such as an ovary and an intestine, one or both of them
needs to have an MTBF of over 64 days.  If they have 32 SPOFs, all but
one of them need to have an MTBF of over 1024 days.

A little bit of redundancy can help somewhat here, but without
regeneration, it has rapidly diminishing returns.  Hens have two eyes,
and [usually die quickly if they go blind][2], so getting to 32 days
of MTBF only requires each eye to have about 21 days of MTBF.  If they
had ten eyes, each eye would only need to have 11 days of MTBF.  For
Argos hens with 100 eyes each, to reach 32 days, each eye only needs
to have 6.2 days of MTBF.  Actually, though, the situation is much
worse than that, because the number of surviving sighted hens drops
off much faster than the usual exponential distribution; with 6.2 days
of MTBF for 100 eyes, less than 1 of every 1000 hens survives to 14
days, and less than one in a million to 21 days.

[2]: https://randyschickenblog.blogspot.com/2017/02/a-blind-hen.html

Alternation of generations and multiple genders are a significant
subject here.  In most animals the alternation of generations is
subtle and easy to dismiss, but plants like ferns make it much more
visible.  Multiple “genders” of manufacturing plants might be
specialized to produce particular parts or materials, which then must
all be combined.