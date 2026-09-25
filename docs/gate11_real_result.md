# Gate 11 — Real ASE20 RER result

Source archive: PATCH-SIM_result.zip from Zenodo DOI 10.5281/zenodo.3730599.
Publisher MD5 verified locally: e3b68e17dd4be6a2bafadd6c6b30b52e.

The released archive contains 38,045 ZIP entries and 1,976 directories with
material. The RER parser uses only each patch directory's human-readable
`result` file. Its first line is the released correctness label and its next
two lines are the two released numeric-vector outputs.

## Exact-cell result

| Generator | Representation | Records | Cells | Mixed cells | Mixed members | RD |
|---|---:|---:|---:|---:|---:|---:|
| EvoSuite | full pair | 879 | 517 | 0 | 0 | 0 |
| EvoSuite | vector 1 only | 879 | 451 | 3 | 12 | 0.0136519 |
| EvoSuite | vector 2 only | 879 | 331 | 0 | 0 | 0 |
| Randoop | full pair | 883 | 644 | 0 | 0 | 0 |
| Randoop | vector 1 only | 883 | 535 | 6 | 31 | 0.0351076 |
| Randoop | vector 2 only | 883 | 480 | 0 | 0 | 0 |
| Combined, generator-aware | full pair | 1762 | 1161 | 0 | 0 | 0 |
| Combined, generator-aware | vector 1 only | 1762 | 986 | 9 | 43 | 0.0244041 |
| Combined, generator-aware | vector 2 only | 1762 | 811 | 0 | 0 | 0 |

## Interpretation

The naive hypothesis that the complete released vector representation contains
many exact opposite-label collisions is falsified on this artifact.

A stronger and more useful result appears instead: vector 1 alone is not
claim-resolving, while vector 2 alone and the full pair are claim-resolving
under exact textual equality on this observed benchmark.

Thus an additional evidence channel can eliminate concrete claim-conflict
cells. This is an empirical evidence-enrichment result, not merely a change in
predictive accuracy.

No claim is made here that exact RCR on this finite benchmark establishes
semantic correctness outside the observed patch population. CBC/corpus-transfer
testing remains necessary.

## Provenance caution

The archived `classifier.class` bytecode was inspected. Its terminal branch
contains a constant comparison involving NaN that does not obviously explain
the mixture of stored Correct/Incorrect outputs. Therefore the stored
`result` files are treated as the released ground artifact; this gate does not
claim that regenerating those labels from the bundled class file has been
validated.
