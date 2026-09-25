# Hard Collision Audit — Gate 2

Status: working research document. The purpose is to eliminate generic rediscoveries before theory names are frozen.

## Result of the collision audit

### 1. Model-based diagnosis
Diagnosis already reasons over sets of hypotheses/explanations consistent with observations. Multiple surviving diagnoses are not a new phenomenon.

**Consequence for RET:** residual repair multiplicity alone is not a contribution.

### 2. Exact learning / teaching dimension / active learning
These fields already study how examples or queries identify a target concept/hypothesis, including minimum distinguishing evidence.

**Consequence for RET:** “minimum evidence needed to uniquely identify a repair” is too generic to claim as a foundational novelty.

### 3. Partial identification
Partial-identification theory already treats evidence as determining an identified set rather than a unique parameter.

**Consequence for RET:** singleton-vs-set identification is not, by itself, new mathematics.

### 4. Observational equivalence / abstraction
Programming-language semantics already studies indistinguishability under observations and abstractions.

**Consequence for RET:** evidence-equivalence of repairs is a building block, not a new theorem.

### 5. Inconsistent / partial specifications
Constraint solving, diagnosis, MaxSAT-style reasoning, and specification engineering already handle inconsistent constraints and partial specifications.

**Consequence for RET:** merely allowing conflicting evidence is insufficient novelty.

### 6. Semantic / specification-based repair
Program repair can already use semantic constraints, invariants, specifications, tests, and other artifacts.

**Consequence for RET:** heterogeneous evidence is not itself new.

---

# Surviving repair-specific gap: claim/evidence resolution mismatch

Modern repair pipelines routinely produce decisions or claims such as:

- “patch is correct”;
- “patch is equivalent to the intended fix”;
- “patch preserves regression behavior”;
- “patch repairs the reported defect”;
- “patch is safe to deploy.”

But the evidence used by an assessor may only distinguish a coarser property.

This motivates a different question:

> **Does the available evidence have sufficient resolution for the exact repair claim being certified?**

This is not the same as unique program identification.

## Formal sketch

Let:
- (mathcal R) be an admissible repair universe;
- (E) be available evidence;
- (sim_E) be indistinguishability under that evidence;
- (c:mathcal R	omathcal C) be the truth value/category relevant to a declared repair claim.

Evidence (E) is **claim-resolving** for (c) over (mathcal R) iff

[
r_1sim_E r_2 Longrightarrow c(r_1)=c(r_2)
quad
orall r_1,r_2inmathcal R.
]

Equivalently, every evidence-equivalence class is homogeneous with respect to the claim.

If an evidence class contains two repairs with different claim values, then the claim is unresolved by that evidence.

## Local form

For a particular candidate (r), define its evidence class

[
[r]_E={r'inmathcal R:r'sim_E r}.
]

The claim about (r) is locally resolved iff

[
|{c(r'):r'in[r]_E}|=1.
]

This permits evidence to be sufficient for one candidate/claim while insufficient globally.

## Why this differs from unique identification

Unique identification asks whether

[
|[r]_E|=1.
]

Claim resolution only requires

[
|{c(r'):r'in[r]_E}|=1.
]

Therefore many syntactically and semantically distinct repairs may remain indistinguishable while a specific claim is still fully resolved.

Conversely, an assessor may output a highly confident binary label even when its evidence class crosses the claim boundary.

## Candidate witness of insufficiency

A compact certificate that evidence cannot resolve claim (c) is a pair

[
(r_+,r_-)
]

such that

[
r_+sim_E r_-
]

but

[
c(r_+)
e c(r_-).
]

Call this provisionally a **claim-conflict witness**. The name is not frozen.

Such a witness is stronger than saying “tests are incomplete”: it demonstrates that the exact claim being made is not invariant over repairs that the available evidence cannot distinguish.

## Candidate theorem direction

**Resolution necessity.** Any deterministic assessor restricted to evidence representation (E) cannot be universally sound for claim (c) on (mathcal R) if a claim-conflict witness exists.

This is an indistinguishability argument and must be positioned against standard classification impossibility/no-free-lunch results. The potential contribution is its repair-specific operationalization and measurement, not the logical skeleton alone.

## Research questions created by this gap

1. Which repair claims are actually resolved by standard APR test suites?
2. How often does a test-passing equivalence class cross a semantic-correctness boundary?
3. Can APCA confidence be high while claim resolution is absent?
4. Do additional artifacts (bug reports, invariants, traces, formal properties) resolve different claims at different rates?
5. Is “repairs the reported bug” easier to resolve than “semantically equivalent to intended behavior”?
6. How does the declared repair universe affect resolution?
7. Can claim-conflict witnesses be generated automatically?
8. Can an assessor abstain specifically when its evidence does not resolve its declared claim?
9. Can evidence acquisition be targeted to a claim-conflict witness rather than generic coverage?
10. Can benchmark labels themselves be shown to have insufficient evidence for some correctness claims?

## Novelty status

Promising repair-specific gap; **not yet declared novel**.

Next collision gate:
- selective classification / abstention;
- conformal prediction;
- epistemic uncertainty;
- specification adequacy;
- proof-carrying code/certification;
- runtime verification monitorability;
- property-directed testing;
- metamorphic relations;
- assurance cases.

The theory survives only if claim-resolution adds something operationally distinct from these fields.
