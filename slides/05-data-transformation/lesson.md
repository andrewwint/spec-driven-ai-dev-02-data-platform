# Module 5: Data Transformation with Skills

**Duration:** 90 minutes
**Lesson Types:** 📖 Lecture | 💻 Hands-on | 📖💻 Lecture + Lab

---

## Lesson 5.0: 📖💻 The Transformer Skill (20 min)

**Concept:** A Doer skill that writes transformation code based on validated schemas.

**The transformer.SKILL.md:**

```markdown
---
name: transformer
description: Writes data transformation and cleaning code
tools: ["read", "edit", "terminal", "search"]
handoffs:
  - label: Ask Advisor
    skill: data-advisor
    prompt: I have questions about the transformation approach.
    send: false
  - label: Review Changes
    skill: reviewer
    prompt: Transformation code complete. Please review.
    send: false
---

# Transformer Skill

You write data transformation code that implements schema contracts
and cleaning logic.

## Core Responsibilities

1. **Read** schema contracts and validation rules
2. **Write** transformation functions
3. **Test** transformations locally
4. **Document** what each transformation does

## Before Writing Code

1. Read the schema contract in docs/proposals/
2. Check HISTORY.md for context
3. Understand what validation already exists

## Code Patterns

### Cleaning Function Pattern

```python
def clean_[column](value: Any) -> Any:
    """Clean [column] according to schema contract.

    Rules:
    - [Rule 1 from contract]
    - [Rule 2 from contract]
    """
    # Implementation
```

### Transformation Pipeline Pattern

```python
def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all customer transformations.

    Steps:
    1. [Step from contract]
    2. [Step from contract]
    """
    return (
        df
        .pipe(clean_customer_id)
        .pipe(clean_email)
        .pipe(clean_signup_date)
        .pipe(clean_age)
    )
```

## Rules

- ✅ **MUST** reference schema contract for every transformation
- ✅ **MUST** write tests for each transformation
- ✅ **MUST** update HISTORY.md after significant changes
- ❌ **NEVER** transform without understanding the rule
```

---

## Lesson 5.1: 💻 Writing Transformation Code (30 min)

**Concept:** Using the transformer skill to implement cleaning logic.

**The Conversation:**

```
@transformer Based on the schema contract in
docs/proposals/001-schema-contract.md, please implement
the customer data cleaning pipeline.

Create:

1. src/transformers/customer_cleaner.py
2. Tests in tests/test_customer_cleaner.py
3. Update Makefile with transform-customers target
```

**What the Transformer Creates:**

```python
# src/transformers/customer_cleaner.py
"""Customer data cleaning transformations.

Implements rules from: docs/proposals/001-schema-contract.md
"""
import pandas as pd
from datetime import datetime

def clean_customer_id(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with null or duplicate customer_ids.

    Schema rule: customer_id must be unique and non-null.
    """
    initial_count = len(df)
    df = df.dropna(subset=['customer_id'])
    df = df.drop_duplicates(subset=['customer_id'], keep='first')
    final_count = len(df)

    if initial_count != final_count:
        print(f"Removed {initial_count - final_count} invalid customer_ids")

    return df

