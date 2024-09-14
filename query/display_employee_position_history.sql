with current_pos as (
	select
		distinct e.EmployeeID
		, e.FullName
		, e.BirthDate
		, e.Address
		, p.PosID
		, p.PosTitle
		, p.StartDate
		, p.EndDate
		, case when 
			ROW_NUMBER() over(partition by p.EmployeeID order by p.StartDate DESC) = 1 
			then 1 else 0 
		end as is_current_pos
	from AdventureWorksLT.dbo.employee e
	left join AdventureWorksLT.dbo.position p
		on p.EmployeeID = e.EmployeeID
)
select 
	distinct cp.EmployeeID
	, cp.FullName
	, cp.BirthDate
	, cp.Address
	, cp.PosID
	, cp.PosTitle
	, cp.StartDate
	, cp.EndDate
from current_pos cp
where cp.is_current_pos = 1
	and cp.PosID is not null