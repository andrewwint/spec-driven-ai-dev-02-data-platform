# Proposal 003: MCP Validation Tool

## Summary
Create a single MCP tool that exposes schema validation to AI assistants.

## Scope (ONE tool only)
- `validate_customer_schema` — validates a CSV against the customer schema contract

## Anti-patterns Avoided
- ❌ "While we're at it, let's add transformation too"
- ❌ "Might as well expose the full pipeline"
- ❌ "Would be easy to also add data profiling"

## Implementation
Single Python MCP server with one tool registration.

## Status
**Accepted** — Implemented in Module 7.
