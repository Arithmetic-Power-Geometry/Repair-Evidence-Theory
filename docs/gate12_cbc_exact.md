# Gate 12 — Exact CBC / false-resolution experiment

Source: the same publisher-verified ASE20 `PATCH-SIM_result.zip` used for
Gate 11 (Zenodo DOI 10.5281/zenodo.3730599).

The full observed corpus contains 1,762 generator-aware records. Under the
vector-1 representation it contains nine mixed correctness cells; vector 2 and
the full pair contain none.

For a uniformly drawn subset (G) of fixed size (n), this gate computes
exactly (not by Monte Carlo) the probability that (G) contains no mixed
vector-1 cell even though the full observed parent does:

[
Pr(RCR(G)=1 mid RCR(R_{obs})=0).
]

The calculation uses a generating function over the correct/incorrect counts in
the nine observed mixed cells and a hypergeometric denominator
(inom{1762}{n}).

Key probabilities for vector 1 are:

| n | exact false-resolution probability |
|---:|---:|
| 25 | 0.9937398573 |
| 50 | 0.9758103544 |
| 100 | 0.9128898721 |
| 200 | 0.7254476392 |
| 400 | 0.3396551769 |
| 800 | 0.0243536573 |
| 1200 | 0.0002086687 |
| 1500 | 0.0000001737 |

The vector-2-only and full-pair negative controls have zero parent mixed cells,
so their parent-relative false-resolution probability is zero by construction.

Interpretation: a restricted evaluation surrogate can appear structurally
claim-resolving simply because it omits the cross-claim members of the parent
mixed cells. This is a finite observed-population demonstration of the transfer
problem formalized by claim-boundary completeness; it does not assert that the
1,762-record corpus is the complete semantic repair universe.
