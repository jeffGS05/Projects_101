# ETL Data Pipeline

A reproducible, production-oriented data engineering pipeline that extracts data from CSV sources, validates and transforms the records, and loads the resulting datasets into PostgreSQL for analytical use.

## Project Status

**Status:** Core ETL pipeline implemented and validated

The current implementation processes:

- Customers
- Orders
- Order items

The pipeline includes extraction, validation, transformation, loading, automated testing, relational integrity checks, analytical SQL, Docker-based PostgreSQL infrastructure, and an automated execution script.

## Objectives

This project demonstrates practical data engineering capabilities using:

- Python
- PostgreSQL
- SQL
- Docker
- Bash
- pytest
- Git and GitHub

Key engineering goals:

1. Build a modular ETL pipeline
2. Validate source data before loading
3. Transform raw records into appropriate data types
4. Load data into a relational database
5. Maintain referential integrity
6. Support idempotent pipeline execution
7. Implement automated tests
8. Provide analytical SQL queries
9. Containerize local database infrastructure
10. Follow professional Git and documentation practices

## Architecture

```text
CSV Source Data
      |
      v
+-------------+
|   Extract   |
+-------------+
      |
      v
+-------------+
|  Validate   |
+-------------+
      |
      v
+-------------+
|  Transform  |
+-------------+
      |
      v
+-------------+
|    Load     |
+-------------+
      |
      v
+----------------------+
|     PostgreSQL       |
|                      |
|  customers           |
|  orders              |
|  order_items         |
+----------------------+
      |
      v
+-------------+
|  Analytics  |
+-------------+
