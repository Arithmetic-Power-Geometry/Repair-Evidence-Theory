# Literature Map — Seed Set

This is a seed map, not the final bibliography. The paper target requires a much larger, verified bibliography.

## Patch overfitting and assessment
- Fei et al. (2025), *Patch Correctness Assessment: A Survey*, ACM TOSEM, DOI: 10.1145/3702972.
- Le-Cong et al., *Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning*.
- FURINA (2026), *A Multi-Agent Framework for Automated Patch Correctness Assessment*, ACM TOSEM, DOI: 10.1145/3811825.
- RePaCA (2026), reasoning-LLM static APCA, Neurocomputing.

## Test evidence and equivalence
- Mechtaev et al. (2018), *Test-Equivalence Analysis for Automatic Patch Generation*, ACM TOSEM, DOI: 10.1145/3241980.
- xTestCluster (2024), test-based patch clustering, Empirical Software Engineering.
- Iter-T (2026), *ITERative Test Suite Generation for Automated Program Repair*, IEEE TSE, DOI: 10.1109/TSE.2026.3671416.
- QuixBugs APR empirical study: plausible/correct/overfitting patch assessment.

## Heterogeneous evidence
- Motwani & Brun, *Better Automatic Program Repair by Using Bug Reports and Tests Together*.
- Invariant-based patch validation lines represented by Invalidator and related APCA.
- Specification-centric repair: *Specification Vibing for Automated Program Repair* (2026).

## Program synthesis collision
- Version Space Algebra / PROSE: program sets consistent with specifications/examples.
- Gulwani, *Programming by Examples*: ambiguity resolution via ranking and active interaction.
- Peleg, Shoham & Yahav (ICSE 2018), *Programming Not Only by Example*: distinguishing inputs and interactive disambiguation.
- *Active Learning for Neurosymbolic Program Synthesis* (OOPSLA 2025): hypothesis-space refinement, distinguishability, observational equivalence termination.

## Oracle problem
- Barr et al. (2015), *The Oracle Problem in Software Testing: A Survey*, IEEE TSE, DOI: 10.1109/TSE.2014.2372785.

## Ground-truth caution
- Automated patch assessment at scale: manual assessment commonly uses human-written patches and semantic-equivalence judgments; difficulty, bias, and scale are recognized problems.
- Studies of machine-generated vs developer-provided correct patches show syntactic identity to the developer patch is not required for correctness.

## Next literature expansion
Target categories:
1. formal/model-based diagnosis;
2. partial specifications;
3. teaching dimension and exact learning;
4. active testing;
5. observational equivalence;
6. abstract interpretation;
7. requirements inconsistency;
8. semantic repair;
9. probabilistic/noisy specifications;
10. LLM APR and agentic repair;
11. human repair assessment;
12. test oracle generation;
13. metamorphic testing;
14. patch diversity and equivalence;
15. repair benchmarks and ground-truth validity.
