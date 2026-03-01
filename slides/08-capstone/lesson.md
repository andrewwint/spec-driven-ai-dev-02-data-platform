# Module 8: Capstone — Complete the Pipeline (90 minutes)

**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

> **Important:** This capstone completes your Customer Data Pipeline. You are NOT starting a new project—you're finishing and validating the work you've built incrementally through Modules 1-7.

### Lesson 8.1: 💻 Fill Any Gaps (25 min)

**Concept:** Ensure all project components exist and are complete.

**Checklist — What You Should Have:**

```

customer-data-pipeline/
├── README.md # ☐ Project overview
├── CHANGELOG.md # ☐ Has version entries
├── AGENTS.md # ☐ Documents all 5 skills
├── HISTORY.md # ☐ Session notes throughout
├── Makefile # ☐ All targets working
├── .pre-commit-config.yaml # ☐ Configured and tested
├── requirements.txt # ☐ All dependencies listed
├── data/
│ ├── raw/
│ │ ├── customers.csv # ☐ Original data with issues
│ │ ├── transactions.csv # ☐ Original data with issues
│ │ └── sessions.csv # ☐ Original data with issues
│ ├── cleaned/
│ │ └── customers.csv # ☐ Cleaned output exists
│ └── features/
│ └── .gitkeep # ☐ Ready for Course 3
├── src/
│ ├── validators/
│ │ └── customer_validator.py # ☐ Schema validation
│ └── transformers/
│ └── customer_cleaner.py # ☐ Transformation logic
├── notebooks/
│ └── 00-data-quality-exploration.ipynb # ☐ Exploration notebook
├── docs/
│ └── proposals/
│ ├── 001-schema-contract.md # ☐ Approved schema
│ ├── 002-deployment-approach.md # ☐ ROI analysis complete
│ └── 003-mcp-validation-tool.md # ☐ Focused MCP proposal
├── mcp/
│ └── pipeline_server.py # ☐ ONE MCP tool
├── skills/
│ ├── data-advisor.SKILL.md # ☐ Advisor skill
│ ├── data-explorer.SKILL.md # ☐ Explorer skill
│ ├── schema-validator.SKILL.md # ☐ Validator skill
│ ├── transformer.SKILL.md # ☐ Transformer skill
│ └── reviewer.SKILL.md # ☐ Reviewer skill
└── .vscode/
└── mcp.json # ☐ MCP configured

```

**Hands-on Activity:** Use the reviewer skill to fill gaps

```

@reviewer Please review our project structure and identify any
missing components compared to this checklist:

[paste checklist above]

Create a list of what's missing or incomplete.

````

---

### Lesson 8.2: 💻 Run Full Verification (15 min)

**Concept:** Validate everything works together.

**Run These Commands:**

```bash
# 1. All make targets should pass
make validate

# 2. Run the full pipeline
make pipeline

# 3. All pre-commit hooks should pass
pre-commit run --all-files

# 4. List skills to verify they're recognized
make skills-check

# 5. Quick status check
make status
````

**Expected Output:**

```
🔍 Validating data schemas...
✅ Customer schema: PASS
✅ Transaction schema: PASS

🔄 Running transformation pipeline...
✅ Cleaned 31 customer records
✅ Output saved to data/cleaned/

🎉 Pipeline complete!
```

**If Something Fails:**

Use troubleshooting patterns from Module 5:

```
@data-advisor I ran `make validate` and got this error:

[paste error]

Can you help me understand what's wrong?
```

---

### Lesson 8.3: 💻 Final Review Cycle (25 min)

**Concept:** Complete a full review cycle on the finished project.

**Hands-on Activity:** Use the reviewer skill for final validation

```
@reviewer Please do a comprehensive review of our completed
Customer Data Pipeline project:

1. **Code Review**
   - src/validators/ - validation functions match schema contract?
   - src/transformers/ - cleaning logic handles all identified issues?
   - Functions have docstrings referencing schema?

2. **Skill Review**
   - Are all five skill files properly structured?
   - Do handoffs make logical sense?
   - Are tool restrictions appropriate for each role?

3. **Documentation Review**
   - HISTORY.md - captures session decisions?
   - AGENTS.md - accurately describes our setup?
   - docs/proposals/ - all three proposals complete?

4. **Infrastructure Review**
   - Makefile - all targets work?
   - .pre-commit-config.yaml - properly configured?
   - MCP server - responds to queries?

5. **DARE Compliance**
   - D: Schema validation is deterministic?
   - A: Transformation logic handled by skills?
   - R: Review gates at appropriate boundaries?
   - E: Escalation thresholds defined?

Provide a final status report.
```

