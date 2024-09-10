drop table if exists AdventureWorksLT.dbo.position;
create table position(
	ID int primary key not null
	, PosID varchar(10) unique not null
	, PosTitle varchar(100) not null
	, EmployeeID varchar(10) not null
	, StartDate date not null
    , EndDate date not null
)