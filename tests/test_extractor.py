from llm_wiki_minimal.extractor import extract_basic_fiches


def test_extract_basic_fiches():
    text = "opt-trading\nsot/mainline\nREPRISE: GO_TEST_01"
    fiches = extract_basic_fiches(text, "sample.md", "2026-04-05")
    ids = {f.id for f in fiches}
    assert "repo_opt_trading_canonique" in ids
    assert "branch_sot_mainline_continuite" in ids
