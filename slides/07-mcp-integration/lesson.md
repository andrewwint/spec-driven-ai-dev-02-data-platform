# Module 7: MCP Integration (60 minutes)

**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

**Prerequisites:** Familiarity with MCP concepts (introduced in Course 1)

### Lesson 7.0: 📖 Small Proposals, Big Results (10 min)

**Concept:** The same "context is attention" principle that applies to prompts also applies to proposals.

**The Bloated Proposal Anti-Pattern:**

```markdown
# Proposal: MCP Server for Data Pipeline

## Features

- Get validation status
- Profile any data file
- List all files in each stage
- Run transformations
- Check agent count
- Generate quality reports
- Send Slack notifications
- Trigger full pipeline
- AND compare datasets
- AND export to Excel
- AND...
```

**What's Wrong:**

- Too many features = unclear scope
- Hard to review = things slip through
- Long implementation = context rot
- If something breaks = hard to debug

> 💡 **Progressive Disclosure:** This bloated proposal is "loading everything upfront" — the exact anti-pattern we're avoiding. Just like you don't dump your entire system prompt into every message, you don't dump every possible feature into one proposal.

**The Focused Proposal Pattern:**

```markdown
# Proposal: MCP Tool — Validation Status Checker

## One Thing

Check if data passes schema validation and report issues.

## Why This First

- Most common question: "Did validation pass?"
- Immediate value for daily workflow
- Simple to implement and test
```

**The Throughline Applies:**

> _"Manage the LLM's context window like you manage your own attention."_

This applies to:

- Prompts (Course 1)
- Data context (Course 2)
- **Proposals and plans** (right now)

A focused proposal keeps the AI agent's context clean. A bloated proposal leads to:

- Missed requirements
- Inconsistent implementation
- Harder reviews

**Discussion:** Think about a project that grew out of control. How did scope creep start? What would "one thing at a time" have looked like?

---

### Lesson 7.1: 💻 Asking the Advisor About MCP (20 min)

**Concept:** Before building an MCP server, ask the Advisor what would actually help.

**The Conversation:**

```
@data-advisor I've completed my data pipeline with validation
and transformation. I'm wondering if an MCP server would help.

What are the most common questions I'll ask about my pipeline?
What would be the SINGLE most valuable MCP tool to build first?
```

**What a Good Advisor Response Looks Like:**

```markdown
### Common Questions About Your Pipeline

Based on your setup, you'll frequently ask:

1. "Did validation pass?" — Most common, multiple times daily
2. "What's in each data folder?" — When debugging
3. "How many rows were processed?" — After transforms
4. "What quality issues exist?" — When data looks wrong

### Recommendation: Start with ONE Tool

**Build first:** `get_validation_status`

**Why this one:**

- Answers your most frequent question
- Simple to implement (wraps `make validate`)
- Immediate daily value
- You can test the MCP pattern before adding more

**Don't build yet:**

- Data profiling (complex, can use notebooks)
- Pipeline triggers (risky, needs more thought)
- Slack notifications (adds external dependency)

Build ONE tool. Use it for a week. Then decide what's next.
```

**Follow-up Questions:**

```
@data-advisor What would the simplest possible implementation
of get_validation_status look like? Just the concept, not code.
```

```
@data-advisor If I wanted to add a second tool later, what
would you recommend and why?
```

**Hands-on Activity:**

1. Ask `@data-advisor` about MCP for your pipeline
2. Get a recommendation for ONE first tool
3. Document the reasoning in HISTORY.md
4. Resist the urge to plan five tools at once!

---

### Lesson 7.2: 📖💻 Creating a Focused MCP Proposal (15 min)

**Concept:** Write a proposal for exactly ONE MCP tool.

**The Proposal:**

````markdown
# Proposal 003: MCP Tool — Validation Status

## Summary

Add a single MCP tool that reports whether data validation passes or fails.

## One Thing Only

This proposal covers ONE tool: `get_validation_status`

**Not included (future proposals):**

- Data profiling
- File listing
- Pipeline triggers

## Motivation

"Did validation pass?" is the question I ask most often. Currently I:

1. Switch to terminal
2. Run `make validate`
3. Read the output
4. Switch back to Copilot

With MCP, I can ask directly in chat.

## DARE Application

