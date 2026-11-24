-- 1. List the full name (FirstName, LastName) of each customer along with the OrderID
--    and Sales of the orders they placed in Orders. Only customers who have orders should appear.
SELECT 
	FirstName,
	LastName,
	OrderID,
	Sales
FROM sales.Customers
INNER JOIN sales.Orders
ON sales.Customers.CustomerID = sales.Orders.CustomerID

-- 2. List ALL customers and their orders in Orders (OrderID, Sales).
--    Customers without orders must also appear in the result.
SELECT 
	FirstName,
	LastName,
	OrderID,
	Sales
FROM sales.Customers
LEFT JOIN sales.Orders
ON sales.Customers.CustomerID = sales.orders.CustomerID

-- 3. Show only the customers who have NEVER placed an order in Orders.
SELECT
	FirstName,
	LastName,
	OrderID,
	Sales
FROM sales.Customers
LEFT JOIN sales.Orders
ON sales.customers.CustomerID = sales.orders.CustomerID
WHERE sales.orders.CustomerID IS NULL

-- 4. List ALL products and the OrderID of the orders in which they appear.
--    Write the query starting from Orders (left table) and Products (right table).
SELECT 
	OrderID,
	sales.Products.ProductID,
	sales.Products.Product,
	Sales
FROM sales.orders
RIGHT JOIN sales.Products
ON sales.orders.ProductID = sales.Products.ProductID

-- 5. Using the same logic as question 4, show only the products that have NEVER been sold.
SELECT 
	OrderID,
	sales.Products.ProductID,
	sales.Products.Product,
	Sales
FROM sales.orders
RIGHT JOIN sales.Products
ON sales.orders.ProductID = sales.Products.ProductID
WHERE sales.Orders.ProductID IS NULL

-- 6. List the customer name, the product name (Product), and the Sales value of each order in Orders.
SELECT 
	FirstName,
	LastName,
	Product,
	Sales
FROM sales.Customers
INNER JOIN sales.orders
	ON sales.customers.CustomerID = sales.Orders.CustomerID
INNER JOIN sales.Products
	ON sales.Orders.ProductID = sales.Products.ProductID

-- 7. List the employees who have NEVER made a sale (SalesPersonID in Orders).
SELECT 
	EmployeeID,
	FirstName,
	LastName
FROM sales.Employees
LEFT JOIN sales.Orders
ON sales.Employees.EmployeeID = sales.orders.SalesPersonID
WHERE sales.Orders.OrderID IS NULL

-- 8. List each employee along with their manager's name (ManagerID).
--    Employees without a manager must also appear, with the manager column empty.
SELECT
	tb2.EmployeeID,
	tb2.FirstName AS EmployeeFirstName,
	tb2.LastName AS EmployeeLastName,
	
	tb1.FirstName AS ManagerFirstName,
	tb1.LastName AS ManagerLastName
FROM sales.Employees AS tb2
LEFT JOIN sales.Employees AS tb1
ON tb2.ManagerID = tb1.EmployeeID


-- 9. Compare Orders with OrdersArchive using OrderID:
--    a) Which OrderIDs exist in Orders but not in OrdersArchive?
SELECT 
	sales.orders.OrderID
FROM sales.Orders
LEFT JOIN sales.OrdersArchive
ON sales.orders.OrderID = sales.OrdersArchive.OrderID
WHERE sales.OrdersArchive.OrderID IS NULL

--    b) Which OrderIDs exist in only one of the two tables (in one but not the other, in both directions)?
SELECT 
	sales.orders.OrderID
FROM sales.Orders
FULL JOIN sales.OrdersArchive
ON sales.orders.OrderID = sales.OrdersArchive.OrderID
WHERE sales.OrdersArchive.OrderID IS NULL or sales.orders.OrderID IS NULL

-- 10. List the customers who have orders in Orders but NEVER appear in OrdersArchive.
SELECT DISTINCT
	sales.customers.CustomerID,
	sales.customers.FirstName,
	sales.customers.LastName
FROM sales.Customers
INNER JOIN sales.orders
	ON sales.customers.CustomerID = sales.orders.CustomerID
LEFT JOIN sales.OrdersArchive
	ON sales.orders.CustomerID = sales.OrdersArchive.CustomerID
WHERE sales.OrdersArchive.CustomerID IS NULL
