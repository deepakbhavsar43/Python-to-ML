Select * from Customer
select * from Orders;
select * from Products;

select *from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id INNER JOIN Customer as c on o.CustomerID=c.Id;

-- Dispalys specific columns of table by joining them
select OrderID, OrderDate, FirstName, LastName, ProductName, Price
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id;

-- Returns the total amout spent by alll customers
select Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id;

-- Displays the total amount spent by each customer
select c.FirstName, c.LastName, Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.FirstName, c.LastName;

-- Displays the total amount spent by each customer on each product
select c.FirstName, c.LastName, p.ProductName, Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.FirstName, c.LastName, p.ProductName;

-- Displays the total amount spent by each customer on each product
select c.City, Sum(Price) as Total, AVG(p.Price) as Average
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.City;

