import pytest

from src.validate import validate_order, validate_orders


VALID_ORDER = {
    "order_id": "1001",
    "customer_id": "1",
    "order_date": "2026-01-20",
    "status": "completed",
    "total_amount": "125.50",
}


def test_validate_order_accepts_valid_record():
    validate_order(VALID_ORDER)


def test_validate_order_rejects_invalid_order_id():
    record = VALID_ORDER.copy()
    record["order_id"] = "abc"

    with pytest.raises(ValueError, match="order_id must be an integer"):
        validate_order(record)


def test_validate_order_rejects_invalid_customer_id():
    record = VALID_ORDER.copy()
    record["customer_id"] = "abc"

    with pytest.raises(ValueError, match="customer_id must be an integer"):
        validate_order(record)


def test_validate_order_rejects_invalid_date():
    record = VALID_ORDER.copy()
    record["order_date"] = "not-a-date"

    with pytest.raises(
        ValueError,
        match="order_date must be a valid ISO date",
    ):
        validate_order(record)


def test_validate_order_rejects_invalid_status():
    record = VALID_ORDER.copy()
    record["status"] = "shipped"

    with pytest.raises(
        ValueError,
        match="Invalid order status: shipped",
    ):
        validate_order(record)


def test_validate_order_rejects_invalid_amount():
    record = VALID_ORDER.copy()
    record["total_amount"] = "abc"

    with pytest.raises(
        ValueError,
        match="total_amount must be a valid decimal",
    ):
        validate_order(record)


def test_validate_order_rejects_negative_amount():
    record = VALID_ORDER.copy()
    record["total_amount"] = "-10.00"

    with pytest.raises(
        ValueError,
        match="total_amount cannot be negative",
    ):
        validate_order(record)


def test_validate_orders_reports_row_number():
    records = [
        VALID_ORDER,
        {
            **VALID_ORDER,
            "status": "unknown",
        },
    ]

    with pytest.raises(
        ValueError,
        match="Invalid order record at row 2: Invalid order status: unknown",
    ):
        validate_orders(records)
