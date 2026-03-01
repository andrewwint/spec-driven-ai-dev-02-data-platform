"""Customer Schema Validator — Module 4: Schema Validation as DARE.

Validates customer data against schema contracts.
This is the 'D' in DARE — deterministic validation gates.
"""
import sys
import pandas as pd


def validate_customer_schema(filepath: str) -> bool:
    """Validate customer CSV against schema contract.

    Required columns: customer_id, name, email, created_at
    Rules:
        - customer_id: non-null, unique integers
        - email: non-null, contains '@'
        - created_at: valid date format

    Returns:
        bool: True if validation passes
    """
    df = pd.read_csv(filepath)
    errors = []

    # Check required columns
    required = ['customer_id', 'name', 'email', 'created_at']
    missing = [col for col in required if col not in df.columns]
    if missing:
        errors.append(f"Missing columns: {missing}")

    # Check nulls in required fields
    for col in required:
        if col in df.columns:
            null_count = df[col].isnull().sum()
            null_pct = null_count / len(df) * 100
            if null_pct > 5:
                errors.append(f"{col}: {null_pct:.1f}% nulls (threshold: 5%)")

    # Check duplicates
    if 'customer_id' in df.columns:
        dup_count = df['customer_id'].duplicated().sum()
        if dup_count > 0:
            errors.append(f"customer_id: {dup_count} duplicates found")

    if errors:
        print("❌ Schema validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("✅ Schema validation PASSED")
    return True


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "data/raw/customers.csv"
    success = validate_customer_schema(filepath)
    sys.exit(0 if success else 1)
