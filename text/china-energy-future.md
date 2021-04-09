I was surprised to learn that [China built more wind-powered
electrical generating capacity last year][0] than [coal][2], and also
more solar than coal.  I [posted about this on the orange website][1].

[0]: https://www.reuters.com/article/us-china-energy-climatechange-idUSKBN29Q0JT
[1]: https://news.ycombinator.com/item?id=26227823
[2]: https://www.reuters.com/article/us-china-coal-idUSKBN2A308U

Specifically, in 02020, the People’s Republic of China installed
71.7 GW of new wind capacity, 48.2 GW of new solar capacity (which was
already [larger than the rest of the world combined][10]), and
38.4 GW(e) of coal capacity.  Assuming typical capacity factors of 40%
for wind, 25% for solar, and 60% for coal, that would add up to 23 GW
average new coal, 29 GW average new wind, and 12 GW average new solar.
(But China’s capacity factors are lower; see below.)  New solar
installations worldwide double on average every three years, which has
slowed down from every two years in the 02010s.

[10]: https://en.wikipedia.org/wiki/Renewable_energy_in_China

Solar capacity factors vary widely by region.  In California they’re
28.1%, but in Germany and the Netherlands only 10%.

For scale, total [German energy use was about 3800 TWh/year over
02007–02013][4], including things like transport fuels.  This works
out to about 430 GW.  Of this, 576 TWh/year (65.7 GW) was produced as
electrical energy, which had reduced to (+ 60.94 81.94 35.56 59.08
131.69 50.7 45.45 18.27) = 484 TWh/year (55 GW) by the year 02020.

[4]: https://en.wikipedia.org/wiki/Energy_in_Germany

But China is a larger country than Germany.  [Chinese marketed energy
consumption][5] was 28 PWh/year (3.2 TW) in 02010, of which
3.9 PWh/year (440 GW) was electric.  [In 02019 they produced 7330 TWh
electric][6] calculated as (+ 4554 233 148 349 1270 32 405 224 113)
rounded to three places.  That’s 836 GW.  (The 32 TWh of
pumped-storage hydro may be double-counted.)  In 02019 224 TWh/year
(26 GW) was produced from solar and 405 TWh/year (46 GW) from wind,
using 204 GW of solar capacity (capacity factor 13%) and 209 GW of
wind capacity (capacity factor 22%).  Also the 4554 TWh/year from coal
(519.5 GW) is on a 1.041 TW basis, so their capacity factor is only
50.0%.  Hopefully they’ll start installing their energy plants in more
propitious places, like the Gobi, and the capacity factor will go up.

So probably last year’s new installations of 38.4 GW (coal), 71.7 GW
(wind), and 48.2 GW (solar) will produce on average 19.2 GW (coal),
16 GW (wind), and 6.3 GW (solar).  The resulting 22 GW (average) of
renewable energy added last year amounts to 2.6% of the total current
*electric* energy use of China.  If we assume that China’s *total*
energy use has increased by 90% since 02010, just as their
*electrical* energy use did by 02019, it would now be 6.1 TW, and
22 GW is 0.36% of it.

[5]: https://en.wikipedia.org/wiki/Energy_policy_of_China
[6]: https://en.wikipedia.org/wiki/Electricity_sector_in_China

Even though wind turbines have a lower cost per kilowatt and higher
capacity factors, I think solar is the more interesting thing here,
because it lasts for many decades and taps a much larger resource, so
I’m going to focus on solar.

The relation between new installations and existing installations
gives us an estimate of the growth rate of solar capacity *in China*:
it’s increasing by 48/204 = 23.5% per year, giving a 3.3-year doubling
time, similar to the way new solar capacity *in the world* has doubled
every three years over the last couple of doublings; we can expect
this to remain roughly exponential for a while.  We can estimate the
current installed capacity as 204 + 48 = 252 GW, or 0.252 TW.  We can
also perhaps estimate that China’s total and electrical energy usage
each continue to grow at the same exponential rate they have been;
7.4% per year gives us the 90% increase we seem to be observing from
02010 to 02019.  We can write this model down as follows:

    installed = 0.252
    cf = 0.13                   # capacity factor
    electric_usage = 0.836
    total_usage = 6.1
    fmt = '| %5s | %7s | %7s | %8s | %8s |'
    print(fmt % ('', 'solar', 'solar', 'electric', 'total'))
    print(fmt % ('year', 'TWp', 'TW', 'TW', 'TW'))
    for i in range(40):
        print(fmt % ('%05d' % (i + 2021),
                     '%.3f' % (installed * 1.235 ** i),
                     '%.3f' % (installed * 1.235 ** i * cf),
                     '%.3f' % (electric_usage * 1.074 ** i),
                     '%.3f' % (total_usage * 1.074 ** i),
                     ))

