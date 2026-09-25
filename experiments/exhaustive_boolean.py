"""Exhaustive finite discovery lab for Repair Evidence Resolution.

Enumerates all Boolean functions on small finite domains, all nonempty proper
evidence subsets, and exact semantic-correctness claim boundaries.
"""
from __future__ import annotations
import csv, json
from itertools import combinations, product
from pathlib import Path
from rer.engine import Repair, evidence_classes, claim_conflict_witnesses, rcr

OUT=Path("artifacts")
OUT.mkdir(exist_ok=True)

def subsets(n):
    for k in range(1,n):
        yield from combinations(range(n),k)

rows=[]
summaries=[]
for n in range(2,5):
    funcs=[Repair("".join(map(str,bits)), tuple(bits)) for bits in product((0,1), repeat=n)]
    total_by_k={}
    resolved_by_k={}
    ccw_by_k={}
    min_evidence_hist={}
    for target in funcs:
        claim=lambda r,t=target: r.outputs==t.outputs
        min_k=None
        for E in subsets(n):
            k=len(E)
            w=claim_conflict_witnesses(funcs,E,claim)
            ok=not w
            total_by_k[k]=total_by_k.get(k,0)+1
            resolved_by_k[k]=resolved_by_k.get(k,0)+int(ok)
            ccw_by_k[k]=ccw_by_k.get(k,0)+len(w)
            rows.append({
                "n":n,"target":target.name,"evidence":";".join(map(str,E)),
                "evidence_size":k,"rcr":int(ok),"ccw_count":len(w),
                "class_count":len(evidence_classes(funcs,E))
            })
            if ok and min_k is None: min_k=k
        key=str(min_k) if min_k is not None else "unresolved_by_proper_subset"
        min_evidence_hist[key]=min_evidence_hist.get(key,0)+1
    summaries.append({
        "n":n,
        "repair_universe_size":len(funcs),
        "by_evidence_size":{
            str(k):{
                "cases":total_by_k[k],
                "resolved":resolved_by_k.get(k,0),
                "resolution_rate":resolved_by_k.get(k,0)/total_by_k[k],
                "mean_ccw_count":ccw_by_k.get(k,0)/total_by_k[k],
            } for k in sorted(total_by_k)
        },
        "minimum_evidence_histogram":min_evidence_hist,
    })

with (OUT/"exhaustive_boolean.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
(OUT/"exhaustive_boolean_summary.json").write_text(json.dumps(summaries,indent=2,sort_keys=True)+"\n")
print(json.dumps(summaries,indent=2,sort_keys=True))
