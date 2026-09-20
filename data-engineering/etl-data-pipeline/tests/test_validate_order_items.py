import pytest

from src.validate import validate_order_item, validate_order_items


def valid_order_item():
    return {
        "order_item_id": "1",
        "order_id": "1001",
        "product_name": "Laptop Stand",
        "quantity": "1",
        "unit_price": "75.50",
    }


def test_validate_order_item_valid():
    validate_order_item(valid_order_item())


def test_validate_order_item_invalid_item_id():
    record = valid_order_item()
    record["order_item_id"] = "abc"

    with pytest.raises(ValueError, match="order_item_id must be an integer"):
        validate_order_item(record)


def test_validate_order_item_invalid_order_id():
    record = valid_order_item()
    record["order_id"] = "abc"

    with pytest.raises(ValueError, match="order_id must be an integer"):
        validate_order_item(record)


def test_validate_order_item_invalid_quantity():
    record = valid_order_item()
    record["quantity"] = "abc"

    with pytest.raises(ValueError, match="quantity must be an integer"):
        validate_order_item(record)


def test_validate_order_item_zero_quantity():
    record = valid_order_item()
    record["quantity"] = "0"

    with pytest.raises(ValueError, match="quantity must be greater than zero"):
        validate_order_item(record)


def test_validate_order_item_negative_quantity():
    record = valid_order_item()
    record["quantity"] = "-1"

    with pytest.raises(ValueError, match="quantity must be greater than zero"):
        validate_order_item(record)


def test_validate_order_item_invalid_unit_price():
    record = valid_order_item()
    record["unit_price"] = "abc"

    with pytest.raises(ValueError, match="unit_price must be a valid decimal"):
        validate_order_item(record)


def test_validate_order_item_negative_unit_price():
    record = valid_order_item()
    record["unit_price"] = "-10.00"

    with pytest.raises(ValueError, match="unit_price cannot be negative"):
        validate_order_item(record)


def test_validate_order_items_reports_row_number():
    record = valid_order_item()
    record["quantity"] = "0"

    with pytest.raises(
        ValueError,
        match="Invalid order item record at row 1",
    ):
        validate_order_items([record])
