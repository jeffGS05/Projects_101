from src.extract import extract_customers
from src.load import load_customers
from src.transform import transform_customers


INPUT_FILE = "data/raw/customers.csv"


def run_pipeline() -> None:
    """Execute the complete customer ETL pipeline."""

    print("Starting ETL pipeline...")

    print("Extracting customer data...")
    records = extract_customers(INPUT_FILE)
    print(f"Records extracted: {len(records)}")

    print("Transforming customer data...")
    records = transform_customers(records)
    print(f"Records transformed: {len(records)}")

    print("Loading customer data...")
    loaded = load_customers(records)
    print(f"Records loaded: {loaded}")

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
