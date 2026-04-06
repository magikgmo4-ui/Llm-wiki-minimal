from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from llm_wiki_minimal.extractor import extract_basic_fiches
from llm_wiki_minimal.linker import auto_link
from llm_wiki_minimal.parser import read_text_file
from llm_wiki_minimal.renderer import render_fiche_markdown

DATA_ROOT = Path("data")
FICHES_DIR = DATA_ROOT / "fiches"
INDEX_DIR = DATA_ROOT / "index"
EXPORTS_DIR = DATA_ROOT / "exports"
SOURCES_DIR = DATA_ROOT / "sources"


def ensure_dirs() -> None:
    for path in [FICHES_DIR, INDEX_DIR, EXPORTS_DIR, SOURCES_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def ingest_source(source_file: str) -> list[str]:
    ensure_dirs()
    source_path = Path(source_file)
    text = read_text_file(source_path)
    fiches = auto_link(extract_basic_fiches(text, source_path.name, date.today().isoformat()))

    written = []
    for fiche in fiches:
        target = FICHES_DIR / f"{fiche.id}.md"
        target.write_text(render_fiche_markdown(fiche), encoding="utf-8")
        written.append(str(target))

    build_index()
    export_promotion_candidates()
    return written


def build_index() -> str:
    ensure_dirs()
    items = [{"id": file.stem, "path": str(file)} for file in sorted(FICHES_DIR.glob("*.md"))]
    target = INDEX_DIR / "index.json"
    target.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return str(target)


def export_promotion_candidates() -> str:
    ensure_dirs()
    lines = ["# Promotion Candidates", ""]
    for file in sorted(FICHES_DIR.glob("*.md")):
        text = file.read_text(encoding="utf-8")
        if "promotion_candidate: true" in text:
            lines.append(f"- {file.stem}")
    target = EXPORTS_DIR / "promotion_candidates.md"
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(target)
