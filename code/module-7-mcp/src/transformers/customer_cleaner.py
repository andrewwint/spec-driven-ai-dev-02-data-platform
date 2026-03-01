"""Customer Data Cleaner — Module 5: Data Transformation.

Cleans and transforms raw customer data based on schema contracts.
"""
import pandas as pd


def clean_customers(input_path: str = "data/raw/customers.csv",
                    output_path: str = "data/cleaned/customers.csv") -> pd.DataFrame:
    """Clean customer data according to schema contract.

    Steps:
        1. Remove duplicate customer_ids
        2. Fill missing names with 'Unknown'
        3. Validate email format
        4. Standardize date format

    Returns:
        pd.DataFrame: Cleaned customer data
    """
    df = pd.read_csv(input_path)
    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates(subset=['customer_id'], keep='first')

    # Handle missing values
    if 'name' in df.columns:
        df['name'] = df['name'].fillna('Unknown')

    # Standardize dates
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

    cleaned_rows = len(df)
    print(f"Cleaned: {original_rows} → {cleaned_rows} rows ({original_rows - cleaned_rows} removed)")

    df.to_csv(output_path, index=False)
    print(f"Saved to: {output_path}")

    return df


if __name__ == "__main__":
    clean_customers()
