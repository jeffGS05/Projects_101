from datetime import date
from decimal import Decimal

from src.transform import transform_orders


def test_transform_orders():
    records = [
        {
            "order_id": "1001",
            "customer_id": "1",
            "order_date": "2026-01-20",
            "status": " COMPLETED ",
            "total_amount": "125.50",
        }
    ]

    transformed = transform_orders(records)

    assert transformed == [
        {
            "order_id": 1001,
            "customer_id": 1,
            "order_date": date(2026, 1, 20),
            "status": "completed",
            "total_amount": Decimal("125.50"),
        }
    ]


def test_transform_orders_converts_numeric_values():
    records = [
        {
            "order_id": "1002",
            "customer_id": "2",
            "order_date": "2026-01-21",
            "status": "pending",
            "total_amount": "89.99",
        }
    ]

    transformed = transform_orders(records)[0]

    assert isinstance(transformed["order_id"], int)
    assert isinstance(transformed["customer_id"], int)
    assert isinstance(transformed["order_date"], date)
    assert isinstance(transformed["total_amount"], Decimal)
