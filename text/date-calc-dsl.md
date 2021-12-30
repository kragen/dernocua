<https://github.com/mvrozanti/dte> is a DSL for doing calculations on
dates, but it doesn’t attack my biggest pain point, which is (as
described in <https://news.ycombinator.com/item?id=29136554>)
timezones.  I want to know what local time is 5 PM US Eastern or 11 AM
US Pacific, or how long it is from now until 8 PM UTC.  Occasionally I
want to know how long it is between 02021-11-15 21:55 and 02021-11-17
05:00, or convert to or from Unix timestamps, or to know how many days
it is since 01983-05-21, or until Christmas.  Occasionally I’d like to
know the tzolkin date, the phase of the moon, or the time of sunset.
Most of dte is useless to me; I *never* want to convert `23h:23` to
`23:23:00`.

Timezone selection is the hardest thing to do in a DSLish way, because
any conceivable way to do it or debug it noninteractively involves
memorizing *something* about every timezone you want to use.  You
really want some kind of interface that gives you a list of the
possibilities.
