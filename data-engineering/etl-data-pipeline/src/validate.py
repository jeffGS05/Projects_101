from datetime import date
from decimal import Decimal, InvalidOperation
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


VALID_ORDER_STATUSES = {"pending", "completed", "cancelled"}


def validate_order(record: dict) -> None:
    """Validate a raw order record."""

    required_fields = [
        "order_id",
        "customer_id",
        "order_date",
        "status",
        "total_amount",
    ]

    for field in required_fields:
        if field not in record:
            raise ValueError(f"Missing required field: {field}")

        if not record[field].strip():
            raise ValueError(f"Field cannot be empty: {field}")

    try:
        int(record["order_id"])
    except ValueError as exc:
        raise ValueError("order_id must be an integer") from exc

    try:
        int(record["customer_id"])
    except ValueError as exc:
        raise ValueError("customer_id must be an integer") from exc

    try:
        date.fromisoformat(record["order_date"])
    except ValueError as exc:
        raise ValueError("order_date must be a valid ISO date") from exc

    status = record["status"].strip().lower()

    if status not in VALID_ORDER_STATUSES:
        raise ValueError(f"Invalid order status: {status}")

    try:
        total_amount = Decimal(record["total_amount"])
    except InvalidOperation as exc:
        raise ValueError("total_amount must be a valid decimal") from exc

    if total_amount < 0:
        raise ValueError("total_amount cannot be negative")


def validate_orders(records: list[dict]) -> None:
    """Validate all raw order records."""

    for index, record in enumerate(records, start=1):
        try:
            validate_order(record)
        except ValueError as exc:
            raise ValueError(
                f"Invalid order record at row {index}: {exc}"
            ) from exc


def validate_order_item(record: dict) -> None:
    """Validate a raw order item record."""

    required_fields = [
        "order_item_id",
        "order_id",
        "product_name",
        "quantity",
        "unit_price",
    ]

    for field in required_fields:
        if field not in record:
            raise ValueError(f"Missing required field: {field}")

        if not record[field].strip():
            raise ValueError(f"Field cannot be empty: {field}")

    try:
        int(record["order_item_id"])
    except ValueError as exc:
        raise ValueError("order_item_id must be an integer") from exc

    try:
        int(record["order_id"])
    except ValueError as exc:
        raise ValueError("order_id must be an integer") from exc

    try:
        quantity = int(record["quantity"])
    except ValueError as exc:
        raise ValueError("quantity must be an integer") from exc

    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")

    try:
        unit_price = Decimal(record["unit_price"])
    except InvalidOperation as exc:
        raise ValueError("unit_price must be a valid decimal") from exc

    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")


def validate_order_items(records: list[dict]) -> None:
    """Validate all raw order item records."""

    for index, record in enumerate(records, start=1):
        try:
            validate_order_item(record)
        except ValueError as exc:
            raise ValueError(
                f"Invalid order item record at row {index}: {exc}"
            ) from exc
