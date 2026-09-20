from datetime import datetime


def transform_customers(records: list[dict]) -> list[dict]:
    """Clean and convert extracted customer records."""

    transformed = []

    for record in records:
        transformed.append(
            {
                "customer_id": int(record["customer_id"]),
                "first_name": record["first_name"].strip(),
                "last_name": record["last_name"].strip(),
                "email": record["email"].strip().lower(),
                "country": record["country"].strip(),
                "created_at": datetime.fromisoformat(record["created_at"]),
            }
        )

    return transformed
