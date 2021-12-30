Apples to Apples is a popular party game; as Wikipedia previously
explained it:

> Each player is dealt seven “red apple” cards; on each is printed a
> noun or noun phrase (Madonna, Lightning, Socks, Mahatma Gandhi,
> Street Gangs, London, The Universe, A Locker Room, The San Andreas
> Fault, Science Fiction, etc.).
> 
> One player is appointed as the first “judge”. She draws a “green
> apple” card on which is printed an adjective (Scary, Smelly,
> Patriotic, Rich, Aged, etc.), and places it face-up. Each of the
> other players places (face down) one of his red apple cards which he
> feels matches the green apple card. The judge shuffles the red apple
> cards then turns them face up (without knowing who submitted each)
> and chooses the one she feels is the best match for the green apple
> card. The player who submitted that red apple card wins the round,
> and takes the green apple card to signify the win.

(by Fritzlein, Vicki Rosenzweig, Zandperl, Fsufezzik, and Brian
Kendig)

Cards Against Humanity is a Creative-Commons-licensed game along the
same lines with blacker humor.

In Scrum, there’s a “planning poker” that is sort of structured as a
game, allowing the project to be planned based on estimates of costs,
but it doesn’t provide incentives for providing good estimates;
consequently the way a selfish player would keep their job or get
promoted is to spend as little effort as possible on estimates, with
the predictable result that the estimates are terrible.  Perhaps
“Planning Apples” or “Planning Against Humanity” could provide correct
incentives, so that people who put the right amount of effort into
estimation would instead keep their job or get promoted.  How would
that work?

The first attempt is the jellybean-jar-game approach: each person’s
estimate of a task is anonymously recorded, and then when the task is
done, whoever had the closest estimate wins a point.  The estimate
used for planning is some sort of average of the estimates; perhaps
the median is the best average to use, or perhaps a median weighted by
people’s scores.

However, this creates a perverse incentive: if you get assigned a
task, you have an incentive to take the exact amount of time you
estimated.  There’s a second-order perverse incentive: you have an
incentive to pad your estimate so that you’re pretty sure that, if you
get the task, you can sandbag your work to hit the estimate.  This can
be ameliorated by disqualifying the performer’s guess if it happens to
be closest, assigning the point to the next-closest estimate, just as
the “judge” in A2A doesn’t get to play a red apple card.  Then two
different people have to collude (against the interests of the rest of
the team) to win these points.  In some social contexts that is
a sufficient control.

Perhaps the perverse incentive can be solved entirely by giving a
*bigger* prize for beating the estimate that was used for planning.
In the case where that estimate was the median, this prize should be
awarded when the actual time taken was lower than the highest estimate
that was less than the median.  So, for example, if the estimates were
2, 4, 7, 11, and 13, the median is 7, but you only win the prize if
you completed it with 4 units of work or less.

That way, if you expect to be assigned the task, and you know what the
other players’ estimates are, by choosing your estimate adversarially
you can only push the estimated time up to the next higher estimate.

In the above example, suppose the estimates on the table are 2, 4, 11,
and 13; this gives you the freedom to *set* the estimate to anything
between 4 and 11 by choosing a number in that range, or to set it to 4
or 11 by picking a number lower than 4 or higher than 11.  If the real
difficulty of the task is in the 4-11 range, you aren’t going to be
able to get the fast completion prize by picking a number in that
range, but you can win the estimation prize by doing the best job
possible at estimating the difficulty, taking the estimation prize
away from the 4 guy and the 11 guy.  If you pick a number below 4,
such as 3, you set the estimate to 4 and forfeit the estimation prize,
but you’d have to beat your own estimate of 3 to win the early
completion prize, which is unlikely.  But if you pick a number over
11, like 12, you set the estimate to 11, but the early completion
prize threshold to 4, which, again, you probably can’t beat, and again
you’re forfeiting the estimation prize.  So, even in that extreme
case, your best strategy is to estimate as honestly as you can.

If the estimates on the table are 2, 4, 7, and 11, then the same
holds, but even more strongly.  You can under some circumstances nudge
the median up to the next partition but you don’t win anything by
doing so.

How do we measure completion times?  Because of course if they’re
entirely self-reported you could claim that every task took you 0
units or 1 unit and thus win an early-completion time for every task
you complete.  If the other players judge your completion time, they
can try to push it closer to their estimate.  Perhaps we could assign
each player a fixed number of points to allocate during the iteration,
or assign them in proportion to their billable hours.  There are
additional tricky incentive-design problems there, but they may be
tractable.
