# Data Profile Template

Use this template when profiling a data file. Fill in each section with actual findings.

## Data Profile: [filename]

**Shape:** X rows, Y columns

**Columns:**

| Column | Type | Nulls | Null % | Unique | Sample Values |
|--------|------|-------|--------|--------|---------------|
| col1   | str  | 0     | 0%     | 100    | a, b, c       |
| col2   | int  | 15    | 5%     | 50     | 1, 2, 3       |

**Quality Issues Found:**

- [ ] Issue 1: Description and severity (HIGH/MEDIUM/LOW)
- [ ] Issue 2: Description and severity

**Recommendations for Schema Contract:**

- column1: required, unique
- column2: optional, range 0-100
- column3: required, valid email format

**Ready to create schema proposal?** Hand off to schema-validator.

## Example Profile

### Data Profile: customers.csv

**Shape:** 31 rows, 8 columns

**Columns:**

| Column | Type | Nulls | Null % | Unique | Sample Values |
|--------|------|-------|--------|--------|---------------|
| customer_id | str | 0 | 0% | 30 | C001, C002, C003 |
| email | str | 5 | 16% | 25 | john@..., jane@... |
| age | int | 0 | 0% | 28 | 34, 28, -5, 999 |
| signup_date | str | 0 | 0% | 31 | 2023-01-15, 03/15/2023 |

**Quality Issues Found:**

- [ ] **HIGH:** 1 duplicate customer_id (C001 appears twice)
- [ ] **MEDIUM:** 16% null emails — decide if required
- [ ] **HIGH:** Invalid ages (-5, 999, 150) — need range validation
- [ ] **MEDIUM:** Mixed date formats (ISO and MM/DD/YYYY)

**Recommendations for Schema Contract:**

- customer_id: required, unique, non-empty
- email: optional OR required with cleaning
- age: required, range 0-120
- signup_date: required, ISO 8601 format
