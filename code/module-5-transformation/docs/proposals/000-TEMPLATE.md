# Proposal Template

> Copy this file to create a new proposal: `docs/proposals/NNN-short-description.md`

---

# Proposal NNN: [Title]

## Summary

[One paragraph describing what this proposal will accomplish]

## Motivation

[Why is this change needed? What problem does it solve?]

## DARE Application

| Letter | This Proposal |
|--------|---------------|
| **D** | [What can be validated deterministically?] |
| **A** | [What requires AI assistance?] |
| **R** | [What gates/reviews are needed?] |
| **E** | [What triggers escalation?] |

## Proposed Schema

### [data_file.csv]

| Column | Type | Required | Validation |
|--------|------|----------|------------|
| column_name | string/int/date | Yes/No | [Validation rules] |

## Escalation Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Null percentage | >5% | ALERT |
| Duplicate count | >0 | BLOCK |
| Format errors | >1% | ALERT |

## Implementation Tasks

### Task 1: [Name]
- [ ] Sub-task A
- [ ] Sub-task B

### Task 2: [Name]
- [ ] Sub-task A
- [ ] Sub-task B

## Files to Create/Modify

### New Files
- [ ] `path/to/new/file.py` — Description

### Modified Files
- [ ] `path/to/existing/file.py` — What changes

## Agents Involved

| Agent | Responsibility |
|-------|---------------|
| data-explorer | Profile data, identify issues |
| schema-validator | Review this contract |
| transformer | Implement validation/cleaning code |
| reviewer | Review implementation |

## Workflow

```
data-explorer profiles data
    ↓
Human creates this proposal
    ↓
schema-validator reviews contract
    ↓
transformer implements code
    ↓
reviewer validates implementation
    ↓
Human approves
```

## Success Criteria

- [ ] Schema validation passes for all rows
- [ ] Null percentage below threshold
- [ ] No duplicate primary keys
- [ ] All tests pass
- [ ] CHANGELOG updated

## Approval

- [ ] **Reviewed by:** [schema-validator / human]
- [ ] **Approved on:** YYYY-MM-DD
- [ ] **Implemented on:** YYYY-MM-DD

---

## Notes

[Any additional context, links, or discussion]
