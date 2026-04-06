from __future__ import annotations

from .models import WikiFiche


def slugify(value: str) -> str:
    return (
        value.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(":", "")
        .replace("/", "_")
    )


def extract_basic_fiches(text: str, source_name: str, date_str: str) -> list[WikiFiche]:
    fiches: list[WikiFiche] = []

    if "opt-trading" in text:
        fiches.append(
            WikiFiche(
                id="repo_opt_trading_canonique",
                title="Repo canonique opt-trading",
                type="repo_role",
                status="ETABLI",
                date=date_str,
                sources=[source_name],
                tags=["ETABLI", "OPT_TRADING"],
                body="Le repo canonique est opt-trading.",
                promotion_candidate=True,
                promotion_target="memory_bricks",
                confidence="high",
            )
        )

    if "sot/mainline" in text:
        fiches.append(
            WikiFiche(
                id="branch_sot_mainline_continuite",
                title="Branche canonique sot/mainline",
                type="repo_role",
                status="ETABLI",
                date=date_str,
                sources=[source_name],
                tags=["ETABLI", "SOT_MAINLINE"],
                body="La branche canonique de continuité est sot/mainline.",
                promotion_candidate=True,
                promotion_target="memory_bricks",
                confidence="high",
            )
        )

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("REPRISE") or "GO_" in line:
            clean = line.replace("REPRISE", "").strip(" :-")
            fiche_id = slugify(clean or "reprise_point")
            fiches.append(
                WikiFiche(
                    id=fiche_id,
                    title=clean or "Reprise point",
                    type="reprise_point",
                    status="REPRISE",
                    date=date_str,
                    sources=[source_name],
                    tags=["REPRISE"],
                    body=line,
                    promotion_candidate=False,
                    confidence="medium",
                )
            )

    return fiches
