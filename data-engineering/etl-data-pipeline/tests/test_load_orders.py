from datetime import date
from decimal import Decimal

from src.load import load_orders


def test_load_orders():
    records = [
        {
            "order_id": 9999,
            "customer_id": 1,
            "order_date": date(2026, 2, 10),
            "status": "completed",
            "total_amount": Decimal("50.00"),
        }
    ]

    loaded = load_orders(records)

    assert loaded == 1
