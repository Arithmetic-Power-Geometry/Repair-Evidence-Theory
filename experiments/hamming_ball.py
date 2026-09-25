"""Structured repair-space discovery: Boolean repairs in a Hamming ball."""
from itertools import combinations, product
import csv, json
from pathlib import Path
from rer.engine import Repair, rcr, claim_conflict_witnesses

OUT=Path("artifacts"); OUT.mkdir(exist_ok=True)

def hd(a,b): return sum(x!=y for x,y in zip(a,b))
def subsets(n):
    for k in range(n+1):
        yield from combinations(range(n),k)

rows=[]
summary=[]
for n in range(2,8):
    baseline=(0,)*n
    allf=list(product((0,1),repeat=n))
    for d in range(1,min(4,n)+1):
        universe=[Repair("".join(map(str,x)),x) for x in allf if hd(x,baseline)<=d]
        # Targets at every attainable distance from baseline.
        targets=[r for r in universe if r.outputs!=baseline]
        mins=[]
        for target in targets:
            claim=lambda r,t=target: r.outputs==t.outputs
            min_k=None
            resolving_count=0
            for E in subsets(n):
                ok=rcr(universe,E,claim)
                if ok:
                    resolving_count+=1
                    if min_k is None: min_k=len(E)
                rows.append({
                    "n":n,"d":d,"universe_size":len(universe),
                    "target":target.name,"target_distance":hd(target.outputs,baseline),
                    "evidence_size":len(E),"evidence":";".join(map(str,E)),
                    "rcr":int(ok),
                    "ccw_count":len(claim_conflict_witnesses(universe,E,claim)),
                })
            mins.append((hd(target.outputs,baseline),min_k))
        hist={}
        by_tdist={}
        for td,m in mins:
            hist[str(m)]=hist.get(str(m),0)+1
            by_tdist.setdefault(str(td),[]).append(m)
        summary.append({
            "n":n,"d":d,"universe_size":len(universe),
            "minimum_evidence_histogram":hist,
            "minimum_by_target_distance":{
                td:sorted(set(vals)) for td,vals in by_tdist.items()
            }
        })

with (OUT/"hamming_ball.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
(OUT/"hamming_ball_summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
print(json.dumps(summary,indent=2,sort_keys=True))