---

### Lesson 8.4: 📖💻 Document Learnings & Course Completion (25 min)

**Concept:** Capture what you learned and verify all objectives met.

**Hands-on Activity:** Update HISTORY.md with your learnings

Add a "Course 2 Completion" section:

```markdown
## Course 2 Completion

### What Worked Well

- [Your observations]

### What Was Harder Than Expected

- [Your observations]

### Key Insights

- [Your observations]

### What I'd Do Differently

- [Your observations]
```

**Course Completion Checklist:**

| Objective                      | Demonstrated By                            |
| ------------------------------ | ------------------------------------------ |
| ☐ Use Advisor pattern          | data-advisor conversations in HISTORY.md   |
| ☐ Profile data with skills     | Exploration notebook, quality issues found |
| ☐ Create schema contracts      | 001-schema-contract.md approved            |
| ☐ Implement validation         | Validators match schema rules              |
| ☐ Transform data               | Cleaned data in data/cleaned/              |
| ☐ Apply ROI analysis           | 002-deployment-approach.md with trade-offs |
| ☐ Build focused proposals      | 003-mcp-validation-tool.md (ONE tool)      |
| ☐ Configure MCP                | Working validation status tool             |
| ☐ Apply progressive disclosure | Context delivered in stages                |
| ☐ Maintain skill memory        | HISTORY.md captures decisions              |

**Final Verification Commands:**

```bash
make validate           # All should pass
make pipeline           # End-to-end works
make skills-check       # Should list 5 skills
pre-commit run --all-files  # All hooks pass
```

---

### Connection to Course 3: ML Workflows

The concepts you learned in Course 2 carry directly into Course 3. Here's how they map:

| Course 2 Concept               | Course 3 Application                       |
| ------------------------------ | ------------------------------------------ |
| Schema contracts               | Feature contracts (expected ranges, types) |
| data/cleaned/ → data/features/ | Feature engineering pipeline               |
| Advisor pattern                | ML-advisor for model selection guidance    |
| ROI analysis                   | Model complexity vs. accuracy trade-offs   |
| Validation gates               | Model validation, drift detection          |
| Progressive disclosure         | Training context management                |

**What You'll Build in Course 3:**

A feature engineering and model training pipeline that:

- Uses the clean data from Course 2 as input
- Applies Advisor pattern to ML concepts
- Creates feature contracts (like schema contracts)
- Implements model validation gates
- Prepares for production deployment

**The Pattern Continues:**

```
Course 1: Hello World Pipeline
    └── "Context is attention" + DARE + Skills + Verification

Course 2: Data Platform ← YOU COMPLETED THIS
    └── Same patterns applied to data engineering
        └── Advisor teaches unfamiliar domain
        └── Schema contracts validate (Deterministic)
        └── Proposals before implementation (Review)
        └── Quality alerts escalate (Escalation)

Course 3: ML Workflows
    └── Same patterns applied to machine learning
        └── Advisor teaches ML concepts
        └── Feature contracts validate
        └── Model selection proposals
        └── Performance alerts escalate
```

**Closing Thought:**

> "You've learned to use the Advisor pattern to navigate unfamiliar domains, create focused proposals one thing at a time, and apply progressive disclosure to manage context. The data platform you built is ready for Course 3's ML workflows."

---

### Module 8 Checkpoint (Final)

By the end of this module, your complete project should:

```
customer-data-pipeline/
├── All files from checklist present     # ✅
├── make validate passes                 # ✅
├── make pipeline produces output        # ✅
├── pre-commit run --all-files passes    # ✅
├── MCP tool responds to queries         # ✅
├── HISTORY.md has completion notes      # ✅
└── Ready for Course 3                   # ✅
```

**Checkpoint:** `git checkout module-8-complete` to see reference implementation

🎉 **Congratulations! You've completed Course 2: Data Platform Architecture.**

---

## AgentSkills.io Alignment Note

This module references skill files and the AGENTS.md project inventory. In AgentSkills.io terminology:
- `.agent.md` files are named `SKILL.md`
- `.github/agents/` directory is renamed to `skills/`
- All core skill concepts (advisor, transformer, reviewer roles) remain consistent
- The skill-based workflow and handoff patterns are the foundation for AgentSkills.io implementations
