import csv
from pathlib import Path


def extract_customers(file_path: str) -> list[dict]:
    """Extract customer records from a CSV file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def extract_orders(file_path: str) -> list[dict]:
    """Extract order records from a CSV file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def extract_order_items(file_path: str) -> list[dict]:
    """Extract order item records from a CSV file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
