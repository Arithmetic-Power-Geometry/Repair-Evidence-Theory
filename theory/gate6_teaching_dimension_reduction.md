# Gate 6 — Teaching-Dimension Reduction and Claim-Relative Pivot

## Hard reduction

For coordinate-observation evidence and exact target identity, define

[
\rho_{\mathcal R}(r)=
\min\{|E|: E\cap\Delta(r,r')\ne\varnothing
\text{ for every }r'\ne r\}.
]

This is not a new invariant. It is the minimum teaching-set size of target
concept (r) with respect to concept class (\mathcal R): a teaching set is
a set of labeled domain points whose restriction distinguishes the target from
every other concept.

Therefore:

- do not claim exact-target repair resolution as a new combinatorial theory;
- do not claim the hitting-set formulation itself as new;
- treat the Hamming-ball result as calibration/specialization.

## Claim-relative pivot

Repair certification usually does not require identifying the exact source-level
repair. It requires deciding a declared claim.

Let

[
c:\mathcal R\to\mathcal C
]

be a repair claim, e.g. regression-safe, satisfies a semantic contract, repairs
the reported failure, or belongs to an accepted behavioral class.

For target repair (r), define the opposite-claim set

[
\mathcal O_c(r)=\{r'\in\mathcal R:c(r')\ne c(r)\}.
]

For coordinate-observation evidence, define the **claim-relative resolving
number**

[
\rho_c(r)=
\min\{|E|:
E\cap\Delta(r,r')\ne\varnothing
\quad\forall r'\in\mathcal O_c(r)\}.
]

Equivalently, (E) need only distinguish (r) from repairs on the other side
of the declared claim boundary. Repairs with the same claim value may remain
indistinguishable.

Immediately,

[
\rho_c(r)\le \rho_{\mathrm{id}}(r),
]

because the exact-identity problem must distinguish (r) from a superset of
alternatives.

## Claim-relative difference hypergraph

Define

[
\mathcal H_c(r)=
\bigl(X,\{\Delta(r,r'):c(r')\ne c(r)\}\bigr).
]

Then

[
\rho_c(r)=\tau(\mathcal H_c(r)),
]

the transversal/hitting number of the claim-relative difference hypergraph.

This equivalence is mathematically standard hitting-set structure; novelty
cannot rest on the equality alone.

## Potentially useful APR object

The new research question is not “how many examples teach this exact repair?”
but:

> What is the minimum assessor-visible evidence required to certify a declared
> repair property while allowing arbitrary indistinguishability among repairs
> that agree on that property?

This changes the target from concept identification to **property/claim
certification over a repair space**.

## Claim-resolution profile

For claims (c_1,\ldots,c_k), define

[
CRN(r)=(\rho_{c_1}(r),\ldots,\rho_{c_k}(r)).
]

This quantitative profile complements the Boolean CRP.

## Required novelty audit

Before claiming novelty, compare (\rho_c) against:

1. teaching dimension for quotient/concept classes;
2. partial concept learning and class teaching;
3. certificate complexity of Boolean functions;
4. decision-tree certificate complexity;
5. distinguishing sets for equivalence classes;
6. property testing and property certification;
7. witness/certificate complexity;
8. test-completeness relative to conformance classes.

If (\rho_c) reduces exactly to certificate complexity or quotient teaching
dimension, retain it only as imported machinery and search for the genuinely
APR-specific theorem.
