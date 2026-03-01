# Module 3: Data Exploration with Agents

**Duration:** 90 minutes

**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 3.0: 📖💻 The Data Explorer Agent (20 min)

**Concept:** Using an agent to profile and understand data you've never seen.

**The data-explorer.SKILL.md:**

````markdown
---
name: data-explorer
description: Analyzes data, runs profiling, identifies quality issues
tools: ["read", "terminal", "search"]
handoffs:
  - label: Ask Advisor
    agent: data-advisor
    prompt: I have questions about what I'm seeing in the data.
    send: false
  - label: Create Schema Proposal
    agent: schema-validator
    prompt: Based on exploration, I'm ready to define the schema contract.
    send: false
---

# Data Explorer Agent

You analyze data files and identify quality issues, patterns, and
anomalies. You run profiling code but don't write transformation logic.

## Core Responsibilities

1. **Profile** data files (row counts, column types, distributions)
2. **Identify** quality issues (nulls, duplicates, outliers)
3. **Summarize** findings in clear reports
4. **Recommend** what to validate in schema contracts

## Tools You Use

You have `terminal` access to run Python commands:

```python
# Quick profiling
import pandas as pd
df = pd.read_csv('data/raw/customers.csv')
print(df.info())
print(df.describe())
print(df.isnull().sum())
```
````

## Output Format

### Data Profile: [filename]

**Shape:** X rows, Y columns

**Columns:**
| Column | Type | Nulls | Unique | Sample Values |
|--------|------|-------|--------|---------------|
| col1 | str | 0 | 100 | a, b, c |

**Quality Issues Found:**

- [ ] Issue 1
- [ ] Issue 2

**Recommendations:**

- Validate X in schema
- Consider Y transformation

```

**Discussion:** Why does the explorer have `terminal` but not `edit`? It runs analysis but shouldn't modify data.

> 💡 **Progressive Disclosure:** The explorer "discovers" instructions from your data — it learns patterns, formats, and issues from what's already there. You don't need to tell it every possible data issue; it finds them by examining the actual data.

---

## Lesson 3.1: 💻 Exploring the Customer Data (30 min)

**Concept:** Hands-on exploration of the sample dataset using the data-explorer agent.

**The Conversation:**

```
@data-explorer Please profile the customer data in data/raw/customers.csv

I want to understand:
1. What columns exist and their types
2. How much missing data there is
3. Any obvious quality issues
```

[📸 Screenshot: data-explorer running pandas profiling in terminal]

**What the Explorer Finds:**

Typical issues in sample customer data:
- Null values in `email` column (15%)
- Duplicate `customer_id` entries (3 rows)
- Inconsistent date formats in `signup_date`
- Invalid values in `age` column (negative numbers, 999)

**Documenting Findings:**

The explorer should output findings that become input for the schema contract:

```markdown
### Exploration: customers.csv

**Quality Issues:**
1. 15% null emails — decide: required or optional?
2. 3 duplicate customer_ids — must be unique
3. Mixed date formats: "2024-01-15" and "01/15/2024"
4. Invalid ages: -5, 999 — need range validation

**Schema Recommendations:**
- customer_id: required, unique
- email: optional (or required with cleaning)
- signup_date: required, ISO format
- age: required, range 0-120
```

**Hands-on Activity:**

1. Start a conversation with `@data-explorer`
2. Profile all three data files (customers, transactions, sessions)
3. Document findings in HISTORY.md
4. Note which issues need transformation vs. schema validation

---

## Lesson 3.2: 📖💻 Notebooks for Deeper Exploration (25 min)

**Concept:** When to use notebooks vs. agent conversations for data work.

**Notebooks vs. Agent Chat:**

| Use Notebooks When    | Use Agent Chat When |
| --------------------- | ------------------- |
| Iterative exploration | Quick questions     |
| Visualizations needed | Profiling commands  |
| Complex analysis      | Explaining findings |
| Sharing with team     | Making decisions    |

**Creating an Exploration Notebook:**

```
@data-explorer Can you create a Jupyter notebook for exploring
the customer data? Include:
- Basic profiling
- Null analysis
- Distribution plots
- Quality issue summary
```

[📸 Screenshot: SageMaker notebook with data visualizations]

**Notebook Structure:**

```
notebooks/
└── 01-data-exploration.ipynb
    ├── Cell 1: Load data
    ├── Cell 2: Basic profiling
    ├── Cell 3: Null analysis
    ├── Cell 4: Distribution plots
    └── Cell 5: Quality summary
```

**Hands-on Activity:**

1. Have data-explorer create the exploration notebook
2. Run the notebook in VS Code or SageMaker
3. Add observations to HISTORY.md

**The Notebook → Production Pattern:**

> _Explore in notebooks. Productionize when ready._

This pattern continues throughout the course. Notebooks are for understanding; production deployment is for automation. Module 6 will help you decide HOW to productionize.

---

## Lesson 3.3: 📖💻 From Exploration to Proposal (15 min)

**Concept:** Translating exploration findings into a formal proposal.

**The Proposal Pattern (from Course 1):**

Proposals document decisions BEFORE implementation. For data, this means:

```markdown
# Proposal 001: Customer Data Schema Contract

## Summary

Define schema validation rules for customer data based on exploration findings.

## Motivation

Exploration revealed quality issues that must be validated before transformation.

## Proposed Schema

### customers.csv

| Column      | Type    | Required | Validation              |
| ----------- | ------- | -------- | ----------------------- |
| customer_id | string  | Yes      | Unique, non-empty       |
| email       | string  | No       | Valid format if present |
| signup_date | date    | Yes      | ISO 8601 format         |
| age         | integer | Yes      | Range 0-120             |

## DARE Application

| Letter | This Proposal                      |
| ------ | ---------------------------------- |
| D      | Schema validation (deterministic)  |
| A      | Transformation logic (AI-assisted) |
| R      | Schema-validator reviews contract  |
| E      | Alert on >5% validation failures   |
```

**Hands-on Activity:**

1. Use the handoff: "Create Schema Proposal"
2. Review the generated proposal
3. Adjust based on your exploration findings
4. Commit to `docs/proposals/001-schema-contract.md`

---

## Module 3 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── ...
├── HISTORY.md                      # ✅ Updated with exploration findings
├── notebooks/
│   └── 01-data-exploration.ipynb   # ✅ Created with profiling
├── docs/
│   └── proposals/
│       └── 001-schema-contract.md  # ✅ Created from exploration
└── skills/
    └── ...                          # All 5 agents present
```

**Checkpoint:** `git checkout module-3-exploration` to see reference implementation

---

## AgentSkills.io Alignment Note

In this module, the data-explorer skill demonstrates the "Doer" role in AgentSkills.io—agents with permission to execute terminal commands (`terminal` tool) but restricted from modifying source code (`edit` tool restricted). This selective tool access pattern is a core principle of AgentSkills.io: each skill definition precisely controls what an agent can and cannot do, enabling safe agent composition in complex workflows.
