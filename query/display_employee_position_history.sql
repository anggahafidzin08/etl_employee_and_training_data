select
	distinct e.EmployeeID
	, e.FullName
	, e.BirthDate
	, e.Address
	, p.PosID
	, p.PosTitle
	, p.StartDate
	, p.EndDate
from dbo.employee e
left join dbo.position p
	on e.EmployeeID = p.EmployeeID
order by e.EmployeeID, p.StartDate