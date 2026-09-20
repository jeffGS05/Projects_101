from src.extract import extract_customers


def test_extract_customers(tmp_path):
    csv_file = tmp_path / "customers.csv"

    csv_file.write_text(
        "customer_id,first_name,last_name,email,country,created_at\n"
        "1,John,Smith,john.smith@example.com,USA,2026-01-15 10:30:00\n"
        "2,Maria,Garcia,maria.garcia@example.com,Spain,2026-01-20 14:15:00\n",
        encoding="utf-8",
    )

    records = extract_customers(str(csv_file))

    assert len(records) == 2
    assert records[0]["customer_id"] == "1"
    assert records[0]["first_name"] == "John"
    assert records[1]["email"] == "maria.garcia@example.com"


def test_extract_customers_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"

    try:
        extract_customers(str(missing_file))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")