With this model, China’s solar energy production exceeds its 02021
current electrical energy consumption of 836 GW in 02037, but doesn’t
exceed its contemporary electrical energy consumption until 02045 (at
which point we extrapolate that it will use 4.6 TWe) and finally
catches up to its total energy consumption in 02059 at 92 TW.

    |       |   solar |   solar | electric |    total |
    |  year |     TWp |      TW |       TW |       TW |
    | 02021 |   0.252 |   0.033 |    0.836 |    6.100 |
    | 02022 |   0.311 |   0.040 |    0.898 |    6.551 |
    | 02023 |   0.384 |   0.050 |    0.964 |    7.036 |
    | 02024 |   0.475 |   0.062 |    1.036 |    7.557 |
    | 02025 |   0.586 |   0.076 |    1.112 |    8.116 |
    | 02026 |   0.724 |   0.094 |    1.195 |    8.717 |
    | 02027 |   0.894 |   0.116 |    1.283 |    9.362 |
    | 02028 |   1.104 |   0.144 |    1.378 |   10.054 |
    | 02029 |   1.364 |   0.177 |    1.480 |   10.799 |
    | 02030 |   1.684 |   0.219 |    1.589 |   11.598 |
    | 02031 |   2.080 |   0.270 |    1.707 |   12.456 |
    | 02032 |   2.569 |   0.334 |    1.833 |   13.378 |
    | 02033 |   3.173 |   0.412 |    1.969 |   14.368 |
    | 02034 |   3.918 |   0.509 |    2.115 |   15.431 |
    | 02035 |   4.839 |   0.629 |    2.271 |   16.573 |
    | 02036 |   5.976 |   0.777 |    2.439 |   17.799 |
    | 02037 |   7.380 |   0.959 |    2.620 |   19.116 |
    | 02038 |   9.115 |   1.185 |    2.814 |   20.531 |
    | 02039 |  11.257 |   1.463 |    3.022 |   22.050 |
    | 02040 |  13.902 |   1.807 |    3.246 |   23.682 |
    | 02041 |  17.169 |   2.232 |    3.486 |   25.434 |
    | 02042 |  21.203 |   2.756 |    3.744 |   27.316 |
    | 02043 |  26.186 |   3.404 |    4.021 |   29.338 |
    | 02044 |  32.340 |   4.204 |    4.318 |   31.509 |
    | 02045 |  39.940 |   5.192 |    4.638 |   33.840 |
    | 02046 |  49.326 |   6.412 |    4.981 |   36.344 |
    | 02047 |  60.917 |   7.919 |    5.350 |   39.034 |
    | 02048 |  75.233 |   9.780 |    5.745 |   41.922 |
    | 02049 |  92.913 |  12.079 |    6.171 |   45.025 |
    | 02050 | 114.747 |  14.917 |    6.627 |   48.356 |
    | 02051 | 141.713 |  18.423 |    7.118 |   51.935 |
    | 02052 | 175.015 |  22.752 |    7.644 |   55.778 |
    | 02053 | 216.144 |  28.099 |    8.210 |   59.906 |
    | 02054 | 266.938 |  34.702 |    8.818 |   64.339 |
    | 02055 | 329.668 |  42.857 |    9.470 |   69.100 |
    | 02056 | 407.140 |  52.928 |   10.171 |   74.213 |
    | 02057 | 502.818 |  65.366 |   10.923 |   79.705 |
    | 02058 | 620.981 |  80.727 |   11.732 |   85.603 |
    | 02059 | 766.911 |  99.698 |   12.600 |   91.937 |
    | 02060 | 947.135 | 123.128 |   13.532 |   98.741 |

Extrapolating an exponential trend over 40 years is very likely to be
wrong, particularly when the trend has only been in effect for a few
years.  If we look back to 01993, 28 years ago, we see a
[significantly faster exponential trend][7] in *worldwide*
photovoltaic installations: 508 GW (peak, DC, nameplate capacity) in
02018, grown from maybe 130 MW in 01993, which works out to 39% growth
per year, arithmetic mean, which is a 2.1-year doubling rate.  [The
estimate for 02019] was 627 TW, though, which is only 23.4% higher
than the 02018 estimate, in line with China’s growth rate.

[7]: https://commons.wikimedia.org/wiki/File:PV_cume_semi_log_chart_2014_estimate.svg
[8]: https://en.wikipedia.org/wiki/Growth_of_photovoltaics#Countries_and_territories

