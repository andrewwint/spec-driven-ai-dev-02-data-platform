.PHONY: help validate-schema validate-quality validate transform pipeline lint test clean status agents-check

# Default target
help: ## Show this help
	@echo "Customer Data Pipeline - Make Targets"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Usage: make <target>"

# =============================================================================
# Data Validation Targets
# =============================================================================

validate-schema: ## Validate data against schema contracts
	@echo "🔍 Validating data schemas..."
	@if [ -f src/validators/customer_validator.py ]; then \
		python -m src.validators.customer_validator data/raw/customers.csv && \
		echo "✅ Customer schema: PASS"; \
	else \
		echo "⏭️  Customer validator not implemented yet"; \
	fi
	@if [ -f src/validators/transaction_validator.py ]; then \
		python -m src.validators.transaction_validator data/raw/transactions.csv && \
		echo "✅ Transaction schema: PASS"; \
	else \
		echo "⏭️  Transaction validator not implemented yet"; \
	fi
	@echo ""

validate-quality: ## Run data quality checks
	@echo "🔍 Running quality checks..."
	@echo "Checking for nulls in required fields..."
	@python -c "import pandas as pd; df=pd.read_csv('data/raw/customers.csv'); nulls=df.isnull().sum().sum(); print(f'  Total nulls: {nulls}')"
	@echo "Checking for duplicates..."
	@python -c "import pandas as pd; df=pd.read_csv('data/raw/customers.csv'); dups=df.duplicated().sum(); print(f'  Duplicate rows: {dups}')"
	@echo "✅ Quality checks complete"
	@echo ""

validate: validate-schema validate-quality ## Full validation suite

# =============================================================================
# Transformation Targets
# =============================================================================

transform: ## Run all transformations
	@echo "🔄 Running transformations..."
	@if [ -f src/transformers/customer_cleaner.py ]; then \
		python -m src.transformers.customer_cleaner && \
		echo "✅ Customer transformations: COMPLETE"; \
	else \
		echo "⏭️  Customer cleaner not implemented yet"; \
	fi
	@echo ""

pipeline: validate-schema transform ## Full pipeline (validate → transform)
	@echo "─────────────────────────────"
	@echo "🎉 Pipeline complete!"

# =============================================================================
# Development Targets
# =============================================================================

lint: ## Run Python linter (requires ruff)
	@command -v ruff >/dev/null 2>&1 && ruff check src/ || echo "⚠️  ruff not installed (pip install ruff)"

format: ## Format Python code (requires ruff)
	@command -v ruff >/dev/null 2>&1 && ruff format src/ || echo "⚠️  ruff not installed (pip install ruff)"

test: ## Run tests
	@if [ -d tests ] && [ "$$(ls -A tests/*.py 2>/dev/null)" ]; then \
		python -m pytest tests/ -v; \
	else \
		echo "⚠️  No tests found in tests/ directory"; \
	fi

# =============================================================================
# Documentation Targets
# =============================================================================

changelog-check: ## Show recent CHANGELOG entries
	@echo "📋 Recent CHANGELOG entries:"
	@echo "─────────────────────────────"
	@head -30 CHANGELOG.md
	@echo ""

agents-check: ## List available agents
	@echo "🤖 Available Copilot Agents:"
	@echo "─────────────────────────────"
	@if [ -d .github/agents ]; then \
		for f in .github/agents/*.agent.md; do \
			if [ -f "$$f" ]; then \
				name=$$(basename "$$f" .agent.md); \
				desc=$$(grep -m1 "^description:" "$$f" 2>/dev/null | sed 's/description: *//'); \
				printf "  %-20s %s\n" "$$name" "$$desc"; \
			fi \
		done \
	else \
		echo "  No agents found. Create them in .github/agents/"; \
	fi
	@echo ""

# =============================================================================
# Status Targets
# =============================================================================

status: ## Show project status
	@echo "📊 Project Status"
	@echo "═════════════════════════════"
	@echo ""
	@echo "📁 Data Files:"
	@echo "  Raw:      $$(ls -1 data/raw/*.csv 2>/dev/null | wc -l | tr -d ' ') files"
	@echo "  Cleaned:  $$(ls -1 data/cleaned/*.csv 2>/dev/null | wc -l | tr -d ' ') files"
	@echo "  Features: $$(ls -1 data/features/*.csv 2>/dev/null | wc -l | tr -d ' ') files"
	@echo ""
	@echo "🤖 Agents:"
	@ls -1 .github/agents/*.agent.md 2>/dev/null | wc -l | xargs printf "  %d agent(s) defined\n"
	@echo ""
	@echo "📝 Proposals:"
	@ls -1 docs/proposals/*.md 2>/dev/null | grep -v TEMPLATE | wc -l | xargs printf "  %d proposal(s)\n"
	@echo ""
	@echo "📋 Changelog versions:"
	@grep -c "^## \[" CHANGELOG.md 2>/dev/null || echo "  0"
	@echo ""

data-profile: ## Quick profile of raw data
	@echo "📊 Data Profile"
	@echo "═════════════════════════════"
	@for f in data/raw/*.csv; do \
		if [ -f "$$f" ]; then \
			name=$$(basename "$$f"); \
			rows=$$(wc -l < "$$f" | tr -d ' '); \
			cols=$$(head -1 "$$f" | tr ',' '\n' | wc -l | tr -d ' '); \
			printf "  %-20s %s rows, %s columns\n" "$$name" "$$rows" "$$cols"; \
		fi \
	done
	@echo ""

# =============================================================================
# Setup Targets
# =============================================================================

setup: ## Install development dependencies
	pip install -r requirements.txt
	pip install pre-commit ruff pytest
	pre-commit install
	@echo "✅ Development environment ready!"

clean: ## Remove generated files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf data/cleaned/*.csv data/features/*.csv 2>/dev/null || true
	@echo "🧹 Cleaned!"

# =============================================================================
# Combined Targets
# =============================================================================

all: status validate ## Full status and validation
	@echo "─────────────────────────────"
	@echo "✅ All checks complete!"

check: lint validate ## Quick check (lint + validate)
