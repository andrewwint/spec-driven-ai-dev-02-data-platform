# Course 2 Appendices & Reference

## Course 2 Wrap-Up (15 minutes)

### What You Built

```
customer-data-pipeline/
├── AGENTS.md               # 5 skills documented
├── HISTORY.md              # Your learning journey
├── notebooks/              # Exploration work
├── src/
│   ├── validators/         # Schema validation (D in DARE)
│   └── transformers/       # Cleaning logic (A in DARE)
├── docs/
│   └── proposals/          # Schema, deployment, MCP proposals
├── mcp/                    # Custom MCP server (ONE tool)
├── data/
│   ├── raw/                # Original data with issues
│   ├── cleaned/            # Validated, transformed data
│   └── features/           # Ready for Course 3
└── skills/                 # Your skill team
```

### What You Learned

| Concept               | Key Takeaway                                              |
| --------------------- | --------------------------------------------------------- |
| Advisor Pattern       | Separate teaching from doing                              |
| Schema Contracts      | Deterministic validation before transformation            |
| Handoff Chains        | Advisor → Explorer → Validator → Transformer → Reviewer   |
| Notebook → Production | Explore interactively, make informed deployment decisions |
| ROI Trade-offs        | Evaluate options, don't just copy solutions               |
| Focused Proposals     | One thing at a time prevents scope creep                  |
| MCP Integration       | Build ONE tool, use it, then iterate                      |
| Industry Context      | Our patterns transfer to dbt, Airflow, GX                 |

### Progress Toward Series Capstone

By the end of the 5-course series, you'll have a **Production-Ready System** with skill-assisted SDLC. Here's your progress:

| Capstone Goal            | Course 1 ✅                    | Course 2 ✅                               | Courses 3-5                           |
| ------------------------ | ------------------------------ | ----------------------------------------- | ------------------------------------- |
| **Specialized Skills**   | verifier, reviewer, translator | Advisor, Explorer, Validator, Transformer | Planner, Builder, Historian           |
| **Production Artifacts** | Hello World pipeline           | Data pipeline + deployment proposal       | APIs, ML models, CI/CD                |
| **Reusable Templates**   | SKILL.md, proposals           | Schema contracts, MCP server              | API specs, deployment playbooks       |
| **Practical Judgment**   | When not to use AI             | When to use Advisor vs. jump to code      | Model selection, deployment decisions |

### Your Skill Portfolio So Far

```
Course 1 Skills:        Course 2 Skills:
├── verifier            ├── data-advisor      ← NEW TYPE (Advisor)
├── reviewer            ├── data-explorer
├── spanish-translator  ├── schema-validator
└── french-translator   ├── transformer
                        └── reviewer
```

**Pattern Evolution:**

- Course 1: Doer + Gate skills for code
- Course 2: **Advisor** + Doer + Gate skills for unfamiliar domains
- Course 3+: Research + Planner skills for complex workflows

### HISTORY.md Final Entry

```markdown
## Course 2 Complete

### What I Learned

- Advisor pattern for unfamiliar domains
- Schema contracts as DARE's "D"
- Multi-skill workflows for data
- MCP for pipeline tooling

### Ready for Course 3

- Clean data in data/cleaned/
- Validation patterns established
- Skill team ready for ML work
- MCP server for pipeline status
```

**Discussion:** What was the most valuable thing you learned? How will you apply the Advisor pattern in your own work?

---

## Appendix A: Quick Reference Cards

### The Advisor Conversation Pattern

```
1. ORIENT  — "I'm building X, working with Y"
2. ASK     — Specific question about concept/trade-off
3. UNDERSTAND — Ask clarifying questions
4. DECIDE  — State your chosen approach
5. HANDOFF — Move to implementation
```

### Course 2 Skill Team

| Skill            | Type    | Tools                    | Purpose             |
| ---------------- | ------- | ------------------------ | ------------------- |
| data-advisor     | Advisor | read, search, fetch      | Teaches concepts    |
| data-explorer    | Doer    | read, terminal, search   | Profiles data       |
| schema-validator | Gate    | read, search             | Validates contracts |
| transformer      | Doer    | read, edit, terminal     | Writes code         |
| reviewer         | Gate    | read, search, githubRepo | Reviews changes     |

### DARE for Data

| Letter | Data Application                                     |
| ------ | ---------------------------------------------------- |
| **D**  | Schema validation, null checks, format checks        |
| **A**  | Transformation logic, feature engineering            |
| **R**  | Schema-validator, reviewer skills                    |
| **E**  | Quality threshold alerts (>5% nulls, any duplicates) |

### Schema Contract Checklist

```
For each column:
- [ ] Name and description
- [ ] Data type
- [ ] Required or optional
- [ ] Validation rules
- [ ] Null handling
- [ ] Edge cases
```

### Focused Proposal Checklist

```
Before submitting a proposal, verify:
- [ ] Does ONE thing only
- [ ] "Not included" section prevents scope creep
- [ ] Success criteria are simple to verify
- [ ] Can be implemented in one session
- [ ] Reviewer can evaluate in 5 minutes
```

### Scope Creep Warning Signs

| Phrase                        | What to Do          |
| ----------------------------- | ------------------- |
| "While we're at it..."        | Stop. New proposal. |
| "It would be easy to also..." | Stop. New proposal. |
| "We might as well..."         | Stop. New proposal. |
| "And then we could..."        | Stop. New proposal. |

### Progressive Disclosure — Instruction Delivery Methods

