# Repair Evidence Theory

Repair Evidence Theory studies a question that precedes patch correctness prediction:

> **When is the available software evidence sufficient to identify a repair, rather than merely accept one?**

## Research thesis

Test-based automated program repair (APR) commonly treats a test-passing patch as *plausible*, while automated patch correctness assessment (APCA) attempts to distinguish correct from overfitting patches. Existing work strengthens test suites, generates counterexamples, clusters behaviorally similar patches, predicts correctness, and uses static or LLM-based assessment.

This project studies a different level of the problem: **evidence sufficiency itself**.

Given a buggy program, a candidate repair space, and an evidence set (tests, specifications, traces, invariants, bug reports, static constraints, or combinations thereof), when does that evidence uniquely determine the behavior required of an acceptable repair? When does it leave multiple mutually incompatible repair behaviors observationally indistinguishable?

## Initial formal objects

Let:
- \(B\) be a buggy program;
- \(\mathcal{R}(B)\) be a repair space;
- \(E\) be available evidence;
- \(\operatorname{Obs}_E(r)\) be the observations that repair \(r\) induces under \(E\).

Define evidence-equivalence:
\[
r_i \equiv_E r_j
\iff
\operatorname{Obs}_E(r_i)=\operatorname{Obs}_E(r_j).
\]

The evidence partitions the repair space:
\[
\mathcal{R}(B)/{\equiv_E}.
\]

The central question is not merely whether one repair passes \(E\), but whether the evidence is strong enough to rule out incompatible behaviors.

A provisional **repair-identifiability condition** is:

\[
E \text{ identifies target behavior } \beta
\iff
\forall r\in\mathcal{R}(B),
\operatorname{Obs}_E(r)=\operatorname{Obs}_E(r^*)
\Rightarrow
\operatorname{Beh}(r)=\beta.
\]

This definition is deliberately provisional. The project will try to falsify or refine it against prior work in test equivalence, patch overfitting, APCA, counterexample-guided repair, specification inference, oracle generation, program equivalence, and active testing.

## Novelty discipline

The project does **not** claim that:
- weak tests and patch overfitting are new;
- test-equivalence classes are new;
- generated tests for patch validation are new;
- patch correctness prediction is new;
- behavioral clustering of patches is new.

The intended contribution must survive reduction to those established ideas.

## Planned research pipeline

1. Literature map and prior-art collision table.
2. Formal repair-evidence model.
3. Impossibility / identifiability results.
4. Algorithms for measuring evidence ambiguity.
5. Synthetic controlled examples with exact ground truth.
6. Experiments on established APR benchmarks.
7. Evidence interventions: tests, invariants, specifications, bug reports.
8. Reproducible CLI/software.
9. GitHub Actions workflow producing frozen CSV/JSON/plots/reports.
10. Paper and archival release.

## Repository status

**Theory-first research scaffold. No novelty claim is frozen yet.**

The repository will treat every major definition as a hypothesis until it survives both literature comparison and executable counterexamples.
