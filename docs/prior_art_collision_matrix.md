# Prior-Art Collision Matrix — Gate 1

Status: working research document. No novelty claim is frozen.

| Neighboring line | What it already establishes | Collision with RET | Surviving repair-specific question |
|---|---|---|---|
| Test-suite overfitting / plausible patches | Passing the available tests does not imply semantic correctness. | Directly kills any claim that weak tests are a new observation. | Can sufficiency of the *available evidence* for a declared repair decision be characterized before accepting/classifying a patch? |
| Test-equivalence analysis | Candidate patches can be partitioned by indistinguishability under tests; useful for search reduction. | Direct collision with evidence-equivalence if RET is test-only. | Lift from search optimization to decision-relative behavioral identifiability across heterogeneous repair evidence. |
| Test-based patch clustering | Dynamic behavior can cluster plausible patches to aid assessment. | Kills novelty of behavioral grouping. | Characterize whether all surviving behaviors are decision-equivalent, rather than merely clustering them. |
| APCA | Predicts/classifies patch correctness beyond test passing using learned/static/LLM signals. | Kills novelty of automated correctness assessment. | Determine when the evidence supplied to an assessor is sufficient for its correctness decision, independent of classifier confidence. |
| Counterexample/test generation | Additional tests/counterexamples reduce overfitting and improve repair. | Kills novelty of evidence refinement by new tests. | Define stopping/sufficiency conditions for evidence acquisition under a declared repair universe and decision relation. |
| Invariant/specification validation | Semantic constraints beyond tests can reject overfitting patches. | Kills novelty of heterogeneous semantic evidence in isolation. | Formalize joint evidence channels and their residual behavioral ambiguity. |
| PBE/version spaces | Evidence/examples induce a set of consistent programs; ambiguity is fundamental. | Major collision with a universal program-evidence theory. | RET must exploit repair-specific structure: known defective baseline, admissible edit relation, regression obligations, heterogeneous/noisy evidence, and repair decision semantics. |
| Active program synthesis | Queries are chosen to distinguish candidate programs until observational equivalence. | Kills novelty of generic distinguishing-evidence acquisition. | Repair evidence may be partial, conflicting, non-queryable, and decision-relative; characterize what can/cannot be concluded from the evidence actually available. |
| Observational equivalence | Programs can be equivalent under an observation semantics. | Kills novelty of equivalence itself. | Define repair-specific decision equivalence and distinguish implementation, behavior, and decision identifiability. |
| Manual/developer-patch assessment | Developer patches are often used as practical ground truth; semantic equivalence is manually judged. | Warns against defining correctness as identity to developer patch. | Treat target as an admissible behavior class, not a unique source patch. |
| Multi-artifact APR | Bug reports and tests can be combined; modern systems add runtime/specification/context signals. | Kills novelty of simply combining evidence types. | Study whether their combination actually identifies the repair decision, and expose unresolved ambiguity/conflict. |

## Current surviving thesis

The broad statement “examples/evidence leave multiple consistent programs” is not new.

The candidate gap is narrower:

> **For a declared automated-program-repair universe and a declared repair decision, characterize whether the heterogeneous evidence actually available is sufficient to make that decision invariant across every admissible repair consistent with the evidence.**

This is deliberately **decision-relative**. It does not require one syntactically unique patch and does not assume the developer patch is the sole correct implementation.

## Novelty threats still open

1. Formal diagnosis / model-based diagnosis.
2. Version-space learning and teaching dimension.
3. Abstract interpretation and observational abstractions.
4. Epistemic logic / knowledge-based program analysis.
5. Requirements inconsistency and partial specifications.
6. Robust decision making under partial identification.
7. Semantic program repair with formal specifications.

The theory gate remains closed until these collisions are audited.
