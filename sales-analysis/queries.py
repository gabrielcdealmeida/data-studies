import sqlite3

def run_query(title, sql):
    connection = sqlite3.connect('sales.db')
    rows = connection.execute(sql).fetchall()
    connection.close()
    print(f'\n{title}')
    for row in rows:
        print(row)

run_query('How many rows?', '''
    SELECT COUNT(*)
    FROM sales
''')

run_query('Products priced as 1500 or more', '''
    SELECT DISTINCT product, unit_price
    FROM sales
    WHERE unit_price > 1500
''')

run_query('Total revenue', '''
    SELECT SUM(quantity * unit_price) AS total_revenue
    FROM sales
''')

run_query('Revenue by category', '''
    SELECT category, SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
''')

run_query('How many air-fryers were sold?', '''
    SELECT product_id, product, SUM(quantity) AS total_sales
    FROM sales
    WHERE product = 'air-fryer'
''')

run_query('What is the percentage of the air-fryer sales revenue over the total revenue?', '''
    SELECT ROUND (100.0 * (SELECT SUM(quantity * unit_price) FROM sales WHERE product = 'air-fryer') / SUM(quantity * unit_price), 2) AS partial_revenue
    FROM sales
''')