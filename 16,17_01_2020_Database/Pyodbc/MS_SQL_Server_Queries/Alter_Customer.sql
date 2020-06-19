-- Adds column City in to table Customer.
ALTER TABLE Customer
ADD City varchar(50)

ALTER TABLE Products
ADD price float;

-- Remane column "price" to "Price" in Products table
EXEC sp_rename 'Products.price', 'Price', 'COLUMN';

-- Makes column "CustomerID" of table Orders as Foreign Key with reference to column "ID" in Customer table
ALTER TABLE Orders
add FOREIGN KEY	(CustomerID) references Customer(Id)

ALTER TABLE Orders
add FOREIGN KEY	(ProductId) references Products(Id)

