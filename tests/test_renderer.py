from llm_wiki_minimal.models import WikiFiche
from llm_wiki_minimal.renderer import render_fiche_markdown


def test_render_markdown():
    fiche = WikiFiche(
        id="x",
        title="Title",
        type="decision",
        status="ETABLI",
        date="2026-04-05",
        sources=["s.md"],
        body="Body",
    )
    text = render_fiche_markdown(fiche)
    assert "title: Title" in text
    assert "## Résumé" in text
