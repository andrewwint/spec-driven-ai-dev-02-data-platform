# Spec-Driven AI Development — Course 2: Data Platform Architecture

Apply spec-driven methodology to data engineering with the Advisor agent pattern.

## Prerequisites

- **Course 1: Foundations** (required)
  - `.agent.md` format
  - DARE model
  - Proposal pattern
  - Makefile conventions
  - HISTORY.md pattern
- Python 3.11+
- VS Code with GitHub Copilot

## How To Use This Repo

Each folder in `code/` is a **complete snapshot** of the project at that module's checkpoint. You don't build on the previous folder — each one stands alone.

**Option A: Follow along**  
Download `attachments/customer-data-pipeline-starter.zip`, unzip it, and build alongside the lectures.

**Option B: Jump to a module**  
Copy any module folder as your starting point:

```bash
cp -r code/module-4-validation/ my-project/
cd my-project/
```

**Option C: Compare your work**  
Diff your project against the reference:

```bash
diff -r my-project/ code/module-5-transformation/
```

## Course Modules

| #   | Module                           | Folder                     | Duration |
| --- | -------------------------------- | -------------------------- | -------- |
| 1   | Entering an Unfamiliar Domain    | `module-1-setup/`          | 90 min   |
| 2   | The Advisor Pattern              | `module-2-advisor/`        | 90 min   |
| 3   | Data Exploration with Agents     | `module-3-exploration/`    | 90 min   |
| 4   | Schema Validation as DARE        | `module-4-validation/`     | 90 min   |
| 5   | Data Transformation Pipeline     | `module-5-transformation/` | 90 min   |
| 6   | From Notebook to Production      | `module-6-production/`     | 75 min   |
| 7   | MCP Integration                  | `module-7-mcp/`            | 60 min   |
| 8   | Capstone — Complete the Pipeline | `module-8-complete/`       | 90 min   |

**Total: ~11–13 hours**

## Agent Team

| Agent            | Type    | Model Tier | Purpose                           |
| ---------------- | ------- | ---------- | --------------------------------- |
| data-advisor     | Advisor | Balanced   | Teaches data concepts (read-only) |
| data-explorer    | Doer    | Fast       | Profiles data, finds issues       |
| schema-validator | Gate    | Fast       | Validates schema contracts        |
| transformer      | Doer    | Fast       | Writes transformation code        |
| reviewer         | Gate    | Balanced   | Reviews changes (read-only)       |

## Tech Stack

| Tool           | Purpose                           |
| -------------- | --------------------------------- |
| Python 3.11+   | Data processing                   |
| pandas         | Data manipulation                 |
| VS Code        | IDE + AI host                     |
| GitHub Copilot | Agent runtime (`.agent.md` files) |
| MCP            | Tool/resource protocol            |
| Make           | Deterministic verification        |
| pre-commit     | Git hook automation               |
| ruff           | Python linting/formatting         |

## Series Overview

This is **Course 2 of 5** in the Spec-Driven AI Development series:

| Course                 | Focus                                      | Status             |
| ---------------------- | ------------------------------------------ | ------------------ |
| 1. Foundations         | Thinking in Chunks                         | ✅ Prerequisite    |
| **2. Data Platform**   | **Advisor Pattern for Unfamiliar Domains** | **← you are here** |
| 3. ML Workflows        | Feature Engineering + Model Training       | Next               |
| 4. API Agents          | Production Services                        | Coming             |
| 5. DevOps & Production | CI/CD + Deployment                         | Coming             |

**Connects From:** Course 1 provides `.agent.md` format, DARE model, proposal pattern, Makefile conventions.

**Connects To:** Course 3 receives clean validated dataset in `data/features/`, schema contract concepts, Advisor pattern.

## Industry Context

We teach principles that transfer to industry tools:

| We Teach               | Industry Equivalent |
| ---------------------- | ------------------- |
| Schema contracts       | dbt schema tests    |
| Makefile orchestration | Airflow DAGs        |
| Python validation      | Great Expectations  |
| S3 folder structure    | Data lake patterns  |

## Udemy Course

👉 [Spec-Driven AI Development: Data Platform Architecture](#)

## License

[Choose your license]
