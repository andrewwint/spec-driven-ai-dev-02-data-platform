# Code Review Checklist

Use this checklist when reviewing implementation code against a schema contract.

## Pre-Review Setup

- [ ] You have the approved schema contract open
- [ ] You have the implementation code open
- [ ] You have the test files open
- [ ] HISTORY.md is reviewed for context

## Schema Compliance Review

For each validation rule in the schema:

- [ ] Rule is explicitly implemented in code
- [ ] Implementation matches rule exactly (not close)
- [ ] Edge cases from rule are handled
- [ ] Comments reference the specific schema rule
- [ ] Tests verify the rule is enforced

For each transformation rule in the schema:

- [ ] Transformation is implemented
- [ ] Implementation matches rule exactly
- [ ] All steps in the rule are present
- [ ] Comments explain WHY it's done this way
- [ ] Tests verify the transformation works correctly

## Code Quality Review

### Readability
- [ ] Function names are clear and descriptive
- [ ] Variable names are meaningful
- [ ] Code is organized logically
- [ ] No deeply nested logic (if > 2 levels, consider extracting)
- [ ] Obvious patterns are followed

### Completeness
- [ ] All functions have docstrings
- [ ] Docstrings are complete (description, args, returns)
- [ ] Module docstring explains purpose
- [ ] Schema reference is in docstring or comments
- [ ] Complex logic has explanatory comments

### Correctness
- [ ] Logic is correct for stated purpose
- [ ] No obvious bugs (off-by-one, null pointer, type errors)
- [ ] Error handling is appropriate
- [ ] Edge cases are handled
- [ ] No dead code or commented-out logic

### Consistency
- [ ] Follows existing code patterns in `src/`
- [ ] Naming conventions match project
- [ ] Indentation and formatting are consistent
- [ ] Type hints are used (if project uses them)

## Test Coverage Review

### Test Existence
- [ ] Test file exists: `tests/test_[module].py`
- [ ] Test file is importable and runnable
- [ ] Tests actually exist for the code being reviewed

### Test Completeness
- [ ] Happy path tests exist (valid input → correct output)
- [ ] Edge case tests exist for each schema rule:
  - [ ] Null values
  - [ ] Empty strings
  - [ ] Boundary values (min, max)
  - [ ] Invalid formats
  - [ ] Unexpected types
- [ ] Tests match schema expectations exactly

### Test Quality
- [ ] Test names describe what they test
- [ ] Assertions are clear and specific
- [ ] Tests are deterministic (same input = same output)
- [ ] No flaky tests or timing dependencies
- [ ] Tests actually validate something (not just calling code)

### Test Execution
- [ ] All tests pass: `python -m pytest tests/ -v`
- [ ] No test skips (unless explicitly documented)
- [ ] Test output is clear and readable

## Schema Compliance Details

Create a compliance matrix for each major rule:

| Schema Rule | Code Location | Implementation | Status |
|------------|---------------|----------------|--------|
| Required column | [file:line] | [description] | ✅/⚠️/❌ |
| Unique values | [file:line] | [description] | ✅/⚠️/❌ |
| Format validation | [file:line] | [description] | ✅/⚠️/❌ |

For each "⚠️" or "❌", specify the issue and required fix.

## Common Issues to Check

| Issue | How to Spot | Fix |
|-------|------------|-----|
| Schema rule not implemented | Check: Is there code for this rule? | Implement the rule |
| Implementation doesn't match schema | Compare code to rule word-by-word | Update code to match exactly |
| Missing edge case handling | Check: Does code handle nulls, empty strings, boundaries? | Add edge case handling |
| Missing test | Check: Is there a test for this rule? | Write test case |
| Test doesn't match schema | Check: Does test verify schema requirement? | Update test to match schema |
| Null handling not explicit | Check: Does code say what happens to nulls? | Add explicit null handling with comment |
| No schema reference in code | Check: Do comments reference schema document? | Add schema reference |
| Ambiguous function behavior | Check: Could reader understand without schema? | Add clarifying comment |

## Final Approval Checklist

Before approving:

- [ ] All schema rules are implemented
- [ ] All tests pass
- [ ] Code quality is acceptable
- [ ] No blocker issues remain
- [ ] Comments reference schema
- [ ] Edge cases are handled

Before rejecting:

- [ ] Issues are specific and actionable
- [ ] Each issue has a specific fix suggestion
- [ ] Severity is accurate (blocking vs. non-blocking)
- [ ] Feedback helps transformer improve code

## Sign-Off

When you approve, state clearly:

"Code correctly implements [schema name]. All schema rules are enforced by tests. Ready for deployment."

When you request changes, state clearly:

"Please address these must-fix issues:
1. [Specific issue with fix]
2. [Specific issue with fix]

Then resubmit for review."
