#!/usr/bin/env bash

set -euo pipefail

echo "Starting ETL pipeline..."

python -m src.pipeline

echo "ETL pipeline finished successfully."
