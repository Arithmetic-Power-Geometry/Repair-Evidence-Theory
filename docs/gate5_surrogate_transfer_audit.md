# Gate 5 — Surrogate Transfer and Prior-Art Reduction Audit

Status: theory-survival audit before implementation. No novelty claim frozen.

## Candidate under audit

For target repair universe (mathcal R), evaluated surrogate (Gsubseteqmathcal R), evidence relation (sim_E), and declared claim (c), define claim-boundary completeness (CBC):

[
orall Cinmathcal R/{sim_E},quad
|c(C)|>1 Rightarrow |c(Ccap G)|>1.
]

CBC says that whenever an evidence-indistinguishability class crosses the declared claim boundary in the target universe, the evaluated surrogate exposes that crossing.

Under CBC, resolution measured on (G) transfers exactly to (mathcal R).

---

# Collision A — Mutation testing: coupling, subsumption, representativeness

## Established territory

Mutation testing intentionally uses a generated mutant set as a surrogate for real faults. Its justification has long relied on ideas such as the competent-programmer hypothesis and coupling effect. Subsuming-mutant work reduces redundant mutants while preserving test requirements.

## Exact collision

CBC also asks whether a generated surrogate preserves distinctions relevant to an evaluation conclusion.

## Difference

Mutation coupling is primarily a fault-detection surrogate claim:

[
	ext{tests killing simple mutants} leadsto 	ext{ability to expose more complex/real faults}.
]

CBC is conditional on an explicit evidence partition and an explicit certification claim:

[
CinPi_E,quad c:C	omathcal C.
]

It asks whether the surrogate preserves **cross-claim variation inside evidence-indistinguishable cells**, not whether mutant killing predicts fault detection generally.

## Verdict

**Strong conceptual ancestor, no exact reduction established.**

Do not claim “surrogate representativeness” as new. The candidate novelty is the boundary-preservation condition for repair certification.

---

# Collision B — PAC/VC/statistical generalization

## Established territory

Statistical learning theory characterizes when performance on sampled data generalizes to a population under assumptions on sampling, hypothesis complexity, distributions, etc.

## Exact collision

Both ask when a conclusion on (G) transfers to a larger universe.

## Difference

CBC is deterministic and worst-case. A single omitted cross-boundary repair invalidates exact transfer:

[
RCR(G,E,c)=1,quad RCR(mathcal R,E,c)=0.
]

PAC-style generalization permits bounded error probability and depends on a distribution. CBC as currently defined uses no probability distribution.

## Important consequence

There should be two theory layers:

### Exact layer
Worst-case structural resolution and exact CBC.

### Statistical layer
Approximate/probabilistic claim resolution when exhaustive repair-universe enumeration is impossible.

Do not confuse the two.

## Verdict

**Not equivalent; statistical learning is a natural extension and comparison baseline.**

---

# Collision C — Benchmark representativeness / external validity

## Established territory

Software-engineering research has extensive literature on benchmark bias, dataset representativeness, external validity, and benchmark construction.

APR/APCA benchmarks are also known to contain practical ground-truth limitations: developer patches are useful references but not necessarily unique correct implementations, and manual semantic assessment is costly.

## Exact collision

CBC is a formal representativeness requirement.

## Difference

Generic representativeness asks whether a benchmark reflects a target population across relevant characteristics. CBC identifies a specific necessary-and-sufficient structural feature for **one transfer statement**:

[
RCR(G,E,c)Rightarrow RCR(mathcal R,E,c).
]

It does not claim to solve general benchmark representativeness.

## Verdict

**CBC can be framed as a repair-claim-specific external-validity condition, not a new general theory of benchmarks.**

---

# Collision D — Test completeness / specification completeness

## Established territory

Testing theory has completeness notions: under stated assumptions/fault domains, a test suite may distinguish conforming from nonconforming implementations. Conformance testing and mutation adequacy can be complete relative to explicit fault models.

## Exact collision

This is the closest mathematical ancestor.

A complete test suite relative to an implementation/fault domain and specification can be viewed as ensuring that incorrect implementations are distinguished from correct ones.

## Reduction pressure

