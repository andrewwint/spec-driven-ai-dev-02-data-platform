# Module 6: From Notebook to Production

**Duration:** 75 minutes
**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 6.0: 📖 The Productionization Decision (15 min)

**Concept:** You have working transformation code in notebooks. Now what? This is where the Advisor pattern truly shines.

**The Situation:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOU ARE HERE                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✅ Exploration complete (notebooks work)                       │
│   ✅ Schema contracts defined                                    │
│   ✅ Validation code tested                                      │
│   ✅ Transformation code tested                                  │
│                                                                  │
│   ❓ "How do I run this automatically in production?"            │
│                                                                  │
│   This question has MANY answers:                                │
│   • AWS Lambda          • Airflow DAG                            │
│   • Docker container    • dbt Cloud                              │
│   • Kubernetes job      • Simple cron                            │
│   • Prefect flow        • GitHub Actions                         │
│                                                                  │
│   The RIGHT answer depends on YOUR context.                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Why This Is an Advisor Moment:**

You likely DON'T have deep expertise in all deployment options. Instead of:

- Googling for hours
- Picking the first tutorial you find
- Over-engineering with Kubernetes when cron would work

You can use the Advisor to:

- Understand your options
- Evaluate trade-offs for YOUR context
- Make an informed decision
- Document the rationale

**Discussion:** What deployment approach would you instinctively reach for? Why? What assumptions are baked into that choice?

---

## Lesson 6.1: 💻 Asking the Advisor About Deployment Options (25 min)

**Concept:** Use the data-advisor to explore productionization options before committing to an approach.

**The Conversation:**

```
@data-advisor I have transformation code working in a Jupyter notebook.
It cleans customer data (about 10MB) and outputs to data/cleaned/.

I need to run this automatically when new data arrives.
What are my options and what trade-offs should I consider?
```

**What a Good Advisor Response Includes:**

The advisor should explain multiple options with honest trade-offs:

```markdown
### Deployment Options for Your Data Pipeline

**Option 1: AWS Lambda**

- **Best for:** Event-driven, small-to-medium data (<500MB), serverless
- **Pros:** No servers to manage, pay-per-use, scales automatically
- **Cons:** 15-min timeout, cold starts, AWS lock-in
- **Complexity:** Medium (need to learn Lambda, S3 triggers, IAM)

**Option 2: Containerized Job (Docker + ECS/Kubernetes)**

- **Best for:** Larger data, complex dependencies, portability
- **Pros:** Runs anywhere, no timeout limits, full control
- **Cons:** More infrastructure to manage, need container expertise
- **Complexity:** High

**Option 3: Simple Cron Job**

- **Best for:** Scheduled runs, simple infrastructure, small teams
- **Pros:** Dead simple, runs on any Linux server, easy to debug
- **Cons:** Not event-driven, single point of failure
- **Complexity:** Low

**Option 4: Workflow Orchestrator (Airflow/Prefect)**

- **Best for:** Complex multi-step pipelines, dependencies between jobs
- **Pros:** Visualization, retries, monitoring built-in
- **Cons:** Significant setup overhead, overkill for simple pipelines
- **Complexity:** High

**Option 5: dbt Cloud**

- **Best for:** SQL-based transformations in a data warehouse
- **Pros:** Industry standard, built-in testing, documentation
- **Cons:** Requires data warehouse, SQL-centric, subscription cost
- **Complexity:** Medium (if you have a warehouse)

**Questions to Help You Decide:**

1. How often does data arrive? (Event-driven vs. scheduled)
2. How large is the data? (Affects timeout/memory constraints)
3. What's your team's expertise? (AWS, Docker, Airflow?)
4. What infrastructure do you already have?
5. How critical is this pipeline? (Affects monitoring needs)
```

**Follow-up Questions to Ask:**

```
@data-advisor
- My team has no AWS experience but we use Docker daily
- Data arrives once per day via SFTP, about 10MB
- We have a Linux server that runs other cron jobs
- This is for internal analytics, not customer-facing

Given this context, what would you recommend?
```

**Hands-on Activity:**

1. Start a conversation with `@data-advisor`
2. Describe YOUR actual context (or use the sample scenario)
3. Ask follow-up questions until you understand the trade-offs
4. Document the options and your thinking in HISTORY.md

