# Formal Core v0.1 — Decision-Relative Repair Identifiability

Status: provisional; designed to be attacked.

## 1. Repair instance

A repair instance is

[
mathfrak{I}=(P_0,mathcal{R},mathcal{E},models,delta)
]

where:

- (P_0) is the known defective program;
- (mathcal{R}) is an explicitly declared admissible repair universe reachable from (P_0);
- (mathcal{E}) is a universe of evidence items/channels;
- (rmodels e) means repair (r) is consistent with evidence item (e);
- (delta:mathcal{R}	omathcal{D}) maps a repair to the decision-relevant behavior/outcome.

For available evidence (Esubseteqmathcal{E}), define the surviving repair set

[
V(E)={rinmathcal{R}:orall ein E, rmodels e}.
]

## 2. Decision image

The residual decision set is

[
D(E)={delta(r):rin V(E)}.
]

This deliberately separates source-code multiplicity from decision ambiguity.

## 3. Decision-relative repair identifiability

Evidence (E) is sufficient for decision (delta) iff

[
|D(E)|=1.
]

Equivalently,

[
orall r_1,r_2in V(E),quad delta(r_1)=delta(r_2).
]

Call this **decision-relative repair identifiability (DRRI)** provisionally.

## 4. Residual ambiguity

A simple exact finite measure is

[
A_delta(E)=|D(E)|.
]

A normalized finite measure can be

[
a_delta(E)=
egin{cases}
0,& |D(E)|=1,\
rac{log |D(E)|}{log |delta(mathcal{R})|},&	ext{otherwise.}
end{cases}
]

Entropy-based versions require an explicit probability model and must not be introduced without one.

## 5. Evidence refinement proposition

If evidence is conjunctive and soundly interpreted, then

[
E_1subseteq E_2 Rightarrow V(E_2)subseteq V(E_1).
]

Therefore

[
D(E_2)subseteq D(E_1)
]

and

[
A_delta(E_2)le A_delta(E_1).
]

Thus valid added evidence cannot increase residual decision ambiguity under this model.

## 6. Impossibility proposition

If

[
exists r_1,r_2in V(E)
quad	ext{with}quad
delta(r_1)
edelta(r_2),
]

then no deterministic assessor whose input is restricted to (E) and information common to all members of (V(E)) can be guaranteed to return the correct (delta)-decision for both possible worlds.

This is an information/indistinguishability result, not yet claimed as a novel theorem.

## 7. Repair-specific structure

RET must not reduce to generic version-space learning. Candidate repair-specific structure includes:

1. (P_0) is known and defective.
2. (mathcal{R}) is induced by admissible changes to (P_0), not an arbitrary hypothesis class.
3. Regression preservation can itself be part of evidence/decision semantics.
4. Evidence can be heterogeneous: tests, invariants, formal properties, traces, bug reports, static facts, developer constraints.
5. Evidence can be unavailable for active querying.
6. Evidence can conflict or be unreliable; the simple conjunctive model above does not yet handle this.
7. The target is a repair decision/behavior class, not necessarily a unique implementation.

## 8. Next mathematical pressure tests

- What survives when evidence is inconsistent?
- What survives when evidence is probabilistic/noisy?
- Can identifiability be local to a repair family but not global?
- How does changing the admissible repair universe change identifiability?
- Can a correctness assessor be calibrated while evidence remains non-identifying?
- What evidence additions are informative versus redundant for (delta)?
- Is there a useful certificate of non-identifiability: two surviving repairs plus a decision witness?

No theorem name is frozen.
