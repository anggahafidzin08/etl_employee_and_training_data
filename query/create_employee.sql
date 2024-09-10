drop table if exists AdventureWorksLT.dbo.employee;
create table employee(
	ID int primary key not null
	, EmployeeID varchar(10) unique not null
	, FullName varchar(100) not null
	, BirthDate date not null
	, Address varchar(500)
)