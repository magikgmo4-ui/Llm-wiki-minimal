from llm_wiki_minimal.linker import auto_link
from llm_wiki_minimal.models import WikiFiche


def test_auto_link():
    a = WikiFiche(
        id="repo_opt_trading_canonique",
        title="repo",
        type="repo_role",
        status="ETABLI",
        date="2026-04-05",
        sources=["x"],
        tags=["OPT_TRADING"],
    )
    b = WikiFiche(
        id="other",
        title="other",
        type="module_note",
        status="ETABLI",
        date="2026-04-05",
        sources=["x"],
        tags=["OPT_TRADING"],
    )
    linked = auto_link([a, b])
    assert linked[1].links
