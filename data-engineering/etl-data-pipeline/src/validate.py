import re


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_customer(record: dict) -> None:
    """Validate a raw customer record."""

    required_fields = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "country",
        "created_at",
    ]

    for field in required_fields:
        if field not in record:
            raise ValueError(f"Missing required field: {field}")

        if not record[field].strip():
            raise ValueError(f"Field cannot be empty: {field}")

    try:
        int(record["customer_id"])
    except ValueError as exc:
        raise ValueError("customer_id must be an integer") from exc

    if not EMAIL_PATTERN.match(record["email"].strip()):
        raise ValueError("Invalid email format")


def validate_customers(records: list[dict]) -> None:
    """Validate all raw customer records."""

    for index, record in enumerate(records, start=1):
        try:
            validate_customer(record)
        except ValueError as exc:
            raise ValueError(
                f"Invalid customer record at row {index}: {exc}"
            ) from exc
