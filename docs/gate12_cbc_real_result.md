# Gate 12 — CBC false-resolution result on the real ASE20 artifact

Gate 12 uses the same checksum-verified ASE20 PATCH-SIM archive as Gate 11.
The full observed population contains 1,762 released result records when
EvoSuite/Randoop generator identity is retained in the evidence signature.

For vector-1 evidence, the parent population contains nine opposite-correctness
mixed cells involving 43 records. Vector 2 and the full pair contain zero
observed mixed cells and therefore serve as negative controls for this
parent-relative false-resolution experiment.

## Exact result

For a uniformly sampled subset of size n without replacement, false resolution
means that the subset contains no mixed vector-1 cell even though the parent
population does.

The probability is computed exactly by a generating function over the nine
mixed cells, not estimated from simulation.

| n | Exact P(false resolution) | 5,000-draw Monte Carlo |
|---:|---:|---:|
| 25 | 0.993740 | 0.9946 |
| 50 | 0.975810 | 0.9692 |
| 100 | 0.912890 | 0.9158 |
| 200 | 0.725448 | 0.7100 |
| 400 | 0.339655 | 0.3390 |
| 800 | 0.024354 | 0.0238 |
| 1200 | 0.000209 | 0.0004 |
| 1500 | 0.000000174 | 0 |

Thus a 100-record evaluation subset has an exact 91.289% probability of
appearing claim-resolving under vector-1 evidence although the observed parent
population is not claim-resolving.

CBC is stricter than merely detecting one mixed cell: it requires the surrogate
to preserve every parent mixed claim boundary. Monte Carlo shows CBC failure
remains common even at large sample sizes.

## Scope

This is a finite-population, parent-relative statement. The 1,762 released
records are not asserted to equal the universe of all possible repairs.
Accordingly, Gate 12 establishes empirical surrogate failure relative to the
released corpus, not universal software-correctness incompleteness.

The exact probability result is reproducible from the primary archive and
requires no learned model or post-hoc threshold.
