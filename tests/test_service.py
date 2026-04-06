from pathlib import Path

from llm_wiki_minimal.service import build_index, export_promotion_candidates, ingest_source


def test_service_ingest_and_exports(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    source = tmp_path / "sample.md"
    source.write_text("opt-trading\nsot/mainline\nREPRISE: GO_TEST_01\n", encoding="utf-8")

    written = ingest_source(str(source))
    assert written

    index_path = Path(build_index())
    export_path = Path(export_promotion_candidates())

    assert index_path.exists()
    assert export_path.exists()
    assert (tmp_path / "data" / "fiches" / "repo_opt_trading_canonique.md").exists()
