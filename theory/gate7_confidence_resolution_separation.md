# Gate 7 — Confidence–Resolution Separation

## Question

Can an automated patch correctness assessor be statistically excellent and highly
confident while its assessor-visible representation is structurally incapable of
resolving the declared correctness claim?

## Setup

Let:
- (mathcal R) be a repair population;
- (c:mathcal R	o{0,1}) be the declared correctness claim;
- (Z:mathcal R	omathcal Z) be exactly the representation/evidence visible to an assessor;
- (h:mathcal Z	o{0,1}) be a deterministic classifier;
- (s:mathcal Z	o[0,1]) be its confidence score.

A representation cell is

[
C_z={r:Z(r)=z}.
]

It is **claim-pure** iff (c) is constant on (C_z), otherwise **claim-mixed**.

Structural resolution requires every relevant cell to be claim-pure.

---

## Proposition 1 — Confidence does not imply resolution

For every confidence threshold (alpha<1), there exists a repair population,
representation, classifier, and confidence score such that:

1. every accepted prediction has confidence (>alpha);
2. empirical classification accuracy is arbitrarily close to (1);
3. the representation is not claim-resolving.

### Construction

Choose one representation cell (C_z) containing (N) repairs:
- (N-1) have (c=1);
- one has (c=0).

Let (h(z)=1), and assign confidence (s(z)=1-arepsilon), where
(1-arepsilon>alpha).

Accuracy on the cell is

[
1-rac1N,
]

which tends to (1) as (N	oinfty), while the cell remains claim-mixed for
every finite (Nge2).

Therefore arbitrarily high accuracy and arbitrarily high declared confidence
do not imply structural claim resolution.

### Novelty warning

As abstract classification mathematics, this is not novel: feature collisions,
Bayes error, sufficient representations, and irreducible ambiguity already
cover the underlying phenomenon. The APR contribution must be an operational
measurement of these mixed cells under real patch-assessment evidence.

---

## Proposition 2 — Confidence-only abstention cannot repair an invisible collision

Suppose two repairs (r_+,r_-) satisfy

[
Z(r_+)=Z(r_-)=z,qquad c(r_+)
e c(r_-).
]

Any deterministic selector/rejector (g) that is a function only of (Z)
must make the same accept/reject decision for both repairs.

Thus it cannot selectively accept one and reject the other.

If it accepts (z), at least one opposite-label member of the cell is exposed
to possible classification error. If it rejects (z), it rejects the entire
cell, including any correctly classifiable members.

This is a representation-level limitation, not a threshold-selection problem.

### Relation to selective classification

Selective classification trades coverage for risk using a confidence/rejection
function. RER asks a prior structural question: does the representation itself
separate the declared claim? Selective rejection can avoid acting on an
unresolved cell only by rejecting the cell as a whole; it cannot recover
information absent from (Z).

---

## Proposition 3 — Cell impurity lower-bounds unavoidable deterministic error

For a finite cell (C_z), let

[
n_0(z)=|{rin C_z:c(r)=0}|,qquad
n_1(z)=|{rin C_z:c(r)=1}|.
]

Any deterministic classifier based only on (Z) makes at least

[
min(n_0(z),n_1(z))
]

errors on that cell under uniform counting over its members.

The optimal cellwise deterministic error rate is

[
e^*(z)=rac{min(n_0(z),n_1(z))}{|C_z|}.
]

A cell may therefore be structurally unresolved while (e^*(z)) is
arbitrarily small.

This formalizes why high accuracy can hide unresolved claim boundaries.

---

## Resolution Deficit

For empirical finite populations define the provisional **resolution deficit**

[
RD(Z,c)=
rac{|{rinmathcal R:C_{Z(r)}	ext{ is claim-mixed}}|}{|mathcal R|}.
]

This is the fraction of evaluated repairs lying in representation cells that
cross the declared claim boundary.

A stricter cell-count version is

[
RD_{cell}(Z,c)=
rac{|{z:C_z	ext{ is claim-mixed}}|}
{|{z:C_z
earnothing}|}.
]

These are descriptive empirical measures, not yet claimed novel.

---

## Critical interpretation

Accuracy asks:

> How often did the assessor predict the benchmark label correctly?

Calibration asks:

> Among predictions assigned probability (p), how often is the event true?

Selective prediction asks:

> Which predictions should be withheld to improve risk at a chosen coverage?

Structural resolution asks:

> Does the assessor-visible representation itself merge repairs that require
> opposite answers to the declared claim?

These questions are related but not equivalent.

---

## Q1 gate

The abstract propositions above are too elementary to constitute a Q1-level
theoretical contribution alone.

A strong software-engineering paper requires evidence that the distinction is
material in APR/APCA:

1. reconstruct assessor-visible representations for established APCA methods;
2. detect exact or controlled near-collisions between correct and incorrect
   patches;
3. compare RD/RCR against accuracy, F1, AUC, confidence/calibration and
   risk-coverage;
4. show cases where conventional metrics are favorable but resolution is poor;
5. enrich evidence and demonstrate that claim-conflict cells split;
6. test transfer across APR tools and benchmarks;
7. evaluate whether CBC predicts failures under patch-corpus shift.

If those empirical separations are strong and reproducible, RER becomes a
credible Q1-level contribution package. Without them, it remains an interesting
framework rather than a Q1-ready paper.
