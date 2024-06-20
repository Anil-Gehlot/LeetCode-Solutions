select unique_id, name from Employees as e left join EmployeeUNI as en on e.id = en.id;

-- select unique_id, name from Employees as e left join EmployeeUNI using (id);