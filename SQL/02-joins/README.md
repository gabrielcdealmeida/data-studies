# SQL JOINs

Practice exercises on SQL JOINs, written in T-SQL and run on SQL Server (SSMS). Part of my study of Baraa's SQL course.

## Overview

This folder covers the JOIN types and when to use each one:

- `INNER JOIN`
- `LEFT JOIN` / `RIGHT JOIN`
- `FULL JOIN`
- `LEFT ANTI` / `RIGHT ANTI` / `FULL ANTI` joins (a `LEFT`, `RIGHT` or `FULL JOIN` followed by a `WHERE ... IS NULL` filter)
- Self join (joining a table with itself)
- Joining more than two tables

The quick rule I used to choose the join: **from which table do I need all the rows?** One table only → `LEFT` or `RIGHT`. Both → `FULL`. Neither → `INNER`.

## Dataset

Tables from the `sales` schema of the course database:

- `sales.Customers`: customers and their country/score
- `sales.Employees`: employees, department, salary and manager (`ManagerID`)
- `sales.Orders`: current orders
- `sales.OrdersArchive`: archived orders (some `OrderID`s repeat)
- `sales.Products`: products and categories

The database itself is not included in this repository. Source: [SQL course materials](https://academy.datawithbaraa.com/l/digital_download/930511/sql-course-materials)

## Exercises

All queries are in [`joins.sql`](joins.sql), each one with its statement as a comment above it.

1. Customers with their orders (only customers with orders): `INNER JOIN`
2. All customers with their orders: `LEFT JOIN`
3. Customers who never placed an order: `LEFT ANTI JOIN`
4. All products with the orders they appear in: `RIGHT JOIN`
5. Products that were never sold: `RIGHT ANTI JOIN`
6. Customer name, product name and sales of each order: `INNER JOIN` (3 tables)
7. Employees who never made a sale: `LEFT ANTI JOIN`
8. Each employee with their manager's name: `LEFT JOIN` (self join)
9. Compare `Orders` with `OrdersArchive`:
   - a) `OrderID`s in `Orders` but not in `OrdersArchive`: `LEFT ANTI JOIN`
   - b) `OrderID`s present in only one of the two tables: `FULL ANTI JOIN`
10. Customers with orders in `Orders` that never appear in `OrdersArchive`: `INNER JOIN` + `LEFT ANTI JOIN`

## Lessons learned

- `FULL JOIN` is not a safe default. It can return the right result by coincidence of the data, so choose the join by what the question asks.
- For anti joins, filter on a column from the other table that is never NULL when a match exists (for example its key).
- Joining two tables on a non-unique key (like `CustomerID`) multiplies rows. Use `DISTINCT` or join on a unique key.
- In a self join, the table on the left is the one you want listed in full. Use clear aliases for the columns (`EmployeeFirstName`, `ManagerFirstName`).
- A query that looks correct and a query that is correct can return the same output on a small dataset. Check the logic, not only the result.

## How to run

1. Restore the course database in SQL Server.
2. Open `joins.sql` in SSMS.
3. Run each query separately.