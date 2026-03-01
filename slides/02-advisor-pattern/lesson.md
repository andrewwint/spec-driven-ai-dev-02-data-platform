# Module 2: The Data Advisor Agent

**Duration:** 90 minutes

**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 2.0: 📖💻 Designing the Data Advisor (20 min)

**Concept:** Building an Advisor agent that teaches without implementing.

**What Makes a Good Advisor?**

| Characteristic      | Why It Matters                      |
| ------------------- | ----------------------------------- |
| Read-only access    | Can't accidentally modify your work |
| Domain knowledge    | Explains concepts you don't know    |
| Trade-off awareness | Helps you make informed decisions   |
| Handoff clarity     | Knows when to pass to a Doer        |

**The data-advisor.SKILL.md:**

```markdown
---
name: data-advisor
description: Explains data concepts and guides decisions (read-only)
tools: ["read", "search", "fetch"]
handoffs:
  - label: Ready to Explore
    agent: data-explorer
    prompt: I understand the concepts. Let's explore the actual data.
    send: false
  - label: Ready to Implement
    agent: transformer
    prompt: I'm ready to implement. Please write the transformation code.
    send: false
---

# Data Advisor Agent

You are a data engineering advisor who helps developers navigate
unfamiliar data concepts. You teach and guide but NEVER modify files.

## Core Responsibilities

1. **Explain** data engineering concepts in practical terms
2. **Identify** trade-offs in data modeling decisions
3. **Suggest** approaches without writing code
4. **Recognize** when the human is ready to implement

## Teaching Approach

When explaining concepts:

- Start with WHY before HOW
- Use analogies to familiar programming concepts
- Identify common pitfalls
- Suggest what to validate

## Important Rules

- ❌ **CANNOT** edit files — you are read-only
- ❌ **CANNOT** run terminal commands
- ❌ **CANNOT** write code (only pseudocode/examples)
- ✅ **CAN** read project files to understand context
- ✅ **CAN** search for relevant patterns
- ✅ **CAN** explain trade-offs and recommendations
- ✅ **MUST** suggest handoff when ready to implement

## Domain Knowledge

You understand:

- Data lake organization (raw → cleaned → features)
- Schema validation and data contracts
- Common data quality issues
- Transformation patterns
- When to use different tools (pandas vs. SQL vs. Spark)

## Output Format

When teaching a concept:

### [Concept Name]

**What it is:** [Simple explanation]

**Why it matters:** [Practical impact]

**Common pitfalls:**

- [Pitfall 1]
- [Pitfall 2]

**What to validate:**

- [Check 1]
- [Check 2]

**Ready to implement?** Use "Ready to Explore" or "Ready to Implement" handoff.
```

**Discussion:** How is this different from the reviewer agent in Course 1? Both are read-only, but serve different purposes.

---

## Lesson 2.1: 💻 Using the Advisor — Asking Good Questions (25 min)

**Concept:** The quality of advisor output depends on the quality of your questions.

**Poor Questions vs. Good Questions:**

| Poor Question          | Good Question                                                                 |
| ---------------------- | ----------------------------------------------------------------------------- |
| "How do I clean data?" | "What should I check in customer data before joining with transactions?"      |
| "What's a schema?"     | "Why would I define a schema contract before writing transformation code?"    |
| "Is my data good?"     | "What are the most common data quality issues in customer demographics data?" |

**The ADVISOR Conversation Pattern:**

```
1. ORIENT — "I'm building X, working with Y data"
2. ASK — Specific question about concept or trade-off
3. UNDERSTAND — Ask clarifying questions
4. DECIDE — State your chosen approach
5. HANDOFF — Move to implementation
```

**Hands-on Activity: Your First Advisor Conversation**

Open Copilot Chat, select `data-advisor`, and try:

```
@data-advisor I'm building a customer analytics pipeline.
I have customer demographics, transactions, and session data.
I've never built a data pipeline before.

What are the key concepts I should understand before I start?
```

[📸 Screenshot: Copilot Chat showing data-advisor response with concept explanations]

**Follow-up Questions to Try:**

1. "What's the difference between raw, cleaned, and features folders?"
2. "What data quality issues should I check for in customer data?"
3. "How do I know when my data is 'clean enough'?"

**Document Your Learning:**

After the conversation, add to HISTORY.md:

```markdown
### Advisor Session: Data Pipeline Concepts

- Learned: raw → cleaned → features organization
- Learned: Common quality issues (nulls, duplicates, format inconsistency)
- Decision: Will validate schema before transformation
- Next: Explore actual data with data-explorer
```

> 💡 **Progressive Disclosure:** HISTORY.md is "instructions decided to be read." Future agents load this context when starting work — not every message. You're building institutional memory that arrives when relevant.

---

## Lesson 2.2: 📖💻 From Teaching to Doing — The Handoff Moment (20 min)

**Concept:** Recognizing when you're ready to move from learning to implementing.

**Signs You're Ready to Handoff:**

| Signal                           | What It Means                      |
| -------------------------------- | ---------------------------------- |
| You can explain the concept back | You understand, not just heard     |
| You know what to validate        | You can verify correctness         |
| You see the trade-offs           | You can make informed decisions    |
| You have a mental model          | You can debug when things go wrong |

