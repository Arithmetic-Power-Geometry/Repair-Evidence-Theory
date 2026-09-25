# Repair Evidence Theory

Repair Evidence Theory studies a question that precedes patch-correctness prediction:

> **Does the evidence visible to a patch assessor actually resolve the repair claim it outputs?**

## Current framework

Given a known defective program (P_0), a declared repair population
(mathcal R(P_0)), an assessor-visible evidence representation (O_E), and a
repair claim (c), the central structural condition is

[
O_E(r_1)=O_E(r_2)Rightarrow c(r_1)=c(r_2).
]

The project uses the following working objects:

- **RER — Repair Evidence Resolution:** umbrella framework.
- **RCR — Repair-Claim Resolution:** whether every evidence cell is
  claim-homogeneous.
- **CCW — Claim-Conflict Witness:** an evidence-indistinguishable pair with
  opposite claim labels.
- **RD — Resolution Deficit:** fraction of evaluated repairs lying in mixed
  evidence cells.
- **CRP — Claim Resolution Profile:** resolution across multiple repair claims.
- **CBC — Claim-Boundary Completeness:** exact condition required for a
  resolution conclusion on an evaluated repair surrogate to transfer to a
  larger declared repair population.

The intended evaluation layers are:

[
	extbf{Prediction}ightarrow	extbf{Resolution}ightarrow	extbf{Transfer}.
]

Prediction asks how often an assessor is right. Resolution asks whether its
visible evidence can distinguish opposite repair claims. Transfer asks whether a
resolution conclusion measured on an evaluated subset survives enlargement or
change of the repair population.

## What is not claimed as new

The project does not claim novelty for:

- patch overfitting or the fact that test-passing patches can be incorrect;
- observational or test equivalence;
- exact target identification;
- teaching-set or certificate-complexity machinery;
- test generation for patch validation;
- generic benchmark representativeness;
- classifier uncertainty, calibration, or selective prediction.

Those ideas are treated as prior foundations or reductions.

## Verified ASE 2020 artifact result

The public `PATCH-SIM_result.zip` artifact associated with the ASE 2020 APCA
study was analyzed after verification against publisher MD5

`e3b68e17dd4be6a2bafadd6c6b30b52e`.

The released human-readable `result` files yield 1,762 generator-aware records.

| Representation | Mixed cells | Patches in mixed cells | Resolution Deficit |
|---|---:|---:|---:|
| Vector 1 only | 9 | 43 | 0.0244041 |
| Vector 2 only | 0 | 0 | 0 |
| Full vector pair | 0 | 0 | 0 |

Thus one released evidence channel is not exact-cell claim-resolving on the
observed corpus, while the second channel and the combined representation are.
This is interpreted as an evidence-enrichment result rather than as a claim
about classifier accuracy.

## Exact false-resolution result

For Vector 1, the full observed corpus is unresolved. Nevertheless, a uniformly
drawn subset can appear resolved because it misses one side of every mixed
claim boundary.

The exact probability that a fixed-size surrogate appears resolved is:

| Sample size | Exact probability |
|---:|---:|
| 25 | 0.9937398573 |
| 50 | 0.9758103544 |
| 100 | 0.9128898721 |
| 200 | 0.7254476392 |
| 400 | 0.3396551769 |
| 800 | 0.0243536573 |
| 1200 | 0.0002086687 |
| 1500 | 0.0000001737 |

This is a finite observed-population demonstration of the transfer problem
formalized by CBC. It does not assert that the 1,762-record corpus is the full
semantic repair universe.

## Software and reproduction

The repository contains:

- finite exact RER engine;
- brute-force calibration tests;
- structured repair-space experiments;
- real ASE 2020 artifact parser;
- exact CBC/false-resolution calculation;
- regression tests for frozen empirical claims;
- GitHub Actions workflows;
- one-command reproduction script.

With the official ASE 2020 ZIP available locally:

```bash
bash scripts/reproduce_ase20.sh PATCH-SIM_result.zip
```

The script verifies the publisher checksum before analysis.

The real ASE 2020 analysis has been executed against the verified primary
archive and its outputs frozen in the repository. Workflow definitions are
available for reproduction; documentation does not claim an independently
inspected GitHub Actions run receipt where one has not been verified.

## Manuscript positioning

The current manuscript is organized around the distinction

[
oxed{	ext{prediction performance}
eq	ext{evidence resolution}}
]

and the transfer question

[
oxed{	ext{resolution on an evaluated surrogate need not transfer to a larger repair population}.}
]

The empirical claims are intentionally narrower than the general framework.
Independent replication on additional APCA systems remains an important next
validation step.
