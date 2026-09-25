"""Gate 9: RER audit for Invalidator's published syntactic representation.

Consumes Invalidator-compatible pickle:
(label, buggy_embedding, patched_embedding, ground_truth_embedding[, ids])

Reconstructs the exact feature transformation in the released classifier:
buggy-patched and gt-patched subtraction/product plus paired cosine/euclidean
distances. Labels are never used in feature construction.
"""
from __future__ import annotations
import argparse,json,pickle
from pathlib import Path
import numpy as np

def paired_cos_dist(a,b):
 num=np.sum(a*b,axis=1); den=np.linalg.norm(a,axis=1)*np.linalg.norm(b,axis=1)
 sim=np.divide(num,den,out=np.zeros_like(num,dtype=float),where=den!=0)
 return 1.0-sim

def features(b,p,g):
 return np.hstack((b-p,b*p,paired_cos_dist(b,p)[:,None],
                   np.linalg.norm(b-p,axis=1)[:,None],
                   g-p,g*p,paired_cos_dist(g,p)[:,None],
                   np.linalg.norm(g-p,axis=1)[:,None]))

def exact_audit(X,y,ids):
 # byte-level exact equality after conversion to contiguous float64.
 groups={}
 for i,row in enumerate(np.ascontiguousarray(X,dtype=np.float64)):
  groups.setdefault(row.tobytes(),[]).append(i)
 mixed=[]
 for inds in groups.values():
  labs={int(y[i]) for i in inds}
  if len(labs)>1:
   mixed.append({"ids":[str(ids[i]) for i in inds],
                 "labels":[int(y[i]) for i in inds]})
 members={i for m in mixed for i,x in enumerate(ids) if str(x) in set(m["ids"])}
 return {"records":len(y),"feature_dimension":int(X.shape[1]),
         "exact_cells":len(groups),"mixed_exact_cells":len(mixed),
         "patches_in_mixed_exact_cells":len(members),
         "resolution_deficit_exact":len(members)/len(y) if len(y) else 0,
         "claim_resolving_exact":not mixed,
         "claim_conflict_witness_cells":mixed[:100]}

def nearest_opposite(X,y):
 # normalized Euclidean nearest opposite-label distance; descriptive robustness
 # diagnostic, NOT exact indistinguishability.
 mu=X.mean(0); sd=X.std(0); sd[sd==0]=1
 Z=(X-mu)/sd
 best=[]
 for i in range(len(y)):
  js=np.where(y!=y[i])[0]
  if len(js)==0: best.append(float("inf")); continue
  d=np.linalg.norm(Z[js]-Z[i],axis=1)
  best.append(float(d.min()))
 q=np.quantile(np.array(best)[np.isfinite(best)],[0,0.01,.05,.1,.25,.5,1]).tolist()
 return {"nearest_opposite_standardized_euclidean_quantiles":q}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("pickle")
 ap.add_argument("--out",default="artifacts/gate9_invalidator_rer.json")
 a=ap.parse_args()
 with open(a.pickle,"rb") as f: data=pickle.load(f)
 if len(data)<4: raise SystemExit("Expected (label, buggy, patched, gt[, ids])")
 y=np.asarray(data[0],dtype=int); b=np.asarray(data[1],dtype=float)
 p=np.asarray(data[2],dtype=float); g=np.asarray(data[3],dtype=float)
 ids=np.asarray(data[4],dtype=object) if len(data)>4 else np.arange(len(y))
 X=features(b,p,g)
 result={"representation":"Invalidator released syntactic feature transform",
         **exact_audit(X,y,ids),**nearest_opposite(X,y)}
 Path(a.out).parent.mkdir(exist_ok=True)
 Path(a.out).write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps(result,indent=2))
if __name__=="__main__": main()
