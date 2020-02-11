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
