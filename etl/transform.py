import pandas as pd

def transform_data(input_path, output_path):
    print("Reading data...")
    df = pd.read_csv(input_path)

    # Data Quality Checks
    print("Running data quality checks...")

    # Remove duplicates
    df = df.drop_duplicates(subset=["order_id"])

    # Handle nulls
    df = df.dropna(subset=["order_id", "customer_id", "amount"])

    # Convert data types
    df["amount"] = df["amount"].astype(float)

    # Validation
    assert len(df) > 0, "Data is empty after cleaning"

    print("Saving cleaned data...")
    df.to_csv(output_path, index=False)

    print("ETL completed successfully!")

    return df


if __name__ == "__main__":
    transform_data("data/raw/orders.csv", "data/processed/cleaned_orders.csv")
