# Focused Proposal Checklist

Before submitting a proposal, verify:

- [ ] **Does ONE thing only** — Single clear objective
- [ ] **"Not included" section** — Explicitly prevents scope creep
- [ ] **Success criteria are simple** — Can verify in 5 minutes
- [ ] **Can be implemented in one session** — Not a multi-week project
- [ ] **Reviewer can evaluate quickly** — Clear inputs/outputs

## Scope Creep Warning Signs

| Phrase | What to Do |
|--------|------------|
| "While we're at it..." | Stop. New proposal. |
| "It would be easy to also..." | Stop. New proposal. |
| "We might as well..." | Stop. New proposal. |
| "And then we could..." | Stop. New proposal. |

## Good vs. Bad Proposals

### ❌ Bloated Proposal

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
- AND compare datasets
- AND export to Excel
```

**Problems:** Unclear scope, hard to review, long implementation, hard to debug.

### ✅ Focused Proposal

```markdown
# Proposal: MCP Tool — Validation Status

## One Thing Only
Check if data passes schema validation and report issues.

## Not Included (future proposals)
- Data profiling
- File listing  
- Pipeline triggers

## Success Criteria
- [ ] Can ask "Did validation pass?" in Copilot
- [ ] Get clear PASS/FAIL answer
- [ ] See specific issues if FAIL
```

**Benefits:** Clear scope, easy to review, quick to implement, easy to test.

## The Principle

> "Manage the LLM's context window like you manage your own attention."

This applies to proposals too. A focused proposal keeps the AI agent's context clean.
