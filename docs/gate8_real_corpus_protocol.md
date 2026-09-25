# Gate 8 — Real APR Corpus Protocol

## Corpus

Primary corpus: the public Shibboleth patch-correctness dataset, which aggregates
labeled Defects4J patches and records bug identity, correctness label, patch
location, patched method (where available), Ochiai suspiciousness, APR-tool
provenance and source-dataset provenance.

Ground-truth labels are used only *after* evidence cells are constructed.

## Leakage rule

The first RER audit excludes:
- correctness label;
- directory/path components encoding correct/incorrect;
- source-dataset provenance;
- APR-tool identity.

Tool identity is excluded because human/reference patches can be marked N/A,
making it a potential label shortcut.

## Evidence signatures

We test progressively richer label-blind representations:

1. bug identity;
2. bug + patched location;
3. bug + patched method;
4. bug + patched location + binned Ochiai suspiciousness.

For each representation (Z), patches are grouped into exact cells

[
C_z=\{r:Z(r)=z\}.
]

A cell is mixed when it contains both CORRECT and INCORRECT labels.

## Outputs

For each representation:
- number of cells;
- mixed-cell count/rate;
- number and fraction of patches in mixed cells (resolution deficit);
- finite-population cellwise unavoidable deterministic error lower bound;
- example claim-conflict cells.

## Interpretation limit

This first experiment does **not** claim that metadata is the complete evidence
used by Shibboleth or another APCA model. It asks a narrower reproducible
question: whether commonly available APR metadata already exhibits
cross-correctness evidence collisions.

A Q1-strength result requires subsequent audits of actual APCA feature vectors,
embeddings or dynamic-test signatures.

## Planned validation ladder

A. Metadata collision audit (this gate).
B. Static-feature representation from an established APCA replication package.
C. Generated-test signatures using the RGT corpus.
D. Learned embedding collisions/near-collisions with controlled thresholds.
E. Compare accuracy/AUC/calibration/risk-coverage with RER metrics.
F. Cross-corpus/CBC transfer.
