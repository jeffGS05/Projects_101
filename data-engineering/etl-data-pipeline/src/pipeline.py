from src.extract import extract_customers, extract_orders, extract_order_items
from src.load import load_customers, load_orders, load_order_items
from src.transform import transform_customers, transform_orders, transform_order_items
from src.validate import validate_customers, validate_orders, validate_order_items


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

    print("Extracting order item data...")
    order_items = extract_order_items("data/raw/order_items.csv")
    print(f"Order items extracted: {len(order_items)}")

    print("Validating order item data...")
    validate_order_items(order_items)
    print(f"Order items validated: {len(order_items)}")

    print("Transforming order item data...")
    order_items = transform_order_items(order_items)
    print(f"Order items transformed: {len(order_items)}")

    print("Loading order item data...")
    order_items_loaded = load_order_items(order_items)
    print(f"Order items loaded: {order_items_loaded}")

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
