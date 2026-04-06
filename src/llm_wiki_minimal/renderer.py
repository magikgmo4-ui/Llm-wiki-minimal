from __future__ import annotations

from .models import WikiFiche


def render_fiche_markdown(fiche: WikiFiche) -> str:
    tags_yaml = "\n".join(f"  - {tag}" for tag in fiche.tags) or "[]"
    sources_yaml = "\n".join(f"  - {src}" for src in fiche.sources) or "[]"

    if fiche.links:
        links_yaml = "\n".join(
            f"  - type: {link.type}\n    target: {link.target}" for link in fiche.links
        )
    else:
        links_yaml = "[]"

    promotion_target = fiche.promotion_target or ""
    promotion_flag = "true" if fiche.promotion_candidate else "false"

    return f"""---
id: {fiche.id}
title: {fiche.title}
type: {fiche.type}
status: {fiche.status}
date: {fiche.date}
sources:
{sources_yaml}
tags:
{tags_yaml}
links:
{links_yaml}
promotion_candidate: {promotion_flag}
promotion_target: {promotion_target}
confidence: {fiche.confidence}
---

## Résumé
{fiche.body}
"""
