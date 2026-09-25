# Gate 8B Pilot Status

## What was verified from the upstream artifact

The released Shibboleth classifier's complete numerical input is exactly:

[
(SCS,TS,BC).
]

Its Python layer standardizes those three columns and sends them to the stored
random-forest model. The Java implementation creates `scores.csv` with
`ID,SCS,TS,BC`, invokes the classifier, and then deletes `scores.csv`.

The repository does not expose a precomputed full-corpus score table through
the paths found in our audit. Therefore **no full-corpus exact-collision result
is claimed yet**.

## Reproducible pilot subjects

The upstream repository provides two configured examples.

### Chart-21
- 1074 — CORRECT
- 1075 — INCORRECT
- 1076 — INCORRECT
- 1077 — INCORRECT

### Time-24
- 17 — CORRECT
- 18 — INCORRECT

These labels come from the upstream example input files and are used only after
feature extraction.

## RER pilot procedure

1. reproduce upstream feature extraction;
2. retain `ID,SCS,TS,BC` before upstream cleanup;
3. join labels by patch ID;
4. run `experiments/audit_shibboleth_scores.py`;
5. report exact opposite-label duplicate triples as CCWs;
6. if none occur, report that result honestly and proceed to controlled
   near-collision/margin analysis.

## Q1 rule

Two toy examples cannot establish the paper's empirical claim. They validate
the instrumentation. Q1-level evidence requires useful-scale reproduction on
the published labeled corpus or an equivalent established APCA dataset.
