# Module 4: Schema Validation as DARE

**Duration:** 90 minutes
**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 4.0: 📖 Why Schema Contracts Matter (15 min)

**Concept:** Schema contracts are the "D" in DARE for data pipelines.

**The DARE Model for Data:**

| Letter | Course 1 (Code) | Course 2 (Data)                |
| ------ | --------------- | ------------------------------ |
| **D**  | Linting, tests  | Schema validation, null checks |
| **A**  | Code generation | Transformation logic           |
| **R**  | Code review     | Data quality gates             |
| **E**  | CI/CD alerts    | Quality threshold alerts       |

**Why Deterministic First?**

```
Without schema validation:
┌─────────────────────────────────────────────────────────────────┐
│  Raw Data → ??? → Transformation → ??? → Features → ??? → ML   │
│              ↑           ↑            ↑                         │
│         Unknown       Unknown      Unknown                      │
│         quality       failures     results                      │
└─────────────────────────────────────────────────────────────────┘

With schema validation:
┌─────────────────────────────────────────────────────────────────┐
│  Raw Data → [GATE] → Transformation → [GATE] → Features → ML   │
│              ↑              ↑            ↑                      │
│          Schema          Schema       Schema                    │
│         validates       validates    validates                  │
│         (KNOWN)         (KNOWN)      (KNOWN)                    │
└─────────────────────────────────────────────────────────────────┘
```

**Discussion:** What happens when you train an ML model on data you haven't validated? Why is "garbage in, garbage out" especially dangerous in ML?

---

## Lesson 4.1: 📖💻 The Schema Validator Skill (20 min)

**Concept:** A Gate skill that validates schemas without modifying files.

**The schema-validator.SKILL.md:**

```markdown
---
name: schema-validator
description: Validates data against schema contracts (read-only)
tools: ["read", "search"]
handoffs:
  - label: Schema Approved
    skill: transformer
    prompt: Schema contract validated. Ready to implement transformations.
    send: false
  - label: Schema Issues
    skill: data-advisor
    prompt: Found issues with the schema contract that need discussion.
    send: false
---

# Schema Validator Skill

You are a read-only validator that checks schema contracts for
completeness and correctness. You CANNOT modify files.

## Core Responsibilities

1. **Review** schema proposals for completeness
2. **Check** that all columns are accounted for
3. **Validate** that rules are implementable
4. **Identify** missing edge cases

## Validation Checklist

### Completeness

- [ ] All columns from source data are defined
- [ ] Required/optional clearly specified
- [ ] Data types are appropriate
- [ ] Validation rules are specific

### Correctness

- [ ] Rules match exploration findings
- [ ] Edge cases are handled
- [ ] Null handling is explicit
- [ ] Format specifications are unambiguous

### Implementability

- [ ] Rules can be coded deterministically
- [ ] Thresholds are defined (e.g., ">5% failures = alert")
- [ ] Error handling is specified

## Output Format

### Schema Review: [proposal name]

**Status:** APPROVED / NEEDS REVISION

**Completeness:** X/Y columns defined

**Issues Found:**

- [ ] Issue 1: [description] — Severity: HIGH/MEDIUM/LOW
- [ ] Issue 2: [description]

**Recommendations:**

- [Specific improvement]

**Ready to implement?** Use appropriate handoff.
```

**Discussion:** Why is schema validation a Gate skill, not a Doer? What would go wrong if it could modify files?

---

## Lesson 4.2: 💻 Writing Validation Code (30 min)

**Concept:** Turning schema contracts into Python validation functions.

**From Contract to Code:**

Schema contract says:

```
customer_id: required, unique, non-empty string
```

Validation code:

```python
def validate_customer_id(df: pd.DataFrame) -> ValidationResult:
    """Validate customer_id column."""
    issues = []

    # Required: no nulls
    null_count = df['customer_id'].isnull().sum()
    if null_count > 0:
        issues.append(f"Found {null_count} null customer_ids")

    # Unique: no duplicates
    dup_count = df['customer_id'].duplicated().sum()
    if dup_count > 0:
        issues.append(f"Found {dup_count} duplicate customer_ids")

    # Non-empty: no empty strings
    empty_count = (df['customer_id'] == '').sum()
    if empty_count > 0:
        issues.append(f"Found {empty_count} empty customer_ids")

    return ValidationResult(
        column='customer_id',
        passed=len(issues) == 0,
        issues=issues
    )
```