**The Handoff Conversation:**

```
You: "So if I understand correctly, I should:
      1. Check for null values in required fields
      2. Validate email format
      3. Ensure customer_id is unique
      Is that right?"

Advisor: "Yes, those are the key validations. You're ready to
         explore the data. Use 'Ready to Explore' to switch
         to the data-explorer agent."
```

**Anti-pattern: Premature Handoff**

```
You: "Just tell me what code to write"

Advisor: "Before I hand off to the transformer, let me make
         sure you understand why we're doing each step..."
```

**The Advisor should resist premature handoffs** because:

- Code without understanding leads to debugging nightmares
- You won't know if the output is correct
- You can't maintain what you don't understand

**Hands-on Activity:** Practice the handoff:

1. Ask data-advisor about schema validation
2. Explain the concept back in your own words
3. When confident, use the "Ready to Explore" handoff button

[📸 Screenshot: Copilot showing handoff button options]

---

## Lesson 2.3: 💻 Understanding Your Agent Team (25 min)

**Concept:** All five agents are provided. Let's understand how they work together.

**The Course 2 Skill Team:**

| Agent                | Type    | Role                               | Tools                    | Model Tier |
| -------------------- | ------- | ---------------------------------- | ------------------------ | ---------- |
| **data-advisor**     | Advisor | Teaches concepts, guides decisions | read, search, fetch      | Balanced   |
| **data-explorer**    | Doer    | Analyzes data, runs profiling      | read, terminal, search   | Fast       |
| **schema-validator** | Gate    | Validates schemas (read-only)      | read, search             | Fast       |
| **transformer**      | Doer    | Writes transformation code         | read, edit, terminal     | Fast       |
| **reviewer**         | Gate    | Reviews changes (read-only)        | read, search, githubRepo | Balanced   |

**Model Tier Principle:** Use the cheapest model that can do the job.

- **Balanced** = Needs nuanced reasoning (teaching, reviewing trade-offs)
- **Fast** = Structured tasks with clear inputs/outputs (profiling, validating, transforming)

**The Workflow:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    COURSE 2 SKILL WORKFLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Human: "I need to build a data pipeline"                       │
│       │                                                          │
│       ▼                                                          │
│   ┌─────────────┐                                                │
│   │data-advisor │ ← Teaches concepts (read-only)                 │
│   └──────┬──────┘                                                │
│          │ "Ready to Explore"                                    │
│          ▼                                                       │
│   ┌──────────────┐                                               │
│   │data-explorer │ ← Profiles data, finds issues                 │
│   └──────┬───────┘                                               │
│          │ "Create Proposal"                                     │
│          ▼                                                       │
│   ┌─────────────────┐                                            │
│   │schema-validator │ ← Validates schema contract (read-only)    │
│   └────────┬────────┘                                            │
│            │ "Implement Transformations"                         │
│            ▼                                                     │
│   ┌─────────────┐                                                │
│   │ transformer │ ← Writes cleaning/transformation code          │
│   └──────┬──────┘                                                │
│          │ "Review Changes"                                      │
│          ▼                                                       │
│   ┌──────────┐                                                   │
│   │ reviewer │ ← Reviews changes (read-only)                     │
│   └────┬─────┘                                                   │
│        │                                                         │
│        ▼                                                         │
│   Human: Approves or requests changes                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Hands-on Activity:** Review and understand each agent:

1. Open each agent file in `skills/`
2. Note the tools each agent has (and doesn't have)
3. Read the handoff definitions — understand the workflow
4. Run `make agents-check` to verify all are present
5. Try a quick conversation with each agent to see how they respond

**Fine-tuning Opportunity:**

Each agent is ready to use, but you might want to customize:

- Add domain-specific knowledge (your company's data conventions)
- Adjust output formats to match your preferences
- Add project-specific context files to read

---

## Module 2 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── ...
├── HISTORY.md                      # ✅ Updated with advisor session notes
└── skills/
    ├── data-advisor.SKILL.md       # ✅ Understood and tested
    ├── data-explorer.SKILL.md      # ✅ Reviewed, ready to use
    ├── schema-validator.SKILL.md   # ✅ Reviewed, ready to use
    ├── transformer.SKILL.md        # ✅ Reviewed, ready to use
    └── reviewer.SKILL.md           # ✅ Reviewed, ready to use
```

**Note:** All agents are provided in the starter kit. Your task is to:

- Understand how each agent works
- Practice the handoff workflow
- Fine-tune agent instructions for your specific needs

**Verify:** `make agents-check` should list all 5 agents

**Checkpoint:** `git checkout module-2-advisor` to see reference implementation

---

## AgentSkills.io Alignment Note

This module heavily uses the AgentSkills.io skill definition framework. The Advisor pattern is implemented as a role-based skill (`.SKILL.md` file) that defines what an agent can and cannot do. The Advisor's read-only constraints are enforced through the `tools` specification, which is central to how AgentSkills.io manages AI agent permissions and capabilities. This structured approach ensures predictable, safe agent behavior across complex multi-agent workflows.
