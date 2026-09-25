# Gate 9 — Invalidator Representation Audit

## Why this target

Invalidator (IEEE TSE 2023) releases a replication package containing patch
metadata, semantic invariants, CodeBERT/BERT/ODS processed representations,
trained models and experiment scripts. This avoids making Shibboleth feature
reproduction the only route to a real APCA representation audit.

## Exact released syntactic transformation

The released classifier constructs, for buggy embedding (b), candidate-patch
embedding (p), and developer-fix embedding (g):

[
Z_I(p)=
[b-p, b\odot p, d_{cos}(b,p), d_2(b,p), g-p, g\odot p, d_{cos}(g,p), d_2(g,p)].
]

It then trains logistic regression on this representation.

This is therefore the correct object for the first Invalidator RER audit, not
raw CodeBERT vectors alone.

## Gate-9 experiment

1. load the released processed evaluation pickle;
2. reconstruct (Z_I) exactly;
3. form exact representation cells without labels;
4. attach labels only after cells exist;
5. enumerate exact opposite-label cells (CCWs);
6. compute exact RCR and Resolution Deficit;
7. separately compute nearest opposite-label distances after standardization;
8. never call near-neighbors exact CCWs;
9. reproduce Invalidator predictive metrics using its released model/scripts;
10. compare predictive performance with structural and margin diagnostics.

## Two-channel extension

Invalidator also releases semantic invariant artifacts. After the syntactic
audit, construct a semantic evidence signature from the invariant decision
rules and evaluate:

- syntactic resolution;
- semantic resolution;
- combined resolution.

This gives RER a direct evidence-enrichment experiment on an established APCA
system.

## Falsification

If the syntactic representation has no exact cross-label collisions and strong
opposite-label margins, then the strongest exact-RCR claim is not supported for
that representation. We will report that result rather than redefine
indistinguishability post hoc.

If semantic evidence resolves conflicts left by syntactic evidence, that is
direct evidence for claim-relative evidence enrichment.

## Q1 gate

Gate 9 becomes Q1-strength only after the released processed data are executed
and the results reproduce at useful scale. Protocol/code alone do not satisfy
the empirical gate.
