# Course 2: Data Platform — Agents for Unfamiliar Domains

## Course Overview

**Duration:** 11-13 hours
**Prerequisites:** Course 1 (Foundations) or equivalent experience with Copilot agents
**Outcome:** Students will build a data pipeline using AI agents to navigate an unfamiliar domain, learning the **Advisor Pattern** for domain exploration and building specialized agents for each phase of data work.

**Running Project:** "Customer Data Pipeline" — A data transformation project that teaches how to use agents when you're NOT the expert.

**Core Throughline:** _"Manage the LLM's context window like you manage your own attention."_

**Course 2 Focus:** What context does a data pipeline need? (schemas, expectations, lineage)

---

> ### 🚀 Fast Track for Experienced Developers
>
> If you're comfortable with Course 1 patterns and have worked with data before, you can move quickly through the early modules.
>
> | Your Goal                         | Start Here                                     |
> | --------------------------------- | ---------------------------------------------- |
> | Just want the Advisor Pattern     | Module 1 (Lesson 1.2) → Module 2               |
> | Already know data concepts        | Skip Module 1, start at Module 2               |
> | Want agent-driven validation      | Module 4 (Schema Validator)                    |
> | Want to see production deployment | Module 6 (ROI Analysis + Deployment Decisions) |
> | Want MCP integration              | Module 7 (MCP Deep Dive)                       |
> | Ready for ML                      | Complete Module 6, proceed to Course 3         |
>
> **Key concepts to extract if skimming:**
>
> - The Advisor Pattern (Module 2) — NEW in this course
> - Schema contracts as "D" in DARE (Module 4)
> - Handoff chains: Advisor → Explorer → Transformer → Validator (Module 5)
> - MCP for data pipeline tooling (Module 7)
> - Industry context: where dbt, Airflow, Great Expectations fit (Lesson 1.3)

---

## What You're Really Learning

This course uses a data pipeline as the **vehicle**, but the real lessons are:

| Surface Topic        | Actual Skill                                    |
| -------------------- | ----------------------------------------------- |
| S3 data organization | Using agents to learn unfamiliar concepts       |
| Data validation      | Schema contracts as deterministic gates         |
| Transformation logic | Multi-agent handoffs with context preservation  |
| Deployment decisions | Feeling confident deploying agent-assisted code |

**You are NOT becoming a data engineer.** You're learning to use agents to:

- Navigate domains you don't know deeply
- Make informed trade-offs with AI assistance
- Build production-quality artifacts with confidence
- Know when to hand off to specialists (human or AI)

---

## Industry Context — Where This Fits

We teach the **WHY** so you can adopt the **WHAT** that fits your stack.

| Our Approach                     | Industry Standard      | Why We Choose Ours                                 |
| -------------------------------- | ---------------------- | -------------------------------------------------- |
| pandas in notebooks → production | dbt + data warehouse   | Teaches same principles without Snowflake/Redshift |
| S3 organized folders             | Lake Formation catalog | Simpler; same mental model                         |
| Python validation scripts        | Great Expectations     | You understand what's happening                    |
| Makefile triggers                | Airflow DAGs           | Focus on transformation logic, not orchestration   |

**The patterns transfer directly:**

| Our Pattern         | dbt Equivalent   | Airflow Equivalent   |
| ------------------- | ---------------- | -------------------- |
| `docs/proposals/`   | `schema.yml`     | DAG documentation    |
| Python validation   | dbt tests        | Task success/failure |
| `CHANGELOG.md`      | `manifest.json`  | DAG versioning       |
| `make validate`     | `dbt test`       | Operators            |
| Deployment proposal | dbt Cloud config | DAG definition       |

When you're ready to adopt dbt or Airflow, you'll recognize the thinking.

---

## Project Structure Evolution

### Module 1: Setup

```
customer-data-pipeline/
├── README.md
├── CHANGELOG.md
├── HISTORY.md
├── AGENTS.md
├── Makefile                        # ✅ Pre-configured
├── .pre-commit-config.yaml         # ✅ Pre-configured
├── requirements.txt
├── data/
│   ├── raw/                        # Sample data loaded here
│   ├── cleaned/
│   └── features/
└── skills/
    └── data-advisor.SKILL.md       # NEW: Advisor pattern
```

### Module 4: Validation

```
customer-data-pipeline/
├── ...
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   └── 02-data-cleaning.ipynb
├── docs/
│   └── proposals/
│       └── 001-schema-contract.md
└── skills/
    ├── data-advisor.SKILL.md
    ├── data-explorer.SKILL.md
    └── schema-validator.SKILL.md
```

### Module 6: Production

```
customer-data-pipeline/
├── README.md
├── CHANGELOG.md
├── HISTORY.md
├── AGENTS.md
├── Makefile
├── .pre-commit-config.yaml
├── requirements.txt
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-data-cleaning.ipynb
│   └── 03-feature-engineering.ipynb
├── src/
│   ├── validators/
│   └── transformers/
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── features/
├── docs/
│   ├── proposals/
│   │   ├── 001-schema-contract.md
│   │   └── 002-deployment-approach.md  # ROI analysis & decision
│   ├── runbooks/
│   └── playbooks/
└── skills/
    ├── data-advisor.SKILL.md
    ├── data-explorer.SKILL.md
    ├── schema-validator.SKILL.md
    ├── transformer.SKILL.md
    └── reviewer.SKILL.md
```

### Module 7: MCP Integration

```
customer-data-pipeline/
├── ...
├── mcp/
│   └── data_pipeline_server.py     # Custom MCP server
└── .vscode/
    └── mcp.json                    # MCP configuration
```

---

## Getting Started

This course builds on Course 1's foundations. You'll use agents, proposals, and the DARE pattern in new ways—specifically for data work.

**What's Different in Course 2:**
- **New Agent Type:** The Advisor (teaches without modifying files)
- **New Domain:** Data engineering (unfamiliar to most developers)
- **New Context:** Schemas, quality issues, and lineage
- **New Pattern:** Separation of teaching (Advisor) from doing (Transformer)

**What Stays the Same:**
- DARE model framework
- Proposal-driven development
- Agent handoff chains
- HISTORY.md for memory
- Makefile for deterministic commands

---

## AgentSkills.io Alignment Note

This course uses AgentSkills.io terminology for AI-assisted workflows. You'll notice references to **skill files** (`.SKILL.md`) and the **skills/** directory instead of the older "agent" terminology. The concepts remain the same—these are role-based AI agents configured through structured files—but the updated naming emphasizes their reusable, composable nature in the AgentSkills ecosystem.
