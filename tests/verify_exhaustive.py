"""Independent closed-form checks for the exhaustive Boolean lab."""
import csv, json
from pathlib import Path

p=Path("artifacts")
rows=list(csv.DictReader((p/"exhaustive_boolean.csv").open()))
summary=json.loads((p/"exhaustive_boolean_summary.json").read_text())

# With the universe of ALL Boolean functions and the claim "equals target on
# the full n-point domain", every proper evidence subset leaves at least one
# unobserved coordinate that can be flipped. Hence semantic RCR must fail.
assert rows
assert all(int(r["rcr"])==0 for r in rows)

# Observation signatures over k Boolean coordinates give exactly 2^k cells.
for r in rows:
    assert int(r["class_count"]) == 2 ** int(r["evidence_size"])

# For a fixed target and evidence of size k, its evidence cell contains
# 2^(n-k) repairs; exactly one is globally equal to the target. Therefore the
# target participates in 2^(n-k)-1 claim-conflict pairs. Other non-target
# pairs do not cross the equality-to-target claim boundary.
for r in rows:
    n=int(r["n"]); k=int(r["evidence_size"])
    assert int(r["ccw_count"]) == 2 ** (n-k) - 1

for block in summary:
    assert all(v["resolved"]==0 for v in block["by_evidence_size"].values())

print("closed-form verification passed")
