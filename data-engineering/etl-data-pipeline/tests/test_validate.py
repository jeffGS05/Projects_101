import pytest

from src.validate import validate_customer, validate_customers


VALID_CUSTOMER = {
    "customer_id": "1",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "country": "Costa Rica",
    "created_at": "2026-01-15T10:30:00",
}


def test_validate_customer_accepts_valid_record():
    validate_customer(VALID_CUSTOMER)


def test_validate_customer_rejects_missing_field():
    record = VALID_CUSTOMER.copy()
    del record["email"]

    with pytest.raises(ValueError, match="Missing required field: email"):
        validate_customer(record)


def test_validate_customer_rejects_empty_field():
    record = VALID_CUSTOMER.copy()
    record["first_name"] = "   "

    with pytest.raises(ValueError, match="Field cannot be empty: first_name"):
        validate_customer(record)


def test_validate_customer_rejects_invalid_customer_id():
    record = VALID_CUSTOMER.copy()
    record["customer_id"] = "abc"

    with pytest.raises(ValueError, match="customer_id must be an integer"):
        validate_customer(record)


def test_validate_customer_rejects_invalid_email():
    record = VALID_CUSTOMER.copy()
    record["email"] = "invalid-email"

    with pytest.raises(ValueError, match="Invalid email format"):
        validate_customer(record)


def test_validate_customers_reports_row_number():
    records = [
        VALID_CUSTOMER,
        {
            **VALID_CUSTOMER,
            "customer_id": "abc",
        },
    ]

    with pytest.raises(
        ValueError,
        match="Invalid customer record at row 2: customer_id must be an integer",
    ):
        validate_customers(records)
