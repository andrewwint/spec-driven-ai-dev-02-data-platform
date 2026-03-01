# Proposal 001: Customer Schema Contract

## Summary
Define a schema contract for `data/raw/customers.csv` to establish deterministic validation gates.

## Schema Definition

| Column | Type | Required | Constraints |
|--------|------|----------|-------------|
| customer_id | integer | yes | unique, non-null |
| name | string | yes | non-null |
| email | string | yes | non-null, contains '@' |
| created_at | date | yes | valid ISO date |

## Escalation Thresholds

| Check | Threshold | Action |
|-------|-----------|--------|
| Null percentage | > 5% | Alert + block |
| Duplicate IDs | > 0 | Block pipeline |
| Invalid emails | > 10% | Alert |

## Status
**Accepted** — Implemented in Module 4.
