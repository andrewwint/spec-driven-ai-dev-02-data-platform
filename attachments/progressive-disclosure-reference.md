# Progressive Disclosure Reference

> Don't dump everything upfront. Deliver instructions to agents in stages — when they're relevant.

Based on: [Delivering Instructions to AI Models](https://blog.huikang.dev/2025/10/20/delivering-ai-instructions.html)

## The 7 Instruction Delivery Methods

| # | Method | Description | Course 2 Example |
|---|--------|-------------|------------------|
| 1 | **Loaded upfront** | Always in context | CLAUDE.md basics (use sparingly) |
| 2 | **Provided by user** | Human gives instructions | Focused prompts to Advisor |
| 3 | **Always injected** | System adds automatically | Safety gates in agents |
| 4 | **Decided to be read** | Agent chooses to load | HISTORY.md, schema contracts |
| 5 | **Discovered** | Agent learns from environment | Explorer finds patterns in data |
| 6 | **Triggered** | Deterministic conditions fire | Pre-commit hooks, Makefile targets |
| 7 | **Given in feedback** | Errors guide next steps | Test failures, validation errors |

## Why This Matters

### Problems with "Load Everything Upfront"

- **Instructions cost money** — Every word is overhead on every request
- **Instructions can conflict** — Longer = more likely to contradict
- **Instructions are open to interpretation** — Ambiguity grows with length

### Benefits of Progressive Disclosure

- **Relevant context** — Agent gets what it needs when it needs it
- **Cleaner reasoning** — Less noise, better outputs
- **Cheaper** — Only load context that matters for the task

## Course 2 Applications

### HISTORY.md = "Decided to be read"
Agents load project history at session start, not every message.

### Data Explorer = "Discovered"
Agent learns patterns from your actual data, not from your descriptions.

### Makefile/Pre-commit = "Triggered"
Validation rules fire on conditions, not AI judgment.

### Error Messages = "Given in feedback"
When tests fail, the output tells you what to fix.

### Bloated Proposals = Anti-pattern
Dumping every feature into one proposal is "loading everything upfront."

## The Throughline

> "Manage the LLM's context window like you manage your own attention."

Just as you focus on one thing at a time, deliver instructions to agents one stage at a time.
