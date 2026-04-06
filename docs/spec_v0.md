# SPEC V0 — llm_wiki_minimal

## Objectif
Créer une couche intermédiaire de pré-consolidation compatible avec des repos consommateurs comme `opt-trading`.

## Inputs V0
- synthèses validées
- journaux de session
- fichiers de reprise
- notes techniques ciblées
- audits repo-sourcés

## Outputs V0
- fiches markdown
- index simple
- liste de candidats de promotion

## Contraintes
- texte only
- provenance obligatoire
- datation obligatoire
- statut obligatoire
- pas de promotion automatique
- pas d’écrasement silencieux
- Git prioritaire pour le durable

## Statuts
- ETABLI
- HYPOTHESE
- TODO
- REPRISE

## Types
- decision
- component
- workflow_rule
- repo_role
- module_note
- reprise_point
