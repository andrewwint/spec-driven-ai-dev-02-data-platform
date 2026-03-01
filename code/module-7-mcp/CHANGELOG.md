# Changelog

## [0.3.0] - Data Transformation

### Added
- Customer cleaner (`src/transformers/customer_cleaner.py`)
- Cleaner tests (`tests/test_customer_cleaner.py`)
- `make transform` and `make pipeline` targets
- Pre-commit hooks for data validation

## [0.2.0] - Schema Validation

### Added
- Customer schema validator (`src/validators/customer_validator.py`)
- Validator tests (`tests/test_customer_validator.py`)
- Schema contract proposal (`docs/proposals/001-schema-contract.md`)
- `make validate-schema` target

## [0.1.0] - Project Setup

### Added
- Project scaffolding with data directories
- Sample data files (customers, transactions, sessions)
- Makefile with help, status, and data-profile targets
- Data advisor skill for domain learning
