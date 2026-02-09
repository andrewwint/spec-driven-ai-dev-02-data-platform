# AGENTS.md

> Human-readable documentation of the AI agents in this project.
> 
> For agent definitions, see `.github/agents/*.agent.md`

---

## Agent Philosophy

This project uses **spec-driven AI assistance** with the following principles:

1. **Context is Attention** — What you feed the agent determines what it can reason about
2. **DARE Model** — Deterministic first, AI for ambiguity, Review at boundaries, Escalate on failure
3. **Tool Restrictions** — Each agent has limited capabilities by design
4. **Handoffs** — Agents pass work to each other at defined boundaries

---

## Human-in-the-Loop Architecture

Humans own the **bookends**. AI assists in the middle.

| Phase | Human Engineer | Advisor Agent | Doer Agents | Gate Agents |
|-------|----------------|---------------|-------------|-------------|
| **Understand** | Ask questions | Explain concepts | | |
| **Explore** | Guide direction | | Profile data | |
| **Propose** | Approve design | | Draft schemas | Validate contracts |
| **Build** | Guide direction | | Write code | |
| **Validate** | Inspect output | | | Review changes |
| **Deploy** | Own release | | | |

---

## Agent Types

| Type | Role | Tools | Can Modify Files? |
|------|------|-------|-------------------|
| **Advisor** | Teaches, guides, explains | read, search, fetch | ❌ No |
| **Doer** | Implements changes | read, edit, terminal | ✅ Yes |
| **Gate** | Reviews, validates | read, search | ❌ No |

### Type Descriptions

**Advisor Agents** — Help navigate unfamiliar domains, explain concepts, suggest approaches. Cannot modify code—only guide. Hand off to Doer agents when ready to implement.

**Doer Agents** — Write and modify code, run commands in terminal, follow proposals and specs. Hand off to Gate agents for review.

**Gate Agents** — Read-only access, validate against specs/schemas/contracts, approve or reject changes, escalate issues to humans.

---

## Agent Team

| Agent | Type | Role | Tools | Model Tier | Status |
|-------|------|------|-------|------------|--------|
| **data-advisor** | Advisor | Teaches data concepts, guides decisions | read, search, fetch | Balanced | ✅ Ready |
| **data-explorer** | Doer | Profiles data, identifies quality issues | read, terminal, search | Fast | ✅ Ready |
| **schema-validator** | Gate | Validates schema contracts | read, search | Fast | ✅ Ready |
| **transformer** | Doer | Writes transformation code | read, edit, terminal | Fast | ✅ Ready |
| **reviewer** | Gate | Reviews code changes | read, search, githubRepo | Balanced | ✅ Ready |

**Model Tier Principle:** Use the cheapest model that can do the job.
- **Balanced** = Needs nuanced reasoning (teaching, reviewing trade-offs)
- **Fast** = Structured tasks with clear inputs/outputs (profiling, validating, transforming)

---

## Documentation Files

| File | Purpose | Updated By | Audience |
|------|---------|------------|----------|
| `CHANGELOG.md` | Version releases ("what shipped") | Human | End users |
| `HISTORY.md` | Project narrative, decisions ("what happened") | Agents + Human | Developers, AI |

### CHANGELOG.md — "What Shipped"

**Format:** [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

**Update when:** New version release, breaking changes, notable bug fixes

### HISTORY.md — "What Happened"

**Format:** Chronological freeform entries (agent memory)

**Update when:** Start of work session, decisions made, agent activity summaries

---

## Agent Memory Pattern

**Before starting work:**
> "Read HISTORY.md to understand prior context."

**After completing significant work:**
> "Append a summary to HISTORY.md."

This pattern solves context rot—agents can recover context from previous sessions.

---

## Handoff Pattern

```
Human: "I need to build a data pipeline"
    ↓
data-advisor: Explains concepts (read-only)
    ↓
Human: "I understand. Let's explore the data."
    ↓
data-explorer: Profiles data, finds issues
    ↓
Human: "Create a schema proposal"
    ↓
schema-validator: Reviews schema contract (read-only)
    ↓
Human: "Implement the transformations"
    ↓
transformer: Writes cleaning code
    ↓
reviewer: Reviews changes (read-only)
    ↓
Human: Approves or requests changes
```

---

## DARE Model in This Project

| Letter | Principle | This Project |
|--------|-----------|--------------|
| **D** | Deterministic First | Schema validation, null checks, format checks |
| **A** | AI for Ambiguity | Transformation logic, feature engineering |
| **R** | Review at Boundaries | schema-validator, reviewer agents |
| **E** | Escalate on Failure | Quality threshold alerts (>5% nulls, any duplicates) |

---

## Adding New Agents

1. Create `.github/agents/agent-name.agent.md`
2. Assign type: Advisor, Doer, or Gate
3. Define appropriate tool restrictions
4. Add handoffs to/from related agents
5. Update this AGENTS.md
6. Test the workflow end-to-end

---

*This AGENTS.md follows the spec-driven AI development methodology.*
