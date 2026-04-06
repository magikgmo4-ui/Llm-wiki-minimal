#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src python3 - <<'PY'
from llm_wiki_minimal.service import build_index, export_promotion_candidates, ingest_source
written = ingest_source("docs/examples/sample_source_01.md")
print(f"written={len(written)}")
print(build_index())
print(export_promotion_candidates())
PY
