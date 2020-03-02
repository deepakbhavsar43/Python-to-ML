Select * from Customer
select * from Orders;
select * from Products;


select FirstName, LastName
from Customer

select FirstName, LastName
from Customer
where FirstName = 'Raj'

select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName = 'Kahar'

/* "_" underscore means there has to be some character */
select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName like 'Varsadiy_'

/* "%" modulo means there hsa to be nay value character or number*/
select FirstName, LastName
from Customer
where FirstName = 'Raj'
and LastName like 'Varsadiy%'

update Customer
set Age = 24
where FirstName = 'ishani'
and		LastName = 'Patel'

UPDATE Customer
SET City = 'Surat'

UPDATE Customer
SET City = 'Navsari'
WHERE FirstName = 'Mehul'
and	LastName = 'Patel'