[📸 Screenshot: Advisor conversation exploring deployment options]

---

## Lesson 6.2: 📖💻 ROI Trade-off Analysis (20 min)

**Concept:** Use the proposal template's ROI section to make a defensible decision.

**The ROI Framework:**

Every deployment decision has costs and benefits. The Advisor can help you think through:

| Factor                  | Questions to Consider                         |
| ----------------------- | --------------------------------------------- |
| **Implementation Time** | How long to set up? Learning curve?           |
| **Operational Cost**    | Infrastructure cost? Maintenance burden?      |
| **Team Expertise**      | Do we have the skills? Training needed?       |
| **Scalability**         | Will this grow with us? Migration cost later? |
| **Reliability**         | Monitoring? Alerting? Recovery?               |
| **Portability**         | Vendor lock-in? Can we move later?            |

**Creating a Decision Matrix:**

Ask the advisor to help build a comparison:

```
@data-advisor Can you help me create a decision matrix comparing:
1. AWS Lambda
2. Docker + cron on our existing server
3. GitHub Actions (we already use GitHub)

Criteria: implementation time, monthly cost, team expertise required,
reliability, and flexibility to change later.
```

**Sample Decision Matrix Output:**

| Criteria         | Lambda               | Docker + Cron          | GitHub Actions          |
| ---------------- | -------------------- | ---------------------- | ----------------------- |
| Implementation   | 8 hours              | 2 hours                | 4 hours                 |
| Monthly Cost     | ~$5                  | $0 (existing)          | $0 (free tier)          |
| Expertise Needed | AWS, IAM, S3         | Docker (have)          | GitHub (have)           |
| Reliability      | High (managed)       | Medium (single server) | High (managed)          |
| Flexibility      | Medium (AWS lock-in) | High (portable)        | Medium (GitHub lock-in) |

**The "Don't Over-Engineer" Check:**

```
@data-advisor I'm tempted to use Kubernetes because it seems
"more professional." But we're a team of 3 and this is our
first data pipeline. Am I over-engineering?
```

A good advisor will be honest:

> "Yes, Kubernetes is likely over-engineering for your situation.
> The operational overhead of managing a K8s cluster far exceeds
> the benefits for a single 10MB daily pipeline. Consider starting
> with the simplest solution that works (cron or GitHub Actions),
> and migrate to more complex infrastructure only when you hit
> actual limitations."

**Hands-on Activity:**

1. Create a decision matrix for your deployment options
2. Ask the advisor to challenge your assumptions
3. Document your analysis in the proposal

---

## Lesson 6.3: 📖💻 Creating a Deployment Proposal (20 min)

**Concept:** Document your decision with rationale, not just the implementation.

**The Deployment Proposal:**

Use the proposal template to document your productionization decision:

```markdown
# Proposal 002: Data Pipeline Deployment Approach

## Summary

Deploy the customer data transformation pipeline using [chosen approach]
based on team expertise, infrastructure constraints, and ROI analysis.

## Motivation

We have working transformation code in notebooks. We need to run this
automatically when new data arrives (daily via SFTP).

## Options Evaluated

| Option         | Pros                      | Cons                              | Verdict                    |
| -------------- | ------------------------- | --------------------------------- | -------------------------- |
| AWS Lambda     | Serverless, scalable      | Team has no AWS experience        | ❌ Too much learning curve |
| Docker + Cron  | Team knows Docker, simple | Single point of failure           | ✅ **Selected**            |
| GitHub Actions | Free, familiar            | Less flexible for data work       | ❌ Not ideal fit           |
| Airflow        | Industry standard         | Massive overkill for one pipeline | ❌ Over-engineering        |

## Decision: Docker + Cron

**Rationale:**

- Team already uses Docker daily (no learning curve)
- Existing Linux server with other cron jobs (no new infrastructure)
- Simple to debug and modify
- Can migrate to Airflow later if we add more pipelines

## ROI Analysis

| Metric                       | Estimate                    |
| ---------------------------- | --------------------------- |
| Implementation time          | 2 hours                     |
| Monthly operational cost     | $0 (existing server)        |
| Time to first production run | 1 day                       |
| Migration cost if we outgrow | ~8 hours to move to Airflow |

## DARE Application

| Letter | This Deployment                            |
| ------ | ------------------------------------------ |
| **D**  | Cron schedule is deterministic             |
| **A**  | Transformation logic (already built)       |
| **R**  | Log review, output validation              |
| **E**  | Email alert on failure, Slack notification |

## Implementation Tasks

- [ ] Create Dockerfile for transformation
- [ ] Write cron job entry
- [ ] Set up log rotation
- [ ] Configure failure alerts
- [ ] Document in runbook

## Success Criteria

- [ ] Pipeline runs daily without manual intervention
- [ ] Failures trigger alerts within 5 minutes
- [ ] Logs retained for 30 days
- [ ] Runbook enables any team member to debug

## Approval

- [ ] **Reviewed by:** [reviewer skill]
- [ ] **Approved on:** YYYY-MM-DD
```

