from pathlib import Path
import importlib.util, math

ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    s=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_gate11_frozen_real_result_exists_and_has_expected_rows():
    p=ROOT/"artifacts/gate11_rer_real.csv"
    text=p.read_text()
    assert "Evosuite,vector1_only,879,451,3,12" in text
    assert "Randoop,vector1_only,883,535,6,31" in text
    assert "combined,vector1_only,1762,986,9,43" in text
    assert "combined,full_pair,1762,1161,0,0" in text

def test_gate11_enrichment_is_monotone_on_observed_exact_cells():
    import csv
    rows=list(csv.DictReader((ROOT/"artifacts/gate11_rer_real.csv").open()))
    d={(r["generator"],r["representation"]):r for r in rows}
    assert float(d[("combined","vector1_only")]["resolution_deficit"])>0
    assert float(d[("combined","full_pair")]["resolution_deficit"])==0
    assert d[("combined","vector1_only")]["claim_resolving"]=="False"
    assert d[("combined","full_pair")]["claim_resolving"]=="True"

def test_gate12_exact_false_resolution_is_monotone_decreasing():
    import csv
    p=ROOT/"artifacts/gate12_cbc_exact.csv"
    if not p.exists(): return
    rows=list(csv.DictReader(p.open()))
    vals=[float(r["exact_false_resolution_probability"]) for r in rows]
    assert all(a>=b for a,b in zip(vals,vals[1:]))
    assert vals[0]>.99
    assert vals[-1]<1e-6
