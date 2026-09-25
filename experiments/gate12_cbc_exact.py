#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict
from math import comb
import csv, json, sys

zip_path=Path(sys.argv[1])
outdir=Path(sys.argv[2]) if len(sys.argv)>2 else Path("artifacts")
outdir.mkdir(parents=True,exist_ok=True)

records=[]
with ZipFile(zip_path) as z:
    for name in z.namelist():
        parts=name.split("/")
        if len(parts)>=4 and parts[-1]=="result" and parts[-3] in ("Evosuite","Randoop"):
            lines=z.read(name).decode("utf-8",errors="replace").splitlines()
            if len(lines)>=3 and lines[0].strip() in ("Correct","Incorrect"):
                records.append({"generator":parts[-3],"patch":parts[-2],
                                "label":lines[0].strip(),
                                "v1":lines[1].strip(),"v2":lines[2].strip()})

def signature(r,rep):
    if rep=="vector1_only": return (r["generator"],r["v1"])
    if rep=="vector2_only": return (r["generator"],r["v2"])
    return (r["generator"],r["v1"],r["v2"])

def cells(rep):
    d=defaultdict(list)
    for i,r in enumerate(records): d[signature(r,rep)].append(i)
    return d

def exact_false_resolution(rep,n):
    d=cells(rep)
    mixed=[]
    mixed_ids=set()
    for idxs in d.values():
        labels=[records[i]["label"] for i in idxs]
        if len(set(labels))>1:
            a=sum(x=="Correct" for x in labels); b=sum(x=="Incorrect" for x in labels)
            mixed.append((a,b)); mixed_ids.update(idxs)
    if not mixed: return 0.0,0
    other=len(records)-len(mixed_ids)
    poly=[1]
    for a,b in mixed:
        q=[1]+[(comb(a,k) if k<=a else 0)+(comb(b,k) if k<=b else 0)
               for k in range(1,max(a,b)+1)]
        new=[0]*(len(poly)+len(q)-1)
        for i,x in enumerate(poly):
            for j,y in enumerate(q): new[i+j]+=x*y
        poly=new
    fav=sum(c*comb(other,n-k) for k,c in enumerate(poly)
            if 0<=n-k<=other)
    return fav/comb(len(records),n),len(mixed)

sizes=[25,50,100,200,400,800,1200,1500]
rows=[]
for rep in ("vector1_only","vector2_only","full_pair"):
    for n in sizes:
        p,m=exact_false_resolution(rep,n)
        rows.append({"representation":rep,"sample_size":n,
                     "parent_mixed_cells":m,
                     "exact_false_resolution_probability":p})

with (outdir/"gate12_cbc_exact.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
(outdir/"gate12_cbc_exact.json").write_text(json.dumps({
    "records":len(records),"sizes":sizes,"rows":rows
},indent=2)+"\n")
print(json.dumps(rows,indent=2))
