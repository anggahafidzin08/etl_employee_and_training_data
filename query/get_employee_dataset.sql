SELECT distinct [EmpID]
    , CONCAT([FirstName],' ',[LastName]) EmpName
    ,[StartDate]
    ,[ExitDate]
    ,[Title]
    ,[EmployeeStatus]
    ,[EmployeeType]
    ,[TerminationType]
    ,[DepartmentType]
    ,[Division]
    ,[JobFunctionDescription]
    ,[GenderCode]
    ,[Current Employee Rating]
FROM [AdventureWorksLT].[dbo].[employee_dataset] ed