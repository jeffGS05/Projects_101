import csv

import pytest

from src.extract import extract_orders


def test_extract_orders(tmp_path):
    file_path = tmp_path / "orders.csv"

    rows = [
        {
            "order_id": "1001",
            "customer_id": "1",
            "order_date": "2026-01-20",
            "status": "completed",
            "total_amount": "125.50",
        },
        {
            "order_id": "1002",
            "customer_id": "2",
            "order_date": "2026-01-21",
            "status": "pending",
            "total_amount": "89.99",
        },
    ]

    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    records = extract_orders(str(file_path))

    assert len(records) == 2
    assert records[0]["order_id"] == "1001"
    assert records[1]["status"] == "pending"


def test_extract_orders_missing_file():
    with pytest.raises(FileNotFoundError):
        extract_orders("/tmp/nonexistent-orders.csv")
