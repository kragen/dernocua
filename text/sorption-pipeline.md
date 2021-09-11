Wikipedia tells me that sorption vacuum pumps cannot operate
continuously.  I think that this might be incorrect, even though a
continuously-operating sorption pump may not have been built yet.
However, initial simulation results are not promising.

Consider a very thin pipe divided into a series of stages, which I
will label A, B, and C:

    A B C A B C
    ===========

We alternately cool and heat these stages.  Initially let us suppose
that all the stages are cold.

In the first phase let us heat the A stages, desorbing their contents;
the leftmost A stage ejects half of its contents to the left, out the
tube, and half to the right, where they are sorbed by the B phase.
The other A stages eject their contents similarly, but into the C
stages to their left and the B stages to their right.

In the second phase, let us heat the B stages.  The leftmost B stage,
similarly, ejects half of its contents into the leftmost A stage,
whence they continue out the end of the pipe, and half of its contents
into the C stage to its right.  (Under some assumptions, these
proportions are less even; perhaps some gas molecules make their way
back to B from A and proceed on to C.  We will come back to that.)
The other B stages eject half their contents into the C stages to
*their* right, and the other half into the A stages to their left,
whence they continue to the following C stage to the left.  So now all
our gas is sorbed in the C stages, except for the part that escaped
out of the left side initially.

In the third phase, we cool the A stages again.  Because all the gas
in the pipe is already sorbed in the C stages, they do not sorb any
gas, except for the leftmost A stage, which sorbs gas that was
previously to the left end of the pipe.

In the fourth phase, we finally heat the C stages.  The rightmost C
stage expels half of its contents to the right end of the pipe, while
the others expel them evenly into the A stages to their left and
right.

In the fifth phase, we cool the B stages back down, which has no
effect on the gas distribution, because all of the gas is sorbed in
the A stages.

In the sixth phase, we heat the A stages again, as in the first phase.
This expels half the contents of the leftmost A stage, which it sorbed
in the third phase, into the B stage to its right, and half back out
the end of the pipe.

In the seventh phase, we cool the C stages back down, which results in
sorbing some gas from the right end of the pipe.

The eighth phase is a return to the second phase, heating the B
stages, but now with a different distribution of gases.  In
particular, half the gas sorbed from the leftmost A stage, which took
it from outside the pipe, is ejected back out the pipe, while the
other half (one quarter of the total initially sorbed) moves to the C
stage to its right.  The cycle repeats from there.

My thought is that, although gas diffuses in both directions through
the tube, it diffuses faster to the right.

In the following simulation, however, this does not work at all:

    def sim(output):
        gas = [1.0] * 20
        a = [i for i in range(1, len(gas)-1) if i % 3 == 1]
        b = [i for i in range(1, len(gas)-1) if i % 3 == 2]
        c = [i for i in range(1, len(gas)-1) if i % 3 == 0]
        temp = [0.0] * len(gas)
        temp[0] = temp[-1] = 3.0
        for t in range(1000):
            output(gas, temp)
            f = t // 5 % 6 + 1
            if f in [1, 3, 5]:
                for i in (c if f == 1 else a if f == 3 else b):
                    temp[i] = 0.0
            else:
                for i in (b if f == 2 else c if f == 4 else a):
                    temp[i] = 7.0

            deltas = [0.0] * len(gas)
            for i in range(len(temp)):
                for neighbor in [i-1, i+1]:
                    if neighbor < 0 or neighbor >= len(gas):
                        continue
                    d = temp[i] * gas[i] * 0.05
                    deltas[neighbor] += d
                    deltas[i] -= d

            for i in range(len(temp)):
                gas[i] += deltas[i]

In the simulation, the phases are applied correctly (from the second
phase, anyway) but the net gas movement is zero.