If China’s photovoltaic installations were to suddenly start growing
at this faster rate, the model looks like this instead.  They’re
generating all their electrical energy from solar by 02034 instead of
02045 and all their energy from solar by 02042.  Their total
production in 02050 is 480 TW, 80 times more than their current energy
consumption, 25 times more than the current *world* marketed energy
consumption of some 18 TW, and an order of magnitude larger than their
projected energy consumption at that time.

    installed = 0.252
    cf = 0.13                   # capacity factor
    electric_usage = 0.836
    total_usage = 6.1
    ygps = 39.2                 # yearly growth percent, solar
    ygpt = 7.4                  # yearly growth percent, total
    fmt = '| %5s | %10s | %10s | %8s | %8s |'
    print(fmt % ('', 'solar', 'solar', 'electric', 'total'))
    print(fmt % ('year', 'TWp', 'TW', 'TW', 'TW'))
    for i in range(40):
        print(fmt % ('%05d' % (i + 2021),
                     '%.3f' % (installed * (1 + ygps/100) ** i),
                     '%.3f' % (installed * (1 + ygps/100) ** i * cf),
                     '%.3f' % (electric_usage * (1 + ygpt/100) ** i),
                     '%.3f' % (total_usage * (1 + ygpt/100) ** i),
                     ))

    |       |      solar |      solar | electric |    total |
    |  year |        TWp |         TW |       TW |       TW |
    | 02021 |      0.252 |      0.033 |    0.836 |    6.100 |
    | 02022 |      0.351 |      0.046 |    0.898 |    6.551 |
    | 02023 |      0.488 |      0.063 |    0.964 |    7.036 |
    | 02024 |      0.680 |      0.088 |    1.036 |    7.557 |
    | 02025 |      0.946 |      0.123 |    1.112 |    8.116 |
    | 02026 |      1.317 |      0.171 |    1.195 |    8.717 |
    | 02027 |      1.833 |      0.238 |    1.283 |    9.362 |
    | 02028 |      2.552 |      0.332 |    1.378 |   10.054 |
    | 02029 |      3.552 |      0.462 |    1.480 |   10.799 |
    | 02030 |      4.945 |      0.643 |    1.589 |   11.598 |
    | 02031 |      6.883 |      0.895 |    1.707 |   12.456 |
    | 02032 |      9.581 |      1.246 |    1.833 |   13.378 |
    | 02033 |     13.337 |      1.734 |    1.969 |   14.368 |
    | 02034 |     18.566 |      2.414 |    2.115 |   15.431 |
    | 02035 |     25.843 |      3.360 |    2.271 |   16.573 |
    | 02036 |     35.974 |      4.677 |    2.439 |   17.799 |
    | 02037 |     50.076 |      6.510 |    2.620 |   19.116 |
    | 02038 |     69.706 |      9.062 |    2.814 |   20.531 |
    | 02039 |     97.030 |     12.614 |    3.022 |   22.050 |
    | 02040 |    135.066 |     17.559 |    3.246 |   23.682 |
    | 02041 |    188.012 |     24.442 |    3.486 |   25.434 |
    | 02042 |    261.713 |     34.023 |    3.744 |   27.316 |
    | 02043 |    364.304 |     47.359 |    4.021 |   29.338 |
    | 02044 |    507.111 |     65.924 |    4.318 |   31.509 |
    | 02045 |    705.898 |     91.767 |    4.638 |   33.840 |
    | 02046 |    982.611 |    127.739 |    4.981 |   36.344 |
    | 02047 |   1367.794 |    177.813 |    5.350 |   39.034 |
    | 02048 |   1903.969 |    247.516 |    5.745 |   41.922 |
    | 02049 |   2650.325 |    344.542 |    6.171 |   45.025 |
    | 02050 |   3689.252 |    479.603 |    6.627 |   48.356 |
    | 02051 |   5135.439 |    667.607 |    7.118 |   51.935 |
    | 02052 |   7148.531 |    929.309 |    7.644 |   55.778 |
    | 02053 |   9950.756 |   1293.598 |    8.210 |   59.906 |
    | 02054 |  13851.452 |   1800.689 |    8.818 |   64.339 |
    | 02055 |  19281.221 |   2506.559 |    9.470 |   69.100 |
    | 02056 |  26839.460 |   3489.130 |   10.171 |   74.213 |
    | 02057 |  37360.528 |   4856.869 |   10.923 |   79.705 |
    | 02058 |  52005.856 |   6760.761 |   11.732 |   85.603 |
    | 02059 |  72392.151 |   9410.980 |   12.600 |   91.937 |
    | 02060 | 100769.874 |  13100.084 |   13.532 |   98.741 |

Of course no exponential curve representing a real-world phenomenon
can go on forever.  China is only 9.6 million square kilometers;
conservatively assuming a 35% “capacity factor” for its sunlight, thus
350 W/m², China only receives 3.4 petawatts of sunlight, which this
projection would have it crossing in 02056.  Covering all of China’s
territory with 21%-efficient solar panels would produce only 700 TW,
which this projection would have it crossing in 02052.  Continuing to
increase energy production past this level would require putting the
solar panels somewhere that isn’t currently China, such as on the
ocean, on the Moon, or in orbit around the Earth or the Sun.
