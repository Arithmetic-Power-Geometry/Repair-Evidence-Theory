"""Gate 8: real-corpus structural-resolution audit on Shibboleth metadata.

Downloads only public CSV metadata. Ground-truth label is NEVER used to build
an evidence signature. It is consulted only after cells are formed.
"""
from __future__ import annotations
import csv, io, json, urllib.request
from collections import defaultdict, Counter
from pathlib import Path

URLS={
 "core":"https://raw.githubusercontent.com/ali-ghanbari/shibboleth/master/Data%20Set/info.csv",
 "ext":"https://raw.githubusercontent.com/ali-ghanbari/shibboleth/master/Data%20Set/info-ext.csv",
}
OUT=Path("artifacts"); OUT.mkdir(exist_ok=True)

def get(url):
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8",errors="replace")

def parse_core(text):
    out=[]
    for row in csv.reader(io.StringIO(text)):
        if len(row)<9: continue
        # id, project, bug, label, patch_path, tool, location, [method], ochiai, provenance
        rid,project,bug,label,path,tool=row[:6]
        provenance=row[-1]
        ochiai=row[-2]
        middle=row[6:-2]
        location=middle[0] if middle else ""
        method=";".join(middle[1:]) if len(middle)>1 else ""
        out.append(dict(source="core",id=rid,project=project,bug=bug,label=label,
                        path=path,tool=tool,location=location,method=method,
                        ochiai=ochiai,provenance=provenance))
    return out

def parse_ext(text):
    out=[]
    for row in csv.reader(io.StringIO(text)):
        if len(row)<9: continue
        rid,project,bug,label,path,tool=row[:6]
        provenance=row[-1]
        middle=row[6:-1]
        location=middle[0] if middle else ""
        method=";".join(middle[1:]) if len(middle)>1 else ""
        out.append(dict(source="ext",id=rid,project=project,bug=bug,label=label,
                        path=path,tool=tool,location=location,method=method,
                        ochiai="",provenance=provenance))
    return out

records=parse_core(get(URLS["core"]))+parse_ext(get(URLS["ext"]))

def norm_location(s):
    return ";".join(sorted(x.strip() for x in s.split(";") if x.strip()))

def norm_method(s):
    return ";".join(sorted(x.strip() for x in s.split(";") if x.strip()))

def ochiai_bucket(s):
    try:
        x=float(s)
    except Exception:
        return "NA"
    return f"{x:.3f}"

# Evidence representations deliberately exclude label, path directory,
# provenance and APR-tool identity to avoid trivial label leakage.
representations={
 "bug": lambda r:(r["project"],r["bug"]),
 "bug_location": lambda r:(r["project"],r["bug"],norm_location(r["location"])),
 "bug_method": lambda r:(r["project"],r["bug"],norm_method(r["method"])),
 "bug_location_ochiai": lambda r:(r["project"],r["bug"],norm_location(r["location"]),ochiai_bucket(r["ochiai"])),
}

def audit(name,keyfn):
    cells=defaultdict(list)
    for r in records: cells[keyfn(r)].append(r)
    mixed=[]
    mixed_members=0
    unavoidable=0
    for key,rs in cells.items():
        cnt=Counter(r["label"] for r in rs)
        if len(cnt)>1:
            mixed.append((key,rs,cnt))
            mixed_members+=len(rs)
            unavoidable+=min(cnt.values())
    n=len(records)
    return {
      "representation":name,
      "records":n,
      "cells":len(cells),
      "mixed_cells":len(mixed),
      "mixed_cell_rate":len(mixed)/len(cells) if cells else 0,
      "patches_in_mixed_cells":mixed_members,
      "resolution_deficit":mixed_members/n if n else 0,
      "cellwise_unavoidable_error_lower_bound":unavoidable/n if n else 0,
      "claim_resolving":len(mixed)==0,
      "example_conflicts":[
        {"signature":[str(x) for x in key],
         "labels":dict(cnt),
         "patch_ids":[r["id"] for r in rs[:8]]}
        for key,rs,cnt in mixed[:20]
      ]
    }

result={
 "dataset":"ali-ghanbari/shibboleth public metadata",
 "label_counts":dict(Counter(r["label"] for r in records)),
 "tool_counts":dict(Counter(r["tool"] for r in records)),
 "audits":[audit(n,f) for n,f in representations.items()],
 "design_note":"Evidence signatures exclude ground-truth label, path label directories, provenance, and APR tool identity."
}
(OUT/"gate8_shibboleth_resolution.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
with (OUT/"gate8_shibboleth_summary.csv").open("w",newline="") as f:
    fields=["representation","records","cells","mixed_cells","mixed_cell_rate","patches_in_mixed_cells","resolution_deficit","cellwise_unavoidable_error_lower_bound","claim_resolving"]
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for a in result["audits"]: w.writerow({k:a[k] for k in fields})
print(json.dumps(result,indent=2,sort_keys=True))
