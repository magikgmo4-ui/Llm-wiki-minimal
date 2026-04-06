#!/usr/bin/env bash
set -euo pipefail

python3 -m llm_wiki_minimal.cli ingest docs/examples/sample_source_01.md
