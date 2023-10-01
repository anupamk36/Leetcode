# Write your MySQL query statement below
select Department.name as "Department", e.name as "Employee", e.salary as "Salary" 
FROM (select *, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary desc) r from Employee) e 
JOIN Department on Department.id=e.departmentId
where r <= 3;

