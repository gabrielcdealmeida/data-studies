# E-Commerce Inventory ETL & SQL Analysis with DuckDB

A lightweight data engineering pipeline that converts raw CSV inventory data into structured, typed JSON and performs analytical SQL queries directly on the semi-structured file using **Python** and **DuckDB**.

## Project Overview

This project demonstrates a classic Extract, Transform, and Load (ETL) workflow followed by serverless analytical querying:

1. **Extract & Generate:** Creates a mock e-commerce inventory dataset (`stock.csv`) containing product SKUs, categories, quantities, unit prices, and sales channels (marketplaces).
2. **Transform & Load:** Uses Python's built-in `csv` and `json` libraries to parse the CSV file, enforce proper data types (`int` for quantities, `float` for prices), and serialize the output into `stock.json`.
3. **Analyze:** Leverages **DuckDB** (`read_json_auto`) to run fast, in-memory SQL queries directly over the JSON file without needing a traditional relational database setup.

## Tech Stack

* **Python 3.x** (`csv`, `json`)
* **DuckDB** (In-process SQL OLAP database)
* **Google Colab**

## Data Schema

| Column | Type | Description |
| :--- | :--- | :--- |
| `sku` | `STRING` | Unique Stock Keeping Unit identifier |
| `product` | `STRING` | Product name |
| `category` | `STRING` | Product department/category |
| `quantity` | `INTEGER` | Available units in stock |
| `unit_price` | `FLOAT` | Retail price per unit |
| `marketplace` | `STRING` | E-commerce platform (Amazon, Mercado Livre, Shopee, Magalu) |

## Analytical Queries Included

The script answers five key business and inventory management questions:

* **Top 3 Most Expensive Products:** Identifies the highest-ticket items in the catalog.
* **Low Stock Alert:** Filters products with fewer than 5 units remaining (`quantity < 5`).
* **Category Inventory Ranking:** Lists all products under `Home & Kitchen` sorted by stock availability.
* **Marketplace Filtering:** Retrieves products listed on `Mercado Livre` priced above 50.00.
* **Stock Value by Category:** Calculates the total inventory valuation (`SUM(unit_price * quantity)`) grouped by category.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
