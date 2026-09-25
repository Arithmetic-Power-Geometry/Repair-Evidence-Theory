#!/usr/bin/env bash
set -euo pipefail
# Run from a checked-out Shibboleth example after its documented prerequisites
# are installed. Shibboleth normally deletes scores.csv after classification.
# This wrapper uses the ranking path to compute scores and is intended as a
# reproducibility scaffold; do not claim results until retained feature output
# is actually produced and audited.
echo "Gate 8B reproduction requires the upstream Shibboleth Java/JDK/Defects4J environment."
echo "Retain an ID,SCS,TS,BC CSV and join labels from the example input-file.csv."
