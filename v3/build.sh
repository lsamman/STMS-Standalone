#!/bin/bash
# The cargo winch. SKIP_MODELS=1 / SKIP_TEX=1 reuse the last build.
set -eo pipefail
cd "$(dirname "$0")"
B="${BLENDER:-$HOME/Applications/blender-3.6/blender}"
export SHAB_TEX=build/tex
mkdir -p build/mu build/tex
if [ -z "$SKIP_MODELS" ]; then for p in boom hoist platform; do "$B" -b --factory-startup --python-exit-code 1 -P scripts/build_$p.py -- build/mu 2>&1 | grep -E "EXPORT|FACING|Error|Traceback"; done; fi
if [ -z "$SKIP_TEX" ]; then python3 -I scripts/tex_winch.py | tail -1; fi
D=../GameData/StarshipThingyMabobsAndSuch
mkdir -p "$D/Parts" "$D/Patches"
cp build/mu/*.mu build/tex/sep_cw_*.dds cfg/*.cfg "$D/Parts/"
