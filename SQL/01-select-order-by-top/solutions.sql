-- 1. TOP 3 products with the most sales
SELECT TOP 3 *
FROM sales.Orders
ORDER BY Sales DESC

-- 2. TOP 5 oldest orders
SELECT TOP 5 *
FROM sales.Orders
ORDER BY OrderDate ASC

-- 3. TOP 4 orders with least sales
SELECT TOP 4 OrderID, OrderStatus, Sales
FROM sales.Orders
ORDER BY Sales ASC

-- 4. TOP 3 delivered orders with the most sales
SELECT TOP 3 *
FROM sales.Orders
WHERE OrderStatus = 'Delivered'
ORDER BY sales DESC

-- 5. TOP 2 most recent shipped orders
SELECT TOP 2 *
FROM sales.Orders
WHERE OrderStatus = 'Shipped'
ORDER BY OrderDate DESC

-- 6. TOP 3 orders with quantity > 1 and least sales
SELECT TOP 3 *
FROM sales.Orders
WHERE Quantity > 1
ORDER BY sales ASC

-- 7. TOP 6 ordered by asc CustomerID and, within each client, desc Sales.
SELECT TOP 6 *
FROM sales.Orders
ORDER BY CustomerID ASC, sales DESC

-- 8. TOP 5 orders ordered by OrderStatus and most recent OrderDate
SELECT TOP 5 *
FROM Sales.Orders
ORDER BY OrderStatus ASC, OrderDate DESC

-- 9. Orders with the most sales in each status
SELECT TOP 1 *
FROM sales.Orders
WHERE OrderStatus = 'Delivered'
ORDER BY SALES DESC
SELECT TOP 1 *
FROM sales.Orders
WHERE OrderStatus = 'Shipped'
ORDER BY SALES DESC

-- 10. 3 after TOP 3 orders with the most sales
SELECT *
FROM sales.Orders
ORDER BY sales DESC
OFFSET 3 ROWS FETCH NEXT 3 ROWS ONLY

-- 11. TOP 3 Orders with the most sales using TOP 3 WITH TIES
SELECT TOP 3 WITH TIES *
FROM sales.orders
ORDER BY Sales DESC

-- 12. SHIPADDRESS NULL investigation
SELECT *
FROM sales.orders
ORDER BY ShipAddress ASC