**The Transformer Writes This:**

```
@transformer Please implement validation functions based on
the schema contract in docs/proposals/001-schema-contract.md

Create:
1. src/validators/customer_validator.py
2. Tests in tests/test_customer_validator.py
3. Makefile target: make validate-customers
```

**Hands-on Activity:**

1. Review your schema contract
2. Use transformer to generate validation code
3. Run `make validate-customers` to test
4. Fix any issues the validator finds

[💻 Code: customer_validator.py with validation functions]

---

## Lesson 4.3: 💻 Validation as a Makefile Target (15 min)

**Concept:** Integrating validation into your workflow with deterministic commands.

**Adding to Makefile:**

```makefile
# =============================================================================
# Data Validation Targets
# =============================================================================

validate-schema: ## Validate all data against schemas
	@echo "🔍 Validating data schemas..."
	@python -m src.validators.customer_validator data/raw/customers.csv
	@python -m src.validators.transaction_validator data/raw/transactions.csv
	@echo "✅ Schema validation complete"

validate-quality: ## Run data quality checks
	@echo "🔍 Running quality checks..."
	@python -m src.quality.null_checker data/raw/
	@python -m src.quality.duplicate_checker data/raw/
	@echo "✅ Quality checks complete"

validate: validate-schema validate-quality ## Full validation suite
```

**The D in DARE:**

These are **deterministic** checks. They:

- Always produce the same result for the same input
- Don't require AI judgment
- Can run in CI/CD
- Fail fast and clearly

> 💡 **Progressive Disclosure:** These Makefile targets are "instructions triggered by conditions." When you run `make validate` or when pre-commit fires, the validation rules activate. You don't need AI to decide IF to validate — that's deterministic.

**Hands-on Activity:**

1. Add validation targets to your Makefile
2. Run `make validate`
3. Intentionally break the data and see validation fail
4. Add validation to pre-commit hooks

---

## Lesson 4.4: 📖 Escalation — When Validation Fails (10 min)

**Concept:** The "E" in DARE — what happens when data doesn't meet the contract.

**Escalation Thresholds:**

```python
# In your validator
ESCALATION_THRESHOLDS = {
    'null_percentage': 5.0,      # Alert if >5% nulls
    'duplicate_count': 0,         # Alert on ANY duplicates
    'format_errors': 1.0,         # Alert if >1% format errors
}

def check_escalation(results: ValidationResult) -> EscalationLevel:
    if results.null_percentage > ESCALATION_THRESHOLDS['null_percentage']:
        return EscalationLevel.ALERT
    if results.duplicate_count > ESCALATION_THRESHOLDS['duplicate_count']:
        return EscalationLevel.BLOCK
    return EscalationLevel.OK
```

**Escalation Levels:**

| Level | Meaning            | Action            |
| ----- | ------------------ | ----------------- |
| OK    | All checks pass    | Continue pipeline |
| WARN  | Minor issues       | Log and continue  |
| ALERT | Threshold exceeded | Notify human      |
| BLOCK | Critical failure   | Stop pipeline     |

**Hands-on Activity:** Define escalation thresholds for your pipeline and add them to the schema contract proposal.

---

## Module 4 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── ...
├── src/
│   └── validators/
│       ├── __init__.py
│       ├── customer_validator.py   # ✅ Schema validation
│       └── transaction_validator.py
├── tests/
│   └── test_customer_validator.py  # ✅ Validation tests
├── Makefile                        # ✅ Updated with validate targets
└── docs/
    └── proposals/
        └── 001-schema-contract.md  # ✅ Includes escalation thresholds
```

**Verify:** `make validate` should run all validation checks

**Checkpoint:** `git checkout module-4-validation` to see reference implementation

---

## Alignment Note: AgentSkills.io Terminology

This module references skill definition files (`.SKILL.md` format, located in `skills/` directory). These correspond to the original `.agent.md` files in `.github/agents/` directory. The concepts and patterns remain the same — validator skills validate deterministically without modification, enabling other skills to act on validated data.