**Key Insight:** The proposal documents the DECISION, not the implementation details. The actual Dockerfile and cron setup will be created by the transformer skill—but only after the approach is approved.

**Hands-on Activity:**

1. Create `docs/proposals/002-deployment-approach.md`
2. Fill in YOUR chosen approach with honest rationale
3. Have `@reviewer` validate the proposal makes sense
4. This becomes your blueprint for implementation

---

## Lesson 6.4: 📖 Connecting to Course 3 (15 min)

**Concept:** What Course 3 receives from your work here.

**What You're Handing Off:**

| Asset               | Location               | Course 3 Use        |
| ------------------- | ---------------------- | ------------------- |
| Clean data          | `data/cleaned/`        | ML training input   |
| Schema contracts    | `docs/proposals/`      | Data expectations   |
| Validation patterns | `src/validators/`      | Training data gates |
| Deployment proposal | `docs/proposals/002-*` | Production patterns |
| Advisor pattern     | `skills/`              | ML-advisor skill    |

**The Feature Engineering Preview:**

Course 3 starts with feature engineering—creating ML-ready features from clean data.

```python
# Course 3 will add:
def engineer_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create features for customer churn prediction."""
    return (
        df
        .pipe(add_tenure_days)
        .pipe(add_transaction_count)
        .pipe(add_avg_order_value)
        .pipe(add_session_frequency)
    )
```

**Your foundation enables:**

- Reliable input data (validated)
- Clear expectations (schema contracts)
- Repeatable process (Makefile + your deployment approach)
- Decision-making patterns (ROI analysis, proposals)
- Skill patterns that transfer (Advisor for ML concepts)

**The Bigger Picture:**

```
Course 2 teaches:              Course 3 applies:
├── Advisor for data concepts  ├── Advisor for ML concepts
├── ROI trade-off analysis     ├── Model selection trade-offs
├── Deployment proposals       ├── Training pipeline proposals
└── "Don't over-engineer"      └── "Don't over-fit"
```

---

## Module 6 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── README.md
├── CHANGELOG.md
├── HISTORY.md                      # ✅ Includes deployment decision rationale
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
│   ├── cleaned/                    # ✅ Contains cleaned data
│   └── features/
├── docs/
│   ├── proposals/
│   │   ├── 001-schema-contract.md
│   │   └── 002-deployment-approach.md  # ✅ Created with ROI analysis
│   ├── runbooks/
│   └── playbooks/
└── skills/
    ├── data-advisor.SKILL.md
    ├── data-explorer.SKILL.md
    ├── schema-validator.SKILL.md
    ├── transformer.SKILL.md
    └── reviewer.SKILL.md       # ✅ All 5 skills
```

**Key Deliverable:** A deployment proposal that documents your decision with rationale—not just "we're using Lambda" but WHY you chose that approach.

**Checkpoint:** `git checkout module-6-production` to see reference implementation

---

## Alignment Note: AgentSkills.io Terminology

This module demonstrates the practical application of skill-driven decision making. The data-advisor and reviewer skills guide productionization decisions through the Advisor Pattern—a framework for navigating unfamiliar domains without implementing prematurely. The proposal structure (docs/proposals/002-deployment-approach.md) becomes the specification that the transformer skill implements, exemplifying the skill handoff pattern central to AgentSkills.io workflows.
