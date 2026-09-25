# Gate 10 — Multi-Assessor Validation Matrix

## Primary-source artifact audit

RER must not depend on one APCA implementation. Gate 10 freezes three
independent published artifact families.

### Invalidator
Primary artifact: Zenodo DOI 10.5281/zenodo.7699142.
Contains source code, datasets and results. The released syntactic classifier
constructs a representation from buggy, candidate-patch and developer-fix
embeddings and uses logistic regression. Semantic evidence is supplied by
Daikon-derived invariant rules.

RER role:
- exact/near syntactic representation audit;
- semantic decision-signature audit;
- evidence-enrichment comparison;
- conventional predictive metrics versus structural diagnostics.

### ASE 2020 APCA benchmark
Primary artifact: Zenodo DOI 10.5281/zenodo.3730599.
The archive exposes patches, generated tests, Daikon output, PATCH-SIM/E-PATCH-
SIM output vectors and ML training results.

RER role:
- dynamic behavioral evidence cells from PATCH-SIM vectors;
- invariant evidence cells;
- generated-test evidence refinement;
- direct test of whether adding evidence splits cross-label cells.

### Cache
Primary artifact family: Zenodo records 4459341 / 4717349.
The released material describes 1,183 deduplicated patches in the small
benchmark and 49,694 patches in a large benchmark, with detailed per-patch
model/classifier result files and cross-dataset experiments.

RER role:
- large-scale prediction-output/confidence audit;
- corpus-shift/CBC experiment;
- compare within-corpus versus cross-corpus resolution.

## Frozen experiment matrix

| Question | Invalidator | ASE20 | Cache |
|---|---:|---:|---:|
| Exact representation CCWs | yes | yes where vector available | if representation available |
| Semantic/invariant evidence | yes | yes | no |
| Generated-test refinement | indirect | yes | no |
| Confidence vs resolution | yes | ML outputs | prediction outputs |
| CBC/corpus transfer | possible | possible | primary target |
| Cross-assessor replication | yes | yes | yes |

## Headline falsification sequence

H1. Published assessor-visible representations contain opposite-correctness
collisions or materially small opposite-label margins.

H2. Conventional predictive performance can remain favorable while structural
resolution diagnostics reveal unresolved regions.

H3. Independent evidence enrichment (invariants or generated tests) reduces
unresolved regions.

H4. Evaluation subsets can appear claim-resolving while a larger observed patch
universe is not; CBC predicts this false-resolution failure.

Any failed hypothesis is reported as a failed hypothesis. Definitions or
thresholds must not be changed after seeing labels to rescue a positive result.

## Q1 completion criterion

Do not call the paper Q1-ready until at least:
1. two independent APCA artifacts have executable RER results;
2. one evidence-enrichment experiment is complete;
3. one cross-corpus/CBC experiment is complete;
4. conventional metrics are reproduced beside RER diagnostics;
5. all central claims survive a fresh prior-art audit.
