# Proposal 002: Deployment Approach

## Summary
Choose a deployment strategy for the customer data pipeline based on ROI analysis.

## Options Evaluated

| Option | Complexity | Cost | Maintenance |
|--------|-----------|------|-------------|
| Manual scripts | Low | Free | High |
| Scheduled cron | Low | Free | Medium |
| AWS Lambda | Medium | ~$5/mo | Low |
| Airflow | High | ~$50/mo | Medium |
| Kubernetes | Very High | ~$200/mo | High |

## Decision
**Scheduled cron** — Start simple, graduate to Lambda when volume justifies it.

## Rationale
- Current data volume doesn't justify infrastructure complexity
- Cron provides automation without deployment overhead
- Easy to migrate to Lambda later (same Python code)

## Status
**Accepted** — Documented in Module 6.
