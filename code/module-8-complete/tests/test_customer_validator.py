"""Tests for customer schema validator."""
import tempfile
import os
import pytest


def test_valid_customer_file():
    """Test that a valid customer file passes validation."""
    from src.validators.customer_validator import validate_customer_schema

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("customer_id,name,email,created_at\n")
        f.write("1,Alice,alice@example.com,2024-01-01\n")
        f.write("2,Bob,bob@example.com,2024-01-02\n")
        path = f.name

    try:
        assert validate_customer_schema(path) is True
    finally:
        os.unlink(path)


def test_missing_columns():
    """Test that missing required columns fail validation."""
    from src.validators.customer_validator import validate_customer_schema

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("id,name\n")
        f.write("1,Alice\n")
        path = f.name

    try:
        assert validate_customer_schema(path) is False
    finally:
        os.unlink(path)
