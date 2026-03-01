# Teaching Scenarios for Data Advisor

These scenarios represent common data platform challenges. Use them to practice the Advisor teaching pattern.

## Scenario 1: Product Catalog Ingestion

**Context:** An e-commerce company receives product data from multiple vendors in different formats (XML, JSON, CSV). The application team wants clean, standardized data.

**Starter Prompt:**
```
We receive product data from 50 vendors in different formats.
Some send XML, some send JSON, some send CSV. Prices are formatted
differently ("$19.99" vs "19.99 USD" vs just "19.99").

What should I consider when designing a pipeline to standardize this data?
What are the common pitfalls?
```

**Teaching Approach:**
1. Explain why standardization matters (consistency for downstream systems)
2. Identify common pitfalls (vendor format changes, missing vendors, stale data)
3. Suggest validation strategy (deterministic format checks, alerts for new formats)
4. Suggest when to hand off (ready to explore the actual data)

**Follow-up Questions to Expect:**
- "How do I handle vendors who change their format without telling us?"
- "Should I store the original data or just the cleaned version?"
- "What validation rules would catch the most common issues?"

---

## Scenario 2: Fraud Detection Training Data

**Context:** A payment company needs clean, accurately-labeled transaction data to train a fraud detection model. Raw logs have labeling issues — some "fraud" was actually legitimate, some "success" was fraud discovered later.

**Starter Prompt:**
```
We want to train a fraud detection model, but our transaction labels
aren't reliable. Sometimes we mark a transaction as fraud, then the
customer proves it was legitimate. Sometimes we mark it as success,
then discover it was fraud weeks later.

How should we think about building a training dataset when
the labels themselves have quality issues?
```

**Teaching Approach:**
1. Explain why label quality matters for ML
2. Discuss trade-offs (exclude uncertain labels vs. include with confidence scores)
3. Suggest validation strategy (label age, dispute rates, reconciliation)
4. Identify handoff point (when ready to explore the actual data)

**Follow-up Questions to Expect:**
- "How long should we wait before considering a label 'final'?"
- "What's the impact of mislabeled data on model accuracy?"
- "Should we exclude uncertain cases or include them with lower confidence?"

---

## Scenario 3: Financial Reporting

**Context:** An e-commerce company needs accurate sales reports. Raw transaction data has issues: returns after month close, human data entry errors, AI agent mistakes, duplicate records from system failures.

**Starter Prompt:**
```
Our CFO wants accurate monthly sales reports, but our raw transaction
data has issues:
- Returns sometimes happen after the reporting period closes
- Product managers occasionally enter wrong prices (typos)
- We had duplicate transactions from a system failure last month
- Some customer records have invalid data (age = -5, age = 999)

How should we approach cleaning this data for accurate reporting?
What validation rules would you recommend?
```

**Teaching Approach:**
1. Explain why each issue matters for reporting accuracy
2. Discuss trade-offs for each problem (e.g., returns: include or exclude?)
3. Suggest deterministic validation rules
4. Identify when to hand off to explorer

**Follow-up Questions to Expect:**
- "How do we handle returns that cross reporting period boundaries?"
- "What's the difference between cleaning data for reporting vs. for ML?"
- "Should we fix bad data or exclude it? What are the trade-offs?"

---

## Scenario 4: Real-Time Event Stream Quality

**Context:** A startup streams user events (clicks, purchases, views) to an analytics database. Events sometimes arrive out of order, with duplicates or delays.

**Starter Prompt:**
```
We're building an analytics platform from user events. Events stream
in real-time but sometimes:
- Arrive out of order (click before view, but recorded after)
- Duplicate (same event recorded twice by mistake)
- Arrive very late (hours delay due to network issues)

How should we think about data quality and validation in a
streaming context? What's different from batch processing?
```

**Teaching Approach:**
1. Explain unique challenges of streaming (state management, windowing, late data)
2. Discuss trade-offs (drop late events vs. hold window open)
3. Suggest validation approach (ordering checks, deduplication, time windows)
4. Identify when to explore actual event patterns

**Follow-up Questions to Expect:**
- "How do we define 'out of order' in real-time data?"
- "Should we replay late events or discard them?"
- "How long should we wait for events before closing a window?"

---

## How to Use These Scenarios

### For Teaching (Advisor):
1. Start with the starter prompt
2. Explain WHY each issue matters
3. Discuss trade-offs
4. Suggest validation strategy
5. Ask: "Does that make sense? Can you explain back what I said?"
6. Confirm understanding before handing off

### For Learning (Developer):
1. Read the starter prompt
2. Ask follow-up questions
3. Try to explain back what you learned
4. Document key decisions
5. When ready: ask for explorer or transformer handoff

## Common Teaching Mistakes to Avoid

| Mistake | Impact | Fix |
|---------|--------|-----|
| Jumping to code without WHY | Developer doesn't understand tradeoffs | Start with concept explanation |
| Overwhelming with options | Developer feels confused | Suggest 1-2 approaches first |
| Not checking understanding | Developer leaves without learning | Ask them to explain back |
| Not identifying pitfalls | Developer encounters predictable problems | Teach from actual scenarios |
| Premature handoff | Developer implements incorrectly | Verify understanding first |

## Key Teaching Principles

1. **Start with WHY** — Help them understand motivation, not just mechanics
2. **Use analogies** — Connect to familiar programming concepts
3. **Identify pitfalls** — Help them avoid predictable mistakes
4. **Check understanding** — Ask them to explain back
5. **Suggest validation** — Help them know what to check
6. **Recommend handoff** — Tell them when to move to explorer/transformer

Follow these principles and your teaching will be effective and memorable.
