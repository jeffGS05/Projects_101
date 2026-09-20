from decimal import Decimal

from src.load import load_order_items


def test_load_order_items():
    records = [
        {
            "order_item_id": 9999,
            "order_id": 1001,
            "product_name": "Test Product",
            "quantity": 2,
            "unit_price": Decimal("19.99"),
        }
    ]

    loaded = load_order_items(records)

    assert loaded == 1

    from src.database import get_connection

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    order_item_id,
                    order_id,
                    product_name,
                    quantity,
                    unit_price
                FROM order_items
                WHERE order_item_id = 9999
                """
            )

            row = cursor.fetchone()

            assert row == (
                9999,
                1001,
                "Test Product",
                2,
                Decimal("19.99"),
            )

            cursor.execute(
                "DELETE FROM order_items WHERE order_item_id = 9999"
            )

        connection.commit()
