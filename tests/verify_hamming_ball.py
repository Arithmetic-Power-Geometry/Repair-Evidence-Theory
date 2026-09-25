"""Independent theorem checks for the Hamming-ball experiment."""
import json
from pathlib import Path
s=json.loads(Path("artifacts/hamming_ball_summary.json").read_text())

# Exact target equality in R_d={x: wt(x)<=d}.
# Boundary targets (wt=d): observing all d edited coordinates forces all
# remaining coordinates to zero, so m=d.
# Interior targets (wt<d): every omitted coordinate can be flipped while
# remaining in the ball, so m=n.
for b in s:
    n,d=b["n"],b["d"]
    for td,vals in b["minimum_by_target_distance"].items():
        td=int(td)
        expected = d if td==d else n
        assert vals == [expected], (n,d,td,vals,expected)
print("Hamming-ball boundary/interior law verified over enumerated range")
