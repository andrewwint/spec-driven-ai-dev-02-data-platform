# Customer Data Pipeline

> Course 2: Data Platform — Agents for Unfamiliar Domains

A data transformation pipeline that teaches how to use AI agents when navigating unfamiliar domains.

## 🎯 What You're Learning

This project uses a data pipeline as the **vehicle**, but the real lessons are:

| Surface Topic | Actual Skill |
|---------------|--------------|
| S3 data organization | Using agents to learn unfamiliar concepts |
| Data validation | Schema contracts as deterministic gates |
| Transformation logic | Multi-agent handoffs with context preservation |
| Lambda deployment | Feeling confident deploying agent-assisted code |

**You are NOT becoming a data engineer.** You're learning to use agents to navigate domains you don't know deeply.

## 🚀 Quick Start

```bash
# 1. Clone and enter the project
cd customer-data-pipeline

# 2. Run setup
./setup.sh

# 3. Verify everything works
make help
make agents-check

# 4. Start your first advisor conversation
# Open VS Code, start Copilot Chat, select @data-advisor
```

## 📁 Project Structure

```
customer-data-pipeline/
├── README.md               # You are here
├── CHANGELOG.md            # Version releases (human owned)
├── HISTORY.md              # Project narrative (agent memory)
├── AGENTS.md               # Agent team documentation
├── Makefile                # Pipeline automation
├── .pre-commit-config.yaml # Quality gates
├── requirements.txt        # Python dependencies
├── data/
│   ├── raw/                # Source data (don't modify)
│   ├── cleaned/            # Validated & cleaned data
│   └── features/           # ML-ready features
├── notebooks/              # Exploration notebooks
├── src/
│   ├── validators/         # Schema validation code
│   └── transformers/       # Data cleaning code
├── docs/
│   ├── proposals/          # Change proposals
│   ├── runbooks/           # Operational procedures
│   └── playbooks/          # Troubleshooting guides
└── .github/
    └── agents/             # Copilot agent definitions
        └── data-advisor.agent.md
```

## 🤖 Agent Team

| Agent | Type | Purpose |
|-------|------|---------|
| **data-advisor** | Advisor | Teaches data concepts (read-only) |
| **data-explorer** | Doer | Profiles data, finds issues |
| **schema-validator** | Gate | Validates schema contracts (read-only) |
| **transformer** | Doer | Writes transformation code |
| **reviewer** | Gate | Reviews changes (read-only) |

All 5 agents are included and ready to use. Fine-tune them for your specific needs.

## 📊 Sample Data

The `data/raw/` folder contains sample customer data:

- **customers.csv** — Customer demographics (1000 rows)
- **transactions.csv** — Purchase history (5000 rows)  
- **sessions.csv** — Website activity (10000 rows)

This data intentionally includes quality issues for you to discover and fix.

## 🔧 Make Targets

```bash
make help              # Show all targets
make agents-check      # List available agents
make validate-schema   # Run schema validation
make transform         # Run transformations
make pipeline          # Full pipeline (validate → transform → validate)
make status            # Show project status
```

## 📚 Course Workflow

```
1. Ask data-advisor to explain concepts
       ↓
2. Use data-explorer to profile data
       ↓
3. Create schema proposal
       ↓
4. Have schema-validator review
       ↓
5. Use transformer to write cleaning code
       ↓
6. Have reviewer validate changes
       ↓
7. Deploy to Lambda
```

## 🔗 Connections

- **From:** Course 1 (Foundations) — DARE model, agent patterns, proposals
- **To:** Course 3 (ML Pipelines) — Clean data for model training

## 📖 Documentation

- [AGENTS.md](AGENTS.md) — Agent team and workflows
- [HISTORY.md](HISTORY.md) — Project narrative and decisions
- [CHANGELOG.md](CHANGELOG.md) — Version releases

---

*Part of the Spec-Driven AI Development Course Series*
