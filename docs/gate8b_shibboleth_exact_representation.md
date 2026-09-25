# Gate 8B — Exact Shibboleth Representation Audit

## Recovered assessor-visible representation

Inspection of the released Shibboleth implementation shows that its classifier
writes exactly three patch scores to `scores.csv`:

[
Z_{Shib}(r)=(SCS(r),TS(r),BC(r)).
]

The Python classifier removes the patch ID, standardizes these three columns,
and passes the resulting vectors to a stored random-forest model.

From the implementation:

- **TS**: token/syntactic similarity score produced by token analysis.
- **SCS**: average cosine similarity between before/after patch instruction
  vectors across tests.
- **BC**: change in covered branch count after patching versus before patching.

Therefore the exact released Shibboleth decision is a function only of this
three-dimensional representation.

## RER consequence

If two patches satisfy

[
(SCS,TS,BC)(r_+)=(SCS,TS,BC)(r_-)
]

but have opposite correctness labels, then no deterministic classifier using
only the released Shibboleth representation can distinguish them.

This is a genuine representation-level claim-conflict witness.

For floating-point features, exact equality is only the strictest case. A
second analysis should quantify near-collisions under controlled tolerances,
but near-collision claims must be tied to model behavior/robustness rather than
treated as exact indistinguishability.

## Required experiment

For every patch in the released evaluation corpus for which the three scores
can be reproduced:

1. extract raw ((SCS,TS,BC));
2. preserve the exact floating-point values;
3. attach correctness labels only after feature extraction;
4. group exact duplicate triples;
5. report opposite-label exact collisions;
6. compute RCR/RD on exact triples;
7. run the released classifier and reproduce accuracy/F1;
8. obtain probabilities from the stored RF model where supported;
9. compare confidence with structural collision status;
10. perform tolerance sweeps only as a separate robustness analysis.

## Strong falsification criterion

If all opposite-label patches have distinct feature triples and the model's
local neighborhoods separate labels robustly, then the strongest
confidence-resolution story weakens substantially.

If opposite-label exact collisions exist, they are direct CCWs.

If only near-collisions exist, the result becomes a robustness/margin question
and must not be overstated as exact non-resolution.

## Scientific status

This is the first Gate-8 target using an **actual published APCA representation**,
rather than metadata proxies.

The framework is still not declared Q1-ready until the feature vectors are
reproduced at useful scale and compared with published predictive metrics.
