# Deployment Proposal Template

Use this template when proposing how to productionize notebook code.

---

## Proposal: [Deployment Approach Name]

### Summary

One sentence describing what this proposal covers.

### Context

- **Current state:** Working transformation code in notebooks
- **Data size:** [e.g., 10MB daily, 1GB weekly]
- **Frequency:** [e.g., on new data arrival, daily batch, weekly]
- **Criticality:** [e.g., nice-to-have, important, business-critical]

### Options Evaluated

| Option | Pros | Cons |
|--------|------|------|
| **AWS Lambda** | Event-driven, serverless, scales automatically | 15-min timeout, AWS lock-in, cold starts |
| **Docker + cron** | Portable, no timeout, full control | Requires container expertise, needs hosting |
| **GitHub Actions** | Free tier, familiar CI/CD, easy setup | Not for production workloads, limited runtime |
| **Simple cron** | Dead simple, no dependencies | No monitoring, manual recovery |

### Decision

**Chosen approach:** [Option name]

**Rationale:** [Why this option fits YOUR context — not just "it's popular"]

### ROI Analysis

| Factor | This Approach | Alternative |
|--------|---------------|-------------|
| Implementation time | [e.g., 2 hours] | [e.g., 8 hours] |
| Operational cost | [e.g., ~$0/month] | [e.g., $20/month] |
| Team expertise required | [e.g., Basic Python] | [e.g., Docker + K8s] |
| Scalability | [e.g., Limited] | [e.g., Unlimited] |
| Reliability | [e.g., Good enough] | [e.g., Enterprise-grade] |
| Portability | [e.g., AWS-locked] | [e.g., Any cloud] |

### "Don't Over-Engineer" Check

Before proceeding, answer honestly:

- [ ] Is this the simplest solution that meets our actual needs?
- [ ] Are we building for current requirements or imagined future ones?
- [ ] Could we start simpler and upgrade later if needed?
- [ ] What's the cost of being wrong about this choice?

### DARE Application

| Letter | This Deployment |
|--------|-----------------|
| **D** | [What's deterministic? e.g., Schema validation runs first] |
| **A** | [What needs AI? e.g., Transformation logic] |
| **R** | [What gets reviewed? e.g., Output data quality check] |
| **E** | [What triggers alerts? e.g., >5% validation failures] |

### Implementation Tasks

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

### Success Criteria

- [ ] Pipeline runs automatically on [trigger]
- [ ] Output appears in [location]
- [ ] Failures alert via [mechanism]

### Approval

- [ ] Reviewed by: [name]
- [ ] Approved on: YYYY-MM-DD

---

## Key Principle

> This proposal documents a DECISION with rationale — not just "we're using Lambda" but WHY we chose that approach for our specific context.
