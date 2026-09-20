from decimal import Decimal

from src.transform import transform_order_items


def test_transform_order_items():
    records = [
        {
            "order_item_id": "1",
            "order_id": "1001",
            "product_name": "  Laptop Stand  ",
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

    transformed = transform_order_items(records)

    assert transformed[0]["order_item_id"] == 1
    assert transformed[0]["order_id"] == 1001
    assert transformed[0]["product_name"] == "Laptop Stand"
    assert transformed[0]["quantity"] == 1
    assert transformed[0]["unit_price"] == Decimal("75.50")


def test_transform_order_items_preserves_decimal_precision():
    records = [
        {
            "order_item_id": "3",
            "order_id": "1002",
            "product_name": "Wireless Mouse",
            "quantity": "1",
            "unit_price": "39.99",
        }
    ]

    transformed = transform_order_items(records)

    assert isinstance(transformed[0]["unit_price"], Decimal)
    assert transformed[0]["unit_price"] == Decimal("39.99")
