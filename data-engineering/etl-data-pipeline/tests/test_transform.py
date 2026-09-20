from datetime import datetime

from src.transform import transform_customers


def test_transform_customers():
    records = [
        {
            "customer_id": "1",
            "first_name": " John ",
            "last_name": " Smith ",
            "email": " JOHN.SMITH@EXAMPLE.COM ",
            "country": " USA ",
            "created_at": "2026-01-15 10:30:00",
        }
    ]

    result = transform_customers(records)

    assert result[0]["customer_id"] == 1
    assert result[0]["first_name"] == "John"
    assert result[0]["last_name"] == "Smith"
    assert result[0]["email"] == "john.smith@example.com"
    assert result[0]["country"] == "USA"
    assert result[0]["created_at"] == datetime(2026, 1, 15, 10, 30)


def test_transform_customers_multiple_records():
    records = [
        {
            "customer_id": "1",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
            "country": "USA",
            "created_at": "2026-01-15 10:30:00",
        },
        {
            "customer_id": "2",
            "first_name": "Maria",
            "last_name": "Garcia",
            "email": "MARIA@EXAMPLE.COM",
            "country": "Spain",
            "created_at": "2026-01-20 14:15:00",
        },
    ]

    result = transform_customers(records)

    assert len(result) == 2
    assert result[1]["email"] == "maria@example.com"
