# Exhaustive Discovery Lab v0.1

The first exact lab uses the full universe of Boolean functions on a finite
(n)-point domain and the strongest claim: exact equality to a designated
target behavior.

For evidence observing (k<n) coordinates:

- there are exactly (2^k) evidence-equivalence classes;
- each class contains exactly (2^{n-k}) repairs;
- the target's evidence class therefore contains
  (2^{n-k}-1) semantically incorrect alternatives;
- semantic RCR is impossible for every proper evidence subset.

Thus the lab recovers the closed form

[
CCW(n,k)=2^{n-k}-1
]

for the target-equality claim.

## Scientific interpretation

This is a calibration theorem, **not a novelty theorem**. It verifies that the
engine behaves exactly as finite-function combinatorics predicts.

More importantly, it tells us where *not* to search for novelty: unrestricted
function universes plus exact semantic equality make RCR collapse to ordinary
complete observation.

The next discovery experiment must therefore impose **repair structure**:
local edit operators, bounded repair distance, regression obligations, and
coarser claim hierarchies. Only there can evidence resolution differ
nontrivially from simply observing every input.

## Next experiment

Construct repair universes induced by edit operators around a defective
baseline (P_0), rather than all functions. Measure:

1. minimum evidence size for each claim;
2. difference between input coverage and claim resolution;
3. claim-resolution profiles across nested claims;
4. CBC under random, mutation-generated, and boundary-seeking surrogates;
5. whether minimal resolving evidence has a combinatorial characterization.

The full-function experiment is retained as a reference/calibration regime.
