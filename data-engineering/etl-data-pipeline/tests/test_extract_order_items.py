import csv

import pytest

from src.extract import extract_order_items


def test_extract_order_items(tmp_path):
    file_path = tmp_path / "order_items.csv"

    rows = [
        {
            "order_item_id": "1",
            "order_id": "1001",
            "product_name": "Laptop Stand",
            "quantity": "1",
            "unit_price": "75.50",
        },
        {
            "order_item_id": "2",
            "order_id": "1001",
            "product_name": "USB-C Cable",
            "quantity": "2",
            "unit_price": "25.00",
        },
    ]

    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    records = extract_order_items(str(file_path))

    assert len(records) == 2
    assert records[0]["order_item_id"] == "1"
    assert records[1]["quantity"] == "2"


def test_extract_order_items_missing_file():
    with pytest.raises(FileNotFoundError):
        extract_order_items("/tmp/nonexistent-order-items.csv")
