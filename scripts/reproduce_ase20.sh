#!/usr/bin/env bash
set -euo pipefail
ZIP="${1:-PATCH-SIM_result.zip}"
WORK="${2:-.rer-reproduce}"
rm -rf "$WORK"
mkdir -p "$WORK/extracted" "$WORK/artifacts"
echo "e3b68e17dd4be6a2bafadd6c6b30b52e  $ZIP" | md5sum -c -
unzip -q "$ZIP" -d "$WORK/extracted"
ROOT="$WORK/extracted/PATCH-SIM_result"
python experiments/gate11_patchsim_rer.py "$ROOT" "$WORK/artifacts"
if [ -f experiments/gate12_cbc_exact.py ]; then
  python experiments/gate12_cbc_exact.py "$ROOT" "$WORK/artifacts"
fi
python -m pytest -q
echo "Reproduction complete: $WORK/artifacts"
