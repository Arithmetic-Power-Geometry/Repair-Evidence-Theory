#!/usr/bin/env python3
"""Gate 12: exact and Monte-Carlo false-resolution audit on ASE20 vector-1 evidence."""
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict
from math import comb
import argparse,csv,json,random

def load(zpath):
    out=[]
    with ZipFile(zpath) as z:
        for name in z.namelist():
            p=name.split("/")
            if len(p)>=4 and p[-1]=="result" and p[-3] in ("Evosuite","Randoop"):
                lines=z.read(name).decode("utf-8",errors="replace").splitlines()
                if len(lines)>=3 and lines[0].strip() in ("Correct","Incorrect"):
                    out.append(dict(generator=p[-3],patch=p[-2],label=lines[0].strip(),
                                    v1=lines[1].strip(),v2=lines[2].strip()))
    return out

def signature(r,rep):
    if rep=="v1": return (r["generator"],r["v1"])
    if rep=="v2": return (r["generator"],r["v2"])
    return (r["generator"],r["v1"],r["v2"])

def cells(rows,rep):
    d=defaultdict(list)
    for i,r in enumerate(rows): d[signature(r,rep)].append(i)
    return d

def mixed(rows,rep):
    return {s:ix for s,ix in cells(rows,rep).items()
            if len({rows[i]["label"] for i in ix})>1}

def exact_false_resolution(rows,rep,n):
    mc=mixed(rows,rep)
    if not mc: return 0.0
    used=set()
    poly=[1]
    for ix in mc.values():
        labs=[rows[i]["label"] for i in ix]
        a=sum(x=="Correct" for x in labs); b=sum(x=="Incorrect" for x in labs)
        used.update(ix)
        q=[1]+[(comb(a,k) if k<=a else 0)+(comb(b,k) if k<=b else 0)
               for k in range(1,max(a,b)+1)]
        new=[0]*(len(poly)+len(q)-1)
        for i,x in enumerate(poly):
            for j,y in enumerate(q): new[i+j]+=x*y
        poly=new
    other=len(rows)-len(used)
    fav=sum(c*comb(other,n-k) for k,c in enumerate(poly)
            if 0<=n-k<=other)
    return fav/comb(len(rows),n)

def monte(rows,rep,n,trials,seed):
    rng=random.Random(seed+n)
    parent=mixed(rows,rep)
    fr=cbc=0
    for _ in range(trials):
        sub=[rows[i] for i in rng.sample(range(len(rows)),n)]
        sm=mixed(sub,rep)
        if not sm and parent: fr+=1
        if parent and not all(s in sm for s in parent): cbc+=1
    return fr/trials,cbc/trials

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("--outdir",default="artifacts")
    ap.add_argument("--trials",type=int,default=5000)
    ap.add_argument("--seed",type=int,default=20260925)
    a=ap.parse_args()
    rows=load(a.zip)
    sizes=[25,50,100,200,400,800,1200,1500]
    out=[]
    for rep in ("v1","v2","full"):
        pm=len(mixed(rows,rep))
        for n in sizes:
            if n>len(rows): continue
            mcfr,cbc=monte(rows,rep,n,a.trials,a.seed)
            out.append(dict(representation=rep,parent_records=len(rows),
              parent_mixed_cells=pm,sample_size=n,trials=a.trials,
              exact_false_resolution_probability=exact_false_resolution(rows,rep,n),
              monte_carlo_false_resolution_rate=mcfr,
              monte_carlo_cbc_failure_rate=cbc))
    od=Path(a.outdir); od.mkdir(parents=True,exist_ok=True)
    (od/"gate12_cbc_false_resolution.json").write_text(json.dumps(out,indent=2)+"\n")
    with (od/"gate12_cbc_false_resolution.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
