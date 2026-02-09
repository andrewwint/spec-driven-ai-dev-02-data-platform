# GitHub Copilot Instructions

This project follows the **spec-driven AI development** methodology.

## Project Overview

**Customer Data Pipeline** — A data transformation project that teaches how to use AI agents when navigating unfamiliar domains.

## Key Files to Reference

- `AGENTS.md` — Agent team and workflows
- `HISTORY.md` — Project narrative and decisions (read this first!)
- `docs/proposals/*.md` — Schema contracts and change proposals

## Agent Philosophy

1. **Context is Attention** — What you provide determines output quality
2. **DARE Model** — Deterministic first, AI for ambiguity, Review at boundaries, Escalate on failure
3. **Tool Restrictions** — Each agent has limited capabilities by design
4. **Handoffs** — Agents pass work to each other at defined boundaries

## DARE for Data Pipelines

| Letter | Application |
|--------|-------------|
| **D** | Schema validation, null checks, format checks |
| **A** | Transformation logic, feature engineering |
| **R** | schema-validator, reviewer agents |
| **E** | Quality threshold alerts |

## Data Organization

```
data/
├── raw/       # Never modify - original source data
├── cleaned/   # Validated and standardized
└── features/  # ML-ready features
```

## Before Implementing

1. Check if a schema contract exists in `docs/proposals/`
2. Read `HISTORY.md` for context
3. Understand the validation rules before writing code

## Documentation Patterns

- **CHANGELOG.md** — Version releases (human owned)
- **HISTORY.md** — Project narrative (agent memory)
- **Proposals** — Document decisions BEFORE implementing
