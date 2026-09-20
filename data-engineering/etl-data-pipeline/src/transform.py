from datetime import date
from decimal import Decimal
from datetime import date, datetime


def transform_customers(records: list[dict]) -> list[dict]:
    """Clean and convert extracted customer records."""

    transformed = []

    for record in records:
        transformed.append(
            {
                "customer_id": int(record["customer_id"]),
                "first_name": record["first_name"].strip(),
                "last_name": record["last_name"].strip(),
                "email": record["email"].strip().lower(),
                "country": record["country"].strip(),
                "created_at": datetime.fromisoformat(record["created_at"]),
            }
        )

    return transformed



def transform_order_items(records: list[dict]) -> list[dict]:
    """Clean and convert extracted order item records."""

    transformed = []

    for record in records:
        transformed.append(
            {
                "order_item_id": int(record["order_item_id"]),
                "order_id": int(record["order_id"]),
                "product_name": record["product_name"].strip(),
                "quantity": int(record["quantity"]),
                "unit_price": Decimal(record["unit_price"]),
            }
        )

    return transformed

def transform_orders(records: list[dict]) -> list[dict]:
    """Clean and convert extracted order records."""

    transformed = []

    for record in records:
        transformed.append(
            {
                "order_id": int(record["order_id"]),
                "customer_id": int(record["customer_id"]),
                "order_date": date.fromisoformat(record["order_date"]),
                "status": record["status"].strip().lower(),
                "total_amount": Decimal(record["total_amount"]),
            }
        )

    return transformed
