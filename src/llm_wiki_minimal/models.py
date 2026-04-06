from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Status = Literal["ETABLI", "HYPOTHESE", "TODO", "REPRISE"]
FicheType = Literal[
    "decision",
    "component",
    "workflow_rule",
    "repo_role",
    "module_note",
    "reprise_point",
]
LinkType = Literal["related_to", "depends_on", "derived_from", "supersedes", "used_by"]


@dataclass
class WikiLink:
    type: LinkType
    target: str


@dataclass
class WikiFiche:
    id: str
    title: str
    type: FicheType
    status: Status
    date: str
    sources: list[str]
    tags: list[str] = field(default_factory=list)
    body: str = ""
    links: list[WikiLink] = field(default_factory=list)
    promotion_candidate: bool = False
    promotion_target: str | None = None
    confidence: str = "medium"
