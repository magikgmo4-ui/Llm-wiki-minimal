from pathlib import Path

from llm_wiki_minimal.parser import read_text_file


def test_read_text_file(tmp_path):
    sample = tmp_path / "sample.md"
    sample.write_text("hello parser\n", encoding="utf-8")

    assert read_text_file(sample) == "hello parser\n"
