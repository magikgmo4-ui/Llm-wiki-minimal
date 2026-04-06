from .models import WikiFiche, WikiLink


def auto_link(fiches: list[WikiFiche]) -> list[WikiFiche]:
    ids = {fiche.id for fiche in fiches}

    for fiche in fiches:
        if fiche.id != "repo_opt_trading_canonique" and "OPT_TRADING" in fiche.tags:
            if "repo_opt_trading_canonique" in ids:
                fiche.links.append(WikiLink(type="related_to", target="repo_opt_trading_canonique"))

    return fiches
