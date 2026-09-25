#!/usr/bin/env python3
"""Inventory an extracted ASE20 PATCH-SIM artifact without assuming its schema."""
from pathlib import Path
import csv,json,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else "external/PATCH-SIM_result")
out=Path(sys.argv[2] if len(sys.argv)>2 else "artifacts/gate11_patchsim_inventory.json")
items=[]
for p in sorted(root.rglob("*")):
 if not p.is_file(): continue
 rec={"path":str(p.relative_to(root)),"bytes":p.stat().st_size,"suffix":p.suffix.lower()}
 if p.stat().st_size <= 2_000_000 and p.suffix.lower() in {".txt",".csv",".tsv",".json",".out",".result"}:
  try:
   text=p.read_text(errors="replace")
   lines=text.splitlines()
   rec["line_count"]=len(lines)
   rec["head"]=lines[:5]
   if p.suffix.lower() in {".csv",".tsv"} and lines:
    dialect=csv.Sniffer().sniff("\n".join(lines[:10]))
    rows=list(csv.reader(lines[:10],dialect))
    rec["sample_widths"]=[len(r) for r in rows]
  except Exception as e: rec["preview_error"]=str(e)
 items.append(rec)
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"root":str(root),"files":len(items),"items":items},indent=2)+"\n")
print(json.dumps({"files":len(items),"suffixes":sorted({x["suffix"] for x in items})},indent=2))
