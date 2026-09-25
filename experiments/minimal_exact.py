"""Small exact RER example.

Domain indices represent inputs 0,1,2.
Evidence observes inputs 0 and 1 only.
"""
import json
from rer.engine import (
    Repair, evidence_classes, claim_conflict_witnesses, rcr,
    claim_boundary_complete, claim_resolution_profile,
)

repairs = [
    Repair("intended", (0, 1, 2)),
    Repair("latent_wrong", (0, 1, 0)),
    Repair("obvious_wrong", (0, 0, 2)),
]
E = (0, 1)

def passes_supplied_tests(r):
    return r.outputs[0] == 0 and r.outputs[1] == 1

def semantic_contract(r):
    return r.outputs == (0, 1, 2)

claims = {
    "passes_supplied_tests": passes_supplied_tests,
    "semantic_contract": semantic_contract,
}

surrogate = [repairs[0]]

result = {
    "evidence_indices": list(E),
    "classes": {
        repr(k): [r.name for r in v]
        for k, v in evidence_classes(repairs, E).items()
    },
    "claim_resolution_profile": claim_resolution_profile(repairs, E, claims),
    "semantic_witnesses": claim_conflict_witnesses(repairs, E, semantic_contract),
    "semantic_rcr": rcr(repairs, E, semantic_contract),
    "surrogate_semantic_rcr": rcr(surrogate, E, semantic_contract),
    "surrogate_cbc": claim_boundary_complete(
        repairs, surrogate, E, semantic_contract
    ),
}
print(json.dumps(result, indent=2, sort_keys=True))
