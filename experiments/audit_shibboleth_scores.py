"""Audit exact Shibboleth score triples retained from a reproduction run.

Input CSV schema:
ID,SCS,TS,BC,LABEL

LABEL is attached only for the audit. It must not participate in the feature
signature.
"""
import argparse,csv,json
from collections import defaultdict,Counter
from pathlib import Path

def main():
 p=argparse.ArgumentParser()
 p.add_argument("csv")
 p.add_argument("--out",default="artifacts/gate8b_shibboleth_exact.json")
 a=p.parse_args()
 rows=list(csv.DictReader(open(a.csv,newline="")))
 required={"ID","SCS","TS","BC","LABEL"}
 if not rows or not required.issubset(rows[0]):
  raise SystemExit(f"required columns: {sorted(required)}")
 cells=defaultdict(list)
 for r in rows:
  # Preserve exact textual floating representation emitted by the run.
  key=(r["SCS"].strip(),r["TS"].strip(),r["BC"].strip())
  cells[key].append(r)
 mixed=[]
 for k,rs in cells.items():
  labs=Counter(x["LABEL"].strip().upper() for x in rs)
  if len(labs)>1:
   mixed.append({"SCS":k[0],"TS":k[1],"BC":k[2],
                 "labels":dict(labs),"ids":[x["ID"] for x in rs]})
 n=len(rows); mixed_ids={i for m in mixed for i in m["ids"]}
 result={
  "records":n,"exact_feature_cells":len(cells),
  "mixed_exact_cells":len(mixed),
  "patches_in_mixed_exact_cells":len(mixed_ids),
  "resolution_deficit_exact":len(mixed_ids)/n if n else 0,
  "claim_resolving_exact":not mixed,
  "claim_conflict_witness_cells":mixed,
 }
 Path(a.out).parent.mkdir(exist_ok=True)
 Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
