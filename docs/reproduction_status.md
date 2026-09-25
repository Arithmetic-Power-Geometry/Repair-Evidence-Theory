# Reproduction status

## What has actually been tested

The official ASE20 `PATCH-SIM_result.zip` supplied by the researcher was
verified against publisher MD5
`e3b68e17dd4be6a2bafadd6c6b30b52e`, read directly, and used to produce the
frozen Gate 11 empirical results.

The repository contains:
- the finite exact RER engine and unit tests;
- exhaustive Boolean and structured Hamming calibration experiments;
- real ASE20 parser and frozen results;
- exact CBC/subsampling analysis;
- GitHub Actions workflows for regeneration.

## Important distinction

The real ASE20 analysis has been executed against the supplied archive and its
outputs committed. A separate successful GitHub Actions execution receipt has
not yet been independently retrieved through the connected GitHub interface.
Therefore documentation must say **workflow available for reproduction**, not
**Actions reproduction independently verified**, until a run receipt/artifact
is inspected.

## One-command reproduction

With the official ZIP in the repository working directory:

```bash
bash scripts/reproduce_ase20.sh PATCH-SIM_result.zip
```

The script verifies the publisher checksum before analysis.

## Paper gate

Start manuscript drafting after engineering hardening, but freeze headline
empirical claims only after one independent APCA artifact reproduces at least
one of:
1. unresolved claim cells under a released evidence representation;
2. reduction of unresolved cells under evidence enrichment;
3. false resolution under a restricted evaluation surrogate / corpus shift.

A negative replication is also publishable evidence if reported without
post-hoc threshold changes.
