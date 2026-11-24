# Dirty Orders: Net Revenue Report

## Overview
A Python + DuckDB project that cleans a dirty marketplace order export (`orders.csv`) and calculates the **net revenue and number of orders per marketplace**. Invalid rows are not calculated: they are saved to a separate file with the reason.

## Scenario
I build reports for a store that sells on several marketplaces. The finance team needs the net revenue per marketplace, but the order export arrived dirty and had to be cleaned and validated before any calculation.

## Input
`orders.csv` with the columns: `order_id`, `order_date`, `customer`, `marketplace`, `product`, `quantity`, `unit_price`, `status`.

Known issues in the data:
- Dates in three different formats
- Inconsistent marketplace names (extra spaces, mixed casing)
- Prices in Brazilian format (`R$ 1.299,90`), plain decimals, or missing
- Invalid or missing quantities
- Duplicated orders
- Inconsistent status spelling (`canceled` / `cancelled`, mixed casing)

## Business Rules
- Only **delivered** orders count toward revenue.
- Duplicated orders (same `order_id`) are counted once.
- Dates containing `/` are in **day/month/year** format.
- Rows with an invalid or missing `quantity` or `unit_price` cannot be calculated: they go to a rejected list, with the reason.
- Marketplace names are standardized (trimmed, consistent casing).

## Deliverables
1. A function `get_revenue_report(path)` that returns a dictionary:
   `{"Mercado Livre": {"orders": ..., "revenue": ...}, ...}`
2. The same dictionary saved as `revenue_report.json`.
3. A `rejected_orders.csv` with the discarded rows and an extra `reason` column.

## Tools
- **Python** (`csv`, `json`, `datetime`): reading, cleaning and type conversions.
- **pandas**: turns the cleaned rows into a DataFrame.
- **DuckDB**: SQL aggregation (`COUNT`, `SUM`, `GROUP BY`) over the cleaned data.

## What Was Done
1. Read `orders.csv` row by row with `csv.DictReader`.
2. Converted `quantity` to integer and `unit_price` to float, handling the Brazilian price format (`R$`, thousands separator, decimal comma).
3. Standardized dates from three formats into `YYYY-MM-DD` with a helper function.
4. Cleaned text fields (`marketplace`, `status`, `customer`): trimmed spaces and fixed casing; unified `canceled` and `cancelled`.
5. Sent rows with invalid quantity or unit price to a rejected list, with the reason.
6. Loaded the valid rows into a DataFrame and used DuckDB to calculate the number of orders and the revenue (`quantity * unit_price`) per marketplace, excluding cancelled orders.
7. Built the report dictionary and saved `revenue_report.json` and `rejected_orders.csv`.

## How to Run
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python analysis.py
```
The script reads `orders.csv` and generates `revenue_report.json` and `rejected_orders.csv` in the same folder.

## Output
```json
{
    "Marketup": {
        "orders": 1,
        "revenue": 578.0
    },
    "Mercado Livre": {
        "orders": 3,
        "revenue": 1551.5
    },
    "Shopee": {
        "orders": 3,
        "revenue": 756.3
    }
}
```

## What I Learned
- Cleaning dirty data with `try/except` and type conversions.
- Parsing multiple date formats with `strptime`.
- Querying cleaned data with DuckDB.
- Organizing a script into a reusable function.
- Isolating dependencies with a virtual environment.
