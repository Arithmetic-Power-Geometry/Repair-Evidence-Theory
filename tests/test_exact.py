from rer.engine import Repair, rcr, claim_conflict_witnesses, claim_boundary_complete

U = [
    Repair("good", (0,1,2)),
    Repair("hidden_bad", (0,1,0)),
    Repair("seen_bad", (0,0,2)),
]
E=(0,1)
semantic=lambda r: r.outputs==(0,1,2)

assert rcr(U,E,semantic) is False
assert ("good","hidden_bad") in claim_conflict_witnesses(U,E,semantic)
assert claim_boundary_complete(U,[U[0]],E,semantic) is False
assert claim_boundary_complete(U,[U[0],U[1]],E,semantic) is True
assert rcr([U[0]],E,semantic) is True
print("all exact checks passed")
