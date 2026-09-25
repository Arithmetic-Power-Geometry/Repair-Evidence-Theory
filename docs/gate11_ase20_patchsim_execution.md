# Gate 11 — ASE20 PATCH-SIM Execution

This gate moves RER from protocols to direct execution on a primary published
APCA artifact.

Primary dataset: Wang et al., ASE 2020, Zenodo 10.5281/zenodo.3730599.

The archive description states that `PATCH-SIM_result.zip` contains output
vector files from PATCH-SIM and E-PATCH-SIM. The workflow downloads that exact
43.2 MB archive, verifies the publisher-reported MD5
`e3b68e17dd4be6a2bafadd6c6b30b52e`, extracts it, inventories the released
schema, and uploads the inventory as a workflow artifact.

## Why inventory first

We do not write a parser based on guessed file names or guessed vector schema.
The first CI run freezes the actual archive structure. The next commit will
build the RER parser against those observed files.

## Next quantitative outputs

After schema inspection:
1. map each vector to patch and correctness label;
2. condition all cells by Defects4J bug;
3. compute exact vector cells;
4. enumerate opposite-label CCWs;
5. compute micro/macro Resolution Deficit;
6. compare PATCH-SIM versus E-PATCH-SIM;
7. add Daikon/generated-test evidence and measure cell splitting;
8. reproduce conventional APCA results beside RER diagnostics.

No numerical RER claim is made by this inventory gate alone.