Based on [Delivering Instructions to AI Models](https://blog.huikang.dev/2025/10/20/delivering-ai-instructions.html)

| Method                 | Example in This Course           | When to Use                       |
| ---------------------- | -------------------------------- | --------------------------------- |
| **Loaded upfront**     | CLAUDE.md basics                 | Rarely — avoid bloating           |
| **Provided by user**   | Focused prompts to Advisor       | When asking for specific guidance |
| **Always injected**    | Safety gates in skills           | Critical guardrails only          |
| **Decided to be read** | HISTORY.md, schema contracts     | Context that varies by task       |
| **Discovered**         | Explorer finds patterns in data  | Let skills learn from reality     |
| **Triggered**          | Pre-commit hooks, Makefile       | Deterministic conditions          |
| **Given in feedback**  | Test failures, validation errors | Let the system guide fixes        |

---

## Appendix B: Skill File Templates

### Advisor Template

```markdown
---
name: [domain]-advisor
description: Explains [domain] concepts (read-only)
tools: ['read', 'search', 'fetch']
handoffs:
  - label: Ready to Explore
    agent: [domain]-explorer
    send: false
  - label: Ready to Implement
    agent: [doer-skill]
    send: false
---

# [Domain] Advisor Skill

You teach [domain] concepts without modifying files.

## Teaching Approach

- Start with WHY before HOW
- Use analogies to familiar concepts
- Identify common pitfalls
- Suggest what to validate

## Rules

- ❌ CANNOT edit files
- ❌ CANNOT run terminal
- ✅ CAN read and explain
- ✅ MUST suggest handoff when ready
```

### Gate Template

```markdown
---
name: [purpose]-validator
description: Validates [what] (read-only)
tools: ['read', 'search']
handoffs:
  - label: Approved
    agent: [next-skill]
    send: false
  - label: Issues Found
    agent: [advisor]
    send: false
---

# [Purpose] Validator Skill

You validate [what] without modifying files.

## Validation Checklist

- [ ] Check 1
- [ ] Check 2
- [ ] Check 3

## Rules

- ❌ CANNOT edit files
- ✅ CAN read and search
- ✅ MUST be specific about issues
```

---

## Appendix C: Troubleshooting Guide

### Advisor Giving Code Instead of Teaching

**Symptom:** Advisor writes implementation code

**Fix:** Reinforce in skill instructions:

```markdown
## Rules

- ❌ NEVER write implementation code
- ✅ Can write pseudocode or examples
- ✅ Must explain concepts first
```

### Explorer Not Running Commands

**Symptom:** Explorer describes what to run but doesn't run it

**Fix:** Ensure `terminal` is in tools:

```yaml
tools: ["read", "terminal", "search"]
```

### Transformer Not Following Schema Contract

**Symptom:** Generated code doesn't match schema rules

**Fix:** Add explicit instruction:

```markdown
## Before Writing Code

1. Read the schema contract in docs/proposals/
2. Quote the rule you're implementing in the docstring
```

### Validation Passing When It Should Fail

**Symptom:** Invalid data passes validation

**Fix:**

1. Check threshold values
2. Add test with known-bad data
3. Review validation logic

### MCP Server Not Connecting

**Symptom:** Tools don't appear in Copilot

**Fix:**

1. Verify server runs standalone: `python mcp/data_pipeline_server.py`
2. Check `.vscode/mcp.json` is valid JSON
3. Reload VS Code window
4. Check Output panel for MCP errors

### Makefile Target Not Found

**Symptom:** `make: *** No rule to make target`

**Fix:**

1. Verify indentation uses TABS not spaces
2. Check target name spelling
3. Run `make help` to see available targets

### Pre-commit Hook Fails

**Symptom:** Commit blocked by hook

**Fix:**

1. Read the error message — it tells you which hook failed
2. Run `pre-commit run --all-files` to see details
3. Fix the issue or temporarily skip: `git commit --no-verify`

---

## Appendix D: Glossary (Course 2 Additions)

| Term                      | Definition                                                                                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Application Layer**     | Where business operations happen — e-commerce sites, payment systems, CRMs. Optimizes for speed and current state. Data quality is "good enough for now."         |
| **Data Platform**         | Organizational memory — collects, cleans, and prepares data for reporting and ML. Optimizes for accuracy and historical record. Data quality must be trustworthy. |
| **Operational Data**      | Short-lived data from applications (months to years). Supports transactions and current operations.                                                               |
| **Analytical Data**       | Long-lived data in the data platform (years to decades). Supports reporting, ML training, and business decisions.                                                 |
| **Advisor Skill**         | Skill that teaches without modifying files (new in Course 2)                                                                                                      |
| **Schema Contract**       | Document defining expected data structure and validation rules                                                                                                    |
| **Data Lake**             | Storage repository organized in zones (raw → cleaned → features)                                                                                                  |
| **Data Lineage**          | Tracking where data comes from and how it's transformed                                                                                                           |
| **Validation Gate**       | Checkpoint that verifies data meets expectations                                                                                                                  |
| **Escalation Threshold**  | Level at which issues trigger alerts or stop processing                                                                                                           |
| **Feature Engineering**   | Creating ML-ready variables from raw data (Course 3 topic)                                                                                                        |
| **Referential Integrity** | Ensuring relationships between data are valid (e.g., every transaction has a valid customer)                                                                      |
| **Orphan Record**         | A record that references another record that doesn't exist                                                                                                        |
| **MCP Server**            | Custom tool server that extends AI skill capabilities                                                                                                             |

---

_Course 2 Complete. Proceed to Course 3: ML Pipelines when ready._
