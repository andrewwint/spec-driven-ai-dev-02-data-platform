# Module 1: Entering an Unfamiliar Domain

**Duration:** 90 minutes

**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 1.0: 📖 Course 1 Refresher — What Carries Forward (10 min)

**Concept:** Quick review of the patterns you'll build on.

**From Course 1, you have:**

| Pattern              | How It Applies Here                                                            |
| -------------------- | ------------------------------------------------------------------------------ |
| DARE Model           | D = schema validation; A = transformation logic; R = quality gates; E = alerts |
| `SKILL.md` format    | Same format, new agents for data work                                          |
| Proposal pattern     | Data transformation proposals before coding                                    |
| HISTORY.md           | Agent memory continues across sessions                                         |
| Makefile conventions | `make validate`, `make transform`, `make deploy`                               |

**The throughline continues:**

> _"Manage the LLM's context window like you manage your own attention."_

In Course 1, context was code and documentation. In Course 2, context is **data** — schemas, expectations, and lineage.

> 💡 **Progressive Disclosure:** Don't dump everything upfront. Deliver instructions to agents in stages — when they're relevant. A well-designed workflow progressively discloses context. **We'll practice this pattern throughout the course.**
> _See: [Delivering Instructions to AI Models](https://blog.huikang.dev/2025/10/20/delivering-ai-instructions.html)_

**Discussion:** What's different about data context vs. code context? Why might agents need different information to work with data effectively?

---

## Lesson 1.1: 📖 The Big Picture — Why Data Platforms Exist (15 min)

**Concept:** Before building a data pipeline, understand WHY organizations need them.

**Two Worlds of Data:**

```
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                           │
│            (Where your apps run — data lives months to years)    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   E-commerce Site     Payment System      CRM         Inventory  │
│   ───────────────     ──────────────      ───         ─────────  │
│   • Shopping carts    • Real-time auth    • Leads     • Stock    │
│   • User sessions     • Fraud checks      • Deals     • Orders   │
│   • Product views     • Transactions      • Contacts  • Shipments│
│                                                                  │
│   GOAL: Fast operations, current state, "good enough" data       │
│   RETENTION: Months to a few years                               │
│   QUALITY: Optimized for speed, not accuracy                     │
│                                                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼  Data flows DOWN (often with quality issues)
                         │
┌────────────────────────┴────────────────────────────────────────┐
│                       DATA PLATFORM                              │
│            (Organizational memory — data lives years to decades) │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Raw Zone             Cleaned Zone           Features / Reporting
│   ────────             ────────────           ──────────────────
│   • Ingest as-is       • Validated            • ML-ready datasets
│   • Keep everything    • Standardized         • Accurate reports
│   • Audit trail        • Deduplicated         • Business insights
│                                                                  │
│   GOAL: Accurate historical record, trustworthy data for decisions
│   RETENTION: Years to decades (regulatory, analytics, ML training)
│   QUALITY: Must be reliable — decisions depend on it
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Why Can't Applications Just Keep Good Data?**

Applications are optimized for **speed and user experience**, not data quality:

| Application Priority               | Data Platform Priority          |
| ---------------------------------- | ------------------------------- |
| "Process this transaction NOW"     | "Is this transaction accurate?" |
| "Show the user something fast"     | "What's the complete picture?"  |
| "Handle this edge case gracefully" | "Document every edge case"      |
| "Keep the system running"          | "Keep the history intact"       |

**Real-World Scenarios:**

**Scenario 1: Product Catalog Integration**

An e-commerce company receives product data from 50 different vendors:

- Vendor A sends XML files daily
- Vendor B sends CSV via SFTP weekly
- Vendor C has an API that returns JSON

Each vendor has different formats, field names, and quality issues. The application needs ONE clean product catalog. The data platform:

- Ingests all formats (raw zone)
- Standardizes and deduplicates (cleaned zone)
- Provides clean data for the e-commerce site to use

**Scenario 2: Fraud Detection Training**

A payment company needs to train an ML model to detect fraud:

- Transaction logs have mislabeled outcomes (fraud marked as legitimate)
- Some transactions were reversed days later
- System outages caused missing records

The model can only be as good as its training data. The data platform:

- Collects all transaction outcomes over time
- Reconciles reversals and corrections
- Builds a clean, labeled dataset for ML training (Course 3 preview!)

**Scenario 3: Financial Reporting**

The CFO needs accurate quarterly revenue numbers:

- Customer returned $50,000 of products after the quarter closed
- A sales rep entered a $10,000 order as $100,000 (typo)
- An AI agent auto-categorized expenses incorrectly

Raw application data would show wrong numbers. The data platform:

- Applies business rules for revenue recognition
- Validates against expected ranges
- Flags anomalies for human review
- Produces trustworthy reports

**The Pattern Across All Scenarios:**

```
Application Data (messy) → Data Platform (clean) → Decisions (trustworthy)
```

**Discussion:** Think about data you've worked with. Where did the quality issues come from? How were they discovered?

---

## Lesson 1.2: 📖 The Challenge — Working Outside Your Expertise (15 min)

**Concept:** Most developers will work in domains they're not experts in. AI changes how we approach this.

**The Traditional Approach:**

```
1. Read documentation for days
2. Take tutorials
3. Make mistakes
4. Ask colleagues
5. Eventually become productive
```

**The Agent-Assisted Approach:**

```
1. Ask an Advisor agent to explain the domain
2. Have it identify key concepts and trade-offs
3. Use Explorer agents to examine real data
4. Build incrementally with validation gates
5. Become productive faster, with guardrails
```

**Key Insight:** You don't need to become an expert. You need to:

- Ask the right questions
- Understand the trade-offs
- Validate your work
- Know when to escalate

**Hands-on Activity:** Think of a domain you've had to learn quickly. What questions did you wish someone had answered upfront? What mistakes did you make that validation could have caught?

---

## Lesson 1.3: 📖 The Advisor Pattern — Teaching Without Doing (20 min)

**Concept:** Advisor agents help you learn without modifying your code. This is the NEW pattern in Course 2.

**Agent Type Review:**

| Type        | Role                      | Tools                | Can Modify? |
| ----------- | ------------------------- | -------------------- | ----------- |
| **Advisor** | Teaches, guides, explains | read, search, fetch  | ❌ No       |
| **Doer**    | Implements changes        | read, edit, terminal | ✅ Yes      |
| **Gate**    | Reviews, validates        | read, search         | ❌ No       |

**Why Advisors Can't Modify Files:**

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE SEPARATION PRINCIPLE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Advisor explains:          Doer implements:                    │
│   "You should validate       [Actually writes the                │
│    nulls before joining      validation code]                    │
│    tables because..."                                            │
│                                                                  │
│   WHY separate?                                                  │
│   • Advisor focuses on teaching, not syntax                      │
│   • You understand before code appears                           │
│   • Clear handoff moment: "Ready to implement?"                  │
│   • Prevents "magic code" you don't understand                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**The Handoff Chain:**

```
Human: "I need to build a data pipeline"
    ↓
Advisor: Explains concepts, identifies trade-offs
    ↓
Human: "I understand. Let's implement."
    ↓
Doer: Writes the code
    ↓
Gate: Validates the output
    ↓
Human: Approves or iterates
```

**Discussion:** When have you received code from AI that you didn't fully understand? How did that affect your confidence in deploying it?

---

## Lesson 1.4: 📖 Industry Context — Where dbt, Airflow, and Great Expectations Fit (15 min)

**Concept:** Honest framing about what we're teaching vs. what industry uses.

**We're Teaching Principles, Not Tools:**

> _"The goal isn't to learn our stack. It's to understand the thinking so you can adopt any stack."_

**dbt (Data Build Tool):**

- Industry standard for data warehouse transformations
- SQL-based, runs in Snowflake/BigQuery/Redshift
- Our Python validation → same thinking as dbt tests
- Our proposals → same thinking as dbt's `schema.yml`

**Airflow:**

- Industry standard for workflow orchestration
- DAGs define task dependencies
- Our Makefile targets → same thinking as Airflow operators
- When you need scheduling + monitoring, adopt Airflow

**Great Expectations:**

- Industry standard for data validation
- Rich expectation library, automatic documentation
- Our Python checks → same concepts, simpler syntax
- When you need enterprise validation, adopt GX

**Why We Don't Teach These Directly:**

| Reason                      | Explanation                                               |
| --------------------------- | --------------------------------------------------------- |
| Learning overhead           | Each tool is a course in itself                           |
| Infrastructure requirements | dbt needs a warehouse, Airflow needs deployment           |
| Principle focus             | Once you understand WHY, tools are implementation details |
| Portability                 | You might use different tools at your company             |

**Hands-on Activity:** If your company uses dbt or Airflow, note how the patterns we build map to what you already know.

---

## Lesson 1.5: 💻 Setting Up the Customer Data Pipeline (15 min)

**Concept:** Clone the starter repo and understand the structure.

**The Scenario:**

You're a developer asked to build a data pipeline for customer analytics. You're not a data engineer, but you have:

- AI agents to guide you
- Patterns from Course 1
- Sample data to work with

**Setup Steps:**

```bash
# Clone the Course 2 starter
git clone https://github.com/spec-driven-ai/course-2-data-platform.git
cd customer-data-pipeline

# Run setup (creates virtual environment, installs deps)
./setup.sh

# Verify setup
make help
make agents-check
```

**Sample Data Overview:**

The `data/raw/` folder contains sample customer data:

- `customers.csv` — Customer demographics
- `transactions.csv` — Purchase history
- `sessions.csv` — Website activity

[📸 Screenshot: Terminal showing `make help` output with data-specific targets]

**HISTORY.md Entry:**

```markdown
## 2025-XX-XX

### Session Start

- Beginning Course 2: Data Platform
- Starting from Course 1 foundation patterns
- Sample data loaded in data/raw/

### Context

- Not a data engineering expert
- Using data-advisor to navigate unfamiliar domain
- Goal: Clean data for ML pipeline (Course 3)
```

**Hands-on Activity:**

1. Run `make agents-check` to see available agents
2. Open `data/raw/customers.csv` — note any obvious data quality issues
3. Add your own session start entry to HISTORY.md

---

## Module 1 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── README.md
├── CHANGELOG.md
├── HISTORY.md                      # ✅ Updated with session start
├── AGENTS.md
├── Makefile                        # ✅ Verified with make help
├── .pre-commit-config.yaml
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── customers.csv           # ✅ Reviewed for quality issues
│   │   ├── transactions.csv
│   │   └── sessions.csv
│   ├── cleaned/
│   └── features/
└── skills/
    └── data-advisor.SKILL.md       # ✅ Present in starter
```

**Checkpoint:** `git checkout module-1-setup` to see reference implementation

---

## AgentSkills.io Alignment Note

This module references AI-assisted workflow patterns using AgentSkills.io terminology. The **Advisor** pattern described here maps to role-based skill definitions (`.SKILL.md` files) that separate teaching concerns (read-only exploration) from implementation concerns (file modifications). This separation is a core principle of the AgentSkills framework.
