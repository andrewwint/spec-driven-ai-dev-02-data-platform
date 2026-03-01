# Schema Validation Checklist

Use this checklist when reviewing any schema contract proposal.

## Completeness Checks

- [ ] Every source column is represented in the schema
- [ ] Required vs. optional is explicit (not ambiguous)
- [ ] Data type is specified for every column
- [ ] Validation rules exist for every column
- [ ] No "TBD" or undefined columns remain

## Correctness Checks

- [ ] Validation rules align with data-explorer findings
- [ ] Edge cases mentioned in exploration are handled
- [ ] Null handling strategy is explicit
- [ ] Empty string handling is specified (if applicable)
- [ ] Boundary values are tested (min/max, first/last)
- [ ] Format specifications are unambiguous (regex provided if needed)

## Implementability Checks

- [ ] Each rule can be checked deterministically
- [ ] Thresholds are quantified (not "mostly", "usually")
- [ ] Error handling is specified (skip row? null? alert?)
- [ ] Success criteria are measurable and testable
- [ ] No circular dependencies between validation rules

## DARE Model Checks

### Deterministic (D)
- [ ] All required validation checks are deterministic
- [ ] Specific examples given for edge cases
- [ ] No human judgment needed for data classification

### AI-Assisted (A)
- [ ] AI decisions are explicitly scoped (where needed)
- [ ] Fallback behavior is defined when AI confidence is low
- [ ] Review gate exists before using AI-cleaned data

### Review (R)
- [ ] Review checkpoints are defined
- [ ] High-severity issues trigger alerts or review gates
- [ ] Exceptions require human approval

### Escalation (E)
- [ ] Failure thresholds are quantified
- [ ] Who gets notified when thresholds are exceeded
- [ ] Escalation path is clear

## Example Validation

### ✅ GOOD: Complete Schema

```yaml
customer_id:
  type: string
  required: true
  rules:
    - must be non-empty
    - must be unique
    - format: ^C\d{3}$
  example: C001

email:
  type: string
  required: false
  rules:
    - if present, must match RFC 5322
    - nulls are allowed
  example: john@example.com

age:
  type: integer
  required: true
  rules:
    - must be in range [0, 120]
    - invalid values: reject row with explanation
  example: 34
```

### ❌ BAD: Incomplete Schema

```yaml
customer_id: string, unique
email: valid email format  # "valid" is ambiguous
age: number, range 0-120   # What about -5, 999, null?
status: TBD                # Not specified
```

## Common Issues to Spot

| Issue | How to Catch | Fix |
|-------|--------------|-----|
| Ambiguous "valid format" | Ask: "What specific characters allowed?" | Provide regex or reference |
| Missing null handling | Check: Is null explicitly allowed/forbidden? | Add null rule for each column |
| Undefined thresholds | Look for: "too many", "mostly", "usually" | Replace with specific numbers |
| No error handling | Ask: "What happens if validation fails?" | Specify action (skip, null, alert) |
| Circular dependencies | Trace: Does validation rule A depend on B which depends on A? | Reorder or simplify |
