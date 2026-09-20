from src.database import get_connection


def load_customers(records: list[dict]) -> int:
    """Load transformed customer records into PostgreSQL."""

    if not records:
        return 0

    query = """
        INSERT INTO customers (
            customer_id,
            first_name,
            last_name,
            email,
            country,
            created_at
        )
        VALUES (
            %(customer_id)s,
            %(first_name)s,
            %(last_name)s,
            %(email)s,
            %(country)s,
            %(created_at)s
        )
        ON CONFLICT (customer_id) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            email = EXCLUDED.email,
            country = EXCLUDED.country,
            created_at = EXCLUDED.created_at
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany(query, records)

        connection.commit()

    return len(records)


def load_orders(records: list[dict]) -> int:
    """Load transformed order records into PostgreSQL."""

    if not records:
        return 0

    query = """
        INSERT INTO orders (
            order_id,
            customer_id,
            order_date,
            status,
            total_amount
        )
        VALUES (
            %(order_id)s,
            %(customer_id)s,
            %(order_date)s,
            %(status)s,
            %(total_amount)s
        )
        ON CONFLICT (order_id) DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            order_date = EXCLUDED.order_date,
            status = EXCLUDED.status,
            total_amount = EXCLUDED.total_amount
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany(query, records)

        connection.commit()

    return len(records)


def load_order_items(records: list[dict]) -> int:
    """Load transformed order item records into PostgreSQL."""

    if not records:
        return 0

    query = """
        INSERT INTO order_items (
            order_item_id,
            order_id,
            product_name,
            quantity,
            unit_price
        )
        VALUES (
            %(order_item_id)s,
            %(order_id)s,
            %(product_name)s,
            %(quantity)s,
            %(unit_price)s
        )
        ON CONFLICT (order_item_id) DO UPDATE SET
            order_id = EXCLUDED.order_id,
            product_name = EXCLUDED.product_name,
            quantity = EXCLUDED.quantity,
            unit_price = EXCLUDED.unit_price
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany(query, records)

        connection.commit()

    return len(records)
