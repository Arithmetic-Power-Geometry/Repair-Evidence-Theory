#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict, Counter
import csv, json, sys

root=Path(sys.argv[1])
outdir=Path(sys.argv[2]) if len(sys.argv)>2 else Path("artifacts")
outdir.mkdir(parents=True,exist_ok=True)

records=[]
for generator in ("Evosuite","Randoop"):
    base=root/generator
    if not base.exists():
        continue
    for d in sorted(base.iterdir()):
        p=d/"result"
        if not d.is_dir() or not p.exists():
            continue
        lines=p.read_text(errors="replace").splitlines()
        if len(lines)<3:
            continue
        label=lines[0].strip()
        if label not in {"Correct","Incorrect"}:
            continue
        records.append({
            "generator":generator,
            "patch":d.name,
            "label":label,
            "v1_text":lines[1].strip(),
            "v2_text":lines[2].strip(),
        })

def audit(rows, fields):
    cells=defaultdict(list)
    for r in rows:
        cells[tuple(r[f] for f in fields)].append(r)
    mixed=[]
    for sig,members in cells.items():
        if len({m["label"] for m in members})>1:
            mixed.append((sig,members))
    mixed_members=sum(len(m) for _,m in mixed)
    unavoidable=sum(min(
        sum(x["label"]=="Correct" for x in m),
        sum(x["label"]=="Incorrect" for x in m)
    ) for _,m in mixed)
    return {
        "records":len(rows),
        "cells":len(cells),
        "mixed_cells":len(mixed),
        "mixed_members":mixed_members,
        "resolution_deficit":mixed_members/len(rows) if rows else 0.0,
        "cell_mixed_rate":len(mixed)/len(cells) if cells else 0.0,
        "unavoidable_uniform_cell_error_count":unavoidable,
        "unavoidable_uniform_cell_error_rate":unavoidable/len(rows) if rows else 0.0,
        "claim_resolving":len(mixed)==0,
        "largest_cell":max((len(v) for v in cells.values()),default=0),
        "examples":[
            {"signature":list(sig),
             "members":[{"patch":x["patch"],"label":x["label"]} for x in members[:20]]}
            for sig,members in mixed[:10]
        ],
    }

summary=[]
detail={}
for gen in ("Evosuite","Randoop"):
    rows=[r for r in records if r["generator"]==gen]
    for name,fields in (
        ("full_pair",["v1_text","v2_text"]),
        ("vector1_only",["v1_text"]),
        ("vector2_only",["v2_text"]),
    ):
        a=audit(rows,fields)
        detail[f"{gen}:{name}"]=a
        summary.append({"generator":gen,"representation":name,
                        **{k:v for k,v in a.items() if k!="examples"}})

for name,fields in (
    ("full_pair",["generator","v1_text","v2_text"]),
    ("vector1_only",["generator","v1_text"]),
    ("vector2_only",["generator","v2_text"]),
):
    a=audit(records,fields)
    detail[f"combined:{name}"]=a
    summary.append({"generator":"combined","representation":name,
                    **{k:v for k,v in a.items() if k!="examples"}})

(outdir/"gate11_rer_real.json").write_text(
    json.dumps({
        "label_counts":dict(Counter(r["label"] for r in records)),
        "generator_counts":dict(Counter(r["generator"] for r in records)),
        "audits":detail
    },indent=2)+"\n"
)
keys=["generator","representation","records","cells","mixed_cells","mixed_members",
      "resolution_deficit","cell_mixed_rate","unavoidable_uniform_cell_error_count",
      "unavoidable_uniform_cell_error_rate","claim_resolving","largest_cell"]
with (outdir/"gate11_rer_real.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=keys)
    w.writeheader()
    for row in summary:
        w.writerow({k:row[k] for k in keys})
print(json.dumps(summary,indent=2))