| Letter | This Tool                                    |
| ------ | -------------------------------------------- |
| **D**  | Wraps deterministic `make validate`          |
| **A**  | AI interprets and summarizes results         |
| **R**  | Tool output is read-only (can't modify data) |
| **E**  | Reports failures clearly for human action    |

## Implementation

### Input

None required (validates default data location)

### Output

```json
{
  "status": "PASS" | "FAIL",
  "details": "Customer schema: PASS\nTransaction schema: FAIL - 3 null customer_ids"
}
```
````

### How It Works

1. Run `make validate-schema`
2. Capture stdout/stderr
3. Parse exit code (0 = pass, non-zero = fail)
4. Return structured result

## Files to Create

- [ ] `mcp/pipeline_server.py` — MCP server with ONE tool
- [ ] `.vscode/mcp.json` — Configuration

## Success Criteria

- [ ] Can ask "Did validation pass?" in Copilot Chat
- [ ] Get clear PASS/FAIL answer
- [ ] See specific issues if FAIL

## What's Next (NOT this proposal)

After using this for one week, consider:

- `get_data_profile` — If I frequently need column stats
- `list_pipeline_files` — If I often check what's in each folder

## Approval

- [ ] Reviewed by: [reviewer]
- [ ] Approved on: YYYY-MM-DD

```

**Key Elements of a Focused Proposal:**

| Element | Purpose |
|---------|---------|
| "One Thing Only" | Explicit scope limitation |
| "Not included" | Prevents scope creep |
| "What's Next" | Acknowledges future without committing |
| Simple success criteria | Easy to verify done |

**Hands-on Activity:**

1. Create `docs/proposals/003-mcp-validation-tool.md`
2. Keep it to ONE tool only
3. Have `@reviewer` check for scope creep
4. Notice how much easier it is to review!

---

### Lesson 7.3: 💻 Implementing the First Tool (10 min)

**Concept:** Hand off to transformer with your focused proposal.

**The Handoff:**

```

@transformer Please implement the MCP tool described in
docs/proposals/003-mcp-validation-tool.md

Create:

1. mcp/pipeline_server.py with get_validation_status tool
2. .vscode/mcp.json configuration

Keep it minimal — just this ONE tool for now.

```

**What the Transformer Creates:**

The transformer implements ONLY what's in the proposal — not "and while I'm at it, let me add five more tools."

**Testing:**

```

# Test standalone

python mcp/pipeline_server.py

# Reload VS Code, then ask:

"Did my data validation pass?"

```

**Hands-on Activity:**

1. Hand off to transformer with your proposal
2. Review the implementation — did it stay focused?
3. Test the ONE tool
4. Use it for real for the rest of the module

---

### Lesson 7.4: 📖 The Iteration Pattern (5 min)

**Concept:** Adding features through successive focused proposals.

**The Pattern:**

```

Week 1: Proposal 003 — get_validation_status
↓ Use it, learn what's missing

Week 2: Proposal 004 — get_data_profile
 ↓ Use it, learn what's missing

Week 3: Proposal 005 — list_pipeline_files
↓ ...

```

**Why This Works:**

| Approach | Result |
|----------|--------|
| Build 5 tools at once | 3 you never use, 2 that don't quite fit |
| Build 1, use, iterate | Each tool shaped by real needs |

**The Anti-Pattern to Avoid:**

```

"While we're at it, let's also add..."
"It would be easy to include..."
"We might as well..."

```

These phrases are scope creep signals. Each "and" deserves its own proposal.

**Connecting to the Throughline:**

Just as you manage the LLM's context window, manage your project's scope:
- Small prompts → better responses
- Small proposals → better implementations
- Small iterations → better products

---

### Module 7 Checkpoint

By the end of this module, your project should look like this:

```

customer-data-pipeline/
├── ...
├── docs/
│ └── proposals/
│ ├── 001-schema-contract.md
│ ├── 002-deployment-approach.md
│ └── 003-mcp-validation-tool.md # ✅ Focused on ONE tool
├── mcp/
│ └── pipeline_server.py # ✅ ONE tool implemented
└── .vscode/
└── mcp.json # ✅ MCP configured

```

**Verify:**
- Ask Copilot "Did my data validation pass?"
- Get a clear answer using your MCP tool

**Key Lesson:** You built ONE useful tool, not five tools you'll never use.

**Checkpoint:** `git checkout module-7-mcp` to see reference implementation

---

## AgentSkills.io Alignment Note

This module references the skill definition format. In AgentSkills.io, `.agent.md` files are named `SKILL.md`, and `.github/agents/` directories are `skills/`. The core patterns of advisor, transformer, and reviewer skill roles remain the same. See your project's AGENTS.md for the complete skill inventory.
