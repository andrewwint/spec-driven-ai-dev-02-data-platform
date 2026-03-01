# Transformer Implementation Checklist

Use this checklist when implementing validation and transformation code.

## Pre-Implementation

- [ ] Approved schema contract exists in `docs/proposals/`
- [ ] Schema has been reviewed and approved by schema-validator
- [ ] You understand what each validation rule means
- [ ] Sample data exists in `data/raw/` for testing
- [ ] You've reviewed existing code in `src/` for patterns

## Validation Code

For each validation rule in the schema:

- [ ] Create dedicated validation function
- [ ] Function name: `validate_[column_name]()`
- [ ] Function is deterministic (same input = same output)
- [ ] Function returns ValidationResult with issues list
- [ ] Comments reference specific schema rule
- [ ] Tests exist for happy path (valid data)
- [ ] Tests exist for edge cases (nulls, boundaries, invalid formats)

## Transformation Code

For each transformation rule in the schema:

- [ ] Create dedicated transformation function
- [ ] Function name: `clean_[column_name]()`
- [ ] Function handles all edge cases mentioned in schema
- [ ] Implementation matches schema rule exactly
- [ ] Comments explain WHY (not just WHAT)
- [ ] Tests verify transformation produces expected output
- [ ] Tests verify edge cases are handled

## Code Organization

- [ ] New files follow `src/validators/` and `src/transformers/` pattern
- [ ] Modules have docstrings explaining purpose
- [ ] All functions have complete docstrings
- [ ] Docstrings reference schema document
- [ ] Imports are organized and used
- [ ] No dead code or commented-out logic

## Testing

- [ ] Tests directory exists: `tests/`
- [ ] Test file: `tests/test_[module_name].py`
- [ ] All validation functions have tests
- [ ] All transformation functions have tests
- [ ] Tests cover happy path (valid data)
- [ ] Tests cover edge cases:
  - [ ] Null values
  - [ ] Empty strings
  - [ ] Boundary values (min, max)
  - [ ] Invalid formats
  - [ ] Unexpected types
- [ ] Tests actually run and pass: `python -m pytest tests/`

## Documentation

- [ ] Module docstring explains what it does
- [ ] Module docstring references schema document
- [ ] Every function has complete docstring
- [ ] Docstring includes parameter types and descriptions
- [ ] Complex logic has inline comments explaining WHY
- [ ] Schema reference appears in function docstring or comments

## Output Verification

- [ ] Cleaned data is written to `data/cleaned/` as expected
- [ ] Output file format matches specification
- [ ] Output column names and types are correct
- [ ] Transformation is idempotent (can run multiple times safely)

## Edge Cases from Schema

For each edge case mentioned in the schema:

- [ ] Identified in code comments with schema reference
- [ ] Handled explicitly in validation or transformation logic
- [ ] Tested with actual test case
- [ ] Behavior matches schema specification

## Integration

- [ ] Pipeline function exists that chains all cleaners
- [ ] Pipeline function is tested end-to-end
- [ ] Pipeline runs without errors
- [ ] Output in `data/cleaned/` is as expected

## Ready for Review

- [ ] All tests pass: `python -m pytest tests/ -v`
- [ ] Code runs without warnings
- [ ] No TODO or FIXME comments in code
- [ ] All schema rules are implemented (not skipped)
- [ ] Ready to hand off to reviewer
