from llm_wiki_minimal.cli import main


def test_cli_build_index(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["llm-wiki-minimal", "build-index"])
    main()
    captured = capsys.readouterr()
    assert "data/index/index.json" in captured.out
