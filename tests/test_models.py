from llm_wiki_minimal.models import WikiFiche


def test_model_basic():
    fiche = WikiFiche(
        id="x",
        title="y",
        type="decision",
        status="ETABLI",
        date="2026-04-05",
        sources=["a.md"],
    )
    assert fiche.id == "x"
    assert fiche.status == "ETABLI"
