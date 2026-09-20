from src.extract import extract_customers, extract_orders
from src.load import load_customers, load_orders
from src.transform import transform_customers, transform_orders
from src.validate import validate_customers, validate_orders


INPUT_FILE = "data/raw/customers.csv"


def run_pipeline() -> None:
    """Execute the complete customer ETL pipeline."""

    print("Starting ETL pipeline...")

    print("Extracting customer data...")
    records = extract_customers(INPUT_FILE)
    print(f"Records extracted: {len(records)}")

    print("Validating customer data...")
    validate_customers(records)
    print(f"Records validated: {len(records)}")

    print("Validating customer data...")
    validate_customers(records)
    print(f"Records validated: {len(records)}")

    print("Transforming customer data...")
    records = transform_customers(records)
    print(f"Records transformed: {len(records)}")

    print("Loading customer data...")
    loaded = load_customers(records)
    print(f"Records loaded: {loaded}")

    print("Extracting order data...")
    orders = extract_orders("data/raw/orders.csv")
    print(f"Orders extracted: {len(orders)}")

    print("Validating order data...")
    validate_orders(orders)
    print(f"Orders validated: {len(orders)}")

    print("Transforming order data...")
    orders = transform_orders(orders)
    print(f"Orders transformed: {len(orders)}")

    print("Loading order data...")
    orders_loaded = load_orders(orders)
    print(f"Orders loaded: {orders_loaded}")

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
