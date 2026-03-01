# Customer Data Pipeline

> Course 2: Data Platform — Skills for Unfamiliar Domains

A data transformation pipeline that teaches how to use AI skills when navigating unfamiliar domains.

## Quick Start

```bash
./setup.sh
make help
```

## Project Structure

```
customer-data-pipeline/
├── README.md
├── Makefile
├── requirements.txt
├── data/
│   ├── raw/          # Source data (don't modify)
│   ├── cleaned/      # Validated & cleaned data
│   └── features/     # ML-ready features
├── notebooks/        # Exploration notebooks
├── src/
│   ├── validators/   # Schema validation code
│   └── transformers/ # Data cleaning code
└── docs/
    └── proposals/    # Change proposals
```
