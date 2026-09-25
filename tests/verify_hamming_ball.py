"""Independent conjecture checks for Hamming-ball experiment."""
import json
from pathlib import Path
s=json.loads(Path("artifacts/hamming_ball_summary.json").read_text())

# For exact target equality in a Hamming ball around 0^n:
# conjecture discovered/checked: minimum coordinate evidence is
# n-d+1 when target is at radius d (boundary), but n when target is interior.
for b in s:
    n,d=b["n"],b["d"]
    for td,vals in b["minimum_by_target_distance"].items():
        td=int(td)
        expected = n-d+1 if td==d else n
        assert vals == [expected], (b,td,vals,expected)
print("Hamming-ball conjecture verified over enumerated range")