If:
- the evidence is exactly test outcomes,
- (c) is binary conformance to a complete specification,
- (mathcal R) is the implementation/fault domain,
- (G) is used only as a test-generation surrogate,

then RCR/CBC can reduce substantially to established relative test-completeness ideas.

## Surviving scope

RET/RCR must therefore not be presented as a replacement for conformance-test completeness.

The potentially new APR-specific setting is broader:
1. (E) may combine tests, bug reports, invariants, traces, static features, learned representations, and specifications;
2. (c) may be weaker/stronger than full conformance;
3. the assessor may be APCA/LLM-based rather than a conformance checker;
4. the evaluated patch corpus (G) is itself used to validate the assessor;
5. multiple nested claims can be tested against the same evidence;
6. ground-truth claim labels may be partial or independently adjudicated;
7. the theory explicitly separates evidence resolution from assessor accuracy/confidence.

## Verdict

**Major ancestor. Exact test-only/full-specification cases are not novel and must be stated as special cases.**

---

# Gate 5 synthesis

The broadest formulations have now been reduced to existing theory.

The surviving research program is narrower and stronger:

## Repair Evidence Resolution (RER)

Given:
- a known defective baseline (P_0);
- an admissible repair universe (mathcal R(P_0));
- an assessor-visible heterogeneous evidence map (O_E);
- a declared repair claim (c);
- and, when empirical evaluation is used, an evaluated candidate surrogate (Gsubseteqmathcal R);

study whether the evidence available to the repair assessor has enough resolution to support the declared claim, and whether an empirical conclusion measured on (G) transfers to the target repair universe.

### Core structural criterion

[
O_E(r_1)=O_E(r_2)Rightarrow c(r_1)=c(r_2).
]

### Failure certificate

[
O_E(r_+)=O_E(r_-),qquad c(r_+)
e c(r_-).
]

### Surrogate-transfer condition

[
orall CinPi_E,quad
|c(C)|>1Rightarrow |c(Ccap G)|>1.
]

---

# What is genuinely worth building now

Theoretical novelty should NOT rest on the elementary partition theorem. Instead the contribution package should be:

1. **APR-specific formalization** of evidence resolution for heterogeneous assessor-visible evidence.
2. **Claim hierarchy** demonstrating that evidence adequacy changes with the certification claim.
3. **Concrete conflict witnesses** that prove a particular certification is unsupported by the available evidence.
4. **Surrogate-transfer analysis** exposing when APCA conclusions on patch corpora do/do not transfer.
5. **Exact + statistical layers** for finite-enumerable and large repair spaces.
6. **Empirical separation** from coverage, mutation score, classifier confidence, and ordinary APCA accuracy.
7. **An abstaining repair assessor** that refuses a claim when structural evidence resolution fails.
8. **Reproducible benchmark/artifact** with exact ground truth.

---

# Theory freeze recommendation

Freeze the following working vocabulary for implementation, but keep names revisable until the final literature audit:

- **Repair Evidence Resolution (RER)** — umbrella framework.
- **Repair-Claim Resolution (RCR)** — claim-specific structural condition.
- **Claim-Conflict Witness (CCW)** — indistinguishable pair crossing the claim boundary.
- **Claim-Boundary Completeness (CBC)** — exact surrogate-transfer condition.
- **Claim Resolution Profile (CRP)** — vector of resolution results across a hierarchy of repair claims.

Candidate profile:

[
CRP(E,mathcal R) =
(RCR_{c_1},RCR_{c_2},ldots,RCR_{c_k}).
]

This profile is promising because it avoids a single overloaded notion of “adequate evidence.”

---

# Implementation Gate — approved with restrictions

Software implementation is now scientifically justified **as a falsification instrument**, not as proof of novelty.

The first implementation must:
1. enumerate a finite repair universe exactly;
2. compute evidence signatures;
3. partition repairs by evidence;
4. attach independently defined claim labels;
5. emit every CCW;
6. compute RCR per claim;
7. test CBC for chosen surrogates;
8. emit a CRP;
9. include brute-force cross-checks;
10. be deterministic.

Do not begin with Defects4J or LLMs. First prove the implementation on a tiny exact universe where every result can be independently enumerated.

Only after the exact engine passes should real APR datasets be added.
