create table Customer
(
	FirstName varchar(50),
	LastName varchar(50),
	Age int
)

create table Customer
(
	Id int PRIMARY KEY IDENTITY(1, 1),
	FirstName varchar(50),
	LastName varchar(50),
	Age int,
	City VARCHAR(50)
)

CREATE TABLE Products
(
	Id int PRIMARY KEY IDENTITY(1, 1),
	ProductName varchar(50)
)


CREATE TABLE Orders
(
	OrderId int PRIMARY KEY IDENTITY(1, 1),
	OrderDate Datetime,
	CustomerID int,
	ProductID int,
)