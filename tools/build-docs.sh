#!/usr/bin/env bash
#
# build-docs.sh — generate WIDOCO documentation into a repository folder.
#
#   ./tools/build-docs.sh versions/v2.1/rdip-v2.1.ttl docs/2.1.0
#   ./tools/build-docs.sh core/rdip.ttl               docs/latest
#
# Why this exists rather than calling WIDOCO directly:
#
#   1. WIDOCO decides for itself whether to write into <outFolder> or into
#      <outFolder>/doc. This runs it into a scratch directory, finds whichever
#      layout it chose, and copies the contents into the target folder, so the
#      repository layout never depends on that choice.
#   2. WIDOCO does not read catalog-v001.xml; it resolves owl:imports over the
#      network, so this needs an internet connection and -includeImportedOntologies
#      to reproduce the merged output that 1.0.0 and 2.0.0 have.
#   3. WIDOCO writes index-en.html but not the index.html redirect stub that
#      GitHub Pages needs. This writes it afterwards.
#
# Set WIDOCO to your jar, or edit the default below.

set -euo pipefail

WIDOCO="${WIDOCO:-$HOME/Downloads/widoco-jar-with-dependencies.jar}"

if [ $# -ne 2 ]; then
  echo "usage: $0 <ontology-file> <target-docs-folder>" >&2
  echo "   eg: $0 versions/v2.1/rdip-v2.1.ttl docs/2.1.0" >&2
  exit 1
fi

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ONT="$REPO/$1"
TARGET="$REPO/$2"

[ -f "$WIDOCO" ] || { echo "WIDOCO jar not found at: $WIDOCO" >&2
                      echo "set it with:  WIDOCO=/path/to/widoco.jar $0 ..." >&2; exit 1; }
[ -f "$ONT" ]    || { echo "no such ontology file: $ONT" >&2; exit 1; }

ONT_DIR="$(cd "$(dirname "$ONT")" && pwd)"
ONT_FILE="$(basename "$ONT")"

if [ ! -f "$ONT_DIR/catalog-v001.xml" ]; then
  echo "WARNING: no catalog-v001.xml beside $ONT_FILE." >&2
  echo "         owl:imports will be fetched over the network or dropped." >&2
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "==> generating from $1"
cd "$ONT_DIR"
java -jar "$WIDOCO" \
  -ontFile "$ONT_FILE" \
  -outFolder "$TMP" \
  -rewriteAll \
  -getOntologyMetadata \
  -includeAnnotationProperties \
  -includeImportedOntologies \
  -webVowl \
  -uniteSections \
  -noPlaceHolderText \
  -lang en

# WIDOCO may have written into $TMP or into $TMP/doc.
SRC="$TMP"
[ -f "$TMP/doc/index-en.html" ] && SRC="$TMP/doc"

if [ ! -f "$SRC/index-en.html" ]; then
  echo "ERROR: WIDOCO produced no index-en.html; nothing copied." >&2
  echo "       scratch directory was $TMP" >&2
  exit 1
fi

echo "==> replacing $2"
mkdir -p "$TARGET"
rsync -a --delete "$SRC"/ "$TARGET"/

# The stub GitHub Pages serves for the bare directory URL.
cat > "$TARGET/index.html" <<'HTML'
<!DOCTYPE html>
<html>
   <head>
      <meta http-equiv="refresh" content="0; url=index-en.html">
   </head>
   <body>
      <p>Redirecting to <a href="index-en.html">documentation</a>...</p>
   </body>
</html>
HTML

echo "==> checking output"
python3 - "$TARGET" <<'PY'
import sys, pathlib
try:
    import rdflib
except ImportError:
    print("  (rdflib not installed; skipping triple count)")
    sys.exit(0)
t = pathlib.Path(sys.argv[1])
for name in ("ontology.ttl", "ontology.owl", "ontology.jsonld", "ontology.nt"):
    f = t / name
    if not f.exists():
        print(f"  MISSING {name}")
        continue
    n = len(rdflib.Graph().parse(f))
    note = "imports merged" if n > 5000 else "RDIP ONLY, imported vocabularies were not loaded"
    print(f"  {name:18s} {n:6d} triples  ({note})")
for name in ("index.html", "index-en.html", "readme.md"):
    print(f"  {name:18s} {'ok' if (t / name).exists() else 'MISSING'}")
for name in ("resources", "webvowl", "provenance"):
    print(f"  {name:18s} {'ok' if (t / name).is_dir() else 'MISSING'}")
PY

echo "==> done: $2"
