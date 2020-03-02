### SQL queries to create table:
- To create a table named **Cutomer**:
```sh
create table Customer
(
	Id int PRIMARY KEY IDENTITY(1, 1),
	FirstName varchar(50),
	LastName varchar(50),
	Age int,
	City VARCHAR(50)
)
```

- To create a table named Products:
```sh
CREATE TABLE Products
(
	Id int PRIMARY KEY IDENTITY(1, 1),
	ProductName varchar(50)
)
```

- To create a table named Orders:
```sh
CREATE TABLE Orders
(
	OrderId int PRIMARY KEY IDENTITY(1, 1),
	OrderDate Datetime,
	CustomerID int,
	ProductID int,
)
```

### SQL queries to insert into table:
- To insert value into table named Customer:
```sh
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Deepak', 'Bhavsar', 24, 'Surat')
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Mehul', 'Patel', 22, 'Navsari')
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Ishani', 'Patel', 25, 'Surat')
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Raj', 'Kahar', 23, 'Surat')
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Shivani', 'Bedre', 23, 'Surat')
insert into Customer
([FirstName], [LastName], [Age], [City]) values('Raj', 'Varsadiya', 23, 'Surat')
insert into Products
([ProductName], [Price]) values('Bat', '300');
insert into Products
([ProductName], [Price]) values('Ball', '60');
INSERT INTO Orders ([OrderDate], [CustomerID], [ProductID])
values (GetDate(), 6, 2);
```

### SQL queries to fetch data from table:
- To fetch all the data from table
```sh
Select * from Customer
select * from Orders;
select * from Products;
```

- To display only first name and last name from table customer:
```sh
select FirstName, LastName
from Customer
```

- To display first name and last name of all customer whose first name is raj:
```sh
select FirstName, LastName
from Customer
where FirstName = 'Raj'
```

- To display first name and last name of all customer whose first name is raj and last name is kahar:
```sh
select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName = 'Kahar'
```

- To display first name and last name of all customer whose first name is raj and last name is varsadiy_. Followed by any character:
```sh
/* "_" underscore means there has to be some character */
select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName like 'Varsadiy_'
```

- To display first name and last name of all customer whose first name is raj and last name is varsadiy_. Followed by any character or number:
```sh
/* "%" modulo means there hsa to be may value character or number*/
select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName like 'Varsadiy%'
```

### SQL queries to update data in a table:
- To update age of a customer in table Customer whose first name is ishani and last name is patel:
```sh
update Customer
set Age = 24
where FirstName = 'ishani'
and	 LastName = 'Patel'
```

- To update the city of all customer as Surat in Customer table:
```sh
UPDATE Customer
SET City = 'Surat'
```

- To update the city of customer to Navsari, whose first name is mehul and last name is patel:
```sh
UPDATE Customer
SET City = 'Navsari'
WHERE FirstName = 'Mehul'
and	LastName = 'Patel'
```


### SQL queries to alter table:

- To add column City in to table Customer:
```sh
ALTER TABLE Customer
ADD City varchar(50)
```

- To add column price in table Products:
```sh
ALTER TABLE Products
ADD price float;
```

- To remane the column name "price" to "Price" in Products table:
```sh
EXEC sp_rename 'Products.price', 'Price', 'COLUMN';
```

- To makes column "CustomerID" of table Orders as Foreign Key with reference to column "ID" in table Customer:
```sh
ALTER TABLE Orders
add FOREIGN KEY	(CustomerID) references Customer(Id)
```

- To makes column "ProductId" of table Orders as Foreign Key with reference to column "ID" in table Products:
```sh
ALTER TABLE Orders
add FOREIGN KEY	(ProductId) references Products(Id)
```

### SQL queries to delete table/record:

- To delete the data of table customer
```sh
Delete Customer
```

- To delete whole table
```sh
Drop Table Customer
```

- To delete data of those customer who are from navsari:
```sh
DELETE from Customer
WHERE City = 'Navsari'
```

### SQL queries to join two different table:
- To display all the colums of all table with their relationship:
```sh 
select *from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id INNER JOIN Customer as c on o.CustomerID=c.Id;
```

- To dispalys specific columns of table by joining them
```sh
select OrderID, OrderDate, FirstName, LastName, ProductName, Price
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id;
```

- To returns the total amout spent by alll customers
```sh
select Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id;
```

- To display the total amount spent by each customer
```sh
select c.FirstName, c.LastName, Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.FirstName, c.LastName;
```

- Displays the total amount spent by each customer on each product
```sh
select c.FirstName, c.LastName, p.ProductName, Sum(Price) as Total
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.FirstName, c.LastName, p.ProductName;
```

- Displays the total amount spent by each customer on each product
```sh
select c.City, Sum(Price) as Total, AVG(p.Price) as Average
from Orders as o
INNER JOIN Products as p on o.ProductID=p.Id
INNER JOIN Customer as c on o.CustomerID=c.Id
GROUP BY c.City;
```