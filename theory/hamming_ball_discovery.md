# Structured Repair Discovery — Hamming-Ball Regime

## Setup

Let the defective baseline be (0^n). Define the admissible repair universe

[
mathcal R_d={xin{0,1}^n:operatorname{wt}(x)le d}.
]

Evidence observes selected coordinates (Esubseteq[n]). The strongest claim for
a target repair (tinmathcal R_d) is exact target identity:

[
c_t(r)=1iff r=t.
]

The exhaustive laboratory enumerates (n=2,ldots,7) and
(d=1,ldots,min(4,n)).

## Discovered pattern

Let (q=operatorname{wt}(t)), the target's edit distance from the baseline.

The enumeration gives:

[
m(t;mathcal R_d)=
\begin{cases}
n-d+1,&q=d,\\
n,&q<d,
\end{cases}
]

where (m) is the minimum number of coordinate observations required to
resolve exact target identity.

This is a striking boundary/interior asymmetry.

## Proof

### Interior target: (q<d)

Take any unobserved coordinate (j).

- If (t_j=1), flipping it to 0 produces another repair in (mathcal R_d).
- If (t_j=0), flipping it to 1 increases weight from (q) to (q+1le d), so
  the result also remains in (mathcal R_d).

Thus every omitted coordinate admits an alternative repair agreeing on all
observed coordinates. Therefore all (n) coordinates are necessary.
Observing all (n) is sufficient, hence (m=n).

### Boundary target: (q=d)

All (d) edited/1 coordinates must be observed: omitting any one allows that
1 to be flipped to 0 while remaining in the ball.

Once all (d) edited coordinates are fixed to 1, any repair consistent with
them already has weight at least (d). Because the repair universe permits
weight at most (d), every remaining coordinate is forced to 0.

Therefore observing the (d) edited coordinates is sufficient.

However the exhaustive experiment reports (n-d+1) only under arbitrary
coordinate-set search if a complementary characterization is used; this
creates a contradiction when (d\ne n-d+1).

## Audit correction

The direct proof above shows that the true minimum for a boundary target is
(d), not (n-d+1). Therefore any computational result asserting
(n-d+1) indicates a mistaken conjecture/check, not a theorem.

**Action:** do not freeze the conjecture. Correct the verifier and rerun the
workflow. This document intentionally records the adversarial proof audit.

## Correct candidate law

[
oxed{
m(t;mathcal R_d)=
\begin{cases}
d,&operatorname{wt}(t)=d,\\
n,&operatorname{wt}(t)<d.
\end{cases}}
]

This law is elementary combinatorics and is not claimed novel. Its importance
for RER is conceptual: repair-space geometry can make a boundary repair
identifiable from far less evidence than an interior repair.

The next question is whether a general structural invariant captures this
phenomenon for arbitrary finite repair spaces.
