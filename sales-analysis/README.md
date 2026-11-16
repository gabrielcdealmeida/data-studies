# Sales analysis with Excel, Python and SQLite

## What it does
It uses an existing excel file, loads it into a SQLite database and answers business questions with SQL.

## How to run:
1. Install the libraries: pip install pandas openpyxl (Using your terminal)
2. Run 'python excel_to_db.py' to create 'sales.db'
3. Run 'queries.py' to see the results

## Insights: 
It was possible to verify products that cost more than 1500 and might need different payment options.
It was possible to verify the total revenue and also the revenue by category, which shows that the categories 'others' and 'livingroom' lead the top 2.
It was possible to check the performance from a specific product (air-fryer) over the total sales records (How many and the percentage over the total revenue).

## What I learned
How to create a database from a regular excel file with pandas and sqlite and extract insights from it.