def clean_email(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize email format, allow nulls.

    Schema rule: email is optional, must be valid format if present.
    """
    def normalize_email(email):
        if pd.isna(email):
            return None
        return str(email).lower().strip()

    df['email'] = df['email'].apply(normalize_email)
    return df

def clean_signup_date(df: pd.DataFrame) -> pd.DataFrame:
    """Convert to ISO 8601 format.

    Schema rule: signup_date required, ISO format.
    """
    df['signup_date'] = pd.to_datetime(
        df['signup_date'],
        format='mixed',
        errors='coerce'
    ).dt.strftime('%Y-%m-%d')

    return df

def clean_age(df: pd.DataFrame) -> pd.DataFrame:
    """Validate age range, set invalid to null.

    Schema rule: age required, range 0-120.
    """
    df.loc[(df['age'] < 0) | (df['age'] > 120), 'age'] = None
    return df

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Full customer transformation pipeline."""
    return (
        df
        .pipe(clean_customer_id)
        .pipe(clean_email)
        .pipe(clean_signup_date)
        .pipe(clean_age)
    )
```

**Hands-on Activity:**

1. Use transformer to create the cleaning code
2. Review the generated code — do you understand each function?
3. Run `make transform-customers`
4. Check the output in `data/cleaned/`

---

## Lesson 5.2: 📖💻 The Review Gate (20 min)

**Concept:** Using the reviewer skill to validate transformation code.

**The Handoff:**

After transformer completes, use "Review Changes" handoff:

```
@reviewer Please review the transformation code in
src/transformers/customer_cleaner.py

Check:
1. Each function references the schema contract
2. Edge cases are handled
3. Tests exist and pass
4. Documentation is accurate
```

**Reviewer Output:**

```markdown
## Review Summary

**Status:** APPROVED with suggestions

**Files Reviewed:**

- src/transformers/customer_cleaner.py
- tests/test_customer_cleaner.py

## Findings

### ✅ What's Good

- Each function documents which schema rule it implements
- Clean use of pandas pipe pattern
- Tests cover happy path

### ⚠️ Suggestions

- Add test for email with unicode characters
- Consider logging removed row counts

### ❌ Required Changes

- None

## Recommendation

Ready to proceed. Consider adding suggested tests.
```

**Discussion:** The reviewer can't fix issues — it can only identify them. Why is this separation valuable?

---

## Lesson 5.3: 💻 Troubleshooting Your Makefile and Pre-commit Hooks (20 min)

**Concept:** The starter kit includes pre-configured Makefile and pre-commit hooks. Let's verify they work and troubleshoot if needed.

**What's Already Configured:**

Your starter kit includes a working Makefile with data pipeline targets:

```makefile
# Already in your Makefile
validate-schema: ## Validate all data against schemas
	@echo "🔍 Validating data schemas..."
	@python -m src.validators.customer_validator data/raw/customers.csv
	@echo "✅ Schema validation complete"

transform: ## Run all transformations
	@echo "🔄 Running transformations..."
	@python -m src.transformers.customer_cleaner
	@echo "✅ Transformations complete"

pipeline: validate-schema transform validate-schema ## Full pipeline
	@echo "🎉 Pipeline complete!"
```

**Pre-commit Hooks:**

```yaml
# Already in your .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: local
    hooks:
      - id: validate-data
        name: Validate Data Schemas
        entry: make validate-schema
        language: system
        pass_filenames: false
        files: ^data/raw/.*\.csv$

      - id: validate-skills
        name: Validate Skill Files
        entry: bash -c 'for f in skills/*.SKILL.md; do head -1 "$f" | grep -q "^---" || (echo "Invalid skill file: $f" && exit 1); done'
        language: system
        pass_filenames: false
        files: ^skills/.*\.SKILL\.md$
```

**Using Copilot to Troubleshoot:**

If `make validate` or `pre-commit run` fails, ask Copilot to help:

```
@verifier I'm getting an error when running `make validate`.
Here's the output:

[paste error output]

Can you help me understand what's wrong and how to fix it?
```

**Hands-on Activity:**

1. Run `make help` to see all available targets
2. Run `pre-commit run --all-files` to test hooks
3. If anything fails, use Copilot to troubleshoot
4. Verify `make pipeline` runs end-to-end

**Common Issues:**

| Symptom                            | Likely Cause          | Fix                                       |
| ---------------------------------- | --------------------- | ----------------------------------------- |
| `make: *** No rule to make target` | Missing target        | Check Makefile indentation (must be tabs) |
| `ModuleNotFoundError`              | Missing dependency    | Run `pip install -r requirements.txt`     |
| Pre-commit hook fails              | File validation error | Check the specific file mentioned         |
| `command not found: ruff`          | Ruff not installed    | Run `pip install ruff`                    |

> 💡 **Progressive Disclosure:** Error messages are "instructions given in feedback." When `make validate` fails, the output tells you exactly what's wrong. When tests fail, the error message guides the fix. You don't need to anticipate every problem upfront — the system provides instructions when issues occur.

---

## Module 5 Checkpoint

By the end of this module, your project should look like this:

```
customer-data-pipeline/
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   └── 02-data-cleaning.ipynb
├── src/
│   ├── transformers/
│   │   ├── __init__.py
│   │   ├── customer_cleaner.py     # ✅ Transformation functions
│   │   └── transaction_cleaner.py
│   └── validators/
│       └── ...
├── tests/
│   └── test_customer_cleaner.py    # ✅ Transformation tests
├── data/
│   ├── raw/
│   └── cleaned/
│       └── customers.csv           # ✅ Generated by transform
├── Makefile                        # ✅ Verified working
└── .pre-commit-config.yaml         # ✅ Verified working
```

**Verify:**

- `make pipeline` runs without errors
- `pre-commit run --all-files` passes

**Checkpoint:** `git checkout module-5-transformation` to see reference implementation

---

## Alignment Note: AgentSkills.io Terminology

This module uses skill definition files in `.SKILL.md` format, located in the `skills/` directory (formerly `.github/agents/` with `.agent.md` extension). The transformer skill implements the "A" (Action) and multi-agent handoffs demonstrate collaborative skill workflows, a core pattern in AgentSkills.io architecture.
