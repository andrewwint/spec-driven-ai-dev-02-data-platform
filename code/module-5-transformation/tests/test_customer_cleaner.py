"""Tests for customer data cleaner."""
import tempfile
import os
import pandas as pd
import pytest


def test_removes_duplicates():
    """Test that duplicate customer_ids are removed."""
    from src.transformers.customer_cleaner import clean_customers

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("customer_id,name,email,created_at\n")
        f.write("1,Alice,alice@example.com,2024-01-01\n")
        f.write("1,Alice,alice@example.com,2024-01-01\n")
        f.write("2,Bob,bob@example.com,2024-01-02\n")
        input_path = f.name

    output_path = input_path + ".out"
    try:
        result = clean_customers(input_path, output_path)
        assert len(result) == 2
    finally:
        os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)
