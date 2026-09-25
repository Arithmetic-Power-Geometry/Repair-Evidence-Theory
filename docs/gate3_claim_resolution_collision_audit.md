# Gate 3 — Claim-Resolution Collision Audit

Status: adversarial audit. No novelty claim frozen.

## Candidate object under attack

Let (mathcal R) be a declared repair universe, (E) the evidence available to an assessor, and (c:mathcal R	omathcal C) the exact claim being certified.

Let (r_1sim_E r_2) mean that the assessor's admissible evidence representation cannot distinguish the two repairs.

Evidence resolves claim (c) on (mathcal R) iff

[
r_1sim_E r_2 Rightarrow c(r_1)=c(r_2)
quadorall r_1,r_2inmathcal R.
]

A **claim-conflict witness** is a pair ((r_1,r_2)) with

[
r_1sim_E r_2,qquad c(r_1)
e c(r_2).
]

The audit asks whether this object is already standard elsewhere.

---

## Collision 1 — Selective classification / reject option

### Existing idea
A classifier may abstain on difficult or uncertain inputs, trading coverage for risk.

### Collision
Both approaches can conclude that a decision should not be issued.

### Non-equivalence
Selective classification is normally stated in terms of predictive risk/confidence under a data-generating distribution or learned score. Claim-resolution failure is structural relative to ((mathcal R,E,c)): even an oracle classifier restricted to the same evidence representation faces two indistinguishable admissible repairs with opposite claim values.

### Status
**Nearby, not an exact reduction found.**

Key experiment required later: compare model confidence/selective risk with structural resolution on the same candidate patches.

---

## Collision 2 — Conformal prediction

### Existing idea
Conformal methods produce prediction sets or abstention-like uncertainty guarantees under exchangeability assumptions.

### Collision
A multi-label prediction set can expose uncertainty about patch correctness.

### Non-equivalence
Conformal validity is distributional. Claim resolution asks whether the evidence representation itself is constant with respect to the claim on each indistinguishability class. A singleton conformal prediction does not logically imply structural resolution; structural resolution does not supply conformal coverage.

### Status
**Complementary, not identical.**

---

## Collision 3 — Epistemic uncertainty

### Existing idea
Epistemic uncertainty represents lack of knowledge/model uncertainty and can motivate abstention or evidence acquisition.

### Collision
An unresolved claim is naturally interpretable as epistemic uncertainty.

### Non-equivalence
“Epistemic uncertainty” is broader. The candidate contribution must be the *repair-specific computable witness/criterion*, not a new uncertainty category.

### Status
**Terminological/theoretical umbrella collision. Do not claim invention of epistemic uncertainty.**

---

## Collision 4 — Runtime verification monitorability

### Existing idea
Monitorability asks whether satisfaction/violation of a property can be determined from observations, often finite prefixes.

### Collision
Both concern whether observations suffice to decide a property.

### Critical distinction
Monitorability is primarily trace/property oriented: whether observations of an execution can eventually decide satisfaction. RET is repair-population oriented: whether the evidence available for a set of candidate modifications is invariant with respect to a declared repair claim.

### Threat
The mathematical skeleton is closely related: observation classes must respect a property boundary.

### Status
**Serious conceptual ancestor. RET must cite and explicitly specialize/differentiate rather than claim the logical form as new.**

---

## Collision 5 — Test adequacy and oracle problem

### Existing idea
Test adequacy criteria assess how thoroughly tests exercise software; the oracle problem concerns deciding expected outcomes. Mutation adequacy asks whether tests distinguish original/mutated behaviors.

### Collision
A test suite that cannot kill a semantically incorrect patch may be inadequate for patch validation.

### Difference worth testing
Traditional adequacy metrics (coverage, mutation score, fault detection) do not necessarily certify that *all repairs indistinguishable under the evidence agree on a declared claim*. APR creates a candidate-relative validation problem: tests can be excellent at detecting faults generally while leaving the correctness boundary crossed inside one patch-equivalence class.

### Status
**Strongest software-testing collision. Requires empirical proof that standard adequacy metrics and claim resolution diverge.**

---

## Collision 6 — Property-directed testing / distinguishing tests

### Existing idea
Generate tests specifically to expose violations of a property or distinguish candidates.

### Collision
A claim-conflict witness can guide acquisition of a distinguishing test.

### Difference
Generation is an intervention after ambiguity is recognized. Claim resolution is a precondition/diagnostic: determine whether the current evidence can support the declared certification claim.

### Status
**Operationally complementary.**

---

## Collision 7 — Assurance cases / certification

### Existing idea
Safety/security assurance cases connect claims, arguments, and evidence and explicitly ask whether evidence supports a claim.

### Collision
This is linguistically and conceptually very close to “claim/evidence compatibility.”

### Critical distinction
Assurance cases are structured argumentation frameworks. The proposed RET object is an extensional semantic criterion over a repair universe: evidence resolves a claim only when every repair that is evidence-indistinguishable has the same claim value.

### Threat
RET must not claim the general principle “evidence must support claims.” Its contribution, if any, is the executable repair-space criterion, witnesses, measures, and empirical consequences for APR/APCA.

### Status
**Major framing ancestor, but not an exact computational reduction found.**

---

# Gate 3 conclusion

The universal logical idea is **not** a new theory: observations supporting property decisions has deep ancestors in monitorability, testing, learning, diagnosis, and assurance.

The candidate research contribution survives only in a narrower operational form:

> **Repair-Claim Resolution (RCR): Given a declared candidate-repair universe, the exact evidence representation available to a repair assessor, and a declared certification claim, determine whether every evidence-indistinguishability class is homogeneous with respect to that claim; otherwise return a concrete cross-boundary witness.**

This is intentionally a computational APR problem, not a claim to have invented identifiability, uncertainty, or evidence-supported reasoning.

## Strong novelty requirement

A publishable foundational contribution now requires at least these results:

1. **Formal specialization:** define RCR precisely for APR and APCA.
2. **Non-reduction evidence:** demonstrate cases where common test adequacy/confidence metrics look strong while RCR fails.
3. **Witness algorithm:** find or approximate cross-boundary repair pairs.
4. **Claim hierarchy:** show that the same evidence may resolve one repair claim but not a stronger claim.
5. **Evidence-channel study:** quantify which evidence types refine which claim boundaries.
6. **Abstaining assessor:** use RCR to prevent unsupported correctness certification.
7. **Benchmark:** exact synthetic instances plus real APR candidate sets.
8. **Reproducibility:** deterministic artifacts and independent verification.

## Proposed claim hierarchy

Do not use one overloaded word “correct.” Candidate claims include:

[
c_1(r)=	ext{passes supplied tests}
]

[
c_2(r)=	ext{repairs reported failing behavior}
]

[
c_3(r)=	ext{preserves declared regression obligations}
]

[
c_4(r)=	ext{satisfies declared semantic specification}
]

[
c_5(r)=	ext{behaviorally equivalent to an accepted repair contract}
]

The theory should study when evidence sufficient for (c_i) is insufficient for (c_j).

## Next gate

Before software implementation, perform a focused literature/benchmark audit of:
- mutation adequacy vs patch correctness;
- patch-space/test-equivalence datasets;
- APCA confidence/calibration;
- plausible/correct patch corpora;
- test generation for overfitting patches;
- correctness labels and developer-patch ground truth.

Then construct the **smallest exact counterexample** where conventional adequacy is maximal/high but RCR for semantic correctness fails.

If such examples are trivial but unavoidable, build a parameterized family and prove the separation. If no meaningful separation exists, kill RCR.
