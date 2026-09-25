# Repair Evidence Theory

A theoretical and empirical framework for determining when available software evidence is sufficient to identify, distinguish, and assess program repairs beyond test-suite plausibility.

## Repair Evidence Resolution

Repair Evidence Resolution (RER) studies a structural question that precedes patch-correctness prediction:

> **Does the evidence visible to a patch assessor actually resolve the repair claim it outputs?**

For a declared repair population, an assessor-visible evidence representation, and a repair claim, RER asks whether repairs that are indistinguishable under the available evidence always receive the same claim.

The framework provides:

- **RCR — Repair-Claim Resolution:** whether every evidence cell is claim-homogeneous.
- **CCW — Claim-Conflict Witness:** a pair with identical visible evidence and opposite claim labels.
- **RD — Resolution Deficit:** the fraction of evaluated repairs lying in mixed evidence cells.
- **CRP — Claim-Resolution Profile:** resolution across multiple repair claims.
- **CBC — Claim-Boundary Completeness:** the boundary-preservation condition used to transfer an exact resolution conclusion from an evaluated surrogate to a larger declared repair population.

The evaluation view is:

**Prediction → Resolution → Transfer**

Prediction asks how often an assessor is right. Resolution asks whether its visible evidence can separate opposite repair claims. Transfer asks whether that structural conclusion survives beyond the evaluated surrogate.

## Scope

RER does not claim novelty for observational equivalence, feature collisions, teaching dimension, certificate complexity, test completeness, classifier uncertainty, or generic benchmark representativeness. These are treated as established foundations or reductions where applicable.

Exact RER is claim-relative and population-relative. An absence of exact claim-conflict witnesses on a finite observed corpus is not interpreted as proof of semantic correctness or universal evidence sufficiency.

## Empirical audit

The current reproducible study uses the public ASE 2020 APCA artifact. The primary `PATCH-SIM_result.zip` archive is checked against publisher MD5:

`e3b68e17dd4be6a2bafadd6c6b30b52e`

The released result files provide 1,762 generator-aware records.

| Representation | Mixed cells | Patches in mixed cells | Resolution Deficit |
|---|---:|---:|---:|
| Vector 1 only | 9 | 43 | 0.0244 |
| Vector 2 only | 0 | 0 | 0 |
| Full vector pair | 0 | 0 | 0 |

Under Vector 1, a uniformly drawn fixed-size subset of 100 records has exact false-resolution probability **0.912890**, although the 1,762-record observed parent corpus is unresolved. These results are finite observed-population statements and do not treat the corpus as the complete semantic repair universe.

## Software and reproducibility

The repository contains deterministic software for exact finite RER audits, claim-conflict witnesses, resolution-deficit calculations, CBC/false-resolution analysis, calibration tests, empirical artifact parsing, regression tests, reproducibility scripts, workflow definitions, and frozen result artifacts.

With the official ASE 2020 archive available locally:

```bash
bash scripts/reproduce_ase20.sh PATCH-SIM_result.zip
```

The reproduction script verifies the publisher checksum before analysis.

## Citation

Akhtar, M. A. K. (2026). *Repair Evidence Resolution: Separating Prediction, Structural Resolution, and Transfer in Automated Patch Correctness Assessment* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22961349

Citation metadata are also provided in `CITATION.cff`.

## License

Apache License 2.0. See `LICENSE`.

Copyright © 2026 Mohammad Amir Khusru Akhtar
