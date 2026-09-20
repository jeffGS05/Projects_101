# ETL Data Pipeline Architecture

## Overview

This project implements a production-style ETL pipeline using Python and PostgreSQL.

The pipeline extracts customer, order, and order-item data from CSV files, validates the source data, transforms it into typed Python structures, and loads it into a relational PostgreSQL database.

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
