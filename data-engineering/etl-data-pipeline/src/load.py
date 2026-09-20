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
